# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

from isort.exceptions import InvalidSettingsPath


def test_invalid_settings_path_initialization() -> None:
    settings_path = "/nonexistent/isort/settings"

    error = InvalidSettingsPath(settings_path)

    assert error.settings_path == settings_path
    assert str(error) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
