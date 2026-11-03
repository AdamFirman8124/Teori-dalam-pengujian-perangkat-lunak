

# Generated at 2026-11-01 23:21:13.540517
# Unit test for constructor of class LiteralParsingFailure
def test_LiteralParsingFailure():
    from isort.exceptions import ISortError, LiteralParsingFailure

    code = "{'key': 'value'"
    original_error = SyntaxError("unexpected EOF while parsing")

    exception = LiteralParsingFailure(code=code, original_error=original_error)

    # Attributes should be stored on the exception instance
    assert exception.code == code
    assert exception.original_error is original_error

    # The exception message should mention both the code and the original error
    message = str(exception)
    assert code in message
    assert str(original_error) in message
    assert "isort failed to parse the given literal" in message
    assert "ast.literal_eval" in message

    # Should be an instance of the base isort exception and Exception
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

# Generated at 2026-11-01 23:21:47.947011
# Unit test for constructor of class FileSkipped
def test_FileSkipped():
    message = "This file was skipped for testing purposes"
    file_path = "path/to/skipped_file.py"

    exception = FileSkipped(message, file_path)

    # Constructor should set the file_path attribute
    assert exception.file_path == file_path

    # Constructor should pass the message to the base Exception
    assert str(exception) == message

    # FileSkipped should inherit from ISortError (and Exception)
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)


def test_FileSkipped_can_be_raised_and_caught():
    message = "Skipped due to test"
    file_path = "another_file.py"

    with pytest.raises(FileSkipped) as exc_info:
        raise FileSkipped(message, file_path)

    assert exc_info.value.file_path == file_path
    assert str(exc_info.value) == message

# Generated at 2026-11-01 23:22:15.090881
# Unit test for constructor of class UnsupportedSettings
def test_UnsupportedSettings():
# nonce:2c2092d4
    from isort.exceptions import ISortError, UnsupportedSettings

    unsupported_settings = {
        "profile": {"value": "nonexistent_profile", "source": "/mock/path/pyproject.toml"},
        "known_first_party": {"value": "10", "source": "cli"},
    }
    exception = UnsupportedSettings(unsupported_settings)

    # It should be an instance of both UnsupportedSettings and the base ISortError
    assert isinstance(exception, UnsupportedSettings)
    assert isinstance(exception, ISortError)

    # The unsupported settings should be stored on the exception instance
    assert exception.unsupported_settings == unsupported_settings

    # The formatted message should include each unsupported option with its value and source
    message = str(exception)
    assert message.startswith("isort was provided settings that it doesn't support:\n\n")
    assert "\t- profile = nonexistent_profile  (source: '/mock/path/pyproject.toml')" in message
    assert "\t- known_first_party = 10  (source: 'cli')" in message
    assert (
        "For a complete and up-to-date listing of supported settings see: "
        "https://pycqa.github.io/isort/docs/configuration/options/.\n" in message
    )

# Generated at 2026-11-01 23:22:20.916594
# Unit test for constructor of class AssignmentsFormatMismatch
def test_AssignmentsFormatMismatch():
    code = "from isort import Config\n" "import os\n"
    assignments_format_mismatch = AssignmentsFormatMismatch(code=code)
    assert assignments_format_mismatch.code == code
    assert isinstance(assignments_format_mismatch, ISortError)
    assert "isort was told to sort a section of assignments" in str(assignments_format_mismatch)
    assert code in str(assignments_format_mismatch)

# Generated at 2026-11-01 23:22:30.039854
# Unit test for constructor of class UnsupportedEncoding
def test_UnsupportedEncoding():
    from pathlib import Path
    from isort.exceptions import UnsupportedEncoding

    # Test construction with a string filename
    filename_str = "example.py"
    exc = UnsupportedEncoding(filename_str)
    assert exc.filename == filename_str
    assert str(exc) == f"Unknown or unsupported encoding in {filename_str}"

    # Test construction with a Path filename
    filename_path = Path("example.py")
    exc = UnsupportedEncoding(filename_path)
    assert exc.filename == filename_path
    assert str(exc) == f"Unknown or unsupported encoding in {filename_path}"
# nonce:f367099a

# Generated at 2026-11-01 23:22:40.886348
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist, ISortError
    from isort.profiles import profiles

    profile = "nonexistent_profile"
    exception = ProfileDoesNotExist(profile)

    # Should be an instance of the base isort exception and Exception
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # The profile attribute should be stored exactly as passed in
    assert exception.profile == profile

    # The error message should mention the profile and that it doesn't exist
    assert profile in str(exception)
    assert "does not exist" in str(exception)

    # The error message should list all available profiles, comma separated
    assert ",".join(profiles) in str(exception)

# Generated at 2026-11-01 23:22:57.373218
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent_profile"
    exception = ProfileDoesNotExist(profile)

    # The profile attribute should be stored exactly as passed in
    assert exception.profile == profile

    # Should inherit from ISortError and Exception
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # The error message should mention the profile and list available profiles
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(exception) == expected_message
    assert profile in str(exception)
    assert ",".join(profiles) in str(exception)

