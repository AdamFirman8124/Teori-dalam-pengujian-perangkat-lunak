

# Generated at 2022-06-13 04:45:39.841580
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class mock_server(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((HOST, 0))
            self.sock.listen(1)
            self.daemon = True

        def run(self):
            (clientsocket, address) = self.sock.accept()
            data = b''
            while True:
                chunk = clientsocket.recv(1024)
                data += chunk
                if len(chunk) == 0:
                    break

# Generated at 2022-06-13 04:45:45.450887
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    RedirectHandler = RedirectHandlerFactory(follow_redirects='urllib2')
    handler = RedirectHandler()
    assert handler.redirect_request

    RedirectHandler = RedirectHandlerFactory(follow_redirects=False)
    handler = RedirectHandler()
    assert handler.redirect_request

    RedirectHandler = RedirectHandlerFactory(follow_redirects=True)
    handler = RedirectHandler()
    assert handler.redirect_request

    RedirectHandler = RedirectHandlerFactory(follow_redirects='safe')
    handler = RedirectHandler()
    assert handler.redirect_request

    RedirectHandler = RedirectHandlerFactory(follow_redirects='all')
    handler = RedirectHandler()
    assert handler.redirect_request


# Generated at 2022-06-13 04:45:47.895926
# Unit test for method __call__ of class UnixHTTPConnection
def test_UnixHTTPConnection___call__():
    conn = UnixHTTPConnection("test")
    conn("host", port=1, strict=2, timeout=3)
    assert conn.host == "host"
    assert conn.port == 1
    assert conn.strict == 2
    assert conn.timeout == 3

# Generated at 2022-06-13 04:45:57.878284
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''
    Unit test for method UnixHTTPConnection.connect
    '''
    with mock.patch('ansible.module_utils.six.moves.socket.socket') as mock_socket:
        mock_sock = mock.Mock()
        mock_sock.connect = mock.Mock(side_effect=OSError)
        mock_socket.return_value = mock_sock
        unix_http_connection = UnixHTTPConnection('/tmp/test')
        try:
            unix_http_connection.connect()
        except OSError as e:
            assert 'Invalid Socket File (/tmp/test): ' in e.args[0]
        else:
            assert False, 'OSError not raised by UnixHTTPConnection.connect'



# Generated at 2022-06-13 04:46:02.329882
# Unit test for function unix_socket_patch_httpconnection_connect
def test_unix_socket_patch_httpconnection_connect():
    with unix_socket_patch_httpconnection_connect():
        assert httplib.HTTPConnection.connect == UnixHTTPConnection.connect
    assert httplib.HTTPConnection.connect != UnixHTTPConnection.connect

    class NotUnixHTTPSConnection(httplib.HTTPSConnection):
        def __init__(self, host, unix_socket=None, **kwargs):
            host, port = host
            httplib.HTTPSConnection.__init__(self, host, port=port, **kwargs)
            self._unix_socket = unix_socket

        def connect(self):
            '''Hack around httplib's connect() method to not set a host/port for unix sockets'''

# Generated at 2022-06-13 04:46:13.448891
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import re
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import urllib as urllib_6
    from ansible.module_utils.six.moves.urllib.parse import urlsplit
    from ansible.module_utils.urls import fetch_url, open_url
    # For some reason the pip version of httplib2 fails with python3
    import httplib2


# Generated at 2022-06-13 04:46:24.274632
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    import ansible.module_utils.pycompat24 as pycompat24

    class MockSocket(object):
        def create_connection(self, args, kwargs):
            return True

        def wrap_socket(self, *args, **kwargs):
            return True

    class MockSSL(object):
        CERT_NONE = 'CERT_NONE'
        def wrap_socket(self, *args, **kwargs):
            return True


    class MockSSLContext(object):
        def __init__(self, *args, **kwargs):
            return 0

        def load_cert_chain(self, *args, **kwargs):
            return True

        def wrap_socket(self, *args, **kwargs):
            return True

    class MockSSLLib(object):
        PROTOCOL_TLSv

# Generated at 2022-06-13 04:46:34.003328
# Unit test for function fetch_file
def test_fetch_file():
    tmp = tempfile.NamedTemporaryFile()
    tmp.close()
    os.mkdir(tmp.name)
    tmpdir=tmp.name
    #create and delete

# Generated at 2022-06-13 04:46:37.553391
# Unit test for function fetch_url
def test_fetch_url():
  host = '127.0.0.1'
  port = 31415
  # Start a server to handle the request
  s = socketserver.TCPServer((host, port), socketserver.BaseRequestHandler)
  s.timeout = 1.0
  t = threading.Thread(target=s.handle_request)
  t.setDaemon(True)
  t.start()

  # The client
  result = fetch_url(module, "http://" + host + ":" + str(port))

  assert result[1].get('status') == -1
  assert type(result[0]) == type(None)
  
test_fetch_url()
 

# Generated at 2022-06-13 04:46:41.681815
# Unit test for function fetch_url
def test_fetch_url():
    # Test case 1
    module = FakeModule({'url': 'http://www.basic.com'})
    url = module.params['url']
    info = dict()


# Generated at 2022-06-13 04:47:38.774173
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    handler = CustomHTTPSHandler()

if hasattr(urllib_request, 'HTTPSHandler'):
    class UnixHTTPSConnection(httplib.HTTPSConnection):
        """
        This class allows coordination of SSL connections with the underlying Ansible transport
        """
        def __init__(self, path, host='', port=None, key_file=None, cert_file=None, strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
                     source_address=None):
            httplib.HTTPSConnection.__init__(self, host, port, key_file, cert_file, strict, timeout, source_address)

            # httplib in python 2.6 doesn't have a source_address.
            # NOTE: we should not assign a value to self.source_address
            # or set it as a

# Generated at 2022-06-13 04:47:52.921849
# Unit test for function getpeercert
def test_getpeercert():
    # Get the peer certificate for google
    try:
        handler = maybe_add_ssl_handler('https://google.com')
    except NoSSLError:
        # Missing ssl modules
        return unittest.SkipTest('SSL module missing')

    opener = urllib_request.build_opener(handler)
    urllib_request.install_opener(opener)

    resp = urllib_request.urlopen('https://google.com')
    # Get the binary form of the certificate
    cert = getpeercert(resp, binary_form=True)
    # the binary certificate should not be empty
    assert cert
    # The binary certificate should be a byte array
    assert isinstance(cert, bytes)

    # Get the non-binary (text) form of the certificate

# Generated at 2022-06-13 04:47:55.397547
# Unit test for function fetch_file
def test_fetch_file():
    raise NotImplementedError('For now only tested in modules/source_control/git.py')


#
# Main function
#



# Generated at 2022-06-13 04:47:57.124132
# Unit test for method open of class Request
def test_Request_open():
    request = Request(module=None, headers=None)
    method = 'GET'


# Generated at 2022-06-13 04:48:07.173576
# Unit test for function prepare_multipart
def test_prepare_multipart():
    # I'm not sure how to test this without more hassle than it's worth.
    # We'll just check that the function runs properly with a given set of data.
    fields = {
        'file1': {
            'filename': '/bin/true',
            'mime_type': 'application/octet-stream'
        },
        'file2': {
            'content': b'text based file content',
            'filename': 'fake.txt',
            'mime_type': 'text/plain',
        },
        'text_form_field': 'value'
    }

    content_type, body = prepare_multipart(fields)

    content_type_str = to_native(content_type).split('; boundary=')
    boundary = content_type_str[1].strip()

    # Check the header
    header

# Generated at 2022-06-13 04:48:14.618270
# Unit test for function generic_urlparse
def test_generic_urlparse():
    '''
    Verify that parsing yields the same results as the
    system implementation of urlparse
    '''
    parts_tuple = urllib_parse.urlparse('http://foo:bar@www.ansible.com:8080/baz/qux?quux=quuz#corge')
    parts_generic = generic_urlparse('http://foo:bar@www.ansible.com:8080/baz/qux?quux=quuz#corge')
    if parts_tuple == parts_generic.as_list():
        print('Pass: Parsed parts are the same')
    else:
        print('Fail: Parsed parts are different')

if __name__ == '__main__':
    test_generic_urlparse()

#
# Connections
#


# Generated at 2022-06-13 04:48:22.305768
# Unit test for method open of class Request
def test_Request_open():

    # Test when instance is passed
    req = urllib_request.Request('http://www.google.com')
    assert isinstance(req, urllib_request.Request)

    # Test when URL is passed
    resp = urllib_request.urlopen('http://www.google.com')
    assert isinstance(resp, urllib_request.HTTPResponse)

# Test for class urllib

# Generated at 2022-06-13 04:48:33.525185
# Unit test for function fetch_url
def test_fetch_url():
    import hashlib
    import os
    import shutil
    import tempfile
    import types
    import unittest

    import ansible_collections.ansible.builtin.plugins.module_utils.urls as urls

    class MockResource(MockResponse):
        def read(self, *args, **kwargs):
            if hasattr(self, 'read_count'):
                self.read_count += 1
            else:
                self.read_count = 1

            if self.read_count > 1:
                raise IOError('No more data to read')

            return super(MockResource, self).read(*args, **kwargs)

        def readlines(self):
            return self.read().splitlines(True)

        def close(self):
            self.closed = True


# Generated at 2022-06-13 04:48:45.403593
# Unit test for function generic_urlparse
def test_generic_urlparse():
    # pylint: disable=unused-variable,too-many-branches,too-many-statements
    if sys.version_info >= (3, 0):
        # Python 3.x has a namedtuple
        import collections
        parts = collections.namedtuple('parts', 'scheme netloc path params query fragment')
    else:
        class parts(object):  # pylint: disable=invalid-name
            def __init__(self, scheme, netloc, path, params, query, fragment):
                self.scheme = scheme
                self.netloc = netloc
                self.path = path
                self.params = params
                self.query = query
                self.fragment = fragment
    # test basic parsing

# Generated at 2022-06-13 04:48:54.365537
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    class FakeSocket(object):
        '''Fake a ssl wrapped socket'''
        def makefile(self, *args, **kwargs):
            return FakeSocket()

        def __init__(self, *args, **kwargs):
            pass

        def getpeercert(self, *args, **kwargs):
            return dict()

        def recv_into(self, *args, **kwargs):
            return FakeSocket()

        def read(self, *args, **kwargs):
            return b''

        def readline(self, *args, **kwargs):
            return b''

        def close(self, *args, **kwargs):
            pass

    class FakeSSL(object):
        '''Fake a ssl object'''
        def __init__(self, *args, **kwargs):
            pass



# Generated at 2022-06-13 04:50:09.817853
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():

    assert SSLValidationHandler('example.com',80).detect_no_proxy('http://example.com') == False
    assert SSLValidationHandler('example.com',80).detect_no_proxy('http://www.example.com') == False
    assert SSLValidationHandler('example.com',80).detect_no_proxy('http://example.com:81') == False

    assert SSLValidationHandler('example.com',80).detect_no_proxy('http://example.com') == False

    os.environ['no_proxy'] = 'not-example.com'
    assert SSLValidationHandler('example.com',80).detect_no_proxy('http://example.com') == True
    os.environ['no_proxy'] = 'not-example.com,www.example.com'
    assert SSLValidationHandler

# Generated at 2022-06-13 04:50:14.625130
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    ssl_handler = maybe_add_ssl_handler('https://localhost', True, ca_path=None)
    assert ssl_handler is not None, 'ssl_handler should not be None'


# Generated at 2022-06-13 04:50:20.046302
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    c = CustomHTTPSConnection('www.')
    c.host = 'www.example.com'
    c.port = 443
    c.cert_file = 'foo'
    c.key_file = 'bar'
    c._tunnel_host = 'www.example.com'
    c._tunnel = lambda: None

    def create_connection(args, kwargs):
        # TODO: make this a mock.
        return args, kwargs

    def wrap_socket(sock, keyfile=None, cert_reqs=None, certfile=None, ssl_version=None, server_hostname=None):
        return (sock, keyfile, cert_reqs, certfile, ssl_version, server_hostname)


# Generated at 2022-06-13 04:50:28.460222
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    # Test without specifying expected return codes
    test_obj = SSLValidationHandler('localhost', '443')
    response = b'HTTP/1.0 200 OK\r\n'
    e = None
    try:
        test_obj.validate_proxy_response(response)
    except Exception as e:
        pass
    assert e is None, 'FAIL: No exceptions expected'

    response = b'HTTP/1.0 200 OK\r\n'
    e = None
    try:
        test_obj.validate_proxy_response(response, [200, 201])
    except Exception as e:
        pass
    assert e is None, 'FAIL: No exceptions expected'

    # Test with unexpected return codes
    response = b'HTTP/1.0 200 OK\r\n'
    e = None

# Generated at 2022-06-13 04:50:33.295459
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    return CustomHTTPSHandler()

if HAS_KERBEROS:
    class HTTPSClientAuthHandler(urllib_request.HTTPSHandler):
        def __init__(self, connection, debuglevel=0, key_file=None, cert_file=None):
            self.key_file = key_file
            self.cert_file = cert_file
            urllib_request.HTTPSHandler.__init__(self, debuglevel)
            self.connection = connection


# Generated at 2022-06-13 04:50:33.987610
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    return True


# Generated at 2022-06-13 04:50:41.142628
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    # Success test
    handler = SSLValidationHandler('test', 1234)
    handler.validate_proxy_response(b'HTTP/1.0 200 OK\r\n\r\n')
    handler.validate_proxy_response(b'HTTP/1.0 200 OK\r\n\r\n', [200, 300])
    handler.validate_proxy_response(b'HTTP/1.0 202 Accepted\r\n\r\n', [200, 300])
    handler.validate_proxy_response(b'HTTP/1.0 301 Moved Permanently\r\n\r\n', [200, 301])

    # Fail test

# Generated at 2022-06-13 04:50:49.664304
# Unit test for method open of class Request
def test_Request_open():
    request = Request()
    request.open(url=None,
                 data=None,
                 timeout=None,
                 validate_certs=None,
                 url_username=None,
                 url_password=None,
                 http_agent=None,
                 force_basic_auth=None,
                 follow_redirects=None,
                 client_cert=None,
                 client_key=None,
                 cookies=None,
                 use_gssapi=False,
                 unix_socket=None,
                 ca_path=None,
                 unredirected_headers=None,
                 headers=None)


# Generated at 2022-06-13 04:50:58.022206
# Unit test for function fetch_url
def test_fetch_url():
    import os
    import tempfile
    # We need to be able to patch uriopen so we can use this
    # function in unit tests
    def uriopen(module, url, data=None, headers=None, method=None,
                use_proxy=True, force=False, last_mod_time=None, timeout=10,
                validate_certs=True, url_username=None,
                url_password=None, http_agent=None,
                force_basic_auth=False, follow_redirects='urllib2',
                client_cert=None,
                client_key=None, cookies=None, use_gssapi=False,
                unix_socket=None, ca_path=None, unredirected_headers=None):
        return url, data, headers, method, use_proxy, force,

# Generated at 2022-06-13 04:51:08.905662
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    import unittest2 as unittest
    import tempfile
    (cert_file, cert_file_name) = tempfile.mkstemp()
    (key_file, key_file_name) = tempfile.mkstemp()
    server = CustomHTTPSConnection("127.0.0.1", 443)
    server.connect()
    server = CustomHTTPSConnection("127.0.0.1", 443, cert_file=cert_file_name, key_file=key_file_name)
    server.connect()
    server = CustomHTTPSConnection("127.0.0.1", 443, cert_file=cert_file_name)
    server.connect()
    server = CustomHTTPSConnection("127.0.0.1", 443, key_file=key_file_name)
    server.connect()
   