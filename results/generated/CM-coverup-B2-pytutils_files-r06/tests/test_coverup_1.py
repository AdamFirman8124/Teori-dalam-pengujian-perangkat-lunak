# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

import pytutils.files as files


def test_burp_writes_to_stdout(capsys, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    files.burp("-", "stdout contents")

    captured = capsys.readouterr()
    assert captured.out == "stdout contents"
    assert captured.err == ""
    assert not (tmp_path / "-").exists()


def test_burp_expands_user_and_environment_variables(tmp_path, monkeypatch):
    destination = tmp_path / "output.txt"
    calls = []

    def fake_expanduser(filename):
        calls.append(("expanduser", filename))
        return "$OUTPUT_FILE"

    def fake_expandvars(filename):
        calls.append(("expandvars", filename))
        return str(destination)

    monkeypatch.setattr(files.os.path, "expanduser", fake_expanduser)
    monkeypatch.setattr(files.os.path, "expandvars", fake_expandvars)

    files.burp("~/output.txt", "file contents")

    assert calls == [
        ("expanduser", "~/output.txt"),
        ("expandvars", "$OUTPUT_FILE"),
    ]
    assert destination.read_text() == "file contents"


def test_burp_treats_dash_as_filename_when_stdout_is_disallowed(
    tmp_path, monkeypatch, capsys
):
    monkeypatch.chdir(tmp_path)

    files.burp(
        "-",
        "dash file contents",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
    assert (tmp_path / "-").read_text() == "dash file contents"
