# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

from isort.exceptions import UnsupportedSettings


def test_unsupported_settings_formats_and_preserves_settings() -> None:
    settings = {
        "unknown_option": {"value": "enabled", "source": "test.ini"},
        "removed_option": {"value": "42", "source": "command line"},
    }

    error = UnsupportedSettings(settings)

    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = enabled  (source: 'test.ini')\n"
        "\t- removed_option = 42  (source: 'command line')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

    assert UnsupportedSettings._format_option(
        "unknown_option", "enabled", "test.ini"
    ) == "\t- unknown_option = enabled  (source: 'test.ini')"
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.unsupported_settings is settings
