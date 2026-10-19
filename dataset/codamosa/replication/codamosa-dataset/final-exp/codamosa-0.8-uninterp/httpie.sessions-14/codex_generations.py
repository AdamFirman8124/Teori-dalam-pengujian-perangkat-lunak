

# Generated at 2022-06-13 22:33:28.949358
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from .cache import BaseCache
    from .session import Session
    from .utils import CookieDict

    session_path = Path('~/.config/httpie/sessions/example.com/session.json').expanduser()
    session = Session(session_path)
    test_sessions_dir = session_path.parent
    test_sessions_dir.mkdir(parents=True, exist_ok=True)

    # Test 1: Update set headers from request to session
    session['headers']['Header-1'] = 'Session-Header-1'
    session['headers']['Header-2'] = 'Session-Header-2'


# Generated at 2022-06-13 22:33:35.863526
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('/')
    h = RequestHeadersDict(input_data={'a': 'aaa', 'Content-Type': 'test'})
    s.update_headers(h)
    assert s['headers']['a'] == 'aaa'
    assert 'Content-Type' not in s['headers'].keys()



# Generated at 2022-06-13 22:33:48.557373
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # print("---------------------")
    # print("Unit test for method update_headers of class Session")
    session = Session("test")

# Generated at 2022-06-13 22:34:01.907346
# Unit test for method update_headers of class Session

# Generated at 2022-06-13 22:34:13.731850
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('s')

    with open('testdata/headers.txt', 'r') as fp:
        request_headers = RequestHeadersDict(dict(fp.read()))
    
    session.update_headers(request_headers) 
    #check the session is correct or not
    assert request_headers['Content-Type'] == session.headers['Content-Type']
    assert request_headers['Connection'] == session.headers['Connection']
    assert request_headers['Accept'] == session.headers['Accept']
    assert request_headers['Accept-Charset'] == session.headers['Accept-Charset']
    assert request_headers['Accept-Encoding'] == session.headers['Accept-Encoding']
    assert request_headers['Accept-Language'] == session.headers['Accept-Language']

# Generated at 2022-06-13 22:34:20.116397
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session_headers_old = {'X-test': 'old', 'Cookie': 'not used'}
    request_headers = {'X-test': 'new', 'Cookies': 'not used', 'Cookie': 'foo=bar'}
    session = Session('')
    session.headers = session_headers_old
    session.update_headers(request_headers)
    assert session.headers == {'X-test': 'new', 'Cookie': 'foo=bar'}



# Generated at 2022-06-13 22:34:27.682182
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    assert {} == session['headers']
    headers = [
        ('cookie', 'cookiename=value'),
        ('Content-Type', 'text/html'),
        ('User-Agent', 'HTTPie/0.9.2'),
        ('Content-Length', '13')
    ]
    session.update_headers(RequestHeadersDict(headers))
    # Cookie header is ignored
    assert {'Content-Type': 'text/html', 'Content-Length': '13'} == session['headers']


# Generated at 2022-06-13 22:34:39.340250
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.config import DEFAULT_SESSIONS_DIR
    from httpie.cookies import CookieJar
    from httpie.plugins.auth.basic import AuthBasicPlugin

    s = Session(DEFAULT_SESSIONS_DIR / 'test.json')
    s.load()

    r = {
        'a': 'b',
        'c': 'd',
        'cookie': 'session_id=123'
    }

    s.update_headers(r)

    assert s['headers'] == {'a': 'b', 'c': 'd'}
    assert s['cookies'] == {'session_id': {'value': '123'}}
    assert s['auth'] == {'type': None, 'username': None, 'password': None}

    # Replace the headers.

# Generated at 2022-06-13 22:34:47.876677
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(path="test.json")
    sess['cookies'] = {'cookie1': {'value': 'value1', 'domain': 'www.domain.com'}, 'cookie2': {'value': 'value2', 'domain': 'www.domain.com'}, 'cookie3': {'value': 'value3', 'domain': 'www.domain.com'}}
    sess.remove_cookies(['cookie1', 'cookie2'])
    assert sess['cookies'] == {'cookie3': {'value': 'value3', 'domain': 'www.domain.com'}}

