

# Generated at 2022-06-13 04:46:28.457145
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    """ Test the get_channel_binding_cert_hash function. """
    # Test basic functionality
    try:
        get_channel_binding_cert_hash(b'\x00')
    except Exception:
        assert False, 'Failed to get channel binding cert hash for DER encoded cert.'

    # Test value of hash for valid DER encoded certificate.

# Generated at 2022-06-13 04:46:37.494881
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
        ),
        supports_check_mode=False,
    )
    url = module.params['url']

    handler = SSLValidationHandler(None, None)
    use_proxy = handler.detect_no_proxy(url)
    if use_proxy:
        module.exit_json(msg=url + " must use proxy")
    else:
        module.exit_json(msg=url + " must not use proxy")


# Generated at 2022-06-13 04:46:42.189520
# Unit test for function prepare_multipart
def test_prepare_multipart():
    fields = {
        'field1': 'value1',
        'field2': 'value2',
        'field3': {
            'content': 'test content',
            'filename': None,
            'mime_type': 'text/plain',
        },
        'field4': {
            'content': None,
            'filename': '/bin/true',
            'mime_type': 'application/octet-stream',
        },
        'field5': {
            'content': 'test content',
            'filename': '/bin/true',
            'mime_type': 'application/octet-stream',
        },
    }
    ct, body = prepare_multipart(fields)
    b_body = to_bytes(body, errors='surrogate_or_strict')

# Generated at 2022-06-13 04:46:52.288669
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    from ansible.module_utils.six.moves.urllib.error import HTTPError

    # check that the handler factory works, and handles
    # different follow_redirects scenarios correctly
    for follow_redirects in ['all', 'yes', True, 'safe', 'no', 'none', 'urllib2', False]:
        handler = RedirectHandlerFactory(follow_redirects)()
        # request without payload and headers, expect request without payload and headers
        req1 = RequestWithMethod('http://www.example.com/', method='POST', headers={'Content-Type': 'application/json'})
        req2 = handler.redirect_request(req1, None, 301, '', None, 'http://www.example.com/xxx')
        assert req1.data is None

# Generated at 2022-06-13 04:47:05.849548
# Unit test for method connect of class CustomHTTPSConnection

# Generated at 2022-06-13 04:47:18.286775
# Unit test for function prepare_multipart
def test_prepare_multipart():
    content_type, body = prepare_multipart({
        "file1": {
            "filename": "/bin/true",
            "mime_type": "application/octet-stream"
        },
        "file2": {
            "content": "text based file content",
            "filename": "fake.txt",
            "mime_type": "text/plain",
        },
        "text_form_field": "value"
    })
    assert content_type == 'multipart/form-data; boundary="===============112821166200188731=="'

# Generated at 2022-06-13 04:47:27.667005
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    # Test values before and after the Epoch, with and without
    # time zone
    test_cases = (
        ((1968, 1, 1, 0, 0, 0, -1, -1, 0), 'Fri, 01 Jan 1968 00:00:00 -0000'),
        ((2038, 1, 1, 0, 0, 0, -1, -1, 0), 'Sun, 01 Jan 2038 00:00:00 -0000'),
        ((2038, 1, 1, 0, 0, 0, -1, -1, -1), 'Sat, 31 Dec 2037 23:59:59 -0001'),
        ((2038, 1, 1, 0, 0, 0, -1, -1, 1), 'Mon, 02 Jan 2038 00:00:00 +0001'),
        )
    for test_case in test_cases:
        timetuple

# Generated at 2022-06-13 04:47:35.792578
# Unit test for function getpeercert
def test_getpeercert():
    """ Unit test for function getpeercert. """
    import json
    import random
    import unittest
    import tempfile
    from subprocess import Popen

    # NOTE: This requires Python to be installed along with the 'pip' command.
    # Also, the 'dummyserver' package must be installed.
    # However, we can't easily mock out the Python and pip commands,
    # so we'll just hope that they're available here.

    class getpeercertTestCase(unittest.TestCase):
        """ Unit test for function getpeercert. """

        def setUp(self):
            port = random.randrange(32768, 65535)
            self.ssl_port = port
            self.normal_port = port + 1

# Generated at 2022-06-13 04:47:37.966344
# Unit test for method open of class Request
def test_Request_open():
    # create a Request object
    request = Request()

    # run the open() method on different inputs and assert the output
    assert request.open('GET', 'https://www.google.com')



