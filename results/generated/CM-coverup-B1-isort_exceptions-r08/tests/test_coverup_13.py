# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path
from typing import Union

import pytest

from isort.exceptions import UnsupportedEncoding


@pytest.mark.parametrize(
    "filename",
    ["unknown_encoding.py", Path("unknown_encoding.py")],
)
def test_unsupported_encoding_initialization(filename: Union[str, Path]) -> None:
    error = UnsupportedEncoding(filename)

    assert error.filename is filename
    assert str(error) == f"Unknown or unsupported encoding in {filename}"
    assert error.args == (f"Unknown or unsupported encoding in {filename}",)
