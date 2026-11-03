

# Generated at 2026-11-02 12:51:07.702948
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    from isort.exceptions import LiteralParsingFailure

    code = "[1, 2, 3"
    original_error = SyntaxError("unexpected EOF while parsing")

    exception = LiteralParsingFailure(code, original_error)

    assert exception.code == code
    assert exception.original_error is original_error
    assert isinstance(exception, Exception)
    assert code in str(exception)
    assert str(original_error) in str(exception)

# Generated at 2026-11-02 12:52:23.646176
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "atomic": {"value": "true", "source": "$HOME/.isort.cfg"},
        "length_sort": {"value": True, "source": "CLI"},
    }
    exception = UnsupportedSettings(unsupported_settings)

    assert exception.unsupported_settings == unsupported_settings
    assert isinstance(exception, UnsupportedSettings)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
    assert str(exception) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- atomic = true  (source: '$HOME/.isort.cfg')\n"
        "\t- length_sort = True  (source: 'CLI')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

# Generated at 2026-11-02 12:53:35.874624
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    # Test with a string filename
    filename = "example.py"
    exception = UnsupportedEncoding(filename)

    assert exception.filename == filename
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(exception, ISortError)

    # Test with a Path object filename
    from pathlib import Path

    path_filename = Path("some") / "file.py"
    path_exception = UnsupportedEncoding(path_filename)

    assert path_exception.filename == path_filename
    assert str(path_exception) == f"Unknown or unsupported encoding in {path_filename}"
    assert isinstance(path_exception, UnsupportedEncoding)

# Generated at 2026-11-02 12:54:36.551284
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "known_first_party": {"value": "False", "source": "CLI"},
        "lines_after_imports": {"value": "2", "source": "pyproject.toml"},
    }

    exception = UnsupportedSettings(unsupported_settings)

    assert isinstance(exception, ISortError)
    assert exception.unsupported_settings == unsupported_settings

    message = str(exception)
    assert "isort was provided settings that it doesn't support" in message
    assert "- known_first_party = False  (source: 'CLI')" in message
    assert "- lines_after_imports = 2  (source: 'pyproject.toml')" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/" in message

# Generated at 2026-11-02 12:55:49.813716
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/path/to/nonexistent/settings"
    error = InvalidSettingsPath(settings_path)
    
    # Check that the exception is an instance of ISortError and InvalidSettingsPath
    assert isinstance(error, ISortError)
    assert isinstance(error, InvalidSettingsPath)
    assert isinstance(error, Exception)
    
    # Check that the settings_path attribute is set correctly
    assert error.settings_path == settings_path
    
    # Check that the error message contains the settings path
    assert settings_path in str(error)
    assert "settings_path" in str(error)
    assert "does not exist" in str(error)

# Generated at 2026-11-02 12:57:02.210680
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    # Test that the constructor correctly sets kind and expected_kind attributes
    kind = dict
    expected_kind = list
    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert exception.kind == kind
    assert exception.expected_kind == expected_kind

    # Test that the exception message contains the correct type information
    assert "isort was told to sort a literal of type" in str(exception)
    assert str(expected_kind) in str(exception)
    assert str(kind) in str(exception)

    # Test inheritance from ISortError
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)


def test_LiteralSortTypeMismatch_with_different_types():
    # Test constructor with a different pair of types
    kind = str
    expected_kind = set
    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert exception.kind is str
    assert exception.expected_kind is set
    assert f"a literal of type {kind}" in str(exception)
    assert f"literal of type {expected_kind}" in str(exception)