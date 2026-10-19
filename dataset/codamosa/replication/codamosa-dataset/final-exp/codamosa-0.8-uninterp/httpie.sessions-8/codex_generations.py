

# Generated at 2022-06-13 22:33:30.166279
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('session.json')
    # 将 RequestHeadersDict.items()转换为list

# Generated at 2022-06-13 22:33:42.937596
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(str(DEFAULT_CONFIG_DIR))

    request_headers = {'User-Agent': 'HTTPie/1.0',
                       'Content-Type': 'application/json'}
    session.update_headers(request_headers)

    assert 'Content-Type' not in session['headers']
    assert 'User-Agent' not in session['headers']

    request_headers = {'User-Agent': 'HTTPie/1.0',
                       'Cookie': 'key1=value1;key2=value2'}
    session.update_headers(request_headers)

    assert 'key1' in session['cookies']
    assert 'value1' == session['cookies']['key1']['value']
    assert 'key2' in session['cookies']

# Generated at 2022-06-13 22:33:51.747017
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.headers import CONTENT_TYPE_HEADER
    from httpie.input import ParseError

    session = Session('/tmp/test.json')
    session.update_headers({'Accept': '*/*'})
    assert 'Accept' in session.headers.keys()
    session.update_headers({'accept': 'application/json'})
    assert 'Accept' in session.headers.keys()
    assert session.headers['Accept'] == 'application/json'
    session.update_headers({'Accept-Encoding': 'gzip, deflate'})
    assert 'Accept-Encoding' in session.headers.keys()

    # Check if explicit unset headers are ignored.
    session.update_headers({'Accept-Encoding': None})
    assert 'Accept-Encoding' in session.headers.keys()

    # Check if

# Generated at 2022-06-13 22:34:00.423721
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    class RequestHeadersDictMock(dict):
        def items(self):
            return [('header-test-key-1', 'header-test-value-1')]

    headers = RequestHeadersDictMock()
    session = Session('test.json')
    session.update_headers(headers)
    assert session['headers'] == {'header-test-key-1': 'header-test-value-1'}

# Generated at 2022-06-13 22:34:05.364588
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('http://httpbin.org/put')
    s.update_headers(RequestHeadersDict({'Content-Type': 'application/json'}))
    assert s['headers'] == {'Content-Type': 'application/json'}



# Generated at 2022-06-13 22:34:11.698199
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("Session")
    request_headers1 = {}
    request_headers1["Cookie"] = ""
    request_headers1["Cookie"] = "foo=bar"
    request_headers1["If-Match"] = ""
    request_headers1["Content-Type"] = ""
    assert session.update_headers(request_headers1) == None

# Generated at 2022-06-13 22:34:17.772182
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'test_cookie': {'value': 'cookie_value', 'path': 'cookie_path'}}
    assert 'test_cookie' in session['cookies']
    session.remove_cookies(['test_cookie'])
    assert 'test_cookie' not in session['cookies']

# Generated at 2022-06-13 22:34:28.924332
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_store = Session('path')
    jar = RequestsCookieJar()
    cookie_store['cookies']['session1'] = {'value': 'value1'}
    cookie_store['cookies']['session2'] = {'value': 'value2'}
    cookie_store['cookies']['session3'] = {'value': 'value3'}
    cookie_store['cookies']['session4'] = {'value': 'value4'}
    cookie_store.remove_cookies(['session2', 'session4'])
    assert len(cookie_store['cookies']) == 2

    cookie_store.remove_cookies(['session1'])
    assert len(cookie_store['cookies']) == 1
    assert 'session3' in cookie_store['cookies']

# Generated at 2022-06-13 22:34:39.872355
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import tempfile
    session_path = Path(tempfile.mkdtemp())
    session_name = 'test'
    session_path = session_path / session_name
    session_path.mkdir(parents=True)
    session = Session(session_path / '{}.json'.format(session_name))
    session['cookies'] = {'a': '1', 'b': '2', 'c': '3'}
    names = ['a', 'b']
    session.remove_cookies(names)
    assert len(session['cookies']) == 1
    session['cookies'] = {'a': '1', 'b': '2', 'c': '3'}
    names = ['a', 'b', 'c']
    session.remove_cookies(names)
    assert not session['cookies']


