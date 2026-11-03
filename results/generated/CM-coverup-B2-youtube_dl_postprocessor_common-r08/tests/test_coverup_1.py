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


def make_pp(downloader=None):
    pp = PostProcessor()
    pp.set_downloader(downloader if downloader is not None else FakeDownloader())
    return pp


def test_try_utime_success(tmp_path, monkeypatch):
    """Lines 59-60: os.utime is called with the encoded path and (atime, mtime)."""
    downloader = FakeDownloader()
    pp = make_pp(downloader)

    target = tmp_path / 'video.mp4'
    target.write_bytes(b'data')
    path = str(target)

    atime, mtime = 1000000000, 1234567890

    calls = []
    real_utime = os.utime

    def fake_utime(filename, times):
        calls.append((filename, times))
        real_utime(filename, times)

    monkeypatch.setattr(os, 'utime', fake_utime)

    result = pp.try_utime(path, atime, mtime)

    assert result is None
    # os.utime must have been called exactly once with the encoded filename
    # and the (atime, mtime) tuple.
    assert calls == [(encodeFilename(path), (atime, mtime))]
    # Postcondition: the timestamps were really written to the file.
    st = os.stat(path)
    assert st.st_atime == pytest.approx(atime, abs=2)
    assert st.st_mtime == pytest.approx(mtime, abs=2)
    # No warning must be reported on the success path.
    assert downloader.warnings == []


def test_try_utime_failure_reports_custom_errnote(monkeypatch):
    """Lines 59, 61-62: an exception from os.utime is caught and reported."""
    downloader = FakeDownloader()
    pp = make_pp(downloader)

    def failing_utime(filename, times):
        raise OSError('utime failed')

    monkeypatch.setattr(os, 'utime', failing_utime)

    errnote = 'custom utime failure note'
    result = pp.try_utime('some/path', 1, 2, errnote=errnote)

    assert result is None
    # Postcondition: the custom errnote was reported through the downloader.
    assert downloader.warnings == [errnote]


def test_try_utime_failure_default_errnote(monkeypatch):
    """Lines 61-62: the default errnote is used when none is supplied."""
    downloader = FakeDownloader()
    pp = make_pp(downloader)

    def failing_utime(filename, times):
        raise ValueError('boom')

    monkeypatch.setattr(os, 'utime', failing_utime)

    result = pp.try_utime('some/path', 1, 2)

    assert result is None
    # Postcondition: the default errnote was reported through the downloader.
    assert downloader.warnings == ['Cannot update utime of file']
