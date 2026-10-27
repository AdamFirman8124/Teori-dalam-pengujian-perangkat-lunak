# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

from isort.exceptions import FileSkipComment, FileSkipped


def test_file_skip_comment_initialization() -> None:
    file_path = "example.py"

    error = FileSkipComment(file_path)

    assert isinstance(error, FileSkipped)
    assert error.file_path == file_path
    assert str(error) == (
        "example.py contains an file skip comment and was skipped."
    )
