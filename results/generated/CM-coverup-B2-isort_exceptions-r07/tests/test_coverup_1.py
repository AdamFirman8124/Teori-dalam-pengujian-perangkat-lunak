# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_single():
    result = UnsupportedSettings._format_option("my_opt", "my_value", "my_source")
    assert result == "\t- my_opt = my_value  (source: 'my_source')"


def test_format_option_various_value_types():
    assert UnsupportedSettings._format_option("a", 123, "cli") == "\t- a = 123  (source: 'cli')"
    assert UnsupportedSettings._format_option("b", True, "config") == "\t- b = True  (source: 'config')"
    assert UnsupportedSettings._format_option("c", None, "runtime") == "\t- c = None  (source: 'runtime')"


def test_init_single_unsupported_setting():
    unsupported = {"bad_option": {"value": "bad_value", "source": "pyproject.toml"}}
    exc = UnsupportedSettings(unsupported)
    assert exc.unsupported_settings == unsupported
    assert exc.unsupported_settings is unsupported
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    assert "\t- bad_option = bad_value  (source: 'pyproject.toml')" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/" in message
    assert exc.args[0] == message


def test_init_multiple_unsupported_settings():
    unsupported = {
        "opt_one": {"value": "1", "source": "cli"},
        "opt_two": {"value": "2", "source:": "config"},
    }
    # fix typo in second source key by rebuilding correctly
    unsupported = {
        "opt_one": {"value": "1", "source": "cli"},
        "opt_two": {"value": "2", "source": "config"},
    }
    exc = UnsupportedSettings(unsupported)
    assert exc.unsupported_settings == unsupported
    message = str(exc)
    assert "\t- opt_one = 1  (source: 'cli')" in message
    assert "\t- opt_two = 2  (source: 'config')" in message
    assert "\n" in message
    # errors joined by newline
    assert message.index("opt_one") < message.index("opt_two")


def test_init_empty_unsupported_settings():
    unsupported = {}
    exc = UnsupportedSettings(unsupported)
    assert exc.unsupported_settings == {}
    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/" in message


def test_raised_as_isort_error():
    unsupported = {"x": {"value": "y", "source": "z"}}
    try:
        raise UnsupportedSettings(unsupported)
    except UnsupportedSettings as e:
        assert e.unsupported_settings == unsupported
        assert "\t- x = y  (source: 'z')" in str(e)
    else:
        assert False, "UnsupportedSettings was not raised"

    try:
        raise UnsupportedSettings(unsupported)
    except ISortError as e:
        assert isinstance(e, UnsupportedSettings)
    else:
        assert False, "UnsupportedSettings should be catchable as ISortError"
