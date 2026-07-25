import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import {
  ProfileService,
  Profile as ProfileModel
} from '../../services/profile.service';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.html',
  styleUrl: './profile.css'
})
export class Profile implements OnInit {

  profile: ProfileModel = {
    employee_id: '',
    full_name: '',
    email: '',
    phone: '',
    department: '',
    role: '',
    joining_date: '',
    status: '',
    attendance: '',
    leave_balance: 0,
    performance: '',
    avatar: ''
  };

  isEditing = false;

  constructor(
    private profileService: ProfileService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadProfile();
  }

  loadProfile(): void {

    this.profileService.getProfile().subscribe({

      next: (data) => {

        this.profile = data;

        this.cdr.detectChanges();

      },

      error: (err) => console.error(err)

    });

  }

  editProfile(): void {
    this.isEditing = true;
  }

  saveProfile(): void {

    this.profileService.updateProfile(this.profile).subscribe({

      next: () => {

        alert("Profile updated successfully");

        this.isEditing = false;

        this.loadProfile();

      },

      error: err => console.error(err)

    });

  }

  cancelEdit(): void {

    this.isEditing = false;

    this.loadProfile();

  }

}