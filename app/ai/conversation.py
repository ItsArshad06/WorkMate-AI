"""
WorkMate AI - Conversation Manager
"""

from copy import deepcopy


class ConversationManager:

    def __init__(self):
        self.sessions = {}

    def start(self, user_id, intent, skill=None):
        self.sessions[user_id] = {
            "intent": intent,
            "skill": skill,
            "step": "START",
            "identified": False,
            "data": {},
        }

    def get(self, user_id):
        return self.sessions.get(user_id)

    def exists(self, user_id):
        return user_id in self.sessions

    def update_step(self, user_id, step):
        if self.exists(user_id):
            self.sessions[user_id]["step"] = step

    def save_data(self, user_id, key, value):
        if self.exists(user_id):
            self.sessions[user_id]["data"][key] = value

    def get_data(self, user_id):
        if self.exists(user_id):
            return deepcopy(self.sessions[user_id]["data"])
        return {}

    def set_identified(self, user_id, value=True):
        if self.exists(user_id):
            self.sessions[user_id]["identified"] = value

    def is_identified(self, user_id):
        if self.exists(user_id):
            return self.sessions[user_id]["identified"]
        return False

    def set_skill(self, user_id, skill):
        if self.exists(user_id):
            self.sessions[user_id]["skill"] = skill

    def get_skill(self, user_id):
        if self.exists(user_id):
            return self.sessions[user_id]["skill"]
        return None

    def clear(self, user_id):
        self.sessions.pop(user_id, None)


conversation = ConversationManager()