# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

from isort.exceptions import FormattingPluginDoesNotExist, ISortError
import pytest


def test_formatting_plugin_does_not_exist_init():
    formatter = "nonexistent_formatter_xyz"
    exc = FormattingPluginDoesNotExist(formatter)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "


def test_formatting_plugin_does_not_exist_raised():
    formatter = "missing_plugin"
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist(formatter)
    assert exc_info.value.formatter == formatter
    assert str(exc_info.value) == f"Specified formatting plugin of {formatter} does not exist. "


def test_formatting_plugin_does_not_exist_empty_string():
    formatter = ""
    exc = FormattingPluginDoesNotExist(formatter)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
