from fastapi import APIRouter

router = APIRouter()


leave_requests = [
    {
        "id": 1,
        "employee": "John Smith",
        "type": "Sick Leave",
        "start_date": "2026-07-25",
        "end_date": "2026-07-26",
        "reason": "Medical appointment",
        "status": "Pending"
    },
    {
        "id": 2,
        "employee": "Sarah Wilson",
        "type": "Casual Leave",
        "start_date": "2026-08-01",
        "end_date": "2026-08-02",
        "reason": "Personal work",
        "status": "Approved"
    },
    {
        "id": 3,
        "employee": "David Brown",
        "type": "Vacation",
        "start_date": "2026-08-10",
        "end_date": "2026-08-15",
        "reason": "Family trip",
        "status": "Rejected"
    }
]


@router.get("/leaves")
def get_leaves():

    return {
        "leaves": leave_requests
    }