# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_static_method():
    """Covers line 147: UnsupportedSettings._format_option return statement."""
    formatted = UnsupportedSettings._format_option(
        "my_setting", "some_value", "pyproject.toml"
    )
    assert formatted == "\t- my_setting = some_value  (source: 'pyproject.toml')"


def test_unsupported_settings_raises_with_formatted_message():
    """Covers lines 150-160: UnsupportedSettings.__init__ with settings present.

    Exercises the generator expression (lines 150-151), the super().__init__
    call building the message (lines 154-159) and the attribute assignment
    (line 160).
    """
    unsupported_settings = {
        "source": {"value": "1", "source": "/path/to/pyproject.toml"},
        "another_setting": {"value": 2, "source": "CLI"},
    }

    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(unsupported_settings)

    error = exc_info.value

    # Postcondition: it is an isort error and it keeps the offending settings.
    assert isinstance(error, ISortError)
    assert error.unsupported_settings == unsupported_settings

    message = str(error)
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    # Each unsupported setting is formatted on its own line, joined by newlines.
    assert (
        "\t- source = 1  (source: '/path/to/pyproject.toml')\n"
        "\t- another_setting = 2  (source: 'CLI')" in message
    )
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n" in message
    )


def test_unsupported_settings_empty_dict():
    """Covers the branch of the generator expression in __init__ with no items."""
    error = UnsupportedSettings({})

    assert error.unsupported_settings == {}
    message = str(error)
    assert message.startswith(
        "isort was provided settings that it doesn't support:\n\n\n\n"
    )
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n" in message
    )
