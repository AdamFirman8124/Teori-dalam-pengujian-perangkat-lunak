# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f013 import greatest_common_divisor


def test_greatest_common_divisor_executes_euclidean_loop():
    assert greatest_common_divisor(48, 18) == 6


def test_greatest_common_divisor_handles_zero_without_loop():
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(0, 7) == 7
