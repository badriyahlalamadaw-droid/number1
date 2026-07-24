# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MealPlanner
def switch_profile(current, profiles):
    if not current:
        return None
    if len(profiles) == 1:
        return profiles[0]
    idx = int(current[0]) - 1 % len(profiles)
    return profiles[idx]
