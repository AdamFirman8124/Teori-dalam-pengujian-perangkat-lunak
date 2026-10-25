

# Generated at 2026-10-24 02:23:02.690710
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "{invalid literal}"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )

# Generated at 2026-10-24 02:23:07.905731
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "foo: str = 'bar'"

    error = AssignmentsFormatMismatch(code)

    assert error.code == code
    assert str(error) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "foo: str = 'bar'\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 02:23:17.612446
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    # with str filename
    filename_str = "example.py"
    exc_str = UnsupportedEncoding(filename_str)

    assert isinstance(exc_str, ISortError)
    assert isinstance(exc_str, Exception)
    assert exc_str.filename == filename_str
    assert str(exc_str) == f"Unknown or unsupported encoding in {filename_str}"
    assert exc_str.args[0] == f"Unknown or unsupported encoding in {filename_str}"

    # with Path filename
    filename_path = Path("example.py")
    exc_path = UnsupportedEncoding(filename_path)

    assert exc_path.filename == filename_path
    assert str(exc_path) == f"Unknown or unsupported encoding in {filename_path}"

# Generated at 2026-10-24 02:23:23.360062
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist

    profile = "nonexistent_profile"

    exception = ProfileDoesNotExist(profile)

    # Attribute set by constructor
    assert exception.profile == profile

    # Message includes the profile name and available profiles
    message = str(exception)
    assert profile in message
    assert "does not exist" in message
    assert "black" in message  # 'black' is one of the built-in profiles
    assert ",".join(
        ["black", "django", "pycharm", "google", "open_stack", "plone", "attrs", "hug"]
    ) or "Available profiles" in message

    # It must be an isort base exception
    assert isinstance(exception, ISortError)

# Generated at 2026-10-24 02:23:29.506119
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "{'invalid':"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert str(error) == (
        "isort failed to parse the given literal {'invalid':. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of malformed node or string."
    )
    assert error.code == code
    assert error.original_error is original_error

# Generated at 2026-10-24 02:23:36.673749
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:23:42.100601
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:23:45.582369
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:23:58.866035
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"

    exception = FileSkipComment(file_path)

    assert isinstance(exception, FileSkipped)
    assert exception.file_path == file_path
    assert str(exception) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-24 02:24:10.875872
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"

    exception = FileSkipComment(file_path)

    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)
    assert exception.file_path == file_path
    assert str(exception) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-24 02:24:15.689549
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert error.formatter == formatter
    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 02:24:20.334560
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert error.formatter == formatter
    assert str(error) == (
        "Specified formatting plugin of unknown_formatter does not exist. "
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 02:24:24.907420
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, ISortError)
    assert error.formatter == formatter
    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "

# Generated at 2026-10-24 02:24:38.729076
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-24 02:24:41.698317
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():error = FileSkipComment("example.py")

# Generated at 2026-10-24 02:24:47.432593
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "path/to/file.py"

    error = ExistingSyntaxErrors(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "path/to/file.py."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 02:24:52.450205
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "
    assert error.formatter == formatter

# Generated at 2026-10-24 02:25:04.359627
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-24 02:25:05.762534
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():error = FileSkipComment("example.py")

# Generated at 2026-10-24 02:25:20.512304
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "unknown_setting": {"value": "42", "source": "pyproject.toml"},
        "other_setting": {"value": "True", "source": "command line"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    assert isinstance(exc, ISortError)
    assert exc.unsupported_settings == unsupported_settings
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_setting = 42  (source: 'pyproject.toml')\n"
        "\t- other_setting = True  (source: 'command line')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

# Generated at 2026-10-24 02:25:21.827423
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:25:26.282604
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:25:30.952987
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:25:32.386220
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:25:37.302656
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:25:41.500627
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:25:43.138353
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:25:47.234394
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

# Generated at 2026-10-24 02:25:50.921339
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:25:52.558929
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:25:56.870147
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(dict, list)

# Generated at 2026-10-24 02:26:00.885067
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:02.218349
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:26:06.179335
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:09.767018
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:11.402492
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:26:15.393498
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:18.775939
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:20.422833
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:26:24.201200
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:29.423501
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:30.854782
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:26:35.157908
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-24 02:26:39.151721
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:40.623192
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:26:44.066984
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:47.649152
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:49.260215
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:26:53.075706
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:56.571849
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:26:58.198613
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:02.398083
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:06.287666
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:07.934975
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:11.919926
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)

# Generated at 2026-10-24 02:27:15.502060
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:16.842407
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:20.521682
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:24.618072
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:26.256000
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:30.045218
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:34.140942
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:35.469277
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:39.363512
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:42.946706
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:44.585494
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:48.374607
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:53.289951
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:27:54.928459
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:27:58.511841
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:02.915412
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(dict, list)

# Generated at 2026-10-24 02:28:06.089765
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:28:12.336533
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:16.370213
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:17.969165
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:28:21.765731
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:25.836104
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:27.286981
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:28:30.908089
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:34.659324
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:36.093343
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:28:39.983701
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:43.363308
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:44.795409
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:28:48.688587
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:52.681890
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:28:54.114990
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:28:59.994553
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:03.671812
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:05.278031
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:29:09.373822
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:12.996044
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:14.596269
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:29:18.691618
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:22.581740
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:24.014496
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:29:28.008724
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:31.082109
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:32.515734
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:29:36.854299
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:40.606688
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)

# Generated at 2026-10-24 02:29:42.076293
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:29:45.930087
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:49.411425
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:50.845462
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:29:54.671984
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:57.716790
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:29:59.053418
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:02.109141
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:05.693709
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:07.001306
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:11.231093
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:15.380734
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:16.750753
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:21.476782
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:28.124192
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:29.591301
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:33.751344
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:37.027651
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:38.352485
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:42.151322
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:45.834675
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:47.276675
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:50.852333
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:54.232714
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:30:55.675728
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:30:59.760656
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:31:04.061429
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:31:05.802046
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:31:08.977505
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:31:13.891991
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:31:15.218885
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:31:18.918207
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:31:22.903229
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 02:31:24.580314
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 02:31:28.944502
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(dict, list)

# Generated at 2026-10-24 02:31:32.938924
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)