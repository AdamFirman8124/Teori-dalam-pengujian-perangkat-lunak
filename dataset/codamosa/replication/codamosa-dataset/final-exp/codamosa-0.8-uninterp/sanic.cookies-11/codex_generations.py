

# Generated at 2022-06-14 06:57:23.340101
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie_val = "s3.q3m4m6.sig=baa7b8d1b9e71785f06523c88033e8ab"
    cookie_key = "AWSELB"
    cookie = Cookie(cookie_key, cookie_val)
    cookie["path"] = "/"
    result = str(cookie)
    expected = "AWSELB=s3.q3m4m6.sig%3Dbaa7b8d1b9e71785f06523c88033e8ab; Path=%2F"
    if result != expected:
        raise RuntimeError(f"Test failed! Response is: {result}, expected: {expected}")
    return True


# Generated at 2022-06-14 06:57:33.474333
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Case 1: input key is a string and the cookie exists
    headers = CIMultiDict()
    headers.add('Set-Cookie', "flavor=chocolate")
    cookie_jar = CookieJar(headers)
    cookie_jar["flavor"] = "vanilla"
    del cookie_jar["flavor"]
    assert str(cookie_jar) == ""

    # Case 2: input key is a string and the cookie does not exist
    headers = CIMultiDict()
    cookie_jar = CookieJar(headers)
    del cookie_jar["flavor"]
    assert str(cookie_jar) == ""



# Generated at 2022-06-14 06:57:44.240884
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    CJ = CookieJar(headers)
    CJ['cookie'] = 'cheesecake'
    CJ['cookie2'] = 'icecream'
    CJ['cookie3'] = 'cookie'
    assert headers['Set-Cookie'] == 'cookie=cheesecake; Path=/; Max-Age=0; ' \
                                    'cookie2=icecream; Path=/; Max-Age=0; ' \
                                    'cookie3=cookie; Path=/; Max-Age=0; '
    del CJ['cookie2']
    assert headers['Set-Cookie'] == 'cookie=cheesecake; Path=/; Max-Age=0; ' \
                                    'cookie3=cookie; Path=/; Max-Age=0; '

# Generated at 2022-06-14 06:57:48.456462
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie('key', 'value')
    c['max_age'] = 0
    c['comment'] = 'comment'
    print(c)


# Generated at 2022-06-14 06:57:52.105487
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookiejar_1 = CookieJar({})
    assert len(cookiejar_1.headers) == 0

    cookiejar_1["key_1"] = "value_1"
    assert len(cookiejar_1.headers) == 1
    assert cookiejar_1["key_1"].value == "value_1"
    assert len(cookiejar_1.cookie_headers) == 1
    assert cookiejar_1.cookie_headers["key_1"] == "Set-Cookie"

    cookiejar_1["key_2"] = "value_2"
    assert len(cookiejar_1.headers) == 1
    assert cookiejar_1["key_2"].value == "value_2"
    assert len(cookiejar_1.cookie_headers) == 2

# Generated at 2022-06-14 06:57:59.158073
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test", "value")
    cookie["path"] = "/"
    cookie["secure"] = True
    cookie["name"] = "value"
    cookie["max-age"] = 0

    # Raise KeyError
    with pytest.raises(KeyError):
        cookie["name"] = "value"

    # Raise ValueError
    with pytest.raises(ValueError):
        cookie["max-age"] = "a"


# Generated at 2022-06-14 06:58:04.669711
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookiejar = CookieJar(headers)
    assert not headers
    assert not cookiejar
    cookiejar['name'] = 'value'
    assert 'name=value' in headers['Set-Cookie']
    assert cookiejar['name'].value == 'value'
    del cookiejar['name']
    assert 'name=value' not in headers['Set-Cookie']
    assert not cookiejar



# Generated at 2022-06-14 06:58:14.304460
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime
    from datetime import timedelta
    expiration=datetime.now()
    expiration=expiration+timedelta(days=1)
    cookie_string=Cookie('username','user@example.com')
    cookie_string['secure']=True
    cookie_string['expires']=expiration
    cookie_string['max-age']=10
    assert 'username=user@example.com; expires=Fri, 21-Feb-2020 18:51:48 GMT; max-age=10; Secure' == str(cookie_string)

