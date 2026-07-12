"""
WorkMate AI - Intent Detection
"""


INTENTS = {
    "APPLY_LEAVE": [
        "apply leave",
        "need leave",
        "vacation",
        "holiday",
        "time off",
        "leave",
    ],

    "APPROVE_LEAVE": [
        "approve leave",
        "approve",
    ],

    "REJECT_LEAVE": [
        "reject leave",
        "reject",
    ],

    "LIST_EMPLOYEES": [
        "show pending leaves",
        "pending leaves",
        "show pending",
    ],

    "PROFILE": [
        "show my profile",
        "my profile",
        "profile",
        "who am i",
        "my details",
    ],

    "ATTENDANCE_ACTION": [
        "check me in",
        "check in",
        "checkin",
        "i'm here",
        "im here",
        "arrived",
        "present",
        "check me out",
        "check out",
        "checkout",
        "going home",
        "leaving",
        "bye",
    ],

    "ATTENDANCE": [
        "attendance",
    ],

    "DASHBOARD": [
        "show dashboard",
        "hr dashboard",
        "dashboard",
        "statistics",
        "stats",
        "analytics",
        "reports",
        "report",
    ],

    "HELP": [
        "help",
        "guide",
        "commands",
        "how",
    ],
}


# Priority order
PRIORITY = [
    "APPROVE_LEAVE",
    "REJECT_LEAVE",
    "LIST_EMPLOYEES",
    "DASHBOARD",
    "ATTENDANCE_ACTION",
    "ATTENDANCE",
    "PROFILE",
    "HELP",
    "APPLY_LEAVE",
]


def detect_intent(message: str) -> str:

    message = message.lower().strip()

    for intent in PRIORITY:
        for keyword in INTENTS[intent]:
            if keyword in message:
                return intent

    return "UNKNOWN"