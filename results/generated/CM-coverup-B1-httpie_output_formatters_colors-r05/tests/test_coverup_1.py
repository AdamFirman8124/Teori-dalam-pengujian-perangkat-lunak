# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import json

import pytest
from pygments.lexer import Lexer
from pygments.lexers import get_lexer_by_name
from pygments.lexers.data import JsonLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.special import TextLexer
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import get_lexer


def test_get_lexer_found_by_mimetype_no_plus_no_json():
    # Covers lines 115-118, 133-138 (break path), 156
    lexer = get_lexer('text/html')
    assert isinstance(lexer, HtmlLexer)


def test_get_lexer_subtype_with_plus_and_json_suffix():
    # Covers lines 120-124 (+ branch), 129-130 ('json' in subtype),
    # found via extended mime type 'application/json'
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_found_by_name_fallback():
    # Covers lines 138-145: mimetype lookup fails (ClassNotFound),
    # for-else falls into name loop, resolved by name 'python'
    lexer = get_lexer('x/foo', body='', explicit_json=False) if False else get_lexer('x/python')
    assert isinstance(lexer, PythonLexer)


def test_get_lexer_nothing_found_returns_none():
    # Covers full fallback exhaustion: no mimetype, no name, no json
    lexer = get_lexer('x/unknownthing')
    assert lexer is None


def test_get_lexer_explicit_json_replaces_text_lexer():
    # Covers lines 147-154: explicit_json, body truthy, lexer is TextLexer,
    # body parses as JSON -> replaced by JSON lexer
    body = '{"a": 1}'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_invalid_body_keeps_lexer():
    # Covers line 151-152: ValueError branch -> lexer unchanged
    body = 'not json {'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_no_lexer_valid_body():
    # explicit_json with lexer None (nothing resolved) and valid JSON body
    body = '[1, 2, 3]'
    lexer = get_lexer('x/unknownthing', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_empty_body_no_override():
    # Branch 147 not taken: body is empty
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_not_triggered_without_flag():
    # Branch 147 not taken: explicit_json is False even with JSON body
    lexer = get_lexer('text/plain', explicit_json=False, body='{"a": 1}')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_valid_json_lexer_not_replaced():
    # Branch 147 not taken: lexer already found and is not TextLexer
    lexer = get_lexer('application/json', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_json_in_subtype_name_fallback():
    # 'json' appended to lexer_names (line 130) used when mimetype
    # lookups all fail: subtype 'json' resolves by name anyway,
    # but a custom '+json' subtype with unknown names exercises
    # the name 'json' fallback via the explicit_json path.
    lexer = get_lexer('x/foo+json', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)
