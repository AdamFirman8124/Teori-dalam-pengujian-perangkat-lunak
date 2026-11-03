

# Generated at 2026-11-01 20:25:41.194236
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "This file was skipped for testing reasons"
    file_path = "/path/to/skipped/file.py"

    exception = FileSkipped(message=message, file_path=file_path)

    assert isinstance(exception, ISortError)
    assert str(exception) == message
    assert exception.file_path == file_path

# Generated at 2026-11-01 20:26:10.376978
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    from isort.exceptions import InvalidSettingsPath

    settings_path = "/nonexistent/path/to/settings"
    error = InvalidSettingsPath(settings_path)

    # Verify the settings_path attribute is stored correctly
    assert error.settings_path == settings_path

    # Verify the exception message contains the settings path
    assert settings_path in str(error)
    assert "settings_path" in str(error)
    assert "does not exist" in str(error)

    # Verify it is an instance of ISortError and Exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Verify with a different path
    another_path = "relative/settings.toml"
    error2 = InvalidSettingsPath(another_path)
    assert error2.settings_path == another_path
    assert another_path in str(error2)

# Generated at 2026-11-01 20:26:52.366915
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = str
    expected_kind = int
    exception = LiteralSortTypeMismatch(kind, expected_kind)
    assert exception.kind == kind
    assert exception.expected_kind == expected_kind
    assert str(exception) == (
        f"isort was told to sort a literal of type {expected_kind} "
        f"but was given a literal of type {kind}."
    )

# Generated at 2026-11-01 20:27:14.788522
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-11-01 20:27:46.737542
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-11-01 20:28:05.578769
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    # Test with a typical formatter name
    formatter = "black"
    exception = FormattingPluginDoesNotExist(formatter)

    assert exception.formatter == formatter
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
    assert str(exception) == f"Specified formatting plugin of {formatter} does not exist. "

    # Test with a different formatter name to ensure attribute is stored correctly
    formatter2 = "isort_formatting_plugin"
    exception2 = FormattingPluginDoesNotExist(formatter2)

    assert exception2.formatter == formatter2
    assert str(exception2) == f"Specified formatting plugin of {formatter2} does not exist. "

# Generated at 2026-11-01 20:28:23.194406
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "black"
    exception = FormattingPluginDoesNotExist(formatter)

    # Test that exception is a subclass of ISortError
    assert isinstance(exception, ISortError)

    # Test that the formatter attribute is set correctly
    assert exception.formatter == formatter

    # Test that the exception message is correct
    assert str(exception) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-11-01 20:28:46.036296
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    # Test that the constructor properly sets the file_path attribute
    file_path = "/path/to/some/file.py"
    exception = IntroducedSyntaxErrors(file_path)

    assert exception.file_path == file_path

    # Test that the exception message contains the file path
    expected_message = (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )
    assert str(exception) == expected_message
    assert file_path in str(exception)

    # Test that it is an instance of ISortError (and therefore Exception)
    from isort.exceptions import ISortError

    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

# Generated at 2026-11-01 20:29:08.658400
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():from isort.exceptions import IntroducedSyntaxErrors


# Generated at 2026-11-01 20:29:37.845843
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    # Test with a string filename
    filename = "example_file.py"
    exception = UnsupportedEncoding(filename)

    assert exception.filename == filename
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"

    # Test with a Path object filename
    path_filename = Path("another_file.py")
    path_exception = UnsupportedEncoding(path_filename)

    assert path_exception.filename == path_filename
    assert str(path_exception) == f"Unknown or unsupported encoding in {path_filename}"

    # Ensure it is an instance of the base isort exception
    assert isinstance(exception, ISortError)
    assert isinstance(path_exception, ISortError)

# Generated at 2026-11-01 20:30:10.055660
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    # Test with a string filename
    filename = "example.py"
    exc = UnsupportedEncoding(filename)

    assert exc.filename == filename
    assert str(exc) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(exc, UnsupportedEncoding)
    assert isinstance(exc, Exception)

    # Test with a Path filename
    path_filename = Path("some") / "module.py"
    exc = UnsupportedEncoding(path_filename)

    assert exc.filename == path_filename
    assert str(exc) == f"Unknown or unsupported encoding in {path_filename}"

# Generated at 2026-11-01 20:30:27.405750
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "x = 1\ny = 2\nz = 3"
    error = AssignmentsFormatMismatch(code=code)

    # Should be an instance of the base isort error class
    assert isinstance(error, ISortError)
    assert isinstance(error, AssignmentsFormatMismatch)

    # The code attribute should be stored exactly as provided
    assert error.code == code

    # The error message should include the offending code
    message = str(error)
    assert code in message

    # The error message should explain the formatting requirement
    assert "isort was told to sort a section of assignments" in message
    assert "Does not match isort's strict single line formatting requirement" in message
    assert "{variable_name} = {value}" in message

