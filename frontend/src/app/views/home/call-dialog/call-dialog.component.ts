import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';
import { CallService } from 'src/app/shared/service/call.service';

@Component({
  selector: 'app-call-dialog',
  templateUrl: './call-dialog.component.html',
  styleUrls: ['./call-dialog.component.css']
})
export class CallDialogComponent implements OnInit {
  public callForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    private rest: CallService,
    public dialogRef: MatDialogRef<CallDialogComponent>
  ) { }

  ngOnInit(): void {
    this.callForm = this.fb.group({
      origin: ['011', [Validators.required]],
      destiny: ['016', [Validators.required]],
      plan: ['', [Validators.required]],
      minutes: [0, [Validators.required]],
      talk_more_tariff: 0,
      default_tariff:0,
      user: 1
    });
  }

  
  createCall(){
    this.rest.postCall(this.callForm.value).subscribe(result => {})
    this.dialogRef.close();
    this.callForm.reset();
    window.location.reload();
  }

  cancel(): void {
    this.dialogRef.close();
    this.callForm.reset();
  }

}
