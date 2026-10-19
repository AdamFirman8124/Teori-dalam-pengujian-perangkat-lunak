

# Generated at 2022-06-13 22:33:40.656169
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_path = "~/.httpie/sessions/httpbin_org/test_session.json"
    session = Session(session_path)
    session.load()
    session.remove_cookies(["foo"])
    assert "foo" not in session["cookies"]
    session.remove_cookies(["bar"])
    assert "bar" not in session["cookies"]
    session["cookies"]["foo"] = {'value': 'foo-value', 'path': '/'}
    session["cookies"]["bar"] = {'value': 'bar-value', 'path': '/'}
    session["cookies"]["qux"] = {'value': 'qux-value', 'path': '/'}
    session.remove_cookies(["foo", "foo"])

# Generated at 2022-06-13 22:33:46.921089
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # assert that method remove_cookies works for class Session
    # when the session file contains no cookies
    path = 'tests/sessions/test_remove_cookies_1.json'
    s = Session(path)
    s.load()
    s.remove_cookies(['cookie1', 'cookie2', 'cookie3'])
    assert len(s['cookies']) == 0

    # assert that method remove_cookies works for class Session
    # when the session file contains cookies
    path = 'tests/sessions/test_remove_cookies_2.json'
    s = Session(path)
    s.load()
    s.remove_cookies(['cookie1', 'cookie2', 'cookie3'])
    assert len(s['cookies']) == 0



# Generated at 2022-06-13 22:33:54.505176
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(config_dir=Path(__file__).parent, session_name="test", host=None, url="http://localhost:80")
    s['cookies'] = {'cookie1': {'value': 'c1'}, 'cookie2': {'value': 'c2'}}
    s.remove_cookies(['cookie1'])
    assert s['cookies']['cookie1'] == {'value': 'c1'}



# Generated at 2022-06-13 22:33:58.288001
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/home/test.json')
    s.headers = {'Content-Type': 'application/json'}
    s.headers = {}
    print(s.headers)

# Generated at 2022-06-13 22:34:02.706527
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict({'Content-Type': 'application/json', 'Accept': 'text/plain'})
    session = Session('foo.json')
    session.update_headers(request_headers)
    assert session['headers'] == {'Content-Type': 'application/json', 'Accept': 'text/plain'}

# Generated at 2022-06-13 22:34:11.214912
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('test')
    s['headers'] = {'header1': 'value1', 'header2': 'value2'}
    request_headers = RequestHeadersDict()
    request_headers.add('header1', 'value1')
    request_headers.add('header3', 'value3')
    s.update_headers(request_headers)
    assert s['headers'] == {'header1': 'value1', 'header2': 'value2',
                            'header3': 'value3'}



# Generated at 2022-06-13 22:34:17.149435
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(None)
    s.update_headers({'test1': 'test1-value', 'test2': 'test2-value', 'test3': 'test3-value'})
    assert s['headers'] == {'test1': 'test1-value', 'test2': 'test2-value'}, "Method update_headers is not working"



# Generated at 2022-06-13 22:34:22.884773
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    ses = Session('/path/to/session')
    ses['cookies'] = {'c1': {'value': 1}, 'c2': {'value': 2}}
    ses.remove_cookies(['c1'])
    assert ses['cookies'] == {'c2': {'value': 2}}

# Generated at 2022-06-13 22:34:33.285919
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session()
    req_headers = {
        'Content-Type': 'application/json',
        'Content-Length': '10',
        'Cookie': 'a=1; b=2',
        'user-agent': 'HTTPie/1.0.3',
        'If-None-Match': 'xxx',
        'Host': 'localhost:8080'
    }
    session.update_headers(req_headers)
    assert session.headers == {
        'Content-Type': 'application/json',
        'Cookie': 'a=1; b=2',
        'user-agent': 'HTTPie/1.0.3',
        'Host': 'localhost:8080'
    }

# Generated at 2022-06-13 22:34:37.385172
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = {}
    request_headers = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    session = Session(path='/sessions/test_Session.json')
    session.update_headers(request_headers)
    assert session['headers'] == request_headers

