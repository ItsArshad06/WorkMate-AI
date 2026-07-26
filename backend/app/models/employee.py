from sqlalchemy import Column, Integer, String

from app.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    department = Column(String)
    role = Column(String)
    joining_date = Column(String)
    status = Column(String)