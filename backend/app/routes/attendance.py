from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

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


# GET ALL
@router.get("/")
def get_attendance():
    return attendance_records


# GET ONE
@router.get("/{record_id}")
def get_record(record_id: int):

    for record in attendance_records:

        if record["id"] == record_id:
            return record

    raise HTTPException(
        status_code=404,
        detail="Attendance record not found"
    )


# ADD
@router.post("/")
def add_record(record: dict):

    attendance_records.append(record)

    return {
        "message": "Attendance added successfully",
        "record": record
    }


# UPDATE
@router.put("/{record_id}")
def update_record(record_id: int, updated_record: dict):

    for index, record in enumerate(attendance_records):

        if record["id"] == record_id:

            attendance_records[index] = updated_record

            return {
                "message": "Attendance updated successfully",
                "record": updated_record
            }

    raise HTTPException(
        status_code=404,
        detail="Attendance record not found"
    )


# DELETE
@router.delete("/{record_id}")
def delete_record(record_id: int):

    for record in attendance_records:

        if record["id"] == record_id:

            attendance_records.remove(record)

            return {
                "message": "Attendance deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Attendance record not found"
    )