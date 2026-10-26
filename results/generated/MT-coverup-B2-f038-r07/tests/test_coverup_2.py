# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import f038


def test_decode_cyclic_returns_double_encoded():
    assert f038.decode_cyclic("abc") == "cab"
    assert f038.decode_cyclic("abcd") == "cabd"
    assert f038.decode_cyclic("") == ""
    assert f038.decode_cyclic("ab") == "ab"


def test_decode_cyclic_matches_encode_twice():
    for s in ["", "a", "ab", "abc", "abcd", "abcdefg", "hello world!"]:
        assert f038.decode_cyclic(s) == f038.encode_cyclic(f038.encode_cyclic(s))


def test_decode_cyclic_calls_encode_cyclic_twice(monkeypatch):
    calls = []
    real_encode = f038.encode_cyclic

    def spy(s):
        calls.append(s)
        return real_encode(s)

    monkeypatch.setattr(f038, "encode_cyclic", spy)

    assert f038.decode_cyclic("abc") == "cab"
    assert calls == ["abc", "bca"]
    assert f038.encode_cyclic is spy
