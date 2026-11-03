# file: project/isort/exceptions.py:163-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

"""Tests for isort.exceptions.UnsupportedEncoding (lines 167-168)."""

import sys
from pathlib import Path

import pytest

from isort.exceptions import ISortError, UnsupportedEncoding


@pytest.mark.parametrize(
    "filename",
    [
        "some_file.py",
        Path("some_file.py"),
        "/tmp/nested/dir/other_file.py",
        Path("/tmp/nested/dir/other_file.py"),
    ],
    ids=["str-relative", "path-relative", "str-absolute", "path-absolute"],
)
def test_unsupported_encoding_stores_filename_and_message(filename):
    """UnsupportedEncoding.__init__ must set the message and the filename
    attribute for both str and pathlib.Path inputs."""
    exception = UnsupportedEncoding(filename)

    # Lines 167-168: the message is built from the filename and the
    # filename attribute is stored on the instance.
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert exception.filename == filename
    assert exception.args == (f"Unknown or unsupported encoding in {filename}",)


@pytest.mark.parametrize("filename", ["a.py", Path("a.py")], ids=["str", "path"])
def test_unsupported_encoding_hierarchy(filename):
    """UnsupportedEncoding must be raisable and catchable as an ISortError
    and as a plain Exception."""
    with pytest.raises(ISortError) as excinfo:
        raise UnsupportedEncoding(filename)

    assert excinfo.value.filename == filename
    assert isinstance(excinfo.value, Exception)
    assert str(excinfo.value) == f"Unknown or unsupported encoding in {filename}"


def test_unsupported_encoding_with_tmp_path(tmp_path):
    """Ensure a real, filesystem-backed Path works end to end; pytest's
    tmp_path fixture guarantees cleanup of any created directories."""
    real_file = tmp_path / "module.py"
    real_file.write_text("import os\n", encoding="utf-8")

    exception = UnsupportedEncoding(real_file)

    assert exception.filename == real_file
    assert str(exception) == f"Unknown or unsupported encoding in {real_file}"
    assert exception.filename.exists()
    # tmp_path is cleaned up automatically by pytest; assert state is intact
    # for the fixture teardown that follows.
    assert str(tmp_path) in str(exception.filename)
