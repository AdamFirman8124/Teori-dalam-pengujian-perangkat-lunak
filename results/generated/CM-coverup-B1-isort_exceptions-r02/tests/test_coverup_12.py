# file: project/isort/exceptions.py:85-90
# asked: {"lines": [89, 90], "branches": []}
# gained: {"lines": [89, 90], "branches": []}

from isort.exceptions import FormattingPluginDoesNotExist


def test_formatting_plugin_does_not_exist_initialization():
    formatter = "custom_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, Exception)
    assert error.formatter == formatter
    assert str(error) == (
        "Specified formatting plugin of custom_formatter does not exist. "
    )
    assert error.args == (
        "Specified formatting plugin of custom_formatter does not exist. ",
    )
