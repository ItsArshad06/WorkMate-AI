import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import {
  AttendanceService,
  Attendance
} from '../../services/attendance.service';

@Component({
  selector: 'app-attendance',
  standalone: true,
  imports: [CommonModule, FormsModule],
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
    check_in: '',
    check_out: ''
  };

  constructor(
    private attendanceService: AttendanceService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadAttendance();
  }

  loadAttendance(): void {

    this.attendanceService.getAttendance().subscribe({

      next: (data) => {

        // Force Angular to receive a new array reference
        this.attendance = [...data];

        this.cdr.detectChanges();

      },

      error: (err) => console.error(err)

    });

  }

  get presentCount(): number {
    return this.attendance.filter(a => a.status === 'Present').length;
  }

  get absentCount(): number {
    return this.attendance.filter(a => a.status === 'Absent').length;
  }

  addRecord(): void {

    if (this.isEditing) {

      this.attendanceService.updateRecord(
        this.newRecord.id,
        this.newRecord
      ).subscribe({

        next: () => {

          alert("Attendance updated successfully");

          this.resetForm();

          this.loadAttendance();

        },

        error: err => console.error(err)

      });

      return;

    }

    this.attendanceService.addRecord(this.newRecord).subscribe({

      next: () => {

        alert("Attendance added successfully");

        this.resetForm();

        this.loadAttendance();

      },

      error: err => console.error(err)

    });

  }

  editRecord(record: Attendance): void {

    this.newRecord = { ...record };

    this.isEditing = true;

  }

  deleteRecord(id: number): void {

    if (!confirm("Delete this attendance record?")) {
      return;
    }

    this.attendanceService.deleteRecord(id).subscribe({

      next: () => {

        alert("Attendance deleted successfully");

        // Remove immediately from UI
        this.attendance = this.attendance.filter(r => r.id !== id);

        // Refresh from backend
        this.loadAttendance();

      },

      error: err => console.error(err)

    });

  }

  resetForm(): void {

    this.newRecord = {
      id: 0,
      employee: '',
      date: '',
      status: 'Present',
      check_in: '',
      check_out: ''
    };

    this.isEditing = false;

  }

}