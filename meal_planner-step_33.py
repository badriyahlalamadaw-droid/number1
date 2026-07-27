# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: MealPlanner
import copy as _copy

class ActionUndo:
    def __init__(self, action):
        self.action = action  # callable that reverts the last change
        self._undo_stack = []

    @property
    def undo_stack(self):
        return self._undo_stack

    def record(self):
        """Save current state so it can be restored later."""
        if isinstance(self.action, dict):
            saved = _copy.deepcopy(self.action)
        else:
            saved = _copy.deepcopy(self.action())
        self._undo_stack.append(saved)

    def undo_last(self):
        if not self._undo_stack:
            print("Нет откатываемых действий.")
            return
        target = self._undo_stack.pop()
        if isinstance(target, dict):
            self.action.update(target)
        else:
            self.action()

    def redo_last(self):
        """Restore the most recent undone state."""
        if not self._undo_stack:
            print("Нет действий для повторного применения.")
            return
        target = self._undo_stack.pop()
        if isinstance(target, dict):
            self.action.update(target)
        else:
            self.action()

    def clear(self):
        """Remove all undo records."""
        self._undo_stack.clear()