# Generated at 2022-06-13 22:34:49.146944
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from collections import OrderedDict

    # pylint: disable=redefined-outer-name, unused-argument
    def run(context, config, args):
        session = Session(os.path.join(config.dir, 'session'))
        session.update_headers({
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Content-Type': 'text/plain'
        })

        assert session.headers == OrderedDict([
            ('Accept', '*/*'),
            ('Accept-Encoding', 'gzip, deflate'),
            ('Content-Type', 'text/plain')
        ])

    # pylint: enable=redefined-outer-name, unused-argument

# Generated at 2022-06-13 22:35:08.850982
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path=Path('path'))
    session.update_headers({'Content-Type': 'application/json'})
    assert dict(session.headers) == {}
    session.update_headers({'User-Agent': 'HTTPie/1.0.2'})
    assert dict(session.headers) == {}
    session.update_headers({'Cookie': 'foo=bar'})
    assert dict(session.headers) == {}
    session.update_headers({'Accept-Encoding': 'gzip, deflate'})
    assert dict(session.headers) == {'Accept-Encoding': 'gzip, deflate'}
    # Test that headers case is preserved
    session.update_headers({'Accept-Encoding': 'gzip'})

# Generated at 2022-06-13 22:35:20.849197
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/test.json')
    session.update_headers({ 'User-Agent': 'test',
                             'Host': 'test.org' })
    assert(session['headers']['User-Agent'] == 'test')
    assert(session['headers']['Host'] == 'test.org')
    session.update_headers({ 'User-Agent': 'test',
                             'Host': 'test.org' })
    assert(session['headers']['User-Agent'] == 'test')
    assert(session['headers']['Host'] == 'test.org')
    session.update_headers({ 'User-Agent': 'test',
                             'Host': 'test.org',
                             'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT' })

# Generated at 2022-06-13 22:35:25.483226
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("/tmp/test/session.json")
    session.update_headers("Test-Header:Test-Value")
    assert session["headers"] == { 'Test-Header': 'Test-Value' }

# Generated at 2022-06-13 22:35:39.641795
# Unit test for method update_headers of class Session

# Generated at 2022-06-13 22:35:47.163905
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = {
        'SESSIONID': '123',
        'X-Cache': '123',
        'Content-Type': 'text/html',
        'If-Modified-Since': '0',
        'Cookie': 'name=value'
    }
    session = Session('./')
    session.update_headers(headers)
    assert session['headers'] == {'SESSIONID': '123', 'X-Cache': '123'}
    assert session['cookies'] == {'name': {'value': 'value'}}

# Generated at 2022-06-13 22:35:53.953477
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('./test_session.json')
    for c in ['c1', 'c2']:
        session['cookies'][c] = {'value': 'test'}
    session.remove_cookies(['c1', 'c3'])
    assert 'c1' not in session['cookies']
    assert 'c2' in session['cookies']

# Generated at 2022-06-13 22:36:02.466361
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('./test.json')
    session['headers'] = {'user-agent': 'test', 'connect-type': 'test'}
    request_headers = {'user-agent': 'test2','connect-type': 'test2', 'cookie': 'test3'}
    session.update_headers(request_headers)
    assert session['headers'] == {'user-agent': 'test', 'connect-type': 'test2'}
    assert session['cookies'] == {'test3': {'value': 'test3'}}

# Generated at 2022-06-13 22:36:17.383892
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session1 = Session("Session1")
    header1 = {'Accept-Encoding': 'gzip, deflate',
               'Cookie': 'something=the-value'}
    session1.update_headers(header1)
    assert session1["headers"] == {'Accept-Encoding': 'gzip, deflate'}  # Cookie not in headers
    assert session1.headers == RequestHeadersDict({'Accept-Encoding': 'gzip, deflate'})  # Cookie not in headers
    assert session1.cookies == RequestsCookieJar()  # No cookies
    assert session1.cookies.items() == []  # No cookies
    assert session1['cookies'] == {}  # No cookies


# Generated at 2022-06-13 22:36:27.378667
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.config import Config
    from httpie.plugins.auth.httpie_auth import HttpieAuthPlugin
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.registry import plugin_manager
    plugin_manager.register(HttpieAuthPlugin())
    # Create a config
    config = Config()
    # Create a session
    path = config.config_dir / SESSIONS_DIR_NAME
    path.mkdir(exist_ok=True, parents=True)
    session = Session(path / 'test.json')
    session.load()
    # Set headers and auth
    session.update_headers({'h1': 'v1', 'h2': 'v2'})
    session.auth = {'type': 'basic', 'raw_auth': 'u:p'}
    #

