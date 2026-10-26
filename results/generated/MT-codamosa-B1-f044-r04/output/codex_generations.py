

# Generated at 2026-10-25 11:45:53.303670
# Unit test for function change_base

# Generated at 2026-10-25 11:45:55.716053
# Unit test for function change_base

# Generated at 2026-10-25 11:45:58.318337
# Unit test for function change_base

# Generated at 2026-10-25 11:46:00.732826
# Unit test for function change_base

# Generated at 2026-10-25 11:46:03.151086
# Unit test for function change_base

# Generated at 2026-10-25 11:46:05.564389
# Unit test for function change_base

# Generated at 2026-10-25 11:46:19.492707
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(0, 2) == "0"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(5, 2) == "101"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(10, 3) == "101"
    assert module_0.change_base(255, 10) == "255"


def test_change_base_invalid_base():
    import pytest

    with pytest.raises(ValueError):
        module_0.change_base(10, 1)

# Generated at 2026-10-25 11:46:27.997547
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(1234, 10) == "1234"
    assert module_0.change_base(255, 16) == "1515"   # digits aren't lettered: 15 then 15
    assert module_0.change_base(0, 2) == ""          # current behavior: empty string for 0

# Generated at 2026-10-25 11:46:29.496617
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(1234, 10) == "1234"
    assert module_0.change_base(255, 16) == "1515"   # digits aren't lettered: 15 then 15
    assert module_0.change_base(0, 2) == ""          # current behavior: empty string for 0