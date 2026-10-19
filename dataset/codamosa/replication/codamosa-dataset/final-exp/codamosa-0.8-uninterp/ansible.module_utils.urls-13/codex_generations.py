

# Generated at 2022-06-13 04:46:20.990055
# Unit test for function getpeercert
def test_getpeercert():
    '''
    Simple test to make sure we are getting atleast something back
    '''
    response = Mock(name="response")
    ssl_sock = Mock()
    ssl_sock.getpeercert.return_value = {"test": "test"}
    pysock = Mock(fp=Mock(raw=Mock(_sock=ssl_sock)))
    response.fp = pysock
    result = getpeercert(response)
    assert "test" in result
    pysock = Mock()
    pysock.fp = Mock(_sock=Mock(fp=Mock(_sock=ssl_sock)))
    response.fp = pysock
    result = getpeercert(response)
    assert "test" in result


# Include distro specific variables.
# If a desired variable

# Generated at 2022-06-13 04:46:28.025948
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class MockSocket(object):
        def __init__(self, host, port):
            self.host = host
            self.port = port
            self.connected = False

        def create_connection(self, address, timeout=None, source_address=None):
            return True

        def wrap_socket(self, sock, keyfile=None, certfile=None, cert_reqs=None, ca_certs=None, server_side=None, ssl_version=2, ca_cert_dir=None):
            return True

    class MockContext():
        def load_cert_chain(self, cert_file, key_file):
            return True

        def load_verify_locations(self, cafile=None, capath=None, cadata=None):
            return True


# Generated at 2022-06-13 04:46:39.718908
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    from ansible.errors import ProxyError
    ssl_handler = SSLValidationHandler('hostname', 'port')

    VALID_PROXY_CODE = 200
    INVALID_PROXY_CODES = [500, 401, 403, 400]
    VALID_RESPONSE = b"HTTP/1.0 200 Connection established\r\n\r\n"
    for code in INVALID_PROXY_CODES:
        response = b"HTTP/1.0 " + str(code).encode('utf-8') + b" Connection failed\r\n\r\n"
        try:
            ssl_handler.validate_proxy_response(response)
        except ProxyError:
            pass

# Generated at 2022-06-13 04:46:45.213925
# Unit test for function atexit_remove_file
def test_atexit_remove_file():
    with open("test.txt","w") as fd:
        fd.write("test")
    assert os.path.exists("test.txt")
    atexit_remove_file("test.txt")
    assert not os.path.exists("test.txt")


# Generated at 2022-06-13 04:46:54.128100
# Unit test for function generic_urlparse

# Generated at 2022-06-13 04:47:06.746721
# Unit test for function fetch_url
def test_fetch_url():

    import sys
    import json
    import errno
    import ssl

    import unittest
    import traceback
    from io import StringIO

    import ansible.module_utils.urls

    class FakeModule(object):

        # FakeModule replaces AnsibleModule but does not provide most of the
        # older functions because these have been migrated to the new url
        # modules into which code is being migrated.  It also does not simulate
        # all kwargs.  This class is only intended to be used as a temporary
        # replacement until the url modules are moved out of the url_*
        # modules and into their respective modules.
        def __init__(self, **kwargs):
            self.params = kwargs
            self.tmpdir = '/tmp'


# Generated at 2022-06-13 04:47:08.826975
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    SSLValidationHandler("api.github.com", 443).http_request("")


# Generated at 2022-06-13 04:47:20.248082
# Unit test for function generic_urlparse
def test_generic_urlparse():
    assert generic_urlparse(urlparse.urlparse('http://foo:bar@example.com:8080/baz')) == \
        {'scheme': 'http',
         'netloc': 'foo:bar@example.com:8080',
         'path': '/baz',
         'params': '',
         'query': '',
         'fragment': '',
         'username': 'foo',
         'password': 'bar',
         'hostname': 'example.com',
         'port': 8080
         }


# Generated at 2022-06-13 04:47:32.799908
# Unit test for function prepare_multipart
def test_prepare_multipart():
    # test all field values as strings
    fields = {
        'text1': 'abc',
        'text2': 'xyz',
        'file1': '/bin/true',
        'file2': '/bin/false',
    }
    content_type, body = prepare_multipart(fields)
    content_type.split(';')[0].strip() == 'multipart/form-data'
    body.startswith(b'--')
    d = {}
    for part in body.split(b'--')[1:-1]:
        headers, sep, content = part.partition(b'\r\n\r\n')
        headers = dict(l.partition(b':')[::2] for l in headers.split(b'\r\n'))

# Generated at 2022-06-13 04:47:38.530784
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    c = SSLValidationHandler('www.google.com', 443)
    req = urllib_request.Request('https://www.google.com')
    req.headers['User-Agent'] = 'Python-urllib/2.7'
    req.add_data(b'page=20&require_type=3')
    req.add_header('Content-Type', 'text/html; charset=gbk')
    # rsp = c.http_request(req)
    print()



