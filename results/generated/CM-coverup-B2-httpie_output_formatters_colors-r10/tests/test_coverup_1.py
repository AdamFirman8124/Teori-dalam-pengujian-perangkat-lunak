# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import pygments.lexers
from pygments.lexers.special import TextLexer
from pygments.util import ClassNotFound
from httpie.output.formatters.colors import get_lexer


def test_plain_mimetype_hit_no_plus_no_json():
    lexer = get_lexer("text/html")
    assert lexer is not None
    assert not isinstance(lexer, TextLexer)


def test_no_plus_with_json_mimetype_hit():
    lexer = get_lexer("application/json")
    assert lexer is not None
    assert "json" in [a.lower() for a in lexer.aliases]


def test_plus_with_json_mimetype_hit():
    # subtype contains '+' and 'json': covers subtype split + json append
    # mime_types = [application/vnd.api+json, application/vnd.api, application/json]
    lexer = get_lexer("application/vnd.api+json")
    assert lexer is not None
    assert "json" in [a.lower() for a in lexer.aliases]


def test_plus_without_json_mimetype_hit():
    lexer = get_lexer("application/atom+xml")
    assert lexer is not None


def test_mimetype_miss_fallback_to_name_partial_failure(monkeypatch):
    def fake_for_mimetype(mime_type):
        raise ClassNotFound(mime_type)

    real_by_name = pygments.lexers.get_lexer_by_name
    seen = []

    def fake_by_name(name):
        seen.append(name)
        if name == "foo":
            raise ClassNotFound(name)
        if name == "bar":
            return real_by_name("python")
        return real_by_name(name)

    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", fake_for_mimetype)
    monkeypatch.setattr(pygments.lexers, "get_lexer_by_name", fake_by_name)
    lexer = get_lexer("application/foo+bar")
    assert lexer is not None
    assert "foo" in seen
    assert "bar" in seen
    assert "python" in [a.lower() for a in lexer.aliases]


def test_all_misses_returns_none(monkeypatch):
    def fake_raise(*args, **kwargs):
        raise ClassNotFound("missing")

    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", fake_raise)
    monkeypatch.setattr(pygments.lexers, "get_lexer_by_name", fake_raise)
    assert get_lexer("foo/bar") is None
    assert get_lexer("foo/bar", explicit_json=False, body='{"a": 1}') is None


def test_explicit_json_fallback_from_none_valid_body(monkeypatch):
    def fake_for_mimetype(mime_type):
        raise ClassNotFound(mime_type)

    real_by_name = pygments.lexers.get_lexer_by_name

    def fake_by_name(name):
        if name == "json":
            return real_by_name("json")
        raise ClassNotFound(name)

    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", fake_for_mimetype)
    monkeypatch.setattr(pygments.lexers, "get_lexer_by_name", fake_by_name)
    lexer = get_lexer("foo/bar", explicit_json=True, body='{"a": 1}')
    assert lexer is not None
    assert "json" in [a.lower() for a in lexer.aliases]


def test_explicit_json_from_none_invalid_body_stays_none(monkeypatch):
    def fake_for_mimetype(mime_type):
        raise ClassNotFound(mime_type)

    real_by_name = pygments.lexers.get_lexer_by_name

    def fake_by_name(name):
        if name == "json":
            return real_by_name("json")
        raise ClassNotFound(name)

    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", fake_for_mimetype)
    monkeypatch.setattr(pygments.lexers, "get_lexer_by_name", fake_by_name)
    lexer = get_lexer("foo/bar", explicit_json=True, body="not-json{{{")
    assert lexer is None


def test_explicit_json_from_text_valid_body_becomes_json(monkeypatch):
    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", lambda m: TextLexer())
    lexer = get_lexer("text/plain", explicit_json=True, body='{"x": true}')
    assert lexer is not None
    assert not isinstance(lexer, TextLexer)
    assert "json" in [a.lower() for a in lexer.aliases]


def test_explicit_json_from_text_invalid_body_stays_text(monkeypatch):
    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", lambda m: TextLexer())
    lexer = get_lexer("text/plain", explicit_json=True, body="not json")
    assert isinstance(lexer, TextLexer)


def test_explicit_json_non_text_lexer_no_override(monkeypatch):
    html_lexer = pygments.lexers.get_lexer_by_name("html")
    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", lambda m: html_lexer)
    lexer = get_lexer("text/html", explicit_json=True, body='{"a": 1}')
    assert lexer is html_lexer


def test_explicit_json_empty_body_no_fallback(monkeypatch):
    def fake_raise(*args, **kwargs):
        raise ClassNotFound("missing")

    monkeypatch.setattr(pygments.lexers, "get_lexer_for_mimetype", fake_raise)
    monkeypatch.setattr(pygments.lexers, "get_lexer_by_name", fake_raise)
    assert get_lexer("foo/bar", explicit_json=True, body="") is None
