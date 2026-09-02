# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MealPlanner
def backup_data(file_path, backup_dir="."):
    import shutil, os
    if not os.path.exists(file_path):
        print(f"[Backup] Файл {file_path} не найден.")
        return None
    backup_path = os.path.join(backup_dir, f"{os.path.basename(file_path)}.bak")
    try:
        shutil.copy2(file_path, backup_path)
        print(f"[Backup] Резервная копия сохранена: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"[Backup] Ошибка резервного копирования: {e}")
        return None
