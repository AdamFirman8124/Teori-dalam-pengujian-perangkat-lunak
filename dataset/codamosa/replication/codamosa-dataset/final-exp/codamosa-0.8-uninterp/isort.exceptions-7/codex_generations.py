

# Generated at 2022-06-13 23:00:41.183129
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    from types import SimpleNamespace
    UnsupportedSettings(
        {
            "use_parentheses": SimpleNamespace(value="True", source="config"),
            "default_section": SimpleNamespace(value="FUTURE", source="config"),
        }
    )

# Generated at 2022-06-13 23:00:42.605217
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "non-existent"
    exception = ProfileDoesNotExist(profile)
    assert exception.profile == profile

# Generated at 2022-06-13 23:00:46.445277
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    fsc = FileSkipComment("test.py")
    assert fsc.message == "test.py contains an file skip comment and was skipped."

# Generated at 2022-06-13 23:00:50.874253
# Unit test for constructor of class MissingSection
def test_MissingSection():
    assert "Found test_import while parsing, but TEST_SECTION was not included " \
           "in the `sections` setting of your config. Please add it before continuing" in str(MissingSection("test_import", "TEST_SECTION"))

# Generated at 2022-06-13 23:00:54.617301
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    encoding_error: UnsupportedEncoding = UnsupportedEncoding(filename="Test file")
    assert encoding_error.filename == "Test file"
    assert encoding_error.__str__() == "Unknown or unsupported encoding in Test file"


# Generated at 2022-06-13 23:00:59.748998
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        test_instance = MissingSection("pygame", "FIRSTPARTY")
    except ISortError as e:
        assert str(e) == "Found pygame import while parsing, but FIRSTPARTY was not included in the `sections` setting of your config. Please add it before continuing\n" + \
            "See https://pycqa.github.io/isort/#custom-sections-and-ordering " + \
            "for more info."



# Generated at 2022-06-13 23:01:21.098111
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    assert FormattingPluginDoesNotExist('formatter').formatter == 'formatter'

# Generated at 2022-06-13 23:01:25.364079
# Unit test for constructor of class MissingSection
def test_MissingSection():
    missingSection = MissingSection("import_module", "section")
    assert missingSection.import_module == "import_module"
    assert missingSection.section == "section"
    assert str(missingSection).startswith("Found import_module import while parsing, but section was not included in")

# Generated at 2022-06-13 23:01:34.082237
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    with pytest.raises(ProfileDoesNotExist) as error:
        raise ProfileDoesNotExist("Test")
    assert str(error.value) == "Specified profile of Test does not exist. Available profiles: black, google, isort, pyup, pyv, pydocstyle, sphinx."
    assert error.value.profile == "Test"



# Generated at 2022-06-13 23:01:47.987536
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist(profile="test")
    except ProfileDoesNotExist as error:
        assert error.profile == "test"

# Generated at 2022-06-13 23:01:53.452659
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    with pytest.raises(ProfileDoesNotExist) as exception:
        raise ProfileDoesNotExist("test")
    assert exception.value.profile == "test"



# Generated at 2022-06-13 23:02:09.883071
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("test")
    except ISortError as e:
        assert str(e) == "test"

# Generated at 2022-06-13 23:02:12.528065
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("test error")
    except ISortError as e:
        assert str(e) == "isort: test error"


# Generated at 2022-06-13 23:02:17.599956
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    print("\nStart testing ProfileDoesNotExist")
    try:
        raise ProfileDoesNotExist("aaa")
    except ProfileDoesNotExist as err:
        print(err)
    print("End testing ProfileDoesNotExist")



# Generated at 2022-06-13 23:02:20.407665
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "spam.py"
    with pytest.raises(FileSkipSetting, match=file_path):
        raise FileSkipSetting(file_path=file_path)

# Generated at 2022-06-13 23:02:28.138406
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    skipped = FileSkipped(message="Failed to read file test.py", file_path="test.py")
    assert skipped.args == ("Failed to read file test.py",)
    assert skipped.file_path == "test.py"
    assert skipped.__str__() == "Failed to read file test.py"

# Generated at 2022-06-13 23:02:29.742614
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    assert "FileSkipSetting" in str(FileSkipSetting("/path/to/file"))



# Generated at 2022-06-13 23:02:32.529312
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    try:
        raise FileSkipped()
    except FileSkipped:
        return True
    return False



