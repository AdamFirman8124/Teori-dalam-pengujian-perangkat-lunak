# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

import pytest

from f039 import prime_fib


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (4, 13),
        (5, 89),
    ],
)
def test_prime_fib(n, expected):
    assert prime_fib(n) == expected
