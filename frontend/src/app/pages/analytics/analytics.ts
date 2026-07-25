import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

import {
  AnalyticsService,
  Analytics
} from '../../services/analytics.service';

@Component({
  selector: 'app-analytics',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './analytics.html',
  styleUrl: './analytics.css'
})
export class AnalyticsPage implements OnInit {

  analytics!: Analytics;

  constructor(
    private analyticsService: AnalyticsService
  ) {}

  ngOnInit(): void {

    this.analyticsService
      .getAnalytics()
      .subscribe({

        next: (data) => {

          this.analytics = data;

          console.log(data);

        },

        error: err => console.error(err)

      });

  }

}