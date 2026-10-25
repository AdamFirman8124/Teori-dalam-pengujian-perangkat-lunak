# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import f059
import pytest


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 1),  # Outer loop is empty.
        (2, 2),  # Prime with an empty inner loop.
        (4, 2),  # Composite divisor.
        (5, 5),  # Inner divisibility check is false.
    ],
)
def test_largest_prime_factor(n, expected):
    assert f059.largest_prime_factor(n) == expected


def test_largest_prime_factor_rejects_values_below_two(monkeypatch):
    calls = []

    def fake_range(*args):
        calls.append(args)
        assert args == (2, 2)
        return iter((1,))

    monkeypatch.setattr(f059, "range", fake_range, raising=False)

    assert f059.largest_prime_factor(1) == 1
    assert calls == [(2, 2)]
