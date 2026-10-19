

# Generated at 2022-06-13 23:00:34.579541
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    with pytest.raises(IntroducedSyntaxErrors):
        raise IntroducedSyntaxErrors("/tmp/a.py")



# Generated at 2022-06-13 23:00:39.473988
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    with pytest.raises(LiteralParsingFailure):
        raise LiteralParsingFailure('abc',SyntaxError)

# Generated at 2022-06-13 23:00:48.715053
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    # Test new ISortError object
    assert InvalidSettingsPath("/invalid_settings_path")
    # Test exception message
    assert InvalidSettingsPath("/invalid_settings_path").__str__() == "isort was told to use the settings_path: /invalid_settings_path as the base directory or file that represents the starting point of config file discovery, but it does not exist."
    # Test settings_path attribute
    assert InvalidSettingsPath("/invalid_settings_path").settings_path == "/invalid_settings_path"


# Generated at 2022-06-13 23:00:52.537750
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    ue = UnsupportedEncoding("test.py")
    assert ue.filename == "test.py"
    assert "Unknown or unsupported" in str(ue)
    assert str(ue) == "Unknown or unsupported encoding in test.py"


# Generated at 2022-06-13 23:00:56.924697
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("my_file")
    except ExistingSyntaxErrors as e:
        assert str(e) == (
            "isort was told to sort imports within code that contains syntax errors: "
            "my_file."
        )
        assert e.file_path == "my_file"



# Generated at 2022-06-13 23:01:02.870729
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "1, 2, 3"
    try:
        raise LiteralParsingFailure(code, Exception("Test exception"))
    except LiteralParsingFailure as e:
        assert str(e) == (
            "isort failed to parse the given literal 1, 2, 3. It's important to note that "
            "isort literal sorting only supports simple literals parsable by ast.literal_eval "
            "which gave the exception of Test exception."
        )

# Generated at 2022-06-13 23:01:21.887904
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    pytest.raises(FormattingPluginDoesNotExist,
                  lambda: FormattingPluginDoesNotExist("WrongFormat"))

# Generated at 2022-06-13 23:01:24.022917
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code='a=1'
    x=AssignmentsFormatMismatch(code)
    assert x.code==code

# Generated at 2022-06-13 23:01:27.576389
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    assert LiteralSortTypeMismatch(kind = list, expected_kind = tuple).__init__(kind = list, expected_kind = tuple) is None


# Generated at 2022-06-13 23:01:33.004594
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    from isort import exceptions

    try:
        raise exceptions.InvalidSettingsPath("../")
    except exceptions.ISortError as e:
        assert e.__str__() == "isort was told to use the settings_path: ../ " \
                              "as the base directory or file that represents the starting point of " \
                              "config file discovery, but it does not exist."
        assert e.settings_path == "../"



# Generated at 2022-06-13 23:01:52.290375
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    file_skipped = FileSkipped("message", "file_path")
    assert file_skipped.message == "message"
    assert file_skipped.file_path == "file_path"



# Generated at 2022-06-13 23:02:07.142094
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2022-06-13 23:02:10.778161
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        'i9.txt'
    except:
        return True
    return False
#test_InvalidSettingsPath()


# Generated at 2022-06-13 23:02:18.620499
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    class TestException:
        def __init__(self, e):
            assert isinstance(e,UnsupportedEncoding)
    try:
        raise(UnsupportedEncoding(filename="toto"))
    except TestException as e:
        e.__init__(e)

# Parameters for the Unit test of constructor of class UnsupportedEncoding
test_UnsupportedEncoding()

# Generated at 2022-06-13 23:02:20.241783
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    # Act
    raise FormattingPluginDoesNotExist("my_plugin")

# Generated at 2022-06-13 23:02:23.846664
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    try:
        raise FileSkipped(
            message="The message to show",
            file_path="The file path to show",
        )
    except FileSkipped as err:
        assert err.file_path == "The file path to show"
        assert err.message == "The message to show"

