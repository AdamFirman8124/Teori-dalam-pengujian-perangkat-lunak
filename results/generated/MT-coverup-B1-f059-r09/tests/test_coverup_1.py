# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import f059


def test_largest_prime_factor_common_paths():
    assert f059.largest_prime_factor(1) == 1
    assert f059.largest_prime_factor(2) == 2
    assert f059.largest_prime_factor(10) == 5
    assert f059.largest_prime_factor(12) == 3


def test_largest_prime_factor_checks_value_below_two(monkeypatch):
    calls = []

    def fake_range(*args):
        calls.append(args)
        assert args == (2, 2)
        return (1,)

    monkeypatch.setattr(f059, "range", fake_range, raising=False)

    assert f059.largest_prime_factor(1) == 1
    assert calls == [(2, 2)]
