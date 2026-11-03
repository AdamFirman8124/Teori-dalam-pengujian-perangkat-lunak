# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist


def test_formatting_plugin_does_not_exist():
    """Test that FormattingPluginDoesNotExist sets the message and formatter attribute."""
    formatter_name = "black"
    exception = FormattingPluginDoesNotExist(formatter_name)

    # Line 89: super().__init__ with the formatted message
    assert str(exception) == (
        f"Specified formatting plugin of {formatter_name} does not exist. "
    )

    # Line 90: the formatter attribute is stored
    assert exception.formatter == formatter_name

    # The exception should still be an ISortError (and thus an Exception)
    from isort.exceptions import ISortError

    assert isinstance(exception, ISortError)