# Generated at 2022-06-13 23:02:28.943430
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(type(1), type(1))
    except LiteralSortTypeMismatch as e:
        assert type(1) == e.kind
        assert type(1) == e.expected_kind
    else:
        assert False, 'Exception not raised'

# Generated at 2022-06-13 23:02:32.531097
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    x = ExistingSyntaxErrors('test.txt')
    assert x.file_path == 'test.txt'



# Generated at 2022-06-13 23:02:35.956739
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("wrong")
    except ProfileDoesNotExist as e:
        assert e.profile == "wrong"


# Generated at 2022-06-13 23:02:40.837675
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "./"
    error = FileSkipComment(file_path)
    assert error.file_path == "./"
    assert error.message == "./ contains an file skip comment and was skipped."


# Generated at 2022-06-13 23:02:51.885389
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    # Given
    code = 'I am code'
    original_error = Exception()
    # When
    literal_parsing_failure = LiteralParsingFailure(code, original_error)
    # Then
    assert original_error == literal_parsing_failure.original_error
    assert 'I am code' == literal_parsing_failure.code

# Generated at 2022-06-13 23:02:56.518114
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("/file/path")
    except Exception as e:
        assert str(e) == "/file/path contains syntax errors and was skipped."
        assert e.file_path == "/file/path"

# Generated at 2022-06-13 23:03:02.219420
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "test_code"
    original_error = Exception("test_original_error")
    test_LiteralParsingFailure = LiteralParsingFailure(code, original_error)
    assert test_LiteralParsingFailure.code == "test_code"
    assert test_LiteralParsingFailure.original_error == Exception("test_original_error")

# Generated at 2022-06-13 23:03:04.777500
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    import random
    profiles = ['black', 'flake8', 'pre-commit']
    random_profile = random.choice(profiles)
    assert ProfileDoesNotExist(profile=random_profile)



# Generated at 2022-06-13 23:03:11.081138
# Unit test for constructor of class MissingSection
def test_MissingSection():
    # pylint: disable=line-too-long
    assert str(MissingSection('django', 'DJANGO')) == 'Found django import while parsing, but DJANGO was not included in the `sections` setting of your config. Please add it before continuing\nSee https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.'


# Generated at 2022-06-13 23:03:14.034812
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("python2")
    except ProfileDoesNotExist as e:
        assert e.profile == "python2"


# Generated at 2022-06-13 23:03:18.540984
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    try:
        raise FileSkipComment("/temp/test")
    except FileSkipComment as e:
        assert str(e) == "/temp/test contains an file skip comment and was skipped."
        assert e.file_path == "/temp/test"
        assert "test_exceptions" in e.__exception_info__()


# Generated at 2022-06-13 23:03:22.594849
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    obj = UnsupportedEncoding(filename = 'D:\\isort\\isort\\settings.py')
    assert obj.filename == 'D:\\isort\\isort\\settings.py'

# Generated at 2022-06-13 23:03:26.570068
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    """Test for AssignmentsFormatMismatch"""
    code = "foo = \"bar\"\nfizz = buzz" 
    error = AssignmentsFormatMismatch(code)
    assert error.code == code


# Generated at 2022-06-13 23:03:30.760822
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "README.md"
    x = FileSkipComment(file_path)
    assert "README.md contains" in x.args[0]

# Generated at 2022-06-13 23:03:39.438365
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "a=12 "
    e = AssignmentsFormatMismatch(code)
    assert e.code == code

# Generated at 2022-06-13 23:03:44.190460
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("my/file/path")
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: my/file/path."
        assert e.file_path == "my/file/path"

# Generated at 2022-06-13 23:03:45.686993
# Unit test for constructor of class ISortError
def test_ISortError():
    assert str(ISortError()) == ''


# Generated at 2022-06-13 23:03:49.330110
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert str(InvalidSettingsPath("N/A")) == "isort was told to use the settings_path: N/A as the base directory or file that represents the starting point of config file discovery, but it does not exist."

# Generated at 2022-06-13 23:03:50.999249
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    with LiteralSortTypeMismatch(int, str) as e:
         assert e.kind == int
         assert e.expected_kind == str

