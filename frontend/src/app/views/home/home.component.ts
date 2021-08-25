import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { CallDialogComponent } from './call-dialog/call-dialog.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(
    public dialog: MatDialog
  ) { }

  ngOnInit(): void {
  }
  addCall(): void {
    const dialogRef = this.dialog.open(CallDialogComponent, {
      minWidth: '400px',
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

  quit(): void {
    window.localStorage.clear();
    window.location.reload();
  }

}
