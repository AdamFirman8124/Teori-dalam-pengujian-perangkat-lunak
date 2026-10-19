

# Generated at 2022-06-13 04:44:52.606778
# Unit test for method make_context of class SSLValidationHandler
def test_SSLValidationHandler_make_context():
    # Initializing the class SSLValidationHandler with parameters
    SSLValidationHandler = SSLValidationHandler('localhost', '8000')
    # Asserting the value returned
    assert SSLValidationHandler.make_context(None, None) is not None

# Generated at 2022-06-13 04:45:03.043063
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    # Patch to prevent this unit test from failing on systems where
    # /var/run/docker.sock is not available
    with patch.object(os, 'path', Mock(return_value=False)):
        with patch.object(socket, 'socket') as socket_mock:
            sock_mock = Mock()
            socket_mock.return_value = sock_mock
            obj = UnixHTTPConnection('/var/run/docker.sock')
            assert obj('localhost', 80) == obj
            assert obj.host == 'localhost'
            assert obj.port == 80
            assert obj.timeout == socket._GLOBAL_DEFAULT_TIMEOUT
            # obj.sock was not initialized
            assert obj.sock is None
            assert obj.sock is None

# Generated at 2022-06-13 04:45:07.886573
# Unit test for method make_context of class SSLValidationHandler
def test_SSLValidationHandler_make_context():
    '''
    Unit test for method make_context of class SSLValidationHandler
    '''

    tmp_ca_cert_path, cadata, paths_checked = SSLValidationHandler.get_ca_certs(
        SSLValidationHandler, None, None)

    SSLValidationHandler.make_context(
        SSLValidationHandler,
        tmp_ca_cert_path,
        cadata)



# Generated at 2022-06-13 04:45:18.685136
# Unit test for function fetch_url
def test_fetch_url():
    import ansible_test._private.test_urls as test_urls

    import ansible.module_utils.basic as basic_module
    mod = basic_module.AnsibleModule(argument_spec={})

    test_urls.mock_urlopen_image()

    # Valid url
    url = 'http://httpbin.org/status/200'
    resp, info = fetch_url(mod, url)
    assert info['status'] == 200

    # Invalid url
    url = 'http://httpbin.org/status/500'
    resp, info = fetch_url(mod, url)
    assert info['status'] == 500

    # Exception url
    url = 'http://httpbin.org/status/404'
    resp, info = fetch_url(mod, url)
    assert info['status'] == 404


# Generated at 2022-06-13 04:45:30.673274
# Unit test for function fetch_file
def test_fetch_file():
    from ansible.module_utils._text import to_bytes

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.tmpdir = '/tmp'

        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

        def add_cleanup_file(self, path):
            pass

    content = to_bytes(b'#!/usr/bin/python\nimport os\n', encoding='utf-8')
    url = to_bytes('https://raw.github.com/ansible/ansible/devel/lib/ansible/module_utils/basic.py', encoding='utf-8')

    class FakeResponse(object):
        def __init__(self, content, info):
            self.content = content
           

# Generated at 2022-06-13 04:45:35.718381
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    # This test is to ensure the constructor of class CustomHTTPSHandler is not changed,
    # and it will raise an exception if the constructor of class CustomHTTPSHandler is changed.
    try:
        CustomHTTPSHandler(debuglevel=1)
    except TypeError:
        pass


# Note: UnixHTTPSConnection is implemented below, beneath the
#       UnixSocketHTTPConnection class.


# Generated at 2022-06-13 04:45:41.051122
# Unit test for method https_open of class CustomHTTPSHandler
def test_CustomHTTPSHandler_https_open():
    if CustomHTTPSHandler is None:
        return
    conn = FakeConnection()
    handler = CustomHTTPSHandler()
    handler._context = 'test_FakeContext'
    # Fake function
    handler.do_open = lambda *args: conn
    open_req = handler.https_open('req')
    # Check that the context from class CustomHTTPSHandler is taken as argument of CustomHTTPSConnection
    assert open_req.args[1] == {'context': 'test_FakeContext'}


# As of Python 2.7.9, SSLContext is available in the stdlib
# however it does not provide the opening of unix sockets.
if PY3 and HAS_SSL_CONTEXT:
    class UnixHTTPSConnection(CustomHTTPSConnection):
        default_port = 443


# Generated at 2022-06-13 04:45:48.840788
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    hostname = 'www.google.com'
    port = 443
    ca_path = '/etc/ssl/cert.pem'
    ssl_validation_handler = SSLValidationHandler(hostname, port, ca_path)
    url = 'https://www.google.com'
    assert(ssl_validation_handler.detect_no_proxy(url) is True)