# Generated at 2022-06-13 23:02:35.907863
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    path = 'C:\\Users\\Python\\settings.cfg'
    exc = InvalidSettingsPath(path)
    assert exc.settings_path == path, 'Invalid settings path'


# Generated at 2022-06-13 23:02:41.375032
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2022-06-13 23:02:45.572402
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    t1 = InvalidSettingsPath("test")
    assert t1.settings_path == "test"


# Generated at 2022-06-13 23:02:48.176717
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    assert(ExistingSyntaxErrors("test").file_path == "test")


# Generated at 2022-06-13 23:02:55.876870
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("settings_path")
    except InvalidSettingsPath as error:
        assert "settings_path" in str(error)
        assert error.message == (
            f"isort was told to use the settings_path: settings_path as the base directory or "
            "file that represents the starting point of config file discovery, but it does not "
            "exist."
        )


# Generated at 2022-06-13 23:03:01.312284
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = 'true_docstring'
    try:
        raise FormattingPluginDoesNotExist(formatter=formatter)
    except FormattingPluginDoesNotExist as e:
        assert e.formatter == formatter
        assert str(e) == f'Specified formatting plugin of {formatter} does not exist. '


# Generated at 2022-06-13 23:03:03.458724
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    SyntaxErrorTest = ExistingSyntaxErrors("test.py")
    assert SyntaxErrorTest.file_path == "test.py"

# Generated at 2022-06-13 23:03:08.371785
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "E:\A case of you.py"
    try:
        raise FileSkipComment(file_path)
    except FileSkipComment as e:
        assert e.file_path == file_path

# Generated at 2022-06-13 23:03:14.051796
# Unit test for constructor of class MissingSection
def test_MissingSection():
    config_missing_section = '''
[settings]
force_single_line = true
'''
    given = MissingSection('foo.bar', 'FUTURE')
    expected = f'Found foo.bar import while parsing, but FUTURE was not included in the `sections` setting of your config. Please add it before continuing\nSee https://pycqa.github.io/isort/#custom-sections-and-ordering for more info.'
    assert given.__str__() == expected

# Generated at 2022-06-13 23:03:15.173737
# Unit test for constructor of class ISortError
def test_ISortError():
    pass


# Generated at 2022-06-13 23:03:17.416522
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    assert FileSkipComment.__init__.__doc__ == (
        "Raised when an entire file is skipped due to a isort skip file comment"
    )

# Generated at 2022-06-13 23:03:20.545926
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath('test')
    except InvalidSettingsPath as error:
        assert str(error) == "isort was told to use the settings_path: test as the base directory or file that represents the starting point of config file discovery, but it does not exist."


# Generated at 2022-06-13 23:03:25.934844
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    with pytest.raises(LiteralSortTypeMismatch) as error:
        raise LiteralSortTypeMismatch(int, str)
    assert error.value.kind == int
    assert error.value.expected_kind == str


# Generated at 2022-06-13 23:03:27.828372
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    assert isinstance(FormattingPluginDoesNotExist('hello world'), ISortError)


# Generated at 2022-06-13 23:03:46.108583
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(1, 2)
    except LiteralSortTypeMismatch as e:
        assert e.kind == 1
        assert e.expected_kind == 2
    try:
        raise LiteralSortTypeMismatch(1.1, 2.2)
    except LiteralSortTypeMismatch as e:
        assert e.kind == 1.1
        assert e.expected_kind == 2.2
    try:
        raise LiteralSortTypeMismatch("a", "b")
    except LiteralSortTypeMismatch as e:
        assert e.kind == "a"
        assert e.expected_kind == "b"

# Generated at 2022-06-13 23:03:50.764772
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():  # noqa: D103
    try:
        raise FormattingPluginDoesNotExist("simple")
    except FormattingPluginDoesNotExist as e:
        assert str(e) == "Specified formatting plugin of simple does not exist. "
        assert e.formatter == "simple"


# Generated at 2022-06-13 23:03:57.364856
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    print("Testing for constructor of class FormattingPluginDoesNotExist:")
    formatter = ""
    error = FormattingPluginDoesNotExist(formatter)
    assert isinstance(error, FormattingPluginDoesNotExist), "error should be an instance of FormattingPluginDoesNotExist"
    print("\tPassed")



