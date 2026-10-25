# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import hashlib

import pytest

from f162 import string_to_md5


def test_string_to_md5_returns_hexdigest_for_non_empty_text():
    result = string_to_md5("hello world")
    assert result == hashlib.md5(b"hello world").hexdigest()
    assert result == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert isinstance(result, str)
    assert len(result) == 32


def test_string_to_md5_returns_none_for_empty_text():
    assert string_to_md5("") is None


def test_string_to_md5_uses_ascii_encoding(monkeypatch):
    calls = []
    real_md5 = hashlib.md5

    def spy_md5(data=b"", *args, **kwargs):
        calls.append(data)
        return real_md5(data, *args, **kwargs)

    monkeypatch.setattr(hashlib, "md5", spy_md5)

    result = string_to_md5("abc")

    assert calls == [b"abc"]
    assert result == real_md5(b"abc").hexdigest()


def test_string_to_md5_rejects_non_ascii_text():
    with pytest.raises(UnicodeEncodeError):
        string_to_md5("héllo")
