# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: MealPlanner
def archive_completed_records(archive_days=30):
    """Архивирует записи, старше указанного количества дней."""
    import shutil
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=archive_days)
    
    # Ищем файлы в директории проекта (предполагается наличие папки data или аналогичной)
    try:
        for filename in os.listdir('data'):  # Или 'recipes', 'meals' и т.д., если они есть отдельно
            filepath = os.path.join('data', filename)
            if not os.path.isfile(filepath):
                continue
                
            file_date_str = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d')
            
            # Если файл содержит дату создания, проверяем её (упрощённая логика для примера: архивируем всё старое)
            if file_date_str < cutoff_date.strftime('%Y-%m-%d'):
                archive_path = os.path.join('data', 'archive', filename + '.old')
                os.makedirs(os.path.dirname(archive_path), exist_ok=True)
                
                # Перемещаем файл в архив, если директория не существует, создаём её
                if not os.path.exists(os.path.dirname(archive_path)):
                    os.makedirs(os.path.dirname(archive_path))
                    
                shutil.move(filepath, archive_path)
    except FileNotFoundError:
        pass  # Директория data отсутствует или пуста
