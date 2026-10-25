

# Generated at 2026-10-25 03:09:55.886346
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-25 03:09:58.303410
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-25 03:10:00.718349
# Unit test for constructor of class AssignmentsFormatMismatch

# Generated at 2026-10-25 03:10:03.133729
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:10:05.548860
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:10:07.963823
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:10:10.378119
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 03:10:12.792787
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 03:10:15.208737
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 03:10:17.623263
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 03:10:20.037686
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 03:10:24.542437
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():error = IntroducedSyntaxErrors("example.py")

# Generated at 2026-10-25 03:10:29.443477
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"

    error = FileSkipSetting(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 03:10:30.876240
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

# Generated at 2026-10-25 03:10:34.254914
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():error = UnsupportedSettings({"apply": {"name": "apply", "value": "true", "source": "CLI"}})

# Generated at 2026-10-25 03:10:42.560100
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

# Generated at 2026-10-25 03:10:45.518988
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:10:46.875246
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:10:48.291363
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

# Generated at 2026-10-25 03:10:49.716995
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():error = UnsupportedSettings({"apply": {"name": "apply", "value": "true", "source": "CLI"}})

# Generated at 2026-10-25 03:10:51.135059
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

# Generated at 2026-10-25 03:10:53.552758
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:10:55.967623
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:10:58.382090
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:00.796990
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:03.211359
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:05.626379
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:08.041051
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:10.635500
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:13.204457
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:15.618796
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:18.034333
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:20.449698
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:22.872932
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:25.289091
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:11:27.707327
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:11:30.122348
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:11:32.536210
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:11:38.562737
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = list

# Generated at 2026-10-25 03:11:40.200410
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:41.634324
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:43.068095
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

# Generated at 2026-10-25 03:11:44.443329
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:45.772019
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:47.101430
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

# Generated at 2026-10-25 03:11:48.431377
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:49.757950
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:51.108796
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

# Generated at 2026-10-25 03:11:52.447960
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:53.775125
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:55.108692
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

# Generated at 2026-10-25 03:11:56.461329
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:57.826307
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:11:59.170527
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

# Generated at 2026-10-25 03:12:01.723739
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:04.137954
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:06.552052
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:08.966715
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:11.380193
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:13.797068
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:16.211384
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:18.625852
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:21.040565
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:23.456445
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:25.872566
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:28.286859
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:30.703928
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:33.119844
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:35.532308
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:37.949570
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:40.362141
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:42.779935
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:45.195372
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:47.609355
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:50.024212
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:12:51.471816
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:12:52.908080
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:12:54.251901
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

# Generated at 2026-10-25 03:12:55.672614
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:12:56.992440
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:12:58.332580
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

# Generated at 2026-10-25 03:12:59.661120
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:00.994702
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:02.345509
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

# Generated at 2026-10-25 03:13:03.694481
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:05.075745
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:06.634014
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

# Generated at 2026-10-25 03:13:07.961534
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:09.288919
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:11.810538
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:14.226202
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:16.640782
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:19.056522
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:21.637405
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:24.049472
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:26.469244
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:28.884482
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:31.309722
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:33.721934
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:36.136390
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:38.550082
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:40.965629
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:43.382068
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:45.795902
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:48.208796
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:50.623635
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:13:55.574189
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)

# Generated at 2026-10-25 03:13:56.914312
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

# Generated at 2026-10-25 03:13:58.236460
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:13:59.669780
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:00.999323
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

# Generated at 2026-10-25 03:14:02.375720
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:03.754819
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:05.087028
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

# Generated at 2026-10-25 03:14:06.534547
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:07.866907
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:09.189469
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

# Generated at 2026-10-25 03:14:10.555865
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:11.920398
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:13.301830
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

# Generated at 2026-10-25 03:14:14.628339
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:14:17.154273
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:19.568633
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:21.982687
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:24.558906
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:26.973771
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:29.388637
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:31.808399
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:34.221616
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:36.636487
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:39.050953
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:14:41.467470
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:14:43.884735
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:14:46.300779
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:14:48.716058
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-25 03:14:51.130319
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-25 03:14:53.544142
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-25 03:14:55.959410
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:14:58.374055
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:00.788286
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:03.202505
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:05.618349
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:08.035531
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:10.449299
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:15:12.863947
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:15:15.283181
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:15:17.702009
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:15:20.114651
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:15:22.528997
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:15:24.943711
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:27.358084
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:29.775464
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:15:32.205890
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:15:34.609248
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:15:43.552226
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():formatter = "black"

# Generated at 2026-10-25 03:15:49.346593
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

# Generated at 2026-10-25 03:15:50.775369
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:16:01.489138
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/fake/path/does_not_exist"

# Generated at 2026-10-25 03:16:02.960526
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

