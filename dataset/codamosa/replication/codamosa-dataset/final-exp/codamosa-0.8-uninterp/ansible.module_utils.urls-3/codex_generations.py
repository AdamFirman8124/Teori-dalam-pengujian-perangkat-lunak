

# Generated at 2022-06-13 04:47:05.759025
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    test_url = 'https://www.digi.com'
    test_validate_certs = True
    
    test_ssl_handler = maybe_add_ssl_handler(url=test_url, validate_certs=test_validate_certs)
    assert test_ssl_handler.hostname == 'www.digi.com'

# Generated at 2022-06-13 04:47:18.198560
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    assert sys.version_info < (3,)
    b_host = compat.str_to_bytes('host')
    b_host2 = compat.str_to_bytes('host2')
    kwargs = {
        'host': b_host,
        'port': 1,
        'timeout': 2,
        'key_file': b_host,
        'cert_file': b_host,
    }
    calls = []
    def create_connection(host_port, timeout, source_address=None):
        calls.append((host_port, timeout, source_address))
        return 10
    sock_calls = []

# Generated at 2022-06-13 04:47:27.730306
# Unit test for method patch of class Request
def test_Request_patch():
    from ansible.modules.network.fortios import fortios_firewall_policy_6
    from ansible.module_utils.network.fortios.fortios import FortiOSHandler
    # create a fake stub that mimics a FortiGate device
    stub = fortios_firewall_policy_6.stub()
    # set up the target device
    stub.system_global.get('replacemsg-fortiguard-wf-profile').value_get.return_value = "Normal"
    # create the AnsibleModule instance
    module = AnsibleModule(argument_spec=stub.argument_spec, supports_check_mode=False)
    from ansible.module_utils.network.fortios.fortios import Connection
    connection = Connection(module._socket_path, module)

# Generated at 2022-06-13 04:47:35.841329
# Unit test for function prepare_multipart
def test_prepare_multipart():
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": "application/octet-stream"
        },
        "file2": {
            "content": "text based file content",
            "filename": "fake.txt",
            "mime_type": "text/plain",
        },
        "text_form_field": "value"
    }

    content_type, body = prepare_multipart(fields)
    assert content_type == "multipart/form-data; boundary================7001255268859351152==", "Failed to prepare multipart/form-data body"
    assert body.startswith(b'--===============7001255268859351152==\r\nContent-Type: text/plain')
    assert b

# Generated at 2022-06-13 04:47:48.386569
# Unit test for function prepare_multipart
def test_prepare_multipart():
    fields = {
        "file1": {
            "filename": "/bin/true",
            "mime_type": "application/octet-stream"
        },
        "file2": {
            "content": "text based file content",
            "filename": "fake.txt",
            "mime_type": "text/plain",
        },
        "text_form_field": "value"
    }
    content_type, body = prepare_multipart(fields)
    assert content_type == "multipart/form-data; boundary="
    assert body.startswith('--')
    assert to_text(body).find('text based file content') >= 0


# Generated at 2022-06-13 04:47:59.076164
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest # noqa

    import tempfile
    with open(os.path.join(CERT_PATH, 'test_cert.pem'), 'r') as f:
        test_cert = f.read()
        test_cert = test_cert.replace('-----BEGIN CERTIFICATE-----', '').replace('-----END CERTIFICATE-----', '').replace('\n', '')
        if PY3:
            test_cert = bytes(test_cert, 'ascii')
        else:
            test_cert = bytes(bytearray(test_cert, 'ascii'))

    fd, temp_file_path = tempfile.mkstemp()


# Generated at 2022-06-13 04:48:05.124519
# Unit test for method connect of class UnixHTTPSConnection
def test_UnixHTTPSConnection_connect():
    '''Test that https_open() works with a UnixHTTPSConnection'''
    def _mock_request(*args, **kwargs):
        '''Mock HTTPConnection.request'''
        if 'timeout' in kwargs:
            return kwargs['timeout']

        return args[4]

    unix_connection = UnixHTTPSConnection('/path/to/socket')

    # We need monkeypatching, but we don't want to pollute the .connect method
    # of our own class, so we'll create a test object and monkeypatch it
    test_connection = httplib.HTTPSConnection('localhost')
    test_connection.request = _mock_request
    httplib.HTTPSConnection.connect = UnixHTTPConnection.connect

    # We need to ensure timeouts are preserved through the unix socket
    # by virtue of

# Generated at 2022-06-13 04:48:12.556783
# Unit test for function getpeercert
def test_getpeercert():
    try:
        url = 'https://docs.ansible.com/ansible/latest/portal/'
        response = urlopen(url, timeout=3,)
        assert getpeercert(response)
    except Exception as e:
        logger.error("Failed to get url: {0}".format(url) + "\nError: {0}".format(e))
        return False
# The following test may fail due to time out to get the certificate from the url
# test_getpeercert()

# Generated at 2022-06-13 04:48:16.833552
# Unit test for function fetch_url
def test_fetch_url():
    # All of the fetch_url tests are in test/integration/test_module_utils_urls.py
    pass