# Generated at 2022-06-14 06:58:26.418884
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key='cookie_name', value='cookie_val')
    assert str(cookie) == "cookie_name=cookie_val"
    cookie['path'] = '/some/path'
    assert str(cookie) == "cookie_name=cookie_val; Path=/some/path"
    cookie['expires'] = datetime(year=2020, month=3, day=11, hour=15, minute=59, second=0)
    cookie['max-age'] = 999
    assert str(cookie) == "cookie_name=cookie_val; Path=/some/path; expires=Wed, 11-Mar-2020 15:59:00 GMT; Max-Age=999"
    cookie['secure'] = True
    cookie['httponly'] = True

# Generated at 2022-06-14 06:58:33.134526
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    some_cookie = Cookie('key', 'value')
    expected = 'key=value'
    assert(str(some_cookie) == expected)
    some_cookie = Cookie('key', 'value_with_no_legal_char')
    expected = 'key="value_with_no_legal_char"'
    assert(str(some_cookie) == expected)
    some_cookie['max-age'] = 29
    expected = 'key="value_with_no_legal_char"; Max-Age=29'
    assert(str(some_cookie) == expected)
    some_cookie['path'] = '/'
    expected = 'key="value_with_no_legal_char"; Max-Age=29; Path=/'
    assert(str(some_cookie) == expected)
    some_cookie['domain'] = 'example.com'
   

# Generated at 2022-06-14 06:58:47.454674
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("cookie_name", "cookie_value")
    c["path"] = "/"
    c["max-age"] = 1
    c["comment"] = "comment"
    c["domain"] = "domain"
    c["secure"] = False
    c["httponly"] = False
    c["version"] = 1
    c["expires"] = datetime.utcnow()
    c["samesite"] = "Strict"
    assert str(c) == "cookie_name=cookie_value; Path=/; Max-Age=1; Comment=comment; Domain=domain; Version=1; Expires=%s; SameSite=Strict" % c["expires"].strftime("%a, %d-%b-%Y %T GMT")

# Generated at 2022-06-14 06:58:58.291635
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {"Set-Cookie": ["foo=bar"]}
    cookie_jar = CookieJar(headers)
    assert "foo" in cookie_jar
    del cookie_jar["foo"]
    assert "foo" not in cookie_jar
    assert "foo=bar" not in cookie_jar.headers["Set-Cookie"]
    # Adding foo back in
    cookie_jar["foo"] = "bar"
    assert "foo=bar" in cookie_jar.headers["Set-Cookie"]
    # Removing new foo
    del cookie_jar["foo"]
    assert "foo" not in cookie_jar
    assert "foo=bar" not in cookie_jar.headers["Set-Cookie"]

# Generated at 2022-06-14 06:59:09.215676
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers(
        {
            "Set-Cookie": [
                "test1=v1; Path=/",
                "test2=v2; Path=/",
                "test3=v3; Path=/",
            ]
        }
    )
    cs = CookieJar(headers)
    del cs["test1"]
    assert list(cs.keys()) == ["test2", "test3"]
    cs["test4"] = "v4"
    assert list(cs.keys()) == ["test2", "test3", "test4"]
    del cs["test3"]
    assert list(cs.keys()) == ["test2", "test4"]

# Generated at 2022-06-14 06:59:18.138389
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test", "test_content")
    cookie.update({"max-age": 0})
    assert cookie["max-age"] == 0
    with pytest.raises(KeyError) as excinfo:
        cookie.update({0: 1})
    assert str(excinfo.value) == "Unknown cookie property"
    with pytest.raises(ValueError) as excinfo:
        cookie.update({"max-age": "not_integer"})
    assert str(excinfo.value) == "Cookie max-age must be an integer"



# Generated at 2022-06-14 06:59:22.934359
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader([])
    cookies = CookieJar(headers)
    cookies["test_cookie"] = "cookie_value"
    # if this is not being deleted, then it would have a value
    assert not cookies.get("test_cookie")

# Generated at 2022-06-14 06:59:32.765220
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["key1"] = "value1"
    jar["key2"] = "value2"
    jar["key3"] = "value3"
    del jar["key2"]
    assert f"key1={jar['key1'].value}" in jar.headers["Set-Cookie"]
    assert f"key3={jar['key3'].value}" in jar.headers["Set-Cookie"]
    assert f"key2={jar['key2'].value}" not in jar.headers["Set-Cookie"]


