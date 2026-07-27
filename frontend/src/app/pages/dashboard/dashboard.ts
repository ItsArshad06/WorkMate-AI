import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule } from '@angular/router';

import { ApiService } from '../../services/api.service';
import { EmployeeService, Employee } from '../../services/employee.service';
import { AuthService } from '../../services/auth.service';

import { Chatbot } from '../../components/chatbot/chatbot';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    Chatbot
  ],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class Dashboard implements OnInit {

  dashboardData: any = {};
  employees: Employee[] = [];
  user: any = {};

  constructor(
    private api: ApiService,
    private employeeService: EmployeeService,
    private authService: AuthService,
    private router: Router,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {

    this.user = this.authService.getUser();

    this.api.getDashboard().subscribe(data => {
      this.dashboardData = data;
      this.cdr.detectChanges();
    });

    this.employeeService.getEmployees().subscribe(data => {
      this.employees = data.slice(0, 3);
      this.cdr.detectChanges();
    });

  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }

}