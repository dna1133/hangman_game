from core.exceptions import WrongLetterException
from domain.word import Word


def validate_letter(letter: str) -> bool:
    return letter.isalpha() and len(letter) == 1


def guess_letter(letter: str, word: Word) -> bool:
    if not validate_letter(letter):
        raise WrongLetterException()
    guessed = False
    for i, value in enumerate(word.raw_word):
        if value == letter:
            word.letters[i].guessed = True
            guessed = True
    return guessed
