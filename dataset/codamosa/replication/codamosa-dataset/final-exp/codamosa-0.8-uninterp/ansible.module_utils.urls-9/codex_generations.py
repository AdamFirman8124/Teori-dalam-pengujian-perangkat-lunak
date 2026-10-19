

# Generated at 2022-06-13 04:45:07.928733
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    handler = SSLValidationHandler('www.sina.com.cn', 443)
    assert handler.detect_no_proxy('https://www.sina.com.cn') == False

    handler = SSLValidationHandler('www.sina.com.cn', 443)
    assert handler.detect_no_proxy('https://www.sina.com.cn/aaa') == False

    handler = SSLValidationHandler('www.sina.com.cn', 443)
    assert handler.detect_no_proxy('https://a.sina.com.cn') == False

    handler = SSLValidationHandler('www.sina.com.cn', 443)
    assert handler.detect_no_proxy('https://a.sina.com.cn/aaa') == False


# Generated at 2022-06-13 04:45:18.751670
# Unit test for method open of class Request
def test_Request_open():
    request = Request()
    #test open with a get method and valid url
    response = request.open('GET', 'https://httpbin.org/get')
    #test open with a get method and valid url and data
    response = request.open('GET', 'https://httpbin.org/based-get', data='This is a test')
    #test open with a get method and valid url, no data and headers
    headers = {'Accept': 'application/json'}
    response = request.open('GET', 'https://httpbin.org/get', headers=headers)
    #test open with a get method and valid url, with data and headers
    response = request.open('GET', 'https://httpbin.org/based-get', data='This is a test', headers=headers)
    #test open with a put method and valid url
   

# Generated at 2022-06-13 04:45:23.951066
# Unit test for function fetch_file
def test_fetch_file():
    # mock module for test
    module = Mock()
    module.tmpdir = '/tmp/'
    # mock module cleanup file
    module.add_cleanup_file = Mock()
    # mock temp file
    class MockFile:
        def __init__(self, temp_name):
            self.name = temp_name
            self.close()

        def close(self):
            with open(self.name, 'w') as temp_file:
                temp_file.write('test_fetch_file')

    # mock tempfile.NamedTemporaryFile
    module.tmpdir = '/tmp/'
    temp_file_name = '/tmp/test_file'
    mock_file = MockFile(temp_file_name)
    mock_tempfile = Mock()
    mock_tempfile.NamedTemporaryFile.return_

# Generated at 2022-06-13 04:45:35.346853
# Unit test for method open of class Request
def test_Request_open():
    import json
    r = Request('https://admintest.ansiblesupport.com')
    response = r.open(method='GET',url='https://admintest.ansiblesupport.com/api/accounts')
    assert response.read() == b'{"count": 0, "next": null, "previous": null, "results": []}'
    response = r.open(method='GET',url='https://admintest.ansiblesupport.com/api/accounts/')
    assert json.loads(response.read()) == {"count": 0, "next": None, "previous": None, "results": []}


# testing http://docs.python-requests.org/en/master/user/quickstart/
# use urllib3.disable_warnings(urllib3.exceptions.SNIM

# Generated at 2022-06-13 04:45:43.156073
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    from mock import patch
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.urls import open_url
    import os
    import json
    import socket
    import ssl

    # the method has to be patched in different ways depending on the
    # version of the ssl module
    if hasattr(ssl, 'HAS_SNI'):
        socket_patch = patch('ansible.module_utils.urls.CustomHTTPSConnection.socket', autospec=True)
        socket_ssl_wrap_socket = patch('ansible.module_utils.urls.ssl_wrap_socket', autospec=True)

# Generated at 2022-06-13 04:45:47.573720
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    p = os.path
    (fd, fname) = tempfile.mkstemp()
    dummy_url = 'https://dummy.example.com'
    os.close(fd)
    kwargs = {
        'key_file': fname,
        'cert_file': fname,
    }
    with UnixHTTPSConnection(unix_socket=fname)(dummy_url, **kwargs) as conn:
        assert conn.host == dummy_url
        assert conn.key_file == fname
        assert conn.cert_file == fname
    os.unlink(fname)

test_UnixHTTPSConnection___call__()



# Generated at 2022-06-13 04:45:54.114221
# Unit test for constructor of class Request
def test_Request():
    '''
    %prog
    unit tests for the urllib2 based http/https/ftp handler classes
    '''

    # modules used for testing

    import unittest
    import os.path
    import tempfile

    # base class for our test cases
    class RequestTestCase(unittest.TestCase):
        ''' base class for request test cases '''

        @classmethod
        def setUpClass(self):
            self.mydir = os.path.dirname(os.path.abspath(__file__))
            self.tmpdir = tempfile.mkdtemp()

        def setUp(self):
            self.response = DummyResponse([b'12345'])
            self.body = b'abcde'
            self.handler = HTTPHandler()


