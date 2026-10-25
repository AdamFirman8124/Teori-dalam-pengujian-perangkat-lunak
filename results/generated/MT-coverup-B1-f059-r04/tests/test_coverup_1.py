# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import f059


def test_largest_prime_factor_covers_prime_composite_and_nonfactor_paths():
    assert f059.largest_prime_factor(1) == 1
    assert f059.largest_prime_factor(12) == 3
    assert f059.largest_prime_factor(35) == 7
    assert f059.largest_prime_factor(13) == 13


def test_largest_prime_factor_handles_candidate_below_two(monkeypatch):
    calls = []

    def fake_range(start, stop):
        calls.append((start, stop))
        return (1,)

    monkeypatch.setattr(f059, "range", fake_range, raising=False)

    assert f059.largest_prime_factor(1) == 1
    assert calls == [(2, 2)]
