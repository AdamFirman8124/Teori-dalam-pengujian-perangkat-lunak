# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


@pytest.mark.parametrize(
    ("interval1", "interval2", "expected"),
    [
        ((0, 1), (0, 1), "NO"),   # length 1
        ((0, 2), (0, 2), "YES"),  # length 2
        ((0, 3), (0, 3), "YES"),  # prime greater than 2
        ((0, 4), (0, 4), "NO"),   # composite
        ((0, 1), (1, 2), "NO"),   # zero length
        ((0, 1), (2, 3), "NO"),   # negative length
    ],
)
def test_intersection(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected


def test_intersection_exercises_zero_prime_guard(monkeypatch):
    class ZeroLength:
        def __sub__(self, other):
            return self

        def __gt__(self, other):
            return True

        def __eq__(self, other):
            return other == 0

    namespace = intersection.__globals__
    previous_max = namespace.get("max")
    previous_min = namespace.get("min")
    had_max = "max" in namespace
    had_min = "min" in namespace

    with monkeypatch.context() as patch:
        patch.setitem(namespace, "max", lambda *args: 0)
        patch.setitem(namespace, "min", lambda *args: ZeroLength())
        assert intersection((0, 1), (0, 1)) == "NO"

    assert ("max" in namespace) is had_max
    assert ("min" in namespace) is had_min
    if had_max:
        assert namespace["max"] is previous_max
    if had_min:
        assert namespace["min"] is previous_min
