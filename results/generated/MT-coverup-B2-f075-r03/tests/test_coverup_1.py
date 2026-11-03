# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

"""Coverage tests for f075.is_multiply_prime.

``is_multiply_prime(a)`` returns True iff ``a`` equals ``i * j * k`` for
some primes ``i, j, k``, each taken from ``range(2, 101)`` (repetition
allowed, e.g. 8 == 2*2*2).

The function under test is pure (it mutates no module state and performs
no I/O), so no monkeypatching/cleanup is required to avoid state
pollution; each test leaves the environment exactly as it found it.
"""

import pytest

from f075 import is_multiply_prime


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        # 8 == 2*2*2: matches on the very first triple (i=2, j=2, k=2),
        # executing the nested loop headers, is_prime's empty-loop
        # ``return True`` (line 7) and the ``return True`` of line 18.
        (8, True),
        # 30 == 2*3*5: k values 2, 3 fail the equality test (False branch
        # of line 18) and k == 4 makes is_prime return False through
        # lines 5-6, exercising the ``if not is_prime(k): continue``
        # branch of line 17 before the match on k == 5.
        (30, True),
        # 125 == 5*5*5: no match exists for i == 2 or i == 3, so the
        # outermost loop must step over composite i == 4 (line 13
        # ``continue``) and, while i == 5, over composite j == 4 (line 15
        # ``continue``) before finding 5*5*5.
        (125, True),
    ],
)
def test_multiply_prime_true(a, expected):
    assert is_multiply_prime(a) is expected


@pytest.mark.parametrize("a", [1, 2])
def test_multiply_prime_false(a):
    # No triple of primes >= 2 can multiply to ``a`` (the smallest
    # product is 2*2*2 == 8), so every loop runs to exhaustion: composite
    # i/j/k values exercise all three ``continue`` branches, the innermost
    # equality test always takes its False branch, and control finally
    # reaches the trailing ``return False`` (line 19).
    assert is_multiply_prime(a) is False
