

# Generated at 2022-06-13 04:46:26.594851
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''
    Test UnixHTTPConnection.connect:
    - Socket file is valid, no exception is expected
    - Socket file is invalid, an exception is expected
    '''
    # Test valid socket file
    uconn = UnixHTTPConnection('/var/run/docker.sock')
    try:
        uconn.connect()
    except OSError as e:
        # Valid socket file, no exception expected
        assert False, 'Valid socket file, no exception expected'
    finally:
        uconn.close()

    # Test invalid socket file
    invalid_socket_file = '/var/run/docker.sock_invalid'
    uconn = UnixHTTPConnection('/var/run/docker.sock_invalid')

# Generated at 2022-06-13 04:46:30.328637
# Unit test for function fetch_file
def test_fetch_file():
    """Test fetch_file"""
    module = AnsibleModule(argument_spec=url_argument_spec())
    rsp = fetch_file(module, 'https://github.com/ansible/ansible/archive/devel.zip')
    assert os.path.exists(rsp)



# Generated at 2022-06-13 04:46:34.711786
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    '''Ensure ``UnixHTTPSConnection(unix_socket).__call__(host, port)`` returns a working HTTPSConnection
    '''
    sock = socket.socket(socket.AF_UNIX)
    tmp = tempfile.NamedTemporaryFile()
    sock.bind(tmp.name)
    sock.listen()
    unix_conn = UnixHTTPSConnection(tmp.name)
    conn = unix_conn('localhost', 0)
    conn.sock.connect((tmp.name, 0))
    # Try to read from the server
    try:
        conn.sock.recv(1024)
    except socket.error:
        # Socket should be closed
        pass
    # Test for creation of socket for the unix domain

# Generated at 2022-06-13 04:46:43.243032
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class MockContext(object):
        def __init__(self, ctx):
            self.ctx = ctx
        def wrap_socket(self, *args, **kwargs):
            print(args)
            print(kwargs)
            if 'server_hostname' in kwargs and kwargs['server_hostname'] == 'google.com':
                with open('/tmp/google.com-443.log', 'w') as f:
                    f.write('success')


# Generated at 2022-06-13 04:46:44.859698
# Unit test for function fetch_url
def test_fetch_url():
    module = AnsibleModule(argument_spec=dict(module=dict(required=False, type='bool')))
    if module.params['module']:
        module.exit_json(changed=False)
    else:
        module.exit_json(changed=True)



# Generated at 2022-06-13 04:46:53.259727
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    data = open(os.path.join(os.path.dirname(__file__), 'test_get_channel_binding_cert_hash.pem'), 'rb').read()
    cert = ssl.PEM_cert_to_DER_cert(data)
    h = get_channel_binding_cert_hash(cert)
    assert base64.b64encode(h).decode() == "8dwWYfknzYmhBX9FWm8e21W/iQhfFLcAa/xnSW5/WjY="
if HAS_CRYPTOGRAPHY:
    test_get_channel_binding_cert_hash()



# Generated at 2022-06-13 04:46:58.165183
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    try:
        build_ssl_validation_error(hostname="localhost", port=443, paths=["/"])
    except Exception:
        pass



# Generated at 2022-06-13 04:47:08.192611
# Unit test for function fetch_url
def test_fetch_url():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    import json

    module = AnsibleModule(
        argument_spec=dict(
            url=dict(type='str', aliases=['dest', 'msg']),
            msg=dict(type='str'),
            dest=dict(type='str'),
        ),
        supports_check_mode=False,
    )

    data = {"msg": "Hi"}
    data_json = json.dumps(data)
    response, info = fetch_url(module,
                               "http://127.0.0.1:18888",
                               data=data_json,
                               headers={'Content-type': 'application/json'},
                               method="POST")

# Generated at 2022-06-13 04:47:10.065138
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    now = time.time()
    timetuple = time.gmtime(now)
    date = rfc2822_date_string(timetuple)
    t = parsedate_tz(date)
    then = time.mktime(t)
    assert abs(now - then) <= 10



# Generated at 2022-06-13 04:47:21.111415
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    '''
    Test function for the detect_no_proxy method of the SSLValidationHandler class
    '''
    _module = SSLValidationHandler(None, None)

    # Use a temp file because we don't really use a cert file, and don't have a valid hostname to use in the constructor
    fd, cert_path = tempfile.mkstemp()
    os.close(fd)
    _module.ca_path = cert_path


# Generated at 2022-06-13 04:48:00.363720
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():  # pylint: disable=missing-docstring,unused-argument
    with unix_socket_patch_httpconnection_connect():
        conn = UnixHTTPSConnection(unix_socket=None)('hostname')
        assert isinstance(conn, UnixHTTPSConnection)



# Generated at 2022-06-13 04:48:08.809303
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    '''Unit test for function build_ssl_validation_error'''

    import tempfile
    import shutil
    import os

    from ansible.module_utils.six.moves.urllib.error import URLError
    from ansible.module_utils.six import StringIO

    paths = ['/fake/path/1', '/fake/path/2']
    hostname = 'example.org'
    port = 443
    exc = URLError('Failed to make HTTPS connection')


# Generated at 2022-06-13 04:48:19.648011
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    '''
    This test should test that the method __call__
    of class UnixHTTPSConnection is actually returning self
    '''

    unix_socket = '/tmp/unk'
    unix_https_connection = UnixHTTPSConnection(unix_socket)

    assert unix_https_connection('127.0.0.1') is unix_https_connection

# Import module level behavior, which is equivalent to that of other
# modules
from ansible.module_utils.connection import Connection
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.connection import ConnectionForURI
from ansible.module_utils.connection import ConnectionFactory
from ansible.module_utils.connection import ConnectionInformation
from ansible.module_utils.connection import EncryptedConnection
from ansible.module_utils.connection import get_connection


# Generated at 2022-06-13 04:48:24.716009
# Unit test for function getpeercert
def test_getpeercert():

    class MyResponse():
        def __init__(self, fp):
            self.fp = fp

    class MyRaw():
        def __init__(self, sock):
            self._sock = sock

    class MySocket():
        def __init__(self, sock):
            self.fp = sock

    class MySock():
        def __init__(self, sock):
            self._sock = sock

    class MyClass():
        def getpeercert(self, binary_form=False):
            return socket.getpeercert(binary_form)

    response = MyResponse(MyRaw(MyClass()))
    assert getpeercert(response), "getpeercert() should euqal to self.fp.raw._sock.getpeercert()"


# Generated at 2022-06-13 04:48:34.404004
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    import shutil
    import tempfile
    import mock

    key_file = None
    cert_file = None

# Generated at 2022-06-13 04:48:39.386444
# Unit test for function getpeercert
def test_getpeercert():
    response = None
    try:
        response = test_urlopen('https://www.digicert.com/')
    except Exception:
        raise

    assert getpeercert(response) == getpeercert(response, binary_form=True)


# Generated at 2022-06-13 04:48:49.951122
# Unit test for function generic_urlparse
def test_generic_urlparse():
    '''
    Make sure that generic_urlparse does the same thing as urlparse
    '''
    import nose

# Generated at 2022-06-13 04:48:52.162910
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    assert SSLValidationHandler('hostname', 'port').http_request('req') == 'req'
# end of class SSLValidationHandler

# beginning of class Downloader

# Generated at 2022-06-13 04:48:55.511047
# Unit test for method validate_proxy_response of class SSLValidationHandler
def test_SSLValidationHandler_validate_proxy_response():
    SSLValidationHandler('test', 'test').validate_proxy_response("HTTP/1.0 200 OK")
    with pytest.raises(ProxErroyr):
        SSLValidationHandler('test', 'test').validate_proxy_response("Invalid response")



# Generated at 2022-06-13 04:49:01.873413
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    """ Run a unit test for function get_channel_binding_cert_hash """
    if not HAS_CRYPTOGRAPHY:
        return

# Generated at 2022-06-13 04:49:47.366412
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    '''Make sure UnixHTTPConnection.connect() method works'''

    # If a valid socket file is passed, the UnixHTTPConnection.connect() method should
    # not raise an error
    path = '/tmp/socket'
    foo = UnixHTTPConnection(path)
    foo.connect()

    # If an invalid socket file is passed, the UnixHTTPConnection.connect() method should
    # raise an OSError
    path = 'invalid/path/'
    foo = UnixHTTPConnection(path)
    with pytest.raises(OSError):
        foo.connect()


#
# Main
#


# Generated at 2022-06-13 04:49:57.538692
# Unit test for constructor of class CustomHTTPSConnection
def test_CustomHTTPSConnection():
    if not CustomHTTPSConnection:
        return False

    tls_version_map = {
        'PROTOCOL_SSLv3': ssl.PROTOCOL_SSLv3,
        'PROTOCOL_SSLv23': ssl.PROTOCOL_SSLv23,
        'PROTOCOL_TLSv1': ssl.PROTOCOL_TLSv1,
    }


# Generated at 2022-06-13 04:49:59.585667
# Unit test for function fetch_file
def test_fetch_file():
    fetch_file(None, 'http://www.google.com')


# Generated at 2022-06-13 04:50:01.161126
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    conn = UnixHTTPSConnection('/path/to/unix-socket')('hostname_not_important')
    assert isinstance(conn, UnixHTTPSConnection)

#
# Main functions
#



# Generated at 2022-06-13 04:50:04.971374
# Unit test for function prepare_multipart
def test_prepare_multipart():
    fields = {"file1": {"filename": "/bin/true", "mime_type": "application/octet-stream"},
              "file2": {"content": "text based file content", "filename": "fake.txt", "mime_type": "text/plain"},
              "text_form_field": "value"}
    try:
        prepare_multipart(fields)
    except Exception as e:
        print("Failed to run prepare_multipart: " + repr(e))



# Generated at 2022-06-13 04:50:11.405886
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    class UrlRequest(object):
        def __init__(self, url):
            self.url = url

        def get_full_url(self):
            return self.url

    handler = SSLValidationHandler("example.com", 443)

    # There is no no_proxy environment variable set
    req = UrlRequest("https://example.com")
    assert handler.detect_no_proxy(req.get_full_url()) == True

    # There is no no_proxy environment variable set
    req = UrlRequest("http://example.com")
    assert handler.detect_no_proxy(req.get_full_url()) == True

    # There is no no_proxy environment variable set
    # Hostname has invalid characters
    req = UrlRequest("http://example.com$")
    assert handler.detect_no_

# Generated at 2022-06-13 04:50:20.485462
# Unit test for function fetch_file
def test_fetch_file():
    ''' Unit test for fetch_file '''
    url = 'https://github.com/ansible/ansible/archive/devel.tar.gz'
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    # check results
    file_path = fetch_file(module, url)
    assert os.path.exists(file_path)
    # check length
    assert os.path.getsize(file_path) == 10792567
    # check content
    # TODO: check that file is a gz file


#
# Parsing functions
#


# Generated at 2022-06-13 04:50:23.997657
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    import httplib
    connection = UnixHTTPSConnection('/tmp/foo')
    assert isinstance(connection, httplib.HTTPSConnection)

# End of Python Software Foundation Licensed code



# Generated at 2022-06-13 04:50:30.909461
# Unit test for method make_context of class SSLValidationHandler
def test_SSLValidationHandler_make_context():

    # To support python < 2.7.9 we mock the constructor
    # of ssl.SSLContext and the method create_default_context
    # which was added in python 2.7.9

    # we need to mock these function of ssl module
    mock_cdata = MagicMock()
    mock_load_verify_locations = MagicMock()

    create_default_context = MagicMock()

    def return_mock_context(*args, **kwargs):
        context = MagicMock()
        context.load_verify_locations = mock_load_verify_locations
        return context

    ssl_context = MagicMock()
    ssl_context.__init__ = return_mock_context

    # We also need to mock these class of urllib3
    # as they are not available in python

# Generated at 2022-06-13 04:50:40.222572
# Unit test for function unix_socket_patch_httpconnection_connect
def test_unix_socket_patch_httpconnection_connect():
    from unittest.mock import MagicMock
    from contextlib import ExitStack

    m_super = MagicMock()
    m_foo_connect = MagicMock()
    foo_self = MagicMock()
    foo_self.sock = None

    class Foo(object):
        def connect(self):
            m_foo_connect(self)

        def __getattribute__(self, name):
            if name == 'connect':
                return m_foo_connect
            if name == '_connect':
                return m_super
            return super(Foo, self).__getattribute__(name)

    with ExitStack() as stack:
        stack.enter_context(unix_socket_patch_httpconnection_connect())
        Foo.connect(foo_self)

        foo_self.sock = 'foo'
       

# Generated at 2022-06-13 04:51:19.824067
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():

    def test_case(follow_redirects, method, status, expected):
        redirect_handler = RedirectHandlerFactory(follow_redirects)
        request = RequestWithMethod('http://example.com', method)
        response = redirect_handler.redirect_request(request, None, status, None, None, 'http://example.com')
        assert isinstance(response, expected)

    test_case('safe', 'GET', 301, urllib_error.HTTPError)   # always fail
    test_case('safe', 'POST', 301, urllib_error.HTTPError)  # always fail
    test_case('safe', 'HEAD', 301, urllib_error.HTTPError)  # always fail
    test_case('safe', 'GET', 302, urllib_request.Request)  # always pass
    test_case