# Generated at 2022-06-13 22:34:49.851507
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    import json
    from httpie.session import Session
    from httpie.cli.dicts import RequestHeadersDict

    request_headers = RequestHeadersDict(
        Authorization='Basic: abc',
        Cookie='a=b;c=d',
        Host='example.com',
        Content_Type='text/html',
        If_Modified_Since='Sun, 01 Jan 2017 00:00:00 GMT',
        User_Agent='HTTPie/1.0.0',
        X_Custom='1, 2, 3',
        Z_Custom_X='X'
    )

    session = Session('')
    session.update_headers(request_headers)


# Generated at 2022-06-13 22:34:56.221837
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('foo')
    assert {} == session['headers']
    request_headers = RequestHeadersDict(
        [
            ('content-length', '0'),
            ('accept', 'text/html'),
            ('host', 'localhost'),
            ('cookie', 'foo=bar')
        ]
    )
    session.update_headers(request_headers)
    print('Sesion: ' + str(session['headers']))
    assert {'Accept': 'text/html', 'Host': 'localhost'} == session['headers']
    assert {'foo': {'value': 'bar'}} == session['cookies']



# Generated at 2022-06-13 22:34:58.571195
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))


# Generated at 2022-06-13 22:35:04.611202
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session(path=Path("path"))
    s.update_headers(RequestHeadersDict({'Content-Type': 'application/json', 'Cookie': 'a=1'}))
    assert "Content-Type" not in s["headers"].keys()
    assert "Cookie" not in s["headers"].keys()
    assert "a" in s["cookies"].keys()

# Generated at 2022-06-13 22:35:11.533004
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    import json

    session = Session('/tmp/test.json')
    headers = {}

    session.update_headers(headers)
    assert 'headers' not in session

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    session['headers'] = {'Content-Type': 'application/json'}
    session.update_headers(headers)
    assert session['headers'] == {'Content-Type': 'application/json; charset=utf-8'}

    headers = {'Content-Type': None}
    session['headers'] = {'Content-Type': 'application/json'}
    session.update_headers(headers)
    assert 'Content-Type' not in session['headers']

    # update with new header
    headers = {'X-Test': 'test'}

# Generated at 2022-06-13 22:35:21.970275
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.plugins.builtin import UnixSocketAuthPlugin
    from httpie.output.formatters.colors import NO_COLOR
    from httpie.context import Environment

    file_path = DEFAULT_CONFIG_DIR / SESSIONS_DIR_NAME / 'localhost' / 'test.json'
    session = Session(file_path)
    env = Environment(colors=NO_COLOR)


# Generated at 2022-06-13 22:35:30.784332
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = Session({'headers': {}})
    headers.update_headers(RequestHeadersDict({'foo': 'bar'}))
    assert headers['headers'] == {'foo': 'bar'}
    headers.update_headers(RequestHeadersDict({'foo': 'baz'}))
    assert headers['headers'] == {'foo': 'baz'}
    headers.update_headers(RequestHeadersDict({'foo': None}))
    assert headers['headers'] == {}

# Generated at 2022-06-13 22:35:40.983590
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import RequestDict

    raw_headers = {}
    raw_headers[b'Content-Type'] = b'application/json'
    raw_headers[b'If-None-Match'] = b'"747097696a7c"'
    raw_headers[b'Host'] = b'example.com'
    raw_headers[b'Accept-Encoding'] = b'gzip, deflate'
    raw_headers[b'Accept'] = b'text/html'
    raw_headers[b'User-Agent'] = b'HTTPie/0.9.9'
    raw_headers[b'Connection'] = b'keep-alive'

# Generated at 2022-06-13 22:35:43.783142
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path='path')
    request_headers = RequestHeadersDict()
    session.update_headers(request_headers)

