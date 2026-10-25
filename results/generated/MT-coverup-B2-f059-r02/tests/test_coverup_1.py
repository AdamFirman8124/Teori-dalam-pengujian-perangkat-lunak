# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import f059


def test_largest_prime_factor_covers_prime_and_composite_candidates():
    assert f059.largest_prime_factor(45) == 5


def test_largest_prime_factor_handles_no_candidates():
    assert f059.largest_prime_factor(1) == 1


def test_largest_prime_factor_rejects_candidate_below_two(monkeypatch):
    calls = []

    def fake_range(*args):
        calls.append(args)
        return (1,)

    monkeypatch.setattr(f059, "range", fake_range, raising=False)

    assert f059.largest_prime_factor(1) == 1
    assert calls == [(2, 2)]
