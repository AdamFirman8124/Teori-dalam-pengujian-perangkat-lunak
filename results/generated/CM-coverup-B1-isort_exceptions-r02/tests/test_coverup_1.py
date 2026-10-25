# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_directly():
    result = UnsupportedSettings._format_option("my_option", "my_value", "my_source")
    assert result == "\t- my_option = my_value  (source: 'my_source')"


def test_format_option_non_string_value():
    result = UnsupportedSettings._format_option("opt", 123, "cli")
    assert result == "\t- opt = 123  (source: 'cli')"


def test_init_single_unsupported_setting():
    payload = {"bad_option": {"value": "bad_value", "source": "pyproject.toml"}}
    exc = UnsupportedSettings(payload)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.unsupported_settings is payload
    expected_line = "\t- bad_option = bad_value  (source: 'pyproject.toml')"
    assert expected_line in str(exc)
    assert str(exc).startswith("isort was provided settings that it doesn't support:\n\n")
    assert "https://pycqa.github.io/isort/docs/configuration/options/." in str(exc)
    assert exc.args[0] == (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_line}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_init_multiple_unsupported_settings():
    payload = {
        "opt_a": {"value": "1", "source": "cli"},
        "opt_b": {"value": "2", "source": "config"},
    }
    exc = UnsupportedSettings(payload)
    assert exc.unsupported_settings == payload
    expected_errors = (
        "\t- opt_a = 1  (source: 'cli')\n"
        "\t- opt_b = 2  (source: 'config')"
    )
    assert expected_errors in str(exc)
    assert exc.args[0] == (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_init_empty_unsupported_settings():
    payload = {}
    exc = UnsupportedSettings(payload)
    assert exc.unsupported_settings == {}
    assert exc.args[0] == (
        "isort was provided settings that it doesn't support:\n\n"
        "\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


def test_raised_and_caught_as_isort_error():
    payload = {"x": {"value": "y", "source": "s"}}
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(payload)
    assert exc_info.value.unsupported_settings == payload
    assert isinstance(exc_info.value, ISortError)
    assert "\t- x = y  (source: 's')" in str(exc_info.value)
