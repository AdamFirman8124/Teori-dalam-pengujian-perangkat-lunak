# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

"""
Coverage tests for httpie.output.formatters.colors.get_lexer (lines 115-156).

get_lexer() is a pure function: it only reads its arguments and pygments'
public lookup API and mutates no module or global state, so no
monkeypatching/cleanup is required to avoid state pollution.

Note: this environment's TextLexer only registers the 'text' alias
(no 'plain'/'verbatim'), so the name-fallback test uses 'x-foo/text'.
"""
from pygments.lexers.data import JsonLexer
from pygments.lexers.html import XmlLexer
from pygments.lexers.special import TextLexer

from httpie.output.formatters.colors import get_lexer


def test_get_lexer_resolves_by_mime_type():
    # Lines 115-118 (no '+' in subtype), 133-137 (mimetype hit -> break).
    lexer = get_lexer('application/json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_mime_type_with_suffix():
    # Lines 120-124 ('+' in subtype: extra names and mime types built),
    # lines 138-139 (ClassNotFound for the unknown candidates) and the
    # eventual mimetype hit on '<type>/<subtype_suffix>'.
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_falls_back_to_lexer_name():
    # Lines 138-139 (mimetype lookup fails), 140-141 (for/else fallback),
    # 142-143 (name lookup succeeds: 'text' -> TextLexer).
    lexer = get_lexer('x-foo/text')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_json_subtype_appends_json_name():
    # Lines 129-130 ('json' in subtype -> 'json' name appended), then the
    # name fallback resolves it.
    lexer = get_lexer('x-foo/json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_unknown_returns_none():
    # Lines 144-145 (ClassNotFound in the name loop) and line 156
    # returning the untouched None.
    assert get_lexer('x-foo/bar-baz-qux') is None


def test_get_lexer_explicit_json_valid_body_overrides_text_lexer():
    # Line 147 condition true via `isinstance(lexer, TextLexer)`,
    # lines 149-150 (json.loads succeeds), 153-154 (JSON lexer chosen).
    lexer = get_lexer('text/plain', explicit_json=True, body='{"a": [1, 2]}')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_invalid_body_keeps_text_lexer():
    # Line 147 condition true, lines 151-152 (ValueError -> pass),
    # original TextLexer returned.
    lexer = get_lexer('text/plain', explicit_json=True, body='definitely not json {')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_no_lexer_valid_body():
    # Line 147 condition true via `not lexer`, lines 149-150 and 153-154.
    lexer = get_lexer('x-foo/bar-baz-qux', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_no_lexer_invalid_body():
    # Line 147 condition true via `not lexer`, lines 151-152, still None.
    assert get_lexer('x-foo/bar-baz-qux', explicit_json=True, body='not json') is None


def test_get_lexer_explicit_json_does_not_override_resolved_lexer():
    # Line 147 condition false (a non-Text lexer was found): the body must
    # not be re-parsed and the XML lexer must survive untouched.
    lexer = get_lexer('application/xml', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, XmlLexer)


def test_get_lexer_explicit_json_empty_body_short_circuits():
    # Line 147 condition false via the falsy `body` operand.
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)
