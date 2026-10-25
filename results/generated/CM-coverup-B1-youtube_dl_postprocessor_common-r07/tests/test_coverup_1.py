# file: project/youtube_dl/postprocessor/common.py:58-62
# asked: {"lines": [59, 60, 61, 62], "branches": []}
# gained: {"lines": [59, 60, 61, 62], "branches": []}

import os

import pytest

from youtube_dl.postprocessor import common
from youtube_dl.postprocessor.common import PostProcessor


class FakeDownloader(object):
    def __init__(self):
        self.warnings = []

    def report_warning(self, msg):
        self.warnings.append(msg)


@pytest.fixture
def downloader():
    return FakeDownloader()


@pytest.fixture
def pp(downloader):
    return PostProcessor(downloader)


def test_try_utime_success_calls_os_utime_with_encoded_path(pp, downloader, monkeypatch):
    calls = []

    def fake_encodeFilename(path):
        return 'ENCODED:' + path

    def fake_utime(path, times):
        calls.append((path, times))

    monkeypatch.setattr(common, 'encodeFilename', fake_encodeFilename)
    monkeypatch.setattr(common.os, 'utime', fake_utime)

    pp.try_utime('some/file.mp4', 1000, 2000)

    assert calls == [('ENCODED:some/file.mp4', (1000, 2000))]
    assert downloader.warnings == []


def test_try_utime_failure_reports_default_warning(pp, downloader, monkeypatch):
    def fake_utime(path, times):
        raise OSError('utime failed')

    monkeypatch.setattr(common.os, 'utime', fake_utime)

    pp.try_utime('some/file.mp4', 1000, 2000)

    assert downloader.warnings == ['Cannot update utime of file']


def test_try_utime_failure_reports_custom_errnote(pp, downloader, monkeypatch):
    def fake_utime(path, times):
        raise PermissionError('nope')

    monkeypatch.setattr(common.os, 'utime', fake_utime)

    pp.try_utime('some/file.mp4', 1000, 2000, errnote='custom note')

    assert downloader.warnings == ['custom note']


def test_try_utime_swallows_exception_and_does_not_propagate(pp, monkeypatch):
    def fake_utime(path, times):
        raise ValueError('boom')

    monkeypatch.setattr(common.os, 'utime', fake_utime)

    # Must not raise
    assert pp.try_utime('some/file.mp4', 1, 2) is None


def test_try_utime_real_os_utime_updates_times(pp, downloader, tmp_path):
    target = tmp_path / 'file.txt'
    target.write_text('x')

    pp.try_utime(str(target), 1000000000, 1000000000)

    assert downloader.warnings == []
    st = os.stat(str(target))
    assert int(st.st_atime) == 1000000000
    assert int(st.st_mtime) == 1000000000
