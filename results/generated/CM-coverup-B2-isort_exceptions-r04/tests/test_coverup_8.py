# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

import pytest

from isort.exceptions import ISortError, InvalidSettingsPath


def test_invalid_settings_path_initialization():
    """Test that InvalidSettingsPath correctly initializes its message and attributes.

    Covers the __init__ body: the super().__init__ call building the error
    message and the assignment of the settings_path attribute.
    """
    settings_path = "/nonexistent/settings/path"
    error = InvalidSettingsPath(settings_path)

    # Postcondition: the settings_path attribute is stored (line 21)
    assert error.settings_path == settings_path

    # Postcondition: the message passed to the base class includes the
    # settings path and the expected explanatory text (lines 16-17)
    message = str(error)
    assert settings_path in message
    assert "isort was told to use the settings_path" in message
    assert "as the base directory or file that represents the starting point of config file discovery" in message
    assert "but it does not exist." in message

    # Postcondition: it is a proper isort error / exception
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)


def test_invalid_settings_path_message_varies_with_input():
    """Ensure the message is dynamically built from the given settings path."""
    error_a = InvalidSettingsPath("path_a")
    error_b = InvalidSettingsPath("path_b")

    assert error_a.settings_path == "path_a"
    assert error_b.settings_path == "path_b"
    assert str(error_a) != str(error_b)
    assert "path_a" in str(error_a)
    assert "path_b" in str(error_b)
