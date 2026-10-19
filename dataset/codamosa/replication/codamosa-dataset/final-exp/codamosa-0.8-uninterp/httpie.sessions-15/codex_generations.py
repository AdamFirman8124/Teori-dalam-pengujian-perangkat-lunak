

# Generated at 2022-06-13 22:33:28.386428
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    #Test for cookie-header
    session = Session('abc')
    request_headers = RequestHeadersDict()
    request_headers['Cookie'] = 'abc'
    session.update_headers(request_headers)
    assert session.headers == RequestHeadersDict()
    assert session['cookies'] == {'abc': {'value': 'abc'}}
    session['cookies'] = {}

    # Test with multiple cookies
    request_headers['Cookie'] = 'a=1; b=2'
    session.update_headers(request_headers)
    assert session.headers == RequestHeadersDict()
    assert session['cookies'] == {'a': {'value': '1'},
                                  'b': {'value': '2'}}
    session['cookies'] = {}

    # Test with a mix
   

# Generated at 2022-06-13 22:33:41.601974
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # initialize an empty Session object
    session = Session('./test_session.json')

    # update_headers() with headers that contain cookie
    request_headers = {
        'User-Agent': 'HTTPie/1.1.2',
        'foo': 'bar',
        'Cookie': 'foo=bar; name=value'
    }

    session.update_headers(request_headers)

    # normal headers should be stored in session
    assert session.headers == {'foo': 'bar'}

    # cookie's name and value should be stored in json-serialized session
    assert session.cookies == {'foo': 'bar', 'name': 'value'}

# Generated at 2022-06-13 22:33:47.267800
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict()
    headers['cookie'] = 'foo="bar"'
    headers['Cookie'] = 'bar="baz"'
    session = Session('')
    session.update_headers(headers)
    assert session['headers'] == {}
    assert session['cookies'] == {'foo': {'value': '"bar"'},
                                  'bar': {'value': '"baz"'}}


# Generated at 2022-06-13 22:33:54.410876
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("test")
    session["headers"] = {"Content-Type": "application/json", "headers": "headers1", "If-Match": "If-Match1"}

    headers = RequestHeadersDict({"Content-Type": "application/json", "headers": "headers2", "If-Match": "If-Match2"})
    session.update_headers(headers)
    assert session["headers"] == {"headers": "headers2"}

# Generated at 2022-06-13 22:34:00.178850
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(Path('test'))
    session.update_headers(RequestHeadersDict(
        {'a': 'foo', 'content-type': 'application/json'}))
    assert session['headers'] == {'a': 'foo'}



# Generated at 2022-06-13 22:34:11.698711
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.context import Environment
    import httpie.cli.argtypes

    session = Session(path=f'{DEFAULT_CONFIG_DIR}/session_test.json')

    session.update_headers({
        'User-Agent': None,
        'Content-Type': 'text/html',
        'If-Matched': '*',
        'Cookie': 'foo=bar; fizz=buzz',
    })
    session.save()


# Generated at 2022-06-13 22:34:17.149827
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {"name1": "value1", "name2": "value2"}
    session.remove_cookies(["name1"])
    assert len(session['cookies']) == 1
    assert "name1" not in session['cookies']
    assert "name2" in session['cookies']

# Generated at 2022-06-13 22:34:22.936417
# Unit test for method update_headers of class Session
def test_Session_update_headers():
	from httpie.cli.dicts import RequestHeadersDict
	s = Session("test/sessions/host/123.json")
	s.update_headers({'Cookie':'123', 'Content-Type':None, 'If-Modified-Since':'1234'})
	print(s.headers)
	assert {'Cookie':'123'} == s.headers
	

# Generated at 2022-06-13 22:34:28.077853
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(Path('~/.httpie/sessions/'))
    headers = {'a': 'b', 'c': ['d', 'e', 'f']}
    s.update_headers(headers)
    assert s['headers'] == {'a': 'b', 'c': 'd,e,f'}

# Generated at 2022-06-13 22:34:36.295824
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/test-session')
    request_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'lang=en; country=us',
            'User-Agent': 'HTTPie/1.0.3',
            'DNT': '1',
            }
    session.update_headers(request_headers)
    print("test_Session_update_headers: ", session)

# Generated at 2022-06-13 22:34:48.574473
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/foo.txt')
    s.cookies = RequestsCookieJar()
    s.cookies.set('foo', 'value')
    s.cookies.set('bar', 'value')

    s.remove_cookies('bar')
    assert len(s.cookies) == 1
    assert 'bar' not in s.cookies
    assert 'foo' in s.cookies

    s.remove_cookies('foo')
    assert len(s.cookies) == 0
    assert 'bar' not in s.cookies
    assert 'foo' not in s.cookies

