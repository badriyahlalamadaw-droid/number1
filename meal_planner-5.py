# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: MealPlanner
def delete_record(collection_name, record_id):
    if collection_name not in db:
        raise KeyError(f"Collection '{collection_name}' does not exist.")
    if record_id not in db[collection_name]:
        print(f"No record with id {record_id} found in '{collection_name}'.")
        return False
    del db[collection_name][record_id]
    print(f"Record deleted from '{collection_name}'.")
    return True

def handle_missing_ids(collection_name, target_list):
    missing = [item for item in target_list if item not in db.get(collection_name, {})]
    if missing:
        print(f"Warning: The following IDs are missing in '{collection_name}': {missing}")
