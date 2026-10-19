

# Generated at 2022-06-13 22:33:29.256860
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('path')
    class RequestHeadersDict(dict):
        def __setitem__(self, key, value):
            if type(value) is not str:
                value = value.decode('utf8')
            super().__setitem__(key, value)

    # Test 1
    request_headers = RequestHeadersDict({'headers_1': '1', 'user-agent': 'HTTPie/1.1.2', 'content-type': 'html', 'if-a': '1'})
    session.update_headers(request_headers)
    expected = session.headers
    real = RequestHeadersDict({'headers_1': '1', 'content-type': 'html'})
    assert real == expected

    # Test 2

# Generated at 2022-06-13 22:33:35.570016
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session('test')
    session.headers = {}
    a = {'Content-Type': "application/json", 'Accept': "application/json"}
    session.update_headers(a)
    b = {'Content-Type': "application/json"}
    assert session.headers == {'Accept': "application/json"}

# Generated at 2022-06-13 22:33:45.992365
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session('test')
    test_session['cookies'] = {'testcookie': {'value': 'test', 'path': '/'}}

    test_session.remove_cookies(['testcookie'])
    assert (test_session['cookies'] == {})

    test_session['cookies'] = {'testcookie': {'value': 'test', 'path': '/'}}

    test_session.remove_cookies(['testcookie2'])
    assert (test_session['cookies'] == {'testcookie': {'value': 'test', 'path': '/'}})



# Generated at 2022-06-13 22:33:58.468917
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    #make a mock session
    mock_session = Session('.httpie')
    mock_session['cookies']={'cookie_1':{'value':'cookie_value_1'},'cookie_2':{'value':'cookie_value_2'}}

    #test the removal of 1 cookie
    mock_session.remove_cookies(['cookie_1'])
    assert mock_session['cookies']=={'cookie_2':{'value':'cookie_value_2'}}

    #test the removal of 2 cookies
    mock_session.remove_cookies(['cookie_2'])
    assert mock_session['cookies']=={}


# Generated at 2022-06-13 22:34:09.794507
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    ses = Session("")
    print("Original session:")
    print(ses)

    update_dict = {}
    update_dict["cookie"] = "JSESSIONID=0123456789"
    update_dict["if-modified-since"] = "Sat, 29 Oct 1994 19:43:31 GMT"

    ses.update_headers(update_dict)

    print("Updated session:")
    print(ses)

    assert ses["cookies"]["JSESSIONID"] == {"value": "0123456789"}
    assert "if-modified-since" not in ses["headers"].keys()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        session_path = sys.argv[1]

# Generated at 2022-06-13 22:34:15.647114
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    import pytest
    headers = {'Content-Type': 'application/json', 'cache-control': 'no-cache'}
    session = Session('./test_session.json')
    session.update_headers(headers)
    assert session['headers'] == {'Content-Type': 'application/json'}



# Generated at 2022-06-13 22:34:28.303769
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    h1 = {'content-type': 'text/html',
            'if-modified-sinced': 'Fri, 21 Oct 2017 01:01:01 GMT'}
    h2 = {'content-type': 'text/hmtl',
            'if-modified-since': 'Fri, 21 Oct 2017 01:01:01 GMT'}
    h3 = {'content-type': 'text/html',
            'If-Modified-Since': 'Fri, 21 Oct 2017 01:01:01 GMT'}
    h4 = {'content-type': 'text/hmtl',
            'If-Modified-Since': 'Fri, 21 Oct 2017 01:01:01 GMT'}

# Generated at 2022-06-13 22:34:39.707338
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test.json')

    session['cookies'] = dict()
    session['cookies']['aaa'] = dict()
    session['cookies']['aaa']['value'] = "aaa"
    session['cookies']['bbb'] = dict()
    session['cookies']['bbb']['value'] = "bbb"
    session['cookies']['ccc'] = dict()
    session['cookies']['ccc']['value'] = "ccc"

    session.remove_cookies(['aaa','ccc'])
    assert not session['cookies'].__contains__('aaa')
    assert not session['cookies'].__contains__('ccc')
    assert session['cookies'].__contains__('bbb')


