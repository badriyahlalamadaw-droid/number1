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

# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MealPlanner
def backup_data_file(filepath, backup_dir="./backups"):
    """Создаёт резервную копию файла данных.

    Функция:
    1. Создаёт директорию backup_dir, если она не существует.
    2. Присваивает дате резервной копии имя файла, содержащее дату и время.
    3. Копирует файл данных в директорию резервных копий.
    4. Возвращает путь к файлу резервной копии.

    Параметры:
    - filepath (str): Путь к файлу данных.
    - backup_dir (str): Путь к директории резервных копий (по умолчанию "./backups").

    Возвращает:
    - str: Путь к файлу резервной копии.
    """
    import os
    import shutil
    from datetime import datetime

    # Создаём директорию резервных копий, если она не существует
    os.makedirs(backup_dir, exist_ok=True)

    # Формируем имя файла резервной копии с датой и временем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}_{os.path.basename(filepath)}"
    backup_path = os.path.join(backup_dir, backup_filename)

    # Копируем файл данных в директорию резервных копий
    shutil.copy2(filepath, backup_path)

    return backup_path
