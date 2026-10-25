# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import json

import pygments.lexers
import pytest
from pygments.lexers.data import JsonLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.special import TextLexer
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import get_lexer


def _raise_class_not_found(*args, **kwargs):
    raise ClassNotFound(args[0] if args else 'nope')


def test_get_lexer_plain_subtype_uses_mimetype_lookup(monkeypatch):
    """Lines 115-118, 133-137: no '+' in subtype, mimetype lookup succeeds."""
    tried_names = []

    def fake_by_name(name):
        tried_names.append(name)
        raise AssertionError('get_lexer_by_name should not be called')

    monkeypatch.setattr(pygments.lexers, 'get_lexer_by_name', fake_by_name)

    lexer = get_lexer('application/json')

    assert isinstance(lexer, JsonLexer)
    assert tried_names == []


def test_get_lexer_plus_subtype_builds_candidates(monkeypatch):
    """Lines 120-124, 129-130, 141-145: '+' branch, candidate mime/name lists.

    Note: subtype 'vnd.api+json' contains 'json', so 'json' is appended
    twice to lexer_names (once as suffix, once as the json fallback).
    """
    tried_mimes = []
    tried_names = []

    def fake_for_mimetype(mime):
        tried_mimes.append(mime)
        raise ClassNotFound(mime)

    def fake_by_name(name):
        tried_names.append(name)
        if name == 'json':
            return JsonLexer()
        raise ClassNotFound(name)

    monkeypatch.setattr(pygments.lexers, 'get_lexer_for_mimetype', fake_for_mimetype)
    monkeypatch.setattr(pygments.lexers, 'get_lexer_by_name', fake_by_name)

    lexer = get_lexer('application/vnd.api+json')

    assert isinstance(lexer, JsonLexer)
    assert tried_mimes == [
        'application/vnd.api+json',
        'application/vnd.api',
        'application/json',
    ]
    assert tried_names == ['vnd.api', 'json', 'json']


def test_get_lexer_plus_subtype_without_json(monkeypatch):
    """Lines 120-124, 129 (False), 141-145: '+' branch, no json fallback name."""
    tried_names = []

    def fake_by_name(name):
        tried_names.append(name)
        raise ClassNotFound(name)

    monkeypatch.setattr(pygments.lexers, 'get_lexer_for_mimetype', _raise_class_not_found)
    monkeypatch.setattr(pygments.lexers, 'get_lexer_by_name', fake_by_name)

    lexer = get_lexer('application/vnd.foo+xml')

    assert lexer is None
    assert tried_names == ['vnd.foo', 'xml']


def test_get_lexer_unknown_mime_returns_none(monkeypatch):
    """Lines 138-139, 141-145, 156: every lookup fails -> None."""
    monkeypatch.setattr(pygments.lexers, 'get_lexer_for_mimetype', _raise_class_not_found)
    monkeypatch.setattr(pygments.lexers, 'get_lexer_by_name', _raise_class_not_found)

    assert get_lexer('application/x-unknown-thing') is None


def test_get_lexer_explicit_json_with_no_lexer_and_valid_body():
    """Lines 147-154: no lexer found, body is valid JSON -> JSON lexer."""
    lexer = get_lexer(
        'application/x-unknown-thing',
        explicit_json=True,
        body=json.dumps({'a': 1}),
    )

    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_with_no_lexer_and_invalid_body():
    """Lines 147-152: no lexer found, body is not JSON -> stays None."""
    lexer = get_lexer(
        'application/x-unknown-thing',
        explicit_json=True,
        body='not json at all',
    )

    assert lexer is None


def test_get_lexer_explicit_json_upgrades_text_lexer():
    """Lines 147-154: TextLexer + valid JSON body -> JSON lexer."""
    assert isinstance(get_lexer('text/plain'), TextLexer)

    lexer = get_lexer('text/plain', explicit_json=True, body='{"a": 1}')

    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_keeps_non_text_lexer():
    """Line 147 (False branch): a real lexer is left untouched."""
    lexer = get_lexer('text/html', explicit_json=True, body='{"a": 1}')

    assert isinstance(lexer, HtmlLexer)


def test_get_lexer_explicit_json_with_empty_body_keeps_lexer():
    """Line 147: empty body short-circuits the JSON sniffing."""
    lexer = get_lexer('text/plain', explicit_json=True, body='')

    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_false_ignores_json_body():
    """Line 147: explicit_json=False never upgrades the lexer."""
    lexer = get_lexer('text/plain', explicit_json=False, body='{"a": 1}')

    assert isinstance(lexer, TextLexer)
