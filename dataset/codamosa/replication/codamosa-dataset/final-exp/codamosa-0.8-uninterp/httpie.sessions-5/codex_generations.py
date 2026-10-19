

# Generated at 2022-06-13 22:33:26.072017
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    class MockSession(Session):
        pass

    mock_path = '-s'
    mock_request_headers = {'Host': 'www.xxx.com', 'Cookie': 'cookie_name=yuanfang'}
    mock_session = MockSession(mock_path)
    print(mock_session.update_headers(mock_request_headers))
    print(mock_session.headers)
    print(mock_session.cookies)
    print(mock_session['cookies'])
    # import json
    # print(json.dumps(mock_session))

# Generated at 2022-06-13 22:33:33.206421
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session.update({'cookies': {'foo': {}, 'bar': {}}})
    assert session['cookies'] == {'foo': {}, 'bar': {}}
    session.remove_cookies(['foo'])
    assert session['cookies'] == {'bar': {}}
    session.remove_cookies(['baz'])
    assert session['cookies'] == {'bar': {}}
    session.remove_cookies(['bar'])
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:33:41.640385
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.argtypes import KeyValueArgType
    session = Session(path='/tmp/session.json')
    request_headers = RequestHeadersDict()
    request_headers['Content-Type'] = 'application/json'
    request_headers['User-Agent'] = 'HTTPie/0.9.8'
    session.update_headers(request_headers)
    print(session.headers)
    print(session.cookies)
    print(session.auth)
    print(session.dict)


if __name__ == '__main__':
    test_Session_update_headers()

# Generated at 2022-06-13 22:33:51.605317
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_update_headers')
    session['headers']['name2'] = 'value2'
    session['headers']['name5'] = 'value5'
    request_headers = {
        'name1': 'value1',
        'name2': 'value2',
        'name3': 'value3',
        'name4': 'value4',
        'name5': 'value5',
        'Cookie': '',
    }
    session.update_headers(request_headers)
    assert request_headers == {
        'name1': 'value1',
        'name3': 'value3',
        'name4': 'value4',
    }

# Generated at 2022-06-13 22:34:03.464436
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict([
            ('content-type', 'application/json'),
            ('content-length', '10'),
            ('user-agent', 'httpie/0.9.9'),
            ('accept-encoding', 'gzip, deflate, compress'),
            ('accept', '*/*'),
            ('host', 'httpbin.org'),
            ('Cookie','foo=bar; bar=baz'),
            ('X-Auth-Token','123'),
            ('X-Auth-Username','456')
        ])
    session = Session(path = 'dummy_path')
    session.update_headers(headers)

# Generated at 2022-06-13 22:34:08.709811
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session.update_headers({"Cookie": "A=A; B=B"})
    session.remove_cookies(['A', 'B'])
    assert session['cookies'].keys() == dict_view({})



# Generated at 2022-06-13 22:34:15.896825
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path = '')
    session['headers'] = {'Cookies': None,'User-Agent': 'HTTPie/1.0.2'}
    session.update_headers(RequestHeadersDict({'Cookies': None,'User-Agent': 'HTTPie/1.0.2'}))
    assert session.headers == {'Cookies': None,'User-Agent': 'HTTPie/1.0.2'}


# Generated at 2022-06-13 22:34:28.352114
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/file/path')

    # Test to see that when the method update_headers is invoked, the
    # headers object will be updated with the request headers
    request_headers = [
        ('h', 'v'),
        ('h1', None),
        ('h2', 'v2'),
    ]
    session.update_headers(request_headers)
    assert session['headers'] == {'h': 'v', 'h2': 'v2'}

    # Test to see that the HTTP_COOKIE value is split, and that the cookie
    # value is added to the session object
    request_headers = [('HTTP_COOKIE', 'k=v; k1=v1')]
    session.update_headers(request_headers)

# Generated at 2022-06-13 22:34:39.511057
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict()
    request_headers.add('User-Agent', 'HTTPie/1.0.2')
    request_headers.add('User-Agent', 'HTTPie/2.0.1')
    cookie_value = 'foo=bar;'
    for http_header_name in ['Cookie', 'cookie']:
        request_headers.add(http_header_name, cookie_value)
    session = Session('test.json')
    session.update_headers(request_headers)
    assert 'User-Agent' not in session.headers
    assert 'Cookie' not in session.headers
    assert 'cookie' not in session.headers
    assert session.cookies == RequestsCookieJar([create_cookie(
        'foo', 'bar')])

