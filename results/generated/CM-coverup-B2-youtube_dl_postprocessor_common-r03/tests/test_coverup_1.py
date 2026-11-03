# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

import pytest

from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl.utils import encodeFilename


class FakeDownloader(object):
    """Minimal downloader stub that records report_warning calls."""

    def __init__(self):
        self.warnings = []

    def report_warning(self, msg):
        self.warnings.append(msg)


def test_try_utime_success(tmp_path, monkeypatch):
    """Cover the try branch (lines 59-60): os.utime is invoked with the
    encoded filename and the (atime, mtime) tuple, the file times are
    actually updated, and no warning is reported."""
    path = str(tmp_path / 'video.mp4')
    with open(path, 'wb'):
        pass  # create an empty file

    real_utime = os.utime
    calls = []

    def spy_utime(filename, times):
        calls.append((filename, times))
        return real_utime(filename, times)

    monkeypatch.setattr(os, 'utime', spy_utime)

    atime, mtime = 1000000000, 1234567890
    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    pp.try_utime(path, atime, mtime)

    # os.utime was called once, with the encoded path and the time tuple
    assert calls == [(encodeFilename(path), (atime, mtime))]
    # the times were really applied to the file
    st = os.stat(path)
    assert st.st_atime == pytest.approx(atime, abs=1)
    assert st.st_mtime == pytest.approx(mtime, abs=1)
    # no warning was reported on the success path
    assert downloader.warnings == []


def test_try_utime_failure_custom_errnote(monkeypatch):
    """Cover the except branch (lines 61-62): when os.utime raises,
    downloader.report_warning is called with the given errnote."""

    def boom(filename, times):
        raise OSError('utime failed')

    monkeypatch.setattr(os, 'utime', boom)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)
    errnote = 'custom utime failure note'

    pp.try_utime('some file', 1, 2, errnote=errnote)

    assert downloader.warnings == [errnote]


def test_try_utime_failure_default_errnote(monkeypatch):
    """Cover the except branch (lines 61-62) with the default errnote."""

    def boom(filename, times):
        raise ValueError('utime failed')

    monkeypatch.setattr(os, 'utime', boom)

    downloader = FakeDownloader()
    pp = PostProcessor(downloader)

    pp.try_utime('some file', 1, 2)

    assert downloader.warnings == ['Cannot update utime of file']
