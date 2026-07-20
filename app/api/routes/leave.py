from fastapi import APIRouter
from pydantic import BaseModel

from app.database.leave import (
    create_leave,
    get_all_leaves,
    get_pending_leaves,
    approve_leave,
    reject_leave,
)

router = APIRouter(
    prefix="/leave",
    tags=["Leave"]
)


class LeaveRequest(BaseModel):
    employee_id: str
    start_date: str
    end_date: str
    reason: str


@router.post("/")
def apply_leave(request: LeaveRequest):

    create_leave(
        request.employee_id.upper(),
        request.start_date,
        request.end_date,
        request.reason
    )

    return {
        "message": "Leave applied successfully"
    }


@router.get("/")
def list_leaves():

    leaves = get_all_leaves()

    return [
        dict(leave)
        for leave in leaves
    ]


@router.get("/pending")
def pending_leaves():

    leaves = get_pending_leaves()

    return [
        dict(leave)
        for leave in leaves
    ]


@router.post("/approve/{leave_id}")
def approve_leave_api(leave_id: int):

    approve_leave(leave_id)

    return {
        "message": f"Leave {leave_id} approved"
    }


@router.post("/reject/{leave_id}")
def reject_leave_api(leave_id: int):

    reject_leave(leave_id)

    return {
        "message": f"Leave {leave_id} rejected"
    }