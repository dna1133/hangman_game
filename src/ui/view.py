from typing import Protocol

from core.configs.common_config import AMOUNT_OF_ATTEMPS
from core.configs.ui_confog import *


class CLIView:
    def __init__(self):
        self._stats = {"attemp": AMOUNT_OF_ATTEMPS, "word": "", "used": ()}

    @property
    def stats(self):
        return self._stats

    @stats.setter
    def stats(self, stats: dict):
        self._stats["attemp"] = stats["attemp"]
        self._stats["word"] = stats["word"]
        self._stats["used"] = stats["used"]

    def start_menu(self):
        print(GREETING)
        print(MENU_START_GAME)
        print(MENU_EXIT_GAME)

    def display_word(self):
        print(f"Введенные буквы: {''.join(self.stats['used'])}")
        print(f"Загаданное слово {self.stats['word']}")
        print(LINE_PH)

    def display_status(self):
        print(HANGMAN_PICS.get(self.stats["attemp"]))

    def handle_incorrect_menu(self):
        print(MENU_INCORRECT_ANSWER)

    def handle_correct_guess(self):
        print(EVENT_RIGHT_ANSWER)

    def handle_incorrect_guess(self):
        print(EVENT_BAD_ANSWER)

    def handle_repited_guess(self):
        print(EVENT_REPETED_LETTER)

    def display_result(self, result: str):
        if result == "win":
            print(EVENT_WIN + self.stats["word"])
        elif result == "loose":
            print(EVENT_LOOSE + self.stats["word"])
        print(LINE_PH)

    def read_guess(self) -> str:
        return input(EVENT_INPUT)

    def read_start_menu(self) -> str:
        return input(MENU_CHOICE)
