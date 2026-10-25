

# Generated at 2026-10-24 05:33:49.215594
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

# Generated at 2026-10-24 05:33:55.791020
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/path/to/nonexistent/settings"
    error = InvalidSettingsPath(settings_path)

    assert error.settings_path == settings_path
    assert isinstance(error, ISortError)
    assert str(error) == (
        "isort was told to use the settings_path: "
        "/path/to/nonexistent/settings as the base directory or file that "
        "represents the starting point of config file discovery, but it does "
        "not exist."
    )

# Generated at 2026-10-24 05:34:01.092541
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:34:07.953827
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)
assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> but was given "
    "a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 05:34:15.542071
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

# Generated at 2026-10-24 05:34:16.903722
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:34:18.293606
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:34:23.210030
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:34:31.601064
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)


# Generated at 2026-10-24 05:34:34.020977
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:34:36.436716
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-24 05:34:38.851313
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-24 05:34:43.087879
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():error = ExistingSyntaxErrors("example.py")

# Generated at 2026-10-24 05:34:48.706958
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "foo = 1\nbar = 2"

    error = AssignmentsFormatMismatch(code)

    assert error.code == code
    assert isinstance(error, ISortError)
    assert str(error) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "foo = 1\n"
        "bar = 2\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

# Generated at 2026-10-24 05:34:55.363559
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "foo = 1\nbar = 2"

    error = AssignmentsFormatMismatch(code)

    assert isinstance(error, ISortError)
    assert error.code == code
    assert error.args == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "foo = 1\nbar = 2\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n",
    )

# Generated at 2026-10-24 05:35:00.485159
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

# Generated at 2026-10-24 05:35:06.832433
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[invalid literal"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert isinstance(error, ISortError)
    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        "isort failed to parse the given literal [invalid literal. "
        "It's important to note that isort literal sorting only supports "
        "simple literals parsable by ast.literal_eval which gave the "
        "exception of malformed node or string."
    )

# Generated at 2026-10-24 05:35:12.886914
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
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:35:19.122014
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[3, 1, invalid]"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    expected_message = (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.code == code
    assert error.original_error is original_error

# Generated at 2026-10-24 05:35:23.523110
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():original_error = ValueError("malformed node or string")

# Generated at 2026-10-24 05:35:24.826135
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

# Generated at 2026-10-24 05:35:26.138643
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

# Generated at 2026-10-24 05:35:34.481538
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        f"isort was told to sort a literal of type {expected_kind} but was given "
        f"a literal of type {kind}."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:35:36.899304
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:35:39.316040
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:36:00.490941
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = list

# Generated at 2026-10-24 05:36:07.657928
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)
assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 05:36:17.077897
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)


# Generated at 2026-10-24 05:36:22.097865
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:36:29.060085
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)
assert str(error) == (
    "isort was told to sort a literal of type <class 'int'> but was given "
    "a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is int

# Generated at 2026-10-24 05:36:36.163845
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> "
    "but was given a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 05:36:44.010836
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:36:53.168689
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)

assert str(error) == (
    "isort was told to sort a literal of type <class 'int'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is int

# Generated at 2026-10-24 05:37:00.089705
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> but was given "
    "a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 05:37:06.007324
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:37:12.770322
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, list)
assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> but was given "
    "a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is list

# Generated at 2026-10-24 05:37:31.916709
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(dict, list)

# Generated at 2026-10-24 05:37:34.428652
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:37:36.849834
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:37:39.270144
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:37:41.689544
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:37:44.106148
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:37:51.800452
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)


# Generated at 2026-10-24 05:37:57.433013
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

# Generated at 2026-10-24 05:38:05.521318
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)

assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> "
    "but was given a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 05:38:13.713296
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)


# Generated at 2026-10-24 05:38:18.529209
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )
    assert error.kind is list
    assert error.expected_kind is tuple
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:38:25.602441
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

# Generated at 2026-10-24 05:38:32.762158
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 05:38:35.182668
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:38:37.597646
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:38:40.014638
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:38:42.431935
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:38:53.650948
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-24 05:39:00.925047
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> but was given "
    "a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 05:39:06.348257
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert error.kind is list
    assert error.expected_kind is tuple
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:39:13.619239
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 05:39:21.007823
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> but was given "
    "a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 05:39:26.318423
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

    assert error.kind is dict
    assert error.expected_kind is list
    assert str(error) == (
        "isort was told to sort a literal of type <class 'list'> but was given "
        "a literal of type <class 'dict'>."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:39:28.834880
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:31.251914
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:33.666241
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:36.080697
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:38.495735
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:40.910100
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:43.324575
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:39:45.890211
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-24 05:39:52.222560
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type "
        "<class 'tuple'> but was given a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:39:59.134155
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, list)
assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is list

# Generated at 2026-10-24 05:40:05.739809
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)
assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 05:40:11.168113
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:40:18.028744
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 05:40:20.445913
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:22.860549
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:25.399048
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:27.816106
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:30.231391
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:32.648542
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:35.063476
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:37.490212
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:39.894626
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:42.309974
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:44.723797
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:47.139319
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:49.553991
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:51.966741
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:54.379276
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:40:56.793994
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:02.962352
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = list
    expected_kind = tuple

    error = LiteralSortTypeMismatch(kind, expected_kind)

    assert isinstance(error, ISortError)
    assert error.kind is kind
    assert error.expected_kind is expected_kind
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:41:09.434936
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)
assert str(error) == "isort was told to sort a literal of type <class 'list'> but was given a literal of type <class 'str'>."
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 05:41:16.909564
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, list)

# Generated at 2026-10-24 05:41:22.541881
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

# Generated at 2026-10-24 05:41:31.624296
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)


# Generated at 2026-10-24 05:41:34.039534
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:36.454190
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:38.867092
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:41.281257
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:43.695208
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:46.111720
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:48.525223
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:50.939114
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:53.353169
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:55.768969
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:41:58.181911
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:05.204980
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 05:42:11.941325
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)


# Generated at 2026-10-24 05:42:19.271808
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is tuple
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:42:26.540661
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)

assert str(error) == (
    "isort was told to sort a literal of type <class 'int'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is int

# Generated at 2026-10-24 05:42:33.402852
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, dict)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> but was given "
    "a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is dict

# Generated at 2026-10-24 05:42:35.903947
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:38.319805
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:40.734775
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:43.150457
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:45.565330
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:47.976648
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:50.391332
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:53.254583
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:55.667117
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:42:58.081341
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:00.502254
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:02.913223
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:05.328972
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:07.742050
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:10.161226
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:12.574232
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:14.989984
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:17.411260
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:19.823789
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:22.240830
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:24.665311
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:27.076058
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:29.493581
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:31.906195
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:34.325230
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:36.742205
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:43:39.158831
# Unit test for constructor of class LiteralSortTypeMismatch