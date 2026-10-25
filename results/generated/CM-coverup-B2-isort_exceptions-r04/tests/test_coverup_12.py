# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

from isort.exceptions import FormattingPluginDoesNotExist, ISortError


def test_formatting_plugin_does_not_exist_initializes_error():
    formatter = "custom_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, ISortError)
    assert error.formatter == formatter
    assert str(error) == (
        "Specified formatting plugin of custom_formatter does not exist. "
    )
