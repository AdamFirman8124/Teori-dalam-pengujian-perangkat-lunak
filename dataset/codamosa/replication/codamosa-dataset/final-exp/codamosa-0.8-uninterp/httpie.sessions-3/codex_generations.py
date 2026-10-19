

# Generated at 2022-06-13 22:33:28.581941
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('temp.json')
    session.update_headers({'key': 'value'})
    assert(session['headers'] == {'key': 'value'})
    session.update_headers({'key': 'value2'})
    assert(session['headers'] == {'key': 'value2'})
    session.update_headers({'key': None})
    assert(session['headers'] == {})
    session.update_headers({'key': 'value'})
    session.update_headers({'key': 'value'})
    assert(session['headers'] == {'key': 'value'})
    session.update_headers({'key': 'value'})
    session.update_headers({'key': 'value2'})
    assert(session['headers'] == {'key': 'value2'})

# Generated at 2022-06-13 22:33:40.214586
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    input_cookies = "__cfduid=d8f6e5cd638fd9df85c4d7f8c25aa80e71568485094"
    input_headers = {'Content-Type':'application/json; charset=utf-8', 'Cookie': input_cookies}
    session = Session('sessions/session1.json')
    session.update_headers(input_headers)
    assert session['headers'] == {'Content-Type':'application/json; charset=utf-8'}
    assert session['cookies']['__cfduid']['value'] == 'd8f6e5cd638fd9df85c4d7f8c25aa80e71568485094'

# Generated at 2022-06-13 22:33:47.003331
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(DEFAULT_SESSIONS_DIR / 'test.json')

# Generated at 2022-06-13 22:33:56.850522
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Session stores headers, cookies, auths
    session = Session("test_file")
    headers = {"content-type": "text/html"}
    session.update_headers(headers)
    # HTTPie header's prefix isn't in SESSION_IGNORED_HEADER_PREFIXES
    assert "content-type" in session['headers'].keys()
    # HTTPie header's prefix is in SESSION_IGNORED_HEADER_PREFIXES
    headers = {"If-Modified-Since": "Wed, 11 Jan 2006 18:40:39 GMT"}
    session.update_headers(headers)
    assert "If-Modified-Since" not in session['headers'].keys()

# Generated at 2022-06-13 22:34:02.674170
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.output.streams import get_stderr
    from httpie.output.util import get_terminal_size_fallback
    from httpie.compat import urlencode
    from httpie.__main__ import get_response
    from requests import Response
    from httpie.downloads import Downloader
    from httpie.context import Environment

    config = {}
    stdin_isatty = False
    stdin = None
    output_options = {}

    config_dir = DEFAULT_CONFIG_DIR

    # create a url to execute an HTTP request
    url = "%s" % "httpbin.org/post"

    # create a session
    session_name = "test"
    host = None
    session = get_httpie_session

# Generated at 2022-06-13 22:34:08.496727
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(None)
    request_headers = RequestHeadersDict()
    request_headers.append('Content-Type', 'application/json')
    request_headers.append('Content-Length', '0')
    request_headers.append('User-Agent', 'HTTPie/0.9.9')

    session.update_headers(request_headers)
    print(session.headers)

# Generated at 2022-06-13 22:34:18.092223
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path='./default.json')
    headers = RequestHeadersDict( {
        'Host': 'www.zslwh.com',
        'User-Agent': 'curl/7.58.0',
        'Accept': '*/*',
        'Cookie': 'PHPSESSID=ajkv124k5jnr0e67pb44ktbe50',
    })

    session.update_headers(headers)
    print(session.headers)
    print(session.cookies)


if __name__ == "__main__":
    test_Session_update_headers()

# Generated at 2022-06-13 22:34:22.620050
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(None)
    sess['cookies'] = {'one': 1, 'two': 2, 'three': 3}
    sess.remove_cookies(['one', 'two'])
    assert sess['cookies'] == {'three' : 3}



# Generated at 2022-06-13 22:34:31.065145
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/test-Session-update_headers.json')
    request_headers = RequestHeadersDict({
        'Accept': 'text/html, application/xml',
        'Accept-Language': 'en-US',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Length': '88',
        'Cookie': 'foo=bar',
        'User-Agent': 'Mozilla/5.0'
    })
    session.update_headers(request_headers)

    assert session['headers'] == {
        'Accept': 'text/html, application/xml',
        'Accept-Language': 'en-US',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0'
    }

