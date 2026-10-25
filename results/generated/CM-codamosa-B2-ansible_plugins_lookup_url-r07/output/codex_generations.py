

# Generated at 2026-10-25 01:13:43.919296
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-25 01:13:48.218241
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 01:13:50.635103
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 01:13:53.050383
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 01:13:55.465486
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 01:13:57.885354
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:00.303084
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:02.714321
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:05.278972
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 01:14:07.695238
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 01:14:10.112598
# Unit test for constructor of class LookupModule

# Generated at 2026-10-25 01:14:44.848147
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, call


# Unit test for method run of class LookupModule
def test_LookupModule_run(monkeypatch):
    lookup = LookupModule()

    options = {
        'validate_certs': True,
        'use_proxy': True,
        'username': 'user',
        'password': 'secret',
        'headers': {'X-Test': 'value'},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': [],
        'split_lines': True,
    }

    set_options = Mock()
    monkeypatch.setattr(lookup, 'set_options', set_options)
    monkeypatch.setattr(lookup, 'get_option', options.__getitem__)

    first_response = Mock()
    first_response.read.return_value = b'first line\nsecond line\n'

    second_response = Mock()
    second_response.read.return_value = b'third line\nfourth line\n'

    mocked_open_url = Mock(side_effect=[first_response, second_response])
    monkeypatch.setitem(
        LookupModule.run.__globals__,
        'open_url',
        mocked_open_url,
    )

    variables = {'inventory_hostname': 'test-host'}
    terms = [
        'https://example.com/first',
        'https://example.com/second',
    ]

    result = lookup.run(terms, variables=variables, split_lines=True)

    assert result == [
        'first line',
        'second line',
        'third line',
        'fourth line',
    ]

    set_options.assert_called_once_with(
        var_options=variables,
        direct={'split_lines': True},
    )

    expected_arguments = {
        'validate_certs': True,
        'use_proxy': True,
        'url_username': 'user',
        'url_password': 'secret',
        'headers': {'X-Test': 'value'},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': [],
    }

    assert mocked_open_url.call_args_list == [
        call('https://example.com/first', **expected_arguments),
        call('https://example.com/second', **expected_arguments),
    ]
    first_response.read.assert_called_once_with()
    second_response.read.assert_called_once_with()

# Generated at 2026-10-25 01:14:47.268574
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:49.683164
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:52.098029
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:54.512761
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:56.929067
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:14:59.343589
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:01.759098
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:04.179226
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:06.591045
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:09.006618
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:11.422085
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:13.836873
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:16.251715
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:18.668483
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:21.084984
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:23.505835
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:25.920409
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:28.336219
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:30.751178
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:33.166150
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:35.585796
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:37.995535
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:40.411718
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:42.828528
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:45.243238
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:47.661260
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:50.074285
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:52.489183
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:54.905654
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:57.321276
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:15:59.735906
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:02.150895
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:04.566184
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:06.982538
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:09.397697
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:11.812765
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:14.226413
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:16.644410
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:19.060667
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:21.474977
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:23.891399
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:26.307360
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:28.722806
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:31.137761
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:33.552954
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:35.968290
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:38.382768
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:40.797437
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:43.212152
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:45.627147
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:48.047033
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:50.460173
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:52.876408
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:55.294026
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:16:57.708802
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:00.123795
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:02.537960
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:04.953026
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:07.371090
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:09.785789
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:12.200451
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:17:23.568621
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 01:18:02.072545
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    url = "https://example.com/file.txt"
    variables = {"example_variable": "value"}

    options = {
        "validate_certs": True,
        "use_proxy": True,
        "username": None,
        "password": None,
        "headers": {"Accept": "text/plain"},
        "force": False,
        "timeout": 10,
        "http_agent": "ansible-httpget",
        "force_basic_auth": False,
        "follow_redirects": "urllib2",
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": None,
        "unredirected_headers": [],
        "split_lines": True,
    }

    response = Mock()
    response.read.return_value = b"first line\nsecond line\n"

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=options.__getitem__)

    mock_open_url = Mock(return_value=response)

    # Patch the global referenced directly by LookupModule.run, regardless of
    # the module path under which this test is executed.
    with patch.dict(LookupModule.run.__globals__, {"open_url": mock_open_url}):
        result = lookup.run([url], variables=variables, split_lines=True)

    assert result == ["first line", "second line"]

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={"split_lines": True},
    )
    mock_open_url.assert_called_once_with(
        url,
        validate_certs=True,
        use_proxy=True,
        url_username=None,
        url_password=None,
        headers={"Accept": "text/plain"},
        force=False,
        timeout=10,
        http_agent="ansible-httpget",
        force_basic_auth=False,
        follow_redirects="urllib2",
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[],
    )
    response.read.assert_called_once_with()

