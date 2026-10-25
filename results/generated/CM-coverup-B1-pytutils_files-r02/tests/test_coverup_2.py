# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import io
import sys

import pytutils.files as files


def test_burp_writes_to_stdout(monkeypatch):
    stdout = io.StringIO()
    monkeypatch.setattr(sys, "stdout", stdout)

    files.burp("-", "hello")

    assert stdout.getvalue() == "hello"


def test_burp_expands_filename_and_writes_file(tmp_path, monkeypatch):
    destination = tmp_path / "expanded.txt"
    calls = []

    def fake_expanduser(filename):
        calls.append(("expanduser", filename))
        return "user-expanded"

    def fake_expandvars(filename):
        calls.append(("expandvars", filename))
        return str(destination)

    monkeypatch.setattr(files.os.path, "expanduser", fake_expanduser)
    monkeypatch.setattr(files.os.path, "expandvars", fake_expandvars)

    files.burp("~/file-$NAME", "expanded contents")

    assert calls == [
        ("expanduser", "~/file-$NAME"),
        ("expandvars", "user-expanded"),
    ]
    assert destination.read_text() == "expanded contents"


def test_burp_can_disable_stdout_and_filename_expansion(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    files.burp(
        "-",
        "file contents",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    assert (tmp_path / "-").read_text() == "file contents"
