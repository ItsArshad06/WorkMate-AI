from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database.employee import get_employee

router = APIRouter()


class LoginRequest(BaseModel):
    employee_id: str


@router.post("/login")
def login(request: LoginRequest):

    employee = get_employee(request.employee_id.upper())

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Login successful",
        "employee": {
            "full_name": employee["full_name"],
            "employee_id": employee["employee_id"],
            "department": employee["department"],
            "phone": employee["phone"],
        },
    }