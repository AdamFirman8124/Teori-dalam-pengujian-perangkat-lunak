

# Generated at 2026-10-25 00:43:44.538504
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 00:43:52.628133
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-25 00:44:30.938062
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys

    try:
        from unittest.mock import MagicMock, patch
    except ImportError:
        from mock import MagicMock, patch

    options = {
        'validate_certs': True,
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
        'ca_path': '/path/to/ca.pem',
        'unredirected_headers': ['Authorization'],
        'split_lines': True,
    }

    response = MagicMock()
    response.read.return_value = b'first line\nsecond line\n'

    lookup = LookupModule()
    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(side_effect=options.__getitem__)

    variables = {'inventory_hostname': 'localhost'}
    module = sys.modules[LookupModule.__module__]

    with patch.object(module, 'open_url', return_value=response) as mock_open_url:
        result = lookup.run(
            ['https://example.com/data'],
            variables=variables,
            split_lines=True,
        )

    assert result == ['first line', 'second line']

    lookup.set_options.assert_called_once_with(
        var_options=variables,
        direct={'split_lines': True},
    )
    response.read.assert_called_once_with()
    mock_open_url.assert_called_once_with(
        'https://example.com/data',
        validate_certs=True,
        use_proxy=False,
        url_username='test-user',
        url_password='test-password',
        headers={'X-Test': 'value'},
        force=True,
        timeout=5,
        http_agent='test-agent',
        force_basic_auth=True,
        follow_redirects='safe',
        use_gssapi=False,
        unix_socket=None,
        ca_path='/path/to/ca.pem',
        unredirected_headers=['Authorization'],
    )

# Generated at 2026-10-25 00:44:38.707036
# Unit test for constructor of class LookupModule
def test_LookupModule():
    loader = object()
    templar = object()

    lookup = LookupModule(loader=loader, templar=templar)

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)
    assert lookup._loader is loader
    assert lookup._templar is templar

# Generated at 2026-10-25 00:44:45.568835
# Unit test for constructor of class LookupModule
def test_LookupModule():
    lookup = LookupModule()

    assert isinstance(lookup, LookupModule)
    assert isinstance(lookup, LookupBase)

# Generated at 2026-10-25 00:45:04.307342
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:45:06.726059
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:45:09.141035
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:45:11.556796
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:45:23.766583
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 00:45:40.454453
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:45:51.923184
# Unit test for method run of class LookupModule
def test_LookupModule_run():import io

# Generated at 2026-10-25 00:46:36.262241
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

# Generated at 2026-10-25 00:46:52.763111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from unittest.mock import MagicMock, patch
    import pytest

    from ansible.errors import AnsibleError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError


# Generated at 2026-10-25 00:46:55.404184
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:46:57.820362
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:00.553207
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:02.965778
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:05.380089
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:07.795420
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:10.211534
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:12.625668
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:15.042803
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:17.454689
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:19.880998
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:22.301955
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:24.717117
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:27.148866
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:29.561386
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:31.984892
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:47:50.605369
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-25 00:48:07.092439
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:09.515095
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:11.931757
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:14.346592
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:16.763872
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:19.190637
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:21.632120
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:24.073897
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:26.490265
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:28.907366
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:31.327323
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:33.758741
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:36.171624
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:38.600874
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:41.024375
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:43.438756
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:48:54.278229
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-25 00:49:27.274044
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:29.690932
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:32.111463
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:34.522586
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:36.937731
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:39.353086
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:41.767506
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:44.181786
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:46.597187
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:49.012270
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:51.426363
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:53.841606
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:56.255427
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:49:58.670333
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:01.085300
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:03.500395
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:05.915144
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:08.329869
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:10.755564
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:22.186551
# Unit test for method run of class LookupModule
def test_LookupModule_run():import io

# Generated at 2026-10-25 00:50:38.653535
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:48.576956
# Unit test for method run of class LookupModule
def test_LookupModule_run():from unittest.mock import Mock, patch


# Generated at 2026-10-25 00:50:51.004552
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:53.432852
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:55.982668
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:50:58.403319
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:00.821638
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:03.240532
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:05.654009
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:08.069183
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:10.484044
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:12.899868
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:15.315294
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:17.734653
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:20.148689
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:22.572510
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:51:34.353521
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 00:51:50.838212
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:52:03.026512
# Unit test for method run of class LookupModule
def test_LookupModule_run():import sys

# Generated at 2026-10-25 00:52:43.781220
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:52:53.402567
# Unit test for method run of class LookupModule
def test_LookupModule_run():from io import BytesIO

# Generated at 2026-10-25 00:53:19.655182
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:22.073432
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:24.489522
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:26.906416
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:29.320876
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:31.737054
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:34.153149
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:36.577674
# Unit test for method run of class LookupModule

# Generated at 2026-10-25 00:53:38.994978
# Unit test for method run of class LookupModule