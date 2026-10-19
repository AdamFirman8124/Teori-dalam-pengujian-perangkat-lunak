

# Generated at 2022-06-13 23:01:18.774015
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    error = AssignmentsFormatMismatch("import os")
    assert error.code == "import os"
    assert str(error) == "isort was told to sort a section of assignments, however the given code:\n\nimport os\n\nDoes not match isort's strict single line formatting requirement for assignment sorting:\n\n{variable_name} = {value}\n{variable_name2} = {value2}\n...\n\n"



# Generated at 2022-06-13 23:01:22.203955
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        raise MissingSection('a', 'b')
    except MissingSection as e:
        assert(e.import_module == 'a')
        assert(e.section == 'b')

# Generated at 2022-06-13 23:01:25.494836
# Unit test for constructor of class ISortError
def test_ISortError():
    error_message = "Error Message"
    try:
        raise ISortError(error_message)
    except ISortError as e:
        assert str(e) == error_message, "Correct error message"

# Generated at 2022-06-13 23:01:27.847012
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    e = ISortError.UnsupportedEncoding()
    assert e


# Generated at 2022-06-13 23:01:31.102471
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    try:
        raise LiteralSortTypeMismatch(str, int)
    except LiteralSortTypeMismatch as e:
        assert e.kind == str
        assert e.expected_kind == int

# Generated at 2022-06-13 23:01:47.633458
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    mssg = 'Test file skipped'
    file = 'test/file'
    FileSkipped(mssg, file)

# Generated at 2022-06-13 23:01:51.842660
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "a = b\nc = d"
    with pytest.raises(AssignmentsFormatMismatch):
        AssignmentsFormatMismatch(code)

# Generated at 2022-06-13 23:02:05.904712
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    from .profiles import profiles

    assert profiles

# Generated at 2022-06-13 23:02:10.838350
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("test")
    except IntroducedSyntaxErrors as e:
        assert e.file_path == "test"



# Generated at 2022-06-13 23:02:14.926501
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    ISortError.__init__(1)
    ISortError.__init__('test')
    ISortError.__init__(1,'test')

# Generated at 2022-06-13 23:02:17.852909
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    assert (FileSkipComment("file.py").file_path == "file.py")

# Generated at 2022-06-13 23:02:21.380205
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    try:
        raise InvalidSettingsPath("este texto deberia estar en el constructor de la excepción")
    except ISortError as e:
        assert e is not None
        print(e)


# Generated at 2022-06-13 23:02:23.572124
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    c = FileSkipComment("test")
    assert c.message == "test contains an file skip comment and was skipped."
    assert c.file_path == "test"

# Generated at 2022-06-13 23:02:31.558796
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        raise MissingSection("import_module","section")
    except MissingSection as e:
        assert e.import_module == "import_module"
        assert e.section == "section"
        assert str(e) == (
            "Found import_module import while parsing, but section was not included "
            "in the `sections` setting of your config. Please add it before continuing\n"
            "See https://pycqa.github.io/isort/#custom-sections-and-ordering "
            "for more info."
        )



# Generated at 2022-06-13 23:02:33.940475
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    p = ProfileDoesNotExist("profilename")
    assert p.profile == "profilename"

# Generated at 2022-06-13 23:02:36.818592
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    with pytest.raises(FormattingPluginDoesNotExist):
        raise FormattingPluginDoesNotExist("nonexistent")


# Generated at 2022-06-13 23:02:44.702709
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    # Should have file_path as attribute
    file_path = "foo/bar.py"
    message = "test comment"
    file_skipped_obj = FileSkipped(message, file_path)
    assert file_skipped_obj.file_path == file_path
    assert file_skipped_obj.message == message

# Generated at 2022-06-13 23:02:53.649819
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    d1 = {'key1': 'value1'}
    d2 = {'key2': 'value2'}
    d3 = {'key3': 'value3'}
    d = {'unsupported_option1': d1, 'unsupported_option2': d2, 'unsupported_option3': d3}

    unsupported_settings = UnsupportedSettings(d)
    assert unsupported_settings.unsupported_settings == d

# Generated at 2022-06-13 23:02:55.417192
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("filename")
    except ISortError as se:
        assert "Unknown or unsupported encoding in filename" == se.args[0]

# Generated at 2022-06-13 23:02:59.445502
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    test = LiteralSortTypeMismatch(int, str)
    correct_string = "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'int'>"
    assert str(test) == correct_string

# Generated at 2022-06-13 23:03:08.253116
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    try:
        raise ExistingSyntaxErrors(file_path="test_file")
    except ExistingSyntaxErrors as e:
        assert e.file_path == "test_file"

