from fastapi import APIRouter

router = APIRouter()


attendance_records = [
    {
        "id": 1,
        "employee": "John Smith",
        "date": "2026-07-22",
        "status": "Present",
        "check_in": "09:05 AM",
        "check_out": "06:10 PM"
    },
    {
        "id": 2,
        "employee": "Sarah Wilson",
        "date": "2026-07-22",
        "status": "Present",
        "check_in": "09:15 AM",
        "check_out": "06:00 PM"
    },
    {
        "id": 3,
        "employee": "David Brown",
        "date": "2026-07-22",
        "status": "Absent",
        "check_in": None,
        "check_out": None
    }
]


@router.get("/attendance")
def get_attendance():

    return {
        "attendance": attendance_records
    }