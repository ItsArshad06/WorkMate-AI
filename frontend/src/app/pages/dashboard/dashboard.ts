import { Component, OnInit } from '@angular/core';
import { RouterModule, Router } from '@angular/router';

import { ApiService } from '../../services/api.service';
import {
  EmployeeService,
  Employee
} from '../../services/employee.service';

import { AuthService } from '../../services/auth.service';


@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [RouterModule],
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

    private router: Router

  ) {}



  ngOnInit(): void {


    this.loadDashboard();

    this.loadEmployees();


    this.user = this.authService.getUser();


    console.log(
      "Logged User:",
      this.user
    );

  }



  loadDashboard(): void {


    this.api.getDashboard()
      .subscribe({

        next: (data) => {

          this.dashboardData = data;

          console.log(
            "Dashboard API:",
            data
          );

        },


        error: (err) =>
          console.error(err)

      });


  }



  loadEmployees(): void {


    this.employeeService.getEmployees()
      .subscribe({

        next: (data) => {

          this.employees = data.slice(0,3);


        },


        error: (err) =>
          console.error(err)

      });


  }



  logout(): void {


    this.authService.logout();


    this.router.navigate([
      '/login'
    ]);


  }


}