# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import json

import pytest
from pygments.lexers.special import TextLexer
from pygments.lexers.data import JsonLexer
from pygments.lexers.html import HtmlLexer
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import get_lexer


def test_get_lexer_simple_mime_resolved_by_mimetype():
    """Covers lines 115-118, 133-138 (mime loop success, break)."""
    lexer = get_lexer('text/html')
    assert isinstance(lexer, HtmlLexer)


def test_get_lexer_subtype_without_plus_and_json_fallback_name():
    """Covers line 117-118 (no '+'), 129-130 ('json' in subtype), 141-145 (name loop)."""
    lexer = get_lexer('application/json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_vendor_plus_suffix():
    """Covers lines 120-124 ('+' in subtype: split, extended mime_types and names)."""
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_unknown_mime_returns_none():
    """Covers lines 138-139, 141-145 with all lookups failing, and 147 (False branch)."""
    lexer = get_lexer('foo/bar')
    assert lexer is None


def test_get_lexer_explicit_json_valid_body_overrides_text_lexer():
    """Covers lines 147-154: explicit_json, TextLexer resolved, valid JSON body."""
    body = '{"a": 1}'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_invalid_body_keeps_text_lexer():
    """Covers lines 149-152: ValueError branch (invalid JSON body)."""
    body = 'not json at all'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_valid_body_with_no_lexer():
    """Covers line 147 'not lexer' branch: unknown mime, valid JSON body."""
    body = '[1, 2, 3]'
    lexer = get_lexer('foo/bar', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_empty_body_no_override():
    """Covers line 147 'body' falsy branch: no JSON parsing happens."""
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_not_needed_when_real_lexer_found():
    """Covers line 147 'isinstance TextLexer' False branch: JSON mime already resolved."""
    body = '{"a": 1}'
    lexer = get_lexer('application/json', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_false_does_not_parse_body():
    """Covers line 147 explicit_json False branch even with a JSON-looking body."""
    lexer = get_lexer('text/plain', explicit_json=False, body='{"a": 1}')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_json_fallback_name_used_when_mime_unknown():
    """Covers line 129-130 plus name-loop resolution for a json-ish unknown mime."""
    lexer = get_lexer('foo/json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_does_not_mutate_pygments_state():
    """Postcondition: repeated calls are pure (no global state pollution)."""
    first = get_lexer('application/vnd.api+json')
    second = get_lexer('application/vnd.api+json')
    assert type(first) is type(second)
    assert isinstance(first, JsonLexer)