# Generated at 2022-06-13 22:34:49.611886
# Unit test for method update_headers of class Session
def test_Session_update_headers():
    session = Session("Session1.json")
    session["headers"] = {
          "accept": "text/html",
          "accept-encoding": "gzip"
    }
    request_headers = RequestHeadersDict({
          "accept-encoding": "gzip",
          "accept": "text/html",
          "content-length": "8",
          "content-type": "plain/text",
          "cookie": "Status=OK; Domain=localhost; Path=/",
          "if-match": "*",
          "if-modified-since": "Fri, 02 May 2014 13:22:30 GMT"
    })
    session.update_headers(request_headers)

# Generated at 2022-06-13 22:34:54.363318
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session['cookies'] = {'value': 'hi', 'path': '/'}
    session.remove_cookies(['value'])
    assert session['cookies'] == {}



# Generated at 2022-06-13 22:35:08.344639
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    dict = {'cookies': {'foo':{'value':'bar'}, 'baz':{'value':'qux'}}}
    session = Session('test')
    session.update(dict)
    assert 'foo' in session['cookies'] and session['cookies']['foo'] == {'value':'bar'}
    assert 'baz' in session['cookies'] and session['cookies']['baz'] == {'value':'qux'}
    session.remove_cookies(['foo'])
    assert 'foo' not in session['cookies'] and 'baz' in session['cookies']

# Generated at 2022-06-13 22:35:14.314927
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session['cookies'] = {'c1': {'value': 'v1'}, 'c2': {'value': 'v2'}}
    session.remove_cookies(['c1'])
    assert session['cookies'] == {'c2': {'value': 'v2'}}

# Generated at 2022-06-13 22:35:16.517721
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('testSession')
    session.remove_cookies({'cookie1', 'cookie2'})

# Generated at 2022-06-13 22:35:19.631912
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path = "/home/user/httpie/sessions/session.json")
    session['cookies'] = {'name1': 0, 'name2': 1, 'name3': 2, 'name4': 3, 'name5': 4}
    session.remove_cookies(names = ['name1', 'name3', 'name5'])
    assert session['cookies'] == {'name2': 1, 'name4': 3}
# End


# Generated at 2022-06-13 22:35:25.509830
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {'a': {'value': 10}, 'b': {'value': 20}}
    test = Session('./test')
    test['cookies'] = cookies
    test.remove_cookies(['c'])
    assert test['cookies'] == cookies
    test.remove_cookies(['a'])
    assert test['cookies'] == {'b': {'value': 20}}
    test.remove_cookies(['b'])
    assert test['cookies'] == {}


# Generated at 2022-06-13 22:35:34.114998
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    expected_cookies = {"A": {'value': 1}, "B": {'value': 2}}
    session = Session("/dev/null")
    session.cookies = RequestsCookieJar()
    for name, value in expected_cookies.items():
        session.cookies.set_cookie(create_cookie(name, value))

    session.remove_cookies("A")
    actual_cookies = session.cookies
    for name, value in actual_cookies.items():
        assert expected_cookies[name] == value, f"Cookies did not match {name}"

# Generated at 2022-06-13 22:35:39.394907
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    names=['sessionID','userID']
    s=Session('path')
    session_dict1={"cookies": {"sessionID": "0x21", "userID": "4"}}
    session_dict2={"cookies": {"sessionID": "0x21"}}
    s.update(session_dict1)
    s.remove_cookies(names)
    assert(session_dict2==s)

# Generated at 2022-06-13 22:35:45.370767
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('path')
    session.cookies = RequestsCookieJar()
    session.cookies.set_cookie(
        create_cookie(name='name', value='value', path='/'))
    assert 'name' in session.cookies
    session.remove_cookies(['name'])
    assert 'name' not in session.cookies
    session.remove_cookies(['name'])

