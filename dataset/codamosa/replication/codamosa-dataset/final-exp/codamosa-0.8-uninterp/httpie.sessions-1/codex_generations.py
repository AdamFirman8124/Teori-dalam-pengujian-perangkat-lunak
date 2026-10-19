

# Generated at 2022-06-13 22:33:28.083069
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("test")
    s.cookies = RequestsCookieJar()
    s.cookies.set("test1", "test")
    s.cookies.set("test2", "test")
    s.cookies.set("test3", "test")
    assert s["cookies"]["test1"]["value"] == "test"
    assert s["cookies"]["test2"]["value"] == "test"
    assert s["cookies"]["test3"]["value"] == "test"
    s.remove_cookies(["test1", "test2"])
    assert s["cookies"].__contains__("test1") == False
    assert s["cookies"].__contains__("test2") == False

# Generated at 2022-06-13 22:33:40.763945
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # GIVEN

    class MockRequestsHeadersDict(RequestHeadersDict):
        def __init__(self):
            self.__content = {
                'Host': 'example.com',
                'Connection': 'keep-alive',
                'Cookie': 'foo=bar; bar=baz',
                'Content-Length': '123',
                'If-None-Match': 'Foo',
                'User-Agent': 'HTTPie/1.0.0',
                'Accept': '*/*',
                'Foo': 'Bar'
            }

        def __getitem__(self, key: str) -> str:
            return self.__content[key]

        def __contains__(self, key: str) -> bool:
            return key in self.__content


# Generated at 2022-06-13 22:33:46.633334
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    class RequestHeadersDictBase:
        content_type = 'Content-Type'
        accept_charset = 'Accept-Charset'
        host = 'Host'
        content_length = 'Content-Length'

    request_headers = RequestHeadersDictBase()
    request_headers[request_headers.content_length] = '4'
    request_headers[request_headers.content_type] = 'application/json'

    session = Session('')
    session.update_headers(request_headers)

    assert session.headers[session.content_type] == 'application/json'
    assert session.headers[session.content_length] == '4'
    assert not session.headers[session.host]

# Generated at 2022-06-13 22:33:52.412443
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/')
    session.update_headers({'accept': 'application/json'})
    assert session.headers == {'accept': 'application/json'}
    session.update_headers({'accept': 'application/xml'})
    assert session.headers == {'accept': 'application/xml'}


# Generated at 2022-06-13 22:34:03.771558
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    session.update_headers({'User-Agent': 'HTTPie/0.13.0',
                            'Accept': 'application/json',
                            'Cookie': 'jsession=xxx; wcs_bt=s_xxx:xxx',
                            'Content-Type': 'application/json',
                            'If-Match': 'xxx',
                            'If-Modified-Since': 'xxx',
                            'If-None-Match': 'xxx'})

    assert session.headers == {
        'User-Agent': 'HTTPie/0.13.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        }

# Generated at 2022-06-13 22:34:15.458363
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = os.path.join(
        os.path.dirname(__file__),
        'session_example',
    )

    with open(path, 'r') as session_handler:
        s = Session(session_handler)

    test_dict = {
        'cookies': {
            'cookie1': 'value1',
            'cookie2': 'value2',
            'cookie3': 'value3',
        },
    }

    s.update(test_dict)
    s.remove_cookies(['cookie2'])

    assert s['cookies'] == {
        'cookie1': 'value1',
        'cookie3': 'value3',
    }

# Generated at 2022-06-13 22:34:26.280854
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import RequestHeadersDict
    session = Session("test")
    request_headers = RequestHeadersDict({"Cookie": "cookie 1", "If-Modified-Since": "Wed, 21 Oct 2015 07:28:00 GMT", "User-Agent": "HTTPie/0.9.9", "Accept-Encoding": "gzip, deflate"})
    session.update_headers(request_headers)
    assert session.headers == RequestHeadersDict({"Accept-Encoding": "gzip, deflate"})
    assert session.cookies.get("cookie").value == "1"


# Generated at 2022-06-13 22:34:34.015300
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/non-existing-path')
    session.update_headers({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'HTTPie/0.9.9',
        'If-Modified-Since': '0',
        'Cookie': 'foo=bar; baz=qux',
        'Host': 'localhost:5000'
    })
    assert session['headers'] == {
        'Accept': 'application/json',
        'Host': 'localhost:5000'
    }
    assert session['cookies'] == {'foo': {'value': 'bar'},
                                  'baz': {'value': 'qux'}}



# Generated at 2022-06-13 22:34:37.262784
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path = "TestSession")
    session.update_headers({"Content-Type": "text/plain; charset=utf-8"})
    print(session['headers'])
    assert session['headers'] == {}

