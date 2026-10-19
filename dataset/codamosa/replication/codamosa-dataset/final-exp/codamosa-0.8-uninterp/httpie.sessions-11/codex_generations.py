

# Generated at 2022-06-13 22:33:28.014551
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.argtypes import KeyValueArg
    request_headers = [
        KeyValueArg(name='Cookie', value='a=1; b=2'),
        KeyValueArg(name='Cookie', value='c=3; d=4'),
        KeyValueArg(name='User-Agent', value='HTTPie/0.9.9')
    ]
    request_headers = {str(kv_ar): kv_ar.value for kv_ar in request_headers}
    session = Session('.')
    session.update_headers(request_headers)
    print(session)


# Generated at 2022-06-13 22:33:32.713923
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    request_headers = RequestHeadersDict({'My-Header': 'my-value'})
    session.update_headers(request_headers)
    assert session['headers']['My-Header'] == 'my-value'

# Generated at 2022-06-13 22:33:37.275580
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path="/tmp/test_session.json")
    session.update_headers({"header1": "value1", "header2": "value2"})
    assert session.headers == {"header1": "value1", "header2": "value2"}



# Generated at 2022-06-13 22:33:45.358607
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.core import main
    from httpie.compat import str

    # Delete HTTPie session file
    os.remove('/home/lele/.config/httpie/sessions/localhost_5000/test.json')
    # Set up the HTTPie session
    main(['--session=test', 'localhost:5000', 'status=200'])

    # Create the Headers object
    headers = KeyValueArgType()(['a=b', 'c=d'])
    # Set up the session
    session = Session('/home/lele/.config/httpie/sessions/localhost_5000/test.json')
    # Mock the HTTP request
    session.update_headers(headers)
    # Check if the headers are correctly set in the Session
    assert session.get

# Generated at 2022-06-13 22:33:52.260665
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = str(DEFAULT_CONFIG_DIR / 'sessions' / 'fname.json')
    session = Session(path)
    session.update({'cookies': {'cname': {'value': 'cval'}}})
    session.remove_cookies(['cname'])
    assert session.get('cookies', {}) == {}



# Generated at 2022-06-13 22:34:00.090725
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("abc")
    session['cookies'] = {"a": {"value": 10}, "b": {"value":20}, "c": {"value":30}}
    session.remove_cookies(("a", "c"))
    assert session['cookies'] == {"b": {"value":20}}
    assert len(session['cookies'].keys()) == 1
    assert "a" not in session['cookies']
    assert "c" not in session['cookies']

# Generated at 2022-06-13 22:34:07.700371
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    ses = Session('/tmp/test_session')
    req_headers = {'user-agent':'test', 'host':'google.com', 'cookie':'test=123', 'if-modified-since':'1234'}
    ses.update_headers(req_headers)
    assert ses.headers['user-agent'] == 'test'
    assert ses.headers['host'] == 'google.com'
    assert ses['cookies'] == {'test': {'value': '123'}}
    assert 'if-modified-since' not in ses.headers

# Generated at 2022-06-13 22:34:21.245959
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict()
    headers['user_agent'] = 'HTTPie/Test'
    headers['content_type'] = 'application/json'
    headers['accept_encoding'] = 'gzip, deflate'
    headers['if_modified_since'] = '2020/03/03'
    headers['cookie'] = 'uid=test; name=test'

    session = Session('test_session_json')
    session.update_headers(headers)

    assert session.headers['user_agent'] == 'HTTPie/Test'
    assert session.headers['content_type'] == 'application/json'
    assert session.headers['accept_encoding'] == 'gzip, deflate'
    assert 'if_modified_since' not in session.headers
    assert 'cookie' not in session.headers


# Generated at 2022-06-13 22:34:28.934225
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    info = {
        'headers': {},
        'cookies': {}
    }
    request_headers = {
        'Content-Type': 'application/json',
        'Cookie': '_token=1234567; _session=abcdefg'
    }

    session = Session('./foo.json')
    session.update_headers(request_headers)

    assert request_headers == {
        'Content-Type': 'application/json',
        'Cookie': '_token=1234567; _session=abcdefg'
    }
    assert session == info

# Generated at 2022-06-13 22:34:34.576985
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict({'key1': 'value1'})
    session = Session(path='path')
    session.update_headers(headers)
    assert session['headers'] == headers


test_Session_update_headers()


