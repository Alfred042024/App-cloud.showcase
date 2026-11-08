import { Routes } from '@angular/router';
import { App } from './app';
import { ApiCalling } from './components/api-calling/api-calling';

export const routes: Routes = [
  {path: "apicalling", component: ApiCalling},
  {path:"**", redirectTo: "apicalling"}
];