# Generated at 2022-06-13 22:36:31.138153
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_Session_remove_cookies')
    session['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    session.remove_cookies(['a', 'c'])
    assert session['cookies'] == {'b': 2}

# Generated at 2022-06-13 22:36:45.893175
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.plugins.registry import plugin_manager
    import httpie.cli.argtypes

    def remove_cookie_from_rep(rep, name):
        cookies = rep.cookies.get_dict()
        assert name in cookies
        cookies.pop(name)
        rep.cookies = cookies

    path = '/tmp/httpie_session'
    session = Session(path)
    session['headers'] = { 'test_header': 'test_value'}
    session['auth'] = { 'type': 'http-basic', 'username': 'test_user', 'password': 'test_password'}
    session['cookies'] = {'test_cookie': {'value' : 'test_value'}}
    session.save()

    plugin_manager.remove_plugin

# Generated at 2022-06-13 22:36:51.318606
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("session.json")
    session["cookies"] = {"name1": "value1", "name2": "value2"}
    assert session["cookies"] == {"name1": "value1", "name2": "value2"}
    session.remove_cookies(("name2",))
    assert session["cookies"] == {"name1": "value1"}

test_Session_remove_cookies()

# Generated at 2022-06-13 22:36:58.449738
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("session.json")
    session['headers'] = {'Content-Type': 'text/html',
                          'Content-Length': '2345'}
    session.update_headers({'Content-Type': 'application/json',
                            'Content-Length': '4523'})
    assert session['headers'] == {'Content-Type': 'application/json',
                                  'Content-Length': '4523'}

# Generated at 2022-06-13 22:37:07.611737
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.compat import OrderedDict
    from httpie.models.config import JSONDict
    session = Session('/foo/bar')
    session['headers'] = {'hello': 'world'}
    session['cookies'] = JSONDict(OrderedDict([('c1','v1')]))
    session.remove_cookies(['c1'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:12.952650
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from pathlib import Path
    from io import TextIOWrapper
    from typing import Iterable
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'test.json'
        with path.open('w') as f:
            f.write('{"cookies": {"name1": "value1", "name2": "value2"}}')
        session = Session(path)
        session.load()
        session.remove_cookies(('name1',))
        assert session.cookies.get_dict() == {'name2': 'value2'}, 'test_Session_remove_cookies - 1'

# Generated at 2022-06-13 22:37:18.683486
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # given
    session = Session('/tmp/session.json')
    session['cookies'] = {'foo': 'bar'}
    session['cookies']['foo'] = 'bar'

    # when
    session.remove_cookies(['foo'])

    # then
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:29.363029
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # Initialize a session
    session = Session(path='test.json')
    del session['headers']
    del session['cookies']
    session['headers'] = {}
    session['cookies'] = {}
    request_headers = RequestHeadersDict()

    # Assert that update_headers with empty headers does not fail
    session.update_headers(request_headers)

    # Assert that update_headers with 'Cookie' in headers adds the
    # cookie to the session cookies instead of the session headers.
    cookie_value = "a=b; c=d" 
    request_headers['Cookie'] = cookie_value
    session.update_headers(request_headers)
    assert session['cookies'] == {'a': {'value': 'b'}, 'c': {'value': 'd'}}

# Generated at 2022-06-13 22:37:33.766104
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(Path('session.json'))
    assert s.remove_cookies(['key', 'value']) is None
    assert s.remove_cookies(['foo', 'bar']) is None

# Generated at 2022-06-13 22:37:37.218717
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    session = Session('test_Session_remove_cookies')
    session['cookies'] = {'cookie_name': None}
    session.remove_cookies(['cookie_name'])
    assert 'cookies' not in session



# Generated at 2022-06-13 22:37:43.583041
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    from httpie.input import ParseResult

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'If-Match': '*',
    }
    parsed = ParseResult(
        method='GET',
        url='http://example.com',
        headers=headers,
        data=b''
    )
    session = Session(path='')
    session.update_headers(parsed.headers)
    assert session.headers == {
        'Accept': 'application/json',
        'If-Match': '*'
    }

# Generated at 2022-06-13 22:37:53.710989
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/foo/bar.json')
    s['cookies'] = {'foo': 'bar'}
    s.remove_cookies(['foo'])
    assert s['cookies'] == {}



# Generated at 2022-06-13 22:37:55.477677
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    jar = RequestsCookieJar()
    for cookie in jar:
        print(cookie.name)



# Generated at 2022-06-13 22:37:58.355813
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_session.json')
    session['cookies'] = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'qux'},
    }
    session.remove_cookies(['foo'])
    assert session['cookies'] == {'baz': {'value': 'qux'}}



