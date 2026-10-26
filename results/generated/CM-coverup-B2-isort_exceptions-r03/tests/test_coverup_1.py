# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_unsupported_settings_single_option():
    unsupported_settings = {
        "unknown_option": {"value": "true", "source": "CLI"},
    }

    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(unsupported_settings)

    exc = exc_info.value
    assert isinstance(exc, ISortError)
    assert exc.unsupported_settings is unsupported_settings
    assert exc.unsupported_settings == {
        "unknown_option": {"value": "true", "source": "CLI"},
    }
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = true  (source: 'CLI')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_multiple_options():
    unsupported_settings = {
        "bad_setting": {"value": "42", "source": "/path/to/pyproject.toml"},
        "other_setting": {"value": "['a', 'b']", "source": "runtime"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    assert exc.unsupported_settings == unsupported_settings
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- bad_setting = 42  (source: '/path/to/pyproject.toml')\n"
        "\t- other_setting = ['a', 'b']  (source: 'runtime')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_empty():
    unsupported_settings = {}

    exc = UnsupportedSettings(unsupported_settings)

    assert exc.unsupported_settings == {}
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_unsupported_settings_format_option():
    assert UnsupportedSettings._format_option("my_option", "my_value", "CLI") == (
        "\t- my_option = my_value  (source: 'CLI')"
    )
    assert UnsupportedSettings._format_option("count", 3, "config file") == (
        "\t- count = 3  (source: 'config file')"
    )
    assert UnsupportedSettings._format_option("items", ["a", "b"], "runtime") == (
        "\t- items = ['a', 'b']  (source: 'runtime')"
    )
