import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  imports: [],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  message = '';

  constructor(private http: HttpClient) {}

  login(employeeId: string) {
    console.log('Login clicked:', employeeId);

    this.http.post('http://127.0.0.1:8000/login', {
      employee_id: employeeId,
    }).subscribe({
      next: (response: any) => {
        console.log(response);
        this.message = `Welcome ${response.employee.full_name}`;
      },
      error: (error) => {
        console.log(error);
        this.message = error.error.detail;
      },
    });
  }
}