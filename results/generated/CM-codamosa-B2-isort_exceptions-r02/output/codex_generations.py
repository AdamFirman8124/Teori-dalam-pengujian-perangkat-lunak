

# Generated at 2026-10-25 10:19:21.685204
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    exc = FileSkipSetting(file_path)

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    assert exc.file_path == file_path

    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-25 10:19:35.492174
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():file_path = "example.py"

# Generated at 2026-10-25 10:19:37.917466
# Unit test for constructor of class MissingSection

# Generated at 2026-10-25 10:19:40.331990
# Unit test for constructor of class MissingSection

# Generated at 2026-10-25 10:19:42.987123
# Unit test for constructor of class MissingSection

# Generated at 2026-10-25 10:19:45.402673
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-25 10:19:47.945448
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-25 10:19:50.358329
# Unit test for constructor of class UnsupportedEncoding

# Generated at 2026-10-25 10:19:52.770083
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:19:55.184044
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:19:59.863563
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():from isort.exceptions import IntroducedSyntaxErrors

error = IntroducedSyntaxErrors("example_file.py")
assert error.file_path == "example_file.py"
assert isinstance(error, Exception)
assert "example_file.py" in str(error)
assert "isort introduced syntax errors" in str(error)

# Generated at 2026-10-25 10:20:16.253862
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "x = 1, y = 2"

    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch(code)

    exc = exc_info.value

    assert isinstance(exc, ISortError)
    assert exc.code == code
    assert str(exc) == (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

# Generated at 2026-10-25 10:20:26.180848
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:20:34.987948
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:20:47.991013
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:20:52.497433
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:20:53.930734
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:20:55.364606
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:20:58.231290
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:20:59.663996
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:21:01.098343
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:21:02.531837
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:21:03.968749
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:21:05.408535
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:21:06.759477
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:08.164492
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:09.505158
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:21:10.845503
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:21:12.260405
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:21:13.693390
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:15.127553
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:16.481264
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:21:17.891758
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:19.229802
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:22.204492
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:21:23.625965
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:24.962224
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:27.927181
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:21:29.360894
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:21:31.902690
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:34.566041
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:36.979841
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:39.394594
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:41.814376
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:44.414604
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:46.830097
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:49.246880
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:51.658689
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:54.072710
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:56.489867
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:21:58.903862
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:22:01.319565
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:22:03.773685
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:22:13.189470
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = int

# Generated at 2026-10-25 10:22:14.622255
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:16.165127
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:22:17.902940
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:20.974907
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:25.685712
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:22:27.116641
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:41.910467
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:43.294674
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:22:44.728453
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:46.160990
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:51.531341
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:22:53.028575
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:54.513045
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:22:57.203394
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:22:59.892850
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:02.312137
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:04.726130
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:07.141273
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:09.557770
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:11.972213
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:18.560873
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:20.056220
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:21.808660
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:23:23.845180
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:25.184585
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:27.224273
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:23:28.760993
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:30.194751
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:31.627597
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:23:32.954311
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:40.769652
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:42.107664
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:23:43.475655
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:44.766547
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:46.272148
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:23:47.599812
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:49.861937
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:52.928481
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:23:54.565030
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:23:56.983868
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:23:59.516992
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:01.930614
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:04.345972
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:06.760255
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:09.175699
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:11.593097
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:14.005865
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:16.421546
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:18.838521
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:21.252819
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:23.668088
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:26.084063
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:28.498187
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:30.913489
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:33.328532
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:35.744111
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:38.159360
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:24:40.303981
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:41.772846
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:24:43.206905
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:45.768141
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:47.247003
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:24:48.629423
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:50.067887
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:51.410787
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:24:52.804875
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:54.136222
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:24:57.031619
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:24:58.384328
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:01.331422
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:02.873988
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:25:17.435663
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:19.852998
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:22.269575
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:24.685202
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:27.102169
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:29.684754
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:32.103737
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:34.513048
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:36.929410
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:39.344498
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:41.757166
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:44.171219
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:25:45.498301
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:46.898428
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:48.311648
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:25:50.482914
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:51.915799
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:53.294615
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:25:54.683623
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:56.114207
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:25:57.653617
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = float
    expected_kind = int

    # Act: construct the exception
    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Assert: attributes are stored on the instance
    assert error.kind == kind
    assert error.expected_kind == expected_kind

    # Assert: it inherits from the isort base exception
    from isort.exceptions import ISortError
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Assert: message mentions both types, expected first
    message = str(error)
    assert str(expected_kind) in message
    assert str(kind) in message
    assert message.index(str(expected_kind)) < message.index(str(kind))

# Generated at 2026-10-25 10:25:59.290884
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:26:14.297744
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:26:15.980559
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    exc = FileSkipSetting(file_path)

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    assert exc.file_path == file_path

    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-25 10:26:29.703705
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():file_path = "example.py"

# Generated at 2026-10-25 10:26:32.119864
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 10:26:34.534552
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 10:26:37.182938
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 10:26:39.596753
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 10:26:42.011188
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 10:26:44.424627
# Unit test for constructor of class ExistingSyntaxErrors

# Generated at 2026-10-25 10:26:46.846521
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 10:26:49.259608
# Unit test for constructor of class InvalidSettingsPath

# Generated at 2026-10-25 10:26:56.005439
# Unit test for constructor of class InvalidSettingsPath
def test_InvalidSettingsPath():exc = InvalidSettingsPath("/nonexistent/settings/path")

# Generated at 2026-10-25 10:27:02.265927
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    import pytest
    from .exceptions import ProfileDoesNotExist

    profile = "nonexistent_profile"

    with pytest.raises(ProfileDoesNotExist) as exc_info:
        ProfileDoesNotExist(profile)

    # Verify the exception's attributes and message
    assert exc_info.value.profile == profile
    assert "Specified profile of nonexistent_profile does not exist." in str(exc_info.value)
    assert "Available profiles:" in str(exc_info.value)

# Generated at 2026-10-25 10:27:09.828461
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "test.py"
    error = FileSkipComment(file_path)

    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-25 10:27:11.381237
# Unit test for constructor of class FormattingPluginDoesNotExist
def test_FormattingPluginDoesNotExist():
    error = FormattingPluginDoesNotExist("black")

    assert isinstance(error, ISortError)
    assert error.formatter == "black"
    assert str(error) == "Specified formatting plugin of black does not exist. "

# Generated at 2026-10-25 10:27:16.106396
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    filename = "example.py"
    error = UnsupportedEncoding(filename)

    assert isinstance(error, Exception)
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert error.filename == filename


def test_UnsupportedEncoding_with_path():
    filename = Path("/tmp/example.py")
    error = UnsupportedEncoding(filename)

    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert error.filename == filename

# Generated at 2026-10-25 10:27:20.596115
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "File skipped due to test condition"
    file_path = "example.py"

    error = FileSkipped(message, file_path)

    assert isinstance(error, ISortError)
    assert str(error) == message
    assert error.file_path == file_path

# Generated at 2026-10-25 10:27:23.582765
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    exc = FileSkipSetting(file_path)

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    assert exc.file_path == file_path

    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-25 10:27:26.051053
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:27:28.455775
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:27:32.806405
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-25 10:27:35.221917
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-25 10:27:37.636075
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-25 10:27:40.249823
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 10:27:42.824270
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 10:27:45.250832
# Unit test for constructor of class LiteralParsingFailure

# Generated at 2026-10-25 10:27:47.663689
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:27:50.078069
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:27:51.770521
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():from isort.exceptions import IntroducedSyntaxErrors

error = IntroducedSyntaxErrors("example_file.py")
assert error.file_path == "example_file.py"
assert isinstance(error, Exception)
assert "example_file.py" in str(error)
assert "isort introduced syntax errors" in str(error)

# Generated at 2026-10-25 10:27:59.507586
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = "os.path"
    section = "THIRDPARTY"

    exception = MissingSection(import_module=import_module, section=section)

    # Constructor must succeed and produce an ISortError
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Message must name both the module and the missing section
    message = str(exception)
    assert import_module in message
    assert section in message
    assert "sections" in message  # points user at the setting to fix

    # Constructor accepts positional args too
    exception_positional = MissingSection("json", "STDLIB")
    assert "json" in str(exception_positional)
    assert "STDLIB" in str(exception_positional)

# Generated at 2026-10-25 10:28:01.002610
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    import pytest
    from .exceptions import ProfileDoesNotExist

    profile = "nonexistent_profile"

    with pytest.raises(ProfileDoesNotExist) as exc_info:
        ProfileDoesNotExist(profile)

    # Verify the exception's attributes and message
    assert exc_info.value.profile == profile
    assert "Specified profile of nonexistent_profile does not exist." in str(exc_info.value)
    assert "Available profiles:" in str(exc_info.value)

# Generated at 2026-10-25 10:28:02.581344
# Unit test for constructor of class MissingSection
def test_MissingSection():
    import_module = "os.path"
    section = "THIRDPARTY"

    exception = MissingSection(import_module=import_module, section=section)

    # Constructor must succeed and produce an ISortError
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Message must name both the module and the missing section
    message = str(exception)
    assert import_module in message
    assert section in message
    assert "sections" in message  # points user at the setting to fix

    # Constructor accepts positional args too
    exception_positional = MissingSection("json", "STDLIB")
    assert "json" in str(exception_positional)
    assert "STDLIB" in str(exception_positional)

# Generated at 2026-10-25 10:28:04.013332
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "test.py"
    error = FileSkipComment(file_path)

    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-25 10:28:13.639145
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "test.py"
    error = FileSkipComment(file_path)

    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-25 10:28:21.626500
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    code = "{'unbalanced': [1, 2"
    original_error = SyntaxError("unexpected EOF while parsing")

    exception = LiteralParsingFailure(code, original_error)

    # Attributes are stored on the exception instance
    assert exception.code == code
    assert exception.original_error is original_error

    # It is an isort exception and an Exception
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # Message contains the code and the original error
    message = str(exception)
    assert code in message
    assert "ast.literal_eval" in message
    assert str(original_error) in message

# Generated at 2026-10-25 10:28:23.073308
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    exc = FileSkipSetting(file_path)

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    assert exc.file_path == file_path

    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-25 10:28:35.552164
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():file_path = "example.py"

# Generated at 2026-10-25 10:28:42.207008
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "test.py"
    error = FileSkipComment(file_path)

    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-25 10:28:46.101226
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported = {
        "bad_option": {"name": "bad_option", "value": "1", "source": "config"},
        "other_option": {"name": "other_option", "value": "x", "source": "cli"},
    }

    error = UnsupportedSettings(unsupported)

    assert error.unsupported_settings == unsupported
    assert "isort was provided settings that it doesn't support:" in str(error)
    assert "\t- bad_option = 1  (source: 'config')" in str(error)
    assert "\t- other_option = x  (source: 'cli')" in str(error)
    assert "https://pycqa.github.io/isort/docs/configuration/options/" in str(error)

# Generated at 2026-10-25 10:28:48.848964
# Unit test for constructor of class ISortError

# Generated at 2026-10-25 10:28:51.265226
# Unit test for constructor of class ISortError

# Generated at 2026-10-25 10:28:55.560802
# Unit test for constructor of class ISortError
def test_ISortError():error = ISortError("something went wrong")

# Generated at 2026-10-25 10:28:56.957251
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "File skipped due to test condition"
    file_path = "example.py"

    error = FileSkipped(message, file_path)

    assert isinstance(error, ISortError)
    assert str(error) == message
    assert error.file_path == file_path

# Generated at 2026-10-25 10:28:58.436165
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():
    file_path = "example.py"
    exc = FileSkipSetting(file_path)

    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    assert exc.file_path == file_path

    expected_message = (
        f"{file_path} was skipped as it's listed in 'skip' setting"
        " or matches a glob in 'skip_glob' setting"
    )
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-25 10:29:06.989211
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():exc = FileSkipSetting("example.py")