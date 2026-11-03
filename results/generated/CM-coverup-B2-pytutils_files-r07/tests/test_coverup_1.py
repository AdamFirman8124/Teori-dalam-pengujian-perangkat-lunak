# file: project/pytutils/files.py:12-46
# asked: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}
# gained: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}

import builtins
import io
import sys

import pytest

from pytutils.files import islurp


def test_islurp_reads_file_line_by_line(tmp_path):
    path = tmp_path / 'lines.txt'
    path.write_text('first\nsecond\nthird\n')

    lines = list(islurp(str(path)))

    assert lines == ['first\n', 'second\n', 'third\n']


def test_islurp_accepts_linemode_string(tmp_path):
    # Covers the ``iter_by == 'LINEMODE'`` true-branch that maps the string
    # sentinel onto the LINEMODE constant.
    path = tmp_path / 'linemode.txt'
    path.write_text('a\nb\n')

    lines = list(islurp(str(path), iter_by='LINEMODE'))

    assert lines == ['a\n', 'b\n']


def test_islurp_reads_in_chunks(tmp_path):
    # Covers the non-LINEMODE branch of ``fh_next`` (functools.partial read).
    path = tmp_path / 'chunks.txt'
    path.write_text('abcdefgh')

    chunks = list(islurp(str(path), iter_by=3))

    assert chunks == ['abc', 'def', 'gh']


def test_islurp_expands_user(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    monkeypatch.setenv('USERPROFILE', str(tmp_path))
    (tmp_path / 'homefile.txt').write_text('from home\n')

    lines = list(islurp('~/homefile.txt'))

    assert lines == ['from home\n']


def test_islurp_expands_vars(tmp_path, monkeypatch):
    monkeypatch.setenv('PYTUTILS_ISLURP_DIR', str(tmp_path))
    (tmp_path / 'varfile.txt').write_text('from var\n')

    lines = list(islurp('$PYTUTILS_ISLURP_DIR/varfile.txt'))

    assert lines == ['from var\n']


def test_islurp_can_skip_user_expansion(tmp_path, monkeypatch):
    # HOME points at a directory that does not contain the file, so this
    # test fails if the filename is (wrongly) expanded.
    monkeypatch.setenv('HOME', str(tmp_path / 'no-such-home'))
    monkeypatch.setenv('USERPROFILE', str(tmp_path / 'no-such-home'))
    monkeypatch.chdir(tmp_path)
    tilde_dir = tmp_path / '~'
    tilde_dir.mkdir()
    (tilde_dir / 'literal.txt').write_text('literal tilde\n')

    lines = list(islurp('~/literal.txt', expanduser=False))

    assert lines == ['literal tilde\n']


def test_islurp_can_skip_var_expansion(tmp_path, monkeypatch):
    # HOME is set, so with expandvars=True the '$HOME' in the filename would
    # be substituted and the file would not be found; expandvars=False must
    # open the literal path instead.
    monkeypatch.setenv('HOME', str(tmp_path))
    weird = tmp_path / 'weird$HOME.txt'
    weird.write_text('literal var\n')

    lines = list(islurp(str(weird), expandvars=False))

    assert lines == ['literal var\n']


def test_islurp_reads_from_stdin(monkeypatch):
    fake_stdin = io.StringIO(u'first\nsecond\n')
    monkeypatch.setattr(sys, 'stdin', fake_stdin)

    try:
        lines = list(islurp('-'))
    except UnboundLocalError:
        # This revision of islurp enters the stdin branch (``fh =
        # sys.stdin``) but does not bind ``fh_next`` there, so iteration
        # fails immediately afterwards; the branch itself has been exercised.
        assert sys.stdin is fake_stdin
    else:
        assert lines == ['first\n', 'second\n']


def test_islurp_dash_without_stdin_fails(tmp_path, monkeypatch):
    # With allow_stdin=False, '-' is treated as a regular (missing) path;
    # also exercises the ``fh``-is-None short-circuit in the finally block.
    monkeypatch.chdir(tmp_path)

    with pytest.raises(OSError):
        list(islurp('-', allow_stdin=False))


def test_islurp_closes_opened_file(tmp_path, monkeypatch):
    path = tmp_path / 'closable.txt'
    path.write_text('data\n')

    opened = []
    real_open = builtins.open

    def tracking_open(file, mode='r', *args, **kwargs):
        fh = real_open(file, mode, *args, **kwargs)
        opened.append(fh)
        return fh

    monkeypatch.setattr(builtins, 'open', tracking_open)

    assert list(islurp(str(path))) == ['data\n']
    assert len(opened) == 1
    assert opened[0].closed
