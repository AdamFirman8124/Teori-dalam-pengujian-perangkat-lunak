# file: project/f077/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f077 import iscube


def test_iscube_accepts_negative_perfect_cube():
    assert iscube(-8) is True


def test_iscube_rejects_non_cube():
    assert iscube(2) is False
