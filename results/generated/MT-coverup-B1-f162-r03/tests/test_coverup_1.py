# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f162 import string_to_md5


def test_string_to_md5_returns_digest_for_nonempty_ascii_text():
    assert string_to_md5("abc") == "900150983cd24fb0d6963f7d28e17f72"


def test_string_to_md5_returns_none_for_empty_text():
    assert string_to_md5("") is None
