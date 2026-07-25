from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/leaves",
    tags=["Leaves"]
)

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


# GET ALL
@router.get("/")
def get_leaves():
    return leave_requests


# GET ONE
@router.get("/{leave_id}")
def get_leave(leave_id: int):

    for leave in leave_requests:
        if leave["id"] == leave_id:
            return leave

    raise HTTPException(
        status_code=404,
        detail="Leave request not found"
    )


# ADD
@router.post("/")
def add_leave(leave: dict):

    leave_requests.append(leave)

    return {
        "message": "Leave request added successfully",
        "leave": leave
    }


# UPDATE
@router.put("/{leave_id}")
def update_leave(leave_id: int, updated_leave: dict):

    for index, leave in enumerate(leave_requests):

        if leave["id"] == leave_id:

            leave_requests[index] = updated_leave

            return {
                "message": "Leave updated successfully",
                "leave": updated_leave
            }

    raise HTTPException(
        status_code=404,
        detail="Leave request not found"
    )


# DELETE
@router.delete("/{leave_id}")
def delete_leave(leave_id: int):

    for leave in leave_requests:

        if leave["id"] == leave_id:

            leave_requests.remove(leave)

            return {
                "message": "Leave deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Leave request not found"
    )