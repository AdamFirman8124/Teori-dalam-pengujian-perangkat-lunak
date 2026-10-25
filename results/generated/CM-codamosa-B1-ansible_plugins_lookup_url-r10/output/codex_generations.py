

# Generated at 2026-10-25 00:11:29.988815
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:11:45.861473
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 00:11:52.516075
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-25 00:12:07.288258
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:12:16.751236
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-25 00:12:23.133604
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 00:12:39.722137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    import pytest

    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError


# Generated at 2026-10-25 00:13:21.129681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from io import BytesIO
    from unittest.mock import Mock, patch


# Generated at 2026-10-25 00:13:58.571680
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:14:08.307372
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-25 00:14:45.991697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    variables = {"inventory_hostname": "test-host"}
    direct_options = {"timeout": 30}

    options = {
        "validate_certs": True,
        "split_lines": True,
        "use_proxy": False,
        "username": "user",
        "password": "secret",
        "headers": {"X-Test": "value"},
        "force": True,
        "timeout": 30,
        "http_agent": "test-agent",
        "force_basic_auth": True,
        "follow_redirects": "safe",
        "use_gssapi": False,
        "unix_socket": None,
        "ca_path": "/path/to/ca.pem",
        "unredirected_headers": ["Authorization"],
    }

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=lambda name: options[name])

    plugin_module = sys.modules[LookupModule.__module__]

    response = BytesIO(b"first line\nsecond line\n")
    with patch.object(plugin_module, "open_url", return_value=response) as mock_open_url:
        result = lookup.run(
            ["https://example.test/data"],
            variables=variables,
            **direct_options
        )

    assert result == ["first line", "second line"]
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options,
    )
    mock_open_url.assert_called_once_with(
        "https://example.test/data",
        validate_certs=True,
        use_proxy=False,
        url_username="user",
        url_password="secret",
        headers={"X-Test": "value"},
        force=True,
        timeout=30,
        http_agent="test-agent",
        force_basic_auth=True,
        follow_redirects="safe",
        use_gssapi=False,
        unix_socket=None,
        ca_path="/path/to/ca.pem",
        unredirected_headers=["Authorization"],
    )

    # Verify split_lines=False returns one text blob.
    options["split_lines"] = False
    response = BytesIO(b"first line\nsecond line\n")

    with patch.object(plugin_module, "open_url", return_value=response):
        result = lookup.run(["https://example.test/data"])

    assert result == ["first line\nsecond line\n"]

# Generated at 2026-10-25 00:14:56.227364
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:15:06.565344
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 00:15:34.532806
# Unit test for method run of class LookupModule
def test_LookupModule_run():
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

    response = MagicMock()
    response.read.return_value = b'first line\nsecond line\n'

    lookup = LookupModule()

    with patch.object(lookup, 'set_options') as set_options, \
            patch.object(lookup, 'get_option',
                         side_effect=lambda name: options[name]), \
            patch.object(display, 'vvvv') as display_vvvv, \
            patch(__name__ + '.open_url', return_value=response) as mocked_open_url:

        result = lookup.run(
            ['https://example.com/file.txt'],
            variables={'example_variable': True},
        )

    assert result == ['first line', 'second line']

    set_options.assert_called_once_with(
        var_options={'example_variable': True},
        direct={},
    )
    display_vvvv.assert_called_once_with(
        'url lookup connecting to https://example.com/file.txt'
    )
    response.read.assert_called_once_with()
    mocked_open_url.assert_called_once_with(
        'https://example.com/file.txt',
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

# Generated at 2026-10-25 00:15:51.014400
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:16:06.675489
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-25 00:16:23.080018
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:16:35.449685
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 00:17:07.197706
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch

    options = {
        'validate_certs': True,
        'use_proxy': False,
        'username': 'test-user',
        'password': 'test-password',
        'headers': {'X-Test': 'value'},
        'force': True,
        'timeout': 5.0,
        'http_agent': 'test-agent',
        'force_basic_auth': True,
        'follow_redirects': 'safe',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': '/tmp/test-ca.pem',
        'unredirected_headers': ['Authorization'],
        'split_lines': True,
    }

    response = MagicMock()
    response.read.return_value = b'first line\nsecond line\n'

    mock_open_url = MagicMock(return_value=response)

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(side_effect=options.__getitem__)

    variables = {'example': 'value'}
    direct_options = {'split_lines': True}

    with patch.dict(
        LookupModule.run.__globals__,
        {'open_url': mock_open_url},
    ):
        result = lookup.run(
            ['https://example.com/data'],
            variables=variables,
            **direct_options
        )

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options,
    )

    mock_open_url.assert_called_once_with(
        'https://example.com/data',
        validate_certs=True,
        use_proxy=False,
        url_username='test-user',
        url_password='test-password',
        headers={'X-Test': 'value'},
        force=True,
        timeout=5.0,
        http_agent='test-agent',
        force_basic_auth=True,
        follow_redirects='safe',
        use_gssapi=False,
        unix_socket=None,
        ca_path='/tmp/test-ca.pem',
        unredirected_headers=['Authorization'],
    )

    response.read.assert_called_once_with()

