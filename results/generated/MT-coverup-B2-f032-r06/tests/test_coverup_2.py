# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f032 import poly


def test_poly_evaluates_all_coefficients():
    assert poly([1, 2, 3], 2.0) == pytest.approx(17.0)


def test_poly_with_empty_coefficients():
    assert poly([], 2.0) == 0