# Generated at 2022-06-13 22:35:53.866586
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.cli.dicts import RequestHeadersDict

    session = Session(path='test')
    headers = RequestHeadersDict({'Host': 'test.com'})
    session.update_headers(headers)
    assert session.headers == headers
    assert session['cookies'] == {}

    headers = RequestHeadersDict({'Host': 'test.com', 'Cookie': 'test=1'})
    session.update_headers(headers)
    assert session.headers == RequestHeadersDict({'Host': 'test.com'})
    assert session['cookies'] == {'test': {'value': '1'}}

    headers = RequestHeadersDict({'Host': 'test.com', 'Cookie': 'test=1'})
    session.update_headers(headers)
    assert session.headers == Request

# Generated at 2022-06-13 22:36:09.290445
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    test_session = Session('path')
    # original_headers is a copy of the session that is used in the update_headers method
    original_headers = test_session.headers
    # request_headers are the headers that are being passed to the update_headers method
    request_headers = RequestHeadersDict()
    request_headers['Cookie'] = 'name1=value1'
    request_headers['Cookie'] = 'name2=value2'
    request_headers['If-Match'] = '"1234"'
    request_headers['Content-Type'] = 'application/json'
    # test_session has a header that is not in the request_headers
    test_session['headers']['Content-Length'] = '4321'
    test_session.update_headers(request_headers)
    # updated_headers is the result of the

# Generated at 2022-06-13 22:36:17.177726
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='test_delete')
    session.update({'cookies': {'cookie1': 'val1', 'cookie2': 'val2'}})
    assert 'cookie1' in session['cookies']
    assert 'cookie2' in session['cookies']

    session.remove_cookies({'cookie2'})

    assert 'cookie1' in session['cookies']
    assert 'cookie2' not in session['cookies']

# Generated at 2022-06-13 22:36:20.555197
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('path')
    test_session['cookies'] = {'a': 'b'}
    test_session.remove_cookies(['a'])
    assert not test_session['cookies']

# Generated at 2022-06-13 22:36:26.529371
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('some/path')
    session['cookies'] = {
        'cookie1': {},
        'cookie2': {},
        'cookie3': {}
    }

    session.remove_cookies(['cookie1', 'cookie3'])
    assert session['cookies'] == {'cookie2': {}}

# Generated at 2022-06-13 22:36:35.516198
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('.httpie/sessions/test.json')
    session['cookies'] = {'name1': {'value': 'value1'}, 'name2': {'value': 'value2'}, 'name3': {'value': 'value3'}}
    session.remove_cookies(['name2', 'name3'])
    session_cookies = session.get('cookies')
    if(session_cookies['name1'] == {'value': 'value1'} and
        'name2' not in session_cookies and
        'name3' not in session_cookies):
        print('Unit test for method remove_cookies of class Session succeed!')
    else:
        print('Unit test for method remove_cookies of class Session failed!')


# Generated at 2022-06-13 22:36:45.174681
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers_dict = RequestHeadersDict()
    request_headers_dict['Content-Type'] = 'text/html'
    request_headers_dict['Accept'] = '*'
    request_headers_dict.append('Accept-Language', 'zh-CN')
    request_headers_dict['Accept-Encoding'] = 'gzip'
    request_headers_dict['If-None-Match'] = '"1"'
    session = Session(path=Path('/tmp/test'))
    session.update_headers(request_headers_dict)
    expected_session_headers = {'Accept': '*', 'Accept-Language': 'zh-CN'}
    assert session['headers'] == expected_session_headers

# Generated at 2022-06-13 22:36:51.812119
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('testSession')
    session['cookies'] = {'cookie1': {'value': 'value1'},
                          'cookie2': {'value': 'value2'},
                          'cookie3': {'value': 'value3'}}
    session.remove_cookies(['cookie1', 'cookie2'])
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' not in session['cookies']
    assert 'cookie3' in session['cookies']