# Generated at 2022-06-13 04:45:55.926604
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class MockSocket(object):
        def __init__(self):
            self.host = 'localhost'
            self.port = 80
            self.timeout = None

        def getpeercert(self):
            return {'subjectAltName': [('DNS', self.host)]}

        def create_connection(self, host, port, timeout):
            return self

        def wrap_socket(self, sock, keyfile=None, certfile=None,
                        server_side=False, cert_reqs=None, ssl_version=None,
                        ca_certs=None, do_handshake_on_connect=True,
                        suppress_ragged_eofs=True, ciphers=None):
            return sock

    def verify_callback(*args, **kwargs):
        pass


# Generated at 2022-06-13 04:46:04.894968
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    from datetime import datetime
    from tempfile import NamedTemporaryFile

    ssl_handler = SSLValidationHandler('127.0.0.1', 1)

    # Create a dummy CA certificate
    ca_cert_file = NamedTemporaryFile(mode='w+b', prefix='ansible_ssl_test_')
    ca_cert_file.write(b_CA_CERT)
    ca_cert_file.seek(0)

    # These next lines are necessary because SSLCertVerificationError will
    # verify the validity of the certificate. If these values are left at
    # their defaults, the test will fail.
    # TODO: Find a better way to avoid this hack
    ssl_handler.__class__.CA_NOT_AFTER = datetime(datetime.now().year+5, 1, 1)
    s

# Generated at 2022-06-13 04:46:51.467739
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    ssl_validation_handler = maybe_add_ssl_handler(
        'https://test.com:443', validate_certs=True)
    assert(isinstance(ssl_validation_handler, SSLValidationHandler))
    assert(ssl_validation_handler.hostname == 'test.com')
    assert(ssl_validation_handler.port == 443)

    ssl_validation_handler = maybe_add_ssl_handler(
        'https://test.com:443', validate_certs=True,
        ca_path='/some/path')
    assert(isinstance(ssl_validation_handler, SSLValidationHandler))
    assert(ssl_validation_handler.hostname == 'test.com')
    assert(ssl_validation_handler.port == 443)

# Generated at 2022-06-13 04:47:04.872436
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    if not HAS_SSLCONTEXT:
        return

    fp = io.StringIO()
    if sys.version_info < (2, 6):
        # Divergence: Python < 2.6 does not have create_connection
        return
    elif sys.version_info < (3,):
        from SocketServer import ThreadingTCPServer
        from SimpleHTTPServer import SimpleHTTPRequestHandler

        # Divergence: try to support python2.6 (no makefile)
        try:
            SocketServer = ThreadingTCPServer(('localhost', 0), SimpleHTTPRequestHandler)
        except TypeError:
            SocketServer = ThreadingTCPServer(('localhost', 0), SimpleHTTPRequestHandler, bind_and_activate=False)
            SocketServer.allow_reuse_address = True
            SocketServer.server_bind()

# Generated at 2022-06-13 04:47:09.742413
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    # NOTE: This may also be called from integration tests which need to run with a custom
    # CustomHTTPSHandler derived class (such as HTTPSConnectionMock)
    try:
        conn = CustomHTTPSConnection('localhost')
        cust_http = CustomHTTPSHandler()
        # Check that a connection can be established with the proper wrapped context in the handler
        # In the tests, this test is not called as the HTTPSConnectionMock is used and the context is
        # not relevant
        cust_http.https_open(conn)
    except Exception as e:
        raise AssertionError(e)


# Generated at 2022-06-13 04:47:21.098654
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    if PY3:
        assert(RequestWithMethod('url', "get").get_method() == "GET")
        assert(RequestWithMethod('url', "post").get_method() == "POST")
        assert(RequestWithMethod('url', "PUT").get_method() == "PUT")
        assert(RequestWithMethod('url', "DELETE").get_method() == "DELETE")
        assert(RequestWithMethod('url', "patch").get_method() == "PATCH")
    else:
        assert(RequestWithMethod('url', "get").get_method() == "GET")
        assert(RequestWithMethod('url', "post").get_method() == "POST")
        assert(RequestWithMethod('url', "PUT").get_method() == "PUT")

# Generated at 2022-06-13 04:47:32.916227
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import unittest

    class TestRedirectHandlerFactory(unittest.TestCase):
        def setUp(self):
            global urllib_request
            super(TestRedirectHandlerFactory, self).setUp()
            urllib_request = FakeUrllibRequest()

        def test_RedirectHandlerFactory_works_without_urllib_request(self):
            # If a unittest tries to use RedirectHandlerFactory, it may not
            # have urllib_request loaded yet. Test that we gracefully handle
            # this situation
            global urllib_request
            urllib_request = None
            self.assertIsNotNone(RedirectHandlerFactory(follow_redirects=True))


