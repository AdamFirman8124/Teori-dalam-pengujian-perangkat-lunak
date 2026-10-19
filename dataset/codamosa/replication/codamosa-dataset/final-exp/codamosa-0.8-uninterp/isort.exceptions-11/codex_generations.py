

# Generated at 2022-06-13 23:00:36.379038
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    obj = LiteralParsingFailure("test_code", "test_error")
    assert obj.code == "test_code"
    assert obj.original_error == "test_error"


# Generated at 2022-06-13 23:00:38.053796
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    unsupported_encoding_instance = UnsupportedEncoding(filename='my-filename.py')
    assert unsupported_encoding_instance.filename == 'my-filename.py'

# Generated at 2022-06-13 23:00:42.844631
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    assert ExistingSyntaxErrors("test.py").file_path == "test.py"

# Generated at 2022-06-13 23:00:49.476687
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    obj = UnsupportedEncoding(filename='')
    assert isinstance(obj, ISortError)
    assert obj.args == ("Unknown or unsupported encoding in ''",)
    assert obj.args[0] == 'Unknown or unsupported encoding in '


if __name__ == '__main__':
    test_UnsupportedEncoding()

# Generated at 2022-06-13 23:00:55.584467
# Unit test for constructor of class MissingSection
def test_MissingSection():
    try:
        raise MissingSection("requests","TEST")
    except Exception as e:
        assert str(e) == "Found requests import while parsing, but TEST was not included " + \
                         "in the `sections` setting of your config. Please add it before continuing\n" \
                         "See https://pycqa.github.io/isort/#custom-sections-and-ordering " \
                         "for more info."


# Generated at 2022-06-13 23:00:57.604925
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError
    except ISortError:
        pass


# Generated at 2022-06-13 23:01:01.996831
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    message = "This file is ignored for testing reasons."
    file_path = "teste.py"
    FileSkipComment(file_path)
    assert FileSkipComment(file_path).message == message
    assert FileSkipComment(file_path).file_path == file_path


# Generated at 2022-06-13 23:01:24.123612
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    """Unit test for class LiteralParsingFailure"""
    class Fnord:
        pass

    instance = Fnord()
    test_exception = LiteralParsingFailure(instance, "foo")
    assert test_exception.code == instance
    assert test_exception.original_error == "foo"

# Generated at 2022-06-13 23:01:26.118073
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file = FileSkipComment('file1')
    assert file.file_path == 'file1'


# Generated at 2022-06-13 23:01:27.741230
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    FileSkipComment(file_path='example1.py')

# Generated at 2022-06-13 23:01:40.153174
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    x = UnsupportedSettings({"test_1": {"value": "test_1", "source": "test"},
                             "test_2": {"value": "test_2", "source": "test_2"}})
    assert x.unsupported_settings == {"test_1": {"value": "test_1", "source": "test"},
                                      "test_2": {"value": "test_2", "source": "test_2"}}



# Generated at 2022-06-13 23:01:47.305467
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    try:
        raise ProfileDoesNotExist("django")
    except ProfileDoesNotExist as exc:
        assert exc.profile == "django"
        assert "Specified profile of django does not exist" in str(exc)
        assert "Available profiles: black" in str(exc)


# Generated at 2022-06-13 23:01:51.770974
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    f = FileSkipped("test", "file_path")
    assert f.file_path == "file_path"
    assert str(f) == "test"

# Generated at 2022-06-13 23:02:07.874219
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    raise FileSkipSetting("test.py")

# Generated at 2022-06-13 23:02:10.187035
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file = 'test'
    assert IntroducedSyntaxErrors(file).file_path == file

# Generated at 2022-06-13 23:02:12.522664
# Unit test for constructor of class ISortError
def test_ISortError():
    try:
        raise ISortError
    except ISortError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 23:02:18.033260
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    filename = 'myfile.py'

    try:
        raise FileSkipped('Skipped because of foo', filename)
    except FileSkipped as e:
        assert e.file_path == filename
        assert e.args[0] == 'Skipped because of foo'

# Generated at 2022-06-13 23:02:21.046639
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    assert FileSkipped('Message', 'File path').message == 'File path'
    assert FileSkipped('Message', 'File path').file_path == 'File path'


# Generated at 2022-06-13 23:02:25.815691
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    try:
        raise UnsupportedEncoding("filename")
    except UnsupportedEncoding as e:
        assert e.filename == "filename"

# Generated at 2022-06-13 23:02:32.366874
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    settings = {
        "foo": {"value": "bar", "source": "mock"},
    }
    instance = UnsupportedSettings(settings)
    assert "foo = bar" in instance.unsupported_settings["foo"]["value"]
    assert "mock" in instance.unsupported_settings["foo"]["source"]