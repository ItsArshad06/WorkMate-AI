"""
WorkMate AI - Skill Registry

This module stores every skill WorkMate AI knows.
The Brain will use this registry to decide
which module should handle the user's request.
"""

SKILLS = {
    "APPLY_LEAVE": {
        "name": "Leave Management",
        "description": "Apply for a leave request."
    },

    "APPROVE_LEAVE": {
        "name": "Leave Approval",
        "description": "Approve an employee leave request."
    },

    "REJECT_LEAVE": {
        "name": "Leave Rejection",
        "description": "Reject an employee leave request."
    },

    "LIST_EMPLOYEES": {
        "name": "Employee Directory",
        "description": "Show all registered employees."
    },

    "PROFILE": {
        "name": "Employee Profile",
        "description": "View an employee profile."
    },

    "ATTENDANCE": {
        "name": "Attendance",
        "description": "Manage employee attendance."
    },

    "DASHBOARD": {
        "name": "HR Dashboard",
        "description": "Display HR statistics."
    },

    "HELP": {
        "name": "Guide",
        "description": "Help users understand WorkMate AI."
    }
}


def get_skill(intent: str):
    """
    Returns information about a skill.
    """

    return SKILLS.get(
        intent,
        {
            "name": "Unknown",
            "description": "No skill available."
        }
    )