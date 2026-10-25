# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

from isort.exceptions import FormattingPluginDoesNotExist, ISortError


def test_formatting_plugin_does_not_exist_initializes_message_and_formatter():
    formatter = "missing_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, ISortError)
    assert str(error) == (
        "Specified formatting plugin of missing_formatter does not exist. "
    )
    assert error.formatter == formatter
