# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os
from unittest.mock import MagicMock

import pytest

from youtube_dl.postprocessor.common import PostProcessor
from youtube_dl.utils import encodeFilename


def test_try_utime_success(tmp_path, monkeypatch):
    """Lines 59-60: os.utime is invoked with the encoded path and (atime, mtime)."""
    target = tmp_path / "video.mp4"
    target.write_bytes(b"data")

    atime, mtime = 1000, 2000
    calls = []
    real_utime = os.utime  # keep a reference to the original before patching

    def fake_utime(path, times):
        calls.append((path, times))
        # Delegate to the real os.utime (captured before patching) so the
        # postcondition can be verified without infinite recursion.
        real_utime(path, times)

    monkeypatch.setattr("youtube_dl.postprocessor.common.os.utime", fake_utime)

    downloader = MagicMock()
    pp = PostProcessor(downloader)
    result = pp.try_utime(str(target), atime, mtime)

    assert result is None
    assert calls == [(encodeFilename(str(target)), (atime, mtime))]
    st = os.stat(str(target))
    assert st.st_atime == atime
    assert st.st_mtime == mtime
    downloader.report_warning.assert_not_called()


def test_try_utime_failure_reports_custom_errnote(monkeypatch):
    """Lines 61-62: an exception from os.utime is swallowed and reported as a warning."""

    def boom(path, times):
        raise OSError("no permission")

    monkeypatch.setattr("youtube_dl.postprocessor.common.os.utime", boom)

    downloader = MagicMock()
    pp = PostProcessor(downloader)

    errnote = "custom error note"
    # Must not raise, despite os.utime failing.
    result = pp.try_utime("some/path", 1, 2, errnote=errnote)

    assert result is None
    downloader.report_warning.assert_called_once_with(errnote)


def test_try_utime_failure_reports_default_errnote(monkeypatch):
    """Lines 61-62: the default errnote is used when none is supplied."""

    def boom(path, times):
        raise OSError("no permission")

    monkeypatch.setattr("youtube_dl.postprocessor.common.os.utime", boom)

    downloader = MagicMock()
    pp = PostProcessor(downloader)

    result = pp.try_utime("some/path", 1, 2)

    assert result is None
    downloader.report_warning.assert_called_once_with("Cannot update utime of file")