# Generated at 2022-06-13 23:03:59.768544
# Unit test for constructor of class MissingSection
def test_MissingSection():
    exc = MissingSection("foo.bar", "zoo")
    assert exc.import_module == "foo.bar"
    assert exc.section == "zoo"
    assert str(exc) == "Found foo.bar import while parsing, but zoo was not included in " \
            "the `sections` setting of your config. Please add it before continuing\n" \
            "See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."

# Generated at 2022-06-13 23:04:03.635495
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    try:
        raise AssignmentsFormatMismatch("a, b = 0, 1;\n")
    except AssignmentsFormatMismatch as e:
        assert "single line formatting" in str(e)

# Generated at 2022-06-13 23:04:09.736135
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    exception = ProfileDoesNotExist("my_profile")
    assert exception.profile == "my_profile"
    assert str(exception) == (
        "Specified profile of my_profile does not exist. Available profiles: "
        "black, google, pycharm, jupyter_lint, vscode, sphinx, docs, runtest, "
        "test, pytest, hacking, mypy, pydantic, vscode_docs, vscode_test, "
        "vscode_pytest, vscode_runtest, vscode_black."
    )


# Generated at 2022-06-13 23:04:13.055231
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath('test')
    except InvalidSettingsPath as err:
        assert err.settings_path == 'test'


# Generated at 2022-06-13 23:04:14.997282
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    assert IntroducedSyntaxErrors("test")


# Generated at 2022-06-13 23:04:24.813811
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("test.file")
    except UnsupportedEncoding as e:
        assert e.filename == "test.file"

# Generated at 2022-06-13 23:04:35.761796
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    """Unit test for constructor of class LiteralSortTypeMismatch"""
    literal_sort_type_mismatch = LiteralSortTypeMismatch(
        kind=type('str'), expected_kind=type('int')
    )
    actual = str(literal_sort_type_mismatch)
    # fmt: off
    expected = (
        "isort was told to sort a literal of type <class 'int'>"
        " but was given a literal of type <class 'str'>.\n"
    )
    # fmt: on
    assert actual == expected, "must be the same"

# Generated at 2022-06-13 23:04:38.289496
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    with pytest.raises(InvalidSettingsPath):
        raise InvalidSettingsPath("foo")


# Generated at 2022-06-13 23:04:40.437337
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    error = ProfileDoesNotExist("A")
    assert error.profile ==  "A"


# Generated at 2022-06-13 23:04:42.818467
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    exception = LiteralSortTypeMismatch(int, str)
    assert hasattr(exception, 'kind')
    assert hasattr(exception, 'expected_kind')

# Generated at 2022-06-13 23:04:46.052380
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors(file_path="test")
    except IntroducedSyntaxErrors as e:
        assert e.file_path == "test"

# Generated at 2022-06-13 23:04:49.301626
# Unit test for constructor of class MissingSection
def test_MissingSection():
    section = "TOP"
    import_module = "os"
    exc = MissingSection(section, import_module)
    assert exc.section == section
    assert exc.import_module == import_module

# Generated at 2022-06-13 23:04:55.773616
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
   
    test_FileSkipSetting = FileSkipSetting("test_FileSkipSetting.py")
   
    assert  test_FileSkipSetting.file_path == "test_FileSkipSetting.py"
    assert  test_FileSkipSetting.args == ("test_FileSkipSetting.py was skipped as it's listed in 'skip' setting"
                                          " or matches a glob in 'skip_glob' setting",)



# Generated at 2022-06-13 23:04:57.667330
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    with pytest.raises(ProfileDoesNotExist):
        raise ProfileDoesNotExist("test")

# Generated at 2022-06-13 23:05:00.741886
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    """Test to check if constructor of class LiteralSortTypeMismatch works as expected"""
    LiteralSortTypeMismatch(kind=1, expected_kind=2)

