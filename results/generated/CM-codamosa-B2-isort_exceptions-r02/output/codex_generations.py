

# Generated at 2026-11-02 15:57:48.238573
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example_file.py"
    exception = FileSkipSetting(file_path)

    assert exception.file_path == file_path
    assert str(exception) == (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Ensure different file paths produce the expected message
    other_path = "another/module.py"
    other_exception = FileSkipSetting(other_path)
    assert other_exception.file_path == other_path
    assert other_path in str(other_exception)

# Generated at 2026-11-02 15:59:38.958076
# Unit test for constructor of class MissingSection
def test_MissingSection():
    from isort.exceptions import ISortError, MissingSection

    import_module = "os"
    section = "THIRDPARTY"

    error = MissingSection(import_module=import_module, section=section)

    # Exception should be an instance of both MissingSection and its base ISortError
    assert isinstance(error, MissingSection)
    assert isinstance(error, ISortError)

    # Verify the exception message contains the relevant details
    assert (
        str(error)
        == f"Found {import_module} import while parsing, but {section} was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info."
    )
    assert import_module in str(error)
    assert section in str(error)

# Generated at 2026-11-02 16:01:27.553753
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    from pathlib import Path

    # Test with a string filename
    filename = "example.py"
    exception = UnsupportedEncoding(filename)
    assert exception.filename == filename
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"

    # Test with a Path filename
    path_filename = Path("example.py")
    exception = UnsupportedEncoding(path_filename)
    assert exception.filename == path_filename
    assert str(exception) == f"Unknown or unsupported encoding in {path_filename}"

    # Ensure it is an ISortError subclass instance
    assert isinstance(exception, ISortError)

# Generated at 2026-11-02 16:04:10.517828
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "/path/to/file.py"
    exception = ExistingSyntaxErrors(file_path)

    assert exception.file_path == file_path
    assert str(exception) == (
        "isort was told to sort imports within code that contains syntax errors: "
        f"{file_path}."
    )

# Generated at 2026-11-02 16:05:18.831806
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    from pathlib import Path
    from isort.exceptions import UnsupportedEncoding, ISortError

    # Test with string filename
    filename = "test_file.py"
    error = UnsupportedEncoding(filename)
    assert error.filename == filename
    assert isinstance(error, ISortError)
    assert str(error) == f"Unknown or unsupported encoding in {filename}"

    # Test with Path filename
    path_filename = Path("some") / "nested" / "file.py"
    error = UnsupportedEncoding(path_filename)
    assert error.filename == path_filename
    assert str(error) == f"Unknown or unsupported encoding in {path_filename}"

    # Test raised as exception context
    try:
        raise UnsupportedEncoding("encoding_fail.py")
    except UnsupportedEncoding as e:
        assert e.filename == "encoding_fail.py"
        assert "encoding_fail.py" in str(e)
    else:
        assert False, "UnsupportedEncoding was not raised"