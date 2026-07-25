# === Stage 32: Добавь журнал действий пользователя ===
# Project: MealPlanner
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, action_type, description, details=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": action_type,
            "description": description,
            "details": details or {},
        }
        self._entries.append(entry)

    @property
    def entries(self):
        return list(self._entries)

    @property
    def summary(self):
        counts = {}
        for e in self._entries:
            t = e["type"]
            counts[t] = counts.get(t, 0) + 1
        return counts
