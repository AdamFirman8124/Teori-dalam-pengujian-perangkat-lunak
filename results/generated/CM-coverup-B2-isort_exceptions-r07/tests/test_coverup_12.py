# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist, ISortError


def test_formatting_plugin_does_not_exist():
    """FormattingPluginDoesNotExist should store the formatter and build a message."""
    formatter_name = "black"

    exc = FormattingPluginDoesNotExist(formatter_name)

    # Line 89: the exception message is built via super().__init__
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert str(exc) == f"Specified formatting plugin of {formatter_name} does not exist. "
    assert formatter_name in str(exc)

    # Line 90: the formatter attribute is stored
    assert exc.formatter == formatter_name


def test_formatting_plugin_does_not_exist_raises_when_raised():
    """The exception should be raisable and catchable with its attributes intact."""
    formatter_name = "nonexistent_formatter"

    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist(formatter_name)

    assert exc_info.value.formatter == formatter_name
    assert str(exc_info.value) == (
        f"Specified formatting plugin of {formatter_name} does not exist. "
    )