# Generated at 2022-06-13 22:35:50.891599
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('.')
    s['cookies'] = {'1': {'value': '1'}, '2': {'value': '2'}}
    s.remove_cookies(['1', '2'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:35:56.923678
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path('/tmp/test.json'))
    session.load()
    session['cookies'] = {'b': 'cookie b', 'a': 'cookie a', 'c': 'cookie c'}
    session.remove_cookies(['b', 'c'])
    assert session['cookies'] == {'a': 'cookie a'}

# Generated at 2022-06-13 22:36:07.916845
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path('./test/test_session.json'))
    session.load()
    session.remove_cookies(['cookies_1_1'])
    assert len(session['cookies']) == 2
    assert session['cookies'].get('cookies_1_1') is None
    assert session['cookies']['cookies_1_2']['value'] == 'cookies_1_2_value'
    assert session['cookies']['cookies_1_3']['value'] == 'cookies_1_3_value'

# Generated at 2022-06-13 22:36:16.506221
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("")
    s.cookies = RequestsCookieJar()
    s.cookies.set("a", "value", domain="example.org", path="/")
    s.cookies.set("b", "value", domain="example.org", path="/")
    assert len(s.cookies) == 2
    s.remove_cookies(("a", "b"))
    assert len(s.cookies) == 0


# Generated at 2022-06-13 22:36:21.090800
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('a')
    s['cookies'] = {'a': {'v': 1}, 'b': {'v': 2}}
    s.remove_cookies(('b', 'c'))
    assert s['cookies'] == {'a': {'v': 1}}



# Generated at 2022-06-13 22:36:30.779768
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path(__file__).parent / 'a.json'
    session = Session(path)
    session['type'] = 'Session'
    session['cookies'] = { 'a': 1, 'b': 2, 'c': 3}
    names = ['a', 'b', 'd']
    session.remove_cookies(names)
    assert (session['cookies'] == {'a': 1, 'b': 2})
    # If a non-existing name is provided, the method remove_cookies
    # should not raise any exception.

test_Session_remove_cookies()



# Generated at 2022-06-13 22:36:33.134957
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test')
    session['cookies'] = {'a':1, 'b':2}
    session.remove_cookies(['a'])
    assert session['cookies'] == {'b':2}

# Generated at 2022-06-13 22:36:44.703827
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # test the Session.remove_cookies(names) method for the case where
    # the same cookie name is specified twice in the 'names' parameter
    # list
    session = Session('test_Session_remove_cookies.json')
    session['cookies'] = {
        'cookie1': {'value': 'cookie1_value'},
        'cookie2': {'value': 'cookie2_value'},
        'cookie3': {'value': 'cookie3_value'},
    }
    session.remove_cookies(['cookie1', 'cookie2', 'cookie3', 'cookie1', 'cookie2'])
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' not in session['cookies']
    assert 'cookie3' not in session['cookies']

# Generated at 2022-06-13 22:36:51.736134
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie1 = {'name': 'c1', 'value': 'v1'}
    cookie2 = {'name': 'c2', 'value': 'v2'}
    session = Session('./test')
    session['cookies'] = {cookie1['name']: {'value': cookie1['value']},
                          cookie2['name']: {'value': cookie2['value']}}
    names = [cookie1['name'], cookie2['name']]
    session.remove_cookies(names)
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:36:59.707786
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('sessions')
    s['cookies'] = {'n1': 'v1', 'n2': 'v2'}
    s.remove_cookies(['n1'])
    assert s['cookies'] == {'n2': 'v2'}, \
        'remove_cookies removes one cookie'
    s.remove_cookies(['n2'])
    assert s['cookies'] == {}, \
        'remove_cookies removes multiple cookies'
    s['cookies'] = {'n1': 'v1', 'n2': 'v2'}
    s.remove_cookies(['n3'])
    assert s['cookies'] == {'n1': 'v1', 'n2': 'v2'}, \
        'remove_cookies does not remove nonexistent cookie'