# Generated at 2022-06-13 22:34:49.205055
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test.json')
    session.load()
    cookies = session.cookies
    assert len(cookies) == 0

    session.cookies = RequestsCookieJar()
    for name in ["foo", "bar", "baz"]:
        cookie = dict(name=name, value="v"+name)
        session["cookies"][name] = cookie
    assert len(cookies) == 3

    session.remove_cookies(["bar", "qux"])
    assert len(cookies) == 2
    assert "foo" in cookies
    assert "bar" not in cookies
    assert "baz" in cookies
    assert cookies["foo"] == "vfoo"
    assert cookies["baz"] == "vbaz"


# Generated at 2022-06-13 22:35:04.104621
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_dict = {
        'auth': {'type': None, 'username': None, 'password': None},
        'cookies': {'a': {'value': 'b'}, 'c': {'value': 'd'}},
        'headers': {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
        }
    }

    session = Session('path')
    session.load_config_from_dict(session_dict)

    session.remove_

# Generated at 2022-06-13 22:35:13.269234
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session.json')
    session['cookies'] = {'test1': 'test1', 'test2': 'test2'}
    new_cookies = []
    for cookie in session.cookies:
        if cookie.name != 'test1' and cookie.name != 'test2':
            new_cookies.append(cookie)
    session.cookies = new_cookies
    if session['cookies']:
        raise AssertionError('Session cookies not deleted')



# Generated at 2022-06-13 22:35:20.094078
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """Unit test for method remove_cookies of class Session"""
    session = Session('/some/session')
    session.update({
        'cookies': {
            'my-cookie': 'some-value',
            'other-cookie': 'some-other-value',
        }
    })
    session.remove_cookies(['my-cookie'])
    assert session['cookies'] == {'other-cookie': 'some-other-value'}

# Generated at 2022-06-13 22:35:33.382617
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie import session, cookiejar
    from httpie.client import parse_headers_file

    sess = {'cookies': {'foo': 'bar'}, "headers": ''}
    path = 'tests/data/session_remove_cookies/httpie.sessions/test.json'
    with open(path, 'w') as fp:
        fp.write(json.dumps({'foo': 'bar'}))
    session.Session(path).remove_cookies(('foo',))
    with open(path, 'r') as fp:
        assert json.loads(fp.read()) == {}

    path = 'tests/data/session_remove_cookies/httpie.sessions/test.json'

# Generated at 2022-06-13 22:35:38.824291
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/foo/bar.json')
    session.update({'cookies': {'foo': {'value': 'a'},
                                'bar': {'value': 'b'}}})
    session.remove_cookies(['foo'])
    assert session.cookies == RequestsCookieJar([create_cookie(
        'bar', 'b')])



# Generated at 2022-06-13 22:35:44.958281
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # method remove_cookies removes cookies given in the input argument names
    ses=Session('./index.json')
    ses['cookies']={'a':1,'b':2,'c':3}
    ses.remove_cookies(['a','c'])
    assert ses['cookies']=={'b':2}

# Generated at 2022-06-13 22:35:53.189770
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('some_file')
    session['cookies'] = {'name1': 'value1', 'name2': 'value2', 'name3': 'value3'}
    session.remove_cookies(['name1', 'name2'])
    assert session == {'cookies': {'name3': 'value3'}, 'auth': {'type': None, 'username': None, 'password': None}, 'headers': {}}

# Generated at 2022-06-13 22:35:58.859855
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path("test.json"))
    session['cookies'] = {'key1': {'value': 'value1'}, 'key2': {'value': 'value2'}}
    session.remove_cookies(['key1','key3'])
    assert session['cookies'] == {'key2': {'value': 'value2'}}