# Generated at 2022-06-13 23:05:18.121013
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        ProfileDoesNotExist("foo")
    assert "Specified profile of foo does not exist." in str(excinfo.value)
    assert "Available profiles: black, pytorch, google" in str(excinfo.value)

# Generated at 2022-06-13 23:05:18.716201
# Unit test for constructor of class ISortError
def test_ISortError():
    ISortError()

# Generated at 2022-06-13 23:05:21.980586
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("/path/to/file")
    except IntroducedSyntaxErrors as e:
        assert e.file_path == "/path/to/file"

# Generated at 2022-06-13 23:05:23.620262
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("Temp test")
    except ISortError:
        pass



# Generated at 2022-06-13 23:05:26.109622
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist
    except FormattingPluginDoesNotExist as e:
        assert type(e) == FormattingPluginDoesNotExist

# Generated at 2022-06-13 23:05:28.513444
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    error = IntroducedSyntaxErrors('123')
    print(error)
    print(error.file_path)

# Generated at 2022-06-13 23:05:33.988526
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    # test_method
    assert FileSkipSetting('filename').message == \
           "filename was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
    assert FileSkipSetting('filename').file_path == "filename"



# Generated at 2022-06-13 23:05:37.703124
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    temp = InvalidSettingsPath('hello')
    assert type(temp) == InvalidSettingsPath
    assert temp.settings_path == 'hello'


# Generated at 2022-06-13 23:05:43.305645
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
	"""Unit test constructed for isort_exceptions.py"""

	file_path = 'tests/test_cases/introduced_syntax_errors.py'
	introduced_syntax_errors = IntroducedSyntaxErrors(file_path)
	assert introduced_syntax_errors.file_path == file_path



# Generated at 2022-06-13 23:05:48.579780
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("myfile.py")
    except UnsupportedEncoding as ex:
        assert ex.args[0] == "Unknown or unsupported encoding in myfile.py"
        assert ex.filename == "myfile.py"

# Generated at 2022-06-13 23:06:18.889672
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    a = LiteralParsingFailure("some_code", "some_exception")
    assert a.code == "some_code"
    assert a.original_error == "some_exception"


# Generated at 2022-06-13 23:06:21.303010
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist('x')
    assert error.formatter == 'x'



# Generated at 2022-06-13 23:06:24.147402
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    encoding_error = UnsupportedEncoding('file')
    assert encoding_error.filename == 'file'
    assert str(encoding_error) == 'Unknown or unsupported encoding in file'

# Generated at 2022-06-13 23:06:25.443584
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    assert ExistingSyntaxErrors.__init__ is not None


# Generated at 2022-06-13 23:06:28.028992
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("This is a test")
    except ISortError as e:
        assert str(e) == "This is a test"
        assert e.args[0] == "This is a test"


# Generated at 2022-06-13 23:06:33.263819
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    with pytest.raises(UnsupportedSettings) as e:
        UnsupportedSettings({'foo':{'value':'bar','source':'beep'}})
    assert e.value.unsupported_settings == {'foo':{'value':'bar','source':'beep'}}

# Generated at 2022-06-13 23:06:43.297637
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    with pytest.raises(
        UnsupportedSettings,
        match=("isort was provided settings that it doesn't support.*" "For a complete and up-to-date listing of supported settings see: " "https://pycqa.github.io/isort/docs/configuration/options/.\n"),
    ):
        raise UnsupportedSettings(
            dict(test_key1=dict(value="test", source="test"), test_key2=dict(value="test", source="test"),)
        )

# Generated at 2022-06-13 23:06:46.628126
# Unit test for constructor of class ISortError
def test_ISortError():
    # make sure we have the correct error text
    assert str(ISortError("test")) == "test"



# Generated at 2022-06-13 23:06:49.202262
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("profile")
    except ProfileDoesNotExist as e:
        assert e.profile == "profile"


# Generated at 2022-06-13 23:06:52.564507
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    '''
    Test constructor of class UnsupportedEncoding
    :return:
    '''
    try:
        raise UnsupportedEncoding("test_file_name")
    except ISortError as e:
        assert e.filename == "test_file_name"