# Generated at 2022-06-13 22:37:08.404335
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='/test_path')
    session.cookies = {
        'cookie1': 'value1',
        'cookie2': 'value2',
        'cookie3': 'value3',
        'cookie4': 'value4',
        'cookie5': 'value5'
    }
    session.remove_cookies(['cookie3', 'cookie5'])
    assert session.cookies == {
        'cookie1': 'value1',
        'cookie2': 'value2',
        'cookie4': 'value4',
        'cookie5': 'value5'
    }

# Generated at 2022-06-13 22:37:17.787628
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():

    session = Session('dummy')
    names = ['cookie1', 'cookie2']
    session['cookies'] = {
        'cookie1' : { 'value' : 'cookie1' },
        'cookie2' : { 'value' : 'cookie2' },
        'cookie3' : { 'value' : 'cookie3' }
    }

    session.remove_cookies(names)

    assert session['cookies'] == { 'cookie3' : { 'value' : 'cookie3' } }

# Generated at 2022-06-13 22:37:26.294079
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('/tmp/test_httpie_session.json')
    session['cookies'] = {"test1": "test1", "test2": "test2"}
    session.remove_cookies(["test1"])
    assert "test2" in session['cookies']
    assert "test1" not in session['cookies']

# Generated at 2022-06-13 22:37:33.444337
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=Path("./session.json"))
    session['cookies']={'name1':'value1','name2':'value'}
    assert session['cookies']=={'name1':'value1','name2':'value'}
    session.remove_cookies(names=['name2'])
    assert session['cookies']=={'name1':'value1'}

# Generated at 2022-06-13 22:37:37.048212
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('session')
    session['cookies'] = {'A': {}, 'B': {}}
    session.remove_cookies(['A', 'C'])
    assert session['cookies'] == {'B': {}}

# Generated at 2022-06-13 22:37:40.504755
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("test")
    session["cookies"] = {"my_cookie": {"value": "my value"}}

    session.remove_cookies(["my_cookie"])
    assert not session.get("cookies")


# Generated at 2022-06-13 22:37:45.740718
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {'name': {'value': 'value', 'path': '/some/path'}}
    s.remove_cookies(['name'])
    assert s['cookies'] == {}

# Generated at 2022-06-13 22:37:50.894683
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("/")
    session['cookies'] = {name: None for name in ['name1', 'name2', 'name3']}
    assert session['cookies'] == {name: None for name in ['name1', 'name2', 'name3']}

    session.remove_cookies(['name1', 'name3'])
    assert session['cookies'] == {'name2': None}

# Generated at 2022-06-13 22:37:54.992203
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_jar = RequestsCookieJar()
    cookie_jar.set('name', 'value', path='/', secure=True)
    session = Session(path=None)
    session.cookies = cookie_jar
    assert 'name' in session.cookies
    session.remove_cookies(['name'])
    assert 'name' not in session.cookies

# Generated at 2022-06-13 22:37:58.484304
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session("path")
    session['cookies'] = {'foo' : 'bar1','boo' : 'bar2','koo' : 'bar3'}
    session.remove_cookies(['foo','boo'])
    assert session['cookies'] == {'koo' : 'bar3'}



# Generated at 2022-06-13 22:38:03.742556
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session("")
    s['cookies'] = {}
    s['cookies']['one'] = {}
    s['cookies']['two'] = {}
    s.remove_cookies(['one', 'two'])
    assert len(s['cookies']) == 0

# Generated at 2022-06-13 22:38:05.805993
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    my_session = Session('testing')
    my_session['cookies'] = {'one':{},'two':{},'three':{}}
    my_session.remove_cookies(['one','two','four'])
    assert my_session['cookies'] == {'three': {}}, 'testing Session.remove_cookies()'

# Generated at 2022-06-13 22:38:11.629373
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(Path('test'))
    session['cookies'] = {'cookie1': 'cookie1', 'cookie2': 'cookie2'}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': 'cookie2'}