# Generated at 2026-11-01 20:30:57.722479
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    # Given
    kind = dict
    expected_kind = list

    # When
    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Then
    assert exception.kind == kind
    assert exception.expected_kind == expected_kind
    assert isinstance(exception, ISortError)
    assert (
        str(exception)
        == f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )

# Generated at 2026-11-01 20:31:17.583149
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list
    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)
    assert exception.kind == dict
    assert exception.expected_kind == list
    assert isinstance(exception, ISortError)
    assert (
        str(exception)
        == "isort was told to sort a literal of type <class 'list'> but was given "
        "a literal of type <class 'dict'>."
    )

# Generated at 2026-11-01 20:31:32.127790
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = str

# Generated at 2026-11-01 20:31:50.247142
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    from isort.exceptions import ISortError, IntroducedSyntaxErrors

    file_path = "/tmp/example_file.py"

    # Construct the exception
    exception = IntroducedSyntaxErrors(file_path)

    # Constructor should store the file_path attribute as given
    assert exception.file_path == file_path

    # Exception should inherit from the base isort exception
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Error message should contain the file path
    assert file_path in str(exception)
    assert str(exception) == (
        "isort introduced syntax errors when attempting to sort the imports "
        f"contained within {file_path}."
    )

    # Constructor should also work when called with keyword argument
    exception_kw = IntroducedSyntaxErrors(file_path="another_file.py")
    assert exception_kw.file_path == "another_file.py"
    assert "another_file.py" in str(exception_kw)

# Generated at 2026-11-01 20:32:27.114745
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert exception.kind == kind
    assert exception.expected_kind == expected_kind
    assert str(exception) == (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )
    assert isinstance(exception, Exception)

# Generated at 2026-11-01 20:32:48.215287
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = dict

# Generated at 2026-11-01 20:33:18.010213
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():from isort.exceptions import ISortError, LiteralSortTypeMismatch


# Generated at 2026-11-01 20:33:42.281528
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "multi_line_output": {"value": "3", "source": "/home/user/project/pyproject.toml"}
    }

    instance = UnsupportedSettings(unsupported_settings=unsupported_settings)

    # Constructor must store the settings dictionary unchanged
    assert instance.unsupported_settings == unsupported_settings

    # Error message should contain the header and the formatted option entry
    message = str(instance)
    assert "isort was provided settings that it doesn't support:" in message
    assert (
        "\t- multi_line_output = 3  (source: '/home/user/project/pyproject.toml')" in message
    )
    assert (
        "https://pycqa.github.io/isort/docs/configuration/options/" in message
    )

    # Multiple unsupported settings should each be rendered, in order, on separate lines
    multiple = {
        "line_length": {"value": "100", "source": "CLI"},
        "known_first_party": {"value": ["my_pkg"], "source": ".isort.cfg"},
    }
    instance_multi = UnsupportedSettings(unsupported_settings=multiple)
    msg_multi = str(instance_multi)

    assert "\t- line_length = 100  (source: 'CLI')" in msg_multi
    assert "\t- known_first_party = ['my_pkg']  (source: '.isort.cfg')" in msg_multi
    assert msg_multi.index("- line_length") < msg_multi.index("- known_first_party")

    # Sanity check: it is still an ISortError / Exception subclass instance
    assert isinstance(instance, ISortError)
    assert isinstance(instance, Exception)

# Generated at 2026-11-01 20:34:06.966175
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    from isort.exceptions import IntroducedSyntaxErrors, ISortError

    file_path = "example.py"
    exception = IntroducedSyntaxErrors(file_path)

    # Verify instance is created and inherits from ISortError
    assert isinstance(exception, IntroducedSyntaxErrors)
    assert isinstance(exception, ISortError)

    # Verify the file_path attribute is set correctly
    assert exception.file_path == file_path

    # Verify the constructed error message
    expected_message = (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        "example.py."
    )
    assert str(exception) == expected_message

# Generated at 2026-11-01 20:34:48.223344
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch, ISortError

    # Basic construction with type objects
    kind = int
    expected_kind = str
    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)
    assert exception.kind == int
    assert exception.expected_kind == str

    # Should still be an ISortError subclass instance
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Message should mention both types
    message = str(exception)
    assert "isort was told to sort a literal of type" in message
    assert str(expected_kind) in message
    assert str(kind) in message

    # Different type combinations
    exception2 = LiteralSortTypeMismatch(kind=dict, expected_kind=set)
    assert exception2.kind == dict
    assert exception2.expected_kind == set
    assert "dict" in str(exception2)
    assert str(set) in str(exception2)

    # Positional argument construction
    exception3 = LiteralSortTypeMismatch(list, tuple)
    assert exception3.kind == list
    assert exception3.expected_kind == tuple