# Generated at 2022-06-13 22:34:49.234085
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('session.json')
    session.update_headers(RequestHeadersDict({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'HTTPie/1.0.0',
        'cookie': 'session_id=abcdef; username=admin; roles=admin;',
        'Cookie': 'session_id=abcdef; username=admin; roles=admin;',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
        'authorization': 'Basic YWRtaW46cGFzc3dvcmQ=',
        'X-VERSION': '1',
    }))

# Generated at 2022-06-13 22:34:54.975724
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from requests.cookies import create_cookie
    s = Session('test')
    c = create_cookie('Test', 'Value')
    s['cookies']['Test'] = {'value': 'Value'}
    s.remove_cookies(['Test'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:35:06.937617
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import RequestHeadersDict

    session = Session('')
    session.headers = RequestHeadersDict({
        'Content-Type': 'application/json'
    })
    valid_cookie = SimpleCookie('foo=bar').output(header='', sep=';')
    httpie_cookie = SimpleCookie('HTTPIE_COOKIES=foo=bar').output(header='', sep=';')
    bad_cookie = SimpleCookie('foo: bar').output(header='', sep=';')
    valid_cookie_list = SimpleCookie('foo=bar; foo2=bar2').output(header='', sep=';')

    # Valid cookie string
    request_headers = RequestHeadersDict({
        'Cookie': valid_cookie
    })

# Generated at 2022-06-13 22:35:13.154553
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/test_Session_remove_cookies.json')
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(['a', 'b'])
    assert s['cookies'] == {'c': 3}

test_Session_remove_cookies()

# Generated at 2022-06-13 22:35:20.324752
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict()
    headers['wrong_header'] = 0
    headers['Accept-Encoding'] = 'gzip'
    headers['right_header'] = 'right'
    session = Session('sessions/test_session.json')
    session.update_headers(headers)
    assert session.headers.get('wrong_header') == None
    assert session.headers.get('Accept-Encoding') == None
    assert session.headers.get('right_header') == 'right'

# Generated at 2022-06-13 22:35:25.973785
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import CaseInsensitiveDict
    from httpie import ExitStatus
    original_headers = CaseInsensitiveDict({"Cookie": "123"})
    session = Session('test.json')
    session.update_headers(original_headers)

# Generated at 2022-06-13 22:35:35.589739
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    config_dir = DEFAULT_SESSIONS_DIR
    session_name = "session_test"
    host = "http://example"
    url = "http://example.com/test/main"
    session = get_httpie_session(config_dir, session_name, host, url)
    assert session.get('headers') == {}

    headers = {"Content-Type": "text/html"}
    session.update_headers(headers)
    assert session.get('headers') == {"Content-Type": "text/html"}

# Generated at 2022-06-13 22:35:45.788893
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    import pathlib
    import os
    import sys
    import unittest

    class SessionTest(unittest.TestCase):
        def setUp(self):
            self.filename = "test_session.json"
            self.directory = str(pathlib.Path(__file__).parent.absolute())+"\\..\\httpie"
            self.file = "{0}\\{1}".format(self.directory, self.filename)
            self.session = "testsession"

# Generated at 2022-06-13 22:35:51.220326
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    p = Path(__file__).parent / 'tests/.httpie/cookies/localhost/test.json'
    session = Session(p)
    assert 'cookie' in session['headers']

    session.remove_cookies(['cookie'])
    assert 'cookie' not in session['headers']

# Generated at 2022-06-13 22:36:00.312639
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Test case 1
    session = Session(path="")
    request_headers =RequestHeadersDict({'content-type':'application/json'})
    session.update_headers(request_headers)
    assert session.headers == {}
    # Test case 2
    session = Session(path="")
    request_headers =RequestHeadersDict({'key':'value'})
    session.update_headers(request_headers)
    assert session.headers == {}
    # Test case 3
    session = Session(path="")
    request_headers =RequestHeadersDict({'if-match':'etag', 'content-type':'application/json'})
    session.update_headers(request_headers)
    assert session.headers == {}
    # Test case 4
    session = Session(path="")

# Generated at 2022-06-13 22:36:14.218395
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("dummy")
    s['cookies'] = {
        "foo": {
            "value": 1,
            "path": "/foo/",
            "secure": True,
            "expires": "2020-02-01T00:00:00",
        },
        "bar-baz": {
            "value": 2,
            "path": "/bar/",
            "secure": True,
            "expires": "2020-02-02T00:00:00",
        },
        "qux": {
            "value": 3,
            "path": "/qux/",
            "secure": True,
            "expires": "2020-02-03T00:00:00",
        }
    }

# Generated at 2022-06-13 22:36:19.287419
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """ test_Session_remove_cookies """
    config = Session(Path('/tmp/mypath.json'))
    config['cookies'] = ['test1', 'test2', 'test3']
    config.remove_cookies(['test1', 'test2'])
    if len(config['cookies']) != 1:
        assert False

# Generated at 2022-06-13 22:36:28.494988
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    def assert_remove_cookies(input_cookies, to_remove, expected):
        obj = Session(path='test')
        obj['cookies'] = input_cookies
        obj.remove_cookies(to_remove)
        assert expected == obj['cookies']

    assert_remove_cookies(
        input_cookies={'a': '1', 'b': '2'},
        to_remove=['a', 'c'],
        expected={'b': '2'}
    )
    assert_remove_cookies(
        input_cookies={'a': '1', 'b': '2', 'a': '3'},
        to_remove=['b', 'c'],
        expected={'a': '3'}
    )

# Generated at 2022-06-13 22:36:33.102361
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
   session = Session('path')
   session['cookies'] = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
   session.remove_cookies(['k2', 'k4'])
   assert session['cookies'] == {'k1': 'v1', 'k3': 'v3'}


# Generated at 2022-06-13 22:36:40.612309
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    jar = RequestsCookieJar()
    jar.set('a', '1')
    jar.set('b', '2')
    jar.set('c', '3')
    session = Session('/path/to/sessions/dir/')
    session.cookies = jar
    session.remove_cookies(['a', 'b'])
    assert (session.cookies ==
            RequestsCookieJar([cookie for cookie in jar if cookie.name == 'c']))



# Generated at 2022-06-13 22:36:48.067476
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = "test_Session_remove_cookies.json"
    session = Session(path)
    session.load()
    session['cookies']['cookie1'] = {'value':'cookie1_value'}
    session['cookies']['cookie2'] = {'value':'cookie2_value'}
    session['cookies']['cookie3'] = {'value':'cookie3_value'}
    session.save()
    session.remove_cookies(['cookie1', 'cookie2'])
    assert set(session['cookies'].keys()) == {'cookie3'}
    session.delete()

# Generated at 2022-06-13 22:36:50.962339
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('sessions/session.json')
    cookies = ['bofa', 'citi', 'chase']
    session.remove_cookies(cookies)
    assert session == {}

# Generated at 2022-06-13 22:36:58.952139
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('games')
    s['cookies'] = {}
    s['cookies'] = {'name': 'John'}
    s['cookies'] = {'name': 'Alice'}

    assert s['cookies'] == {'name': 'Alice'}

    s['cookies'] = {'name': 'John'}
    s['cookies'] = {'name': 'Alice'}
    s.remove_cookies(['name'])

    assert s['cookies'] == {}



# Generated at 2022-06-13 22:37:02.196780
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = os.getcwd()+'/tests/sessions/test'
    session = Session(path)
    session.load()
    session.remove_cookies(['A'])
    assert 'A' not in session['cookies']

# Generated at 2022-06-13 22:37:10.437060
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {
        "name1": {},
        "name2": {},
        "name3": {}
    }
    assert list(session['cookies'].keys()) == ["name1", "name2", "name3"]
    session.remove_cookies(["name1", "name2", "name4"])
    assert list(session['cookies'].keys()) == ["name3"]
    session.remove_cookies(["name2", "name4"])
    assert list(session['cookies'].keys()) == ["name3"]

# Generated at 2022-06-13 22:37:29.182072
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #setup
    session = {}
    session['cookies'] = {}
    session['cookies']['cookie1'] = {'key1': 'value1', 'key2': 'value2'}
    session['cookies']['cookie2'] = {'key1': 'value1', 'key2': 'value2'}
    session['cookies']['cookie3'] = {'key1': 'value1', 'key2': 'value2'}
    #exercise
    session.remove_cookies({'cookie1', 'cookie2'})
    #verify
    assert session['cookies']['cookie1'] is None
    assert session['cookies']['cookie2'] is None
    assert session['cookies']['cookie3'] is not None

# Generated at 2022-06-13 22:37:35.462277
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s: Session = Session("tmp")
    s["cookies"] = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
    }
    s.remove_cookies(["key1"])
    assert "key1" not in s["cookies"]


# Generated at 2022-06-13 22:37:44.207549
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    ses = Session('./test_session.json')
    ses['cookies'] = {'name1':{'value':'name1'}, 'name2':{'value':'name2'}}
    ses.remove_cookies(['name1', 'name2'])
    assert ses['cookies'] == {}
    ses['cookies'] = {'name1':{'value':'name1'}, 'name2':{'value':'name2'}}
    ses.remove_cookies(['name2', 'name1'])
    assert ses['cookies'] == {}
    ses['cookies'] = {'name1':{'value':'name1'}, 'name2':{'value':'name2'}, 'name3':{'value':'name3'}}
    ses

# Generated at 2022-06-13 22:37:48.345652
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
        session = Session('test')
        dict_test = {'test': 'test'}
        session['cookies'] = dict_test

        session.remove_cookies(('test','test2'))
        assert 'test' not in session['cookies']


# Generated at 2022-06-13 22:37:51.324488
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='/home/pontus/test.json')
    session.load()
    session.remove_cookies(['cookie2'])
    print(session)



