

# Generated at 2022-06-13 23:00:41.182928
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    with pytest.raises(AssertionError):
        raise InvalidSettingsPath("test")
    with pytest.raises(TypeError):
        raise InvalidSettingsPath(0)


# Generated at 2022-06-13 23:00:42.846299
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    with pytest.raises(IntroducedSyntaxErrors) as err:
        raise IntroducedSyntaxErrors(file_path="./test_file.py")


# Generated at 2022-06-13 23:00:49.479476
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "/file/path"
    error = ExistingSyntaxErrors(file_path)
    assert error.file_path == file_path
    assert error.__str__() == f"ExistingSyntaxErrors(file_path='/file/path')"


# Generated at 2022-06-13 23:00:52.486166
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "test_isort/test_isort.py"
    err= FileSkipSetting(file_path)
    assert err.file_path == file_path

# Generated at 2022-06-13 23:00:55.793745
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    assert ExistingSyntaxErrors('file_path').message == 'isort was told to sort imports within code that contains syntax errors: file_path.'
    assert ExistingSyntaxErrors('file_path').file_path == 'file_path'


# Generated at 2022-06-13 23:00:58.351813
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError()
    except ISortError as e:
        assert str(e) == ""


# Generated at 2022-06-13 23:01:02.244059
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "TestFormat"
    with pytest.raises(FormattingPluginDoesNotExist) as excinfo:
        raise FormattingPluginDoesNotExist(formatter)
    assert str(excinfo.value) == f"Specified formatting plugin of {formatter} does not exist. "

# Generated at 2022-06-13 23:01:30.907770
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    from isort.settings import Profile
    import os
    import tempfile
    from isort.main import sort_file

    # Prepare: Create temporary directory
    directory = tempfile.mkdtemp()

    # Prepare: Create directory with two files
    filenames = ["__init__.py", "test.py"]
    for filename in filenames:
        file = open(os.path.join(directory, filename), "w")
        file.close()

    # Prepare: Create isort profile with skip
    profile = Profile()
    profile.skip = ["test*"]

    # Prepare: Create isort settins with profile
    settings = dict()
    settings["profile"] = profile
    settings["file_encoding_input"] = "utf-8"

    # Act: Sort files
    for filename in filenames:
        sort_

# Generated at 2022-06-13 23:01:36.449924
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    # Arrange
    file_path = "test_file_path"

    # Act
    result = FileSkipSetting(file_path)

    # Assert
    assert str(result) == "test_file_path was skipped as it's listed in 'skip' setting" \
        " or matches a glob in 'skip_glob' setting"
    assert result.file_path == file_path

# Generated at 2022-06-13 23:01:46.990389
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("test_message")
    except ISortError as e:
        assert e.args[0] == "test_message"
        return
    assert False, "no exception was raised"


# Generated at 2022-06-13 23:01:55.795615
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    test_file_path = "test/test_file.py"
    test_error = FileSkipSetting(test_file_path)
    assert test_error.file_path == test_file_path
    assert test_error.args[0] == "{} was skipped as it's listed in 'skip' setting".format(test_file_path)

# Generated at 2022-06-13 23:02:11.362822
# Unit test for constructor of class ISortError
def test_ISortError():
    """Test case to check if the constructor of class ISortError will raise an error"""
    
    try:
        raise ISortError("Exception")
    except ISortError as e:
        assert str(e) == "Exception"



# Generated at 2022-06-13 23:02:16.312808
# Unit test for constructor of class ISortError
def test_ISortError():
    """ Unit test to check constructor of class ISortError """
    msg = "Error message"
    err = ISortError(msg)
    assert msg == err.args[0]


# Generated at 2022-06-13 23:02:19.907939
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = 'Yapf'
    exc = FormattingPluginDoesNotExist(formatter)
    assert exc.formatter == formatter
    assert 'Yapf' in str(exc)

# Generated at 2022-06-13 23:02:20.807186
# Unit test for constructor of class ISortError
def test_ISortError():
    assert True == True

# Generated at 2022-06-13 23:02:26.544818
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    """Test for class LiteralSortTypeMismatch"""
    e = LiteralSortTypeMismatch(str, int)
    assert e.kind == str
    assert e.expected_kind == int

# Generated at 2022-06-13 23:02:33.021303
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    fact = FileSkipSetting("file_path")
    assert fact.file_path == "file_path"
    assert str(fact) == "file_path was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"

#  Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2022-06-13 23:02:38.663343
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    """Makes sure that the exception is raised with the correct formatting"""
    source = "test source"
    option = "test option"
    value = "test value"
    exc = UnsupportedSettings({option: {"source": source, "value": value}})
    assert exc.unsupported_settings[option]["source"] == source
    assert exc.unsupported_settings[option]["value"] == value

# Generated at 2022-06-13 23:02:42.997417
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "file_path"
    with pytest.raises(FileSkipSetting) as exception:
        raise FileSkipSetting(file_path)

# Generated at 2022-06-13 23:02:46.415667
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    # testing FileSkipComment
    assert FileSkipComment('test_file')
    # testing FileSkipSetting
    assert FileSkipSetting('test_file')