# Generated at 2022-06-13 04:45:58.415698
# Unit test for function prepare_multipart

# Generated at 2022-06-13 04:46:09.480783
# Unit test for function get_channel_binding_cert_hash

# Generated at 2022-06-13 04:46:19.079355
# Unit test for method patch of class Request
def test_Request_patch():
    url = 'http://ansible.com'
    data = 'id'

# Generated at 2022-06-13 04:47:37.746892
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    assert maybe_add_ssl_handler('https://www.ansible.com', True) is not None
    assert maybe_add_ssl_handler('https://www.ansible.com', False) is None
    assert maybe_add_ssl_handler('http://www.ansible.com', True) is None




# Generated at 2022-06-13 04:47:52.484655
# Unit test for function fetch_url
def test_fetch_url():
    import AnsibleModule as module

 
    # Test the case of no server, that is, no http/ftp server with
    # the given url, which should cause "Connection Error"
    # This test is not expected to pass
    r, info = fetch_url(module, "http://127.0.0.1:11212", method="GET", timeout=3)

    
    # Test the case of a http server, but using http GET method at first
    # and then using http POST method
    r, info = fetch_url(module, "http://httpbin.org/get", method="GET", timeout=3)

    r, info = fetch_url(module, "http://httpbin.org/post", method="POST", timeout=3)

    # Test the case of ftp server, which is not expected to pass

# Generated at 2022-06-13 04:48:02.807502
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    def test_redirect_handler_disabled(follow_redirects=None):
        redirect_handler = RedirectHandlerFactory(follow_redirects)()
        req = urllib_request.Request('http://www.example.com')
        fp = None
        code = 302
        msg = 'Found'
        hdrs = {'location': 'http://www.google.com'}
        newurl = 'http://www.google.com'

        try:
            redirect_handler.redirect_request(req, fp, code, msg, hdrs, newurl)
        except urllib_error.HTTPError as e:
            assert e.code == 302
        else:
            raise AssertionError("redirect_request() should raise HTTPError when redirects are disabled")  # noqa


# Generated at 2022-06-13 04:48:07.915588
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    import requests
    from requests.packages.urllib3.util.ssl_ import create_urllib3_context
    class TestSSLValidationHandler(SSLValidationHandler):
        def __init__(self, hostname, port, ca_path=None):
            self.hostname = hostname
            self.port = port
            self.ca_path = ca_path
            self.CERTIFICATES_DIR = os.path.join(os.path.dirname(__file__), "certs")
        def make_context(self, cafile=None, cadata=None):
            context = create_urllib3_context(ssl_version=PROTOCOL)
            context.load_verify_locations(cafile=cafile, cadata=cadata)
            return context

    scheme, hostname,

# Generated at 2022-06-13 04:48:10.902448
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    handler = SSLValidationHandler(None, None, None)
    if handler.get_ca_certs() is None:
        raise AssertionError()    

# Generated at 2022-06-13 04:48:16.891621
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''Tests if unix socket files can be handled'''
    import tempfile
    with tempfile.NamedTemporaryFile() as socket_file:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(socket_file.name)
        sock.listen(5)
        sock.close()
        # test if module works correctly with path to socket file
        unix_conn = UnixHTTPConnection(socket_file.name)
        unix_conn.connect()
        # test if module works correctly with bytestring
        unix_conn = UnixHTTPConnection(to_bytes(socket_file.name))
        unix_conn.connect()



# Generated at 2022-06-13 04:48:21.943226
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    request = RequestWithMethod('http://localhost/', 'PUT', 'some kind of data')
    assert request.get_method() == 'PUT'
    request._method = None
    request.data = None
    assert request.get_method() == 'GET'
    request._method = None
    request.data = 'some kind of data'
    assert request.get_method() == 'POST'
    request._method = 'POST'
    request.data = None
    assert request.get_method() == 'POST'



# Generated at 2022-06-13 04:48:30.884138
# Unit test for function getpeercert
def test_getpeercert():
    """ Ensure we get a peer cert when there is one and not an error when there is not. """
    handler = urllib_request.HTTPSHandler()
    opener = urllib_request.build_opener(handler)
    urllib_request.install_opener(opener)
    response = urllib_request.urlopen("https://www.google.com")
    peercert = getpeercert(response)
    assert peercert
    response = urllib_request.urlopen("http://www.google.com")
    peercert = getpeercert(response)
    assert peercert is None



# Generated at 2022-06-13 04:48:43.264036
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    sslValidationHandler = SSLValidationHandler(None, None)
    assert_raises_regexp(ProxyError, 'Connection to proxy failed', sslValidationHandler.validate_proxy_response, "HTTP/1.0 123 Invalid code for validation")
    assert_raises_regexp(ProxyError, 'Connection to proxy failed', sslValidationHandler.validate_proxy_response, "HTTP/1.0 200 Invalid code for validation")

    # Testing with a valid response
    assert_equal(sslValidationHandler.validate_proxy_response(b"HTTP/1.0 200 Connection established\r\n"), None)

    # Testing with different representations of '200'

# Generated at 2022-06-13 04:48:53.461171
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''
    Tests if the methods raises the right exceptions
    '''
    with pytest.raises(OSError):
        UnixHTTPConnection('/not/a/valid/socket').connect()
    UnixHTTPSConnection('/not/a/valid/socket').connect()


