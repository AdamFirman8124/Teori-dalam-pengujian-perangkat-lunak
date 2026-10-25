# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

from isort.exceptions import FormattingPluginDoesNotExist


def test_formatting_plugin_does_not_exist_initializes_message_and_formatter():
    formatter = "missing_formatter"

    exception = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exception, Exception)
    assert exception.formatter == formatter
    assert str(exception) == (
        f"Specified formatting plugin of {formatter} does not exist. "
    )
