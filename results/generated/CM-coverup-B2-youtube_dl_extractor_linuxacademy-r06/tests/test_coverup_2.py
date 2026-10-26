# file: project/youtube_dl/extractor/linuxacademy.py:72-152
# asked: {"lines": [73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 111, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152], "branches": [[74, 75], [74, 77], [123, 124], [123, 128], [143, 144], [143, 150]]}
# gained: {"lines": [73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 111, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 140, 141, 142, 143, 144, 145, 146, 147, 148, 150, 151, 152], "branches": [[74, 75], [74, 77], [123, 124], [123, 128], [143, 144], [143, 150]]}

import base64
import io
import json
from types import SimpleNamespace

import pytest

from youtube_dl.compat import compat_HTTPError
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE
from youtube_dl.utils import ExtractorError


class _FakeHandle:
    def __init__(self, url):
        self._url = url

    def geturl(self):
        return self._url


def _make_ie():
    return LinuxAcademyIE(SimpleNamespace(params={'no_color': True}))


def _authorize_page(extra):
    payload = base64.b64encode(json.dumps({'extraParams': extra}).encode('utf-8')).decode('ascii')
    return 'prefix atob("%s") suffix' % payload


def test_login_no_credentials(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: (None, None))

    def _unexpected(*args, **kwargs):
        raise AssertionError('should not download without credentials')

    monkeypatch.setattr(ie, '_download_webpage_handle', _unexpected)
    monkeypatch.setattr(ie, '_download_webpage', _unexpected)
    assert ie._login() is None


def test_login_success_token_in_url(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: ('myuser', 'mypass'))
    monkeypatch.setattr(ie, '_hidden_inputs', lambda html: {'wa': 'w', 'wresult': 'r'})

    authorize_html = _authorize_page({'foo': 'bar'})
    login_state_url = 'https://login.linuxacademy.com/state123'
    login_html = '<html>login</html>'
    callback_html = '<html>callback</html>'
    token = 'TOKEN_URL_123'
    callback_url = 'https://linuxacademy.com/#access_token=%s&x=1' % token
    captured = {}

    def fake_handle(url_or_request, video_id, *args, **kwargs):
        s = str(url_or_request)
        if 'authorize' in s:
            captured['authorize_query'] = kwargs.get('query', {})
            return (authorize_html, _FakeHandle(login_state_url))
        if 'login/callback' in s:
            captured['callback_data'] = kwargs.get('data')
            captured['callback_headers'] = kwargs.get('headers', {})
            return (callback_html, _FakeHandle(callback_url))
        raise AssertionError('unexpected handle url %r' % s)

    def fake_page(url_or_request, video_id, *args, **kwargs):
        s = str(url_or_request)
        if 'usernamepassword/login' in s:
            captured['login_raw'] = kwargs.get('data')
            captured['login_headers'] = kwargs.get('headers', {})
            captured['login_referer'] = kwargs.get('headers', {}).get('Referer')
            return login_html
        if 'tokenValidateLogin/token/' in s:
            captured['validate_url'] = s
            return 'ok'
        raise AssertionError('unexpected page url %r' % s)

    monkeypatch.setattr(ie, '_download_webpage_handle', fake_handle)
    monkeypatch.setattr(ie, '_download_webpage', fake_page)

    assert ie._login() is None
    # authorize query used client id / state / nonce
    assert captured['authorize_query']['client_id'] == ie._CLIENT_ID
    assert len(captured['authorize_query']['state']) == 32
    assert len(captured['authorize_query']['nonce']) == 32
    # login json contains credentials and merged extraParams
    login_data = json.loads(captured['login_raw'].decode('utf-8'))
    assert login_data['username'] == 'myuser'
    assert login_data['password'] == 'mypass'
    assert login_data['foo'] == 'bar'
    assert login_data['client_id'] == ie._CLIENT_ID
    assert login_data['connection'] == 'Username-Password-Authentication'
    assert captured['login_referer'] == login_state_url
    # callback posted urlencoded hidden inputs
    assert b'wa=' in captured['callback_data']
    # token validation used token from url
    assert captured['validate_url'] == 'https://linuxacademy.com/cp/login/tokenValidateLogin/token/%s' % token


