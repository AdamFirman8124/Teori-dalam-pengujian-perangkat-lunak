# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os
import sys

import pytest

from pytutils.files import burp


def test_burp_stdout(tmp_path, monkeypatch, capsys):
    """filename == '-' with allow_stdout=True writes to stdout."""
    monkeypatch.chdir(tmp_path)
    burp('-', 'hello stdout')
    captured = capsys.readouterr()
    assert captured.out == 'hello stdout'
    # No file named '-' should have been created
    assert not (tmp_path / '-').exists()


def test_burp_stdout_disabled(tmp_path, capsys):
    """filename == '-' with allow_stdout=False writes to a file named '-'."""
    target = tmp_path / '-'
    burp(str(target), 'to file', allow_stdout=False)
    assert target.read_text() == 'to file'
    assert capsys.readouterr().out == ''


def test_burp_expanduser(tmp_path, monkeypatch):
    """~ in filename is expanded via os.path.expanduser."""
    fake_home = tmp_path / 'home'
    fake_home.mkdir()
    monkeypatch.setenv('HOME', str(fake_home))
    burp('~/out.txt', 'home content')
    assert (fake_home / 'out.txt').read_text() == 'home content'


def test_burp_expandvars(tmp_path, monkeypatch):
    """$VAR in filename is expanded via os.path.expandvars."""
    monkeypatch.setenv('BURP_TEST_DIR', str(tmp_path))
    burp('$BURP_TEST_DIR/vars.txt', 'vars content')
    assert (tmp_path / 'vars.txt').read_text() == 'vars content'


def test_burp_no_expansion(tmp_path):
    """expanduser/expandvars disabled leaves the filename untouched."""
    target = tmp_path / '$NOVAR'
    burp(str(target), 'raw', expanduser=False, expandvars=False)
    assert target.read_text() == 'raw'


def test_burp_append_mode(tmp_path):
    """mode is forwarded to open()."""
    target = tmp_path / 'appended.txt'
    burp(str(target), 'first\n')
    burp(str(target), 'second\n', mode='a')
    assert target.read_text() == 'first\nsecond\n'
