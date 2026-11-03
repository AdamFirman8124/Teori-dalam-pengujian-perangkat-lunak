# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

import pytest

from f163 import generate_integers


def test_generate_integers_basic_increasing():
    # a < b, both within [2, 8]: exercises min/max with a < b and the even filter
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_generate_integers_reversed_args():
    # a > b: exercises min(a, b) and max(a, b) picking the other argument
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_generate_integers_lower_clamped():
    # min(a, b) < 2 so lower is clamped up to 2; odd values are filtered out
    assert generate_integers(1, 5) == [2, 4]


def test_generate_integers_upper_clamped():
    # max(a, b) > 8 so upper is clamped down to 8
    assert generate_integers(3, 9) == [4, 6, 8]


def test_generate_integers_both_clamped():
    # both bounds clamped simultaneously, with reversed argument order
    assert generate_integers(20, 0) == [2, 4, 6, 8]


def test_generate_integers_odd_bounds_only():
    # both bounds odd: filter must skip lower and upper odd endpoints
    assert generate_integers(3, 7) == [4, 6]


def test_generate_integers_empty_when_lower_exceeds_upper():
    # lower (10) > upper (8): range is empty, list comprehension yields []
    assert generate_integers(10, 20) == []


def test_generate_integers_negative_inputs():
    # negative values: lower clamped to 2, upper below lower -> empty result
    assert generate_integers(-5, -1) == []


def test_generate_integers_single_even_value():
    # a == b == even value inside range: exactly one element
    assert generate_integers(4, 4) == [4]


def test_generate_integers_single_odd_value():
    # a == b == odd value inside range: filter removes it -> empty list
    assert generate_integers(5, 5) == []


def test_generate_integers_result_is_new_list():
    # postcondition: a fresh list is returned each call (no shared state)
    first = generate_integers(2, 8)
    second = generate_integers(2, 8)
    assert first == second == [2, 4, 6, 8]
    assert first is not second
