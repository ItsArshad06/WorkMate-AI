from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database.employee import get_employee
from app.database.session import (
    save_session,
    delete_session,
)

router = APIRouter(
    tags=["Authentication"]
)


class LoginRequest(BaseModel):
    telegram_user_id: int
    employee_id: str


class LogoutRequest(BaseModel):
    telegram_user_id: int


@router.post("/login")
def login(request: LoginRequest):

    employee = get_employee(request.employee_id.upper())

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    save_session(
        request.telegram_user_id,
        employee["employee_id"],
        employee["role"],
        employee["full_name"],
        employee["department"],
    )

    return {
        "message": "Login successful",
        "employee": {
            "full_name": employee["full_name"],
            "employee_id": employee["employee_id"],
            "department": employee["department"],
            "role": employee["role"],
            "phone": employee["phone"],
        },
    }


@router.post("/logout")
def logout(request: LogoutRequest):

    delete_session(request.telegram_user_id)

    return {
        "message": "Logout successful"
    }