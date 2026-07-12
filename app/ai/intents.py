"""
WorkMate AI - Intent Detection

This module identifies what the user wants to do.
The Brain will use this to choose the correct skill.
"""


INTENTS = {
    "APPLY_LEAVE": [
        "leave",
        "apply leave",
        "need leave",
        "vacation",
        "holiday",
        "time off",
    ],

    "APPROVE_LEAVE": [
        "approve leave",
        "approve",
        "accept leave",
    ],

    "REJECT_LEAVE": [
        "reject leave",
        "reject",
        "decline leave",
    ],

    "LIST_EMPLOYEES": [
        "employees",
        "employee list",
        "list employees",
        "show employees",
    ],

    "PROFILE": [
        "profile",
        "my profile",
        "who am i",
    ],

    "ATTENDANCE_ACTION": [
        "check in",
        "checkin",
        "i'm here",
        "im here",
        "present",
        "arrived",
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
        "dashboard",
        "hr dashboard",
        "statistics",
        "stats",
        "report",
    ],

    "HELP": [
        "help",
        "guide",
        "how",
        "commands",
    ],
}


def detect_intent(message: str) -> str:

    message = message.lower().strip()

    for intent, keywords in INTENTS.items():
        for keyword in keywords:
            if keyword in message:
                return intent

    return "UNKNOWN"