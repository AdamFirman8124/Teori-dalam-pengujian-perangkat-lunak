# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f122.add_elements covering line 3 and all of its branches.

The function under test (f122/__init__.py):

    def add_elements(arr, k):
        return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

Branches exercised:
  * the `return` line itself (previously uncovered),
  * the generator condition being True  (len(str(elem)) <= 2),
  * the generator condition being False (len(str(elem)) >  2),
  * slicing with k < len(arr), k == 0, k > len(arr), and an empty arr.

add_elements is a pure function (no I/O, no globals, no monkeypatching
required), so no cleanup beyond normal test teardown is needed.
"""

from f122 import add_elements


def test_add_elements_sums_all_short_elements():
    # Every element in arr[:k] has str length <= 2 -> all are summed.
    assert add_elements([1, 22, 3], 3) == 26


def test_add_elements_skips_long_elements():
    # Mix of short and long elements: both outcomes of the
    # `len(str(elem)) <= 2` condition are exercised.
    # 5, 12, -7 kept (str length 1 or 2); 100 and 999 skipped (length 3).
    assert add_elements([5, 100, 12, -7, 999], 5) == 10


def test_add_elements_negative_long_element_is_skipped():
    # A negative number whose string form is longer than 2 chars
    # ("-100") must also be filtered out.
    assert add_elements([-100, 5], 2) == 5


def test_add_elements_limits_to_first_k_elements():
    # Elements beyond index k are ignored even though they would qualify.
    assert add_elements([1, 2, 3, 4, 5], 2) == 3


def test_add_elements_k_zero_returns_zero():
    # k == 0 -> empty slice -> sum of empty generator is 0.
    assert add_elements([1, 2, 3], 0) == 0


def test_add_elements_empty_array_returns_zero():
    # Empty input array -> 0 regardless of k.
    assert add_elements([], 3) == 0


def test_add_elements_k_larger_than_array_length():
    # k beyond the array length is safe: the slice simply clamps.
    # str(-8) == "-8" has length 2, so it is included.
    assert add_elements([9, -8], 10) == 1


def test_add_elements_no_qualifying_elements_returns_zero():
    # All elements are too "long" -> the generator yields nothing -> 0.
    assert add_elements([100, 200, -300], 3) == 0
