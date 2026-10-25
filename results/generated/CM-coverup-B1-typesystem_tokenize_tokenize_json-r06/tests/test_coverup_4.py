# file: project/typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [196, 197], "branches": []}
# gained: {"lines": [196, 197], "branches": []}

import importlib


def test_validate_json_tokenizes_content_and_validates_with_positions(monkeypatch):
    module = importlib.import_module("typesystem.tokenize.tokenize_json")
    content = '{"value": 123}'
    validator = object()
    token = object()
    expected = object()
    calls = {}

    def fake_tokenize_json(received_content):
        calls["content"] = received_content
        return token

    def fake_validate_with_positions(**kwargs):
        calls["validation_kwargs"] = kwargs
        return expected

    monkeypatch.setattr(module, "tokenize_json", fake_tokenize_json)
    monkeypatch.setattr(
        module, "validate_with_positions", fake_validate_with_positions
    )

    result = module.validate_json(content, validator)

    assert result is expected
    assert calls == {
        "content": content,
        "validation_kwargs": {"token": token, "validator": validator},
    }
