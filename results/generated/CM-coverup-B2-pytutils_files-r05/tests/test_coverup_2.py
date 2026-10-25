# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os
import sys
from pytutils.files import burp


def test_burp_writes_to_stdout(capsys):
    burp('-', 'hello stdout')
    captured = capsys.readouterr()
    assert captured.out == 'hello stdout'


def test_burp_dash_with_allow_stdout_true_writes_stdout(capsys, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    burp('-', 'explicit stdout', allow_stdout=True)
    captured = capsys.readouterr()
    assert captured.out == 'explicit stdout'
    assert not (tmp_path / '-').exists()


def test_burp_dash_with_allow_stdout_false_writes_file(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    burp('-', 'dash content', allow_stdout=False)
    captured = capsys.readouterr()
    assert captured.out == ''
    dash_file = tmp_path / '-'
    assert dash_file.is_file()
    assert dash_file.read_text() == 'dash content'


def test_burp_writes_file_default_expansion(tmp_path):
    target = tmp_path / 'out.txt'
    burp(str(target), 'file content')
    assert target.is_file()
    assert target.read_text() == 'file content'


def test_burp_no_expansion(tmp_path, monkeypatch):
    target = tmp_path / 'noexpand.txt'
    calls = []

    def fake_expanduser(p):
        calls.append(('expanduser', p))
        return p

    def fake_expandvars(p):
        calls.append(('expandvars', p))
        return p

    monkeypatch.setattr(os.path, 'expanduser', fake_expanduser)
    monkeypatch.setattr(os.path, 'expandvars', fake_expandvars)
    burp(str(target), 'no expand', expanduser=False, expandvars=False)
    assert calls == []
    assert target.read_text() == 'no expand'


def test_burp_expanduser_only(tmp_path, monkeypatch):
    target = tmp_path / 'user_only.txt'
    seen = {}

    def fake_expanduser(p):
        seen['called'] = True
        return str(target)

    def fake_expandvars(p):
        seen['expandvars_called'] = True
        return p

    monkeypatch.setattr(os.path, 'expanduser', fake_expanduser)
    monkeypatch.setattr(os.path, 'expandvars', fake_expandvars)
    burp('~/fake_user.txt', 'user only', expanduser=True, expandvars=False)
    assert seen.get('called') is True
    assert 'expandvars_called' not in seen
    assert target.read_text() == 'user only'


def test_burp_expandvars_only(tmp_path, monkeypatch):
    target = tmp_path / 'vars_only.txt'
    seen = {}

    def fake_expanduser(p):
        seen['expanduser_called'] = True
        return p

    def fake_expandvars(p):
        seen['called'] = True
        return str(target)

    monkeypatch.setattr(os.path, 'expanduser', fake_expanduser)
    monkeypatch.setattr(os.path, 'expandvars', fake_expandvars)
    burp('$FAKE_VAR/fake.txt', 'vars only', expanduser=False, expandvars=True)
    assert 'expanduser_called' not in seen
    assert seen.get('called') is True
    assert target.read_text() == 'vars only'


def test_burp_expanduser_actually_expands(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    # ensure expandvars does not alter the path
    monkeypatch.setenv('PYTUTILS_BURP_TEST_UNUSED', 'unused')
    burp(os.path.join('~', 'expanded_user.txt'), 'user expanded', expanduser=True, expandvars=False)
    target = tmp_path / 'expanded_user.txt'
    assert target.is_file()
    assert target.read_text() == 'user expanded'


def test_burp_expandvars_actually_expands(tmp_path, monkeypatch):
    monkeypatch.setenv('PYTUTILS_BURP_DIR', str(tmp_path))
    burp(os.path.join('$PYTUTILS_BURP_DIR', 'expanded_vars.txt'), 'vars expanded', expanduser=False, expandvars=True)
    target = tmp_path / 'expanded_vars.txt'
    assert target.is_file()
    assert target.read_text() == 'vars expanded'
