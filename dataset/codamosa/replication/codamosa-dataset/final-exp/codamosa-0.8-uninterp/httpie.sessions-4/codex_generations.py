

# Generated at 2022-06-13 22:33:21.669765
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    s = Session('test_Session_update_headers')
    s.update_headers({'Accept':'text/html', 'User-agent':'test'})
    assert 'Accept' in s.headers
    assert 'User-agent' not in s.headers



# Generated at 2022-06-13 22:33:26.071766
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('')
    session.update_headers({'test' : 'test'})
    assert session.headers == {'test' : 'test'}
    session.update_headers({'test' : None})
    assert session.headers == {'test' : 'test'}



# Generated at 2022-06-13 22:33:26.998791
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    assert False, "not implemented"

# Generated at 2022-06-13 22:33:31.776864
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("./test_Session")
    c = {
        'foo': {'value': 'bar'},
        'baz': {'value': 'qux'},
    }
    s['cookies'] = c
    s.remove_cookies(['foo'])
    assert s['cookies'] == {'baz': {'value': 'qux'}}

# Generated at 2022-06-13 22:33:40.704828
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("")
    request_headers = RequestHeadersDict()
    request_headers.update({'Content-Type':'text/html','If-None-Match':'1234567'})
    request_headers.update({'Cookie':'name=value'})
    request_headers.update({'User-Agent':'HTTPie/0.9.9'})

    session.update_headers(request_headers)

    print (session.headers)
    print (session['cookies'])
    assert len(session['headers']) == 0
    assert len(session['cookies']) == 1

if __name__ == '__main__':
    test_Session_update_headers()

# Generated at 2022-06-13 22:33:46.370535
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'cookie1': 'value1', 'cookie2': 'value2', 'cookie3': 'value3'}
    session = Session('test_session')
    session['cookies'] = cookies
    assert session['cookies'] == cookies

    names_to_remove = ['cookie1', 'cookie3']
    session.remove_cookies(names_to_remove)
    cookies.pop('cookie1')
    cookies.pop('cookie3')
    assert session['cookies'] == cookies

    session.remove_cookies([])
    assert session['cookies'] == cookies

    session.remove_cookies(['cookie4'])
    assert session['cookies'] == cookies

# Generated at 2022-06-13 22:33:57.618806
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    headers = RequestHeadersDict()
    session = Session('')
    session.update_headers(headers)
    assert session == {'auth': {'password': None, 'type': None, 'username': None}, 'cookies': {}, 'headers': {}}
    headers.update({'some': 'header'})
    session.update_headers(headers)
    assert session == {'auth': {'password': None, 'type': None, 'username': None}, 'cookies': {}, 'headers': {'some': 'header'}}


if __name__ == "__main__":
    test_Session_update_headers()

# Generated at 2022-06-13 22:34:05.810762
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    # given
    session = Session("foo")
    request_headers = {
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "If-Modified-Since": "Tue, 17 Apr 2018 15:08:31 GMT",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    # when
    session.update_headers(request_headers)
    # then

# Generated at 2022-06-13 22:34:16.122536
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session(path=Path('test'))
    request_headers = {
                "Name":"Gowrav",
                "Cookie":"abcd",
                "Content-Type":"Hello/world",
                "If-Modified-Since":"10Nov 2019",
                "Accept-language":"en-US"
                }
    session.update_headers(request_headers)
    assert request_headers == {"Name":"Gowrav","Accept-language":"en-US"}
    assert session['headers'] == {"Name":"Gowrav","Accept-language":"en-US"}
    assert session['cookies'] == {"abcd": {"value": "abcd"}}



# Generated at 2022-06-13 22:34:23.879665
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/test_Session_remove_cookies')
    session['cookies'] = {'cookie_name_1': 'cookie_value_1', 'cookie_name_2': 'cookie_value_2'}
    session.remove_cookies(['cookie_name_1', 'cookie_name_2'])
    session.save()
    assert not os.path.exists(session.path.as_posix())

# Generated at 2022-06-13 22:34:34.433314
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    myS = Session('myS')
    myS['cookies'] = {'foo': {}, 'bar': {}}
    myS.remove_cookies(['bar'])
    assert {'foo': {}} == myS['cookies']

# Generated at 2022-06-13 22:34:38.704640
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(""))
    session['cookies'] = {'key': 'value'}
    session.remove_cookies(['key'])
    assert 'key' not in session['cookies']