if CustomHTTPSConnection:
    # extend the handler class with a password manager
    class HTTPSPasswordMgr(HTTPPasswordMgr):
        def find_user_password(self, realm, uri):
            host = urllib_parse.splitport(uri[8:])[0]
            return HTTPPasswordMgr.find_user_password(self, realm, host)
else:
    class HTTPSPasswordMgr(object):
        pass



# Generated at 2022-06-13 04:49:52.797411
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    if not CustomHTTPSHandler:
        raise SkipTest("CustomHTTPSHandler() not available")
    https_handler = CustomHTTPSHandler()

#
# Support for SSL Connections
#


# Generated at 2022-06-13 04:50:01.155069
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    import test.urllib_testserver as urllib_testserver
    host = 'localhost'
    port = 8888
    import threading
    import time
    server = urllib_testserver.test_https_handler()
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    time.sleep(2)

# Generated at 2022-06-13 04:50:08.677443
# Unit test for function prepare_multipart
def test_prepare_multipart():
    passed = True
    tmp_output_file = 'tmp_output_file'
    tmp_input_file = 'tmp_input_file'
    with open(to_bytes(tmp_output_file, errors='surrogate_or_strict'), 'wb') as f:
        f.write(b'foobar')
    with open(to_bytes(tmp_input_file, errors='surrogate_or_strict'), 'w') as f:
        f.write('foobar')

# Generated at 2022-06-13 04:50:19.643787
# Unit test for method https_open of class CustomHTTPSHandler
def test_CustomHTTPSHandler_https_open():
    class HTTPSConnectionTest(CustomHTTPSConnection):
        "This class allows testing https_open without actually doing HTTP"
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.context = kwargs.get('context')
            self.sock = None

    class HTTPSHandlerTest(CustomHTTPSHandler):
        def __init__(self, *args, **kwargs):
            self._context = kwargs.get('context')
            urllib_request.AbstractHTTPHandler.__init__(self)

    # Test
    handler = HTTPSHandlerTest(context = ssl._create_default_https_context())
    connection = handler.https_open(None)
    assert isinstance(connection, HTTPSConnectionTest)
    assert connection.context == handler._

# Generated at 2022-06-13 04:50:22.676133
# Unit test for method open of class Request
def test_Request_open():
    req = Request()
    res = req.open('GET', 'http://certbot.eff.org')
    assert(res.code == 200)


# Generated at 2022-06-13 04:50:30.293467
# Unit test for function fetch_file
def test_fetch_file():
    URL = 'https://github.com/ansible/ansible/archive/v2.0.0.1.tar.gz'
    file_name, file_ext = os.path.splitext(str(URL.rsplit('/', 1)[1]))
    fetch_temp_file = tempfile.NamedTemporaryFile(dir=module.tmpdir, prefix=file_name, suffix=file_ext, delete=False)
    module.add_cleanup_file(fetch_temp_file.name)

# Generated at 2022-06-13 04:50:39.018103
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    if not HAS_CRYPTOGRAPHY:
        pytest.skip(msg="Skipping cryptography tests because the cryptography library is missing.")


# Generated at 2022-06-13 04:50:44.587209
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    #
    # The following test is to be sure that a CustomHTTPSHandler object is
    # properly constructed. It will cause an exception if a class attribute is
    # missing.
    # This test MUST be executed before creating a CustomHTTPSHandler object.
    #
    # Note: the purpose of this test is to detect a missing attribute at
    # construction time rather than at request time.
    #
    urllib_request.Request(
        url='https://127.0.0.1',
        data=None,
        headers={
            'Content-Type': 'text/plain',
            'Accept': 'text/plain',
        },
    )


# Generated at 2022-06-13 04:50:53.778040
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    factory = RedirectHandlerFactory("no")
    handler = factory()
    try:
        handler.redirect_request(None, None, 301, "Some message", {}, "http://foo.bar/")
        assert False, "Expected to throw an exception"
    except urllib_error.HTTPError:
        pass
    factory = RedirectHandlerFactory("all")
    handler = factory()
    try:
        handler.redirect_request(None, None, 200, "Some message", {}, "http://foo.bar/")
        assert False, "Expected to throw an exception"
    except urllib_error.HTTPError:
        pass
    factory = RedirectHandlerFactory("safe")
    dummy_req = Mock()
    # Don't follow redirect when not a GET or HEAD
    dummy_req.get_method.return_

# Generated at 2022-06-13 04:50:54.641907
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request(): pass

