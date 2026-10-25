# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

import pytest

from isort.exceptions import FormattingPluginDoesNotExist


def test_formatting_plugin_does_not_exist():
    formatter = "black"
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist(formatter)

    assert exc_info.value.formatter == formatter
    assert str(exc_info.value) == (
        f"Specified formatting plugin of {formatter} does not exist. "
    )
