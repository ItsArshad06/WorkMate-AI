from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Attendance
from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# DATABASE CONNECTION
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



# SEED DATA
def seed_attendance():

    db = SessionLocal()

    try:

        if db.query(Attendance).count() == 0:

            records = [

                Attendance(
                    employee="John Smith",
                    date="2026-07-22",
                    status="Present",
                    check_in="09:05 AM",
                    check_out="06:10 PM"
                ),

                Attendance(
                    employee="Sarah Wilson",
                    date="2026-07-22",
                    status="Present",
                    check_in="09:15 AM",
                    check_out="06:00 PM"
                ),

                Attendance(
                    employee="David Brown",
                    date="2026-07-22",
                    status="Absent",
                    check_in=None,
                    check_out=None
                )

            ]

            db.add_all(records)
            db.commit()

    finally:

        db.close()



# GET ALL ATTENDANCE
@router.get("/")
def get_attendance(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    return db.query(Attendance).all()



# GET SINGLE RECORD
@router.get("/{record_id}")
def get_record(
    record_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    record = db.query(Attendance).filter(
        Attendance.id == record_id
    ).first()


    if not record:

        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )


    return record



# ADD ATTENDANCE
@router.post("/")
def add_record(
    record: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    new_record = Attendance(**record)

    db.add(new_record)

    db.commit()

    db.refresh(new_record)


    return {
        "message": "Attendance added successfully",
        "record": new_record
    }



# UPDATE ATTENDANCE
@router.put("/{record_id}")
def update_record(
    record_id: int,
    updated_record: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    record = db.query(Attendance).filter(
        Attendance.id == record_id
    ).first()


    if not record:

        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )


    for key, value in updated_record.items():

        setattr(record, key, value)


    db.commit()

    db.refresh(record)


    return {
        "message": "Attendance updated successfully",
        "record": record
    }



# DELETE ATTENDANCE
@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    record = db.query(Attendance).filter(
        Attendance.id == record_id
    ).first()


    if not record:

        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )


    db.delete(record)

    db.commit()


    return {
        "message": "Attendance deleted successfully"
    }