# Generated at 2022-06-14 06:59:36.064785
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookie_jar = CookieJar(headers)
    key = 'a'
    cookie_jar[key] = 'a'
    assert key in cookie_jar
    del cookie_jar[key]
    assert key not in cookie_jar



# Generated at 2022-06-14 06:59:49.251321
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Create headers
    headers = Headers()

    # Create a cookie
    cookie = Cookie("test", "data")
    cookie["path"] = "/"

    # Add cookie to headers
    headers.add("Set-Cookie", cookie)

    # Create CookieJar object
    cookie_jar = CookieJar(headers)

    # Add cookie to cookie_jar
    cookie_jar["test"] = "data"

    # Test for cookie in cookie_jar
    assert "test" in cookie_jar

    # del cookie from CookieJar
    del cookie_jar["test"]

    # Test for cookie in CookieJar
    assert "test" not in cookie_jar

    # Test for cookie in headers
    assert "test" not in headers



# Generated at 2022-06-14 06:59:58.749413
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from multidict import MultiDict
    headers = MultiDict()
    # Testing CookieJar.__setitem__
    jar = CookieJar(headers)
    jar["key"] = "value"
    assert "key=value" in headers.getall("Set-Cookie")

    # Testing CookieJar.__setitem__ where key already exists
    jar = CookieJar(headers)
    jar["key"] = "value"
    jar["key"] = "new_value"
    assert "key=new_value" in headers.getall("Set-Cookie")



# Generated at 2022-06-14 07:00:09.210322
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader("Set-Cookie", ["cookie1=value1", "cookie2=value2"])
    jar = CookieJar(headers)

    # Initialization of the cookie jar
    assert len(jar) == 2
    assert len(headers) == 2
    assert "cookie1" in jar
    assert "cookie2" in jar
    assert jar["cookie1"].value == "value1"
    assert jar["cookie2"].value == "value2"
    assert headers["Set-Cookie"][0] == "cookie1=value1"
    assert headers["Set-Cookie"][1] == "cookie2=value2"

    # Adding a cookie
    jar["cookie3"] = "value3"
    assert len(jar) == 3
    assert len(headers) == 3
    assert "cookie3" in jar
   

# Generated at 2022-06-14 07:00:18.612194
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    my_cookies = CookieJar(headers={})
    my_cookies.update({'cookie1' : 'value1', 'cookie2' : 'value2'})
    my_cookies.__delitem__('cookie1')
    assert my_cookies.get('cookie1') == None
    assert my_cookies.get('cookie2') == 'value2'


# Generated at 2022-06-14 07:00:26.988812
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "val")
    assert cookie.key == "key"
    assert cookie.value == "val"
    cookie1 = Cookie("key1", "val1")
    assert cookie1.key == "key1"
    assert cookie1.value == "val1"
    cookie["expires"] = "10"
    assert cookie["expires"] == "10"
    assert cookie1["expires"] == None


# Generated at 2022-06-14 07:00:37.485158
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie("test", "value")

    assert c["expires"] is None
    with pytest.raises(ValueError):
        c["expires"] = "test"

    c["expires"] = datetime(month=12, day=12, year=2020)
    assert c["expires"] == datetime(month=12, day=12, year=2020)
    assert c["expires"] != "test"

    assert c["max-age"] is None
    with pytest.raises(ValueError):
        c["max-age"] = "test"

    c["max-age"] = "10"
    assert c["max-age"] == "10"
    assert c["max-age"] != 10



# Generated at 2022-06-14 07:00:44.984446
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from starlette.testclient import TestClient

    app = Starlette()

    @app.route("/cookie")
    def cookie(request):
        request.cookies["Hello"] = "World"
        del request.cookies["Hello"]
        return PlainTextResponse("Hello, World!")

    client = TestClient(app)
    response = client.get("/cookie")
    assert response.cookies == {}

# Generated at 2022-06-14 07:00:47.746432
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookie_jar = CookieJar({})
    cookie_jar['key'] = 'value'
    assert(cookie_jar['key'].value == 'value')


