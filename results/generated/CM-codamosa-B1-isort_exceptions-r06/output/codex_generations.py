

# Generated at 2026-10-24 05:33:50.488526
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-24 05:33:56.234131
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[invalid literal"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )

# Generated at 2026-10-24 05:33:57.711923
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

# Generated at 2026-10-24 05:33:59.144315
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

# Generated at 2026-10-24 05:34:02.948788
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("unknown")

# Generated at 2026-10-24 05:34:09.925041
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[1, invalid]"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert str(error) == (
        "isort failed to parse the given literal [1, invalid]. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of malformed node or string."
    )
    assert error.code == code
    assert error.original_error is original_error
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:34:15.556390
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = "example_module"
    section = "THIRDPARTY"
    expected_message = (
        f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    error = MissingSection(import_module, section)

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.args == (expected_message,)

# Generated at 2026-10-24 05:34:19.838321
# Unit test for constructor of class MissingSection
def test_MissingSection():error = MissingSection("requests", "THIRDPARTY")

# Generated at 2026-10-24 05:34:26.051141
# Unit test for constructor of class MissingSection
def test_MissingSection():
    error = MissingSection("example_module", "CUSTOM_SECTION")

    expected_message = (
        "Found example_module import while parsing, but CUSTOM_SECTION was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.args == (expected_message,)

# Generated at 2026-10-24 05:34:28.567804
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:34:30.985791
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:34:33.400169
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:34:35.814161
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:34:38.231824
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:34:44.815969
# Unit test for constructor of class MissingSection
def test_MissingSection():exc = MissingSection("os", "STDLIB")

# Generated at 2026-10-24 05:34:46.557711
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:34:52.395364
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

    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:34:57.617452
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

# Generated at 2026-10-24 05:35:04.967873
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)


# Generated at 2026-10-24 05:35:12.269591
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)

# Generated at 2026-10-24 05:35:18.617080
# Unit test for constructor of class MissingSection
def test_MissingSection():
    error = MissingSection("example_module", "CUSTOM")

    expected_message = (
        "Found example_module import while parsing, but CUSTOM was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

    assert isinstance(error, ISortError)
    assert str(error) == expected_message
    assert error.args == (expected_message,)

# Generated at 2026-10-24 05:35:20.040571
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:35:21.474266
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:35:26.905253
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=tuple)

    assert error.kind is list
    assert error.expected_kind is tuple
    assert str(error) == (
        "isort was told to sort a literal of type <class 'tuple'> but was given "
        "a literal of type <class 'list'>."
    )

# Generated at 2026-10-24 05:35:34.172502
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)
assert str(error) == (
    "isort was told to sort a literal of type <class 'tuple'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is tuple

# Generated at 2026-10-24 05:35:36.697972
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 05:35:39.229266
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-24 05:35:52.707228
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():from isort.exceptions import LiteralParsingFailure

# Generated at 2026-10-24 05:35:58.032903
# Unit test for constructor of class ISortError
def test_ISortError():
    message = "An isort error occurred"

    error = ISortError(message)

    assert isinstance(error, Exception)
    assert error.args == (message,)
    assert str(error) == message

# Generated at 2026-10-24 05:36:03.138900
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"

    error = FileSkipSetting(file_path)

    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

# Generated at 2026-10-24 05:36:08.055006
# Unit test for constructor of class ISortError
def test_ISortError():
    message = "An isort error occurred"

    error = ISortError(message)

    assert isinstance(error, Exception)
    assert error.args == (message,)
    assert str(error) == message

# Generated at 2026-10-24 05:36:13.593367
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
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:36:21.584810
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 05:36:28.696837
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, dict)
assert str(error) == (
    "isort was told to sort a literal of type <class 'dict'> "
    "but was given a literal of type <class 'list'>."
)
assert error.kind is list
assert error.expected_kind is dict

# Generated at 2026-10-24 05:36:38.518115
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[1, invalid]"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        "isort failed to parse the given literal [1, invalid]. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of malformed node or string."
    )

# Generated at 2026-10-24 05:36:41.115384
# Unit test for constructor of class ISortError

