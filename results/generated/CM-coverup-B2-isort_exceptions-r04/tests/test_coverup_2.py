# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import LiteralParsingFailure


def test_literal_parsing_failure_stores_code_and_original_error():
    code = "sort"
    original_error = ValueError("invalid literal")

    exc = LiteralParsingFailure(code, original_error)

    assert exc.code == code
    assert exc.original_error is original_error
    assert "isort failed to parse the given literal sort" in str(exc)
    assert "ast.literal_eval" in str(exc)
    assert "invalid literal" in str(exc)
