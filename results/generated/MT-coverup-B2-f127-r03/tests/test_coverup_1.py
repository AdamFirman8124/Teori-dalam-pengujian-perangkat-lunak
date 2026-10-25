# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

import f127


@pytest.mark.parametrize(
    ("interval1", "interval2", "expected"),
    [
        ((0, 0), (0, 0), "NO"),
        ((0, 1), (0, 1), "NO"),
        ((0, 2), (0, 2), "YES"),
        ((0, 3), (0, 3), "YES"),
        ((0, 4), (0, 4), "NO"),
    ],
)
def test_intersection_prime_length_branches(interval1, interval2, expected):
    assert f127.intersection(interval1, interval2) == expected


def test_intersection_zero_like_positive_length(monkeypatch):
    class ZeroLike:
        def __gt__(self, other):
            return other == 0

        def __eq__(self, other):
            return other == 0

    class RightEndpoint:
        def __sub__(self, other):
            assert other == 0
            return ZeroLike()

    monkeypatch.setattr(f127, "max", lambda *_: 0, raising=False)
    monkeypatch.setattr(f127, "min", lambda *_: RightEndpoint(), raising=False)

    assert f127.intersection((0, 1), (0, 1)) == "NO"
