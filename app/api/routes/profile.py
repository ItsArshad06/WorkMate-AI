from fastapi import APIRouter, HTTPException

from app.database.employee import get_employee_details

router = APIRouter()


@router.get("/profile/{employee_id}")
def get_profile(employee_id: str):

    employee = get_employee_details(employee_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "full_name": employee["full_name"],
        "employee_id": employee["employee_id"],
        "department": employee["department"],
        "phone": employee["phone"],
    }