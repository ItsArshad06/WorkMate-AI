import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { EmployeeService, Employee } from '../../services/employee.service';


@Component({
  selector: 'app-employees',
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './employees.html',
  styleUrl: './employees.css',
})
export class Employees implements OnInit {


  employees: Employee[] = [];

  searchText = '';

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
    private employeeService: EmployeeService
  ) {}


  ngOnInit(): void {

    this.loadEmployees();

  }


  loadEmployees(){

    this.employeeService
      .getEmployees()
      .subscribe({

        next: (data)=>{

          this.employees = data;

        },

        error:(error)=>{

          console.error(
            "Failed to load employees",
            error
          );

        }

      });

  }


  addEmployee(){


    if(
      !this.newEmployee.full_name ||
      !this.newEmployee.employee_id ||
      !this.newEmployee.email ||
      !this.newEmployee.phone ||
      !this.newEmployee.department ||
      !this.newEmployee.role ||
      !this.newEmployee.joining_date
    ){

      alert("Please fill all fields");

      return;

    }


    this.employeeService
      .addEmployee(this.newEmployee)
      .subscribe({

        next:()=>{


          alert(
            "Employee added successfully"
          );


          this.loadEmployees();


          this.newEmployee = {

            full_name:'',
            employee_id:'',
            email:'',
            phone:'',
            department:'',
            role:'',
            joining_date:'',
            status:'Active'

          };


        },


        error:(error)=>{

          console.error(error);

          alert(
            "Failed to add employee"
          );

        }


      });


  }



  deleteEmployee(id:string){


    const confirmDelete =
      confirm(
        "Delete this employee?"
      );


    if(!confirmDelete){

      return;

    }


    this.employeeService
      .deleteEmployee(id)
      .subscribe({

        next:()=>{

          this.loadEmployees();

        },

        error:(error)=>{

          console.error(error);

        }

      });


  }



  get filteredEmployees(){

    if(!this.searchText.trim()){

      return this.employees;

    }


    const search =
      this.searchText.toLowerCase();


    return this.employees.filter(
      employee =>

        employee.full_name
        .toLowerCase()
        .includes(search)

        ||

        employee.department
        .toLowerCase()
        .includes(search)

        ||

        employee.role
        .toLowerCase()
        .includes(search)

    );


  }


}