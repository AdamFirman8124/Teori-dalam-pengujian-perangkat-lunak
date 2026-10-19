

# Generated at 2022-06-13 04:45:40.214822
# Unit test for method __call__ of class UnixHTTPSConnection
def test_UnixHTTPSConnection___call__():
    # Disable pylint check for the super() call. It complains about UnixHTTPSConnection
    # being a NoneType because of the initial definition above, but it won't actually
    # be a NoneType when this code runs
    # pylint: disable=bad-super-call
    super(UnixHTTPSConnection, UnixHTTPSConnection('/path/to/unix/socket'))

# Generated at 2022-06-13 04:45:41.175355
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    http_handler = CustomHTTPSHandler
    # Just call the constructor
    http_handler()


# Generated at 2022-06-13 04:45:49.254177
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    for url in ('https://www.google.com', 'https://www.redhat.com', 'https://github.com'):
        handler = SSLValidationHandler('', hostname='', port=443)
        req = urllib_request.Request('https://www.redhat.com')
        try:
            handler.http_request(req)
        except Exception as e:
            return False
    return True

# Generated at 2022-06-13 04:45:59.941906
# Unit test for function fetch_file
def test_fetch_file():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    test_url = "https://raw.githubusercontent.com/ansible/ansible/devel/hacking/test-module"
    test_file_path = os.path.join(curr_dir, "test_fetch_file.py")
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
    module = AnsibleModule({}, {'dest': test_file_path})
    test_file_path = fetch_file(module, test_url)
    assert os.path.exists(test_file_path)
    os.remove(test_file_path)



# Generated at 2022-06-13 04:46:13.230169
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    '''
    Build out an error in all the different scenarios
    '''
    # If we have all the way down to the SSL wrap socket, then we know what the exception is
    if HAS_URLLIB3_SSL_WRAP_SOCKET:
        with pytest.raises(SSLValidationError) as ex:
            build_ssl_validation_error('test', 80, [], Exception('bad_ssl'))
        assert 'bad_ssl' in str(ex.value)

    # If we don't have urllib3 support all the way down, and we don't have
    # SSLContext to raise a meaningful error, raise the more generic one
    # when we don't have a specific error

# Generated at 2022-06-13 04:46:21.738613
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    try:
        CustomHTTPSHandler()
    except TypeError as e:
        if '_context' in str(e):
            raise TypeError("%s needs to be initialized with a ssl context in order to use CustomHTTPSHandler.\n"
                            "Try installing a ssl library such as pyopenssl or pyopenssl." % repr(CustomHTTPSHandler))
        else:
            raise



# Generated at 2022-06-13 04:46:32.944961
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    def _create_request(hostname, port, ca_path=None):
        req = Request('https://%s:%s/' % (hostname, port))
        req.add_header('Accept-Encoding', 'identity')
        # Don't use original SSL handler
        req.get_method = lambda: 'GET'

        handler = SSLValidationHandler(hostname, port, ca_path)
        return handler.do_open(MockOpenerDirector(), req)

    def _custom_ssl_context(cafile=None, cadata=None):
        context = create_default_context(cafile=cafile)
        if cafile or cadata:
            context.load_verify_locations(cafile=cafile, cadata=cadata)
        return context


# Generated at 2022-06-13 04:46:38.932429
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    # setup
    global HAS_SSLCONTEXT
    global HAS_URLLIB3_PYOPENSSLCONTEXT
    global HAS_URLLIB3_SSL_WRAP_SOCKET
    HAS_SSLCONTEXT = True
    HAS_URLLIB3_PYOPENSSLCONTEXT = True
    HAS_URLLIB3_SSL_WRAP_SOCKET = True

    # test 1
    url = 'https://ansible.com/'
    handler = maybe_add_ssl_handler(url, True)
    assert isinstance(handler, SSLValidationHandler)

    # tear down
    HAS_SSLCONTEXT = False
    HAS_URLLIB3_PYOPENSSLCONTEXT = False
    HAS_URLLIB3_SSL_WRAP_SOCKET = False



# Generated at 2022-06-13 04:46:45.568888
# Unit test for method connect of class CustomHTTPSConnection
def test_CustomHTTPSConnection_connect():
    ok_(hasattr(CustomHTTPSConnection, '__init__'))
    ok_(hasattr(CustomHTTPSConnection, 'connect'))


    cc = CustomHTTPSConnection('example.com')
    cc.connect()


    ok_(hasattr(CustomHTTPSConnection, '_context'))
    ok_(isinstance(cc, CustomHTTPSConnection))
    ok_(hasattr(cc, 'context'))
    eq_(cc.context, None)

    if HAS_SSLCONTEXT:
        eq_(cc._context.verify_flags, CERT_REQUIRED)
        eq_(cc._context.check_hostname, True)

        ok_(id(cc._context) != id(cc.context))
    else:
        ok_(HAS_URLLIB3_PYOPENSSLCONTEXT)

# Generated at 2022-06-13 04:46:49.760553
# Unit test for function fetch_url
def test_fetch_url():

    r = """<html><body><h1>401 Unauthorized</h1>
You need a valid user and password to access this resource.
</body></html>
"""

    class MockRequest(object):
        def __init__(self, r):
            self.readline = [r]

        def readlines(self):
            return self.readline

    class MockUrllib(object):
        class error(object):
            class URLError(Exception):
                def __init__(self, r):
                    pass

            class HTTPError(Exception):
                def __init__(self, r):
                    pass

        def HTTPBasicAuthHandler(self, handler):
            return handler

        def HTTPDigestAuthHandler(self, handler):
            return handler

        def HTTPPasswordMgrWithDefaultRealm(self):
            return