# Generated at 2022-06-13 22:38:10.952326
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path='')
    session.update_headers(request_headers = {})
    assert session['headers'] == {}
    session.update_headers(request_headers = {'one': 1})
    assert session['headers'] == {}
    session.update_headers(request_headers = {'content-type': 'text'})
    assert session['headers'] == {}
    session.update_headers(request_headers = {'Cookie': 'one=1'})
    assert session['headers'] == {}
    session.update_headers(request_headers = {'user-agent': 'HTTPie/1'})
    assert session['headers'] == {}
    session.update_headers(request_headers = {'two': 2})
    assert session['headers'] == {'two': 2}

# Generated at 2022-06-13 22:38:16.931398
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/path/to/session.json')
    s['cookies'] = {"a": "1", "b": "2", "c": "3", "d": "4"}
    assert len(s['cookies']) == 4
    s.remove_cookies(["a", "d"])
    assert len(s['cookies']) == 2
    assert "a" not in s['cookies']
    assert "b" in s['cookies']
    assert "c" in s['cookies']
    assert "d" not in s['cookies']

# Generated at 2022-06-13 22:38:22.013770
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='')
    session.load()

    session['cookies'] = {'a': 'a', 'b': 'b', 'c': 'c'}
    session.remove_cookies(['b'])
    assert session['cookies'] == {'a': 'a', 'c': 'c'}

    session['cookies'] = {'a': 'a', 'b': 'b', 'c': 'c'}
    session.remove_cookies(['d'])
    assert session['cookies'] == {'a': 'a', 'b': 'b', 'c': 'c'}

    session['cookies'] = {'a': 'a', 'b': 'b', 'c': 'c'}
    session.remove_cookies(['b', 'c'])

# Generated at 2022-06-13 22:38:30.427069
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from hypothesis import given, settings, example
    from hypothesis.strategies import text, lists
    from httpie.compat import MutableMapping
    from httpie.session import Session
    from httpie.cli.argtypes import KeyValueArg, KeyValueArgType
    sessions_dir = DEFAULT_SESSIONS_DIR
    if not sessions_dir.exists():
        sessions_dir.mkdir(parents=True)
    session_path = sessions_dir / 'test.json'
    session = Session(path=session_path)
    if 'cookies' in session:
        del session['cookies']

# Generated at 2022-06-13 22:38:38.262483
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('/tmp/test.json')
    session.update_headers({'a': 'b', 'c': 'd'})
    assert session.headers == {'a': 'b', 'c': 'd'}
    session.update_headers({'a': 'b', 'c': 'd', 'Content-Type': 'gzip'})
    assert session.headers == {'a': 'b', 'c': 'd'}
    # Invalid headers (not str) should be ignored.
    session.update_headers({'e': 'f', 'g': b'\x01\x02'})
    assert session.headers == {'a': 'b', 'c': 'd', 'e': 'f'}
    # Empty values (None) should be ignored.

