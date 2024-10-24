from typing import Protocol

from app.game import Game
from core.exceptions import BaseAppException


class View(Protocol):
    @property
    def stats(self) -> dict: ...
    def start_menu(self) -> None: ...
    def handle_incorrect_menu(self) -> None: ...
    def display_word(self) -> None: ...
    def display_status(self) -> None: ...
    def display_result(self, result) -> None: ...
    def handle_correct_guess(self) -> None: ...
    def handle_incorrect_guess(self) -> None: ...
    def handle_repited_guess(self) -> None: ...
    def read_guess(self) -> str: ...
    def read_start_menu(self) -> str: ...


class Presenter:
    def __init__(self, game: Game, view: View):
        self.game = game
        self.view = view
        self.used = set()

    def start_game(self):
        self.view.start_menu()
        menu_choise = self.view.read_start_menu()
        if menu_choise.lower() == "н":
            self.game.new_game()
            self.update_game_dto()
            self.game_loop()
        elif menu_choise.lower() == "в":
            exit()
        else:
            self.view.handle_incorrect_menu()
            self.start_game()

    def game_loop(self):
        while self.game.attemps > 0 and not self.game.word.guessed:
            self.view.display_status()
            self.view.display_word()
            guess = self.view.read_guess()
            guess_result = self.game.handle_guess(guess)
            self.used.add(guess)
            match guess_result:
                case "Repited":
                    self.view.handle_repited_guess
                case "Correct":
                    self.view.handle_correct_guess
                case "Incorrect":
                    self.view.handle_incorrect_guess

            self.update_game_dto()
        if self.game.attemps == 0:
            self.view.stats = {
                "attemp": self.game.attemps,
                "word": str(self.game.raw_word),
                "used": self.used,
            }
            self.view.display_result("loose")
        elif self.game.word.guessed:
            self.view.stats = {
                "attemp": self.game.attemps,
                "word": str(self.game.raw_word),
                "used": self.used,
            }
            self.view.display_result("win")
        else:
            raise BaseAppException()

        self.start_game()

    def update_game_dto(self) -> dict:
        self.view.stats = {
            "attemp": self.game.attemps,
            "word": str(self.game.word),
            "used": self.used,
        }
