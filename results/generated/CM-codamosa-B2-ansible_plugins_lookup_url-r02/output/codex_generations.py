

# Generated at 2026-11-02 12:28:01.810597
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup_plugin = LookupModule()
    assert lookup_plugin is not None
    assert isinstance(lookup_plugin, LookupModule)
    assert isinstance(lookup_plugin, LookupBase)
    assert callable(lookup_plugin.run)

# Generated at 2026-11-02 12:30:48.429090
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError
    from ansible.plugins.lookup.url import LookupModule

    with patch('ansible.plugins.lookup.url.open_url') as mock_open_url:
        mock_response = MagicMock()
        mock_response.read.return_value = b'line1\nline2\nline3\n'
        mock_open_url.return_value = mock_response

        lookup = LookupModule()

        defaults = {
            'validate_certs': True,
            'split_lines': True,
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
        }
        lookup.set_options = MagicMock()
        lookup.get_option = MagicMock(side_effect=lambda opt: defaults[opt])

        # Default behavior: split_lines=True returns a list of lines
        result = lookup.run(['http://example.com/file.txt'])
        assert result == ['line1', 'line2', 'line3']
        mock_open_url.assert_called_once_with(
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
            unredirected_headers=None)

        # split_lines=False returns a single text blob
        defaults['split_lines'] = False
        mock_open_url.reset_mock()
        result = lookup.run(['http://example.com/file.txt'])
        assert result == ['line1\nline2\nline3\n']
        assert mock_open_url.call_count == 1

        # Multiple terms accumulate results in order
        defaults['split_lines'] = True
        mock_open_url.reset_mock()
        result = lookup.run(['http://example.com/a', 'http://example.com/b'])
        assert result == ['line1', 'line2', 'line3', 'line1', 'line2', 'line3']
        assert mock_open_url.call_count == 2

        # HTTPError is converted to AnsibleError
        mock_open_url.reset_mock()
        mock_open_url.side_effect = HTTPError('http://example.com', 500, 'Server Error', None, None)
        try:
            lookup.run(['http://example.com'])
            raise AssertionError("Expected AnsibleError for HTTPError")
        except AnsibleError as e:
            assert 'Received HTTP error' in str(e)

        # URLError is converted to AnsibleError
        mock_open_url.side_effect = URLError('connection refused')
        try:
            lookup.run(['http://example.com'])
            raise AssertionError("Expected AnsibleError for URLError")
        except AnsibleError as e:
            assert 'Failed lookup url' in str(e)

        # SSLValidationError is converted to AnsibleError
        mock_open_url.side_effect = SSLValidationError('bad certificate')
        try:
            lookup.run(['http://example.com'])
            raise AssertionError("Expected AnsibleError for SSLValidationError")
        except AnsibleError as e:
            assert "Error validating the server's certificate" in str(e)

        # ConnectionError is converted to AnsibleError
        mock_open_url.side_effect = ConnectionError('connection failure')
        try:
            lookup.run(['http://example.com'])
            raise AssertionError("Expected AnsibleError for ConnectionError")
        except AnsibleError as e:
            assert 'Error connecting to' in str(e)

        mock_open_url.side_effect = None

# Generated at 2026-11-02 12:35:32.414333
# Unit test for method run of class LookupModule