import { Routes } from '@angular/router';

import { Home } from './pages/home/home';
import { Login } from './pages/login/login';
import { Dashboard } from './pages/dashboard/dashboard';
import { Employees } from './pages/employees/employees';
import { AttendancePage } from './pages/attendance/attendance';
import { Leave } from './pages/leave/leave';
import { Profile } from './pages/profile/profile';
import { AnalyticsPage } from './pages/analytics/analytics';
import { Resume } from './pages/resume/resume';
import { Interview } from './pages/interview/interview';
import { authGuard } from './guards/auth-guard';


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
    canActivate: [authGuard]
  },


  {
    path: 'employees',
    component: Employees,
    canActivate: [authGuard]
  },


  {
    path: 'attendance',
    component: AttendancePage,
    canActivate: [authGuard]
  },


  {
    path: 'leave',
    component: Leave,
    canActivate: [authGuard]
  },


  {
    path: 'analytics',
    component: AnalyticsPage,
    canActivate: [authGuard]
  },


  {
    path: 'profile',
    component: Profile,
    canActivate: [authGuard]
  },


  {
    path: 'resume',
    component: Resume,
    canActivate: [authGuard]
  },
  
  {
  path: 'interview',
  component: Interview,
  canActivate: [authGuard]
  },
  {
    path: '**',
    redirectTo: ''
  }

];