def test_login_success_token_in_callback(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: ('u2', 'p2'))
    monkeypatch.setattr(ie, '_hidden_inputs', lambda html: {'a': 'b'})

    authorize_html = _authorize_page({'k': 'v'})
    login_state_url = 'https://login.linuxacademy.com/state456'
    login_html = '<html>login2</html>'
    token = 'CALLBACKTOKEN999'
    callback_html = 'var authorizationResponse = {"response": {"access_token": "%s"}};' % token
    callback_url = 'https://linuxacademy.com/cb-no-token'
    captured = {}

    def fake_handle(url_or_request, video_id, *args, **kwargs):
        s = str(url_or_request)
        if 'authorize' in s:
            return (authorize_html, _FakeHandle(login_state_url))
        if 'login/callback' in s:
            return (callback_html, _FakeHandle(callback_url))
        raise AssertionError('unexpected handle url %r' % s)

    def fake_page(url_or_request, video_id, *args, **kwargs):
        s = str(url_or_request)
        if 'usernamepassword/login' in s:
            captured['login_raw'] = kwargs.get('data')
            return login_html
        if 'tokenValidateLogin/token/' in s:
            captured['validate_url'] = s
            return 'ok'
        raise AssertionError('unexpected page url %r' % s)

    monkeypatch.setattr(ie, '_download_webpage_handle', fake_handle)
    monkeypatch.setattr(ie, '_download_webpage', fake_page)

    assert ie._login() is None
    login_data = json.loads(captured['login_raw'].decode('utf-8'))
    assert login_data['username'] == 'u2'
    assert login_data['k'] == 'v'
    assert captured['validate_url'].endswith('/%s' % token)


def test_login_401_with_description(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: ('bad', 'bad'))
    authorize_html = _authorize_page({})
    login_state_url = 'https://login.linuxacademy.com/state401'

    def fake_handle(url_or_request, video_id, *args, **kwargs):
        return (authorize_html, _FakeHandle(login_state_url))

    body = json.dumps({'description': 'Wrong email or password.', 'code': 'invalid'}).encode('utf-8')
    cause = compat_HTTPError(
        'https://login.linuxacademy.com/usernamepassword/login', 401, 'Unauthorized', {}, io.BytesIO(body))
    original = ExtractorError('login failed', cause=cause)

    def fake_page(*args, **kwargs):
        raise original

    monkeypatch.setattr(ie, '_download_webpage_handle', fake_handle)
    monkeypatch.setattr(ie, '_download_webpage', fake_page)

    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert 'Wrong email or password.' in str(excinfo.value)
    assert ie.IE_NAME in str(excinfo.value)


def test_login_401_with_code_fallback(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: ('bad', 'bad'))
    authorize_html = _authorize_page({})
    login_state_url = 'https://login.linuxacademy.com/state402'

    def fake_handle(url_or_request, video_id, *args, **kwargs):
        return (authorize_html, _FakeHandle(login_state_url))

    body = json.dumps({'code': 'invalid_user_password'}).encode('utf-8')
    cause = compat_HTTPError(
        'https://login.linuxacademy.com/usernamepassword/login', 401, 'Unauthorized', {}, io.BytesIO(body))
    original = ExtractorError('login failed', cause=cause)

    def fake_page(*args, **kwargs):
        raise original

    monkeypatch.setattr(ie, '_download_webpage_handle', fake_handle)
    monkeypatch.setattr(ie, '_download_webpage', fake_page)

    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert 'invalid_user_password' in str(excinfo.value)
    assert ie.IE_NAME in str(excinfo.value)


def test_login_reraise_http_non401(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: ('u', 'p'))
    authorize_html = _authorize_page({})

    def fake_handle(url_or_request, video_id, *args, **kwargs):
        return (authorize_html, _FakeHandle('https://login.linuxacademy.com/state500'))

    body = json.dumps({'description': 'server error'}).encode('utf-8')
    cause = compat_HTTPError(
        'https://login.linuxacademy.com/usernamepassword/login', 500, 'Error', {}, io.BytesIO(body))
    original = ExtractorError('server error', cause=cause)

    def fake_page(*args, **kwargs):
        raise original

    monkeypatch.setattr(ie, '_download_webpage_handle', fake_handle)
    monkeypatch.setattr(ie, '_download_webpage', fake_page)

    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert excinfo.value is original


def test_login_reraise_non_http(monkeypatch):
    ie = _make_ie()
    monkeypatch.setattr(ie, '_get_login_info', lambda: ('u', 'p'))
    authorize_html = _authorize_page({})

    def fake_handle(url_or_request, video_id, *args, **kwargs):
        return (authorize_html, _FakeHandle('https://login.linuxacademy.com/stateX'))

    original = ExtractorError('network fail', cause=ValueError('oops'))

    def fake_page(*args, **kwargs):
        raise original

    monkeypatch.setattr(ie, '_download_webpage_handle', fake_handle)
    monkeypatch.setattr(ie, '_download_webpage', fake_page)

    with pytest.raises(ExtractorError) as excinfo:
        ie._login()
    assert excinfo.value is original