# Generated at 2022-06-13 22:34:58.028210
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    import json
    import tempfile

    session_path = Path(tempfile.mkdtemp()) / 'session.json'
    session = Session(session_path)
    session['cookies'] = {'foo': {'value': 'bar'}}

    # remove existing
    session.remove_cookies(['foo'])
    assert json.loads(session_path.read_text())['cookies'] == {}

    # remove non-existing
    session.remove_cookies(['foo'])
    assert json.loads(session_path.read_text())['cookies'] == {}

# Generated at 2022-06-13 22:35:05.789975
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test = dict()
    test['cookies'] = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    test_del = ['a', 'c', 'e']
    expected = dict()
    expected['cookies'] = {'b': 2, 'd': 4}
    new_session = Session('http://localhost:3030')
    new_session['cookies'] = test['cookies']
    new_session.remove_cookies(test_del)
    assert expected == new_session


# Generated at 2022-06-13 22:35:19.089881
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
        Test remove_cookies
    """

    session = Session(path='test')
    session['cookies'] = {
        'test': {
            'path': 'test',
            'value': 'test'
        }
    }
    assert session['cookies']['test']['value'] == 'test'
    session['cookies'] = {
        'test': {
            'path': 'test',
            'value': 'test'
        },
        'test2': {
            'path': 'test2',
            'value': 'test2'
        }
    }
    assert session['cookies']['test']['value'] == 'test'
    session.remove_cookies(['test'])
    assert session['cookies']['test2']['value'] == 'test2'

# Generated at 2022-06-13 22:35:26.486289
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    config_dir = Path('/tmp/httpie-config')
    session_name = "test"
    path = config_dir / SESSIONS_DIR_NAME / session_name / f'{session_name}.json'
    session = Session(path)
    session['cookies'] = {
        'session_id': {'value': '123abc'},
        'csrf_token': {'value': '456xyz'},
        'other_cookie': {'value': '789uio'},
    }
    session.remove_cookies(['session_id', 'csrf_token'])
    assert(not session['cookies'])

# Generated at 2022-06-13 22:35:39.927855
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('dummy_path')
    cookies_dict = {
        'cookie1': {
            'value': 'cookie1_value',
            'path': '/'
        },
        'cookie2': {
            'value': 'cookie2_value',
            'path': '/'
        }
    }
    session['cookies'] = cookies_dict
    assert session['cookies'] == cookies_dict
    session.remove_cookies(names=['cookie1'])
    assert session['cookies'] == {
        'cookie2': {
            'value': 'cookie2_value',
            'path': '/'
        }
    }
    session.remove_cookies(names=['cookie1', 'cookie2'])
    assert session['cookies'] == {}
    session.remove_cookies(names=[])


# Generated at 2022-06-13 22:35:45.058895
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #-----------------arrange-------------------------
    cookie_name = 'cookie1'
    session = Session(None)
    session['cookies'][cookie_name] = 'value1'

    #-----------------act-----------------------------
    session.remove_cookies(['cookie1'])

    #-----------------assert--------------------------
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:35:55.862148
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Test of method remove_cookies of class Session.
    """
    # Create instance of class Session
    session = Session(path=Path('./test_Session_remove_cookies.json'))
    # Create a dictionnary of cookies
    cookies = {'a': '1', 'b': '2', 'c': '3'}
    # Add this dictionnary to session
    session['cookies'] = cookies
    session.remove_cookies(['a'])
    # Test that cookie 'a' is removed
    assert 'a' not in session['cookies']



# Generated at 2022-06-13 22:35:59.754581
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="test")
    session['cookies'] = {'abc': {'value': 'abc'}}
    session.remove_cookies(['abc'])
    assert session['cookies'] == {}


# Generated at 2022-06-13 22:36:10.959413
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {}
    s['cookies']['aaa'] = {'value': 1}
    s['cookies']['bbb'] = {'value': 2}
    s['cookies']['ccc'] = {'value': 3}
    s.remove_cookies(['cca', 'ccc'])
    assert s['cookies']['aaa'] == {'value': 1}
    assert s['cookies']['bbb'] == {'value': 2}
    assert 'ccc' not in s['cookies']