# Generated at 2026-11-01 23:23:08.329615
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():from isort.exceptions import ProfileDoesNotExist, ISortError

# Generated at 2026-11-01 23:23:24.699553
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist
    from isort.profiles import profiles

    profile = "nonexistent_profile"

    error = ProfileDoesNotExist(profile)

    assert error.profile == profile
    assert str(error) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(sorted(profiles))}."
    ) if False else str(error) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert isinstance(error, Exception)

# Generated at 2026-11-01 23:23:50.007382
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():from isort.exceptions import ISortError, ProfileDoesNotExist


# Generated at 2026-11-01 23:24:00.924184
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent_profile"
    error = ProfileDoesNotExist(profile)

    # Verify the profile attribute is set correctly
    assert error.profile == profile

    # Verify the exception message contains expected content
    assert "Specified profile of nonexistent_profile does not exist." in str(error)
    assert "Available profiles:" in str(error)

    # Verify it is an instance of ISortError
    assert isinstance(error, Exception)

    # Ensure valid known profiles do not trigger the error
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist("black")

    assert exc_info.value.profile == "black"

# Generated at 2026-11-01 23:24:25.342735
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ISortError, ProfileDoesNotExist
    from isort.profiles import profiles

    profile = "nonexistent_profile"
    error = ProfileDoesNotExist(profile)

    # The exception should store the profile name
    assert error.profile == profile

    # It should derive from the base isort exception
    assert isinstance(error, ISortError)

    # The generated message should include the profile and available profiles
    assert str(error) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )

# Generated at 2026-11-01 23:24:47.146722
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():from isort.exceptions import ISortError, ProfileDoesNotExist

# Generated at 2026-11-01 23:24:57.960571
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist
    from isort.profiles import profiles

    profile = "nonexistent_profile"
    error = ProfileDoesNotExist(profile)

    assert error.profile == profile
    assert isinstance(error, Exception)
    assert profile in str(error)
    assert ",".join(profiles) in str(error)

    # Verify available profiles are listed in the error message
    for available_profile in profiles:
        assert available_profile in str(error)

# Generated at 2026-11-01 23:25:01.443081
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist
    from isort.profiles import profiles

    # Test that the exception is constructed with the given profile
    profile = "nonexistent_profile"
    exception = ProfileDoesNotExist(profile)

    # Verify the profile attribute is set correctly
    assert exception.profile == profile

    # Verify the error message contains the profile name
    assert profile in str(exception)

    # Verify the error message lists the available profiles
    assert "Available profiles:" in str(exception)
    assert ",".join(profiles) in str(exception)

    # Verify inheritance from the base isort exception
    from isort.exceptions import ISortError
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

# Generated at 2026-11-01 23:25:20.182249
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    # Test instantiation with a non-existent profile name
    profile = "nonexistent_profile"
    exception = ProfileDoesNotExist(profile)

    # Verify the profile attribute is stored correctly
    assert exception.profile == profile

    # Verify it is an instance of the base isort exception
    assert isinstance(exception, ISortError)

    # Verify the exception message includes the profile name and available profiles
    assert str(exception) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )

# Generated at 2026-11-01 23:25:29.540636
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist, ISortError
    from isort.profiles import profiles

    error = ProfileDoesNotExist("does_not_exist")

    assert error.profile == "does_not_exist"
    assert isinstance(error, ISortError)
    assert str(error) == (
        "Specified profile of does_not_exist does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )

# Generated at 2026-11-01 23:25:45.208470
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():from isort.exceptions import ProfileDoesNotExist

# Generated at 2026-11-01 23:26:00.056619
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    profile = "nonexistent_profile"
    exception = ProfileDoesNotExist(profile)

    # Should be an instance of both ProfileDoesNotExist and the base ISortError
    assert isinstance(exception, ProfileDoesNotExist)
    assert isinstance(exception, ISortError)

    # The profile attribute should be set to the provided profile
    assert exception.profile == profile

    # The error message should mention the missing profile and available profiles
    assert f"Specified profile of {profile} does not exist." in str(exception)
    assert "Available profiles:" in str(exception)

# Generated at 2026-11-01 23:26:24.427891
# Unit test for constructor of class ProfileDoesNotExist
def test_ProfileDoesNotExist():
    from isort.exceptions import ProfileDoesNotExist, ISortError

    # Constructor should store the profile name as an attribute
    profile = "non_existent_profile"
    error = ProfileDoesNotExist(profile)

    assert error.profile == profile

    # Should be an instance of the base isort exception and Exception
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # Error message should mention the missing profile and available profiles
    message = str(error)
    assert profile in message
    assert "does not exist" in message
    assert "Available profiles:" in message