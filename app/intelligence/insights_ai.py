from app.intelligence.analytics_ai import (
    company_statistics,
    leave_statistics,
)


def attendance_insight():

    stats = company_statistics()

    percentage = stats["attendance_percentage"]

    if percentage >= 95:

        return (
            "🟢 Attendance is excellent today.\n"
            "Employee participation is very high."
        )

    elif percentage >= 80:

        return (
            "🟡 Attendance is good today.\n"
            "No major attendance concerns."
        )

    elif percentage >= 60:

        return (
            "🟠 Attendance is below expectations.\n"
            "HR should review absenteeism."
        )

    else:

        return (
            "🔴 Attendance is critically low today.\n"
            "Immediate HR attention is recommended."
        )


def leave_insight():

    leave = leave_statistics()

    pending = leave["pending"]

    if pending == 0:

        return (
            "✅ All leave requests have been processed."
        )

    elif pending <= 5:

        return (
            f"📝 {pending} leave request(s) are awaiting approval."
        )

    else:

        return (
            f"⚠ {pending} leave requests are pending.\n"
            "HR review is recommended."
        )


def company_insights():

    report = "🤖 AI HR Insights\n\n"

    report += attendance_insight()

    report += "\n\n"

    report += leave_insight()

    return report
def executive_brief():

    stats = company_statistics()

    report = (
        "📋 Daily Executive HR Brief\n\n"
    )

    report += (
        f"👥 Workforce : {stats['employees']} employees\n"
        f"🟢 Present : {stats['present']}\n"
        f"🔴 Absent : {stats['absent']}\n"
        f"📈 Attendance : {stats['attendance_percentage']}%\n\n"
    )

    report += attendance_insight()

    report += "\n\n"

    report += leave_insight()

    report += "\n\n"

    if stats["attendance_percentage"] >= 95:

        report += (
            "💡 HR Recommendation\n"
            "No immediate HR action is required today.\n"
            "Overall workforce health is excellent."
        )

    elif stats["attendance_percentage"] >= 80:

        report += (
            "💡 HR Recommendation\n"
            "Continue monitoring attendance.\n"
            "No urgent intervention required."
        )

    else:

        report += (
            "💡 HR Recommendation\n"
            "Attendance requires HR review.\n"
            "Investigate absenteeism trends."
        )

    return report