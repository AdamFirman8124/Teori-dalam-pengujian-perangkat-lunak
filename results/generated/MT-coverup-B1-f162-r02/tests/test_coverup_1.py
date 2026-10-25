# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f162 import string_to_md5


def test_string_to_md5_returns_md5_digest_for_nonempty_ascii_text():
    result = string_to_md5("hello")

    assert result == "5d41402abc4b2a76b9719d911017c592"


def test_string_to_md5_returns_none_for_empty_text():
    result = string_to_md5("")

    assert result is None
