# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

from f130 import tri


def test_tri_zero_returns_base_case():
    assert tri(0) == [1]


def test_tri_exercises_even_and_odd_iterations():
    assert tri(3) == [1, 3, 2.0, 8.0]
