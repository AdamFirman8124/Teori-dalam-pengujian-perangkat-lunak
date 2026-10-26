# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

from isort.exceptions import ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist() -> None:
    profile = "nonexistent-profile"
    expected_message = (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )

    error = ProfileDoesNotExist(profile)

    assert error.profile == profile
    assert str(error) == expected_message
    assert error.args == (expected_message,)