# Generated at 2022-06-13 04:49:17.692913
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    '''
    Unit test for method http_request of class SSLValidationHandler
    '''
    # Create a temporary request object
    req = urllib_request.Request(url="https://www.google.com", method="GET")
    
    # Create a temporary SSLValidationHandler object
    tmp_object = SSLValidationHandler(hostname='www.google.com', port=443)

    # Call the method
    result = tmp_object.http_request(req)

    # Check the result
    assert result is not None



# Generated at 2022-06-13 04:49:32.053892
# Unit test for function get_channel_binding_cert_hash

# Generated at 2022-06-13 04:49:36.283373
# Unit test for function fetch_url
def test_fetch_url():

    url = 'http://www.example.com/'
    module = AnsibleModule(argument_spec={})

    try:
        r, info = fetch_url(module, url)
        assert info['url'] == url
        assert info['status'] >= 200 and info['status'] < 400
        assert r is not None
    except Exception:
        raise ValueError('Fetch URL failed')



# Generated at 2022-06-13 04:49:41.258137
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    req = RequestWithMethod('', 'GET')
    assert req.get_method() == 'GET'
    req = RequestWithMethod('', 'POST')
    assert req.get_method() == 'POST'
    req = RequestWithMethod('', 'PUT')
    assert req.get_method() == 'PUT'

    req = RequestWithMethod('', None)
    assert req.get_method() == 'GET'
    req.method = 'POST'
    assert req.get_method() == 'POST'
    req.method = 'PUT'
    assert req.get_method() == 'PUT'


# request functions


# Generated at 2022-06-13 04:49:45.956512
# Unit test for function atexit_remove_file
def test_atexit_remove_file():
    import tempfile
    tmpfh, tmpfile = tempfile.mkstemp(prefix='ansible-test')
    os.close(tmpfh)
    # check if file exists
    assert os.path.exists(tmpfile)
    # run function atexit_remove_file
    atexit_remove_file(tmpfile)
    # check if file not exists
    assert not os.path.exists(tmpfile)



# Generated at 2022-06-13 04:49:50.905635
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    def _test_connect(exception, unix_socket, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        ''' Unit test for method connect of class UnixHTTPConnection
        '''
        try:
            with UnixHTTPConnection(unix_socket)('localhost') as conn:
                if timeout != socket._GLOBAL_DEFAULT_TIMEOUT:
                    conn.timeout = timeout
                conn.connect()
                assert isinstance(conn.sock, socket._socketobject)
        except OSError as e:
            if e.strerror == exception:
                raise Exception('Invalid Socket File: %s' % (e))

    _test_connect('[Errno 2] No such file or directory', '/tmp/UnixHTTPConnection.sock.test.invalid')

    # Only run the following test on linux

# Generated at 2022-06-13 04:50:00.209814
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    """ test rfc2822_date_string() """
    assert rfc2822_date_string(time.gmtime()) == 'Mon, 01 Jan 0001 00:00:00 -0000'
    assert rfc2822_date_string(time.gmtime(0), zone='+0000') == 'Thu, 01 Jan 1970 00:00:00 +0000'
    assert rfc2822_date_string(time.gmtime(0), zone='+1200') == 'Thu, 01 Jan 1970 00:00:00 +1200'
    assert rfc2822_date_string(time.gmtime(0), zone='-0100') == 'Thu, 01 Jan 1970 00:00:00 -0100'

# Generated at 2022-06-13 04:50:09.396927
# Unit test for function fetch_file
def test_fetch_file():
    '''Unit test for function fetch_file.
    The target URL is a file in a gist.
    '''

    import tempfile
    module = AnsibleModule(argument_spec={})
    url = 'https://gist.githubusercontent.com/RadicalZephyr/59ebc77d7640b8c8f935a54e763c3e1f/raw/8d54e4b1f2135a20a4c66b4bd9e3e75f9ec28b02/test_fetch_file.txt'
    file_path = fetch_file(module, url)
    with open(file_path) as fd:
        file_content = fd.read()
    assert(file_content == 'ansible test file')


# Generated at 2022-06-13 04:50:21.463148
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    # Test when self.ca_path has value
    def get_ca_certs():
        url_handler = SSLValidationHandler('hostname', 'port', 'ca_path')
        return url_handler.get_ca_certs()
    # Mock os.path.exists to return True
    with patch.object(os.path, 'exists', return_value=True):
        # Mock os.path.isfile to return True
        with patch.object(os.path, 'isfile', return_value=True):
            # Mock open to return mock_open
            with patch('builtins.open', mock_open(read_data='data'), create=True):
                ca_path, cadata, paths_checked = get_ca_certs()
    # Verify if argument 'read' of mock_open had been called
    mock_

# Generated at 2022-06-13 04:50:28.640064
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class TestCustomHTTPSConnection(CustomHTTPSConnection):
        def __init__(self, *args):
            self.host = "https://www.ansible.com"
            self.port = 443
            self.timeout = None
            self.source_address = None
            self.sock = None
            self.cert_file = None
            self.key_file = None
            self.context = None
        # Overrides the _context method of HTTPSConnection
        def _context(self):
            return self.context
        # Overrides the connect method of HTTPSConnection
        def connect(self):
            self.sock = socket.create_connection((self.host, self.port), self.timeout, self.source_address)
            server_hostname = self.host