# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

from pytutils.files import burp


def test_burp_writes_to_stdout(capsys):
    burp("-", "stdout contents")

    captured = capsys.readouterr()
    assert captured.out == "stdout contents"
    assert captured.err == ""


def test_burp_expands_filename_and_writes_file(tmp_path, monkeypatch):
    target = tmp_path / "expanded.txt"
    calls = []

    def fake_expanduser(filename):
        calls.append(("expanduser", filename))
        return "$BURP_TARGET"

    def fake_expandvars(filename):
        calls.append(("expandvars", filename))
        return str(target)

    monkeypatch.setattr("pytutils.files.os.path.expanduser", fake_expanduser)
    monkeypatch.setattr("pytutils.files.os.path.expandvars", fake_expandvars)

    burp("~/input.txt", "file contents")

    assert calls == [
        ("expanduser", "~/input.txt"),
        ("expandvars", "$BURP_TARGET"),
    ]
    assert target.read_text() == "file contents"


def test_burp_can_disable_stdout_and_filename_expansion(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    burp(
        "-",
        "literal filename contents",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    assert (tmp_path / "-").read_text() == "literal filename contents"
