

# Generated at 2026-10-25 04:02:50.936914
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "{'a': 1, 'b': }"  # malformed literal isort can't parse
    original_error = ValueError("malformed node")
    exception = LiteralParsingFailure(code, original_error)

    # Attributes are stored on the instance
    assert exception.code == code
    assert exception.original_error is original_error

    # Exception is part of the isort hierarchy
    assert isinstance(exception, ISortError)

    # Message includes both the failing code and the underlying error
    message = str(exception)
    assert code in message
    assert str(original_error) in message
    assert "ast.literal_eval" in message

# Generated at 2026-10-25 04:02:53.355471
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 04:02:55.771432
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 04:03:01.958368
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():from isort.exceptions import ISortError


# Generated at 2026-10-25 04:03:07.882865
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    from isort.exceptions import UnsupportedEncoding

    # str input
    exc = UnsupportedEncoding("my_file.py")
    assert exc.filename == "my_file.py"
    assert "my_file.py" in str(exc)
    assert isinstance(exc, Exception)

    # Path input
    path = Path("/tmp/some_file.py")
    exc = UnsupportedEncoding(path)
    assert exc.filename == path
    assert str(path) in str(exc)

# Generated at 2026-10-25 04:03:09.561726
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "bad_option": {"value": "foo", "source": "pyproject.toml"},
        "another_bad": {"value": 123, "source": "setup.cfg"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    # stores input
    assert isinstance(exc, ISortError)
    assert exc.unsupported_settings == unsupported_settings

    # formats message via _format_option
    message = str(exc)
    assert "isort was provided settings that it doesn't support:" in message
    assert "\t- bad_option = foo  (source: 'pyproject.toml')" in message
    assert "\t- another_bad = 123  (source: 'setup.cfg')" in message
    assert "https://pycqa.github.io/isort/docs/configuration/options/" in message

    # exact formatting for single option
    single = {"unknown_opt": {"value": "bar", "source": "isort.cfg"}}
    single_exc = UnsupportedSettings(single)
    expected_errors = "\t- unknown_opt = bar  (source: 'isort.cfg')"
    expected_msg = (
        "isort was provided settings that it doesn't support:\n\n"
        f"{expected_errors}\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )
    assert single_exc.args[0] == expected_msg

# Generated at 2026-10-25 04:03:10.924247
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():error = UnsupportedSettings({"apply": {"name": "apply", "value": "true", "source": "CLI"}})

# Generated at 2026-10-25 04:03:12.254793
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 04:03:13.657077
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/fake/path/does_not_exist"

# Generated at 2026-10-25 04:03:14.985667
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"

    with pytest.raises(IntroducedSyntaxErrors) as exc_info:
        raise IntroducedSyntaxErrors(file_path)

    exc = exc_info.value
    assert exc.file_path == file_path
    assert str(exc) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-25 04:03:20.173852
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"

    error = FileSkipSetting(file_path)

    assert isinstance(error, FileSkipped)
    assert error.file_path == file_path
    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )

# Generated at 2026-10-25 04:03:26.420345
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, ISortError)
    assert error.formatter == formatter
    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "

# Generated at 2026-10-25 04:03:32.560917
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "path/to/file.py"

    error = ExistingSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: "
        "path/to/file.py."
    )

# Generated at 2026-10-25 04:03:37.066853
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert error.formatter == formatter
    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 04:03:41.075416
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "
    assert error.args == ("Specified formatting plugin of black does not exist. ",)

# Generated at 2026-10-25 04:03:45.975179
# Unit test for constructor of class ExistingSyntaxErrors
def test_ExistingSyntaxErrors():
    file_path = "example.py"

    error = ExistingSyntaxErrors(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "isort was told to sort imports within code that contains syntax errors: example.py."
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 04:03:48.500490
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 04:03:50.915220
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 04:03:53.330923
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 04:03:55.746457
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 04:03:58.161458
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 04:04:04.828741
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )
    assert error.file_path == file_path
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 04:04:06.169757
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:07.501941
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:08.833790
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:10.254722
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:11.677416
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:13.110538
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:14.544430
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:15.977579
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:17.308783
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:18.742921
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:20.177255
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:21.610322
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:23.043670
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:24.383221
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:25.717849
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:27.140212
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:28.573456
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:29.900763
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:31.232812
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:32.669313
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:34.103539
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:04:35.536512
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:04:38.062721
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:40.480503
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:43.035212
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:45.454471
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:47.866985
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:50.280687
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:52.695302
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:55.111658
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:57.530411
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:04:59.947183
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:02.362841
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:04.777915
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:07.199583
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:09.617065
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:12.031256
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:18.139639
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-25 04:05:19.502292
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:20.836678
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:22.219323
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:23.665131
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:25.083689
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:26.420989
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:27.754377
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:29.097888
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:30.429867
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:31.764666
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:33.102117
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:34.518710
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:35.911657
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:37.306669
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:38.638782
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:40.048478
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:41.383921
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:42.813222
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:44.215914
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 04:05:45.547917
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    error = LiteralSortTypeMismatch(kind=list, expected_kind=dict)

    assert isinstance(error, ISortError)
    assert error.kind is list
    assert error.expected_kind is dict
    assert str(error) == (
        "isort was told to sort a literal of type <class 'dict'> but was given "
        "a literal of type <class 'list'>."
    )

    with pytest.raises(LiteralSortTypeMismatch):
        raise LiteralSortTypeMismatch(kind=list, expected_kind=dict)

# Generated at 2026-10-25 04:05:48.074922
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:50.494222
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:53.019624
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:55.433242
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 04:05:57.970350
# Unit test for constructor of class LiteralSortTypeMismatch