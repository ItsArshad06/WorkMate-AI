from fastapi import APIRouter
from pydantic import BaseModel

from app.database.leave import (
    create_leave,
    get_pending_leaves,
    approve_leave,
    reject_leave,
)

router = APIRouter()


class LeaveRequest(BaseModel):
    employee_id: str
    start_date: str
    end_date: str
    reason: str


@router.post("/leave/apply")
def apply_leave(request: LeaveRequest):

    create_leave(
        request.employee_id.upper(),
        request.start_date,
        request.end_date,
        request.reason,
    )

    return {
        "message": "Leave applied successfully"
    }


@router.get("/leave/pending")
def pending_leaves():

    return get_pending_leaves()


@router.post("/leave/approve/{leave_id}")
def approve_leave_api(leave_id: int):

    approve_leave(leave_id)

    return {
        "message": f"Leave {leave_id} approved"
    }


@router.post("/leave/reject/{leave_id}")
def reject_leave_api(leave_id: int):

    reject_leave(leave_id)

    return {
        "message": f"Leave {leave_id} rejected"
    }