# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f077 import iscube


def test_iscube_positive_cube():
    """A positive perfect cube returns True (executes lines 3-4, True branch)."""
    assert iscube(27) is True
    assert iscube(1) is True
    assert iscube(0) is True


def test_iscube_negative_cube():
    """A negative perfect cube returns True via abs() on line 3."""
    assert iscube(-8) is True
    assert iscube(-27) is True


def test_iscube_not_a_cube():
    """A non-cube returns False (executes lines 3-4, False branch)."""
    assert iscube(2) is False
    assert iscube(26) is False
    assert iscube(-2) is False
