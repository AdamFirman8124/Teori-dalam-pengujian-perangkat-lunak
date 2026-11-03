# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_returns_formatted_string():
    result = UnsupportedSettings._format_option(
        name="profile", value="black", source="cli"
    )
    assert result == "\t- profile = black  (source: 'cli')"


def test_format_option_handles_non_string_value():
    result = UnsupportedSettings._format_option(
        name="line_length", value=88, source="/home/user/pyproject.toml"
    )
    assert result == "\t- line_length = 88  (source: '/home/user/pyproject.toml')"


def test_unsupported_settings_no_settings():
    settings: dict = {}
    exc = UnsupportedSettings(settings)

    # The unsupported settings are stored verbatim on the instance.
    assert exc.unsupported_settings is settings

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_single_setting():
    settings = {"profile": {"value": "black", "source": "cli"}}
    exc = UnsupportedSettings(settings)

    assert exc.unsupported_settings is settings
    assert exc.unsupported_settings == settings

    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- profile = black  (source: 'cli')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_multiple_settings():
    settings = {
        "profile": {"value": "black", "source": "cli"},
        "line_length": {"value": 100, "source": "/home/user/.isort.cfg"},
        "known_first_party": {"value": ["foo", "bar"], "source": "pyproject.toml"},
    }
    exc = UnsupportedSettings(settings)

    assert exc.unsupported_settings is settings

    # Insertion order is preserved, so the formatted options appear in order.
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- profile = black  (source: 'cli')\n"
        "\t- line_length = 100  (source: '/home/user/.isort.cfg')\n"
        "\t- known_first_party = ['foo', 'bar']  (source: 'pyproject.toml')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_can_be_raised_and_caught():
    settings = {"profile": {"value": "black", "source": "cli"}}
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(settings)

    assert excinfo.value.unsupported_settings is settings
    assert "\t- profile = black  (source: 'cli')" in str(excinfo.value)
    assert "isort was provided settings that it doesn't support" in str(excinfo.value)
