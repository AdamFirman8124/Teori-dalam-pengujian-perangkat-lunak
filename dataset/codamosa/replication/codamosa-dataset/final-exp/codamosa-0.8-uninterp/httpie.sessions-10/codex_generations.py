

# Generated at 2022-06-13 22:33:23.688593
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(Path('s'))
    s.update_headers(RequestHeadersDict(
        [('Content-Length', '0'), ('url', 'httpbin.org')]))
    assert s.headers == RequestHeadersDict([('url', 'httpbin.org')])

# Generated at 2022-06-13 22:33:27.566617
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('a.json')
    session['cookies'] = {'a': {'value':'1'}, 'b': {'value':'2'}}
    session.remove_cookies(['a'])
    assert session['cookies'] == {'b': {'value':'2'}}

# Generated at 2022-06-13 22:33:29.621473
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    Method update_headers of class Session can be tested by
    events of httpie.
    """
    pass


# Generated at 2022-06-13 22:33:34.855534
# Unit test for method update_headers of class Session
def test_Session_update_headers():
  session = Session(path = "test")
  session.update_headers({"h1":"v1", "h2":"v2"})

  #print(session)
  assert(session.headers == {'h1': 'v1', 'h2': 'v2'})

# Generated at 2022-06-13 22:33:44.049603
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    class request_headers_with_cookies:
        def items(self):
            return (
                ('User-Agent', 'HTTPie/1.0.3'),
                ('Host', 'httpbin.org'),
                ('Cookie', 'yummy_cookie=choco; tasty_cookie=strawberry'),
            )
    session = Session("asd")
    session.update_headers(request_headers_with_cookies())
    assert (
        session.cookies ==
        RequestsCookieJar([
            create_cookie('yummy_cookie', 'choco'),
            create_cookie('tasty_cookie', 'strawberry'),
        ])
    )

# Generated at 2022-06-13 22:33:56.942701
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = {'Content-Type': 'application/json',
        'Content-Length': '10',         # ignored
        'user-agent': 'HTTPie/2.0.0',    # ignored
        'te': 'trailers',               # not ignored
        'host': 'httpie.org',           # not ignored
        'Content-MD5': '123ABC'         # ignored
    }

    session = Session('file')
    # set initial session headers
    session['headers'] = {'te': 'trailers', 'Cookie': 'test_cookie=test_value'}

    session.update_headers(request_headers)

    assert session['headers']['te'] == 'trailers'
    assert session['headers']['host'] == 'httpie.org'
    assert len(session['headers'].keys()) == 4

# Generated at 2022-06-13 22:34:01.388982
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    Test of method "update_headers"
    """
    s = Session("")
    headers = {"key1": "value1", "key2": "value2", "key3": "value3"}
    s.update_headers(headers)
    assert s.headers == headers

# Generated at 2022-06-13 22:34:05.534698
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    expected_headers = {'name1': 'value1', 'name2': 'value2'}
    session = Session(path='dummy.txt')
    session.update_headers(expected_headers)
    assert session.headers == expected_headers

# Generated at 2022-06-13 22:34:18.371340
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.argtypes import KeyValueArg
    args = [
        KeyValueArg('key', 'value'),
        KeyValueArg('c', 'vvv'),
        KeyValueArg('C', 'www'),
        KeyValueArg('header', 'b'),
        KeyValueArg('H', 'a')
    ]
    session = Session('session')
    session.update_headers(RequestHeadersDict(args))
    print(session)

# Generated at 2022-06-13 22:34:26.229085
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session.json')
    session['cookies'] = {'foo': {'value': 'bar'},
                          'baz': {'value': 'qux'},
                          'quux': {'value': 'quuux'}}
    assert len(session['cookies']) == 3
    session.remove_cookies(['foo', 'quux'])
    assert len(session['cookies']) == 1
    assert session['cookies']['baz']['value'] == 'qux'

# Generated at 2022-06-13 22:34:40.102574
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/fake/path')
    session['headers'] = {'Arbitrary':'Value'}
    assert session['headers'] == {'Arbitrary':'Value'}

    session.update_headers({'If-Modified-Since':'Sat, 29 Oct 1994 19:43:31 GMT'})
    assert session['headers'] == {'Arbitrary':'Value'}

    session.update_headers({'User-Agent':'HTTPie/0.9.8'})
    assert session['headers'] == {'Arbitrary':'Value'}

    session.update_headers({'Cookie':'session_id=38afes7a8'})
    assert session['cookies'] == {'session_id': {'value': '38afes7a8'}}