# Generated at 2022-06-13 22:34:45.940117
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session.json')
    dict_headers = {'Test-Headers1': 'Test-Value1', 'Test-Headers2': 'Test-Value2'}
    headers = RequestHeadersDict(dict_headers)
    # test the function update_headers
    session.update_headers(headers)

    # check the result
    expected_headers = RequestHeadersDict({'Test-Headers2': 'Test-Value2'})
    assert session.headers == expected_headers

# Generated at 2022-06-13 22:35:02.205382
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path='')

    request_headers = {'user-agent': 'HTTPie/0.9.9', 'cookie': 'a=b; c=d;'}
    session.update_headers(request_headers)

    assert session.headers['user-agent'] == 'HTTPie/0.9.9'
    assert session.cookies['a'].value == 'b'
    assert session.cookies['c'].value == 'd'

    # Test cookie is not updated
    request_headers = {'cookie': 'a=e;'}
    session.update_headers(request_headers)
    assert session.cookies['a'].value == 'b'

# Generated at 2022-06-13 22:35:07.359628
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_file.json')
    session['cookies'] = {'name1': {'value': 'value1'}, 'name2': {'value': 'value2'}}
    session.remove_cookies(['name1'])
    assert session['cookies'] == {'name2': {'value': 'value2'}}



# Generated at 2022-06-13 22:35:17.806272
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('example')
    session.cookies = RequestsCookieJar()
    cookie1 = create_cookie('name1', 'value1')
    cookie2 = create_cookie('name2', 'value2')
    cookie3 = create_cookie('name3', 'value3')
    session.cookies.set_cookie(cookie1)
    session.cookies.set_cookie(cookie2)
    session.cookies.set_cookie(cookie3)
    session.remove_cookies(['name1', 'name2'])
    assert session.cookies.get_dict() == {'name3': 'value3'}


# Generated at 2022-06-13 22:35:24.883112
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('example_session')
    session.cookies = create_cookie('1', 'a'), create_cookie('2', 'b')
    assert len(session.cookies) == 2

    session.remove_cookies(['3'])
    assert list(session.cookies) == ['2']

    session.remove_cookies(['2'])
    assert not list(session.cookies)

    session.remove_cookies(['1'])
    assert not list(session.cookies)

# Generated at 2022-06-13 22:35:30.657367
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('C:\\Documents\\Python_Projects\\httpie\\httpie\\session.json')
    s['cookies'] = {'user': 'admin',
                    'passwd': 'admin'}
    s.remove_cookies(['user'])
    assert s['cookies'] == {'passwd': 'admin'}


# Generated at 2022-06-13 22:35:37.136187
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path='/test')
    jar = RequestsCookieJar()
    jar.set('test_cookie_1', 'test_value_1', path='/test/')
    jar.set('test_cookie_2', 'test_value_2', path='/test/')
    s.cookies = jar
    assert len(s['cookies']) == 2
    s.remove_cookies(['test_cookie_1'])
    assert len(s['cookies']) == 1
    assert next(iter(s['cookies'].keys())) == 'test_cookie_2'

# Generated at 2022-06-13 22:35:50.187669
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test.json')
    session.update_headers({'Accept': 'text/html'})
    assert session['headers'] == {'Accept': 'text/html'}
    session.update_headers({'Cookie': 'Name=Value'})
    assert session['cookies'] == {'Name': {'value': 'Value'}}
    session.update_headers({'User-Agent': 'HTTPie/0.9.9'})
    assert not session['headers'].get('User-Agent')
    session.update_headers({'Content-Type': 'Your mom', 'User-Agent': 'Your mom'})
    assert not session['headers'].get('Content-Type')
    session.update_headers({'If-Match': '*'})
    assert not session['headers'].get('If-Match')
    session