# Generated at 2022-06-14 07:00:52.243002
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    set_cookie = Cookie("session_id", "abc")
    headers = MultiHeader(set_cookie)
    cookies = CookieJar(headers)
    cookies["session_id"] = "abc"
    assert headers.getall("Set-Cookie") == [
        "session_id=abc; Path=/",
    ]
    del cookies["session_id"]
    assert headers.getall("Set-Cookie") == ["session_id=; Max-Age=0"]

# Generated at 2022-06-14 07:01:06.866199
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("cookie name", "cookie value")
    assert str(cookie) == "cookie name=cookie value"

    cookie["path"] = "/path"
    assert str(cookie) == "cookie name=cookie value; Path=/path"

    cookie["max-age"] = 100
    assert str(cookie) == "cookie name=cookie value; Path=/path; Max-Age=100"

    cookie["expires"] = datetime(2030, 1, 1, 0, 0, 0)
    assert (
        str(cookie)
        == "cookie name=cookie value; Path=/path; Max-Age=100; Expires=Mon, 01-Jan-2030 00:00:00 GMT"
    )

    cookie["flag property"] = True

# Generated at 2022-06-14 07:01:20.975485
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # When a Cookie object has only 1 attribute
    cookie = Cookie('name', 'value')
    assert(str(cookie) == 'name=value')

    # When a Cookie object has only 2 attributes - (name, value) and (path, /)
    cookie = Cookie('name', 'value')
    cookie['path'] = '/'
    assert(str(cookie) == 'name=value; Path=/')

    # When a Cookie object has only 2 attributes - (name, value) and (expires, datetime)
    cookie = Cookie('name', 'value')
    cookie['expires'] = datetime.now()
    # assert(str(cookie) == 'name=value; Expires=datetime.now()')
    # expected = 'Fri, 20 Feb 2015 22:49:00 GMT'
    # cookie = Cookie('name', 'value')


# Generated at 2022-06-14 07:01:25.891519
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    cj = CookieJar(headers)
    cj["test"] = "test_value"
    assert cj["test"].value == "test_value"
    del cj["test"]
    assert cj["test"].value == ""
    assert cj["test"]["max-age"] == 0



# Generated at 2022-06-14 07:01:30.831949
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")
    cookies = [
        c,
        c,
        c.copy(),
        c.copy(),
        c.copy(),
        c.copy(),
        c.copy(),
        c.copy(),
        c.copy(),
        c.copy(),
        c.copy(),
    ]

    cookies[0]["domain"] = "example.com"
    cookies[1]["expires"] = datetime(1970, 1, 1, 0, 0, 0)
    cookies[2]["path"] = "/"
    cookies[3]["max-age"] = 100
    cookies[4]["secure"] = True
    cookies[5]["httponly"] = True
    cookies[6]["domain"] = "example.com"

# Generated at 2022-06-14 07:01:40.009486
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = h11.Headers([
        ("Server", "h11"),
    ])
    c = CookieJar(headers)
    c["key"] = "value"
    assert c.headers[0][1] == "key=value"
    del c["key"]
    assert c.headers[0][1] == "key=; Max-Age=0"


# Generated at 2022-06-14 07:01:42.807932
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie("c", "v")
    with pytest.raises(KeyError):
        c["foo"] = "bar"



# Generated at 2022-06-14 07:01:53.785669
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    class TmpCookie(Cookie):
        def __init__(self, name, value):
            super().__init__(name, value)

    # Test 1: Change the value of a key
    cookie = TmpCookie("user_id", "john")
    cookie["path"] = "/"
    assert cookie["path"] == "/"

    # Test 2: Raise error when value is false
    cookie["path"] = False
    with pytest.raises(KeyError):
        assert cookie["path"] == ""

    # Test 3: Raise error when value is of wrong type
    with pytest.raises(TypeError):
        cookie["expires"] = "tomorrow"

    # Test 4: Raise error when key not in _keys
    with pytest.raises(KeyError):
        cookie["bob"] = "jones"

# Generated at 2022-06-14 07:01:58.375538
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('key', 'value')
    c['max-age'] = 0
    c['secure'] = True
    c['httponly'] = False
    c['domain'] = 'domain'

    assert str(c) == 'key=value; Domain=domain; Max-Age=0; Secure'


