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
            return (
                "🤖 Sorry, I don't know how to do that yet."
            )

        return skill.execute(
            user_id=user_id,
            message=message,
        )


skill_manager = SkillManager()