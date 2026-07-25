import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Attendance {

  id: number;

  employee: string;

  date: string;

  status: string;

  check_in: string | null;

  check_out: string | null;

}

@Injectable({
  providedIn: 'root'
})

export class AttendanceService {

  private apiUrl = 'http://127.0.0.1:8000/attendance';

  constructor(private http: HttpClient) {}

  getAttendance(): Observable<Attendance[]> {
    return this.http.get<Attendance[]>(`${this.apiUrl}/`);
  }

  getRecord(id: number): Observable<Attendance> {
    return this.http.get<Attendance>(`${this.apiUrl}/${id}`);
  }

  addRecord(record: Attendance): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, record);
  }

  updateRecord(id: number, record: Attendance): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, record);
  }

  deleteRecord(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }

}