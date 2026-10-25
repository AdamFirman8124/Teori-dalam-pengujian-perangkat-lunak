# file: project/youtube_dl/extractor/linuxacademy.py:72-152
# asked: {"lines": [73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 111, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152], "branches": [[74, 75], [74, 77], [123, 124], [123, 128], [143, 144], [143, 150]]}
# gained: {"lines": [73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 111, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152], "branches": [[74, 75], [74, 77], [123, 124], [123, 128], [143, 144], [143, 150]]}

import base64
import io
import json
import pytest
from youtube_dl.compat import compat_HTTPError
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE
from youtube_dl.utils import ExtractorError


class _FakeURLH(object):
    def __init__(self, url):
        self._url = url

    def geturl(self):
        return self._url


def _make_authorize_webpage(extra_params):
    payload = json.dumps({"extraParams": extra_params})
    b64 = base64.b64encode(payload.encode("utf-8")).decode("utf-8")
    return 'prefix atob("%s") suffix' % b64


def _make_ie_with_login(monkeypatch, username, password):
    ie = LinuxAcademyIE()
    from youtube_dl import YoutubeDL
    ydl = YoutubeDL({"quiet": True, "no_color": True})
    ie._downloader = ydl
    monkeypatch.setattr(
        ie, "_get_login_info", lambda *a, **k: (username, password))
    return ie


def test_login_no_username_returns_early(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, None, None)
    called = {"handle": False, "page": False}

    def fake_handle(*a, **k):
        called["handle"] = True
        raise AssertionError("should not be called")

    def fake_page(*a, **k):
        called["page"] = True
        raise AssertionError("should not be called")

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)
    assert ie._login() is None
    assert called == {"handle": False, "page": False}


def test_login_success_direct_access_token(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, "user1", "pass1")
    extra = {"foo": "bar"}
    authorize_webpage = _make_authorize_webpage(extra)
    login_state_url = "https://login.linuxacademy.com/state123"
    login_page_html = (
        '<html><input type="hidden" name="wctx" value="WCTX123"/>'
        '<input type="hidden" name="other" value="OV"/></html>'
    )
    callback_page = "<html>callback</html>"
    callback_url = "https://linuxacademy.com/cb?access_token=DIRECT123&x=1"
    calls = {}

    def fake_handle(url_or_request, video_id, note=None, errnote=None,
                    fatal=True, encoding=None, data=None, headers=None,
                    query=None, expected_status=None):
        s = str(url_or_request)
        if "authorize" in s:
            calls["authorize_query"] = dict(query or {})
            calls["authorize_url"] = s
            return (authorize_webpage, _FakeURLH(login_state_url))
        if "login/callback" in s:
            calls["callback_data"] = data
            calls["callback_headers"] = dict(headers or {})
            calls["callback_url_arg"] = s
            return (callback_page, _FakeURLH(callback_url))
        raise AssertionError("unexpected handle url %r" % s)

    def fake_page(url_or_request, video_id, note=None, errnote=None,
                  fatal=True, tries=1, timeout=5, encoding=None, data=None,
                  headers=None, query=None, expected_status=None):
        s = str(url_or_request)
        if "usernamepassword/login" in s:
            calls["login_data_raw"] = data
            calls["login_headers"] = dict(headers or {})
            return login_page_html
        if "tokenValidateLogin/token/" in s:
            calls["validate_url"] = s
            return "ok"
        raise AssertionError("unexpected page url %r" % s)

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)

    ie._login()

    q = calls["authorize_query"]
    assert q["client_id"] == ie._CLIENT_ID
    assert q["response_type"] == "token id_token"
    assert q["redirect_uri"] == ie._ORIGIN_URL
    assert len(q["state"]) == 32
    assert len(q["nonce"]) == 32
    login_data = json.loads(calls["login_data_raw"].decode("utf-8"))
    assert login_data["username"] == "user1"
    assert login_data["password"] == "pass1"
    assert login_data["foo"] == "bar"
    assert login_data["client_id"] == ie._CLIENT_ID
    assert login_data["tenant"] == "lacausers"
    assert login_data["connection"] == "Username-Password-Authentication"
    assert login_data["sso"] == "true"
    assert calls["login_headers"]["Content-Type"] == "application/json"
    assert calls["login_headers"]["Referer"] == login_state_url
    assert calls["callback_headers"]["Content-Type"] == "application/x-www-form-urlencoded"
    assert b"wctx=WCTX123" in calls["callback_data"] or "wctx" in str(calls["callback_data"])
    assert calls["validate_url"] == (
        "https://linuxacademy.com/cp/login/tokenValidateLogin/token/DIRECT123")


