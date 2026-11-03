# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

import pytest

from isort.exceptions import InvalidSettingsPath, ISortError


def test_invalid_settings_path_initialization():
    """Executing lines 16-21: __init__ body of InvalidSettingsPath."""
    settings_path = "/nonexistent/settings/path"

    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)

    exception = exc_info.value

    # Line 16-20: super().__init__(...) was called with the expected message
    expected_message = (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert str(exception) == expected_message
    assert settings_path in str(exception)

    # Line 21: self.settings_path was assigned
    assert exception.settings_path == settings_path

    # Postcondition: inheritance from ISortError (and therefore Exception)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
