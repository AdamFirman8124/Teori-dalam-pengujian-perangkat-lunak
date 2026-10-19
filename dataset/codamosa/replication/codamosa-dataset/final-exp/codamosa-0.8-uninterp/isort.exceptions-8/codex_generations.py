

# Generated at 2022-06-13 23:00:44.020867
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting('path/to/file')
    except FileSkipSetting as e:
        assert str(e) == 'path/to/file was skipped as it\'s listed in \'skip\' setting' \
                           ' or matches a glob in \'skip_glob\' setting'
        assert e.file_path == 'path/to/file'

# Generated at 2022-06-13 23:00:53.558601
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {"test_attr": {"value": "value", "source": "source"}}
    setting_error = UnsupportedSettings(unsupported_settings)
    expected = "isort was provided settings that it doesn't support:\n\n"\
               "\t- test_attr = value  (source: 'source')\n\n"\
               "For a complete and up-to-date listing of supported settings see: " \
               "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    assert setting_error.args[0] == expected

# Generated at 2022-06-13 23:00:56.087196
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "x = 1\ny = 2\nz = a + b"
    error = AssignmentsFormatMismatch(code)
    assert error.code == code

# Generated at 2022-06-13 23:00:58.526113
# Unit test for constructor of class ISortError
def test_ISortError():
    a = ISortError("Test for ISortError")
    assert str(a) == "Test for ISortError"


# Generated at 2022-06-13 23:01:02.290910
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    try:
        file_path = "test.py"
        raise FileSkipComment(file_path=file_path)
    except FileSkipComment as exc:
        assert exc.file_path == file_path
        assert str(exc) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2022-06-13 23:01:21.358347
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    """Unit test for constructor of class LiteralSortTypeMismatch"""

    def test_different_type_raise_exception():
        """Unit test for LiteralSortTypeMismatch.__init__ method"""
        try:
            raise LiteralSortTypeMismatch(type(8), type("hi"))
        except Exception as exception:
            assert isinstance(exception, LiteralSortTypeMismatch)

    test_different_type_raise_exception()

# Generated at 2022-06-13 23:01:25.535058
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "name = \"Akash\""
    exp_code = "\nname = \"Akash\"\n"
    actual_code = "\n".join(AssignmentsFormatMismatch(code).code.split()[4:])
    assert exp_code == actual_code

# Generated at 2022-06-13 23:01:29.329182
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors('test')
    except IntroducedSyntaxErrors as e:
        assert(e.file_path == 'test')

# Generated at 2022-06-13 23:01:32.352373
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = """
    a = 1
    bb = 2
    ccc"""
    try:
        raise AssignmentsFormatMismatch(code)
    except AssignmentsFormatMismatch as m:
        assert code in str(m)

# Generated at 2022-06-13 23:01:51.965626
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("/path/to/file.py")
    except Exception as err:
        assert err.args[0] == (
            "/path/to/file.py was skipped as it contains syntax errors. "
            "Please fix these before running isort."
        )
        assert err.file_path == "/path/to/file.py"