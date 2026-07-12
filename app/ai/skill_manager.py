"""
WorkMate AI - Skill Manager
"""

from app.skills.leave_skill import LeaveSkill
from app.skills.login_skill import login_skill
from app.skills.attendance_skill import attendance_skill
from app.skills.profile_skill import profile_skill
from app.skills.dashboard_skill import dashboard_skill
from app.skills.hr_leave_skill import hr_leave_skill


class SkillManager:

    def __init__(self):

        self.skills = {
            "APPLY_LEAVE": LeaveSkill(),
            "ATTENDANCE_ACTION": attendance_skill,
            "PROFILE": profile_skill,
            "DASHBOARD": dashboard_skill,
            "APPROVE_LEAVE": hr_leave_skill,
            "REJECT_LEAVE": hr_leave_skill,
            "LIST_EMPLOYEES": hr_leave_skill,
        }

    def has_skill(self, intent):
        return intent in self.skills

    def execute(self, intent, user_id, message):

        if intent == "LOGIN":
            return login_skill.execute(
                telegram_user_id=user_id,
                employee_id=message,
            )

        skill = self.skills.get(intent)

        if skill is None:
            return "🤖 Sorry, I don't know how to do that yet."

        return skill.execute(
            user_id=user_id,
            message=message,
        )


skill_manager = SkillManager()