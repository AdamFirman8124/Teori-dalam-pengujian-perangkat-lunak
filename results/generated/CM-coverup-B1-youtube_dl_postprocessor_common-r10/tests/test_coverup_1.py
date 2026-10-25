# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    def __init__(self):
        self.warnings = []

    def report_warning(self, msg):
        self.warnings.append(msg)


@pytest.fixture
def pp():
    return PostProcessor(FakeDownloader())


def test_try_utime_success(pp, tmp_path, monkeypatch):
    """Lines 59-61: os.utime is called with encoded path and (atime, mtime)."""
    f = tmp_path / "video.mp4"
    f.write_bytes(b"data")
    path = str(f)
    old_atime, old_mtime = os.stat(path).st_atime, os.stat(path).st_mtime

    calls = {}

    def fake_utime(filename, times):
        calls["filename"] = filename
        calls["times"] = times

    monkeypatch.setattr(
        "youtube_dl.postprocessor.common.os.utime", fake_utime
    )

    pp.try_utime(path, 1000, 2000)

    assert calls["filename"] == path.encode("utf-8") if isinstance(
        __import__("youtube_dl.utils", fromlist=["encodeFilename"]).encodeFilename(path),
        bytes,
    ) else calls["filename"] == path
    assert calls["times"] == (1000, 2000)
    # No warning reported on success
    assert pp._downloader.warnings == []
    # File untouched since os.utime was mocked
    st = os.stat(path)
    assert (st.st_atime, st.st_mtime) == (old_atime, old_mtime)


def test_try_utime_real_file(pp, tmp_path):
    """Success path with the real os.utime: timestamps actually change."""
    f = tmp_path / "video.mp4"
    f.write_bytes(b"data")
    path = str(f)

    pp.try_utime(path, 1000, 2000)

    st = os.stat(path)
    assert st.st_atime == 1000
    assert st.st_mtime == 2000
    assert pp._downloader.warnings == []


def test_try_utime_failure_reports_warning(pp, monkeypatch):
    """Lines 61-62: exception from os.utime triggers report_warning(errnote)."""
    def failing_utime(filename, times):
        raise OSError("no such file")

    monkeypatch.setattr(
        "youtube_dl.postprocessor.common.os.utime", failing_utime
    )

    # Default errnote
    pp.try_utime("nonexistent_file.mp4", 1000, 2000)
    assert pp._downloader.warnings == ["Cannot update utime of file"]

    # Custom errnote
    pp._downloader.warnings = []
    pp.try_utime("nonexistent_file.mp4", 1000, 2000, errnote="custom failure")
    assert pp._downloader.warnings == ["custom failure"]
