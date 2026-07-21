from app.database.leave import (
    get_employee_leave_summary,
    get_all_leaves,
)


def leave_summary(employee_id):

    summary = get_employee_leave_summary(employee_id)

    return (
        f"📝 Leave Summary\n\n"
        f"Pending : {summary['Pending']}\n"
        f"Approved: {summary['Approved']}\n"
        f"Rejected: {summary['Rejected']}"
    )


def latest_leave(employee_id):

    leaves = get_all_leaves()

    employee_leaves = [
        leave for leave in leaves
        if leave["employee_id"] == employee_id
    ]

    if not employee_leaves:
        return "You don't have any leave requests."

    latest = employee_leaves[0]

    return (
        f"📄 Latest Leave\n\n"
        f"From : {latest['start_date']}\n"
        f"To : {latest['end_date']}\n"
        f"Reason : {latest['reason']}\n"
        f"Status : {latest['status']}"
    )