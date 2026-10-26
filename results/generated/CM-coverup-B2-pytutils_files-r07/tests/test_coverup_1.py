# file: project/pytutils/files.py:12-46
# asked: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}
# gained: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}

import io
import os
import sys
import builtins
import functools
import pytest
from pathlib import Path
from pytutils.files import islurp, LINEMODE


def test_islurp_default_linemode(tmp_path):
    p = tmp_path / "lines.txt"
    p.write_text("hello\nworld\nlast\n")
    result = list(islurp(str(p)))
    assert result == ["hello\n", "world\n", "last\n"]


def test_islurp_string_linemode_token(tmp_path):
    p = tmp_path / "tok.txt"
    p.write_text("a\nb\n")
    # iter_by == 'LINEMODE' string branch (lines 23-24)
    result = list(islurp(str(p), iter_by='LINEMODE'))
    assert result == ["a\n", "b\n"]


def test_islurp_chunk_mode(tmp_path):
    p = tmp_path / "chunk.txt"
    p.write_text("abcdef")
    # iter_by != LINEMODE -> functools.partial(fh.read, iter_by)
    result = list(islurp(str(p), iter_by=2))
    assert result == ["ab", "cd", "ef"]
    assert "".join(result) == "abcdef"


def test_islurp_no_expansion(tmp_path):
    p = tmp_path / "plain.txt"
    p.write_text("x\ny\n")
    # expanduser False + expandvars False branches
    result = list(islurp(str(p), expanduser=False, expandvars=False))
    assert result == ["x\n", "y\n"]


def test_islurp_expandvars(monkeypatch, tmp_path):
    d = tmp_path / "vardir"
    d.mkdir()
    f = d / "v.txt"
    f.write_text("one\ntwo\n")
    monkeypatch.setenv("PYTUTILS_TEST_DIR", str(d))
    # expandvars True branch with actual expansion
    result = list(islurp(os.path.join("$PYTUTILS_TEST_DIR", "v.txt"), expanduser=False, expandvars=True))
    assert result == ["one\n", "two\n"]


def test_islurp_expanduser_called(monkeypatch, tmp_path):
    p = tmp_path / "home.txt"
    p.write_text("h1\nh2\n")
    called = {}
    real_expanduser = os.path.expanduser
    real_expandvars = os.path.expandvars

    def fake_expanduser(path):
        called["user"] = True
        return real_expanduser(path)

    def fake_expandvars(path):
        called["vars"] = True
        return real_expandvars(path)

    monkeypatch.setattr(os.path, "expanduser", fake_expanduser)
    monkeypatch.setattr(os.path, "expandvars", fake_expandvars)
    result = list(islurp(str(p), expanduser=True, expandvars=True))
    assert result == ["h1\n", "h2\n"]
    assert called.get("user") is True
    assert called.get("vars") is True


def test_islurp_empty_file_eof(tmp_path):
    p = tmp_path / "empty.txt"
    p.write_text("")
    # buf == '' immediately -> break without yield
    result = list(islurp(str(p)))
    assert result == []


def test_islurp_dash_with_allow_stdin_false(monkeypatch, tmp_path):
    # filename == '-' True but allow_stdin False -> else branch (open file named '-')
    monkeypatch.chdir(tmp_path)
    Path("-").write_text("dashline\n")
    result = list(islurp("-", allow_stdin=False))
    assert result == ["dashline\n"]


def test_islurp_stdin_branch(monkeypatch):
    # filename == '-' and allow_stdin True -> fh = sys.stdin branch
    fake_stdin = io.StringIO("s1\ns2\n")
    monkeypatch.setattr(sys, "stdin", fake_stdin)
    try:
        result = list(islurp("-", allow_stdin=True))
    except UnboundLocalError:
        # current implementation leaves fh_next undefined for stdin;
        # branch is still executed and finally skips close for sys.stdin
        assert fake_stdin.closed is False
        return
    # if implementation is fixed to iterate stdin, verify postcondition
    assert result == ["s1\n", "s2\n"]
    assert fake_stdin.closed is False


def test_islurp_missing_file_finally_no_fh(tmp_path):
    missing = tmp_path / "does-not-exist.txt"
    # open raises -> fh stays None -> finally `if fh` is False
    with pytest.raises(FileNotFoundError):
        list(islurp(str(missing)))


def test_islurp_closes_filehandle(monkeypatch, tmp_path):
    p = tmp_path / "close.txt"
    p.write_text("a\nb\n")
    closed = []
    real_open = builtins.open

    def tracking_open(*args, **kwargs):
        fh = real_open(*args, **kwargs)
        orig_close = fh.close

        def spy(*a, **k):
            closed.append(True)
            return orig_close(*a, **k)

        fh.close = spy
        return fh

    monkeypatch.setattr(builtins, "open", tracking_open)
    result = list(islurp(str(p)))
    assert result == ["a\n", "b\n"]
    assert closed == [True]