# Generated at 2022-06-13 22:38:19.024815
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    default_session = Session('default')
    default_session.load()
    default_session['cookies'] = {'A': '1', 'B': '2'}
    assert len(default_session['cookies']) == 2
    default_session.remove_cookies(['A', 'B'])
    assert len(default_session['cookies']) == 0
    default_session.remove_cookies(['A', 'C', 'D'])
    assert len(default_session['cookies']) == 0
    default_session['cookies'] = {'A': '1', 'B': '2'}
    assert len(default_session['cookies']) == 2
    default_session.remove_cookies(['A', 'C'])
    assert len(default_session['cookies']) == 1
   

# Generated at 2022-06-13 22:38:27.127476
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(".cookies")
    session["cookies"] = {}
    session["cookies"]["c_1"] = "1"
    session["cookies"]["c_2"] = "2"
    session["cookies"]["c_3"] = "3"
    session["cookies"]["c_4"] = "4"

    cookies = ["c_1", "c_3", "c_5"]
    session.remove_cookies(cookies)

    assert len(session["cookies"]) == 2
    for key in session["cookies"].keys():
        assert key in ["c_2", "c_4"]

# Generated at 2022-06-13 22:38:34.544999
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = {
        'name1': {'value': 'value1', 'path': '/', 'expires': None, 'secure': False},
        'name2': {'value': 'value2', 'path': '/', 'expires': None, 'secure': False}
    }
    session = Session('/path/to')
    session.cookies = cookies
    session.remove_cookies(['name1', 'name3'])
    assert len(session.cookies) == 1

# Generated at 2022-06-13 22:38:44.861564
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import json
    import requests
    session_path = requests.Session()
    data = {
        "headers": {}
    }
    with open("/tmp/test_file.txt", 'w') as outfile:
        json.dump(data, outfile)
    session = Session("/tmp/test_file.txt")
    cookie1 = requests.cookies.RequestsCookieJar()
    cookie2 = requests.cookies.RequestsCookieJar()
    cookie1.set("a", "b")
    cookie2.set("a", "c")
    session.cookies = cookie1
    session.cookies = cookie2
    session.remove_cookies(["a"])
    assert(session["cookies"] == {})

# Generated at 2022-06-13 22:38:53.768409
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('sessions/test/test.json')
    session['cookies'] = dict(
        aa=dict(value='aa'),
        bb=dict(value='bb')
    )

    assert 'aa' in session['cookies']
    assert 'bb' in session['cookies']

    session.remove_cookies(['aa'])

    assert 'aa' not in session['cookies']
    assert 'bb' in session['cookies']

# Generated at 2022-06-13 22:38:58.941967
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_session.json')
    session['cookies']={'AA':{'value':'AAC'},'BB':{'value':'BBC'}}
    session.remove_cookies(['AA','CC'])
    assert session['cookies'] == {'BB':{'value':'BBC'}}

# Generated at 2022-06-13 22:39:06.297726
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('.')
    session['cookies'].update({'name1': {'value': 'cookie1'},
                               'name2': {'value': 'cookie2'},
                               'name3': {'value': 'cookie3'}})
    session.remove_cookies(['name1','name3'])
    assert set(session['cookies']) == set(['name2'])
    assert session['cookies']['name2']['value'] == 'cookie2'
    assert len(session['cookies']) == 1

# Generated at 2022-06-13 22:39:11.038496
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    j = RequestsCookieJar()
    j.set('test_session.py', '123', path='/')
    j.set('test_session.py', '456', path='/')
    s = Session(path='test.json')
    s['cookies'] = j
    s.remove_cookies(['test_session.py'])
    assert not s['cookies']

# Generated at 2022-06-13 22:39:16.554752
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    mySession = Session(Path('test.json'))
    mySession['cookies'] = {'name_valid': 1, 'name_invalid': 2}
    names = ['name_valid']
    mySession.remove_cookies(names)
    assert len(mySession['cookies']) == 1
    assert mySession['cookies'].get('name_valid') is None

