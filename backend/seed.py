from app.database import SessionLocal
from app.models.employee import Employee


db = SessionLocal()


employees = [
    {
        "employee_id": "EMP001",
        "name": "John Smith",
        "email": "john@workmate.ai",
        "department": "Engineering",
        "position": "Software Engineer"
    },
    {
        "employee_id": "EMP002",
        "name": "Sarah Wilson",
        "email": "sarah@workmate.ai",
        "department": "HR",
        "position": "HR Manager"
    },
    {
        "employee_id": "EMP003",
        "name": "David Brown",
        "email": "david@workmate.ai",
        "department": "Finance",
        "position": "Accountant"
    }
]


for emp in employees:

    exists = (
        db.query(Employee)
        .filter(Employee.employee_id == emp["employee_id"])
        .first()
    )

    if not exists:
        db.add(Employee(**emp))


db.commit()
db.close()


print("Employees seeded successfully")