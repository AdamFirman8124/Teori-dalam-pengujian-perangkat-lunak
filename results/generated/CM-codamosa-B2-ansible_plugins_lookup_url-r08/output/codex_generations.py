

# Generated at 2026-10-24 23:20:33.318535
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 23:20:35.741554
# Unit test for constructor of class LookupModule

# Generated at 2026-10-24 23:20:42.346212
# Unit test for constructor of class LookupModule
def test_LookupModule():lookup = LookupModule()

# Generated at 2026-10-24 23:21:19.318541
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    url = 'https://example.com/data.txt'
    variables = {'example_variable': 'value'}
    direct_options = {'split_lines': True}

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

    plugin_module = sys.modules[LookupModule.__module__]

    with patch.object(plugin_module, 'open_url', return_value=response) as mock_open_url:
        result = lookup.run([url], variables=variables, **direct_options)

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options,
    )

    mock_open_url.assert_called_once_with(
        url,
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

# Generated at 2026-10-24 23:21:27.329214
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is None
    assert lookup._templar is None

# Generated at 2026-10-24 23:21:29.750408
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:21:32.288109
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:21:34.688479
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:21:37.104620
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:21:39.520875
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:21:41.940201
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:21:52.806033
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    lookup = LookupModule()

    # Case 1: multiple URLs, split_lines default (True) -> flat list of lines
    lookup_1 = LookupModule()
    result = lookup_1.run(terms=['http://www.ansible.com/httpbin/get?a=b&c=d',
                                 'http://www.ansible.com/httpbin/get?e=f&g=h'],
                          variables=None)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "{'args': {'a': 'b', 'c': 'd'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?a=b&c=d'}"
    assert result[1] == "{'args': {'e': 'f', 'g': 'h'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?e=f&g=h'}"

    # Case 2: single URL, split_lines=False -> single blob entry
    lookup_2 = LookupModule()
    result = lookup_2.run(terms=['http://www.ansible.com/httpbin/get?a=b&c=d'],
                          variables={'ansible_lookup_url_split_lines': False})
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{'args': {'a': 'b', 'c': 'd'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?a=b&c=d'}"

    # Case 3: HTTPError raised -> AnsibleError with HTTP error message
    lookup_3 = LookupModule()
    try:
        lookup_3.run(terms=['http://www.ansible.com/void'], variables=None)
    except HTTPError as e:
        assert e.code == 404
    except AnsibleError as e:
        assert 'Received HTTP error for' in to_native(e)
    else:
        raise AssertionError("Expected HTTPError or AnsibleError for 'http://www.ansible.com/void'")

    # Case 4: URLError / ConnectionError raised -> AnsibleError with failure message
    lookup_4 = LookupModule()
    try:
        lookup_4.run(terms=['http://localhost:1/'], variables=None)
    except AnsibleError as e:
        assert ('Failed lookup url for' in to_native(e)) or ('Error connecting to' in to_native(e))
    else:
        raise AssertionError("Expected AnsibleError for unreachable URL 'http://localhost:1/'")

    # Case 5: invalid scheme -> URLError style AnsibleError
    lookup_5 = LookupModule()
    try:
        lookup_5.run(terms=['file:///foo/bar.txt'], variables=None)
    except AnsibleError as e:
        assert 'Failed lookup url for' in to_native(e)
    else:
        raise AssertionError("Expected AnsibleError for unsupported scheme 'file:///foo/bar.txt'")

    # Case 6: term without scheme -> ansiblehttpget prepends http://
    lookup_6 = LookupModule()
    result = lookup_6.run(terms=['www.ansible.com/httpbin/get'], variables=None)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{'args': {}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get'}"

# Generated at 2026-10-24 23:22:32.232484
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from unittest.mock import MagicMock, call, patch

    terms = [
        'https://example.com/first',
        'https://example.com/second',
    ]
    variables = {'example_variable': 'value'}
    direct_options = {'split_lines': True}

    options = {
        'validate_certs': True,
        'use_proxy': False,
        'username': 'user',
        'password': 'secret',
        'headers': {'X-Test': 'value'},
        'force': True,
        'timeout': 5.0,
        'http_agent': 'test-agent',
        'force_basic_auth': True,
        'follow_redirects': 'safe',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': '/tmp/ca.pem',
        'unredirected_headers': ['Authorization'],
        'split_lines': True,
    }

    first_response = MagicMock()
    first_response.read.return_value = b'first line\nsecond line\n'

    second_response = MagicMock()
    second_response.read.return_value = b'third line\n'

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(side_effect=lambda name: options[name])

    module = sys.modules[LookupModule.__module__]
    with patch.object(
        module,
        'open_url',
        side_effect=[first_response, second_response],
    ) as mocked_open_url:
        result = lookup.run(
            terms,
            variables=variables,
            **direct_options
        )

    assert result == ['first line', 'second line', 'third line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options,
    )


# Generated at 2026-10-24 23:23:00.462357
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:12.674864
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-24 23:23:29.158651
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:40.113622
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-24 23:23:42.532896
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:44.951633
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:47.368186
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:49.785796
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:52.203634
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:54.623450
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:23:57.219493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    from ansible.module_utils.urls import ConnectionError, SSLValidationError

    lookup = LookupModule()

    # Case 1: multiple URLs, split_lines default (True) -> flat list of lines
    lookup_1 = LookupModule()
    result = lookup_1.run(terms=['http://www.ansible.com/httpbin/get?a=b&c=d',
                                 'http://www.ansible.com/httpbin/get?e=f&g=h'],
                          variables=None)
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == "{'args': {'a': 'b', 'c': 'd'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?a=b&c=d'}"
    assert result[1] == "{'args': {'e': 'f', 'g': 'h'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?e=f&g=h'}"

    # Case 2: single URL, split_lines=False -> single blob entry
    lookup_2 = LookupModule()
    result = lookup_2.run(terms=['http://www.ansible.com/httpbin/get?a=b&c=d'],
                          variables={'ansible_lookup_url_split_lines': False})
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{'args': {'a': 'b', 'c': 'd'}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get?a=b&c=d'}"

    # Case 3: HTTPError raised -> AnsibleError with HTTP error message
    lookup_3 = LookupModule()
    try:
        lookup_3.run(terms=['http://www.ansible.com/void'], variables=None)
    except HTTPError as e:
        assert e.code == 404
    except AnsibleError as e:
        assert 'Received HTTP error for' in to_native(e)
    else:
        raise AssertionError("Expected HTTPError or AnsibleError for 'http://www.ansible.com/void'")

    # Case 4: URLError / ConnectionError raised -> AnsibleError with failure message
    lookup_4 = LookupModule()
    try:
        lookup_4.run(terms=['http://localhost:1/'], variables=None)
    except AnsibleError as e:
        assert ('Failed lookup url for' in to_native(e)) or ('Error connecting to' in to_native(e))
    else:
        raise AssertionError("Expected AnsibleError for unreachable URL 'http://localhost:1/'")

    # Case 5: invalid scheme -> URLError style AnsibleError
    lookup_5 = LookupModule()
    try:
        lookup_5.run(terms=['file:///foo/bar.txt'], variables=None)
    except AnsibleError as e:
        assert 'Failed lookup url for' in to_native(e)
    else:
        raise AssertionError("Expected AnsibleError for unsupported scheme 'file:///foo/bar.txt'")

    # Case 6: term without scheme -> ansiblehttpget prepends http://
    lookup_6 = LookupModule()
    result = lookup_6.run(terms=['www.ansible.com/httpbin/get'], variables=None)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{'args': {}, 'headers': {'Accept-Encoding': 'identity'}, 'origin': '127.0.0.1', 'url': 'http://www.ansible.com/httpbin/get'}"

# Generated at 2026-10-24 23:24:13.702772
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:24:26.720063
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-24 23:25:00.399134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from unittest.mock import MagicMock, patch

    lookup = LookupModule()
    variables = {'example_variable': 'value'}
    kwargs = {'timeout': 5}

    options = {
        'validate_certs': True,
        'use_proxy': False,
        'username': 'user',
        'password': 'password',
        'headers': {'Accept': 'text/plain'},
        'force': True,
        'timeout': 5,
        'http_agent': 'test-agent',
        'force_basic_auth': True,
        'follow_redirects': 'safe',
        'use_gssapi': False,
        'unix_socket': None,
        'ca_path': None,
        'unredirected_headers': ['Authorization'],
        'split_lines': True,
    }

    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(side_effect=options.__getitem__)

    response = MagicMock()
    response.read.return_value = b'first line\nsecond line\n'

    module = sys.modules[LookupModule.__module__]
    url = 'https://example.test/data'

    with patch.object(module, 'open_url', return_value=response) as mocked_open_url:
        result = lookup.run([url], variables=variables, **kwargs)

    assert result == ['first line', 'second line']
    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=kwargs,
    )
    mocked_open_url.assert_called_once_with(
        url,
        validate_certs=True,
        use_proxy=False,
        url_username='user',
        url_password='password',
        headers={'Accept': 'text/plain'},
        force=True,
        timeout=5,
        http_agent='test-agent',
        force_basic_auth=True,
        follow_redirects='safe',
        use_gssapi=False,
        unix_socket=None,
        ca_path=None,
        unredirected_headers=['Authorization'],
    )
    response.read.assert_called_once_with()

# Generated at 2026-10-24 23:25:16.882693
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:25:26.712851
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-24 23:26:06.042453
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import Mock, patch

    url = 'https://example.com/file.txt'
    variables = {'inventory_hostname': 'test-host'}
    direct_options = {'split_lines': True}

    options = {
        'validate_certs': True,
        'use_proxy': False,
        'username': 'alice',
        'password': 'secret',
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
        'split_lines': True,
    }

    response = Mock()
    response.read.return_value = b'first line\nsecond line\n'

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=options.__getitem__)

    mock_open_url = Mock(return_value=response)

    # Patch the global used directly by LookupModule.run().
    with patch.dict(LookupModule.run.__globals__,
                    {'open_url': mock_open_url}):
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
        use_proxy=False,
        url_username='alice',
        url_password='secret',
        headers={'X-Test': 'value'},
        force=True,
        timeout=5,
        http_agent='test-agent',
        force_basic_auth=True,
        follow_redirects='safe',
        use_gssapi=False,
        unix_socket=None,
        ca_path='/tmp/ca.pem',
        unredirected_headers=['Authorization'],
    )
    response.read.assert_called_once_with()

# Generated at 2026-10-24 23:26:50.988468
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    import pytest

    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError


# Generated at 2026-10-24 23:27:07.474787
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:27:18.535048
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-24 23:27:34.936702
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:27:46.313866
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-24 23:28:02.770998
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:28:15.918117
# Unit test for method run of class LookupModule
def test_LookupModule_run():import io

# Generated at 2026-10-24 23:28:52.858977
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from io import BytesIO
    from unittest.mock import Mock, patch

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

    lookup = LookupModule()
    lookup.set_options = Mock()
    lookup.get_option = Mock(side_effect=options.__getitem__)

    response = BytesIO(b'first line\nsecond line\n')
    variables = {'inventory_hostname': 'test-host'}
    direct_options = {'split_lines': True}

    module = sys.modules[LookupModule.__module__]

    with patch.object(module, 'open_url', return_value=response) as mock_open_url:
        result = lookup.run(
            ['https://example.test/data'],
            variables=variables,
            **direct_options
        )

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct=direct_options
    )

    mock_open_url.assert_called_once_with(
        'https://example.test/data',
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

# Generated at 2026-10-24 23:28:55.277479
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:28:57.873582
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:00.292477
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:02.710886
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:05.126149
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:24.118491
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-24 23:29:40.770844
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:51.520145
# Unit test for method run of class LookupModule
def test_LookupModule_run():import io

# Generated at 2026-10-24 23:29:53.941351
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:56.358748
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:29:58.777469
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:01.193843
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:03.610004
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:06.027134
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:08.454748
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:10.860710
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:13.277991
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:15.694167
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:18.113372
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:20.528908
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:22.949493
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:25.370217
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:27.782558
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:30.199445
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:32.617089
# Unit test for method run of class LookupModule

# Generated at 2026-10-24 23:30:35.033609
# Unit test for method run of class LookupModule