import { Routes } from '@angular/router';

import { Login } from './pages/login/login';
import { Dashboard } from './pages/dashboard/dashboard';
import { Profile } from './pages/profile/profile';
import { Attendance } from './pages/attendance/attendance';
import { Leave } from './pages/leave/leave';

export const routes: Routes = [
  { path: '', component: Login },
  { path: 'dashboard', component: Dashboard },
  { path: 'profile', component: Profile },
  { path: 'attendance', component: Attendance },
  { path: 'leave', component: Leave },
];