# Generated at 2022-06-13 22:34:56.510703
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Given
    session = Session(path='path')

# Generated at 2022-06-13 22:35:10.190914
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.context import Environment
    from httpie.output.streams import get_default_streams
    from httpie.sessions import Session

    env = Environment(
        config_dir=DEFAULT_CONFIG_DIR,
        is_windows=is_windows,
        stdin=get_default_streams().stdin,
        stdout=get_default_streams().stdout,
        stderr=get_default_streams().stderr,
    )
    session = Session(env.config_dir / SESSIONS_DIR_NAME / 'session.json')

# Generated at 2022-06-13 22:35:20.437646
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(Path('/dummy/path'))
    session.update_headers({'Content-Type': 'application/json'})
    assert 'Content-Type' not in session['headers']

    session.update_headers({'Authorization': 'bearer token'})
    assert 'Authorization' in session['headers']

    session.update_headers({'Cookie': 'a=b; c=d'})
    assert 'Cookie' not in session['headers']
    assert 'Cookies' in session.keys()
    assert session['cookies']['a']['value'] == 'b'
    assert session['cookies']['c']['value'] == 'd'

# Generated at 2022-06-13 22:35:33.657535
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Initialization
    path = 'path/to/file.json'
    request_headers = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    session = Session(path)
    session['headers'] = {'key1': 'value1', 'key3': 'value3'}
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2', 'cookie3': 'value3'}
    # Update session headers with request headers where headers in request headers are not ignored
    session.update_headers(request_headers)
    # Unit test
    assert session['headers'] == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Generated at 2022-06-13 22:35:41.999821
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Prepare
    config_dir = Path("/path/to/config/directory")
    request_headers = ['Cookie: name=value', 'Content-Type: application/json']
    # Run
    session = get_httpie_session(config_dir, 'name', 'host', 'url')
    session.update_headers(request_headers)
    # Verify
    assert isinstance(session, Session)
    assert session['headers'] == {}
    assert session['cookies'] == {'name': {'value': 'value'}}
    assert session['auth'] == {'type': None, 'username': None, 'password': None}

# Generated at 2022-06-13 22:35:56.442086
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from collections import OrderedDict
    from httpie.cli.parser import get_parser
    from httpie.compat import is_windows
    from httpie.core import main
    from httpie.models import Request, Response
    from httpie.output import get_parser_ladder
    from httpie.output.streams import get_stream

    stdout = get_stream('stdout')
    parser_ladder = get_parser_ladder(get_parser()) if not is_windows else []


# Generated at 2022-06-13 22:36:05.045507
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="mock")
    session['cookies'] = {"1" : "val1", "2" : "val2" , "3" : "val3"}
    assert len(session['cookies']) == 3
    session.remove_cookies(["2", "3"])
    assert len(session['cookies']) == 1
    assert "1" in session['cookies']
    try:
        session.remove_cookies(["4"])
    except KeyError as e:
        assert "4" == e.args[0]


# Generated at 2022-06-13 22:36:10.134378
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path("example_file")) # Mock a session
    session['cookies'] = {'Authorization' : {'value': 'mysecret'}}
    session.remove_cookies(['Authorization'])
    assert session['cookies'] == {}  # the cookie has been removed



# Generated at 2022-06-13 22:36:18.928995
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.core import main

    session = Session(path='test-session')

    request_headers = RequestHeadersDict(main.parse_headers('Foo: Bar', '--session=test-session'))
    data = {
        'headers': {'Foo': 'Bar'},
        'cookies': {}
    }

    os.makedirs(os.path.dirname(session.path), exist_ok=True)

    with open(session.path, 'w') as f:
        import json
        json.dump(session, f)

    session.update_headers(request_headers)
    with open(session.path, 'r') as f:
        assert json.load(f) == data

