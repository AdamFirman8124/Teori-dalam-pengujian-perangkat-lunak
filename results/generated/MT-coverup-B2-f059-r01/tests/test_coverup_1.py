# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import f059


def test_largest_prime_factor_normal_paths():
    assert f059.largest_prime_factor(1) == 1
    assert f059.largest_prime_factor(10) == 5
    assert f059.largest_prime_factor(12) == 3


def test_largest_prime_factor_rejects_values_below_two(monkeypatch):
    had_module_range = "range" in f059.__dict__
    original_range = f059.__dict__.get("range")
    calls = []

    def fake_range(*args):
        calls.append(args)
        return [1]

    with monkeypatch.context() as patch:
        patch.setattr(f059, "range", fake_range, raising=False)
        assert f059.largest_prime_factor(5) == 1
        assert calls == [(2, 6)]

    assert ("range" in f059.__dict__) == had_module_range
    if had_module_range:
        assert f059.__dict__["range"] is original_range
