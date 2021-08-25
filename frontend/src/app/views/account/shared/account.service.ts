import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor(private http: HttpClient) { }

  async login(user: any){
    
    const result = await this.http.post<any>('http://127.0.0.1:8000/token/', user).toPromise();
    
    if (result && result.token){
      window.localStorage.setItem('token', result.token);
      return true;
    }
    return false;
  }

  async createAccount(account: any){
    return await this.http.post<any>("http://127.0.0.1:8000/create/", {
      email: account.email,
      username: account.email,
      password: account.password
    }).toPromise();
  }
}
