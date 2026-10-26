# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_basic():
    assert flip_case("Hello World") == "hELLO wORLD"


def test_flip_case_empty():
    assert flip_case("") == ""


def test_flip_case_mixed():
    assert flip_case("PyThOn 123!") == "pYtHoN 123!"
