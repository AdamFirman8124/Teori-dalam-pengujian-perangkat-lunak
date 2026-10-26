# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

import pytest

from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    def __init__(self):
        self.warnings = []

    def report_warning(self, message):
        self.warnings.append(message)


@pytest.fixture
def pp():
    downloader = FakeDownloader()
    post_processor = PostProcessor(downloader)
    return post_processor, downloader


def test_try_utime_success(pp, tmp_path):
    post_processor, downloader = pp
    target = tmp_path / 'video.mp4'
    target.write_bytes(b'data')

    atime, mtime = 1000000000, 1234567890
    post_processor.try_utime(str(target), atime, mtime)

    stat = os.stat(str(target))
    assert stat.st_atime == atime
    assert stat.st_mtime == mtime
    assert downloader.warnings == []


def test_try_utime_failure_reports_warning(pp, monkeypatch):
    post_processor, downloader = pp

    def failing_utime(path, times):
        raise OSError('utime failed')

    monkeypatch.setattr(os, 'utime', failing_utime)

    errnote = 'custom utime error note'
    # Must not raise despite os.utime failing
    post_processor.try_utime('whatever', 1, 2, errnote=errnote)

    assert downloader.warnings == [errnote]