# Generated at 2022-06-13 22:36:21.754305
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class A:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    jar = [A('cookie', 'value'), A('cookie1', 'value'), A('to_delete', 'value')]
    session = Session('test_session')
    session.cookies = jar
    session.remove_cookies(['to_delete'])
    assert len(session['cookies']) == 2



# Generated at 2022-06-13 22:36:29.887457
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Test that cookies are removed properly.
    """
    # define the session and the cookies
    session_name = 'test'
    host = 'www.google.com'
    url = 'www.google.com'

# Generated at 2022-06-13 22:36:37.418400
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Create new Session
    test_session_dir = DEFAULT_SESSIONS_DIR / 'test_Session'
    test_session_dir.mkdir(parents=True, exist_ok=True)
    test_sesssion_file = test_session_dir / 'test_remove_cookies.json'
    test_session = Session(test_sesssion_file)

    # Populate test session with data
    test_session['headers'] = {'header1': 'value1'}
    test_session['cookies'] = {
        'cookie1': {'cookie1': 'value1'},
        'cookie2': {'cookie2': 'value2'},
        'cookie3': {'cookie3': 'value3'},
    }
    test_headers = test_session['headers']
    test_cook

# Generated at 2022-06-13 22:36:46.465271
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import requests
    # cookies = requests.utils.dict_from_cookiejar(requests.request(
    #     'get',
    #     'http://httpbin.org/cookies',
    #     cookies={
    #         'A': '3',
    #         'B': '4'
    #     }
    # ).cookies)

    cookies = {
        'A': '3',
        'B': '4'
    }

    s = Session(None)
    s.cookies = requests.cookies.cookiejar_from_dict(cookies)
    s.remove_cookies(('A', 'B'))
    assert not s.cookies

# Generated at 2022-06-13 22:36:51.435392
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('http://httpbin.org/cookies/set')

    # remove cookie not exist
    session.remove_cookies(['name1'])

    # remove cookie exist
    session['cookies']['name1'] = True
    session.remove_cookies(['name1'])
    assert session['cookies'].get('name1') is None


# Generated at 2022-06-13 22:36:59.308362
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test-session-name')
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie('test-cookie-name', 'test-value'))
    assert list(session.get('cookies').keys()) == ['test-cookie-name']
    session.remove_cookies(['test-cookie-name'])
    assert list(session.get('cookies').keys()) == []
    session.cookies.set_cookie(create_cookie('test-cookie-name', 'test-value'))
    assert list(session.get('cookies').keys()) == ['test-cookie-name']
    session.remove_cookies(['not-exist'])
    assert list(session.get('cookies').keys()) == ['test-cookie-name']

# Generated at 2022-06-13 22:37:09.837597
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_name_list = []
    cookie_list = []
    session = Session(path="")
    for i in range(20):
        cookie_name_list.append('cookie_' + str(i))
        cookie_list.append(dict(Name=cookie_name_list[i], Value=i))
    session['cookies'] = dict(zip(cookie_name_list, cookie_list))
    cookie_name_list.pop(1)
    cookie_name_list.pop(12)
    cookie_name_list.pop(14)
    session.remove_cookies(cookie_name_list)
    assert len(session['cookies']) == 3
    assert 'cookie_1' not in session['cookies']
    assert 'cookie_12' not in session['cookies']
    assert 'cookie_14'

# Generated at 2022-06-13 22:37:14.814059
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('path')
    test_session['cookies'] = {'name': {'value': 'value'}}
    test_session.remove_cookies(['name'])
    assert 'name' not in test_session['cookies']

# Generated at 2022-06-13 22:37:19.759027
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('')
    sess.update({"cookies": {'one': '1', 'two': '2'}})
    sess.remove_cookies(['one'])
    assert sess['cookies'] == {'two': '2'}

# Generated at 2022-06-13 22:37:26.344120
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session('./test')
    sess['cookies'] = {'test': {'value': '20'}, 
                       'test2': {'value': '21'}}
    sess.remove_cookies(['test'])
    assert sess['cookies'] == {'test2': {'value': '21'}}


# Generated at 2022-06-13 22:37:36.831847
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session.update({'cookies': {'test': 'value'}})
    session.remove_cookies(['test'])
    assert session == {'cookies': {}, 'auth': {'type': None, 'username': None, 'password': None}}

# Generated at 2022-06-13 22:37:40.961386
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s['cookies'] = {'name1': 'value1', 'name2': 'value2'}
    s.remove_cookies(['name1', 'name3'])
    assert(s['cookies'] == {'name2': 'value2'})

# Generated at 2022-06-13 22:37:48.577717
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    '''
    Test for Session.remove_cookies method
    '''
    session = Session('')
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie(
        'cookie_name', 'session_value', domain='', expires=None, secure=False, path='/'))
    session.remove_cookies(['cookie_name'])
    assert len(session.cookies) == 0

# Generated at 2022-06-13 22:37:56.821568
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path(__file__)
    session = Session(path)
    session.load()
    session['cookies'] =  {"foo": "bar", "baz": "qux"}
    session.remove_cookies(["foo"])
    assert not session['cookies']
    session['cookies'] =  {"foo": "bar", "baz": "qux"}
    session.remove_cookies(["baz"])
    assert not session['cookies']
    session['cookies'] =  {"foo": "bar", "baz": "qux"}
    session.remove_cookies(["qux"])
    assert not session['cookies']
    session['cookies'] =  {"foo": "bar", "baz": "qux"}
    session.remove_cookies(["foo","baz"])

# Generated at 2022-06-13 22:38:01.982306
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/test_session.json')
    s['cookies'] = {'token': {'value': '12345-67890'}}
    s.remove_cookies(['token'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:38:02.741381
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    pass

# Generated at 2022-06-13 22:38:12.847575
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.sessions import Session
    from httpie.compat import BytesIO
    from httpie.output.streams import BytesIORawIO
    from httpie.output.streams import FileBytesRawIO
    path = BytesIO()
    session_test = Session(BytesIORawIO(path))
    session_test['cookies'] = {'abc':{'value':'value'}, 'cde':{'value':'value'}}
    session_test.remove_cookies(['abc'])
    assert session_test['cookies'] == {'cde':{'value':'value'}}

# Generated at 2022-06-13 22:38:22.296589
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=None)
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(create_cookie('key1', 'value1'))
    session.cookies.set_cookie(create_cookie('key2', 'value2'))
    assert len(session.cookies) == 2
    session.remove_cookies(['key1'])
    assert len(session.cookies) == 1
    assert next(iter(session.cookies)).name == 'key2'

test_Session_remove_cookies()

# Generated at 2022-06-13 22:38:28.078531
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test")
    cookie_jar = RequestsCookieJar()
    cookie_jar.set("aa", "value1", path="/", secure=False, expires=None)
    cookie_jar.set("bb", "value2", path="/", secure=False, expires=None)
    session.cookies = cookie_jar
    session.remove_cookies(["aa"])
    assert session.cookies == [{"name": "bb", "value": "value2", "path": "/",
                                "secure": False, "expires": None}]

# Generated at 2022-06-13 22:38:32.633831
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s=Session('a')
    a={'x':1,'y':2}
    s.cookies=a
    s.remove_cookies(['x'])
    assert s.cookies=={'y':2}

# Generated at 2022-06-13 22:38:43.163485
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    obj = Session(None)
    obj.cookies = RequestsCookieJar()
    obj.cookies.set('exampleCookie', 'value')
    obj.remove_cookies(['exampleCookie'])
    assert len(obj['cookies']) == 0



# Generated at 2022-06-13 22:38:49.304278
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="test.json")
    session['cookies'] = {
        'key1':'value1',
        'key2':'value2'
    }
    session.remove_cookies(['key1'])
    assert session['cookies'] == {
        'key2':'value2'
    }, "test failed"

# Generated at 2022-06-13 22:38:55.348318
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('sessions/test_Session_remove_cookies')
    s['cookies'] = {'c1': 'v1', 'c2': 'v2'}
    s.remove_cookies(['c1'])
    assert s['cookies'] == {'c2': 'v2'}



# Generated at 2022-06-13 22:39:00.089467
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test.json')
    session['cookies'] = {'foo': 'bar'}
    assert len(session['cookies']) == 1
    session.remove_cookies(['foo'])
    assert len(session['cookies']) == 0
        


# Generated at 2022-06-13 22:39:10.352497
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Unit test for method remove_cookies of class Session
    """
    s = Session(path='')
    s['cookies'] = {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    s.remove_cookies(('c1',))
    assert s['cookies'] == {'c2': {'value': 'v2'}}
    s.remove_cookies(('c3', 'c4'))
    assert s['cookies'] == {'c2': {'value': 'v2'}}
    s.remove_cookies(('c2',))
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:39:18.465254
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = 'sessions/localhost/default.json'
    session = Session(path)
    assert session['cookies'] == {}
    session['cookies'] = {
        'foo': {'value': 'bar'},
        'abc': {'value': 'def'}
    }
    assert session['cookies'] == {
        'foo': {'value': 'bar'},
        'abc': {'value': 'def'}
    }
    session.remove_cookies(['abc'])
    assert session['cookies'] == {
        'foo': {'value': 'bar'}
    }
    session.remove_cookies('foo')
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:39:29.235828
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('C:/httpie/test_session.json')
    session['cookies'] = {'session': 
        {'value': 'cookie-value', 
        'path': '/path', 
        'secure': True, 
        'expires': '2019-03-06T10:38:43.749Z'
        }
    }
    assert session['cookies'] == {'session': 
        {'value': 'cookie-value', 
        'path': '/path', 
        'secure': True, 
        'expires': '2019-03-06T10:38:43.749Z'
        }
    }
    session.remove_cookies(['session'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:39:39.478410
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    json_file = DEFAULT_SESSIONS_DIR / 'localhost'
    if not json_file.exists():
        json_file.mkdir()
    json_file = json_file/'httpie.json'
    session = Session(json_file)

# Generated at 2022-06-13 22:39:48.473354
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_dict = {"headers": {}, "cookies": {"a": 1, "b": 2, "c": 3}, "auth": {"type": None, "username": None, "password": None}}
    session = Session(Path())
    session.data = session_dict
    session.remove_cookies(["a", "c"])
    assert session_dict["cookies"] == {"b": 2}


# Generated at 2022-06-13 22:39:55.031670
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.sessions import Session
    from httpie.cli.argtypes import parse_items

    s = Session('s')
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(parse_items('a b'))
    assert s['cookies'] == {'c': 3}

# Generated at 2022-06-13 22:40:12.869935
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Case 1: None input
    sess = Session('path')
    sess.remove_cookies(None)

    # Case 2: not empty input, and the cookie is not present in the session
    sess.remove_cookies(['B'])

    # Case 3: not empty input, and the cookie is present in the session
    sess['cookies'] = {'A' : {'value': 'A_value'}}
    sess.remove_cookies(['A'])


# Generated at 2022-06-13 22:40:17.102357
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/httpie.json')
    s['cookies'] = {'a':'1'}
    assert s['cookies'] == {'a':'1'}
    s.remove_cookies('a')
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:40:26.065375
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie import ExitStatus
    from httpie.context import Environment
    from httpie.plugins import builtin
    from httpie.output.streams import ColorizedStream
    from pygments import highlight
    from httpie.output.formatters.colors import get_lexer
    from pygments.formatters import TerminalFormatter
    from pygments.token import Keyword, Name, Comment, String, Error, \
        Number, Operator, Generic, Whitespace, Text, Literal
    from tests.utilities import TestEnvironment, http, HTTP_OK, COLOR, CRLF
    session = Session('sessions/test')
    session['headers'] = {'user-agent': 'httpie'}
    session.update_headers({'content-type': 'application/json'})

# Generated at 2022-06-13 22:40:41.271192
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    from collections import OrderedDict
    from pathlib import Path

    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    cookies = {'key1': 'value1', 'key2': 'value2'}
    auth = {"type": "basic", "raw_auth": "user:password"}

    session = Session(Path('testSession'))

    session['headers'] = headers
    session['cookies'] = cookies
    session['auth'] = auth
    session.save()

    # test remove_cookies of class Session
    session.remove_cookies(['key1'])
    assert session.keys() == {'auth', 'cookies', 'headers'}
    assert session['headers'] == headers
    assert session['auth'] == auth
    assert session['cookies']

# Generated at 2022-06-13 22:40:43.613898
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(path=Path('./test_data/test1.json'))
    s.load()
    s.remove_cookies(['PHPSESSID'])
    assert len(s['cookies']) == 1
    s.remove_cookies(['CSRF_TOKEN'])
    assert len(s['cookies']) == 0

# Generated at 2022-06-13 22:40:47.901760
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='')
    session.cookies = RequestsCookieJar()
    session.cookies.set('test1', 'test1')
    session.cookies.set('test2', 'test2')
    session.cookies.set('test3', 'test3')
    session.remove_cookies(('test1','test2','test4'))
    assert session.cookies.get('test1') == None
    assert session.cookies.get('test2') == None
    assert session.cookies.get('test3') != None

# Generated at 2022-06-13 22:40:56.012427
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.session import Session

    session = Session('')
    session['cookies'] = {
        'cookiename1': {'value': 'cookievalue1'},
        'cookiename2': {'value': 'cookievalue2'}
    }

    session.remove_cookies(['cookiename1', 'cookiename3'])

    assert session['cookies'] == {
        'cookiename2': {'value': 'cookievalue2'}
    }

# Generated at 2022-06-13 22:41:01.100111
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("sessions/session_test.json")
    s["cookies"] = {"abc": {}, "def": {}, "ghi": {}}
    s.remove_cookies(["def", "jkl"])
    assert s["cookies"] == {"abc": {}, "ghi": {}}

# Generated at 2022-06-13 22:41:04.778214
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('https://www.google.com')
    session['cookies'] = {'name':'Google','value':'Hello', 'domain':'google.com'}
    session.remove_cookies(['name'])
    assert not session['cookies']


# Generated at 2022-06-13 22:41:05.534529
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    pass



# Generated at 2022-06-13 22:41:37.445573
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'a': '1', 'b': '2', 'c': '3'}
    s = Session('foo')
    s.cookies = cookies
    assert(s.cookies == cookies)
    s.remove_cookies(['a', 'c'])
    assert(s.cookies == {'b': '2'})

# Generated at 2022-06-13 22:41:47.190055
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("")
    session["cookies"] = {}
    session.remove_cookies(['cookie1'])
    assert session["cookies"] == {}

    session = Session("")
    session["cookies"] = {'cookie1': {'value': 'value'}}
    session.remove_cookies(['cookie1'])
    assert session["cookies"] == {}

    session = Session("")
    session["cookies"] = {'cookie1': {'value': 'value'}}
    session.remove_cookies(['cookie1', 'cookie2'])
    assert session["cookies"] == {}

    session = Session("")
    session["cookies"] = {'cookie1': {'value': 'value'}}
    session.remove_cookies(['cookie2'])

# Generated at 2022-06-13 22:41:50.604234
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.argtypes import KeyValueArg
    from httpie.session import Session
    from httpie.plugins.builtin import HTTPBasicAuth
    session = Session('cookie_test_remove.json')
    session['headers'] = {'Content-Type': 'application/json'}
    session.auth = {'type': 'basic', 'raw_auth': 'user:pass'}
    session.cookies = HTTPBasicAuth.parse_auth('user:pass')
    session.remove_cookies(['user'])
    assert not session['cookies']

# Generated at 2022-06-13 22:41:58.856653
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    a = Session('/test')
    a['cookies'] = {'test': 'value', 'test2': 'value2'}
    assert (sorted(a['cookies'].keys()) == ['test', 'test2'])
    names = ['test']
    a.remove_cookies(names)
    assert (sorted(a['cookies'].keys()) == ['test2'])

# Generated at 2022-06-13 22:42:03.101820
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'name1': {'value': 'val1'}, 'name2': {'value': 'val2'}}
    session = Session(Path('session_file'))
    session['cookies'] = cookies
    session.remove_cookies(['name1'])
    assert session['cookies'] == {'name2': {'value': 'val2'}}