# Generated at 2022-06-13 22:34:40.300319
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    session.update_headers({'header1': 'value1', 'header2': 'value2'})
    assert ('header1', 'value1') in session.headers.items()
    assert ('header2', 'value2') in session.headers.items()

    session = Session('')
    session.update_headers({'cooKie': 'Cookie1=value1; Cookie2=value2'})
    assert ('Cookie1', 'value1') in session.cookies.items()
    assert ('Cookie2', 'value2') in session.cookies.items()
    assert len(session.headers) == 0

    session = Session('')
    session.update_headers({'Content-Length': '100', 'If-Modified-Since': '10/28/08'})

# Generated at 2022-06-13 22:34:47.806985
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict()
    request_headers['Content-Length'] = '0'
    session = Session(Path('/home/mh/.httpie/sessions/session-name.json'))
    session.load()
    session.update_headers(request_headers)

    # Output the result
    print(session.headers)

# Generated at 2022-06-13 22:35:01.309858
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
        s = Session(Path(__file__))
        s.update_headers({'cookie': 'session=lorem; session2=ipsum'})
        cookie_jar = s.cookies
        assert len(cookie_jar) == 2
        s.remove_cookies(['session','session2'])
        cookie_jar = s.cookies
        assert len(cookie_jar) == 0
        s.update_headers({'cookie': 'session=lorem; session2=ipsum'})
        cookie_jar = s.cookies
        assert len(cookie_jar) == 2
        s.remove_cookies(['session'])
        cookie_jar = s.cookies
        assert len(cookie_jar) == 1
        s.remove_cookies(['session2'])
        cookie_jar = s.cookies

# Generated at 2022-06-13 22:35:04.528206
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    input = {'foo': 'bar', 'baz': 'qux'}
    session = Session('/path/to/session')
    session.update_headers(input)
    assert session['headers'] == input



# Generated at 2022-06-13 22:35:11.000235
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    Session1 = Session('my_session')
    Session1['cookies'] = {'c1':{'value':'v1'},'c2':{'value':'v2'}}
    Session1.remove_cookies(['c1'])
    assert Session1['cookies'] == {'c2':{'value':'v2'}}

# Generated at 2022-06-13 22:35:17.806506
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path.cwd() / 'session.json')
    session.update_headers({'Cookie': 'username=mrsj; age=32; gender=m'})
    session.remove_cookies(['age'])
    jar = session.cookies
    assert {'username': 'mrsj', 'gender': 'm'} == {
        cookie.name: cookie.value for cookie in jar
    }

# Generated at 2022-06-13 22:35:27.166713
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # create a new session
    session = Session('http://localhost')
    session['cookies'] = {
        'YII_CSRF_TOKEN': {'value': 'a'},
        'foo': {'value': 'b'},
        'bar': {'value': 'c'},
    }
    # remove a cookie
    session.remove_cookies(['YII_CSRF_TOKEN'])
    assert 'YII_CSRF_TOKEN' not in session['cookies']
    # remove multiple cookies
    session.remove_cookies(['foo', 'bar'])
    assert 'foo' not in session['cookies']
    assert 'bar' not in session['cookies']
    assert len(session['cookies']) == 0


# Generated at 2022-06-13 22:35:32.712341
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(None)
    s.update_headers({'A':'a','B':'c'})
    s.update_headers({'A':None})
    print(s)
    print('----')
    s.update_headers({'Cookie':'a=b;c=d'})
    print(s)

# Generated at 2022-06-13 22:35:38.538930
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'cookie1': {}, 'cookie2': {}, 'cookie3': {}}
    cookies_to_remove = ['cookie1', 'cookie3']

    session = Session('')
    session['cookies'] = cookies
    session.remove_cookies(cookies_to_remove)

    assert session['cookies'] == {'cookie2': {}}

# Generated at 2022-06-13 22:35:42.683388
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session.update({'cookies': {'test': '12'}})
    session.remove_cookies(['test', 'test2'])
    assert not session['cookies']

# Generated at 2022-06-13 22:35:50.036041
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    # Create a Session object
    path = "./httpie.json"
    session = Session(path=path)

    # yield {name, cookie_dict}
    cookie_dict = {name, cookie_dict}

    # save the session
    session.save()

    # remove cookies
    session.remove_cookies(['name'])

    # save the session
    session.save()

