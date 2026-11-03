

# Generated at 2026-11-02 12:08:22.207112
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock, patch

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _make_lookup(options=None):
    lookup = LookupModule()
    opts = {
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
        'split_lines': True,
    }
    if options:
        opts.update(options)
    lookup.set_options = MagicMock()
    lookup.get_option = lambda name: opts[name]
    return lookup


@patch('ansible.plugins.lookup.url.open_url')
def test_run_split_lines_default(mock_open_url):
    mock_open_url.return_value = MagicMock(read=lambda: b'line1\nline2\n')
    lookup = _make_lookup()
    result = lookup.run(['http://example.com'])
    assert result == ['line1', 'line2']
    mock_open_url.assert_called_once_with('http://example.com', validate_certs=True,
                                          use_proxy=True, url_username=None,
                                          url_password=None, headers={}, force=False,
                                          timeout=10, http_agent='ansible-httpget',
                                          force_basic_auth=False,
                                          follow_redirects='urllib2',
                                          use_gssapi=False, unix_socket=None,
                                          ca_path=None, unredirected_headers=None)


@patch('ansible.plugins.lookup.url.open_url')
def test_run_no_split_lines(mock_open_url):
    mock_open_url.return_value = MagicMock(read=lambda: b'whole content')
    lookup = _make_lookup({'split_lines': False})
    result = lookup.run(['http://example.com'])
    assert result == ['whole content']


@patch('ansible.plugins.lookup.url.open_url')
def test_run_multiple_terms(mock_open_url):
    mock_open_url.return_value = MagicMock(read=lambda: b'a\nb')
    lookup = _make_lookup()
    result = lookup.run(['http://one', 'http://two'])
    assert result == ['a', 'b', 'a', 'b']
    assert mock_open_url.call_count == 2


@patch('ansible.plugins.lookup.url.open_url')
def test_run_passes_auth_options(mock_open_url):
    mock_open_url.return_value = MagicMock(read=lambda: b'x')
    lookup = _make_lookup({'username': 'bob', 'password': 'hunter2'})
    lookup.run(['http://example.com'])
    kwargs = mock_open_url.call_args[1]
    assert kwargs['url_username'] == 'bob'
    assert kwargs['url_password'] == 'hunter2'


@patch('ansible.plugins.lookup.url.open_url')
def test_run_http_error(mock_open_url):
    mock_open_url.side_effect = HTTPError('http://example.com', 500, 'boom', None, None)
    lookup = _make_lookup()
    with pytest.raises(AnsibleError) as exc:
        lookup.run(['http://example.com'])
    assert 'Received HTTP error' in to_native(exc.value)


@patch('ansible.plugins.lookup.url.open_url')
def test_run_url_error(mock_open_url):
    mock_open_url.side_effect = URLError('nope')
    lookup = _make_lookup()
    with pytest.raises(AnsibleError) as exc:
        lookup.run(['http://example.com'])
    assert 'Failed lookup url' in to_native(exc.value)


@patch('ansible.plugins.lookup.url.open_url')
def test_run_ssl_validation_error(mock_open_url):
    mock_open_url.side_effect = SSLValidationError('bad cert')
    lookup = _make_lookup()
    with pytest.raises(AnsibleError) as exc:
        lookup.run(['http://example.com'])
    assert "Error validating the server's certificate" in to_native(exc.value)


@patch('ansible.plugins.lookup.url.open_url')
def test_run_connection_error(mock_open_url):
    mock_open_url.side_effect = ConnectionError('refused')
    lookup = _make_lookup()
    with pytest.raises(AnsibleError) as exc:
        lookup.run(['http://example.com'])
    assert 'Error connecting' in to_native(exc.value)


from ansible.module_utils._text import to_native

# nonce:3c58d9b6

# Generated at 2026-11-02 12:10:08.647681
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert callable(lookup.run)

# Generated at 2026-11-02 12:13:23.762578
# Unit test for constructor of class LookupModule

# Generated at 2026-11-02 12:15:31.039970
# Unit test for constructor of class LookupModule
def test_LookupModule():from unittest.mock import MagicMock, patch