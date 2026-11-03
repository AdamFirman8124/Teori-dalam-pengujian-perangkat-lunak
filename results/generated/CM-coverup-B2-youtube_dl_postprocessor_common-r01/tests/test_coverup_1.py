# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

import pytest

from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl.utils import encodeFilename


class FakeDownloader(object):
    """Minimal downloader stub that records reported warnings."""

    def __init__(self):
        self.warnings = []

    def report_warning(self, message):
        self.warnings.append(message)


def test_try_utime_success(tmp_path, monkeypatch):
    """Lines 59-60: os.utime is called with the encoded filename and times."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    path = str(tmp_path / 'video.mp4')
    with open(path, 'wb'):
        pass  # create an empty file so os.utime has a real target

    real_utime = os.utime
    utime_calls = []

    def spying_utime(filename, times):
        utime_calls.append((filename, times))
        return real_utime(filename, times)

    monkeypatch.setattr(os, 'utime', spying_utime)

    atime, mtime = 1000, 2000
    pp.try_utime(path, atime, mtime)

    # os.utime must have been called exactly once, with the encoded path
    # and the (atime, mtime) tuple
    assert utime_calls == [(encodeFilename(path), (atime, mtime))]

    # the file timestamps must actually have been updated
    st = os.stat(path)
    assert st.st_atime == pytest.approx(atime, abs=2)
    assert st.st_mtime == pytest.approx(mtime, abs=2)

    # no warning must have been reported on success
    assert downloader.warnings == []


def test_try_utime_failure_reports_custom_errnote(monkeypatch):
    """Lines 61-62: a failing os.utime is reported as a warning (custom note)."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    def failing_utime(filename, times):
        raise OSError('utime failed')

    monkeypatch.setattr(os, 'utime', failing_utime)

    errnote = 'custom utime failure note'
    pp.try_utime('video.mp4', 1000, 2000, errnote=errnote)

    assert downloader.warnings == [errnote]


def test_try_utime_failure_reports_default_errnote(monkeypatch):
    """Lines 61-62: the default errnote is used when none is supplied."""
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    def failing_utime(filename, times):
        raise OSError('utime failed')

    monkeypatch.setattr(os, 'utime', failing_utime)

    pp.try_utime('video.mp4', 1000, 2000)

    assert downloader.warnings == ['Cannot update utime of file']
