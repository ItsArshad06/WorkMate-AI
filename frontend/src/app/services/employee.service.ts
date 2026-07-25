import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Employee {
  full_name: string;
  employee_id: string;
  email: string;
  phone: string;
  department: string;
  role: string;
  joining_date: string;
  status: string;
}

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  private apiUrl = 'http://127.0.0.1:8000/employees';

  constructor(private http: HttpClient) {}

  getEmployees(): Observable<Employee[]> {
    return this.http.get<Employee[]>(`${this.apiUrl}/`);
  }

  getEmployee(employeeId: string): Observable<Employee> {
    return this.http.get<Employee>(`${this.apiUrl}/${employeeId}`);
  }

  addEmployee(employee: Employee): Observable<any> {
    return this.http.post(`${this.apiUrl}/`, employee);
  }

  updateEmployee(employeeId: string, employee: Employee): Observable<any> {
    return this.http.put(`${this.apiUrl}/${employeeId}`, employee);
  }

  deleteEmployee(employeeId: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${employeeId}`);
  }

}