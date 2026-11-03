# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

import pytest

from isort.exceptions import AssignmentsFormatMismatch, ISortError


def test_assignments_format_mismatch_message_and_code():
    code = "x = 1\ny = 2"
    error = AssignmentsFormatMismatch(code)

    # The exception should be an ISortError (and thus an Exception).
    assert isinstance(error, ISortError)
    assert isinstance(error, Exception)

    # The `code` attribute must be stored exactly as given (line 137).
    assert error.code == code

    # The message must include the offending code and the formatting
    # requirement explanation (lines 128-136).
    message = str(error)
    assert "isort was told to sort a section of assignments" in message
    assert code in message
    assert "Does not match isort's strict single line formatting requirement" in message
    assert "{variable_name} = {value}" in message
    assert "{variable_name2} = {value2}" in message
    assert "..." in message

    # The message should end with the trailing blank lines from the template.
    assert message.endswith("...\n\n")


def test_assignments_format_mismatch_with_empty_code():
    error = AssignmentsFormatMismatch("")

    assert error.code == ""
    message = str(error)
    assert "isort was told to sort a section of assignments" in message
    assert "Does not match isort's strict single line formatting requirement" in message
