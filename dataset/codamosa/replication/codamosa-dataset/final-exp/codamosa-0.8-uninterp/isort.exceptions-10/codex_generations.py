

# Generated at 2022-06-13 23:00:54.180722
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "dummy_formatter"
    try:
        raise FormattingPluginDoesNotExist(formatter)
    except FormattingPluginDoesNotExist as e:
        assert type(e).__name__ == "FormattingPluginDoesNotExist"
        assert e.args[0] == "Specified formatting plugin of dummy_formatter does not exist. "
        assert e.formatter == "dummy_formatter"

# Generated at 2022-06-13 23:00:57.211077
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "Default"
    message = "Specified formatting plugin of Default does not exist."
    assert FormattingPluginDoesNotExist(formatter).args[0] == message
    assert FormattingPluginDoesNotExist(formatter).formatter == formatter

# Generated at 2022-06-13 23:01:02.547226
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    try:
        UnsupportedSettings({})
    except ISortError as isort_error:
        assert str(isort_error) == (
            "isort was provided settings that it doesn't support:\n\n"
            "For a complete and up-to-date listing of supported settings see: "
            "https://pycqa.github.io/isort/docs/configuration/options/.\n"
        )

# Generated at 2022-06-13 23:01:23.063605
# Unit test for constructor of class ISortError
def test_ISortError():
    error_message = "Test ISortError"
    test_error = ISortError(error_message)
    assert test_error.message == error_message


# Generated at 2022-06-13 23:01:26.154384
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert InvalidSettingsPath("test.py").settings_path == "test.py"


# Generated at 2022-06-13 23:01:31.327635
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = '/home/mariano'
    ex = IntroducedSyntaxErrors(file_path)
    assert ex.file_path == file_path
    assert str(ex) == 'isort introduced syntax errors when attempting to sort the imports contained within '+file_path+'.'


# Generated at 2022-06-13 23:01:46.277899
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    with pytest.raises(AssignmentsFormatMismatch):
        raise AssignmentsFormatMismatch('')

# Generated at 2022-06-13 23:01:48.806108
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert InvalidSettingsPath("test").settings_path == "test"


# Generated at 2022-06-13 23:01:55.164791
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "name"
    original_error = ISortError("original error")
    try:
        raise LiteralParsingFailure(code, original_error)
    except LiteralParsingFailure as e:
        assert e.code == code
        assert e.original_error == original_error


# Generated at 2022-06-13 23:02:06.845257
# Unit test for constructor of class ISortError
def test_ISortError():
    msg='test ISortError'
    error1=ISortError(msg)
    assert error1.args[0] == msg


# Generated at 2022-06-13 23:02:11.612846
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    with pytest.raises(FormattingPluginDoesNotExist):
        raise FormattingPluginDoesNotExist("formatter value")


# Generated at 2022-06-13 23:02:19.869534
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = "x"
    section = "y"
    section_error = MissingSection(import_module, section)
    assert section_error.args[0] == f"Found {import_module} import while parsing, but {section} was not included in the `sections` setting of your config. Please add it before continuing\nSee https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."

# Generated at 2022-06-13 23:02:24.181316
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting("/tmp/test_file_path")
    except FileSkipSetting as e:
        assert e.message == "/tmp/test_file_path was skipped as it's listed in 'skip' setting" \
                            " or matches a glob in 'skip_glob' setting"
        assert e.file_path == "/tmp/test_file_path"

# Generated at 2022-06-13 23:02:29.517992
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    import pytest
    from isort.exceptions import FileSkipComment
    try:
        raise FileSkipComment("/test/path")
    except FileSkipComment as e :
        assert e.file_path == "/test/path"
        assert 'does not' in e.message
    else:
        pytest.fail()


# Generated at 2022-06-13 23:02:35.487788
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "test"
    file_skip_comment = FileSkipComment(file_path)
    assert file_skip_comment
    assert file_skip_comment.message == f"{file_path} contains an file skip comment and was skipped."
    assert file_skip_comment.file_path == file_path

# Generated at 2022-06-13 23:02:36.911283
# Unit test for constructor of class ISortError
def test_ISortError():
    assert ISortError.__init__ == Exception.__init__

# Generated at 2022-06-13 23:02:38.817247
# Unit test for constructor of class MissingSection
def test_MissingSection():
    err = MissingSection("import_module", "section")
    print(err)

# Generated at 2022-06-13 23:02:42.298316
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    import json
    assert isinstance(LiteralParsingFailure(json.dumps([1,2,3]), "abc"), ISortError)
    

# Generated at 2022-06-13 23:02:54.132086
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    # Tests:
    #   - Constructor of class FileSkipSetting
    # Arguments:
    #   message: string
    #   file_path: string
    # Purpose:
    #   Test that the constructor of FileSkipSetting is working properly,
    #   by creating an instance and validating the value of 'message' and
    #   'file_path'.
    message = 'I am a valid file path.'
    file_path = 'I am also a valid file path.'
    f = FileSkipSetting(message, file_path)
    assert f.message == message
    assert f.file_path == file_path

# Generated at 2022-06-13 23:02:57.479808
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path="path"
    FS=FileSkipComment(file_path=file_path)
    assert FS.file_path == file_path


# Generated at 2022-06-13 23:03:02.013173
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch(): 
    tmp = LiteralSortTypeMismatch(3, 4)
    assert tmp.kind == 3
    assert tmp.expected_kind == 4


# Generated at 2022-06-13 23:03:06.126893
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("settings.yaml")
    except InvalidSettingsPath as e:
        assert str(e) == "isort was told to use the settings_path: settings.yaml as the base directory or " \
                         "file that represents the starting point of config file discovery, but it does not " \
                         "exist."
        assert e.settings_path == "settings.yaml"


# Generated at 2022-06-13 23:03:09.602083
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    e = FileSkipped("message", "file_path")
    assert e.message == "message"
    assert e.file_path == "file_path"

# Generated at 2022-06-13 23:03:13.992364
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    try:
        raise FileSkipComment(file_path="tests/")
    except FileSkipped as e:
        assert e.file_path == "tests/"
        assert e.message == "tests/ contains an file skip comment and was skipped."



# Generated at 2022-06-13 23:03:16.910385
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    abc_file = "abc"
    try:
        raise ExistingSyntaxErrors(abc_file)
    except:
        assert abc_file == ExistingSyntaxErrors.file_path


# Generated at 2022-06-13 23:03:19.327039
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath(settings_path= "Test")
    except InvalidSettingsPath as ISE:
        assert ISE.settings_path == "Test"


# Generated at 2022-06-13 23:03:20.944409
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    IntroducedSyntaxErrors("file_path")

# Generated at 2022-06-13 23:03:26.345105
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    test_file_path = "test_file_path"
    file_skip_comment = FileSkipComment(test_file_path)
    assert str(file_skip_comment) == f"{test_file_path} contains an file skip comment and was skipped."
    assert file_skip_comment.file_path == test_file_path

# Generated at 2022-06-13 23:03:27.885549
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert InvalidSettingsPath("foo").settings_path == "foo"


# Generated at 2022-06-13 23:03:30.263207
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist(profile="test")
    except ProfileDoesNotExist as e:
        assert e.profile == "test"

# Generated at 2022-06-13 23:03:38.234734
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting("example.py")
    except FileSkipSetting as err:
        assert err.message == "example.py was skipped as it's listed in 'skip' setting" \
                              " or matches a glob in 'skip_glob' setting"

# Generated at 2022-06-13 23:03:44.347336
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    exception = FileSkipSetting("test")
    assert exception.file_path == "test"
    assert str(exception) == "test was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Generated at 2022-06-13 23:03:45.439987
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    _ = InvalidSettingsPath("file")

