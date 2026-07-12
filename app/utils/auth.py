HR_ADMINS = [
    "EMP001",  # Change this to your HR/Admin Employee ID
]


def is_hr(employee_id):
    return employee_id.upper() in HR_ADMINS
