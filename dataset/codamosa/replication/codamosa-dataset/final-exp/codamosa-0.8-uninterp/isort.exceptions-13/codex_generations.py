

# Generated at 2022-06-13 23:00:31.377167
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    test_input = {"unsupported_setting": {"value": "test_value", "source": "test_source"}}
    unsupported_setting = UnsupportedSettings(test_input)
    assert unsupported_setting.unsupported_settings == test_input

# Generated at 2022-06-13 23:00:37.823378
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    """Testing the constructor of UnsupportedSettings"""
    with pytest.raises(UnsupportedSettings) as exception:
        UnsupportedSettings({"obviously_not_real": "obviously_not_real"})
        error_message = f"isort was provided settings that it doesn't support:\n\n\t- obviously_not_real = obviously_not_real  (source: 'None')\n\nFor a complete and up-to-date listing of supported settings see: https://pycqa.github.io/isort/docs/configuration/options/.\n"
        assert str(exception.value) == error_message
        assert exception.value.unsupported_settings == {"obviously_not_real": "obviously_not_real"}


# Generated at 2022-06-13 23:00:39.973762
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    exception = FileSkipped("hello", "world.py")

    assert exception.message == "hello"
    assert exception.file_path == "world.py"

# Generated at 2022-06-13 23:00:42.205662
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("")
    except InvalidSettingsPath as invalidSettingsPath:
        print(invalidSettingsPath)

# Generated at 2022-06-13 23:00:51.462340
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    import os
    import pytest
    from isort.exceptions import IntroducedSyntaxErrors

    # pytest.raises(ExceptionClass, ExceptionCall, *args)
    with pytest.raises(IntroducedSyntaxErrors, match=r"isort introduced syntax errors"):
        # raising object of class IntroducesSyntaxErrors
        raise IntroducedSyntaxErrors(f"{os.getcwd()}/examples/examples_1.py")

# Generated at 2022-06-13 23:00:53.365912
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "/path/to/file.py"
    FileSkipComment(file_path)

# Generated at 2022-06-13 23:00:56.215238
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    err = LiteralParsingFailure("test code", SyntaxError("Invalid syntax"))
    assert "test code" == err.code
    assert isinstance(err.original_error, SyntaxError)

# Generated at 2022-06-13 23:00:57.381869
# Unit test for constructor of class ISortError
def test_ISortError():
    assert ISortError()


# Generated at 2022-06-13 23:01:00.060915
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("/some/file")
    except IntroducedSyntaxErrors as error:
        assert error.file_path == "/some/file"

# Generated at 2022-06-13 23:01:25.047803
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    from isort.main import _skip_file
    try:
        _skip_file('pathlib.py')
    except FileSkipped as error:
        assert error.file_path == 'pathlib.py'
        assert str(error) == "pathlib.py was skipped as it's listed in 'skip' setting" \
                             " or matches a glob in 'skip_glob' setting"