# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

import pytest

from isort.exceptions import AssignmentsFormatMismatch, ISortError


def test_assignments_format_mismatch_stores_code():
    code = "x=1"
    exc = AssignmentsFormatMismatch(code)
    assert exc.code == code
    assert exc.args[0].find(code) != -1


def test_assignments_format_mismatch_message_format():
    code = "bad_code_example"
    exc = AssignmentsFormatMismatch(code)
    msg = str(exc)
    assert "isort was told to sort a section of assignments" in msg
    assert code in msg
    assert "Does not match isort's strict single line formatting requirement" in msg
    assert "{variable_name} = {value}" in msg
    assert "{variable_name2} = {value2}" in msg


def test_assignments_format_mismatch_is_isort_error():
    code = "a = 1\nb=2"
    exc = AssignmentsFormatMismatch(code)
    assert isinstance(exc, ISortError)
    assert isinstance(exc, Exception)
    assert exc.code == code


def test_assignments_format_mismatch_can_be_raised_and_caught():
    code = "invalid assignment format"
    with pytest.raises(AssignmentsFormatMismatch) as exc_info:
        raise AssignmentsFormatMismatch(code)
    assert exc_info.value.code == code
    assert code in str(exc_info.value)


def test_assignments_format_mismatch_empty_code():
    code = ""
    exc = AssignmentsFormatMismatch(code)
    assert exc.code == ""
    assert "isort was told to sort a section of assignments" in str(exc)
