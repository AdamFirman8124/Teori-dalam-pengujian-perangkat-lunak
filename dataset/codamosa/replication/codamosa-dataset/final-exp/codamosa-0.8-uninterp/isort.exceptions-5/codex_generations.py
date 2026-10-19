

# Generated at 2022-06-13 23:00:24.290999
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = 1
    # test
    assert InvalidSettingsPath(settings_path)


# Generated at 2022-06-13 23:00:28.080939
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "test/test.py"
    try:
        raise FileSkipSetting(file_path)
    except FileSkipSetting as obj:
        assert obj.file_path == "test/test.py"
        assert "was skipped as it's listed in 'skip' setting" in str(obj)


# Generated at 2022-06-13 23:00:31.150100
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    object = FormattingPluginDoesNotExist("venv_isort_plugin")
    assert object.formatter == "venv_isort_plugin"

# Generated at 2022-06-13 23:00:35.463282
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors("this_is_a_file.py")
    except ExistingSyntaxErrors as e:
        assert e.args[0] == "isort was told to sort imports within code that contains " \
                            "syntax errors: this_is_a_file.py."
        assert e.file_path == "this_is_a_file.py"

# Generated at 2022-06-13 23:00:38.239213
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "formatter"
    formatter_error = FormattingPluginDoesNotExist(formatter)
    assert type(formatter_error) is FormattingPluginDoesNotExist
    assert formatter_error.formatter == formatter

# Generated at 2022-06-13 23:00:42.592653
# Unit test for constructor of class ISortError
def test_ISortError():
    assert ISortError()


# Generated at 2022-06-13 23:00:48.228476
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    try:
        raise AssignmentsFormatMismatch("\tapple = 1\n\tbanana = 2\n")
    except AssignmentsFormatMismatch as e:
        print(e)

# Generated at 2022-06-13 23:00:49.373851
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    FileSkipComment("file_path")

# Generated at 2022-06-13 23:00:59.418853
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    from ast import parse
    from io import StringIO
    from tokenize import (
        generate_tokens,
        COMMENT,
        DEDENT,
        ENCODING,
        INDENT,
        NEWLINE,
        NAME,
        NUMBER,
        OP,
        STRING,
    )

    def _tokenize(to_tokenize: str) -> Iterator[Any]:
        tokens = generate_tokens(StringIO(to_tokenize).readline)
        for tok in tokens:
            _type = tok[0]
            if _type == ENCODING:
                continue
            yield (tok[1], _type)


# Generated at 2022-06-13 23:01:23.975884
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    e = ExistingSyntaxErrors('file.py')
    assert e.file_path == 'file.py'
    assert str(e) == 'isort was told to sort imports within code that contains syntax errors: file.py.'

# Generated at 2022-06-13 23:01:34.259492
# Unit test for constructor of class MissingSection
def test_MissingSection():
    # GIVEN
    import_module = "bar"
    section = "Foo"
    expected_message = (
            f"Found {import_module} import while parsing, but {section} was not included "
            "in the `sections` setting of your config. Please add it before continuing\n"
            "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
            "for more info."
    )
    # WHEN
    actual = MissingSection(import_module, section)
    # THEN
    assert actual.import_module == import_module
    assert actual.section == section
    assert actual.args[0] == expected_message

# Generated at 2022-06-13 23:01:47.309084
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    assert LiteralParsingFailure(code=["abc"], original_error="original_error")


# Generated at 2022-06-13 23:01:52.950145
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    err = IntroducedSyntaxErrors('file_name')
    assert (
        str(err)
        == 'isort introduced syntax errors when attempting to sort the imports contained within file_name.'
    )


test_IntroducedSyntaxErrors()

# Generated at 2022-06-13 23:02:06.069332
# Unit test for constructor of class ISortError
def test_ISortError():
    assert ISortError.__init__.__annotations__ == dict()

# Generated at 2022-06-13 23:02:09.815898
# Unit test for constructor of class ISortError
def test_ISortError():
    err = ISortError('This is a test error')
    assert err.args[0] == 'This is a test error'

# Generated at 2022-06-13 23:02:13.574464
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(kind=int, expected_kind=str)
    except LiteralSortTypeMismatch as lstm:
        assert issubclass(lstm.kind, object)
        assert issubclass(lstm.expected_kind, basestring)

# Generated at 2022-06-13 23:02:18.244254
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist("does not exist")
    except FormattingPluginDoesNotExist as err:
        assert err.formatter == "does not exist"

# Generated at 2022-06-13 23:02:21.889877
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        t = ()
        t.split()
    except Exception as e:
        f = LiteralParsingFailure('code', e)
        assert f.code == 'code'


# Generated at 2022-06-13 23:02:25.871912
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    actual = FileSkipSetting("FileSkipSetting")
    assert actual.file_path == "FileSkipSetting"
# test_FileSkipSetting


# Generated at 2022-06-13 23:02:31.611284
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "msg"
    file_path = "file_path"
    file_skipped = FileSkipped(message, file_path)
    assert file_skipped.message == message
    assert file_skipped.file_path == file_path



# Generated at 2022-06-13 23:02:39.242879
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(1, "string")
    assert error.kind == int
    assert error.expected_kind == str
    assert str(error) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'int'>.\n"

# Generated at 2022-06-13 23:02:42.997280
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    assert InvalidSettingsPath("settings_path").settings_path == "settings_path"


# Generated at 2022-06-13 23:02:53.652887
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    setting = UnsupportedSettings({"trailing_comma": {"value": "foo", "source": "bar"}})
    assert setting.unsupported_settings == {"trailing_comma": {"value": "foo", "source": "bar"}}
    assert str(setting) == (
        "isort was provided settings that it doesn't support:\n\n\t- trailing_comma = foo  (source: 'bar')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )


# Generated at 2022-06-13 23:02:56.273512
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
	tmp = FileSkipComment("test.py")

	assert tmp.file_path == "test.py"
	assert str(tmp) == "test.py contains an file skip comment and was skipped."

# Generated at 2022-06-13 23:03:00.358382
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(str, dict)
    except LiteralSortTypeMismatch as e:
        assert e.kind == str
        assert e.expected_kind == dict
    else:
        assert False

# Generated at 2022-06-13 23:03:04.411525
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("my_profile")
    except ProfileDoesNotExist as exc:
        assert str(exc) == f"""Specified profile of my_profile does not exist. Available profiles: black, isort, pep8."""
        assert exc.profile == "my_profile"

# Generated at 2022-06-13 23:03:10.279752
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    import isort.exceptions

    try:
        raise isort.exceptions.UnsupportedEncoding(
            "A file name"
        )
    except isort.exceptions.UnsupportedEncoding as e:
        assert e.filename == "A file name"
    else:
        assert False

# Generated at 2022-06-13 23:03:15.122868
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist("a")
    except FormattingPluginDoesNotExist as err:
        assert err.formatter == "a"
        assert "Specified formatting plugin of a does not exist" in str(err)



# Generated at 2022-06-13 23:03:17.068192
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    ans = IntroducedSyntaxErrors('test')
    assert ans.file_path == 'test'



# Generated at 2022-06-13 23:03:18.822679
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    assert FileSkipSetting('test_file').file_path == 'test_file'