# Generated at 2022-06-13 22:37:59.564986
# Unit test for method remove_cookies of class Session

# Generated at 2022-06-13 22:38:05.640318
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(''))
    cookies = {
        'abc': {},
        'def': {},
        'hij': {}
    }
    session['cookies'] = cookies
    session.remove_cookies(['abc', 'hij'])
    assert session['cookies'] == {'def': {}}



# Generated at 2022-06-13 22:38:12.081154
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('temp_session.json')
    session['cookies'] = {'Cookies': {'value': 'Chocolate'}, 'Biscuit': {'value': 'Other type'}}
    session.remove_cookies({'Cookies', 'Other'})
    assert session['cookies'] == {'Biscuit': {'value': 'Other type'}}

# Generated at 2022-06-13 22:38:16.125297
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    dummy_session_path = 'dummy_session.json'
    dummy_session = Session(dummy_session_path)
    dummy_session['cookies'] = {'cookie_name': {'value': 'cookie_value'}}
    dummy_session.remove_cookies(['cookie_name'])
    assert dummy_session['cookies'] == {}
    os.remove(dummy_session_path)

# Generated at 2022-06-13 22:38:24.621859
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    from httpie.compat import Path

    session = Session(Path('test_session'))
    session.load()
    test_cookies = json.loads(
        '{"cookies": {"sessionid": {"value": "test"}, "csrftoken": '
        '{"value": "test"}}}'
    )
    session.update(test_cookies)
    assert 'sessionid' in session['cookies']
    session.remove_cookies('sessionid')
    assert 'sessionid' not in session['cookies']

