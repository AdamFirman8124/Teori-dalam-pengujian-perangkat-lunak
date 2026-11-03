# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

"""Coverage tests for httpie.output.formatters.colors.get_lexer.

These tests exercise every line and branch of ``get_lexer``:

* mime types without a '+' suffix (resolved directly via the mime type
  table, so the name-based fallback for/else is skipped),
* mime types with a '+' suffix (extra mime type candidates and the
  name-based fallback loop, both failing and succeeding),
* the ``explicit_json`` override: TextLexer replaced by the JSON lexer,
  TextLexer kept on an unparseable body, the JSON lexer kept as-is, and
  the override supplying a lexer when none was found -- plus the
  short-circuits (``explicit_json=False``, empty body).

The tests only read pygments' global registries and never mutate any
global state, so no cleanup/patching is required.
"""

import pygments.lexers
from pygments.lexers.special import TextLexer

from httpie.output.formatters.colors import get_lexer


def json_lexer_cls():
    """The class of the lexer pygments resolves for the 'json' alias."""
    return type(pygments.lexers.get_lexer_by_name('json'))


def test_no_plus_subtype_resolved_by_mime_type():
    # 'text/plain': no '+' in the subtype, no 'json' in the subtype, and
    # the very first mime type candidate resolves -> the name fallback
    # loop (the for/else branch) is never entered.
    lexer = get_lexer('text/plain')
    assert isinstance(lexer, TextLexer)


def test_unknown_mime_and_unknown_name_returns_none():
    # Neither the mime type lookup ('foo/bar') nor the lexer name lookup
    # ('bar') resolves, so the for/else fallback runs and still yields
    # None.
    assert get_lexer('foo/bar') is None


def test_plus_subtype_falls_back_to_name_lookup():
    # 'foo/bar+json': none of the mime type candidates ('foo/bar+json',
    # 'foo/bar', 'foo/json') are known to pygments, so the name fallback
    # runs: 'bar' raises ClassNotFound but 'json' resolves.
    lexer = get_lexer('foo/bar+json')
    assert type(lexer) is json_lexer_cls()


def test_plus_subtype_mime_candidates_tried_in_order():
    # 'application/vnd.api+json' and 'application/vnd.api' are unknown to
    # pygments, but the generated 'application/json' candidate resolves,
    # so the mime type loop breaks on its last candidate.
    lexer = get_lexer('application/vnd.api+json')
    assert type(lexer) is json_lexer_cls()


def test_explicit_json_replaces_text_lexer_for_valid_json_body():
    # 'text/plain' resolves to TextLexer; a parseable JSON body with
    # explicit_json=True overrides it with the JSON lexer.
    lexer = get_lexer('text/plain', explicit_json=True, body='{"a": [1, 2]}')
    assert type(lexer) is json_lexer_cls()
    assert not isinstance(lexer, TextLexer)


def test_explicit_json_keeps_text_lexer_for_invalid_json_body():
    # The body does not parse -> the ValueError is swallowed and the
    # TextLexer is kept as-is.
    lexer = get_lexer('text/plain', explicit_json=True, body='{nope')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_does_not_override_real_json_lexer():
    # 'application/json' already resolves to the JSON lexer, which is
    # neither falsy nor a TextLexer, so the override branch must be
    # skipped entirely.
    lexer = get_lexer('application/json', explicit_json=True, body='{"a": 1}')
    assert type(lexer) is json_lexer_cls()


def test_explicit_json_supplies_lexer_when_none_was_found():
    # No lexer resolved at all ('foo/bar') + a parseable JSON body
    # -> the JSON lexer is used.
    lexer = get_lexer('foo/bar', explicit_json=True, body='[1, 2, 3]')
    assert type(lexer) is json_lexer_cls()


def test_explicit_json_with_unparseable_body_and_no_lexer():
    # No lexer + unparseable body -> still no lexer.
    assert get_lexer('foo/bar', explicit_json=True, body='{') is None


def test_explicit_json_ignores_empty_body():
    # An empty body short-circuits the explicit_json branch.
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)


def test_explicit_json_disabled_never_sniffs_body():
    # explicit_json=False -> the JSON sniffing branch must not run even
    # for a TextLexer with a JSON-looking body.
    lexer = get_lexer('text/plain', explicit_json=False, body='{"a": 1}')
    assert isinstance(lexer, TextLexer)
