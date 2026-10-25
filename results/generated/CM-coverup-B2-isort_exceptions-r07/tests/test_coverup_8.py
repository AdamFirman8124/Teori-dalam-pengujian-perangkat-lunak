# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

from isort.exceptions import ISortError, InvalidSettingsPath


def test_invalid_settings_path_initialization() -> None:
    settings_path = "/path/that/does/not/exist"

    error = InvalidSettingsPath(settings_path)

    expected_message = (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert isinstance(error, ISortError)
    assert error.settings_path == settings_path
    assert str(error) == expected_message
    assert error.args == (expected_message,)
