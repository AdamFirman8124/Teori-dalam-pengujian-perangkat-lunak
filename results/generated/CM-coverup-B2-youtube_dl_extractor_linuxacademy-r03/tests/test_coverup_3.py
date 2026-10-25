# file: project/youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [70], "branches": []}
# gained: {"lines": [70], "branches": []}

import pytest

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


class _FakeDownloader(object):
    def __init__(self, params=None):
        self.params = params if params is not None else {}


@pytest.fixture
def ie():
    return LinuxAcademyIE(downloader=_FakeDownloader({'geo_bypass': False}))


def test_real_initialize_calls_login(ie, monkeypatch):
    calls = []

    def fake_login(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(ie, '_login', fake_login)

    ie._real_initialize()

    assert calls == [((), {})]


def test_initialize_logs_in_and_marks_ready(ie, monkeypatch):
    calls = []

    def fake_login(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(ie, '_login', fake_login)

    assert ie._ready is False

    ie.initialize()

    assert calls == [((), {})]
    assert ie._ready is True