# Generated at 2022-06-13 04:48:29.278257
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    class MockSocket(object):
        def create_connection(self, *args, **kwargs):
            return None
    class MockSSLContext(object):
        def wrap_socket(self, *args, **kwargs):
            return None
    import ssl
    httplib.HTTPSConnection.__init__ = lambda x: None
    class MockHTTPSConnection(CustomHTTPSConnection):
        def __init__(self, *args, **kwargs):
            self.sock = None
            self.key_file = None
            self.cert_file = None
            self.timeout = None
            self.host = None
            self.port = None
            self.source_address = None
            self._tunnel_host = None
    MockHTTPSConnection.connect()
    MockHTTPSConnection.sock = MockSocket()
    Mock

# Generated at 2022-06-13 04:49:36.769596
# Unit test for function generic_urlparse
def test_generic_urlparse():
    import types
    # test for index lookups, and pass in an object that
    # does not have attributes
    parts = tuple(range(6))
    generic_parts = generic_urlparse(parts)
    assert generic_parts['scheme'] == 0
    assert generic_parts['netloc'] == 1
    assert generic_parts['path'] == 2
    assert generic_parts['params'] == 3
    assert generic_parts['query'] == 4
    assert generic_parts['fragment'] == 5
    with pytest.raises(AttributeError):
        generic_parts.netloc
    # test when we can access attributes

# Generated at 2022-06-13 04:49:40.340423
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    # Parameter check
    # no exception
    RedirectHandlerFactory()
    # exception
    try:
        RedirectHandlerFactory(follow_redirects='test')
    except ValueError as e:
        assert e.args[0] == 'follow_redirects must be one of no, none, urllib2, safe, or all'
    # Return type check
    assert isinstance(RedirectHandlerFactory(), RedirectHandlerFactory('no').__class__)


# Generated at 2022-06-13 04:49:43.292065
# Unit test for function getpeercert
def test_getpeercert():
    # Testing getpeercert in the "happy path"
    # NOTE: I'm not too sure how unit testing and mocking works, but this seems right
    # NOTE-2: If I'm running this on a host without an internet connection, this won't work
    response = urllib_request.urlopen('https://www.google.com')
    getpeercert(response)



# Generated at 2022-06-13 04:49:55.292063
# Unit test for function fetch_file

# Generated at 2022-06-13 04:50:01.006093
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    from unittest.mock import MagicMock
    from copy import deepcopy

    RedirectHandler = RedirectHandlerFactory('all')
    hdlr = RedirectHandler()


# Generated at 2022-06-13 04:50:07.366930
# Unit test for function fetch_file
def test_fetch_file():
    module = AnsibleModule(argument_spec=dict())
    url = 'http://www.google.com'
    file_path = fetch_file(module, url)
    fp = open(file_path, 'r')
    content = fp.read()
    if content.find('<html') == -1:
        raise AnsibleError('Unit test for function fetch_file failed %s' % content)
    os.remove(file_path)


# Generated at 2022-06-13 04:50:20.384716
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    handler = RedirectHandlerFactory(follow_redirects='all')
    assert type(handler) is RedirectHandlerFactory.RedirectHandler
    assert handler.follow_redirects == True

    handler = RedirectHandlerFactory(follow_redirects='none')
    assert type(handler) is RedirectHandlerFactory.RedirectHandler
    assert handler.follow_redirects == False

    handler = RedirectHandlerFactory(follow_redirects='safe')
    assert type(handler) is RedirectHandlerFactory.RedirectHandler
    assert handler.follow_redirects == 'safe'

    handler = RedirectHandlerFactory(follow_redirects='urllib2')
    assert type(handler) is RedirectHandlerFactory.RedirectHandler
    assert handler.follow_redirects == 'urllib2'


# Generated at 2022-06-13 04:50:25.173038
# Unit test for function fetch_url
def test_fetch_url():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(argument_spec=dict())
    url = 'http://localhost:8888/'
    r, info = fetch_url(module, url)
    print(info)
    print('\n'.join(sorted(info.keys())))



# Generated at 2022-06-13 04:50:31.556772
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    handler = SSLValidationHandler('httpbin.org', 443)
    cafile, cadata, paths_checked = handler.get_ca_certs()
    # Checks if get_ca_certs returns expected value
    if cafile and cadata and paths_checked:
        assert True
    else:
        assert False

# Generated at 2022-06-13 04:50:36.514499
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    from tempfile import NamedTemporaryFile
    import os

    # save previous trusted_hosts
    _trusted_hosts = url_opener.trusted_hosts

# Generated at 2022-06-13 04:51:27.649131
# Unit test for method connect of class UnixHTTPConnection
def test_UnixHTTPConnection_connect():
    # test that create a UnixHTTPConnection with a valid unix socket file
    unix_socket = '/tmp/test'
    u_socket = UnixHTTPConnection(unix_socket)
    # this method doesn't raise an exception
    u_socket.connect()
    assert u_socket.sock is not None
    try:
        os.remove('/tmp/test')
    except OSError:
        # The file didn't exist or has already been removed.
        pass
    # test that create a UnixHTTPConnection with an invalid unix socket file
    unix_socket = '/tmp/test'
    u_socket = UnixHTTPConnection(unix_socket)
    with pytest.raises(OSError):
        u_socket.connect()
    # Unit test for method __call__ of class UnixHTTPConnection
    # test that call a