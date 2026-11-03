# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

"""Tests for f077.iscube — covering lines 3-4 (the function body).

iscube is a pure function (no globals, I/O, or mutable state), so no
monkeypatching or teardown is required; each test leaves no state behind.
"""

from f077 import iscube


def test_iscube_positive_perfect_cubes():
    """Perfect cubes (including 0) must be recognized as cubes."""
    assert iscube(0) is True
    assert iscube(1) is True
    assert iscube(8) is True
    assert iscube(27) is True
    assert iscube(64) is True


def test_iscube_negative_perfect_cubes():
    """abs() is applied first, so negative perfect cubes are recognized."""
    assert iscube(-1) is True
    assert iscube(-8) is True
    assert iscube(-27) is True


def test_iscube_non_cubes():
    """Non-cubes (positive and negative) must not be recognized as cubes."""
    assert iscube(2) is False
    assert iscube(9) is False
    assert iscube(26) is False
    assert iscube(-2) is False
    assert iscube(-9) is False
