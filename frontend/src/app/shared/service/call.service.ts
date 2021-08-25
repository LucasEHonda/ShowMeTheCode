import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Call } from '../model/call.model';

@Injectable({
  providedIn: 'root'
})
export class CallService {
  apiUrl = 'http://127.0.0.1:8000/calls/';
  httpOptions = {
    headers: new HttpHeaders({
      'content-type': 'application/json',
      'Authorization': `Token ${window.localStorage.getItem('token')}`
    })
  };
  constructor(
    private httpCliente: HttpClient
  ) { }

  public getCalls(): Observable<Call[]> {
    return this.httpCliente.get<Call[]>(this.apiUrl, {headers: new HttpHeaders({'Authorization': `Token ${window.localStorage.getItem('token')}`})});
  }

  public postCall(call: any): Observable<Call>{
    return this.httpCliente.post<any>(this.apiUrl, call, this.httpOptions)
  }

}
