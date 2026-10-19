

# Generated at 2022-06-13 23:01:18.774455
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        a = MissingSection("django.views.generic","django")
    except:
        print("Failed")
    else:
        print("Passed")

test_MissingSection()

# Generated at 2022-06-13 23:01:23.757896
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("file_path")
    except ExistingSyntaxErrors as e:
        assert e.file_path == "file_path"
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: file_path."

# Generated at 2022-06-13 23:01:28.162712
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    path = "/home/foo/bar"
    try:
        raise ExistingSyntaxErrors(path)
    except ExistingSyntaxErrors as e:
        assert e.file_path == path

# Generated at 2022-06-13 23:01:30.907871
# Unit test for constructor of class MissingSection
def test_MissingSection():
    m = MissingSection('foo', 'bar')
    assert(str(m).startswith('Found foo import while parsing, but bar was not included in the `sections` setting of your config.'))

# Generated at 2022-06-13 23:01:34.735013
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("test.py")
    except IntroducedSyntaxErrors as e:
        assert isinstance(e, IntroducedSyntaxErrors)
        assert e.file_path == "test.py"


# Generated at 2022-06-13 23:01:52.290696
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    import ast
    from .known_errors import LiteralParsingFailure
    try:
        ast.literal_eval("{'foo': 'bar'}")
    except SyntaxError as ex:
        assert isinstance(ex, SyntaxError)
        assert isinstance(LiteralParsingFailure("{'foo': 'bar'}", ex), LiteralParsingFailure)

# Generated at 2022-06-13 23:02:12.702927
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    # Given
    kind = type
    expected_kind = type

    # When
    try:
        raise LiteralSortTypeMismatch(kind, expected_kind)
    except LiteralSortTypeMismatch as error:
        # Then
        assert str(error) == "isort was told to sort a literal of type <class 'type'> but was given a literal of type <class 'type'>."

# Generated at 2022-06-13 23:02:15.919043
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath('E:\isort')
    except InvalidSettingsPath:
        print('Exception: invalid settings path')


# Generated at 2022-06-13 23:02:25.598575
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    from pathlib import Path
    from .profiles import profiles

    settings_path = "E:/Downloads/config/isort.cfg"
    file_path = "E:/Downloads/isort.py"
    profile = "black"
    formatter = "black"
    kind = "settings"
    expected_kind = "syntax error"

    def raise_exception():
        raise Exception("Something went wrong")


# Generated at 2022-06-13 23:02:29.925004
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    error = ExistingSyntaxErrors("/home/user/test.py")
    assert error.file_path == "/home/user/test.py"
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "/home/user/test.py."
    )
    

# Generated at 2022-06-13 23:02:37.443786
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "./path/to/my/file.py"
    try:
        raise ExistingSyntaxErrors(file_path)
    except ExistingSyntaxErrors as e:
        assert e.file_path == file_path
    else:
        assert False

# Tests for constructor of class FileSkipped

# Generated at 2022-06-13 23:02:38.283397
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    e = E

# Generated at 2022-06-13 23:02:44.334857
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    invalid_settings_path = InvalidSettingsPath(settings_path="test")
    assert invalid_settings_path.settings_path == "test"
    assert str(invalid_settings_path) == "isort was told to use the settings_path: test as the base directory or file that represents the starting point of config file discovery, but it does not exist."



# Generated at 2022-06-13 23:02:45.996733
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    assert UnsupportedEncoding("filename").filename == "filename"

# Generated at 2022-06-13 23:02:49.871283
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    exception = FileSkipped("Skipped", "file_path")
    assert exception.message == "Skipped"
    assert exception.file_path == "file_path"


# Generated at 2022-06-13 23:02:54.671627
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = '/home/a/test2.py'
    try:
        raise ExistingSyntaxErrors(file_path)
    except ExistingSyntaxErrors:
        pass

# Generated at 2022-06-13 23:03:02.271214
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        raise LiteralParsingFailure("{ 1 , 2 }", "error")
    except LiteralParsingFailure as e:
        assert e.args[0] == "isort failed to parse the given literal { 1 , 2 }. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of error."
        assert e.code == "{ 1 , 2 }"
        assert e.original_error == "error"


# Generated at 2022-06-13 23:03:02.789087
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    pass



# Generated at 2022-06-13 23:03:03.724963
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    encoding = UnsupportedEncoding(filename="example.py")

# Generated at 2022-06-13 23:03:05.588676
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    class_instance = FileSkipComment("file_path")
    assert class_instance.__class__ == FileSkipComment
    assert class_instance.file_path == "file_path"

# Generated at 2022-06-13 23:03:11.253009
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    with pytest.raises(LiteralSortTypeMismatch) as e:
        e = LiteralSortTypeMismatch(kind=1, expected_kind=2)
    assert e.kind == 1
    assert e.expected_kind == 2


# Generated at 2022-06-13 23:03:14.639180
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    error = FileSkipSetting("test/path")
    assert error.message == "test/path was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
    assert error.file_path == "test/path"


# Generated at 2022-06-13 23:03:15.984336
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    assert AssignmentsFormatMismatch("a, b, c")

# Generated at 2022-06-13 23:03:18.136440
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("test.py")
    except ExistingSyntaxErrors as e:
        assert e.file_path == "test.py"


# Generated at 2022-06-13 23:03:22.505851
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    result = UnsupportedSettings({"test": {"value": "test", "source": "test"}})
    assert result.unsupported_settings == {"test": {"value": "test", "source": "test"}}

# Generated at 2022-06-13 23:03:24.960597
# Unit test for constructor of class ISortError
def test_ISortError():
    """Testing constructor"""

    try:
        raise ISortError
    except ISortError:
        pass

# Generated at 2022-06-13 23:03:28.488802
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        line = 1/0
    except ZeroDivisionError as e:
        line = e
    filename = "test.py"
    code = IntroducedSyntaxErrors(filename)
    assert code.file_path == filename



# Generated at 2022-06-13 23:03:30.341081
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError()
    except ISortError:
        pass



# Generated at 2022-06-13 23:03:42.327147
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        raise LiteralParsingFailure("a {0}".format("b"), Exception("Syntax error"))
    except Exception as e:
        assert str(e) == "isort failed to parse the given literal a b. It's important to note that isort literal sorting only supports simple literals parsable by ast.literal_eval which gave the exception of Syntax error."
        assert e.code == "a b"
        assert str(e.original_error) == "Syntax error"


# Generated at 2022-06-13 23:03:43.355392
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    assert FileSkipSetting('some/path')