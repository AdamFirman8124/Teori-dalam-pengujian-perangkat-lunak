# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f077 import iscube


def test_iscube_positive_cube():
    assert iscube(27) is True


def test_iscube_positive_non_cube():
    assert iscube(26) is False


def test_iscube_negative_cube():
    # abs() branch: negative input is converted to positive
    assert iscube(-27) is True


def test_iscube_negative_non_cube():
    assert iscube(-26) is False


def test_iscube_zero():
    assert iscube(0) is True


def test_iscube_one():
    assert iscube(1) is True


def test_iscube_large_cube():
    assert iscube(1000) is True


def test_iscube_rounding_branch():
    # 3.999... cubes near a perfect cube exercise the round() branch
    assert iscube(64) is True
    assert iscube(65) is False
