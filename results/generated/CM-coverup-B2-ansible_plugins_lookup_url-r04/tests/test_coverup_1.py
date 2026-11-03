# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

"""Tests for ansible/plugins/lookup/url.py LookupModule.run (lines 190-224).

The option machinery (set_options/get_option) and the network call (open_url)
are stubbed so the tests exercise only the lookup plugin's own logic, run
offline, and leave no global state behind (everything goes through
``monkeypatch``).
"""

import io

import pytest

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup import url as url_lookup_module
from ansible.plugins.lookup.url import LookupModule


class FakeResponse(object):
    """Minimal file-like stand-in for the object returned by open_url."""

    def __init__(self, data):
        self._data = data

    def read(self):
        return self._data


BASE_OPTIONS = {
    'validate_certs': True,
    'use_proxy': True,
    'username': 'someuser',
    'password': 'somepass',
    'headers': {'X-Test': '1'},
    'force': False,
    'timeout': 10,
    'http_agent': 'ansible-test-agent',
    'force_basic_auth': False,
    'follow_redirects': 'urllib2',
    'use_gssapi': False,
    'unix_socket': None,
    'ca_path': None,
    'unredirected_headers': [],
    'split_lines': True,
}


@pytest.fixture
def make_lookup(monkeypatch):
    """Factory building a LookupModule whose option machinery is backed by a
    plain dict.  A fresh dict is created for every instance, so tests cannot
    pollute each other's options."""

    def create_lookup(**option_overrides):
        options = dict(BASE_OPTIONS)
        options.update(option_overrides)
        instance = LookupModule()
        monkeypatch.setattr(
            instance, 'set_options',
            lambda var_options=None, direct=None: None)
        monkeypatch.setattr(
            instance, 'get_option',
            lambda name, hostvars=None: options[name])
        return instance

    return create_lookup


def _patch_open_url(monkeypatch, handler):
    """Replace open_url in the lookup module's namespace; return the list of
    (term, kwargs) calls recorded so far."""

    calls = []

    def record_and_handle(term, **kwargs):
        calls.append((term, kwargs))
        return handler(term, **kwargs)

    monkeypatch.setattr(url_lookup_module, 'open_url', record_and_handle)
    return calls


def test_run_split_lines_by_default(make_lookup, monkeypatch):
    lookup = make_lookup()
    calls = _patch_open_url(
        monkeypatch,
        lambda term, **kwargs: FakeResponse('héllo\nwörld\n'.encode('utf-8')))

    result = lookup.run(['http://ansible.example.com/'])

    assert result == ['héllo', 'wörld']
    assert len(calls) == 1
    term, kwargs = calls[0]
    assert term == 'http://ansible.example.com/'
    assert kwargs == {
        'validate_certs': True,
        'use_proxy': True,
        'url_username': 'someuser',
        'url_password': 'somepass',
        'headers': {'X-Test': '1'},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-test-agent',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': [],
    }


def test_run_without_split_lines_returns_whole_body(make_lookup, monkeypatch):
    lookup = make_lookup(split_lines=False)
    _patch_open_url(
        monkeypatch,
        lambda term, **kwargs: FakeResponse('héllo wörld\n'.encode('utf-8')))

    result = lookup.run(['http://ansible.example.com/'])

    assert result == ['héllo wörld\n']


def test_run_empty_response_with_split_lines(make_lookup, monkeypatch):
    lookup = make_lookup()
    _patch_open_url(monkeypatch, lambda term, **kwargs: FakeResponse(b''))

    assert lookup.run(['http://ansible.example.com/']) == []


def test_run_multiple_terms(make_lookup, monkeypatch):
    lookup = make_lookup()
    responses = {
        'http://one.example.com/': FakeResponse(b'a\nb'),
        'http://two.example.com/': FakeResponse(b'c\nd'),
    }
    calls = _patch_open_url(monkeypatch, lambda term, **kwargs: responses[term])

    result = lookup.run(['http://one.example.com/', 'http://two.example.com/'])

    assert result == ['a', 'b', 'c', 'd']
    assert [term for term, _kwargs in calls] == [
        'http://one.example.com/', 'http://two.example.com/']


def test_run_forwards_variables_and_kwargs_to_set_options(make_lookup,
                                                          monkeypatch):
    lookup = make_lookup()
    recorded = {}

    def recording_set_options(var_options=None, direct=None):
        recorded['var_options'] = var_options
        recorded['direct'] = direct

    monkeypatch.setattr(lookup, 'set_options', recording_set_options)
    _patch_open_url(monkeypatch, lambda term, **kwargs: FakeResponse(b'x'))

    lookup.run(['http://ansible.example.com/'],
               variables={'k': 'v'}, custom=42)

    assert recorded == {'var_options': {'k': 'v'}, 'direct': {'custom': 42}}


@pytest.mark.parametrize('exception, expected_prefix', [
    (HTTPError('http://ansible.example.com/', 500, 'Internal Server Error',
               {}, io.BytesIO(b'')),
     'Received HTTP error for'),
    (URLError('connection refused'),
     'Failed lookup url for'),
    (SSLValidationError('certificate verify failed'),
     "Error validating the server's certificate for"),
    (ConnectionError('timed out'),
     'Error connecting to'),
], ids=['http-error', 'url-error', 'ssl-error', 'connection-error'])
def test_run_translates_errors_to_ansible_errors(make_lookup, monkeypatch,
                                                 exception, expected_prefix):
    lookup = make_lookup()

    def raise_error(term, **kwargs):
        raise exception

    _patch_open_url(monkeypatch, raise_error)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['http://ansible.example.com/'])

    message = excinfo.value.message
    assert message.startswith(expected_prefix)
    assert 'http://ansible.example.com/' in message


def test_run_error_on_second_term_aborts(make_lookup, monkeypatch):
    lookup = make_lookup()
    responses = {'http://good.example.com/': FakeResponse(b'ok')}

    def handler(term, **kwargs):
        response = responses.get(term)
        if response is None:
            raise URLError('nope')
        return response

    _patch_open_url(monkeypatch, handler)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['http://good.example.com/', 'http://bad.example.com/'])

    assert 'Failed lookup url for http://bad.example.com/' in excinfo.value.message
