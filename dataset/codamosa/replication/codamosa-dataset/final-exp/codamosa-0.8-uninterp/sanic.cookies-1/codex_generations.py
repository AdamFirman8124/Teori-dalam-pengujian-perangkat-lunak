

# Generated at 2022-06-14 06:57:36.415825
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")
    assert str(c) == "name=value"
    c["path"] = "/"
    assert str(c) == "name=value; Path=/".replace(" ", "")
    c["comment"] = "my comment"
    assert str(c) == "name=value; Path=/; Comment=mycomment".replace(" ", "")

    c["secure"] = True
    assert str(c) == (
        "name=value; Path=/; Comment=mycomment; Secure"
    ).replace(" ", "")

    c["httponly"] = True
    assert str(c) == (
        "name=value; Path=/; Comment=mycomment; Secure; HttpOnly"
    ).replace(" ", "")

    c["version"] = 1

# Generated at 2022-06-14 06:57:41.075236
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key","value")
    cookie["path"] = "/"
    assert cookie["path"] == "/"
    cookie["max-age"] = 1
    assert cookie["max-age"] == 1

# Generated at 2022-06-14 06:57:52.974752
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("cookie_key", "cookie_value")
    # Test key not in self._keys
    assert_raises(KeyError, cookie.__setitem__, "not_in_self._keys", "not_in_self._keys_value")
    # Test cookie max-age not integer
    assert_raises(ValueError, cookie.__setitem__, "max-age", "not_integer")
    # Test cookie expires not datetime
    assert_raises(TypeError, cookie.__setitem__, "expires", "not_datetime")
    # Test cookie samesite not str
    assert_raises(TypeError, cookie.__setitem__, "samesite", 100)



# Generated at 2022-06-14 06:58:00.213410
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers([])
    cookie_jar = CookieJar(headers)
    cookie_jar["foo"] = "bar"
    header_value = headers.get("Set-Cookie")
    assert "foo=bar" in header_value
    assert "expires=" in header_value
    cookie_jar["foo2"] = "bar2"
    assert "foo2=bar2" in headers.get("Set-Cookie")


# Generated at 2022-06-14 06:58:02.920067
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie(key="cname", value="cvalue")
    c["max-age"] = DEFAULT_MAX_AGE
    c["samesite"] = "Lax"

    print(str(c))

# Generated at 2022-06-14 06:58:10.912744
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cookie_jar = CookieJar(headers)
    cookie_jar["key1"] = "value1"

    del cookie_jar["key1"]
    assert "key1" not in cookie_jar.cookie_headers
    assert "key1" not in headers
    assert cookie_jar["key1"] == ""

    # TODO: verify that the header is not set for the second case
    del cookie_jar["key2"]


# Generated at 2022-06-14 06:58:24.681853
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    compare = "name=value"

    # Default value of this
    assert str(cookie) == compare

    # Add max-age
    cookie["max-age"] = 10
    compare = "name=value; Max-Age=10"
    assert str(cookie) == compare

    # Add expires
    d = datetime(2018, 11, 17, 10, 20, 30)
    cookie["expires"] = d
    compare = "name=value; Max-Age=10; expires=Sat, 17-Nov-2018 10:20:30 GMT"
    assert str(cookie) == compare

    # Add secure
    cookie["secure"] = True
    compare = "name=value; Max-Age=10; expires=Sat, 17-Nov-2018 10:20:30 GMT; Secure"
    assert str

# Generated at 2022-06-14 06:58:30.778868
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    cookies["test"] = "test"
    assert headers["Set-Cookie"] == "test=test; Path=/", "Cookie was not added to header"
    del cookies["test"]
    assert not "Set-Cookie" in headers,"Cookie was not removed from header"


# Generated at 2022-06-14 06:58:38.402768
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie('foo', 'bar')
    c['path'] = '/'
    c['secure'] = True
    c['httponly'] = True
    c['domain'] = 'httpbin.org'
    c['version'] = 1
    c['samesite'] = 'Lax'
    c['max-age'] = '3600'
    c['expires'] = datetime.now()
    print(c)

# Generated at 2022-06-14 06:58:41.012657
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    result = CookieJar().__delitem__("cookie_name")
    assert(type(result) is type(None))


