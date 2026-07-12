"""
WorkMate AI - Skill Manager
"""

from app.skills.leave_skill import LeaveSkill
from app.skills.login_skill import login_skill


class SkillManager:

    def __init__(self):
        self.skills = {
            "APPLY_LEAVE": LeaveSkill(),
        }

    def execute(self, intent, user_id, message):

        if intent == "LOGIN":
            return login_skill.execute(
                telegram_user_id=user_id,
                employee_id=message.strip(),
            )

        skill = self.skills.get(intent)

        if skill:
            return skill.execute(
                user_id,
                message,
            )

        return "🤖 I don't know how to handle that yet."


skill_manager = SkillManager()