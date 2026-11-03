# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_direct_call():
    """Directly exercise UnsupportedSettings._format_option (line 147)."""
    result = UnsupportedSettings._format_option("some_setting", "some_value", "cli")
    assert result == "\t- some_setting = some_value  (source: 'cli')"


def test_unsupported_settings_construction():
    """Exercise UnsupportedSettings.__init__ (lines 150-160) and verify postconditions."""
    unsupported_settings = {
        "ignored_sources": {"source": "cli", "value": "false"},
        "known_first_party": {"source": "/path/to/setup.cfg", "value": "5"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    # Postcondition: it is an isort error carrying the expected message.
    assert isinstance(exc, ISortError)
    expected_errors = "\n".join(
        f"\t- {name} = {option['value']}  (source: '{option['source']}')"
        for name, option in unsupported_settings.items()
    )
    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert str(exc) == expected_message

    # Postcondition: the offending settings are stored for later inspection.
    assert exc.unsupported_settings == unsupported_settings


def test_unsupported_settings_raised_and_caught():
    """Ensure the exception behaves correctly when raised and caught."""
    unsupported_settings = {"profile": {"source": "config", "value": "black-ish"}}

    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(unsupported_settings)

    assert excinfo.value.unsupported_settings == unsupported_settings
    message = str(excinfo.value)
    assert "isort was provided settings that it doesn't support:" in message
    assert "\t- profile = black-ish  (source: 'config')" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/." in message
