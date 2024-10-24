from core.exceptions import WordsListNotFoundServiceExeption
import pytest
from services.services import random_word, words_reader


def test_success_words_reader(path: str = r"static\words.txt"):
    words = words_reader(path)
    assert isinstance(words, list)
    assert words[0] == "абажур"
    assert words[-1] == "ящурка"


def test_success_random_word():
    words = words_reader(path=r"static\words.txt")
    word = random_word(words)
    assert isinstance(word, str)
    assert word in words


def test_fail_random_word():
    with pytest.raises(WordsListNotFoundServiceExeption):
        random_word(1)