# Generated at 2022-06-13 23:03:48.772154
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        x = LiteralSortTypeMismatch(type, type)
    except:
        x = None
    assert x is None


# Generated at 2022-06-13 23:03:49.741672
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    FileSkipComment("file_path")

# Generated at 2022-06-13 23:03:53.156305
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("formatter")
    assert error.formatter == "formatter"



# Generated at 2022-06-13 23:04:00.829145
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(kind = [], expected_kind = dict)
    except ISortError as err:
        assert(err.kind == [])
        assert(err.expected_kind == dict)
        assert(str(err) == "isort was told to sort a literal of type <class 'dict'> but was given a literal of type <class 'list'>.")
# Test by Joe_Song


# Generated at 2022-06-13 23:04:03.635684
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    assert LiteralSortTypeMismatch(1, 1).kind == LiteralSortTypeMismatch(1, 1).expected_kind

# Generated at 2022-06-13 23:04:07.447623
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    test = ExistingSyntaxErrors("file_path.py")
    assert "isort was told to sort imports" in str(test)
    assert test.file_path == "file_path.py"

# Generated at 2022-06-13 23:04:11.463846
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("temp")
        assert False
    except IntroducedSyntaxErrors as e:
        assert e.file_path == "temp"

# Generated at 2022-06-13 23:04:22.237601
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    setting = FileSkipSetting("Foo")
    assert setting.file_path == "Foo"
    assert str(setting) == "Foo was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Generated at 2022-06-13 23:04:29.862859
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2022-06-13 23:04:34.928429
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    path = '/Users/Nikita/PycharmProjects/isort/isort.py'
    assert path == FileSkipped('/Users/Nikita/PycharmProjects/isort/isort.py', 'isort').file_path


# Generated at 2022-06-13 23:04:39.333943
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    test_formatter = "default"
    test_error = FormattingPluginDoesNotExist(formatter=test_formatter)
    assert test_error
    assert test_error.formatter == test_formatter

# Generated at 2022-06-13 23:04:44.444853
# Unit test for constructor of class MissingSection
def test_MissingSection():
    err = MissingSection('spam', 'further_spam')
    assert str(err) == 'Found spam import while parsing, but further_spam was not included ' \
        'in the `sections` setting of your config. Please add it before continuing\n' \
        'See https://pycqa.github.io/isort/#custom-sections-and-ordering ' \
        'for more info.'
    assert err.import_module == 'spam'
    assert err.section == 'further_spam'



# Generated at 2022-06-13 23:04:51.755704
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    """Unit tests for ProfileDoesNotExist class"""
    assert ProfileDoesNotExist("blabla").profile == "blabla"
    assert ProfileDoesNotExist("blabla").args[0] == "Specified profile of blabla does not exist. Available profiles: black,google,pep8,pycharm,jupyter,knuth,mozilla,mypy,numpy,sonarqube,vintage."



# Generated at 2022-06-13 23:04:53.405302
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    FormattingPluginDoesNotExist(formatter='test')


# Generated at 2022-06-13 23:05:00.742500
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    expected_message = "isort was told to sort a literal of type {} but was given " \
                       "a literal of type {}.".format(str, int)
    try:
        raise LiteralSortTypeMismatch(kind = int, expected_kind = str)
    except LiteralSortTypeMismatch as e:
        assert e.message == expected_message

        assert e.kind == int
        assert e.expected_kind == str

        assert e.expected_kind is str
        assert e.kind is int

# Generated at 2022-06-13 23:05:06.293104
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    my_settings = UnsupportedSettings({'bad_setting': {'value': True, 'source': 'cli'}})
    assert str(my_settings) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- bad_setting = True  (source: 'cli')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

# Generated at 2022-06-13 23:05:09.215391
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "path/to/file"
    msg = f"{file_path} contains an file skip comment and was skipped."
    e = FileSkipComment(file_path)
    assert e.message == msg
    assert e.file_path == file_path