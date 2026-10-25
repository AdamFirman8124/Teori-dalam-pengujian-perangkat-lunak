# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

from pytutils import files


def test_burp_writes_to_stdout(capsys, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    files.burp("-", "stdout contents")

    captured = capsys.readouterr()
    assert captured.out == "stdout contents"
    assert captured.err == ""
    assert not (tmp_path / "-").exists()


def test_burp_expands_user_and_environment_paths(tmp_path, monkeypatch):
    output_file = tmp_path / "output.txt"
    calls = []

    def fake_expanduser(filename):
        calls.append(("expanduser", filename))
        return "$BURP_DIR/output.txt"

    def fake_expandvars(filename):
        calls.append(("expandvars", filename))
        return str(output_file)

    monkeypatch.setattr(files.os.path, "expanduser", fake_expanduser)
    monkeypatch.setattr(files.os.path, "expandvars", fake_expandvars)

    files.burp("~/output.txt", "expanded contents")

    assert calls == [
        ("expanduser", "~/output.txt"),
        ("expandvars", "$BURP_DIR/output.txt"),
    ]
    assert output_file.read_text() == "expanded contents"


def test_burp_treats_dash_as_filename_when_stdout_is_disallowed(
    capsys, tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)

    files.burp(
        "-",
        "file contents",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
    assert (tmp_path / "-").read_text() == "file contents"
