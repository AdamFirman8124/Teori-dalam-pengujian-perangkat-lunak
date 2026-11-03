# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

import pytest

from isort.exceptions import AssignmentsFormatMismatch, ISortError


def test_assignments_format_mismatch_message_and_code():
    code = "x = 1\ny = 2"
    error = AssignmentsFormatMismatch(code)

    # The exception should be an ISortError (and therefore an Exception).
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # The 'code' attribute must be stored exactly as given (line 137).
    assert error.code == code

    # The message built in super().__init__ (lines 128-136) must contain
    # the given code and the strict formatting requirement text.
    message = str(error)
    assert code in message
    assert (
        "isort was told to sort a section of assignments, however the given code:"
        in message
    )
    assert (
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:" in message
    )
    assert "{variable_name} = {value}" in message
    assert "{variable_name2} = {value2}" in message
    assert "..." in message


def test_assignments_format_mismatch_empty_code():
    # Edge case: empty code string still exercises the full constructor.
    error = AssignmentsFormatMismatch("")
    assert error.code == ""
    assert str(error).startswith(
        "isort was told to sort a section of assignments, however the given code:\n\n"
    )
    assert str(error).endswith(
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )
