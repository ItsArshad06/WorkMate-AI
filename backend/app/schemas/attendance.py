from pydantic import BaseModel


class AttendanceBase(BaseModel):
    employee: str
    date: str
    status: str
    check_in: str | None = None
    check_out: str | None = None


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        from_attributes = True