

# Generated at 2022-06-13 04:45:18.837317
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    test_handler = SSLValidationHandler('localhost', 443)

    # Test 1: no_proxy not set
    os.environ.pop('no_proxy', None)

    assert test_handler.detect_no_proxy('https://localhost') == True
    assert test_handler.detect_no_proxy('https://localhost:443') == True

    # Test 2: no_proxy is set, but does not match
    os.environ['no_proxy'] = 'example.com'

    assert test_handler.detect_no_proxy('https://localhost') == True
    assert test_handler.detect_no_proxy('https://localhost:443') == True

    # Test 3: no_proxy matches the hostname only
    os.environ['no_proxy'] = 'localhost'

    assert test_handler.detect_no_proxy

# Generated at 2022-06-13 04:45:30.388865
# Unit test for function generic_urlparse
def test_generic_urlparse():
    ##########################################################################
    # NOTE the tests here are here to handle the difference between
    # Python 2.6 and Python 2.7
    # The tests should run successfully on both versions
    ##########################################################################
    # Unit tests for generic_urlparse
    # tests for Py2.6
    #pylint: disable=protected-access
    urlparse = urlparse26 = urllib_parse._original_result
    #pylint: enable=protected-access
    with patch('ansible.module_utils.urls.urllib_parse._original_result', new=urlparse):
        parts = urlparse('git+https://github.com/ansible/ansible-modules-core.git#egg=ansible-modules-core&subdirectory=lib/ansible')
        # testing an older style urlparse with a relative path


# Generated at 2022-06-13 04:45:39.062922
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    from time import timezone
    from calendar import timegm
    from time import gmtime
    t = gmtime(timegm(gmtime()) - timezone)
    if gmtime(timegm(t) - timezone) == t:
        t = gmtime(timegm(t))
    t = t[:6] + (-t[6],)
    assert rfc2822_date_string(t) == 'Fri, 09 Nov 2001 01:08:47 -0000'


# Generated at 2022-06-13 04:45:44.799791
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.six.moves import mock
    import json
    class FakeResponse(object):
        def __init__(self, status_code=200, text=None,
                     headers=None, json_data=None,
                     links=None, reason=None):
            self.status_code = status_code
            self.text = text
            self.headers = headers
            self.links = links
            self.json_data = json_data
            self.reason = reason

        def json(self):
            return self.json_data

        def header_links(self):
            return self.links

        def raise_for_status(self):
            raise HTTPError(self.reason)


# Generated at 2022-06-13 04:45:48.982723
# Unit test for function getpeercert
def test_getpeercert():
    # create a mocked HTTP reponse for http://www.google.ca
    response = httptest.HTTPServer(('www.google.ca', 443))
    response.data = 'foo'

    # Ensure the peer certificate is returned
    if PY3:
        socket = response.fileno()
    else:
        socket = response.socket
    assert getpeercert(response) == socket.getpeercert()



# Generated at 2022-06-13 04:45:53.295108
# Unit test for constructor of class CustomHTTPSConnection
def test_CustomHTTPSConnection():
    h = CustomHTTPSConnection('example.org', 443)
    # Note: self._tunnel_host is not available on py < 2.6 but this code isn't used on py < 2.6 (lack of create_connection)
    h._tunnel_host = 'something'
    h.cert_file = '/dev/null'
    h.key_file = '/dev/null'
    h.connect()


# Generated at 2022-06-13 04:46:03.877314
# Unit test for function fetch_url
def test_fetch_url():
    ''' Test fetch_url.py '''

    class TestModule(object):
        ''' mock object '''
        def __init__(self, params, tmpdir):
            self.params = params
            self.tmpdir = tmpdir

        def fail_json(self, msg, **kwargs):
            ''' mock fail_json '''
            self.msg = msg
            self.kwargs = kwargs

    # Test valid response
    module = TestModule({'url_username': '', 'url_password': '', 'use_gssapi': False}, '/tmp')
    try:
        r, info = fetch_url(module, 'http://httpbin.org/get', None, None, None, True, False, None, 10, None, None)
    except:
        assert False, 'Error getting %s' % info

