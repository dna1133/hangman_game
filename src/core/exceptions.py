class BaseAppException(Exception): ...


class WordsFileNotFoundServiceExeption(BaseAppException):
    @property
    def message():
        return "File with words was not found!"


class WordsListNotFoundServiceExeption(BaseAppException):
    @property
    def message():
        return "Not list of the words!"


class WrongLetterException(BaseAppException):
    @property
    def message():
        return "Wrang letter!"
