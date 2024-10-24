from core.configs.common_config import AMOUNT_OF_ATTEMPS
import pytest
from ui.view import CLIView

view = CLIView()


def test_view():
    assert view.stats["attemp"] == AMOUNT_OF_ATTEMPS
