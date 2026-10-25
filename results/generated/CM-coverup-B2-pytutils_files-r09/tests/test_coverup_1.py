# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

from pytutils.files import burp


def test_burp_writes_to_stdout(capsys, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    burp("-", "stdout contents")

    assert capsys.readouterr().out == "stdout contents"
    assert not (tmp_path / "-").exists()


def test_burp_expands_user_and_environment_variables(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("PYTUTILS_BURP_FILE", "expanded.txt")

    burp("~/$PYTUTILS_BURP_FILE", "expanded contents")

    assert (tmp_path / "expanded.txt").read_text() == "expanded contents"


def test_burp_writes_dash_filename_when_stdout_is_disallowed(
    tmp_path, monkeypatch, capsys
):
    monkeypatch.chdir(tmp_path)

    burp(
        "-",
        "file contents",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    assert capsys.readouterr().out == ""
    assert (tmp_path / "-").read_text() == "file contents"
