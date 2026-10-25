# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

from isort.exceptions import UnsupportedSettings


def test_unsupported_settings_format_option() -> None:
    assert (
        UnsupportedSettings._format_option("unknown_option", True, "command line")
        == "\t- unknown_option = True  (source: 'command line')"
    )


def test_unsupported_settings_initialization() -> None:
    unsupported_settings = {
        "unknown_option": {"value": "enabled", "source": "command line"},
        "obsolete_option": {"value": "legacy", "source": "config file"},
    }

    error = UnsupportedSettings(unsupported_settings)

    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = enabled  (source: 'command line')\n"
        "\t- obsolete_option = legacy  (source: 'config file')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.unsupported_settings is unsupported_settings
