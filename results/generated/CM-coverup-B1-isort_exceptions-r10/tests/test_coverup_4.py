# file: project/isort/exceptions.py:24-32
# asked: {"lines": [28, 29, 30, 32], "branches": []}
# gained: {"lines": [28, 29, 30, 32], "branches": []}

from isort.exceptions import ExistingSyntaxErrors, ISortError


def test_existing_syntax_errors_init_sets_message_and_file_path():
    file_path = "/some/path/to/file.py"
    exc = ExistingSyntaxErrors(file_path)
    expected_message = (
        f"isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message
    assert exc.file_path == file_path
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)


def test_existing_syntax_errors_can_be_raised_and_caught():
    file_path = "my_module.py"
    expected_message = (
        f"isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )
    try:
        raise ExistingSyntaxErrors(file_path)
    except ExistingSyntaxErrors as exc:
        assert exc.file_path == file_path
        assert str(exc) == expected_message
    else:
        raise AssertionError("ExistingSyntaxErrors was not raised")


def test_existing_syntax_errors_caught_as_base_isort_error():
    file_path = "/tmp/broken.py"
    with __import__("pytest").raises(ISortError) as exc_info:
        raise ExistingSyntaxErrors(file_path)
    assert exc_info.value.file_path == file_path
    assert file_path in str(exc_info.value)
    assert "syntax errors" in str(exc_info.value)
