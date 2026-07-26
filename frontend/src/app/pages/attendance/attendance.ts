import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import {
  AttendanceService,
  Attendance
} from '../../services/attendance.service';


@Component({
  selector: 'app-attendance',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './attendance.html',
  styleUrl: './attendance.css'
})
export class AttendancePage implements OnInit {


  attendance: Attendance[] = [];


  isEditing = false;


  newRecord: Attendance = {

    id: 0,
    employee: '',
    date: '',
    status: 'Present',
    check_in: null,
    check_out: null

  };


  constructor(
    private attendanceService: AttendanceService
  ) {}



  ngOnInit(): void {

    this.loadAttendance();

  }



  loadAttendance(): void {


    console.log("📡 Loading attendance...");


    this.attendanceService.getAttendance()
      .subscribe({

        next: (data) => {


          console.log(
            "🔥 Attendance API DATA:",
            data
          );


          this.attendance = data;


          console.log(
            "✅ Attendance Array:",
            this.attendance
          );


        },


        error: (err) => {


          console.error(
            "❌ Attendance API Error:",
            err
          );


        }


      });


  }



  get presentCount(): number {

    return this.attendance.filter(
      a => a.status === 'Present'
    ).length;

  }



  get absentCount(): number {

    return this.attendance.filter(
      a => a.status === 'Absent'
    ).length;

  }



  addRecord(): void {


    if(this.isEditing){


      this.attendanceService.updateRecord(
        this.newRecord.id,
        this.newRecord
      )
      .subscribe({

        next:()=>{

          alert(
            "Attendance updated successfully"
          );

          this.resetForm();

          this.loadAttendance();

        },


        error:(err)=>{

          console.error(err);

        }


      });


      return;

    }



    this.attendanceService.addRecord(
      this.newRecord
    )
    .subscribe({

      next:()=>{


        alert(
          "Attendance added successfully"
        );


        this.resetForm();

        this.loadAttendance();


      },


      error:(err)=>{

        console.error(err);

      }


    });


  }




  editRecord(record: Attendance): void {


    this.newRecord = {
      ...record
    };


    this.isEditing = true;


  }





  deleteRecord(id:number):void{


    if(!confirm("Delete this attendance record?")){

      return;

    }


    this.attendanceService.deleteRecord(id)
    .subscribe({

      next:()=>{


        alert(
          "Attendance deleted successfully"
        );


        this.loadAttendance();


      },


      error:(err)=>{

        console.error(err);

      }


    });


  }




  resetForm():void{


    this.newRecord = {

      id:0,
      employee:'',
      date:'',
      status:'Present',
      check_in:null,
      check_out:null

    };


    this.isEditing = false;


  }


}