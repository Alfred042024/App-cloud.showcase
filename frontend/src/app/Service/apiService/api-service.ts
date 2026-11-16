import { HttpClient, HttpErrorResponse, httpResource } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { catchError, map, Observable, throwError } from 'rxjs';
import { rawRes, urls, urlsDTO } from '../../types/getapi.interface';
import { UrlMapper } from '../../mapper/urlmapper/urlMapper.class';

@Service()
export class ApiService {
  http = inject(HttpClient);

  URL_ARCHIVE = {
    getallurls: '/api/getInitialApi',
    geturlsbyid: '/api/getInitialApi/',
    addUrl: '/api/addNewUrl',
  };

  getAll(): Observable<urls[]> {
    return this.http.get<urlsDTO[]>(this.URL_ARCHIVE.getallurls).pipe(
      map((urls: urlsDTO[]): urls[] => {
        return urls.map((singleUrl: urlsDTO): urls => {
          return UrlMapper.dtoToUrl(singleUrl);
        });
      }),
         catchError((err:HttpErrorResponse, cat) => {
        alert(err.error.detail[0]);
        return throwError(()=> new Error(err.error.detail[1]));
      }),
    );
  }

  getByID(id: number): Observable<urls> {
    return this.http.get<urlsDTO>(this.URL_ARCHIVE.geturlsbyid + String(id)).pipe(
      map((url: urlsDTO): urls => {
        return UrlMapper.dtoToUrl(url);
      }),
        catchError((err:HttpErrorResponse, cat) => {
        alert(err.error.detail[0]);
        return throwError(()=> new Error(err.error.detail[1]));
      }),
    );
  }

  addNewUrl(shortUrl: string, originalUrl: string) {
    return this.http.post<rawRes>(this.URL_ARCHIVE.addUrl, {
      short_url: shortUrl,
      original_url: originalUrl,
    }).pipe(
      catchError((err:HttpErrorResponse, cat) => {
        alert(err.error.detail[0]);
        return throwError(()=> new Error(err.error.detail[1]));
      }),
    );

  }
}
