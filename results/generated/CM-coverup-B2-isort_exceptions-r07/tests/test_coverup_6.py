# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

import pytest

from isort.exceptions import ISortError, ProfileDoesNotExist


def test_profile_does_not_exist_sets_attributes_and_message(monkeypatch):
    """Constructing ProfileDoesNotExist must execute __init__ fully: it should
    build the error message from the available profiles and store .profile."""
    # Patch the profiles mapping imported into isort.exceptions so the expected
    # message is deterministic. monkeypatch restores the original afterwards.
    monkeypatch.setattr(
        "isort.exceptions.profiles",
        {"black": True, "django": True, "pycharm": True},
    )

    exception = ProfileDoesNotExist("nonexistent")

    # Postconditions: profile attribute set and exact message built.
    assert exception.profile == "nonexistent"
    assert str(exception) == (
        "Specified profile of nonexistent does not exist. "
        "Available profiles: black,django,pycharm."
    )
    assert isinstance(exception, ISortError)
    assert isinstance(exception, Exception)


def test_profile_does_not_exist_with_real_profiles():
    """Exercise the same code path against the real, unpatched profiles mapping."""
    from isort.profiles import profiles as real_profiles

    exception = ProfileDoesNotExist("my_custom_profile")

    # Postconditions: attribute matches and message lists real profile names.
    assert exception.profile == "my_custom_profile"
    assert str(exception) == (
        f"Specified profile of my_custom_profile does not exist. "
        f"Available profiles: {','.join(real_profiles)}."
    )
    assert "my_custom_profile" in str(exception)