# Generated at 2022-06-13 04:47:52.538309
# Unit test for function fetch_url
def test_fetch_url():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            url_username=dict(default='', no_log=True),
            url_password=dict(default='', no_log=True),
            force_basic_auth=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )

    url = module.params['url']
    url_username = module.params['url_username']
    url_password = module.params['url_password']
    force_basic_auth = module.params['force_basic_auth']

    if module.check_mode:
        raise AnsibleExitJson(changed=False)


# Generated at 2022-06-13 04:48:47.648347
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    from urllib.parse import urlparse
    from ansible.module_utils.urls import open_url
    import json
    from io import StringIO
    response = open_url('https://localhost')
    res = json.load(StringIO(response.read()))
    assert 'ansible' in res



# Generated at 2022-06-13 04:48:53.451337
# Unit test for function generic_urlparse
def test_generic_urlparse():
    parts = generic_urlparse(urlparse.urlparse('http://username:password@example.com/path/to/index.html#index'))
    assert parts['scheme'] == 'http'
    assert parts['netloc'] == 'username:password@example.com'
    assert parts['path'] == '/path/to/index.html'
    assert parts['params'] == ''
    assert parts['query'] == ''
    assert parts['fragment'] == 'index'
    assert parts['username'] == 'username'
    assert parts['password'] == 'password'
    assert parts['hostname'] == 'example.com'
    assert parts['port'] is None

    parts = generic_urlparse(urlparse.urlparse('http:///var/run/docker.sock/containers/json'))
    assert parts['scheme']

# Generated at 2022-06-13 04:48:55.901346
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    tmp_ca_cert_path, cadata, paths_checked = SSLValidationHandler(None, None).get_ca_certs()
    assert len(paths_checked) > 1

# Generated at 2022-06-13 04:48:59.635112
# Unit test for function atexit_remove_file
def test_atexit_remove_file():
    filename = "fetch_url_test.txt"
    with open(filename, "w+") as f:
        pass
    assert os.path.exists(filename) == 1
    atexit_remove_file(filename)
    assert os.path.exists(filename) == 0



# Generated at 2022-06-13 04:49:03.910203
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    # Tests use a public key, so the test is skipped if cryptography is not installed
    if not HAS_CRYPTOGRAPHY:
        return

    # Tests are using DER encoding of a public key, so that we can compare the returned result.
    # Certificate created by:
    # https://superdry.apphb.com/tools/online-rsa-key-converter
    # https://superdry.apphb.com/tools/online-asn1-parser
    #
    # The certificate contains the following ASN.1 structure:
    # 0:d=0  hl=4 l= 290 cons: SEQUENCE
    # 4:d=1  hl=2 l=   1 prim:  INTEGER           :00
    # 7:d=1  hl=2 l=  13 cons:  SEQU

# Generated at 2022-06-13 04:49:17.340558
# Unit test for function generic_urlparse
def test_generic_urlparse():
    '''
    basic tests for parsing URLs
    '''
    try:
        urlparse
    except NameError:
        urlparse = None
    def _urlparse(url):
        '''
        wrapper to call the urlparse method and return parts in the
        same format as is returned from the generic_urlparse method
        '''
        return generic_urlparse(urlparse.urlparse(url))
    def _test_url_type(url_type, url, netloc, hostname, port, username, password, **kwargs):
        '''
        test a specific type of URL
        '''

# Generated at 2022-06-13 04:49:25.970095
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
  urls = ['https://www.baidu.com', 'https://www.google.com', 'https://www.zhihu.com']
  for url in urls:
    req = RequestWithMethod(url)
    req.add_header('Connection', 'close')
    proxy_handler = build_opener(SSLValidationHandler(hostname='baidu.com', port=443))
    content = proxy_handler.open(req, timeout=10)
    assert content.status == 200, 'status code is: {}'.format(content.status)

if __name__ == "__main__":
  test_SSLValidationHandler_http_request()

# Generated at 2022-06-13 04:49:35.266126
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    url = 'https://example.com/path/file'
    for method in 'GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS':
        request = RequestWithMethod(url, method, 'data')
        assert request.get_method() == method.upper()


#
# urllib_request.quote, urllib_request.unquote, urllib_request.quote_plus and urllib_request.unquote_plus
# can't handle unicode strings on Python 2, so we need to encode them first
# except on Python 3 where they can handle unicode
#

