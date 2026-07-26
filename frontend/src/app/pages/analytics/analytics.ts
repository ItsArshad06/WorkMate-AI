import {
  Component,
  OnInit,
  AfterViewInit
} from '@angular/core';

import { CommonModule } from '@angular/common';

import {
  AnalyticsService,
  Analytics
} from '../../services/analytics.service';

import {
  Chart,
  registerables
} from 'chart.js';

Chart.register(...registerables);

@Component({
  selector: 'app-analytics',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './analytics.html',
  styleUrl: './analytics.css'
})
export class AnalyticsPage
  implements OnInit, AfterViewInit {

  analytics!: Analytics;

  chartsLoaded = false;

  constructor(
    private analyticsService: AnalyticsService
  ) {}

  ngOnInit(): void {

    this.analyticsService
      .getAnalytics()
      .subscribe({

        next: (data) => {

          this.analytics = data;

          console.log("Analytics:", data);

          setTimeout(() => {

            this.createCharts();

          }, 100);

        },

        error: err => console.error(err)

      });

  }

  ngAfterViewInit(): void {}

  createCharts(): void {

    if (this.chartsLoaded) return;

    this.chartsLoaded = true;

    /* ==========================
       Employee Growth
    ========================== */

    new Chart("growthChart",{

      type:"line",

      data:{

        labels:Object.keys(
          this.analytics.employee_growth
        ),

        datasets:[{

          label:"Employees",

          data:Object.values(
            this.analytics.employee_growth
          ),

          borderWidth:3,

          tension:.35,

          fill:true

        }]

      },

      options:{

        responsive:true,

        plugins:{
          legend:{
            display:false
          }
        }

      }

    });

    /* ==========================
       Department Distribution
    ========================== */

    new Chart("departmentChart",{

      type:"doughnut",

      data:{

        labels:Object.keys(
          this.analytics.department_distribution
        ),

        datasets:[{

          data:Object.values(
            this.analytics.department_distribution
          )

        }]

      },

      options:{

        responsive:true

      }

    });

    /* ==========================
       Attendance Summary
    ========================== */

    new Chart("attendanceChart",{

      type:"pie",

      data:{

        labels:[
          "Present",
          "Absent"
        ],

        datasets:[{

          data:[

            this.analytics.attendance_summary.present_percentage,

            this.analytics.attendance_summary.absent_percentage

          ]

        }]

      },

      options:{

        responsive:true

      }

    });

    /* ==========================
       Leave Summary
    ========================== */

    new Chart("leaveChart",{

      type:"bar",

      data:{

        labels:[
          "Approved",
          "Pending",
          "Rejected"
        ],

        datasets:[{

          label:"Requests",

          data:[

            this.analytics.leave_summary.approved,

            this.analytics.leave_summary.pending,

            this.analytics.leave_summary.rejected

          ]

        }]

      },

      options:{

        responsive:true,

        plugins:{
          legend:{
            display:false
          }
        }

      }

    });

  }

}