# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_covers_all_lines():
    # n == 0: covers lines 3, 4 (loop never taken), and 6; 2**0 mod p == 1
    assert modp(0, 5) == 1

    # n > 0: covers lines 3, 4, 5 (loop body) and 6; 2**3 % 5 == 8 % 5 == 3
    assert modp(3, 5) == 3

    # Another n > 0 case: 2**10 == 1024, 1024 % 11 == 1
    assert modp(10, 11) == 1

    # n > 0 where result wraps multiple times: 2**5 == 32, 32 % 3 == 2
    assert modp(5, 3) == 2

    # Negative n: range(n) is empty, loop body skipped, returns 1
    assert modp(-2, 7) == 1
