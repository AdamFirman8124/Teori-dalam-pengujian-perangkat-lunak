# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import UnsupportedSettings


def test_format_option_static_method():
    """Cover line 147: the _format_option return statement."""
    formatted = UnsupportedSettings._format_option(
        "my_setting", value="some_value", source="/path/to/config"
    )
    assert formatted == "\t- my_setting = some_value  (source: '/path/to/config')"

    # Also verify formatting with non-string values (Any).
    assert (
        UnsupportedSettings._format_option("num", value=42, source="cli")
        == "\t- num = 42  (source: 'cli')"
    )


def test_unsupported_settings_init_attributes_and_message():
    """Cover lines 150-160: UnsupportedSettings.__init__ builds the message
    and stores the unsupported_settings attribute."""
    unsupported = {
        "my_setting": {"value": "some_value", "source": "/path/to/config"},
        "other_setting": {"value": 42, "source": "cli"},
    }
    exc = UnsupportedSettings(unsupported)

    # Postcondition: the settings are stored unmodified.
    assert exc.unsupported_settings == unsupported
    assert exc.unsupported_settings is not None

    # Postcondition: it is a valid Exception subclass.
    assert isinstance(exc, Exception)

    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    # Each unsupported option must be formatted and joined with newlines.
    assert "\t- my_setting = some_value  (source: '/path/to/config')" in message
    assert "\t- other_setting = 42  (source: 'cli')" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/." in message


def test_unsupported_settings_exact_message():
    """Verify the exact full message for a single setting (dicts preserve
    insertion order, so a single entry gives a deterministic message)."""
    exc = UnsupportedSettings(
        {"bad_option": {"value": True, "source": "environment"}}
    )
    expected = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- bad_option = True  (source: 'environment')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert str(exc) == expected


def test_unsupported_settings_can_be_raised():
    """The exception works with pytest.raises and keeps its payload."""
    settings = {"a": {"value": "1", "source": "s"}}
    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(settings)

    assert excinfo.value.unsupported_settings == settings
    assert str(excinfo.value).startswith(
        "isort was provided settings that it doesn't support:"
    )


def test_unsupported_settings_empty_dict():
    """Edge case: no unsupported settings still produces a valid message."""
    exc = UnsupportedSettings({})
    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    assert exc.unsupported_settings == {}
    assert "\t- " not in message
