# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import f127


def test_negative_length_returns_no():
    assert f127.intersection((1, 2), (3, 4)) == "NO"


def test_zero_length_returns_no():
    assert f127.intersection((1, 2), (2, 3)) == "NO"


def test_length_one_not_prime_returns_no():
    # l = max(0, 1) = 1, r = min(2, 2) = 2, length = 1 -> is_prime(1) is False
    assert f127.intersection((0, 2), (1, 2)) == "NO"


def test_length_two_prime_returns_yes():
    # l = 0, r = 2, length = 2 -> is_prime(2) is True
    assert f127.intersection((0, 2), (0, 2)) == "YES"


def test_length_three_prime_returns_yes():
    # length = 3 -> loop runs once, 3 % 2 != 0, returns True
    assert f127.intersection((0, 3), (0, 3)) == "YES"


def test_length_four_composite_returns_no():
    # length = 4 -> 4 % 2 == 0, returns False
    assert f127.intersection((0, 4), (0, 4)) == "NO"


def test_length_nine_composite_returns_no():
    # length = 9 -> 9 % 2 != 0 (False branch), 9 % 3 == 0 (True branch)
    assert f127.intersection((0, 9), (0, 9)) == "NO"


def test_is_prime_zero_branch_returns_no(monkeypatch):
    class _TrickLength:
        def __gt__(self, other):
            return True

        def __eq__(self, other):
            return other == 0

    class _FakeR:
        def __sub__(self, other):
            return _TrickLength()

    monkeypatch.setitem(f127.__dict__, "max", lambda *args: object())
    monkeypatch.setitem(f127.__dict__, "min", lambda *args: _FakeR())
    # length is _TrickLength(): length > 0 is True, length == 1 is False,
    # length == 0 is True -> is_prime returns False -> "NO"
    assert f127.intersection((0, 1), (0, 1)) == "NO"
