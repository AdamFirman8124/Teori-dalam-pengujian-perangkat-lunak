

# Generated at 2022-06-13 23:00:52.123289
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    fp = "./tests/test_cases/test_case_2.py"
    syntax_error = IntroducedSyntaxErrors(fp)
    assert syntax_error.file_path == fp

# Generated at 2022-06-13 23:00:54.081689
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    a = IntroducedSyntaxErrors('test')
    assert a.file_path == 'test'

# Generated at 2022-06-13 23:00:55.710679
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    a = InvalidSettingsPath("")
    assert a.settings_path == ""



# Generated at 2022-06-13 23:00:59.767037
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist("test_formatter")
    except FormattingPluginDoesNotExist as e:
        assert str(e) == "Specified formatting plugin of test_formatter does not exist. "
        assert e.formatter == "test_formatter"

# Generated at 2022-06-13 23:01:23.306889
# Unit test for constructor of class MissingSection
def test_MissingSection():
    with pytest.raises(MissingSection) as e:
        raise MissingSection("import_module", "section")
    assert e.value.import_module == "import_module"
    assert e.value.section == "section"

# Generated at 2022-06-13 23:01:32.621361
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    import os
    # Testing case 1
    exc = UnsupportedEncoding("dummy.txt")
    assert str(exc) == "Unknown or unsupported encoding in dummy.txt"
    assert exc.filename == "dummy.txt"
    # Testing case 2
    exc = UnsupportedEncoding(os.path.abspath("dummy.txt"))
    assert str(exc) == f"Unknown or unsupported encoding in {os.path.abspath('dummy.txt')}"
    assert exc.filename == os.path.abspath("dummy.txt")

# Generated at 2022-06-13 23:01:50.469142
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    e = ExistingSyntaxErrors("/home/user/filename.py")
    assert e.file_path == "/home/user/filename.py"
    assert e.args[0] == "/home/user/filename.py"
    assert e.args[1] is None

# Generated at 2022-06-13 23:02:07.554332
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
  assert str(InvalidSettingsPath("/tmp/foo")) == "isort was told to use the settings_path: /tmp/foo as the base directory or file that represents the starting point of config file discovery, but it does not exist."


# Generated at 2022-06-13 23:02:10.531192
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    className = FileSkipSetting("a")
    assert className.file_path == "a"

# Generated at 2022-06-13 23:02:18.145602
# Unit test for constructor of class MissingSection
def test_MissingSection():
    error = MissingSection("lalala", "goodman")
    assert str(error) == "Found lalala import while parsing, but goodman was not included in the `sections` setting of your config. Please add it before continuing\nSee https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."

# Generated at 2022-06-13 23:02:21.287363
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    err = FileSkipSetting("test.py")
    assert isinstance(err, FileSkipped)

# Generated at 2022-06-13 23:02:24.412351
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("testfilename")
    except UnsupportedEncoding as e:
        assert e is not None
        assert e.filename == "testfilename"
        assert str(e) == "Unknown or unsupported encoding in testfilename"


# Generated at 2022-06-13 23:02:26.049589
# Unit test for constructor of class MissingSection
def test_MissingSection():
    e = MissingSection("import_module", "section")
    assert e.import_module == "import_module"
    assert e.section == "section"

# Generated at 2022-06-13 23:02:30.023076
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    a=FileSkipComment("test_file")
    assert (a.file_path=="test_file") or (a.message=="test_file contains an file skip comment and was skipped.")

# Generated at 2022-06-13 23:02:34.835327
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = 'message'
    file_path = 'file_path'
    file_skipped = FileSkipped(message, file_path)
    assert file_skipped.message == message
    assert file_skipped.file_path == file_path

# Generated at 2022-06-13 23:02:37.569287
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    assert LiteralSortTypeMismatch(str, int).kind == str
    assert LiteralSortTypeMismatch(str, int).expected_kind == int

# Generated at 2022-06-13 23:02:48.201586
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
  result = UnsupportedSettings({"fake_setting": {"value": "fake_value", "source": "fake_source"}})
  assert str(result) == "isort was provided settings that it doesn't support:\n\n\t- fake_setting = fake_value  (source: 'fake_source')\n\nFor a complete and up-to-date listing of supported settings see: https://pycqa.github.io/isort/docs/configuration/options/.\n"
  assert result.unsupported_settings == {"fake_setting": {"value": "fake_value", "source": "fake_source"}}

# Generated at 2022-06-13 23:02:54.219388
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    code = "This is a test for the constructor of class IntroducedSyntaxErrors.\n"
    try:
        raise IntroducedSyntaxErrors(file_path="test_file")
    except IntroducedSyntaxErrors as e:
        assert e.file_path == "test_file"
        assert str(e) == code
        assert repr(e) == code


# Generated at 2022-06-13 23:02:55.492705
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    assert FileSkipped("msg", "path")

# Generated at 2022-06-13 23:02:57.792801
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert InvalidSettingsPath("/InvalidSettingsPath").settings_path == "/InvalidSettingsPath"