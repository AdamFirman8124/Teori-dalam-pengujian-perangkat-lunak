

# Generated at 2022-06-13 22:33:24.907212
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test')
    request_headers = {
        'Content-Type': 'application/json',
        'Content-Length': '13',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }
    session.update_headers(request_headers)
    assert session['headers'] == {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8'
    }

# Generated at 2022-06-13 22:33:31.550068
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('./test/session')
    name = ['X-API-KEY', 'api-key', 'X-API_KEY', 'x-api-key']
    value = ['1234567890', '0987654321', '1234567890', '0987654321']
    ss = {}
    for i, (n, v) in enumerate(zip(name, value)):
        s['headers'][n] = v
        ss[n] = v
    assert s['headers'] == ss
    s.update_headers(ss)
    assert s['headers'] == ss
    s['headers'].clear()
    name = ['Content-Length', ' If-Modified-Since', 'If-None-Match', 'X-CSRF-TOKEN']

# Generated at 2022-06-13 22:33:43.732678
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.compat import OrderedDict
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.plugins.registry import plugin_manager
    plugin_manager.init(config_dir=DEFAULT_CONFIG_DIR)

    s = Session(DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME / 'test_file.json')

    # <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>

# Generated at 2022-06-13 22:33:51.905322
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session')

    # test username and password in basic auth
    request_headers = RequestHeadersDict()
    request_headers['Authorization'] = 'Basic dXNlcjpwYXNzd29yZA=='
    session.update_headers(request_headers)
    assert session['auth']['type'] == 'basic'
    assert session['auth']['username'] == 'user'
    assert session['auth']['password'] == 'password'

    # test Bearer token
    request_headers['Authorization'] = 'Bearer a2V5'
    session.update_headers(request_headers)
    assert session['auth']['type'] == 'bearer'
    assert session['auth']['raw_auth'] == 'a2V5'

    # test token
    request_headers

# Generated at 2022-06-13 22:34:04.602165
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session')
    def test_update_headers(
        headers,
        headers_expected,
        cookies_expected,
    ):
        session.update_headers(RequestHeadersDict(headers))
        headers_actual = session.headers
        cookies_actual = session.cookies
        assert headers_actual == headers_expected
        for cookie in cookies_expected.keys():
            assert cookies_actual.get(cookie) == cookies_expected.get(cookie)
    # Test with an empty RequestHeadersDict
    test_update_headers({}, {}, {})
    # Test with a RequestHeadersDict containing only the "Content-Type" header
    test_update_headers(
        {'Content-Type': 'application/json'},
        {},
        {},
    )
    # Test with a RequestHead

# Generated at 2022-06-13 22:34:12.586766
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test.json')
    request_headers = RequestHeadersDict({'User-Agent': 'test', 'Cookie': 'foo=bar'})
    session.update_headers(request_headers)
    assert session.headers == RequestHeadersDict({'Cookie': 'foo=bar'})
    assert session.cookies.get_dict('.example.com') == {'foo': 'bar'}

# Generated at 2022-06-13 22:34:23.714998
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    # case 1
    session = Session(path = Path(config_dir) / SESSIONS_DIR_NAME / hostname / f'{session_name}.json')
    session['headers'] = {'Server': 'httpie'}
    session['cookies'] = {'name': 'httpie'}
    session['auth'] = {'type': 'basic', 'username': 'Saitama','password': 'one-punch'}
    request_headers = {'Server': 'httpie'}
    session.update_headers(request_headers)
    assert session['headers'] == {'Server': 'httpie'}
    assert session['cookies'] == {'name': 'httpie'}
    assert session['auth'] == {'type': 'basic', 'username': 'Saitama','password': 'one-punch'}

   

# Generated at 2022-06-13 22:34:31.727776
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/dummy/path')
    session['cookies']['key1'] = 'v1'
    session['cookies']['key2'] = 'v2'
    session['cookies']['key3'] = 'v3'
    assert session['cookies'] == {'key1': 'v1', 'key2': 'v2', 'key3': 'v3'}
    session.remove_cookies(['key1', 'key2', 'key4'])
    assert session['cookies'] == {'key3': 'v3'}