# Generated at 2022-06-13 22:39:27.105865
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session['cookies'] = {'foo': {},
                          'bar': {},
                          'baz': {}}
    session.remove_cookies(['foo', 'bar'])
    assert list(session['cookies'].keys()) == ['baz']

# Generated at 2022-06-13 22:39:34.586362
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookiename='sessionid'
    cookiename1='sessionid1'
    s = Session({'cookies':{'sessionid':'1234','sessionid1':'1234'}})
    s.remove_cookies([cookiename])
    assert cookiename1 in s['cookies']
    assert cookiename not in s['cookies']

# Generated at 2022-06-13 22:39:38.381561
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    cookies = {'foo': 'bar'}
    session['cookies'] = cookies
    session.remove_cookies(['foo'])
    assert len(session['cookies']) == 0, \
        'Cookies could not be removed from the session'

# Generated at 2022-06-13 22:39:52.184536
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies = [{'value': 'test', 'path': 'test', 'expires': 12345, 'secure': True}]
    session = Session("test")
    session.cookies = [{'value': 'test', 'path': 'test', 'expires': 12345, 'secure': True}]

    # Re-initialize the class value
    session = Session("test")
    session.cookies = [{'value': 'test', 'path': 'test', 'expires': 12345, 'secure': True}]
    session.remove_cookies([])
    assert session.cookies == cookies

    # Re-initialize the class value
    session = Session("test")
    session.cookies = [{'value': 'test', 'path': 'test', 'expires': 12345, 'secure': True}]

# Generated at 2022-06-13 22:39:57.402798
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path='path')
    session['cookies'] = {'cookies': {'key1': 'value1', 'key2': 'value2'}}
    session.remove_cookies(['key1', 'key3'])
    assert session['cookies'] == {'cookies': {'key2': 'value2'}}


# Generated at 2022-06-13 22:40:01.733897
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(os.getcwd())
    s['cookies'] = {'foo': 'bar', 'baz': 'qux'}
    s.remove_cookies(['baz'])
    assert s['cookies'] == {'foo': 'bar'}

# Generated at 2022-06-13 22:40:13.876802
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    from httpie.session import Session
    from httpie.compat import urlunparse
    from httpie.cookies import CookieJar

    headers = {
        'Connection': 'keep-alive',
        'Host': 'httpbin.org',
        'User-Agent': 'HTTPie/0.9.3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'application/json',
        'Content-Length': 0
    }
    cookies = {
        'fake': 'fake_value'
    }
    cookies_to_remove = ['fake']
    url = urlunparse(('http', 'httpbin.org', '/cookies/delete', '', '', ''))
    session = Session('test.json')

    session.update_headers(headers)

# Generated at 2022-06-13 22:40:21.870794
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = "test.json"
    session = Session(path)
    session.load()
    session['cookies']['name1'] = {'value': 'value1'}
    session['cookies']['name2'] = {'value': 'value2'}
    session['cookies']['name3'] = {'value': 'value3'}
    session.save()
    session = Session(path)
    session.load()
    session.remove_cookies(['name1','name3'])
    assert session['cookies']['name2'] == {'value': 'value2'}
    os.remove(path)

# Generated at 2022-06-13 22:40:28.533529
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session(str(DEFAULT_CONFIG_DIR))
    s.load()
    s['cookies'] = {'name': {'value': 'value1'}}
    assert len(s['cookies']) == 1
    s.remove_cookies(['name'])
    assert len(s['cookies']) == 0



# Generated at 2022-06-13 22:40:42.072091
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    import shutil
    import tempfile
    import json
    # Set up a temporary directory
    tmpdir = tempfile.mkdtemp()
    tmp_session_dir = os.path.join(tmpdir, SESSIONS_DIR_NAME)
    os.mkdir(tmp_session_dir)
    # Create a session file and add some cookies to it
    tmp_session_file = os.path.join(tmp_session_dir, 'test_session_file.json')
    session_file = open(tmp_session_file, 'w')
    session_json = {'headers': {}, 'cookies': {'cookie_1': 'value_1',
                                               'cookie_2': 'value_2'}}
    json.dump(session_json, session_file)
    session_file.close()
    # Create a