# Generated at 2022-06-13 22:34:45.202912
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('/path/to/session.json'))
    session['cookies'] = {'id': {'value': 1234}, 'name': {'value': 'xyz'}}
    session.remove_cookies(['name'])
    assert session['cookies'] == {'id': {'value': 1234}}

# Generated at 2022-06-13 22:34:53.962312
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test/test_session.json")
    session.cookies= {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    assert session.cookies == {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    session.remove_cookies(['c1'])
    assert session.cookies == {'c2': {'value': 'v2'}}

# Generated at 2022-06-13 22:34:54.932686
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    assert True

# Generated at 2022-06-13 22:35:02.378106
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path = 'path/to/session.json')
    session['cookies'] = {}
    session['cookies']['name1'] = {}
    session['cookies']['name2'] = {}
    session['cookies']['name3'] = {}
    session.remove_cookies(names = ['name1', 'name2'])
    assert session['cookies'] == {'name3': {}}

# Generated at 2022-06-13 22:35:14.046653
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session_remove_cookies')
    session['cookies'] = {'cook1': 1, 'cook2': 2, 'cook3': 3, 'cook4': 4}
    assert session.cookies == {'cook1': 1, 'cook2': 2, 'cook3':3, 'cook4': 4}
    session.remove_cookies(['cook2', 'cook3'])
    assert session.cookies == {'cook1': 1, 'cook4': 4}
    session.remove_cookies(['cook1', 'cook4'])
    assert session['cookies'] == {}
    assert session.cookies == {}

# Generated at 2022-06-13 22:35:20.583524
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test.json')
    cookies = {}
    cookies['a'] = {}
    cookies['b'] = {}
    cookies['c'] = {}
    session['cookies'] = cookies
    assert len(session['cookies']) == 3
    session.remove_cookies(['a', 'b'])
    assert len(session['cookies']) == 1
    assert 'c' in session['cookies']

# Generated at 2022-06-13 22:35:28.329058
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    test_session = Session('./test_session.json')
    test_session['cookies'] = {'test_cookies': {'value': 'test_value'}}

    assert 'test_cookies' in test_session['cookies']
    test_session.remove_cookies(['test_cookies'])

    assert 'test_cookies' not in test_session['cookies']

# Generated at 2022-06-13 22:35:40.409179
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('none')
    session['cookies']['name1'] = {'value': 'value1'}
    session['cookies']['name2'] = {'value': 'value2'}
    session['cookies']['name3'] = {'value': 'value3'}
    session.remove_cookies(['name1', 'name2'])
    assert session['cookies'] == {}
    session['cookies']['name1'] = {'value': 'value1'}
    session['cookies']['name2'] = {'value': 'value2'}
    session['cookies']['name3'] = {'value': 'value3'}
    session.remove_cookies(['name1', 'name2', 'name3'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:35:51.823493
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names = ['access_token', 'refresh_token']
    session = Session(path='/')
    session['cookies']['access_token'] = 'access token'
    session['cookies']['refresh_token'] = 'refresh token'
    session.remove_cookies(names)
    assert session['cookies'] == {}
    # TODO test when cookies dictionary is empty

# Generated at 2022-06-13 22:35:58.106410
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names = ['name1','name2','name2']
    s = Session('session.json')
    s['cookies'] = {'name1':{'value':'value1'}, 'name2':{'value':'value2'}}
    s.remove_cookies(names)
    assert s.cookies == RequestsCookieJar()

# Generated at 2022-06-13 22:36:03.445411
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('sessions')
    session['cookies'] = {"cookie_name": "cookie_value"}
    names = list(session['cookies'].keys())
    session.remove_cookies(names)
    assert len(session['cookies']) == 0

# Generated at 2022-06-13 22:36:17.682245
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.plugins.builtin import HTTPBasicAuth
    from httpie.compat import urlparse
    class FakeRequest:
        def __init__(self, url):
            self.url = urlparse(url)
            self.headers = {}

    A = Session('fake_path')
    headers = RequestHeadersDict({"h1":"v1","h2":"v2"})
    A.update_headers(RequestHeadersDict(headers))
    assert set(A.headers) == set(["h1","h2"])

    cookie_jar = RequestsCookieJar()
    cookie_jar.set("ck1","v1")
    cookie_jar.set("ck2","v2")
    A.cookies = cookie_jar

# Generated at 2022-06-13 22:36:21.669998
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test.json')
    s['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    s.remove_cookies(names=['b','d'])
    assert s['cookies'] == {'a': 1, 'c': 3}

# Generated at 2022-06-13 22:36:27.943417
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    """
    test remove_cookies

    """
    session = Session("test")
    session['cookies'] = {"name1":"value1", "name2":"value2"}
    names = ["name1","name3"]
    session.remove_cookies(names)
    assert session['cookies'] == {"name2":"value2"}

# Generated at 2022-06-13 22:36:36.322803
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test")
    session['cookies']['test'] = {}
    session['cookies']['example'] = {}
    session['cookies']['example.com'] = {}
    session.remove_cookies(['example', 'example.com', 'test'])
    assert not session['cookies']
    session['cookies']['test'] = {}
    session['cookies']['example'] = {}
    session['cookies']['example.com'] = {}
    session.remove_cookies(['example'])
    assert session['cookies'] == {'test': {}, 'example.com': {}}
    session['cookies']['test'] = {}
    session['cookies']['example'] = {}
    session['cookies']['example.com'] = {}

# Generated at 2022-06-13 22:36:40.705221
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'foo': 'bar', 'baz': 'qux'}
    session.remove_cookies(['baz'])
    assert session['cookies'] == {'foo': 'bar'}


# Generated at 2022-06-13 22:36:49.659133
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('path')
    s.cookies = RequestsCookieJar()
    s.cookies.set_cookie(create_cookie(
        'cookie1', 'value1', path='path1', secure=True, expires=12345))
    s.cookies.set_cookie(create_cookie(
        'cookie2', 'value2', path='path2', secure=False, expires=54321))
    assert s.headers == {}
    assert s['cookies'] == {'cookie1': {'value': 'value1', 'path': 'path1', 'secure': True, 'expires': 12345},
                            'cookie2': {'value': 'value2', 'path': 'path2', 'secure': False, 'expires': 54321}}
    assert s.cookies == RequestsCookieJar()

   

# Generated at 2022-06-13 22:37:00.522474
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('test_session')
    test_session['cookies'] = {
        'test1': {
            'value': 'test_1',
            'path': 'test_path_1',
            'secure': 'test_secure_1',
            'expires': 'test_expires_1'
        },
        'test2': {
            'value': 'test_2',
            'path': 'test_path_2',
            'secure': 'test_secure_2',
            'expires': 'test_expires_2'
        }
    }
    assert 'test1' in test_session['cookies']
    '''
    When we remove cookies that don't exist, it doesn't change anything
    '''
    test_session.remove_cookies(['test3'])

# Generated at 2022-06-13 22:37:19.430654
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie('testcookie1', 'gh'))
    jar.set_cookie(create_cookie('testcookie2', 'hg'))
    jar.set_cookie(create_cookie('testcookie3', 'hg'))

    s = Session('test_session')
    s.cookies = jar
    assert len(s['cookies']) == 3
    s.remove_cookies(['testcookie1', 'testcookie2'])
    assert len(s['cookies']) == 1

# Generated at 2022-06-13 22:37:25.581270
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/tmp/test_Session_remove_cookies')
    
    s['cookies'] = {'cookies_key_1': 'cookies_value_1', 'cookies_key_2': 'cookies_value_2'}
    s.remove_cookies(['cookies_key_1'])
    assert s['cookies'] == {'cookies_key_2': 'cookies_value_2'}

# Generated at 2022-06-13 22:37:38.181779
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session')
    # Add cookies
    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie('abc', 'value', path='/', secure=True, expires=300000000))
    jar.set_cookie(create_cookie('def', 'value', path='/', secure=True, expires=300000000))
    jar.set_cookie(create_cookie('ghi', 'value', path='/', secure=True, expires=300000000))
    session.cookies = jar
    # Delete 'def'
    names = ['def']
    session.remove_cookies(names)
    assert len(session['cookies']) == 2
    assert 'abc' in session['cookies']
    assert 'ghi' in session['cookies']
    assert 'def' not in session['cookies']

# Generated at 2022-06-13 22:37:43.583486
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    config_dir = DEFAULT_CONFIG_DIR
    session_name = "httpie"
    host = "github.com"
    url = "https://github.com/"
    
    session = get_httpie_session(config_dir, session_name, host, url)
    session['cookies'] = {'cookie1': {'value': 'val1'}, 'cookie2': {'value': 'val2'}}
    session.remove_cookies(['cookie1', 'cookie2'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:47.257952
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('.')
    session['cookies'] = {'cookie': {'value': 'test', 'domain': 'test.com'}}
    session.remove_cookies(['cookie'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:37:51.406988
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'ats': {'value': 'ats'}, 'ai': {'value': 'ai'}}

    session.remove_cookies(names=['ats'])
    assert session['cookies'] == {'ai': {'value': 'ai'}}



# Generated at 2022-06-13 22:37:59.589434
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    c=Session({})
    dict_test = {}
    dict_test['cookies'] = {'my_cookie1': {'value': 'my_value1'},
                            'my_cookie2': {'value': 'my_value2'},
                            'my_cookie3': {'value': 'my_value3'}}
    c.dict = dict_test

    c.remove_cookies(['my_cookie1'])
    assert len(c.dict) == 1
    assert len(c.dict['cookies']) == 2

    c.remove_cookies(['my_cookie2'])
    assert len(c.dict) == 1
    assert len(c.dict['cookies']) == 1

    c.remove_cookies(['my_cookie3'])
    assert len(c.dict)

# Generated at 2022-06-13 22:38:03.744563
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = '../sessions/'
    s = Session(path + 'session1')
    s.remove_cookies(['color'])
    assert 'color' not in s['cookies']

# Generated at 2022-06-13 22:38:07.894757
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names = ['one', 'two']
    session = Session(None)
    session['cookies'] = {'one': 'value'}

    session.remove_cookies(names)
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:38:12.998844
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.client.session import Session
    session = Session('/tmp/test_Session_remove_cookies.json')
    session['cookies'] = {'session': '123'}
    session.remove_cookies(['session'])
    assert 'session' not in session['cookies']

# Generated at 2022-06-13 22:38:41.016819
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    sess = Session(None)
    sess.load()
    sess.cookies = RequestsCookieJar()
    sess.cookies.set("name", "value")
    sess.cookies.set("name1", "value1")
    assert {"name": {}, "name1": {}} == sess.cookies.get_dict()
    sess.remove_cookies(["name"])
    assert {"name1": {}} == sess.cookies.get_dict()

# Generated at 2022-06-13 22:38:46.970588
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(os.path.join(DEFAULT_SESSIONS_DIR, 'test'))
    session['cookies'] = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
    }
    session.remove_cookies(['a', 'c', 'e'])
    if session['cookies'] == {'c': '', 'a': '', 'e': ''}:
        raise Exception("failed!")

# Generated at 2022-06-13 22:38:53.580447
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'cookie1': {'value': 'value1'},
                          'cookie2': {'value': 'value2'}}
    session.remove_cookies(names=['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value2'}}



# Generated at 2022-06-13 22:39:00.794515
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(os.devnull))
    cookies = [
        create_cookie('foo', '1'),
        create_cookie('bar', '2')
    ]
    jar = RequestsCookieJar()
    [jar.set_cookie(cookie) for cookie in cookies]
    session.cookies = jar

    session.remove_cookies(['foo'])
    cookies = dict(session.cookies)
    assert len(cookies) == 1
    assert 'bar' in cookies
    assert 'foo' not in cookies

# Generated at 2022-06-13 22:39:06.825799
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_Session_remove_cookies.json')
    session['cookies'] = {
        'cookie_name_1': {'value': 'cookie_value_1'},
        'cookie_name_2': {'value': 'cookie_value_2'},
        'cookie_name_3': {'value': 'cookie_value_3'},
    }

    session.remove_cookies(['cookie_name_1', 'cookie_name_3'])

    assert 'cookies' in session
    assert session['cookies'] == {'cookie_name_2': {'value': 'cookie_value_2'}}

# Generated at 2022-06-13 22:39:09.857225
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("~/test.json")
    s['cookies'] = {'asdf':'asdf'}
    s.remove_cookies('asdf')
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:39:16.417959
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_path = "test_session.json"
    session = Session(session_path)
    jar = RequestsCookieJar()

    # Remove non-existing cookie
    jar.clear_expired_cookies()
    session.cookies = jar
    session.remove_cookies(('non-existing',))
    assert session.cookies == jar

    # Remove non-existing cookie while other exists
    session.load()
    jar.set_cookie(create_cookie('existing', 'value'))
    session.cookies = jar
    session.remove_cookies(('non-existing',))
    assert session.cookies == jar

    # Remove existing cookie
    session.load()
    jar.set_cookie(create_cookie('existing', 'value'))
    session.cookies = jar

# Generated at 2022-06-13 22:39:28.750750
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    test_sess_path = '/tmp/test_sess.json'
    test_sess = Session(test_sess_path)
    test_sess['headers'] = {'Accept': 'text/html'}
    test_sess['cookies'] = {'JSESSIONID': {'value': '12345'}, 'weebly.com': {'value': '2.00', 'httponly': True}, 'expires': {'value': '2019-03-31'}}
    test_sess.save()
    with open(test_sess_path, 'r') as json_file:
        test_sess_json = json.load(json_file)
        assert test_sess_json['headers'] == {'Accept': 'text/html'}
        assert test_sess_

# Generated at 2022-06-13 22:39:34.354880
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('foo')
    session.cookies = RequestsCookieJar()
    assert not session.cookies
    session.cookies.set('foo', 'bar')
    assert session.cookies
    session.remove_cookies(['foo'])
    assert not session.cookies


# Generated at 2022-06-13 22:39:39.826088
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("/tmp/httpie.json")
    session['cookies'] = {'a': 1, 'b': 2, 'c': 3}
    session.remove_cookies(['b', 'c'])
    assert session['cookies'] == {'a': 1}
    session.remove_cookies([])
    assert session['cookies'] == {'a': 1}
    session.remove_cookies(['a', 'b'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:40:29.761942
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    config_dir = DEFAULT_CONFIG_DIR
    session_name = 'my_session'
    url = 'http://host.example.com/'
    session = get_httpie_session(config_dir, session_name, None, url)
    session['cookies'] = {'first': 1, 'second': 2, 'third': 3}
    jar = session.cookies
    assert jar._cookies[url].keys() == ['first', 'second', 'third']
    session.remove_cookies(['first', 'third'])
    jar = session.cookies
    assert jar._cookies[url].keys() == ['second']

# Generated at 2022-06-13 22:40:40.721380
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    p1 = Path("/tmp/test_Session_remove_cookies")
    s1 = Session(p1)
    assert s1['cookies'] == {}
    s1['cookies'] = {'abc' : {'value' : 'abc_value'}, 'cde' : {'value' : 'cde_value'}}
    assert s1['cookies'] == {'abc' : {'value' : 'abc_value'}, 'cde' : {'value' : 'cde_value'}}
    s1.remove_cookies([])
    assert s1['cookies'] == {'abc' : {'value' : 'abc_value'}, 'cde' : {'value' : 'cde_value'}}
    s1.remove_cookies(['abc'])

# Generated at 2022-06-13 22:40:43.731054
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path(""))
    session['cookies']['cookie_name'] = 'cookie_value'
    session.remove_cookies(['cookie_name'])
    assert('cookie_name' not in session.keys())

# Generated at 2022-06-13 22:40:46.089583
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='path')
    cookies = {'name1': 'value1', 'name2': 'value2'}
    session.cookies = cookies
    session.remove_cookies(['name2'])
    
    assert session.cookies.keys() == ['name1']

# Generated at 2022-06-13 22:40:53.310317
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'cookie1': {'value': '1'}, 'cookie2': {'value': '2'}}
    session.remove_cookies(['cookie1', 'cookie3'])
    assert session['cookies'] == {'cookie2': {'value': '2'}}

