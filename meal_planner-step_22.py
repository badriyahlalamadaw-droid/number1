# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: MealPlanner
def check_expired_reminders():
    """Проверяет просроченные напоминания и возвращает список устаревших."""
    expired = []
    now = datetime.now()
    for reminder in reminders:
        if isinstance(reminder, dict) and "date" in reminder:
            r_date = datetime.strptime(reminder["date"], "%Y-%m-%d")
            if now > r_date:
                expired.append({"text": reminder.get("text", ""), "date": reminder["date"]})
    return expired

def print_expired_reminders():
    """Выводит список просроченных напоминаний, если они есть."""
    expired = check_expired_reminders()
    if not expired:
        print("\nНапоминания актуальны. Ничего не упущено.")
        return
    print("\n⚠️  Просроченные напоминания:")
    for item in expired:
        print(f"   - {item['text']} (было запланировано на {item['date']})")

check_expired_reminders()
