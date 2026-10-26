# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

import pytest

from isort.exceptions import UnsupportedEncoding


@pytest.mark.parametrize("filename", ["example.py", Path("example.py")])
def test_unsupported_encoding_initialization(filename):
    error = UnsupportedEncoding(filename)

    assert error.filename == filename
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert error.args == (f"Unknown or unsupported encoding in {filename}",)
