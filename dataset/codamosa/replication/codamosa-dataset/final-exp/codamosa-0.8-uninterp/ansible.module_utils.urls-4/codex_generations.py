

# Generated at 2022-06-13 04:46:26.432755
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''Handles http requests to a unix socket file'''
    # Initialize UnixHTTPConnection object
    unix_http_conn = UnixHTTPConnection('foo')
    mock_socket = mock.MagicMock()
    unix_http_conn.sock = mock_socket

    # Perform the connect
    unix_http_conn.connect()
    assert mock_socket.connect.called


# Generated at 2022-06-13 04:46:29.681417
# Unit test for method open of class Request
def test_Request_open():
    # Declare the instance of class Request
    req = Request()
    # Check the type of variable returned by method open
    assert isinstance(req.open(method='GET', url='api.github.com'), urllib_request.Response)


# Generated at 2022-06-13 04:46:40.814581
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    class MockRequest():
        class MockOpener():
            class MockHttpHandler():
                def __init__(self, foo=None, validate_certs=None, ca_path=None):
                    self.foo = foo
                    self.validate_certs = validate_certs
                    self.ca_path = ca_path
                def https_open(self, req):
                    return None

            def add_handler(self, handler):
                assert handler
                assert handler.validate_certs
                assert handler.ca_path == 'ca_path'

        def __init__(self, method, url, data=None, headers=None, origin_req_host=None, unverifiable=True):
            self.method = method
            self.url = url
            self.data = data
            self.headers = headers
            self.origin

# Generated at 2022-06-13 04:46:44.246244
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    assert rfc2822_date_string(time.gmtime(0)) == 'Thu, 01 Jan 1970 00:00:00 -0000'



# Generated at 2022-06-13 04:46:50.118178
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    import time

    for x in range(1, 10):
        a = rfc2822_date_string(time.localtime(x * 10000))
        b = time.strftime('%a, %d %b %Y %H:%M:%S -0000', time.localtime(x * 10000))
        assert a == b



# Generated at 2022-06-13 04:46:53.379579
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    http_response = AnsibleResponse('200 OK', '12345')
    request = SSLValidationHandler('www.google.com', 443)
    assert request.http_request('request') == 'request'


# Generated at 2022-06-13 04:47:06.100639
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    __call___args = dict()
    __call___args['host'] = 'host'
    __call___args['port'] = 'port'
    __call___args['timeout'] = 'timeout'
    __call___args['source_address'] = 'source_address'
    __call___args['sock'] = 'sock'
    __call___args['_tunnel_host'] = '_tunnel_host'
    __call___args['_tunnel_port'] = '_tunnel_port'
    __call___args['strict'] = 'strict'
    return UnixHTTPConnection('unix_socket')(**__call___args)
#
# Utilities
#


# Generated at 2022-06-13 04:47:11.941795
# Unit test for function fetch_url
def test_fetch_url():
    module, conn = mock_module_helper()
    url = 'http://example.com/'
    data = 'data'
    headers = dict(Content_type='application/json')
    method = 'POST'
    use_proxy = False
    force = False
    last_mod_time = None
    timeout = 10
    use_gssapi = False
    unix_socket = None
    cookies = None
    unredirected_headers = None
    r, info = fetch_url(module, url, data, headers, method, use_proxy, force,
                        last_mod_time, timeout, use_gssapi, unix_socket, cookies, unredirected_headers)
    assert info['url'] == url
    assert info['msg'] == 'OK (%s bytes)' % info['content-length']

# Generated at 2022-06-13 04:47:15.090441
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    ssl_handler = SSLValidationHandler('localhost', 443)
    assert ssl_handler.get_ca_certs() != None



# Generated at 2022-06-13 04:47:19.746420
# Unit test for function getpeercert
def test_getpeercert():
    try:
        import ssl
    except ImportError:
        return
    try:
        # We can't just use ansible.module_utils.urls.urllib_error.URLError because it's not a proper
        # subclass of Exception and we can't catch it in Ansible code
        raise urllib_error.URLError('test')
    except urllib_error.URLError:
        response = sys.exc_info()[1]
        assert getpeercert(response) is None
        assert getpeercert(response, binary_form=True) is None

    if PY3:
        response.fp.raw._sock = ssl.SSLSocket(context=TLS_CONTEXT)  # pylint: disable=protected-access
    else:
        response.fp._s

# Generated at 2022-06-13 04:48:25.847983
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    from time import gmtime, strftime
    from email.utils import parsedate_tz, mktime_tz
    from datetime import datetime
    time_tuple = gmtime()
    rfc2822_string = rfc2822_date_string(time_tuple)
    time_epoch = mktime_tz(parsedate_tz(rfc2822_string))
    # This should be very close to 0
    assert abs(time_epoch - time.mktime(time_tuple)) < 1

# -----------------------------------------------------------------------------



# Generated at 2022-06-13 04:48:35.397218
# Unit test for function get_channel_binding_cert_hash

# Generated at 2022-06-13 04:48:43.030158
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    # test if port number is included in the URL
    url = "https://example.com:8080/"
    handler = maybe_add_ssl_handler(url, 1)
    result = handler.hostname
    expected = "example.com"
    assert result==expected
    result = handler.port
    expected = 8080
    assert result==expected
    assert handler.ca_path is None
    # test if port number is not included in the URL
    url = "https://example.com/"
    handler = maybe_add_ssl_handler(url, 1)
    result = handler.hostname
    expected = "example.com"
    assert result==expected
    result = handler.port
    expected = 443
    assert result==expected
    assert handler.ca_path is None

    # Test if ca_path is passed in

# Generated at 2022-06-13 04:48:52.340066
# Unit test for function fetch_file
def test_fetch_file():
    import os, tempfile
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.urls import fetch_file
    from ansible.module_utils.common.collections import ImmutableDict

    def urlretrieve_side_effect(url, filename=None, reporthook=None, data=None):
        fh = open(filename, 'w')
        fh.write("test data")
        fh.close()

    url_mock = Mock(side_effect=urlretrieve_side_effect)


# Generated at 2022-06-13 04:48:57.297794
# Unit test for constructor of class CustomHTTPSConnection
def test_CustomHTTPSConnection():
    # A non-existant host should fail to validate cert when
    # we pass in a ca_cert file
    if HAS_SSLCONTEXT:
        try:
            CustomHTTPSConnection('localhost', 0, ca_certs=b_DUMMY_CA_CERT)
        except SSLValidationError:
            pass
        else:
            assert False, "SSLCONTEXT should have raised invalid cert"
    # An existant host should validate the cert when we pass in a ca_cert file
    else:
        CustomHTTPSConnection('www.ansible.com', 443, ca_certs=b_DUMMY_CA_CERT)

    # A non-existant host should fail to validate cert when
    # we pass in a ca_cert file but allow insecure requests

# Generated at 2022-06-13 04:49:02.393443
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    class MyHTTPConnection(HTTPConnection):
        def __init__(self, *args, **kwargs):
            HTTPConnection.__init__(self, *args, **kwargs)

        def connect(self):
            pass

    class MyHTTPSConnection(HTTPSConnection):
        def __init__(self, *args, **kwargs):
            HTTPSConnection.__init__(self, *args, **kwargs)

        def connect(self):
            pass

    class MyHandler(HTTPSHandler):
        def __init__(self, *args, **kwargs):
            HTTPSHandler.__init__(self, *args, **kwargs)

        def https_open(self, req):
            return self.do_open(MyHTTPSConnection, req)

    def test_url(url, use_proxy=True):
        ssl

# Generated at 2022-06-13 04:49:06.266216
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    assert RequestWithMethod('http://127.0.0.1', 'GET').get_method() == 'GET'
    assert RequestWithMethod('http://127.0.0.1', 'POST', '{"id": 1}').get_method() == 'POST'



# Generated at 2022-06-13 04:49:17.305429
# Unit test for function fetch_url
def test_fetch_url():

    req_headers = \
        {
            'User-Agent': 'python-requests/2.20.1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }

    r = Mock()
    r.code = 200
    r.msg = 'OK'
    r.headers = req_headers
    r.geturl = Mock(return_value='http://www.google.com')


# Generated at 2022-06-13 04:49:29.568344
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    from ansible.compat.tests.mock import patch
    import socket

    @patch.object(SSLValidationHandler, 'get_ca_certs')
    @patch.object(SSLValidationHandler, 'validate_proxy_response')
    @patch.object(SSLValidationHandler, 'make_context')
    def test_SSLValidationHandler_http_request(mock_context_obj, mock_validate_response, mock_get_ca_cert):
        ca_path = '/test_dir/test_cert.pem'
        hostname = 'www.google.com'
        port = 443
        mock_get_ca_cert.return_value = ca_path, b'', [ca_path]
        mock_validate_response.return_value = None
        ssl_handler_obj = SSLValidationHandler

# Generated at 2022-06-13 04:49:37.202417
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    with patch("socket.create_connection", return_value=True):
        with patch("ssl.wrap_socket", return_value=True):
            with patch("os.path.exists", return_value=True):
                with patch("os.access", return_value=True):
                    with patch("os.R_OK", return_value=True):
                        my_connection = CustomHTTPSConnection("fake_host")
                        my_connection.connect()
    assert my_connection.sock


    class CustomHTTPSHandler(urllib_request.HTTPSHandler):
        def __init__(self, debuglevel=0, context=None, check_hostname=None):
            urllib_request.HTTPSHandler.__init__(self, debuglevel)
            self._context = context
            self._check_hostname = check_host

# Generated at 2022-06-13 04:51:03.570364
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    import doctest

    globs = {'handler': SSLValidationHandler('www.google.com','443')}
    doctest.run_docstring_examples(SSLValidationHandler.get_ca_certs, globs, True)



# Generated at 2022-06-13 04:51:16.379608
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
  import httplib
  import ssl
  import socket
  class https_connection(httplib.HTTPSConnection):
    def __init__(self, host, port=None, key_file=None, cert_file=None, strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
      self.key_file=key_file
      self.cert_file=cert_file
      httplib.HTTPSConnection.__init__(self, host, port, strict, timeout)
    def connect(self):
      "Connect to a host on a given (SSL) port."
      sock = socket.create_connection((self.host, self.port), self.timeout)
      server_hostname = self.host
      server_hostname = self._tunnel_host
      self.sock = ssl.wrap_

# Generated at 2022-06-13 04:51:20.905124
# Unit test for function fetch_url
def test_fetch_url():

    module.params = dict(
        use_proxy=False,
        timeout=20,
        url='http://127.0.0.1:2401',
        url_username='username',
        url_password='password',
        force_basic_auth=True,
        http_agent='ansible-test',
        validate_certs=True,
        follow_redirects='urllib2',
        client_cert=None,
        client_key=None,
        use_gssapi=False,
        unix_socket=None,
        ca_path='/path',
    )

    fetch_url(module, 'http://127.0.0.1:2401')

#
# HTTP AUTHENTICATION STUFF

# HTTPProxyAuthHandler was only added in 2.4 so we must create it ourselves
