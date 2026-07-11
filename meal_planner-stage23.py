# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MealPlanner
def print_table(headers, rows):
    """Compact console table."""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, v in enumerate(row):
            if len(str(v)) > col_widths[i]:
                col_widths[i] = len(str(v))
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    sep = "-+-".join("-" * w for w in col_widths)
    print(fmt.format(*headers))
    print(sep)
    for row in rows:
        print(fmt.format(*row))
