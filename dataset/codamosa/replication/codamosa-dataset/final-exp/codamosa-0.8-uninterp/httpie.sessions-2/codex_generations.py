

# Generated at 2022-06-13 22:33:26.114759
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Test class Session
    session = Session('sessions_path')
    session['cookies'] = {'key1': {'value': 'value1'}, 'key2': {'value': 'value2'}}
    session.remove_cookies(['key2'])
    assert session['cookies'] == {'key1': {'value': 'value1'}}



# Generated at 2022-06-13 22:33:29.693583
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('~/.config/httpie/sessions/bbc.json')
    session.update_headers({'HOST': 'bbc.co.uk', 'Cookie': 'BBC-UID=1234567; expires=Fri'})
    assert session.headers == {'HOST': 'bbc.co.uk'}
    assert session.cookies == RequestsCookieJar()

# Generated at 2022-06-13 22:33:42.627090
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Set headers that will be stored in the session (no ignored header prefix)
    request_headers = RequestHeadersDict({
        'Content-type': 'text/html',
        'Accept': 'text/plain',
        'Accept-Language': 'fr',
    })
    session = Session(path=Path('/tmp/.httpie-session'))
    session.load()
    # Put headers in the session
    session.update_headers(request_headers)
    assert session.headers == request_headers
    session.save()
    # Check file content

# Generated at 2022-06-13 22:33:51.656465
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(None)

    request_headers = {
        'accept': 'application/json',
        'content-type': 'application/json'
    }
    session.update_headers(request_headers)
    assert session['headers'] == request_headers

    session['headers'] = {}

    request_headers = {
        'content-type': None,
        'accept': 'application/json',
    }
    session.update_headers(request_headers)
    assert session['headers'] == {'accept': 'application/json'}

    session['headers'] = {}

    request_headers = {
        'content-type': None,
        'accept': None,
    }
    session.update_headers(request_headers)
    assert session['headers'] == {}

    session['headers'] = {}


# Generated at 2022-06-13 22:34:01.779238
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie1 = RequestsCookieJar()
    cookie1.set_cookie(create_cookie('abc', 'def'))
    cookie2 = RequestsCookieJar()
    cookie2.set_cookie(create_cookie('xyz', 'uvw'))
    s = Session('/root/session')
    s['cookies'] = {'abc': cookie1, 'xyz': cookie2}
    s.remove_cookies(['abc'])
    assert s['cookies']['xyz'] == cookie2

# Generated at 2022-06-13 22:34:07.830889
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    import unittest

    class TestCase(unittest.TestCase):

        def test_update_headers(self):
            request_headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip, deflate, br'}
            s = Session('sessions/test-session')
            s.update_headers(request_headers)


test_Session_update_headers()

# Generated at 2022-06-13 22:34:14.171943
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(path="path/to/session")
    s.update_headers({"Accept-Encoding": "null", "Content-Type": "application/json", "If-Match": "test"})
    assert s['headers'] == {"Accept-Encoding": "null", "Content-Type": "application/json"}
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:34:24.404026
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path='')

# Generated at 2022-06-13 22:34:31.621203
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('test_session.json'))
    assert len(session['cookies'])==0
    cookie1 = create_cookie(name='testCookie1', value='123')
    cookie2 = create_cookie(name='testCookie2', value='456')
    session['cookies'][cookie1.name] = {
        'value': cookie1.value
    }
    session['cookies'][cookie2.name] = {
        'value': cookie2.value
    }
    assert len(session['cookies'])==2
    session.remove_cookies(['testCookie1'])
    assert len(session['cookies'])==1
    session.remove_cookies(['testCookie1'])
    assert len(session['cookies'])==1
    del session

# Generated at 2022-06-13 22:34:40.530655
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session("./test")
    s.update_headers({
        'If-Modified-Since': 'Sat, 29 Oct 1994 19:43:31 GMT',
        'Accept-Language': 'pl-pl,pl;q=0.8,en;q=0.5,en-us;q=0.3',
        'User-Agent': 'HTTPie/0.9.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'some_cookie=some_value',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'httpie.org'
    })


# Generated at 2022-06-13 22:34:51.252911
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('~/test_remove_cookies_Session')
    session['cookies'] = {
        'a': '1',
        'b': '2',
    }
    session.remove_cookies(['b'])
    assert session['cookies'] == {
        'a': '1'
    }

