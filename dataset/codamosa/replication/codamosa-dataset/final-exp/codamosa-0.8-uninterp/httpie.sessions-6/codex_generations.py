

# Generated at 2022-06-13 22:33:26.509584
# Unit test for method update_headers of class Session
def test_Session_update_headers():

    session = Session('/home/dang/httpie/httpie/config/sessions/localhost/test.json')
    session.update_headers({'key1': 'value1', 'key2': 'value2'})
    print(session.headers)

# Generated at 2022-06-13 22:33:35.881786
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.headers import CONTENT_TYPE_HEADER
    request_headers = RequestHeadersDict()
    request_headers['cookie'] = 'abc=123'
    request_headers[CONTENT_TYPE_HEADER] = 'application/json'
    request_headers['If-None-Match'] = 'xx'

    session = Session(path='')
    session.update_headers(request_headers)
    assert not request_headers.get('cookie', None)
    assert not request_headers.get('If-None-Match', None)
    assert session['cookies'] == {'abc': {'value': '123'}}
    assert session['headers'] == {CONTENT_TYPE_HEADER: 'application/json'}

# Generated at 2022-06-13 22:33:45.427455
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    We test here the following:
    1) the case when the session contains a cookie with the given name
    2) the case when the session does not contain the cookie with the given name
    3) the case when there are two cookies with a given name but different path
    """
    test_session = Session(Path(SESSIONS_DIR_NAME))
    cookie_one = {"name":"simple_cookie", "value":"simple_value"}
    cookie_two = {"name": "simple_cookie", "value": "simple_value_second", "path": "/cookie_two"}
    test_session["cookies"]["simple_cookie"] = cookie_one
    test_session["cookies"]["simple_cookie"] = cookie_two
    test_session.remove_cookies(["simple_cookie"])

# Generated at 2022-06-13 22:33:55.706672
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('session')
    session.update_headers({'foo':'bar'})
    assert session.headers['foo'] == 'bar'
    session.update_headers({'Cookie':'foo=bar; bar=baz'})
    assert session['cookies']['foo']['value'] == 'bar'
    assert session['cookies']['bar']['value'] == 'baz'
    session.update_headers({'CookiE':'foo=; Expires=Thu, 01 Jan 1970 00:00:00 GMT'})
    assert 'foo' not in session['cookies'].keys()



# Generated at 2022-06-13 22:34:04.949523
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    old_headers = {
        'Content-Type': 'application/json',
        'Cookie': 'username=admin;password=12345'
    }
    new_headers = {
        'Content-Type': 'application/json',
        'Cookie': 'username=test;password=test'
    }
    headers_dict = RequestHeadersDict(old_headers)
    session = Session('')
    session.update_headers(headers_dict)
    session['headers']['Cookie'] = 'username=test;password=test'
    session['cookies'] = {'username': {'value': 'test'}, 'password': {'value': 'test'}}
    assert session['headers'] == new_headers

# Generated at 2022-06-13 22:34:18.544730
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict()
    request_headers['Content-Type'] = 'text/html; charset=utf-8'
    request_headers['If-Match'] = '"this-is-a-strong-etag"'
    request_headers['User-Agent'] = 'HTTPie/1.0.2'
    request_headers['Cookie'] = 'session=happybunny'
    session = Session('test.json')
    session.update_headers(request_headers)
    session.dump()

# Generated at 2022-06-13 22:34:22.989626
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session['cookies'] = {'abc': '123', 'def': '456'}
    session.remove_cookies(['abc', 'ghi'])
    assert session['cookies'] == {'def': '456'}

# Generated at 2022-06-13 22:34:33.348446
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_name1 = 'first_name'
    test_name2 = 'second_name'
    test_name3 = 'third_name'
    test_value1 = 'first_value'
    test_value2 = 'second_value'
    test_value3 = 'third_value'
    cookie_jar = RequestsCookieJar()
    cookie_jar.set_cookie(create_cookie(test_name1, test_value1))
    cookie_jar.set_cookie(create_cookie(test_name2, test_value2))
    cookie_jar.set_cookie(create_cookie(test_name3, test_value3))
    session = Session('/')
    session.cookies = cookie_jar
    names = [test_name1, test_name3]
    session.remove_cookies(names)

# Generated at 2022-06-13 22:34:37.135405
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('foo')
    assert session.cookies == {}
    session.cookies.set('foo', 'bar')
    assert session.cookies['foo'] == 'bar'
    session.remove_cookies(['foo'])
    assert session.cookies == {}

# Generated at 2022-06-13 22:34:44.779675
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('./test_Session_remove_cookies.json')
    test_session['cookies'] = {'csrftoken': 'csrfvalue', 'sessionid': 'sessionidvalue'}
    test_session.remove_cookies(['csrftoken'])
    assert test_session['cookies'] == {'sessionid': 'sessionidvalue'}
# end unit test

# Generated at 2022-06-13 22:35:03.089264
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.argtypes import KeyValueArgType
    from httpie.downloads import Response
    from httpie.input import FileLister, FileReader
    from httpie.output import BINARY_SUPPRESSED_NOTICE
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.manager import PLUGIN_MANAGER
    from httpie.plugins.registry import plugin_manager
    from httpie.context import Environment
    from httpie import ExitStatus
    from httpie.compat import urlopen
    from httpie.models import HTTPRequest

    s = Session('./sessions/test1.json')
    s.load()
    print(s)

# Generated at 2022-06-13 22:35:17.017515
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(Path("test_session"))
    session.update_headers({"accept": "application/json","content-type":"application/json","user-agent": "HTTPie/0.9.9","cookie": "sessionid=1233","if-modified-since":"Sat, 23 Jun 2018 12:00:00 GMT"})
    session.update_headers({"accept": "application/xml","content-type":"application/xml","user-agent": "HTTPie/0.9.9","cookie": "sessionid=1233","if-modified-since":"Sat, 23 Jun 2018 12:00:00 GMT"})

# Generated at 2022-06-13 22:35:27.260771
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.utils import CaseInsensitiveDict
    from httpie.cli.cli import Parser
    from httpie.context import Environment
    from httpie.help import Help
    from httpie.input import Input, KeyValue
    from httpie.plugins.registry import plugin_manager

    args = Parser(prog='test_Session_update_headers').parse_args([
        '--session=test_Session_update-headers',
        'get',  'http://localhost:8088/get?arg1=value1', '-H User-Agent:12345',
        '-H Cookie:foo=bar; baz=qux', '-H Foo:bar',
        'Authorization:Basic YmFyOnF1eA=='
    ])

# Generated at 2022-06-13 22:35:30.594029
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session')
    request_headers = {'Header1': 'value1', 'Header2': 'value2', 'Header3': None,
                       'Header4': 'value4', 'Header5': 'value5'}
    # Test for method update_headers of class Session
    session.update_headers(request_headers)
    assert session.data == {"headers": {"Header1": "value1", "Header2": "value2", "Header4": "value4", "Header5": "value5"},
                            "cookies": {}, "auth": {"type": None, "username": None, "password": None}}

# Generated at 2022-06-13 22:35:38.155786
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = {
        'Host': 'httpbin.org',
        'Connection': 'keep-alive',
        'User-Agent': 'HTTPie/0.9.9',
        'Length': '135',
        'Content-Type': 'application/json',
        'Accept': '*/*'
    }
    session = Session('./sessions/httpbin.org/httpbin.org.json')
    session.update_headers(headers)
    assert session.headers == {
        'Host': 'httpbin.org',
        'Connection': 'keep-alive',
        'Length': '135',
        'Accept': '*/*'
    }
    assert session.path == Path('./sessions/httpbin.org/httpbin.org.json')

# Generated at 2022-06-13 22:35:48.009038
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('path')
    assert type(session.header) == RequestHeadersDict
    session['headers'] = {'key1': 'value1', 'key2': 'value2'}
    headers = RequestHeadersDict()
    headers['key3'] = 'value3'
    session.update_headers(headers)
    assert session.get('headers', {}) == {'key3': 'value3'}
    headers['key1'] = None
    session.update_headers(headers)
    assert session.get('headers', {}) == {'key3': 'value3'}


# Generated at 2022-06-13 22:35:59.366843
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    Test Session.update_headers() with different inputs.
    """
    s = Session('test_update_headers')
    s['headers'] = {'key': 'value'}  # default session (not in overloaded test cases)
    assert s['headers'] == {'key': 'value'}

    s.update_headers(RequestHeadersDict())
    assert s['headers'] == {'key': 'value'}  # unchanged

    s.update_headers(RequestHeadersDict({'key': 'value'}))
    assert s['headers'] == {'key': 'value'}  # unchanged

    s.update_headers(RequestHeadersDict({'key': 'value2'}))
    assert s['headers'] == {'key': 'value2'}  # changed


