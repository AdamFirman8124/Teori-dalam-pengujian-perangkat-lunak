# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist


def test_formatting_plugin_does_not_exist_message_and_attribute():
    formatter = "black"
    exc = FormattingPluginDoesNotExist(formatter)

    # Line 89: the base ISortError is initialized with the formatted message.
    assert str(exc) == (
        f"Specified formatting plugin of {formatter} does not exist. "
    )

    # Line 90: the formatter attribute is stored on the instance.
    assert exc.formatter == formatter

    # The exception should still behave as a proper Exception subclass.
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("my_formatter")

    assert exc_info.value.formatter == "my_formatter"
    assert str(exc_info.value) == (
        "Specified formatting plugin of my_formatter does not exist. "
    )
