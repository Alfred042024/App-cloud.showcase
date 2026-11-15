import { JsonPipe } from '@angular/common';
import { Component, inject, OnInit, signal } from '@angular/core';
import { ApiService } from '../../Service/apiService/api-service';
import { lastValueFrom } from 'rxjs';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  imports: [JsonPipe, ReactiveFormsModule],
  selector: 'app-api-calling',
  styleUrl: './api-calling.scss',
  templateUrl: './api-calling.html',
})
export class ApiCalling  implements OnInit{
  callapiSrv = inject(ApiService);

  resultapi = signal([] as urls[]);
  addNewForm = new FormGroup(
    {
      original : new FormControl(""),
      short: new FormGroup("")
    }
  )

ngOnInit(): void {
  this.getall()
}

  getall() {
    this.callapiSrv.getAll().subscribe((res) => {
      this.resultapi.set(res);
    });
  }

  detailsUrl(id:number){
    console.info(["il mio id preferito cliccato", id])
  }

  async addNewUrl(){

    const  values = this.addNewForm.getRawValue();

    await lastValueFrom( this.callapiSrv.addNewUrl(values.short || "",values.original || ""))
  }
}
