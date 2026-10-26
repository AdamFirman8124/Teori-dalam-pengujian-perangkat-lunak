# file: project/isort/exceptions.py:93-105
# asked: {"lines": [99, 100, 102, 104, 105], "branches": []}
# gained: {"lines": [99, 100, 102, 104, 105], "branches": []}

import pytest

from isort.exceptions import LiteralParsingFailure


def test_literal_parsing_failure_attributes_and_message():
    code = "isort:skip"
    original_error = ValueError("invalid literal")

    error = LiteralParsingFailure(code, original_error)

    assert error.code == code
    assert error.original_error is original_error
    assert isinstance(error, Exception)
    assert (
        str(error)
        == "isort failed to parse the given literal isort:skip. It's important to note "
        "that isort literal sorting only supports simple literals parsable by "
        "ast.literal_eval which gave the exception of invalid literal."
    )
