# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MealPlanner
from typing import Callable, Dict, List, Any

def dry_run_mode(enabled: bool = False) -> None:
    """Enable or disable dry-run mode for data operations."""
    global _dry_run
    _dry_run = enabled

def _dry_run(operation: str, *args, **kwargs) -> None:
    """Execute an operation in dry-run mode (log only if enabled)."""
    if _dry_run:
        print(f"[DRY-RUN] {operation}({args}, {kwargs})")
    else:
        print(f"[EXEC] {operation}({args}, {kwargs})")

def _set_dry_run_status(status: bool) -> None:
    global _dry_run
    _dry_run = status

class DryRunContext:
    def __init__(self):
        self._enabled = False

    def enable(self):
        self._enabled = True
        global _dry_run
        _dry_run = True

    def disable(self):
        self._enabled = False
        global _dry_run
        _dry_run = False

    def is_enabled(self) -> bool:
        return self._enabled
