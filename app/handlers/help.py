from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = """
🤖 WorkMate AI
HR Management Assistant

━━━━━━━━━━━━━━
👤 Employee Commands
━━━━━━━━━━━━━━

/login <Employee ID>
Login to your account

/logout
Logout from your account

/myprofile
View your employee profile

/applyleave <start> <end> <reason>
Apply for leave request


━━━━━━━━━━━━━━
📅 Attendance
━━━━━━━━━━━━━━

/checkin
Mark today's attendance

/checkout
Complete your attendance

/attendance
View today's attendance report


━━━━━━━━━━━━━━
🏢 HR/Admin Commands
━━━━━━━━━━━━━━

/employees <HR ID>
View employee list

/leaves <HR ID>
View leave requests

/approve <Leave ID>
Approve leave request

/reject <Leave ID>
Reject leave request


━━━━━━━━━━━━━━
📊 Dashboard
━━━━━━━━━━━━━━

/dashboard
View HR dashboard


━━━━━━━━━━━━━━

Version: 1.0.0
"""

    await update.message.reply_text(message)