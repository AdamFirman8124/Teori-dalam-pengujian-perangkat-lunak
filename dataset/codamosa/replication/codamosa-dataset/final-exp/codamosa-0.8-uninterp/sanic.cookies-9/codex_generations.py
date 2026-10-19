

# Generated at 2022-06-14 06:57:33.845747
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test_key", "test_value")
    cookie["path"] = "/"
    cookie["httponly"] = True
    assert str(cookie) == "test_key=test_value; Path=/; HttpOnly"

    cookie = Cookie("test_key", "test_value")
    cookie["expires"] = datetime(2020, 4, 1, 17, 45, 59)
    assert str(cookie) == "test_key=test_value; expires=Wed, 01-Apr-2020 17:45:59 GMT"

    cookie = Cookie("test_key", "test_value")
    cookie["max-age"] = DEFAULT_MAX_AGE
    assert str(cookie) == "test_key=test_value; Max-Age=0"


# Generated at 2022-06-14 06:57:41.074987
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers({"Set-Cookie": ["name1=foo; path=/", "name2=bar; path=/"]})
    cookies = CookieJar(headers)
    assert cookies["name1"].value == "foo"
    assert cookies["name2"].value == "bar"

    del cookies["name1"]
    cookie_header = headers.items()[0]
    assert cookie_header[0] == "Set-Cookie"
    assert cookie_header[1] == "name2=bar; Path=/"



# Generated at 2022-06-14 06:57:49.973178
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    ck = Cookie('foo', 'bar')
    ck['path'] = '/'
    ck['comment'] = 'test'
    ck['secure'] = True
    print(ck)
    # ck['foo'] = 'bar'
    # ck['expires'] = '2020-01-01'
    # print(ck)
    # print(ck.value)
    # print(ck['comment'])
    # print(ck['path'])
    # print(ck['secure'])


# Generated at 2022-06-14 06:57:52.078404
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = {}
    CookieJar(headers)[0] = "one"
    return headers



# Generated at 2022-06-14 06:58:01.677330
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiDict()
    jar = CookieJar(headers)
    # When a key isn't present, it is added to the headers
    jar["test_key"] = "test_value"
    assert jar["test_key"].value == "test_value"
    assert jar.header_key in headers
    assert jar.header_key in jar.headers
    # When a key is present, it gets updated
    jar["test_key"].value = "test_value2"
    assert jar["test_key"].value == "test_value2"
    # Ensure multi-headers are supported
    jar["test_key2"] = "test_value2"
    assert jar.header_key in headers
    assert jar.header_key in jar.headers
    assert "test_key" in jar.headers[jar.header_key]


# Generated at 2022-06-14 06:58:12.934800
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    # Case 1: Cookie key contains illegal characters
    with pytest.raises(KeyError):
        Cookie(key=";", value=";")
    # Case 2: Unknown cookie property
    with pytest.raises(KeyError):
        Cookie(key=";", value=";")["name"] = "value"
    # Case 3: Cookie max-age is not an integer
    with pytest.raises(ValueError):
        Cookie(key="key", value="value")["max-age"] = "str"
    # Case 4: Cookie 'expires' property is not a datetime
    with pytest.raises(TypeError):
        Cookie(key="key", value="value")["expires"] = "str"
    # Case 5: Key is a reserved word

# Generated at 2022-06-14 06:58:24.680901
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import pytest
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"
    obj = Cookie('a', 'b')
    assert str(obj) == "a=b"

# Generated at 2022-06-14 06:58:36.806435
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("key", "value")
    c["httponly"] = True
    assert str(c) == "key=value; HttpOnly"

    c["secure"] = True
    assert str(c) == "key=value; HttpOnly; Secure"

    c["max-age"] = "100"
    assert str(c) == "key=value; Max-Age=100; HttpOnly; Secure"

    c["expires"] = datetime(2018, 3, 14, 17, 30, 58)
    assert (
        str(c)
        == "key=value; expires=Wed, 14-Mar-2018 17:30:58 GMT; Max-Age=100; HttpOnly; Secure"
    )

    c["expires"] = datetime(2018, 3, 14, 17, 30, 58)

# Generated at 2022-06-14 06:58:40.211880
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    cookies["foo"] = "bar"
    cookies.__delitem__("foo")
    del cookies["foo"]


