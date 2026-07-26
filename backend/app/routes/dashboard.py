from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user


router = APIRouter()


@router.get("/dashboard")
def get_dashboard(
    user = Depends(get_current_user)
):

    return {

        "total_employees": 250,

        "attendance_rate": "94%",

        "pending_leaves": 15,

        "active_departments": 8,

        "ai_status": "Online",

        "logged_in_user": user

    }