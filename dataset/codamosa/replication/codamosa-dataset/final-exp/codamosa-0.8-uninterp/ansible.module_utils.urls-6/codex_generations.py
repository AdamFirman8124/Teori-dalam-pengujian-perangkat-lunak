

# Generated at 2022-06-13 04:45:34.692994
# Unit test for function get_channel_binding_cert_hash

# Generated at 2022-06-13 04:45:36.923925
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''This method tests that the UnixHTTPConnection raises an exception when
    trying to connect to a missing sock file'''
    connection = UnixHTTPConnection('/missing/server.sock')
    with pytest.raises(OSError) as exc:
        connection.connect()
    assert 'Invalid Socket File' in str(exc)



# Generated at 2022-06-13 04:45:43.564372
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    '''
    Run the RedirectHandlerFactory unit tests
    '''
    follow_redirects_list = [True, 'all', False, 'none', 'no', 'safe', 'urllib2']
    # Instantiate each of the handlers, and store in a dict
    # so we can generate a list of all the handlers for the unit test
    # (this is for the unit test, the actual code will only use one handler)
    redirect_handlers = dict((follow_redirects, RedirectHandlerFactory(follow_redirects)) for follow_redirects in follow_redirects_list)

    # Run test data
    # (this is for the unit test, the actual code will only use one set of test data)

# Generated at 2022-06-13 04:45:46.045800
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    unix_http_connection = UnixHTTPConnection('/foo/bar')
    assert unix_http_connection.sock == None
    unix_http_connection('localhost', 8080)
    assert isinstance(unix_http_connection, httplib.HTTPConnection)



# Generated at 2022-06-13 04:45:54.787085
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    from ansible.module_utils.six.moves.urllib.parse import urlparse

    url = "https://www.google.com"

    # Check for a normal url
    validate_cert = maybe_add_ssl_handler(url, True, "")
    parsed = urlparse(url)
    assert parsed.hostname == validate_cert.hostname
    assert parsed.port == validate_cert.port

    # Check for a port in the url
    url = "https://www.google.com:636"
    validate_cert = maybe_add_ssl_handler(url, True, "")
    parsed = urlparse(url)
    assert parsed.hostname == validate_cert.hostname
    assert parsed.port == validate_cert.port


# add_context_to_pyopenssl_class
# Add a ssl

# Generated at 2022-06-13 04:45:57.651892
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    handler = maybe_add_ssl_handler('https://www.python.org/', True)
    assert handler is not None
    handler = maybe_add_ssl_handler('https://www.python.org/', False)
    assert handler is None
    handler = maybe_add_ssl_handler('http://www.python.org/', False)
    assert handler is None


# Generated at 2022-06-13 04:46:05.544304
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    import tempfile
    import threading
    import time
    import unittest
    # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    #     temp_file.write(b'data')
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b'data')
    temp_file.close()

    class Test(unittest.TestCase):
        def test(self):
            def server():
                s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                s.bind(temp_file.name)
                s.listen(1)
                conn, _ = s.accept()
                conn.recv(1024)

# Generated at 2022-06-13 04:46:16.831831
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    from time import gmtime, strptime
    assert rfc2822_date_string(gmtime(), zone='-0000') == 'Sun, 19 Mar 2017 19:19:21 -0000'
    assert rfc2822_date_string(gmtime(), zone='+0000') == 'Sun, 19 Mar 2017 19:19:21 +0000'
    assert rfc2822_date_string(strptime('Sat, 11 Jan 1975 08:00:00 +0000', '%a, %d %b %Y %H:%M:%S %z'), zone='-0000') == 'Sat, 11 Jan 1975 08:00:00 -0000'

# Generated at 2022-06-13 04:46:21.017599
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    handler = SSLValidationHandler('test_hostname', 443)
    assert handler.get_ca_certs()
    assert len(handler.get_ca_certs()[1]) > 0
    assert handler.get_ca_certs()[0] is None

# Generated at 2022-06-13 04:46:27.997665
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():

    # Generate a self-signed cert which we can use to test this function
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    name = x509.Name([
        x509.NameAttribute(x509.oid.NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(x509.oid.NameOID.STATE_OR_PROVINCE_NAME, u"Massachusetts"),
        x509.NameAttribute(x509.oid.NameOID.LOCALITY_NAME, u"Boston"),
        x509.NameAttribute(x509.oid.NameOID.COMMON_NAME, "SomeHostName")
    ])

    # Use 10 years of validity
    valid_

# Generated at 2022-06-13 04:47:18.589969
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():

    def _build_req(url):
        req = urllib_request.Request(url)
        req.get_method = lambda: 'HEAD'
        return req

    # We need to test validation of ssl
    # with the following cases
    # 1. Connect to a host with a ssl certificate
    #      whose domain matches the hostname
    # 2. Connect to a host with a ssl certificate
    #      whose domain does not match the hostname
    # 3. Connect to a host with a ssl certificate
    #      whose certificate is signed by a vendor CA
    # 4. Connect to a host with a ssl certificate
    #      whose certificate is signed by a private CA
    # 5. Connect to a host with a ssl certificate
    #      whose certificate is self-signed

    # Case 1
    # connect to a host with a s

# Generated at 2022-06-13 04:47:26.948149
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    try:
        ssl_context = urllib_request.HTTPSHandler(debuglevel=0)
        ssl_context.https_open = ssl_context.do_open
        urllib_request.install_opener(urllib_request.build_opener(ssl_context))
        urllib_request.urlopen('https://google.com')
    except urllib_error.URLError as e:
        print(e)
    return True


# Generated at 2022-06-13 04:47:35.463725
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    class Mock_get_ca_certs():
        def __init__(self):
            self.paths_checked = []
            self.cadata = bytearray()
        def get_ca_certs(self):
            self.paths_checked.append('/etc/ssl/certs')
            self.cadata.extend(b'certificate')
            self.paths_checked.append('/etc/pki/ca-trust/extracted/pem')
            self.cadata.extend(b'certificate')
            self.paths_checked.append('/etc/pki/tls/certs')
            self.cadata.extend(b'certificate')
            self.paths_checked.append('/usr/share/ca-certificates/cacert.org')
            self

# Generated at 2022-06-13 04:47:47.391418
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    # Test using a urllib2 compatible redirect handler
    follow_redirects = 'urllib2'
    validate_certs = True
    ca_path = None
    RedirectHandler = RedirectHandlerFactory(follow_redirects, validate_certs, ca_path)
    redirect_handler = RedirectHandler()
    request = RequestWithMethod('https://www.google.com', 'GET')

    # Test using a urllib2 compatible redirect handler
    follow_redirects = 'urllib2'
    validate_certs = True
    ca_path = None
    RedirectHandler = RedirectHandlerFactory(follow_redirects, validate_certs, ca_path)
    redirect_handler = RedirectHandler()

    # Test http 301 redirect

# Generated at 2022-06-13 04:47:53.149825
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    hostname = 'pypi.python.org'
    port = 443
    ca_path = ''
    s = SSLValidationHandler(hostname, port, ca_path)
    cafile, cadata, paths_checked = s.get_ca_certs()
    assert cafile == ''
    assert cadata is None
    assert paths_checked == ['/etc/ssl/certs']


# Generated at 2022-06-13 04:48:02.118535
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    class TestAnsibleModule(object):
        def __init__(self):
            self.params = dict()
            self.params['environment'] = dict()
            self.params['environment']['no_proxy'] = None
            self.params['environment']['https_proxy'] = None
            self.fail_json = None
            self.fail_json_in_check_mode = None
            self.exit_json = None
            self.params['no_log'] = True
            self.params['_ansible_check_mode'] = False

    module = TestAnsibleModule()
    url = 'http://example.org/my/url'
    # Check that with No Proxy, it returns the expected false value
    actual = SSLValidationHandler(module.params['url']).detect_no_proxy(url)

# Generated at 2022-06-13 04:48:10.154016
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    # Test redirects
    for redirect in ('no', 'none', 'urllib2', False):
        h = RedirectHandlerFactory(follow_redirects=redirect)()
        assert hasattr(h, 'redirect_request')
    # Test bad redirects
    for redirect in ('all', 'yes', 'safe', True, 'foo', None):
        try:
            RedirectHandlerFactory(follow_redirects=redirect)()
        except Exception:
            pass
        else:
            assert False, 'An error should have been raised'


# Generated at 2022-06-13 04:48:17.031636
# Unit test for constructor of class CustomHTTPSConnection
def test_CustomHTTPSConnection():
    conn = CustomHTTPSConnection(HOSTNAME, PORT)
    assert conn is not None


if hasattr(urllib_request, 'HTTPSHandler'):
    class CustomHTTPSHandler(urllib_request.HTTPSHandler):
        def https_open(self, req):
            return self.do_open(CustomHTTPSConnection, req)


if hasattr(urllib_request, 'HTTPSHandler'):

    class HTTPSClientAuthHandler(urllib_request.HTTPSHandler):

        def __init__(self, key, cert):
            urllib_request.HTTPSHandler.__init__(self)
            self.key = key
            self.cert = cert


# Generated at 2022-06-13 04:48:27.008874
# Unit test for method connect of class UnixHTTPSConnection
def test_UnixHTTPSConnection_connect():
    class MockUnixHTTPConnection(object):
        def connect(self):
            pass
    mock_unix_http_connection = MockUnixHTTPConnection()
    mock_unix_http_connection.connect = Mock(return_value=None)
    mocked_unix_http_connection_connect = mock_unix_http_connection.connect

    with unix_socket_patch_httpconnection_connect():
        unix_https_connection = UnixHTTPSConnection(None)
        unix_https_connection.connect()
        mocked_unix_http_connection_connect.assert_called_once_with()


#
# HTTP connection handling
#


# Generated at 2022-06-13 04:48:36.282584
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    import mock
    import os
    os.environ['ANSIBLE_KEEP_REMOTE_FILES'] = '1'
    import ansible.module_utils.urls as urls
    h = CustomHTTPSConnection(
        '1.1.1.1',
        port = 80,
        ca_cert = 'some_cert',
        key_file = 'some_key',
        cert_file = 'some_cert',
        timeout = 10)

    h.connect()
    h._tunnel_host = '1.1.1.2'
    h._tunnel()
    h._tunnel_host = None
    h.source_address = '1.1.1.3'
    h.connect()
    h.context = mock.sentinel.context
    h.context.wrap_socket.side_effect

# Generated at 2022-06-13 04:50:29.096734
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    url = 'https://www.google.com/'
    try:
        #https://stackoverflow.com/questions/29459106/python-get-domain-name-from-url
        hostname = urlparse(url).netloc
    except AttributeError:
        hostname = None
    try:
        port = urlparse(url).port
    except AttributeError:
        port = 443
    validate_certs = True
    if port == None:
        port = 443
    handler = SSLValidationHandler(hostname, port, validate_certs)
    http_req = Request(url)
    handler.http_request(http_req)


# Generated at 2022-06-13 04:50:38.219509
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    hostname = "test.com"
    port = 443
    ca_path = "/etc/ssl/test.pem"
    expected_path = ca_path
    expected_data = "data"

    class MockContext(object):
        def load_verify_locations(self, cafile, cadata):
            self.cafile = cafile
            self.cadata = cadata

    def get_ca_certs_method(SSLValidationHandler):
        # args
        handler = SSLValidationHandler(hostname, port, ca_path)

        # mocks
        if HAS_SSLCONTEXT:
            ssl.create_default_context = lambda: MockContext()


# Generated at 2022-06-13 04:50:39.570452
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    conn = UnixHTTPConnection('/tmp/foo')
    assert conn.sock == None
    conn = conn('/tmp/foo', 80)
    assert conn.sock != None



# Generated at 2022-06-13 04:50:43.551315
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    handler = SSLValidationHandler("", 443)
    if handler.validate_proxy_response("HTTP/1.1 200 OK\r\n") is None:
        raise Exception("test_SSLValidationHandler_validate_proxy_response(): Test failed")


# Generated at 2022-06-13 04:50:50.084954
# Unit test for method make_context of class SSLValidationHandler
def test_SSLValidationHandler_make_context():
    _hostname = 'hostname'
    _port = 80
    _ca_path = None
    _ca_file = '/etc/ssl/certs'
    _ca_data = bytearray()

    handler = SSLValidationHandler(_hostname, _port, _ca_path)

    try:
        context = handler.make_context(_ca_file, _ca_data)
        assert isinstance(context, ssl.SSLContext)
    except NotImplementedError:
        pass


# Generated at 2022-06-13 04:50:58.077852
# Unit test for function fetch_file
def test_fetch_file():
    # Save the original function in case there's a mock somewhere
    original_fetch_url = __name__ + '.fetch_url'
    mocked_fetch_url = __name__ + '.test_fetch_file.mocked_fetch_url'

# Generated at 2022-06-13 04:51:08.929451
# Unit test for method patch of class Request
def test_Request_patch():
    def test():
        from requests.packages.urllib3.exceptions import MaxRetryError
        from requests.adapters import HTTPAdapter
        from ansible.module_utils._text import to_bytes
        from ansible.module_utils.connection import ConnectionError
        from ansible.module_utils.connection import Connection
        from ansible.module_utils.six.moves.urllib.error import HTTPError
        from ansible.module_utils.six.moves.urllib.error import URLError
        from ansible.module_utils.six.moves.urllib.request import Request
        connection = Connection(None)

# Generated at 2022-06-13 04:51:14.768723
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    # Test for method detect_no_proxy
    class TestSSLValidationHandler(SSLValidationHandler):
        def __init__(self, hostname, port):
            self.hostname = hostname
            self.port = port

    ssl_handler = TestSSLValidationHandler('example.com', '443')
    # Test1 is a success case with https_proxy set and no_proxy set to not include example.com
    os.environ['https_proxy'] = 'https://127.0.0.1:8080'
    os.environ['no_proxy'] = 'otherdomain.net, otherdomain.com'
    assert ssl_handler.detect_no_proxy('https://example.com/test') is False

    # Test2 is a success case with https_proxy set and no_proxy set to include example.com
   

# Generated at 2022-06-13 04:51:16.882266
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    url = "http://www.google.com"
    expected_result = True

    handler = SSLValidationHandler("", 0)
    result = handler.detect_no_proxy(url)

    assert result == expected_result


# Generated at 2022-06-13 04:51:23.329338
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    '''
    tests the http_request method of SSLValidationHandler class
    '''

    # This example code only tests the condition where
    # SSLValidationHandler.get_ca_certs returns non-empty value
    # to simulate that, we need to update the module level
    # LOADED_VERIFY_LOCATIONS with a path
    LOADED_VERIFY_LOCATIONS.append("/some/path")

    # We will return empty values for temp file as we are
    # only interested to test the path with non-empty reutrn
    # values from get_ca_certs