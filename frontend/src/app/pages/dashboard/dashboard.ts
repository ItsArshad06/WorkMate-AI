import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { ApiService } from '../../services/api.service';
import {
  EmployeeService,
  Employee
} from '../../services/employee.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule
  ],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class Dashboard implements OnInit {

  dashboardData: any = {};

  employees: Employee[] = [];

  constructor(
    private api: ApiService,
    private employeeService: EmployeeService
  ) {}

  ngOnInit(): void {

    this.loadDashboard();

    this.loadEmployees();

  }

  loadDashboard(): void {

    this.api.getDashboard().subscribe({

      next: (data) => {

        this.dashboardData = data;

        console.log("Dashboard API:", data);

      },

      error: (err) => console.error(err)

    });

  }

  loadEmployees(): void {

    this.employeeService.getEmployees().subscribe({

      next: (data) => {

        this.employees = data.slice(0, 3);

        console.log("Recent Employees:", this.employees);

      },

      error: (err) => console.error(err)

    });

  }

}