# Generated at 2022-06-14 06:58:48.818437
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    key_1 = "key_1"
    key_2 = "key_2"
    value_1 = "value_1"
    value_2 = "value_2"
    cookies[key_1] = value_1
    cookies[key_2] = value_2
    assert cookies[key_1] == value_1
    assert key_1 in cookies.keys()
    assert key_2 in cookies.keys()


# Generated at 2022-06-14 06:59:00.019225
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    expected = "name=value"
    result = str(cookie)
    assert result == expected



# Generated at 2022-06-14 06:59:03.839124
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("myname", "myvalue")
    print(cookie)
    assert str(cookie) == "myname=myvalue"

# ------------------------------------------------------------ #
#  Middleware
# ------------------------------------------------------------ #



# Generated at 2022-06-14 06:59:10.567964
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie()
    for k,v in {"expires": "expires","path": "Path","comment": "Comment","domain": "Domain","max-age": "Max-Age","secure": "Secure","httponly": "HttpOnly","version": "Version","samesite": "SameSite"}.items():
        c[k] = v
        assert c[k] == v


# Generated at 2022-06-14 06:59:23.294942
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('hello', 'world')
    c['max-age'] = 55
    c['domain'] = '.test.com'
    assert str(c) == "hello=world; Max-Age=55; Domain=.test.com"
    # Validating that the default values are used
    del c['max-age']
    c['expires'] = datetime.now()
    c['secure'] = True
    c['comment'] = "hello world"
    c['version'] = 1
    c['httponly'] = True
    assert str(c) == "hello=world; Expires=%s; Comment=hello world; Version=1; Secure; HttpOnly" % c['expires'].strftime("%a, %d-%b-%Y %T GMT")



# Generated at 2022-06-14 06:59:35.109014
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    cookie["expires"] = datetime(2017, 8, 3, 11, 34, 59)
    cookie["path"] = "/"
    cookie["comment"] = "This is a test!"
    cookie["domain"] = "example.com"
    cookie["max-age"] = DEFAULT_MAX_AGE
    cookie["secure"] = True
    cookie["httponly"] = False
    cookie["version"] = 1
    cookie["samesite"] = "Strict"
    assert str(cookie) == "name=value; expires=Thu, 03-Aug-2017 11:34:59 GMT; " \
                          "Path=/; Comment=This is a test!; Domain=example.com; " \
                          "Max-Age=0; Secure; Version=1; SameSite=Strict"

# Generated at 2022-06-14 06:59:46.221861
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    
    cookie_jar["y"] = "y"
    cookie_jar["z"] = "z"
    assert cookie_jar["y"] == "y"
    assert cookie_jar["z"] == "z"
    assert headers == {"Set-Cookie": ["y=y", "z=z"]}
    
    # delete existent cookie
    del cookie_jar["y"]
    assert cookie_jar.get("y") is None
    assert headers == {"Set-Cookie": ["z=z"]}
    
    # delete non-existent cookie
    del cookie_jar["x"]
    assert cookie_jar.get("x") is None
    # nothing should change
    assert headers == {"Set-Cookie": ["z=z"]}

    # delete second

# Generated at 2022-06-14 06:59:59.650567
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    testCookie = Cookie("Test", "Cookie")
    testCookie["max-age"] = "500"
    assert str(testCookie) == "Test=Cookie; Max-Age=500"

    testCookie["max-age"] = 500
    assert str(testCookie) == "Test=Cookie; Max-Age=500"

    testCookie = Cookie("Test", "Cookie")
    testCookie["path"] = "/test"
    assert str(testCookie) == "Test=Cookie; Path=/test"

    testCookie = Cookie("Test", "Cookie")
    testCookie["secure"] = True
    assert str(testCookie) == "Test=Cookie; Secure"

    testCookie = Cookie("Test", "Cookie")

