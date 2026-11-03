

# Generated at 2026-11-02 13:50:49.383942
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "src/example.py"

    exception = FileSkipSetting(file_path)

    # The file path should be stored as an attribute
    assert exception.file_path == file_path

    # The message should match the expected skip message
    assert str(exception) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

    # It should inherit from FileSkipped and ISortError
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)

    # It should be raisable and catchable, preserving file_path
    with pytest.raises(FileSkipSetting) as exc_info:
        raise FileSkipSetting(file_path)
    assert exc_info.value.file_path == file_path

# Generated at 2026-11-02 13:53:40.106599
# Unit test for constructor of class ISortError
def test_ISortError():
    """
    Test the constructor of the base ISortError exception class.
    """
    # Instantiate with a message
    exception = ISortError("An error occurred")
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)
    assert str(exception) == "An error occurred"

    # Instantiate without arguments
    plain_exception = ISortError()
    assert isinstance(plain_exception, ISortError)
    assert isinstance(plain_exception, Exception)

# Generated at 2026-11-02 13:55:36.138379
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
        """
        Test that the AssignmentsFormatMismatch constructor correctly stores
        the provided code and generates the expected error message.
        """
        code = "x = 1\ny: 2"

        exc = AssignmentsFormatMismatch(code)

        # The exception should store the code as an attribute
        assert exc.code == code

        # The exception should be an instance of ISortError and Exception
        assert isinstance(exc, ISortError)
        assert isinstance(exc, Exception)

        # The error message should contain the provided code
        assert code in str(exc)

        # The error message should contain formatting instructions
        assert "Does not match isort's strict single line formatting requirement" in str(exc)
        assert "{variable_name} = {value}" in str(exc)

        # Constructing with a different code should store that code instead
        other_code = "invalid assignment"
        exc2 = AssignmentsFormatMismatch(other_code)
        assert exc2.code == other_code
        assert other_code in str(exc2)