# Generated at 2022-06-13 04:46:15.080069
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():

    """This function is called when this module is imported, and is used
    to check that the ``RedirectHandler`` is working as expected.
    """

    # Make sure the behavior of RedirectHandler matches that of
    # httplib2 for these values of follow_redirects
    for follow_redirects in [
        'all',
        'safe',
        'urllib2',
        'no',
        'none',
        '',
        False,
    ]:
        # We do this as a loop rather than a single test so that if anything
        # fails, we know exactly what value of follow_redirects caused the
        # failure.
        RedirectHandler = RedirectHandlerFactory(follow_redirects=follow_redirects)

        # Python 2-3.3
        # pylint: disable=E1123

# Generated at 2022-06-13 04:46:19.961629
# Unit test for method open of class Request
def test_Request_open():
    with pytest.raises(ValueError):
        req = Request('https')
        req.open(headers={1:2})
    req = Request('https')
    req.open(url='https://github.com', method='GET', headers={'a': 'b'}, use_proxy=True)
    req.open(url='https://github.com', method='GET', headers={'a': 'b'})
    req = Request(url='https://github.com', method='GET', headers={'a': 'b'})
    req.open()



# Generated at 2022-06-13 04:46:27.048525
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    """ Test that get_channel_binding_cert_hash returns a hash matching an example from RFC 5929 for a known test cert. """

    # The test cert is from https://tools.ietf.org/html/rfc5929#appendix-A

# Generated at 2022-06-13 04:47:32.066953
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():

    try:
        from ansible.tests.unit.compat.unittest import mock
    except Exception:
        import mock

    # Set up stub function for urllib2 to use
    urllib_request._opener.open = mock.Mock()
    urllib_request._opener.open.return_value.info.return_value = {}
    urllib_request._opener.open.return_value.getcode.return_value = 200

    # Test HTTP redirect
    handler = RedirectHandlerFactory(follow_redirects=True)
    redirect = handler.redirect_request(None, None, 302, 'Found', {}, 'http://localhost:8080/foo')
    assert redirect.get_full_url() == 'http://localhost:8080/foo'

    # Test HTTP redirect with payload
    handler

# Generated at 2022-06-13 04:47:42.628469
# Unit test for function generic_urlparse
def test_generic_urlparse():
    assert generic_urlparse(urlparse('http://foo:bar@localhost:8080/path?a=b&c=d#anchor')) == {
        'scheme': 'http',
        'netloc': 'foo:bar@localhost:8080',
        'path': '/path',
        'params': '',
        'query': 'a=b&c=d',
        'fragment': 'anchor',
        'username': 'foo',
        'password': 'bar',
        'hostname': 'localhost',
        'port': 8080,
    }

# Generated at 2022-06-13 04:47:54.063545
# Unit test for method http_request of class SSLValidationHandler
def test_SSLValidationHandler_http_request():
    try:
        # Check whether the connection to the url is allowed.
        url = 'https://www.mcs.anl.gov/~jqu/cgi-bin/echo'
        request = urllib.request.Request(url)
        request.add_header('User-Agent', 'Ansible')

        handler = SSLValidationHandler('www.mcs.anl.gov', 443)
        try:
            handler.http_request(request)
        except Exception:
            result = False

        # Check whether the connection to the url will be blocked.
        handler = SSLValidationHandler('www.google.com', 443)
        try:
            handler.http_request(request)
        except Exception:
            result = True
    except Exception:
        result = False


# Generated at 2022-06-13 04:48:00.481975
# Unit test for function rfc2822_date_string
def test_rfc2822_date_string():
    from datetime import datetime
    from pytz import timezone, utc
    def _test(local_time, expected_string):
        utc_dt = utc.localize(local_time)
        assert rfc2822_date_string(utc_dt.timetuple()) == expected_string, 'string: %s' % rfc2822_date_string(utc_dt.timetuple())

    _test(datetime(2001, 11, 9, 1, 8, 47), 'Fri, 09 Nov 2001 01:08:47 -0000')



