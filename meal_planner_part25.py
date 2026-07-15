# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MealPlanner
def parse_date(date_str):
    """Parse date string in DD.MM.YYYY or YYYY-MM-DD format."""
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Неверный формат даты: '{date_str}'. Используйте DD.MM.YYYY или YYYY-MM-DD.")

def validate_week_range(start_date, end_date):
    if start_date > end_date:
        raise ValueError("Начальная дата не может быть позже конечной.")
    week = [start_date]
    for i in range(1, 7):
        next_day = (start_date + timedelta(days=i)).date() if isinstance(start_date, datetime) else start_date + timedelta(days=i)
        week.append(next_day)
    return week

def get_menu_for_week(planner, date_str):
    try:
        target_date = parse_date(date_str)
        week = validate_week_range(target_date, target_date + timedelta(days=6))
        menu = {}
        for day in week:
            key = f"{day.year}-{day.month:02d}-{day.day:02d}"
            if key not in planner.weekly_menu:
                raise ValueError(f"Нет данных на {key}.")
            menu[day] = planner.weekly_menu[key]
        return menu
    except ValueError as e:
        print(f"Ошибка: {e}")
