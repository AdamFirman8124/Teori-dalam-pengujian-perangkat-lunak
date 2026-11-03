# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

"""Tests for httpie.output.formatters.colors.get_lexer (lines 115-156).

These tests are pure: get_lexer() only reads pygments' lexer registry and
never mutates global state, so no patching/cleanup is required. Nothing is
monkeypatched, hence there is no state to leak between tests.
"""

from pygments.lexers.data import JsonLexer
from pygments.lexers.html import HtmlLexer, XmlLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.special import TextLexer

from httpie.output.formatters.colors import get_lexer


def test_mime_without_plus_resolved_by_mimetype():
    # Lines 115-118 ('+' not in subtype) and 133-137 (mime match -> break).
    lexer = get_lexer('text/html')
    assert isinstance(lexer, HtmlLexer)


def test_mime_with_plus_resolved_by_expanded_mimetype():
    # Lines 120-124 (else branch: expand mime_types/lexer_names) and
    # 129-130 skipped ('json' not in subtype). The suffix-derived mime
    # 'application/xml' is what matches.
    lexer = get_lexer('application/vnd.unknown+xml')
    assert isinstance(lexer, XmlLexer)


def test_json_substring_without_plus_resolved_by_name():
    # Lines 117-118, 129-130 ('json' in subtype), 133-139 (mime lookup
    # fails) and 140-145 (name lookup succeeds via the appended 'json').
    lexer = get_lexer('foo/json')
    assert isinstance(lexer, JsonLexer)


def test_json_substring_with_plus_resolved_by_expanded_mimetype():
    # Lines 120-124 and 129-130 with a '+json' subtype; the expanded
    # 'application/json' candidate matches after earlier ones fail
    # (lines 138-139).
    lexer = get_lexer('application/hal+json')
    assert isinstance(lexer, JsonLexer)


def test_no_candidate_matches_returns_none():
    # Lines 133-139 (every mime candidate raises ClassNotFound),
    # 140-145 (name lookup raises too) and 156 (None returned).
    assert get_lexer('foo/bar') is None


def test_resolved_by_name_after_mimetype_failure():
    # Lines 140-145: mime lookup fails, the subtype name resolves.
    lexer = get_lexer('x-unknown/python')
    assert isinstance(lexer, PythonLexer)


def test_plus_subtype_resolved_by_name_after_mimetype_failure():
    # Lines 120-124, 133-139, 141-145: neither the original nor the
    # expanded mime types match; the suffix name 'xml' does, after
    # 'bar' raises ClassNotFound (lines 144-145).
    lexer = get_lexer('x-unknown/bar+xml')
    assert isinstance(lexer, XmlLexer)


def test_explicit_json_replaces_text_lexer_for_valid_json_body():
    # Lines 147 (true via isinstance TextLexer), 149-151, 154.
    lexer = get_lexer('text/plain', explicit_json=True, body='{"a": [1, 2]}')
    assert isinstance(lexer, JsonLexer)


def test_explicit_json_keeps_text_lexer_for_invalid_json_body():
    # Lines 147 (true), 151-152 (ValueError -> pass): TextLexer kept.
    lexer = get_lexer('text/plain', explicit_json=True, body='not json')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_skipped_when_real_lexer_found():
    # Line 147 false branch: lexer is neither None nor a TextLexer.
    lexer = get_lexer('application/json', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)


def test_explicit_json_skipped_when_body_empty():
    # Line 147 false branch: empty body short-circuits the condition.
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_skipped_when_flag_not_set():
    # Line 147 false branch: explicit_json defaults to False.
    lexer = get_lexer('text/plain', body='{"a": 1}')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_replaces_none_lexer_for_valid_json_body():
    # Lines 147 (true via `not lexer`), 149-151, 154: no lexer was
    # found, but the body parses, so the JSON lexer is used.
    lexer = get_lexer('foo/bar', explicit_json=True, body='{"a": null}')
    assert isinstance(lexer, JsonLexer)


def test_explicit_json_keeps_none_lexer_for_invalid_json_body():
    # Lines 147 (true via `not lexer`), 151-152: body does not parse,
    # so the (absent) lexer is kept and None is returned.
    assert get_lexer('foo/bar', explicit_json=True, body='nope') is None
