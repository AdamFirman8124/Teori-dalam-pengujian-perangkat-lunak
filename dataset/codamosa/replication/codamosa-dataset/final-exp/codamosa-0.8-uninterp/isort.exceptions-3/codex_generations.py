

# Generated at 2022-06-13 23:00:29.373365
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    message = "file_path was skipped as it's listed in 'skip' setting"
    file_path = "src/file_skip_setting.py"
    assert FileSkipSetting(file_path) == (message, file_path)


# Generated at 2022-06-13 23:00:33.899435
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    with pytest.raises(LiteralSortTypeMismatch) as exception_info:
        raise LiteralSortTypeMismatch(kind=type(16), expected_kind=type(1))
    assert "isort was told to sort a literal of type <class 'int'>" in str(
        exception_info.value
    )

# Generated at 2022-06-13 23:00:35.576864
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("error")
    except ISortError as e:
        assert str(e) == "error"


# Generated at 2022-06-13 23:00:38.515168
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    FileSkipSetting("/Path/to/file")

# Generated at 2022-06-13 23:00:43.333710
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("test.py")
    except UnsupportedEncoding as err:
        assert err.filename == "test.py"

# Generated at 2022-06-13 23:00:49.070829
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        raise LiteralParsingFailure("123", Exception("mock exception"))
    except LiteralParsingFailure as e:
        assert e.code == "123"
        assert e.original_error == Exception("mock exception")


# Generated at 2022-06-13 23:00:52.944336
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    mock_path = "path/to/file"
    message = "message"
    error = FileSkipped(message, mock_path)

    assert error.message == message
    assert error.file_path == mock_path



# Generated at 2022-06-13 23:00:54.317253
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    UnsupportedSettings.__init__({"a": 1})



# Generated at 2022-06-13 23:01:01.251979
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    """
    Unit test for constructor of class AssignmentsFormatMismatch
    """
    try:
        raise AssignmentsFormatMismatch("")
    except AssignmentsFormatMismatch as error:
        assert str(error) == "isort was told to sort a section of assignments, however the given code:\n\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n\n"

# Generated at 2022-06-13 23:01:22.267522
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    e = FileSkipComment("some.py")
    assert e.message == "some.py contains an file skip comment and was skipped."
    assert e.file_path == "some.py"

# Generated at 2022-06-13 23:01:33.390481
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        raise MissingSection("a", "b")
    except MissingSection as e:
        assert e.import_module == "a"
        assert e.section == "b"
        assert str(e) == ("Found a import while parsing, but b was not "
                          "included in the `sections` setting of your "
                          "config. Please add it before continuing\n"
                          "See https://pycqa.github.io/isort/#custom-sections"
                          "-and-ordering for more info.")



# Generated at 2022-06-13 23:01:48.586161
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    target = UnsupportedSettings(
        {"force_to_top": {"value": "test", "source": "test2"}}
    )
    assert target.unsupported_settings is not None

# Generated at 2022-06-13 23:01:53.786342
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("test")
    except IntroducedSyntaxErrors as ex:
        assert ex.file_path == "test"
        print("IntroducedSyntaxErrors test passed!")


# Generated at 2022-06-13 23:02:06.452333
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    exception = IntroducedSyntaxErrors('filePath')
    assert isinstance(exception, ISortError)
    assert exception.file_path == 'filePath'


# Generated at 2022-06-13 23:02:11.462019
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist("formatter123")
    except FormattingPluginDoesNotExist as ex:
        assert ex.formatter == "formatter123"


# Generated at 2022-06-13 23:02:23.610614
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    print("    * Run the testcase of AssignmentsFormatMismatch")
    # test-1
    code = "lazy_foo = 'abc'\n" \
           "lazy_bar = 'def'\n" \
           "lazy_baz = 'ghi'\n"
    result = AssignmentsFormatMismatch(code)

# Generated at 2022-06-13 23:02:29.319084
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    with pytest.raises(ExistingSyntaxErrors(file_path = "file_path")) as exc:
        raise ExistingSyntaxErrors(file_path = 'file_path')
    assert str(exc.value) == "isort was told to sort imports within code that contains syntax errors: file_path."
    assert exc.value.file_path == 'file_path'


# Generated at 2022-06-13 23:02:32.640455
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        int("hello")
    except ValueError as e:
        raise LiteralParsingFailure("hello", e)

# Generated at 2022-06-13 23:02:33.735569
# Unit test for constructor of class ISortError
def test_ISortError():
    ISortError('message')

# Generated at 2022-06-13 23:02:38.262372
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    # object created with message and code
    code = "a = 0\nb = 1\n"
    object1 = AssignmentsFormatMismatch(code)
    self.assertIsNotNone(object1)
    self.assertEqual(object1.code, code)