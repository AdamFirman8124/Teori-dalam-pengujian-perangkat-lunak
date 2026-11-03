# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

"""Tests for isort.exceptions.UnsupportedSettings covering lines 147, 150-160."""

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_static_method():
    """Covers line 147: _format_option returns the correctly formatted string."""
    result = UnsupportedSettings._format_option("my_setting", "some_value", "cli")
    assert result == "\t- my_setting = some_value  (source: 'cli')"

    # Also verify formatting of non-string values (Any) and sources with spaces.
    result_int = UnsupportedSettings._format_option("line_length", 88, "config file")
    assert result_int == "\t- line_length = 88  (source: 'config file')"


def test_unsupported_settings_multiple_entries():
    """Covers lines 150-160: __init__ joins formatted options, calls super().__init__
    with the full message, and stores the unsupported settings."""
    unsupported_settings = {
        "unsupported_option": {"value": 42, "source": "cli"},
        "another_bad_option": {"value": "x", "source": "config file"},
    }
    exception = UnsupportedSettings(unsupported_settings)

    # Postcondition: the settings are stored unchanged on the instance.
    assert exception.unsupported_settings == unsupported_settings

    # Postcondition: it is still an ISortError.
    assert isinstance(exception, ISortError)

    # Postcondition: the message contains the header, each formatted option,
    # and the documentation link.
    message = str(exception)
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    assert "\t- unsupported_option = 42  (source: 'cli')" in message
    assert "\t- another_bad_option = x  (source: 'config file')" in message
    # The two options must be joined by a newline.
    assert (
        "\t- unsupported_option = 42  (source: 'cli')\n"
        "\t- another_bad_option = x  (source: 'config file')"
    ) in message
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    ) in message


def test_unsupported_settings_empty_dict():
    """Covers lines 150-160 with an empty mapping (join over empty generator)."""
    exception = UnsupportedSettings({})

    assert exception.unsupported_settings == {}
    message = str(exception)
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    ) in message


def test_unsupported_settings_raise_and_catch():
    """Covers lines 150-160 via the normal raise/catch flow."""
    settings = {"bad_setting": {"value": True, "source": "runtime"}}
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(settings)

    assert exc_info.value.unsupported_settings == settings
    assert "\t- bad_setting = True  (source: 'runtime')" in str(exc_info.value)
