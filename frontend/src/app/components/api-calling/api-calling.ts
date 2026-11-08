import { JsonPipe } from '@angular/common';
import { Component ,inject,signal } from '@angular/core';
import { ApiService } from '../../Service/apiService/api-service';

@Component({
  imports: [ JsonPipe],
  selector: 'app-api-calling',
  styleUrl: './api-calling.scss',
  templateUrl: './api-calling.html',
})
export class ApiCalling {

  callapiSrv = inject(ApiService)

  resultapi = signal([] as getapiStandard[])

  callApi(){+
    this.callapiSrv.getApiPython().subscribe((res) =>{
      this.resultapi.set(res)
    })
  }

}
