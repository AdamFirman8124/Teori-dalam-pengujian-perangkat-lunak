

# Generated at 2022-06-13 22:33:28.452693
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('./test-session.json')
    input_headers = RequestHeadersDict({'Content-Type': 'text/plain'})
    session.update_headers(input_headers)
    output_headers = session.headers
    assert input_headers == output_headers


# Generated at 2022-06-13 22:33:43.971946
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from pathlib import Path
    from os import mkdir, unlink, remove
    from os.path import exists, curdir
    from tempfile import TemporaryDirectory
    from httpie.session import Session

    with TemporaryDirectory() as tmp_dir:
        mkdir(tmp_dir + '/.httpie/', mode=0o755)
        mkdir(tmp_dir + '/.httpie/sessions/', mode=0o755)

# Generated at 2022-06-13 22:33:55.372618
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path=None)
    session.update_headers({"x-foo": "foo", "x-bar": "bar"})
    assert session["headers"] == {"x-foo": "foo", "x-bar": "bar"}
    session.update_headers({"x-foo": "foofoo", "x-baz": "baz"})
    assert session["headers"] == {"x-foo": "foofoo", "x-bar": "bar", "x-baz": "baz"}
    session.update_headers({"x-foo": None})
    assert session["headers"] == {"x-bar": "bar", "x-baz": "baz"}

# Generated at 2022-06-13 22:34:03.466552
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = 'tmp/Session_remove_cookies.json'
    session = Session(path)
    session['cookies'] = {'test1': {'value': 'test1value'},
                          'test2': {'value': 'test2value'}}
    session.remove_cookies(["test1"])
    assert "test1" not in session['cookies'] and "test1" in session['cookies']
    # clean
    os.remove(path)

# Generated at 2022-06-13 22:34:07.641692
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test')
    d = {"key1": ["value1", "value2"], "key2": "value3"}
    session.update_headers(d)

