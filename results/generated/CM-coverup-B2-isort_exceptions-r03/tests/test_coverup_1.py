# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import UnsupportedSettings


def test_format_option_static_method():
    """Directly covers UnsupportedSettings._format_option (line 147)."""
    result = UnsupportedSettings._format_option("some_setting", "some_value", "some_source")
    assert result == "\t- some_setting = some_value  (source: 'some_source')"


def test_unsupported_settings_exception():
    """Covers UnsupportedSettings.__init__ (lines 150-160) with multiple settings."""
    unsupported_settings = {
        "ignored_setting": {"source": "cli", "value": "1"},
        "another_setting": {"source": "config file", "value": "2"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    # Postcondition: it is still a proper isort error / exception.
    assert isinstance(exc, Exception)

    # Postcondition: the unsupported settings are stored on the exception (line 160).
    assert exc.unsupported_settings == unsupported_settings

    message = str(exc)

    # Postcondition: header and footer from lines 154-159 are present.
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n" in message
    )

    # Postcondition: each setting is formatted via _format_option (lines 147, 150-151).
    assert "\t- ignored_setting = 1  (source: 'cli')" in message
    assert "\t- another_setting = 2  (source: 'config file')" in message

    # Postcondition: the formatted options are joined with newlines (line 150).
    assert (
        "\t- ignored_setting = 1  (source: 'cli')\n"
        "\t- another_setting = 2  (source: 'config file')" in message
    )


def test_unsupported_settings_single_entry():
    """Covers the generator expression (lines 150-151) with a single setting."""
    unsupported_settings = {"only_setting": {"source": "runtime", "value": True}}

    exc = UnsupportedSettings(unsupported_settings)

    assert exc.unsupported_settings == unsupported_settings
    message = str(exc)
    assert "\t- only_setting = True  (source: 'runtime')" in message
    assert "isort was provided settings that it doesn't support:" in message


def test_unsupported_settings_empty():
    """Edge case: an empty mapping still builds a valid message and stores the input."""
    exc = UnsupportedSettings({})

    assert exc.unsupported_settings == {}
    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    assert (
        "https://pycqa.github.io/isort/docs/configuration/options/." in message
    )


def test_unsupported_settings_raises_as_exception():
    """Verifies the exception can be raised and caught normally."""
    unsupported_settings = {"bad_setting": {"source": "cli", "value": "x"}}

    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(unsupported_settings)

    assert exc_info.value.unsupported_settings == unsupported_settings
    assert "\t- bad_setting = x  (source: 'cli')" in str(exc_info.value)