# Generated at 2026-10-25 03:16:08.695886
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "foo = 1\nbar = 2"

    error = AssignmentsFormatMismatch(code)

    expected_message = (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

    assert error.code == code
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 03:16:17.091765
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "a = 1\nb = 2"
    error = AssignmentsFormatMismatch(code)

    expected_message = (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.code == code

    other_code = "x = [1, 2, 3]"
    other_error = AssignmentsFormatMismatch(other_code)
    assert other_error.code == other_code
    assert other_code in str(other_error)
    assert str(other_error) == expected_message.replace(code, other_code)
    assert other_error.code != error.code

# Generated at 2026-10-25 03:16:18.525876
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "a = 1\nb = 2"
    error = AssignmentsFormatMismatch(code)

    expected_message = (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert str(error) == expected_message
    assert error.args == (expected_message,)
    assert error.code == code

    other_code = "x = [1, 2, 3]"
    other_error = AssignmentsFormatMismatch(other_code)
    assert other_error.code == other_code
    assert other_code in str(other_error)
    assert str(other_error) == expected_message.replace(code, other_code)
    assert other_error.code != error.code

# Generated at 2026-10-25 03:16:23.955963
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"

    error = FileSkipComment(file_path)

    assert error.file_path == file_path
    assert str(error) == "example.py contains an file skip comment and was skipped."
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 03:16:29.994972
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

# Generated at 2026-10-25 03:16:31.329072
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:16:33.752868
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:16:36.293985
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:16:38.709477
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-25 03:16:41.124899
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-25 03:16:43.539636
# Unit test for constructor of class FileSkipComment

# Generated at 2026-10-25 03:16:49.143416
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert isinstance(error, ISortError)
    assert error.formatter == formatter
    assert str(error) == "Specified formatting plugin of unknown_formatter does not exist. "

# Generated at 2026-10-25 03:16:50.557852
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

# Generated at 2026-10-25 03:16:52.010470
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:16:53.388502
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/fake/path/does_not_exist"

# Generated at 2026-10-25 03:16:59.690519
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    formatter = "unknown_formatter"

    error = FormattingPluginDoesNotExist(formatter)

    assert error.formatter == formatter
    assert str(error) == (
        "Specified formatting plugin of unknown_formatter does not exist. "
    )
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 03:17:01.320970
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:17:02.722480
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():settings_path = "/fake/path/does_not_exist"

# Generated at 2026-10-25 03:17:08.693034
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent-profile"

    error = ProfileDoesNotExist(profile)

    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(error) == expected_message
    assert error.profile == profile
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 03:17:12.595541
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():error = ProfileDoesNotExist("nonexistent")


# Generated at 2026-10-25 03:17:15.011215
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:17:17.425313
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:17:19.841001
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:17:22.256869
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:17:24.672477
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:17:27.091022
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:17:29.508548
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 03:17:31.922400
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 03:17:34.337578
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 03:17:36.753308
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:17:39.171485
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:17:41.585315
# Unit test for constructor of class FormattingPluginDoesNotExist

# Generated at 2026-10-25 03:17:44.006741
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:17:46.423334
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:17:48.839084
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-25 03:17:51.253176
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:17:53.669350
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:17:56.083248
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:17:58.498064
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:18:00.916765
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:18:03.337564
# Unit test for constructor of class FileSkipped

# Generated at 2026-10-25 03:18:05.749206
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:18:08.165929
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:18:10.583564
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 03:18:13.462178
# Unit test for constructor of class ISortError

# Generated at 2026-10-25 03:18:15.876051
# Unit test for constructor of class ISortError

# Generated at 2026-10-25 03:18:18.292933
# Unit test for constructor of class ISortError

# Generated at 2026-10-25 03:18:20.707077
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:18:23.124576
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:18:25.549326
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:18:27.964925
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:18:30.379658
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:18:32.795887
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:18:35.211024
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-25 03:18:37.625149
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-25 03:18:40.038617
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-25 03:18:42.453842
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:18:53.149774
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():exc = FileSkipSetting("example.py")

# Generated at 2026-10-25 03:18:59.296654
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"

    error = FileSkipSetting(file_path)

    assert error.file_path == file_path
    assert str(error) == (
        "example.py was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)

# Generated at 2026-10-25 03:19:00.653400
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

# Generated at 2026-10-25 03:19:02.060208
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:19:03.493073
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(kind=dict, expected_kind=list)

# Generated at 2026-10-25 03:19:17.800280
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    exc = FileSkipped("File skipped for testing", file_path="example.py")

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert str(exc) == "File skipped for testing"
    assert exc.args == ("File skipped for testing",)
    assert exc.file_path == "example.py"

# Generated at 2026-10-25 03:19:20.216577
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 03:19:22.746911
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 03:19:25.161681
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 03:19:27.576862
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:19:29.993794
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:19:32.585024
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 03:19:37.295805
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:19:39.712095
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:19:42.126367
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 03:19:44.541382
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 03:19:47.111277
# Unit test for constructor of class IntroducedSyntaxErrors