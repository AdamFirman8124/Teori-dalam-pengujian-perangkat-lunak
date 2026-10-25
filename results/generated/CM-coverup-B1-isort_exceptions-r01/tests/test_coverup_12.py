# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist, ISortError


def test_formatting_plugin_does_not_exist_init():
    exc = FormattingPluginDoesNotExist("black")

    assert exc.formatter == "black"
    assert str(exc) == "Specified formatting plugin of black does not exist. "
    assert exc.args == ("Specified formatting plugin of black does not exist. ",)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_formatting_plugin_does_not_exist_raised():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("yapf")

    assert exc_info.value.formatter == "yapf"
    assert str(exc_info.value) == "Specified formatting plugin of yapf does not exist. "


@pytest.mark.parametrize("formatter", ["autopep8", "custom-formatter", ""])
def test_formatting_plugin_does_not_exist_various_formatters(formatter):
    exc = FormattingPluginDoesNotExist(formatter)

    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