def test_login_success_fallback_access_token(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, "u2", "p2")
    authorize_webpage = _make_authorize_webpage({"a": 1})
    login_state_url = "https://login.linuxacademy.com/state456"
    login_page_html = '<html><input type="hidden" name="k" value="v"/></html>'
    callback_page = (
        '<script>authorizationResponse = '
        '{"response": {"access_token": "FALLBACK456"}};</script>'
    )
    callback_url = "https://linuxacademy.com/cb-no-token"
    calls = {}

    def fake_handle(url_or_request, video_id, note=None, errnote=None,
                    fatal=True, encoding=None, data=None, headers=None,
                    query=None, expected_status=None):
        s = str(url_or_request)
        if "authorize" in s:
            calls["q"] = dict(query or {})
            return (authorize_webpage, _FakeURLH(login_state_url))
        if "login/callback" in s:
            return (callback_page, _FakeURLH(callback_url))
        raise AssertionError(s)

    def fake_page(url_or_request, video_id, note=None, errnote=None,
                  fatal=True, tries=1, timeout=5, encoding=None, data=None,
                  headers=None, query=None, expected_status=None):
        s = str(url_or_request)
        if "usernamepassword/login" in s:
            return login_page_html
        if "tokenValidateLogin/token/" in s:
            calls["validate_url"] = s
            return "ok"
        raise AssertionError(s)

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)

    ie._login()

    assert len(calls["q"]["state"]) == 32
    assert len(calls["q"]["nonce"]) == 32
    assert calls["validate_url"].endswith("/FALLBACK456")


def _make_401_cause(payload_dict, code=401):
    fp = io.BytesIO(json.dumps(payload_dict).encode("utf-8"))
    return compat_HTTPError(
        "https://login.linuxacademy.com/usernamepassword/login",
        code, "Unauthorized", {}, fp)


def test_login_401_with_description(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, "u", "p")
    authorize_webpage = _make_authorize_webpage({})
    login_state_url = "https://login.linuxacademy.com/s1"

    def fake_handle(url_or_request, video_id, note=None, errnote=None,
                    fatal=True, encoding=None, data=None, headers=None,
                    query=None, expected_status=None):
        return (authorize_webpage, _FakeURLH(login_state_url))

    def fake_page(url_or_request, video_id, note=None, errnote=None,
                  fatal=True, tries=1, timeout=5, encoding=None, data=None,
                  headers=None, query=None, expected_status=None):
        s = str(url_or_request)
        if "usernamepassword/login" in s:
            raise ExtractorError(
                "login failed",
                cause=_make_401_cause(
                    {"description": "Wrong email or password", "code": "invalid"}))
        raise AssertionError(s)

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)
    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert "Wrong email or password" in str(excinfo.value)
    assert ie.IE_NAME in str(excinfo.value)


def test_login_401_without_description_uses_code(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, "u", "p")
    authorize_webpage = _make_authorize_webpage({})
    login_state_url = "https://login.linuxacademy.com/s2"

    def fake_handle(url_or_request, video_id, note=None, errnote=None,
                    fatal=True, encoding=None, data=None, headers=None,
                    query=None, expected_status=None):
        return (authorize_webpage, _FakeURLH(login_state_url))

    def fake_page(url_or_request, video_id, note=None, errnote=None,
                  fatal=True, tries=1, timeout=5, encoding=None, data=None,
                  headers=None, query=None, expected_status=None):
        s = str(url_or_request)
        if "usernamepassword/login" in s:
            raise ExtractorError(
                "login failed",
                cause=_make_401_cause({"code": "bad_code_xyz"}))
        raise AssertionError(s)

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)
    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert "bad_code_xyz" in str(excinfo.value)
    assert ie.IE_NAME in str(excinfo.value)


def test_login_reraises_on_wrong_code(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, "u", "p")
    authorize_webpage = _make_authorize_webpage({})
    login_state_url = "https://login.linuxacademy.com/s3"

    def fake_handle(url_or_request, video_id, note=None, errnote=None,
                    fatal=True, encoding=None, data=None, headers=None,
                    query=None, expected_status=None):
        return (authorize_webpage, _FakeURLH(login_state_url))

    orig = ExtractorError(
        "server error", cause=_make_401_cause({"code": "x"}, code=500))

    def fake_page(url_or_request, video_id, note=None, errnote=None,
                  fatal=True, tries=1, timeout=5, encoding=None, data=None,
                  headers=None, query=None, expected_status=None):
        raise orig

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)
    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert excinfo.value is orig


def test_login_reraises_on_non_http_cause(monkeypatch):
    ie = _make_ie_with_login(monkeypatch, "u", "p")
    authorize_webpage = _make_authorize_webpage({})
    login_state_url = "https://login.linuxacademy.com/s4"

    def fake_handle(url_or_request, video_id, note=None, errnote=None,
                    fatal=True, encoding=None, data=None, headers=None,
                    query=None, expected_status=None):
        return (authorize_webpage, _FakeURLH(login_state_url))

    orig = ExtractorError("other", cause=ValueError("oops"))

    def fake_page(url_or_request, video_id, note=None, errnote=None,
                  fatal=True, tries=1, timeout=5, encoding=None, data=None,
                  headers=None, query=None, expected_status=None):
        raise orig

    monkeypatch.setattr(ie, "_download_webpage_handle", fake_handle)
    monkeypatch.setattr(ie, "_download_webpage", fake_page)
    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert excinfo.value is orig
