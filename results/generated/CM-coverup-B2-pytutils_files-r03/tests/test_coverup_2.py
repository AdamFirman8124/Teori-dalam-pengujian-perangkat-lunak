# file: project/pytutils/files.py:55-68
# asked: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}
# gained: {"lines": [59, 60, 62, 63, 64, 65, 67, 68], "branches": [[59, 60], [59, 62], [62, 63], [62, 64], [64, 65], [64, 67]]}

from pytutils.files import burp


def test_burp_writes_to_stdout(capsys):
    burp("-", "stdout contents")

    captured = capsys.readouterr()
    assert captured.out == "stdout contents"


def test_burp_expands_user_and_environment_variables(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("BURP_FILENAME", "expanded.txt")

    burp("~/$BURP_FILENAME", "expanded contents")

    output_file = tmp_path / "expanded.txt"
    assert output_file.read_text() == "expanded contents"


def test_burp_can_disable_stdout_and_path_expansion(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    def unexpected_expansion(_filename):
        raise AssertionError("Path expansion must be disabled")

    monkeypatch.setattr("pytutils.files.os.path.expanduser", unexpected_expansion)
    monkeypatch.setattr("pytutils.files.os.path.expandvars", unexpected_expansion)

    burp(
        "-",
        "file contents",
        allow_stdout=False,
        expanduser=False,
        expandvars=False,
    )

    assert (tmp_path / "-").read_text() == "file contents"