# Generated at 2022-06-14 07:02:11.286057
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "peter"
    value = "paul"
    cookie = Cookie(key, value)
    assert str(cookie) == "peter=paul"
    cookie["max-age"] = str(12345)
    assert str(cookie) == "peter=paul; Max-Age=12345"
    cookie["max-age"] = 12345
    assert str(cookie) == "peter=paul; Max-Age=12345"
    cookie["max-age"] = "abcdef"
    assert str(cookie) == "peter=paul; Max-Age=abcdef"
    cookie["expires"] = datetime.now()
    assert "expires" in str(cookie)
    cookie["path"] = "/"

# Generated at 2022-06-14 07:02:19.609804
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar({})
    cookies["foo"] = "bar"
    cookies["bar"] = "foo"
    cookies["foobar"] = "foobar"
    assert len(cookies) == 3

    del cookies["foo"]
    assert len(cookies) == 2
    assert len(cookies.headers) == 2

    del cookies["bar"]
    assert len(cookies) == 1
    assert len(cookies.headers) == 1



# Generated at 2022-06-14 07:02:26.072262
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers=MultiHeader()
    headers.add("test", "test")
    cookie_jar=CookieJar(headers)
    del cookie_jar["test"] 
    assert "test" not in cookie_jar
    assert isinstance(cookie_jar["test"],Cookie)
    assert headers.getall("Set-Cookie")==[Cookie("test",value="")]

# Generated at 2022-06-14 07:02:37.814575
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    a = Cookie("x", "y")
    assert a["x"] == "y"
    assert a["expires"] == None
    assert a["path"] == None
    assert a["comment"] == None
    assert a["domain"] == None
    assert a["max-age"] == None
    assert a["secure"] == False
    assert a["httponly"] == False
    assert a["version"] == None
    assert a["samesite"] == None

    a["expires"] = datetime.now()
    assert a["expires"] == datetime.now()
    a["expires"] = None

    a["path"] = "/"
    assert a["path"] == "/"
    a["path"] = None

    a["comment"] = "comment"
    assert a["comment"] == "comment"

# Generated at 2022-06-14 07:02:48.184988
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_headers = dict()
    h = HTTPHeaderMap(cookie_headers)
    cookie_jar = CookieJar(h)
    cookie_jar["sessid"] = "cookie_value_1"
    cookie_jar["sessid1"] = "cookie_value_2"
    cookie_jar["sessid2"] = "cookie_value_3"
    cookie_jar["sessid3"] = "cookie_value_4"
    cookie_jar["sessid4"] = "cookie_value_5"
    cookie_jar["sessid5"] = "cookie_value_6"
    cookie_jar["sessid6"] = "cookie_value_7"
    del cookie_jar["sessid"]

# Generated at 2022-06-14 07:03:01.514377
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cs = Cookie('key', 'value')
    assert cs.__str__() == 'key=value'

    cs['expires'] = datetime.strptime('Sun, 17-Jan-2038 19:14:07 GMT', '%a, %d-%b-%Y %H:%M:%S GMT')
    assert cs.__str__() == 'key=value; Expires=Sun, 17-Jan-2038 19:14:07 GMT'
    cs['expires'] = 'Sun, 17-Jan-2038 19:14:07 GMT'
    assert cs.__str__() == 'key=value; Expires=Sun, 17-Jan-2038 19:14:07 GMT'

    cs['path'] = '/'

# Generated at 2022-06-14 07:03:20.732563
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime

    # Case 1: Max age is an int
    cookie = Cookie("key", "value")
    cookie["max-age"] = 2
    assert cookie.__str__() == "key=value; Max-Age=2"

    # Case 2: Max age is a string
    cookie = Cookie("key", "value")
    cookie["max-age"] = "2"
    assert cookie.__str__() == "key=value; Max-Age=2"

    # Case 3: Expires is a datetime
    cookie = Cookie("key", "value")
    cookie["expires"] = datetime(2019, 3, 24, 17, 32, 53)
    assert cookie.__str__() == "key=value; expires=Sun, 24-Mar-2019 17:32:53 GMT"

    # Case 4: There

