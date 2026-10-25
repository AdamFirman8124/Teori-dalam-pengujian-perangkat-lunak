# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

from pygments.lexers.special import TextLexer
from pygments.util import ClassNotFound

from httpie.output.formatters import colors


def test_get_lexer_resolves_direct_mimetype(monkeypatch):
    expected = object()
    mime_calls = []

    def get_for_mimetype(mime):
        mime_calls.append(mime)
        return expected

    def unexpected_name_lookup(name):
        raise AssertionError(f"unexpected lexer-name lookup: {name}")

    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_for_mimetype",
        get_for_mimetype,
    )
    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_by_name",
        unexpected_name_lookup,
    )

    result = colors.get_lexer("text/html")

    assert result is expected
    assert mime_calls == ["text/html"]


def test_get_lexer_uses_structured_suffix_name_fallback(monkeypatch):
    mime_calls = []
    name_calls = []
    expected = object()

    def missing_mimetype(mime):
        mime_calls.append(mime)
        raise ClassNotFound("missing MIME type")

    def get_by_name(name):
        name_calls.append(name)
        if name == "vnd.acme":
            raise ClassNotFound("missing lexer name")
        assert name == "json"
        return expected

    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_for_mimetype",
        missing_mimetype,
    )
    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_by_name",
        get_by_name,
    )

    result = colors.get_lexer("application/vnd.acme+json")

    assert result is expected
    assert mime_calls == [
        "application/vnd.acme+json",
        "application/vnd.acme",
        "application/json",
    ]
    assert name_calls == ["vnd.acme", "json", "json"]


def test_get_lexer_promotes_valid_json_when_no_lexer_exists(monkeypatch):
    name_calls = []
    expected = object()

    def missing_mimetype(mime):
        raise ClassNotFound(f"missing MIME type: {mime}")

    def get_by_name(name):
        name_calls.append(name)
        if name == "json":
            return expected
        raise ClassNotFound(f"missing lexer name: {name}")

    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_for_mimetype",
        missing_mimetype,
    )
    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_by_name",
        get_by_name,
    )

    result = colors.get_lexer(
        "application/x-unknown",
        explicit_json=True,
        body='{"answer": 42}',
    )

    assert result is expected
    assert name_calls == ["x-unknown", "json"]


def test_get_lexer_does_not_promote_invalid_json(monkeypatch):
    mime_calls = []
    name_calls = []

    def missing_mimetype(mime):
        mime_calls.append(mime)
        raise ClassNotFound("missing MIME type")

    def missing_name(name):
        name_calls.append(name)
        raise ClassNotFound("missing lexer name")

    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_for_mimetype",
        missing_mimetype,
    )
    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_by_name",
        missing_name,
    )

    result = colors.get_lexer(
        "application/x-unknown",
        explicit_json=True,
        body="{",
    )

    assert result is None
    assert mime_calls == ["application/x-unknown"]
    assert name_calls == ["x-unknown"]


def test_get_lexer_replaces_text_lexer_for_valid_explicit_json(monkeypatch):
    text_lexer = TextLexer()
    expected = object()
    name_calls = []

    def get_for_mimetype(mime):
        assert mime == "text/plain"
        return text_lexer

    def get_by_name(name):
        name_calls.append(name)
        assert name == "json"
        return expected

    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_for_mimetype",
        get_for_mimetype,
    )
    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_by_name",
        get_by_name,
    )

    result = colors.get_lexer(
        "text/plain",
        explicit_json=True,
        body="[1, 2, 3]",
    )

    assert result is expected
    assert name_calls == ["json"]


def test_get_lexer_keeps_non_text_lexer_for_explicit_json(monkeypatch):
    expected = object()

    def get_for_mimetype(mime):
        assert mime == "application/custom"
        return expected

    def unexpected_json_parse(body):
        raise AssertionError("body must not be parsed when a non-text lexer exists")

    def unexpected_name_lookup(name):
        raise AssertionError(f"unexpected lexer-name lookup: {name}")

    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_for_mimetype",
        get_for_mimetype,
    )
    monkeypatch.setattr(
        colors.pygments.lexers,
        "get_lexer_by_name",
        unexpected_name_lookup,
    )
    monkeypatch.setattr(colors.json, "loads", unexpected_json_parse)

    result = colors.get_lexer(
        "application/custom",
        explicit_json=True,
        body='{"valid": true}',
    )

    assert result is expected