# Generated at 2022-06-13 23:04:05.184455
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting('file_path')
    except FileSkipSetting as error:
        assert error.file_path == 'file_path'
        assert str(error) == 'file_path was skipped as it\'s listed in \'skip\' setting or ' \
            'matches a glob in \'skip_glob\' setting'
        assert isinstance(error, FileSkipSetting)
        assert isinstance(error, ISortError)


# Generated at 2022-06-13 23:04:07.192403
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
  test = FormattingPluginDoesNotExist('')
  assert isinstance(test, FormattingPluginDoesNotExist)

# Generated at 2022-06-13 23:04:10.457345
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    try:
        raise FileSkipSetting("test")
    except FileSkipSetting as e:
        assert e.file_path == "test"

# Generated at 2022-06-13 23:04:19.250240
# Unit test for constructor of class ISortError
def test_ISortError():
    noargs = ISortError()
    assert str(noargs) == ''
    assert repr(noargs) == 'ISortError()'

    args = ISortError('msg')
    assert str(args) == 'msg'
    assert repr(args) == "ISortError('msg')"

    # cod is different from the above; be thorough
    cod = ISortError('msg', 2)
    assert str(cod) == 'msg'
    assert repr(cod) == "ISortError('msg', 2)"

# Generated at 2022-06-13 23:04:20.250119
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    error = IntroducedSyntaxErrors("somefile.py")
    assert error.file_path == 'somefile.py'

# Generated at 2022-06-13 23:04:29.585146
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    try:
        raise AssignmentsFormatMismatch(["var1 = 1"])
    except AssignmentsFormatMismatch as exc:
        expected = "isort was told to sort a section of assignments, however the given code:\n\n" \
                   "['var1 = 1']\n\n" \
                   "Does not match isort's strict single line formatting requirement for assignment " \
                   "sorting:\n\n" \
                   "{variable_name} = {value}\n" \
                   "{variable_name2} = {value2}\n" \
                   "...\n\n"
        assert exc.__str__() == expected
        assert exc.code == ["var1 = 1"]


# Generated at 2022-06-13 23:04:32.883115
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "a = 1"
    try:
        raise AssignmentsFormatMismatch(code)
    except AssignmentsFormatMismatch as e:
        assert e.code == code

# Generated at 2022-06-13 23:04:35.429688
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "FILE = \"file\"\n"
    isort.api.AssignmentsFormatMismatch(code)

# Generated at 2022-06-13 23:04:40.062408
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    test_object = LiteralParsingFailure(code="somecode", original_error=ISortError())
    assert test_object.code == "somecode"
    assert test_object.original_error != 0


# Generated at 2022-06-13 23:04:42.875369
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    assert ExistingSyntaxErrors.__init__(ExistingSyntaxErrors, "FilePath") == None
    assert ExistingSyntaxErrors.file_path == "FilePath"


# Generated at 2022-06-13 23:04:49.558828
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    with pytest.raises(AssignmentsFormatMismatch) as e:
        raise AssignmentsFormatMismatch(
            "a, b, c = 1, 2, 3 \n a = b = c = 2 \n "
            "a, b, c = 3, 4, 5 \n a = b = c = 4 \n "
        )
    assert "isort was told to sort a section of assignments" in str(e.value)

# Generated at 2022-06-13 23:05:01.293001
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    from .isort import _get_options
    # Set up test values
    options = _get_options(
        known_first_party=(),
        known_third_party=(),
        known_other_party=(),
        known_names=#,
        known_names_lowercase#,
    )
    options['atomic'], options['order_by_type'], options['settings_path'] = False, False, None
    source_code = options['wrap_length'] = 50
    options['length_sort'] = False
    # Create a new LiteralParsingFailure object, then check its fields
    assert LiteralParsingFailure(source_code, SyntaxError)
    assert LiteralParsingFailure(source_code, SyntaxError).original_error is SyntaxError

# Generated at 2022-06-13 23:05:04.321499
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    try:
        raise AssignmentsFormatMismatch("a = b + c")
    except AssignmentsFormatMismatch as e:
        assert e.code == "a = b + c"


# Generated at 2022-06-13 23:05:08.907331
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    filename = './class_exists_syntax_error_file.py'
    message = f"isort was told to sort imports within code that contains syntax errors: {filename}."
    try:
        raise ExistingSyntaxErrors(file_path=filename)
    except ExistingSyntaxErrors as e:
        assert e.file_path == filename
        assert str(e) == message