# Generated at 2022-06-13 22:34:37.965027
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('~/.httpie/sessions/test_session')
    session.update_headers({
        'A': 'a',
        'Cookie': 'test_cookie=test_value',
        'Content-Type': 'text/plain'
    })
    assert session.headers == {
        'A': 'a'
    }
    assert session.cookies == {
        'test_cookie': 'test_value'
    }

# Generated at 2022-06-13 22:34:48.119557
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(''))
    session.cookies = {
        'somedomain.com/path': [
            ('one', '1'), ('two', '2'), ('three', '3')
        ]
    }

    removed_cookies = ['one', 'two']
    session.remove_cookies(removed_cookies)

    cookies = session.cookies
    assert len(cookies) == 1
    assert list(cookies) == ['somedomain.com/path']
    assert len(cookies['somedomain.com/path']) == 1
    assert cookies['somedomain.com/path'][0] == ('three', '3')

# Generated at 2022-06-13 22:35:03.942441
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from os import makedirs
    from tempfile import NamedTemporaryFile
    from httpie.config import DEFAULT_CONFIG_DIR
    DEFAULT_SESSIONS_DIR = DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME
    if not DEFAULT_SESSIONS_DIR.exists():
        makedirs(DEFAULT_SESSIONS_DIR)

    with NamedTemporaryFile(delete=False, mode='w+', dir=DEFAULT_SESSIONS_DIR) as temp:
        temp.write("{}")
        temp.flush()
        session = Session(temp.name)
        session.load()
        session['cookies'] = {'cookie1': '1', 'cookie2': '2', 'cookie3': '3'}
        session.save()


# Generated at 2022-06-13 22:35:12.644494
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session')
    session['cookies']['cookie1'] = {'value': 'value1'}
    session['cookies']['cookie2'] = {'value': 'value2'}
    session['cookies']['cookie3'] = {'value': 'value3'}
    session.remove_cookies(('cookie1', 'cookie3'))
    assert session['cookies']['cookie2'] == {'value': 'value2'}

# Generated at 2022-06-13 22:35:21.115145
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Create a session
    path = Path('./tests/sessions/httpbin.org/session_test.json')
    session = Session(path)
    session.load()
    # Check the session
    assert 'cookies' in session.dict
    assert len(session['cookies']) == 1
    assert '_gauges_unique_hour' in session['cookies']
    # Remove the cookie '_gauge_unique_hour'
    session.remove_cookies(['_gauges_unique_hour'])
    # Check the session
    assert 'cookies' not in session.dict

# Generated at 2022-06-13 22:35:33.370714
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import RequestHeadersDict
    session = Session('/path')
    session.update_headers(RequestHeadersDict({
        'A': 'a',
        'B': 'b',
        'Content-Type': 'application/json',
        'If-Modified-Since': '1',
        'Cookie': 'a=b; c=d',
    }))
    assert session['headers'] == {'A': 'a', 'B': 'b'}
    assert session['cookies'] == {
        'a': {'value': 'b'},
        'c': {'value': 'd'},
    }

# Generated at 2022-06-13 22:35:38.823745
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_session.json')
    session['cookies'] = {'cook1': {'value': 'value1'}, 'cook2': {'value': 'value2'}}
    session.remove_cookies(['cook1'])
    assert 'cook1' not in session['cookies']
    assert 'cook2' in session['cookies']

# Generated at 2022-06-13 22:35:51.141260
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    from httpie.cli.argtypes import KeyValueArgType

    headers = RequestHeadersDict()
    session = Session(path='')
    Session.update_headers(session, headers)
    assert session == Session(path='')

    headers = RequestHeadersDict([
        ('foo', 'bar'),
        ('Authorization', 'Basic abcdef'),
        ('content-type', 'application/json'),
        ('Content-Length', '12345')
    ])
    session = Session(path='')

    Session.update_headers(session, headers)

    # After update, the session must have all headers except the ones
    # ignored.
    assert session == Session(path='')
    assert session['headers'] == {'Authorization': 'Basic abcdef', 'foo': 'bar'}

    # cookies header must be

# Generated at 2022-06-13 22:35:55.902821
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("Session_test.json")
    s.cookies = RequestsCookieJar()
    s.cookies.set_cookie(create_cookie('cookie1', 'value1'))
    s.cookies.set_cookie(create_cookie('cookie2', 'value2'))
    s.cookies.set_cookie(create_cookie('cookie3', 'value3'))
    s.remove_cookies(['cookie1','cookie2'])
    assert len(s.cookies) == 1
    assert next(iter(s.cookies)).name == 'cookie3'



