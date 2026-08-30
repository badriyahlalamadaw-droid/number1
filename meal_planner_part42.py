# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MealPlanner
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
}

class Colored:
    def __init__(self, enabled=True):
        self.enabled = enabled

    def set_enabled(self, value):
        self.enabled = value

    def _wrap(self, text, code):
        if not self.enabled:
            return text
        return f"{code}{text}{ANSI['reset']}"

    def red(self, text): return self._wrap(text, ANSI["red"])
    def green(self, text): return self._wrap(text, ANSI["green"])
    def yellow(self, text): return self._wrap(text, ANSI["yellow"])
    def blue(self, text): return self._wrap(text, ANSI["blue"])
    def cyan(self, text): return self._wrap(text, ANSI["cyan"])
    def bold(self, text): return self._wrap(text, ANSI["bold"])
    def dim(self, text): return self._wrap(text, ANSI["dim"])
    def bg_green(self, text): return self._wrap(text, ANSI["bg_green"])