# Generated at 2022-06-13 22:34:13.964824
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    测试 Session.update_headers()
    """
    s = Session('./test.json')
    s.update_headers({"User-Agent":"hie","Cookie":"a=b"})
    print(s.headers)
    print(s.cookies)

# test_Session_update_headers()

# Generated at 2022-06-13 22:34:21.426838
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path=Path('test'))
    assert session.headers == {}

    session.update_headers(RequestHeadersDict({
        'Content-Type': 'foo/bar',
        'Cookie': 'a=b;c=d;e=f',
        'referer': 'https://example.org/',
        'if-modified-since': '2017-07-09T19:40:03+00:00',
    }))

    assert session.headers == {
        'referer': 'https://example.org/'
    }
    assert session.cookies == RequestsCookieJar([
        create_cookie('a', 'b'),
        create_cookie('c', 'd'),
        create_cookie('e', 'f')
    ])



# Generated at 2022-06-13 22:34:26.686285
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(path=None)
    request_headers = {'Accept-Encoding': 'gzip', 'Content-Length': '5'}
    s.update_headers(request_headers)
    assert s.headers == {'Accept-Encoding': 'gzip'}

if __name__ == '__main__':
    test_Session_update_headers()

# Generated at 2022-06-13 22:34:32.742914
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(None)
    session.update_headers({
        'Content-Type': 'application/json',
        'Cookie': 'a=1',
        'Content-Length': '123',
        'accept': 'application/xml',
        'User-Agent': 'HTTPie/1.0.0',
    })
    assert session.headers == {'accept': 'application/xml'}
    assert len(session.cookies) == 1
    assert session.cookies['a'] == '1'

# Generated at 2022-06-13 22:34:38.751243
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    test_session = Session("test_session")
    test_session.update_headers(
        {'Host': '127.0.0.1', 'User-Agent': 'Test-Agent', 'Content-Type': 'application/json',
         'Content-Length': '500', 'connection': 'keep-alive'})
    assert test_session['headers'] == {'Host': '127.0.0.1',
                                       'User-Agent': 'Test-Agent', 'Content-Type': 'application/json'}

# Generated at 2022-06-13 22:34:49.570969
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('../test/session')
    session.load()
    print(session)
    session.remove_cookies(['JSESSIONID'])
    print(session)

# Generated at 2022-06-13 22:35:02.788197
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session')
    session['headers'] = {'s1': 'v1'}
    session['cookies'] = {'c1': 'v1'}
    request_headers = RequestHeadersDict()
    request_headers['s2'] = 'v2'
    request_headers['set-cookie'] = 'c2=v2'
    request_headers['cookie'] = 'c3=v3'
    session.update_headers(request_headers)
    assert session['headers'] == {'s1': 'v1', 's2': 'v2'}
    assert session['cookies'] == {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}, 'c3': {'value': 'v3'}}

# Generated at 2022-06-13 22:35:15.589180
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('session1')
    s['cookies'] = {
        'name1': {
            'value': 'value1'
        },
        'name2': {
            'value': 'value2'
        },
        'name3': {
            'value': 'value3'
        }
    }
    assert len(s['cookies'].keys()) == 3
    s.remove_cookies(['name1', 'name3'])
    assert len(s['cookies'].keys()) == 1
    assert 'name2' in s['cookies'].keys()
    assert 'name1' not in s['cookies'].keys()
    assert 'name3' not in s['cookies'].keys()

# Generated at 2022-06-13 22:35:23.336785
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import unittest
    import json
    import base64
    from httpie.session import Session
    from httpie.core import main
    from httpie.core import RawRequest

    class TestClass(unittest.TestCase):
        def setUp(self):
            import tempfile
            self.tmpdir = tempfile.TemporaryDirectory()

        def tearDown(self):
            self.tmpdir.cleanup()

        def test(self):
            self.stdin = b'{"foo": "bar", "baz": "baz"}'
            argv = ['--json', '--pretty=colors', '--session=session', '--session-read-only']
            raw_request = RawRequest(method='GET', url=self.url,
                headers=self.request_headers, body=self.stdin)
           

# Generated at 2022-06-13 22:35:35.371271
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cookies import CookieJar
    sess = Session('/tmp/test_remove_cookies')
    sess['cookies'] = {'foo':'bar', 'baz':'buz'}
    sess.remove_cookies(['baz'])
    assert sess['cookies'] == {'foo':'bar', 'baz':'buz'}
    #
    jar = CookieJar()
    jar.set('foo', 'bar')
    jar.set('baz', 'buz')
    sess.cookies = jar
    sess.remove_cookies(['baz'])
    assert sess['cookies'] == {'foo':'bar', 'baz':'buz'}
    sess.remove_cookies(['baz'])

# Generated at 2022-06-13 22:35:42.221784
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    mycookies = {'a':'b','c':'d','e':'f','g':'h','i':'j','k':'l','m':'n'}
    s = Session('/path/to/something')
    s['cookies'] = mycookies
    assert len(s['cookies'])==7
    s.remove_cookies(['a','i'])
    assert len(s['cookies'])==5
    assert 'a' not in s['cookies']
    assert 'i' not in s['cookies']

# Generated at 2022-06-13 22:35:56.624631
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers_dict = {
        "referer": "http://localhost:8000/",
        "content-type": "application/json",
        "cookie": "csrftoken=KXNbaV7AMz5vh8V7Kj0cw5BMLuO24h4i; sessionid=j9l5b5h5l5lp5e5u5q2ki3bqmi5vf832"
    }
    # create a new session
    session_path = (
        DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME / 'localhost' / 'session.json'
    )
    session = Session(path=session_path)
    session.update_headers(headers_dict)
    assert session['headers'] == headers_dict

# Generated at 2022-06-13 22:36:03.024880
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test.json')
    session['cookies'] = {'choco': {'value': 1}, 'water': {'value': 1}}
    assert session['cookies'] == {'choco': {'value': 1}, 'water': {'value': 1}}
    session.remove_cookies(['choco'])
    assert session['cookies'] == {'water': {'value': 1}}

# Generated at 2022-06-13 22:36:13.190849
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict()
    request_headers['Content-Type'] = 'application/x-www-form-urlencoded'
    request_headers['Content-Length'] = '98'
    request_headers['If-Match'] = '*'
    request_headers['User-Agent'] = 'Mozilla/5.0'
    request_headers.raw = [
        [k, request_headers[k]] for k in request_headers
        if k not in SESSION_IGNORED_HEADER_PREFIXES
    ]
    session = Session('test')
    session.update_headers(request_headers)
    assert session['headers'] == {'User-Agent': 'Mozilla/5.0'}

# Generated at 2022-06-13 22:36:18.121405
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    names = ['name1','name2','name3','name4']
    session['cookies'] = {
        'name1': {},
        'name2': {},
        'name3': {},
        'name4': {},
    }
    session.remove_cookies(names)
    assert names == list(session['cookies'].keys())

# Generated at 2022-06-13 22:36:29.888006
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # GIVEN
    session = Session(os.devnull)
    session.update_headers({'Accept': 'application/json'})
    session.update_headers({'Cookie': 'bar=baz'})
    session.update_headers({'Cookie': 'foo=bar'})
    session.update_headers({'if-modified-since': 'blah'})
    session.update_headers({'if-none-match': 'blah'})
    session.update_headers({'if-match': 'blah'})
    session.update_headers({'if-range': 'blah'})
    session.update_headers({'if-unmodified-since': 'blah'})
    session.update_headers({'user-agent': 'HTTPie/1.0.2'})
    # WHEN

# Generated at 2022-06-13 22:36:37.003780
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import tempfile
    test_file = tempfile.NamedTemporaryFile(delete=False)
    test_session_path = test_file.name
    test_file.close()
    test_s = Session(test_session_path)
    test_s['cookies'] = {"a":{"value":"A"}, "b":{"value":"B"}, "c":{"value":"C"}, "d":{"value":"D"}, "e":{"value":"E"}, "f":{"value":"F"}}
    test_s.remove_cookies(["a", "c", "f"])
    assert set(test_s['cookies'].keys()) == set(["b", "d", "e"])
    import os
    os.remove(test_session_path)

# Generated at 2022-06-13 22:36:42.206683
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session')
    session['cookies'] = {
        "test1" : 'value1',
        "test2" : 'value2',
    }
    session.remove_cookies(['test1', 'test3'])
    assert session['cookies'] == {
        'test2' : 'value2'
    }

# Generated at 2022-06-13 22:36:45.637500
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/test')
    s['cookies'] = {'foo':{}, 'bar':{}}
    s.remove_cookies(['foo'])
    assert s['cookies'] == {'bar':{}}



# Generated at 2022-06-13 22:36:50.572476
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("tests/sessions/test")
    headers = {'Set-Cookie':'user=james'}
    session.update_headers(headers)
    print("headers:", headers)
    print("session headers:", session.headers)
    print("session cookies:", session.cookies)


# Generated at 2022-06-13 22:36:58.855822
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = {
        'User-Agent': 'request-u-a',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': 'a=b',
        'If-Match': 'a-tag',
        'If-Modified-Since': 'SomeDate'
    }
    session = Session("test_session")
    session.update_headers(headers)
    assert {'Accept': 'application/json', 'Cookie': 'a=b'} == session.headers

# Generated at 2022-06-13 22:37:07.126003
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session')
    session.update_headers({
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
        'If-None-Match': '"4d1-4aa2e33c48540"',
        'Cookie': 'x=y',
    })
    assert {'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
            'Cookie': 'x=y'} == session.headers

# Generated at 2022-06-13 22:37:11.266271
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("session")
    session['cookies'] = {
        'name1': {'value': 'value1'},
        'name2': {'value': 'value2'},
        'name3': {'value': 'value3'},
    }
    session.remove_cookies(['name1', 'name2'])
    assert(session.cookies == {'name3': {'value': 'value3'}})



# Generated at 2022-06-13 22:37:24.188675
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    class DummyHeaders():
        Cookie = 'key=value'
        Host = 'www.example.com'

# Generated at 2022-06-13 22:37:29.751195
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('Session.json')
    session['cookies'] = {
        "cookie1" : {
            "value": "value1",
            "path": "/",
            "secure" : "False"
        },
        "cookie2" : {
            "value": "value2",
            "path": "/",
            "secure" : "False"
        },
        "cookie3" : {
            "value": "value3",
            "path": "/",
            "secure" : "False"
        }
    }
    session.remove_cookies(["cookie2"])
    assert "cookie2" not in session['cookies']
    assert "cookie1" in session['cookies']
    assert "cookie3" in session['cookies']

    # If a cookie name to remove is not in cookies, it is

# Generated at 2022-06-13 22:37:44.568744
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.__main__ import main
    from httpie.core import main as core_main
    from httpie.context import Environment
    import random

    import conftest

    config_dir = conftest.root_dir / 'conftest-data' / 'config-dir'

    c_session = get_httpie_session(config_dir,
                                   'httpie-test',
                                   'httpie.org',
                                   'http://httpie.org')

    cookies_list = dict()

    def prepare_cookies_list(count):
        cookie_list = []
        d = dict()
        while len(cookie_list) < count:
            cookie_name = random.randint(1, 100000)

# Generated at 2022-06-13 22:37:51.701341
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    session = Session('test')
    session['cookies'] = {'cookie1': None,'cookie2': None}
    assert session['cookies'] == {'cookie1': None,'cookie2': None}
    assert 'cookie1' in session['cookies']
    assert 'cookie2' in session['cookies']
    names = ['cookie1']
    session.remove_cookies(names)
    assert session['cookies'] == {'cookie2': None}
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' in session['cookies']

# Generated at 2022-06-13 22:37:56.021070
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/')
    session['cookies'] = {}
    session.remove_cookies([])
    assert session['cookies'] == {}
    session['cookies']['name'] = {'value': 'value'}
    session.remove_cookies(['name'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:59.618792
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('teste')
    names = ['a', 'b', 'c']

    s.remove_cookies(names)

# Generated at 2022-06-13 22:38:12.847806
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/Users/user/httpie/sessions/google.com/google.json')
    session['cookies'] = {
        'name': {
            'value': 'value1',
            'path': '/',
            'secure': False,
            'expires': None
        },
        'name2': {
            'value': 'value2',
            'path': '/',
            'secure': False,
            'expires': None
        },
        'name3': {
            'value': 'value3',
            'path': '/',
            'secure': False,
            'expires': None
        }
    }
    session.remove_cookies(['name', 'name3'])

# Generated at 2022-06-13 22:38:17.648548
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session_headers = RequestHeadersDict()
    session_headers['x-foo'] = '1'
    session_headers['x-bar'] = '2'
    session1 = Session(path=Path.cwd())
    session1['headers'] = session_headers

    request_headers = RequestHeadersDict()
    request_headers['X-FOO'] = '10'
    request_headers['X-BAR'] = '20'
    request_headers['x-baz'] = '3'
    session1.update_headers(request_headers=request_headers)

    assert session1['headers'] == {
        'x-foo': '10',
        'x-bar': '20',
        'x-baz': '3'
    }



# Generated at 2022-06-13 22:38:24.571864
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_path = Path(DEFAULT_SESSIONS_DIR / 'test.json')
    session = Session(session_path)
    session.load()
    session.remove_cookies(['name1', 'name2'])
    names = ['name1', 'name2', 'name5']
    assert list(session['cookies'].keys()) == names
    session.remove_cookies(names)
    assert list(session['cookies'].keys()) == []
    session.save()

# Generated at 2022-06-13 22:38:35.797114
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    import copy
    request_headers = RequestHeadersDict()
    request_headers['Content-Language'] = 'en-US'
    request_headers['Content-Length'] = 0
    request_headers['Cookie'] = 'key1=value1; key2=value2; key3=value3'
    request_headers['If-Modified-Since'] = 'Sat, 29 Oct 1994 19:43:31 GMT'
    request_headers['If-None-Match'] = '*'
    request_headers['Content-Type'] = 'application/json'

    session = Session("./session.json")
    session.update_headers(copy.copy(request_headers))

    # Python 2.7 and Python 3.3 will return OrderedDict while new
    # version of Python will return dict.

# Generated at 2022-06-13 22:38:46.326749
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    config_dir = DEFAULT_SESSIONS_DIR
    url = 'http://httpie.org/'
    session = get_httpie_session(config_dir, '', '', url)
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie(
        name='test_cookie', value='test_value', domain='httpie.org'))
    session.cookies.set_cookie(create_cookie(
        name='test_cookie2', value='test_value2', domain='httpie.org'))
    session.cookies.set_cookie(create_cookie(
        name='test_cookie3', value='test_value3', domain='httpie.org'))

# Generated at 2022-06-13 22:38:54.141437
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('a/b')

    assert session.headers == {}

    session.update_headers({
        'User-Agent': 'HTTPie/0.9.9',
        'Cookie': 'foo1=bar1; foo2=bar2',
        'Content-Type': 'application/json',
    })

    assert session.headers == {'Cookie': 'foo1=bar1; foo2=bar2',
                               'Content-Type': 'application/json'}

# Generated at 2022-06-13 22:39:10.925802
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    '''
    Test method remove_cookies of class Session
    '''
    session = Session(DEFAULT_SESSIONS_DIR / 'test_session.json')
    session['cookies'] = {
        'name1': {
            'value': 'val1',
            'path': '/',
            'secure': False,
            'expires': None
        },
        'name2': {
            'value': 'val2',
            'path': '/',
            'secure': True,
            'expires': 'Tue, 8 Jan 2019 12:47:44 GMT'
        },
        'name3': {
            'value': 'val3',
            'path': '/',
            'secure': False,
            'expires': 'Tue, 8 Jan 2019 12:47:44 GMT'
        }
    }

    expected

# Generated at 2022-06-13 22:39:17.090871
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('path')
    s['cookies'] = {
        'c1': {'value': 'v1'},
        'c2': {'value': 'v2'},
        'c3': {'value': 'v3'},
    }
    s.remove_cookies(['c1', 'c5', 'c2'])
    assert s['cookies'] == {'c3': {'value': 'v3'}}

# Generated at 2022-06-13 22:39:17.914412
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    assert 1 == 1

# Generated at 2022-06-13 22:39:25.897320
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("test")
    s['cookies'] = {
        "1": {"value": "value1"},
        "2": {"value": "value2"},
        "3": {"value": "value3"}
    }
    names = ["1", "3"]
    s.remove_cookies(names)
    assert s['cookies'] == {"2": {"value": "value2"}}



# Generated at 2022-06-13 22:39:32.411539
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie import ExitStatus
    from httpie.client import JSON_ACCEPT
    from httpie.compat import urlopen
    from httpie.context import Environment
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    from tests import http, HTTP_OK, TestEnvironment

    env = TestEnvironment()
    env.config['default_options'] = ['--session=test']
    env.config.dir = Path('/')
    r = http('--print=BHB', '--session=test', 'GET', httpbin.url + '/cookies/set?test=foo&bar=baz', env=env)
    assert HTTP_OK in r
    assert r.json == {'test': 'foo', 'bar': 'baz'}
    assert 'HTTPie-Session: test' in r.headers

# Generated at 2022-06-13 22:39:38.720731
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('/tmp/test'))
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}, 'cookie3': {'value': 'value3'}}
    session.remove_cookies(names=['cookie1'])

    assert 'cookie1' not in session['cookies']
    assert 'cookie2' in session['cookies']
    assert 'cookie3' in session['cookies']

# Generated at 2022-06-13 22:39:52.208353
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sessions_dir = DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME
    if not sessions_dir.exists():
        sessions_dir.mkdir()
    session_path = sessions_dir.joinpath('test.json')
    with open(session_path, 'w') as f:
        f.write("""
{
    "cookies": {
        "name1": {
            "value": "value1"
        },
        "name2": {
            "value": "value2",
            "path": "/"
        },
        "name3": {
            "value": "value3"
        }
    }
}
    """)

    session = Session(session_path)
    session.load()
    session.remove_cookies(['name1', 'name3'])


# Generated at 2022-06-13 22:39:53.193002
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
  raise NotImplementedError


# Generated at 2022-06-13 22:40:03.943821
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test_cookie_remove")
    session.cookies = RequestsCookieJar()

    new_cookie = {'name': 'cookie', 'value': 'value', 'domain': 'domain'}
    session.cookies.set_cookie(create_cookie(**new_cookie))

    session.remove_cookies(['cookie'])
    assert 'cookie' not in session['cookies'].keys()

    session.cookies.set_cookie(create_cookie(**new_cookie))
    session.remove_cookies(['cookie'])
    assert 'cookie' not in session['cookies'].keys()

    session.cookies.set_cookie(create_cookie(**new_cookie))
    session.remove_cookies(['cookie'])
    assert 'cookie' not in session['cookies'].keys()

# Generated at 2022-06-13 22:40:13.023338
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.plugins import AuthPlugin, plugin_manager
    plugin_manager.clear()
    plugin_manager.register(SimpleAuthPlugin())
    session = Session(path = './test_Session_remove_cookies')
    cookie_value = 'testCookie'
    cookie_name = 'testName'
    session['cookies'] = {}
    session['cookies'][cookie_name] = {'value': cookie_value}
    assert cookie_name in session['cookies']
    session.remove_cookies([cookie_name])
    assert cookie_name not in session['cookies']


# Generated at 2022-06-13 22:40:33.381519
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session.update_headers({'Cookie': 'username=joe'})
    assert(session['cookies'] == {'username': {'value': 'joe'}})
    session.remove_cookies(['username'])
    assert(session['cookies'] == {})



# Generated at 2022-06-13 22:40:40.386820
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s.cookies = RequestsCookieJar()
    s['cookies'] = {'A': {'value': 1}, 'B': {'value': 2}, 'C': {'value': 3}}
    s.remove_cookies(['A', 'B'])
    s.remove_cookies(['C'])
    s.remove_cookies(['C'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:40:44.221456
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session['cookies'] = {'cookie1': {'value': 'value1'}, 
                          'cookie2': {'value': 'value2'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value2'}}

# Generated at 2022-06-13 22:40:46.472201
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/sessions/unit_test')
    session['cookies'] = {'a': {'value': '1'}, 'b': {'value': '1'}}
    session.remove_cookies(['a'])

# Generated at 2022-06-13 22:40:53.059940
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'c1': 1, 'c2': 2, 'c3': 3}
    s = Session(None)
    s['cookies'] = cookies
    s.remove_cookies(['c2', 'c3'])
    assert s['cookies'] == {'c1': 1}

# Generated at 2022-06-13 22:41:03.645544
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # setup test data
    cookie_name_list = ['test1', 'test2', 'test3']
    test_cookies_dict = dict()
    for name in cookie_name_list:
        test_cookies_dict[name] = {'value': name, 'max-age': 1000}

    # test before
    assert len(test_cookies_dict.keys()) == len(cookie_name_list)

    # test during
    for item in cookie_name_list:
        Session.remove_cookies(test_cookies_dict, item)

    # test after
    assert len(test_cookies_dict.keys()) == 0

# Generated at 2022-06-13 22:41:13.739240
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = 'tests/sessions/test.json'
    session = Session(path)

    # case 1: valid input
    session.cookies = None
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie('foo', 'bar'))
    session.cookies.set_cookie(create_cookie('baz', 'qux'))

    session.remove_cookies(['foo','baz'])
    assert (session['cookies'] is None) or (len(session['cookies']) == 0)

    # case 2: invalid input
    session.cookies = None
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie('foo', 'bar'))

# Generated at 2022-06-13 22:41:23.932670
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_Session_remove_cookies')
    assert session.remove_cookies([]) == None
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie(
        'a', '1', path= '/', secure=True, expires=True))
    session.cookies.set_cookie(create_cookie(
        'b', '2', path= '/', secure=True, expires=True))
    session.cookies.set_cookie(create_cookie(
        'c', '3', path= '/', secure=True, expires=True))
    assert session.cookies != {}
    session.remove_cookies(['a','b'])
    assert session.cookies != {}
    session.remove_cookies(['c'])

# Generated at 2022-06-13 22:41:31.501190
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("path")
    session.cookies = [
        create_cookie("c1", "v1", path='/p1'),
        create_cookie("c2", "v2", path='/p2'),
    ]
    session.remove_cookies("c2")
    assert len(session.cookies) == 1
    assert session.cookies.get("c1") is not None
    assert session.cookies.get("c2") is None

# Generated at 2022-06-13 22:41:37.952352
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('some-file')
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie(
        'cookie1', 'value1'))
    session.cookies.set_cookie(create_cookie(
        'cookie2', 'value2'))
    session.cookies.set_cookie(create_cookie(
        'cookie3', 'value3'))
    session.remove_cookies(['cookie1', 'cookie3'])
    assert len(session['cookies']) == 1
    assert session['cookies']['cookie2']['value'] == 'value2'

# Generated at 2022-06-13 22:42:10.022470
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {
        'cookie1': {'value': 'value1'},
        'cookie2': {'value': 'value2'},
        'cookie3': {'value': 'value3'},
    }
    session = Session(path='')
    session['cookies'] = cookies
    session.remove_cookies(['cookie1', 'cookie2'])
    assert session['cookies'] == {'cookie3': {'value': 'value3'}}

# Generated at 2022-06-13 22:42:19.945626
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    mysession = Session('./test_path.json')
    mysession['cookies'] = {'c1': {'path': '/', 'expires': 99999, 'secure': False, 'value': '1'},
                            'c2': {'path': '/', 'expires': 99999, 'secure': False, 'value': '2'}}
    names = ['c1', 'c2', 'c3']
    mysession.remove_cookies(names)
    assert mysession['cookies'] == {'c2': {'path': '/', 'expires': 99999, 'secure': False, 'value': '2'}}


# Generated at 2022-06-13 22:42:27.770989
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = ''
    session = Session(path)
    session.headers = {'a': 'b'}
    session['cookies'] = {'a': 'b', 'c': 'd', 'e': 'f'}
    session.remove_cookies(['a', 'b', 'c'])
    assert session['cookies'] == {'e': 'f'}
    session.remove_cookies(['e', 'f'])
    assert session['cookies'] == {'e': 'f'}

# Generated at 2022-06-13 22:42:32.837404
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    config_dir = Path("C:/httpie/tests")
    session_name = "test_session"
    host = "github.com"
    url = "https://github.com"
    session = get_httpie_session(config_dir, session_name, host=host, url=url)

    assert session['cookies']
    session.remove_cookies(['bla'])
    assert session['cookies']['user_session']
    session.remove_cookies(['user_session'])
    assert not session['cookies']['user_session']

# Generated at 2022-06-13 22:42:42.587207
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {
        'cookie1': {'value': 'value1'},
        'cookie2': {'value': 'value2'},
        'cookie3': {'value': 'value3'},
        'cookie4': {'value': 'value4'}
    }
    session.remove_cookies(['cookie1', 'cookie3'])
    assert session['cookies'] == {
        'cookie2': {'value': 'value2'},
        'cookie4': {'value': 'value4'}
    }

# Generated at 2022-06-13 22:42:48.098024
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class TestSession(Session):
        def __init__(self):
            self['cookies'] = {'test1': {'value': 'test1'}, 'test2': {'value': 'test2'}}
    session = TestSession()
    session.remove_cookies(['test2'])
    assert session['cookies'] == {'test1': {'value': 'test1'}}

# Generated at 2022-06-13 22:42:54.749755
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session.json')
    session['cookies']['a'] = {}
    session['cookies']['b'] = {}
    session.remove_cookies(['a', 'c'])
    assert 'b' in session['cookies']
    assert 'a' not in session['cookies']

# Generated at 2022-06-13 22:43:03.506625
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path("test"))
    cookies = {"cookie1":{"value":"value1", "path":"path1", "secure":True, "expires":"2020-01-01"}}
    session['cookies'] = cookies
    session.remove_cookies(["cookie1"])
    assert session['cookies']=={}


# Generated at 2022-06-13 22:43:11.650691
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/path/to/file')
    session['cookies'] = {}
    session.remove_cookies([])
    assert session['cookies'] == {}
    session['cookies'] = {'foo': 'bar'}
    session.remove_cookies([])
    assert session['cookies'] == {'foo': 'bar'}
    session['cookies'] = {'foo': 'bar', 'baz': 'qux'}
    session.remove_cookies(['quux'])
    assert session['cookies'] == {'foo': 'bar', 'baz': 'qux'}
    session['cookies'] = {'foo': 'bar', 'baz': 'qux'}
    session.remove_cookies(['baz'])

# Generated at 2022-06-13 22:43:17.104891
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="path")
    session['cookies'] = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3'
    }
    session.remove_cookies(['key1', 'key2'])
    assert session['cookies'] == {'key3': 'value3'}