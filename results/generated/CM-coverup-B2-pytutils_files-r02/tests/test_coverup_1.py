# file: project/pytutils/files.py:12-46
# asked: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}
# gained: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}

import io
import os
import sys
import pytest
from pytutils.files import islurp, LINEMODE


def test_islurp_line_mode_default(tmp_path):
    p = tmp_path / "lines.txt"
    p.write_text("line1\nline2\nline3\n")
    result = list(islurp(str(p)))
    assert result == ["line1\n", "line2\n", "line3\n"]


def test_islurp_string_linemode_converted(tmp_path):
    p = tmp_path / "strmode.txt"
    p.write_text("a\nb\n")
    assert LINEMODE == 0
    result = list(islurp(str(p), iter_by='LINEMODE'))
    assert result == ["a\n", "b\n"]


def test_islurp_chunk_mode(tmp_path):
    p = tmp_path / "chunk.txt"
    p.write_text("abcdef")
    result = list(islurp(str(p), iter_by=2))
    assert result == ["ab", "cd", "ef"]


def test_islurp_no_expanduser_no_expandvars(tmp_path):
    p = tmp_path / "plain.txt"
    p.write_text("x\n")
    result = list(islurp(str(p), expanduser=False, expandvars=False))
    assert result == ["x\n"]


def test_islurp_expanduser(tmp_path, monkeypatch):
    target = tmp_path / "exp_user.txt"
    target.write_text("hello user\n")
    monkeypatch.setenv("HOME", str(tmp_path))
    # ensure expanduser path resolves to target
    result = list(islurp(os.path.join("~", "exp_user.txt")))
    assert result == ["hello user\n"]


def test_islurp_expandvars(tmp_path, monkeypatch):
    target = tmp_path / "exp_vars.txt"
    target.write_text("hello vars\n")
    monkeypatch.setenv("PYTUTILS_TEST_DIR", str(tmp_path))
    result = list(islurp(os.path.join("$PYTUTILS_TEST_DIR", "exp_vars.txt")))
    assert result == ["hello vars\n"]
    # also verify no-expand path does not resolve env var
    with pytest.raises(FileNotFoundError):
        list(islurp(os.path.join("$PYTUTILS_TEST_DIR", "exp_vars.txt"), expandvars=False))


def test_islurp_empty_file(tmp_path):
    p = tmp_path / "empty.txt"
    p.write_text("")
    result = list(islurp(str(p)))
    assert result == []


def test_islurp_dash_with_allow_stdin_false(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    dash = tmp_path / "-"
    dash.write_text("dash content\n")
    result = list(islurp("-", allow_stdin=False))
    assert result == ["dash content\n"]


def test_islurp_stdin_branch_does_not_close_stdin(monkeypatch):
    fake_stdin = io.StringIO("from stdin\n")
    monkeypatch.setattr(sys, "stdin", fake_stdin)
    # current implementation assigns fh=sys.stdin but never sets fh_next,
    # so consuming the generator raises UnboundLocalError
    with pytest.raises(UnboundLocalError):
        list(islurp("-"))
    # postcondition: stdin must not be closed by finally block
    assert fake_stdin.closed is False
    fake_stdin.close()
    assert fake_stdin.closed is True


def test_islurp_missing_file_raises_and_cleans_up(tmp_path):
    missing = tmp_path / "does-not-exist.txt"
    assert not os.path.exists(str(missing))
    with pytest.raises(FileNotFoundError):
        list(islurp(str(missing)))