# Generated at 2022-06-13 22:36:24.048923
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/s')
    s['cookies'] = {'a': {'value': 'a'}, 'b': {'value': 'b'}}
    s.remove_cookies(['a'])
    assert s['cookies'] == {'b': {'value': 'b'}}

test_Session_remove_cookies()

# Generated at 2022-06-13 22:36:34.176645
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    test_session = Session('')
    test_session.update_headers({'header1': 'value1'})
    test_session.update_headers({'header2': 'value2'})
    test_session.update_headers({
        'If-Match': '"737060cd8c284d8af7ad3082f209582d"'
    })
    test_session.update_headers({'Cookie': 'session=1234'})
    test_session.update_headers({'Cookie': 'test_Cookie=1234'})
    assert test_session['headers']['header1'] == 'value1'
    assert test_session['headers']['header2'] == 'value2'
    assert 'If-Match' not in test_session['headers']
    assert 'Cookie' not in test_session

# Generated at 2022-06-13 22:36:45.391179
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # given
    session = Session('path')
    session.update({
        'cookies': {
            'foo': {'value': '1'},
            'bar': {'value': '2'},
            'baz': {'value': '3'}
        }
    })

    # when
    session.remove_cookies(['foo', 'bar'])

    # then
    assert session == {
        'cookies': {'baz': {'value': '3'}},
    }

# Generated at 2022-06-13 22:36:50.388704
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('./test/test_sessions/example.com/test.json'))
    session.load()
    session.remove_cookies(['sessionid', 'foo'])
    assert session['cookies']['sessionid'] == None 
    assert session['cookies']['foo'] == None

# Generated at 2022-06-13 22:37:01.315569
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict({"Content-Length": "11", "Date": "Mon, 01 Jan 2018 00:00:00 GMT"})
    session = Session(path='')
    session.update_headers(request_headers)
    session_headers = session.headers
    assert session_headers.get('cont') is None
    assert session_headers.get('date') == 'Mon, 01 Jan 2018 00:00:00 GMT'
    assert session_headers.get('content-length') is None

#Unit test for method cookies of class Session

# Generated at 2022-06-13 22:37:08.568617
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='')
    session['cookies'] = {'cookies1': {'value': 'value1'}, 'cookies2': {'value': 'value2'}}
    session.remove_cookies(names=['cookies2'])
    assert session['cookies'] == {'cookies1': {'value': 'value1'}}



# Generated at 2022-06-13 22:37:22.393072
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    try:
        os.mkdir(str(DEFAULT_CONFIG_DIR))
    except OSError:
        pass
    try:
        os.mkdir(str(DEFAULT_SESSIONS_DIR))
    except OSError:
        pass
    try:
        os.mkdir(str(DEFAULT_SESSIONS_DIR/'test'))
    except OSError:
        pass

    session = Session(DEFAULT_SESSIONS_DIR/'test' / 'test_session.json')

    # Test without header
    request_headers = RequestHeadersDict({"Content-Type": "application/json"})
    session.update_headers(request_headers)

    # Test with header
    request_headers = RequestHeadersDict({"Host": "httpbin.org"})
    session

# Generated at 2022-06-13 22:37:28.020457
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_dict = {'headers': {}, 'cookies': {
        'first': {'key': 'first', 'value': 'first'},
        'second': {'key': 'second', 'value': 'second'}
    }}
    session = Session("")
    session.data = session_dict
    session.remove_cookies(['first', 'third'])
    assert len(session['cookies']) == 1



# Generated at 2022-06-13 22:37:38.647917
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Arrange
    session_path = "test.json"
    session = Session(session_path)
    session.load()
    request_headers = RequestHeadersDict({'a': '1', 'b': '2', 'c': '3', 'd': '4'})

    # Act
    session.update_headers(request_headers)

    # Assert
    a = session.get_header("a")
    b = session.get_header("b")
    c = session.get_header("c")
    d = session.get_header("d")
    assert a == "1"
    assert b == "2"
    assert c == "3"
    assert d == "4"



