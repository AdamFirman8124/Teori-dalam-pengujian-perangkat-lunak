# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

import pytest
from isort.exceptions import ISortError, ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist_init_sets_attribute_and_message():
    profile_name = "nonexistent_profile_xyz"
    exc = ProfileDoesNotExist(profile_name)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.profile == profile_name
    expected_message = (
        f"Specified profile of {profile_name} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(exc) == expected_message
    assert profile_name in str(exc)
    assert exc.args[0] == expected_message


def test_profile_does_not_exist_can_be_raised_and_caught():
    profile_name = "another_missing_profile"
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        raise ProfileDoesNotExist(profile_name)
    assert exc_info.value.profile == profile_name
    assert f"Specified profile of {profile_name} does not exist." in str(exc_info.value)
    assert f"Available profiles: {','.join(profiles)}." in str(exc_info.value)
