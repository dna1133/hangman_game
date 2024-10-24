from dataclasses import dataclass

from domain.letter import Letter


@dataclass
class Word:
    raw_word: str

    def __post_init__(self):
        self._letters = [Letter(letter) for letter in self.raw_word]

    def __str__(self):
        return "".join([str(letter) for letter in self.letters])

    def __len__(self):
        return len(self.raw_word)

    @property
    def letters(self):
        return self._letters

    @property
    def guessed(self):
        return all([letter.guessed for letter in self.letters])
