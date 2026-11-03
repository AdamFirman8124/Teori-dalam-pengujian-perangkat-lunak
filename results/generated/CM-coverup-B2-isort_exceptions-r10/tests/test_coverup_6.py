# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

import pytest

from isort.exceptions import ISortError, ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist_message_and_attributes():
    profile = "definitely_not_a_real_profile"
    exc = ProfileDoesNotExist(profile)

    # Verify the exception is properly initialized (lines 78-82)
    assert isinstance(exc, ISortError)
    assert exc.profile == profile

    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(exc) == expected_message


def test_profile_does_not_exist_raised():
    profile = "another_fake_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile)

    assert exc_info.value.profile == profile
    assert profile in str(exc_info.value)
    assert ",".join(profiles) in str(exc_info.value)
