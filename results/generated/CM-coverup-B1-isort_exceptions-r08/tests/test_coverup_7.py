# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

from isort.exceptions import AssignmentsFormatMismatch, ISortError


def test_assignments_format_mismatch_preserves_code_and_message():
    code = "FIRST = 1\nSECOND = 2"
    error = AssignmentsFormatMismatch(code)

    expected_message = (
        "isort was told to sort a section of assignments, however the given code:\n\n"
        f"{code}\n\n"
        "Does not match isort's strict single line formatting requirement for assignment "
        "sorting:\n\n"
        "{variable_name} = {value}\n"
        "{variable_name2} = {value2}\n"
        "...\n\n"
    )

    assert isinstance(error, ISortError)
    assert error.code == code
    assert error.args == (expected_message,)
    assert str(error) == expected_message