# Generated at 2022-06-13 22:38:48.098656
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session=Session(path="httpie.session")
    session['cookies']={'csrftoken':{'value':'vV8WySJEuR7GihuIGo2QV8WZm4q1d7Ey'},'sessionid':{'value':'h2t7ybdozwvz845bkf319u0p1jvx9xuc'}}
    session.remove_cookies(('csrftoken',))
    assert 'csrftoken' not in session['cookies']

test_Session_remove_cookies()



# Generated at 2022-06-13 22:38:59.461228
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    t = Session("test_path")
    t.cookies = RequestsCookieJar()

    t['cookies']['cookie_name'] = {'value': 'cookie_value'}
    t['cookies']['another_cookie_name'] = {'value': 'another_cookie_value'}

    assert t['cookies'] == {
        'cookie_name': {'value': 'cookie_value'},
        'another_cookie_name': {'value': 'another_cookie_value'}
    }

    t.remove_cookies(['cookie_name'])

    assert t['cookies'] == {
        'another_cookie_name': {'value': 'another_cookie_value'}
    }

# Generated at 2022-06-13 22:39:04.201373
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test_Session_remove_cookies')
    s['cookies'] = {
        'foo': {'value': 'bar'},
        'bar': {'value': 'baz'},
    }
    s.remove_cookies(['foo'])
    assert s['cookies'] == {'bar': {'value': 'baz'}}

