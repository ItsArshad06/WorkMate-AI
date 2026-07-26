from sqlalchemy import Column, Integer, String

from app.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee = Column(String)
    date = Column(String)
    status = Column(String)
    check_in = Column(String, nullable=True)
    check_out = Column(String, nullable=True)