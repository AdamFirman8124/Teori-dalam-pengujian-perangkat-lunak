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

    assert len(calls) == 1
    assert calls[0] is ie
    assert result is None


def test_real_initialize_delegates_to_instance(monkeypatch):
    ie = LinuxAcademyIE()
    called = {"count": 0}

    def fake_login():
        called["count"] += 1

    monkeypatch.setattr(ie, "_login", fake_login)

    ie._real_initialize()

    assert called["count"] == 1
