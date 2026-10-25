# file: project/pytutils/files.py:12-46
# asked: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}
# gained: {"lines": [23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 45, 46], "branches": [[23, 24], [23, 26], [28, 29], [28, 31], [31, 32], [31, 33], [33, 34], [33, 36], [39, 40], [41, 42], [41, 43], [45, 0], [45, 46]]}

import builtins
import io
import os
import sys

import pytest

from pytutils.files import LINEMODE, islurp


def _write(tmp_path, name, content):
    path = tmp_path / name
    path.write_text(content)
    return path


def test_islurp_reads_lines(tmp_path):
    path = _write(tmp_path, 'lines.txt', 'a\nb\nc\n')
    assert list(islurp(str(path))) == ['a\n', 'b\n', 'c\n']


def test_islurp_string_linemode_is_converted(tmp_path):
    path = _write(tmp_path, 'lines.txt', 'x\ny\n')
    assert list(islurp(str(path), iter_by='LINEMODE')) == ['x\n', 'y\n']


def test_islurp_reads_chunks(tmp_path):
    path = _write(tmp_path, 'chunks.txt', 'abcdefghij')
    assert list(islurp(str(path), iter_by=4)) == ['abcd', 'efgh', 'ij']


def test_islurp_empty_file_yields_nothing(tmp_path):
    path = _write(tmp_path, 'empty.txt', '')
    assert list(islurp(str(path))) == []


def test_islurp_expands_user(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    _write(tmp_path, 'home.txt', 'hi\n')
    assert list(islurp('~/home.txt')) == ['hi\n']


def test_islurp_expands_env_vars(tmp_path, monkeypatch):
    monkeypatch.setenv('ISLURP_DIR', str(tmp_path))
    _write(tmp_path, 'var.txt', 'yo\n')
    assert list(islurp(os.path.join('$ISLURP_DIR', 'var.txt'))) == ['yo\n']


def test_islurp_without_expansion(tmp_path):
    path = _write(tmp_path, 'plain.txt', 'z\n')
    assert list(islurp(str(path), expanduser=False, expandvars=False)) == ['z\n']


def test_islurp_closes_file_when_exhausted(tmp_path, monkeypatch):
    path = _write(tmp_path, 'close.txt', 'a\nb\n')
    opened = []
    real_open = builtins.open

    def tracking_open(*args, **kwargs):
        fh = real_open(*args, **kwargs)
        opened.append(fh)
        return fh

    monkeypatch.setattr(builtins, 'open', tracking_open)

    assert list(islurp(str(path))) == ['a\n', 'b\n']
    assert len(opened) == 1
    assert opened[0].closed


def test_islurp_closes_file_on_generator_close(tmp_path, monkeypatch):
    path = _write(tmp_path, 'close_early.txt', 'a\nb\n')
    opened = []
    real_open = builtins.open

    def tracking_open(*args, **kwargs):
        fh = real_open(*args, **kwargs)
        opened.append(fh)
        return fh

    monkeypatch.setattr(builtins, 'open', tracking_open)

    gen = islurp(str(path))
    assert next(gen) == 'a\n'
    assert not opened[0].closed
    gen.close()
    assert opened[0].closed


def test_islurp_stdin_path_raises_unbound_local(monkeypatch):
    fake_stdin = io.StringIO('a\nb\n')
    monkeypatch.setattr(sys, 'stdin', fake_stdin)

    with pytest.raises(UnboundLocalError):
        list(islurp('-'))

    # sys.stdin must never be closed by islurp
    assert not fake_stdin.closed


def test_islurp_dash_without_stdin_opens_literal_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / '-').write_text('dash\n')
    assert list(islurp('-', allow_stdin=False)) == ['dash\n']


def test_islurp_missing_file_raises_and_skips_close(tmp_path):
    missing = tmp_path / 'nope.txt'
    with pytest.raises(FileNotFoundError):
        list(islurp(str(missing)))
    assert not missing.exists()