# Generated at 2022-06-13 04:48:06.277806
# Unit test for method detect_no_proxy of class SSLValidationHandler
def test_SSLValidationHandler_detect_no_proxy():
    proxy_env_var_set = 'https_proxy=http://172.29.236.204:3128'
    url_excluded_from_proxy = 'https://github.com'
    url_excluded_from_proxy2 = 'https://gitlab.ics.com'
    url_matched_by_proxy = 'https://172.29.236.204'
    url_matched_by_proxy2 = 'https://172.29.236.204:3128'

    #check that if the proxy environment variable is not set the function returns always true
    assert SSLValidationHandler('host.name.com', 443).detect_no_proxy(url_excluded_from_proxy)

    #check that if the url is excluded from proxy the function returns false
    assert not SSLValidationHandler('host.name.com', 443).detect_

# Generated at 2022-06-13 04:48:18.562685
# Unit test for function maybe_add_ssl_handler
def test_maybe_add_ssl_handler():
    # very simple test, just to make sure it returns
    # good output for various inputs
    urls = [
        'https://www.ansible.com',
        'https://www.ansible.com:444',
        'https://www.ansible.com:444/index.html',
        'https://www.ansible.com/test/test.html',
        'https://www.ansible.com/test/test.html?foo=Foo&bar=Bar',
        ]
    for url in urls:
        res = maybe_add_ssl_handler(url, True)
        assert res.hostname == 'www.ansible.com'
        assert res.port == 444
        assert res.ca_path is None


# Generated at 2022-06-13 04:48:23.522169
# Unit test for function fetch_url
def test_fetch_url():
    class FakeModule:
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            print(args, kwargs)
            raise AssertionError(args, kwargs)

    module = FakeModule(url='https://stackoverflow.com/questions/5419204')

    resp, info = fetch_url(module, 'https://stackoverflow.com/questions/531397/')
    assert info['status'] == 200
    resp.close()

    resp, info = fetch_url(module, 'http://not.found/')
    assert info['status'] == 404

    resp, info = fetch_url(module, 'http://not.found/', use_proxy=False)
    assert info['status'] == 404

# Generated at 2022-06-13 04:48:31.682992
# Unit test for function get_channel_binding_cert_hash
def test_get_channel_binding_cert_hash():
    cert = base64.b64encode(b_DUMMY_CA_CERT)
    cert = base64.b64decode(cert)
    if get_channel_binding_cert_hash(cert) != b'm\x9b\xdb\x04\x96\x8d\x89\r\xbc\xa9\xdf\x9f\xc3\x17\x07\xeb44\xab\x1f\x7f\x81P9\x9fU\x80\xa7j\x99\x15\xfb\xe1\x1c\x15\xf7':
        raise Exception


# Generated at 2022-06-13 04:48:43.930110
# Unit test for function RedirectHandlerFactory
def test_RedirectHandlerFactory():
    import unittest

    class TestCases(unittest.TestCase):
        def test_follow_redirects_no(self):
            with self.assertRaises(urllib_error.HTTPError):
                RedirectHandlerFactory('no')

        def test_follow_redirects_none(self):
            with self.assertRaises(urllib_error.HTTPError):
                RedirectHandlerFactory('none')

        def test_follow_redirects_false(self):
            with self.assertRaises(urllib_error.HTTPError):
                RedirectHandlerFactory(False)

        def test_follow_redirects_all(self):
            with self.assertRaises(urllib_error.HTTPError):
                RedirectHandlerFactory('all')


# Generated at 2022-06-13 04:48:57.173692
# Unit test for function open_url
def test_open_url():
    http = requests.packages.urllib3.connectionpool('http')
    https = requests.packages.urllib3.connectionpool('https')
    request = urllib_request.Request
    if sys.version_info[0] == 2:
        http = urllib2.HTTPConnection('http')
        https = urllib2.HTTPSConnection('https')
        request = urllib2.Request
    else:
        http = urllib.request.HTTPConnection('http')
        https = urllib.request.HTTPSConnection('https')
        request = urllib.request.Request
    assert isinstance(open_url('http://httpbin.org/get'), http.response_class)