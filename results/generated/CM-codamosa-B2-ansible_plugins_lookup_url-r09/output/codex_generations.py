

# Generated at 2026-11-02 14:41:11.478454
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    import pytest

    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError
    from ansible.plugins.lookup.url import LookupModule

    def _make_lookup(mocks=None):
        """Create a LookupModule with mocked set_options/get_option."""
        lookup = LookupModule()
        lookup._loader = MagicMock()
        lookup._templar = MagicMock()
        lookup.set_options = MagicMock()
        return lookup

    def _configure_options(lookup, **overrides):
        """Configure get_option return values."""
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
            'split_lines': True,
        }
        options.update(overrides)
        lookup.get_option = lambda name: options[name]

    class FakeResponse(object):
        def __init__(self, data):
            self._data = data

        def read(self):
            return self._data

    # Test 1: default behavior (split_lines=True) splits content into lines
    lookup = _make_lookup()
    _configure_options(lookup, split_lines=True)
    with patch('ansible.plugins.lookup.url.open_url',
               return_value=FakeResponse(b'line1\nline2\nline3')) as mock_open:
        result = lookup.run(['http://example.com/file.txt'])
        assert result == ['line1', 'line2', 'line3']
        mock_open.assert_called_once_with(
            'http://example.com/file.txt',
            validate_certs=True,
            use_proxy=True,
            url_username=None,
            url_password=None,
            headers={},
            force=False,
            timeout=10,
            http_agent='ansible-httpget',
            force_basic_auth=False,
            follow_redirects='urllib2',
            use_gssapi=False,
            unix_socket=None,
            ca_path=None,
            unredirected_headers=None,
        )

    # Test 2: split_lines=False returns a single blob
    lookup = _make_lookup()
    _configure_options(lookup, split_lines=False)
    with patch('ansible.plugins.lookup.url.open_url',
               return_value=FakeResponse(b'line1\nline2\nline3')):
        result = lookup.run(['http://example.com/file.txt'])
        assert result == ['line1\nline2\nline3']

    # Test 3: multiple terms are processed in order
    lookup = _make_lookup()
    _configure_options(lookup, split_lines=False)
    with patch('ansible.plugins.lookup.url.open_url',
               side_effect=[FakeResponse(b'first'), FakeResponse(b'second')]):
        result = lookup.run(['http://example.com/1', 'http://example.com/2'])
        assert result == ['first', 'second']

    # Test 4: options are propagated to open_url
    lookup = _make_lookup()
    _configure_options(lookup,
                       validate_certs=False,
                       use_proxy=False,
                       username='bob',
                       password='hunter2',
                       headers={'X-Test': 'value'},
                       force=True,
                       timeout=5,
                       http_agent='custom-agent',
                       force_basic_auth=True,
                       follow_redirects='all',
                       use_gssapi=True,
                       unix_socket='/tmp/sock',
                       ca_path='/tmp/ca.pem',
                       unredirected_headers=['Authorization'])
    with patch('ansible.plugins.lookup.url.open_url',
               return_value=FakeResponse(b'data')) as mock_open:
        lookup.run(['http://example.com/'])
        kwargs = mock_open.call_args[1]
        assert kwargs['validate_certs'] is False
        assert kwargs['use_proxy'] is False
        assert kwargs['url_username'] == 'bob'
        assert kwargs['url_password'] == 'hunter2'
        assert kwargs['headers'] == {'X-Test': 'value'}
        assert kwargs['force'] is True
        assert kwargs['timeout'] == 5
        assert kwargs['http_agent'] == 'custom-agent'
        assert kwargs['force_basic_auth'] is True
        assert kwargs['follow_redirects'] == 'all'
        assert kwargs['use_gssapi'] is True
        assert kwargs['unix_socket'] == '/tmp/sock'
        assert kwargs['ca_path'] == '/tmp/ca.pem'
        assert kwargs['unredirected_headers'] == ['Authorization']

    # Test 5: HTTPError raises AnsibleError
    lookup = _make_lookup()
    _configure_options(lookup)
    with patch('ansible.plugins.lookup.url.open_url',
               side_effect=HTTPError('http://example.com/', 404, 'Not Found', None, None)):
        with pytest.raises(AnsibleError, match='Received HTTP error'):
            lookup.run(['http://example.com/missing'])

    # Test 6: URLError raises AnsibleError
    lookup = _make_lookup()
    _configure_options(lookup)
    with patch('ansible.plugins.lookup.url.open_url',
               side_effect=URLError('connection refused')):
        with pytest.raises(AnsibleError, match='Failed lookup url'):
            lookup.run(['http://example.com/'])

    # Test 7: SSLValidationError raises AnsibleError
    lookup = _make_lookup()
    _configure_options(lookup)
    with patch('ansible.plugins.lookup.url.open_url',
               side_effect=SSLValidationError('bad certificate')):
        with pytest.raises(AnsibleError, match="Error validating the server's certificate"):
            lookup.run(['https://example.com/'])

    # Test 8: ConnectionError raises AnsibleError
    lookup = _make_lookup()
    _configure_options(lookup)
    with patch('ansible.plugins.lookup.url.open_url',
               side_effect=ConnectionError('timed out')):
        with pytest.raises(AnsibleError, match='Error connecting to'):
            lookup.run(['http://example.com/'])

    # Test 9: binary content is decoded to text
    lookup = _make_lookup()
    _configure_options(lookup, split_lines=True)
    with patch('ansible.plugins.lookup.url.open_url',
               return_value=FakeResponse(u'caf\u00e9\nna\u00efve'.encode('utf-8'))):
        result = lookup.run(['http://example.com/unicode'])
        assert result == [u'caf\u00e9', u'na\u00efve']

