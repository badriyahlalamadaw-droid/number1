# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: MealPlanner
def edit_record(record_id, updates):
    if record_id not in records:
        print(f"Запись с id {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in record_fields and key in records[record_id]:
            records[record_id][key] = value
        else:
            print(f"Ошибка: поле '{key}' отсутствует в записи или списке полей.")
            return False
    
    print(f"Запись {record_id} успешно обновлена.")
    return True

# Пример вызова (раскомментируйте при необходимости):
# edit_record(1, {"name": "Новое название", "value": 42})
