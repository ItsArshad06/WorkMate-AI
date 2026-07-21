from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
def get_dashboard():

    return {
        "total_employees": 250,
        "attendance_rate": "94%",
        "pending_leaves": 15,
        "active_departments": 8,
        "ai_status": "Online"
    }