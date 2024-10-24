import random

from core.exceptions import WordsListNotFoundServiceExeption


def words_reader(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as file:
        words = [word.strip().lower() for word in file]
    return words


def random_word(words: list) -> str:
    try:
        return random.choice(words)
    except TypeError as e:
        raise WordsListNotFoundServiceExeption()