# Generated at 2022-06-13 22:34:58.137813
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='path/to/session.json')
    session['cookies'] = {
        'bad_cookie': {'value': 'value1'},
        'good_cookie': {'value': 'value2'}
    }
    session.remove_cookies(['bad_cookie'])
    assert session['cookies'] == {'good_cookie': {'value': 'value2'}}



# Generated at 2022-06-13 22:35:05.180285
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from requests.cookies import RequestsCookieJar
    session = Session('.')
    session['cookies'] = {'foo': {'value': 'bar'}, 'baz': {'value': 'qux'}}
    session.remove_cookies(['foo', 'quux'])
    assert session['cookies'] == {'baz': {'value': 'qux'}}
    assert session.cookies == RequestsCookieJar([('baz', 'qux')])

# Generated at 2022-06-13 22:35:14.106621
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {
        'firstName': {'value': 'firstName'},
        'lastName': {'value': 'lastName'},
        'thirdName': {'value': 'thirdName'}
    }
    names = ['firstName', 'lastName']
    session = Session("<path>")
    session['cookies'] = cookies
    session.remove_cookies(names)
    assert session['cookies'] == {'thirdName': {'value': 'thirdName'}}



# Generated at 2022-06-13 22:35:17.239481
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'1': {'value':'test1'}, '2': {'value':'test2'} }
    session.remove_cookies(['2'])
    assert session['cookies'] == {'1': {'value':'test1'} },\
    "Session.remove_cookies(): Cookie 2 wasn't deleted"
# End unit tests

# Generated at 2022-06-13 22:35:22.859225
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('dummy')
    session['cookies'] = {
        'cookie1': {},
        'cookie2': {},
        'cookie3': {},
    }
    session.remove_cookies(['cookie2', 'cookie3'])
    assert session['cookies'] == {
        'cookie1': {},
    }

# Generated at 2022-06-13 22:35:27.245583
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test_session')
    s['cookies'] = {'name1': {'value': 'value'}}
    s.remove_cookies(['name1'])
    assert s.get('cookies', {}) == {}

# Generated at 2022-06-13 22:35:33.181561
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names = ['abc', 'efg']
    s = Session(path = "")
    s['cookies'] = {'abc': {'value': 1}, 'efg': {'value': 2}, 'hij': {'value': 3}}
    s.remove_cookies(names)
    assert s['cookies'] == {'hij': {'value': 3}}



# Generated at 2022-06-13 22:35:41.008453
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Test initialisation
    session = Session("test")
    session['cookies']['key1'] = 'val1'
    session['cookies']['key2'] = 'val2'
    session['cookies']['key3'] = 'val3'
    # Test remove_cookies
    session.remove_cookies(['key1', 'key2'])
    assert 'key1' not in session['cookies']
    assert 'key2' not in session['cookies']
    assert 'key3' in session['cookies']


# Generated at 2022-06-13 22:35:46.395096
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.plugins.builtin import FormAuthPlugin
    session = Session("")
    session["cookies"] = {"a": "aaa", "b": "bbb"}
    session.remove_cookies(["b"])
    assert ("b" not in session["cookies"])
    assert ("a" in session["cookies"])
    form_auth_plugin = FormAuthPlugin()

# Generated at 2022-06-13 22:36:06.544693
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.cli.dicts import RequestDataDict
    username = 'admin'
    password = '123'
    session_name = 'mysession'
    config_dir = Path('~/.config/httpie')
    cookies = 'session_id=1; delete_cookie=2; delete_cookie_too=3'
    session: Session = get_httpie_session(config_dir, session_name, None, None)

    session.update_headers(RequestHeadersDict())
    session.update_cookies(RequestDataDict(KeyValueArgType.parse(cookies)))
    session.update_auth(RequestDataDict(KeyValueArgType.parse(
        f'{username}:{password}')))
    session.dump()

    session_path

# Generated at 2022-06-13 22:36:12.477569
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/session')
    session.cookies.set('a', 'aa')
    session.cookies.set('b', 'bb')
    session.cookies.set('c', 'cc')
    session.cookies.set('d', 'dd')
    assert len(session.cookies.get_dict()) == 4
    session.remove_cookies(('c', 'd'))
    assert len(session.cookies.get_dict()) == 2

