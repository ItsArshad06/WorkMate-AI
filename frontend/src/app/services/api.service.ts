import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://127.0.0.1:8000';


  constructor(private http: HttpClient) { }


  getDashboard() {
    return this.http.get(
      `${this.apiUrl}/dashboard`
    );
  }


  getEmployees() {
    return this.http.get(
      `${this.apiUrl}/employees`
    );
  }


  getAttendance() {
    return this.http.get(
      `${this.apiUrl}/attendance`
    );
  }


  getLeaves() {
    return this.http.get(
      `${this.apiUrl}/leaves`
    );
  }


  getAnalytics() {
    return this.http.get(
      `${this.apiUrl}/analytics`
    );
  }

}