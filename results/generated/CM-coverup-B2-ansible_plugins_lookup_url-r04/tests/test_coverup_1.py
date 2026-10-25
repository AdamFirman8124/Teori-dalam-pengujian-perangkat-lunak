# file: project/ansible/plugins/lookup/url.py:186-224
# asked: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}
# gained: {"lines": [190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 219, 220, 221, 223, 224], "branches": [[193, 194], [193, 224], [219, 220], [219, 223], [220, 193], [220, 221]]}

import pytest
from unittest.mock import MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


class FakeResponse(object):
    """Minimal stand-in for the object returned by open_url()."""
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
    'http_agent': 'ansible-test-agent',
    'force_basic_auth': False,
    'follow_redirects': 'urllib2',
    'use_gssapi': False,
    'unix_socket': None,
    'ca_path': None,
    'unredirected_headers': [],
    'split_lines': True,
}


def _make_lookup(monkeypatch, options=None, open_url_mock=None):
    """Build a LookupModule with option access stubbed out and open_url patched."""
    lookup = LookupModule()
    opts = dict(DEFAULT_OPTIONS)
    if options:
        opts.update(options)

    # Avoid the real config-manager machinery; the run() code path only
    # needs set_options() to be callable and get_option() to return values.
    monkeypatch.setattr(lookup, 'set_options',
                        lambda var_options=None, direct=None: None)
    monkeypatch.setattr(lookup, 'get_option', lambda key: opts[key])

    if open_url_mock is not None:
        monkeypatch.setattr('ansible.plugins.lookup.url.open_url', open_url_mock)
    return lookup


def test_run_split_lines_default(monkeypatch):
    """Default split_lines=True: response body is split into separate lines."""
    mock_open = MagicMock(return_value=FakeResponse(b'line1\nline2\n'))
    lookup = _make_lookup(monkeypatch, open_url_mock=mock_open)

    result = lookup.run(['http://example.com'])

    assert result == ['line1', 'line2']
    mock_open.assert_called_once_with(
        'http://example.com',
        validate_certs=True,
        use_proxy=True,
        url_username='user',
        url_password='pass',
        headers={'X-Test': '1'},
        force=False,
        timeout=10,
        http_agent='ansible-test-agent',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_run_no_split_lines(monkeypatch):
    """split_lines=False: the whole body is returned as a single string."""
    mock_open = MagicMock(return_value=FakeResponse(b'line1\nline2'))
    lookup = _make_lookup(monkeypatch, options={'split_lines': False},
                          open_url_mock=mock_open)

    result = lookup.run(['http://example.com'])

    assert result == ['line1\nline2']
    mock_open.assert_called_once()


def test_run_multiple_terms(monkeypatch):
    """Every term is fetched and its lines appended in order."""
    responses = [FakeResponse(b'a\nb'), FakeResponse(b'c\nd')]
    mock_open = MagicMock(side_effect=responses)
    lookup = _make_lookup(monkeypatch, open_url_mock=mock_open)

    result = lookup.run(['http://one.example.com', 'http://two.example.com'])

    assert result == ['a', 'b', 'c', 'd']
    assert mock_open.call_count == 2
    assert mock_open.call_args_list[0][0][0] == 'http://one.example.com'
    assert mock_open.call_args_list[1][0][0] == 'http://two.example.com'


def test_run_decodes_bytes_to_text(monkeypatch):
    """Non-ASCII bytes are decoded to text, not returned as bytes."""
    mock_open = MagicMock(return_value=FakeResponse(u'héllo\nwörld'.encode('utf-8')))
    lookup = _make_lookup(monkeypatch, open_url_mock=mock_open)

    result = lookup.run(['http://example.com'])

    assert result == [u'héllo', u'wörld']
    assert all(isinstance(line, str) for line in result)


@pytest.mark.parametrize('exc,expected_fragment', [
    (HTTPError('http://example.com', 500, 'Internal Server Error', None, None),
     'Received HTTP error for http://example.com'),
    (URLError('connection refused'),
     'Failed lookup url for http://example.com'),
    (SSLValidationError('bad certificate'),
     "Error validating the server's certificate for http://example.com"),
    (ConnectionError('timed out'),
     'Error connecting to http://example.com'),
])
def test_run_exception_handling(monkeypatch, exc, expected_fragment):
    """Each expected exception type is converted to an AnsibleError."""
    def raise_error(*args, **kwargs):
        raise exc

    lookup = _make_lookup(monkeypatch, open_url_mock=raise_error)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['http://example.com'])

    assert expected_fragment in str(excinfo.value)
