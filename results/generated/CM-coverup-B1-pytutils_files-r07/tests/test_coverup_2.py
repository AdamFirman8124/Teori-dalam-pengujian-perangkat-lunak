# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

from pytutils import files


def test_burp_writes_to_stdout_without_expanding(capsys, monkeypatch):
    def fail_if_called(filename):
        raise AssertionError("filename expansion should not occur for stdout")

    monkeypatch.setattr(files.os.path, "expanduser", fail_if_called)
    monkeypatch.setattr(files.os.path, "expandvars", fail_if_called)

    files.burp("-", "stdout contents")

    captured = capsys.readouterr()
    assert captured.out == "stdout contents"
    assert captured.err == ""


def test_burp_expands_user_and_environment_variables(tmp_path, monkeypatch):
    target = tmp_path / "expanded.txt"
    calls = []

    def fake_expanduser(filename):
        calls.append(("expanduser", filename))
        return "$BURP_TARGET"

    def fake_expandvars(filename):
        calls.append(("expandvars", filename))
        return str(target)

    monkeypatch.setattr(files.os.path, "expanduser", fake_expanduser)
    monkeypatch.setattr(files.os.path, "expandvars", fake_expandvars)

    files.burp("~/original.txt", "file contents")

    assert calls == [
        ("expanduser", "~/original.txt"),
        ("expandvars", "$BURP_TARGET"),
    ]
    assert target.read_text() == "file contents"


def test_burp_treats_dash_as_filename_when_stdout_is_disabled(
    tmp_path, monkeypatch, capsys
):
    def fail_if_called(filename):
        raise AssertionError("disabled filename expansion should not occur")

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(files.os.path, "expanduser", fail_if_called)
    monkeypatch.setattr(files.os.path, "expandvars", fail_if_called)

    files.burp(
        "-",
        "literal dash file",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
    assert (tmp_path / "-").read_text() == "literal dash file"
