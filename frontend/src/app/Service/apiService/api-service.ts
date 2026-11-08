import {  HttpClient, httpResource } from '@angular/common/http';
import { inject, Service } from '@angular/core';


@Service()
export class ApiService {

   http = inject(HttpClient)

  URL_ARCHIVE= {
    "getApiPython" : "/api/getInitialApi"
  }

  getApiPython(){
    return this.http.get<getapiStandard[]>(this.URL_ARCHIVE.getApiPython)
  }

}
