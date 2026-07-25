import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface LeaveRequest {
  id: number;
  employee: string;
  type: string;
  start_date: string;
  end_date: string;
  reason: string;
  status: string;
}

@Injectable({
  providedIn: 'root'
})
export class LeaveService {

  private apiUrl = 'http://127.0.0.1:8000/leaves';

  constructor(private http: HttpClient) {}

  getLeaves(): Observable<LeaveRequest[]> {
    return this.http.get<LeaveRequest[]>(`${this.apiUrl}/`);
  }

  getLeave(id: number): Observable<LeaveRequest> {
    return this.http.get<LeaveRequest>(`${this.apiUrl}/${id}`);
  }

  addLeave(leave: LeaveRequest): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, leave);
  }

  updateLeave(id: number, leave: LeaveRequest): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, leave);
  }

  deleteLeave(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
  }

}