# Generated at 2022-06-13 23:03:11.712392
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    with pytest.raises(Exception) as excinfo:
        raise InvalidSettingsPath("/path/to/directory")
    assert excinfo.type is InvalidSettingsPath
    assert excinfo.value.settings_path == "/path/to/directory"


# Generated at 2022-06-13 23:03:13.555620
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    under_test = FileSkipped('','')
    assert type(under_test) == FileSkipped

# Generated at 2022-06-13 23:03:19.108499
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = 'os.path'
    section = 'FIRSTPARTY'
    
    err = MissingSection(import_module, section)
    assert str(err) == "Found os.path import while parsing, but FIRSTPARTY was not included in the `sections` setting of your config. Please add it before continuing\nSee https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."
test_MissingSection()

# Generated at 2022-06-13 23:03:20.781383
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    result = ISortError()

# Generated at 2022-06-13 23:03:23.894769
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("file_path")
    except IntroducedSyntaxErrors as error:
        assert error.file_path == "file_path"



# Generated at 2022-06-13 23:03:28.587772
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    a = LiteralSortTypeMismatch(int, str)
    assert str(a) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'int'>.\n"
    assert a.kind == int
    assert a.expected_kind == str

# Generated at 2022-06-13 23:03:33.838898
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("imports.py")
    except IntroducedSyntaxErrors as e:
        # check that the exception's message is correct
        error_message = (
            "isort introduced syntax errors when attempting to sort the imports contained" " within imports.py."
        )
        assert e.args[0] == error_message
        # check that the exception's file_path attribute is correct
        assert e.file_path == "imports.py"

# Generated at 2022-06-13 23:03:37.713897
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = "flask"
    section = "first-party"

    error = MissingSection(import_module, section)
    assert import_module in error.__str__() and section in error.__str__()

# Generated at 2022-06-13 23:03:40.845325
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("filename")
    except ISortError as e:
        assert "Unknown or unsupported encoding in filename" == e.args[0]


if __name__ == "__main__":
    test_UnsupportedEncoding()

# Generated at 2022-06-13 23:03:50.579106
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    filename = "Dummy"
    try:
        raise IntroducedSyntaxErrors(filename)
    except IntroducedSyntaxErrors as e:
        assert filename == e.file_path

# Generated at 2022-06-13 23:03:55.889579
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():
    input_settings_path = "D:\home\isort_path"
    with pytest.raises(InvalidSettingsPath) as e:
        raise InvalidSettingsPath(settings_path=input_settings_path)
    assert input_settings_path == str(e.value)



# Generated at 2022-06-13 23:04:05.999234
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    error = ValueError('arbitrary error msg')
    test = LiteralParsingFailure(code='test-code', original_error=error)
    print(test)
    assert str(test) == (f"isort failed to parse the given literal test-code. It's important "
                         f"to note that isort literal sorting only supports simple literals "
                         f"parsable by ast.literal_eval which gave the exception of "
                         f"{error}.")
    assert test.code == 'test-code'
    assert test.original_error == error


# Generated at 2022-06-13 23:04:08.403769
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    a = FileSkipSetting("ff")
    print(a.message)
    print(a.file_path)

# Generated at 2022-06-13 23:04:11.286411
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    error = ProfileDoesNotExist('my_profile')
    assert error.profile == 'my_profile'

# Generated at 2022-06-13 23:04:17.079101
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    try:
        raise FileSkipped("Type of Error", "the File's Location")
    except FileSkipped as e:
        assert e.message == "Type of Error"
        assert e.file_path == "the File's Location"
    else:
        assert False, "Expected Exception to be raised"


# Generated at 2022-06-13 23:04:23.406526
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        raise MissingSection
    except ISortError as e:
        assert e.__str__() == "Found import while parsing, but was not included in the `sections` setting of your config. Please add it before continuing\nSee https://pycqa.github.io/isort/#custom-sections-and-ordering for more info."
    except:
        assert False


# Generated at 2022-06-13 23:04:25.434253
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    assert UnsupportedSettings({'foo': {'value': 'bar', 'source': 'baz'}})

# Generated at 2022-06-13 23:04:31.457850
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    try:
        raise IntroducedSyntaxErrors("file.py")
    except IntroducedSyntaxErrors as e:
        assert e.file_path == "file.py"
        assert str(e) == "isort introduced syntax errors when attempting to sort the imports contained within file.py."



# Generated at 2022-06-13 23:04:38.863232
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist('foobar')
    except ProfileDoesNotExist as e:
        assert e.profile == 'foobar'
        assert str(e) == f"Specified profile of foobar does not exist. " \
                         f"Available profiles: {','.join(profiles)}."
    else:
        raise AssertionError("Expected ProfileDoesNotExist to be raised")