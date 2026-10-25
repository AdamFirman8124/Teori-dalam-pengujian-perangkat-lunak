# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f077 import iscube


def test_iscube_perfect_cubes():
    assert iscube(0) is True
    assert iscube(1) is True
    assert iscube(8) is True
    assert iscube(27) is True
    assert iscube(64) is True
    assert iscube(125) is True
    assert iscube(1000) is True


def test_iscube_negative_cubes():
    assert iscube(-1) is True
    assert iscube(-8) is True
    assert iscube(-27) is True
    assert iscube(-64) is True


def test_iscube_non_cubes():
    assert iscube(2) is False
    assert iscube(3) is False
    assert iscube(4) is False
    assert iscube(7) is False
    assert iscube(9) is False
    assert iscube(10) is False
    assert iscube(26) is False
    assert iscube(28) is False
    assert iscube(100) is False
    assert iscube(-2) is False
    assert iscube(-9) is False
