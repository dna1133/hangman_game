from typing import Protocol

from core.configs.common_config import AMOUNT_OF_ATTEMPS
from core.configs.ui_confog import *


class Presenter(Protocol):
    def update_game_dto(self): ...


class CLIView:
    def __init__(self):
        self.stats = {"attemp": AMOUNT_OF_ATTEMPS, "word": ""}

    def init_ui(self, presenter: Presenter):
        self.stats = presenter.update_game_dto()

    @property
    def current_status(self):
        return HANGMAN_PICS.get(self.stats["attemp"])

    def start_menu(self):
        print(GREETING)
        print(MENU_START_GAME)
        print(MENU_EXIT_GAME)

    def display_word(self):
        print(f"Загаданное слово {self.stats['word']}")

    def display_status(self):
        print(self.current_status)

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
        if result == "loose":
            print(EVENT_LOOSE + self.stats["word"])

    def read_guess(self) -> str:
        return input(EVENT_INPUT)

    def read_start_menu(self) -> str:
        return input(MENU_CHOICE)
