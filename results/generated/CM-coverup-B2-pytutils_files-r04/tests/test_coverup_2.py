# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os

from pytutils.files import burp


def test_burp_dash_writes_to_stdout(capsys):
    # Covers line 59 (condition True) and line 60.
    burp('-', 'hello stdout\n')
    captured = capsys.readouterr()
    assert captured.out == 'hello stdout\n'
    assert captured.err == ''


def test_burp_writes_contents_to_file(tmp_path):
    # Covers line 59 (condition False via filename != '-') and lines 67-68.
    target = tmp_path / 'out.txt'
    burp(str(target), 'file contents\n')
    assert target.is_file()
    assert target.read_text() == 'file contents\n'


def test_burp_dash_writes_file_when_stdout_not_allowed(tmp_path, monkeypatch, capsys):
    # Covers line 59 (condition False via allow_stdout=False) and lines 67-68.
    monkeypatch.chdir(tmp_path)
    burp('-', 'dash file contents\n', allow_stdout=False)
    captured = capsys.readouterr()
    assert captured.out == ''
    assert (tmp_path / '-').is_file()
    assert (tmp_path / '-').read_text() == 'dash file contents\n'


def test_burp_expands_user(tmp_path, monkeypatch):
    # Covers line 62 (True) and line 63.
    home = tmp_path / 'home'
    home.mkdir()
    monkeypatch.setenv('HOME', str(home))
    monkeypatch.setenv('USERPROFILE', str(home))
    burp(os.path.join('~', 'burped.txt'), 'expanded user\n', expanduser=True)
    assert (home / 'burped.txt').read_text() == 'expanded user\n'


def test_burp_skips_user_expansion(tmp_path, monkeypatch):
    # Covers line 62 (False branch); line 63 must not run.
    home = tmp_path / 'home'
    monkeypatch.setenv('HOME', str(home))
    monkeypatch.setenv('USERPROFILE', str(home))
    monkeypatch.chdir(tmp_path)
    (tmp_path / '~').mkdir()
    burp(os.path.join('~', 'burped.txt'), 'no user expansion\n', expanduser=False)
    assert (tmp_path / '~' / 'burped.txt').read_text() == 'no user expansion\n'
    assert not (home / 'burped.txt').exists()


def test_burp_expands_vars(tmp_path, monkeypatch):
    # Covers line 64 (True) and line 65.
    var_dir = tmp_path / 'vardir'
    var_dir.mkdir()
    monkeypatch.setenv('PYTUTILS_BURP_DIR', str(var_dir))
    burp(os.path.join('$PYTUTILS_BURP_DIR', 'burped.txt'), 'expanded var\n', expandvars=True)
    assert (var_dir / 'burped.txt').read_text() == 'expanded var\n'


def test_burp_skips_var_expansion(tmp_path, monkeypatch):
    # Covers line 64 (False branch); line 65 must not run.
    monkeypatch.setenv('PYTUTILS_BURP_DIR', str(tmp_path / 'vardir'))
    monkeypatch.chdir(tmp_path)
    (tmp_path / '$PYTUTILS_BURP_DIR').mkdir()
    burp(os.path.join('$PYTUTILS_BURP_DIR', 'burped.txt'), 'no var expansion\n', expandvars=False)
    assert (tmp_path / '$PYTUTILS_BURP_DIR' / 'burped.txt').read_text() == 'no var expansion\n'
    assert not (tmp_path / 'vardir').exists()


def test_burp_respects_mode(tmp_path):
    # Exercises lines 67-68 again, verifying the mode parameter is passed through.
    target = tmp_path / 'appended.txt'
    burp(str(target), 'first\n')
    burp(str(target), 'second\n', mode='a')
    assert target.read_text() == 'first\nsecond\n'
