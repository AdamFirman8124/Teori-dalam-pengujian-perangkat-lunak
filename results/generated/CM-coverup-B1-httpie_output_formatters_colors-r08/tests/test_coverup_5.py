# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

from unittest.mock import Mock

import pytest

from httpie.output.formatters import colors


@pytest.mark.parametrize("explicit_json", [False, True])
def test_get_lexer_for_body_delegates_to_get_lexer(monkeypatch, explicit_json):
    formatter = object.__new__(colors.ColorFormatter)
    formatter.explicit_json = explicit_json

    expected_lexer = object()
    get_lexer_mock = Mock(return_value=expected_lexer)
    monkeypatch.setattr(colors, "get_lexer", get_lexer_mock)

    result = formatter.get_lexer_for_body(
        mime="application/json",
        body='{"key": "value"}',
    )

    assert result is expected_lexer
    get_lexer_mock.assert_called_once_with(
        mime="application/json",
        explicit_json=explicit_json,
        body='{"key": "value"}',
    )
