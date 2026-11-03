# file: project/pytutils/files.py:12-46
# asked: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}
# gained: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}

"""
Tests for pytutils.files.islurp, targeting the previously-uncovered body
(lines 23-46): the 'LINEMODE' string coercion, stdin selection, path
expansion, both iteration strategies, EOF handling and the finally-block
cleanup guards.
"""

import builtins
import io
import sys

import pytest

from pytutils.files import LINEMODE, islurp


def test_islurp_line_mode_default(tmp_path):
    """Default call iterates a file line by line, including a final line
    without a trailing newline, and stops at EOF."""
    p = tmp_path / "sample.txt"
    p.write_text("first\nsecond\nlast")

    chunks = list(islurp(str(p)))

    assert chunks == ["first\n", "second\n", "last"]


def test_islurp_explicit_linemode_and_string_linemode(tmp_path):
    """iter_by=LINEMODE and the literal string 'LINEMODE' (lines 23-24)
    behave identically."""
    p = tmp_path / "lines.txt"
    p.write_text("a\nb\nc\n")

    assert list(islurp(str(p), iter_by=LINEMODE)) == ["a\n", "b\n", "c\n"]
    # Covers the True branch of `if iter_by == 'LINEMODE'`.
    assert list(islurp(str(p), iter_by="LINEMODE")) == ["a\n", "b\n", "c\n"]


def test_islurp_iter_by_byte_chunks(tmp_path):
    """A numeric iter_by uses functools.partial(fh.read, iter_by)."""
    p = tmp_path / "chunks.txt"
    p.write_text("abcdefghij")

    chunks = list(islurp(str(p), iter_by=4))

    assert chunks == ["abcd", "efgh", "ij"]


def test_islurp_closes_opened_file(tmp_path, monkeypatch):
    """After the generator is exhausted, the finally block must have closed
    the file handle (lines 45-46)."""
    p = tmp_path / "close_check.txt"
    p.write_text("data\n")

    real_open = builtins.open
    opened = []

    def tracking_open(file, mode="r", *args, **kwargs):
        fh = real_open(file, mode, *args, **kwargs)
        opened.append(fh)
        return fh

    monkeypatch.setattr(builtins, "open", tracking_open)

    assert list(islurp(str(p))) == ["data\n"]
    assert len(opened) == 1
    assert opened[0].closed


def test_islurp_missing_file_raises_without_close(tmp_path):
    """If open() fails, the OSError propagates and the finally block sees
    fh is None, so the `if fh and ...` guard short-circuits (no close)."""
    missing = tmp_path / "does-not-exist.txt"

    with pytest.raises(OSError):
        list(islurp(str(missing)))


def test_islurp_expanduser_and_expandvars(tmp_path, monkeypatch):
    """expanduser/expandvars rewrite the path before opening (lines 31-34)."""
    target = tmp_path / "expanded.txt"
    target.write_text("expanded content\n")

    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))  # Windows
    monkeypatch.setenv("PYTUTILS_ISLURP_DIR", str(tmp_path))

    assert list(islurp("~/expanded.txt")) == ["expanded content\n"]
    assert list(islurp("$PYTUTILS_ISLURP_DIR/expanded.txt")) == ["expanded content\n"]


def test_islurp_expansion_disabled(tmp_path, monkeypatch):
    """expanduser=False / expandvars=False leave the filename untouched:
    literal '~' and '$VAR' paths are opened as-is."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("PYTUTILS_SHOULD_NOT_EXPAND", "elsewhere")

    # Files that path expansion would hijack if the flags were True.
    tilde_dir = tmp_path / "~"
    tilde_dir.mkdir()
    (tilde_dir / "inner.txt").write_text("literal tilde\n")
    (tmp_path / "$PYTUTILS_SHOULD_NOT_EXPAND.txt").write_text("literal dollar\n")

    assert list(islurp("~/inner.txt", expanduser=False, expandvars=False)) == [
        "literal tilde\n"
    ]
    assert list(islurp("$PYTUTILS_SHOULD_NOT_EXPAND.txt", expandvars=False)) == [
        "literal dollar\n"
    ]


def test_islurp_dash_with_allow_stdin_false_reads_literal_file(tmp_path, monkeypatch):
    """filename='-' with allow_stdin=False short-circuits the stdin branch
    and opens a literal file named '-' instead."""
    dash = tmp_path / "-"
    dash.write_text("dash file content\n")
    monkeypatch.chdir(tmp_path)

    assert list(islurp("-", allow_stdin=False)) == ["dash file content\n"]


def test_islurp_stdin_selection(monkeypatch, tmp_path):
    """
    filename='-' with allow_stdin=True selects sys.stdin (lines 28-29).

    NOTE: the current implementation never assigns ``fh_next`` on the stdin
    path, so the first ``next()`` raises NameError. This test documents that
    behavior while executing the stdin-selection lines and the
    ``fh != sys.stdin`` guard in the finally block (stdin is left open).
    """
    fake_stdin = io.StringIO("stdin line 1\nstdin line 2\n")
    monkeypatch.setattr(sys, "stdin", fake_stdin)
    # Ensure no literal '-' file exists that the else-branch could open;
    # a NameError therefore proves the stdin branch (lines 28-29) ran.
    monkeypatch.chdir(tmp_path)

    gen = islurp("-")
    with pytest.raises(NameError):
        next(gen)

    # finally-block guard: fh is sys.stdin, so it must NOT be closed.
    assert not fake_stdin.closed
