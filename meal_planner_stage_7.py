# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MealPlanner
def sort_records(records, key='date', reverse=False):
    if not records: return []
    date_key = lambda r: (r.get('date') or 0) * -1 if isinstance(r['date'], str) else r['date']
    priority_key = lambda r: -(r.get('priority') or 5)
    name_key = lambda r: r.get('name', '').lower()
    sort_keys = [key] + ['priority' if key != 'priority' else None, 'name' if key not in ('date','priority') else None]
    valid_keys = {'date': date_key, 'priority': priority_key, 'name': name_key}
    keys_to_use = []
    for k in sort_keys:
        if k and k in valid_keys:
            keys_to_use.append(valid_keys[k])
        elif k is None: continue
    def composite_sort(r):
        values = [k(r) for k in keys_to_use]
        return tuple(values) + (r.get('name', ''), r.get('date') or 0, -r.get('priority') or 5)
    sorted_records = sorted(records, key=composite_sort, reverse=reverse if len(keys_to_use)==1 else False)
    return sorted_records
