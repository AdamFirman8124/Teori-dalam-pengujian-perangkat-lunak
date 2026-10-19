

# Generated at 2024-06-02 15:33:09.827352
# Unit test for function make_default_headers
def test_make_default_headers():    args = argparse.Namespace(
        data=None,
        form=False,
        json=False,
        files=False
    )

# Generated at 2024-06-02 15:33:15.743553
# Unit test for function collect_messages

# Generated at 2024-06-02 15:33:16.900487
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:33:17.864232
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:33:19.649361
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    args = argparse.Namespace(timeout=30, allow_redirects=False)

# Generated at 2024-06-02 15:33:20.622671
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:33:23.439337
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:33:26.363677
# Unit test for function collect_messages

# Generated at 2024-06-02 15:33:27.389403
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:33:29.219152
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:33:55.057285
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    args = argparse.Namespace(timeout=30, allow_redirects=True)

# Generated at 2024-06-02 15:33:59.397760
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers={},
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:34:01.073508
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    args = argparse.Namespace(timeout=30, allow_redirects=False)

# Generated at 2024-06-02 15:34:03.690314
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    args = argparse.Namespace(timeout=30, allow_redirects=False)

# Generated at 2024-06-02 15:34:06.013055
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    args = argparse.Namespace(timeout=30, allow_redirects=False)

# Generated at 2024-06-02 15:34:09.225031
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    # Test case 1: Verify with 'yes'
    args = argparse.Namespace(
        proxy=[],
        verify='yes',
        cert=None,
        cert_key=None
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    assert make_send_kwargs_mergeable_from_env(args) == expected

    # Test case 2: Verify with 'no'
    args = argparse.Namespace(
        proxy=[],
        verify='no',
        cert=None,
        cert_key=None
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': False,
        'cert': None,
    }
    assert make_send_kwargs_mergeable_from_env(args) == expected

    # Test case 3: Custom cert without key

# Generated at 2024-06-02 15:34:10.312337
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:34:11.284108
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:34:14.180695
# Unit test for function make_default_headers
def test_make_default_headers():    args = argparse.Namespace(
        json=False,
        data=None,
        form=False,
        files=None
    )

# Generated at 2024-06-02 15:34:16.220666
# Unit test for function build_requests_session
def test_build_requests_session():    session = build_requests_session(verify=True, ssl_version='TLSv1.2', ciphers='ECDHE-RSA-AES128-GCM-SHA256')

# Generated at 2024-06-02 15:34:58.132935
# Unit test for function make_default_headers
def test_make_default_headers():    # Test case 1: No data, no form, no json
    args = argparse.Namespace(data=None, form=False, json=False, files=False)
    expected_headers = RequestHeadersDict({'User-Agent': DEFAULT_UA})
    assert make_default_headers(args) == expected_headers

    # Test case 2: JSON data
    args = argparse.Namespace(data={'key': 'value'}, form=False, json=True, files=False)
    expected_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    })
    assert make_default_headers(args) == expected_headers

    # Test case 3: Form data
    args = argparse.Namespace(data={'key': 'value'}, form=True, json=False, files=False)
    expected_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Content-Type': FORM_CONTENT_TYPE
    })

# Generated at 2024-06-02 15:34:59.215872
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:35:02.207302
# Unit test for function collect_messages

# Generated at 2024-06-02 15:35:05.548164
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:35:10.255269
# Unit test for function collect_messages

# Generated at 2024-06-02 15:35:13.104075
# Unit test for function make_default_headers
def test_make_default_headers():    args = argparse.Namespace(
        data=None,
        form=False,
        json=False,
        files=False
    )

# Generated at 2024-06-02 15:35:17.122270
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2024-06-02 15:35:18.095701
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:35:21.333852
# Unit test for function make_default_headers
def test_make_default_headers():    # Test case 1: No data, no form, no json
    args = argparse.Namespace(data=None, form=False, json=False, files=None)
    expected_headers = RequestHeadersDict({'User-Agent': DEFAULT_UA})
    assert make_default_headers(args) == expected_headers

    # Test case 2: JSON data
    args = argparse.Namespace(data={'key': 'value'}, form=False, json=True, files=None)
    expected_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    })
    assert make_default_headers(args) == expected_headers

    # Test case 3: Form data
    args = argparse.Namespace(data={'key': 'value'}, form=True, json=False, files=None)
    expected_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Content-Type': FORM_CONTENT_TYPE
    })

# Generated at 2024-06-02 15:35:24.755705
# Unit test for function collect_messages

# Generated at 2024-06-02 15:36:06.366524
# Unit test for function make_request_kwargs

# Generated at 2024-06-02 15:36:09.379172
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:36:12.297116
# Unit test for function make_default_headers
def test_make_default_headers():    # Test case 1: No data, no form, no json
    args = argparse.Namespace(data=None, form=False, json=False, files=None)
    expected_headers = RequestHeadersDict({'User-Agent': DEFAULT_UA})
    assert make_default_headers(args) == expected_headers

    # Test case 2: JSON data
    args = argparse.Namespace(data={'key': 'value'}, form=False, json=True, files=None)
    expected_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    })
    assert make_default_headers(args) == expected_headers

    # Test case 3: Form data
    args = argparse.Namespace(data={'key': 'value'}, form=True, json=False, files=None)
    expected_headers = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Content-Type': FORM_CONTENT_TYPE
    })

