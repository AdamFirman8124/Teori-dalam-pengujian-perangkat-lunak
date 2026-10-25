# file: project/youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [70], "branches": []}
# gained: {"lines": [70], "branches": []}

import pytest

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


@pytest.fixture
def ie():
    return LinuxAcademyIE()


def test_real_initialize_calls_login(ie, monkeypatch):
    calls = []

    def fake_login():
        calls.append(True)

    monkeypatch.setattr(ie, '_login', fake_login)

    result = ie._real_initialize()

    assert result is None
    assert calls == [True]
