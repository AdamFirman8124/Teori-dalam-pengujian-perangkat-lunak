# file: project/isort/exceptions.py:122-137
# asked: {"lines": [128, 129, 130, 137], "branches": []}
# gained: {"lines": [128, 129, 130, 137], "branches": []}

import pytest

from isort.exceptions import AssignmentsFormatMismatch, ISortError


class TestAssignmentsFormatMismatch:
    def test_message_and_code_attribute(self):
        code = "x = 1\ny = 2"
        error = AssignmentsFormatMismatch(code)

        # Verify the exception is properly initialized (lines 128-137)
        assert isinstance(error, AssignmentsFormatMismatch)
        assert isinstance(error, ISortError)
        assert isinstance(error, Exception)

        # Verify the code attribute is stored (line 137)
        assert error.code == code

        # Verify the full message built in super().__init__ (lines 128-136)
        expected_message = (
            "isort was told to sort a section of assignments, however the given code:\n\n"
            f"{code}\n\n"
            "Does not match isort's strict single line formatting requirement for assignment "
            "sorting:\n\n"
            "{variable_name} = {value}\n"
            "{variable_name2} = {value2}\n"
            "...\n\n"
        )
        assert str(error) == expected_message

    def test_message_embeds_given_code(self):
        code = "foo = 'bar'"
        error = AssignmentsFormatMismatch(code)

        assert code in str(error)
        assert "isort was told to sort a section of assignments" in str(error)
        assert "Does not match isort's strict single line formatting requirement" in str(error)
        assert "{variable_name} = {value}" in str(error)
        assert "{variable_name2} = {value2}" in str(error)

    def test_empty_code(self):
        error = AssignmentsFormatMismatch("")
        assert error.code == ""
        assert "however the given code:\n\n\n\n" in str(error)

    def test_multiline_code_preserved(self):
        code = "a = 1\nb = 2\nc = 3"
        error = AssignmentsFormatMismatch(code)
        assert error.code == code
        assert code in str(error)

    def test_can_be_raised_and_caught(self):
        code = "bad = format"
        with pytest.raises(AssignmentsFormatMismatch) as exc_info:
            raise AssignmentsFormatMismatch(code)

        assert exc_info.value.code == code
        assert code in str(exc_info.value)
