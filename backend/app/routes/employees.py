from fastapi import APIRouter

router = APIRouter()


employees = [
    {
        "id": 1,
        "name": "John Smith",
        "department": "Engineering",
        "role": "Python Developer",
        "status": "Active"
    },
    {
        "id": 2,
        "name": "Sarah Wilson",
        "department": "HR",
        "role": "HR Manager",
        "status": "Active"
    },
    {
        "id": 3,
        "name": "David Brown",
        "department": "Finance",
        "role": "Accountant",
        "status": "On Leave"
    }
]


@router.get("/employees")
def get_employees():
    return {
        "employees": employees
    }