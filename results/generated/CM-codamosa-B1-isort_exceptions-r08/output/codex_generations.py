

# Generated at 2026-10-24 06:19:37.739527
# Unit test for constructor of class FileSkipped
def test_FileSkipped():import unittest


class TestFileSkipped(unittest.TestCase):
    """Unit test for constructor of class FileSkipped"""

    def test_constructor(self):
        message = "test message: file skipped"
        file_path = "/path/to/skipped_file.py"

        exception = FileSkipped(message, file_path)

        # Constructor stores the file path and passes message to base Exception
        self.assertEqual(exception.file_path, file_path)
        self.assertEqual(str(exception), message)

    def test_inheritance(self):
        # FileSkipped must inherit from ISortError (and therefore Exception)
        self.assertTrue(issubclass(FileSkipped, ISortError))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-10-24 06:19:45.364120
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = "example_module"
    section = "THIRDPARTY"

    error = MissingSection(import_module, section)

    expected_message = (
        "Found example_module import while parsing, but THIRDPARTY was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.args == (expected_message,)

# Generated at 2026-10-24 06:19:51.060638
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "unknown_option": {
            "value": "some_value",
            "source": "test_config",
        }
    }

    error = UnsupportedSettings(unsupported_settings)

    assert error.unsupported_settings == unsupported_settings
    assert str(error) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = some_value  (source: 'test_config')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert error.args == (str(error),)

# Generated at 2026-10-24 06:19:52.494199
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    # Arrange
    profile = "no_such_profile"

    # Act
    exc = ProfileDoesNotExist(profile)

    # Assert - type hierarchy
    assert isinstance(exc, ProfileDoesNotExist)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    # Assert - stored attribute preserves input exactly
    assert exc.profile == profile

    # Assert - message passed to base Exception
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert exc.args[0] == expected_message
    assert str(exc) == expected_message

    # Assert - usable with raise / except ISortError
    try:
        raise ProfileDoesNotExist(profile)
    except ISortError as caught:
        assert caught.profile == profile
        assert str(caught) == expected_message
    else:
        assert False, "ProfileDoesNotExist was not raised"

# Generated at 2026-10-24 06:19:58.126355
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("nonexistent")

# Generated at 2026-10-24 06:20:03.864148
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    error = FileSkipSetting(file_path)

    expected_message = (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

    assert error.file_path == file_path
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 06:20:05.302949
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "bad_syntax.py"

    error = ExistingSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "bad_syntax.py."
    )

    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)
    assert exc_info.value.file_path == file_path

# Generated at 2026-10-24 06:20:06.728179
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "bad_syntax.py"

    error = ExistingSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "bad_syntax.py."
    )

    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)
    assert exc_info.value.file_path == file_path

# Generated at 2026-10-24 06:20:31.713551
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"
    exception = FileSkipComment(file_path)

    # Inherits from FileSkipped -> ISortError -> Exception
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)

    # file_path attribute is stored correctly
    assert exception.file_path == file_path

    # Message mentions the file and the skip comment reason
    message = str(exception)
    assert file_path in message
    assert "file skip comment" in message

# Generated at 2026-10-24 06:20:52.809097
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"

    error = FileSkipComment(file_path)

    assert error.file_path == file_path
    assert str(error) == "example.py contains an file skip comment and was skipped."
    assert error.args == ("example.py contains an file skip comment and was skipped.",)

# Generated at 2026-10-24 06:20:59.921472
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[invalid literal"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        "isort failed to parse the given literal [invalid literal. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of malformed node or string."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 06:21:01.416860
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "bad_syntax.py"

    error = ExistingSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "bad_syntax.py."
    )

    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(file_path)
    assert exc_info.value.file_path == file_path

# Generated at 2026-10-24 06:21:06.635297
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/path/to/nonexistent/settings"
    error = InvalidSettingsPath(settings_path)

    assert error.settings_path == settings_path
    assert str(error) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 06:21:12.015635
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/path/to/nonexistent/settings"

    error = InvalidSettingsPath(settings_path)

    assert error.settings_path == settings_path
    assert str(error) == (
        "isort was told to use the settings_path: "
        "/path/to/nonexistent/settings as the base directory or file that represents "
        "the starting point of config file discovery, but it does not exist."
    )
    assert error.args == (str(error),)

# Generated at 2026-10-24 06:21:18.923224
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert error.kind is list
    assert error.expected_kind is tuple
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 06:21:28.136370
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)


# Generated at 2026-10-24 06:21:35.005952
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list
assert error.args == (str(error),)

# Generated at 2026-10-24 06:21:44.139856
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'list'> but was given "
        "a literal of type <class 'dict'>."
    )

# Generated at 2026-10-24 06:21:49.962849
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> but was given "
    "a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 06:21:57.110029
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)
assert str(error) == (
    "isort was told to sort a literal of type <class 'int'> but was given "
    "a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is int

# Generated at 2026-10-24 06:21:59.624798
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 06:22:02.038834
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 06:22:04.454498
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 06:22:15.035407
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert error.kind is list
    assert error.expected_kind is tuple
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 06:22:21.589349
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)

assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> "
    "but was given a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 06:22:30.190971
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 06:22:36.036944
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert error.kind is list
    assert error.expected_kind is tuple
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 06:22:43.399638
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> but was given "
    "a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 06:22:49.339063
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> but was given "
    "a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 06:22:51.851033
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:22:54.353386
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:22:56.774255
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:22:59.187836
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:23:01.602741
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:23:04.017718
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:23:06.432030
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 06:23:08.846958
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 06:23:11.262805
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-24 06:23:13.679339
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:23:16.096313
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:23:24.056697
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)


# Generated at 2026-10-24 06:23:29.641988
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=str, expected_kind=int)

    assert isinstance(error, ISortError)
    assert error.kind is str
    assert error.expected_kind is int
    assert str(error) == (
        "isort was told to sort a literal of type <class 'int'> but was given "
        "a literal of type <class 'str'>."
    )

# Generated at 2026-10-24 06:23:36.770434
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 06:23:48.936168
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 06:23:55.131691
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 06:24:02.458560
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 06:24:09.211527
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)


# Generated at 2026-10-24 06:24:11.712114
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:24:14.128405
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 06:24:16.546113
# Unit test for constructor of class LiteralSortTypeMismatch