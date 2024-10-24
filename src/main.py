from app.game import Game
from interface.presenter import Presenter
from ui.view import CLIView


def start_app() -> None:
    game = Game()
    ui = CLIView()
    presenter = Presenter(game, ui)
    presenter.start_game()


if __name__ == "__main__":
    start_app()
