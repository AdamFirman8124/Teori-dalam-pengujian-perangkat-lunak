# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_returns_expected_string():
    formatted = UnsupportedSettings._format_option(
        "some_option", "some_value", "config file"
    )
    assert formatted == "\t- some_option = some_value  (source: 'config file')"


def test_format_option_is_static_and_handles_non_string_values():
    formatted = UnsupportedSettings._format_option("line_length", 79, "cli")
    assert formatted == "\t- line_length = 79  (source: 'cli')"
    assert isinstance(UnsupportedSettings.__dict__["_format_option"], staticmethod)


def test_unsupported_settings_single_entry():
    settings = {"bad_option": {"value": "1", "source": "setup.cfg"}}
    error = UnsupportedSettings(settings)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.unsupported_settings == settings
    assert error.unsupported_settings is settings

    message = str(error)
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    assert "\t- bad_option = 1  (source: 'setup.cfg')" in message
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    ) in message
    assert message.endswith("options/.\n")


def test_unsupported_settings_multiple_entries_joined_with_newlines():
    settings = {
        "first_option": {"value": "a", "source": "cli"},
        "second_option": {"value": "b", "source": "pyproject.toml"},
    }
    error = UnsupportedSettings(settings)

    expected_errors = (
        "\t- first_option = a  (source: 'cli')\n"
        "\t- second_option = b  (source: 'pyproject.toml')"
    )
    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

    assert str(error) == expected_message
    assert error.unsupported_settings == settings
    assert list(error.unsupported_settings) == ["first_option", "second_option"]


def test_unsupported_settings_empty_dict():
    settings = {}
    error = UnsupportedSettings(settings)

    assert error.unsupported_settings == {}
    assert str(error) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_can_be_raised_and_caught(monkeypatch):
    settings = {"unknown": {"value": "x", "source": "runtime"}}

    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(settings)

    assert exc_info.value.unsupported_settings == settings
    assert "\t- unknown = x  (source: 'runtime')" in str(exc_info.value)

    with pytest.raises(ISortError):
        raise UnsupportedSettings(settings)

    # No global state is mutated by these tests; nothing to restore.
    assert "unknown" not in dir(UnsupportedSettings)
