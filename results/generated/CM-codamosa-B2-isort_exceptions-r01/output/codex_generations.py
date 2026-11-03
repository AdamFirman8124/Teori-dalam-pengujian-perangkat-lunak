

# Generated at 2026-11-02 15:25:07.480246
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    """Test constructor of class AssignmentsFormatMismatch."""
    code = "x = 1\ny = 2"
    exception = AssignmentsFormatMismatch(code)

    assert isinstance(exception, ISortError)
    assert exception.code == code
    assert code in str(exception)
    assert "isort was told to sort a section of assignments" in str(exception)
    assert "Does not match isort's strict single line formatting requirement" in str(exception)

# Generated at 2026-11-02 15:27:38.980099
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():from isort.exceptions import InvalidSettingsPath


# Generated at 2026-11-02 15:29:10.263796
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    from pathlib import Path

    # Test construction with a string filename
    filename_str = "example.py"
    exception_str = UnsupportedEncoding(filename_str)

    assert exception_str.filename == filename_str
    assert isinstance(exception_str.filename, str)
    assert f"Unknown or unsupported encoding in {filename_str}" == str(exception_str)
    assert isinstance(exception_str, UnsupportedEncoding)
    assert isinstance(exception_str, ISortError)
    assert isinstance(exception_str, Exception)

    # Test construction with a Path filename
    filename_path = Path("some") / "module.py"
    exception_path = UnsupportedEncoding(filename_path)

    assert exception_path.filename == filename_path
    assert isinstance(exception_path.filename, Path)
    assert f"Unknown or unsupported encoding in {filename_path}" == str(exception_path)
    assert isinstance(exception_path, UnsupportedEncoding)
    assert isinstance(exception_path, ISortError)
    assert isinstance(exception_path, Exception)

    # Ensure the message can be raised and caught properly
    try:
        raise UnsupportedEncoding(filename_path)
    except ISortError as caught:
        assert caught.filename == filename_path
    else:
        raise AssertionError("Expected UnsupportedEncoding to be raised as ISortError")

# Generated at 2026-11-02 15:30:13.934499
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    from isort.exceptions import FileSkipped, ISortError

    message = "test file was skipped"
    file_path = "test_file.py"

    error = FileSkipped(message, file_path)

    # Verify the error is an instance of FileSkipped and ISortError
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Verify attributes are set correctly
    assert error.file_path == file_path
    assert str(error) == message
    assert error.args == (message,)

# Generated at 2026-11-02 15:31:16.586793
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    from isort.exceptions import FileSkipSetting, FileSkipped, ISortError

    file_path = "example.py"
    exception = FileSkipSetting(file_path)

    assert exception.file_path == file_path
    assert str(exception) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert isinstance(exception, FileSkipSetting)
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
# nonce:7f2a84ff