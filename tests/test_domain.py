from domain.letter import Letter
from domain.word import Word
import pytest


test_letter_data = [
    ("a", True, "a"),
    ("a", False, "*"),
    ("z", True, "z"),
    ("f", False, "*"),
]


@pytest.mark.parametrize("letter, guessed, expected", test_letter_data)
def test_success_letter(letter, guessed, expected):
    letter = Letter(letter, guessed)
    assert isinstance(letter, Letter)
    assert str(letter) == expected


def test_fail_letter():
    with pytest.raises(AttributeError):
        letter = Letter(1, True)


def test_success_word(test_word="someword"):
    word = Word(raw_word=test_word)
    assert isinstance(word, Word)
    assert str(word) == "*" * len(test_word)

    word.letters[0].guessed = True
    assert str(word) == "s" + ("*" * (len(test_word) - 1))


def test_success_word_guessed():
    word = Word("sa")
    word.letters[0].guessed = True
    word.letters[1].guessed = True
    assert word.guessed == True