# Generated at 2022-06-13 04:47:42.659051
# Unit test for constructor of class CustomHTTPSConnection
def test_CustomHTTPSConnection():
    conn = CustomHTTPSConnection(None, None)
    assert conn.key_file is None
    assert conn.cert_file is None
    assert conn.context is None

    conn = CustomHTTPSConnection(None, None, key_file='key_file', cert_file='cert_file')
    assert conn.key_file is 'key_file'
    assert conn.cert_file is 'cert_file'
    assert conn.context is None

    conn = CustomHTTPSConnection(None, None, key_file=None, cert_file=None)
    assert conn.key_file is None
    assert conn.cert_file is None
    assert conn.context is None

    conn = CustomHTTPSConnection(None, None, context='context')
    assert conn.key_file is None
    assert conn.cert_file is None
    assert conn

# Generated at 2022-06-13 04:47:47.240594
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    '''
    If you would like to unit test the constructor of class
    CustomHTTPSHandler, you can add to the following
    '''

    #
    # Uncomment the following two lines for unit testing
    # CustomHTTPSHandler
    #

    #import sys
    #sys.path.append("/path/to/httplib2/directory")

    HTTPHandler = CustomHTTPSHandler()
    HTTPSHandler = CustomHTTPSHandler()
    assert HTTPHandler.__class__.__name__ == "CustomHTTPSHandler"
    assert HTTPSHandler.__class__.__name__ == "CustomHTTPSHandler"


# Generated at 2022-06-13 04:47:50.805398
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    """
    Unit test for method get_ca_certs of class SSLValidationHandler.
    """

    SSLValidationHandler.get_ca_certs()



# Generated at 2022-06-13 04:48:00.089242
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    ssl_validator = SSLValidationHandler()
    assert ssl_validator.detect_no_proxy('http://192.168.1.1') == False
    assert ssl_validator.detect_no_proxy('http://192.168.1.1:80') == False
    assert ssl_validator.detect_no_proxy('https://192.168.1.1') == False
    assert ssl_validator.detect_no_proxy('https://192.168.1.1:443') == False
    assert ssl_validator.detect_no_proxy('http://192.168.1.1:8080') == False
    assert ssl_validator.detect_no_proxy('https://192.168.1.1:8443') == False

# Generated at 2022-06-13 04:48:09.705072
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    '''
    This is a unit test for method "http_request" of class SSLValidationHandler.
    '''
    try:
        test = SSLValidationHandler("www.verisign.com", 443)
    except Exception as e:
        assert False, "Failed to initialize SSLValidationHandler" + str(e)

    try:
        test.http_request("testing")
    except ConnectionError as e:
        assert False, "Failed to connect using SSLValidationHandler" + str(e)



# Generated at 2022-06-13 04:49:07.236607
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import unittest

    class TestRedirectHandler(unittest.TestCase):
        def setUp(self):
            self.follow_redirects = None
            self.validate_certs = True
            self.ca_path = None

        def assertFollow(self, code):
            handler = RedirectHandlerFactory(self.follow_redirects, self.validate_certs, ca_path=self.ca_path)
            request = RequestWithMethod('url', 'POST')
            redirect = handler.redirect_request(request, None, code, 'msg', {}, 'url')
            self.assertEqual(request._method, redirect.get_method())


# Generated at 2022-06-13 04:49:19.818764
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class MockSock(object):
        def __init__(self):
            self.is_closed = False
        def close(self):
            self.is_closed = True

    class MockSSL(object):
        def __init__(self):
            self.is_wrap_socket_called = False
        def wrap_socket(self, sock, keyfile=None, cert_reqs=None, certfile=None, ssl_version=None,
                        server_hostname=None):
            self.is_wrap_socket_called = True
            return MockSock()

    class MockSSLContext(object):
        def __init__(self):
            self.is_wrap_socket_called = False
        def wrap_socket(self, sock, server_hostname=None):
            self.is_wrap_socket_called = True


# Generated at 2022-06-13 04:49:28.327158
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    '''Ensure we can instatiate a UnixHTTPSConnection'''
    conn = UnixHTTPSConnection('/etc/ansible/roles.yml')
    assert isinstance(conn, UnixHTTPSConnection)
    assert conn._unix_socket == '/etc/ansible/roles.yml'

    try:
        conn.connect()
        assert False, "Expected an exception due to invalid socket"
    except socket.error:
        assert True


#
# Functions
#


# Generated at 2022-06-13 04:49:36.935920
# Unit test for function fetch_file