# Generated at 2022-06-13 22:36:08.088398
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session.txt')
    cookies_dict = {}
    cookies_dict["cookie1"] = 'value1'
    cookies_dict["cookie2"] = 'value2'
    cookies_dict["cookie3"] = 'value3'
    session.cookies = cookies_dict
    names = ['cookie1']
    session.remove_cookies(names)
    assert {'cookie2': 'value2', 'cookie3': 'value3'} == session['cookies']

# Generated at 2022-06-13 22:36:14.290245
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {'a': '1', 'b': '2', 'c': '3'}
    s.remove_cookies(['a', 'c'])
    assert s['cookies'] == {'b': '2'}

# Generated at 2022-06-13 22:36:30.779875
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session1 = {
        'headers': {},
        'cookies': {'csrftoken': {'value': '12345', 'path': '/'}},
        'auth': {
            'type': None,
            'username': None,
            'password': None
        }
    }
    session = Session(path=Path('./test.json'))
    session.__dict__.update(session1)
    session.remove_cookies(['csrftoken'])
    assert session.cookies == {'csrftoken': {'value': '12345', 'path': '/'}}

# Generated at 2022-06-13 22:36:36.052855
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('~/.httpie/sessions/sbrk-0.sbrk.cloud:32778/test.json')
    session['cookies'] = {'1': {'value': '1'}, '2': {'value': '2'}}
    session.remove_cookies(['1', '3'])
    assert session['cookies'] == {'2': {'value': '2'}}

# Generated at 2022-06-13 22:36:39.286381
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    obj = Session("test")
    obj.update_headers({"asdf": "fdsa"})
    obj.remove_cookies({'asdf'})
    dump = obj.dumps()
    print(dump)

# Generated at 2022-06-13 22:36:46.771341
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_dict = {
                    'headers': {},
                    'cookies': {'sessionid': {'value': '123', 'domain': '.test.com', 'path': '/'},
                                'user_id': {'value': '12'}},
                    'auth': {
                            'type': None,
                            'username': None,
                            'password': None
                            }
                    }
    session = Session('path')
    session.update(session_dict)

    session.remove_cookies(['sessionid', 'user_id'])

    assert session['cookies'] == {}

# Generated at 2022-06-13 22:36:54.954500
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.compat import str
    from httpie.plugins import AuthPlugin

    class DummyAuth(AuthPlugin):
        auth_type = 'dummy-auth'
        auth_parse = True
        auth_require = False

        def get_auth(self, username, password):
            return username, password

        def __call__(self, r):
            r.headers['Authorization'] = f'{self.username} {self.password}'
            return r

    session = Session('/path/to/session')
    session.update_headers({
        'Cookie': 'foo=bar; baz=buz'
    })
    session.update_headers({
        'Cookie': 'boo=boz'
    })

# Generated at 2022-06-13 22:37:09.447002
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from requests import cookies
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.sessions import SESSIONS_DIR_NAME, Session, get_httpie_session, VALID_SESSION_NAME_PATTERN

    # Unit test for removal of cookies
    def test_unit_removal_of_cookies():
        c = cookies.RequestsCookieJar()
        c.set('name', 'value1', path='/path')
        c.set('name', 'value2', path='/path')
        c.set('name', 'value3', path='/path')
        s = Session(DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME / 'test.json')
        assert s.cookies == c

    # Unit test for removal of cookies

# Generated at 2022-06-13 22:37:20.045545
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {
        'cookie1': {'value': 'value1'},
        'cookie2': {'value': 'value2'},
        'cookie3': {'value': 'value3'}
    }
    assert isinstance(session['cookies'], dict)
    assert len(session['cookies']) == 3
    session.remove_cookies(['cookie1', 'cookie2'])
    assert len(session['cookies']) == 1
    assert session['cookies'] == { 'cookie3': {'value': 'value3'}}

# Generated at 2022-06-13 22:37:26.581464
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session1 = Session('/tmp/test1.json')
    session1['cookies']['abc'] = {'value': 'abc'}
    session1['cookies']['def'] = {'value': 'def'}
    session1['cookies']['ghi'] = {'value': 'ghi'}
    session1.remove_cookies(['def', 'jkl'])
    assert session1['cookies'] == {'abc': {'value': 'abc'}, 'ghi': {'value': 'ghi'}}

