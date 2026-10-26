# file: project/youtube_dl/extractor/linuxacademy.py:69-70
# asked: {"lines": [70], "branches": []}
# gained: {"lines": [70], "branches": []}

from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


def test_real_initialize_calls_login(monkeypatch):
    ie = LinuxAcademyIE()
    calls = []

    def fake_login(self):
        calls.append(self)
        return "logged-in"

    monkeypatch.setattr(LinuxAcademyIE, "_login", fake_login)
    result = ie._real_initialize()
    assert calls == [ie]
    assert result is None


def test_real_initialize_propagates_login(monkeypatch):
    ie = LinuxAcademyIE()
    called = {"count": 0}

    def fake_login(self):
        assert self is ie
        called["count"] += 1

    monkeypatch.setattr(ie, "_login", fake_login.__get__(ie, LinuxAcademyIE))
    ie._real_initialize()
    assert called["count"] == 1
