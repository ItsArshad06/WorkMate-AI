import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import {
  LeaveService,
  LeaveRequest
} from '../../services/leave.service';

@Component({
  selector: 'app-leave',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './leave.html',
  styleUrl: './leave.css'
})
export class Leave implements OnInit {

  leaves: LeaveRequest[] = [];

  isEditing = false;

  newLeave: LeaveRequest = {
    id: 0,
    employee: '',
    type: '',
    start_date: '',
    end_date: '',
    reason: '',
    status: 'Pending'
  };

  constructor(
    private leaveService: LeaveService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadLeaves();
  }

  loadLeaves(): void {

    this.leaveService.getLeaves().subscribe({

      next: (data) => {

        console.log("Leaves Loaded:", data);

        this.leaves = data;

        this.cdr.detectChanges();

      },

      error: (err) => console.error(err)

    });

  }

  addLeave(): void {

    if (this.isEditing) {

      this.leaveService.updateLeave(this.newLeave.id, this.newLeave).subscribe({

        next: () => {

          alert("Leave updated successfully");

          this.resetForm();

          this.loadLeaves();

        },

        error: err => console.error(err)

      });

      return;

    }

    this.leaveService.addLeave(this.newLeave).subscribe({

      next: () => {

        alert("Leave added successfully");

        this.resetForm();

        this.loadLeaves();

      },

      error: err => console.error(err)

    });

  }

  editLeave(leave: LeaveRequest): void {

    this.newLeave = { ...leave };

    this.isEditing = true;

  }

  deleteLeave(id: number): void {

    if (!confirm("Delete this leave request?")) return;

    this.leaveService.deleteLeave(id).subscribe({

      next: () => {

        alert("Leave deleted successfully");

        this.loadLeaves();

      },

      error: err => console.error(err)

    });

  }

  resetForm(): void {

    this.newLeave = {
      id: 0,
      employee: '',
      type: '',
      start_date: '',
      end_date: '',
      reason: '',
      status: 'Pending'
    };

    this.isEditing = false;

  }

  get pendingCount(): number {
    return this.leaves.filter(l => l.status === 'Pending').length;
  }

  get approvedCount(): number {
    return this.leaves.filter(l => l.status === 'Approved').length;
  }

  get rejectedCount(): number {
    return this.leaves.filter(l => l.status === 'Rejected').length;
  }

}