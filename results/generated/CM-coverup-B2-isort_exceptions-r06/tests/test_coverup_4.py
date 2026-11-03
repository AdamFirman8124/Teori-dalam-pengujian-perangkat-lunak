# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

import pytest

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_errors_initialization():
    """Test that ExistingSyntaxErrors sets its message and file_path attribute correctly."""
    file_path = "/path/to/file_with_syntax_errors.py"
    exc = ExistingSyntaxErrors(file_path)

    # Verify the exception message is built correctly from the file path
    assert str(exc) == (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )

    # Verify the file_path attribute is stored
    assert exc.file_path == file_path

    # Verify inheritance from the isort base exception
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_existing_syntax_errors_is_raisable_and_catchable():
    """Test that ExistingSyntaxErrors can be raised and caught as an ISortError."""
    file_path = "another_file.py"
    with pytest.raises(ISortError) as exc_info:
        raise ExistingSyntaxErrors(file_path)

    assert exc_info.value.file_path == file_path
    assert file_path in str(exc_info.value)
