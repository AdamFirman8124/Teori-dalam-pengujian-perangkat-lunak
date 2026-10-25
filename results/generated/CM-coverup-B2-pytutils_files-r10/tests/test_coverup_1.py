# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import os

from pytutils.files import burp


def test_burp_writes_to_stdout(capsys):
    burp("-", "hello\n")

    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == ""


def test_burp_expands_user_and_variables_before_writing(tmp_path, monkeypatch):
    destination = tmp_path / "output.txt"
    calls = []

    def fake_expanduser(filename):
        calls.append(("expanduser", filename))
        return "$BURP_TARGET"

    def fake_expandvars(filename):
        calls.append(("expandvars", filename))
        return os.fspath(destination)

    monkeypatch.setattr("pytutils.files.os.path.expanduser", fake_expanduser)
    monkeypatch.setattr("pytutils.files.os.path.expandvars", fake_expandvars)

    burp("~/output.txt", "file contents")

    assert calls == [
        ("expanduser", "~/output.txt"),
        ("expandvars", "$BURP_TARGET"),
    ]
    assert destination.read_text() == "file contents"


def test_burp_can_disable_stdout_and_filename_expansion(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    def unexpected_expansion(filename):
        raise AssertionError(f"Unexpected filename expansion: {filename}")

    monkeypatch.setattr("pytutils.files.os.path.expanduser", unexpected_expansion)
    monkeypatch.setattr("pytutils.files.os.path.expandvars", unexpected_expansion)

    burp(
        "-",
        "written to a file",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    assert (tmp_path / "-").read_text() == "written to a file"
