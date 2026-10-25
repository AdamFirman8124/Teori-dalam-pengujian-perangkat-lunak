# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import json

from pygments.lexers.data import JsonLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.special import TextLexer

from httpie.output.formatters.colors import get_lexer


def test_mime_resolves_via_mimetype_loop_break():
    # Covers lines 115-118, 133-137 (loop with break), 156.
    lexer = get_lexer('text/plain')
    assert isinstance(lexer, TextLexer)


def test_json_mime_resolves_directly():
    # Covers lines 115-118, 129-130 ('json' in subtype, no '+'), 136-137, 156.
    lexer = get_lexer('application/json')
    assert isinstance(lexer, JsonLexer)


def test_subtype_with_plus_resolves_via_derived_mimetype():
    # Covers lines 120-124 ('+' in subtype branch), 129-130, 134-139
    # (ClassNotFound for unknown mimetypes, success on derived one), 156.
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)


def test_fallback_to_lexer_names_after_all_mimetypes_fail():
    # Covers lines 138-139 (all mimetype lookups raise ClassNotFound),
    # 140-145 (for/else -> name loop, ClassNotFound pass, then success), 156.
    lexer = get_lexer('text/weird+python')
    assert isinstance(lexer, PythonLexer)


def test_json_in_subtype_falls_back_to_json_lexer_name():
    # Covers lines 120-124, 129-130, 138-145 with 'json' resolved by name, 156.
    lexer = get_lexer('text/foo+json')
    assert isinstance(lexer, JsonLexer)


def test_no_lexer_found_returns_none():
    # Covers lines 133-145 with every lookup failing, and 147/156 with a
    # falsy lexer (explicit_json defaults to False here).
    assert get_lexer('foo/bar') is None


def test_explicit_json_overrides_text_lexer():
    # Covers lines 147-150, 153-154 (valid JSON body, TextLexer -> JsonLexer), 156.
    body = '{"a": [1, 2]}'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)


def test_explicit_json_invalid_body_keeps_existing_lexer():
    # Covers lines 147-152 (ValueError -> pass), 156.
    lexer = get_lexer('text/plain', explicit_json=True, body='not json {')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_empty_body_does_not_override():
    # Covers line 147 with a falsy body (short-circuit), 156.
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_with_no_lexer_resolves_json():
    # Covers line 147 with `not lexer` true, 149-154, 156.
    lexer = get_lexer('foo/bar', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)


def test_explicit_json_skips_parsing_when_lexer_already_json(monkeypatch):
    # Covers line 147 with the isinstance(lexer, TextLexer) / `not lexer`
    # disjunct false: body must NOT be parsed, existing lexer kept.
    calls = []

    def fake_loads(body):
        calls.append(body)
        return {}

    monkeypatch.setattr(json, 'loads', fake_loads)
    lexer = get_lexer('application/json', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)
    assert calls == []


def test_explicit_json_non_text_lexer_unchanged(monkeypatch):
    # Covers line 147 with a resolved non-Text lexer: no re-parsing, no override.
    calls = []

    def fake_loads(body):
        calls.append(body)
        return {}

    monkeypatch.setattr(json, 'loads', fake_loads)
    lexer = get_lexer('text/weird+python', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, PythonLexer)
    assert calls == []


def test_explicit_json_parses_body_before_overriding(monkeypatch):
    # Verifies the body really is parsed (line 150) on the override path.
    calls = []

    def fake_loads(body):
        calls.append(body)
        return json.__dict__ and {}

    real_loads = json.loads

    def recording_loads(body):
        calls.append(body)
        return real_loads(body)

    monkeypatch.setattr(json, 'loads', recording_loads)
    lexer = get_lexer('text/plain', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)
    assert calls == ['{"a": 1}']
