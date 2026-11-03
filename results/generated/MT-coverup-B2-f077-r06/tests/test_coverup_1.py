# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f077 import iscube


def test_iscube_positive_cube():
    """A positive perfect cube should be recognized as a cube."""
    assert iscube(8) is True
    assert iscube(27) is True
    assert iscube(64) is True


def test_iscube_negative_cube():
    """A negative perfect cube is a cube because of the abs() on line 3."""
    assert iscube(-8) is True
    assert iscube(-27) is True


def test_iscube_non_cube():
    """A positive non-cube should not be recognized as a cube."""
    assert iscube(9) is False
    assert iscube(2) is False


def test_iscube_negative_non_cube():
    """A negative non-cube should not be recognized as a cube."""
    assert iscube(-9) is False
    assert iscube(-2) is False


def test_iscube_zero_and_one():
    """Edge cases: 0 and 1 are perfect cubes."""
    assert iscube(0) is True
    assert iscube(1) is True
    assert iscube(-1) is True
