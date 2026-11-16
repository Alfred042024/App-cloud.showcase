import { JsonPipe } from '@angular/common';
import { AfterContentInit, Component, inject, OnInit, signal } from '@angular/core';
import { ApiService } from '../../Service/apiService/api-service';
import { lastValueFrom } from 'rxjs';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { urls } from '../../types/getapi.interface';

@Component({
  imports: [JsonPipe, ReactiveFormsModule],
  selector: 'app-api-calling',
  styleUrl: './api-calling.scss',
  templateUrl: './api-calling.html',
})
export class ApiCalling  {
  callapiSrv = inject(ApiService);

  resultapi = signal([] as urls[]);

  addNewForm = new FormGroup({
    original: new FormControl(''),
    short: new FormControl(''),
  });

  ngAfterContentInit(): void {
    this.getall();
  }

  getall() {
    this.callapiSrv.getAll().subscribe((res:urls[]) => {
      this.resultapi.update(()=>{return res});
    });
  }

  detailsUrl(id: number) {
    console.info(['il mio id preferito cliccato', id]);
  }

  async addNewUrl() {
    const values = this.addNewForm.getRawValue();

    await lastValueFrom(this.callapiSrv.addNewUrl(values.short || '', values.original || ''));
    this.getall()
  }
}
