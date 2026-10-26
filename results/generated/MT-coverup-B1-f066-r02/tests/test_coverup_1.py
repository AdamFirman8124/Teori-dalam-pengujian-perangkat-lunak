# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

from f066 import digitSum


def test_digitSum_empty_string():
    assert digitSum("") == 0


def test_digitSum_all_uppercase():
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C")


def test_digitSum_mixed_case():
    assert digitSum("aBcD") == ord("B") + ord("D")


def test_digitSum_no_uppercase():
    assert digitSum("abc123! ") == 0