# Generated at 2022-06-13 04:47:57.968643
# Unit test for function getpeercert
def test_getpeercert():
    """ Ensure the getpeercert() function works correctly. """
    # Mock the response object
    class MockResponse(object):
        """ Response object, which can be monkey-patched with a different socket. """

        def __init__(self, socket):
            self.socket = socket

    # Mock the socket object
    class MockSocket(object):
        """ Socket object, which can be monkey-patched with a different getpeercert method. """

        def __init__(self, getpeercert):
            self.getpeercert = getpeercert

    # Test 1: Socket returns a string.
    mock_socket = MockSocket(lambda x: "string")
    mock_response = MockResponse(mock_socket)
    response = getpeercert(mock_response)

# Generated at 2022-06-13 04:48:07.655059
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    hostname = 'foo'
    port = 42
    paths = ['p1', 'p2']
    try:
        raise SSLValidationError('shazam!')
    except SSLValidationError as e:
        exc = e

    try:
        raise build_ssl_validation_error(hostname, port, paths, exc=exc)
    except SSLValidationError as e:
        # since we don't control the exact exception message format,
        # we can't use to_native() here or the test will fail
        exc = e
        print(exc.args[0])

    py_version = sys.version_info[:3]

# Generated at 2022-06-13 04:48:15.672302
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    # Test default behavior
    handler = RedirectHandlerFactory()
    assert isinstance(handler, urllib_request.HTTPRedirectHandler)
    assert handler.follow_redirects == True

    # Test 'no' handling
    handler = RedirectHandlerFactory('no')
    assert isinstance(handler, urllib_request.HTTPRedirectHandler)
    assert handler.follow_redirects == False

    # Test 'all' handling
    handler = RedirectHandlerFactory('all')
    assert isinstance(handler, urllib_request.HTTPRedirectHandler)
    assert handler.follow_redirects == True

    # Test 'safe' handling
    handler = RedirectHandlerFactory('safe')
    assert isinstance(handler, urllib_request.HTTPRedirectHandler)
    assert handler.follow_red

# Generated at 2022-06-13 04:48:23.669034
# Unit test for method get_ca_certs of class SSLValidationHandler
def test_SSLValidationHandler_get_ca_certs():
    '''
    Unit test for method get_ca_certs of class SSLValidationHandler
    '''
    hostname = 'localhost'
    port = 443
    svh = SSLValidationHandler(hostname, port)
    ca_path, cadata, paths_checked = svh.get_ca_certs()
    assert ca_path or cadata, "Failed to get CA cert."
    assert paths_checked, "Failed to get path checked."



# Generated at 2022-06-13 04:48:32.420941
# Unit test for method make_context of class SSLValidationHandler
def test_SSLValidationHandler_make_context():
    def test_func(hostname, port, expected_context):
        class MockContext(object):
            def __init__(self, cafile, capath):
                self.capath = capath
                self.cafile = cafile

        context = SSLValidationHandler(hostname, port).make_context(None)
        assert isinstance(context, expected_context)


    test_func.description = "Test method make_context of class SSLValidationHandler"
    yield test_func, 'hostname', 'port', ssl.SSLContext
    yield test_func, 'hostname', 'port', urllib3.util.ssl_.SSLContext



# Generated at 2022-06-13 04:48:44.708514
# Unit test for constructor of class CustomHTTPSHandler
def test_CustomHTTPSHandler():
    import os
    import tempfile
    (fd, dummy_cert_file) = tempfile.mkstemp()

    with os.fdopen(fd, "w"):
        os.utime(dummy_cert_file, None)

    handler = CustomHTTPSHandler(cert_file=dummy_cert_file)
    assert handler.cert_file == dummy_cert_file


# An HTTPSConnection class that uses the platform/system certs

# Generated at 2022-06-13 04:48:45.821817
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    assert RedirectHandlerFactory is not None

# Generated at 2022-06-13 04:48:58.786155
# Unit test for function build_ssl_validation_error
def test_build_ssl_validation_error():
    """
    Check if msg is set up correctly for various SSLValidationError conditions
    """
    from ansible.module_utils.urls import SSLValidationError

    # If SSLContext is available, exc will be None
    with pytest.raises(SSLValidationError) as excinfo:
        build_ssl_validation_error(hostname='example.com', port=443,
                                   paths=['/etc/ssl/certs/ca-certificates.crt'],
                                   exc=None)
    msg = str(excinfo.value)
    assert msg.startswith('Failed to validate the SSL certificate for example.com:443.')
    assert 'You can use validate_certs=False if you do not need to confirm the servers identity' in msg

# Generated at 2022-06-13 04:49:08.646575
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import subprocess

    # Get an HTTP url to test with
    cmd = './tests/module_utils/test_urlopen.py'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sout, serr = proc.communicate()
    url = to_text(sout).strip()
    if not url:
        raise Exception('No URL returned from test_urlopen.py: %s' % to_text(serr))

    # Test behavior of different parameters
    for param in [True, False, 'no', 'none', 'all', 'yes', 'urllib2', 'safe']:
        handler = RedirectHandlerFactory(follow_redirects=param)
        opener = urllib_request.build_op

# Generated at 2022-06-13 04:49:14.529063
# Unit test for function fetch_file
def test_fetch_file():
    module = AnsibleModule(
        argument_spec={},
    )
    url = "https://github.com/ansible/ansible/archive/devel.tar.gz"
    data = None
    headers = None
    method = None
    use_proxy = True
    force = False
    last_mod_time = None
    timeout = 10
    unredirected_headers = None
    fetch_file(module, url, data=data, headers=headers, method=method, use_proxy=use_proxy,
               force=force, last_mod_time=last_mod_time, timeout=timeout, unredirected_headers=unredirected_headers)
    assert True