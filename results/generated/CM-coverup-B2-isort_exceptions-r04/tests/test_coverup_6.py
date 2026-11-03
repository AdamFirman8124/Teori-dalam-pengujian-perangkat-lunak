# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

import pytest

from isort.exceptions import ISortError, ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist_message_and_attribute():
    """Test that ProfileDoesNotExist builds its message and stores the profile.

    This covers the previously unexecuted lines 78-82 of isort/exceptions.py:
    the super().__init__ call building the message and the self.profile
    assignment.
    """
    profile = "definitely_not_a_real_profile"

    # Instantiating the exception directly executes the __init__ body.
    exception = ProfileDoesNotExist(profile)

    # The exception should be an isort error (and thus an Exception).
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)

    # The stored profile attribute must match what was passed in.
    assert exception.profile == profile

    # The message must contain the profile name and the available profiles.
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(exception) == expected_message
    assert profile in str(exception)
    for available_profile in profiles:
        assert available_profile in str(exception)


def test_profile_does_not_exist_raises_when_raised():
    """Test that the exception can be raised and caught with correct payload."""
    profile = "another_missing_profile"

    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile)

    assert exc_info.value.profile == profile
    assert str(exc_info.value) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
