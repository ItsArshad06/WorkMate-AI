import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

interface AttendanceRecord {
  date: string;
  checkIn: string;
  checkOut: string;
  workingHours: string;
  status: string;
}

@Component({
  selector: 'app-attendance',
  imports: [CommonModule],
  templateUrl: './attendance.html',
  styleUrl: './attendance.css',
})
export class Attendance {

  checkedIn = false;
  checkedOut = false;

  todayCheckIn = '--';
  todayCheckOut = '--';
  todayWorkingHours = '--';

  private checkInDate: Date | null = null;

  attendanceRecords: AttendanceRecord[] = [

    {
      date: '19 Jul 2026',
      checkIn: '09:05 AM',
      checkOut: '05:58 PM',
      workingHours: '08h 53m',
      status: 'Present'
    },

    {
      date: '18 Jul 2026',
      checkIn: '--',
      checkOut: '--',
      workingHours: '--',
      status: 'Leave'
    }

  ];
get presentCount(): number {

  return this.attendanceRecords.filter(

    record => record.status === 'Present'

  ).length;

}

get leaveCount(): number {

  return this.attendanceRecords.filter(

    record => record.status === 'Leave'

  ).length;

}

get workingCount(): number {

  return this.attendanceRecords.filter(

    record => record.status === 'Working'

  ).length;

}

get attendanceRate(): number {

  if (this.attendanceRecords.length === 0) {

    return 0;

  }

  return Math.round(

    (this.presentCount / this.attendanceRecords.length) * 100

  );

}
  checkIn() {

    if (this.checkedIn) {

      alert('Already checked in.');

      return;

    }

    this.checkedIn = true;
    this.checkedOut = false;

    this.checkInDate = new Date();

    this.todayCheckIn = this.checkInDate.toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit'
    });

    const today = this.checkInDate.toLocaleDateString('en-GB', {
      day: '2-digit',
      month: 'short',
      year: 'numeric'
    });

    this.todayCheckOut = '--';
    this.todayWorkingHours = '--';

    this.attendanceRecords.unshift({

      date: today,

      checkIn: this.todayCheckIn,

      checkOut: '--',

      workingHours: '--',

      status: 'Working'

    });

  }

  checkOut() {

    if (!this.checkedIn) {

      alert('Please check in first.');

      return;

    }

    if (this.checkedOut) {

      alert('Already checked out.');

      return;

    }

    if (!this.checkInDate) {

      return;

    }

    this.checkedOut = true;

    const checkOutDate = new Date();

    this.todayCheckOut = checkOutDate.toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit'
    });

    const difference = checkOutDate.getTime() - this.checkInDate.getTime();

    const hours = Math.floor(difference / (1000 * 60 * 60));

    const minutes = Math.floor(
      (difference % (1000 * 60 * 60)) / (1000 * 60)
    );

    this.todayWorkingHours =
      hours.toString().padStart(2, '0') +
      'h ' +
      minutes.toString().padStart(2, '0') +
      'm';

    this.attendanceRecords[0].checkOut = this.todayCheckOut;
    this.attendanceRecords[0].workingHours = this.todayWorkingHours;
    this.attendanceRecords[0].status = 'Present';

  }

}