# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

"""Tests for isort.exceptions.UnsupportedSettings.

These tests execute the previously uncovered lines 147 and 150-160:
the ``_format_option`` helper and the full body of
``UnsupportedSettings.__init__``.

No global state is touched (the exception only builds a message and
stores its argument), so no monkeypatching/cleanup is required to
avoid state pollution.
"""

import pytest

from isort.exceptions import UnsupportedSettings


def test_unsupported_settings_message_and_stored_settings():
    unsupported_settings = {
        "unknown_option": {"value": "bad_value", "source": "pyproject.toml"},
        "another_unknown": {"value": 42, "source": "setup.cfg"},
    }

    exception = UnsupportedSettings(unsupported_settings)
    message = str(exception)

    # Every unsupported option must be formatted into the message
    # (exercises _format_option via the generator in __init__).
    assert "\t- unknown_option = bad_value  (source: 'pyproject.toml')" in message
    assert "\t- another_unknown = 42  (source: 'setup.cfg')" in message

    # Header and footer of the message.
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    ) in message

    # The original mapping must be stored on the instance.
    assert exception.unsupported_settings == unsupported_settings


def test_unsupported_settings_single_setting_exact_message():
    settings = {"only_option": {"value": "x", "source": "cli"}}
    exception = UnsupportedSettings(settings)

    assert str(exception) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- only_option = x  (source: 'cli')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert exception.unsupported_settings == settings


def test_unsupported_settings_empty_settings():
    exception = UnsupportedSettings({})

    assert exception.unsupported_settings == {}
    assert str(exception) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_raise_and_catch():
    settings = {"src_only_option": {"value": "v", "source": "cli"}}

    with pytest.raises(UnsupportedSettings) as excinfo:
        raise UnsupportedSettings(settings)

    assert excinfo.value.unsupported_settings == settings
    assert "\t- src_only_option = v  (source: 'cli')" in str(excinfo.value)


def test_format_option_static_method():
    assert (
        UnsupportedSettings._format_option("option_name", "option_value", "option_source")
        == "\t- option_name = option_value  (source: 'option_source')"
    )
