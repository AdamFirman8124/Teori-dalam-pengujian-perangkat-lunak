# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

import pytest

from isort.exceptions import InvalidSettingsPath, ISortError


def test_invalid_settings_path_message_and_attribute():
    """Executing InvalidSettingsPath.__init__ (lines 16-21) should build the
    error message from the given settings path and store it as an attribute."""
    settings_path = "/nonexistent/settings/path"
    exc = InvalidSettingsPath(settings_path)

    # Line 21: the settings_path attribute is set on the instance.
    assert exc.settings_path == settings_path

    # Lines 16-18: the message passed to super().__init__ includes the path.
    assert settings_path in str(exc)
    assert (
        str(exc)
        == f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )

    # Postconditions: inheritance chain is intact and it behaves as an exception.
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    with pytest.raises(InvalidSettingsPath):
        raise exc
