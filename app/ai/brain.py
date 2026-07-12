"""
WorkMate AI - Brain
"""

from app.ai.conversation import conversation
from app.ai.intents import detect_intent
from app.ai.skill_manager import skill_manager


class WorkMateBrain:

    def process(self, user_id: int, message: str):

        # Continue existing conversation
        session = conversation.get(user_id)

        if session:
            return skill_manager.execute(
                session["intent"],
                user_id,
                message,
            )

        # Detect new intent
        intent = detect_intent(message)

        if not skill_manager.has_skill(intent):
            return (
                "🤖 Sorry, I didn't understand that.\n"
                "Try asking for leave, attendance, profile or help."
            )

        # Start conversation
        conversation.start(user_id, intent)

        return skill_manager.execute(
            intent,
            user_id,
            message,
        )


brain = WorkMateBrain()