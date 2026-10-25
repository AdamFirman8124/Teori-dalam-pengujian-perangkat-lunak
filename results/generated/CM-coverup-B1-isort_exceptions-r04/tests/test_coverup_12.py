# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist


def test_formatting_plugin_does_not_exist_message_and_attribute():
    formatter = "black"
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist(formatter)

    # Line 89: message built via super().__init__
    assert str(exc_info.value) == (
        f"Specified formatting plugin of {formatter} does not exist. "
    )
    # Line 90: attribute assignment
    assert exc_info.value.formatter == formatter


def test_formatting_plugin_does_not_exist_is_isort_error():
    from isort.exceptions import ISortError

    exc = FormattingPluginDoesNotExist("isort")
    assert isinstance(exc, ISortError)
    assert exc.formatter == "isort"