# Generated at 2022-06-13 22:37:45.463596
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    try:
        from httpie.cli.argtypes import KeyValueArgType
    except ImportError:
        from tests.utils import MockKeyValueArgType as KeyValueArgType

    s = Session("")

# Generated at 2022-06-13 22:37:52.731075
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    import tempfile
    # Create a temporary directory to avoid messing up the default one
    with tempfile.TemporaryDirectory() as config_dir:
        sess = Session(config_dir + '/sess.json')
        sess['cookies'] = {'cookie1': {'value': '1'}, 'cookie2': {'value': '2'}}
        sess.remove_cookies(['cookie1', 'cookie3'])
        assert json.loads(sess.dumps()) == {'cookies': {'cookie2': {'value': '2'}}, 'headers': {}}

# Generated at 2022-06-13 22:37:59.345125
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/test.json')
    request_headers = {
        'key1': 'value1',
        'key2': 'value2',
        'user-agent': 'httpie/0.9.2',
        'if-match': 'test',
        'cookie': 'test_cookie=test_value'
    }
    session.update_headers(request_headers)
    assert(session['headers'] == {'key1': 'value1',
                                  'key2': 'value2'})
    assert(session['cookies'] == {'test_cookie': {'value': 'test_value'}})


# Generated at 2022-06-13 22:38:14.764881
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(DEFAULT_SESSIONS_DIR)
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'host': 'httpbin.org',
        'user-agent': 'python-httpie',
        'accept': 'application/json, */*',
        'x-test': 'foo',
        'content-length': '18',
        'cookie': 'foo=bar; spam=eggs',
        'x-foo': 'bar'
    }
    session.update_headers(headers)
    assert session['headers']['x-test'] == 'foo'
    assert session['headers']['x-foo'] == 'bar'

# Generated at 2022-06-13 22:38:26.516676
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='/tmp/session.json')
    session['cookies'] = {
        'name1': 'value1',
        'name2': 'value2',
        'name3': 'value3'
    }
    assert session['cookies'] == {
        'name1': 'value1',
        'name2': 'value2',
        'name3': 'value3'
    }

    session.remove_cookies(['name1', 'name3'])
    assert session['cookies'] == {
        'name2': 'value2'
    }

    session.remove_cookies(['name2'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:38:33.858644
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_dir = DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME

    session = Session(session_dir)
    session['cookies'] = {'gh_auth': 'token', 'gh_sess': 'session'}
    session.remove_cookies(['gh_auth'])
    assert 'gh_sess' in session['cookies']
    assert 'gh_auth' not in session['cookies']

# Generated at 2022-06-13 22:38:39.935296
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="/tmp/test_Session_remove_cookies.json")
    session['cookies'] = {'id': {'value': '123'}}
    session.remove_cookies(['id'])
    assert 'id' not in session['cookies']
    session.remove_cookies(['id'])
    assert 'id' not in session['cookies']

# Generated at 2022-06-13 22:38:44.568384
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path = 'test.json')
    s['cookies'] = {'a': {'value': 'v1'}, 'b': {'value': 'v2'}}
    s.remove_cookies(['b'])
    assert s['cookies'] == {'a': {'value': 'v1'}}

