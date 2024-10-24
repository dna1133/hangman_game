from app.use_cases import guess_letter
from core.exceptions import WrongLetterException
from domain.word import Word
import pytest


def test_success_guess_letter_usecase():
    letter, word = "р", Word("пожар")
    assert guess_letter(letter, word) == True
    assert str(word) == "****р"
    assert str(word.letters[-1]) == "р"


def test_fail_guess_letter_usecase():
    with pytest.raises(WrongLetterException):
        letter, word = "er", Word("пожар")
        guess_letter(letter, word)