# Generated at 2026-10-25 00:17:44.614357
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import Mock, patch

    url = 'https://example.com/file.txt'
    variables = {'example_variable': 'value'}
    direct_options = {'timeout': 5}

    options = {
        'validate_certs': True,
        'use_proxy': True,
        'username': 'user',
        'password': 'password',
        'headers': {'X-Test': 'value'},
        'force': False,
        'timeout': 5,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': [],
        'split_lines': True,
    }

    response = Mock()
    response.read.return_value = b'first line\nsecond line\r\n'

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=options.__getitem__)

    with patch(__name__ + '.open_url', return_value=response) as mock_open_url:
        result = lookup.run(
            [url],
            variables=variables,
            **direct_options
        )

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options
    )
    mock_open_url.assert_called_once_with(
        url,
        validate_certs=True,
        use_proxy=True,
        url_username='user',
        url_password='password',
        headers={'X-Test': 'value'},
        force=False,
        timeout=5,
        http_agent='ansible-httpget',
        force_basic_auth=False,
        follow_redirects='urllib2',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=[]
    )
    response.read.assert_called_once_with()

# Generated at 2026-10-25 00:17:52.350570
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:18:01.669252
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-25 00:18:18.064813
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:18:28.090205
# Unit test for method run of class LookupModule
def test_LookupModule_run():import io

# Generated at 2026-10-25 00:19:01.619303
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:19:09.766424
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-25 00:19:26.263864
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:19:38.437766
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-25 00:20:11.287588
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from unittest.mock import Mock, call, patch

    lookup = LookupModule()
    lookup.set_options = Mock()

    options = {
        'validate_certs': True,
        'split_lines': True,
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
        'unredirected_headers': ['Authorization'],
    }
    lookup.get_option = Mock(side_effect=options.__getitem__)

    first_response = Mock()
    first_response.read.return_value = b'first line\nsecond line\n'

    second_response = Mock()
    second_response.read.return_value = b'third line\n'

    module = sys.modules[LookupModule.__module__]
    with patch.object(
        module,
        'open_url',
        side_effect=[first_response, second_response],
    ) as mocked_open_url:
        result = lookup.run(
            ['https://example.com/one', 'https://example.com/two'],
            variables={'test_variable': 'value'},
            split_lines=True,
        )

    assert result == ['first line', 'second line', 'third line']

    lookup.set_options.assert_called_once_with(
        var_options={'test_variable': 'value'},
        direct={'split_lines': True},
    )

    expected_arguments = {
        'validate_certs': True,
        'use_proxy': True,
        'url_username': 'test-user',
        'url_password': 'test-password',
        'headers': {'X-Test': 'value'},
        'force': False,
        'timeout': 10,
        'http_agent': 'ansible-httpget',
        'force_basic_auth': False,
        'follow_redirects': 'urllib2',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': ['Authorization'],
    }
    assert mocked_open_url.call_args_list == [
        call('https://example.com/one', **expected_arguments),
        call('https://example.com/two', **expected_arguments),
    ]

    first_response.read.assert_called_once_with()
    second_response.read.assert_called_once_with()

# Generated at 2026-10-25 00:20:13.705238
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:20:16.119940
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:20:18.534272
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:20:46.432776
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import Mock, patch
    import sys

    options = {
        'validate_certs': True,
        'use_proxy': True,
        'username': 'user',
        'password': 'password',
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

    response = Mock()
    response.read.return_value = b'first line\nsecond line\n'

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=options.__getitem__)

    module = sys.modules[LookupModule.__module__]

    with patch.object(module, 'open_url', return_value=response) as mock_open_url:
        result = lookup.run(
            ['https://example.com/data'],
            variables={'example': 'variable'},
            timeout=10,
        )

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options={'example': 'variable'},
        direct={'timeout': 10},
    )

    mock_open_url.assert_called_once_with(
        'https://example.com/data',
        validate_certs=True,
        use_proxy=True,
        url_username='user',
        url_password='password',
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

# Generated at 2026-10-25 00:21:20.019632
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:21:22.594460
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:21:25.008866
# Unit test for method run of class LookupModule