# Generated at 2022-06-13 22:36:20.616261
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie = {'value': 'test', 'token':'test'}
    cookie2 = {'value': 'test', 'token':'test'}
    session = Session('test')
    session['cookies'] = {'test_cookie':cookie,'test_cookie2':cookie2}
    assert session.get('cookies') == {'test_cookie':cookie,'test_cookie2':cookie2}
    session.remove_cookies(['test_cookie'])
    assert session.get('cookies') == {'test_cookie2':cookie2}

# Generated at 2022-06-13 22:36:25.053057
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('file')
    session['cookies'] = {"cookie_name": {"value": "cookie_value"}}
    session.remove_cookies(['cookie_name'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:36:30.858413
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('test')
    print(test_session.cookies)

    test_session['cookies'] = {'abc': 1, 'def': 2}
    print(test_session.cookies)

    test_session.remove_cookies(['ab', 'def'])
    print(test_session.cookies)

#test_Session_remove_cookies()

# Generated at 2022-06-13 22:36:37.189652
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_file = './Session_test_sessions.json'
    os.system('rm ' + test_file)
    S = Session(test_file)
    S['cookies']['name1'] = 'value1'
    S['cookies']['name2'] = 'value2'
    S['cookies']['name3'] = 'value3'
    S.remove_cookies(['name2', 'name3'])
    assert S['cookies']['name1'] == 'value1'
    assert ('name2' not in S['cookies'])
    assert ('name3' not in S['cookies'])

# Generated at 2022-06-13 22:36:42.021534
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')

    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': 'value2'}
# Unit test ends

# Generated at 2022-06-13 22:36:48.592660
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_json = {"headers": {}, "cookies": {'cookie1': {'value': '1'}, 'cookie2': {'value': '2'}}}
    my_session = Session('test_session')
    my_session.update(session_json)
    my_session.remove_cookies(['cookie1'])
    assert my_session.json == {"headers": {}, "cookies": {'cookie2': {'value': '2'}}}
    my_session.remove_cookies(['cookie2'])
    assert my_session.json == {"headers": {}, "cookies": {}}

# Generated at 2022-06-13 22:36:53.013470
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = {'cookies': {'cookie1': 'value1', 'cookie2': 'value2'}}
    test_sess = Session('/home/user/example_session.json')
    test_sess.update(sess)
    names = ['cookie1', 'cookie2']
    test_sess.remove_cookies(names)
    assert test_sess == {'cookies': {}}

# Generated at 2022-06-13 22:36:58.357574
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'a': 'a', 'b': 'b'}
    session.remove_cookies(['a'])
    assert session['cookies'] == {'b': 'b'}

# Generated at 2022-06-13 22:37:09.328286
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Checks if remove_cookies removes cookies from session
    """
    session = Session('/tmp/sessions/session.json')
    session['cookies'] = {'name':{'value':'value'}}
    session.remove_cookies(['name'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:14.881497
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/')
    session['cookies'] = {'name': {'value': 'value'}}

    assert len(session['cookies']) == 1

    session.remove_cookies(['name'])

    assert len(session['cookies']) == 0

# Generated at 2022-06-13 22:37:19.362634
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('teste')
    sess['cookies'] = {'a': 1, 'b': 2}
    sess.remove_cookies(['a','d'])
    assert sess['cookies'] == {'b':2}

# Generated at 2022-06-13 22:37:29.553468
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_Session_remove_cookies.json')
    session['cookies'] = {
        'c1': {
            'value': 1,
            'path': '/',
            'secure': False,
            'expires': None
        },
        'c2': {
            'value': 2,
            'path': '/',
            'secure': False,
            'expires': None
        },
        'c3': {
            'value': 3,
            'path': '/',
            'secure': False,
            'expires': None
        },
    }
    assert len(session['cookies']) == 3
    session.remove_cookies(['c2', 'c3'])

# Generated at 2022-06-13 22:37:37.513356
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    t_session = Session('test_session.json')
    t_session['cookies'] = {'a':{'value':'aaaaaa'},'b':{'value':'bbbbbb'},'c':{'value':'cccccc'}}
    t_session.remove_cookies(['a','b'])
    assert(len(t_session['cookies']) == 1)
    assert(t_session['cookies'] == {'c':{'value': 'cccccc'}})

# Generated at 2022-06-13 22:37:41.434155
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test1')
    s['cookies']={'foo':{'value':'bar'},'foobar':{'value':'baz'}}
    s.remove_cookies(['foo','foobar'])
    assert s['cookies']=={}


# Generated at 2022-06-13 22:37:50.745579
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s.cookies = RequestsCookieJar()
    s.cookies.set('test_cookie_1', 'value1')
    s.cookies.set('test_cookie_2', 'value2')
    assert len(s.cookies) == 2
    s.remove_cookies(['test_cookie_1'])
    assert len(s.cookies) == 1
    s.remove_cookies(['test_cookie_3'])
    assert len(s.cookies) == 1
    s.remove_cookies(['test_cookie_2'])
    assert len(s.cookies) == 0

# Generated at 2022-06-13 22:37:57.594002
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    a = {}
    a['cookies'] = {}
    a['cookies']['session'] = {}
    a['cookies']['session']['value'] = 123
    a['cookies']['session1'] = {}
    a['cookies']['session1']['value'] = 123
    a['cookies']['session2'] = {}
    a['cookies']['session2']['value'] = 123
    Session.remove_cookies(a, ['session', 'session1'])
    assert len(a['cookies']) == 1
    assert 'session2' in a['cookies']
    assert 'session1' not in a['cookies']
    assert 'session' not in a['cookies']

# Generated at 2022-06-13 22:38:07.520061
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    c1 = {'name': 'a', 'value': 'a', 'path': '/'}
    c2 = {'name': 'b', 'value': 'b', 'path': '/'}
    c3 = {'name': 'c', 'value': 'c', 'path': '/'}
    s['cookies'] = {'a': c1, 'b': c2, 'c': c3}
    s.remove_cookies(['a', 'c'])
    assert s['cookies'] == {'b': c2}

# Generated at 2022-06-13 22:38:12.956515
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='test.json')
    session['cookies'] = '{name : test}'
    names = ['test']
    assert session['cookies'] == '{name : test}'
    session.remove_cookies(names)
    assert session['cookies'] != '{name : test}'


# Generated at 2022-06-13 22:38:28.306553
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(''))

# Generated at 2022-06-13 22:38:36.525817
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    expected_cookie_dict = {'key1': 'val1', 'key2': 'val2'}
    session = Session('path')
    session['cookies'] = expected_cookie_dict
    assert session['cookies'] == expected_cookie_dict
    session.remove_cookies(['key1'])
    assert session['cookies'] == {'key2': 'val2'}
    session.remove_cookies(['key3'])
    assert session['cookies'] == {'key2': 'val2'}
    session.remove_cookies(['key2'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:38:46.836163
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    jar = RequestsCookieJar()
    jar.set(
        'mock_cookie_name1', 'mock_cookie_value1', domain='example.org',
        path='/', expires=None, discard=True, comment=None, comment_url=None,
        rest=None, rfc2109=False
    )
    jar.set(
        'mock_cookie_name2', 'mock_cookie_value2', domain='example.org',
        path='/', expires=None, discard=True, comment=None, comment_url=None,
        rest=None, rfc2109=False
    )

# Generated at 2022-06-13 22:38:53.892622
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('dummy_path')
    session['cookies'] = { "cookie1" : {"value" : "value1"}}
    session.remove_cookies(["cookie2"])
    assert session['cookies'] == { "cookie1" : {"value" : "value1"}}
    session.remove_cookies(["cookie1"])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:38:59.057488
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/afile/someother-file.json')
    session.update({'cookies':{'c1':'mockValue', 'c2':'anotherValue'}})
    session.remove_cookies({'c2'})
    assert(session['cookies']['c1'])



# Generated at 2022-06-13 22:39:08.456279
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("./test_httpie_json_session")
    s.cookies = create_cookie('c1', 'v1')
    s.cookies = create_cookie('c2', 'v2')
    s.cookies = create_cookie('c3', 'v3')
    s.cookies = create_cookie('c4', 'v4')
    s.cookies = create_cookie('c5', 'v5')
    s.cookies = create_cookie('c6', 'v6')
    assert len(s['cookies']) == 6
    s.remove_cookies(['c1', 'c2'])
    assert len(s['cookies']) == 4


# Generated at 2022-06-13 22:39:10.787130
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('a')
    s.update_headers({'cookie': '"a=b"'})
    assert s.remove_cookies(['a'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:39:18.245529
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = RequestsCookieJar()
    cookies.set("name1", "value1", path="/", domain=".example.com", secure=True)
    cookies.set("name2", "value2", path="/", domain=".example.com", secure=True)
    cookies.clear_expired_cookies()
    session = Session("test")
    session.cookies = cookies
    session.remove_cookies(['name2'])
    assert 'name1' in session.cookies.get_dict().keys()
    assert 'name2' not in session.cookies.get_dict().keys()


# Generated at 2022-06-13 22:39:27.147682
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path.cwd() / 'test.json')
    session['cookies'] = dict(
        a=dict(value="A1A1A1A1", path="/"),
        b=dict(value="B2B2B2B2", path="/path")
    )
    session.remove_cookies(['a', 'c'])
    assert session['cookies'] == dict(b=dict(value="B2B2B2B2", path="/path"))


# Generated at 2022-06-13 22:39:39.119153
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    assert session.remove_cookies(['test']) == None, 'test1'
    session['cookies'] = {'test': {'value': 'test'}}
    assert session.remove_cookies(['test']) == None, 'test2'
    assert 'test' not in session['cookies'], 'test3'
    session['cookies'] = {'test1': {'value': 'test'}}
    assert session.remove_cookies(['test']) == None, 'test4'
    session['cookies'] = {}
    assert session.remove_cookies(['test']) == None, 'test5'
    assert session.remove_cookies(['test', 'test1']) == None, 'test6'

# Generated at 2022-06-13 22:39:59.117488
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    from httpie.sessions import Session
    from tempfile import NamedTemporaryFile
    from pathlib import Path

    with NamedTemporaryFile(mode='w+') as fp:
        session_path = Path(fp.name)
        session = Session(session_path)
        session['cookies'] = {'a': {}, 'b': {}, 'c': {}}
        session.remove_cookies(['a', 'b', 'd'])
        assert set(json.loads(session_path.read_text())['cookies'].keys()) == {'c'}

# Generated at 2022-06-13 22:40:06.809953
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test.json")
    #Normal case
    session['cookies'] = {"a": "1", "b": "2", "c": "3"}
    test_names = ["a", "d"]
    session.remove_cookies(test_names)
    assert len(session['cookies']) == 2
    assert "a" not in session['cookies']
    #Empty case
    session['cookies'] = {}
    test_names = []
    session.remove_cookies(test_names)
    assert len(session['cookies']) == 0
    #All case
    session['cookies'] = {"a": "1", "b": "2", "c": "3"}
    test_names = ["a", "b", "c"]
    session.remove_cookies(test_names)
   

# Generated at 2022-06-13 22:40:11.946782
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sp1 = Session(path = 'foo')
    sp1['cookies'] = {'1': '2'}
    assert sp1['cookies'] == {'1': '2'}
    sp1.remove_cookies(['1'])
    assert sp1['cookies'] == {}

# Generated at 2022-06-13 22:40:16.111143
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/test.json')
    s['cookies'] = {'name1': {'value': 'value1'}}
    s.remove_cookies(['name1'])
    assert s['cookies'] == {}


# Generated at 2022-06-13 22:40:24.515315
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_names = ['cookie_name1', 'cookie_name2', 'cookie_name3']
    session = Session("test_session.json")
    session.cookies = RequestsCookieJar()
    for name in cookie_names:
        session.cookies.set(name, 'value')
    session.remove_cookies(cookie_names[:2])
    # 3 cookies in Session.cookies
    assert len(session.cookies) == 3
    # session.cookies has 2 cookies
    session.remove_cookies(cookie_names)
    assert len(session.cookies) == 0

# Generated at 2022-06-13 22:40:26.259169
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('./test_session.json')
    session.load()
    session.remove_cookies('a')


# Generated at 2022-06-13 22:40:36.792987
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s=Session('temp.json')
    s.update_headers({'cookie': 'name1=value1;name2=value2'})
    assert len(s.cookies) == 2
    assert 'name1' in s.cookies
    assert 'name2' in s.cookies
    s.remove_cookies(['name1'])
    assert len(s.cookies) == 1
    assert 'name2' in s.cookies
    assert 'name1' not in s.cookies

# Generated at 2022-06-13 22:40:41.446200
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="test_path.json")
    session['cookies'] = {"name1": {"value": 1}}
    assert session['cookies'] == {"name1": {"value": 1}}
    session.remove_cookies(["name1"])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:40:45.214154
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s=Session('s.session')
    s['cookies']={'name1':'value1','name2':'value2','name3':'value3'}
    
    names=('name2','name3')
    s.remove_cookies(names)

    assert(s['cookies']=={'name1':'value1'})

# Generated at 2022-06-13 22:40:56.611549
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies_dict = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}}

    # Test 1: Assert that a cookie is removed from the Session.
    from httpie.sessions import Session
    session = Session('path')
    session['cookies'] = cookies_dict
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value2'}}

    # Test 2: Assert that a cookie is not removed from the Session.
    session = Session('path')
    session['cookies'] = cookies_dict
    session.remove_cookies(['cookie3'])
    assert session['cookies'] == cookies_dict

# Generated at 2022-06-13 22:41:30.252524
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("~/sessions.json")
    session.update_headers({
        "Cookie": "foo=bar"
    })
    session.remove_cookies(['foo'])
    assert len(session.cookies) == 0



# Generated at 2022-06-13 22:41:35.367481
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Remove cookies from session.

    """
    s = Session('')
    s['cookies'] = {'session': None, 'cookies': None}
    s.remove_cookies(['cookies', 'session'])
    assert s['cookies'] == {}



# Generated at 2022-06-13 22:41:41.866306
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path/to/session-file')
    session['cookies'] = {'c1': {'value': 'v1', 'path': '/', 'secure': True, 'expires': None},
                          'c2': {'value': 'v2', 'path': '/', 'secure': True, 'expires': None}}
    session.remove_cookies(('c1'))
    assert session['cookies']['c2']
    assert 'c1' not in session['cookies']
    session.remove_cookies(('c2', 'c3'))
    assert 'c2' not in session['cookies']

# Generated at 2022-06-13 22:41:57.133104
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.config import DEFAULT_CONFIG_DIR

    import pytest
    from requests.cookies import RequestsCookieJar
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.plugins.registry import plugin_manager
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.auth import BasicAuth
    from httpie.config import DEFAULT_CONFIG_DIR

    path = DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME / "session_test" / f'session_test_test.json'
    session = Session(path)
    session.load()

    session.update_headers(RequestHeadersDict({'User-Agent': 'test/test'}))

    jar = RequestsCookieJar()

# Generated at 2022-06-13 22:42:03.323916
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Context
    names = ['admin', 'session', 'user']
    session = Session('.')
    session['cookies'] = {name: {'value': '1234'} for name in ['admin', 'session']}

    # Remove the cookie session
    session.remove_cookies(names)

    # The cookie session is removed from session
    assert 'session' not in session['cookies']
    assert 'admin' in session['cookies']
    assert 'user' not in session['cookies']

# Generated at 2022-06-13 22:42:06.674947
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    a = Session('./cookies')

    a['cookies'] = {'key': 'value'}
    assert a.remove_cookies(['key']) == None
    assert  a['cookies'] == {}

# Generated at 2022-06-13 22:42:10.194428
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('path')
    sess['cookies'] = {'c1': {'value': 'val1'},
                       'c2': {'value': 'val2'}}
    sess.remove_cookies(['c1', 'c3'])
    assert sess['cookies'] == {'c2': {'value': 'val2'}}

# Generated at 2022-06-13 22:42:18.356755
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("")
    s.cookies = RequestsCookieJar()
    s.cookies.set('a', '1')
    s.cookies.set('b', '2')
    s.cookies.set('c', '3')
    s.cookies.set('d', '4')
    assert 2 == len(s['cookies'])
    s.remove_cookies(['a', 'b', 'c', 'd'])
    assert 0 == len(s['cookies'])

# Generated at 2022-06-13 22:42:22.695452
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/session')
    session['cookies'] = {'a': {'value': 'A'}, 'b': {'value': 'B'}, 'c': {'value': 'C'}}
    session.remove_cookies(['b', 'c'])
    assert (session['cookies'] == {'a': {'value': 'A'}})



# Generated at 2022-06-13 22:42:27.889521
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="/path/to/session/file.json")
    session['cookies'] = {
        'foo': {'value': 'bar1'},
        'baz': {'value': 'qux1'}
    }
    session.remove_cookies(names=['foo'])
    assert session['cookies'] == {
        'baz': {'value': 'qux1'}
    }