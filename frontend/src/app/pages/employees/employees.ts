import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { EmployeeService, Employee } from '../../services/employee.service';

@Component({
  selector: 'app-employees',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './employees.html',
  styleUrl: './employees.css'
})
export class Employees implements OnInit {

  employees: Employee[] = [];

  searchText = '';

  isEditing = false;

  newEmployee: Employee = {
    full_name: '',
    employee_id: '',
    email: '',
    phone: '',
    department: '',
    role: '',
    joining_date: '',
    status: 'Active'
  };

  constructor(
    private employeeService: EmployeeService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadEmployees();
  }
loadEmployees(): void {

  console.log("🚀 loadEmployees() called");

  this.employeeService.getEmployees().subscribe({

    next: (data) => {

      console.log("✅ API Response:", data);

      this.employees = data;

      this.cdr.detectChanges();

    },

    error: (err) => {

      console.error("❌ Error:", err);

    }

  });

}
  get filteredEmployees(): Employee[] {

    if (!this.searchText.trim()) {
      return this.employees;
    }

    const search = this.searchText.toLowerCase();

    return this.employees.filter(emp =>

      emp.full_name.toLowerCase().includes(search) ||

      emp.employee_id.toLowerCase().includes(search) ||

      emp.department.toLowerCase().includes(search) ||

      emp.role.toLowerCase().includes(search)

    );

  }

  get activeEmployees(): number {
    return this.employees.filter(e => e.status === 'Active').length;
  }

  get leaveEmployees(): number {
    return this.employees.filter(e => e.status === 'Leave').length;
  }

  get departmentCount(): number {

    return new Set(
      this.employees.map(emp => emp.department)
    ).size;

  }

  addEmployee(): void {

    if (this.isEditing) {

      this.employeeService.updateEmployee(
        this.newEmployee.employee_id,
        this.newEmployee
      ).subscribe({

        next: () => {

          alert("Employee updated successfully");

          this.resetForm();

          this.loadEmployees();

        },

        error: err => console.error(err)

      });

      return;
    }

    this.employeeService.addEmployee(this.newEmployee).subscribe({

      next: () => {

        alert("Employee added successfully");

        this.resetForm();

        this.loadEmployees();

      },

      error: err => console.error(err)

    });

  }

  editEmployee(emp: Employee): void {

    this.newEmployee = { ...emp };

    this.isEditing = true;

  }

  deleteEmployee(employeeId: string): void {

    if (!confirm("Delete this employee?")) {
      return;
    }

    this.employeeService.deleteEmployee(employeeId).subscribe({

      next: () => {

        alert("Employee deleted successfully");

        this.loadEmployees();

      },

      error: err => console.error(err)

    });

  }

  resetForm(): void {

    this.newEmployee = {
      full_name: '',
      employee_id: '',
      email: '',
      phone: '',
      department: '',
      role: '',
      joining_date: '',
      status: 'Active'
    };

    this.isEditing = false;

  }

}