# Generated at 2022-06-13 22:38:49.197053
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session([])
    session['cookies'] = {'n1': 'v1'}
    session.remove_cookies(['n1'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:38:53.217666
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test.json')
    session['cookies'] = {'a': 'b'}
    session.remove_cookies(['a'])
    assert 'a' not in session['cookies']

# Generated at 2022-06-13 22:39:00.650823
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path='/')
    s['cookies'] = {'one': {'value': 1}, 'two': {'value': 2}}
    assert len(s['cookies']) == 2
    s.remove_cookies(['one'])
    assert len(s['cookies']) == 1
    s.remove_cookies(['two'])
    assert len(s['cookies']) == 0
    s.remove_cookies(['one', 'two'])
    assert len(s['cookies']) == 0


# Generated at 2022-06-13 22:39:05.050138
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('test.json')
    sess.update({'cookies': {"a": "1", "b": "2", "c": "3"}})
    assert(sess['cookies']['c'] == "3")
    sess.remove_cookies(["a", "c"])
    assert(sess['cookies']['b'] == "2")

# Generated at 2022-06-13 22:39:10.429544
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import string
    import random
    s = Session('')
    c = ''.join(random.choices(string.ascii_lowercase, k=8))
    s['cookies'] = {}
    s['cookies'][c] = {'value': '123'}
    s.remove_cookies([c])
    assert not s['cookies']

# Generated at 2022-06-13 22:39:26.601693
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(""))
    session['cookies'] = {"cookie1": 1, "cookie2": 2, "cookie3": 3, "cookie4": 4, "cookie5": 5}
    session.remove_cookies(["cookie1", "cookie2", "cookie4"])
    assert session['cookies'] == {"cookie3": 3, "cookie5": 5}

# Generated at 2022-06-13 22:39:35.016322
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'abc':'abc', 'def':'def'}
    assert session['cookies'] == {'abc':'abc', 'def':'def'}
    session.remove_cookies(['abc'])
    assert session['cookies'] == {'def':'def'}
    session.remove_cookies(['ghi'])
    assert session['cookies'] == {'def':'def'}

# Generated at 2022-06-13 22:39:40.002885
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('testSession.session')
    session['cookies']['foo'] = {}
    session['cookies']['bar'] = {}
    session['cookies']['baz'] = {}
    session.remove_cookies(['foo', 'baz'])
    assert not ('foo' in session['cookies'])
    assert 'bar' in session['cookies']
    assert not ('baz' in session['cookies'])



# Generated at 2022-06-13 22:39:46.359439
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    session.update_headers(RequestHeadersDict({'Host': 'localhost:8080', 'Content-Length': '5'}))
    print(session.headers)
    print(session['headers'])


test_Session_update_headers()

# Generated at 2022-06-13 22:39:53.249505
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.argtypes import KeyValueArgType

    sess = Session('')
    name = KeyValueArgType(key='').parse('NAME=value')
    sess['cookies'][name.key] = name.value
    sess.remove_cookies([name.key])
    assert not sess['cookies']



# Generated at 2022-06-13 22:40:01.584743
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session.json')
    session['cookies'] = {'c1': {'value': 'v1', 'path': '/'},
                          'c2': {'value': 'v2', 'path': '/'},
                          'c3': {'value': 'v3', 'path': '/'}
                          }
    session.remove_cookies(['c2', 'c3'])
    assert session['cookies'] == {'c1': {'value': 'v1', 'path': '/'}}

# Generated at 2022-06-13 22:40:07.519264
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Test if method remove_cookies work flawless
    session = Session('/tmp/test')
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    session.remove_cookies(['cookie1','cookie4'])
    assert session['cookies'] == {'cookie2': 'value2'}


