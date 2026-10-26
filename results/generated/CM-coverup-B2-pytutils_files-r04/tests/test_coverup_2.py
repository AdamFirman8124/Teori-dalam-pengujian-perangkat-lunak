# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os
from pytutils.files import burp


def test_burp_stdout_allowed(capsys):
    burp('-', 'hello stdout')
    captured = capsys.readouterr()
    assert captured.out == 'hello stdout'


def test_burp_dash_with_allow_stdout_false_writes_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    burp('-', 'dash file contents', allow_stdout=False)
    assert (tmp_path / '-').is_file()
    assert (tmp_path / '-').read_text() == 'dash file contents'


def test_burp_writes_file_no_expansion(tmp_path):
    target = tmp_path / 'plain.txt'
    burp(str(target), 'plain contents', expanduser=False, expandvars=False)
    assert target.is_file()
    assert target.read_text() == 'plain contents'


def test_burp_expands_user_and_vars(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    monkeypatch.setenv('BURP_TEST_VAR', 'expanded_dir')
    nested = tmp_path / 'expanded_dir'
    nested.mkdir()
    burp('~/$BURP_TEST_VAR/out.txt', 'expanded contents')
    expected = nested / 'out.txt'
    assert expected.is_file()
    assert expected.read_text() == 'expanded contents'


def test_burp_expanduser_disabled(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv('HOME', str(tmp_path))
    tilde_dir = tmp_path / '~'
    tilde_dir.mkdir()
    burp('~/no_expand_user.txt', 'raw user', expanduser=False, expandvars=False)
    expected = tilde_dir / 'no_expand_user.txt'
    assert expected.is_file()
    assert expected.read_text() == 'raw user'


def test_burp_expandvars_disabled(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv('BURP_TEST_VAR2', 'should_not_expand')
    burp('$BURP_TEST_VAR2.txt', 'raw vars', expanduser=True, expandvars=False)
    expected = tmp_path / '$BURP_TEST_VAR2.txt'
    assert expected.is_file()
    assert expected.read_text() == 'raw vars'