# Generated at 2022-06-13 22:40:59.283599
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('')
    s['cookies'] = {'test': {'test': 'test'}}
    s.remove_cookies(['test'])
    assert s['cookies'] == {}


# Generated at 2022-06-13 22:41:06.382617
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = os.getcwd() / "test_Session_remove_cookies.json"
    path.write_text("""
    {
        "cookies": {
            "a": {
                "value": "A"
            },
            "b": {
                "value": "B"
            }
        }
    }
    """)
    session = Session(path)
    session.load()
    session.remove_cookies(["a","b","c"])
    assert session["cookies"] == {}
    path.unlink()


# Generated at 2022-06-13 22:41:12.206083
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # given
    s = Session("test.json")
    s['cookies'] = {'a': 'a', 'b': 'b', 'c': 'c'}
    # when
    s.remove_cookies(['b'])
    # then
    assert s['cookies'] == {'a': 'a', 'c': 'c'}



# Generated at 2022-06-13 22:41:23.425222
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session(path ='/home/debian/.config/httpie/sessions/www.google.com/google.json')

# Generated at 2022-06-13 22:41:30.572681
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test.json')
    session['cookies'] = {
        'cookie1': {'value': 'value1'},
        'cookie2': {'value': 'value2'},
    }
    session.remove_cookies(['cookie2'])
    assert session['cookies'] == {
        'cookie1': {'value': 'value1'},
    }


# Generated at 2022-06-13 22:41:34.885578
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    test_session = Session("test_Session_remove_cookies")
    test_session['cookies'] = {'session': {'name': 'session', 'value': 'test_value'}}
    test_session.remove_cookies(['session'])
    assert 'session' not in test_session['cookies']

# Generated at 2022-06-13 22:41:37.601685
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session  = Session('test.json')
    session['cookies'] = {'key': 'value'}
    session.remove_cookies(['key'])
    assert 'key' not in session['cookies']

# Generated at 2022-06-13 22:41:43.908085
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_file = 'sessions/localhost/example.com.json'
    session = Session(session_file)
    session.load()
    session.remove_cookies(['name1', 'name2'])
    assert 'name1' not in session['cookies']
    assert 'name2' not in session['cookies']
    session.save()

    session_file = 'sessions/localhost/example.com.json'
    session = Session(session_file)
    session.load()
    assert 'name1' not in session['cookies']
    assert 'name2' not in session['cookies']



# Generated at 2022-06-13 22:41:53.238667
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('foo')
    session.gather_session_cookies = lambda: RequestsCookieJar()
    session['cookies'] = {
        'bar': {'value': 'baz', 'path': '/foo', 'secure': True},
        'qux': {'value': 'quux'},
        'corge': {'value': 'grault'},
    }
    session.remove_cookies(['bar', 'corge'])
    assert session['cookies'] == {'qux': {'value': 'quux'}}

# Generated at 2022-06-13 22:41:59.096478
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('test_remove_cookies')
    session.update({'cookies': {'name1':{'name':'name1','value':'value1'},
                                'name2':{'name':'name2','value':'value2'},
                                'name3':{'name':'name3','value':'value3'}}})
    session.remove_cookies(['name1','name3'])
    assert not 'name1' in session['cookies']
    assert not 'name3' in session['cookies']

# Generated at 2022-06-13 22:42:19.170610
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('')
    session.cookies = RequestsCookieJar()
    cookie = dict(
        name = 'my_cookie',
        value = 'my_value',
        path = '/',
        domain = 'example.com',
        secure = True
    )
    session.cookies.set(**cookie)
    assert cookie['name'] in session['cookies']
    session.remove_cookies(['my_cookie'])
    assert cookie['name'] not in session['cookies']

