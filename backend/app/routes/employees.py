from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


employees = [
    {
        "employee_id": "EMP001",
        "full_name": "John Smith",
        "email": "john.smith@workmate.ai",
        "phone": "9876543210",
        "department": "Engineering",
        "role": "Python Developer",
        "joining_date": "2025-03-15",
        "status": "Active"
    },
    {
        "employee_id": "EMP002",
        "full_name": "Sarah Wilson",
        "email": "sarah.wilson@workmate.ai",
        "phone": "9123456780",
        "department": "HR",
        "role": "HR Manager",
        "joining_date": "2024-11-10",
        "status": "Active"
    },
    {
        "employee_id": "EMP003",
        "full_name": "David Brown",
        "email": "david.brown@workmate.ai",
        "phone": "9988776655",
        "department": "Finance",
        "role": "Accountant",
        "joining_date": "2023-08-21",
        "status": "Leave"
    }
]


# GET ALL EMPLOYEES
@router.get("/")
def get_employees():
    return employees


# GET SINGLE EMPLOYEE
@router.get("/{employee_id}")
def get_employee(employee_id: str):

    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# ADD EMPLOYEE
@router.post("/")
def add_employee(employee: dict):

    employees.append(employee)

    return {
        "message": "Employee added successfully",
        "employee": employee
    }
@router.put("/{employee_id}")
def update_employee(employee_id: str, updated_employee: dict):

    for index, employee in enumerate(employees):

        if employee["employee_id"] == employee_id:

            employees[index] = updated_employee

            return {
                "message": "Employee updated successfully",
                "employee": updated_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

# DELETE EMPLOYEE
@router.delete("/{employee_id}")
def delete_employee(employee_id: str):

    for employee in employees:

        if employee["employee_id"] == employee_id:

            employees.remove(employee)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )