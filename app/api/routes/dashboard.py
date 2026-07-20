from fastapi import APIRouter

from app.database.employee import get_employee_count
from app.database.leave import (
    get_pending_leave_count,
    get_approved_leave_count,
    get_rejected_leave_count,
)
from app.database.attendance import get_today_attendance_count

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard():

    return {
        "total_employees": get_employee_count(),
        "present_today": get_today_attendance_count(),
        "pending_leaves": get_pending_leave_count(),
        "approved_leaves": get_approved_leave_count(),
        "rejected_leaves": get_rejected_leave_count(),
    }