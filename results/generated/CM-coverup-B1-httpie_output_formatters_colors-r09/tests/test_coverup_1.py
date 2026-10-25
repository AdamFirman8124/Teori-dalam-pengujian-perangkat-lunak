# file: project/httpie/output/formatters/colors.py:109-156
# asked: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import pytest

from httpie.output.formatters import colors


def test_get_lexer_returns_direct_mimetype_match(monkeypatch):
    expected_lexer = object()
    mimetype_calls = []

    def get_for_mimetype(mime_type):
        mimetype_calls.append(mime_type)
        return expected_lexer

    def unexpected_name_lookup(name):
        pytest.fail(f"Unexpected lexer name lookup: {name}")

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

    result = colors.get_lexer("application/custom")

    assert result is expected_lexer
    assert mimetype_calls == ["application/custom"]


def test_get_lexer_tries_structured_suffix_mimetypes(monkeypatch):
    expected_lexer = object()
    mimetype_calls = []

    def get_for_mimetype(mime_type):
        mimetype_calls.append(mime_type)
        if mime_type == "application/json":
            return expected_lexer
        raise colors.ClassNotFound(mime_type)

    def unexpected_name_lookup(name):
        pytest.fail(f"Unexpected lexer name lookup: {name}")

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

    result = colors.get_lexer("application/vnd.example+json")

    assert result is expected_lexer
    assert mimetype_calls == [
        "application/vnd.example+json",
        "application/vnd.example",
        "application/json",
    ]


def test_get_lexer_falls_back_to_structured_suffix_names(monkeypatch):
    expected_lexer = object()
    mimetype_calls = []
    name_calls = []

    def get_for_mimetype(mime_type):
        mimetype_calls.append(mime_type)
        raise colors.ClassNotFound(mime_type)

    def get_by_name(name):
        name_calls.append(name)
        if name == "foo":
            raise colors.ClassNotFound(name)
        return expected_lexer

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

    result = colors.get_lexer("application/foo+bar")

    assert result is expected_lexer
    assert mimetype_calls == [
        "application/foo+bar",
        "application/foo",
        "application/bar",
    ]
    assert name_calls == ["foo", "bar"]


def test_get_lexer_adds_json_as_last_name_fallback(monkeypatch):
    expected_lexer = object()
    name_calls = []

    def get_for_mimetype(mime_type):
        raise colors.ClassNotFound(mime_type)

    def get_by_name(name):
        name_calls.append(name)
        if name == "problem-json":
            raise colors.ClassNotFound(name)
        return expected_lexer

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

    result = colors.get_lexer("application/problem-json")

    assert result is expected_lexer
    assert name_calls == ["problem-json", "json"]


def test_get_lexer_returns_none_when_no_candidate_matches(monkeypatch):
    mimetype_calls = []
    name_calls = []

    def get_for_mimetype(mime_type):
        mimetype_calls.append(mime_type)
        raise colors.ClassNotFound(mime_type)

    def get_by_name(name):
        name_calls.append(name)
        raise colors.ClassNotFound(name)

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

    result = colors.get_lexer("application/unknown")

    assert result is None
    assert mimetype_calls == ["application/unknown"]
    assert name_calls == ["unknown"]


def test_get_lexer_replaces_text_lexer_for_valid_explicit_json(monkeypatch):
    text_lexer = colors.TextLexer()
    json_lexer = object()
    name_calls = []

    def get_for_mimetype(mime_type):
        assert mime_type == "text/plain"
        return text_lexer

    def get_by_name(name):
        name_calls.append(name)
        assert name == "json"
        return json_lexer

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
        body='{"answer": 42}',
    )

    assert result is json_lexer
    assert name_calls == ["json"]


def test_get_lexer_keeps_none_for_invalid_explicit_json(monkeypatch):
    name_calls = []

    def get_for_mimetype(mime_type):
        raise colors.ClassNotFound(mime_type)

    def get_by_name(name):
        name_calls.append(name)
        raise colors.ClassNotFound(name)

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
        "application/unknown",
        explicit_json=True,
        body="{invalid json",
    )

    assert result is None
    assert name_calls == ["unknown"]


def test_get_lexer_uses_json_for_valid_body_when_no_lexer_matches(monkeypatch):
    json_lexer = object()
    name_calls = []

    def get_for_mimetype(mime_type):
        raise colors.ClassNotFound(mime_type)

    def get_by_name(name):
        name_calls.append(name)
        if name == "unknown":
            raise colors.ClassNotFound(name)
        assert name == "json"
        return json_lexer

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
        "application/unknown",
        explicit_json=True,
        body="[1, 2, 3]",
    )

    assert result is json_lexer
    assert name_calls == ["unknown", "json"]
