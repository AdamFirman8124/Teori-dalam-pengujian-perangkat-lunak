

# Generated at 2022-06-13 04:47:21.100872
# Unit test for function prepare_multipart
def test_prepare_multipart():
    """
    test_prepare_multipart - Basic unit test to verify prepare_multipart function

    :returns: None
    """
    file_data = 'This is a test\n'
    plain_data = 'plain text'
    file_name = to_bytes(sys.argv[0])
    file_handle = open(file_name, 'wb')
    file_handle.write(to_bytes(file_data, errors='surrogate_or_strict'))
    file_handle.close()

# Generated at 2022-06-13 04:47:32.926005
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    test_data = {
        b'HTTP/1.0 200 Connection established\r\n': [200],
        b'HTTP/1.0 200 OK\r\n': [200, 201],
        b'HTTP/1.0 404 Not Found\r\n': None,
        b'HTTP/1.0 301 Moved Permanently\r\n': None,
        b'HTTP/1.0 302 Moved Temporarily\r\n': None,
        b'HTTP/1.0 200 OK\r\n\r\n': [200],
        b'HTTP/1.0 200 OK\n': [200],
        b'HTTP/1.0 200 OK\n\n': [200]
    }

    for test_response in test_data:
        valid_codes = test_data[test_response]
       

# Generated at 2022-06-13 04:47:37.124319
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    # Check that the method returns three values
    ca_path, cadata, paths_checked = SSLValidationHandler("", "").get_ca_certs()
    assert len(ca_path) > 0
    assert len(cadata) > 0
    assert len(paths_checked) > 0