# Generated at 2022-06-13 22:36:07.916825
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import requests
    from httpie.session import Session
    from httpie.plugins import builtin
    from httpie.plugins.builtin import session

    uri = 'https://httpbin.org'

    # set up session
    s = Session('/tmp/test.json')
    s.update_headers(session.headers)
    s.cookies = session.cookies

    # make a test request with session, which will set cookies in the session
    r = requests.get(uri, headers=s.headers, cookies=s.cookies)
    s.cookies = r.cookies

    # remove cookies from session
    s.remove_cookies(['foo', 'baz'])

    # create a new session with the same path, which should read the removed cookies
    t = Session('/tmp/test.json')

# Generated at 2022-06-13 22:36:14.664095
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {'biscuit': {}, 'cookie': {}}
    session.remove_cookies(['cookie'])
    assert not 'cookie' in session['cookies']
    assert 'biscuit' in session['cookies']



# Generated at 2022-06-13 22:36:22.331174
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/1')
    s['cookies'] = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
    s.remove_cookies(['k1', 'k2'])
    assert 'k1' not in s['cookies']
    assert 'k2' not in s['cookies']
    assert 'k3' in s['cookies']
    s.remove_cookies(['k3'])
    assert 'k3' not in s['cookies']

# Generated at 2022-06-13 22:36:32.839781
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = {
        'Host': 'google.com',
        'Content-Length': 6,
        'Content-Type': 'text/html',
        'Accept-Encoding': 'compress, gzip',
        'User-Agent': 'HTTPie/2.2.0',
        'Cookie': 'SID=31d4d96e407aad42',
        'If-None-Match': 'W/"abc"'
    }
    session = Session(path=Path('./test.json'))
    session.update_headers(request_headers)
    assert session['headers']['Host'] == 'google.com'
    assert 'Content-Length' not in session['headers']
    assert 'Content-Type' not in session['headers']

# Generated at 2022-06-13 22:36:44.659982
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session()
    session.update_headers(RequestHeadersDict(
        {'User-Agent': 'HTTPie/0.9.2',
         'Cookie': 'a=1; b=2; c=3'}))
    assert session.headers['User-Agent'] == 'HTTPie/0.9.2'
    assert session.cookies['a'].value == '1'
    assert session.cookies['b'].value == '2'
    assert session.cookies['c'].value == '3'


# Generated at 2022-06-13 22:36:52.370505
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test")
    assert session['cookies'] == {}

    session['cookies']['a'] = {'value': 1}
    session['cookies']['b'] = {'value': 2}
    session['cookies']['c'] = {'value': 3}
    assert session['cookies'] == {'a': {'value': 1}, 'b': {'value': 2}, 'c': {'value': 3}}

    session.remove_cookies(['a', 'b'])
    assert session['cookies'] == {'c': {'value': 3}}

# Generated at 2022-06-13 22:36:58.100375
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('test/sessions/test.json')
    sess['cookies'] = {}
    sess['cookies']['foo'] = 'bar'
    sess['cookies']['boo'] = 'far'
    sess.remove_cookies(['foo'])
    print (sess['cookies'])
#test_Session_remove_cookies()

# Generated at 2022-06-13 22:37:07.306693
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session()
    session.update_headers({"lin": "lin", "duan": "duan"})
    assert session["headers"] == {"lin": "lin", "duan": "duan"}
    session.update_headers({"duan": "duan", "xin": "xin"})
    assert session["headers"] == {"lin": "lin", "duan": "duan", "xin": "xin"}
    session.update_headers({"lin": None, "duan": "duan"})
    assert session["headers"] == {"duan": "duan", "xin": "xin"}


# Generated at 2022-06-13 22:37:11.140203
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session1 = Session()
    session1['cookies'] = {'cookie_name_1': 'cookie_value_1',
                           'cookie_name_2': 'cookie_value_2'}
    session1.remove_cookies(['cookie_name_2'])
    assert session1['cookies'] == {'cookie_name_1': 'cookie_value_1'}



# Generated at 2022-06-13 22:37:16.963803
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/test/path')
    session['cookies'] = {'test': 'test', 'test1': 'test1'}
    session.remove_cookies(['test'])
    assert 'cookies' not in session.keys() or 'test' not in session['cookies'].keys()

