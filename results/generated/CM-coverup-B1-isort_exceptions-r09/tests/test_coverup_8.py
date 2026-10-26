# file: project/isort/exceptions.py:12-21
# asked: {"lines": [16, 17, 21], "branches": []}
# gained: {"lines": [16, 17, 21], "branches": []}

from isort.exceptions import InvalidSettingsPath, ISortError


def test_invalid_settings_path_stores_path_and_message():
    settings_path = "/nonexistent/settings/path"
    exc = InvalidSettingsPath(settings_path)
    assert exc.settings_path == settings_path
    assert exc.args[0] == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert settings_path in str(exc)
    assert "settings_path" in str(exc)


def test_invalid_settings_path_inheritance():
    settings_path = "some/missing/dir"
    exc = InvalidSettingsPath(settings_path)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.settings_path == settings_path


def test_invalid_settings_path_raise_and_catch():
    settings_path = "/does/not/exist"
    try:
        raise InvalidSettingsPath(settings_path)
    except ISortError as exc:
        assert isinstance(exc, InvalidSettingsPath)
        assert exc.settings_path == settings_path
        assert settings_path in str(exc)
    else:
        raise AssertionError("InvalidSettingsPath was not raised")