# Generated at 2022-06-13 22:34:49.805853
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    sess = Session('n')
    sess.update_headers({'Cookie': 'foo=bar'})
    assert sess['cookies'] == {'foo': {'value': 'bar'}}
    del sess['cookies']
    assert('Cookie' not in sess['headers'].keys() or sess['headers']['Cookie'] != 'foo=bar')

    sess.update_headers({'User-agent': 'HTTPie/1.0.3'})
    del sess['headers']['User-agent']
    assert('User-agent' not in sess['headers'].keys())

    sess.update_headers({'Content-Type': 'application/json'})
    assert('Content-Type' not in sess['headers'].keys())


# Generated at 2022-06-13 22:35:02.926066
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = ('{"auth": {"username": null, "password": null, "type": null},'
               '"cookies": {}, "headers": {}}')
    path = Path('toto')
    session = Session(path)
    session.load()
    session.update_headers({'Cookie': 'mycookie=myvalue'})
    assert dict(session) == {
        'headers': {},
        'cookies': {'mycookie': {'value': 'myvalue'}},
        'auth': {'type': None, 'username': None, 'password': None},
    }
    session.update_headers({'Cookie': 'mycookie=myvalue2'})

# Generated at 2022-06-13 22:35:16.336477
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    session = Session("./")
    headers = {
        'Cookie': 'name=value',
        'HOST': 'host_name',
        'Content-Length': '1234',
        'If-Modified-Since': 'Wed, 13 Jul 2016 18:15:35 GMT',
        'If-None-Match': '"abc"'
    }

    session.update_headers(headers)

    assert session['cookies'] == {'name': {'value': 'value'}}
    assert session['headers'] == {'Host': 'host_name'}
    assert headers == {
        'Content-Length': '1234',
        'If-Modified-Since': 'Wed, 13 Jul 2016 18:15:35 GMT',
        'If-None-Match': '"abc"'
    }

