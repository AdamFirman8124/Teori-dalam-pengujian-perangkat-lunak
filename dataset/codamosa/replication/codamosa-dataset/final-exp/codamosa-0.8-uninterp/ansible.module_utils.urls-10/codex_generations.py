

# Generated at 2022-06-13 04:45:22.618747
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    # Setup
    ssl_handler = SSLValidationHandler('test_hostname', 'test_port', 'test_ca_path')
    expected = False
    os.environ['no_proxy'] = "google.com, cnn.com"
    # Exercise
    actual = ssl_handler.detect_no_proxy("https://localhost:2345")
    # Verify
    assert expected == actual

# Generated at 2022-06-13 04:45:26.013335
# Unit test for function unix_socket_patch_httpconnection_connect
def test_unix_socket_patch_httpconnection_connect():
    with unix_socket_patch_httpconnection_connect():
        assert UnixHTTPConnection.connect == httplib.HTTPConnection.connect
    assert UnixHTTPConnection.connect != httplib.HTTPConnection.connect


# Generated at 2022-06-13 04:45:38.838045
# Unit test for function prepare_multipart
def test_prepare_multipart():
    # Use a binary file for this test and load the entire file into memory
    filename = to_bytes(os.path.join(os.path.dirname(__file__), './http-test-server.py'))
    with open(filename, 'rb') as f:
        file_content = f.read()

    # A simple form with one field and one file
    test_fields = {
        'file1': {
            'filename': filename,
            'mime_type': 'application/octet-stream'
        },
        'text_form_field': 'value'
    }

    content_type, body = prepare_multipart(test_fields)
    assert isinstance(content_type, str)
    assert isinstance(body, bytes)

    # Simple test, validate the Content-Type
    assert content_type

# Generated at 2022-06-13 04:45:51.168947
# Unit test for function generic_urlparse

# Generated at 2022-06-13 04:45:53.383878
# Unit test for constructor of class Request
def test_Request():

    req = Request('https://httpbin.org/get')
    assert req.get_method() == 'GET'
    assert req.get_full_url() == 'https://httpbin.org/get'
    assert not req.has_data()


# Generated at 2022-06-13 04:46:00.573051
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    hostname = 'localhost'
    port = 22
    ca_path = None

    handler = SSLValidationHandler(hostname, port, ca_path)

    url = 'https://127.0.0.1:22'
    assert handler.detect_no_proxy(url) is False

    url = 'https://127.0.0.1:33'
    assert handler.detect_no_proxy(url) is True

# Generated at 2022-06-13 04:46:13.333699
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    request = RequestWithMethod('http://www.google.com', 'GET')
    assert request.get_method() == 'GET'
    request = RequestWithMethod('http://www.google.com', 'PUT')
    assert request.get_method() == 'PUT'
    request = RequestWithMethod('http://www.google.com', 'DELETE')
    assert request.get_method() == 'DELETE'
    request = RequestWithMethod('http://www.google.com', 'HEAD')
    assert request.get_method() == 'HEAD'
    request = RequestWithMethod('http://www.google.com', 'OPTIONS')
    assert request.get_method() == 'OPTIONS'
    request = RequestWithMethod('http://www.google.com', 'TRACE')

# Generated at 2022-06-13 04:46:18.404087
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    try:
        build_ssl_validation_error(hostname='foo', port='443', paths=['foo', 'bar'])
        assert False, 'Should fail without SSLContext module'
    except SSLValidationError:
        assert True
        pass


# Generated at 2022-06-13 04:46:19.550574
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    with pytest.raises(AttributeError):
        CustomHTTPSHandler()


# Generated at 2022-06-13 04:46:30.764465
# Unit test for function prepare_multipart
def test_prepare_multipart():
    expected_content_type = 'multipart/form-data; boundary="===============1089153067=="'

# Generated at 2022-06-13 04:49:37.877320
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    from calendar import timegm
    from datetime import datetime

    two_hours_before_epoch = timegm((1969, 12, 31, 21, 0, 0, 2, 365, 0)) * 1000
    two_hours_before_epoch_datetime = datetime.utcfromtimestamp(two_hours_before_epoch / 1000)
    assert rfc2822_date_string(two_hours_before_epoch_datetime.utctimetuple()) == "Wed, 31 Dec 1969 21:00:00 -0000"
# end Unit test



# Generated at 2022-06-13 04:49:43.894461
# Unit test for method get_method of class RequestWithMethod
def test_RequestWithMethod_get_method():
    '''
    Unit tests for the get_method method of the RequestWithMethod class
    '''
    rwm = RequestWithMethod('http://foo.bar', 'post')
    assert rwm.get_method() == 'POST'
    del rwm
    rwm = RequestWithMethod('http://foo.bar', 'delete')
    assert rwm.get_method() == 'DELETE'
    del rwm
    rwm = RequestWithMethod('http://foo.bar', 'PUT')
    assert rwm.get_method() == 'PUT'
    del rwm
    rwm = RequestWithMethod('http://foo.bar', 'put')
    assert rwm.get_method() == 'PUT'
    del rwm
    rwm = RequestWithMethod('http://foo.bar')

