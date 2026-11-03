

# Generated at 2026-11-03 01:49:40.336246
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    # Arrange
    code = "{invalid: literal"
    original_error = SyntaxError("unexpected EOF while parsing")

    # Act
    error = LiteralParsingFailure(code=code, original_error=original_error)

    # Assert
    assert error.code == code
    assert error.original_error == original_error
    assert isinstance(error, ISortError)
    assert code in str(error)
    assert str(original_error) in str(error)

# Generated at 2026-11-03 01:50:33.501243
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "from a import b\n\nfrom c import d"
    exception = AssignmentsFormatMismatch(code=code)

    # The code attribute should be stored as provided
    assert exception.code == code

    # The exception message should contain the given code and the formatting requirement
    assert str(exception) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

    # It should be an instance of the base isort exception
    from isort.exceptions import ISortError
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

# Generated at 2026-11-03 01:52:02.636659
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    # Test with a string filename
    filename = "example.py"
    exception = UnsupportedEncoding(filename)

    assert exception.filename == filename
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert isinstance(exception, ISortError)

    # Test with a Path filename
    path_filename = Path("example.py")
    exception = UnsupportedEncoding(path_filename)

    assert exception.filename == path_filename
    assert str(exception) == f"Unknown or unsupported encoding in {path_filename}"
    assert isinstance(exception, ISortError)

# Generated at 2026-11-03 01:52:46.157421
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "black2"
    exception = ProfileDoesNotExist(profile)

    # The profile attribute should be set to the provided profile name
    assert exception.profile == profile

    # The exception message should mention the profile and available profiles
    assert profile in str(exception)
    assert "does not exist" in str(exception)
    assert "black" in str(exception)  # 'black' is one of the default available profiles
    assert "Available profiles:" in str(exception)

    # It should be an instance of the base isort exception
    assert isinstance(exception, ProfileDoesNotExist)

# Generated at 2026-11-03 01:53:57.733435
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "x = [1, 2, 3"
    original_error = SyntaxError("unexpected EOF while parsing")

    exception = LiteralParsingFailure(code, original_error)

    # Attributes should be set correctly
    assert exception.code == code
    assert exception.original_error is original_error

    # Should be an instance of the base isort exception and Exception
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Message should contain the code and the original error's message
    message = str(exception)
    assert "isort failed to parse the given literal" in message
    assert code in message
    assert str(original_error) in message
    assert "ast.literal_eval" in message

# Generated at 2026-11-03 01:54:29.686516
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    kind = str
    expected_kind = list

    exception = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    assert exception.kind == kind
    assert exception.expected_kind == expected_kind
    assert f"{expected_kind}" in str(exception)
    assert f"{kind}" in str(exception)
    assert isinstance(exception, Exception)

# Generated at 2026-11-03 01:55:28.155621
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = int
expected_kind = str
error = LiteralSortTypeMismatch(kind, expected_kind)
assert error.kind == kind
assert error.expected_kind == expected_kind
assert str(error) == (
    "isort was told to sort a literal of type <class 'str'> but was given "
    "a literal of type <class 'int'>."
)
assert isinstance(error, ISortError)

# Generated at 2026-11-03 01:56:47.619486
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = dict

# Generated at 2026-11-03 01:57:15.578519
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    from isort.exceptions import FileSkipComment

    file_path = "example.py"
    exception = FileSkipComment(file_path)

    # The exception should be an instance of FileSkipped and ISortError
    from isort.exceptions import FileSkipped, ISortError
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # The file_path attribute should be set correctly
    assert exception.file_path == file_path

    # The exception message should mention the file path and the skip comment
    assert str(exception) == f"{file_path} contains an file skip comment and was skipped."
    assert file_path in str(exception)
    assert "file skip comment" in str(exception)