# Generated at 2022-06-14 07:03:32.885190
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    mock_headers = MockMultiHeaders()
    mock_headers.add("Set-Cookie", Cookie("cookie_name", "cookie_value"))

    cookie_jar = CookieJar(mock_headers)

    assert len(cookie_jar) == 1
    assert len(mock_headers["Set-Cookie"]) == 1

    # delete the only cookie
    del cookie_jar["cookie_name"]
    assert "cookie_name" not in cookie_jar
    assert "cookie_name" not in mock_headers

    # delete non-existed cookie
    del cookie_jar["cookie_name"]
    assert "cookie_name" not in cookie_jar
    assert "cookie_name" not in mock_headers



# Generated at 2022-06-14 07:03:41.666674
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test_headers = CIMultiDict()
    test_headers.add("Set-Cookie", "first=value")
    test_headers.add("Set-Cookie", "second=value")
    test_headers.add("Set-Cookie", "third=value")
    test_headers.add("Set-Cookie", "fourth=value")
    test_cookies = CookieJar(test_headers)
    test_cookies["first"] = "1"
    test_cookies["second"] = "2"
    test_cookies["third"] = "3"
    test_cookies["fourth"] = "4"
    assert set(test_cookies) == {"first", "second", "third", "fourth"}
    assert len(test_cookies) == 4
    del test_cookies["first"]
    assert set

# Generated at 2022-06-14 07:03:48.452367
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    '''
    Method __delitem__ of class CookieJar test
    '''

    headers = starlette.datastructures.Headers()
    cookiejar = CookieJar(headers)
    cookiejar["company_name"] = "getpostman"
    assert headers.get("Set-Cookie")
    del cookiejar["company_name"]
    assert not headers.get("Set-Cookie")


# Generated at 2022-06-14 07:03:54.354504
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from mitmproxy import http
    h = http.HTTPHeaders(raw_headers=b"Set-Cookie: name=value\r\n")
    c = CookieJar(h)
    c['name'] = 'value'
    assert 'name' in c
    del c['name']
    assert 'name' not in c
test_CookieJar___delitem__()

# Generated at 2022-06-14 07:04:04.033592
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': '8',
        'Set-Cookie': 'cookie1=v1; HttpOnly; Path=/'
    }
    cookie_jar = CookieJar(headers)
    del cookie_jar['cookie1']
    assert 'cookie1' not in cookie_jar
    assert 'cookie1' not in cookie_jar.cookie_headers
    assert cookie_jar.headers.get_all('cookie1') == None
    

# Generated at 2022-06-14 07:04:04.366857
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    pass

# Generated at 2022-06-14 07:04:10.729987
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["foo"] = "bar"
    assert isinstance(cookie_jar["foo"], Cookie)
    assert headers.getall("Set-Cookie")[0] == "foo=bar"
    cookie_jar["foo"] = "baz"
    assert cookies["foo"].value == "baz"
    assert headers.getall("Set-Cookie")[0] == "foo=baz"
    cookie_jar["foo"] = "bar"
    assert headers.getall("Set-Cookie")[0] == "foo=bar"



# Generated at 2022-06-14 07:04:20.258960
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")
    assert str(c) == "name=value"

    c["path"] = "/"
    assert str(c) == "name=value; Path=/"

    c["httponly"] = True
    assert str(c) == "name=value; Path=/; HttpOnly"

    c["secure"] = True
    assert str(c) == "name=value; Path=/; Secure; HttpOnly"

    c["max-age"] = 12
    assert str(c) == "name=value; Path=/; Max-Age=12; Secure; HttpOnly"

    c["httponly"] = False
    assert str(c) == "name=value; Path=/; Max-Age=12; Secure"

    c["max-age"] = 0

# Generated at 2022-06-14 07:04:26.245891
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    C = CookieJar(headers)
    C["delete_cookie"] = "delete_me"
    assert headers["Set-Cookie"] == "delete_cookie=delete_me; Path=/; Version=0"
    del C["delete_cookie"]
    assert list(headers.items()) == []