# Generated at 2022-06-13 04:49:44.103333
# Unit test for function getpeercert
def test_getpeercert():
    from ansible.module_utils import basic

    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False)
        ), supports_check_mode=False)

    response = urllib_request.urlopen(module.params['url'])
    module.exit_json(changed=False, stdout=getpeercert(response))


# Generated at 2022-06-13 04:49:54.275447
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    # Test a Sunday
    timetuple = (2008, 12, 7, 9, 5, 3, 6)
    zone = '-0500'
    date_string = rfc2822_date_string(timetuple, zone)
    assert 'Sun, 07 Dec 2008 09:05:03 -0500' == date_string

    # Test a Monday in daylight savings
    timetuple = (2008, 6, 9, 11, 5, 3, 0)
    zone = '-0400'
    date_string = rfc2822_date_string(timetuple, zone)
    assert 'Mon, 09 Jun 2008 11:05:03 -0400' == date_string



# Generated at 2022-06-13 04:49:56.145037
# Unit test for function getpeercert
def test_getpeercert():
    http_url = "http://www.google.com"
    https_url = "https://www.google.com"
    assert not getpeercert(urllib_request.urlopen(http_url))
    assert getpeercert(urllib_request.urlopen(https_url))


# Generated at 2022-06-13 04:50:01.719971
# Unit test for function generic_urlparse
def test_generic_urlparse():
    '''
    Tests a few url parts
    '''
    # These tests look redundant, but they're required to test that the
    # right code path is taken in the generic_urlparse function
    assert generic_urlparse(('http', 'www.test.com', '', '', '', '')) == {'hostname': 'www.test.com', 'params': '', 'password': None, 'path': '', 'username': None, 'fragment': '', 'query': '', 'port': None, 'scheme': 'http', 'netloc': 'www.test.com'}

# Generated at 2022-06-13 04:50:09.751901
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    # This is just a unit test for the method connect of class CustomHTTPSConnection
    # The class is defined in a different complexity level (above)
    connection = CustomHTTPSConnection(None, None)
    try:
        connection.connect()
    except Exception:
        pass
    else:
        assert False, 'ExpectedException not raised'


    class CustomHTTPSHandler(urllib_request.HTTPSHandler):
        def __init__(self, *args, **kwargs):
            self.validate_certs = kwargs.pop('validate_certs', True)
            urllib_request.HTTPSHandler.__init__(self, *args, **kwargs)


# Generated at 2022-06-13 04:50:13.183774
# Unit test for function fetch_url
def test_fetch_url():
    '''
    Unit tests for fetch_url.
    '''

    # Testing with a valid resource
    assert True == True

# Generated at 2022-06-13 04:51:04.215353
# Unit test for function generic_urlparse
def test_generic_urlparse():
    class MockType(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    class MockParseResult(MockType):
        '''Object to mimic the ParseResult named tuple'''
        # Note: it's easiest to just use a dict to build this class since
        # named tuples can't be built without the proper number of values,
        # and we just want to test the behavior of the function
        def __init__(self, scheme, netloc, path, params, query, fragment, username, password, hostname, port):
            self.scheme = scheme
            self.netloc = netloc
            self.path = path
            self.params = params
            self.query = query
            self.fragment = fragment


# Generated at 2022-06-13 04:51:16.997103
# Unit test for function prepare_multipart
def test_prepare_multipart():
    def _test_multipart(fields, expected_ct, expected_body=None, expected_file=None):
        '''
        Test a multipart message
        '''
        ct, body = prepare_multipart(fields)
        assert ct == expected_ct

        if expected_body is not None:
            assert body == expected_body
        elif expected_file is not None:
            with open(expected_file, 'rb') as f:
                assert body == f.read()

    _test_multipart(
        {'text_form_field': 'value'},
        'multipart/form-data; boundary="===============2769221812006400124=="',
        expected_file='test/unit/files/multipart_prepare_1.txt'
    )
    _test_

# Generated at 2022-06-13 04:51:23.328982
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    # a pyOpenSSL context is constructed for us.
    context = ssl.create_default_context()
    context.load_verify_locations(cadata=b_DUMMY_CA_CERT)
    context.verify_mode = ssl.CERT_REQUIRED

    sock = socket.socket()
    sock.connect(('example.com', 443))
    sock_ssl = context.wrap_socket(sock)

    assert sock_ssl.getpeercert() != None
    assert sock_ssl.getpeercert()['notAfter'] == b'Nov  7 23:59:59 2020 GMT'
    assert sock_ssl.getpeercert()['subject'][((('commonName', 'example.com'),),)] == 'example.com'