# Generated at 2026-11-02 14:42:40.279627
# Unit test for method run of class LookupModule
def test_LookupModule_run():import pytest
from unittest.mock import MagicMock, patch

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError
from ansible.plugins.lookup.url import LookupModule


def _get_lookup(options=None):
    """Create a LookupModule with stubbed option handling."""
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
    lookup.get_option = MagicMock(side_effect=lambda name: opts[name])
    return lookup


def test_run_splits_lines_by_default():
    response = MagicMock()
    response.read.return_value = b"line1\nline2\nline3"
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = lookup.run(['http://example.com'])
    mock_open.assert_called_once_with(
        'http://example.com',
        validate_certs=True,
        use_proxy=True,
        url_username=None,
        url_password=None,
        headers={},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=None)
    assert result == ['line1', 'line2', 'line3']


def test_run_no_split_lines_returns_blob():
    response = MagicMock()
    response.read.return_value = b"line1\nline2"
    lookup = _get_lookup({'split_lines': False})
    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = lookup.run(['http://example.com'])
    assert result == ['line1\nline2']


def test_run_multiple_terms():
    r1, r2 = MagicMock(), MagicMock()
    r1.read.return_value = b"a\nb"
    r2.read.return_value = b"c"
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url', side_effect=[r1, r2]):
        result = lookup.run(['http://one', 'http://two'])
    assert result == ['a', 'b', 'c']


def test_run_decodes_bytes_to_text():
    response = MagicMock()
    response.read.return_value = u"caf\u00e9".encode('utf-8')
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = lookup.run(['http://example.com'])
    assert result == [u"caf\u00e9"]


def test_run_http_error_raises_ansible_error():
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url',
               side_effect=HTTPError('http://example.com', 500, 'Server Error', {}, None)):
        with pytest.raises(AnsibleError, match="Received HTTP error for http://example.com"):
            lookup.run(['http://example.com'])


def test_run_url_error_raises_ansible_error():
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url', side_effect=URLError('no route to host')):
        with pytest.raises(AnsibleError, match="Failed lookup url for http://example.com"):
            lookup.run(['http://example.com'])


def test_run_ssl_validation_error_raises_ansible_error():
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url', side_effect=SSLValidationError('bad certificate')):
        with pytest.raises(AnsibleError, match="Error validating the server's certificate for http://example.com"):
            lookup.run(['http://example.com'])


def test_run_connection_error_raises_ansible_error():
    lookup = _get_lookup()
    with patch('ansible.plugins.lookup.url.open_url', side_effect=ConnectionError('connection refused')):
        with pytest.raises(AnsibleError, match="Error connecting to http://example.com"):
            lookup.run(['http://example.com'])


def test_run_passes_custom_options_to_open_url():
    response = MagicMock()
    response.read.return_value = b"data"
    lookup = _get_lookup({
        'username': 'bob',
        'password': 'hunter2',
        'force_basic_auth': True,
        'headers': {'X-Test': '1'},
        'timeout': 5.0,
        'validate_certs': False,
        'use_proxy': False,
    })
    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        lookup.run(['https://example.com'])
    kwargs = mock_open.call_args[1]
    assert kwargs['url_username'] == 'bob'
    assert kwargs['url_password'] == 'hunter2'
    assert kwargs['force_basic_auth'] is True
    assert kwargs['headers'] == {'X-Test': '1'}
    assert kwargs['timeout'] == 5.0
    assert kwargs['validate_certs'] is False
    assert kwargs['use_proxy'] is False

# Generated at 2026-11-02 14:45:16.281888
# Unit test for method run of class LookupModule
def test_LookupModule_run():import unittest
from unittest.mock import patch, MagicMock

from ansible.errors import AnsibleError
from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
from ansible.module_utils.urls import ConnectionError, SSLValidationError

