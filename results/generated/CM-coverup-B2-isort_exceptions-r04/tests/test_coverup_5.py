# file: project/isort/exceptions.py:35-43
# asked: {"lines": [39, 40, 41, 43], "branches": []}
# gained: {"lines": [39, 40, 41, 43], "branches": []}

import pytest

from isort.exceptions import ISortError, IntroducedSyntaxErrors


class TestIntroducedSyntaxErrors:
    """Tests for the IntroducedSyntaxErrors exception (isort/exceptions.py lines 39-43)."""

    def test_message_and_file_path_attribute(self):
        """Constructing the exception must build the correct message and store file_path."""
        file_path = "/some/path/to/file.py"
        exc = IntroducedSyntaxErrors(file_path)

        # Line 43: file_path attribute is stored
        assert exc.file_path == file_path

        # Lines 39-42: super().__init__ was called with the expected message
        expected_message = (
            "isort introduced syntax errors when attempting to sort the imports "
            f"contained within {file_path}."
        )
        assert str(exc) == expected_message
        assert file_path in str(exc)

    def test_inherits_from_isort_error(self):
        """The exception must be an ISortError (and therefore an Exception)."""
        exc = IntroducedSyntaxErrors("another_file.py")
        assert isinstance(exc, ISortError)
        assert isinstance(exc, Exception)

    def test_can_be_raised_and_caught(self):
        """The exception can be raised and caught as an ISortError."""
        file_path = "relative/module.py"
        with pytest.raises(ISortError) as excinfo:
            raise IntroducedSyntaxErrors(file_path)

        assert excinfo.value.file_path == file_path
        assert file_path in str(excinfo.value)