# Generated at 2022-06-14 07:04:44.794709
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Test setup
    headers = MultiHeader()
    cookiejar = CookieJar(headers)
    cookiejar["foo"] = "bar"

    # Test execution
    del cookiejar["foo"]

    # Test setup
    cookiejar = CookieJar(headers)
    cookiejar["foo"] = "bar"
    headers.add("Set-Cookie", cookiejar["foo"])

    # Test execution
    del cookiejar["foo"]

    # Test setup
    cookiejar = CookieJar(headers)
    cookiejar["foo"] = "bar"
    headers.add("Set-Cookie", cookiejar["foo"])
    headers.add("Set-Cookie", "test1=value1")

    # Test execution
    del cookiejar["foo"]


    # Test setup
    cookiejar = CookieJar(headers)

# Generated at 2022-06-14 07:04:57.848313
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test", "value")
    cookie["max-age"] = 0
    assert cookie["max-age"] == 0
    try:
        cookie["test"] = ""
    except KeyError:
        assert True
    cookie["path"] = "/"
    assert cookie["path"] == "/"
    cookie["expires"] = "tomorrow"
    assert cookie["expires"] == "tomorrow"
    try:
        cookie["test"] = False
    except KeyError:
        assert True
    try:
        cookie["max-age"] = "test"
    except ValueError:
        assert True
    try:
        cookie["expires"] = now()
    except TypeError:
        assert True

# Generated at 2022-06-14 07:05:04.899628
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = { 'content-type': 'text/plain' }
    CookieJarObj = CookieJar(headers)
    CookieJarObj['key'] = 'value'
    assert('key' in CookieJarObj.cookie_headers)
    assert('Set-Cookie' in headers)
    assert('key' in headers['Set-Cookie'])
    assert('value' in headers['Set-Cookie']['key'])
    del CookieJarObj['key']
    assert('key' not in CookieJarObj.cookie_headers)
    assert('Set-Cookie' in headers)
    assert('key' in headers['Set-Cookie'])
    assert('max-age=0' in headers['Set-Cookie']['key'])


# Generated at 2022-06-14 07:05:11.454077
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = HeaderStore()
    cookies = CookieJar(headers)
    cookies["username"] = "admin"
    
    set_cookie_header = headers['Set-Cookie']
    assert set_cookie_header
    # We are assuming the cookie header value is "username=admin"
    assert 'username=admin' in set_cookie_header.value


# Generated at 2022-06-14 07:05:17.660230
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    testHeaders = {"Content-Type":"text/html"}
    testCookieJar = CookieJar(testHeaders)
    testCookieJar["myName"] = "myValue"
    result = "myValue"
    assert testCookieJar["myName"] == result, "Value is not myValue"
    del testCookieJar["myName"]
    result = ""
    assert testCookieJar["myName"] == result, "Value is not empty"


# Generated at 2022-06-14 07:05:20.851372
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('key', 'value')
    cookie['expires'] = datetime.now()
    assert isinstance(cookie['expires'], datetime)

# Generated at 2022-06-14 07:05:31.285953
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    h = {}
    c = CookieJar(h)
    c['a'] = 1
    c['b'] = 2
    c['c'] = 3
    c['d'] = 4

    assert(str(c['a']) == 'a=1; Path=/; Max-Age=0')
    assert(str(c['b']) == 'b=2; Path=/; Max-Age=0')
    assert(str(c['c']) == 'c=3; Path=/; Max-Age=0')
    assert(str(c['d']) == 'd=4; Path=/; Max-Age=0')


# Generated at 2022-06-14 07:05:36.307322
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    assert str(cookie) == 'foo=bar'

    cookie["max-age"] = 3600
    assert str(cookie) == 'foo=bar; Max-Age=3600'

    cookie["samesite"] = "strict"
    assert str(cookie) == 'foo=bar; Max-Age=3600; SameSite=strict'

# ------------------------------------------------------------ #
#  Decode
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:05:48.602471
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('a', 'b')
    with pytest.raises(KeyError):
        cookie['expires'] = []
    with pytest.raises(KeyError):
        cookie['path'] = []
    with pytest.raises(KeyError):
        cookie['comment'] = []
    with pytest.raises(KeyError):
        cookie['domain'] = []
    with pytest.raises(KeyError):
        cookie['max-age'] = []
    with pytest.raises(KeyError):
        cookie['secure'] = []
    with pytest.raises(KeyError):
        cookie['httponly'] = []
    with pytest.raises(KeyError):
        cookie['version'] = []
    with pytest.raises(KeyError):
        cookie['samesite'] = []

