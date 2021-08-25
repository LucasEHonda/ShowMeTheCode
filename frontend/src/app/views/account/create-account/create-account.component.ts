import { Component, OnInit } from '@angular/core';
import { AccountService } from '../shared/account.service';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})
export class CreateAccountComponent implements OnInit {
  account = {
    email: '',
    password: ''
  };

  constructor(private accountService: AccountService) { }

  ngOnInit() {
  }

  async onSubmit() {
    try {
      const result = await this.accountService.createAccount(this.account);
    } catch(error){
      console.error(error);
    }

  }
}