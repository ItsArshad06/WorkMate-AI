"""
WorkMate AI - Brain
"""

from app.ai.conversation import conversation
from app.ai.intents import detect_intent
from app.ai.skill_manager import skill_manager


class WorkMateBrain:

    def process(self, user_id: int, message: str):

        # Detect what the user currently wants
        intent = detect_intent(message)

        print("Detected Intent:", intent)

        # If the user starts a new command, abandon the old conversation
        if intent != "UNKNOWN":

            current = conversation.get(user_id)

            if current:

                if current["intent"] != intent:
                    conversation.clear(user_id)

            if not conversation.get(user_id):
                conversation.start(user_id, intent)

            return skill_manager.execute(
                intent,
                user_id,
                message,
            )

        # Continue existing conversation only if no new intent was detected
        current = conversation.get(user_id)

        if current:
            return skill_manager.execute(
                current["intent"],
                user_id,
                message,
            )

        return (
            "🤖 Sorry, I didn't understand that.\n"
            "Try asking for leave, attendance, profile or help."
        )


brain = WorkMateBrain()