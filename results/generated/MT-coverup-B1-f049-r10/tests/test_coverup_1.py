# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f049 import modp


def test_modp_returns_initial_value_when_n_is_zero():
    assert modp(0, 7) == 1


def test_modp_repeatedly_doubles_modulo_p():
    assert modp(3, 5) == 3
