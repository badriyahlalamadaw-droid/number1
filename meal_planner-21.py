# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: MealPlanner
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def is_due(self, today=None):
        if today is None:
            from datetime import date
            today = date.today()
        return today >= self.due_date

    def __str__(self):
        status = "⏳" if not self.is_due() else "✅"
        return f"{status} {self.title} (до {self.due_date})"


def setup_reminders(planner, week_days):
    planner.reminders = []
    for day in week_days:
        title = f"Приготовить обед для {day}"
        due = date.today() + timedelta(days=week_days.index(day))
        planner.reminders.append(Reminder(title, due))


def show_reminders(planner):
    today = date.today()
    print("📌 Напоминания:")
    for r in planner.reminders:
        if r.due_date <= today:
            print(f"  ✅ {r.title}")
        else:
            days_left = (r.due_date - today).days
            print(f"  ⏳ {r.title} ({days_left} дн.)")


class Planner:
    def __init__(self):
        self.days_of_week = []
        self.week_plan = {}
        self.products = {}
        self.recipes = {}
        self.shopping_list = []
        self.reminders = []

    def add_day(self, day_name, meal_items=None):
        self.days_of_week.append(day_name)
        if meal_items:
            self.week_plan[day_name] = meal_items
        else:
            self.week_plan[day_name] = []


planner = Planner()
setup_reminders(planner, ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"])

show_reminders(planner)
