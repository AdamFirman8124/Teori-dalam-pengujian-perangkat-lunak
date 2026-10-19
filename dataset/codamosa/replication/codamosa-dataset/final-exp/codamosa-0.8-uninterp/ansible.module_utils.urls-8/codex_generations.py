

# Generated at 2022-06-13 04:45:55.390453
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    # From the RFC 2822 document:
    #
    #     Fri, 09 Nov 2001 01:08:47 -0000
    #
    #     Examples:
    #
    #     Fri, 09 Nov 2001 01:08:47 -0000
    #     ---> 2001-11-09T01:08:47-00:00
    #
    #     Thu, 13 Oct 1983 10:13:00 -0700
    #     ---> 1983-10-13T10:13:00-07:00
    timetuple = (2001, 11, 9, 1, 8, 47, 4)
    zone = '-0000'
    assert rfc2822_date_string(timetuple, zone) == 'Fri, 09 Nov 2001 01:08:47 -0000', rfc2822_date_string(timetuple, zone)


# Generated at 2022-06-13 04:46:00.093668
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    '''
    Unit test for function RedirectHandlerFactory
    '''
    mock_req = MagicMock(spec_set=urllib_request.Request)
    mock_req.get_method.return_value = 'GET'
    mock_req.get_full_url.return_value = "https://example.com"
    mock_req.data = None
    mock_req.headers = {'Test-Header': '42'}
    mock_fp = MagicMock(spec_set=file)
    mock_fp.read.return_value = '<html>Hello World</html>'
    # Test for 301 redirect
    redirect_handler = RedirectHandlerFactory('urllib2')

# Generated at 2022-06-13 04:46:05.141334
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    import urllib2
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six.moves.urllib.error import URLError
    from ansible.module_utils.urls import assert_url_https

    url = 'https://docs.python.org/2/library/ssl.html'
    # urllib2.HTTPSHandler is always present, even if we are using the SSLContext
    # version of the handler
    assert 'HTTPSHandler' in dir(urllib2)
    assert 'urlopen' in dir(urllib2)

    # we skip this check on py2.6 and below, because we only support >= 2.7

# Generated at 2022-06-13 04:46:16.492905
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    global DUMMY_CA_CERT
    class Mocked(object):
        def __init__(self):
            self.cert = b_DUMMY_CA_CERT
            self.capath = None

        def load_verify_locations(self, cafile=None, cadata=None):
            if cafile:
                with open(cafile, 'rb') as f:
                    self.cert += f.read()
            elif cadata:
                self.cert += cadata

    s = Mocked()
    tmp_ca_cert_path, cadata, paths_checked = SSLValidationHandler.get_ca_certs(s, '127.0.0.1', 443)
    with open(tmp_ca_cert_path, 'rb') as f:
        result = f.read()

# Generated at 2022-06-13 04:46:22.765352
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    hostname = 'test.example.com'
    port = 443

    try:
        build_ssl_validation_error(hostname, port, [])
    except SSLValidationError:
        pass

    try:
        build_ssl_validation_error(hostname, port, [], None)
    except SSLValidationError:
        pass

    try:
        build_ssl_validation_error(hostname, port, [], 'Test Error')
    except SSLValidationError:
        pass



# Generated at 2022-06-13 04:46:33.305576
# Unit test for function unix_socket_patch_httpconnection_connect
def test_unix_socket_patch_httpconnection_connect():
    sock = '/tmp/foo.bar.sock'
    with unix_socket_patch_httpconnection_connect():
        conn = UnixHTTPSConnection(sock)
    assert conn.sock is None
test_unix_socket_patch_httpconnection_connect()


# Generated at 2022-06-13 04:46:36.395406
# Unit test for function fetch_file
def test_fetch_file():
    p, d, u = fetch_file(module, 'https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/modules/core/cloud/amazon/ec2_lc_find.py')
    assert os.path.exists(p), 'Failed to fetch file'
    assert 'ec2_lc_find' in open(p, 'r').read(), 'Did not fetch correct file'
    os.remove(p)


# Generated at 2022-06-13 04:46:44.056280
# Unit test for function getpeercert
def test_getpeercert():
    if not os.path.exists('/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem'):
        return
    try:
        response = open_url('https://pypi.python.org/pypi/')
        pem = getpeercert(response, True)
    except (UnicodeError, IOError, ssl.SSLError):
        return
    assert isinstance(pem, bytes)
    # Check if pem is a valid certificate
    assert ssl.DER_cert_to_PEM_cert(pem).startswith(b'-----BEGIN CERTIFICATE-----')
    assert ssl.DER_cert_to_PEM_cert(pem).endswith(b'-----END CERTIFICATE-----\n')


