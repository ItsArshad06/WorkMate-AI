from fastapi import APIRouter

from app.database.employee import get_employee_count
from app.database.leave import (
    get_pending_leave_count,
    get_approved_leave_count,
    get_rejected_leave_count,
)
from app.database.attendance import get_today_attendance

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    return {
        "total_employees": get_employee_count(),
        "today_attendance": len(get_today_attendance()),
        "pending_leaves": get_pending_leave_count(),
        "approved_leaves": get_approved_leave_count(),
        "rejected_leaves": get_rejected_leave_count(),
    }