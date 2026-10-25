

# Generated at 2026-10-24 14:54:49.200668
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:54:51.614729
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:54:54.029142
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:54:56.447124
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:54:58.856036
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:01.268675
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:03.682334
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:06.096667
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:08.509346
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:10.922271
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:55:13.335252
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:55:15.748467
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:55:18.160107
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:55:20.578559
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:55:22.092701
# Unit test for constructor of class LookupModule
def test_LookupModule():from ansible.plugins.lookup.url import LookupModule

# Generated at 2026-10-24 14:55:23.411544
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:24.773706
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:26.089656
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:27.473781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:29.037549
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:30.358643
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:31.666722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:33.033269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:34.338837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:35.721110
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:37.036305
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:55:39.570726
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:41.982367
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:44.393943
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:46.806341
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:49.220017
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:51.631157
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:54.205472
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:56.620624
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:55:59.034095
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:01.447110
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:03.860111
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:06.272642
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:08.684858
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:11.097112
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:13.509090
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:15.922479
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:18.335681
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:20.747980
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:23.159792
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:25.571787
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:27.984162
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:30.395594
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:32.805829
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:35.217889
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:37.628724
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:40.040795
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:42.454441
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:44.867536
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:47.280280
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:49.693977
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:52.107105
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:54.520647
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:56.936030
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:56:59.346296
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:01.757144
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:04.170797
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:06.582942
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:08.995401
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:11.412203
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:29.143610
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:31.742523
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:34.149919
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:36.688314
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:39.101612
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:41.514538
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:44.070272
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:46.592832
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:49.005186
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:51.417678
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:53.831653
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:56.242909
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:57:58.654709
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:01.067761
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:03.479923
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:05.891896
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:08.304323
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:10.716257
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:13.126832
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:15.542895
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:17.956313
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:20.368991
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:22.781874
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:25.196487
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:27.611165
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:30.028686
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:32.442077
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:34.855215
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:37.267505
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:39.682140
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:42.094360
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:44.507229
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:46.924468
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:49.333936
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:51.749341
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:54.160786
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:56.573530
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:58:59.139522
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:01.814649
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:03.144095
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:04.477354
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:05.780159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:07.253232
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:08.798190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:10.530274
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:11.893838
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:13.601531
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:15.278462
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:16.567814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:17.884165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:19.206021
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:20.601081
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:24.149868
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:25.521611
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:26.833037
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:28.155425
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:29.781511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:31.291184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 14:59:33.894172
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:36.306653
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:38.720892
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:41.266733
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:43.679597
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:46.211347
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:48.629180
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:51.051361
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:53.574951
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:55.989692
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:59:58.403713
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:00.816352
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:07.245818
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:10.103570
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:12.855785
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:14.223529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:15.531221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:16.914974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:20.159456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:21.907287
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:23.266812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:24.582417
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:25.909694
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:27.232659
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:00:38.825194
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:41.239217
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:43.654317
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:46.289149
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:48.706103
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:51.120676
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:53.532214
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:55.946031
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:00:58.359876
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:00.774616
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:03.188629
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:05.601878
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:08.016381
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:10.432599
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:12.844268
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:15.258067
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:17.672268
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:20.086408
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:22.499008
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:24.913967
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:27.327114
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:29.740142
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:32.154689
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:34.567361
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:36.981700
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:39.394449
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:41.807585
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:44.221934
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:46.634741
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:01:49.049100
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:02:11.356951
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:12.671329
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:14.039210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:15.353335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:16.715065
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:18.071668
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:19.385786
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:20.700672
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:22.310644
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:02:23.629477
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:16.068989
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:03:18.482896
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:03:21.111096
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 15:03:22.538021
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:23.949181
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:25.406928
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:26.791225
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:28.164815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:29.478426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:30.791927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:32.367876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])

# Generated at 2026-10-24 15:03:33.682237
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    response = MagicMock()
    response.read.return_value = b'line1\nline2\nline3'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response) as mock_open:
        result = _lookup().run(['https://example.com/file.txt'], variables={})

    assert result == ['line1', 'line2', 'line3']
    mock_open.assert_called_once_with(
        'https://example.com/file.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='bob',
        url_password='hunter2',
        headers={'header1': 'value1'},
        force=False,
        timeout=10,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )


def test_LookupModule_run_no_split_lines_and_multiple_terms():
    response = MagicMock()
    response.read.return_value = b'line1\nline2'

    with patch('ansible.plugins.lookup.url.open_url', return_value=response):
        result = _lookup({'split_lines': False}).run(
            ['https://example.com/a', 'https://example.com/b'])

    assert result == ['line1\nline2', 'line1\nline2']


@pytest.mark.parametrize('exc,match', [
    (HTTPError('https://example.com', 404, 'Not Found', {}, None), 'Received HTTP error'),
    (URLError('boom'), 'Failed lookup url'),
    (SSLValidationError('bad cert'), "validating the server's certificate"),
    (UrlConnectionError('refused'), 'Error connecting'),
])
def test_LookupModule_run_errors(exc, match):
    with patch('ansible.plugins.lookup.url.open_url', side_effect=exc):
        with pytest.raises(AnsibleError, match=match):
            _lookup().run(['https://example.com/file.txt'])