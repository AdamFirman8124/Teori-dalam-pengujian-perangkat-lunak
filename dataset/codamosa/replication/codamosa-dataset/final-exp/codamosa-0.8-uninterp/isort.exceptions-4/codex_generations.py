

# Generated at 2022-06-13 23:01:18.774159
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    original_error = Exception("dump")
    a = AssignmentsFormatMismatch("print('p')")
    assert a.code == "print('p')"
    b = LiteralParsingFailure("print('p')", original_error)
    assert b.code == "print('p')"
    assert b.original_error == original_error
    c = LiteralSortTypeMismatch(type(0), type(1))
    assert c.kind == type(0)
    assert c.expected_kind == type(1)

# Generated at 2022-06-13 23:01:21.332680
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    e = IntroducedSyntaxErrors('example/file.py')
    assert 'example/file.py' in str(e)

# Generated at 2022-06-13 23:01:24.864140
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    with pytest.raises(ExistingSyntaxErrors) as error:
        raise ExistingSyntaxErrors('test')
    assert error.value.file_path == 'test'


# Generated at 2022-06-13 23:01:27.945006
# Unit test for constructor of class ISortError
def test_ISortError():
    e = ISortError("")
    assert e.__str__() == ""



# Generated at 2022-06-13 23:01:33.123429
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    try:
        raise FileSkipComment('Filepath')
    except FileSkipComment as error:
        assert error.message == "Filepath contains an file skip comment and was skipped."
        assert error.file_path == 'Filepath'

# Generated at 2022-06-13 23:01:52.875475
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    assert 'foo.py was skipped as it\'s listed in \'skip\' setting or matches a glob in \'skip_glob\' setting' == FileSkipSetting('foo.py').__str__()

    assert 'foo.py was skipped as it\'s listed in \'skip\' setting or matches a glob in \'skip_glob\' setting' == FileSkipSetting('./foo.py').__str__()


# Generated at 2022-06-13 23:02:14.035406
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("test")
    except ProfileDoesNotExist as e:
        assert str(e) == "Specified profile of test does not exist. Available profiles: black,pycharm,pytest,test,test_v4,test_v4_pycharm-style,test_v4_typing. Available profiles: black,pycharm,pytest,test,test_v4,test_v4_pycharm-style,test_v4_typing."
        assert e.profile == "test"

# Generated at 2022-06-13 23:02:15.791723
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError('This is a custom error message')
    except ISortError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 23:02:18.666175
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    with pytest.raises(FormattingPluginDoesNotExist):
        raise FormattingPluginDoesNotExist("formatter")



