# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f049 import modp


def test_modp_with_positive_exponent():
    assert modp(3, 5) == 3


def test_modp_with_zero_exponent():
    assert modp(0, 5) == 1
