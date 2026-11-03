# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl.utils import encodeFilename


class FakeDownloader(object):
    """Minimal downloader stand-in that records reported warnings."""

    def __init__(self):
        self.warnings = []

    def report_warning(self, message):
        self.warnings.append(message)


def test_try_utime_success(monkeypatch):
    # Covers lines 59-60: the try block and the os.utime() call.
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)

    utime_calls = []

    def fake_utime(path, times):
        utime_calls.append((path, times))

    monkeypatch.setattr(os, 'utime', fake_utime)

    path = u'some_file.mp4'
    atime, mtime = 1234567890, 987654321

    pp.try_utime(path, atime, mtime)

    # os.utime must have been called exactly once, with the encoded filename
    # and the (atime, mtime) tuple, and no warning may be reported on success.
    assert utime_calls == [(encodeFilename(path), (atime, mtime))]
    assert downloader.warnings == []


def test_try_utime_failure_reports_custom_errnote(monkeypatch):
    # Covers lines 61-62: the except branch and report_warning() call.
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)

    def failing_utime(path, times):
        raise OSError('utime failed')

    monkeypatch.setattr(os, 'utime', failing_utime)

    errnote = u'custom utime failure note'
    # The exception raised by os.utime must be swallowed, not propagated.
    pp.try_utime(u'some_file.mp4', 1, 2, errnote=errnote)

    assert downloader.warnings == [errnote]


def test_try_utime_failure_reports_default_errnote(monkeypatch):
    # Covers lines 61-62 again, this time exercising the default errnote.
    downloader = FakeDownloader()
    pp = PostProcessor(downloader=downloader)

    def failing_utime(path, times):
        raise ValueError('boom')

    monkeypatch.setattr(os, 'utime', failing_utime)

    pp.try_utime(u'some_file.mp4', 1, 2)

    assert downloader.warnings == [u'Cannot update utime of file']