# Generated at 2022-06-13 22:36:01.829485
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {
        'name1' : 'value1',
        'name2' : 'value2',
    }
    session = Session('test')
    session['cookies'] = cookies

    session.remove_cookies(['name1'])

    assert len(session['cookies']) == 1
    assert 'name2' in session['cookies']



# Generated at 2022-06-13 22:36:08.318776
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_remove_cookies.json')
    session['cookies'] = {'foo': None, 'bar': None}
    session.remove_cookies(['foo'])
    session.save()
    assert session['cookies'] == {'bar': None}


# Generated at 2022-06-13 22:36:14.782698
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict({'Content-Type':b'test', 'Cookie':b'test'})
    session = Session(path = "test")
    session.update_headers(request_headers)
    assert session.headers == RequestHeadersDict({'Content-Type':b'test'})

# Generated at 2022-06-13 22:36:25.634688
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # create session object
    path = '~/file.json'
    session = Session(path)

    # load cookies if they haven't been loaded
    if not session['cookies']:
        session.load()

    # test
    session.remove_cookies(['cook1', 'cook2'])
    assert session['cookies'] == {'cook3': 'val3'}

    session.remove_cookies(['cook3'])
    assert session['cookies'] == {}

    session.remove_cookies(['cook4'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:36:34.809994
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_sessions')
    session.load()
    session.cookies = dict()
    session['cookies'] = {'test1': {'value': 'test1value'}, 'test2': {'value': 'test2value'}, 'test3': {'value': 'test3value'}}
    assert session['cookies'] == {'test1': {'value': 'test1value'}, 'test2': {'value': 'test2value'}, 'test3': {'value': 'test3value'}}
    session.remove_cookies(['test1'])
    assert session['cookies'] == {'test2': {'value': 'test2value'}, 'test3': {'value': 'test3value'}}

# Generated at 2022-06-13 22:36:42.297955
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Tests for removing all cookies for given names from the session,
    when cookies are present for the given names.
    """
    session = Session(path=Path('tmp'))
    cookie_names = ['csrftoken', 'sessionid']
    session['cookies'] = {
        cookie_name: {'value': 'testing'}
        for cookie_name in cookie_names
    }
    session.remove_cookies(cookie_names)
    assert len(session['cookies']) == 0


# Generated at 2022-06-13 22:36:48.758472
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("Test")
    s['cookies']['cookie1'] = {'value': 'value1'}
    s['cookies']['cookie2'] = {'value': 'value2'}
    # cookies before remove
    assert len(s['cookies']) == 2
    s.remove_cookies(['cookie2', 'cookie3'])
    # cookies after remove
    assert len(s['cookies']) == 1
    assert 'cookie1' in s['cookies']
    assert 'cookie2' not in s['cookies']
    assert 'cookie3' not in s['cookies']

# Generated at 2022-06-13 22:36:51.887772
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("")
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(['b', 'd'])
    assert s['cookies'] == {'a': 1, 'c': 3}

# Generated at 2022-06-13 22:36:59.825503
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    import pytest

    session_headers = Session.headers
    session_headers.clear()
    request_headers = RequestHeadersDict({
        'Accept': 'application/json',
        'Content-Type': 'text/html; charset=UTF-8',
        'Content-Length': '0',
        'Cookie': 'foo=bar; baz=qux',
        'If-Match: *': None,
        'If-Unmodified-Since: Thu, 05 Apr 2012 15:46:37 GMT': None
    })
    Session.update_headers(session_headers, request_headers)
    assert session_headers == {
        'Accept': 'application/json',
        'Content-Type': 'text/html; charset=UTF-8',
        'Cookie': 'foo=bar; baz=qux'
    }

# Generated at 2022-06-13 22:37:10.218380
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path=None)

# Generated at 2022-06-13 22:37:17.970168
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('filepath')
    test_session['cookies'] = {
            'cookie1': {'value': 'aaaaa'},
            'cookie2': {'value': 'bbbbb'}
        }
    test_session.remove_cookies({'cookie1'})
    assert test_session['cookies'] == {
            'cookie2': {'value': 'bbbbb'}
        }

# Generated at 2022-06-13 22:37:24.153141
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {'a': '1', 'b': '2', 'c': '3'}
    s.remove_cookies(['a', 'b'])
    assert s['cookies'] == {'c': '3'}

# Generated at 2022-06-13 22:37:28.544514
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(DEFAULT_SESSIONS_DIR)
    cookie1 = create_cookie('foo', 'bar')
    cookie2 = create_cookie('baz', 'quux')
    session.cookies.set_cookie(cookie1)
    session.cookies.set_cookie(cookie2)
    assert 'foo' in session.cookies
    assert 'baz' in session.cookies
    session.remove_cookies(['foo', 'quux'])
    assert 'foo' not in session.cookies
    assert 'baz' in session.cookies

# Generated at 2022-06-13 22:37:50.929692
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    '''
    Test for Session.remove_cookies
    '''
    cookies = {
        'a': {'value': 'a_value'},
        'b': {'value': 'b_value'}
    }
    s = Session(path='path')
    s['cookies'] = cookies

    s.remove_cookies(['a'])
    # Assert cookies after remove cookies 'a'
    assert s['cookies'] == {'b': {'value': 'b_value'}}
    # Clear cookies
    s.remove_cookies(['a', 'b'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:37:54.892501
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("path")
    session["cookies"] = {"a": 1}
    #assert that a is in the session
    assert "a" in session["cookies"]
    session.remove_cookies(["a"])
    #assert that a has been removed
    assert "a" not in session["cookies"]

# Generated at 2022-06-13 22:37:58.418509
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session_remove_cookies.json')

    cookie_name = 'test_Session_remove_cookies'
    session['cookies'][cookie_name] = {'value': cookie_name}

    session.remove_cookies([cookie_name])

    assert cookie_name not in session['cookies']

# Generated at 2022-06-13 22:38:05.159203
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('file.name')
    sess.update({
        'cookies': {
            'one': 'something',
            'two': 'something',
            'three': 'something'
        }
    })
    sess.remove_cookies(['one', 'three'])
    assert sess['cookies'] == {'two': 'something'}

# Generated at 2022-06-13 22:38:11.278937
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='/test/sessions/test_session.json')
    session['cookies'] = {'name': 'value', 'name2': 'value2', 'name3': 'value3'}
    session.remove_cookies(names=['name', 'name3'])
    assert session['cookies'] == {'name2': 'value2'}


# Generated at 2022-06-13 22:38:14.937721
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session['cookies'] = {'a': {'value': '1'}, 'b': {'value': '2'}}
    session.remove_cookies(['a'])
    assert session['cookies'] == {'b': {'value': '2'}}

# Generated at 2022-06-13 22:38:20.135509
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'testcookies': {'testvalue': 'test', 'test': 'test'}}
    session.remove_cookies(['testcookies'])
    assert not session.cookies


# Generated at 2022-06-13 22:38:25.485575
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/s.json')
    s['cookies'] = {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    s.remove_cookies(['c2', 'c3'])
    assert s['cookies'] == {'c1': {'value': 'v1'}}

# Generated at 2022-06-13 22:38:36.801574
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('./sessions/test_session_remove_cookies.json')
    if path.exists():
        path.unlink()
    if not path.parent.exists():
        path.parent.mkdir(mode=0o777)

    session = Session(path=path)

# Generated at 2022-06-13 22:38:46.870662
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test")
    session["cookies"] = {}
    session["cookies"]["cookie1"] = "cookie_value1"
    session["cookies"]["cookie2"] = "cookie_value2"
    session["cookies"]["cookie3"] = "cookie_value3"
    assert len(session["cookies"]) == 3
    assert session["cookies"]["cookie1"] == "cookie_value1"
    assert session["cookies"]["cookie2"] == "cookie_value2"
    assert session["cookies"]["cookie3"] == "cookie_value3"
    session.remove_cookies(["cookie2"])
    assert len(session["cookies"]) == 2
    assert session["cookies"]["cookie1"] == "cookie_value1"

# Generated at 2022-06-13 22:39:08.733826
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('some_dummy_name')
    s['cookies'] = {'a': {'value': '1'}, 'b': {'value': '2'}}
    s.remove_cookies(['b'])
    assert s['cookies'] == {'a': {'value': '1'}}

# Generated at 2022-06-13 22:39:16.960706
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {
        'name1': {'value': 'value1', 'path': '/path1'},
        'name2': {'value': 'value2', 'path': '/path2'},
        'name3': {'value': 'value3', 'path': '/path3'}
    }
    session = Session(Path('./test.json'))
    session['cookies'] = cookies
    session.remove_cookies(['name1', 'name3'])

    new_cookies = session['cookies']
    assert set(new_cookies.keys()) == set(['name2'])
    assert new_cookies['name2'] == cookies['name2']

# Generated at 2022-06-13 22:39:23.665431
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies']['cookie1'] = 'cookie1'
    s['cookies']['cookie2'] = 'cookie2'
    s.remove_cookies(['cookie2'])
    assert set(s['cookies']) == {'cookie1'}

# Generated at 2022-06-13 22:39:28.040745
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('./config/hostname.json'))
    session.load()
    session.remove_cookies(['cookie1', 'cookie2'])

    # Check if cookies are removed
    assert session['cookies'] == {'cookie3': {'value': 'value3'}}

# Generated at 2022-06-13 22:39:34.262479
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("/tmp/test_jsonsession")
    cookies = {'foo': 'bar', 'baz': 'qux'}
    session['cookies'] = cookies
    session.remove_cookies(['baz', 'foobar'])
    assert session['cookies'] == {'foo': 'bar'}

# Generated at 2022-06-13 22:39:41.252432
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.input.utils import MockEnvironment
    from httpie.plugins.core import CorePlugin

    env = MockEnvironment(stdin_isatty=True,
                          stdin=b'',
                          stdout_isatty=True)
    config = CorePlugin().get_config(env)

    # Test Case 1: Session exists
    session_path = 'tests/fixtures/sessions/test_Session_remove_cookies.json'
    session = get_httpie_session(config.dir, session_path, None, '')
    session.remove_cookies(['cookie1'])
    session.save()
    session = get_httpie_session(config.dir, session_path, None, '')
    assert 'cookie1' not in session['cookies']

# Generated at 2022-06-13 22:39:48.697361
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from http.cookies import SimpleCookie
    from requests.cookies import RequestsCookieJar, create_cookie

    sess = Session('foo')
    cookie1 = SimpleCookie()
    cookie1['foo'] = 'bar'
    cookie2 = SimpleCookie()
    cookie2['bar'] = 'baz'

    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie('foo', 'bar'))
    jar.set_cookie(create_cookie('bar', 'baz'))

    assert not sess['cookies']
    sess.cookies = jar
    assert sess['cookies']

    sess.remove_cookies(['foo'])
    assert 'foo' not in sess['cookies']
    sess.remove_cookies(['bar'])

# Generated at 2022-06-13 22:39:56.492238
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    config_dir = Path("/tmp")
    session_name = "test_Session_remove_cookies"
    url = "http://test.com"
    session = get_httpie_session(config_dir, session_name, None, url)
    request_headers = RequestHeadersDict({'X-Test-Header': "abc"})
    session.update_headers(request_headers)
    session.remove_cookies(["X-Test-Header"])
    assert session['cookies'] is None

# Generated at 2022-06-13 22:40:01.876556
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = { 'cookie1': {}, 'cookie2': {}, 'cookie3': {} }
    s.remove_cookies(['cookie2'])
    assert s['cookies'] == { 'cookie1': {}, 'cookie3': {} }


# Generated at 2022-06-13 22:40:11.743239
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('dummy.json')
    s.cookies = RequestsCookieJar()
    s.cookies.set('name1', 'value1')
    s.cookies.set('name2', 'value2')
    s.cookies.set('name3', 'value3')
    s.cookies.set('name4', 'value4')
    assert len(s.cookies) == 4
    s.remove_cookies(['name1', 'name3'])
    assert len(s.cookies) == 2
    assert list(s.cookies.keys()) == ['name2', 'name4']


# Generated at 2022-06-13 22:40:57.175087
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('http_session')
    s['cookies'] = {'cookie1':'abc', 'cookie2':'def', 'cookie3':'ghi'}
    s.remove_cookies({'cookie2'})
    assert s['cookies'] == {'cookie1':'abc', 'cookie3':'ghi'}, 'remove_cookies() did not work as expected'
    s = Session('http_session')
    s['cookies'] = {'cookie1':'abc', 'cookie2':'def', 'cookie3':'ghi'}
    s.remove_cookies({'cookie1','cookie3'})
    assert s['cookies'] == {'cookie2':'def'}, 'remove_cookies() did not work as expected'


# Generated at 2022-06-13 22:41:02.489230
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    name = 'test'
    session = Session(Path('test_session.json'))

    session['cookies'] = {}
    session.remove_cookies([name])
    assert name not in session['cookies']

    session['cookies'][name] = {}
    session.remove_cookies([name])
    assert name not in session['cookies']

# Generated at 2022-06-13 22:41:08.153540
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/')
    s['headers'] = {}
    s['cookies'] = {'a': {'value': '1'}, 'b': {'value': '2'}}
    s.remove_cookies(['a'])
    assert s['cookies'] == {'b': {'value': '2'}}, \
        'Cookies must be removed'
    s._load_file()
    assert s['cookies'] == {}, \
        'Cookies must be cleared if file doesn\'t exist'


# Generated at 2022-06-13 22:41:13.578198
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Arrange
    session = Session(Path(""))
    session['cookies'] = {'abc': 'xyz', 'bcd': 'xyz', 'def': 'xyz'}

    # Act
    session.remove_cookies(['abc', 'cde'])

    # Assert
    assert 'abc' not in session['cookies']
    assert 'bcd' in session['cookies']
    assert 'def' in session['cookies']
    assert len(session['cookies']) == 2



# Generated at 2022-06-13 22:41:20.201718
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s['cookies'] = {'test': {'test1': 'test', 'test2': 'test'}}
    s['cookies']['test2'] = {'test1': 'test', 'test2': 'test'}
    s.remove_cookies(['test', 'test2'])
    assert (s['cookies'] == {})


# Generated at 2022-06-13 22:41:22.981288
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('0')
    session['cookies'] = {'foo': 'bar', 'baz': 'qux'}
    session.remove_cookies(('foo', 'baz'))
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:41:34.409187
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import copy
    import tempfile
    import shutil

    test_fold = copy.deepcopy(SESSIONS_DIR_NAME)
    with tempfile.TemporaryDirectory() as tmpfolder:
         new_fold = os.path.join(tmpfolder, test_fold)
         os.makedirs(new_fold)

         example_path = os.path.join(tmpfolder, "example.json")
         session = Session(example_path)
         session.load()

         session['cookies'] = {}
         session['cookies'] = {'name': {'value': 'value'}}

         session.remove_cookies({'name'})
         assert 'name' not in session['cookies'], "cookies are not removed"

# Generated at 2022-06-13 22:41:43.054582
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from nose.tools import assert_equal
    from requests.cookies import RequestsCookieJar

    session = Session('./sessions/test.json')

    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie(
        'foo', 'bar', **{'path': '/', 'expires': 100}
    ))
    jar.set_cookie(create_cookie(
        'bar', 'foo', **{'path': '/', 'expires': 100}
    ))

    session.cookies = jar

    assert_equal(list(session['cookies'].keys()), ['foo', 'bar'])
    session.remove_cookies(['foo'])
    assert_equal(list(session['cookies'].keys()), ['bar'])
    session.remove_cookies(['bar'])


# Generated at 2022-06-13 22:41:52.512665
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("../cookie.txt")
    session['cookies']['a'] = 1
    session['cookies']['b'] = 2
    session['cookies']['c'] = 3
    session['cookies']['d'] = 4
    session['cookies']['e'] = 4
    session['cookies']['f'] = 4
    session.remove_cookies(['b','e'])
    assert session['cookies'] == {'a':1,'c':3,'d':4,'f':4}

# Generated at 2022-06-13 22:42:02.047567
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie = RequestsCookieJar()
    cookie.set_cookie(create_cookie('SID', '123'))
    cookie.set_cookie(create_cookie('www.example.com', 'id', '123'))

    session = Session(None)
    session.cookies = cookie
    assert 'SID' in session
    assert 'www.example.com' in session
    session.remove_cookies(['SID', 'www.example.com'])
    assert 'SID' not in session
    assert 'www.example.com' not in session

    session.cookies = cookie
    assert 'SID' in session
    assert 'www.example.com' in session
    session.remove_cookies(['SID'])
    assert 'SID' not in session
    assert 'www.example.com' in session