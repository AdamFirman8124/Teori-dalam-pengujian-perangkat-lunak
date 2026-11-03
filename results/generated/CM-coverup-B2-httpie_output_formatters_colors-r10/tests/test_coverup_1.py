# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

"""Coverage tests for ``httpie.output.formatters.colors.get_lexer``.

These tests exercise every line and branch of ``get_lexer`` (lines 115-156):
the '+'-subtype splitting, the 'json' subtype hint, the mimetype lookup loop
(including its ``except ClassNotFound`` path and the ``for/else`` fallback to
name-based lookup, including its ``except ClassNotFound`` path), and the
``explicit_json`` promotion logic (valid JSON, invalid JSON, no lexer
resolved, non-TextLexer, empty body, and flag disabled).

The tests only read pygments' global lexer registries, so no state is
mutated and no cleanup/monkeypatching is required.
"""

from pygments.lexers import HtmlLexer, JsonLexer, PythonLexer, TextLexer

from httpie.output.formatters.colors import get_lexer


def test_get_lexer_resolves_simple_mime_type():
    """Lines 115-118, 133-137, 156: no '+' in subtype, mimetype lookup
    succeeds on the first candidate and breaks out of the loop."""
    lexer = get_lexer('text/html')
    assert isinstance(lexer, HtmlLexer)


def test_get_lexer_text_plain_resolves_to_text_lexer():
    """'text/plain' resolves to the null TextLexer via mimetype lookup."""
    lexer = get_lexer('text/plain')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_mime_with_plus_sign_falls_back_to_component_mimes():
    """Lines 120-124, 129-130, 138-139: a '+' subtype splits into name and
    suffix, extra candidate mimetypes are tried, earlier candidates raise
    ClassNotFound (caught and passed), and 'application/json' finally
    matches because the subtype contains 'json'."""
    lexer = get_lexer('application/foo+json')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_falls_back_to_name_lookup():
    """Lines 141-143: the mimetype loop exhausts without a break, so the
    ``for/else`` name-lookup loop runs and resolves the subtype as a lexer
    alias."""
    lexer = get_lexer('weird/python')
    assert isinstance(lexer, PythonLexer)


def test_get_lexer_falls_back_to_name_lookup_with_plus_sign():
    """Same fallback path, but for a '+'-containing subtype: the suffix
    'python' is used as a lexer name after all mimetype candidates fail."""
    lexer = get_lexer('weird/bar+python')
    assert isinstance(lexer, PythonLexer)


def test_get_lexer_returns_none_when_nothing_resolves():
    """Lines 144-145, 156: both mimetype and name lookups raise
    ClassNotFound, so ``lexer`` stays ``None``."""
    assert get_lexer('foo/bar') is None


def test_get_lexer_returns_none_for_unresolvable_suffixed_mime():
    """A '+' subtype whose name/suffix/mimetype candidates all fail to
    resolve still yields ``None``."""
    assert get_lexer('foo/bar+baz') is None


def test_get_lexer_explicit_json_promotes_text_lexer_to_json():
    """Lines 147-150, 154: explicit_json with a non-empty body and a
    TextLexer result; the body parses as JSON, so the JSON lexer is
    substituted."""
    lexer = get_lexer('text/plain', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_promotes_when_no_lexer_resolved():
    """Line 147: the ``not lexer`` true-path of the explicit_json condition
    (nothing resolved for 'foo/bar'), with a valid JSON body."""
    lexer = get_lexer('foo/bar', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_explicit_json_invalid_body_keeps_text_lexer():
    """Lines 151-152: ``json.loads`` raises ValueError, which is caught and
    passed, so the originally resolved TextLexer is returned."""
    lexer = get_lexer('text/plain', explicit_json=True, body='definitely not json')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_invalid_body_without_lexer_returns_none():
    """Lines 151-152 in the no-lexer case: invalid JSON body means no
    promotion happens and ``None`` is returned."""
    lexer = get_lexer('foo/bar', explicit_json=True, body='definitely not json')
    assert lexer is None


def test_get_lexer_explicit_json_ignored_for_non_text_lexer():
    """Line 147 false-path: the resolved lexer is neither ``None`` nor a
    TextLexer, so the JSON promotion is skipped even for a valid JSON
    body."""
    lexer = get_lexer('text/html', explicit_json=True, body='{"a": 1}')
    assert isinstance(lexer, HtmlLexer)


def test_get_lexer_explicit_json_ignored_for_empty_body():
    """Line 147 false-path: an empty body short-circuits the condition."""
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert isinstance(lexer, TextLexer)


def test_get_lexer_explicit_json_flag_off():
    """Line 147 false-path: ``explicit_json`` disabled means the body is
    never parsed and the TextLexer is kept."""
    lexer = get_lexer('text/plain', explicit_json=False, body='{"a": 1}')
    assert isinstance(lexer, TextLexer)
