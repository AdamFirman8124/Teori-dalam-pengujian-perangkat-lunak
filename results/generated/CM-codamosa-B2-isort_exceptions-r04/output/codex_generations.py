

# Generated at 2026-10-24 07:11:17.547055
# Unit test for constructor of class ISortError
def test_ISortError():
    message = "An isort error occurred"

    error = ISortError(message)

    assert isinstance(error, Exception)
    assert str(error) == message
    assert error.args == (message,)

# Generated at 2026-10-24 07:11:18.879947
# Unit test for constructor of class FileSkipped
def test_FileSkipped():import unittest


class TestFileSkipped(unittest.TestCase):
    """Unit test for constructor of class FileSkipped"""

    def test_constructor(self):
        message = "test message: file skipped"
        file_path = "/path/to/skipped_file.py"

        exception = FileSkipped(message, file_path)

        # Constructor stores the file path and passes message to base Exception
        self.assertEqual(exception.file_path, file_path)
        self.assertEqual(str(exception), message)

    def test_inheritance(self):
        # FileSkipped must inherit from ISortError (and therefore Exception)
        self.assertTrue(issubclass(FileSkipped, ISortError))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-10-24 07:11:20.205411
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 07:11:27.861935
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, list)

assert str(error) == (
    "isort was told to sort a literal of type <class 'list'> "
    "but was given a literal of type <class 'str'>."
)
assert error.kind is str
assert error.expected_kind is list

# Generated at 2026-10-24 07:11:35.338165
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():from isort.exceptions import ISortError, LiteralSortTypeMismatch


# Generated at 2026-10-24 07:11:37.897852
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-24 07:11:40.321293
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-24 07:11:42.727929
# Unit test for constructor of class FileSkipSetting

# Generated at 2026-10-24 07:11:45.148077
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-24 07:11:47.568315
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-24 07:11:49.979652
# Unit test for constructor of class IntroducedSyntaxErrors

# Generated at 2026-10-24 07:11:52.394047
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:11:54.804936
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:11:57.219298
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:11:59.632630
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 07:12:02.047293
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 07:12:04.462150
# Unit test for constructor of class ProfileDoesNotExist

# Generated at 2026-10-24 07:12:06.877366
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 07:12:09.291807
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 07:12:11.705539
# Unit test for constructor of class UnsupportedSettings

# Generated at 2026-10-24 07:12:14.117159
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:12:16.532237
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:12:19.139562
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-24 07:12:35.547415
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"
    exception = FileSkipComment(file_path)

    # Inherits from FileSkipped -> ISortError -> Exception
    assert isinstance(exception, FileSkipped)
    assert isinstance(exception, ISortError)

    # file_path attribute is stored correctly
    assert exception.file_path == file_path

    # Message mentions the file and the skip comment reason
    message = str(exception)
    assert file_path in message
    assert "file skip comment" in message

# Generated at 2026-10-24 07:12:36.982157
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    # Arrange
    profile = "no_such_profile"

    # Act
    exc = ProfileDoesNotExist(profile)

    # Assert - type hierarchy
    assert isinstance(exc, ProfileDoesNotExist)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    # Assert - stored attribute preserves input exactly
    assert exc.profile == profile

    # Assert - message passed to base Exception
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert exc.args[0] == expected_message
    assert str(exc) == expected_message

    # Assert - usable with raise / except ISortError
    try:
        raise ProfileDoesNotExist(profile)
    except ISortError as caught:
        assert caught.profile == profile
        assert str(caught) == expected_message
    else:
        assert False, "ProfileDoesNotExist was not raised"

# Generated at 2026-10-24 07:12:43.332606
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist

    profile = "nonexistent_profile"
    error = ProfileDoesNotExist(profile)

    assert error.profile == profile
    assert isinstance(error, Exception)
    assert profile in str(error)
    assert "does not exist" in str(error)
    assert "Available profiles:" in str(error)

# Generated at 2026-10-24 07:13:08.541124
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():
    file_path = "example.py"
    expected_message = f"{file_path} contains an file skip comment and was skipped."

    exc = FileSkipComment(file_path)

    assert isinstance(exc, FileSkipComment)
    assert isinstance(exc, FileSkipped)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.file_path == file_path
    assert str(exc) == expected_message
    assert exc.args[0] == expected_message

# Generated at 2026-10-24 07:13:17.141381
# Unit test for constructor of class FileSkipComment
def test_FileSkipComment():exc = FileSkipComment("example.py")