# Generated at 2022-06-13 23:05:12.294429
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    try:
        AssignmentsFormatMismatch('test')
    except Exception as e:
        print(e)
test_AssignmentsFormatMismatch()

# Generated at 2022-06-13 23:05:20.190093
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {"named_imports_after_stars": {"source": "config"}}
    UnsupportedSettings(unsupported_settings)

# Generated at 2022-06-13 23:05:23.022777
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    lstm = LiteralSortTypeMismatch(int, str)
    assert lstm.kind is int
    assert lstm.expected_kind is str

# Generated at 2022-06-13 23:05:27.301779
# Unit test for constructor of class MissingSection
def test_MissingSection():
    missing_section = MissingSection("foo", "bar")
    assert missing_section.__str__() == "Found foo import while parsing, but bar was not included " \
        "in the `sections` setting of your config. Please add it before continuing\n" \
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."

# Generated at 2022-06-13 23:05:33.630722
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    import pytest
    with pytest.raises(IntroducedSyntaxErrors) as raised1:
        raise IntroducedSyntaxErrors("test file name")
    assert raised1.type == IntroducedSyntaxErrors
    assert raised1.value.file_path == "test file name"



# Generated at 2022-06-13 23:05:41.191951
# Unit test for constructor of class MissingSection
def test_MissingSection():
    ms = MissingSection("testmodule", "testsection")
    assert ms.args == (
        "Found testmodule import while parsing, but testsection was not included "
        "in the `sections` setting of your config. Please add it before continuing\n"
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
        "for more info.",
    )

# Generated at 2022-06-13 23:05:45.710770
# Unit test for constructor of class MissingSection
def test_MissingSection():
    assert MissingSection("import_module", "section").args[0] == \
        f"Found import_module import while parsing, but section was not included " \
        "in the `sections` setting of your config. Please add it before continuing\n" \
        "See https://pycqa.github.io/isort/#custom-sections-and-ordering " \
        "for more info."



# Generated at 2022-06-13 23:05:51.370598
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors('file.py')
    except ExistingSyntaxErrors as err:
        assert err.file_path == 'file.py'
        assert str(err) == "isort was told to sort imports within code that contains syntax errors: file.py."



# Generated at 2022-06-13 23:05:55.202039
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    exc = LiteralSortTypeMismatch(kind=int, expected_kind=float)
    assert exc.kind == int
    assert exc.expected_kind == float



# Generated at 2022-06-13 23:05:58.386576
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    a = ExistingSyntaxErrors('/sd/asd/qwe')
    assert a.file_path == '/sd/asd/qwe'


# Generated at 2022-06-13 23:06:02.787989
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    try:
        raise FormattingPluginDoesNotExist("Fake Formatter")
    except FormattingPluginDoesNotExist as error:
        assert error.formatter == "Fake Formatter"
        assert error.__repr__().startswith("FormattingPluginDoesNotExist(formatter='Fake Formatter')")
        assert error.__str__() == "Specified formatting plugin of Fake Formatter does not exist. "


# Generated at 2022-06-13 23:06:15.905129
# Unit test for constructor of class MissingSection
def test_MissingSection():
    missing_section = MissingSection("import", "section")
    assert isinstance(missing_section, MissingSection)
    assert "import" in missing_section.args[0]
    assert "section" in missing_section.args[0]


# Generated at 2022-06-13 23:06:19.508179
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    assert FileSkipSetting('file_path').message == \
        "'file_path' was skipped as it's listed in 'skip' setting" \
        " or matches a glob in 'skip_glob' setting"

# Generated at 2022-06-13 23:06:22.888137
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding('test.py')
    except UnsupportedEncoding as error:
        assert error.filename == 'test.py'


# Generated at 2022-06-13 23:06:25.700124
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    # Example
    try:
        raise FormattingPluginDoesNotExist("Test")
    except FormattingPluginDoesNotExist as e:
        assert str(e) == "Specified formatting plugin of Test does not exist."

# Generated at 2022-06-13 23:06:30.659237
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():

    class Foo:
        pass

    try:
        raise LiteralSortTypeMismatch(Foo, float)
    except LiteralSortTypeMismatch as e:
        assert e.kind == Foo
        assert e.expected_kind == float
        assert str(e) == "isort was told to sort a literal of type <class 'float'> but was given a literal of type <class '__main__.Foo'>. "
        # assert repr(e) == "isort was told to sort a literal of type <class 'float'> but was given a literal of type <class '__main__.Foo'>. "

