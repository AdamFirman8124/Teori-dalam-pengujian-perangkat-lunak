# file: project/isort/exceptions.py:54-60
# asked: {"lines": [58, 59], "branches": []}
# gained: {"lines": [58, 59], "branches": []}

from isort.exceptions import FileSkipComment, FileSkipped


def test_file_skip_comment_initializes_message_and_file_path():
    file_path = "src/example.py"

    exception = FileSkipComment(file_path)

    assert isinstance(exception, FileSkipped)
    assert exception.file_path == file_path
    assert str(exception) == (
        f"{file_path} contains an file skip comment and was skipped."
    )
    assert exception.args == (
        f"{file_path} contains an file skip comment and was skipped.",
    )
