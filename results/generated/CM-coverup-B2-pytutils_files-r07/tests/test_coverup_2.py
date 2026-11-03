# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os

import pytest

from pytutils.files import burp


def test_burp_writes_contents_to_file(tmp_path):
    """Covers the else branch and the open/write lines (67-68)."""
    target = tmp_path / "out.txt"
    burp(str(target), "hello world")
    assert target.is_file()
    assert target.read_text() == "hello world"


def test_burp_dash_writes_to_stdout(capsys):
    """Covers lines 59-60: filename '-' with allow_stdout=True."""
    burp("-", "stdout payload")
    captured = capsys.readouterr()
    assert captured.out == "stdout payload"
    assert captured.err == ""


def test_burp_dash_with_allow_stdout_false_writes_literal_file(tmp_path, monkeypatch):
    """Covers the False branch of 'filename == - and allow_stdout':
    a file literally named '-' must be created instead of touching stdout."""
    monkeypatch.chdir(tmp_path)
    burp("-", "literal dash", allow_stdout=False)
    dash_file = tmp_path / "-"
    assert dash_file.is_file()
    assert dash_file.read_text() == "literal dash"


def test_burp_expands_user(tmp_path, monkeypatch):
    """Covers lines 62-63: expanduser=True expands '~' via $HOME."""
    monkeypatch.setenv("HOME", str(tmp_path))
    burp("~/burp_expanduser_test.txt", "user expanded")
    expected = tmp_path / "burp_expanduser_test.txt"
    assert expected.is_file()
    assert expected.read_text() == "user expanded"


def test_burp_expands_vars(tmp_path, monkeypatch):
    """Covers lines 64-65: expandvars=True expands environment variables."""
    monkeypatch.setenv("PYTUTILS_BURP_TEST_DIR", str(tmp_path))
    burp("$PYTUTILS_BURP_TEST_DIR/burp_expandvars_test.txt", "vars expanded")
    expected = tmp_path / "burp_expandvars_test.txt"
    assert expected.is_file()
    assert expected.read_text() == "vars expanded"


@pytest.fixture()
def expansion_spies(monkeypatch):
    """Wrap os.path.expanduser/expandvars to count invocations."""
    calls = {"expanduser": 0, "expandvars": 0}
    real_expanduser = os.path.expanduser
    real_expandvars = os.path.expandvars

    def fake_expanduser(path):
        calls["expanduser"] += 1
        return real_expanduser(path)

    def fake_expandvars(path):
        calls["expandvars"] += 1
        return real_expandvars(path)

    monkeypatch.setattr(os.path, "expanduser", fake_expanduser)
    monkeypatch.setattr(os.path, "expandvars", fake_expandvars)
    return calls


def test_burp_skips_expansion_when_disabled(tmp_path, expansion_spies):
    """Covers the False branches of the expanduser/expandvars checks."""
    target = tmp_path / "no_expansion.txt"
    burp(str(target), "raw contents", expanduser=False, expandvars=False)
    assert expansion_spies == {"expanduser": 0, "expandvars": 0}
    assert target.read_text() == "raw contents"


def test_burp_applies_expansions_when_enabled(tmp_path, expansion_spies):
    """Sanity check that the spies see the expansions happen by default."""
    target = tmp_path / "with_expansion.txt"
    burp(str(target), "expanded contents")
    assert expansion_spies["expanduser"] >= 1
    assert expansion_spies["expandvars"] >= 1
    assert target.read_text() == "expanded contents"


def test_burp_append_mode(tmp_path):
    """Exercise the mode parameter end-to-end."""
    target = tmp_path / "append.txt"
    burp(str(target), "first\n")
    burp(str(target), "second\n", mode="a")
    assert target.read_text() == "first\nsecond\n"
