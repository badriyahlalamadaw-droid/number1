# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MealPlanner
class Profile:
    def __init__(self, name="", calories=2000):
        self.name = name
        self.calories = calories


profiles = [Profile("Default", 2000)]


def get_profile(name=None):
    for p in profiles:
        if not name or p.name == name:
            return p
    raise ValueError(f"Profile '{name}' not found")
