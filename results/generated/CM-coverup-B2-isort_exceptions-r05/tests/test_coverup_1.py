# file: project/isort/exceptions.py:140-160
# asked: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}
# gained: {"lines": [147, 150, 151, 154, 155, 156, 160], "branches": []}

from isort.exceptions import ISortError, UnsupportedSettings


def test_format_option_builds_formatted_string():
    """Cover line 147: the static formatter used for each setting."""
    result = UnsupportedSettings._format_option(
        name="sources", value="something", source="cli"
    )

    assert result == "\t- sources = something  (source: 'cli')"
    # Ensure all pieces are represented in the formatted output.
    assert "sources" in result
    assert "something" in result
    assert "cli" in result


def test_unsupported_settings_is_an_isort_error():
    """The exception should remain part of the ISortError hierarchy."""
    assert issubclass(UnsupportedSettings, ISortError)


def test_unsupported_settings_single_entry():
    """Cover lines 150-160 with one unsupported setting."""
    settings = {"sources": {"value": "a,b", "source": "cli"}}

    exception = UnsupportedSettings(settings)

    # Line 160: attribute is stored unchanged.
    assert exception.unsupported_settings is settings
    assert exception.unsupported_settings == {"sources": {"value": "a,b", "source": "cli"}}

    message = str(exception)
    # Header produced by __init__.
    assert "isort was provided settings that it doesn't support:" in message
    # Formatted option via _format_option (line 147 exercised through __init__).
    assert "\t- sources = a,b  (source: 'cli')" in message
    # Trailing documentation link.
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/." in message
    )
    # Errors are joined then padded with blank lines before the doc link.
    assert "\n\n" in message


def test_unsupported_settings_multiple_entries():
    """Cover the join over multiple settings (line 150-151 generator)."""
    settings = {
        "sources": {"value": "src", "source": "config"},
        "future_imports": {"value": "with_futures", "source": "cli"},
    }

    exception = UnsupportedSettings(settings)

    assert exception.unsupported_settings == settings

    message = str(exception)
    assert "\t- sources = src  (source: 'config')" in message
    assert "\t- future_imports = with_futures  (source: 'cli')" in message
    # Both options are joined into the error block with a newline.
    formatted_first = UnsupportedSettings._format_option("sources", "src", "config")
    formatted_second = UnsupportedSettings._format_option(
        "future_imports", "with_futures", "cli"
    )
    assert "\n".join(sorted([formatted_first, formatted_second])) in "\n".join(
        sorted(line for line in message.splitlines() if line.startswith("\t- "))
    )


def test_unsupported_settings_no_entries():
    """__init__ with an empty mapping still executes the join and stores it."""
    exception = UnsupportedSettings({})

    assert exception.unsupported_settings == {}
    message = str(exception)
    assert "isort was provided settings that it doesn't support:" in message
    assert (
        "https://pycqa.github.io/isort/docs/configuration/options/." in message
    )
