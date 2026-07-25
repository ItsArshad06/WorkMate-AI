import { Routes } from '@angular/router';

import { Home } from './pages/home/home';
import { Login } from './pages/login/login';
import { Dashboard } from './pages/dashboard/dashboard';
import { Employees } from './pages/employees/employees';
import { AttendancePage } from './pages/attendance/attendance';
import { Leave } from './pages/leave/leave';
import { Profile } from './pages/profile/profile';
import { AnalyticsPage } from './pages/analytics/analytics';

export const routes: Routes = [

  {
    path: '',
    component: Home,
  },

  {
    path: 'login',
    component: Login,
  },

  {
    path: 'dashboard',
    component: Dashboard,
  },

  {
    path: 'employees',
    component: Employees,
  },

  {
    path: 'attendance',
    component: AttendancePage,
  },

  {
    path: 'leave',
    component: Leave,
  },

  {
    path: 'profile',
    component: Profile,
  },

  {
    path: 'analytics',
    component: AnalyticsPage,
  },

  {
    path: '**',
    redirectTo: '',
  }

];