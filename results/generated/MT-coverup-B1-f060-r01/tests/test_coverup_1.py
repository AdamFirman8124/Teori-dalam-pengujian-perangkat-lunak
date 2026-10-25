# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f060 import sum_to_n


def test_sum_to_n() -> None:
    assert sum_to_n(5) == 15