# Generated at 2022-06-13 22:37:34.219686
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/new1')
    session['cookies'] = {'1': {'value': '11'}, '2': {'value': '22'}}
    assert session['cookies'] == {'1': {'value': '11'}, '2': {'value': '22'}}
    session.remove_cookies(['1'])
    assert session['cookies'] == {'2': {'value': '22'}}

# Generated at 2022-06-13 22:37:42.211159
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.context import Environment
    from httpie.plugins import AuthPlugin
    from httpie.plugins import builtin
    from httpie.plugins.builtin import HTTPBasicAuth
    import unittest
    import copy
    import json
    import sys

    class TestSessionRemoveCookies(unittest.TestCase):

        def setUp(self):
            # Redefine mockups for plugins
            original_plugins = copy.deepcopy(builtin.__all__)
            # Remove plugin HTTPieBasicAuth
            builtin.__all__.remove(builtin.HTTPBasicAuth)
            # Add new class mockups
            self.http_basic_auth = HTTPBasicAuth
            builtin.__all__.append('HTTPBasicAuth')
            # Patch plugin manager
            self.auth_plugin = AuthPlugin()

# Generated at 2022-06-13 22:37:54.957055
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('abc.json')
    # remove_cookies from empty session
    assert session['cookies'] == {}
    session.remove_cookies(['a'])

    session['cookies'] = {
        'a': {'value': 'a'},
        'b': {'value': 'b'},
    }
    session.remove_cookies(['a'])
    assert session['cookies'] == {
        'b': {'value': 'b'},
    }

# Generated at 2022-06-13 22:38:00.598401
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path = 'test_file')
    s['cookies'] = {'key': 'value'}
    s.remove_cookies(['key'])
    assert 'key' not in s['cookies']
    s['cookies'] = {'key': 'value'}
    s.remove_cookies(['key', 'key'])
    assert 'key' not in s['cookies']
    s['cookies'] = {'key': 'value', 'key1': 'value1'}
    s.remove_cookies(['key', 'key1'])
    assert 'key' not in s['cookies'] and 'key1' not in s['cookies']

# Generated at 2022-06-13 22:38:08.516230
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {
        'test1': 'test1',
        'test3': 'test3'
    }
    assert session['cookies']['test1'] == 'test1'
    assert session['cookies']['test3'] == 'test3'
    session.remove_cookies(['test1'])
    assert 'test1' not in session['cookies']
    assert 'test3' in session['cookies']

# Generated at 2022-06-13 22:38:17.257954
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.input.utils import KeyValueArg

    s = Session('test.json')
    s['cookies'] = {'hello': {'value': 'value'}, 'deleted': {'value': 'value'}}
    s.remove_cookies(KeyValueArg('deleted'))
    assert 'hello' in s['cookies']
    assert 'deleted' not in s['cookies']

    s = Session('test.json')
    s['cookies'] = {'hello': {'value': 'value'}, 'deleted': {'value': 'value'}}
    s.remove_cookies(KeyValueArg('non existent'))
    assert 'hello' in s['cookies']
    assert 'deleted' in s['cookies']

    s = Session('test.json')
    s['cookies']

# Generated at 2022-06-13 22:38:20.859233
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('filepath')
    s['cookies'] = {'cookie':{'value':'value'}}
    s.remove_cookies(['cookie'])
    assert dict == s.cookies.__class__

# Generated at 2022-06-13 22:38:25.999247
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session')
    session['cookies']={'Cookie1':{'value':'value1'},'Cookie2':{'value':'value2'}}
    session.remove_cookies(['Cookie1'])
    assert ('Cookie1' not in session['cookies']) and ('Cookie2' in session['cookies'])

# Generated at 2022-06-13 22:38:32.455372
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    cookies = {'a':'1', 'b':'2', 'c':'3'}
    session['cookies'] = cookies
    session.remove_cookies(['a', 'c'])
    assert session['cookies'] == {'b':'2'}

