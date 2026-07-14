from fastapi import APIRouter, HTTPException

from app.database.attendance import check_in, check_out

router = APIRouter()


@router.post("/attendance/checkin/{employee_id}")
def attendance_checkin(employee_id: str):

    result = check_in(employee_id.upper())

    if result == "SUCCESS":
        return {
            "message": "Check-in successful"
        }

    raise HTTPException(
        status_code=400,
        detail="Already checked in today"
    )


@router.post("/attendance/checkout/{employee_id}")
def attendance_checkout(employee_id: str):

    result = check_out(employee_id.upper())

    if result == "SUCCESS":
        return {
            "message": "Check-out successful"
        }

    if result == "NOT_CHECKED_IN":
        raise HTTPException(
            status_code=400,
            detail="Employee has not checked in today"
        )

    raise HTTPException(
        status_code=400,
        detail="Employee has already checked out"
    )