# Generated at 2022-06-13 22:36:59.763061
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    print("Test Session_update_headers starts")
    s = Session("test")
    assert (s.update_headers({"test":"test"}) == None)
    s['headers'] = {"a":"a"}
    assert (s.update_headers({"b":"b"}) == None)
    assert (s.update_headers({"c":"c"}) == None)
    assert (s['headers'] == {"a":"a","c":"c"})

    s['headers'] = {}
    for prefix in SESSION_IGNORED_HEADER_PREFIXES:
        print("Testing prefix:", prefix)
        name = prefix + "temp"
        s.update_headers({name:"temp"})
        assert (s['headers'] == {})
    print("Test Session_update_headers ends\n")


# Generated at 2022-06-13 22:37:02.936418
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path(''))
    session['cookies'] = dict(un=1, deux=2, trois=3)
    session.remove_cookies(['deux', 'trois'])
    assert session['cookies'] == dict(un=1)

# Generated at 2022-06-13 22:37:09.866971
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s.update_headers({'cookie': 'cookie1=val1; cookie2=val2'})

    assert 'cookie1' in s['cookies'].keys()
    assert 'cookie2' in s['cookies'].keys()
    s.remove_cookies(('cookie1',))
    assert 'cookie1' not in s['cookies'].keys()
    assert 'cookie2' in s['cookies'].keys()

# Generated at 2022-06-13 22:37:23.502112
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    assert 1 == (1+1)

# Generated at 2022-06-13 22:37:27.709732
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path('./'))
    cookies = {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    session.cookies = cookies
    for c in session.cookies:
        print(c)
    session.remove_cookies(['c1'])
    cookies = session.cookies
    for c in cookies:
        print(c)

#test_Session_remove_cookies()

# Generated at 2022-06-13 22:37:37.512827
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    class Temp():
        def __init__(self):
            self['cookies'] = {}
            self['cookies']['a'] = {'value': '1'}
            self['cookies']['b'] = {'value': '2'}
            self['cookies']['c'] = {'value': '3'}

    a = Temp()
    a.remove_cookies(['a', 'd'])
    assert len(a['cookies']) == 2 and 'a' not in a['cookies'] and 'b' in a['cookies'] and 'c' in a['cookies']

# Generated at 2022-06-13 22:37:44.993822
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    import os
    import shutil
    import tempfile
    import unittest
    session_name = "test_Session_remove_cookies"
    path = '/tmp/sessions/localhost/' + session_name + '.json'

    config_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(config_dir, "sessions", "localhost"))
    session = Session(path)

    session['cookies']['c1'] = {'value': 'v1'}
    session['cookies']['c2'] = {'value': 'v2'}

    session.remove_cookies(['c1'])
    session.save()

    loaded_session = Session(path)
    loaded_session.load()


# Generated at 2022-06-13 22:37:54.741618
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict([
        ('Host', 'example.com'),
        ('User-Agent', 'HTTPie/1.0.2'),
        ('Accept-Encoding', 'gzip, deflate'),
        ('Connection', 'keep-alive'),
        ('Accept', '*/*'),
        ('Content-Length', '18'),
        ('Content-Type', 'application/x-www-form-urlencoded'),
        ('If-Modified-Since', 'Mon, 27 Jul 2009 01:15:26 GMT'),
        ('Cookie', 'name=value; name_two=value_two'),
    ])
    session = Session('/tmp/foo')
    session.update_headers(headers)
    assert len(session['headers']) == 5
    assert 'Host' in session['headers']

# Generated at 2022-06-13 22:38:00.834273
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("./test")
    session['cookies'] = {
        'cookie1': {
            "value": "value1",
            "path": "/",
            "secure": False,
            "expires": None,
        },
        'cookie2': {
            "value": "value2",
            "path": "/",
            "secure": False,
            "expires": None,
        }
    }
    session.remove_cookies(["cookie1"])
    assert session['cookies'] == {
        'cookie2': {
            "value": "value2",
            "path": "/",
            "secure": False,
            "expires": None,
        }
    }


# Generated at 2022-06-13 22:38:07.298248
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('foo.json')
    session['cookies'] = {
        'foo': {'value': 'foo'},
        'bar': {'value': 'bar'}
    }
    session.remove_cookies(['bar'])
    assert session['cookies']['foo']['value'] == 'foo'
    assert 'bar' not in session['cookies']

