# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

from isort.exceptions import UnsupportedSettings


def test_unsupported_settings_formats_and_stores_all_settings():
    unsupported_settings = {
        "source_one": {"value": "1", "source": "config file"},
        "source_two": {"value": "2", "source": "cli"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- source_one = 1  (source: 'config file')\n"
        "\t- source_two = 2  (source: 'cli')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert exc.unsupported_settings is unsupported_settings


def test_unsupported_settings_accepts_empty_mapping():
    unsupported_settings = {}

    exc = UnsupportedSettings(unsupported_settings)

    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert exc.unsupported_settings is unsupported_settings


def test_format_option_supports_non_string_values():
    assert UnsupportedSettings._format_option(
        "my_option", ["a", "b"], "runtime"
    ) == "\t- my_option = ['a', 'b']  (source: 'runtime')"
