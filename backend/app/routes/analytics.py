from fastapi import APIRouter

router = APIRouter()


@router.get("/analytics")
def get_analytics():

    return {

        "employee_growth": {
            "January": 180,
            "February": 210,
            "March": 230,
            "April": 250
        },

        "attendance_summary": {
            "present_percentage": 94,
            "absent_percentage": 6
        },

        "leave_summary": {
            "approved": 20,
            "pending": 8,
            "rejected": 3
        },

        "department_distribution": {
            "Engineering": 120,
            "HR": 30,
            "Finance": 40,
            "Operations": 60
        }
    }