# Generated at 2022-06-14 07:00:10.073995
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    import http.cookies
    cookie = CookieJar(http.cookies.SimpleCookie())
    cookie["foo"] = "bar"
    del cookie["foo"]
    cookie = CookieJar(http.cookies.SimpleCookie())
    cookie["foo"] = "bar"
    cookie.headers["Set-Cookie"] = 'foo="bar"; Path=/; Max-Age=3600'
    del cookie["foo"]
    cookie = CookieJar(http.cookies.SimpleCookie())
    cookie["foo"] = "bar"
    cookie.headers["Set-Cookie"] = 'foo="bar"; Path=/; Max-Age=3600'
    cookie.headers["Set-Cookie"] = 'test="test"; Path=/; Max-Age=3600'
    del cookie["foo"]

# Generated at 2022-06-14 07:00:17.771746
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers(CASE_INSENSITIVE_HEADERS)

    cookie_jar = CookieJar(headers)

    cookie_jar['test-cookie-jar'] = 'test-value'
    cookie_jar['test-cookie-jar-1'] = 'test-value'

    assert(2 == len(cookie_jar.keys()))

    del cookie_jar['test-cookie-jar']

    assert(len(cookie_jar.keys()) == 1)



# Generated at 2022-06-14 07:00:31.666747
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():

    c = Cookie("a", "b")
    c["httponly"] = True
    assert c["httponly"] == True
    c["secure"] = True
    assert c["secure"] == True
    c["samesite"] = "strict"
    assert c["samesite"] == "strict"
    # Below will raise KeyError as the key is not recognized
    try:
        c["not a real key"] = False
        assert False
    except KeyError:
        assert True
    # Below will raise ValueError as the key is not an integer
    try:
        c["max-age"] = "this is not an integer"
        assert False
    except ValueError:
        assert True
    # Below will raise TypeError as the key is not a datetime

# Generated at 2022-06-14 07:00:45.442592
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    jar["test"] = "test"
    assert headers["set-cookie"] == ["test=test; Path=/"]
    del jar["test"]
    assert headers["set-cookie"] == ["test=; Max-Age=0; Path=/"]
    headers = Headers()
    jar = CookieJar(headers)
    jar["test"] = "test"
    assert headers["set-cookie"] == ["test=test; Path=/"]
    jar["test"] = ""
    assert headers["set-cookie"] == ["test=; Max-Age=0; Path=/"]

# Generated at 2022-06-14 07:00:53.682129
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from starlette.requests import Request
    from starlette.responses import Response

    request = Request(None, None)
    response = Response(None, None)

    cookie = CookieJar(response.set_cookie)
    cookie["hello"] = "world"
    cookie["a"] = "b"

    assert response.headers == {'Set-Cookie': [{
        'Content-Type': 'application/json',
        'max-age': 0,
        'expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
        'path': '/'
    }, {
        'Content-Type': 'application/json',
        'max-age': 0,
        'expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
        'path': '/'
    }]}

    del cookie["a"]
   

# Generated at 2022-06-14 07:01:07.978220
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('test', '1')
    # test properties:
    cookie["comment"] = 'comment'
    cookie["domain"] = 'domain'
    cookie["max-age"] = 10
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = '1'
    cookie["samesite"] = 'lax'
    cookie["expires"] = datetime.fromisoformat('2020-10-25T12:34:56')
    # test __str__:
    assert str(cookie) == (
        "test=1; comment=comment; domain=domain; max-age=10; secure; httponly;" +
        " version=1; samesite=lax; expires=Sun, 25-Oct-2020 12:34:56 GMT")


# ------------------------------------------------------------ #
#  SimpleC

# Generated at 2022-06-14 07:01:21.130362
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    input_value = 'X-Test'
    input_value2 = '"Test"'
    input_value3 = 'This is a test'
    input_valu4 = 'This is/a test'
    input_valu4 = 'This is/a test'
    cookie = Cookie(input_value, input_value2)
    cookie2 = Cookie(input_value, input_value3)
    cookie3 = Cookie(input_value, input_valu4)
    cookie4 = Cookie(input_value, input_value3)
    cookie4["path"] = "/"
    cookie4["comment"] = "This is a comment"
    cookie4["domain"] = "domain.com"
    cookie4["max-age"] = 3600
    cookie4["expires"] = datetime(2018, 1, 1, 0, 0)

