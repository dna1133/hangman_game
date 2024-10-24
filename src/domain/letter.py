from abc import ABC
from dataclasses import dataclass, field
from functools import lru_cache

from core.configs.common_config import UKNOWN_LETTER_PLACEHOLDER


@dataclass
class BaseLetter(ABC):
    letter: str
    guessed: bool = False


@dataclass
class Letter(BaseLetter):
    def __post_init__(self):
        if not self.letter.isalpha():
            raise ValueError("Not a letter")

    def __str__(self):
        return self.letter if self.guessed else UKNOWN_LETTER_PLACEHOLDER


@dataclass
class Word:
    raw_word: str

    def __post_init__(self):
        self._letters = [Letter(letter) for letter in self.raw_word]

    def __str__(self):
        return "".join([str(letter) for letter in self.letters])

    @property
    def letters(self):
        return self._letters
