# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

from isort.exceptions import ISortError, ProfileDoesNotExist
from isort.profiles import profiles


def test_profile_does_not_exist_initialization() -> None:
    profile = "__missing_profile__"

    error = ProfileDoesNotExist(profile)

    assert isinstance(error, ISortError)
    assert error.profile == profile
    assert str(error) == (
        f"Specified profile of {profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert error.args == (str(error),)
