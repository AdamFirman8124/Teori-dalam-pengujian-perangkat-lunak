# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_single():
    result = UnsupportedSettings._format_option(
        "my_option", value="my_value", source="pyproject.toml"
    )
    assert result == "\t- my_option = my_value  (source: 'pyproject.toml')"


def test_format_option_non_string_value():
    result = UnsupportedSettings._format_option("opt", 123, "setup.cfg")
    assert result == "\t- opt = 123  (source: 'setup.cfg')"
    result_none = UnsupportedSettings._format_option("opt2", None, "cli")
    assert result_none == "\t- opt2 = None  (source: 'cli')"


def test_init_single_unsupported_setting():
    unsupported = {"bad_option": {"value": "123", "source": "pyproject.toml"}}
    expected_errors = "\t- bad_option = 123  (source: 'pyproject.toml')"
    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    with pytest.raises(UnsupportedSettings) as exc_info:
        raise UnsupportedSettings(unsupported)
    exc = exc_info.value
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message
    assert exc.unsupported_settings == unsupported
    assert exc.unsupported_settings is unsupported


def test_init_multiple_unsupported_settings():
    unsupported = {
        "opt_a": {"value": "1", "source": "setup.cfg"},
        "opt_b": {"value": "True", "source": "cli"},
    }
    expected_errors = (
        "\t- opt_a = 1  (source: 'setup.cfg')\n"
        "\t- opt_b = True  (source: 'cli')"
    )
    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    exc = UnsupportedSettings(unsupported)
    assert isinstance(exc, ISortError)
    assert str(exc) == expected_message
    assert exc.unsupported_settings == unsupported
    # verify each formatted line is present
    assert "\t- opt_a = 1  (source: 'setup.cfg')" in str(exc)
    assert "\t- opt_b = True  (source: 'cli')" in str(exc)


def test_init_can_be_caught_as_isort_error():
    unsupported = {"x": {"value": "y", "source": "src"}}
    with pytest.raises(ISortError):
        raise UnsupportedSettings(unsupported)
