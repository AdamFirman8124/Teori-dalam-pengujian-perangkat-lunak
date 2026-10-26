# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os
import sys

import pytest

from pytutils.files import burp


def test_burp_stdout(capsys):
    """filename == '-' with allow_stdout=True writes to stdout (lines 59-60)."""
    burp('-', 'to stdout')
    captured = capsys.readouterr()
    assert captured.out == 'to stdout'


def test_burp_stdout_disabled(tmp_path, monkeypatch, capsys):
    """filename == '-' with allow_stdout=False writes to a file named '-' (else branch)."""
    monkeypatch.chdir(tmp_path)
    burp('-', 'to file', allow_stdout=False)
    captured = capsys.readouterr()
    assert captured.out == ''
    target = tmp_path / '-'
    assert target.is_file()
    assert target.read_text() == 'to file'


def test_burp_writes_file_with_expansion(tmp_path, monkeypatch):
    """Default expanduser/expandvars expand ~ and $VAR (lines 62-65, 67-68)."""
    monkeypatch.setenv('HOME', str(tmp_path))
    monkeypatch.setenv('BURP_TEST_VAR', 'expanded')
    expected_dir = tmp_path / 'burpdir' / 'expanded'
    expected_dir.mkdir(parents=True)
    burp('~/burpdir/$BURP_TEST_VAR/out.txt', 'expanded contents')
    expected = expected_dir / 'out.txt'
    assert expected.is_file()
    assert expected.read_text() == 'expanded contents'


def test_burp_no_expansion(tmp_path):
    """expanduser=False and expandvars=False leave the filename untouched."""
    target = tmp_path / '$NOVAR' / 'out.txt'
    target.parent.mkdir()
    burp(str(target), 'raw contents', expanduser=False, expandvars=False)
    assert target.read_text() == 'raw contents'


def test_burp_append_mode(tmp_path):
    """mode is forwarded to open (e.g. append)."""
    target = tmp_path / 'out.txt'
    burp(str(target), 'first\n')
    burp(str(target), 'second\n', mode='a')
    assert target.read_text() == 'first\nsecond\n'
