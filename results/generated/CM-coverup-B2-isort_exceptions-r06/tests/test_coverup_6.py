# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

import pytest

from isort.exceptions import ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist_message_and_attributes():
    profile = "nonexistent_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile)

    exception = exc_info.value
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(exception) == expected_message
    assert exception.profile == profile