# Generated at 2022-06-13 22:35:55.247903
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from pprint import pprint
    session = Session('D:\Python\HTTPie\httpie\config.json')
    session['cookies'] = {'abc': '123', 'efg': '456'}
    session.remove_cookies(['abc'])
    pprint(session)

# Generated at 2022-06-13 22:36:06.883266
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    print("Testing method remove_cookies of class Session")

    dummy_jar = RequestsCookieJar()
    dummy_jar.set_cookie(
        create_cookie(name='a', value='a_value',  path='/a_path', expires=3600)
    )
    dummy_jar.set_cookie(
        create_cookie(name='b', value='b_value', path='/b_path', expires=3600)
    )
    dummy_jar.set_cookie(
        create_cookie(name='c', value='c_value', path='/c_path', expires=3600)
    )

    session = Session('dummy_path')
    session.cookies = dummy_jar

    names_to_remove = ['a', 'b', 'D']

# Generated at 2022-06-13 22:36:15.070445
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from requests.cookies import RequestsCookieJar
    from httpie.cli.argtypes import KeyValue
    from httpie.compat import is_windows
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.context import Environment

    class MockSession(Session):
        """A mock Session class for the test, where read() and write() are
        replaced by load() and save().

        """
        def load(self):
            self.update(dict(
                headers=dict(
                    self['headers']
                ),
                cookies=dict(
                    self['cookies']
                ),
                auth=dict(
                    type='basic',
                    username='user',
                    password='password'
                )
            ))


# Generated at 2022-06-13 22:36:26.076618
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {}
    cookies['name1'] = {'value':'value1'}
    cookies['name2'] = {'value':'value2'}
    cookies['name3'] = {'value':'value3'}
    session = {"cookies": cookies}
    assert len(session['cookies']) == 3
    names = ['name1', 'name3']
    Session.remove_cookies(session, names)
    assert len(session['cookies']) == 1
    assert 'name1' not in session['cookies']
    assert 'name3' not in sess

# Generated at 2022-06-13 22:36:31.515699
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path("/tmp/session.json"))
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value2'}}

# Generated at 2022-06-13 22:36:34.980829
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class Session(object):
        def __init__(self):
            self.cookies = {}
    session = Session()
    session.cookies = {'cookie1': 'cookie1', 'cookie2': 'cookie2'}
    session.remove_cookies(['cookie1'])
    assert session.cookies == {'cookie2': 'cookie2'}

# Generated at 2022-06-13 22:36:40.016048
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('dummy')
    session['cookies'] = {'A': 1, 'B': 2, 'C': 3}
    session.remove_cookies(['A', '3'])
    attributes = {'cookies': {'B': 2, 'C': 3}}
    assert session.dict() == attributes

# Generated at 2022-06-13 22:36:47.119942
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    c = {}
    i = 0
    while i < 3:
        c[str(i)] = i
        i += 1
    s = Session(path='A\\B')
    s.update({'cookies': c})
    s.remove_cookies(['1', '0', '5'])
    assert '1' not in s['cookies']
    assert s['cookies']['2'] == 2
    try:
        s.remove_cookies('s')
    except Exception as e:
        assert type(e) == TypeError



# Generated at 2022-06-13 22:36:55.146010
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.core import main
    from utils import http, HTTP_OK, MOCK_BASE_URL, MockEnvironment
    env = MockEnvironment()
    env.config['sessions']['default'] = {
        'name': 'https://example.org',
        'path': '/tmp/httpie-sessions-xxx'
    }
    env.config['sessions']['path'] = '/tmp/httpie-session-dir-xxx'
    env.config.dir = Path(env.config['sessions']['path'])
    session = Session(f"{env.config['sessions']['path']}/example.org.json")
    session.save()

# Generated at 2022-06-13 22:37:02.791033
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'cookie1': 'cookie1value', 'cookie2': 'cookie2value'}
    session_obj = Session('dummy_path.json')
    session_obj['cookies'] = cookies

    session_obj.remove_cookies(['cookie1', 'cookie2'])

    assert session_obj['cookies'] == {}

# Generated at 2022-06-13 22:37:08.285841
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(r'~/.config/httpie/sessions/vk.com/httpie-session.json'))
    session.load()
    session.remove_cookies(['remixsid'])
    session.save()


