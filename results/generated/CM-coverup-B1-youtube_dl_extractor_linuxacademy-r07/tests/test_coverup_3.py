# file: project/youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [70], "branches": []}
# gained: {"lines": [70], "branches": []}

import pytest

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


class FakeDownloader(object):
    def __init__(self):
        self.params = {'geo_bypass': True}


@pytest.fixture
def ie():
    ie = LinuxAcademyIE()
    ie.set_downloader(FakeDownloader())
    return ie


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

    ie.initialize()

    assert calls == [((), {})]
    assert ie._ready is True
