

# Generated at 2026-11-02 00:00:01.319462
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = DictDataLoader({})
    lookup_plugin = LookupModule(loader)
    assert lookup_plugin is not None
    assert callable(lookup_plugin.run)

# Generated at 2026-11-02 00:01:21.602656
# Unit test for method run of class LookupModule

# Generated at 2026-11-02 00:02:21.609840
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import patch

# Generated at 2026-11-02 00:03:58.685107
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup_plugin = LookupModule()
    assert lookup_plugin is not None
    assert isinstance(lookup_plugin, LookupModule)
    assert callable(getattr(lookup_plugin, 'run', None))

# Generated at 2026-11-02 00:04:37.190007
# Unit test for method run of class LookupModule

# Generated at 2026-11-02 00:05:29.106893
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    from ansible.plugins.lookup.url import LookupModule

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
        'split_lines': True,
    }
    lookup.get_option = options.get

    fake_response = MagicMock()
    fake_response.read.return_value = b'line one\nline two\n'

    with patch('ansible.plugins.lookup.url.open_url', return_value=fake_response) as mock_open:
        result = lookup.run(['http://example.com/data.txt'])

    assert result == ['line one', 'line two']
    mock_open.assert_called_once_with(
        'http://example.com/data.txt',
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

    options['split_lines'] = False
    with patch('ansible.plugins.lookup.url.open_url', return_value=fake_response):
        result = lookup.run(['http://example.com/data.txt'])

    assert result == ['line one\nline two\n']

# Generated at 2026-11-02 00:06:16.274294
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3\n'

    lookup = _get_lookup()

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as fake_open_url:
        result = lookup.run(['http://example.com/data.txt'])

    assert result == ['line1', 'line2', 'line3']
    fake_open_url.assert_called_once_with(
        'http://example.com/data.txt',
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


def test_LookupModule_run_split_lines_false():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    lookup = _get_lookup(split_lines=False)

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = lookup.run(['http://example.com/data.txt'])

    assert result == ['line1\nline2']


def test_LookupModule_run_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'content'

    lookup = _get_lookup(split_lines=False)

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = lookup.run(['http://one.example.com', 'http://two.example.com'])

    assert result == ['content', 'content']


def test_LookupModule_run_http_error():
    lookup = _get_lookup()
    error = HTTPError('http://example.com', 500, 'Internal Server Error', None, None)

    with patch('ansible.plugins.lookup.url.open_url', side_effect=error):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['http://example.com'])

    assert 'Received HTTP error' in str(excinfo.value)


def test_LookupModule_run_url_error():
    lookup = _get_lookup()

    with patch('ansible.plugins.lookup.url.open_url', side_effect=URLError('no route to host')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['http://example.com'])

    assert 'Failed lookup url' in str(excinfo.value)


def test_LookupModule_run_ssl_validation_error():
    lookup = _get_lookup()

    with patch('ansible.plugins.lookup.url.open_url', side_effect=SSLValidationError('bad certificate')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['https://example.com'])

    assert "Error validating the server's certificate" in str(excinfo.value)


def test_LookupModule_run_connection_error():
    lookup = _get_lookup()

    with patch('ansible.plugins.lookup.url.open_url', side_effect=ConnectionError('connection refused')):
        with pytest.raises(AnsibleError) as excinfo:
            lookup.run(['http://example.com'])

    assert 'Error connecting to' in str(excinfo.value)


def test_LookupModule_run_custom_options():
    response = MagicMock()
    response.read.return_value = b'ok'

    lookup = _get_lookup(username='bob', password='hunter2', timeout=5, validate_certs=False)

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as fake_open_url:
        result = lookup.run(['https://example.com/file.txt'])

    assert result == ['ok']
    kwargs = fake_open_url.call_args[1]
    assert kwargs['url_username'] == 'bob'
    assert kwargs['url_password'] == 'hunter2'
    assert kwargs['timeout'] == 5
    assert kwargs['validate_certs'] is False

# Generated at 2026-11-02 00:08:37.628417
# Unit test for method run of class LookupModule