# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f044 import change_base


def test_change_base_binary():
    assert change_base(8, 2) == "1000"


def test_change_base_decimal():
    assert change_base(255, 10) == "255"


def test_change_base_hex_like():
    assert change_base(15, 16) == "15"


def test_change_base_single_digit():
    assert change_base(5, 10) == "5"
