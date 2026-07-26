from fastapi import APIRouter

router = APIRouter()


@router.get("/analytics")
def get_analytics():

    return {

        "summary": {
            "total_employees": 250,
            "active_employees": 242,
            "leave_employees": 8,
            "attendance_rate": "94%"
        },

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
        },

        "ai_insights": [

            "Attendance increased by 12% this month.",

            "Engineering has the highest workforce.",

            "Only 8 employees are currently on leave.",

            "AI predicts stable workforce growth next month."

        ]

    }