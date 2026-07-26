from app.database import SessionLocal
from app.models.employee import Employee


db = SessionLocal()


employees = [
    Employee(
        employee_id="EMP001",
        full_name="John Smith",
        email="john@workmate.ai",
        phone="9876543210",
        department="Engineering",
        role="Software Engineer",
        joining_date="2026-01-10",
        status="Active"
    ),

    Employee(
        employee_id="EMP002",
        full_name="Sarah Wilson",
        email="sarah@workmate.ai",
        phone="9876543211",
        department="HR",
        role="HR Manager",
        joining_date="2026-02-15",
        status="Active"
    ),

    Employee(
        employee_id="EMP003",
        full_name="David Brown",
        email="david@workmate.ai",
        phone="9876543212",
        department="Finance",
        role="Accountant",
        joining_date="2026-03-20",
        status="Active"
    )
]


for employee in employees:

    exists = (
        db.query(Employee)
        .filter(Employee.employee_id == employee.employee_id)
        .first()
    )

    if not exists:
        db.add(employee)


db.commit()
db.close()

print("Employees seeded successfully")