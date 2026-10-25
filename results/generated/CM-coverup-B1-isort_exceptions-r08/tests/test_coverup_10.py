# file: project/isort/exceptions.py:46-51
# asked: {"lines": [50, 51], "branches": []}
# gained: {"lines": [50, 51], "branches": []}

from isort.exceptions import FileSkipped, ISortError


def test_file_skipped_initialization():
    message = "File was skipped"
    file_path = "example.py"

    error = FileSkipped(message, file_path)

    assert isinstance(error, ISortError)
    assert str(error) == message
    assert error.args == (message,)
    assert error.file_path == file_path
