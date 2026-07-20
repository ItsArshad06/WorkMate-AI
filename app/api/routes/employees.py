from fastapi import APIRouter, HTTPException

from app.database.employee import (
    save_employee,
    get_all_employees,
    get_employee_details,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/")
def list_employees():

    employees = get_all_employees()

    return [
        dict(employee)
        for employee in employees
    ]


@router.post("/")
def add_employee(employee: dict):

    save_employee(
        employee["full_name"],
        employee["employee_id"],
        employee["email"],
        employee["phone"],
        employee["department"],
        employee["role"],
        employee["joining_date"],
        employee["status"]
    )

    return {
        "message": "Employee added successfully"
    }


@router.get("/{employee_id}")
def get_employee(employee_id: str):

    employee = get_employee_details(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return dict(employee)


@router.delete("/{employee_id}")
def remove_employee(employee_id: str):

    employee = get_employee_details(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    delete_employee(employee_id)

    return {
        "message": "Employee deleted successfully"
    }