# Generated at 2022-06-13 22:35:20.997627
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    Test the method update_headers from class Session
    with a dummy request_headers object
    """
    req_headers_dummy = {"x-real-ip": "127.0.0.1"}
    session = Session(".")
    session.update_headers(req_headers_dummy)
    assert session['headers'] == req_headers_dummy

# Generated at 2022-06-13 22:35:31.941783
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = [create_cookie(name, value) for name, value in \
        [('name1', 'value1'), ('name2', 'value2'), ('name3', 'value3')]
    ]

    # Case of deleting an existing cookie
    session = Session(path='')
    session['cookies'] = {cookie.name: {'value': cookie.value} \
        for cookie in cookies}
    session.remove_cookies(['name2', 'name4'])
    assert session['cookies'] == {'name1': {'value': 'value1'}, \
        'name3': {'value': 'value3'}}



# Generated at 2022-06-13 22:35:42.953970
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_Session_update_headers.json')
    headers = {
        'a': 'b',
        'Accept': 'c',
        'Accept-Encoding': 'd',
        'Accept-Language': 'e',
        'authorization': 'f',
        'Cookie': 'g',
        'User-Agent': 'h',
    }
    session.update_headers(RequestHeadersDict(headers))

    expected_headers = {
        'a': 'b',
        'Accept': 'c',
        'Accept-Encoding': 'd',
        'Accept-Language': 'e',
        'authorization': 'f',
    }
    assert session.headers == expected_headers
    expected_cookies = {
        'g': {
            'value': 'g',
        }
    }


# Generated at 2022-06-13 22:35:46.871561
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path="tests/session.json")
    request_headers = {'name': 'val' , 'name2':'val2'}
    session.update_headers(request_headers)
    assert session.headers == request_headers

# Generated at 2022-06-13 22:35:53.639526
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('name')
    session.cookies = {}
    session.update_headers({'cookie': 'foo=bar; baz=qux'})
    session.remove_cookies(['foo'])
    assert ('foo=bar' not in session.headers['Cookie'])


if __name__ == '__main__':
    exit(test_Session_remove_cookies())

# Generated at 2022-06-13 22:36:05.795976
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test')
    session.update_headers({'hello': 'world'})
    assert session['headers'] == {'hello': 'world'}

    cookies = {
        'cookie1': {
            'value': 'cookie1-value',
            'expires': 123,
            'secure': True
        },
        'cookie2': {
            'value': 'cookie2-value',
            'path': '/path/to/cookie'
        },
        'cookie3': {
            'value': 'cookie3-value',
            'domain': '.example.com'
        },
    }

# Generated at 2022-06-13 22:36:19.438188
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/path/to/session')
    # Without cookies
    session.remove_cookies(['non_existant'])

    session['cookies'] = {
        'cookie1': {'value': 'foo'},
        'cookie2': {'value': 'bar'},
    }

    session.remove_cookies(['cookie1', 'non_existant'])
    assert session['cookies'] == {'cookie2': {'value': 'bar'}}

    session.remove_cookies(['cookie2'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:36:28.638724
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    config_dir = Path('/tmp/')
    session_name = 'test_Session_remove_cookies'
    session_file = config_dir / SESSIONS_DIR_NAME / session_name + ".json"
    if session_file.exists():
        os.remove(session_file)
    session = Session(session_file)
    session.load()
    session['cookies']['a'] = {'value': 'value_a'}
    session['cookies']['b'] = {'value': 'value_b'}
    session.save()
    session = Session(session_file)
    session.load()
    assert session['cookies']['a'] == {'value': 'value_a'}

# Generated at 2022-06-13 22:36:34.946655
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('path')
    s.cookies = RequestsCookieJar()
    assert not s.cookies
    s.cookies.update({'A': 'a'})
    s.cookies.update({'B': 'b'})
    s.cookies.update({'C': 'c'})
    assert s.cookies
    s.remove_cookies(['A', 'C'])
    assert len(s.cookies) == 1
    assert 'A' not in s.cookies
    assert 'C' not in s.cookies
    assert 'B' in s.cookies



# Generated at 2022-06-13 22:36:41.324038
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('/tmp/session.json')
    session = Session (path)
    session['cookies'] = {'cookie1':{'value': '1234'}, 'cookie2':{'value': '5678'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2':{'value': '5678'}}



# Generated at 2022-06-13 22:36:45.893838
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session("./some_file")
    sess['cookies'] = {"a": 1, "b": 2}
    sess.remove_cookies(["a", "c"])
    assert sess['cookies'] == {"b": 2}
    assert type(sess['cookies']) is dict


# Generated at 2022-06-13 22:36:50.608991
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session.json')
    session['cookies'] = {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    session.remove_cookies(['c1'])
    assert session['cookies'] == {'c2': {'value': 'v2'}}

# Generated at 2022-06-13 22:36:58.855782
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('~/.httpie/sessions/ig.com/ig.json')
    session = Session(path)
    session.load()

    session.remove_cookies(["ipo", "ok", "ss", "ds_user_id", "sessionid", "urlgen", "mcd", "shbid", "shbts", "rur", "mid", "ds_user", "csrftoken"])

    assert session['cookies'].__contains__("urlgen") == False

    session.save()

# Generated at 2022-06-13 22:37:03.777862
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("")
    session["cookies"]["cookie1"] = "value1"
    session["cookies"]["cookie2"] = "value2"
    session.remove_cookies(["cookie1", "cookie3"])
    if "cookie1" in session["cookies"] or "cookie2" not in session["cookies"]:
        raise Exception("test_Session_remove_cookies failed")

# Generated at 2022-06-13 22:37:11.771516
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
  cookies = {}
  headers = {}
  auth = {
    'type': None,
    'username': None,
    'password': None
  }
  config = {
    'headers': headers,
    'cookies': cookies,
    'auth': auth
  }
  sess = Session('./test')
  sess['headers'] = {}
  sess['cookies'] = {}
  sess['auth'] = auth

  cookies['test1'] = 'test1'
  cookies['test2'] = 'test2'
  cookies['test3'] = 'test3'
  sess['cookies'] = cookies
  sess.remove_cookies(['test1'])
  assert sess == config

  cookies = {}
  cookies['test2'] = 'test2'

# Generated at 2022-06-13 22:37:21.965736
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s.cookies = RequestsCookieJar()
    s.cookies.set('cookie-to-remove', '', path='/')
    s.cookies.set('cookie-to-keep', '', path='/')
    s.cookies.clear_expired_cookies()
    assert len(s.cookies) == 2
    s.remove_cookies(['cookie-to-remove'])
    assert len(s.cookies) == 1



# Generated at 2022-06-13 22:37:33.929313
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("path")
    session['cookies'] = {'cookie1' : 'cookie1_value', 'cookie2' : 'cookie2_value'}
    session.remove_cookies(['cookie1'])
    assert 'cookie1' not in session['cookies']
    assert 'cookie1_value' not in session['cookies']
    assert 'cookie2' in session['cookies']
    assert 'cookie2_value' in session['cookies']

# Generated at 2022-06-13 22:37:38.267722
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    a = Session('abc')
    a['cookies'] = {'key1':'value1', 'key2':'value2'}
    assert len(a['cookies']) == 2
    a.remove_cookies(['key1'])
    assert len(a['cookies']) == 1



# Generated at 2022-06-13 22:37:42.871717
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Setup
    from httpie.config.sessions import Session
    from httpie.plugins import plugin_manager
    session = Session(path='path')
    session['cookies'] = {'A': {'value': 'B'}, 'C': {'value': 'D'}}
    # Exercise
    session.remove_cookies(['A'])
    # Verify
    assert session['cookies'] == {'C': {'value': 'D'}}

# Generated at 2022-06-13 22:37:47.148074
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('../test/test_session')
    session['cookies'] = {'test1': {'value': 'test'}}
    session.remove_cookies(['test1'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:50.464988
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
        s = Session("test_session.json")
        s["cookies"] = {"cookie1": {"value": "cookie1_value"}}
        s.remove_cookies(['cookie1'])
        assert s["cookies"] == {}

# Generated at 2022-06-13 22:37:53.100329
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session['cookies'] = {'foo': {'value': 'bar'}}
    session.remove_cookies(['foo'])
    assert 'foo' not in session['cookies']

# Generated at 2022-06-13 22:37:56.941675
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names = ['abc', 'xyz']
    session = Session('temp')
    session['cookies']['abc'] = 'def'
    session['cookies']['ghi'] = 'jkl'
    session.remove_cookies(names)
    session_cookies = session['cookies']
    assert 'abc' not in session_cookies
    assert 'ghi' in session_cookies

# Generated at 2022-06-13 22:38:02.043168
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'a': {}, 'b': {}}
    session.remove_cookies(['a'])
    assert session['cookies'] == {'b': {}}



# Generated at 2022-06-13 22:38:13.219997
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_jar = RequestsCookieJar()
    cookie_jar.set_cookie(create_cookie("key1", "value1", path='/'))
    cookie_jar.set_cookie(create_cookie("key2", "value1", path='/'))
    cookie_jar.set_cookie(create_cookie("key3", "value1", path='/'))

    session = Session('/')
    session.cookies = cookie_jar
    session.remove_cookies(['key2', 'key3'])
    assert len(session.cookies) == 1
    assert 'key1' in session.cookies
    assert 'key2' not in session.cookies
    assert 'key3' not in session.cookies

# Generated at 2022-06-13 22:38:21.646393
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(':memory:')
    s.cookies = RequestsCookieJar()
    s.cookies.set('a', 'a')
    s.cookies.set('b', 'b')
    assert s['cookies'] == {'a': {'value': 'a'}, 'b': {'value': 'b'}}
    s.remove_cookies(['a', 'b'])
    assert s['cookies'] == {}



# Generated at 2022-06-13 22:38:34.676727
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('./session.json')
    session = Session(path)
    session['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'qux'},
    }
    session.remove_cookies(['foo'])
    assert session['cookies']['baz'] == {'value': 'qux'}
    assert 'foo' not in session['cookies']
    session.remove_cookies(['baz'])
    assert 'baz' not in session['cookies']

# Generated at 2022-06-13 22:38:39.889343
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test session")
    cookie_name = "Cookie_test"
    session.cookies[cookie_name] = "Cookie_test_value"
    assert cookie_name in session.cookies
    session.remove_cookies([cookie_name])
    assert cookie_name not in session.cookies

# Generated at 2022-06-13 22:38:47.002374
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("")
    session['cookies'] = {"1": {'value': "1"}, "2": {'value': "2"}}
    assert session['cookies']["1"] == {'value': "1"}
    assert session['cookies']["2"] == {'value': "2"}
    session.remove_cookies(["1"])
    assert len(session['cookies']) == 1
    assert session['cookies']["2"] == {'value': "2"}
    session.remove_cookies(["2"])
    assert len(session['cookies']) == 0

# Generated at 2022-06-13 22:38:57.080476
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(os.path.sep)
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}}
    print(session.cookies)
    for cookie in session.cookies:
        print(cookie)

    print('remove_cookies')
    session.remove_cookies(['cookie1', 'cookie2'])
    print(session.cookies)
    for cookie in session.cookies:
        print(cookie)

if __name__ == '__main__':
    test_Session_remove_cookies()

# Generated at 2022-06-13 22:39:06.081182
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    config_path = 'tests/session/session.json'
    session = Session(config_path)
    session['cookies'] = {'name1': 'value1', 'name2': 'value2', 'name3': 'value3'}

    # test case 1: remove single cookie
    session.remove_cookies(['name1'])
    assert 'name1' not in session['cookies']

    # test case 2: remove multiple cookies
    session.remove_cookies(['name2', 'name3'])
    assert 'name2' not in session['cookies']
    assert 'name3' not in session['cookies']


# Generated at 2022-06-13 22:39:11.149681
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='path')
    session['cookies'] = {'a':'a_val', 'b':'b_val'}
    assert session['cookies'] == {'a':'a_val', 'b':'b_val'}
    session.remove_cookies(['a'])
    assert session['cookies'] == {'b':'b_val'}


# Generated at 2022-06-13 22:39:19.481173
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(path=None)
    sess['cookies']={'username':'xzw', 'pwd':'123456'}
    cookie_dict={
        'username': {
            'value': 'xzw',
            'path': '/',
            'secure': True,
            'expires': None
        },
        'pwd':{
            'value': '123456',
            'path': '/',
            'secure': True,
            'expires': None
        }
    }
    assert cookie_dict == sess['cookies']
    # delete a cookie that exists
    sess.remove_cookies(['username'])

# Generated at 2022-06-13 22:39:27.227722
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(config_dir=DEFAULT_CONFIG_DIR,
                      session_name='default',
                      host='127.0.0.1',
                      url='')
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    cookie_names = ['cookie1']
    session.remove_cookies(cookie_names)
    assert session['cookies'] == {'cookie2': 'value2'}

# Generated at 2022-06-13 22:39:39.119590
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(os.path.join(DEFAULT_SESSIONS_DIR, 'localhost', 'test'))
    session['cookies'] = {
        'JSESSIONID': {
            'path': '/',
            'secure': True,
            'expires': 0,
            'value': 'abc'
        },
        'SSOID': {
            'path': '/',
            'secure': True,
            'expires': 0,
            'value': 'xyz'
        },
        'othercookie': {
            'path': '/',
            'secure': True,
            'expires': 0,
            'value': 'xyz'
        }
    }
    session.remove_cookies(['JSESSIONID'])
    assert len(session['cookies']) == 2
    assert 'JSESSIONID'

# Generated at 2022-06-13 22:39:44.035401
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("")
    session['cookies'] = {"name": ["value"]}
    session.remove_cookies(["name"])
    assert "name" not in session['cookies']



# Generated at 2022-06-13 22:40:00.036915
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('temp.json')
    session['cookies'] = {'name1': {'value': 'value1', 'path': '/path1'}, 'name2': {'value': 'value2', 'path': '/path2'}}
    session.remove_cookies(['name1'])
    assert session['cookies'] == {'name2': {'value': 'value2', 'path': '/path2'}}

# Generated at 2022-06-13 22:40:05.267397
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #given
    session_path = Path(__file__).parent / "test_Session_remove_cookies.txt"
    session = Session(session_path)
    session['cookies'] = {
                        "cookie1": "1",
                        "cookie2": "2",
                        "cookie3": "3"
                        }
    #when
    session.remove_cookies(["cookie1","cookie2"])
    #then
    assert session['cookies'] == {"cookie3": "3"}

# Generated at 2022-06-13 22:40:17.230322
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(None)

    # Case 1: There is no cookie in the session
    session.remove_cookies(['foo'])

    # Case 2: There is one cookie in the session and it will be deleted
    session['cookies'] = {'foo': 'bar'}
    session.remove_cookies(['foo'])
    assert len(session['cookies']) == 0

    # Case 3: There are two cookies in the session and one of them will be deleted
    session['cookies'] = {'foo': 'bar', 'baz': 'bar'}
    session.remove_cookies(['foo'])
    assert len(session['cookies']) == 1

    # Case 4: There are two cookies in the session, both of them will be deleted

# Generated at 2022-06-13 22:40:22.326179
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test.json')
    s.update_headers({'Cookie': 'a=1; b=2'})
    s.remove_cookies(['b'])
    cookies = s.cookies
    assert cookies['a'].value == '1'
    assert str(cookies['a']) == 'a=1'
    assert not cookies.get('b')

# Generated at 2022-06-13 22:40:26.318668
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path = 'test')
    assert {'1': {'value': '1'}, '2': {'value': '2'}} == session.cookies
    session.remove_cookies(['1'])
    assert {'2': {'value': '2'}} == session.cookies
    session.remove_cookies(['2'])
    assert {} == session.cookies



# Generated at 2022-06-13 22:40:33.540223
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import pytest

    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.plugins import plugin_manager

    from httpie.plugins.builtin import HTTPBasicAuth

    plugin_manager.register(HTTPBasicAuth)

    session = Session(DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME / 'test.json')
    session['cookies'] = {"name1":"value1", "name2": "value2"}

    # Case-1: Case-insensitive cookie names
    session.remove_cookies(['NAME1', 'NAME2'])
    assert session['cookies'] == {}

    # Case-2: Case-sensitive cookie names
    session['cookies'] = {"name1":"value1", "name2": "value2"}

# Generated at 2022-06-13 22:40:37.875476
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s['cookies'] = {'a': 'b', 'b': 'c'}
    s.remove_cookies(['a', 'c'])
    assert s['cookies'] == {'b': 'c'}

# Generated at 2022-06-13 22:40:46.883618
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Create a Session object and a test cookie jar
    session = Session(DEFAULT_SESSIONS_DIR)
    jar = RequestsCookieJar()

    # Populate the jar with some cookies
    jar.set_cookie(create_cookie('a', '1'))
    jar.set_cookie(create_cookie('b', '2'))
    jar.set_cookie(create_cookie('c', '3'))

    session.cookies = jar
    assert 'a' in session.cookies
    assert 'b' in session.cookies
    assert 'c' in session.cookies

    # Test the method remove_cookies
    session.remove_cookies(['a', 'b'])
    assert 'a' not in session.cookies
    assert 'b' not in session.cookies
    assert 'c' in session

# Generated at 2022-06-13 22:40:57.506764
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.plugins.registry import plugin_manager
    from httpie.config import BaseConfigDict
    from httpie.context import Environment
    from httpie.input import ParseError
    from requests.cookies import RequestsCookieJar
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.registry import plugin_manager
    import json
    import os
    import re
    import shutil
    import sys
    import tempfile
    import requests
    import urllib3
    import pytest
    from httpie.config import AUTH_PLUGIN_PREFIX
    from httpie.plugins import AuthPlugin, BuiltinAuthPlugin


# Generated at 2022-06-13 22:41:02.305349
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('sessions/test_session')
    session['cookies'] = {'cookie1': {'value': 'value1','path': 'path1','secure': 'secure1','expires': 'expires1'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:41:22.079896
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_cookies = {'name1': 'value', 'name2': 'value'}
    test_r_cookies = {'name1': 'value'}
    s = Session('test.json')
    s.cookies = test_cookies
    test_names = ['name2']
    s.remove_cookies(test_names)
    assert test_r_cookies == s.cookies


# Generated at 2022-06-13 22:41:30.159658
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test.json")
    session["cookies"] = {
            "key1": {"value": "value1"},
            "key2": {"value": "value2"}
            }

    names = ["key2"]
    session.remove_cookies(names)

    assert len(session["cookies"]) == 1
    assert session["cookies"] == {"key1": {"value": "value1"}}



# Generated at 2022-06-13 22:41:33.404586
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("test.json")
    s.cookies = { "c1": "v1" }
    s.remove_cookies(["c1"])
    assert (s.cookies == {})

# Generated at 2022-06-13 22:41:42.047419
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('~/.config/httpie/sessions/localhost/s1.json')
    session = Session(path)
    session['cookies'] = {
        'cookie1': {
            'secure': True,
            'path': '/',
            'expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
            'value': 'test1'
        },
        'cookie2': {
            'secure': True,
            'path': '/',
            'expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
            'value': 'test2'
        }
    }
    session.remove_cookies(['cookie1', 'cookie3'])

# Generated at 2022-06-13 22:41:47.140574
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(None)
    s['cookies'] = {'key1': 'value1', 'key2': 'value2'}
    s.remove_cookies(['key1','key2'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:41:56.368018
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cfg_dir = Path('.') / 'tests' / 'testdir'
    session = get_httpie_session(cfg_dir, 'test', host='example.org', url='localhost')
    session.load()
    session['cookies'] = {'name': {'value': 'value'}}
    assert 'name' in session['cookies']
    session.remove_cookies(names=['name'])
    assert 'name' not in session['cookies']

# Generated at 2022-06-13 22:42:00.862326
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='test')
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value2'}}

# Generated at 2022-06-13 22:42:06.840028
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('./test')
    s['cookies'] = {
        'test1': {'value': 'test1'},
        'test2': {'value': 'test2'},
        'test3': {'value': 'test3'},
    }
    s.remove_cookies(('test1',))
    assert s['cookies'] == {
        'test2': {'value': 'test2'},
        'test3': {'value': 'test3'},
    }

# Generated at 2022-06-13 22:42:10.873003
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(''))
    session.load()
    session['cookies'] = {'cookie1': {}, 'cookie2': {}}
    assert session['cookies']['cookie1'] == {}
    assert session['cookies']['cookie2'] == {}
    session.remove_cookies(('cookie1', 'cookie2'))
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' not in session['cookies']


# Generated at 2022-06-13 22:42:20.861979
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_sessions/test_remove_cookies.json')
    import random
    # random cookies: ['l3qgkgf', '9cbmrvh', 'xz8hosw']
    cookies = [''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(8)) for j in range(3)]
    for cookie in cookies:
        session['cookies'][cookie] = {'value': cookie}
    session.remove_cookies([cookies[0], cookies[2]])
    assert session['cookies'] == {cookies[1]: {'value': cookies[1]}}

# Generated at 2022-06-13 22:42:45.154465
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(__file__.replace('.py', '.json')))
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value1'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value1'}}

# Generated at 2022-06-13 22:42:48.757871
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/httpie_test')
    session['cookies'] = {'A': {'value': 'B'}, 'C': {'value': 'D'}}
    session.remove_cookies(['A', 'B'])
    assert 'A' not in session['cookies']

# Generated at 2022-06-13 22:42:51.021568
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.session import Session
    session = Session
    session.remove_cookies(['cookie_name'])

# Generated at 2022-06-13 22:42:58.137965
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("./test-session-remove-cookies.json")
    cookies = {
        'cookie1': {
            'value': 'value1',
            'path': '/'
        },
        'cookie2': {
            'value': 'value2',
            'path': '/'
        }
    }
    session['cookies'] = cookies
    session.remove_cookies(['cookie1', 'cookie2'])
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:43:09.048139
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    data = {'cookies': {'cookie_1': {"value": "1"}, 'cookie_2': {"value": "2"},
                        'cookie_3': {"value": "3"}}}
    ses = Session('test')
    ses.update(data)
    assert ses['cookies'] == data['cookies']
    ses.remove_cookies(['cookie_1', 'cookie_2'])
    assert ses['cookies'] == {'cookie_3': {"value": "3"}}

# Generated at 2022-06-13 22:43:15.765037
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(DEFAULT_SESSIONS_DIR, 'example.json'))
    session.load()
    session.remove_cookies({'name1', 'name2'})
    assert 'name1' not in session['cookies'].keys()
    assert 'name2' not in session['cookies'].keys()
    assert 'name3' in session['cookies'].keys()