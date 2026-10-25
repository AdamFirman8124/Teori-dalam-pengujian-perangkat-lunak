# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

from f093 import encode


def test_encode_swaps_case_and_replaces_vowels():
    assert encode("Hello World!") == "hGLLQ wQRLD!"


def test_encode_handles_empty_message():
    assert encode("") == ""