# Generated at 2022-06-13 22:42:07.369178
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/testSession')
    session['cookies'] = {'a': {'value': 'b'}, 'c': {'value': 'd'}}
    session.remove_cookies(['a', 'b'])
    assert session['cookies'] == {'c': {'value': 'd'}}

# Generated at 2022-06-13 22:42:20.676704
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("/path/to/session.json")
    session['cookies']['jsessionid'] = {'value': 'JSESSIONID=A764B9A6C7588F4A4A4E7A36D3F065E6', 'path':'/'}
    session['cookies']['id'] = {'value': 'ID=A764B9A6C7588F4A4A4E7A36D3F065E6', 'path':'/'}
    session['cookies']['cookie'] = {'value': 'COOKIE=A764B9A6C7588F4A4A4E7A36D3F065E6', 'path':'/'}
    session.remove_cookies(['id', 'cookie'])
    assert session

# Generated at 2022-06-13 22:42:26.562369
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='../httpie/tests/.httpie/sessions/test.json')
    session['cookies'] = {'name': {'val': 2}}
    session.remove_cookies(['name'])
    assert session['cookies'] == {}
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:42:29.809850
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("test")
    s['cookies'] = {'name1': 'value1', 'name2': 'value2', 'name3': 'value3'}
    s.remove_cookies(['name2','name3'])
    assert s['cookies'] == {'name1': 'value1'}

# Generated at 2022-06-13 22:42:31.601427
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(None)
    session['cookies'] = {'foo': 'bar'}
    session.remove_cookies(['foo'])
    assert session['cookies'] == {}