# Generated at 2022-06-13 04:49:37.982598
# Unit test for function getpeercert
def test_getpeercert():
    fake_socket = Mock(getpeercert=Mock(return_value="FakeCertificate"),
                       raw=Mock(spec=socket.socket, _sock=fake_socket))
    fake_response = Mock(fp=fake_socket)

    assert getpeercert(fake_response) == "FakeCertificate"



# Generated at 2022-06-13 04:49:47.339295
# Unit test for function fetch_url
def test_fetch_url():
    # Mock the module to be called
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    # Mock the urlopen function
    with mock.patch.object(urllib.request, 'urlopen') as patch_urlopen:
        # Mock an object to be returned by the function
        mock_obj = mock.Mock()
        # The type of the object to be returned
        mock_obj.code = 200
        mock_obj.read.return_value = None
        mock_obj.info.return_value = None
        # To return the object
        patch_urlopen.return_value = mock_obj
        # Call the function
        fetch_url(module, '')
        # Check if it has returned the object
        assert patch_urlopen.return_value == mock_obj


# Generated at 2022-06-13 04:50:38.876805
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
  from ansible.module_utils.urls import SSLValidationHandler

  SSLValidationHandler = SSLValidationHandler('example.com', 443, None)
  assert SSLValidationHandler.detect_no_proxy('https://www.example.com:443') == True



# Generated at 2022-06-13 04:50:49.631270
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    ip = '1.1.1.1'
    hostname = 'my.host.name'
    protocol = 'https'
    url = build_url({'ip': ip, 'protocol': protocol, 'hostname': hostname})
    h = SSLValidationHandler(hostname, 443, None)

    # no 'no_proxy' environment variable is set
    os.environ.pop('no_proxy', None)
    assert h.detect_no_proxy(url) == True

    # case 1: hostname is *.my.host.name
    os.environ['no_proxy'] = '*.my.host.name, my.other.host.name'
    assert h.detect_no_proxy(url) == False

    # case 2: hostname is my.host.name

# Generated at 2022-06-13 04:51:01.458405
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    try:
        import urlparse  # pylint: disable=import-error
    except ImportError:
        import urllib.parse as urlparse
    import urllib.error as urllib_error
    import urllib.request as urllib_request
    from ansible.module_utils.urls import RedirectHandlerFactory

    class FakeRequest(urllib_request.Request):
        def __init__(self, url, method, data=None, headers=None, origin_req_host=None, unverifiable=True):
            self.method = method
            urllib_request.Request.__init__(self, url, data, headers, origin_req_host, unverifiable)

        def get_method(self):
            if self.method:
                return self.method
            else:
                return ur

# Generated at 2022-06-13 04:51:02.361260
# Unit test for function fetch_url
def test_fetch_url():
    pass

# Generated at 2022-06-13 04:51:11.154993
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import mock
    import os

    # Mock urllib_error.HTTPError, re.compile, and os.path.isdir
    HTTPError = urllib_error.HTTPError
    urllib_error.HTTPError = mock.Mock()
    re.compile = mock.Mock()
    os.path.isdir = mock.Mock(return_value=True)

    # With everything mocked, run the unit test

    # Test that the redirect handler is created and not the https handler
    RedirectHandlerFactory('all')
    assert urllib_error.HTTPError.call_count == 0
    RedirectHandlerFactory('no')
    assert urllib_error.HTTPError.call_count == 1
    RedirectHandlerFactory('urllib2')

# Generated at 2022-06-13 04:51:14.859748
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    with pytest.raises(OSError):
        c = UnixHTTPConnection('fake_socket')
        c.request('GET', '/')
        c.getresponse()


#
# Retry lib
#



# Generated at 2022-06-13 04:51:19.606113
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    handler = SSLValidationHandler('hostname', 'port')

    with mock.patch('ansible.module_utils.urls.urllib_request.BaseHandler.get_ca_certs', new=mock.Mock()):
        handler.get_ca_certs.return_value = ('blah', 'blah', 'blah')

        with mock.patch('ansible.module_utils.urls.urllib_request.socket') as mock_socket:
            with mock.patch('ansible.module_utils.urls.urllib_request.ssl') as mock_ssl:
                mock_socket.create_connection.return_value = s = mock.Mock()
                mock_socket.return_value = s = mock.Mock()

# Generated at 2022-06-13 04:51:30.057692
# Unit test for function fetch_url