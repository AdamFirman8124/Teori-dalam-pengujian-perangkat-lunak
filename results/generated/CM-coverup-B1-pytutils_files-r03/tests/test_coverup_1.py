# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os

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


def test_burp_stdout_disallowed_writes_file(tmp_path, monkeypatch, capsys):
    """filename == '-' with allow_stdout=False falls through to file write."""
    monkeypatch.chdir(tmp_path)
    burp('-', 'to file', allow_stdout=False)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert (tmp_path / '-').read_text() == 'to file'


def test_burp_writes_file_with_expansion(tmp_path, monkeypatch):
    """Default expanduser/expandvars expand ~ and $VAR in filename."""
    fake_home = tmp_path / 'home'
    fake_home.mkdir()
    monkeypatch.setenv('HOME', str(fake_home))
    monkeypatch.setenv('BURP_TEST_VAR', str(tmp_path))

    # expanduser branch (line 63)
    burp('~/burp_user.txt', 'user content')
    assert (fake_home / 'burp_user.txt').read_text() == 'user content'

    # expandvars branch (line 65)
    burp('$BURP_TEST_VAR/burp_vars.txt', 'var content')
    assert (tmp_path / 'burp_vars.txt').read_text() == 'var content'


def test_burp_no_expansion(tmp_path, monkeypatch):
    """expanduser=False and expandvars=False skip the expansion branches."""
    fake_home = tmp_path / 'home'
    fake_home.mkdir()
    monkeypatch.setenv('HOME', str(fake_home))
    monkeypatch.setenv('BURP_TEST_VAR', str(tmp_path))
    monkeypatch.chdir(tmp_path)

    # A literal '~' directory and a literal '$BURP_TEST_VAR' directory
    tilde_dir = tmp_path / '~'
    tilde_dir.mkdir()
    dollar_dir = tmp_path / '$BURP_TEST_VAR'
    dollar_dir.mkdir()

    burp('~/burp_nouser.txt', 'no user expansion', expanduser=False)
    assert (tilde_dir / 'burp_nouser.txt').read_text() == 'no user expansion'
    assert not (fake_home / 'burp_nouser.txt').exists()

    burp('$BURP_TEST_VAR/burp_novars.txt', 'no var expansion', expandvars=False)
    assert (dollar_dir / 'burp_novars.txt').read_text() == 'no var expansion'
    assert not (tmp_path / 'burp_novars.txt').exists()


def test_burp_append_mode(tmp_path):
    """mode is passed through to open()."""
    target = tmp_path / 'append.txt'
    burp(str(target), 'first')
    burp(str(target), ' second', mode='a')
    assert target.read_text() == 'first second'
