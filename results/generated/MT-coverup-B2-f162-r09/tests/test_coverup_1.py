# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from hashlib import md5

from f162 import string_to_md5


def test_string_to_md5_returns_digest_for_nonempty_ascii_text():
    text = "hello"

    result = string_to_md5(text)

    assert result == md5(text.encode("ascii")).hexdigest()


def test_string_to_md5_returns_none_for_empty_text():
    assert string_to_md5("") is None