# Generated at 2022-06-13 04:49:47.596560
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    import os.path
    import tempfile
    tf, tfname = tempfile.mkstemp()
    try:
        import requests
        from requests.compat import urlparse
        r = requests.get(urlparse.urlunsplit(('http', tfname, '/v1/keys/foo', '', '')), stream=True)
    finally:
        os.unlink(tfname)



#
# Requests



# Generated at 2022-06-13 04:49:54.532606
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    """
    Test RedirectHandlerFactory.
    """
    u = urllib_request.build_opener(RedirectHandlerFactory('urllib2'))
    urllib_request.install_opener(u)
    _http_error_302 = urllib_error.HTTPErrorProcessor()
    _http_error_302.http_error_302 = mock.Mock(return_value=True)
    _http_error_302.http_error_default(mock.Mock(), mock.Mock(), 302, mock.Mock(), mock.Mock())
    assert _http_error_302.http_error_302.called
    u = urllib_request.build_opener(RedirectHandlerFactory(None))
    urllib_request.install_opener(u)

# Generated at 2022-06-13 04:49:58.622622
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    '''unit test for function build_ssl_validation_error'''
    error = build_ssl_validation_error('test', '1234', ['/valid/path', '/invalid/path'])
    assert error.args[0].startswith('Failed to validate the SSL certificate for test:1234.')
    assert 'validate_certs=False' in error.args[0]
    assert 'SNI' in error.args[0]
    assert ', /valid/path, /invalid/path' in error.args[0]
    error = build_ssl_validation_error('test', '1234', ['/valid/path', '/invalid/path'], exc='test exception')
    assert 'The exception msg was: test exception' in error.args[0]


# Generated at 2022-06-13 04:50:04.039989
# Unit test for function generic_urlparse
def test_generic_urlparse():
    parts = generic_urlparse(urlparse('https://foo:bar@baz:8080/path/to?arg=1#fragment'))
    assert parts.scheme == 'https'
    assert parts.netloc == 'foo:bar@baz:8080'
    assert parts.path == '/path/to'
    assert parts.params == ''
    assert parts.query == 'arg=1'
    assert parts.fragment == 'fragment'
    assert parts.username == 'foo'
    assert parts.password == 'bar'
    assert parts.hostname == 'baz'
    assert parts.port == 8080
    parts = generic_urlparse(urlparse('https://baz:8080/path/to?arg=1#fragment'))
    assert parts.scheme == 'https'
   

# Generated at 2022-06-13 04:50:11.065451
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    test_certificate_file = 'test/unit/support/certificate.cer'
    test_certificate_der = load_file(test_certificate_file)
    test_certificate_hash = x509.load_der_x509_certificate(test_certificate_der, default_backend()).fingerprint(hashes.SHA256())
    assert test_certificate_hash == get_channel_binding_cert_hash(test_certificate_der)

# Generated at 2022-06-13 04:50:14.735188
# Unit test for function generic_urlparse
def test_generic_urlparse():
    '''
    Test generic_urlparse with no data
    '''
    assert generic_urlparse(urlparse('')) == generic_urlparse(urlparse(''))



# Generated at 2022-06-13 04:50:26.679391
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    url_without_no_proxy_env = "https://10.0.0.1"
    url_with_hostname_in_no_proxy_env = "https://10.0.0.2"
    url_with_hostname_substring_in_no_proxy_env = "https://10.0.0.3"
    url_with_ip_in_no_proxy_env = "https://10.0.0.4"
    os.environ['no_proxy'] = "10.0.0.2,10.0.0.3.substring,10.0.0.4"
    handler = SSLValidationHandler("foo", "443")
    handler_no_proxy = SSLValidationHandler("foo", "443")
    handler_proxy = SSLValidationHandler("foo", "443")

# Generated at 2022-06-13 04:50:32.743397
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    '''Test build_ssl_validation_error'''
    global HAS_SSLCONTEXT
    global HAS_URLLIB3_PYOPENSSLCONTEXT
    global HAS_URLLIB3_SSL_WRAP_SOCKET
    HAS_SSLCONTEXT = True
    HAS_URLLIB3_PYOPENSSLCONTEXT = True
    HAS_URLLIB3_SSL_WRAP_SOCKET = False

    hostname = 'www.example.com'
    port = '80'
    paths = ['/usr/local/etc/ssl/cert.pem', '/etc/ssl/cert.pem']
    exc = 'SSL_ERROR_SSL'