# Generated at 2022-06-13 22:42:26.223012
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session(path=DEFAULT_SESSIONS_DIR / 'session.json')
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}}
    session.remove_cookies(['cookie1'])
    assert session['cookies'] == {'cookie2': {'value': 'value2'}}



# Generated at 2022-06-13 22:42:29.842710
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_path = Path('./Session.json')
    session = Session(session_path)
    session['cookies'] = {'cookie1': {'value': 'value1'}, 'cookie2': {'value': 'value2'}}
    session.remove_cookies(['cookie1', 'cookie2'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:42:33.887206
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    s = Session('test')
    cookie_1 = {'name': 'Httpie', 'value': 'cookie'}
    cookie_2 = {'name': 'Curl', 'value': 'biscuit'}
    s['cookies'] = {cookie_1['name']: cookie_1, cookie_2['name']: cookie_2}
    before = len(s['cookies'])
    s.remove_cookies([cookie_1['name']])
    after = len(s['cookies'])
    assert (before - after) == 1

# Generated at 2022-06-13 22:42:46.598121
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookie_a = {'value': 'a', 'path': '/', 'secure': True, 'expires': '01/01/01'}
    cookie_b = {'value': 'b', 'path': '/', 'secure': True, 'expires': '02/02/02'}
    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie('foo', cookie_a['value'], **cookie_a))
    jar.set_cookie(create_cookie('bar', cookie_b['value'], **cookie_b))
    s = Session('test')
    s.cookies = jar
    assert 'foo' in s['cookies']
    assert 'bar' in s['cookies']
    s.remove_cookies(['foo'])
    assert 'foo' not in s['cookies']
   

# Generated at 2022-06-13 22:42:52.583833
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    path = Path('/home/louis_gomez/.config/httpie/sessions/http-prompt.com/test.json')
    session = Session(path)
    session.load()
    print(session.cookies)
    session.remove_cookies(['csrftoken'])
    print(session.cookies)

# Generated at 2022-06-13 22:42:58.174292
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session_name = "http://www.example.com"
    sd1 = Session('{}.json'.format(session_name))
    sd1['cookies'] =  {"name1":{"value":"val1"}}
    assert sd1.remove_cookies(["name1"]) == None
    assert sd1.cookies == RequestsCookieJar()


# Generated at 2022-06-13 22:43:03.580848
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    cookies_dict = {'name_1': {'value': 'value_1'}, 'name_2': {'value': 'value_2'}}
    session = Session('path')    
    session['cookies'] = cookies_dict
    names = ['name_1']
    session.remove_cookies(names)
    assert len(session['cookies']) == 1
    assert 'name_2' in session['cookies']
    assert 'name_1' not in session['cookies']

# Generated at 2022-06-13 22:43:11.652047
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    session = Session('a.json')
    session['cookies'] = {
        'a': {'value': 'aa'},
        'b': {'value': 'bb'},
        'c': {'value': 'cc'},
        'd': {'value': 'dd'},
    }
    assert sorted(session['cookies'].keys()) == ['a', 'b', 'c', 'd']

    session.remove_cookies(['b'])
    assert sorted(session['cookies'].keys()) == ['a', 'c', 'd']

    session.remove_cookies(['a', 'c', 'e'])
    assert sorted(session['cookies'].keys()) == ['d']

    session.remove_cookies(['d', 'e'])
    assert session['cookies'] == {}

# Generated at 2022-06-13 22:43:21.021819
# Unit test for method remove_cookies of class Session
def test_Session_remove_cookies():
    # Test if Session.remove_cookies() actually removes the cookies
    
    s = Session('test')

    assert len(s) == 3

    # Add a list of cookies with some values
    s['cookies'] = {"a": {"value": "image"}, "b": {"value": "video"}, "c": {"value": "song"}}

    assert len(s['cookies']) == 3

    # Remove the cookies from the name list
    s.remove_cookies(["a", "b"])

    assert len(s['cookies']) == 1
    assert s['cookies'] == {"c": {"value": "song"}}