# Generated at 2022-06-13 22:37:40.259913
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(
        path=Path.home() / '.config/httpie/sessions/localhost/test.json')
    session_headers = {
        'Cookie': ['id=111'],
        'Content-Type': ['application/json;charset=utf-8'],
        'If-None-Match': ['*']
    }
    request_headers = {
        'Cookie': ['id=222'],
        'Content-Type': ['application/json;charset=utf-8'],
        'User-Agent': ['HTTPie/0.9.6'],
        'If-None-Match': ['*']
    }
    session.update_headers(request_headers)
    assert session_headers == session.headers

# Generated at 2022-06-13 22:37:47.353446
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("tests/fixtures/session.json")
    assert 'c_cookie' in session['cookies']
    assert 'csrf_token' in session['cookies']
    del session['cookies']['c_cookie']
    del session['cookies']['csrf_token']
    assert not session['cookies']
    assert session['headers']

# Generated at 2022-06-13 22:37:52.982540
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("path")
    cookie_dict = {
        'cookies': {
            'some_cookie': None,
            'some_other_cookie': None
        }
    }
    session.update(cookie_dict)
    names = {
        'some_cookie',
        'some_other_cookie'
    }
    session.remove_cookies(names)
    assert {} == session['cookies']

test_Session_remove_cookies()

# Generated at 2022-06-13 22:37:59.194968
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #Test for Session_remove_cookies()
    a = Session('abc')
    a.cookies = RequestsCookieJar()
    a.cookies.set('test', '123', path='/bar')
    a.cookies.set('b', '123', path='/bar')
    a.cookies.set('c', '123', path='/bar')
    a.cookies.set('d', '123', path='/bar')
    a.cookies.set('e', '123', path='/bar')
    a.cookies.set('f', '123', path='/bar')
    a.cookies.set('g', '123', path='/bar')
    a.cookies.set('h', '123', path='/bar')

# Generated at 2022-06-13 22:38:05.479999
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/test.json')
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(['a', 'c'])
    assert len(s['cookies']) == 1
    assert s['cookies']['b'] == 2

# Generated at 2022-06-13 22:38:08.267734
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = {}
    session = Session(path=None)
    session.update_headers(headers)
    assert session.headers == {}



# Generated at 2022-06-13 22:38:17.418427
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Set up a Session
    config_dir = DEFAULT_SESSIONS_DIR
    session_name = 'test'
    host = 'github.com'
    url = 'http://github.com'
    session = get_httpie_session(config_dir, session_name, host, url)
    # Set up a request_headers
    request_headers = RequestHeadersDict()
    request_headers['content-type'] = 'application/json'
    request_headers['if-modified-since'] = '01-01-01'
    request_headers['X-Request-Id'] = '01-01-01'
    # Update the session headers with the request headers
    session.update_headers(request_headers)
    # Set up a new headers dict
    headers = dict(session['headers'])
    headers_dict = dict

# Generated at 2022-06-13 22:38:27.557637
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    '''
    Test for method remove_cookies of class Session.
    '''
    s = Session("test.json")
    s['headers'] = {}
    s['cookies'] = {}
    s['cookies']['test1'] = {'value': "test1"}
    s['cookies']['test2'] = {'value': "test2"}
    s['cookies']['test3'] = {'value': "test3"}
    names = ["test1","test3","test4"]
    s.remove_cookies(names)
    assert len(s['cookies']) == 1
    assert "test1" not in s['cookies']
    assert "test3" not in s['cookies']
    assert "test2" in s['cookies']


# Generated at 2022-06-13 22:38:33.190006
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_Session_remove_cookies')
    assert session.cookies == {}
    session['cookies']['foo'] = 'bar'
    assert session.cookies == {'foo': 'bar'}
    session.remove_cookies(['foo'])
    assert session.cookies == {}

# Generated at 2022-06-13 22:38:39.309388
# Unit test for method remove_cookies of class Session

# Generated at 2022-06-13 22:39:13.976253
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import requests
    import requests.cookies
    from requests.cookies import RequestsCookieJar
    from httpie.sessions import Session

    jar = requests.cookies.cookiejar_from_dict({
        'web_session_cookie': '3ed63698dc6c2de6e0d4d4f4b52f6e4d'
    })
    session = Session('/path')
    session.cookies = jar
    session.remove_cookies(['web_session_cookie'])
    jar2 = session.cookies
    assert jar2 == RequestsCookieJar()