# Generated at 2022-06-14 07:06:03.322096
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    c = CookieJar(MultiHeader([]))
    c['id'] = '0'
    c['username'] = 'test'
    c['flag'] = '1'

    # normal case
    assert c['id'] == '0'
    del c['id']
    # assert that key is removed from c
    with pytest.raises(KeyError):
        assert c['id']
    # assert that id is removed from cookie headers
    assert 'id' not in c.cookie_headers
    # assert that id is removed from headers
    assert c.headers.get('Set-Cookie') == 'username=test; flag=1'
    # new case
    c['id'] = '0'
    # assert that id is added to cookie headers
    assert 'id' in c.cookie_headers
    # assert that id is added to headers

# Generated at 2022-06-14 07:06:31.136538
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Test the case that given the param is not in self.cookie_headers
    # This will NOT raise an exception
    cookieJar = CookieJar(headers = {})
    cookieJar['test_key'] = 'test_value'
    cookieJar.__delitem__('test_key')
    assert cookieJar == {}
    # Test the case that given the param is in self.cookie_headers
    # This will NOT raise an exception
    cookieJar = CookieJar(headers = {})
    cookieJar['test_key_1'] = 'test_value_1'
    cookieJar['test_key_2'] = 'test_value_2'
    cookieJar.__delitem__('test_key_1')
    assert cookieJar == {'test_key_2': 'test_value_2'}


# Generated at 2022-06-14 07:06:37.318878
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from starlette.responses import Response
    from starlette.testclient import TestClient
    from starlette_context.middleware import ContextMiddleware

    app = Starlette(debug=True)

    @app.route("/")
    def index(request: Request):
        request.cookies["some"] = "some"
        request.cookies["some"] = "somee"
        request.cookies["some"] = "someee"
        request.cookies["somee"] = "somee"
        request.cookies["someee"] = "someee"
        request.cookies["some2"] = "some2"
        request.cookies["some3"] = "some3"
        request.cookies["some4"] = "some4"
        return Response("OK")

    client = TestClient(app)


# Generated at 2022-06-14 07:06:47.079299
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    assert str(cookie) == 'foo="bar"'

    cookie = Cookie("mycookie", "myvalue")
    cookie['expires'] = datetime( 2024, 12, 12, 12, 12, 12)
    assert str(cookie) == 'mycookie="myvalue"; Expires=Thu, 12-Dec-2024 12:12:12 GMT'

    cookie = Cookie("a", "b")
    cookie["domain"] = "localhost"
    assert str(cookie) == 'a="b"; Domain=localhost'

    cookie = Cookie("c", "d")
    cookie["comment"] = "comment"
    assert str(cookie) == 'c="d"; Comment=comment'

    cookie = Cookie("e", "f")
    cookie["max-age"] = "100"

# Generated at 2022-06-14 07:06:54.638313
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookie_jar = CookieJar(headers)

    cookie_jar["name"] = "admin"
    assert headers.getall("Set-Cookie")[0].value == "name=admin"
    cookie = cookie_jar["name"]
    assert cookie.value == "admin"
    del cookie_jar["name"]
    assert cookie_jar.get("name") == None



# Generated at 2022-06-14 07:07:00.127426
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    header = MultiHeader()
    cookie = Cookie("a", "1")
    cookie_jar = CookieJar(header)

    cookie_jar["a"] = "1"
    assert cookie_jar["a"] == cookie

    cookie.value = "2"
    cookie_jar["a"] = "2"
    assert cookie_jar["a"] == cookie


# Generated at 2022-06-14 07:07:12.543560
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Arrange - Create a new CookieJar instance
    _headers = []
    cookie_jar = CookieJar(_headers)
    # Act - Invoke method on CookieJar instance
    cookie_jar['testKey'] = 'test'
    cookie_jar['testKey'] = 'test'
    del cookie_jar['testKey']
    # Assert - Examine results
    assert _headers == [
        'Set-Cookie: testKey=%22test%22; Path=%2F; Max-Age=0',
        'Set-Cookie: testKey=%22test%22; Path=%2F',
    ], 'Incorrect __delitem__ behavior'

# ------------------------------------------------------------ #
# ------------------------------------------------------------ #
# ------------------------------------------------------------ #