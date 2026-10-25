

# Generated at 2026-10-24 14:39:05.367449
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()
    assert lookup is not None

# Generated at 2026-10-24 14:39:08.020667
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:39:10.684415
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:39:13.336103
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:39:15.750770
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:39:18.163687
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:39:20.584761
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:39:23.001006
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:39:25.413586
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:39:27.827301
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:39:30.242191
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 14:39:42.548282
# Unit test for constructor of class LookupModule
def test_LookupModule():from ansible.plugins.lookup.url import LookupModule

# Generated at 2026-10-24 14:39:56.382330
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

# Generated at 2026-10-24 14:39:57.761222
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

# Generated at 2026-10-24 14:39:59.138302
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

# Generated at 2026-10-24 14:40:01.854793
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

# Generated at 2026-10-24 14:40:03.339773
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

# Generated at 2026-10-24 14:40:04.780220
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

# Generated at 2026-10-24 14:40:06.206319
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

# Generated at 2026-10-24 14:40:07.567812
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

# Generated at 2026-10-24 14:40:08.969785
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

# Generated at 2026-10-24 14:40:10.402293
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

# Generated at 2026-10-24 14:40:13.017500
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:15.430407
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:17.844781
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:20.258431
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:22.672187
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:25.085184
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:27.500114
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:29.911554
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:32.326238
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:34.743902
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:37.157762
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:39.572333
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:40:56.895780
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:41:34.987659
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch

# Generated at 2026-10-24 14:41:36.521394
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

# Generated at 2026-10-24 14:41:38.937689
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:00.688332
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:03.453197
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:04.785685
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

# Generated at 2026-10-24 14:42:06.117050
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

# Generated at 2026-10-24 14:42:07.548617
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

# Generated at 2026-10-24 14:42:08.981241
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

# Generated at 2026-10-24 14:42:10.334800
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

# Generated at 2026-10-24 14:42:11.695253
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

# Generated at 2026-10-24 14:42:14.232497
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:16.647577
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:19.060927
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:21.668228
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:24.082224
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:26.495714
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:28.910356
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:31.322822
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:33.736400
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:36.151299
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:38.562089
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:40.974525
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:43.386743
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:45.812596
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:48.226223
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:42:49.826534
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

# Generated at 2026-10-24 14:42:52.299872
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

# Generated at 2026-10-24 14:42:53.730588
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

# Generated at 2026-10-24 14:42:55.049555
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

# Generated at 2026-10-24 14:42:56.700944
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

# Generated at 2026-10-24 14:42:58.017881
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

# Generated at 2026-10-24 14:42:59.336077
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

# Generated at 2026-10-24 14:43:00.660111
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

# Generated at 2026-10-24 14:43:01.979960
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

# Generated at 2026-10-24 14:43:03.305948
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

# Generated at 2026-10-24 14:43:04.635620
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

# Generated at 2026-10-24 14:43:05.950285
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

# Generated at 2026-10-24 14:43:08.009798
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

# Generated at 2026-10-24 14:43:09.334128
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

# Generated at 2026-10-24 14:43:10.649868
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

# Generated at 2026-10-24 14:43:11.963119
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

# Generated at 2026-10-24 14:43:14.470921
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:17.050020
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:19.561956
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:21.974470
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:24.556324
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:26.971697
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:29.388880
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:31.801453
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:34.466436
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:36.877249
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:39.289752
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:41.702622
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:44.114593
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:46.527730
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:48.941111
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:43:50.322774
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

# Generated at 2026-10-24 14:43:53.370699
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

# Generated at 2026-10-24 14:43:54.762234
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

# Generated at 2026-10-24 14:43:56.076773
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

# Generated at 2026-10-24 14:43:57.529899
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

# Generated at 2026-10-24 14:43:58.889176
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

# Generated at 2026-10-24 14:44:00.216467
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

# Generated at 2026-10-24 14:44:01.532290
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

# Generated at 2026-10-24 14:44:02.849197
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

# Generated at 2026-10-24 14:44:04.181341
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

# Generated at 2026-10-24 14:44:05.616542
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

# Generated at 2026-10-24 14:44:14.209757
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:16.624998
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:19.038783
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:21.451342
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:23.863540
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:26.287655
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:28.699585
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:31.113038
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:33.779334
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:36.192109
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:38.605948
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:41.019668
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:43.432825
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:45.851038
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:44:48.262221
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:06.034579
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:08.685931
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:11.459658
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:12.786851
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

# Generated at 2026-10-24 14:45:14.118067
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

# Generated at 2026-10-24 14:45:15.440919
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

# Generated at 2026-10-24 14:45:16.888977
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

# Generated at 2026-10-24 14:45:30.369199
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:32.872674
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:35.286781
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:37.703863
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:40.114795
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:42.529332
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:44.943944
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:47.358135
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:49.770700
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:52.187262
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:54.597358
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:57.009789
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:45:59.421410
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:01.835233
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:04.252183
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:06.663619
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:09.077079
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:11.492850
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:13.909014
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:16.321364
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:19.051065
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:46:20.371692
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

# Generated at 2026-10-24 14:46:21.682985
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

# Generated at 2026-10-24 14:46:23.007488
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

# Generated at 2026-10-24 14:46:49.869719
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

# Generated at 2026-10-24 14:46:51.300773
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

# Generated at 2026-10-24 14:46:52.623105
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

# Generated at 2026-10-24 14:46:53.935264
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

# Generated at 2026-10-24 14:46:55.313689
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

# Generated at 2026-10-24 14:46:56.627959
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

# Generated at 2026-10-24 14:46:59.134699
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:01.667063
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:04.535729
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:06.947642
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:09.679362
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:12.097773
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:14.631072
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:17.046187
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:19.459366
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:21.876853
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:24.287515
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:47:26.700541
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:18.443627
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

# Generated at 2026-10-24 14:48:19.760860
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

# Generated at 2026-10-24 14:48:21.071451
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

# Generated at 2026-10-24 14:48:22.382425
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

# Generated at 2026-10-24 14:48:24.799960
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:27.214698
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:29.624315
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:32.038072
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:34.449797
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:36.862976
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:39.409961
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:41.821224
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:44.235491
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:46.648899
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:49.061115
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:51.475037
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:53.889650
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:56.743537
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:48:59.507544
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 14:49:00.845471
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