from ansible.plugins.lookup.url import LookupModule


class FakeResponse(object):
    def __init__(self, content=b'line1\nline2\nline3'):
        self.content = content

    def read(self):
        return self.content


def _make_lookup(**kwargs):
    lookup = LookupModule()
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
        'split_lines': True,
    }
    options.update(kwargs)
    lookup.set_options = lambda var_options=None, direct=None: None
    lookup.get_option = lambda option: options[option]
    return lookup


@patch('ansible.plugins.lookup.url.open_url')
def test_run_single_term_split_lines(mock_open_url):
    mock_open_url.return_value = FakeResponse(b'line1\nline2\nline3')
    lookup = _make_lookup()
    result = lookup.run(['http://example.com'])
    assert result == ['line1', 'line2', 'line3']
    mock_open_url.assert_called_once_with(
        'http://example.com',
        validate_certs=True,
        use_proxy=True,
        url_username=None,
        url_password=None,
        headers={},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=None,
    )


@patch('ansible.plugins.lookup.url.open_url')
def test_run_no_split_lines(mock_open_url):
    mock_open_url.return_value = FakeResponse(b'line1\nline2\nline3')
    lookup = _make_lookup(split_lines=False)
    result = lookup.run(['http://example.com'])
    assert result == ['line1\nline2\nline3']


@patch('ansible.plugins.lookup.url.open_url')
def test_run_multiple_terms(mock_open_url):
    mock_open_url.return_value = FakeResponse(b'a\nb')
    lookup = _make_lookup()
    result = lookup.run(['http://example.com/1', 'http://example.com/2'])
    assert result == ['a', 'b', 'a', 'b']
    assert mock_open_url.call_count == 2


@patch('ansible.plugins.lookup.url.open_url')
def test_run_empty_content(mock_open_url):
    mock_open_url.return_value = FakeResponse(b'')
    lookup = _make_lookup()
    result = lookup.run(['http://example.com'])
    assert result == []


@patch('ansible.plugins.lookup.url.open_url')
def test_run_with_auth_options(mock_open_url):
    mock_open_url.return_value = FakeResponse(b'data')
    lookup = _make_lookup(username='bob', password='hunter2', force_basic_auth=True)
    lookup.run(['http://example.com'])
    args, kwargs = mock_open_url.call_args
    assert kwargs['url_username'] == 'bob'
    assert kwargs['url_password'] == 'hunter2'
    assert kwargs['force_basic_auth'] is True


@patch('ansible.plugins.lookup.url.open_url')
def test_run_with_headers(mock_open_url):
    mock_open_url.return_value = FakeResponse(b'data')
    lookup = _make_lookup(headers={'header1': 'value1'})
    lookup.run(['http://example.com'])
    args, kwargs = mock_open_url.call_args
    assert kwargs['headers'] == {'header1': 'value1'}


def test_run_http_error():
    with patch('ansible.plugins.lookup.url.open_url') as mock_open_url:
        mock_open_url.side_effect = HTTPError('http://example.com', 500, 'Server Error', None, None)
        lookup = _make_lookup()
        try:
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Received HTTP error' in str(e)
        else:
            raise AssertionError('AnsibleError not raised')


def test_run_url_error():
    with patch('ansible.plugins.lookup.url.open_url') as mock_open_url:
        mock_open_url.side_effect = URLError('connection refused')
        lookup = _make_lookup()
        try:
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Failed lookup url' in str(e)
        else:
            raise AssertionError('AnsibleError not raised')


def test_run_ssl_validation_error():
    with patch('ansible.plugins.lookup.url.open_url') as mock_open_url:
        mock_open_url.side_effect = SSLValidationError('bad cert')
        lookup = _make_lookup()
        try:
            lookup.run(['https://example.com'])
        except AnsibleError as e:
            assert "Error validating the server's certificate" in str(e)
        else:
            raise AssertionError('AnsibleError not raised')


def test_run_connection_error():
    with patch('ansible.plugins.lookup.url.open_url') as mock_open_url:
        mock_open_url.side_effect = ConnectionError('timed out')
        lookup = _make_lookup()
        try:
            lookup.run(['http://example.com'])
        except AnsibleError as e:
            assert 'Error connecting to' in str(e)
        else:
            raise AssertionError('AnsibleError not raised')


@patch('ansible.plugins.lookup.url.open_url')
def test_run_decodes_bytes_to_text(mock_open_url):
    mock_open_url.return_value = FakeResponse(u'caf\u00e9'.encode('utf-8'))
    lookup = _make_lookup(split_lines=False)
    result = lookup.run(['http://example.com'])
    assert result == [u'caf\u00e9']
    assert all(isinstance(item, str) for item in result)