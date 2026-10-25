# file: project/pytutils/files.py:12-46
# asked: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}
# gained: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}

import builtins
import io
import sys

import pytest

from pytutils import files as files_module
from pytutils.files import LINEMODE, islurp


@pytest.fixture
def sample_file(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("alpha\nbeta\ngamma\n")
    return path


def test_islurp_reads_lines_by_default(sample_file):
    assert list(islurp(str(sample_file))) == ["alpha\n", "beta\n", "gamma\n"]


def test_islurp_accepts_linemode_string(sample_file):
    # covers: if iter_by == 'LINEMODE': iter_by = LINEMODE
    assert list(islurp(str(sample_file), iter_by="LINEMODE")) == [
        "alpha\n",
        "beta\n",
        "gamma\n",
    ]


def test_islurp_reads_fixed_size_chunks(sample_file):
    chunks = list(islurp(str(sample_file), iter_by=4))
    assert chunks == ["alph", "a\nbe", "ta\ng", "amma", "\n"]
    assert "".join(chunks) == sample_file.read_text()


def test_islurp_empty_file_yields_nothing(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("")
    assert list(islurp(str(path))) == []


def test_islurp_expands_user(monkeypatch, tmp_path):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    (tmp_path / "homefile.txt").write_text("home\n")
    assert list(islurp("~/homefile.txt")) == ["home\n"]


def test_islurp_expands_vars(monkeypatch, tmp_path):
    monkeypatch.setenv("ISLURP_DIR", str(tmp_path))
    (tmp_path / "envfile.txt").write_text("env\n")
    assert list(islurp("$ISLURP_DIR/envfile.txt")) == ["env\n"]


def test_islurp_skips_expansion_when_disabled(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("ISLURP_DIR", str(tmp_path))
    (tmp_path / "$ISLURP_DIR").write_text("literal-var\n")
    (tmp_path / "~literal.txt").write_text("literal-user\n")

    assert list(islurp("$ISLURP_DIR", expandvars=False)) == ["literal-var\n"]
    assert list(islurp("~literal.txt", expanduser=False)) == ["literal-user\n"]


def test_islurp_reads_stdin(monkeypatch):
    fake_stdin = io.StringIO("one\ntwo\n")
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    gen = islurp("-")
    # fh_next is never bound on the stdin path, so iteration raises.
    with pytest.raises(UnboundLocalError):
        next(gen)
    # finally block must not close sys.stdin
    assert not fake_stdin.closed


def test_islurp_stdin_disallowed_treats_dash_as_filename(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(FileNotFoundError):
        list(islurp("-", allow_stdin=False))
    assert not (tmp_path / "-").exists()


def test_islurp_closes_file_after_exhaustion(monkeypatch, sample_file):
    opened = []
    real_open = builtins.open

    def recording_open(*args, **kwargs):
        fh = real_open(*args, **kwargs)
        opened.append(fh)
        return fh

    monkeypatch.setattr(files_module, "open", recording_open, raising=False)

    assert list(islurp(str(sample_file))) == ["alpha\n", "beta\n", "gamma\n"]
    assert len(opened) == 1
    assert opened[0].closed


def test_islurp_closes_file_when_generator_closed_early(monkeypatch, sample_file):
    opened = []
    real_open = builtins.open

    def recording_open(*args, **kwargs):
        fh = real_open(*args, **kwargs)
        opened.append(fh)
        return fh

    monkeypatch.setattr(files_module, "open", recording_open, raising=False)

    gen = islurp(str(sample_file))
    assert next(gen) == "alpha\n"
    assert not opened[0].closed
    gen.close()
    assert opened[0].closed