# Generated at 2022-06-14 06:58:58.726611
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    header = MultiHeaders()
    cookie_jar = CookieJar(header)
    # Test removing a key that doesn't exist
    cookie_jar["test"] = "test"
    cookie_jar["test2"] = "test2"
    del cookie_jar["test"]
    del cookie_jar["test2"]
    assert not cookie_jar.headers["Set-Cookie"]

# Generated at 2022-06-14 06:59:11.030203
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookiejar = CookieJar(headers)
    cookie1 = Cookie("TestCookie1", "testcookie1")
    cookie2 = Cookie("TestCookie2", "testcookie2")
    cookie3 = Cookie("TestCookie3", "testcookie3")
    cookie4 = Cookie("TestCookie4", "testcookie4")
    cookiejar[cookie1.key] = cookie1
    cookiejar[cookie2.key] = cookie2
    cookiejar[cookie3.key] = cookie3
    cookiejar[cookie4.key] = cookie4
    # case 1: key not in cookiejar.cookie_headers
    cookiejar.__delitem__("TestCookie5")
    assert cookie1.key in cookiejar.cookie_headers
    assert cookie2.key in cookiejar.cookie_headers
    assert cookie3

# Generated at 2022-06-14 06:59:20.886305
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    set_cookie_header_list = []
    headers = MultiHeader(set_cookie_header_list)
    cookiejar = CookieJar(headers)
    cookie_key = "foo"
    cookie_value = "bar"
    cookiejar[cookie_key] = cookie_value

    assert cookiejar.get(cookie_key) != None
    assert set_cookie_header_list != []

    del cookiejar[cookie_key]

    assert cookiejar.get(cookie_key) == None
    assert set_cookie_header_list != []

test_CookieJar___delitem__()

# Generated at 2022-06-14 06:59:34.218573
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    import time
    headers = MultiDict()
    cj = CookieJar(headers)
    # Set a new cookie
    cj["test"] = "foo"
    # Set an existing cookie
    cj["test"] = "bar"
    assert len(headers[cj.header_key]) == 1
    assert len(cj.cookie_headers) == 1
    assert cj["test"].value == "bar"
    # Delete the cookie
    del cj["test"]
    assert cj.get("test") == None
    assert cj.cookie_headers.get("test") == None
    assert len(headers[cj.header_key]) == 1
    assert isinstance(headers.get(cj.header_key), str)

# Generated at 2022-06-14 06:59:39.805937
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar(MultiHeader())
    cookie_jar["some_key"] = "some_value"
    del cookie_jar["some_key"]
    assert "some_key" not in cookie_jar
    assert cookie_jar.headers.get("Set-Cookie") is None
    return True

# Generated at 2022-06-14 06:59:52.122604
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"
    cookie["expires"] = datetime(year=2019, month=11, day=11)
    assert str(cookie) == "key=value; Expires=Mon, 11-Nov-2019 00:00:00 GMT"
    cookie["max-age"] = 123
    assert str(cookie) == "key=value; Expires=Mon, 11-Nov-2019 00:00:00 GMT; Max-Age=123"
    cookie["secure"] = True
    assert str(cookie) == "key=value; Expires=Mon, 11-Nov-2019 00:00:00 GMT; Max-Age=123; Secure"
    cookie["path"] = "/"