# Generated at 2026-10-24 05:36:45.855195
# Unit test for constructor of class ISortError
def test_ISortError():error = ISortError("test error")

# Generated at 2026-10-24 05:36:47.202170
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-24 05:36:52.515554
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "[invalid literal"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert str(error) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
    assert error.code == code
    assert error.original_error is original_error
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:36:59.679089
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/path/to/nonexistent/settings"

    error = InvalidSettingsPath(settings_path)

    assert isinstance(error, ISortError)
    assert error.settings_path == settings_path
    assert str(error) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )

# Generated at 2026-10-24 05:37:04.788931
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/path/that/does/not/exist"

    error = InvalidSettingsPath(settings_path)

    assert error.settings_path == settings_path
    assert str(error) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:37:11.454944
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

# Generated at 2026-10-24 05:37:19.748776
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.args == (str(error),)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 05:37:27.330075
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, str)
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> but was given "
    "a literal of type <class 'int'>."
)
assert error.kind is int
assert error.expected_kind is str

# Generated at 2026-10-24 05:37:29.747359
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 05:37:32.251345
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 05:37:34.666616
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 05:37:37.085722
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 05:37:39.505739
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 05:37:41.925192
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 05:37:52.721480
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():code = "first = 1\nsecond = 2"

# Generated at 2026-10-24 05:37:54.155266
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

# Generated at 2026-10-24 05:38:01.555053
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("unknown")

# Generated at 2026-10-24 05:38:02.933867
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:38:04.396034
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "nonexistent_formatter"
    exc = FormattingPluginDoesNotExist(formatter)

    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.formatter == formatter
    assert str(exc) == f"Specified formatting plugin of {formatter} does not exist. "
    assert exc.args[0] == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2026-10-24 05:38:09.822183
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = '{"key": invalid}'
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert str(error) == (
        f"isort failed to parse the given literal {code}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        f"ast.literal_eval which gave the exception of {original_error}."
    )
    assert error.code == code
    assert error.original_error is original_error
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:38:16.173386
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"

    error = FileSkipSetting(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:38:21.700825
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    error = FileSkipSetting(file_path)

    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert error.file_path == file_path
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 05:38:26.411509
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "/nonexistent/path/to/settings"

    error = InvalidSettingsPath(settings_path)

    assert isinstance(error, ISortError)
    assert error.settings_path == settings_path
    assert str(error) == (
        f"isort was told to use the settings_path: {settings_path} as the base directory or "
        "file that represents the starting point of config file discovery, but it does not "
        "exist."
    )

# Generated at 2026-10-24 05:38:33.581026
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "unknown_option": {"value": "some_value", "source": "config file"},
        "another_option": {"value": "42", "source": "command line"},
    }

    error = UnsupportedSettings(unsupported_settings)

    assert error.unsupported_settings is unsupported_settings
    assert str(error) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = some_value  (source: 'config file')\n"
        "\t- another_option = 42  (source: 'command line')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

# Generated at 2026-10-24 05:38:36.085190
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:38:38.504400
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:38:40.999422
# Unit test for constructor of class MissingSection

# Generated at 2026-10-24 05:38:43.521324
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 05:38:49.350764
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():unsupported_settings = {
        "invalid_option": {"value": "invalid_value", "source": "test_config"}
    }

# Generated at 2026-10-24 05:38:51.089108
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

# Generated at 2026-10-24 05:38:57.645302
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "unknown_option": {"value": "value", "source": "test"},
        "another_option": {"value": "42", "source": "config"},
    }

    error = UnsupportedSettings(unsupported_settings)

    assert error.unsupported_settings == unsupported_settings
    assert str(error) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = value  (source: 'test')\n"
        "\t- another_option = 42  (source: 'config')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

# Generated at 2026-10-24 05:38:59.077614
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

# Generated at 2026-10-24 05:39:07.034238
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("nonexistent")

# Generated at 2026-10-24 05:39:20.226129
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"

    exception = FileSkipComment(file_path)

    assert isinstance(exception, FileSkipped)
    assert exception.file_path == file_path
    assert str(exception) == f"{file_path} contains an file skip comment and was skipped."