# Generated at 2022-06-13 22:39:13.421312
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(None)
    session.update({'cookies': {'c1': {'value': 1}, 'c2': {'value': 2}}})
    assert session['cookies']['c1']['value'] == 1
    assert session['cookies']['c2']['value'] == 2
    session.remove_cookies(['c1'])
    assert 'c1' not in session['cookies']
    assert session['cookies']['c2']['value'] == 2
    session = Session(None)
    session.update({'cookies': {'c1': {'value': 1}, 'c2': {'value': 2}}})
    assert session['cookies']['c1']['value'] == 1

# Generated at 2022-06-13 22:39:20.198377
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # write contents in 'test_remove_cookies'
    session = Session('test_remove_cookies')
    session.cookies = [{'name': 'name1', 'value': 'value1'}, {'name': 'name2',
                                                              'value': 'value2'}]
    session.save()
    session.load()
    session.remove_cookies(['name1'])
    # pass name1, so the corresponding cookie should be deleted
    assert session['cookies']['name1'] == None
    assert session['cookies']['name2'] != None
    session.remove_cookies(['name2'])
    assert session['cookies']['name2'] == None
    # delete file 'test_remove_cookies' after test
    session.delete()

# Generated at 2022-06-13 22:39:25.761741
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path='./httpie_session.json')
    s['cookies'] = {'name': 'value', 'name2': 'value2'}
    s.remove_cookies(names=['name2'])
    assert s['cookies'] == {'name': 'value'}

# Generated at 2022-06-13 22:39:32.394762
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie1 = {}
    cookie1["name"] = "Test 1"
    cookie1["attname"] = "attname Test 1"
    cookie1["value"] = "value Test 1"
    cookie2 = {}
    cookie2["name"] = "Test 2"
    cookie2["attname"] = "attname Test 2"
    cookie2["value"] = "value Test 2"
    cookie3 = {}
    cookie3["name"] = "Test 3"
    cookie3["attname"] = "attname Test 3"
    cookie3["value"] = "value Test 3"
    cookie4 = {}
    cookie4["name"] = "Test 4"
    cookie4["attname"] = "attname Test 4"
    cookie4["value"] = "value Test 4"
    session = Session("C:\\test.json")
    session

# Generated at 2022-06-13 22:39:38.116340
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Arrange
    session = Session("MySession")
    jar = RequestsCookieJar()
    names = ['foo', 'bar']
    for name in names:
        jar.set_cookie(create_cookie(name, "value"))
    session.cookies = jar

    # Act
    session.remove_cookies(names)

    # Assert
    assert not session['cookies']

test_Session_remove_cookies()

# Generated at 2022-06-13 22:39:52.106005
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('tmp')
    session['cookies']['a'] = '1'
    session['cookies']['b'] = '2'
    session['cookies']['c'] = '3'
    session.remove_cookies(['a', 'c'])
    assert ['b'] == list(session['cookies'].keys())


    assert not VALID_SESSION_NAME_PATTERN.match('httpie.org')
    assert VALID_SESSION_NAME_PATTERN.match('httpie-org')
    assert not VALID_SESSION_NAME_PATTERN.match('http://httpie.org')
    assert not VALID_SESSION_NAME_PATTERN.match('httpie.org/')

# Generated at 2022-06-13 22:39:56.140518
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("fake_path")
    session['cookies'] = {"cookie_1": 1, "cookie_2": 2, "cookie_3": 3}
    session.remove_cookies(("cookie_1", "cookie_3"))
    assert session['cookies'] == {"cookie_2": 2}

# Generated at 2022-06-13 22:40:42.478099
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class CookieJar:
        def __init__(self, cookie_list):
            self.cookie_list = cookie_list
        def __iter__(self):
            return iter(self.cookie_list)
    class Cookie:
        def __init__(self, name, value, path, secure, expires):
            self.name = name
            self.value = value
            self.path = path
            self.secure = secure
            self.expires = expires
    myjar = CookieJar([])
    myjar.cookie_list.append(Cookie("Cookie1","Cookie1_value","/",False,None))
    myjar.cookie_list.append(Cookie("Cookie2","Cookie2_value","/",False,None))