# Generated at 2022-06-13 23:02:24.329973
# Unit test for constructor of class MissingSection
def test_MissingSection():
    exception = MissingSection("my_module", "my_section")
    assert str(exception) == (
        "Found my_module import while parsing, but "
        "my_section was not included in the `sections` "
        "setting of your config. Please add it before "
        "continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )

# Generated at 2022-06-13 23:02:27.910869
# Unit test for constructor of class ISortError
def test_ISortError():
    isortError = ISortError()



# Generated at 2022-06-13 23:02:29.852260
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    x = FileSkipSetting('testfile/path')
    assert x.file_path == 'testfile/path'

test_FileSkipSetting()

# Generated at 2022-06-13 23:02:33.474389
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("message")
    except ISortError as e:
        message = e.args[0]
        assert message == "message"



# Generated at 2022-06-13 23:02:35.228454
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert InvalidSettingsPath is None


# Generated at 2022-06-13 23:02:39.147474
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("test")
    except ExistingSyntaxErrors as e:
        assert  e.file_path == "test"
        print(e)


# Generated at 2022-06-13 23:02:42.120496
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    path = "C://Desktop/USER"
    ex = InvalidSettingsPath(path)
    assert ex.settings_path == path


# Generated at 2022-06-13 23:02:50.384705
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    import unittest.mock
    from .sort_imports import FileSkipComment
    g_file_path = "file_path"
    g_exception = FileSkipComment(file_path=g_file_path)
    assert g_exception.file_path == g_file_path
    assert g_exception.message == f"{g_file_path} contains an file skip comment and was skipped."

# Generated at 2022-06-13 23:02:54.271947
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    instance = FileSkipComment(file_path=r"F:\PC\CODE\test\test.py")
    assert isinstance(instance, ISortError)

test_FileSkipComment()

# Generated at 2022-06-13 23:02:55.903631
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
	value = LiteralParsingFailure('code', 'original_error')

# Generated at 2022-06-13 23:02:57.844223
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    assert FormattingPluginDoesNotExist("formatter").formatter == "formatter"

# Generated at 2022-06-13 23:03:02.852089
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
  message = "abc"
  file_path = "./test"
  f = FileSkipped(message, file_path)
  assert f.args[0] == message
  assert f.file_path == file_path

# Generated at 2022-06-13 23:03:03.994381
# Unit test for constructor of class ISortError
def test_ISortError():
    e = ISortError()
    assert e.args == ()


# Generated at 2022-06-13 23:03:09.176927
# Unit test for constructor of class ISortError
def test_ISortError():

    a = ISortError()
    b = ISortError()
    c = ISortError()

    assert a is not None
    assert b is not None
    assert c is not None



# Generated at 2022-06-13 23:03:11.082980
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2022-06-13 23:03:12.911913
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    exception = ExistingSyntaxErrors("error")
    assert isinstance(exception, ISortError)

# Generated at 2022-06-13 23:03:15.173656
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    error = AssignmentsFormatMismatch("foo")
    assert "isort was told to sort a section of assignments" in error.__str__()

# Generated at 2022-06-13 23:03:18.166546
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    with pytest.raises(FileSkipComment) as excinfo:
        raise FileSkipComment('test/test_file')
    assert str(excinfo.value) == 'test/test_file contains an file skip comment and was skipped.'


# Generated at 2022-06-13 23:03:20.629599
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    a = LiteralSortTypeMismatch
    print(a)

# Generated at 2022-06-13 23:03:23.746503
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    error = UnsupportedEncoding("test.py")
    assert str(error) == "Unknown or unsupported encoding in test.py"
    assert error.filename == "test.py"

# Generated at 2022-06-13 23:03:29.192213
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("test profile")
    except ProfileDoesNotExist as e:
        assert e.profile == "test profile"
        assert str(e) == "Specified profile of test profile does not exist. " \
            "Available profiles: black,pycharm,pep8,mypy,google,pydev,jupyter"


# Generated at 2022-06-13 23:03:38.587334
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    # Arrange
    file_path = "test.txt"

    # Act
    exception = IntroducedSyntaxErrors(file_path)

    # Assert
    assert str(exception) == "isort introduced syntax errors when attempting to sort the imports contained within test.txt."
    assert exception.file_path == "test.txt"

# Generated at 2022-06-13 23:03:39.863979
# Unit test for constructor of class ISortError
def test_ISortError():
    assert ISortError
    assert ISortError.__init__


# Generated at 2022-06-13 23:03:47.591378
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    try:
        raise FileSkipSetting(file_path = 'test_file.py')
    except FileSkipSetting as e:
        assert str(e) == 'test_file.py was skipped as it\'s listed in \'skip\' setting' \
                         ' or matches a glob in \'skip_glob\' setting'

# Generated at 2022-06-13 23:03:49.672425
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    test = LiteralSortTypeMismatch(int, str)
    assert test != LiteralSortTypeMismatch(int, str), "Failed to instantiate LiteralSortTypeMismatch"

# Generated at 2022-06-13 23:03:55.635236
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "test_data"
    original_error = ValueError('Failed to parse test_data')
    try:
        raise LiteralParsingFailure(code, original_error)
    except LiteralParsingFailure as e:
        assert e.original_error == original_error
        assert e.code == code

# Generated at 2022-06-13 23:04:01.274352
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "file.py"
    file_skipped = FileSkipComment(file_path)
    assert file_skipped.file_path == file_path
    assert file_skipped.message == f"{file_path} contains an file skip comment and was skipped."


# Generated at 2022-06-13 23:04:04.943678
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        raise MissingSection("foo", "bar")
    except MissingSection as e:
        assert "foo" in str(e)
        assert "bar" in str(e)

# Generated at 2022-06-13 23:04:07.425937
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    e = InvalidSettingsPath("nonexistent.file")
    assert e.settings_path == "nonexistent.file"



# Generated at 2022-06-13 23:04:15.909556
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    literal_parsing_failure = LiteralParsingFailure("code","original_error")
    expected = "isort failed to parse the given literal code. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of original_error."
    assert literal_parsing_failure.args[0] == expected
    print("Passed test for LiteralParsingFailure constructor.")


# Generated at 2022-06-13 23:04:18.823425
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    with pytest.raises(LiteralSortTypeMismatch): 
        raise LiteralSortTypeMismatch('int', 'str')

# Generated at 2022-06-13 23:04:37.072044
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "file_path"
    test_object = FileSkipComment(file_path)
    assert type(test_object) == FileSkipComment
    assert isinstance(test_object, FileSkipped)
    assert isinstance(test_object, ISortError)
    assert test_object.file_path == file_path
    assert test_object.args == (
        f"{file_path} contains an file skip comment and was skipped.",
    )
    assert str(test_object) == (
        f"{file_path} contains an file skip comment and was skipped."
    )



# Generated at 2022-06-13 23:04:39.575935
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    assert ProfileDoesNotExist(profile='asdf')


# Generated at 2022-06-13 23:04:44.544344
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    file_path = "D:/MCA/sem_2/PES/isort-4.3.21/isort/settings.py"
    message = "D:/MCA/sem_2/PES/isort-4.3.21/isort/settings.py contains an file skip comment and was skipped."
    try:
        raise FileSkipped(message, file_path)
    except FileSkipped as e:
        assert e.file_path == file_path
        assert e.message == message


# Generated at 2022-06-13 23:04:48.670818
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = 'Message'
    file_path = 'path/file'
    file_skipped = FileSkipped(message, file_path)

    assert file_skipped.message == message
    assert file_skipped.file_path == file_path

# Generated at 2022-06-13 23:04:51.484980
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting("file_path")
    except FileSkipSetting as error:
        print(error.file_path)


# Generated at 2022-06-13 23:04:56.138423
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting('somefile.txt')
    except FileSkipSetting as e:
        assert e.file_path == 'somefile.txt'
        assert e.message == 'somefile.txt was skipped as it\'s listed in \'skip\' setting or matches a glob in \'skip_glob\' setting'

# Generated at 2022-06-13 23:04:59.012174
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    print("Test for constructor of class FormattingPluginDoesNotExist")
    formatter = 'FORMATTER'
    Error = FormattingPluginDoesNotExist(formatter)
    

# Generated at 2022-06-13 23:05:00.742097
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    assert FileSkipSetting("")

# Generated at 2022-06-13 23:05:03.836708
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        print("Testing LiteralParsingFailure()")
        string = "{"
        raise Exception("Test Exception")
    except Exception as e:
        LiteralParsingFailure(string, e)

# Generated at 2022-06-13 23:05:07.427412
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    filename = 'foo'
    file_error = FileSkipSetting(filename)
    assert file_error.file_path == filename
    assert file_error.__str__() == f"{filename} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

# Generated at 2022-06-13 23:05:24.105035
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    new_object=FileSkipComment("path")
    assert new_object is not None


# Generated at 2022-06-13 23:05:26.822278
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {'bad_setting': {'value': 1, 'source': 'cli'}}
    settings_error = UnsupportedSettings(unsupported_settings)
    assert settings_error.unsupported_settings == unsupported_settings

# Generated at 2022-06-13 23:05:33.145103
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(False, int)
    except LiteralSortTypeMismatch as e:
        assert str(e) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'bool'>"

# Generated at 2022-06-13 23:05:39.979005
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    def throwing_function():
        raise Exception("This is a test exception")
    exception = Exception("This is a test exception")
    try:
        throwing_function()
    except Exception:
        exception = ISortError("This is a isort exception")
    assert exception.__str__() == "This is a isort exception"

# Generated at 2022-06-13 23:05:42.833855
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    error = LiteralParsingFailure('bad_code', Exception('error'))
    assert error.code == 'bad_code'
    assert error.original_error.args == ('error',)

# Generated at 2022-06-13 23:05:47.073298
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    encoding_error = "Unknown or unsupported encoding in mystuff.txt"
    filename = "mystuff.txt"
    assert UnsupportedEncoding(filename).__str__() == encoding_error

# Generated at 2022-06-13 23:05:49.865940
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    instance = LiteralSortTypeMismatch("a", "b")
    assert instance.kind == "a"
    assert instance.expected_kind == "b"

# Generated at 2022-06-13 23:05:56.240618
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    # Arrange
    code = """('foo', 'bar')"""
    original_error = IndexError()
    # Act
    try:
        raise LiteralParsingFailure(code, original_error)
    except LiteralParsingFailure as e:
        # Assert
        assert e.code == code
        assert e.original_error == original_error

# Generated at 2022-06-13 23:06:00.661533
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    try:
        raise FileSkipComment("test.py")
    except FileSkipComment as e:
        assert str(e) == "test.py contains an file skip comment and was skipped."
        assert e.file_path == "test.py"
        assert isinstance(e, ISortError)

# Generated at 2022-06-13 23:06:05.378228
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    """Tests that constructor raises exception if the provided settings path does not exist"""
    with pytest.raises(InvalidSettingsPath):
        InvalidSettingsPath('tests/not-a-real-file')

