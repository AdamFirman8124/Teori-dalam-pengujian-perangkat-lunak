# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

from pathlib import Path

import pytest

from isort.exceptions import UnsupportedEncoding


@pytest.mark.parametrize(
    "filename",
    [
        "example.py",
        Path("example.py"),
        Path("/some/dir") / "example.py",
    ],
)
def test_unsupported_encoding(filename):
    with pytest.raises(UnsupportedEncoding) as excinfo:
        raise UnsupportedEncoding(filename)

    assert excinfo.value.filename == filename
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"