# Generated at 2022-06-14 07:00:02.426818
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test method Cookie.__str__()

    __str__ is the "magic method" which is used when str() is called on the
    object.  In this case, the str() method returns the value of the cookie
    formatted as a header that can be sent to the browser.
    """
    cookie = Cookie("sample", "cookie value")
    cookie["path"] = "/"
    cookie["comment"] = "this is a test"

    str_val = str(cookie)
    assert str_val == "sample=cookie%20value; Path=/; Comment=this%20is%20a%20test"
    print("Test Passed")

if __name__ == "__main__":
    test_Cookie___str__()

# Generated at 2022-06-14 07:00:16.041618
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert str(Cookie('one', 'two')) == 'one=two'
    assert str(Cookie('one', 'two;')) == 'one="two;"'
    assert str(Cookie('one', 'two')) == 'one=two'
    assert str(Cookie('one', 'two;')) == 'one="two;"'
    cookie = Cookie('one', 'two')
    expected = 'one=two'
    expected += '; Max-Age=0'
    cookie['max-age'] = 0
    assert str(cookie) == expected
    expected = 'one=two; Path=/'
    cookie = Cookie('one', 'two')
    cookie['path'] = '/'
    assert str(cookie) == expected
    expected = 'one=two; Domain=127.0.0.8'
    cookie = Cookie

# Generated at 2022-06-14 07:00:21.647182
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("a", "b")
    cookie["expires"] = datetime.strptime("Thu, 01 Jan 1970 00:00:00 GMT", "%a, %d-%b-%Y %T GMT")
    assert str(cookie) == "a=b; expires=Thu, 01-Jan-1970 00:00:00 GMT"


# Generated at 2022-06-14 07:00:27.695904
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    headers.add("Set-Cookie", "hello=world; path=/")
    headers.add("Set-Cookie", "cookie=monster; path=/")
    jar = CookieJar(headers)
    del jar["cookie"]
    assert "cookie=monster" not in str(headers)

# Generated at 2022-06-14 07:00:41.854944
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    assert str(cookie) == "foo=bar"
    cookie["path"] = "/"
    assert str(cookie) == "foo=bar; Path=/"
    cookie["comment"] = "comment"
    assert str(cookie) == "foo=bar; Comment=comment; Path=/"
    cookie["max-age"] = 123
    assert str(cookie) == "foo=bar; Max-Age=123; Comment=comment; Path=/"

    # Test invalid type of cookie value
    cookie = Cookie("name", None)
    assert str(cookie) == "name="

# ------------------------------------------------------------ #
#  Tests
# ------------------------------------------------------------ #


# Generated at 2022-06-14 07:00:52.488915
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from collections import ChainMap
    from fastapi.testclient import TestClient
    from httpcore import Cookies
    from fastapi import FastAPI

    app = FastAPI()
    client = TestClient(app)

    @app.get("/")
    def read_root():
        return {}

    @app.get("/write-cookie")
    async def write_cookies():
        response = PlainTextResponse("hey")
        cookies = Cookies(response.headers)
        cookies["cookie1"] = "test1"
        cookies["cookie2"] = "test2"
        cookies["cookie3"] = "test3"
        return response

    @app.get("/delete-cookie")
    async def delete_cookies(cookies: Cookies = Depends(CookieJar)):
        response = PlainTextResponse("hey")

# Generated at 2022-06-14 07:01:03.921023
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    cookies = CookieJar(headers)

    cookies["cookie1"] = "value"
    cookies["cookie2"] = "value"

    assert cookies["cookie1"] == "value"
    assert cookies["cookie2"] == "value"

    del cookies["cookie1"]
    assert headers["Set-Cookie"] == ["cookie2=value; Path=/"]

    # Case where key doesn't exist
    try:
        del cookies["cookie3"]
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError")


# Generated at 2022-06-14 07:01:11.067526
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    output = cookie.__str__()
    assert output == "name=value"
    cookie["path"] = "/test"
    output = cookie.__str__()
    assert output == "name=value; Path=/test"
    cookie["max-age"] = 10
    output = cookie.__str__()
    assert output == "name=value; Path=/test; Max-Age=10"
    cookie["secure"] = True
    output = cookie.__str__()
    assert output == "name=value; Path=/test; Max-Age=10; Secure"

# Generated at 2022-06-14 07:01:22.908641
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    cookie.update({"path": "/", "expires": datetime.now()})
    print(cookie)
    # key=value; Path=/; Expires=Sat, 02-Nov-2019 00:30:27 GMT
    cookie["max-age"] = 10
    print(cookie)
    # key=value; Path=/; Expires=Sat, 02-Nov-2019 00:30:27 GMT; Max-Age=10
    cookie["secure"] = True
    print(cookie)
    # key=value; Path=/; Expires=Sat, 02-Nov-2019 00:30:27 GMT; Max-Age=10; Secure
    
    
# ------------------------------------------------------------ #
#  Main Exported Class
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:01:33.459768
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar({})
    
    ## If key not in self.cookie_headers
    # Test 1:
    cookies["test1"] = "value1"
    assert cookies["test1"] == "value1"
    
    del cookies["test1"]

    ## If key in self.cookie_headers
    # Test 2:
    cookies["test2"] = "value2"
    assert cookies["test2"] == "value2"
    
    cookies["test3"] = "value3"
    assert cookies["test3"] == "value3"
    
    del cookies["test2"]
    assert cookies["test3"] == "value3"

# Generated at 2022-06-14 07:01:42.479622
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    expected_output = "a=b; Version=1; Expires=Sat, 01-Jan-2000 00:00:00 GMT; Path=/; Comment=; Domain=; Max-Age=0; Secure; HttpOnly"
    c = Cookie("a", "b")
    c["version"] = 1
    c["expires"] = datetime(2000, 1, 1)
    c["path"] = "/"
    c["comment"] = ""
    c["domain"] = ""
    c["max-age"] = 0
    c["httponly"] = True
    c["secure"] = True
    assert str(c) == expected_output

# ------------------------------------------------------------ #
#  Cookies Middleware
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:01:47.117516
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers({"blah": ""})
    cookie = CookieJar(headers)
    cookie["dsf"] = "sdfsdf"

    del cookie["dsf"]

    assert "Set-Cookie" not in cookie.headers



# Generated at 2022-06-14 07:01:48.209038
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    pass


# Generated at 2022-06-14 07:01:54.792878
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from starlette.testclient import TestClient
    from starlette.applications import Starlette

    app = Starlette()
    client = TestClient(app)

    @app.route('/set')
    async def set_cookies(request):
        response = JSONResponse({"msg": "done"})
        response.set_cookie(key="test", value="test-value")

        return response

    response = client.get('/set')
    assert response.cookies.get('test').value == "test-value"

    response = client.delete('/set')
    assert response.cookies.get('test') == None

# Generated at 2022-06-14 07:02:11.350187
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {'Set-Cookie':[Cookie('name', 'John'), Cookie('age', '32'), Cookie('address', 'BOSTON')]}
    cookie_jar = CookieJar(headers)

    del cookie_jar['address']
    assert not cookie_jar.headers.has('address')

    del cookie_jar['age']
    assert not cookie_jar.headers.has('age')

    del cookie_jar['age']
    assert not cookie_jar.headers.has('age')

    del cookie_jar['name']
    assert not cookie_jar.headers.has('name')

if __name__ == "__main__":
    test_CookieJar___delitem__()

# Generated at 2022-06-14 07:02:24.754398
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    """CookieJar.__delitem__(key)"""
    h = Headers() 
    c = CookieJar(h)
    c['1'] = 'hello'
    assert h['Set-Cookie'] == '1=hello; Path=/'
    del c['1']
    assert h['Set-Cookie'] == '1=; Max-Age=0'
    assert len(h['Set-Cookie']) == 1
    c['1'] = 'hello'
    c['2'] = 'ok'
    assert len(c) == 2
    assert len(h['Set-Cookie']) == 3
    del c['1']
    assert h['Set-Cookie'] == '1=; Max-Age=0,2=ok; Path=/'
    c['1'] = 'hello'

# Generated at 2022-06-14 07:02:31.077615
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class A:
        def get_all(self, key):
            return []
        def add(self, key, value):
            return
        def pop(self, key):
            return None

    for key, value in [("a", 1), ("b", 2)]:
        a = A()
        d = CookieJar(a)
        d[key] = value

    for key in d:
        del d[key]


# Generated at 2022-06-14 07:02:43.972069
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    _headers = MultiHeader()
    _cookies = CookieJar(_headers)
    _cookies["cookie1"] = "value1"
    _cookies["cookie2"] = "value2"

    assert _cookies["cookie1"]["path"] == "/"
    assert _cookies["cookie2"]["path"] == "/"

    _headers.popall(_cookies.header_key)
    _cookies.cookie_headers = {}
    _cookies.update({})

    assert not _headers.getall(_cookies.header_key)

    _cookies["cookie1"] = "value1"
    _cookies["cookie2"] = "value2"

    assert _cookies["cookie1"]["path"] == "/"
    assert _cookies["cookie2"]["path"] == "/"

    del _cook

# Generated at 2022-06-14 07:02:50.986140
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers=MultiDict()
    cj = CookieJar(headers)
    cj["a"] = "b"
    assert cj["a"].value == "b"
    cj["a"] = "c"
    assert cj["a"].value == "c"
    assert headers["Set-Cookie"] == ["a=c"]


# Generated at 2022-06-14 07:03:04.447421
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie(
        "key",
        "value"
    )
    assert c.__str__() == "key=value"
    # Test reserved word key
    c.__setitem__(
        "expires",
        "date"
    )
    assert c.__str__() == "key=value; Expires=date"
    # Test reserved word value
    c.__setitem__(
        "comment",
        "comment"
    )
    assert c.__str__() == "key=value; Expires=date; Comment=comment"
    # Test reserved word
    c.__setitem__(
        "max-age",
        "date"
    )
    assert c.__str__() == "key=value; Expires=date; Comment=comment; Max-Age=date"
    #

# Generated at 2022-06-14 07:03:06.833965
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

# ------------------------------------------------------------ #
#  Response and HTTPExceptions
# ------------------------------------------------------------ #


# Generated at 2022-06-14 07:03:18.694646
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    import pytest
    cj = CookieJar({})
    # happy path
    cj["key"] = "value"
    assert cj["key"] == "value"
    assert cj.cookie_headers == {'key': 'Set-Cookie'}
    assert cj.headers == {"Set-Cookie": ['key="value"; Path=/']}
    # update existing
    cj["key"] = "newvalue"
    assert cj["key"] == "newvalue"
    assert cj.cookie_headers == {'key': 'Set-Cookie'}
    assert cj.headers == {"Set-Cookie": ['key="newvalue"; Path=/']}
    # key already exists in cookies
    cj["key"] = "value"
    assert cj["key"] == "value"
    assert cj.cookie_

# Generated at 2022-06-14 07:03:23.811166
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('key', 'val')
    result = str(cookie)
    assert result == "key=val", f"Cookie.__str__()'s result should be 'key=val' but is '{result}'"


# Generated at 2022-06-14 07:03:27.345902
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("1", "2")
    cookie["max-age"] = 30
    result = str(cookie)
    print(result)


# Generated at 2022-06-14 07:03:40.596392
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    """
    Unit tests for Class CookieJar and method __delitem__()

    CookieJar Scenario:
    1. Add CookieJar to HTTP Response Headers
    2. Add a cookie to CookieJar
    3. Remove a cookie from CookieJar
    4. Verify the cookie is removed from the CookieJar and the HTTP Response Header
    """
    headers = dict()
    cookie_jar = CookieJar(headers)
    cookie_jar["foo"] = "bar"
    del cookie_jar["foo"]
    assert cookie_jar.get('foo') is None
    assert cookie_jar.cookie_headers.get('foo') is None
    assert headers.get('Set-Cookie') is None

# Generated at 2022-06-14 07:03:52.525137
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    
    # Arrange
    headers = {'Set-Cookie':'choco_chip=on'}
    CookieJar_instance = CookieJar(headers)

    # Act
    key = 'choco_chip'
    value = 'off'
    CookieJar_instance[key] = value
    print('CookieJar_instance[choco_chip]= ' , CookieJar_instance[key])
    expected_output = 'Set-Cookie:choco_chip=off; Path=/; Max-Age=0'
    actual_output = headers['Set-Cookie']
    print('headers: ',headers['Set-Cookie'] )

    # Assert
    assert expected_output == actual_output


# Generated at 2022-06-14 07:04:07.109625
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Test empty cookie jar where key is not in the headers.
    headers = MultiHeader()
    cookieJar = CookieJar(headers)
    key = "name"
    value = "test value"
    cookieJar[key] = value
    assert(cookieJar[key] == value)
    assert(headers.getone(cookieJar.header_key) is not None)

    del cookieJar[key]
    assert(key not in cookieJar)
    assert(headers.getone(cookieJar.header_key) is None)

    # Test where key is in the headers
    headers = MultiHeader()
    cookieJar = CookieJar(headers)
    key = "name"
    cookieJar[key] = value
    assert(cookieJar[key] == value)
    assert(headers.getone(cookieJar.header_key) is not None)

# Generated at 2022-06-14 07:04:17.867185
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class HttpHeaders(dict):
        def __init__(self):
            super().__init__()
    
        def get(self, key, default = None):
            return self.__dict__.get(key, default)
    
        def pop(self, key, default = None):
            try:
                item = self.__dict__.pop(key)
                return item
            except KeyError:
                return default
        
        def add(self, key, value):
            try:
                self.__dict__[key].append(value)
            except KeyError:
                self.__dict__[key] = [value]
    
        def popall(self, key):
            try:
                value = self.__dict__.pop(key)
            except KeyError:
                return []
            return value


# Generated at 2022-06-14 07:04:27.139070
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    print(cookie.__str__())
    cookie["expires"] = datetime(2023, 11, 3, 3, 3, 3)
    print(cookie.__str__())
    cookie["max-age"] = 5
    print(cookie.__str__())
    cookie["secure"] = True
    print(cookie.__str__())
    cookie["path"] = "/"
    print(cookie.__str__())
    cookie["domain"] = "sivalabs.in"
    print(cookie.__str__())
    assert False


# Generated at 2022-06-14 07:04:40.180134
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from mangum import Headers
    from multidict import MultiDict
    headers = Headers(MultiDict())
    cj = CookieJar(headers)
    cj["test_key"] = "test_value"
    test_string = 'test_key="test_value"; Path=/; Version=1'
    assert test_string == str(headers["Set-Cookie"])
    cj["test_key2"] = "test_value2"
    test_string = 'test_key="test_value"; Path=/; Version=1'
    test_string_2 = 'test_key2="test_value2"; Path=/; Version=1'
    assert test_string == str(headers["Set-Cookie"])
    assert test_string_2 == str(headers["Set-Cookie2"])

# Generated at 2022-06-14 07:04:44.147204
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    j = CookieJar(headers)
    j["cookie_name"] = "cookie_value"
    del j["cookie_name"]
    assert "cookie_name" not in headers
    assert "cookie_name" not in j
    assert headers.getall("Set-Cookie") == []


# Generated at 2022-06-14 07:04:56.816740
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["test_cookie"] = "test_value"
    assert cookie_jar["test_cookie"].value == "test_value"
    assert headers.getall('Set-Cookie') == ['test_cookie=test_value; Path=/']
    cookie_jar["test_cookie"] = "test_value2"
    assert cookie_jar["test_cookie"].value == "test_value2"
    assert headers.getall('Set-Cookie') == ['test_cookie=test_value2; Path=/']
    assert cookie_jar.get("test_cookie")


# Generated at 2022-06-14 07:05:04.751736
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('key', 'value')
    assert c.__str__() == "key=value"
    c = Cookie('key', 'value2')
    assert c.__str__() == "key=value2"
    c = Cookie('key', 'value')
    assert c.__str__() == "key=value"
    c = Cookie('key', '3value')
    assert c.__str__() == "key=3value"
    c = Cookie('key', '123value')
    assert c.__str__() == "key=123value"
    c = Cookie('key', '123')
    assert c.__str__() == "key=123"
    c = Cookie('key', 'value3')
    assert c.__str__() == "key=value3"

# Generated at 2022-06-14 07:05:11.789299
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test_headers = CIMultiDict()
    test_headers.add("Set-Cookie", "mykey=myvalue; path=/")
    cookie_jar = CookieJar(test_headers)

    del cookie_jar["mykey"]
    assert cookie_jar == {}
    assert test_headers == CIMultiDict()
    assert cookie_jar.cookie_headers == {}



# Generated at 2022-06-14 07:05:25.812830
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = {"Set-Cookie" : "name=value"}
    cookies = CookieJar(headers)
    cookies["name"] = "value2"
    assert cookies["name"].value == "value2"


# Generated at 2022-06-14 07:05:29.737004
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    resp = Response()
    resp.COOKIES["key"] = "value"
    assert resp.COOKIES.cookie_headers["key"] == "Set-Cookie"
    del resp.COOKIES["key"]
    assert not resp.COOKIES.cookie_headers.get("key")
    assert resp.COOKIES.headers.getlist("Set-Cookie") == []


# Generated at 2022-06-14 07:05:37.129001
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():

    c = Cookie("cookie1", "monster")
    assert str(c) == "cookie1=monster"

    # Make sure that Max-Age is outputted in the str representation
    c["Max-Age"] = DEFAULT_MAX_AGE
    assert str(c) == "cookie1=monster; Max-Age=0"

    # Make sure that comment is outputted in the str representation
    c["Comment"] = "Hey! I'm a comment!"
    assert str(c) == "cookie1=monster; Max-Age=0; Comment=Hey! I'm a comment!"

    c2 = Cookie("cookie2", "not a monster")
    assert str(c2) == "cookie2=not a monster"

# Generated at 2022-06-14 07:05:40.324366
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    s = []
    d = CookieJar(s)
    d["foo"] = "bar"
    del d["foo"]
    print(s)



# Generated at 2022-06-14 07:05:47.914487
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    import json
    cookie_name = "mycookie"
    cookie_value = "mycookievalue"
    cookie_jar = CookieJar()
    cookie_jar[cookie_name] = cookie_value
    cookie_encoded = cookie_jar[cookie_name].encode("utf-8")
    assert cookie_encoded == b"Set-Cookie: mycookie=mycookievalue"
    print("CookieJar::__setitem__() passed unit test")


# Generated at 2022-06-14 07:05:50.017470
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('key', 'value')
    assert c.__str__() == 'key=value'

# Generated at 2022-06-14 07:05:51.570664
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    assert True == False


# Generated at 2022-06-14 07:06:03.737797
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers: Dict[str, str] = {}
    cj = CookieJar(headers)
    cj1 = Cookie("usename", "Tom")
    cj.cookie_headers["usename"] = "Set-Cookie"
    assert len(cj.cookie_headers) == 1
    assert headers["Set-Cookie"] == "usename=Tom; Path=/; Max-Age=0"
    del cj["usename"]
    assert cj.__delitem__ == cj1
    assert len(cj.cookie_headers) == 0
    assert cj.cookie_headers == {}
    assert headers["Set-Cookie"] == ""


# Generated at 2022-06-14 07:06:13.371033
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Test if a cookie can be transformed into a Set-Cookie header value.
    # Create a new cookie
    cookie = Cookie("test_cookie", "Testing String")
    assert str(cookie) == "test_cookie=Testing String"
    # add an expiration time
    cookie["expires"] = datetime(2019, 9, 24, 3, 45, 12)
    assert str(cookie) == "test_cookie=Testing String; Expires=Tue, 24-Sep-2019 03:45:12 GMT"
    # check if flag properties are reflected properly
    cookie["HttpOnly"] = True
    assert str(cookie) == "test_cookie=Testing String; Expires=Tue, 24-Sep-2019 03:45:12 GMT; HttpOnly"
    # check if ordered properties are reflected properly. Cookie value must be first, followed by ordered properties and
    #

# Generated at 2022-06-14 07:06:25.207468
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    from pytest import raises
    from http_types.exceptions import HTTPValidationError

    cookie = Cookie('foo', 'bar')

    # Raise error
    # Wrong type for 'expires' property
    with raises(TypeError):
        cookie["expires"] = 5
    # Wrong type for 'max-age' property
    with raises(ValueError):
        cookie["max-age"] = "hello"
    # Not supported property
    with raises(KeyError):
        cookie["bad-key"] = 5
    # key set to false
    with raises(KeyError):
        cookie["secure"] = False
    # Legal key
    cookie["secure"] = True
    assert cookie["secure"] == True
    cookie["httponly"] = True
    assert cookie["httponly"] == True
    cookie["expires"] = datetime.utcnow()

# Generated at 2022-06-14 07:06:59.243566
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime

    time = datetime.fromisoformat('2019-01-01 12:00:00')

    cookie = Cookie('cookie_key', 'cookie_value')
    cookie['expires'] = time
    cookie['path'] = '/'
    cookie['comment'] = 'comment'
    cookie['domain'] = 'domain'
    cookie['max-age'] = 50
    cookie['secure'] = True
    cookie['httponly'] = False
    cookie['version'] = 1
    cookie['samesite'] = 'lax'

    expected_string = 'cookie_key=cookie_value; Expires=Wed, 01-Jan-2019 12:00:00 GMT; Path=/; Comment=comment; Domain=domain; Max-Age=50; Secure; Version=1; SameSite=lax'

    assert cookie.__str__

# Generated at 2022-06-14 07:07:12.656430
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class MockHeaders:

        def __init__(self):
            self.headers = {}
            self.status_code = 200

        def add(self, key, value):
            multi_headers = self.headers.get(key, [])
            multi_headers.append(value)
            self.headers[key] = multi_headers

        def popall(self, key):
            multi_headers = self.headers.get(key, [])
            self.headers[key] = []
            return multi_headers

    headers = MockHeaders()

    # Testing the case where a cookie is already in the header
    cookie_jar = CookieJar(headers)
    cookie_jar["cookie1"] = "test1"
    cookie_jar["cookie2"] = "test2"

    cookie_jar["cookie2"] = "test2"
   

# Generated at 2022-06-14 07:07:17.028780
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    expect = 'id=1; HttpOnly; Path=/'
    cookie = Cookie('id', '1')
    cookie['httponly'] = True
    cookie['path'] = '/'
    ret = str(cookie)
    assert ret == expect


# ------------------------------------------------------------ #
#  Middleware
# ------------------------------------------------------------ #
