# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


class FakeResponse(object):
    def __init__(self, body):
        self._body = body

    def read(self):
        return self._body


DEFAULT_OPTIONS = {
    'validate_certs': True,
    'use_proxy': True,
    'username': 'user',
    'password': 'pass',
    'headers': {'X-Test': '1'},
    'force': False,
    'timeout': 10,
    'http_agent': 'test-agent',
    'force_basic_auth': False,
    'follow_redirects': 'all',
    'use_gssapi': False,
    'unix_socket': None,
    'ca_path': None,
    'unredirected_headers': None,
    'split_lines': True,
}


def make_lookup(monkeypatch, options=None):
    opts = dict(DEFAULT_OPTIONS)
    if options:
        opts.update(options)

    lookup = LookupModule()

    def fake_set_options(var_options=None, direct=None):
        assert direct is not None or var_options is not None

    def fake_get_option(name):
        return opts[name]

    monkeypatch.setattr(lookup, 'set_options', fake_set_options)
    monkeypatch.setattr(lookup, 'get_option', fake_get_option)
    return lookup


def test_run_split_lines_true(monkeypatch):
    lookup = make_lookup(monkeypatch, {'split_lines': True})
    captured = {}

    def fake_open_url(term, **kwargs):
        captured['term'] = term
        captured['kwargs'] = kwargs
        return FakeResponse(b'line1\nline2\nline3\n')

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', fake_open_url)

    ret = lookup.run(['http://example.com/'])

    assert ret == ['line1', 'line2', 'line3']
    assert captured['term'] == 'http://example.com/'
    # verify all options are forwarded to open_url
    kwargs = captured['kwargs']
    assert kwargs['validate_certs'] is True
    assert kwargs['use_proxy'] is True
    assert kwargs['url_username'] == 'user'
    assert kwargs['url_password'] == 'pass'
    assert kwargs['headers'] == {'X-Test': '1'}
    assert kwargs['force'] is False
    assert kwargs['timeout'] == 10
    assert kwargs['http_agent'] == 'test-agent'
    assert kwargs['force_basic_auth'] is False
    assert kwargs['follow_redirects'] == 'all'
    assert kwargs['use_gssapi'] is False
    assert kwargs['unix_socket'] is None
    assert kwargs['ca_path'] is None
    assert kwargs['unredirected_headers'] is None


def test_run_split_lines_false(monkeypatch):
    lookup = make_lookup(monkeypatch, {'split_lines': False})
    monkeypatch.setattr(
        'ansible.plugins.lookup.url.open_url',
        lambda term, **kwargs: FakeResponse(b'whole body\nwith lines'))

    ret = lookup.run(['http://example.com/'])

    assert ret == ['whole body\nwith lines']


def test_run_multiple_terms(monkeypatch):
    lookup = make_lookup(monkeypatch)

    def fake_open_url(term, **kwargs):
        return FakeResponse(b'body of ' + term.encode('utf-8'))

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', fake_open_url)

    ret = lookup.run(['http://a.example.com/', 'http://b.example.com/'])

    assert ret == ['body of http://a.example.com/', 'body of http://b.example.com/']


def test_run_http_error(monkeypatch):
    lookup = make_lookup(monkeypatch)

    def fake_open_url(term, **kwargs):
        raise HTTPError('http://example.com/', 404, 'Not Found', None, None)

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', fake_open_url)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['http://example.com/'])
    assert 'Received HTTP error for http://example.com/' in to_text(excinfo.value)


def test_run_url_error(monkeypatch):
    lookup = make_lookup(monkeypatch)

    def fake_open_url(term, **kwargs):
        raise URLError('connection refused')

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', fake_open_url)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['http://example.com/'])
    assert 'Failed lookup url for http://example.com/' in to_text(excinfo.value)
    assert 'connection refused' in to_text(excinfo.value)


def test_run_ssl_validation_error(monkeypatch):
    lookup = make_lookup(monkeypatch)

    def fake_open_url(term, **kwargs):
        raise SSLValidationError('certificate verify failed')

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', fake_open_url)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['https://example.com/'])
    assert "Error validating the server's certificate for https://example.com/" in to_text(excinfo.value)
    assert 'certificate verify failed' in to_text(excinfo.value)


def test_run_connection_error(monkeypatch):
    lookup = make_lookup(monkeypatch)

    def fake_open_url(term, **kwargs):
        raise ConnectionError('timed out')

    monkeypatch.setattr('ansible.plugins.lookup.url.open_url', fake_open_url)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['http://example.com/'])
    assert 'Error connecting to http://example.com/' in to_text(excinfo.value)
    assert 'timed out' in to_text(excinfo.value)


def to_text(value):
    from ansible.module_utils._text import to_text as _to_text
    return _to_text(value)
