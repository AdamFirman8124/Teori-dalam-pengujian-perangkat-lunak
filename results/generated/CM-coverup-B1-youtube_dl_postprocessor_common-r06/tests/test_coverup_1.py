# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os
from youtube_dl.postprocessor.common import PostProcessor


def test_try_utime_success_updates_file_times(tmp_path):
    class FakeDownloader:
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    f = tmp_path / "utime_success.txt"
    f.write_text("hello", encoding="utf-8")
    path = str(f)
    atime = 1000000000
    mtime = 1200000000

    pp.try_utime(path, atime, mtime)

    st = os.stat(path)
    assert int(st.st_atime) == atime
    assert int(st.st_mtime) == mtime
    assert downloader.warnings == []


def test_try_utime_failure_reports_default_warning(monkeypatch, tmp_path):
    class FakeDownloader:
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    path = str(tmp_path / "missing_default.txt")

    def fake_utime(p, times):
        raise OSError("mock utime failure")

    monkeypatch.setattr(os, "utime", fake_utime)

    pp.try_utime(path, 1000000000, 1000000000)

    assert downloader.warnings == ["Cannot update utime of file"]


def test_try_utime_failure_reports_custom_errnote(monkeypatch, tmp_path):
    class FakeDownloader:
        def __init__(self):
            self.warnings = []

        def report_warning(self, msg):
            self.warnings.append(msg)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    path = str(tmp_path / "missing_custom.txt")
    custom_note = "custom utime error"

    def fake_utime(p, times):
        raise OSError("mock utime failure")

    monkeypatch.setattr(os, "utime", fake_utime)

    pp.try_utime(path, 1000000000, 1000000000, errnote=custom_note)

    assert downloader.warnings == [custom_note]
