import { Component, OnInit } from '@angular/core';
import { Call } from 'src/app/shared/model/call.model';
import { CallService } from 'src/app/shared/service/call.service';

@Component({
  selector: 'app-call-list',
  templateUrl: './call-list.component.html',
  styleUrls: ['./call-list.component.css']
})
export class CallListComponent implements OnInit {

  calls!: Call[];
  formatter = new Intl.NumberFormat('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  });


  constructor(
    public callService: CallService
  ) { }

  ngOnInit(): void {
    this.getCalls();
  }


  getCalls(){
    this.callService.getCalls().subscribe(data =>{
      this.calls = data;
      console.log(this.calls)
    })
  }

}
