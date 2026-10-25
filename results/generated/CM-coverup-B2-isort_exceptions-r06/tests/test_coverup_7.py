# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

import pytest

from isort.exceptions import AssignmentsFormatMismatch, ISortError


def test_assignments_format_mismatch_stores_code_and_message():
    code = "x = 1\ny = 2\nnot an assignment"
    exc = AssignmentsFormatMismatch(code)

    assert isinstance(exc, AssignmentsFormatMismatch)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.code == code
    assert exc.args[0] == str(exc)
    assert (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    ) == str(exc)


def test_assignments_format_mismatch_can_be_raised_and_caught():
    code = "value: int = 1"

    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch(code)

    assert exc_info.value.code == code
    assert code in str(exc_info.value)
    assert "{variable_name} = {value}" in str(exc_info.value)
    assert "{variable_name2} = {value2}" in str(exc_info.value)


def test_assignments_format_mismatch_with_empty_code():
    exc = AssignmentsFormatMismatch("")

    assert exc.code == ""
    assert "given code:\n\n\n\nDoes not match" in str(exc)
