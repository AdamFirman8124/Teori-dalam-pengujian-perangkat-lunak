

# Generated at 2026-10-25 10:46:26.664517
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

# Generated at 2026-10-25 10:46:28.186618
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

# Generated at 2026-10-25 10:46:29.634858
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

# Generated at 2026-10-25 10:46:31.392267
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

# Generated at 2026-10-25 10:46:37.007626
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "test.py"
    error = FileSkipComment(file_path)

    assert isinstance(error, FileSkipped)
    assert isinstance(error, ISortError)
    assert error.file_path == file_path
    assert str(error) == f"{file_path} contains an file skip comment and was skipped."

# Generated at 2026-10-25 10:46:44.070948
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-25 10:46:45.504281
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

# Generated at 2026-10-25 10:46:46.848556
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:46:48.284954
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:46:49.804753
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-25 10:46:52.877915
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

# Generated at 2026-10-25 10:46:54.415017
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:46:55.762660
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:46:57.085117
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-25 10:46:58.614303
# Unit test for constructor of class IntroducedSyntaxErrors
def test_IntroducedSyntaxErrors():
    file_path = "example.py"
    error = IntroducedSyntaxErrors(file_path)

    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)
    assert error.file_path == file_path
    assert str(error) == (
        "isort introduced syntax errors when attempting to sort the imports contained within "
        f"{file_path}."
    )

# Generated at 2026-10-25 10:47:00.148205
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

# Generated at 2026-10-25 10:47:12.333400
# Unit test for constructor of class FileSkipSetting
def test_FileSkipSetting():file_path = "src/example.py"

# Generated at 2026-10-25 10:47:13.681395
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

# Generated at 2026-10-25 10:47:15.096812
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:47:16.468348
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-25 10:47:19.011849
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:47:21.679357
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:47:24.259889
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-25 10:47:26.924573
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:47:29.343565
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:47:31.761733
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-25 10:47:34.174210
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:36.628495
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:39.043601
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:41.462287
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:44.280208
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:46.699611
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:49.113377
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:51.532827
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:53.951986
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:56.367938
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:47:58.779710
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:01.193210
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:03.609770
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:06.023920
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:08.439098
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:10.855032
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:13.271580
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:15.685585
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:18.100024
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:20.516069
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:22.929804
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:25.344898
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:27.760115
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:30.175384
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:32.587965
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:35.033289
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:37.447532
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:39.862173
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:42.285404
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-25 10:48:44.697454
# Unit test for constructor of class FileSkipSetting