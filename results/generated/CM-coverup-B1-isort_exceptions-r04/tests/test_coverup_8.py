# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

import pytest

from isort.exceptions import InvalidSettingsPath


def test_invalid_settings_path_message_and_attribute():
    settings_path = "/nonexistent/settings/path"
    with pytest.raises(InvalidSettingsPath) as exc_info:
        raise InvalidSettingsPath(settings_path)

    exception = exc_info.value
    assert exception.settings_path == settings_path
    assert (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    ) == str(exception)
