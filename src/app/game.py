from app.use_cases import guess_letter
from core.configs.common_config import AMOUNT_OF_ATTEMPS, WORD_FILE_PATH
from domain.word import Word
from services.services import random_word, words_reader


class Game:
    def __init__(self):
        self.new_game()

    def new_game(self, test_word: Word | None = None):
        self.guess: str = ""
        self.guessed_letters: set = set()
        self.attemps: int = AMOUNT_OF_ATTEMPS
        self.raw_word: list = self._load_words()
        self.raw_word: Word = self._get_word(self.raw_word)
        self.word = Word(self.raw_word) if not test_word else Word(test_word)

    def _load_words(self) -> list:
        return words_reader(WORD_FILE_PATH)

    def _get_word(self, words) -> str:
        return random_word(words)

    def _handle_correct_guess(self, guess):
        self.guessed_letters.add(guess)

    def _handle_incorrect_guess(self):
        self.attemps -= 1

    def _handle_repited_guess(self): ...

    def handle_guess(self, guess):
        if guess in self.guessed_letters:
            self._handle_repited_guess()
            return "Repited"
        elif guess_letter(guess, self.word):
            self._handle_correct_guess(guess)
            return "Correct"
        else:
            self._handle_incorrect_guess()
            return "Incorrect"