# Generated at 2026-10-24 07:13:18.525042
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    # Arrange
    profile = "no_such_profile"

    # Act
    exc = ProfileDoesNotExist(profile)

    # Assert - type hierarchy
    assert isinstance(exc, ProfileDoesNotExist)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    # Assert - stored attribute preserves input exactly
    assert exc.profile == profile

    # Assert - message passed to base Exception
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert exc.args[0] == expected_message
    assert str(exc) == expected_message

    # Assert - usable with raise / except ISortError
    try:
        raise ProfileDoesNotExist(profile)
    except ISortError as caught:
        assert caught.profile == profile
        assert str(caught) == expected_message
    else:
        assert False, "ProfileDoesNotExist was not raised"

# Generated at 2026-10-24 07:13:20.081281
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist

    profile = "nonexistent_profile"
    error = ProfileDoesNotExist(profile)

    assert error.profile == profile
    assert isinstance(error, Exception)
    assert profile in str(error)
    assert "does not exist" in str(error)
    assert "Available profiles:" in str(error)

# Generated at 2026-10-24 07:13:21.402916
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
    unsupported_settings = {
        "unknown_setting": {"value": "42", "source": "pyproject.toml"},
        "other_setting": {"value": "True", "source": "command line"},
    }

    exc = UnsupportedSettings(unsupported_settings)

    assert isinstance(exc, ISortError)
    assert exc.unsupported_settings == unsupported_settings
    assert str(exc) == (
        "isort was provided settings that it doesn't support:\n\n"
        "\t- unknown_setting = 42  (source: 'pyproject.toml')\n"
        "\t- other_setting = True  (source: 'command line')\n\n"
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n"
    )

# Generated at 2026-10-24 07:13:22.857765
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    # Arrange
    profile = "no_such_profile"

    # Act
    exc = ProfileDoesNotExist(profile)

    # Assert - type hierarchy
    assert isinstance(exc, ProfileDoesNotExist)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)

    # Assert - stored attribute preserves input exactly
    assert exc.profile == profile

    # Assert - message passed to base Exception
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert exc.args[0] == expected_message
    assert str(exc) == expected_message

    # Assert - usable with raise / except ISortError
    try:
        raise ProfileDoesNotExist(profile)
    except ISortError as caught:
        assert caught.profile == profile
        assert str(caught) == expected_message
    else:
        assert False, "ProfileDoesNotExist was not raised"

# Generated at 2026-10-24 07:13:24.171117
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist

    profile = "nonexistent_profile"
    error = ProfileDoesNotExist(profile)

    assert error.profile == profile
    assert isinstance(error, Exception)
    assert profile in str(error)
    assert "does not exist" in str(error)
    assert "Available profiles:" in str(error)

# Generated at 2026-10-24 07:13:25.483675
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 07:13:33.818110
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():kind = str

# Generated at 2026-10-24 07:13:40.879201
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, list)

# Generated at 2026-10-24 07:13:42.205211
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 07:13:49.281603
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exception = LiteralSortTypeMismatch(str, int)

# Generated at 2026-10-24 07:13:51.795927
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:13:54.206547
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:13:56.622447
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:13:59.052031
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:14:01.456685
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:14:04.016143
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:14:06.431474
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:14:08.847454
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:14:11.428071
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-24 07:14:19.701163
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, list)


# Generated at 2026-10-24 07:14:21.013394
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 07:14:27.795016
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(list, tuple)


# Generated at 2026-10-24 07:14:33.923172
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(str, int)

# Generated at 2026-10-24 07:14:35.248444
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():
    from isort.exceptions import LiteralSortTypeMismatch

    kind = dict
    expected_kind = list

    error = LiteralSortTypeMismatch(kind=kind, expected_kind=expected_kind)

    # Attributes set by the constructor
    assert error.kind is kind
    assert error.expected_kind is expected_kind

    # Exception inheritance and message
    assert isinstance(error, ISortError)
    assert "isort was told to sort a literal of type" in str(error)
    assert str(expected_kind) in str(error)
    assert str(kind) in str(error)

# Generated at 2026-10-24 07:14:46.314190
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():exc = LiteralSortTypeMismatch(list, dict)

# Generated at 2026-10-24 07:14:53.174331
# Unit test for constructor of class LiteralSortTypeMismatch
def test_LiteralSortTypeMismatch():error = LiteralSortTypeMismatch(int, list)


# Generated at 2026-10-24 07:14:55.593472
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:14:58.010519
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:00.572312
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:02.986729
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:05.551528
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:07.966937
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:10.380518
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:12.797950
# Unit test for constructor of class LiteralSortTypeMismatch

# Generated at 2026-10-24 07:15:15.215032
# Unit test for constructor of class LiteralSortTypeMismatch