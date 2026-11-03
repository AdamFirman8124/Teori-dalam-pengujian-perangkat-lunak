# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    """Minimal downloader stub that records report_warning calls."""

    def __init__(self):
        self.warnings = []

    def report_warning(self, msg):
        self.warnings.append(msg)


def test_try_utime_updates_file_times(tmp_path):
    """Covers lines 59-60 (success path): os.utime is called, no warning emitted."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    fpath = os.path.join(str(tmp_path), 'video.mp4')
    with open(fpath, 'wb'):
        pass  # create an empty file

    atime, mtime = 1000000000, 2000000000
    result = pp.try_utime(fpath, atime, mtime)

    st = os.stat(fpath)
    assert st.st_atime == atime
    assert st.st_mtime == mtime
    # No exception occurred, so no warning must have been reported.
    assert downloader.warnings == []
    # try_utime has no explicit return value.
    assert result is None


def test_try_utime_reports_warning_on_failure(tmp_path):
    """Covers lines 61-62 (exception path): os.utime on a missing file fails
    and the errnote is reported instead of propagating."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    fpath = os.path.join(str(tmp_path), 'missing.mp4')  # parent exists, file does not
    errnote = 'utime failed on purpose'

    result = pp.try_utime(fpath, 1, 2, errnote=errnote)

    assert downloader.warnings == [errnote]
    assert result is None


def test_try_utime_reports_default_warning(monkeypatch, tmp_path):
    """Covers lines 59-62 with the default errnote when os.utime raises."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    utime_calls = []

    def fake_utime(path, times):
        utime_calls.append((path, times))
        raise OSError('simulated utime failure')

    # monkeypatch restores os.utime automatically at test teardown.
    monkeypatch.setattr(os, 'utime', fake_utime)

    fpath = os.path.join(str(tmp_path), 'whatever.mp4')
    result = pp.try_utime(fpath, 3, 4)

    assert utime_calls == [(fpath, (3, 4))]
    assert downloader.warnings == ['Cannot update utime of file']
    assert result is None
