# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

import pytest

from isort.exceptions import AssignmentsFormatMismatch, ISortError


@pytest.mark.parametrize(
    "code",
    [
        "FOO = 1\nBAR = 2",
        "invalid =\n    multiline_value",
    ],
)
def test_assignments_format_mismatch(code):
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
    assert str(error) == expected_message
    assert error.args == (expected_message,)
