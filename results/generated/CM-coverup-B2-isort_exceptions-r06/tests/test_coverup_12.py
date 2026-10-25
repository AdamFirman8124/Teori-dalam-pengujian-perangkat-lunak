# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist, ISortError


def test_formatting_plugin_does_not_exist_init():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_formatting_plugin_does_not_exist_raised():
    formatter = "bad_plugin"
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist(formatter)
    assert exc_info.value.formatter == formatter
    assert str(exc_info.value) == f"Specified formatting plugin of {formatter} does not exist. "


def test_formatting_plugin_does_not_exist_empty_formatter():
    formatter = ""
    exc = FormattingPluginDoesNotExist(formatter)
    assert exc.formatter == formatter
    assert str(exc) == "Specified formatting plugin of  does not exist. "
