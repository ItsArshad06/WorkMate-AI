from fastapi import APIRouter
from pydantic import BaseModel

from app.database.attendance import (
    check_in,
    check_out,
    get_today_attendance,
    get_employee_attendance,
    get_today_attendance_count,
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


class AttendanceRequest(BaseModel):
    employee_id: str


@router.post("/checkin")
def employee_check_in(request: AttendanceRequest):

    result = check_in(request.employee_id.upper())

    if result == "ALREADY_CHECKED_IN":
        return {"message": "Employee already checked in today"}

    return {"message": "Check-in successful"}


@router.post("/checkout")
def employee_check_out(request: AttendanceRequest):

    result = check_out(request.employee_id.upper())

    if result == "NOT_CHECKED_IN":
        return {"message": "Employee has not checked in today"}

    if result == "ALREADY_CHECKED_OUT":
        return {"message": "Employee already checked out"}

    return {"message": "Check-out successful"}


@router.get("/")
def today_attendance():

    attendance = get_today_attendance()

    return [
        dict(record)
        for record in attendance
    ]


@router.get("/employee/{employee_id}")
def employee_attendance(employee_id: str):

    attendance = get_employee_attendance(employee_id)

    return [
        dict(record)
        for record in attendance
    ]


@router.get("/count")
def attendance_count():

    return {
        "present_today": get_today_attendance_count()
    }