# Generated at 2022-06-13 22:39:15.365028
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path='./test.json')
    request_headers = {'header': 'value'}
    session.update_headers(request_headers)
    assert session.headers == request_headers

# Generated at 2022-06-13 22:39:23.767548
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    fname = DEFAULT_SESSIONS_DIR/'abcdefg'
    s = Session(fname)
    s['cookies'] = {'mycookie': 'myvalue'}
    s.remove_cookies(('mycookie',))
    assert not s['cookies']
    s['cookies'] = {'mycookie': 'myvalue'}
    s.remove_cookies(('whatever',))
    assert s['cookies']



# Generated at 2022-06-13 22:39:30.708690
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from unittest import TestCase, main

    class Test(TestCase):
        def test_remove_cookies(self):
            session = Session('/')
            lst = list(range(10))
            for i in lst:
                session['cookies'][i] = i
            session.remove_cookies([0, 5, 9])
            self.assertEqual(set(session['cookies'].keys()), set(lst[1:5] + lst[6:9]))
            session.remove_cookies(list(range(10)))
            self.assertEqual(set(session['cookies'].keys()), set())

    main()

# Generated at 2022-06-13 22:39:36.349694
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('./session.json')
    headers = RequestHeadersDict()
    headers['Content-Type'] = 'application/json'
    headers['User-Agent'] = 'HTTPie/0.9.9'
    headers['Cookie'] = 'key_1=value_1;key_2=value_2'
    s.update_headers(headers)
    print(s.headers)

# Generated at 2022-06-13 22:39:45.543841
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.auth import BasicAuth
    from requests.auth import AuthBase
    from requests.cookies import RequestsCookieJar
    from typing import Iterable
    from urllib.parse import urlsplit
    get_httpie_session = Session('test.json')
    get_httpie_session['headers'] = {'test': '1'}
    get_httpie_session['cookies'] = {'name': 'value'}
    get_httpie_session['auth'] = {'type': 'basic', 'username': 'username', 'password': 'password'}
    get_httpie_session.remove_cookies(['name'])
    assert 'name' not in get_httpie_session['cookies']

# Generated at 2022-06-13 22:39:57.608982
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    empty_session_1 = Session('/path/to/session.json')
    empty_session_1_expected = {'headers': {}, 'cookies': {}, 'auth': {'type': None, 'username': None, 'password': None}}
    assert empty_session_1.data == empty_session_1_expected
    empty_request_headers_1 = RequestHeadersDict()
    empty_session_1.update_headers(empty_request_headers_1)
    empty_session_1_expected = {'headers': {}, 'cookies': {}, 'auth': {'type': None, 'username': None, 'password': None}}
    assert empty_request_headers_1 == empty_session_1_expected
    cookies_1 = RequestsCookieJar()
    empty_session_1.cookies = cookies_1


# Generated at 2022-06-13 22:40:01.925804
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_file_path = '/home/myhome/.httpie/sessions/httpbin.org/test.json'
    session = Session(session_file_path)
    session.load()
    session.remove_cookies(['test_cookie'])
    session.save()


# Generated at 2022-06-13 22:40:13.976726
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    from httpie.cli.dicts import CaseInsensitiveDict
    from httpie.plugins import plugin_manager
    from httpie.plugins.auth import BasicAuth
    from httpie.input import ParseError

    class DummyAuthPlugin(BasicAuth):
        auth_type = 'dummy'
        def get_auth(self,username,password):
            return username,password
        
    plugin_manager.register(DummyAuthPlugin)

    s = Session("test.json")

    s.update_headers(CaseInsensitiveDict({'content-type': 'application/json'}))
    s.update_headers(CaseInsensitiveDict({'cookie': 'foo=bar; baz=bar'}))

# Generated at 2022-06-13 22:40:20.565115
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=DEFAULT_CONFIG_DIR)
    session.cookies = RequestsCookieJar()
    session.cookies.set('cookie1', 'value1')
    session.cookies.set('cookie2', 'value2')
    assert len(session.cookies) == 2
    names = ['cookie1']
    session.remove_cookies(names)
    assert len(session.cookies) == 1
    assert session.cookies['cookie2'].value == 'value2'

