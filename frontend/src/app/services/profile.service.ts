import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Profile {

  employee_id: string;

  full_name: string;

  email: string;

  phone: string;

  department: string;

  role: string;

  joining_date: string;

  status: string;

  attendance: string;

  leave_balance: number;

  performance: string;

  avatar: string;

}

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  private apiUrl = 'http://127.0.0.1:8000/profile';

  constructor(private http: HttpClient) {}

  getProfile(): Observable<Profile> {
    return this.http.get<Profile>(this.apiUrl);
  }

  updateProfile(profile: Profile): Observable<any> {
    return this.http.put(this.apiUrl, profile);
  }

}