# Generated at 2022-06-13 04:47:49.062361
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    return """
    from __main__ import SSLValidationHandler
    hostname = 'd.x'
    port = 80
    req = None
    h = SSLValidationHandler(hostname, port)

    # The following raises an AttributeError, because the return value of
    # h.get_ca_certs is not a string.
    h.http_request(req)

    # The following raises an AttributeError, because the return value of
    # h.get_ca_certs is not a string.
    h.https_request(req)
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 04:47:51.016814
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    pass


# Generated at 2022-06-13 04:48:00.280811
# Unit test for method make_context of class SSLValidationHandler
def test_SSLValidationHandler_make_context():
    '''
    A unit test for the make_context method of SSLValidationHandler.

    This method tests the make_context method of the SSLValidationHandler class
    to make sure the SSL context is created properly
    '''
    class Test_SSLValidationHandler(SSLValidationHandler):
        '''
        A test class used to test the make_context method of SSLValidationHandler.
        '''
        def __init__(self, hostname, port, ca_path=None):
            super(Test_SSLValidationHandler, self).__init__(hostname, port, ca_path)

        def make_context(self, cafile, cadata):
            return super(Test_SSLValidationHandler, self).make_context(cafile, cadata)


# Generated at 2022-06-13 04:48:12.972200
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    handler = RedirectHandlerFactory(False)()
    req = urllib_request.Request('http://127.0.0.1')
    fp = io.StringIO()
    try:
        handler.redirect_request(req, fp, 301, 'Moved Permanently', {}, 'http://127.0.0.1')
        assert False
    except urllib_error.HTTPError:
        assert True
    try:
        handler.redirect_request(req, fp, 302, 'Found', {}, 'http://127.0.0.1')
        assert False
    except urllib_error.HTTPError:
        assert True

# Generated at 2022-06-13 04:48:15.222407
# Unit test for function getpeercert
def test_getpeercert():
    pass




# Generated at 2022-06-13 04:48:18.827330
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    pass

    # variable = SSLValidationHandler( hostname, port, ca_path )
    # method = variable.http_request( req )


# Generated at 2022-06-13 04:48:20.110923
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():

    assert callable(RedirectHandlerFactory(follow_redirects=True))

# Generated at 2022-06-13 04:49:04.330281
# Unit test for function unix_socket_patch_httpconnection_connect
def test_unix_socket_patch_httpconnection_connect():
    import tempfile
    import os
    import shutil
    test_dir = tempfile.mkdtemp()
    test_socket = os.path.join(test_dir, 'unix_socket_test')
    with unix_socket_patch_httpconnection_connect():
        unix_conn = UnixHTTPSConnection(test_socket)
        unix_conn.connect()
    assert hasattr(unix_conn, 'sock')
    shutil.rmtree(test_dir)

    with pytest.raises(OSError):
        unix_conn.connect()

    unix_conn = UnixHTTPSConnection(test_socket)
    unix_conn._tunnel_host = 'unix_socket'
    unix_conn._tunnel()
    assert hasattr(unix_conn, 'sock')



# Generated at 2022-06-13 04:49:13.022407
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    sock = socket.create_connection(('www.ansible.com', 443), 30)
    host = 'www.ansible.com'
    port = 443
    cert_file = '/etc/pki/tls/certs/ca-bundle.crt'
    key_file = None
    chc = CustomHTTPSConnection(host, port, key_file=key_file, cert_file=cert_file, timeout=30, source_address=None)
    chc.host = 'www.ansible.com'
    chc.port = 443
    chc.key_file = None
    chc.cert_file = '/etc/pki/tls/certs/ca-bundle.crt'
    chc._tunnel_host = None
    chc.source_address = None
    assert chc

# Generated at 2022-06-13 04:49:13.494741
# Unit test for function fetch_file
def test_fetch_file():
   pass


# Generated at 2022-06-13 04:49:18.173639
# Unit test for function fetch_url
def test_fetch_url():
    arguments = dict(
        url='https://github.com/cjschroder/ansible-testing/blob/master/README.md',
        use_proxy=True,
        client_cert='/opt/ssl/certs/test.pem',
        client_key='/opt/ssl/certs/test.key',
        validate_certs=True,
        timeout=10,
        follow_redirects='urllib2',
        force_basic_auth=False,
        unix_socket='/opt/apache/run/httpd.sock',
    )
    # test the no arg return in the fetch_url
    response, info = fetch_url(None, **arguments)
    assert info.get('status') == 200 or info.get('status') == -1



# Generated at 2022-06-13 04:49:32.111088
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    # If we can't verify the cert, we should get an ssl error
    web_url = 'https://raw.githubusercontent.com/ansible/ansible-modules-core/devel/command/library/command.py'
    with pytest.raises(SSLValidationError):
        maybe_add_ssl_handler(web_url, True)

    # If we can verify the cert, we should not get an ssl error
    web_url = 'https://raw.githubusercontent.com/ansible/ansible-modules-core/devel/command/library/command.py'
    handler = maybe_add_ssl_handler(web_url, True, ca_path='test/ansible_test/unit/utils/requests_ca_bundle')
    with pytest.raises(SSLValidationError):
        handler.http

# Generated at 2022-06-13 04:49:39.215247
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    # Test all values of follow_redirects=
    for follow_redirects in ['urllib2', 'yes', 'all', 'no', 'none', 'safe', False, True]:
        # Test various redirects, status codes should be in range 300-399
        for status_code in [301, 302, 303, 307, 308]:
            # create request and response objects
            req = RequestWithMethod('', method='GET')
            fp = MockResponse(status=status_code, reason='Mock status', body='Mock body')
            hdrs = dict(Location='http://127.0.0.1:8080/mock_location')
            # create new URL
            new_url = 'http://127.0.0.1:8080/mock-new-url'

            # Create redirect handler

# Generated at 2022-06-13 04:49:48.228540
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    class FakeSSL(object):
        pass
    old_ssl = __builtin__.ssl
    __builtin__.ssl = FakeSSL()
    old_HAVE_SSL = HAVE_SSL
    global HAVE_SSL
    HAVE_SSL = True
    old_PROTOCOL = PROTOCOL
    global PROTOCOL
    PROTOCOL = 'TEST'
    old_HAVE_URLLIB3 = HAVE_URLLIB3
    global HAVE_URLLIB3
    HAVE_URLLIB3 = True
    old_HAVE_URLLIB3_PYOPENSSLCONTEXT = HAVE_URLLIB3_PYOPENSSLCONTEXT
    global HAVE_URLLIB3_PYOPENSSLCONTEXT
    HAVE_URLLIB3_PYOPENSSLCONTEXT = True
   

# Generated at 2022-06-13 04:49:55.117718
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import types
    import unittest
    import unittest.mock as mock

    class FakeRequest(object):
        def __init__(self, method, headers, data=None, origin_req_host=None):
            self.method = method
            self.headers = headers
            self.data = data
            self.origin_req_host = origin_req_host

        def get_method(self):
            return self.method

        def get_data(self):
            return self.data

        def get_origin_req_host(self):
            return self.origin_req_host

    class TestRedirectHandlerFactory(unittest.TestCase):
        def test_redirect_handler_factory(self):
            ureq = urllib_request

# Generated at 2022-06-13 04:50:02.721184
# Unit test for function generic_urlparse
def test_generic_urlparse():
    # Test Py2.7 behavior
    parts = ParseResultDottedDict(scheme='http', netloc='user:pass@www.example.com:8888', path='/path', params='', query='', fragment='')
    assert generic_urlparse(parts) == {
        'hostname': 'www.example.com',
        'netloc': 'user:pass@www.example.com:8888',
        'fragment': '',
        'password': 'pass',
        'path': '/path',
        'params': '',
        'port': 8888,
        'scheme': 'http',
        'query': '',
        'username': 'user',
    }

# Generated at 2022-06-13 04:50:08.873451
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    # Test module function with no exception
    try:
        maybe_add_ssl_handler("https://www.google.com", False, ca_path=None)
    except Exception as err:
        assert "No exception was supposed to be raised"
    # Test module function with exception
    try:
        maybe_add_ssl_handler("https://www.google.com", True, ca_path=None)
    except NoSSLError:
        assert True
    except Exception as err:
        assert "NoSSLError exception was supposed to be raised"


# Generated at 2022-06-13 04:50:57.110282
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():

    with patch('socket.create_connection') as mock_create_connection:
        mock_create_connection.return_value = MagicMock()

        obj = CustomHTTPSConnection('localhost')
        obj.connect()

        assert mock_create_connection.call_count == 1

        # Note: Patching wrap_socket/wrap_socket and context.wrap_socket is not
        # possible with mock.  Thus, we only test that the method is called, but
        # not with the correct parameters.  The ssl module is tested in detail in
        # the test_utils_ssl module.
        if HAS_SSLCONTEXT or HAS_URLLIB3_PYOPENSSLCONTEXT:
            assert obj.context.wrap_socket.call_count == 1

# Generated at 2022-06-13 04:51:08.936111
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    handler_instance = RedirectHandlerFactory(follow_redirects='yes')(None, None)
    redirect_reqest = handler_instance.redirect_request(urllib_request.Request('http://localhost'), None, 301, 'msg', {}, 'http://localhost')
    assert redirect_reqest.has_header('Content-Length') is False
    assert redirect_reqest.get_method() == 'GET'

    handler_instance = RedirectHandlerFactory(follow_redirects='no')(None, None)
    try:
        handler_instance.redirect_request(urllib_request.Request('http://localhost'), None, 301, 'msg', {}, 'http://localhost')
        assert False, "should have raised an exception"
    except urllib_error.HTTPError:
        assert True

# Generated at 2022-06-13 04:51:10.741475
# Unit test for function fetch_url
def test_fetch_url():
    import requests
    t, u = fetch_url()



# Generated at 2022-06-13 04:51:16.431325
# Unit test for method detect_no_proxy of class SSLValidationHandler

# Generated at 2022-06-13 04:51:20.475309
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    '''Ensure build_ssl_validation_error raises a proper exception'''
    hostname = 'github.com'
    port = '443'
    paths = ['/usr/lib/ssl/certs/ca-certificates.crt', '/etc/ssl/certs/ca-certificates.crt']
    exc = 'certificate verify failed: %s' % paths[0]

    build_ssl_validation_error(hostname, port, paths, exc=exc)



# Generated at 2022-06-13 04:51:24.767157
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    try:
        build_ssl_validation_error('localhost', '443', ['/usr/local/etc/ca-certificates', '/etc/ssl/certs'])
    except SSLValidationError:
        assert True