# Generated at 2022-06-13 22:38:44.586753
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('./test.json')
    names = ['a', 'b', 'c']
    s.cookies = RequestsCookieJar()
    s.cookies.set('a', '1')
    s.cookies.set('b', '2')
    s.cookies.set('c', '3')
    s.cookies.set('d', '4')
    s.remove_cookies(names)
    assert 'a' not in s.cookies
    assert 'b' not in s.cookies
    assert 'c' not in s.cookies
    assert 'd' in s.cookies
    s.cookies.clear()
    s.cookies.set('a', '1')
    s.cookies.set('b', '2')

# Generated at 2022-06-13 22:38:49.320564
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test.json")
    session["cookies"] = {"a":1}
    session.remove_cookies(["a"])
    assert "a" not in session["cookies"]

# Generated at 2022-06-13 22:38:57.089655
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("/home/User/.config/httpie/sessions")
    s['cookies'] = {
        "cookie1": {"value": "value1"},
        "cookie2": {"value": "value2"},
        "cookie3": {"value": "value3"}
    }

    s.remove_cookies(["cookie1", "cookie2"])

    assert s['cookies'] == {"cookie3": {"value": "value3"}}

# Generated at 2022-06-13 22:39:16.552954
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    new_session = Session('new_session')
    new_session['cookies'] = {'name1': {'value': 'value1'}, 'name2': {'value': 'value2'}}
    new_session.remove_cookies(['name1'])
    assert new_session['cookies'] == {'name2': {'value': 'value2'}}

# Generated at 2022-06-13 22:39:28.848969
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='tests/fixtures/httpie_session_to_remove_cookies')
    session.load()
    session.remove_cookies(names = ['session_id', '_identity'])

# Generated at 2022-06-13 22:39:39.442531
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("/Test/")
    string_cookies = '''
        {
            "cookies": { "aa": 1, "bb" : 2, "cc" : 3 }
        }
    '''
    s.load_from_json_string(string_cookies )
    assert s['cookies'] == { "aa": 1, "bb" : 2, "cc" : 3 }
    s.remove_cookies(["aa", "cc"])
    assert s['cookies'] == { "bb" : 2 }
    s.remove_cookies(["bb"])
    assert s['cookies'] == {  }
    string_cookies = '''
        {
            "cookies": { }
        }
    '''
    s.load_from_json_string(string_cookies )
   

# Generated at 2022-06-13 22:39:47.743694
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/')
    session['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'qux'}
    }
    session.remove_cookies({'foo', 'bar'})
    assert session['cookies'] == {'baz': {'value': 'qux'}}



# Generated at 2022-06-13 22:39:58.611563
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
  from httpie.client import JSON_ACCEPT, JSON_ACCEPT_ENCODING
  from httpie.context import Environment
  from httpie.plugins.builtin import HTTPBasicAuth
  from httpie.plugins.registry import plugin_manager
  from httpie.plugins.registry import plugin_manager
  from httpie.session import Session
  from httpie.plugins.builtin import HTTPBasicAuth
  from httpie.plugins.registry import plugin_manager
  # Initialize basic auth plugin
  plugin_manager.get_auth_plugin('basic')
  #fixme: doesn't work with unit tests
  #environment = Environment(config_dir=DEFAULT_CONFIG_DIR, colors=NoColors())

  # Test removing cookies
  expected = {'Cookie': 'X=value'}

# Generated at 2022-06-13 22:40:02.391260
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session({})
    session['cookies']['key1'] = 'value'
    session.remove_cookies('key1')
    if 'key1' in session['cookies']:
        assert False
    else:
        assert True

# Generated at 2022-06-13 22:40:14.318811
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    c1 = {'name': "name 1", 'value': "value 1"}
    c2 = {'name': "name 2", 'value': "value 2"}
    c3 = {'name': "name 3", 'value': "value 3"}

    session = Session('tests')
    session.cookies = {c1, c2, c3}

    assert session.cookies.__contains__(c1)
    assert session.cookies.__contains__(c2)
    assert session.cookies.__contains__(c3)

    session.remove_cookies({c1['name'], c2['name']})

    assert not session.cookies.__contains__(c1)
    assert not session.cookies.__contains__(c2)
    assert session.cookies.__contains__

