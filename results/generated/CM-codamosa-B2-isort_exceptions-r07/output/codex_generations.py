

# Generated at 2026-10-24 23:11:27.439875
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

# Generated at 2026-10-24 23:11:33.582945
# Unit test for constructor of class ISortError
def test_ISortError():
    # ISortError should be instantiable with no arguments
    error = ISortError()
    assert str(error) == ""

    # ISortError should be instantiable with a message
    error = ISortError("some message")
    assert str(error) == "some message"

    # ISortError should behave as a standard Exception
    assert isinstance(error, Exception)

    # All isort exceptions should inherit from ISortError
    for exc_class in [
        InvalidSettingsPath,
        ExistingSyntaxErrors,
        IntroducedSyntaxErrors,
        FileSkipped,
        FileSkipComment,
        FileSkipSetting,
        ProfileDoesNotExist,
        FormattingPluginDoesNotExist,
        LiteralParsingFailure,
        LiteralSortTypeMismatch,
        AssignmentsFormatMismatch,
        UnsupportedSettings,
        UnsupportedEncoding,
        MissingSection,
    ]:
        assert issubclass(exc_class, ISortError)

    # ISortError should be raisable and catchable
    try:
        raise ISortError("test error")
    except ISortError as e:
        assert str(e) == "test error"
    else:
        assert False, "ISortError was not raised"

# Generated at 2026-10-24 23:11:39.624228
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "foo = 1\nbar = 2"

    error = AssignmentsFormatMismatch(code)

    assert isinstance(error, ISortError)
    assert error.code == code
    assert str(error) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "foo = 1\nbar = 2\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

# Generated at 2026-10-24 23:11:44.232702
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, ISortError)
    assert error.formatter == formatter
    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "

# Generated at 2026-10-24 23:11:49.455916
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        "contained within example.py."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 23:11:54.414056
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    filename = Path("example.py")

    error = UnsupportedEncoding(filename)

    assert str(error) == "Unknown or unsupported encoding in example.py"
    assert error.filename == filename
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 23:12:03.412827
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:12:08.604571
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():error = InvalidSettingsPath("/nonexistent/settings/path")

# Generated at 2026-10-24 23:12:13.646294
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

# Generated at 2026-10-24 23:12:14.996681
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:12:18.541564
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/nonexistent/isort/config"

# Generated at 2026-10-24 23:12:23.247670
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    filename = Path("example.py")
    error = UnsupportedEncoding(filename)

    assert str(error) == "Unknown or unsupported encoding in example.py"
    assert error.filename == filename
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 23:12:28.043322
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

# Generated at 2026-10-24 23:12:32.155904
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 23:12:35.944196
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 23:12:37.377788
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:12:40.860034
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/nonexistent/isort/config"

# Generated at 2026-10-24 23:12:45.775728
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

# Generated at 2026-10-24 23:12:49.981355
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 23:12:53.863654
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 23:12:59.702989
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    filename = Path("example.py")

    error = UnsupportedEncoding(filename)

    assert str(error) == "Unknown or unsupported encoding in example.py"
    assert error.filename == filename
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 23:13:01.030221
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:13:04.514050
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():error = InvalidSettingsPath("/nonexistent/settings")


# Generated at 2026-10-24 23:13:10.202451
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "foo = 1\nbar = 2"
    error = AssignmentsFormatMismatch(code)

    assert error.code == code
    assert str(error) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        "foo = 1\nbar = 2\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )
    assert error.args == (str(error),)

# Generated at 2026-10-24 23:13:15.364310
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        "example.py."
    )

# Generated at 2026-10-24 23:13:25.302030
# Unit test for constructor of class MissingSection
def test_MissingSection():
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module="os", section="FUTURE")

    assert str(exc_info.value) == (
        "Found os import while parsing, but FUTURE was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert isinstance(exc_info.value, ISortError)

# Generated at 2026-10-24 23:13:26.747172
# Unit test for constructor of class MissingSection
def test_MissingSection():
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module="os", section="FUTURE")

    assert str(exc_info.value) == (
        "Found os import while parsing, but FUTURE was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert isinstance(exc_info.value, ISortError)

# Generated at 2026-10-24 23:13:32.674412
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent-profile"

    error = ProfileDoesNotExist(profile)

    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert isinstance(error, ISortError)
    assert error.profile == profile
    assert str(error) == expected_message
    assert error.args == (expected_message,)

# Generated at 2026-10-24 23:13:38.716306
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("nonexistent")

# Generated at 2026-10-24 23:13:43.323287
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"

    error = FileSkipSetting(file_path)

    assert isinstance(error, FileSkipped)
    assert error.file_path == file_path
    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

# Generated at 2026-10-24 23:13:48.136679
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        "contained within example.py."
    )

# Generated at 2026-10-24 23:13:53.359617
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

# Generated at 2026-10-24 23:13:57.659242
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 23:14:00.629441
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-24 23:14:05.954436
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"

    error = FileSkipComment(file_path)

    assert error.file_path == file_path
    assert str(error) == "example.py contains an file skip comment and was skipped."
    assert error.args == ("example.py contains an file skip comment and was skipped.",)

# Generated at 2026-10-24 23:14:07.351512
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:14:11.381374
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/nonexistent/isort/config"

# Generated at 2026-10-24 23:14:15.785736
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent-profile"

    error = ProfileDoesNotExist(profile)

    assert isinstance(error, ISortError)
    assert error.profile == profile
    assert str(error) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )

# Generated at 2026-10-24 23:14:24.899276
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("missing-profile")

# Generated at 2026-10-24 23:14:29.765628
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports "
        "contained within example.py."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-24 23:14:33.707934
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"

    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        "example.py."
    )

# Generated at 2026-10-24 23:14:39.542808
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "unknown_option": {
            "value": "some_value",
            "source": "test_config",
        }
    }

    error = UnsupportedSettings(unsupported_settings)

    expected_message = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_option = some_value  (source: 'test_config')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.unsupported_settings == unsupported_settings

# Generated at 2026-10-24 23:14:40.922523
# Unit test for constructor of class MissingSection
def test_MissingSection():
    with pytest.raises(MissingSection) as exc_info:
        raise MissingSection(import_module="os", section="FUTURE")

    assert str(exc_info.value) == (
        "Found os import while parsing, but FUTURE was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert isinstance(exc_info.value, ISortError)

# Generated at 2026-10-24 23:14:47.326609
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "{invalid literal}"
    original_error = ValueError("malformed node or string")

    error = LiteralParsingFailure(code, original_error)

    assert error.code == code
    assert error.original_error is original_error
    assert str(error) == (
        "isort failed to parse the given literal {invalid literal}. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of malformed node or string."
    )

# Generated at 2026-10-24 23:14:52.860020
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

# Generated at 2026-10-24 23:14:54.191405
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:14:57.974089
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/missing/settings"

# Generated at 2026-10-24 23:14:59.345294
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:15:02.584238
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/nonexistent/isort/config"

# Generated at 2026-10-24 23:15:03.928737
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-24 23:15:07.893452
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():error = InvalidSettingsPath("/missing/settings")
