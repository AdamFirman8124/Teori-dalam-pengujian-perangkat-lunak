# file: script_77.py:1-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
from script_77 import iscube


def test_iscube_positive_cubes():
    assert iscube(1) == True
    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(64) == True
    assert iscube(125) == True
    assert iscube(1000) == True


def test_iscube_zero():
    assert iscube(0) == True


def test_iscube_negative_cubes():
    assert iscube(-1) == True
    assert iscube(-8) == True
    assert iscube(-27) == True
    assert iscube(-64) == True
    assert iscube(-125) == True


def test_iscube_positive_non_cubes():
    assert iscube(2) == False
    assert iscube(3) == False
    assert iscube(7) == False
    assert iscube(9) == False
    assert iscube(26) == False
    assert iscube(63) == False
    assert iscube(65) == False
    assert iscube(180) == False


def test_iscube_negative_non_cubes():
    assert iscube(-2) == False
    assert iscube(-3) == False
    assert iscube(-7) == False
    assert iscube(-26) == False
    assert iscube(-180) == False
