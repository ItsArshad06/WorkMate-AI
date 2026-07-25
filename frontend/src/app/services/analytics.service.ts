import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Analytics {

  summary: {
    total_employees: number;
    active_employees: number;
    leave_employees: number;
    attendance_rate: string;
  };

  employee_growth: {
    [key: string]: number;
  };

  attendance_summary: {
    present_percentage: number;
    absent_percentage: number;
  };

  leave_summary: {
    approved: number;
    pending: number;
    rejected: number;
  };

  department_distribution: {
    [key: string]: number;
  };

  ai_insights: string[];

}

@Injectable({
  providedIn: 'root'
})
export class AnalyticsService {

  private apiUrl = 'http://127.0.0.1:8000/analytics';

  constructor(private http: HttpClient) {}

  getAnalytics(): Observable<Analytics> {
    return this.http.get<Analytics>(this.apiUrl);
  }

}