# Generated at 2022-06-14 07:01:26.585037
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headerDict = {'Set-Cookie': ['key1=value1; Path=/; HttpOnly; SameSite=Strict; Secure',
                              'key2=value2; Path=/; HttpOnly; SameSite=Strict; Secure']}
    result = CookieJar(headerDict)
    del result['key1']
    assert result == {'key2': Cookie(key='key2', value='value2')}


# Generated at 2022-06-14 07:01:39.408149
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers: Dict[str, str] = {}
    jar = CookieJar(headers)
    jar["key"] = "value1"

    # assert that the removal of the key 'key' removes the key-value pair
    # associated with the given key
    del jar["key"]
    assert jar.get("key") is None

    # assert that the Max-Age property of the cookie is set to 0 (i.e.
    # the cookie expires).
    assert headers.get("Set-Cookie") == "key=; Max-Age=0"

    # Test case where key 'key2' is NOT present in the cookiejar
    del jar["key2"]

    assert headers.get("Set-Cookie") == "key2=; Max-Age=0"

    # Test case where cookie has multiple key-value pairs
    jar["key3"]

# Generated at 2022-06-14 07:01:47.600642
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    jar["foo"] = "bar"
    assert jar.headers[0].value == "foo=bar; Path=/; Max-Age=0"
    assert jar.headers[1].value == "foo=; Path=/; Max-Age=0"
    jar.__delitem__("foo")
    assert jar.headers.to_list() == []
    assert jar.cookie_headers == {}



# Generated at 2022-06-14 07:01:53.116656
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = 'TestKey'
    value = 'TestValue'
    cookie = Cookie(key, value)
    cookie["path"] = "/"
    assert str(cookie) == "%s=%s; path=/" % (key, value)


# ------------------------------------------------------------ #
#  Response.
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:02:04.047632
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Test the regular cases.
    cookie = Cookie(key="key", value="value")
    assert str(cookie) == "key=value"
    cookie["path"] = "/"
    assert str(cookie) == "key=value; Path=/; SameSite=Lax"
    cookie["comment"] = "test"
    assert str(cookie) == "key=value; Path=/; Comment=test; SameSite=Lax"
    cookie["domain"] = "test.com"
    assert (
        str(cookie) == "key=value; Path=/; Comment=test; Domain=test.com; SameSite=Lax"
    )
    cookie["max-age"] = 3600

# Generated at 2022-06-14 07:02:13.769961
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test-key", "test-value")
    cookie["path"] = "/"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["samesite"] = "strict"
    cookie["expires"] = datetime(2020, 5, 23, 16, 25, 21)
    cookie["max-age"] = 3600
    assert str(cookie) == "test-key=test-value; Path=/; Secure; HttpOnly; SameSite=strict; expires=Sat, 23-May-2020 16:25:21 GMT; Max-Age=3600"

# Generated at 2022-06-14 07:02:24.903011
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    CookieJar.add(headers, "user", "vjpy")
    assert 'Set-Cookie' in headers
    CookieJar.remove(headers, 'user')
    assert "Set-Cookie" not in headers
    CookieJar.add(headers, "user", "vjpy")
    CookieJar.remove(headers, "user")
    assert "Set-Cookie" not in headers

