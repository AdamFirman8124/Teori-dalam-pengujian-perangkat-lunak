# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f027 import flip_case


def test_flip_case_swaps_letter_case():
    assert flip_case("Hello, WORLD! 123") == "hELLO, world! 123"