# Generated at 2022-06-13 22:40:47.649305
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_sessions_dir')
    session['cookies'] = {
        'sessionid': {'value': '1'},
        'csrftoken': {'value': '2'},
    }
    names = ['sessionid', 'csrftoken']
    session.remove_cookies(names)
    assert session['cookies'] == {
        'sessionid': {'value': '1'},
    }
    session.remove_cookies(['sessionid'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:40:56.646162
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("/tmp/test_remove_cookies_session.json")
    assert not s.get("cookies")
    s["cookies"] = {"name1": 1, "name2": 2, "name3": 3, "name4": 4, "name5": 5}
    assert s.get("cookies")
    assert len(s.get("cookies")) == 5
    s.remove_cookies(["name1", "name3", "name5"])
    assert len(s.get("cookies")) == 2
    assert s.get("cookies") == {"name2": 2, "name4": 4}

# Generated at 2022-06-13 22:41:01.997685
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    ses = Session("tests/fixtures/session.json")
    ses.update_headers({'Host':'www.google.com', 'Cookie':'Name=Anurag'})
    names = ['Name', 'Value']
    ses.remove_cookies(names)
    assert 'Name' not in ses.cookies

# Generated at 2022-06-13 22:41:07.163175
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = get_httpie_session(
        config_dir=DEFAULT_CONFIG_DIR,
        session_name="test",
        host="http://localhost",
        url="http://localhost/index.html")

    session['cookies']["cookie 1"] = '{"value": "1"}'
    session['cookies']["cookie 2"] = '{"value": "2"}'

    session.remove_cookies(["cookie 1", "cookie 3"])

    assert session['cookies'] == {'cookie 2': {'value': '2'}}

# Generated at 2022-06-13 22:41:12.290759
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_path = Path('./test.json')
    session = Session(session_path)
    class Dummy:
        cookie_dict = 'cookie_dict'
        name = 'name'
    session.cookies = Dummy()
    session.remove_cookies(names=['name'])
    assert session.cookies != Dummy().cookie_dict

# Generated at 2022-06-13 22:41:20.682145
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Unit test for method remove_cookies of class Session

    :return:
    """
    session = Session(path='path')
    session['cookies']['session_cookie'] = '9a9a'
    session['cookies']['non_session_cookie'] = '9a9b'
    session.remove_cookies(['session_cookie'])
    assert 'non_session_cookie' in session['cookies']
    assert 'session_cookie' not in session['cookies']



# Generated at 2022-06-13 22:41:28.016522
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('~/.config/httpie/localhost_8000/my_session.json')
    session['cookies'] = {'cookie1': {'value': 'foo'}}

    session.remove_cookies(['cookie1'])
    assert not session['cookies']
    session.remove_cookies(['cookie2'])
    assert not session['cookies']

# Generated at 2022-06-13 22:41:33.007676
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('.')
    session['cookies'] = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    session.remove_cookies(['key1', 'key2'])
    assert session['cookies'] == {'key3': 'value3'}

# Generated at 2022-06-13 22:41:41.145935
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Test for Session.remove_cookies
    """
    config_dir = DEFAULT_CONFIG_DIR
    session_name = 'test_remove_cookies'
    path = (config_dir / SESSIONS_DIR_NAME / session_name / 'test_remove_cookies.json')
    session = Session(path)
    session.load()
    session['cookies'] = {'cookie_1': {'value': 'cook_1'}, 'cookie_2': {'value': 'cook_2'}}
    session.remove_cookies(('cookie_1', 'cookie_3'))
    assert session['cookies'] == {'cookie_2': {'value': 'cook_2'}}

# Generated at 2022-06-13 22:43:12.686321
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import time
    import json

    session_data = '{"cookies": {"foo": {"path": "/", "value": "a", "secure": true, "expires": 789456}, '\
                   '"bar": {"path": "/", "value": "b", "secure": true, "expires": 789456}}}'
    session = Session('~/test.json')
    session.update(json.loads(session_data))
    session.remove_cookies(['foo', 'bar'])
    assert not 'cookies' in session
    assert not session
    session = Session('~/test.json')
    session.update(json.loads(session_data))
    session.remove_cookies(['nonexist'])
    assert len(session['cookies']) == 2

# Generated at 2022-06-13 22:43:20.792560
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import requests  # The test depends on the type of RequestsCookieJar
    init = {'cookies': {'foo': {'value': 1}, 'bar': {'value': 2}}}
    session = Session('/dev/null')
    session.update(init)
    assert type(session.cookies) == requests.cookies.RequestsCookieJar
    assert session.get('cookies') == init.get('cookies')
    session.remove_cookies(['foo','bar'])
    assert session.get('cookies') == {}