# Generated at 2022-06-13 22:41:34.571603
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    cookie_name = 'cookie_name'
    cookie_value = 'cookie_value'
    cookie_value_new = 'cookie_value_new'
    
    # Test that a cookie from HTTPie session is not overridden by cookie from the request
    session = Session(path=None)
    session['cookies'] = {
        cookie_name: {'value': cookie_value},
    }
    session_cookies_old = session['cookies']
    headers = RequestHeadersDict({
        'Cookie': f'{cookie_name}={cookie_value_new}',
    })
    session.update_headers(headers)
    session_cookies_new = session['cookies']
    assert session_cookies_old == session_cookies_new
    assert session_cookies_old[cookie_name]['value']

# Generated at 2022-06-13 22:41:43.169861
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session1 = Session('/tmp/test_session1.json')
    session1['cookies']['abc'] = {'value': 'abc'}
    session1.remove_cookies(['abc'])
    assert 'abc' not in session1['cookies']

    session2 = Session('/tmp/test_session2.json')
    session2['cookies']['abc'] = {'value': 'abc'}
    session2['cookies']['def'] = {'value': 'def'}
    session2['cookies']['ghi'] = {'value': 'ghi'}
    session2.remove_cookies(['abc', 'def'])
    assert 'abc' not in session2['cookies']
    assert 'def' not in session2['cookies']
    assert 'ghi'

# Generated at 2022-06-13 22:41:54.750894
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('./sessions/localhost/test.json'))
    test_jar = RequestsCookieJar()
    test_jar.set_cookie(create_cookie(name='test_c1', value='test_v1'))
    test_jar.set_cookie(create_cookie(name='test_c2', value='test_v2'))
    test_jar.set_cookie(create_cookie(name='test_c3', value='test_v3'))
    session.cookies = test_jar
    session.remove_cookies(['test_c1', 'test_c3'])
    assert session['cookies'] == {'test_c2': {'value': 'test_v2'}}

# Generated at 2022-06-13 22:41:56.710699
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session.remove_cookies(['cookie1'])
    assert 'cookie1' not in session.cookies

# Generated at 2022-06-13 22:41:59.339510
# Unit test for method update_headers of class Session
def test_Session_update_headers():
  session = Session("test")
  session.update_headers({"A":"a", "B":"b"})
  assert session["headers"]["A"] == "a"
  assert session["headers"]["B"] == "b"

# Generated at 2022-06-13 22:42:04.441074
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session_remove_cookies.json')

    session['cookies']['1'] = {}
    session['cookies']['2'] = {}
    session['cookies']['3'] = {}
    session.remove_cookies(['2'])
    assert session['cookies'] == {'1': {}, '3': {}}

# Generated at 2022-06-13 22:42:07.688569
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = {'Content-Type': 'text/html', 'If-Modified-Since': 'date'}
    headers = request_headers.copy()
    Session({}).update_headers(headers)
    assert request_headers == headers

# Generated at 2022-06-13 22:42:20.864593
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # create a cookie jar
    cookienames = ['test', 'test2']
    cookiedicts = [{'value': 'test', 'path': 'test'}, {'value': 'test2', 'path': 'test2'}]
    urls = ['http://test.com', 'http://test2.com']
    jar = RequestsCookieJar()
    for i in range(len(cookienames)):
        jar.set_cookie(create_cookie(cookienames[i], cookiedicts[i].pop('value'), **cookiedicts[i]), urls[i])
    jar.clear_expired_cookies()
    assert len(jar) == 2
    # create session and set cookies
    session_path = Path('test.json')
    session = Session(session_path)

# Generated at 2022-06-13 22:42:27.840327
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test')
    request_headers = RequestHeadersDict()
    request_headers['User-Agent'] = 'HTTPie/0.9.8'
    request_headers['Accept'] = '*/*'
    session.update_headers(request_headers)
    assert session.get('headers').get('User-Agent') is None
    assert session.get('headers').get('Accept') == '*/*'



# Generated at 2022-06-13 22:42:31.038008
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("./mock_session.json")
    session['cookies'] = {
        'cookie1': '',
        'cookie2': '',
    }
    session.remove_cookies(['cookie2'])
    assert session['cookies'] == {'cookie1': ''}