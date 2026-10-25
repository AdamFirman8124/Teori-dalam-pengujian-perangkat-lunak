# file: project/typesystem/tokenize/tokenize_json.py:165-180
# asked: {"lines": [166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}
# gained: {"lines": [166, 167, 169, 171, 172, 174, 175, 176, 177, 179, 180], "branches": [[166, 167], [166, 169], [169, 171], [169, 174]]}

import pytest
from typesystem.base import ParseError
from typesystem.tokenize.tokenize_json import tokenize_json


def _combined_text(exc):
    parts = []
    try:
        parts.append(str(exc))
    except Exception:
        pass
    try:
        parts.append(repr(exc))
    except Exception:
        pass
    try:
        parts.append(str(getattr(exc, "args", "")))
    except Exception:
        pass
    try:
        parts.append(str(getattr(exc, "__dict__", "")))
    except Exception:
        pass
    for attr in ("text", "code", "msg", "message", "position", "pos"):
        try:
            if hasattr(exc, attr):
                parts.append(str(getattr(exc, attr)))
        except Exception:
            pass
    try:
        m = getattr(exc, "messages", None)
        msgs = m() if callable(m) else m
        if msgs is not None:
            parts.append(str(msgs))
            items = list(msgs) if isinstance(msgs, (list, tuple)) else [msgs]
            for item in items:
                try:
                    parts.append(repr(item))
                except Exception:
                    pass
                try:
                    parts.append(str(getattr(item, "__dict__", "")))
                except Exception:
                    pass
                for a in ("text", "code", "msg", "position", "start_position", "end_position", "line_no", "column_no", "char_index"):
                    try:
                        if hasattr(item, a):
                            parts.append(str(getattr(item, a)))
                    except Exception:
                        pass
    except Exception:
        pass
    try:
        priv = getattr(exc, "_messages", None)
        if priv:
            parts.append(str(priv))
    except Exception:
        pass
    return " ".join(parts)


def _find_position(exc):
    for attr in ("position", "pos", "start_position"):
        if hasattr(exc, attr):
            try:
                v = getattr(exc, attr)
                if v is not None and hasattr(v, "line_no"):
                    return v
            except Exception:
                pass
    try:
        m = getattr(exc, "messages", None)
        msgs = m() if callable(m) else m
        if msgs:
            first = msgs[0] if isinstance(msgs, (list, tuple)) else msgs
            for attr in ("position", "start_position", "pos"):
                try:
                    if hasattr(first, attr):
                        v = getattr(first, attr)
                        if v is not None and hasattr(v, "line_no"):
                            return v
                except Exception:
                    pass
            if hasattr(first, "line_no"):
                return first
            # nested start_position may hold line_no
            try:
                sp = getattr(first, "start_position", None)
                if sp is not None and hasattr(sp, "line_no"):
                    return sp
            except Exception:
                pass
    except Exception:
        pass
    return None


def test_tokenize_json_valid_str():
    token = tokenize_json('{"hello": "world"}')
    assert token.value == {"hello": "world"}
    assert token._content == '{"hello": "world"}'


def test_tokenize_json_valid_bytes():
    token = tokenize_json(b'{"a": 1}')
    assert token.value == {"a": 1}
    assert token._content == '{"a": 1}'


def test_tokenize_json_bytes_invalid_utf8_ignored():
    token = tokenize_json(b'\xff{"a": 1}')
    assert token.value == {"a": 1}


def test_tokenize_json_empty_str():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("")
    combined = _combined_text(exc_info.value)
    assert "No content" in combined
    assert "no_content" in combined
    pos = _find_position(exc_info.value)
    if pos is not None:
        assert pos.line_no == 1
        assert pos.column_no == 1
        assert pos.char_index == 0


def test_tokenize_json_whitespace_only_str():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("   \n\t  ")
    combined = _combined_text(exc_info.value)
    assert "No content" in combined
    assert "no_content" in combined


def test_tokenize_json_empty_bytes():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(b"")
    combined = _combined_text(exc_info.value)
    assert "No content" in combined
    assert "no_content" in combined


def test_tokenize_json_whitespace_bytes():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(b"   ")
    combined = _combined_text(exc_info.value)
    assert "No content" in combined


def test_tokenize_json_parse_error_str():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("{invalid}")
    combined = _combined_text(exc_info.value)
    assert "parse_error" in combined
    assert combined.strip() != ""


def test_tokenize_json_parse_error_bytes():
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(b"{invalid}")
    combined = _combined_text(exc_info.value)
    assert "parse_error" in combined


def test_tokenize_json_parse_error_position():
    import json
    from json.decoder import JSONDecodeError
    bad = '{"a": }'
    try:
        json.loads(bad)
        pytest.fail("expected JSONDecodeError")
    except JSONDecodeError as jde:
        exp_msg = jde.msg + "."
        exp_line, exp_col, exp_pos = jde.lineno, jde.colno, jde.pos
    with pytest.raises(ParseError) as exc_info:
        tokenize_json(bad)
    combined = _combined_text(exc_info.value)
    assert "parse_error" in combined
    assert exp_msg in combined
    pos = _find_position(exc_info.value)
    if pos is not None:
        assert pos.line_no == exp_line
        assert pos.column_no == exp_col
        assert pos.char_index == exp_pos