# Generated at 2022-06-13 23:06:34.462610
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    result = LiteralParsingFailure("1",None)
    assert result.code == "1"
    assert result.original_error == None


# Generated at 2022-06-13 23:06:48.735357
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    import_module = 'os'
    section = 'FUTURE'
    code = 'variable = True\n'
    name = 'test'
    option = {'value': '0', 'source': 'default'}
    assert code == 'variable = True\n'
    assert option['value'] == '0'
    assert option['source'] == 'default'
    a = AssignmentsFormatMismatch(code)
    assert a.code == code
    b = UnsupportedSettings({})
    c = UnsupportedEncoding('test.py')
    d = MissingSection(import_module, section)
    e = UnsupportedSettings._format_option(name, **option)
    assert e == '\t- test = 0  (source: \'default\')'

# Generated at 2022-06-13 23:06:50.808040
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    assert ExistingSyntaxErrors("test").__str__() == \
        'isort was told to sort imports within code that contains syntax errors: test.'

# Generated at 2022-06-13 23:07:00.905720
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    try:
        raise LiteralParsingFailure("fail", RuntimeError("fail"))
    except LiteralParsingFailure as err:
        assert str(err) == (
            "isort failed to parse the given literal fail. It's important to note "
            "that isort literal sorting only supports simple literals parsable by "
            "ast.literal_eval which gave the exception of fail."
        )
        assert err.code == "fail"
        assert isinstance(err.original_error, RuntimeError)

# Generated at 2022-06-13 23:07:05.061493
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        print('Here is the test for constructor of class IntroducedSyntaxErrors')
        raise IntroducedSyntaxErrors('/Users/yayunhuang/Documents/isort/isort.py')
    except IntroducedSyntaxErrors as e:
        print(e)


# Generated at 2022-06-13 23:07:27.373887
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    # set up
    err = FormattingPluginDoesNotExist("")
    # assert
    assert err.formatter == ""



# Generated at 2022-06-13 23:07:29.067721
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    assert ProfileDoesNotExist('foo')


# Generated at 2022-06-13 23:07:35.587544
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    # function is called and exception is raised for file (path) test.py
    try:
        raise ExistingSyntaxErrors('test.py')
    except ExistingSyntaxErrors as e:
        assert str(e) == "isort was told to sort imports within code that contains syntax errors: test.py."
        assert e.file_path == 'test.py'

# Generated at 2022-06-13 23:07:38.699682
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("Invalid")
    except InvalidSettingsPath:
        assert True
assert True


# Generated at 2022-06-13 23:07:43.675753
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    """Unit test for constructor of class UnsupportedSettings"""
    # pylint: disable=protected-access
    obj = UnsupportedSettings(unsupported_settings={"a": {"value": 1, "source": ""}})
    assert obj._format_option("a", 1, "")

# Generated at 2022-06-13 23:07:48.349352
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("test_file_path")

    except IntroducedSyntaxErrors as e:
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within test_file_path."
        assert e.file_path == "test_file_path"



# Generated at 2022-06-13 23:07:55.472894
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist(profile='test')
    except ProfileDoesNotExist as e:
        assert e.profile == 'test'
        assert str(e) == 'Specified profile of test does not exist. Available profiles: django, google, pycharm, kivy, doc8, pytest, numpy, black, atom, vim, vscode, travis, jupyter, github, openstack, hug, strict.'

# Generated at 2022-06-13 23:08:00.119739
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    """Unit test for UnsupportedEncoding class constructor"""
    exc = UnsupportedEncoding('file.py')
    assert isinstance(exc, ISortError)
    assert exc.args[0] == 'Unknown or unsupported encoding in file.py'
    assert exc.filename == 'file.py'

# Generated at 2022-06-13 23:08:02.596718
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError("Testing an Exception")
    except ISortError as e:
        assert str(e) == "Testing an Exception"

# Generated at 2022-06-13 23:08:05.589924
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    settings_path = "test.txt"
    try:
        raise InvalidSettingsPath(settings_path)
    except InvalidSettingsPath as err:
        print(err.settings_path)