# Generated at 2022-06-14 07:02:30.552414
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Unit test for method __str__ of class Cookie
    """
    cookie = Cookie('cookie_name', 'cookie_value')
    assert str(cookie) == 'cookie_name=cookie_value'

    cookie["path"] = "/"
    cookie["max-age"] = DEFAULT_MAX_AGE
    assert str(cookie) == 'cookie_name=cookie_value; expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/; Max-Age=0'

# Generated at 2022-06-14 07:02:38.142947
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Initialization of a Cookie
    cookie = Cookie("cookie-name", "cookie-value")
    cookie["expires"] = datetime(2020, 2, 10, 2, 0, 0)
    cookie["max-age"] = 60
    cookie["path"] = "/"
    cookie["comment"] = "cookie-comment"
    cookie["domain"] = "cookie-domain"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 1
    str_cookie = str(cookie)
    assert (
        str_cookie
        == 'cookie-name=cookie-value; Expires=Mon, 10-Feb-2020 02:00:00 GMT; Max-Age=60; Path=/; Comment=cookie-comment; Domain=cookie-domain; Secure; HttpOnly; Version=1'
    )

# Generated at 2022-06-14 07:02:47.881544
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Create a sample Cookie class and then populate it with some valid data
    sample_cookie = Cookie("key", "value")
    sample_cookie["domain"] = "example.com"
    sample_cookie["expires"] = datetime(2018, 7, 18, 23, 59, 59)
    sample_cookie["path"] = "/path/"
    sample_cookie["max-age"] = 3600
    sample_cookie["secure"] = True
    sample_cookie["httponly"] = False

    # Test method
    assert (str(sample_cookie) ==
        'key=value; Domain=example.com; expires=Fri, 18-Jul-2018 23:59:59 GMT; Path=/path/; Max-Age=3600; Secure; HttpOnly'
    )

# Generated at 2022-06-14 07:02:58.426399
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers: Dict[str, str] = {}
    cookie_jar = CookieJar(headers)

    assert (len(cookie_jar.keys()) == 0)
    cookie_jar["someKey"] = "someValue"
    assert (len(cookie_jar.keys()) == 1)
    cookie_jar.__delitem__("someKey")
    assert (len(cookie_jar.keys()) == 0)


    try:
        cookie_jar.__delitem__("aNonExistingKey")
    except KeyError:
        pass
    else:
        raise Exception("Wrong exception was thrown.")



# Generated at 2022-06-14 07:03:04.899153
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie('age', '18')
    c['max-age'] = 123
    assert c['max-age'] == 123
    c['domain'] = 'testbird.com'
    assert c['domain'] == 'testbird.com'
    c['secure'] = True
    assert c['secure'] == True
    c['httponly'] = True
    assert c['httponly'] == True


# Generated at 2022-06-14 07:03:10.906723
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

    cookie["httponly"] = True
    assert str(cookie) == "key=value; HttpOnly"

    cookie["secure"] = True
    assert str(cookie) == "key=value; HttpOnly; Secure"

    cookie["path"] = "/"
    assert str(cookie) == "key=value; Path=/; HttpOnly; Secure"

    cookie["expires"] = datetime(year=2020, month=1, day=1)
    assert str(cookie) == "key=value; Expires=Wed, 01-Jan-2020 00:00:00 GMT; Path=/; HttpOnly; Secure"

    cookie["max-age"] = DEFAULT_MAX_AGE

# Generated at 2022-06-14 07:03:20.496784
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    headers.add("Set-Cookie", Cookie("cookie1", "value1"))
    headers.add("Set-Cookie", Cookie("cookie2", "value2"))
    headers.add("Set-Cookie", Cookie("cookie3", "value3"))
    jar = CookieJar(headers)
    jar.__delitem__("cookie1")
    jar.__delitem__("cookie2")
    del jar["cookie3"]

    assert len(jar) == 0
    assert len(jar.cookie_headers) == 0
    assert "Set-Cookie" not in headers


# Generated at 2022-06-14 07:03:30.311240
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar(MultiDict())
    assert cookie_jar.headers == {}
    assert cookie_jar.cookie_headers == {}
    cookie_jar['name'] = 'value'
    assert cookie_jar.cookie_headers == {'name': 'cookie'}
    assert cookie_jar.headers == {'cookie': ['name=value']}
    del cookie_jar['name']
    assert cookie_jar.cookie_headers == {}
    assert cookie_jar.headers == {'cookie': ['name=; max-age=0']}

# Generated at 2022-06-14 07:03:40.468382
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("a", "b")
    # invalid max-age
    c["max-age"] = "abc"
    assert str(c) == "a=b"
    # valid max-age
    c["max-age"] = 123
    assert str(c) == "a=b; Max-Age=123"
    # valid expires
    c["expires"] = datetime.fromtimestamp(0)
    assert str(c) == "a=b; Max-Age=123; expires=Thu, 01-Jan-1970 00:00:00 GMT"
    # valid path
    c["path"] = "/"
    assert str(c) == "a=b; Max-Age=123; expires=Thu, 01-Jan-1970 00:00:00 GMT; Path=/"
    # valid secure

# Generated at 2022-06-14 07:03:56.813843
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # arrange
    name = "user_id"
    value = "1234"
    cookie = Cookie(name, value)
    cookie["path"] = "/"
    cookie["max-age"] = 0
    cookie["domain"] = "localhost"
    cookie["expires"] = datetime(2020, 10, 10, 10, 10, 10)
    cookie['samesite'] = 'None'

    cookie2 = Cookie(name, value)

    # act
    actual1 = cookie.__str__()
    actual2 = cookie2.__str__()

    # assert
    assert actual1 == (
        "user_id=1234; Path=/; Domain=localhost; Max-Age=0; "
        "Expires=Fri, 10-Oct-2020 10:10:10 GMT; SameSite=None"
    )
    assert actual

# Generated at 2022-06-14 07:04:01.571617
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers([])
    headers["Foo"] = "Bar"
    cookie_headers = CookieJar(headers)
    cookie_headers["Foo"] = "Bar"
    del cookie_headers["Foo"]
    assert cookie_headers.get("Foo") is None
    assert cookie_headers.headers.get("Set-Cookie") is None


# Generated at 2022-06-14 07:04:10.861666
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    test_dict = {
        "expires": datetime.now(),
        "path": "test_path",
        "comment": "test_comment",
        "domain": "test_domain",
        "max-age": "test_max_age",
        "secure": True,
        "httponly": False,
        "version": "test_version",
        "samesite": "test_samesite"
    }
    result = []
    expected = []
    cookie = Cookie("test_key", "test_value")
    result.append(str(cookie))
    expected.append("%s=%s" % ("test_key", "test_value"))
    for key in test_dict:
        cookie[key] = test_dict[key]
        result.append(str(cookie))

# Generated at 2022-06-14 07:04:23.018823
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # create an instance of Cookie

    c = Cookie('test', 'test_value')
    output = "%s=%s" % (c.key, _quote(c.value))
    assert output == str(c)

    # update value of key "test"

    c.value = 'new_value'
    output = "%s=%s" % (c.key, _quote(c.value))
    assert output == str(c)

    # update an existing key

    c['test'] = 'test_key'
    output = "%s=%s" % (c.key, _quote(c.value))
    assert output == str(c)

    # add a new key

    c['new_key'] = 'new_value'

# Generated at 2022-06-14 07:04:32.078184
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = defaultdict(list)
    cookies = CookieJar(headers)
    cookies["a"] = "a"
    cookies["b"] = "b"
    assert "a" in cookies
    assert "b" in cookies
    assert len(cookies) == 2
    assert cookies["a"] == "a"
    assert cookies["b"] == "b"
    del cookies["a"]
    assert "a" not in cookies
    assert "b" in cookies
    assert len(cookies) == 1
    assert cookies["b"] == "b"
    cookies["a"] = "a"
    assert "a" in cookies
    assert "b" in cookies
    assert len(cookies) == 2
    assert cookies["a"] == "a"
    assert cookies["b"] == "b"
    cookies["a"] = "aa"


# Generated at 2022-06-14 07:04:42.897354
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = [("Set-Cookie", "a=1")]
    #print("In test_CookieJar___delitem__")
    cookies = CookieJar(headers)
    #print("cookies are", cookies)
    print(cookies.headers)
    cookies["a"] = "3"
    print("cookies are", cookies)
    del cookies["a"]
    print("cookies are", cookies)
    print(cookies.headers)
    try:
        del cookies["a"]
    except KeyError:
        print("Key Error")
    #except Exception as e:
    #    print("Error is ", e)
test_CookieJar___delitem__()


# Generated at 2022-06-14 07:04:54.898937
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class Headers:
        def __init__(self):
            self.content: dict = dict()

        def add(self, key, value):
            self.content[key] = value

        def popall(self, key):
            return self.content[key]

    class Cookie:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __setitem__(self, key, value):
            return None

        def __str__(self):
            return self.value

    headers = Headers()
    cookie_jar = CookieJar(headers)
    cookie_jar["test_key_1"] = "test_value_1"
    cookie_jar["test_key_2"] = "test_value_2"
    cookie_jar["test_key_3"]

# Generated at 2022-06-14 07:05:00.099291
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():

    from rivr_restful.http import Headers

    jar = CookieJar(Headers())
    jar['foo'] = 'bar'

    assert len(jar) == 1
    assert 'foo' in jar

    del jar['foo']

    assert len(jar) == 0
    assert 'foo' not in jar

# Generated at 2022-06-14 07:05:04.177210
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()

    cookies = CookieJar(headers)
    cookies["foo"] = "bar"

    assert "foo" in cookies
    assert "foo" in cookies.cookie_headers
    assert "Set-Cookie" in headers

    del cookies["foo"]

    assert "foo" not in cookies
    assert "foo" not in cookies.cookie_headers
    assert "Set-Cookie" not in headers

# Generated at 2022-06-14 07:05:17.467158
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    cookie["expires"] = datetime(year=2050, day=22, month=2, hour=22)
    cookie["path"] = "/"
    cookie["domain"] = "localhost"
    cookie["comment"] = "this is a comment"
    cookie["max-age"] = 1
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = True
    cookie["samesite"] = True
    output = (
        "key=value; expires=Mon, 22-Feb-2050 22:00:00 GMT; "
        "Path=/; Domain=localhost; Comment=this is a comment; "
        "Max-Age=1; Secure; HttpOnly; Version; SameSite"
    )
    assert str(cookie) == output

# Generated at 2022-06-14 07:05:31.827027
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader({"Set-Cookie": "test1=value1;Path=/"})
    cookies = CookieJar(headers)
    del cookies["test1"]
    assert headers["Set-Cookie"] == "test1=value1;Path=/"
    assert not cookies
    headers = MultiHeader({"Set-Cookie": "test1=value1;Path=/;HttpOnly"})
    cookies = CookieJar(headers)
    del cookies["test1"]
    assert headers["Set-Cookie"] == "test1=value1;Path=/"
    assert not cookies
    headers = MultiHeader(
        {
            "Set-Cookie": [
                "test1=value1;Path=/;HttpOnly",
                "test2=value2;Path=/;HttpOnly",
            ]
        }
    )
    cookies = Cookie

# Generated at 2022-06-14 07:05:38.832599
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    obj = Cookie("a", "b")
    assert str(obj) == "a=b"

    obj["Path"] = "/"
    assert str(obj) == "a=b; Path=/"

    obj["secure"] = True
    assert str(obj) == "a=b; Path=//; Secure"

    obj["max-age"] = 123
    assert str(obj) == "a=b; Path=//; Secure; Max-Age=123"



# Generated at 2022-06-14 07:05:51.506742
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from quart.serving.headers import Headers
    headers = Headers()
    cj = CookieJar(headers)
    cj['foo'] = 'bar'
    assert 'foo' in cj
    assert cj['foo'].value == 'bar'
    assert str(cj['foo']) == 'foo=bar; Path=/'
    assert headers.get_list('Set-Cookie') == ['foo=bar; Path=/']
    # Test overwrite
    cj['foo'] = 'baz'
    assert 'foo' in cj
    assert cj['foo'].value == 'baz'
    assert str(cj['foo']) == 'foo=baz; Path=/'
    assert headers.get_list('Set-Cookie') == ['foo=baz; Path=/']


# Generated at 2022-06-14 07:06:04.513065
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("a", "b")
    assert c.__str__() == "a=b"
    c["max-age"] = 25
    assert c.__str__() == "a=b; Max-Age=25"
    c["expires"] = datetime.now()
    assert c.__str__().startswith("a=b; Max-Age=25; Expires=")
    c["secure"] = True
    assert c.__str__().startswith("a=b; Max-Age=25; Expires=; Secure")
    c["httponly"] = False
    assert c.__str__().startswith("a=b; Max-Age=25; Expires=; Secure")

# Generated at 2022-06-14 07:06:13.434275
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    mock_headers = mock.create_autospec(HeaderStore)
    jar = CookieJar(headers=mock_headers)
    jar["cookie_foo"] = "bar"
    jar["cookie_bar"] = "foo"
    jar["cookie_dup"] = "foo"
    jar["cookie_dup"] = "bar"
    assert len(mock_headers.getlist.return_value) == 3
    jar.__delitem__("cookie_foo")
    assert len(mock_headers.getlist.return_value) == 2
    jar.__delitem__("asdf")
    assert len(mock_headers.getlist.return_value) == 2
    mock_headers.getlist.assert_called_with("Set-Cookie")



# Generated at 2022-06-14 07:06:22.445878
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = dict()
    cookie_jar = CookieJar(headers)
    cookie_jar["name"] = "username"
    cookie_jar["pwd"] = "password"
    cookie_jar["url"] = "https://127.0.0.1"
    # Test if __delitem__ returns None and remove an cookie
    assert cookie_jar.__delitem__("pwd") is None
    # Test if the cookie is removed
    assert cookie_jar.__contains__("pwd") == False

# Generated at 2022-06-14 07:06:26.953709
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookie = CookieJar(headers)
    assert headers == {}
    cookie["foo"] = "bar"
    assert headers == {"Set-Cookie": "foo=bar; Path=/"}
    assert cookie == {"foo": "bar"}
    del cookie["foo"]
    assert headers == {}
    assert cookie == {}

# Generated at 2022-06-14 07:06:35.054145
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    obj_test_Cookie___str__ = Cookie('test_Cookie___str__', 'test_Cookie___str__')
    obj_test_Cookie___str__['secure'] = 1
    obj_test_Cookie___str__['httponly'] = 0
    obj_test_Cookie___str__['version'] = 1
    obj_test_Cookie___str__['samesite'] = 'Lax'
    obj_test_Cookie___str__['expires'] = datetime.now()
    obj_test_Cookie___str__['max-age'] = 0
    obj_test_Cookie___str__['path'] = str(datetime.now())
    obj_test_Cookie___str__['comment'] = str(datetime.now())
    obj_test_Cookie___str__['domain'] = str

# Generated at 2022-06-14 07:06:46.163031
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = HTTPHeaderMap()
    jar = CookieJar(headers)
    # Adding a cookie to jar.
    jar["test_CookieJar___delitem__"] = "test_CookieJar___delitem__"
    assert jar.cookie_headers["test_CookieJar___delitem__"]
    assert jar["test_CookieJar___delitem__"]
    # Deleting the cookie from jar.
    del jar["test_CookieJar___delitem__"]
    assert not jar.cookie_headers["test_CookieJar___delitem__"]
    assert not jar["test_CookieJar___delitem__"]
    # Deleting a cookie that never existed
    del jar["test_CookieJar___delitem__"]
    assert not jar.cookie_headers["test_CookieJar___delitem__"]

# Generated at 2022-06-14 07:06:58.785877
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test_cookie", "test_value")
    assert (
        str(cookie) == "test_cookie=test_value"
    ), "output was:" + str(cookie) + " instead of expected 'test_cookie=test_value"
    cookie["secure"] = True
    assert (
        str(cookie) == "test_cookie=test_value; Secure"
    ), "output was:" + str(cookie) + " instead of expected 'test_cookie=test_value; Secure'"
    cookie["path"] = "/somepath"
    assert (
        str(cookie) == "test_cookie=test_value; Path=/somepath; Secure"
    ), "output was:" + str(cookie) + " instead of expected 'test_cookie=test_value; Path=/somepath; Secure'"

# Generated at 2022-06-14 07:07:14.116501
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("foo", "bar")
    assert c.__str__() == "foo=bar"

    c["Path"] = "/"
    assert c.__str__() == "foo=bar; Path=/";
    c["Path"] = "/bar"
    assert c.__str__() == "foo=bar; Path=/bar"
    c["Secure"] = True
    assert c.__str__() == "foo=bar; Path=/bar; Secure"

    c["max-age"] = 100
    assert c.__str__() == "foo=bar; Path=/bar; Secure; max-age=100"
    c["max-age"] = -1
    assert c.__str__() == "foo=bar; Path=/bar; Secure; max-age=0"


# Generated at 2022-06-14 07:07:27.320169
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime

    c = Cookie("c", "v")
    assert c.__str__() == "c=v"
    c["path"] = "/"
    assert c.__str__() == "c=v; Path=/; Version=1"
    c["max-age"] = 3600
    assert c.__str__() == "c=v; Path=/; Max-Age=3600; Version=1"
    c["expires"] = datetime(2019, 12, 5, 17, 0, 0)
    assert c.__str__() == "c=v; Path=/; Max-Age=3600; Expires=Thu, 05-Dec-2019 17:00:00 GMT; Version=1"
    c = Cookie("cöökie", "valuë")