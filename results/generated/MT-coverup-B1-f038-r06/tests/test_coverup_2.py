# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

import f038


def test_decode_cyclic_executes_return_line():
    # Line 12 is the only statement in decode_cyclic; calling it must run it.
    assert f038.decode_cyclic("abc") == "cab"


@pytest.mark.parametrize(
    "s",
    ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefghij"],
)
def test_decode_cyclic_equals_double_encode(s):
    expected = f038.encode_cyclic(f038.encode_cyclic(s))
    assert f038.decode_cyclic(s) == expected
    assert len(f038.decode_cyclic(s)) == len(s)


@pytest.mark.parametrize("s", ["", "a", "ab", "d", "de"])
def test_decode_cyclic_is_identity_when_no_full_group(s):
    # Strings with no complete 3-char group are left untouched by
    # encode_cyclic, so decoding them is the identity.
    assert f038.decode_cyclic(s) == s


def test_decode_cyclic_calls_encode_cyclic_twice(monkeypatch):
    calls = []
    real_encode = f038.encode_cyclic

    def spy(text):
        calls.append(text)
        return real_encode(text)

    monkeypatch.setattr(f038, "encode_cyclic", spy)

    result = f038.decode_cyclic("abcdef")

    once = real_encode("abcdef")
    assert calls == ["abcdef", once]
    assert result == real_encode(once)
    assert result == "cabfde"