# Generated at 2026-10-25 01:18:04.489076
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:06.903209
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:09.319166
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:11.734733
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:14.148462
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:27.260572
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-25 01:18:33.918697
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:18:45.339467
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch

# Generated at 2026-10-25 01:19:18.645990
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from unittest.mock import MagicMock, call, patch

    options = {
        'validate_certs': True,
        'split_lines': True,
        'use_proxy': False,
        'username': 'test-user',
        'password': 'test-password',
        'headers': {'X-Test': 'value'},
        'force': True,
        'timeout': 5,
        'http_agent': 'test-agent',
        'force_basic_auth': True,
        'follow_redirects': 'safe',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': '/tmp/ca.pem',
        'unredirected_headers': ['Authorization'],
    }

    first_response = MagicMock()
    first_response.read.return_value = b'first line\nsecond line\n'

    second_response = MagicMock()
    second_response.read.return_value = b'third line\n'

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(side_effect=options.__getitem__)

    variables = {'inventory_hostname': 'localhost'}
    terms = ['https://example.com/first', 'https://example.com/second']

    module = sys.modules[LookupModule.__module__]
    with patch.object(
        module,
        'open_url',
        side_effect=[first_response, second_response],
    ) as mock_open_url:
        result = lookup.run(terms, variables=variables, split_lines=True)

    assert result == ['first line', 'second line', 'third line']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={'split_lines': True},
    )

    request_options = {
        'validate_certs': True,
        'use_proxy': False,
        'url_username': 'test-user',
        'url_password': 'test-password',
        'headers': {'X-Test': 'value'},
        'force': True,
        'timeout': 5,
        'http_agent': 'test-agent',
        'force_basic_auth': True,
        'follow_redirects': 'safe',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': '/tmp/ca.pem',
        'unredirected_headers': ['Authorization'],
    }

    assert mock_open_url.call_args_list == [
        call('https://example.com/first', **request_options),
        call('https://example.com/second', **request_options),
    ]
    first_response.read.assert_called_once_with()
    second_response.read.assert_called_once_with()

# Generated at 2026-10-25 01:19:35.152980
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:19:49.308060
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 01:20:22.461401
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {'example_variable': 'value'}
    kwargs = {'split_lines': True}

    options = {
        'validate_certs': True,
        'use_proxy': True,
        'username': 'test-user',
        'password': 'test-password',
        'headers': {'X-Test': 'value'},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': [],
        'split_lines': True,
    }

    response = MagicMock()
    response.read.return_value = b'first line\nsecond line\n'

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(side_effect=options.__getitem__)

    mocked_open_url = MagicMock(return_value=response)

    # Patch the global used by LookupModule.run without depending on the
    # module's import path.
    with patch.dict(
        LookupModule.run.__globals__,
        {'open_url': mocked_open_url},
    ):
        result = lookup.run(
            ['https://example.com/data.txt'],
            variables=variables,
            **kwargs
        )

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=kwargs,
    )

    mocked_open_url.assert_called_once_with(
        'https://example.com/data.txt',
        validate_certs=True,
        use_proxy=True,
        url_username='test-user',
        url_password='test-password',
        headers={'X-Test': 'value'},
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

    response.read.assert_called_once_with()

# Generated at 2026-10-25 01:21:00.452488
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:02.869081
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:05.284501
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:07.929060
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:10.344372
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:12.759850
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:15.174584
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:17.851027
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:20.255378
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:22.672079
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:25.086087
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:27.500641
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:29.917291
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:32.331427
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:21:43.875522
# Unit test for method run of class LookupModule
def test_LookupModule_run():import io

# Generated at 2026-10-25 01:22:26.759845
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:22:29.286511
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:22:31.850345
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:22:48.381649
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:22:58.690656
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 01:23:15.210380
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:17.628024
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:20.042757
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:22.458498
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:24.873111
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:27.288272
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:29.703035
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:32.117137
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:34.531459
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 01:23:36.949580
# Unit test for method run of class LookupModule