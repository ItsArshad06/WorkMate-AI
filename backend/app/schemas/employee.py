from pydantic import BaseModel


class EmployeeBase(BaseModel):
    employee_id: str
    full_name: str
    email: str
    phone: str
    department: str
    role: str
    joining_date: str
    status: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True