# Generated at 2022-06-13 22:40:20.519555
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session.update_headers({'Cookie': 'a=b;c=d'})
    assert 'a' in session.cookies and 'c' in session.cookies
    session.remove_cookies(['a'])
    assert 'a' not in session.cookies and 'c' in session.cookies
    session.remove_cookies(['c'])
    assert 'c' not in session.cookies


# Generated at 2022-06-13 22:40:23.064592
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/')
    session['cookies'] = {'a': 'b'}
    session.remove_cookies(['a'])
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:40:29.531081
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("/Users/mona/DA/Python/httpie/httpie/compat.py")
    l = ['a', 'b']
    session.remove_cookies(l)

    if session.remove_cookies(l) != session:
        print("Error: test_Session_remove_cookies")
        exit(1)

# Generated at 2022-06-13 22:41:00.356373
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_Session_remove_cookies')
    session['cookies'] = {'a': {'value': '1'}, 'b': {'value': '2'}, 'c': {'value': '3'}}
    session.remove_cookies(['a', 'b'])
    assert session['cookies'] == {'c': {'value': '3'}}

# Generated at 2022-06-13 22:41:04.417335
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(path='path/file')
    sess['cookies'] = {'a': 'aa', 'b': 'bb'}
    sess.remove_cookies(['a'])
    assert sess['cookies'] == {'b': 'bb'}

# Generated at 2022-06-13 22:41:11.367208
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    a_session = Session(path=''.join(('file.json')))
    a_session.cookies = {'a':'b', 'c':'d'}
    assert a_session.cookies == {'a':'b', 'c':'d'}
    a_session.remove_cookies(['a', 'b'])
    assert a_session.cookies == {'c':'d'}

# Generated at 2022-06-13 22:41:21.536599
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(path=Path("test.json"))
    # Test when cookie present in session
    names = []
    names.append("test")
    sess['cookies'] = {"test": "test"}
    sess.remove_cookies(names)
    assert sess['cookies'] == {}

    # Test when cookie not present in the session
    names = []
    names.append("test1")
    names.append("test2")
    sess['cookies'] = {"test": "test"}
    sess.remove_cookies(names)
    assert sess['cookies'] == {"test": "test"}

# Generated at 2022-06-13 22:41:34.124793
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('/tmp/testsess.json')
    sess['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'bing'},
    }
    sess.remove_cookies(['foo','baz'])
    assert not sess['cookies']

    sess['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'bing'},
    }
    sess.remove_cookies(['foo'])
    assert sess['cookies'] == {'baz': {'value': 'bing'}}

    sess['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'bing'},
    }


# Generated at 2022-06-13 22:41:38.597379
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sesh = Session('my_session')
    cookies = {'name1': {}, 'name2': {}, 'name3': {}}
    sesh['cookies'] = cookies

    sesh.remove_cookies(['name1', 'name3'])

    assert (sesh['cookies'] == {'name2': {}})

# Generated at 2022-06-13 22:41:45.611419
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_instance = Session("/home/")
    session_instance['cookies']['foo'] = {'value': 'bar'}
    assert 'foo' in session_instance['cookies']
    session_instance.remove_cookies(['foo'])
    assert 'foo' not in session_instance['cookies']
    session_instance['cookies']['foo'] = {'value': 'bar'}
    assert 'foo' in session_instance['cookies']
    session_instance.remove_cookies(['bar'])
    assert 'foo' in session_instance['cookies']

# Generated at 2022-06-13 22:41:52.312183
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(DEFAULT_SESSIONS_DIR / 'sessions')
    session['cookies'] = {'cookie1' : 'cookie1', 'cookie2' : 'cookie2'}
    session.remove_cookies(['cookie1','cookie2'])
    assert len(session) == 1

test_Session_remove_cookies()



# Generated at 2022-06-13 22:42:00.387202
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = get_httpie_session(DEFAULT_CONFIG_DIR, 'test', None, 'http://example.com')
    headers = {'Cookie': 'a=1; b=2; c=3'}
    session.update_headers(headers)
    session.remove_cookies(['b', 'c'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:42:04.523092
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {'id': {'value': "value"}}
    session.remove_cookies(['id'])
    if not 'id' in session['cookies']:
        print('Test Session_remove_cookies succeeds')
    else:
        print('Test Session_remove_cookies fails')