# Generated at 2024-06-02 15:36:16.794247
# Unit test for function collect_messages

# Generated at 2024-06-02 15:36:18.129543
# Unit test for function make_send_kwargs
def test_make_send_kwargs():    args = argparse.Namespace(timeout=30)

# Generated at 2024-06-02 15:36:19.408066
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:36:22.097396
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:36:26.206427
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    args = argparse.Namespace(
        proxy=[argparse.Namespace(key='http', value='http://proxy.example.com')],
        verify='true',
        cert=None,
        cert_key=None
    )

# Generated at 2024-06-02 15:36:30.137444
# Unit test for function make_default_headers
def test_make_default_headers():    # Test case 1: No data, no form, no json
    args = argparse.Namespace(data=None, form=False, json=False, files=False)
    expected = RequestHeadersDict({'User-Agent': DEFAULT_UA})
    assert make_default_headers(args) == expected

    # Test case 2: JSON data
    args = argparse.Namespace(data={'key': 'value'}, form=False, json=True, files=False)
    expected = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Accept': JSON_ACCEPT,
        'Content-Type': JSON_CONTENT_TYPE
    })
    assert make_default_headers(args) == expected

    # Test case 3: Form data
    args = argparse.Namespace(data={'key': 'value'}, form=True, json=False, files=False)
    expected = RequestHeadersDict({
        'User-Agent': DEFAULT_UA,
        'Content-Type': FORM_CONTENT_TYPE
    })
    assert make_default_headers(args)

# Generated at 2024-06-02 15:36:32.464796
# Unit test for function finalize_headers
def test_finalize_headers():    headers = RequestHeadersDict({
        'Content-Type': ' application/json ',
        'User-Agent': ' HTTPie/1.0 ',
        'Custom-Header': ' Custom Value ',
        'None-Header': None
    })

# Generated at 2024-06-02 15:37:47.139011
# Unit test for function make_default_headers
def test_make_default_headers():    args = argparse.Namespace(
        json=False,
        data=None,
        form=False,
        files=None
    )

# Generated at 2024-06-02 15:37:52.414153
# Unit test for function collect_messages

# Generated at 2024-06-02 15:37:56.845137
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    args = argparse.Namespace(
        proxy=[argparse.Namespace(key='http', value='http://proxy.example.com')],
        verify='true',
        cert=None,
        cert_key=None
    )

# Generated at 2024-06-02 15:38:00.230483
# Unit test for function collect_messages

# Generated at 2024-06-02 15:38:03.197127
# Unit test for function make_request_kwargs

# Generated at 2024-06-02 15:38:06.097996
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:38:09.314973
# Unit test for function make_default_headers
def test_make_default_headers():    args = argparse.Namespace(
        data=None,
        form=False,
        json=False,
        files=False
    )

# Generated at 2024-06-02 15:38:12.219778
# Unit test for function collect_messages

# Generated at 2024-06-02 15:38:15.497021
# Unit test for function make_default_headers
def test_make_default_headers():    args = argparse.Namespace(
        data=None,
        form=False,
        json=False,
        files=False
    )

# Generated at 2024-06-02 15:38:18.017504
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='GET',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data=None,
        json=False,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:41:34.055478
# Unit test for function max_headers
def test_max_headers():    limit = 10

# Generated at 2024-06-02 15:41:36.227695
# Unit test for function make_send_kwargs

# Generated at 2024-06-02 15:41:39.754874
# Unit test for function collect_messages

# Generated at 2024-06-02 15:41:44.625600
# Unit test for function make_send_kwargs_mergeable_from_env

# Generated at 2024-06-02 15:41:48.850779
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    args = argparse.Namespace(
        proxy=[argparse.Namespace(key='http', value='http://proxy.example.com')],
        verify='true',
        cert=None,
        cert_key=None
    )

# Generated at 2024-06-02 15:41:51.977817
# Unit test for function make_request_kwargs
def test_make_request_kwargs():    args = argparse.Namespace(
        method='POST',
        url='http://example.com',
        headers=RequestHeadersDict({'Custom-Header': 'value'}),
        data={'key': 'value'},
        json=True,
        form=False,
        files=None,
        multipart=False,
        multipart_data=None,
        boundary=None,
        auth=None,
        params={},
        chunked=False,
        offline=False
    )

# Generated at 2024-06-02 15:41:55.079018
# Unit test for function collect_messages

# Generated at 2024-06-02 15:42:00.170575
# Unit test for function make_send_kwargs_mergeable_from_env
def test_make_send_kwargs_mergeable_from_env():    args = argparse.Namespace(
        proxy=[argparse.Namespace(key='http', value='http://proxy.example.com')],
        verify='true',
        cert=None,
        cert_key=None
    )

# Generated at 2024-06-02 15:42:02.826443
# Unit test for function make_request_kwargs

# Generated at 2024-06-02 15:42:04.329532
# Unit test for function make_send_kwargs