"""
WorkMate AI Brain
"""

from app.ai.intents import detect_intent
from app.ai.conversation import conversation
from app.ai.skill_manager import skill_manager


class WorkMateBrain:

    def process(self, user_id: int, message: str):

        # Continue existing conversation
        session = conversation.get(user_id)

        if session:
            intent = session["intent"]
            return skill_manager.execute(
                intent,
                user_id,
                message,
            )

        # Detect new intent
        intent = detect_intent(message)

        if intent == "UNKNOWN":
            return (
                "🤖 Sorry, I didn't understand.\n\n"
                "Try saying:\n"
                "• I need leave\n"
                "• Show my profile\n"
                "• Check attendance"
            )

        # Start conversational skills
        if intent == "APPLY_LEAVE":
            return skill_manager.execute(
                intent,
                user_id,
                message,
            )

        return (
            f"✅ I understood your request.\n"
            f"Detected Intent: {intent}\n\n"
            "This feature will be connected soon."
        )


brain = WorkMateBrain()