

# Generated at 2022-06-13 23:00:30.440856
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    class customException(Exception):
        pass
    try:
        raise UnsupportedSettings({"test_setting":"test_setting_value"})
    except Exception as e:
        if not(str(e).__contains__("isort was provided settings that it doesn't support")):
            raise customException

# Generated at 2022-06-13 23:00:35.097990
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "test message"
    file_path = "test file path"

    class TestError(FileSkipped):
        def __init__(self, file_path):
            super().__init__(message, file_path)
    try:
        raise TestError(file_path)
    except TestError as e:
        assert str(e) == message
        assert e.message == message
        assert e.file_path == file_path

# Generated at 2022-06-13 23:00:37.810124
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    f1 = IntroducedSyntaxErrors('/hello/world')
    assert f1.file_path == '/hello/world'

# Generated at 2022-06-13 23:00:45.173497
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting('abc.py')
    except FileSkipSetting as e:
        assert isinstance(e, ISortError)
        assert isinstance(e, FileSkipped)
        assert e.file_path == 'abc.py'

# Generated at 2022-06-13 23:00:51.541418
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    a = ExistingSyntaxErrors("/tmp/hello.py")
    assert "isort was told to sort imports within code that contains syntax errors: /tmp/hello.py." == a.args[0]
    assert "/tmp/hello.py" == a.file_path

# Generated at 2022-06-13 23:00:53.831939
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    f = FileSkipped("reason", "file")
    assert f.message == "reason"
    assert f.file_path == "file"

# Generated at 2022-06-13 23:00:56.632050
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("ISortError_test")
    except ISortError as e:
        assert e.args[0] == "ISortError_test"


# Generated at 2022-06-13 23:01:00.681637
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = '/home/david/tulip/isort/isort/settings_path.py'
    try:
        raise InvalidSettingsPath(settings_path)
    except InvalidSettingsPath as error:
        assert error.settings_path == settings_path

# Generated at 2022-06-13 23:01:24.700287
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "code"
    original_error = Exception("error")
    literal_parsing_failure = LiteralParsingFailure(code, original_error)
    assert literal_parsing_failure.code == code
    assert literal_parsing_failure.original_error == original_error



# Generated at 2022-06-13 23:01:28.477021
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("Error!")
    except ISortError as e:
        assert str(e) == "Error!"


# Generated at 2022-06-13 23:01:32.621673
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    with pytest.raises(AssignmentsFormatMismatch) as error:
        raise AssignmentsFormatMismatch("hello")

    assert error.value.code == "hello"


# Generated at 2022-06-13 23:01:49.549921
# Unit test for constructor of class ISortError
def test_ISortError():
    # Create a new instance of ISortError
    isort_error = ISortError("Message for the exception")

    # Check the value of the instance variables.
    assert isort_error.args[0] == "Message for the exception"


# Generated at 2022-06-13 23:01:54.658437
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("/home/Test.py")
    except Exception as e:
        assert type(e) == ExistingSyntaxErrors
        assert e.file_path == "/home/Test.py"

# Generated at 2022-06-13 23:02:07.958517
# Unit test for constructor of class MissingSection
def test_MissingSection():
    assert MissingSection("test1", "test2")
    assert MissingSection("test1", "test2").import_module == "test1"
    assert MissingSection("test1", "test2").section == "test2"
    assert MissingSection("test1", "test2").args == ("test1", "test2")



# Generated at 2022-06-13 23:02:08.629791
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    assert IntroducedSyntaxErrors(file_path="a")


# Generated at 2022-06-13 23:02:12.371956
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("hello")
    except ISortError as e:
        assert isinstance(e, ISortError)
        assert isinstance(e, UnsupportedEncoding)

# Generated at 2022-06-13 23:02:17.035052
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = 'a'
    exception = FileSkipSetting(file_path)
    assert exception.message == "a was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Generated at 2022-06-13 23:02:22.128676
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    message = "isort failed to parse the given literal []. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of cannot use list literals."
    test_instance = LiteralParsingFailure(code="", original_error=Exception())
    assert test_instance.args[0] == message


# Generated at 2022-06-13 23:02:24.219930
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    error = LiteralParsingFailure("code", "original_error")
    assert error.code == "code"
    assert error.original_error == "original_error"



# Generated at 2022-06-13 23:02:27.915482
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("test")
    except ProfileDoesNotExist as exception:
        assert isinstance(exception, ProfileDoesNotExist)
        assert exception.profile == "test"


# Generated at 2022-06-13 23:02:33.683146
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist("Hello World")
    except FormattingPluginDoesNotExist as error:
        assert error.formatter == "Hello World"



# Generated at 2022-06-13 23:02:40.681481
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    # test set up
    kind = str
    expected_kind = str
    expected_msg = "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'str'>"

    # trigger
    instance = LiteralSortTypeMismatch(expected_kind=str, kind=str)

    # assert
    assert isinstance(instance, LiteralSortTypeMismatch)
    assert str(instance) == expected_msg
    assert instance.kind == kind
    assert instance.expected_kind == expected_kind


test_LiteralSortTypeMismatch()

# Generated at 2022-06-13 23:02:46.627547
# Unit test for constructor of class MissingSection
def test_MissingSection():
    sec = 'TESTSECTION'
    imp = 'TESTIMPORT'
    msg = str(MissingSection(imp, sec))
    assert sec in msg
    assert imp in msg
    assert 'TESTIMPORT import while parsing, but TESTSECTION was not included ' in msg

# Generated at 2022-06-13 23:02:49.941212
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(int, str)
    except LiteralSortTypeMismatch as e:
        assert repr(e)

# Generated at 2022-06-13 23:03:00.358924
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    output = str(UnsupportedSettings({
        "option1": {
            "value": "foo",
            "source": ".isort.cfg",
        },
    }))
    expected = (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- option1 = foo  (source: '.isort.cfg')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert output == expected

# Generated at 2022-06-13 23:03:03.220466
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "/path/to/file.py"
    error = ExistingSyntaxErrors(file_path)
    assert error.file_path == file_path
    assert (
        str(error)
        == "isort was told to sort imports within code that contains syntax errors: /path/to/file.py."
    )



# Generated at 2022-06-13 23:03:07.942502
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("testfile")
    except IntroducedSyntaxErrors as error:
        assert error.file_path == "testfile"
        assert "testfile" in str(error)

# Generated at 2022-06-13 23:03:09.510335
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "path/to/file"
    FileSkipComment(file_path)

# Generated at 2022-06-13 23:03:12.763047
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("test.py")
    except UnsupportedEncoding as e:
        assert e.filename == "test.py"

# Generated at 2022-06-13 23:03:15.411270
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    raised = False
    try:
        raise IntroducedSyntaxErrors("fname")
    except IntroducedSyntaxErrors:
        raised = True
    assert raised is True
