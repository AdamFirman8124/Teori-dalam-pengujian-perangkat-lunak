# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

import pytest

from isort.exceptions import ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist_message_and_attributes():
    profile = "nonexistent_profile_xyz_123"
    assert profile not in profiles

    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile)

    exc = exc_info.value
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(exc) == expected_message
    assert exc.profile == profile