# Generated at 2022-06-13 22:38:12.764350
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = RequestHeadersDict({
        'Content-Type': 'application/json',
        'Host': 'localhost:5000',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'session=abcde'
    })
    session = Session('test.json')
    session.update_headers(request_headers)
    assert set(session['headers'].keys()) == {'Accept', 'Accept-Encoding', 'Host', 'Connection'}
    assert session['cookies'] == {
        'session': {
            'value': 'abcde'
        }
    }

# Generated at 2022-06-13 22:38:14.844953
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test_session.json')
    session.update_headers()



# Generated at 2022-06-13 22:38:21.013044
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    ses = Session('temp_session')
    ses['cookies'] = {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    ses.remove_cookies(['c1'])
    assert ses['cookies'] == {'c2': {'value': 'v2'}}

# Generated at 2022-06-13 22:38:39.210344
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(str(Path(__file__).parent / "session.json"))
    session.remove_cookies(["a"])
    assert ("a" not in session['cookies'])

# Generated at 2022-06-13 22:38:44.575290
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = DEFAULT_SESSIONS_DIR / 'test.json'
    session = Session(path)
    session.load()
    session['cookies']['a'] = {}
    session['cookies']['b'] = {}
    session.remove_cookies(['a', 'c'])
    assert set(session['cookies'].keys()) == {'b'}



# Generated at 2022-06-13 22:38:58.405243
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.context import Environment
    from httpie.cli import parse_items
    import json
    env = Environment()
    baseConfigDict = BaseConfigDict(path=path)
    baseConfigDict.load()
    env.config = baseConfigDict

    kwargs = parse_items(
        env.config_dir,
        ['--session=myrequests',
         '-H', 'Content-Type: application/json',
         '-H', 'testheader: testvalue',
         '--auth=testuser:testpass',
         '--session-read-only'
         ],
        env,
    )
    session = kwargs['session']

    session.remove_cookies(['notexists'])
    assert session.cookies == {}

    # Set a cookie
    headers = RequestHeaders

# Generated at 2022-06-13 22:39:01.398588
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {'key': 'value'}
    session.remove_cookies(['key'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:39:04.247917
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/example.json')
    session.load()
    names = ['192.168.1.1']
    session.remove_cookies(names)
    assert '192.168.1.1' not in session

# Generated at 2022-06-13 22:39:09.714585
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session['cookies'] = {'test': '0', 'test1': '1'}
    session.remove_cookies(['test'])
    assert session['cookies'] == {'test1': '1'}
    session = Session('test.json')
    session.remove_cookies([])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:39:13.879842
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session("test_remove_cookies.json")
    test_session['cookies'] = {'token': '12345', 'authorization': '12345'}
    test_session.remove_cookies(names=('token',))
    assert 'token' not in test_session['cookies']
    assert 'authorization' in test_session['cookies']
    os.remove("test_remove_cookies.json")

# Generated at 2022-06-13 22:39:18.793682
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    c1 = create_cookie('name1', 'value1')
    c2 = create_cookie('name2', 'value2')
    jar = RequestsCookieJar()
    jar.set_cookie(c1)
    jar.set_cookie(c2)

    session = Session('./test_session')
    session.cookies = jar
    session.remove_cookies(['name1'])
    assert session.cookies.get_dict() == {'name2': 'value2'}

# Generated at 2022-06-13 22:39:29.763101
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    from httpie.clierror import ExitStatus
    from httpie.context import Environment
    from httpie.session import Session
    from pytest import raises
    from tempfile import mkdtemp
    from unittest import mock

    conf_dir = Path(mkdtemp())
    session = Session(conf_dir / 'test.json')
    env = Environment(config_dir=conf_dir)

    with mock.patch('httpie.context.Environment', return_value=env):
        with raises(SystemExit) as excinfo:
            # Two arguments provided, not allowed
            session.remove_cookies(['cookie', 'cookie2'])
        assert excinfo.value.code == ExitStatus.ERROR
        with raises(SystemExit) as excinfo:
            # No cookie provided
            session.remove_cookies([])


# Generated at 2022-06-13 22:39:33.504826
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/fake/path')

    # remove_cookies should not fail even if 'cookies' is not set or is None
    assert session.remove_cookies(['foo']) is None

    session['cookies'] = {}
    assert session.remove_cookies(['foo']) is None

    session['cookies'] = {'foo': 'bar', 'baz': 'quux'}
    assert session.remove_cookies(['foo']) is None
    assert session.remove_cookies(['foo', 'baz']) is None
    assert session['cookies']=={}


# Generated at 2022-06-13 22:40:03.906982
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_remove_cookies.json')
    session.update_headers(RequestHeadersDict({"Cookie": "test1=1; test2=2; test3=3"}))
    session.remove_cookies(['test1', 'test3'])
    assert len(session.cookies) == 1
    assert "test1=1" not in session.cookies
    assert "test2=2" in session.cookies
    assert "test3=3" not in session.cookies
    session.save()

# Generated at 2022-06-13 22:40:15.750890
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('./json')
    cookie1 = {
        "version": 0,
        "name": "foo",
        "value": "bar",
        "port": None,
        "domain": "httpbin.org",
        "path": "/",
        "secure": False,
        "expires": None,
        "discard": True,
        "comment": None,
        "comment_url": None,
        "rest": {"HttpOnly": None},
        "rfc2109": False,
    }

# Generated at 2022-06-13 22:40:20.889861
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies']['cookie1'] = 'cookie1'
    s['cookies']['cookie2'] = 'cookie2'
    s['cookies']['cookie3'] = 'cookie3'
    s.remove_cookies(['cookie2'])
    assert set(s['cookies'].keys()) == set(['cookie1', 'cookie3'])

# Generated at 2022-06-13 22:40:25.608299
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = os.path.expanduser('~/.config/httpie/sessions/dummy.json')
    session = Session(path)
    session.load()
    session.remove_cookies(['a'])
    session.save()

# Generated at 2022-06-13 22:40:30.141229
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('./')
    session['cookies'] = {'foo': {'value': 'bar'}, 'bar': {'value': 'baz'}}
    session.remove_cookies(['foo'])
    assert session['cookies'] == {'bar': {'value': 'baz'}}

# Generated at 2022-06-13 22:40:35.368576
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    s['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'qux'}
    }
    s.remove_cookies({'foo'})
    assert s['cookies'] == {'baz': {'value': 'qux'}}



# Generated at 2022-06-13 22:40:45.409924
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='test')
    session.update({'cookies': {'test': {'value': 'something'}}})
    session.remove_cookies(['test'])
    assert session.get('cookies') == {}
    session.update({'cookies': {'test': {'value': 'something'}}})
    session.remove_cookies(['nothere'])
    assert session.get('cookies') == {'test': {'value': 'something'}}
    session.update({'cookies': {'test': {'value': 'something'}}})
    session.remove_cookies(['nothere', 'test'])
    assert session.get('cookies') == {}
    session.update({'cookies': {'test': {'value': 'something'}}})
    session.remove_cook

# Generated at 2022-06-13 22:40:52.408581
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'session': {'name': 'session', 'value': '1234567890'}}
    session = Session('/foo/bar')
    session.load()
    session['cookies'] = cookies
    session.remove_cookies(['session'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:40:55.715505
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session.txt')
    session.update({'cookies': {'a': 1, 'b': 2, 'c': 3}})
    session.remove_cookies(['b', 'c'])
    assert session['cookies'] == {'a': 1}

# Generated at 2022-06-13 22:41:06.011718
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    import sys
    import os
    sys.path.append(os.path.abspath('..'))
    from httpie.config import DEFAULT_SESSIONS_DIR
    from httpie.session import Session
    from copy import deepcopy
    
    session_name = 'test_Session_remove_cookies'
    

# Generated at 2022-06-13 22:41:35.976267
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    request_headers = {}
    session_headers = {}
    session = Session('')
    session.update_headers(request_headers)
    assert session['headers'] == session_headers

    request_headers = {'something': 'header'}
    session_headers = {'something': 'header'}
    session = Session('')
    session.update_headers(request_headers)
    assert session['headers'] == session_headers

    request_headers = {'Cookie': 'somethin=somethingsomething',
                       'Content-Type': 'text/css'}
    session_headers = {'cookies': {'somethin': {'value': 'somethingsomething'}}}
    session = Session('')
    session.update_headers(request_headers)
    assert session['headers'] == session_headers



# Generated at 2022-06-13 22:41:36.624964
# Unit test for constructor of class Session
def test_Session():
    pass

# Generated at 2022-06-13 22:41:43.121982
# Unit test for constructor of class Session
def test_Session():
    s = Session("./test/httpie/sessions/httpbin/s1.json")
    assert s.cookies == {}
    assert s.path == Path("./test/httpie/sessions/httpbin/s1.json")
    assert s.about == "HTTPie session file"
    assert s.helpurl == "https://httpie.org/doc#sessions"

# Generated at 2022-06-13 22:41:44.304586
# Unit test for constructor of class Session
def test_Session():
    assert type(Session('test_Session')) == Session

# Generated at 2022-06-13 22:41:56.213147
# Unit test for constructor of class Session
def test_Session():
    import httpie
    import os
    import re
    import urllib
    config_dir=Path(httpie.__file__).parent.parent.parent / '.config' / 'httpie'
    session_name = 'test'
    host = None
    url = "http://httpbin.org/cookies/set?name=value"
    session = get_httpie_session(config_dir, session_name, host, url)
    assert re.match(VALID_SESSION_NAME_PATTERN, session_name)
    for prefix in SESSION_IGNORED_HEADER_PREFIXES:
        assert session['headers'].keys()[0].lower().startswith(prefix.lower())
    assert 'Content-Length' in session['headers'].keys()

# Generated at 2022-06-13 22:42:05.920896
# Unit test for function get_httpie_session
def test_get_httpie_session():
    config_dir = ''
    url = ''
    #host = ''
    session_name = 'hello'
    session = get_httpie_session(config_dir, session_name, 2,url)
    assert session.headers == {}
    assert session.auth == {}

    session.update_headers(test_headers)
    assert session.headers == test_headers



# Generated at 2022-06-13 22:42:09.090119
# Unit test for constructor of class Session
def test_Session():
    s = Session('filepath')
    assert s['headers'] == {}
    assert s['cookies'] == {}
    assert s['auth']['type'] == None
    assert s['auth']['username'] == None
    assert s['auth']['password'] == None
    assert s.helpurl == 'https://httpie.org/doc#sessions'
    assert s.about == 'HTTPie session file'


# Generated at 2022-06-13 22:42:21.368387
# Unit test for function get_httpie_session
def test_get_httpie_session():

    # Test 1: session name is not a directory
    test_config_dir = Path("/testing/configuration/directory")
    session_name = "test_session"
    test_session = get_httpie_session(test_config_dir, session_name, "", "")
    assert str(test_session.path) == "/testing/configuration/directory/sessions/test_session.json"

    # Test 2: session name is a directory
    test_config_dir = Path("/testing/configuration/directory")
    session_name = "/testing/configuration/directory/sessions/test_session"
    test_session = get_httpie_session(test_config_dir, session_name, "", "")

# Generated at 2022-06-13 22:42:28.175157
# Unit test for constructor of class Session
def test_Session():
    s = Session('path')
    assert s.helpurl == 'https://httpie.org/doc#sessions'
    assert s.about == 'HTTPie session file'
    assert s.path == 'path'
    assert s['headers'] == {}
    assert s['cookies'] == {}
    assert s['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }


# Generated at 2022-06-13 22:42:29.741015
# Unit test for function get_httpie_session
def test_get_httpie_session():
    assert get_httpie_session('test', 'https://www.baidu.com')
