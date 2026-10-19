

# Generated at 2022-06-13 22:33:28.150830
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Test 1 : Test simple remove cookies
    session = Session(path=Path('./test.json'))
    session['cookies'] = {'h3': 5, 'v': 7}
    session.remove_cookies(['h3','v'])
    assert session['cookies'] == {}
    # Test 2 : Test there is no cookie to remove
    session = Session(path=Path('./test.json'))
    session['cookies'] = {'h3': 5, 'v': 7}
    session.remove_cookies(['h4','v5', 'v'])
    assert session['cookies'] == {'h3': 5, 'v': 7}
    # Test 3 : Remove nonexistent cookies
    session = Session(path=Path('./test.json'))
    session['cookies'] = {}


# Generated at 2022-06-13 22:33:38.869506
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('./test_sessions/Session_remove_cookies')

    # Create a cookie
    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie('test_cookie', 'test_value'))
    session.cookies = jar

    # Test removing the cookie
    session.remove_cookies(['test_cookie'])
    assert session.headers == {}
    assert session.cookies == RequestsCookieJar()

    # Test removing an non-existing cookie
    session.remove_cookies(['test_cookie'])
    assert session.headers == {}
    assert session.cookies == RequestsCookieJar()


# Generated at 2022-06-13 22:33:44.722344
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli import parse_items
    session = Session(path="sessions/test")
    session.load()
    session.cookies = parse_items('Cookie', [
        'foo=bar',
        'baz=qux',
        'name=value',
        'state=CA'
    ])
    session.remove_cookies(['baz', 'state'])
    assert 'baz' not in session['cookies']
    assert 'foo' in session['cookies']
    assert 'state' not in session['cookies']

# Generated at 2022-06-13 22:33:50.835238
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/bla/bla')
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(['a', 'b', 'd'])
    assert s['cookies'] == {'c': 3}

# Generated at 2022-06-13 22:33:56.783576
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/test_Session_update_headers.json')
    request_headers = {'Connection': 'close', 'User-Agent': 'HTTPie/2.2.0'}
    session.update_headers(request_headers)
    expected_headers = {'Connection': 'close'}
    assert session.headers == expected_headers

# Generated at 2022-06-13 22:34:04.184711
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_list = ['foo', 'bar']
    cookie_list2 = ['foo', 'buzz']
    session = Session(path='')
    session['cookies'] = {'foo': 'bar', 'buzz': 'bar'}
    session.remove_cookies(cookie_list)
    assert {'buzz': 'bar'} == session['cookies']
    session.remove_cookies(cookie_list2)
    assert {'buzz': 'bar'} == session['cookies'] # Session is empty

# Generated at 2022-06-13 22:34:09.871626
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    test_obj = Session("test")
    request_headers = {'Host': 'localhost', 'Cookie': 'x'}
    test_obj.update_headers(request_headers)
    assert test_obj['headers'] == {}
    assert test_obj['cookies'] == {"x": {"value": "x"}}

# Generated at 2022-06-13 22:34:19.692258
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session_obj = Session(Path('myfile.json'))
    request_headers = {'Content-Type': 'application/json',
                       'If-Match': '"abc"',
                       'Cookie': 'lang=en-US; csrftoken=1234'}
    session_obj.update_headers(request_headers)
    assert session_obj['headers'] == {}
    assert session_obj['cookies'] == {'lang': {'value': 'en-US'}, 'csrftoken': {'value': '1234'}}


# Generated at 2022-06-13 22:34:27.287050
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = 'asd'
    session = Session(path)
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie(
        "first", 'value1'))
    session.cookies.set_cookie(create_cookie(
        "second", 'value2',path='/'))
    session.remove_cookies(['first'])
    result = session.cookies.get_dict()
    expected = {'second': 'value2'}
    assert result == expected


# Generated at 2022-06-13 22:34:32.883470
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    print("\n test_Session_update_headers")
    s = Session("./sessions/test.json")
    list_headers = RequestHeadersDict()
    list_headers['Content-Type'] = "text/html"
    s.update_headers(list_headers)
    print(s['headers'])
    assert type(s['headers']) is dict
    assert type(s['headers']['Content-Type']) is str


