# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError as AnsibleConnectionError
from ansible.module_utils.urls import SSLValidationError as AnsibleSSLValidationError
import ansible.plugins.lookup.url as url_module
from ansible.plugins.lookup.url import LookupModule


def _make_lookup(monkeypatch, split_lines=True, extra_options=None):
    lookup = LookupModule(loader=None, templar=None)
    options = {
        'validate_certs': True,
        'use_proxy': True,
        'username': None,
        'password': None,
        'headers': {},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': None,
        'split_lines': split_lines,
    }
    if extra_options:
        options.update(extra_options)

    def _fake_set_options(var_options=None, direct=None):
        # simulate direct kwargs overriding options, keep call itself covered
        if direct:
            for k, v in direct.items():
                if k in options:
                    options[k] = v

    monkeypatch.setattr(lookup, "set_options", _fake_set_options)
    monkeypatch.setattr(lookup, "get_option", lambda name, *a, **kw: options[name])
    return lookup, options


class _FakeResponse:
    def __init__(self, data):
        self._data = data

    def read(self):
        return self._data


def test_url_lookup_split_lines_true(monkeypatch):
    lookup, options = _make_lookup(monkeypatch, split_lines=True)
    captured = {}

    def _fake_open_url(term, **kwargs):
        captured['term'] = term
        captured['kwargs'] = kwargs
        return _FakeResponse(b"line1\nline2\nline3")

    monkeypatch.setattr(url_module, "open_url", _fake_open_url)
    ret = lookup.run(["http://example.com"], variables={})
    assert ret == ["line1", "line2", "line3"]
    assert captured['term'] == "http://example.com"
    # verify option mapping for lines 196-209
    assert captured['kwargs']['validate_certs'] == options['validate_certs']
    assert captured['kwargs']['use_proxy'] == options['use_proxy']
    assert captured['kwargs']['url_username'] == options['username']
    assert captured['kwargs']['url_password'] == options['password']
    assert captured['kwargs']['headers'] == options['headers']
    assert captured['kwargs']['force'] == options['force']
    assert captured['kwargs']['timeout'] == options['timeout']
    assert captured['kwargs']['http_agent'] == options['http_agent']
    assert captured['kwargs']['force_basic_auth'] == options['force_basic_auth']
    assert captured['kwargs']['follow_redirects'] == options['follow_redirects']
    assert captured['kwargs']['use_gssapi'] == options['use_gssapi']
    assert captured['kwargs']['unix_socket'] == options['unix_socket']
    assert captured['kwargs']['ca_path'] == options['ca_path']
    assert captured['kwargs']['unredirected_headers'] == options['unredirected_headers']


def test_url_lookup_no_split_lines(monkeypatch):
    lookup, options = _make_lookup(monkeypatch, split_lines=False)
    monkeypatch.setattr(url_module, "open_url", lambda term, **kw: _FakeResponse(b"hello world\nsecond line"))
    ret = lookup.run(["http://example.com"], variables={})
    assert ret == ["hello world\nsecond line"]
    assert len(ret) == 1


def test_url_lookup_split_lines_via_direct_kwarg(monkeypatch):
    lookup, options = _make_lookup(monkeypatch, split_lines=True)
    monkeypatch.setattr(url_module, "open_url", lambda term, **kw: _FakeResponse(b"a\nb"))
    # pass split_lines=False via direct kwargs, fake set_options applies it
    ret = lookup.run(["http://example.com"], variables={}, split_lines=False)
    assert ret == ["a\nb"]
    # and True case
    lookup2, _ = _make_lookup(monkeypatch, split_lines=False)
    monkeypatch.setattr(url_module, "open_url", lambda term, **kw: _FakeResponse(b"a\nb"))
    ret2 = lookup2.run(["http://example.com"], variables={}, split_lines=True)
    assert ret2 == ["a", "b"]


def test_url_lookup_multiple_terms(monkeypatch):
    lookup, options = _make_lookup(monkeypatch, split_lines=False)
    calls = []

    def _fake_open_url(term, **kwargs):
        calls.append(term)
        return _FakeResponse(("content-for-%s" % term).encode("utf-8"))

    monkeypatch.setattr(url_module, "open_url", _fake_open_url)
    ret = lookup.run(["http://a.example", "http://b.example"], variables={})
    assert ret == ["content-for-http://a.example", "content-for-http://b.example"]
    assert calls == ["http://a.example", "http://b.example"]


def test_url_lookup_http_error(monkeypatch):
    lookup, _ = _make_lookup(monkeypatch, split_lines=True)

    def _raise(term, **kwargs):
        raise HTTPError(term, 404, "Not Found", {}, None)

    monkeypatch.setattr(url_module, "open_url", _raise)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["http://example.com/missing"], variables={})
    assert "Received HTTP error" in str(excinfo.value)
    assert "http://example.com/missing" in str(excinfo.value)


def test_url_lookup_url_error(monkeypatch):
    lookup, _ = _make_lookup(monkeypatch, split_lines=True)

    def _raise(term, **kwargs):
        raise URLError("connection refused")

    monkeypatch.setattr(url_module, "open_url", _raise)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["http://example.com"], variables={})
    assert "Failed lookup url" in str(excinfo.value)
    assert "http://example.com" in str(excinfo.value)


def test_url_lookup_ssl_validation_error(monkeypatch):
    lookup, _ = _make_lookup(monkeypatch, split_lines=True)

    def _raise(term, **kwargs):
        raise AnsibleSSLValidationError("bad cert")

    monkeypatch.setattr(url_module, "open_url", _raise)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["https://example.com"], variables={})
    assert "Error validating the server's certificate" in str(excinfo.value)
    assert "https://example.com" in str(excinfo.value)


def test_url_lookup_connection_error(monkeypatch):
    lookup, _ = _make_lookup(monkeypatch, split_lines=True)

    def _raise(term, **kwargs):
        raise AnsibleConnectionError("refused")

    monkeypatch.setattr(url_module, "open_url", _raise)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(["http://example.com"], variables={})
    assert "Error connecting to" in str(excinfo.value)
    assert "http://example.com" in str(excinfo.value)
