# file: project/isort/exceptions.py:74-82
# asked: {"lines": [78, 79, 80, 82], "branches": []}
# gained: {"lines": [78, 79, 80, 82], "branches": []}

from isort.exceptions import ISortError, ProfileDoesNotExist


def test_profile_does_not_exist_message_and_attribute():
    from isort.profiles import profiles

    bad_profile = "no_such_profile_xyz"
    err = ProfileDoesNotExist(bad_profile)
    assert isinstance(err, ISortError)
    assert isinstance(err, Exception)
    assert err.profile == bad_profile
    expected_message = (
        f"Specified profile of {bad_profile} does not exist. "
        f"Available profiles: {','.join(profiles)}."
    )
    assert str(err) == expected_message
    assert bad_profile in str(err)
    assert ",".join(profiles) in str(err)
    assert err.args[0] == expected_message


def test_profile_does_not_exist_raised_and_caught():
    bad_profile = "missing_profile_123"
    try:
        raise ProfileDoesNotExist(bad_profile)
    except ISortError as exc:
        assert isinstance(exc, ProfileDoesNotExist)
        assert exc.profile == bad_profile
        assert f"Specified profile of {bad_profile} does not exist." in str(exc)
    else:
        raise AssertionError("ProfileDoesNotExist was not raised")


def test_profile_does_not_exist_uses_patched_profiles(monkeypatch):
    import isort.exceptions as exceptions_module

    monkeypatch.setattr(exceptions_module, "profiles", {"aaa": {}, "bbb": {}})
    bad_profile = "unknown"
    err = exceptions_module.ProfileDoesNotExist(bad_profile)
    assert err.profile == bad_profile
    assert str(err) == "Specified profile of unknown does not exist. Available profiles: aaa,bbb."