# Generated at 2022-06-13 22:34:45.779607
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/home/user/.config/httpie/sessions/stackoverflow.com/token.json')
    session['cookies'] = {'persistent': {'value': 'true', 'domain': 'stackoverflow.com', 'path': '/', 'expires': '2018-04-29 14:58:59.174277'}}
    cookies_names = ['persistent', 'not_exist']
    session.remove_cookies(cookies_names)
    assert 'persistent' not in session.cookies.__dict__['_cookies']

# Generated at 2022-06-13 22:34:53.492462
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('a_path'))
    session['cookies'] = {'k1': 'v1', 'k2': 'v2'}
    session.remove_cookies(['k1'])
    assert session['cookies'] == {'k2': 'v2'}
    session.remove_cookies(['k2'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:35:04.312201
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.compat import urlopen
    from httpie.input import ParseError

    request_headers = RequestHeadersDict({
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Type': 'text/html',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=E9F17888516C0715A3C5E5C2D6D28AF6.tomcat3',
        'custom-header': 'Custom header value',
        'Pragma': 'no-cache',
        'User-Agent': 'HTTPie/0.9.2',
    })

    session = Session

# Generated at 2022-06-13 22:35:12.906054
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Session.remove_cookies must remove one or more cookies from self['cookies']
    dict.
    """
    session = Session('/test')
    session['cookies'] = {'test1': {}, 'test2': {}}
    session.remove_cookies(['test1'])
    assert session['cookies'] == {'test2': {}}
    session.remove_cookies(['test2', 'test3'])
    assert not session['cookies']

# Generated at 2022-06-13 22:35:19.549352
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(None)
    session['cookies'] = {'cookie_1': 'cookie_1', 'cookie_2': 'cookie_2', 'cookie_3': 'cookie_3'}
    session.remove_cookies(['cookie_1', 'cookie_2'])
    assert session.get('cookies') == {'cookie_3': 'cookie_3'}


# Generated at 2022-06-13 22:35:27.423262
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # given
    session = Session('foo.json')
    session['cookies'] = {'foo': 'bar', 'baz': 'qux'}

    # when
    session.remove_cookies(['baz'])

    # then
    assert len(session['cookies']) == 1
    assert 'foo' in session['cookies']
    assert 'baz' not in session['cookies']



# Generated at 2022-06-13 22:35:33.359934
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('')
    request_headers = {'foo-bar': '42', 'Content-Length': '134'}
    s.update_headers(request_headers)
    assert s.headers == {'foo-bar': '42'}
    assert request_headers == {'foo-bar': '42', 'Content-Length': '134'}



# Generated at 2022-06-13 22:35:44.167357
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.input import KeyValueArg
    from httpie.models import Request
    from httpie import cli
    session = Session('./test.json')
    request_headers = RequestHeadersDict()
    request_headers['content-type'] = 'application/json'
    request_headers['If-Modified-Since'] = 'Mon, 30 Jan 2006 01:01:01 GMT'
    request_headers['Content-Encoding'] = 'foobar'
    request_headers['cookie'] = 'foo=bar'
    request_headers['user-agent'] = 'HTTPie/0.9.9'
    args = cli.parser.parse_args([])
    args.session = 'test'
    request = Request(args, config=cli.Config())
    request.headers = request_headers
    request.session = session


# Generated at 2022-06-13 22:35:54.092091
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.input import KeyValue
    from httpie.config import UserConfig

    config = UserConfig()
    session = Session(config.config_dir / 'foo.json')
    # 准备要传入的headers
    headers = RequestHeadersDict()
    for item in ('a', 'b', 'Content-type', 'Date', 'If-Modified-Since',
                    'User-Agent', 'Cookie'):
        headers[item] = 'value'
    headers['Content-Type'] = 'application/json'
    headers['Cookie'] = 'A=A'
    headers['User-Agent'] = 'HTTPie/0.9.9'
    headers['Date'] = 'Sat, 11 Jul 2020 14:08:58 GMT'

# Generated at 2022-06-13 22:35:59.390305
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('test_session.json'))
    session['cookies'] = {
        "USER_TOKEN": "",
        "USER_TOKEN_NEW": "",
    }
    session.remove_cookies(["USER_TOKEN", "USER_TOKEN_NOT_EXIST"])
    assert session['cookies'] == {
        "USER_TOKEN_NEW": "",
    }


# Generated at 2022-06-13 22:36:11.992709
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('dummy')
    request_headers = RequestHeadersDict()

    session.update_headers(request_headers)
    assert session['headers'] == {}

    request_headers['Accept'] = 'application/json'
    request_headers['Cookie'] = 'a=3'
    assert request_headers['Cookie'] == 'a=3'

    session.update_headers(request_headers)
    assert session['headers'] == {'Accept': 'application/json'}
    assert session['cookies'] == {'a': {'value': '3'}}

# Generated at 2022-06-13 22:36:12.660619
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    assert True


# Generated at 2022-06-13 22:36:21.610102
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.plugins import plugin_manager
    from httpie.auth.plugins import AuthPlugin
    plugin_manager.set('auth', [AuthPlugin()])

    ses = Session('')
    ses.cookies = RequestsCookieJar()
    ses.cookies.set_cookie(create_cookie('test_cookie', '123'))
    assert (ses.cookies.get_dict() == {'test_cookie': '123'})
    ses.remove_cookies(['test_cookie'])
    assert (ses.cookies.get_dict() == {})

# Generated at 2022-06-13 22:36:26.885403
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = {'A': 1, 'b': None, 'c': '123'}
    session = Session('test.json')
    session.update_headers(headers)
    assert session['headers'] == {'A': '1', 'c': '123'}
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:36:32.257545
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {'cookie1': {'value':'value1', 'path':'/'}, 'cookie2': {'value':'value2', 'path':'/'}}
    session.remove_cookies(['cookie1', 'cookie3'])
    assert session['cookies'] == {'cookie2': {'value':'value2', 'path':'/'}}

# Generated at 2022-06-13 22:36:43.800542
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_name = 'cookie_name'
    cookie_value = 'cookie_value'
    remove_cookie_name = 'remove_cookie_name'
    remove_cookie_value = 'remove_cookie_value'
    session = Session('example')
    session['cookies'] = {cookie_name: {'value' : cookie_value},
                          remove_cookie_name: {'value' : remove_cookie_value}}
    # test for removing a cookie
    session.remove_cookies([remove_cookie_name])
    assert remove_cookie_name not in session['cookies']
    # test for removing a cookie that is not present in the session
    session.remove_cookies(['notpresent_cookie'])
    assert remove_cookie_name not in session['cookies']
    # test for removing a cookie that is not present in the

# Generated at 2022-06-13 22:36:48.484343
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import tempfile
    tf = tempfile.NamedTemporaryFile(suffix=".json")
    session = Session(tf.name)
    names = ['foo', 'bar', 'baz']
    session.remove_cookies(names)
    assert 'cookies' not in session.raw

    session['cookies'] = dict()
    session.remove_cookies(names)
    assert 'cookies' not in session.raw


# Generated at 2022-06-13 22:36:52.120907
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test_Session_remove_cookies")
    session['cookies'] = {'key1': 'value1', 'key2': 'value2'}

    session.remove_cookies(['key1', 'key3'])
    assert session['cookies'] == {'key2': 'value2'}

# Generated at 2022-06-13 22:36:54.977710
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    a = Session(Path("test.json"))
    a['cookies'] = {'test': {'test': '1'}, 'test2': {'test': '1'}}
    a.remove_cookies(['test'])
    if 'test' in a['cookies']:
        raise Exception("test not removed")



# Generated at 2022-06-13 22:36:57.924342
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('./test.json')
    session = Session(path)
    session.load()
    session.remove_cookies(['cookie1'])
    print(session['cookies'])

# Generated at 2022-06-13 22:37:11.420858
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    session.update_headers({'foo': 'bar'})
    assert session.headers == {'foo': 'bar'}

    session.update_headers({'foo': 'bar2'})
    assert session.headers == {'foo': 'bar2'}

    session.update_headers({'foo': ''})
    assert session.headers == {'foo': ''}

    session.update_headers({'foob': 'ar2'})
    assert session.headers == {'foo': '', 'foob': 'ar2'}

    session.update_headers({'foo': 'ar3'})
    assert session.headers == {'foo': 'ar3', 'foob': 'ar2'}

    session.update_headers({'fo': 'ar2'})

# Generated at 2022-06-13 22:37:20.021660
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names = ["test1", "test2"]
    session = Session(None)
    session['cookies'] = {"test1": "test1", "test2": "test2"}
    session['cookies']['test1'] = "test1"
    assert session.get('cookies') == {"test1": "test1", "test2": "test2"}

    session.remove_cookies(names)
    assert session.get('cookies') == {}

# Generated at 2022-06-13 22:37:25.343152
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {'foo': 'bar', 'qux': 'quux'}

    session.remove_cookies(['qux'])
    assert 'qux' not in session['cookies']


# Generated at 2022-06-13 22:37:31.476550
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    c = {'name': 'test'}
    s = Session("/tmp/test")
    s['cookies'] = c
    assert(s['cookies'] == {'name': 'test'})
    s.remove_cookies(['name'])
    assert(s['cookies'] == {})



# Generated at 2022-06-13 22:37:37.715762
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test1.json")
    session['cookies'] = {'cookie1': {'value': 'cookie1-value'}, 'cookie2': {'value': 'cookie2-value'}}
    session.remove_cookies(['cookie2'])
    assert len(session['cookies']) == 1
    session.remove_cookies(['cookie1'])
    assert len(session['cookies']) == 0

# Generated at 2022-06-13 22:37:43.785002
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from collections import OrderedDict
    from httpie.compat import is_py26

    s = Session("")
    s['cookies'] = OrderedDict([("a",1),("b",2),("c",3)])
    s.remove_cookies(("a","c"))
    # OrderedDict in python2.6 does not have method keys
    # so we convert to a list to test the result
    if is_py26:
        assert list(s['cookies']) == ["b"]
    else:
        assert s['cookies'].keys() == ["b"]

# Generated at 2022-06-13 22:37:53.537510
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('')
    assert s.update_headers({'a':'b'}) is None
    assert s.headers == {'a':'b'}
    assert s.update_headers({'B':'a'}) is None
    assert s.headers == {'a':'b','B':'a'}
    assert s.update_headers({'HTTPie/0.9.9': 'a'}) is None
    assert s.headers == {'a':'b','B':'a'}
    assert s.update_headers({'coOkie': 'c=d'}) is None
    assert s.headers == {'a':'b','B':'a'}
    assert s.update_headers({'If-Range': 'a'}) is None

# Generated at 2022-06-13 22:37:55.650919
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session.json')
    session.load()
    session.remove_cookies(['foo'])


# Generated at 2022-06-13 22:38:06.491333
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=None)
    session.load()
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie('name1','value1','domain','path'))
    session.cookies.set_cookie(create_cookie('name2','value2','domain','path'))
    assert len(session.cookies) == 2

    session.remove_cookies(['name1'])
    assert len(session.cookies) == 1

    session.remove_cookies(['name2'])
    assert len(session.cookies) == 0


# Generated at 2022-06-13 22:38:15.505275
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.context import Environment
    from httpie.config import Config
    from httpie.sessions import Session

    config = Config(env=Environment())
    config_dir = config.directory
    session_name = 'test_session'
    url = 'http://127.0.0.1:8080/'
    host = None

    session = get_httpie_session(config_dir, session_name, host, url)
    original_size = len(session['cookies'])
    session['cookies'] = {'foo': {'value': 'bar'}, 'abc': {'value': 'xyz'}}
    session.save()
    session.load()
    assert len(session['cookies']) == 2
    session.remove_cookies(['foo'])
    session.save()
    session.load

# Generated at 2022-06-13 22:38:23.949265
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("path")
    session['cookies'] = {'cookies_name': 'cookie'}
    session.remove_cookies(['cookies_name'])
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:38:27.161199
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('dummy_path')
    session['cookies'] = {'test_cookie': {'value': '1'}}
    session.remove_cookies(['test_cookie'])

    assert ('test_cookie' not in session['cookies'])

# Generated at 2022-06-13 22:38:37.357135
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    example_cookies = {
        'user_id': {'value': '1'},
        'user_name': {'value': 'Alex'},
        'session_id': {'value': '00c922a2'},
    }
    session = Session(DEFAULT_SESSIONS_DIR/'test.json')
    session['cookies'] = example_cookies
    assert len(session['cookies']) == 3
    session.remove_cookies(example_cookies)
    assert len(session['cookies']) == 0
    session['cookies'] = example_cookies
    assert len(session['cookies']) == 3
    session.remove_cookies(['user_id', 'user_name'])
    assert len(session['cookies']) == 1

# Generated at 2022-06-13 22:38:43.307550
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {
        'cookie1': dict(value='1'),
        'cookie2': dict(value='2'),
        'cookie3': dict(value='3'),
    }
    session.remove_cookies(['cookie2', 'cookie3'])
    assert session['cookies'] == {
        'cookie1': dict(value='1'),
    }



# Generated at 2022-06-13 22:38:56.535404
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.compat import is_windows

    if is_windows:
        return
    s = Session(path='/tmp/test_session')
    s['cookies'] = {}
    s.remove_cookies(names=['key1'])
    assert s['cookies'] == {}
    s['cookies']['key1'] = 'value1'
    s['cookies']['key2'] = 'value2'
    s.remove_cookies(names=['key1','key2'])
    assert s['cookies'] == {}
    s['cookies']['key1'] = 'value1'
    s['cookies']['key2'] = 'value2'
    s.remove_cookies(names=['key1'])

# Generated at 2022-06-13 22:39:01.773210
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {'name1': 'value1', 'name2': 'value2'}
    s.remove_cookies(['name1', 'name3'])
    assert s == {'headers': {}, 'cookies': {'name2': 'value2'}}

# Generated at 2022-06-13 22:39:05.699632
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('TestSession')
    sess['cookies']['name1'] = 'value1'
    sess['cookies']['name2'] = 'value2'
    sess['cookies']['name3'] = 'value3'
    sess['cookies']['name4'] = 'value4'
    sess.remove_cookies(['name1', 'name3', 'name5'])
    assert sess['cookies'] == {'name2': 'value2', 'name4': 'value4'}


# Generated at 2022-06-13 22:39:06.891342
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # TODO: implement
    pass


# Generated at 2022-06-13 22:39:15.107935
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies_str = '''
    session=
    __cfduid=
    guest_id=v1%3A152652017859367967
    _ga=
    personalization_id=
    twid=
    swift_session_id=
    '''
    cookies_list = cookies_str.strip().split('\n')
    cookies = {
        cookie.split('=')[0]: cookie.split('=')[1]
        for cookie in cookies_list
    }
    session = Session('test')
    session['cookies'] = cookies
    session.remove_cookies(('session', 'personalization_id', '_ga'))

# Generated at 2022-06-13 22:39:27.698803
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from datetime import date
    from dateutil.tz import tzutc
    from requests.cookies import RequestsCookieJar
    from httpie import config

    session = Session(config.DEFAULT_SESSIONS_DIR / 'test_session')

    session['cookies'] = {'foo': {}}
    session['cookies']['bar'] = {'value': 'baz'}
    session['cookies']['baz'] = {'value': 'qux', 'expires': date(1999, 3, 2)}
    session['cookies']['qux'] = {
        'value': 'spam',
        'expires': date(1999, 3, 2).replace(tzinfo=tzutc()),
    }

# Generated at 2022-06-13 22:39:39.249314
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    target = Session('')
    target['cookies'] = {'a': 'b', 'c': 'd'}
    target.remove_cookies(['a', 'd'])
    assert target['cookies'] == {'c': 'd'}

# Generated at 2022-06-13 22:39:46.276612
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    x_session = Session('.')
    x_session['cookies'] = {'foo': {'value': 'b'}, 'bar': {'value': 'a'}}
    x_session.remove_cookies(['foo', 'bar'])
    assert dict() == x_session['cookies']

# Generated at 2022-06-13 22:39:58.100196
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.compat import is_windows
    from httpie.context import Environment
    env = Environment(config_dir=os.getcwd())
    path = str(DEFAULT_SESSIONS_DIR / 'localhost/test.json')
    session = Session(path)
    session.load()
    cookie_saved = "Cookie: PHPSESSID=hq3fq6q2q14k8g6i1tes9b88p6"
    cookie_not_saved = "Cookie: bg1=black; bg2=white"
    cookie_saved_not_modified = "Cookie: bg1=black; bg2=white; PHPSESSID=hq3fq6q2q14k8g6i1tes9b88p6"

# Generated at 2022-06-13 22:40:06.506220
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class my_cookies(RequestsCookieJar):
        my_cookies = [
            {'name': 'aaa', 'value': '111', 'path': '/'},
            {'name': 'bbb', 'value': '222', 'path': '/'},
            {'name': 'ccc', 'value': '333', 'path': '/'},
        ]
        def __init__(self):
            super().__init__()
            for cookie in self.my_cookies:
                self.set_cookie(
                    create_cookie(
                        cookie['name'],
                        cookie['value'],
                        **cookie))

    # Init my_cookies
    my_cookiejar = my_cookies()
    assert len(my_cookiejar) == 3
    # Remove cookies in my_cookiejar by method remove_cookies

# Generated at 2022-06-13 22:40:11.243417
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_SessionObject = Session("test")
    test_SessionObject['cookies'] = {'testcookie': {'value': 'testvalue'}}
    test_SessionObject.remove_cookies(['testcookie'])
    assert 'testcookie' not in test_SessionObject['cookies']

# Generated at 2022-06-13 22:40:17.014776
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/testFile')
    s['cookies'] = {
        'key1' : {'value' : 'val1'},
        'key2' : {'value' : 'val2'},
    }
    s.remove_cookies(['key2'])
    assert s['cookies'] == {
        'key1' : {'value' : 'val1'},
    }

# Generated at 2022-06-13 22:40:25.998295
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('my_session')
    session.cookies = RequestsCookieJar()
    session.cookies.set('a', 'A')
    session.cookies.set('b', 'B')
    session.cookies.set('c', 'C')
    session.cookies.set('d', 'D')
    session.cookies.set('e', 'E')
    assert sorted(session.cookies.keys()) == ['a', 'b', 'c', 'd', 'e']

    # Remove multiple cookies
    session.remove_cookies(['b', 'd'])
    assert sorted(session.cookies.keys()) == ['a', 'c', 'e']

    # Remove non-existing cookie
    session.remove_cookies(['x'])

# Generated at 2022-06-13 22:40:41.242716
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Example Session
    session = Session("~/httpie-session.json")

    # Set cookies in session
    session['cookies'] = {
        'name1': {  # value and attributes
            'value': 'value1',
            'path': 'p1',
            'secure': True,
            'expires': 'e1',
        },
        'name2': {  # value and attributes
            'value': 'value2',
            'path': 'p2',
            'secure': False,
            'expires': 'e2',
        },
    }
    # Remove one cookie from session
    names = ['name2']
    session.remove_cookies(names)

    # Remove multiple cookies from session
    names = ['name2', 'name3']
    session.remove_cookies(names)

#

# Generated at 2022-06-13 22:40:44.688750
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path('~/.config/httpie/sessions/test_host/test.json'))
    session['cookies'] = {'cookie1': {}, 'cookie2': {}, 'cookie3': {}, 'cookie4': {}}
    session.remove_cookies(['cookie1', 'cookie3'])
    assert sorted(session['cookies'].keys()) == ['cookie2', 'cookie4']

# Generated at 2022-06-13 22:40:55.053998
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session')
    session['cookies'] = {'name1':{'value':'value1'},'name2':{'value':'value2'}}
    print('1:   %s' % session['cookies'])
    session.remove_cookies(['name1','name3'])
    print('2:   %s' % session['cookies'])
    session.remove_cookies(['name2'])
    print('3:   %s' % session['cookies'])
    session.remove_cookies(['name2'])
    print('4:   %s' % session['cookies'])

# Generated at 2022-06-13 22:41:18.455535
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('./test.json')
    session.cookies.set('type', 'test', path='/', secure=True, expires=0)
    session.remove_cookies(['type'])
    assert session.cookies == RequestsCookieJar()

# Generated at 2022-06-13 22:41:23.487869
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(path=Path('/foo/bar'))
    sess['cookies'] = {'foo': {'value': 'bar'}, 'baz': {'value': 'qaz'}}
    sess.remove_cookies(['foo'])
    assert 'foo' not in sess['cookies']
    assert sess['cookies'] == {'baz': {'value': 'qaz'}}



# Generated at 2022-06-13 22:41:35.175590
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.session import Session, get_httpie_session
    from pathlib import Path
    from requests.cookies import create_cookie
    from httpie.cli.dicts import RequestHeadersDict
    from httpie.config import BaseConfigDict
    #obj = Session()
    session = Session("test_session.json")
    session.load()
    #assert str(session) == "test_session.json"
    assert type(session) == Session
    assert type(session.headers) == RequestHeadersDict
    assert type(session.cookies) == type(RequestsCookieJar())
    #assert type(session.auth) == type(AuthBase())

    #test remove_cookies method
    session['cookies'] = {'test_cookie': {'value': 'test_value'}}

# Generated at 2022-06-13 22:41:40.670462
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = '/tmp/foo.json'
    s = Session(path)
    s['cookies'] = {
        'a': {'value': 'foo'},
        'b': {'value': 'foo'},
        'c': {'value': 'foo'}
    }
    names = ['a', 'b']
    s.remove_cookies(names)
    assert len(s['cookies']) == 1
    assert 'c' in s['cookies']



# Generated at 2022-06-13 22:41:44.729199
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('sessions/default.json')
    sess['cookies'] = {'abc':'123', 'def':'456', 'hij':'789'}
    sess.remove_cookies(['abc', 'def'])
    assert sess['cookies'] == {'hij':'789'}

# Generated at 2022-06-13 22:41:50.771138
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/some/path.json')
    session['cookies'] = dict(foo='bar', bar='baz', baz='quux')
    session.remove_cookies(['bar', 'quux'])

    assert session['cookies'] == dict(foo='bar')



# Generated at 2022-06-13 22:41:57.161366
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = '/tmp/somesession.json'
    try:
        os.remove(path)
    except:
        pass
    session = Session(path)
    session['cookies'] = {"a": {}, "b": {}}
    session.remove_cookies(["a"])
    assert {"b": {}} == session['cookies']

    session['cookies'] = {"a": {}, "b": {}}
    session.remove_cookies(["a", "b"])
    assert {} == session['cookies']

# Generated at 2022-06-13 22:42:04.647717
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test_remove_cookies.json')
    assert s['cookies'] == {}

    cookie1 = create_cookie('test1', 'test1')
    cookie2 = create_cookie('test2', 'test2')
    cookie3 = create_cookie('test3', 'test3')

    s['cookies'][cookie1.name] = {'value': cookie1.value}
    s['cookies'][cookie2.name] = {'value': cookie2.value}
    s['cookies'][cookie3.name] = {'value': cookie3.value}

    assert s['cookies'] == {'test1': {'value': 'test1'}, 'test2': {'value': 'test2'}, 'test3': {'value': 'test3'}}


# Generated at 2022-06-13 22:42:08.682472
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'name': 'cookie'}
    session = Session('./test_session.json')
    session['cookies'] = cookies
    assert session['cookies']['name'] == 'cookie'
    session.remove_cookies(['name'])
    assert len(session['cookies']) == 0


# Generated at 2022-06-13 22:42:17.880762
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_data = {'cookies': {'foo': 'baz', 'bar': 'baz'}, 'auth': {'foo': 'bar'}, 'headers': {'foo': 'bar'}}
    my_session = Session('~/.httpie/test.json')
    my_session.update(test_data)
    my_session.remove_cookies(['foo','bar','baz'])
    assert my_session['cookies'] == {}



# Generated at 2022-06-13 22:42:47.589415
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("session_file")
    session['cookies'] = {}
    session['cookies']['cookie1'] = {}
    session['cookies']['cookie2'] = {}
    session['cookies']['cookie3'] = {}
    session.remove_cookies(["cookie1", "cookie2"])
    assert session['cookies'] == {'cookie3': {}}

# Generated at 2022-06-13 22:42:53.840264
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # arrange
    session = Session(1)
    session['cookies'] = {'cookies1': {'value': 'Apple'}}
    session['cookies']['cookies2'] = {'value': 'Orange'}

    # act
    session.remove_cookies(['cookies1', 'cookies2'])

    # assert
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:43:00.522854
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_jar = RequestsCookieJar()
    cookie_jar.set_cookie(create_cookie('foo', 'bar'))
    cookie_jar.set_cookie(create_cookie('baz', 'qux'))

    session = Session('test')
    session.cookies = cookie_jar

    session.remove_cookies(['foo'])
    assert 'foo' not in session['cookies']

    session.remove_cookies(['qux'])
    assert 'baz' in session['cookies']

# Generated at 2022-06-13 22:43:06.446318
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(path='.')
    sess['cookies'] = {'a': '1', 'b': '2'}
    sess.remove_cookies(names=['a', 'b', 'c'])
    assert sess['cookies'] == {'b': '2'}
    sess.remove_cookies(names=['b'])
    assert sess['cookies'] == {}

# Generated at 2022-06-13 22:43:15.636022
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session=Session('')
    session['cookies']={'cookie1':{'value':'aaaaaaaaaaa'},'cookie2':{'value':'bbbbbbbbbbbb'}}
    try:
        session.remove_cookies(['cookie1'])
    except AssertionError:
        print(" AssertionError")
    else:
        if session['cookies'] == {'cookie2':{'value':'bbbbbbbbbbbb'}}:
            print("pass")
        else:
            print("fail")