# Generated at 2022-06-13 22:41:05.286398
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.compat import is_windows
    from httpie.context import Environment
    from httpie.session import Session
    from httpie import ExitStatus
    from tests import http, HTTP_OK

    env = Environment()
    env.config['session.save'] = 'no'
    env.config['session.load'] = 'no'
    env.config.save()

    test_session1 = 'test-session1'

    r = http(
        '--session=' + test_session1,
        '--session-read-only=' + test_session1,
        '--follow',
        '--auth=username:password',
        'GET',
        HTTP_OK
    )
    r = http(
        '--session=' + test_session1,
        'GET',
        HTTP_OK
    )

# Generated at 2022-06-13 22:41:09.217782
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'test': {'value': 'test'}}
    session.remove_cookies(['test'])
    print(session['cookies'])

# Generated at 2022-06-13 22:41:21.887887
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session.cookies = RequestsCookieJar()
    session.cookies.set('c1', 'v1')
    session.cookies.set('c2', 'v2')
    session.cookies.set('c3', 'v3')
    session.remove_cookies(['c1', 'c3'])
    assert session.cookies == RequestsCookieJar()
    session.cookies.set('c1', 'v1')
    session.cookies.set('c2', 'v2')
    session.cookies.set('c3', 'v3')
    session.remove_cookies(['c1', 'c4'])
    assert session.cookies == RequestsCookieJar()
    session.cookies.set('c1', 'v1')
    session

# Generated at 2022-06-13 22:41:31.862086
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(os.devnull)
    s.update({'cookies': {'abc': {'value':'abc'}, 'def': {'value':'def'}}})
    s.remove_cookies(['abc'])
    assert s == {'cookies': {'def': {'value':'def'}}}
    s.remove_cookies(['xyz'])
    assert s == {'cookies': {'def': {'value':'def'}}}
    s.remove_cookies(['def'])
    assert s == {}



# Generated at 2022-06-13 22:41:41.011308
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('/path/to/session.json')
    assert not s['cookies']
    s['cookies'] = {'key1': {'value': 'value1'}, 'key2': {'value': 'value2'}}
    s.remove_cookies([])
    assert s['cookies'] == {'key1': {'value': 'value1'}, 'key2': {'value': 'value2'}}
    s.remove_cookies(['key1'])
    assert s['cookies'] == {'key2': {'value': 'value2'}}
    s.remove_cookies(['key1', 'key2'])
    assert not s['cookies']

test_Session_remove_cookies()