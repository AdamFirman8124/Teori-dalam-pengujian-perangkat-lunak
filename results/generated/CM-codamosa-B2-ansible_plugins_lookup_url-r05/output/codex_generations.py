

# Generated at 2026-11-02 17:44:57.844598
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from unittest.mock import MagicMock, patch
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError
    from ansible.plugins.lookup.url import LookupModule

    def _make_lookup(split_lines=True):
        lookup = LookupModule()
        lookup.set_options = MagicMock()
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
        lookup.get_option = MagicMock(side_effect=lambda opt, **kw: options[opt])
        return lookup

    with patch('ansible.plugins.lookup.url.open_url') as mock_open, \
            patch('ansible.plugins.lookup.url.display'):

        # Default behaviour: split_lines=True -> list of lines
        response = MagicMock()
        response.read.return_value = b'line1\nline2\nline3\n'
        mock_open.return_value = response
        lookup = _make_lookup()
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

        # split_lines=False -> single blob per term, multiple terms
        mock_open.reset_mock()
        response.read.return_value = b'whole content'
        lookup = _make_lookup(split_lines=False)
        result = lookup.run(['http://example.com/one', 'http://example.com/two'])
        assert result == ['whole content', 'whole content']
        assert mock_open.call_count == 2

        # HTTPError -> AnsibleError
        mock_open.reset_mock()
        mock_open.return_value = response
        mock_open.side_effect = HTTPError('http://example.com', 500, 'server error', None, None)
        lookup = _make_lookup()
        with pytest.raises(AnsibleError) as exc:
            lookup.run(['http://example.com'])
        assert 'Received HTTP error' in str(exc.value)

        # URLError -> AnsibleError
        mock_open.side_effect = URLError('name resolution failed')
        with pytest.raises(AnsibleError) as exc:
            lookup.run(['http://example.com'])
        assert 'Failed lookup url' in str(exc.value)

        # SSLValidationError -> AnsibleError
        mock_open.side_effect = SSLValidationError('bad certificate')
        with pytest.raises(AnsibleError) as exc:
            lookup.run(['http://example.com'])
        assert "Error validating the server's certificate" in str(exc.value)

        # ConnectionError -> AnsibleError
        mock_open.side_effect = ConnectionError('connection refused')
        with pytest.raises(AnsibleError) as exc:
            lookup.run(['http://example.com'])
        assert 'Error connecting to' in str(exc.value)

# Generated at 2026-11-02 17:47:19.051899
# Unit test for constructor of class LookupModule
def test_LookupModule():
    # Constructor should not require any arguments
    lookup = LookupModule()

    # It should produce a proper LookupModule instance deriving from LookupBase
    assert lookup is not None
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

    # The lookup entry point should be available
    assert callable(lookup.run)

    # Separate instantiations should be independent objects
    another = LookupModule()
    assert another is not lookup

# Generated at 2026-11-02 17:49:02.796214
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None
    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)