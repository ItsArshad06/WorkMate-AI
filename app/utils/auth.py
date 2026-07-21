HR_ADMINS = [
    "EMP-101"
]


def is_hr(employee_id):
    return employee_id.upper() in HR_ADMINS