# Generated at 2022-06-13 22:40:17.270453
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test_session_cookies.json")
    session['cookies'] = {'cook1': 'val1', 'cook2': 'val2', 'cook3': 'val3'}
    assert session['cookies'] == {'cook1': 'val1', 'cook2': 'val2', 'cook3': 'val3'}
    session.remove_cookies(['cook3', 'cook4'])
    assert session['cookies'] == {'cook1': 'val1', 'cook2': 'val2'}
    session.remove_cookies(['cook1', 'cook2'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:40:23.099559
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session_remove_cookies')
    print(session)
    session['cookies'] = {'c1':{'value': 'a'}, 'c2': {'value': 'b'}}
    print(session)
    session.remove_cookies(['c1'])
    print(session)

if __name__ == '__main__':
    test_Session_remove_cookies()

# Generated at 2022-06-13 22:40:32.623779
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test.json')

    session.update_headers({})
    assert session == {'headers': {}, 'cookies': {}, 'auth': {'type': None,'username': None,'password': None}}

    session.update_headers({'a': 0})
    assert session == {'headers': {'a': 0}, 'cookies': {}, 'auth': {'type': None,'username': None,'password': None}}

    session.update_headers({'a': 1, 'b': 2, 'c': 3})
    assert session == {'headers': {'a': 1, 'b': 2, 'c': 3}, 'cookies': {}, 'auth': {'type': None,'username': None,'password': None}}

    session.update_headers({'a': None})

# Generated at 2022-06-13 22:40:57.530887
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Session_remove_cookies::test_01
    # Given a session,
    session = Session('/path/to/my/session')
    # and a list of cookie names {'foo', 'bar'},
    cookies = ['foo', 'bar']
    # and a dict of cookies {'foo': {'value': 'foo-value'},},
    session['cookies'] = {'foo': {'value': 'foo-value'}}
    # when remove_cookies(cookies) is called,
    session.remove_cookies(cookies)
    # then 'foo' cookie will not be in session cookies.
    assert 'foo' not in session['cookies']

# Generated at 2022-06-13 22:41:06.205735
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    session = Session('/tmp/session.json')
    session.load()

    request_headers = {'Accept': 'application/json', 'Cookie': 'foo=bar; baz=auth'}
    session.update_headers(request_headers)

    expected_session_headers = {'Accept': 'application/json'}
    assert session['headers'] == expected_session_headers

    expected_session_cookies = {'foo': {'value': 'bar'}, 'baz': {'value': 'auth'}}
    assert session['cookies'] == expected_session_cookies

    assert session.cookies.get('foo').value == 'bar'
    assert session.cookies.get('baz').value == 'auth'

# Generated at 2022-06-13 22:41:12.775443
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_list = [
        'SESSION',
        'SESSION_DATA'
    ]

    s = Session('test')
    for cookie in cookie_list:
        s['cookies'][cookie] = {'value': 'Mock'}
    s.remove_cookies(['SESSION'])
    assert s['cookies']['SESSION_DATA'] == {'value': 'Mock'}
    assert 'SESSION' not in s['cookies']



# Generated at 2022-06-13 22:41:21.181718
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/does/not/exist')
    # TODO: More comprehensive testing, especially for cookies.
    session.update_headers(RequestHeadersDict({
        'accept-encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'HTTPie/0.9.8',
        'Content-Length': '9'
    }))
    assert session['headers'] == {
        'Accept': '*/*',
        'Content-Length': '9'
    }



# Generated at 2022-06-13 22:41:30.212571
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("./some_file")
    s['cookies'] = { "name1": "value1", "name2": "value2", "name3": "value3" }
    assert s['cookies'] == { "name1": "value1", "name2": "value2", "name3": "value3" }
    s.remove_cookies(["name2"])
    assert s['cookies'] == { "name1": "value1", "name3": "value3" }



# Generated at 2022-06-13 22:41:33.058366
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('path')
    session = Session(p=path)
    names = ['cookie1', 'cookie2']
    session.remove_cookies(names)

# Generated at 2022-06-13 22:41:36.739130
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(Path('testSession'))
    s['cookies'] = {'A': {}, 'B': {}}
    s.remove_cookies(['B'])
    assert s['cookies'] == {'A': {}}

# Generated at 2022-06-13 22:41:46.047791
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="/path/to/session")
    cookie_a = {"name":"a", "value":"a_value"}
    cookie_b = {"name":"b", "value":"b_value"}
    cookie_c = {"name":"c", "value":"c_value"}
    session['cookies'] = {
        'a' : cookie_a,
        'b' : cookie_b,
        'c' : cookie_c
    }

    session.remove_cookies(['a', 'd'])
    assert 'a' not in session['cookies']
    assert session['cookies']['b'] == cookie_b
    assert session['cookies']['c'] == cookie_c

# Generated at 2022-06-13 22:41:51.762497
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session.cookies=RequestsCookieJar()
    session.cookies.set('name1', 'value1')
    session.cookies.set('name2', 'value2')
    session.remove_cookies(['name1'])
    assert 'name2' in session.cookies
    assert 'name1' not in session.cookies

# Generated at 2022-06-13 22:41:57.729045
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    default_session = Session('~/.config/httpie/sessions/test_Session_update_headers.json')
    default_session.update_headers({
        'key1': 'val1',
        'key2': 'val2',
        'User-Agent': 'HTTPie/0.9.9',
        'Cookie': 'key3=val3',
    })
    print('headers: ', default_session['headers'])
    print('cookies: ', default_session['cookies'])

# Generated at 2022-06-13 22:42:22.399168
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class Cookie:
        name = 'cookie-name'
    class CookieJar:
        def __init__(self, cookie_names):
            self._cookie_names = cookie_names
        def __iter__(self):
            return iter(Cookie(name) for name in self._cookie_names)
    session = Session('/')
    session['cookies'] = {'cookie-name': {'value': '0'}}
    jar = CookieJar(['cookie-name', 'cookie-name-2'])
    session.cookies = jar
    session.remove_cookies(jar)
    assert len(session['cookies']) == 0


# Generated at 2022-06-13 22:42:30.288340
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('/test')
    sess.cookies = RequestsCookieJar()
    sess.cookies.set('test', 'test')
    sess.cookies.set('test1', 'test1')
    sess.cookies.set('test2', 'test2')

    sess.remove_cookies(['test1', 'test2'])

    assert len(sess.cookies) == 1
    assert list(sess.cookies)[0].name == 'test'

# Generated at 2022-06-13 22:42:32.787576
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = DEFAULT_CONFIG_DIR / 'sessions/myhost/myname.json'
    session = Session(path)
    session['cookies'] = {"cookie1": "val1"}

    session.remove_cookies(["cookie1"])

    assert "cookie1" not in session['cookies']



# Generated at 2022-06-13 22:42:42.587395
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('dummy_path')
    sess['cookies'] = {}
    sess['cookies']['a'] = 'b'
    sess['cookies']['c'] = 'd'
    sess['cookies']['e'] = 'f'
    assert len(sess['cookies'].keys()) == 3
    sess.remove_cookies(['a', 'b', 'e', 'f', 'g'])
    assert len(sess['cookies'].keys()) == 1
    assert 'c' in sess['cookies']

# Generated at 2022-06-13 22:42:48.893994
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path_tmp_session = "test.json"
    session = Session(path_tmp_session)
    cookie_names = ['cc', 'bb', 'dd']
    for name in cookie_names:
        session['cookies'].update({name: {'a': 'b'}})
    session.remove_cookies(['aa', 'cc', 'bb'])
    assert session['cookies'] == {'dd': {'a': 'b'}}
    os.remove(path_tmp_session)

# Generated at 2022-06-13 22:42:55.455310
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = os.getcwd() + "/test/test-session.json"
    session = Session(path)
    session.update_headers({'Cookie': 'foo=bar;baz=qux'})
    session.remove_cookies(['foo', 'baz'])
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:43:09.218297
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    request_headers = {
        'User-Agent': 'HTTPie/0.9.8',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Cookie': 'a=b; c=d'
    }

    s = Session(path='test.json')
    s.update_headers(request_headers)
    assert s['cookies'] == {'a': {'value': 'b'}, 'c': {'value': 'd'}}

    s.remove_cookies(['a', 'd'])
    assert s['cookies'] == {'c': {'value': 'd'}}