# Generated at 2022-06-13 04:46:46.376992
# Unit test for method open of class Request
def test_Request_open():
    assert True



# Generated at 2022-06-13 04:46:50.133758
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    use_proxy = SSLValidationHandler('127.0.0.1', 443, 'ca_path').detect_no_proxy('https://hourglass.example.com')
    assert (use_proxy == False), 'Failed to detect no_proxy!'


# Generated at 2022-06-13 04:49:25.446699
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    ##########################################################################
    # NOTE: Please do not add tests for CustomHTTPSConnection.connect() here.
    #       Tests for this method belong in the test_connection.py file.
    ##########################################################################
    pass


# Generated at 2022-06-13 04:49:33.093931
# Unit test for function fetch_file
def test_fetch_file():
    testmodule = AnsibleModule(argument_spec={})
    testmodule.tmpdir = "/tmp"
    testmodule.fail_json = lambda msg: None
    testmodule.add_cleanup_file = lambda file: None
    file_name = fetch_file(testmodule, "http://localhost:8080/example.txt")
    with open(file_name, "r") as fd:
        assert fd.read() == "Example text"


# Generated at 2022-06-13 04:49:45.986966
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    import platform

# Generated at 2022-06-13 04:49:56.690368
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    class MockSSLContext(object):
        def load_verify_locations(self, *args):
            return
    class MockSocket(object):
        def create_connection(self, address):
            return
    class MockSSL(object):
        def wrap_socket(self, sock, *args):
            return
        def get_default_verify_paths(self):
            class MockDefaultVerifyPaths(object):
                capath=''
            return MockDefaultVerifyPaths()
    class MockSSLValidationHandler(SSLValidationHandler):
        def detect_no_proxy(self, url):
            return True
    class MockOs(object):
        def __init__(self):
            self.path = MockOsPath()

# Generated at 2022-06-13 04:50:02.483400
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    try:
        mock_wrap_socket = MagicMock(side_effect=socket.error('boo'))
        with patch('ssl.wrap_socket', mock_wrap_socket):
            c = CustomHTTPSConnection('hostname', 443)
            c.connect()
            assert False, 'should have failed because of invalid cert'
    except socket.error as e:
        assert 'boo' == str(e)
    except Exception as e:
        assert False, 'Should not have failed with %s' % e

    # checks: self.context.wrap_socket(

# Generated at 2022-06-13 04:50:07.967687
# Unit test for function generic_urlparse

# Generated at 2022-06-13 04:50:20.640191
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():

    hostname = 'localhost'
    port = 443

    try:
        handler = SSLValidationHandler(hostname, port, None)
    except SSLValidationError as e:
        assert True, ('SSLValidationError exception did not occur')
    except Exception as e:
        assert False, ('Wrong exception caught')


if HAS_SSLCONTEXT:

    class CertificateError(ssl.SSLError):
        pass

elif HAS_URLLIB3_PYOPENSSLCONTEXT:

    class CertificateError(CertificateError):
        pass
else:

    class CertificateError(ssl.SSLError):
        pass
        # from OpenSSL import SSL


        # def certificate_error(connection, certificate, errorType, errorNumber, errorDepth, request):
        #         return True
        #
        # class Context

# Generated at 2022-06-13 04:50:26.492576
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    cert_path = 'tests/fixtures/test_ca.pem'
    handler = SSLValidationHandler(None, None, cert_path)
    test_ca_cert_path, test_cadata, test_paths_checked = handler.get_ca_certs()
    assert test_ca_cert_path == cert_path
    assert len(test_cadata) > 0

# Unit tests for method detect_no_proxy of class SSLValidationHandler

# Generated at 2022-06-13 04:50:31.509893
# Unit test for method open of class Request
def test_Request_open():
    request = Request()
    response = request.open("GET", "https://www.baidu.com")
    print("test_Request_open: %d" % response.getcode())

if __name__ == '__main__':
    test_Request_open()

# Generated at 2022-06-13 04:50:39.652991
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
  url = "https://somehost"
  def test_returns_true_when_env_no_proxy_not_set():
    assert SSLValidationHandler('foo', 123).detect_no_proxy(url) == True
  def test_returns_true_when_env_no_proxy_is_empty():
    os.environ['no_proxy'] = ''
    assert SSLValidationHandler('foo', 123).detect_no_proxy(url) == True
  def test_returns_true_when_env_no_proxy_not_match():
    os.environ['no_proxy'] = 'localhost'
    assert SSLValidationHandler('foo', 123).detect_no_proxy(url) == True
  def test_returns_false_when_env_no_proxy_is_set():
    os.en