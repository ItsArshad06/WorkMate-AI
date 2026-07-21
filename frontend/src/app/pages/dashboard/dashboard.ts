import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';


@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class Dashboard implements OnInit {

  dashboardData: any = {};


  constructor(
    private api: ApiService
  ) {}


  ngOnInit(): void {

    console.log("Dashboard component loaded");


    this.api.getDashboard()
      .subscribe({

        next: (data) => {

          this.dashboardData = data;

          console.log(
            "Dashboard API Data:",
            data
          );

        },

        error: (error) => {

          console.error(
            "Dashboard API Error:",
            error
          );

        }

      });

  }

}