# Generated at 2022-06-13 22:38:44.244676
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    Test remove_cookies method.
    """
    session = Session(path="/tmp/httpie-test-session.json")
    names = ['httpbin', 'foo']
    for name in names:
        session['cookies'][name] = {'value':'bar'}

    session.remove_cookies(['httpbin', 'bar'])

    assert 'foo' in session['cookies']



# Generated at 2022-06-13 22:38:51.075795
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    """
    Test Session.update_headers()
    """
    import json
    path = '~/.config/httpie/sessions'
    session = Session(path)
    session.load()
    session.update_headers({'key': 'value'})
    print(json.dumps(session, indent=4))


# Generated at 2022-06-13 22:39:14.438723
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    config = Session(path = './test_session')
    # test for prefix: Content-
    request_headers = RequestHeadersDict({'Content-Type': "application/json"})
    config.update_headers(request_headers)
    assert config.get('headers', None) == {}
    # test for prefix: If-
    request_headers = RequestHeadersDict({
        'If-Modified-Since': "Wed, 29 Jul 2020 08:30:12 GMT",
        'If-Match': "match this"
    })
    config.update_headers(request_headers)
    assert config.get('headers', None) == {}
    # test for name: User-Agent
    request_headers = RequestHeadersDict({'User-Agent': "httpie/1.0.3"})

# Generated at 2022-06-13 22:39:20.042530
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    data = {
        'type': 'basic',
        'raw_auth': 'fake_type fake_username:fake_password',
        'username': None,
        'password': None
    }

    s = Session(path = '')
    s['cookies'] = {'fake1': data, 'fake12': data, 'fake123': data}
    s.remove_cookies(names = ['fake23', 'fake2'])
    assert s['cookies'] == {'fake1': data, 'fake12': data, 'fake123': data}
    s.remove_cookies(names = ['fake1', 'fake12'])
    assert s['cookies'] == {'fake123': data}

# Generated at 2022-06-13 22:39:25.087758
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    conf = Session('test')
    conf['cookies'] = {'one': {'value': 1}, 'two': {'value': 2}}

    conf.remove_cookies(['one'])
    assert conf['cookies'] == {'two': {'value': 2}}



# Generated at 2022-06-13 22:39:28.647611
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('session')
    original_session_headers = {'Content-Type': 'application/json'}
    session.update_headers(original_session_headers)
    assert session['headers'] == {'Content-Type': 'application/json'}



# Generated at 2022-06-13 22:39:34.315462
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='path')
    session['cookies'] = {'name1': 'cookie1', 'name2': 'cookie2'}
    session.remove_cookies(['name1'])
    assert session['cookies'] == {'name2': 'cookie2'}



# Generated at 2022-06-13 22:39:39.562197
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=None)
    session.cookies=RequestsCookieJar()
    session['cookies']['test1']={'value':'testvalue1'}
    session['cookies']['test2']={'value':'testvalue2'}
    session.remove_cookies(['test1'])
    assert session['cookies']['test1']==None
    assert session['cookies']['test2']!=None

# Generated at 2022-06-13 22:39:49.860216
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import tempfile
    tempdir = tempfile.TemporaryDirectory()
    sess = Session(tempdir.name+'/sessfile.json')
    sess['cookies'] = {'c1': {}, 'c2': {}, 'c3': {}}
    sess.remove_cookies(['c2', 'c4'])
    assert set(sess['cookies']) == {'c1', 'c3'}
    tempdir.cleanup()

# Generated at 2022-06-13 22:39:56.163013
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('C:\\Users\\Yiyang\\pycharmprojects\\httpie\\test.json')
    session['headers'] = {"Connection": "keep-alive"}
    print(session)
    request_headers = RequestHeadersDict({'Connection': 'close'})
    session.update_headers(request_headers)
    print(session)
    print(request_headers)


# Generated at 2022-06-13 22:40:02.914713
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session')
    session['cookies'] = {
        'cookie1': {
            'value': 'val1'
        },
        'cookie2': {
            'value': 'val2'
        }
    }

    names = {'cookie1', 'cookie3'}
    session.remove_cookies(names)
    assert set(session['cookies'].keys()) == {'cookie2'}

# Generated at 2022-06-13 22:40:08.054548
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.cli.dicts import RequestHeadersDict
    session = Session(Path('test'))
    session['cookies'] = {'name': {'value': 'value'}}
    assert 'name' in session['cookies']
    session.remove_cookies(['name'])
    assert 'name' not in session['cookies']

# Generated at 2022-06-13 22:40:43.572826
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_name = 'test'
    session = Session(None)
    session["cookies"] = {cookie_name: None}
    assert cookie_name in session['cookies']
    assert session['cookies'][cookie_name] == None

    session.remove_cookies(['test'])
    assert cookie_name not in session['cookies']

# Generated at 2022-06-13 22:40:47.244636
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path="path")
    assert not session['cookies']
    session['cookies']['cookie1'] = 'value1'
    session['cookies']['cookie2'] = 'value2'
    assert session['cookies'] == {'cookie1': 'value1', 'cookie2': 'value2'}
    session.remove_cookies(['cookie2'])
    assert session['cookies'] == {'cookie1': 'value1'}

# Generated at 2022-06-13 22:40:54.136840
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {
        'name1': {'value': 'val1'},
        'name2': {'value': 'val2'}
    }
    session.remove_cookies(['name1'])
    assert session['cookies'] == {
        'name2': {'value': 'val2'}
    }

# Generated at 2022-06-13 22:41:03.517405
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    import pickle
    config_dir= '/tmp/'
    session_name= 'test_session'
    url= 'http://www.google.com'
    session=get_httpie_session(config_dir, session_name, None, url)
    session['cookies']['a'] = 1
    session['cookies']['b'] = 2
    session['cookies']['c'] = 3
    session.remove_cookies(['a', 'b'])
    assert(session['cookies'] == {'c': 3})


# Generated at 2022-06-13 22:41:13.739330
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.config import Config
    from httpie.context import Environment
    from httpie.output.streams import NoopStream
    from httpie.plugins import AuthPlugin, AuthCookiePlugin
    from httpie.core import main as cli

    class DummyAuthAuthPlugin(AuthPlugin):
        auth_type = 'dummy-auth'
        auth_parse = False

        def get_auth(self, username=None, password=None):
            class DummyAuth:
                def __call__(self, r):
                    pass
            return DummyAuth()

    class DummyAuthCookiePlugin(AuthCookiePlugin):
        auth_type = 'dummy-auth-cookie'
        auth_parse = False


# Generated at 2022-06-13 22:41:19.977047
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.txt')
    session['cookies'] = {
        'name1': 'value1',
        'name2': 'value2',
        'name3': 'value3',
    }
    session.remove_cookies(['name1', 'name2'])
    assert session['cookies'] == {'name3': 'value3'}

# Generated at 2022-06-13 22:41:23.089616
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = {'cookies': {'s1':'s1', 's2':'s2'}}
    Session(s).remove_cookies({'s1','s2'})
    result = {"cookies":{}}
    print(s)
    assert s == result

# Generated at 2022-06-13 22:41:34.082362
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test_Session_remove_cookies.json')
    s['cookies']['name1'] = {
        'value': 'value1',
        'secure': True,
        'expires': 'Tue, 07-Aug-2018 13:53:04 GMT'
    }
    s['cookies']['name2'] = {
        'value': 'value2',
        'secure': False,
        'expires': 'Wed, 08-Aug-2018 13:53:04 GMT'
    }
    s.remove_cookies(['name1', 'name3'])
    assert 'name1' not in s['cookies']
    assert 'name2' in s['cookies']

# Generated at 2022-06-13 22:41:38.916796
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
	s = Session(path="sessions")
	s["cookies"] = {"cookie1":"value1", "cookie2":"value2"}
	s.remove_cookies(["cookie1"])
	assert s["cookies"] == {"cookie2":"value2"}
	return

if __name__ == '__main__':
    test_Session_remove_cookies()

# Generated at 2022-06-13 22:41:46.487603
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.plugins import AuthPlugin
    from httpie.auth.basic import BasicAuth
    session = Session(path=Path(''))
    session['auth'] = {'type': 'basic', 'username': 'foo', 'password': 'bar'}
    session['cookies'] = {'test': {'value': 'test'}}
    assert(session.auth.key == 'foo')
    assert(session.auth.value == 'bar')
    session.cookies = session.cookies
    assert(session['cookies']['test'] == {'value': 'test'})
    session.remove_cookies(['test'])
    assert(session['cookies'] == {})

# Generated at 2022-06-13 22:43:06.999754
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {}
    s = Session("./test")
    s['cookies'] = cookies
    assert s['cookies'] == cookies

    s.remove_cookies(['test'])
    assert s['cookies'] == cookies

    cookies['test1'] = 'test'
    s['cookies'] = cookies
    assert s['cookies']['test1'] == 'test'

    s.remove_cookies(['test1'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:43:18.733414
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #Given
    cookie_dict = {'cookied': {'value': '0', 'path': '/', 'secure': True, 'expires': 0}}
    cookie_dict2 = {'cookied2': {'value': '0', 'path': '/', 'secure': True, 'expires': 0}}
    session = Session('.session')
    session['cookies'] = cookie_dict
    session['cookies'].update(cookie_dict2)
    #When
    session.remove_cookies(['cookied'])
    #Then
    assert session['cookies'] == {'cookied2': {'value': '0', 'path': '/', 'secure': True, 'expires': 0}}