# Generated at 2022-06-13 22:36:14.849977
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session((Path('~').expanduser() / '.config') / SESSIONS_DIR_NAME / 'session.json')
    session.update_headers(RequestHeadersDict({'User-Agent': 'HTTPie/0.9.9', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate'}))
    assert session['headers']['User-Agent'] == 'HTTPie/0.9.9'
    assert session['headers']['Accept'] == '*/*'
    assert session['headers']['Accept-Encoding'] == 'gzip, deflate'

    session2 = Session((Path('~').expanduser() / '.config') / SESSIONS_DIR_NAME / 'session2.json')

# Generated at 2022-06-13 22:36:25.356815
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    self = Session(r'')
    self['headers'] = {}
    self['cookies'] = {}
    self['auth'] = {
        'type': None,
        'username': None,
        'password': None
    }
    request_headers = {
        b'Content-Type': b'application/json',
        b'Authorization': b'Basic foo:bar',
        b'Date': b'2018-10-07T12:34:56+01:00',
        b'Set-Cookie': b'foo=bar; Secure',
        b'Cookie': b'a=b',
        b'User-Agent': b'HTTPie/0.9.9',
    }
    request_headers = RequestHeadersDict(request_headers)
    self.update_headers(request_headers)
    assert self

# Generated at 2022-06-13 22:36:29.750182
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict({'Content-Type': 'application/json'})
    session = Session('http://www.example.org')
    session.update_headers(headers)
    assert 'Content-Type' not in session.headers

# Generated at 2022-06-13 22:36:45.770215
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    SESSION1 = Session(DEFAULT_SESSIONS_DIR / "test2.json")

    SESSION1['cookies']['test1'] = {'value': 'cookies'}
    SESSION1['cookies']['test2'] = {'value': 'cookies'}
    SESSION1['cookies']['test3'] = {'value': 'cookies'}
    assert len(SESSION1['cookies']) == 3

    SESSION1.remove_cookies(['test2'])
    assert len(SESSION1['cookies']) == 2
    assert SESSION1['cookies']['test1']['value'] == 'cookies'
    assert SESSION1['cookies']['test2']['value'] != 'cookies'

# Generated at 2022-06-13 22:36:52.367077
# Unit test for function get_httpie_session
def test_get_httpie_session():
    from httpie.config import Config, DEFAULT_CONFIG_DIR
    from httpie.context import Environment
    from httpie.output.streams import Streams
    from httpie.plugins import plugin_manager
    config = Config(env=Environment(streams=Streams()), dir=DEFAULT_CONFIG_DIR)
    plugin_manager.load_installed_plugins(config=config, env=config.env)
    session = get_httpie_session(config_dir = DEFAULT_CONFIG_DIR, session_name = 'testname', host = 'hostname', url = 'http://localhost')
    assert session.helpurl == 'https://httpie.org/doc#sessions'
    assert session.about == 'HTTPie session file'
    assert session.load == BaseConfigDict.load
    assert session.save == BaseConfigD

# Generated at 2022-06-13 22:36:57.202633
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(Path('./test.json'))
    s.cookies = RequestsCookieJar()
    s.cookies.set_cookie(create_cookie('intouch', '12345', secure=True, domain='localhost'))
    s.cookies.set_cooki

# Generated at 2022-06-13 22:37:07.976252
# Unit test for function get_httpie_session
def test_get_httpie_session():
    config_dir = Path(__file__).parent / 'test' / 'config'
    session_name = 'session'
    host = 'example.com'
    url = 'https://example.com'
    httpie_session = get_httpie_session(config_dir, session_name, host, url)
    print(httpie_session)
    session_path = config_dir / SESSIONS_DIR_NAME / host / f'{session_name}.json'
    assert httpie_session.path == session_path

# Generated at 2022-06-13 22:37:17.290940
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    print("\n")
    print("> Testing Session.remove_cookies()...")

    sess = Session('/tmp/test')
    sess['cookies']['a'] = 1
    sess['cookies']['b'] = 2
    print(sess['cookies'])
    # {'b': 2, 'a': 1}

    sess.remove_cookies(['a'])
    print(sess['cookies'])
    # {'b': 2}



# Generated at 2022-06-13 22:37:27.684147
# Unit test for function get_httpie_session
def test_get_httpie_session():
    config_dir = Path('~/.config/httpie')
    sess_name = 'test_session'
    sess_host = 'foo.example.com'
    sess_url = 'http://foo.example.com/api/'

    sess = get_httpie_session(config_dir, sess_name, sess_host, sess_url)
    path = (
        config_dir / SESSIONS_DIR_NAME / sess_host / f'{sess_name}.json'
    )
    base_config_dict = BaseConfigDict(path)

    assert sess == base_config_dict

# Generated at 2022-06-13 22:37:34.934723
# Unit test for constructor of class Session
def test_Session():
    # create a new session (session_1)
    session_1 = Session(DEFAULT_SESSIONS_DIR, 'session_1')
    assert session_1.name == 'session_1'

    # create a new session (session_2)
    session_2 = Session(DEFAULT_SESSIONS_DIR, 'session_2')
    assert session_2.name == 'session_2'


# Generated at 2022-06-13 22:37:38.939979
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("/tmp/test1")
    s.update_headers({'Cookie': 'a=1; b=2', 'User-Agent': 'test'})
    s.remove_cookies(['a'])
    assert s['cookies'] == {'b': {'value': '2'}}

# Generated at 2022-06-13 22:37:41.445256
# Unit test for constructor of class Session
def test_Session():    
    session = Session(path = 'path')
    assert session[0] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {'type': None, 'username': None, 'password': None }

# Generated at 2022-06-13 22:37:42.325047
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    assert False

# Generated at 2022-06-13 22:37:56.655458
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import pytest
    from httpie.config.browser_cookie_jar import BrowserCookieJar
    from requests.cookies import RequestsCookieJar
    from httpie.plugins.builtin import HTTPBasicAuth, DigestAuth

    def get_cookie_jar(session_file: Path, cookie_name: str) -> RequestsCookieJar:
        """
        Returns a session's cookie jar.
        """
        session = Session(session_file)
        session.load()
        cookie_jar = session.cookies
        return cookie_jar

    def get_session_auth(session_file: Path) -> HTTPBasicAuth or DigestAuth:
        """
        Returns a session's auth plugin.
        """
        session = Session(session_file)
        session.load()
        return session.auth

    # without cookies

# Generated at 2022-06-13 22:38:01.761361
# Unit test for constructor of class Session
def test_Session():
    s = Session('./test.json')
    assert s['headers'] == {}
    assert s['cookies'] == {}
    assert s['auth'] == {
                'type': None,
                'username': None,
                'password': None
                }



# Generated at 2022-06-13 22:38:13.605666
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(None)

    request_headers = {
        'Header-A': 'Value A',
        'Header-B': 'Value B',
        'Content-Type': 'application/json',
        'Content-Length': '123',
        'If-None-Match': 'w/"123"',
        'Cookie': 'A=B; C=D'
    }

    session.update_headers(request_headers)

    assert session.headers == {
        'Header-A': 'Value A',
        'Header-B': 'Value B'
    }

    assert request_headers == {
        'Header-A': 'Value A',
        'Header-B': 'Value B',
        'If-None-Match': 'w/"123"'
    }


# Generated at 2022-06-13 22:38:20.223685
# Unit test for constructor of class Session
def test_Session():
    session = Session('./test-session')
    print(type(session))
    print(session)
    print(session.helpurl)
    print(session.about)
    print('headers', session.headers)
    print('cookies', session.cookies)
    print('auth', session.auth)



# Generated at 2022-06-13 22:38:25.309720
# Unit test for constructor of class Session
def test_Session():
    path = 'C:/Users/.config/httpie/sessions/'
    s = Session(path)
    assert s['headers'] == {}
    assert s['cookies'] == {}
    assert s['auth'] == {
            'type': None,
            'username': None,
            'password': None
        }



# Generated at 2022-06-13 22:38:31.837292
# Unit test for constructor of class Session
def test_Session():
    s = get_httpie_session(DEFAULT_SESSIONS_DIR, 'session_name', None, None)
    assert path == s.path
    assert s.items() == {'headers':{}, 'cookies':{}, 'auth':{'type':None,'username':None,'password':None}}


# Generated at 2022-06-13 22:38:37.125925
# Unit test for constructor of class Session
def test_Session():
    config = Session('test123')
    assert config.path == Path('test123')
    assert config['headers'] == {}
    assert config['cookies'] == {}
    assert config['auth'] == {'type': None, 'username': None, 'password': None}


# Generated at 2022-06-13 22:38:47.065946
# Unit test for function get_httpie_session
def test_get_httpie_session():
    assert get_httpie_session('C:\\Users\\user\\AppData\\Roaming\\httpie\\sessions',
                        'examples.org', 'http://example.org') is not None
    assert get_httpie_session('C:\\Users\\user\\AppData\\Roaming\\httpie\\sessions',
                        'examples.org', 'http://example.org') is not None
    assert get_httpie_session('C:\\Users\\user\\AppData\\Roaming\\httpie\\sessions',
                        'examples.org', 'http://example.org') is not None
    assert get_httpie_session('C:\\Users\\user\\AppData\\Roaming\\httpie\\sessions',
                        'examples.org', 'http://example.org') is not None

# Generated at 2022-06-13 22:38:59.901343
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    #No update_headers
    s=Session("tmp/does/not/mattter")
    s.update_headers({})
    #No update_headers, but basic headers
    s=Session("tmp/does/not/mattter")
    s.update_headers({'User-Agent':'HTTPie/0.9.9', 'Accept-Encoding':'gzip, deflate',
                                 'Accept':'*/*', 'Host':'localhost:8000'})
    #No update_headers, but basic headers and some extra headers
    #T
    s=Session("tmp/does/not/mattter")

# Generated at 2022-06-13 22:39:10.232514
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_path = Path('./tests/fixtures/my_session.json')
    session = Session(session_path)
    session.load()
    assert "phpsessid" in session['cookies']
    assert "__cfduid" in session['cookies']
    assert "visit" in session['cookies']
    assert session['cookies']['visit']['value'] == "1"
    session.remove_cookies(['phpsessid', '__cfduid'])
    assert "phpsessid" not in session['cookies']
    assert "__cfduid" not in session['cookies']
    assert "visit" in session['cookies']
    assert session['cookies']['visit']['value'] == "1"



# Generated at 2022-06-13 22:39:16.731154
# Unit test for constructor of class Session
def test_Session():
    name = 'testSession'
    test = Session(name)
    assert name == test.path


# Generated at 2022-06-13 22:39:25.088268
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict(
        {
            "header-a": "123",
            "Content-Length": 123,
            "If-Modified-Since": "123",
        }
    )
    session = Session("")
    session.update_headers(request_headers)
    assert session.headers == RequestHeadersDict(
        {
            "header-a": "123",
        }
    )

# Generated at 2022-06-13 22:39:32.168145
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    from httpie.utils import StringIO
    from httpie.compat import urlopen

    def mock_urlopen(url, data):
        return StringIO(
            'Set-Cookie: name1=value1; expires=Fri, 01-Jan-2100 00:00:00 GMT\n'
            'Set-Cookie: name2=value2\n'
            'Set-Cookie: name3=value3\n'
        )

    urlopen_real = urlopen
    urlopen = mock_urlopen
    sess = Session('sess')

    # remove cookies with name1
    sess.remove_cookies(['name1'])

    assert 'name1' not in sess['cookies']
    assert 'name2' in sess['cookies']

# Generated at 2022-06-13 22:39:36.553852
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/sessions.json')
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    session.remove_cookies(['cookie2'])
    assert session['cookies'] == {'cookie1': 'value1'}

# Generated at 2022-06-13 22:39:39.003588
# Unit test for function get_httpie_session
def test_get_httpie_session():
    url = 'https://api.example.com'
    result = get_httpie_session( DEFAULT_CONFIG_DIR, 'example', 'api.example.com', url)
    assert result is not None

# Generated at 2022-06-13 22:39:49.941162
# Unit test for constructor of class Session
def test_Session():
    from pathlib import Path
    from httpie.config import DEFAULT_SESSIONS_DIR

    temp_file = 'httpie_session.json'
    temp_path = DEFAULT_SESSIONS_DIR / temp_file

    test_path = 'httpie_session.json'
    session = Session(test_path)
    assert session.path == Path(test_path)
    # print(session['headers'])
    # print(session['cookies'])
    # print(session['auth'])

# Generated at 2022-06-13 22:39:57.938331
# Unit test for function get_httpie_session
def test_get_httpie_session():
    from httpie.context import Environment
    from tests.test_httpserver import TEST_SESSIONS_DIR, TEST_SESSION_NAME

    session1 = get_httpie_session(
        TEST_SESSIONS_DIR,
        TEST_SESSION_NAME,
        None,
        "https://test.test")
    assert session1

    session2 = get_httpie_session(
        TEST_SESSIONS_DIR,
        TEST_SESSION_NAME,
        None,
        "https://test.test")
    assert session2

    assert id(session1) == id(session2)



# Generated at 2022-06-13 22:40:03.419925
# Unit test for function get_httpie_session
def test_get_httpie_session():
    path = '~/.config/httpie/sessions'
    config_dir = Path(path)
    session_name = 'the_session'
    host = 'example.com'
    url = 'http://example.com'

    assert get_httpie_session(config_dir, session_name, host, url).path == config_dir / 'example.com' / 'the_session.json'

# Generated at 2022-06-13 22:40:10.993598
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    r = RequestHeadersDict('cookies: c1=v1; c2=v2; c3=v3')
    s = Session('/tmp/test.session')
    s.update_headers(r)
    assert s['headers'] == {}
    assert s['cookies'] == {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}, 'c3': {'value': 'v3'}}


# Generated at 2022-06-13 22:40:21.262567
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    If a request sets a cookie, the cookie is added to the session's
    cookies, and the cookie is removed from the request's headers.

    Otherwise, all headers are preserved.

    """
    session = Session('/tmp/test_Session_update_headers.json')
    request_headers = RequestHeadersDict({
        'cookie': 'a=b; c=d',
        'content-type': 'application/json',
        'if-match': 'W/"xyzzy"',
        'user-agent': 'HTTPie/0.9.2'
    })
    session.update_headers(request_headers)

# Generated at 2022-06-13 22:40:29.497395
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    assert True

# Generated at 2022-06-13 22:40:36.241005
# Unit test for constructor of class Session
def test_Session():
    path = '/tmp/httpie/sessions/hostname/session_name.json'
    session = Session(path)
    assert isinstance(session, BaseConfigDict)
    assert session.path == path
    assert session['headers'] == {}
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:40:45.166001
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('hello')
    assert sess
    saved_cookies  = {
        'cookies':{
            'token':{
                'value':'test_token'
            },
            'test_name':{
                'value':'test_value'
            }
        }
    }
    new_cookies = {
        'cookies':{
            'token':{
                'value':'test_token'
            }
        }
    }

    sess.update(saved_cookies)
    #assert sess.get('cookies') == saved_cookies.get('cookies')
    sess.remove_cookies(['test_name'])
    assert sess == new_cookies

# Generated at 2022-06-13 22:40:47.324409
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session['cookies'] = {'a': 'b', 'c': 'd'}
    session.remove_cookies(['a', 'b'])
    assert session['cookies'] == {'c': 'd'}


# Generated at 2022-06-13 22:40:55.179543
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/httpie_testing/test_session')
    session['cookies'] = {
        'xyz': {'value': 'xyz'},
        'abc': {'value': 'abc'},
        'cde': {'value': 'cde'}
    }
    names = ['xyz', 'abc']
    session.remove_cookies(names)
    assert session['cookies'] == {'cde': {'value': 'cde'}}

# Generated at 2022-06-13 22:41:00.530140
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session({'cookies':{'a':'1','b':'2','c':'3'}})
    session.remove_cookies(['a','c'])
    assert session == {'cookies':{'b':'2'}}



# Generated at 2022-06-13 22:41:08.385667
# Unit test for function get_httpie_session
def test_get_httpie_session():

    session_name = 'localhost'
    host = 'localhost'
    url = 'http://localhost/sessions'

    config_dir = Path('/config')
    session = get_httpie_session(config_dir, session_name, host, url)
    path = session.path
    assert path == Path('/config/sessions/localhost/localhost.json')

    config_dir = Path('/config')
    host = None
    url = 'http://localhost/sessions'
    session = get_httpie_session(config_dir, session_name, host, url)
    path = session.path
    assert path == Path('/config/sessions/localhost/localhost.json')

    config_dir = Path('/config')
    host = 'localhost'
    url = 'http://localhost:8111/sessions'
   

# Generated at 2022-06-13 22:41:11.205778
# Unit test for function get_httpie_session
def test_get_httpie_session():
    print(str(get_httpie_session(DEFAULT_CONFIG_DIR, '123', 'localhost', 'http://localhost')))

# Generated at 2022-06-13 22:41:17.045734
# Unit test for function get_httpie_session
def test_get_httpie_session():
    config_dir = Path('~/.httpie').expanduser()
    session_name = 'sessions-dir'
    host = None
    url = 'http://127.0.0.1'
    get_httpie_session(config_dir, session_name, host, url)

# Generated at 2022-06-13 22:41:23.549690
# Unit test for constructor of class Session
def test_Session():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.json')
    if os.path.isfile(path):
        os.remove(path)
    s = Session(path)
    assert s.path == Path(path)
    assert s['headers'] == {}
    assert s['cookies'] == {}
    assert s['auth']['type'] == None
    assert s['auth']['username'] == None
    assert s['auth']['password'] == None

# Generated at 2022-06-13 22:41:44.430882
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session=Session('/root/httpie-0.9.2/httpie/config/.httpie/sessions/localhost')
    session.load()
    session.remove_cookies(['name'])
    aut_value = session.get('auth')
    cookies_value = session.get('cookies')
    head_value = session.get('headers')
    assert aut_value is None
    assert cookies_value == {}
    assert head_value == {}

# Generated at 2022-06-13 22:41:49.135726
# Unit test for constructor of class Session
def test_Session():
    from httpie.cli.dicts import RequestHeadersDict

    session = Session(path='test')
    assert session.headers == RequestHeadersDict({})


# Generated at 2022-06-13 22:41:57.767782
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('~/.httpie/sessions/foo-bar.json')
    s = Session(path)
    s.load()
    s['cookies'] = {
        "foo": {
            "value": "42"
        },
        "bar": {
            "value": "42"
        },
        "baz": {
            "value": "42"
        },
    }
    s.remove_cookies(("bar", "baz"))
    assert s['cookies'] == {
        "foo": {
            "value": "42"
        },
    }, "remove_cookies expecting {'foo': {'value': '42'}}, got %s" % s["cookies"]



# Generated at 2022-06-13 22:42:02.384731
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sessions = Session('sessions/test1')
    cookies = {"Name_1" : "Cookies_1", "Name_2" : "Cookies_2"}
    sessions["cookies"] = cookies
    sessions.remove_cookies(["Name_1"])
    assert not sessions["cookies"]["Name_1"]

# Generated at 2022-06-13 22:42:07.327849
# Unit test for constructor of class Session
def test_Session():

    # Test simple constructor
    path = 'test.json'
    session = Session(path)

    assert type(session) is Session
    assert session.path is Path(path)
    assert session['headers'] is {}
    assert session['cookies'] is {}
    assert session['auth'] is {
        'type' : None,
        'username': None,
        'password': None
    }


# Generated at 2022-06-13 22:42:18.355889
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s.cookies = RequestsCookieJar()
    s.cookies.set('name1', 'value1', path='/', secure=True)
    s.cookies.set('name2', 'value2', path='/')
    s.cookies.set('name3', 'value3', path='/')
    assert len(s.cookies) == 3

    s.remove_cookies(['name2', 'name3'])
    assert len(s.cookies) == 1
    assert next(iter(s.cookies)) == 'name1'

# Generated at 2022-06-13 22:42:21.056409
# Unit test for function get_httpie_session
def test_get_httpie_session():
    session = get_httpie_session(DEFAULT_CONFIG_DIR, "session", "host", "url")
    assert isinstance(session, Session)

# Generated at 2022-06-13 22:42:26.820709
# Unit test for constructor of class Session
def test_Session():
    session_file_name = 'test'
    session = Session(session_file_name)
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }

# Generated at 2022-06-13 22:42:28.109656
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session.remove_cookies(['test'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:42:31.291341
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(['b', 'c'])
    assert len(s['cookies']) == 1
    assert s['cookies']['a'] == 1

# Generated at 2022-06-13 22:43:15.591993
# Unit test for function get_httpie_session
def test_get_httpie_session():
    get_httpie_session(
        config_dir = Path(__file__).parent,
        session_name = "test",
        host = None,
        url = "https://test.com/test",
    )