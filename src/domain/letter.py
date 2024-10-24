from abc import ABC
from dataclasses import dataclass

from core.configs.common_config import UKNOWN_LETTER_PLACEHOLDER


@dataclass
class BaseLetter(ABC):
    value: str
    guessed: bool = False


@dataclass
class Letter(BaseLetter):
    def __post_init__(self):
        if not self.value.isalpha():
            raise ValueError("Not a letter")

    def __str__(self):
        return self.value if self.guessed else UKNOWN_LETTER_PLACEHOLDER

    def __eq__(self, value):
        return self.value == value