# Generated at 2022-06-13 22:37:13.563901
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('session/test/test.json')
    s['cookies'] = {'test': dict(value='test'), 'test2': dict(value='test2')}
    s.remove_cookies(['test', 'test2'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:37:25.581523
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.config import Config
    from httpie.context import Environment
    from httpie.plugins import plugin_manager

    config = Config(env=Environment())
    plugin_manager.load_installed_plugins(config)

    session = Session('test.json')
    session['cookies'] = {
        'cookie1': {'value': 'value1'},
        'cookie2': {'value': 'value2'},
        'cookie3': {'value': 'value3'}
    }
    session.remove_cookies(['cookie1', 'cookie2'])
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' not in session['cookies']
    assert session['cookies'] == {'cookie3': {'value': 'value3'}}



# Generated at 2022-06-13 22:37:35.075426
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.sessions import Session
    assert(Session)

# Generated at 2022-06-13 22:37:41.958965
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # test data
    session_path = Path('/Users/chenjian/httpie/test_session.json')
    session = Session(path=session_path)
    session['headers'] = {}
    session['cookies'] = {
        'username': {'value': 'chenjian'},
        'password': {'value': '123456'},
    }
    # test data

    assert len(session['cookies']) == 2
    assert session['cookies']['password']['value'] == '123456'
    # test data
    session.remove_cookies(['username', 'password'])
    # test data

    assert len(session['cookies']) == 0

# Generated at 2022-06-13 22:37:50.370785
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session.update_headers({'cookie': 'c1=1; c2=2'})
    assert len(session.cookies) == 2
    assert {'c1': '1', 'c2': '2'} == {c.name: c.value for c in session.cookies}
    session.remove_cookies(['c1'])
    assert len(session.cookies) == 1
    assert {'c2': '2'} == {c.name: c.value for c in session.cookies}


# Generated at 2022-06-13 22:37:53.633923
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("localhost")
    session['cookies'] = {"one":"val_one", "two":"val_two"}
    session.remove_cookies(["one"])
    assert session['cookies'] == {"two":"val_two"}



# Generated at 2022-06-13 22:37:59.814642
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #Assign
    session = Session("/Users/gabrielsaccone/.httpie/sessions/localhost/_2000/google.json")
    names = ["SSID", "APISID", "CONSENT", "SID"]
    #Act
    session.remove_cookies(names)
    #Assert
    assert(not("SSID" in session["cookies"].keys()))
    assert(not("APISID" in session["cookies"].keys()))
    assert (not("CONSENT" in session["cookies"].keys()))
    assert (not("SID" in session["cookies"].keys()))



# Generated at 2022-06-13 22:38:08.081112
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("/path/to/session")
    session['cookies'] = {'one': {'value': '1'}, 'two': {'value': '2'}}
    session.remove_cookies(['one'])
    assert {'two': {'value': '2'}} == session['cookies']
    session.remove_cookies(['three'])
    assert {'two': {'value': '2'}} == session['cookies']

# Generated at 2022-06-13 22:38:14.009630
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    from unittest.mock import patch

    s = Session(path='path')
    s['cookies'] = {'one': 1, 'two': 2}

    with patch('httpie.sessions.Session.save') as mock_obj:
        s.remove_cookies(names=['one'])
        mock_obj.assert_called_once()
        assert s['cookies'] == {'two': 2}

# Generated at 2022-06-13 22:38:20.317862
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'test1': 'test1', 'test2': 'test2', 'test3': 'test3'}
    session.remove_cookies(['test1', 'test3'])
    assert session['cookies'] == {'test2': 'test2'}



# Generated at 2022-06-13 22:38:25.700950
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s['cookies'] = {"cookie_1": {'value': 'value_1'}, "cookie_2": {'value': 'value_2'}}
    s.remove_cookies(["cookie_1"])
    assert s['cookies'] == {"cookie_2": {'value': 'value_2'}}



# Generated at 2022-06-13 22:38:34.332080
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_Session_remove_cookies')
    session['cookies'] = {
        'cookie1' : {'value' : 'value1'},
        'cookie2' : {'value' : 'value2'},
        'cookie3' : {'value' : 'value3'},
    }
    session.remove_cookies(['cookie1', 'cookie3'])
    assert session['cookies'] == {'cookie2' : {'value' : 'value2'}}

# Generated at 2022-06-13 22:38:46.327605
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session['cookies'] = {"foo": {"value": "123"},
                          "bar": {"value": "456"},
                          "baz": {"value": "789"}}
    session.remove_cookies(['foo', 'foo', 'bar'])
    assert session['cookies'] == {"baz": {"value": "789"}}

# Generated at 2022-06-13 22:38:54.541699
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = (Path.home() / 'config') / SESSIONS_DIR_NAME
    path.mkdir(parents=True, exist_ok=True)
    path = path / 'Session_remove_cookies.json'
    session = Session(path)
    session['cookies'] = {'C1': {}, 'C2': {}, 'C3': {}}
    session.remove_cookies(['C1', 'C2'])
    assert session['cookies'] == {'C3': {}}


# Generated at 2022-06-13 22:38:58.706012
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Test unitario per la rimozione di cookies
    :return:
    """


# Generated at 2022-06-13 22:39:04.514843
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='wow')
    session['cookies'] = {'cookie1': '', 'cookie2': ''}
    session.remove_cookies(names=['cookie1'])
    assert session['cookies'] == {'cookie2': ''}
    session['cookies'] = {'cookie1': ''}
    session.remove_cookies(names=['cookie1'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:39:13.618267
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class DummyAuth(AuthBase):
        def __init__(self, username=None, password=None):
            self.raw_auth = f'{username}:{password}'

    cookies_dict = {'cookie_1': 'value_1', 'cookie_2': 'value_2'}
    cookies = RequestsCookieJar()
    for name, value in cookies_dict.items():
        cookies.set_cookie(create_cookie(name, value))

    session = Session('/tmp/test.json')
    session.headers['test'] = 'test'
    session.cookies = cookies
    session.auth = {'type': 'auth-type', 'raw_auth': 'raw_auth'}

    # remove specific cookies
    session.remove_cookies(['cookie_1'])

# Generated at 2022-06-13 22:39:17.800320
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session.json')
    session.update_headers(RequestHeadersDict({"Cookie": "session_id=a;remove_me=b"}))
    session.remove_cookies(["remove_me"])
    assert not session.headers
    assert session["cookies"] == {'session_id': {'value': 'a'}}

# Generated at 2022-06-13 22:39:23.157480
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/x.json')
    s['cookies'] = {'a': 'b'}
    s.remove_cookies(['a'])
    assert 'a' not in s['cookies']

# Generated at 2022-06-13 22:39:29.300299
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    assert s.cookies.keys() == []
    s.cookies = RequestsCookieJar()
    s.cookies.set('cookie1', 'value1')
    s.cookies.set('cookie2', 'value2')
    assert len(s.cookies.keys()) == 2
    s.remove_cookies(['cookie1'])
    assert len(s.cookies.keys()) == 1
    assert s.cookies.get_dict().get('cookie1') is None

# Generated at 2022-06-13 22:39:36.350104
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    httpie_session = Session('https://httpie.org/test_Session_remove_cookies')
    httpie_session['cookies'] = {'A': {'value':'a'}, 'B': {'value':'b'}, 'C': {'value':'c'}}
    httpie_session.remove_cookies(['A', 'C'])
    assert httpie_session['cookies'] == {'B':{'value':'b'}}

# Generated at 2022-06-13 22:39:37.913815
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    Session.remove_cookies(['c0'])
    Session.remove_cookies({'c0'})

# Generated at 2022-06-13 22:39:52.620371
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('~/.httpie/session.json')
    session.update_headers({"Content-Type": "application/json", "User-Agent": "HTTPie/1.0.3", "Connection": "keep-alive"})
    assert session.headers.get("Content-Type") is None
    assert session.headers.get("User-Agent") is not None

# Generated at 2022-06-13 22:39:58.954563
# Unit test for constructor of class Session
def test_Session():
    assert(VALID_SESSION_NAME_PATTERN.match('oneline').group() == 'oneline')
    assert(VALID_SESSION_NAME_PATTERN.match('more.time.than.oneline') == None)
    assert(VALID_SESSION_NAME_PATTERN.match('spaces are not allowed') == None)
    assert(VALID_SESSION_NAME_PATTERN.match('../is not allowed') == None)
    assert(VALID_SESSION_NAME_PATTERN.match('./is not allowed') == None)


# Generated at 2022-06-13 22:40:04.406825
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(None)
    session['headers'] = {}
    # test updating headers
    test_header = {'test_key': 'test_value'}
    session.update_headers(test_header)
    assert session['headers'] == {'test_key': 'test_value'}
    # test updating headers with empty headers
    session.update_headers({})
    assert session['headers'] == {'test_key': 'test_value'}


# Generated at 2022-06-13 22:40:12.765533
# Unit test for function get_httpie_session
def test_get_httpie_session():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    config_dir = os.path.join(
        this_dir, os.pardir, os.pardir, 'examples', 'config')
    session = get_httpie_session(config_dir, 'test', 'https://example.com', 'https://example.com')
    assert session.get('headers') == {'Host': 'example.com'}
    assert session.get('auth') == {'type': 'basic'}

# Generated at 2022-06-13 22:40:23.056173
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    class MockSession(Session):
        def __init__(self):
            super().__init__(path=None)
            self.headers = RequestHeadersDict()
    s = MockSession()
    rh = RequestHeadersDict()
    rh.add('Cookie', 'foo=bar; baz=qux')
    rh.add('Content-Type', 'text/html')
    rh.add('X-BAR', 'qux')
    rh.add('X-Foo-Bar', 'baz')
    s.update_headers(rh)
    assert s['headers'] == {
        'x-bar': 'qux',
        'x-foo-bar': 'baz'
    }

# Generated at 2022-06-13 22:40:26.161724
# Unit test for function get_httpie_session
def test_get_httpie_session():
    config_dir = DEFAULT_CONFIG_DIR
    session_name = 'session'
    url = 'http://127.0.0.1/test/test.html'
    host = '127.0.0.1'
    get_httpie_session(config_dir, session_name, host, url)

# Generated at 2022-06-13 22:40:34.029081
# Unit test for function get_httpie_session
def test_get_httpie_session():
    session_name = 'secret_session'
    config_dir = DEFAULT_CONFIG_DIR
    host = None
    url = 'http://127.0.0.1:8888'

    session = get_httpie_session(
        config_dir,
        session_name,
        host,
        url
    )

    assert session != None, "session should not be None"

# Generated at 2022-06-13 22:40:40.249934
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session_headers = {"X-Session-Header": "session-value"}
    request_headers = {"X-Session-Header": "request-value"}
    session = Session(Path('/dummy/path'))
    original = session.headers
    session.update_headers(request_headers)
    assert session.headers != original
    assert session.headers != request_headers


# Generated at 2022-06-13 22:40:48.020628
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('~/test')
    session.update({
        'headers': {
            'HTTP_HOST': 'localhost:8000',
            'HTTP_ACCEPT': '*/*'
        },
        'cookies': {
            'sessionid': {'value': '1jg4f6o4tx36rb4uj9njk7ycj6wz1kp8'},
            'csrftoken': {'value': 'q8eGWNVM0hJk1QlYmjqc3tuuAavetNzZ'}
        },
        'auth': {
            'type': 'basic',
            'username': 'user',
            'password': 'password'
        }
    })

    session.remove_cookies(['sessionid'])
    assert 'sessionid'

# Generated at 2022-06-13 22:40:53.805062
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test")
    session['cookies'] = {'test': {'value': 'test'}}
    assert len(session['cookies']) == 1
    session.remove_cookies(['test'])
    assert len(session['cookies']) == 0


# Generated at 2022-06-13 22:41:12.511857
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    this_session = Session('test_session.json')
    this_session['cookies'] = {'foo': 'bar'}
    
    assert this_session['cookies'] == {'foo': 'bar'}
    this_session.remove_cookies(['foo'])
    assert this_session['cookies'] == {}

# Generated at 2022-06-13 22:41:15.389006
# Unit test for constructor of class Session
def test_Session():
    assert Session(path=Path(DEFAULT_SESSIONS_DIR))




# Generated at 2022-06-13 22:41:22.519824
# Unit test for function get_httpie_session
def test_get_httpie_session():
    session_name = "my-session"
    url = "https://foo.bar/"
    config_dir = Path('~/') / '.config'
    host = 'localhost:123'
    s = get_httpie_session(config_dir, session_name, host, url)
    assert s['path'] == (Path('~') / '.config' / SESSIONS_DIR_NAME / 'localhost_123' / 'my-session.json')
    assert s.create_dirs
    assert s.create_file


# Generated at 2022-06-13 22:41:34.689182
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.session import Session

    session = Session('/tmp/test_Session_remove_cookies_session.tmp')
    session.update(dict(cookies={'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}))
    assert session['cookies'] == {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    session.remove_cookies(['c1'])
    assert session['cookies'] == {'c2': {'value': 'v2'}}
    session.remove_cookies(['c2'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:41:43.247804
# Unit test for function get_httpie_session
def test_get_httpie_session():
    from httpie.config import Config

    config_dir = Config.DEFAULT_CONFIG_DIR.parent.parent / 'tests/fixtures'

    session = get_httpie_session(
        config_dir,
        session_name='no_hostname_known',
        host=None,
        url='http://localhost:8080/',
    )
    assert 'localhost_8080/no_hostname_known.json' == str(session._path)
    assert {'Host': 'localhost:8080'} == session.headers

    session = get_httpie_session(
        config_dir,
        session_name='hostname_known',
        host='www.example.org',
        url='http://hostname_known/',
    )

# Generated at 2022-06-13 22:41:49.182909
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies(): 
    s = Session()
    s['cookies'] = {'a': 1, 'b': 2}
    s.remove_cookies(['a', 'c'])
    assert s['cookies'] == {'b': 2}



# Generated at 2022-06-13 22:41:50.530455
# Unit test for constructor of class Session
def test_Session():
    path = "session.json"
    session = Session(path)
    assert isinstance(session, dict)

if __name__ == "__main__":
    test_Session()

# Generated at 2022-06-13 22:42:03.011606
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # 没有用户名密码的请求头
    request_headers = {'Accept-Language': 'zh-CN',
                       'Cache-Control': 'no-cache',
                       'Connection': 'keep-alive'}
    # 创建session对象
    session = Session('test_session.json')
    # 执行update_headers方法
    session.update_headers(request_headers)
    # 检查headers是否等于request headers
    assert (session.headers == request_headers)

    # 有用户名密码的请求头

# Generated at 2022-06-13 22:42:07.609531
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/')
    session['cookies'] = {'name1': 'value1', 'name2': 'value2', 'name3': 'value3'}
    names = ['name1', 'name4']
    session.remove_cookies(names)
    assert session['cookies'] == {'name2': 'value2', 'name3': 'value3'}

# Generated at 2022-06-13 22:42:20.787629
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.plugins.builtin import HTTPBasicAuth, HTTPAuthPlugin
    session = Session("/test/test.json")
    session.update_headers({"Host": "example.com", "Content-Type": "application/json"})
    assert "host" in session["headers"]
    assert "content-type" in session["headers"]
    session.update_headers({"User-Agent": "HTTPie/1.0.2"})
    assert "user-agent" not in session["headers"]
    session.update_headers({"Cookie": "session=1"})
    assert "cookie" not in session["headers"]
    assert "session" in session["cookies"]
    session.update_headers({"Accept": None})
    assert "accept" not in session["headers"]

    auth_plugin = HTTPAuthPlugin

# Generated at 2022-06-13 22:42:57.860748
# Unit test for constructor of class Session
def test_Session():
    sess = Session('/path/to/a/file')
    sess.load()

# Generated at 2022-06-13 22:43:08.932146
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import pytest
    path = Path('/tmp')
    session_name = 'test_session'
    host = None
    url = 'http://www.google.com'
    session = get_httpie_session(path, session_name, host, url)

    session['cookies'] = {'name1':'value1', 'name2':'value2'}
    session.remove_cookies(['name1'])
    assert session['cookies'] == {'name2':'value2'}

# Generated at 2022-06-13 22:43:13.032552
# Unit test for constructor of class Session
def test_Session():
    from pathlib import Path
    import os
    os.mkdir("./sessions")
    Path('./sessions').mkdir(parents=True, exist_ok=True)
    Session('./sessions')
