

# Generated at 2022-06-14 06:57:33.845692
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    print("Testing CookieJar's method __setitem__")
    headers = Headers()
    cookies = CookieJar(headers)
    cookie = cookies["new_cookie"] = "first_value"
    assert cookie.key == "new_cookie"
    assert cookie.value == "first_value"
    assert headers["Set-Cookie"] == 'new_cookie="first_value"; Path=/'
    cookie = cookies["new_cookie"]["max-age"] = 5
    assert cookie == 5
    assert headers["Set-Cookie"] == 'new_cookie="first_value"; Path=/; Max-Age=5'
    assert isinstance(cookies["new_cookie"], Cookie)
    assert cookies["new_cookie"].value == "first_value"
    assert cookies["new_cookie"]["path"] == "/"

# Generated at 2022-06-14 06:57:43.242182
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    cookie["domain"] = "127.0.0.1"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = "1"
    cookie["max-age"] = 100
    cookie["expires"] = datetime(year=2024, month=10, day=18)

    assert(str(cookie) == "key=value; Path=/; Domain=127.0.0.1; "
                         "Secure; HttpOnly; Version=1; Max-Age=100; "
                         "Expires=Thu, 18-Oct-2024 00:00:00 GMT")


# ------------------------------------------------------------ #
#  Cookie Headers
# ------------------------------------------------------------ #



# Generated at 2022-06-14 06:57:54.715028
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie('key', 'value')
    c['expires'] = datetime(2019, 1, 1)
    c['path'] = '/'
    c['comment'] = 'asdf'
    c['domain'] = 'localhost'
    c['max-age'] = 1
    c['secure'] = True
    c['httponly'] = True
    c['version'] = '1'
    c['samesite'] = 'lax'
    c['garbage'] = 'garbage'
    assert str(c) == 'key=value; Expires=Tue, 01-Jan-2019 00:00:00 GMT; Path=/; Comment=asdf; Domain=localhost; Max-Age=1; Secure; HttpOnly; Version=1; SameSite=lax'
    del c['garbage']


# ------------------------------------------------------------ #


# Generated at 2022-06-14 06:58:01.207527
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    cookie = Cookie("x", "5")
    cookies["x"] = cookie
    cookies["y"] = cookie
    cookies["z"] = cookie
    cookies["y"] = cookie
    assert headers.getlist("Set-Cookie") == cookie
    del cookies["y"]
    cookies["q"] = cookie
    del cookies["x"]
    del cookies["q"]
    del cookies["z"]
    assert not headers.getlist("Set-Cookie")


# Generated at 2022-06-14 06:58:07.536741
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    morsel = Cookie('test', 'haha')
    assert str(morsel) == 'test=haha'
    morsel['path'] = '/'
    assert str(morsel) == 'test=haha; Path=/'
    morsel['domain'] = 'localhost'
    assert str(morsel) == 'test=haha; Path=/; Domain=localhost'
    morsel['secure'] = True
    assert str(morsel) == 'test=haha; Path=/; Domain=localhost; Secure'
    morsel['httponly'] = True
    assert str(morsel) == 'test=haha; Path=/; Domain=localhost; Secure; HttpOnly'
    morsel['max-age'] = 100

# Generated at 2022-06-14 06:58:20.868799
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookies = CookieJar(headers)
    cookies["key"] = "value"
    cookies["key2"] = "value2"
    cookies["key3"] = "value3"

    assert cookies["key"] == "value"
    assert cookies["key2"] == "value2"
    assert cookies["key3"] == "value3"

    del cookies["key"]
    assert cookies.get("key") is None
    assert "key" not in cookies
    assert cookies["key2"] == "value2"
    assert cookies["key3"] == "value3"

    del cookies["key2"]
    assert cookies.get("key") is None
    assert "key" not in cookies
    assert cookies.get("key2") is None
    assert "key2" not in cookies

# Generated at 2022-06-14 06:58:29.086466
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("a", "b")

    assert str(c) == "a=b"

    c["expires"] = "Fri, 31 Dec 2010 23:59:59 GMT"
    c["path"] = "/acme"
    c["secure"] = True
    c["httponly"] = True
    c["version"] = 1
    c["Comment"] = "no comment"
    c["domain"] = "dummy.com"

    expected = """\
a=b; expires=Fri, 31 Dec 2010 23:59:59 GMT; Path=/acme; Secure; \
HttpOnly; Version=1; Comment="no comment"; Domain=dummy.com"""
    assert str(c) == expected



# Generated at 2022-06-14 06:58:37.709219
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    cookie["max-age"] = DEFAULT_MAX_AGE
    cookie_str = str(cookie)

    cookiejar = CookieJar(dict())
    cookiejar["key"] = "value"
    assert cookiejar.headers["Set-Cookie"] == cookie_str
    cookiejar["key"] = "value2"
    assert cookiejar.headers["Set-Cookie"] == cookie_str


# Generated at 2022-06-14 06:58:50.690650
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    import pytest

    jar = CookieJar()

    # Case 1: delete item from empty jar
    jar["test"] = "test"
    del jar["test"]
    assert jar == {}
    assert jar.headers == {}
    assert jar.cookies == {}

    # Case 2: delete non-existent item
    del jar["test"]
    assert jar == {}
    assert jar.headers == {}
    assert jar.cookies == {}

    # Case 3: delete item with one cookie and one header
    jar["test"] = "test"
    jar["test2"] = "test2"
    del jar["test2"]
    assert jar == {"test": "test"}
    # TODO(josh): figure out the best test for headers/cookies
    # assert jar.cookies == {"test": "test"}
    # assert jar.headers

# Generated at 2022-06-14 06:59:02.351406
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    cookie2 = Cookie("key2", "value2")
    cookie2["path"] = "/"
    cookie2["secure"] = True
    cookie2["httponly"] = True
    cookie2["max-age"] = "10"
    cookie2["expires"] = datetime.now()

    assert cookie2["path"] == "/"
    assert cookie2["secure"] == True
    assert cookie2["httponly"] == True
    assert cookie2["max-age"] == "10"
    assert isinstance(cookie2["expires"], datetime)

    with pytest.raises(KeyError):
        cookie["random"] = "random"
    with pytest.raises(KeyError):
        cookie2["random"] = "random"

    cookie["max-age"] = "10"


# Generated at 2022-06-14 06:59:18.517791
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    test_cookie = Cookie("test", "foo")
    assert str(test_cookie) == "test=foo"

    test_cookie["path"] = "/testpath"
    test_cookie["domain"] = "test.com"
    assert str(test_cookie) == "test=foo; Path=/testpath; Domain=test.com"

    test_cookie = Cookie("test", "foo")
    test_cookie["max-age"] = 10
    test_cookie["domain"] = "test.com"
    assert str(test_cookie) == "test=foo; Max-Age=10; Domain=test.com"

    test_cookie = Cookie("test", "foo")
    test_cookie["httponly"] = True
    assert str(test_cookie) == "test=foo; HttpOnly"

# Generated at 2022-06-14 06:59:24.421204
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers1 = MultiHeader()
    jar1 = CookieJar(headers1)
    jar1["foo"] = "bar"
    jar1["baz"] = "bam"
    del jar1["foo"]
    res = jar1 == {"baz": "bam"}
    return res



# Generated at 2022-06-14 06:59:33.709077
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    # Setup
    from tracim_backend.lib.utils.request import TracimRequest
    headers = TracimRequest.dict_class()
    cookie_jar = CookieJar(headers)

    # Test
    cookie_jar["key1"] = "cookie_1_value"

    # Check
    assert len(cookie_jar)==1
    assert len(headers)==1
    assert headers["Set-Cookie"]=="key1=cookie_1_value; Path=/; Max-Age=0"
    assert "key1" in cookie_jar



# Generated at 2022-06-14 06:59:45.611746
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("my_key", "my_value")
    assert str(cookie) == "my_key=my_value"

    cookie = Cookie("my_key", "my_value")
    cookie["path"] = "/"
    assert str(cookie) == "my_key=my_value; Path=/"

    cookie = Cookie("my_key", "my_value")
    cookie["path"] = "/"
    cookie["expires"] = datetime(2018, 1, 2, 12, 12, 12)
    assert (
        str(cookie) == "my_key=my_value; Path=/; expires=Tue, 02-Jan-2018 12:12:12 GMT"
    )

    cookie = Cookie("my_key", "my_value")
    cookie["path"] = "/"

# Generated at 2022-06-14 06:59:56.048668
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookie_jar = CookieJar(headers={})
    cookie_jar["key"] = "value"
    
    expected = Cookie("key", "value") 
    expected["path"] = "/"
    assert cookie_jar["key"] == expected
    assert cookie_jar.headers["Set-Cookie"] == expected.__str__()
    
    expected["path"] = "/path"
    cookie_jar["key"] = expected

    assert cookie_jar["key"] == expected
    assert cookie_jar.headers["Set-Cookie"] == expected.__str__()



# Generated at 2022-06-14 07:00:07.091752
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cj = CookieJar(headers)
    assert headers == {}
    cj.__setitem__("name1", "value1")
    cj.__setitem__("name2", "value2")
    cj.__setitem__("name3", "value3")
    assert headers == {
        "Set-Cookie": [
            "name1=value1; Path=/; Max-Age=0",
            "name2=value2; Path=/; Max-Age=0",
            "name3=value3; Path=/; Max-Age=0",
        ]
    }

    ## Delete before add
    cj.__delitem__("name4")

# Generated at 2022-06-14 07:00:16.472259
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = dict()
    cookiejar = CookieJar(headers)
    cookiejar["a"] = 1
    cookiejar["b"] = 2
    cookiejar["c"] = 3
    del cookiejar["b"]

    assert headers["Set-Cookie"][0] == "a=1; Path=/; HttpOnly"
    assert headers["Set-Cookie"][1] == "c=3; Path=/; HttpOnly"
    assert len(headers["Set-Cookie"]) == 2

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------


# Generated at 2022-06-14 07:00:23.376577
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Unit test for method Cookie.__str__.
    """
    def assert_cookie_str(key, value, expected_str):
        cookie = Cookie(key, value)
        assert str(cookie) == expected_str

    assert_cookie_str("key_test", "value test", "key_test=value test")
    assert_cookie_str("key_test", "vave test", "key_test=\"vave test\"")

# Generated at 2022-06-14 07:00:30.736499
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaders({})
    cookiejar = CookieJar(headers)
    cookiejar["n"] = "v"
    assert headers == { "Set-Cookie": ["n=v; path=/"]}
    assert cookiejar == { "n": "v"}
    assert cookiejar["n"].value == "v"
    assert cookiejar["n"] == "v"
    


# Generated at 2022-06-14 07:00:39.712024
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    n = "simplecookie"
    c = Cookie(n, "testvalue")
    assert c.__str__() == "simplecookie=testvalue"

    c["max-age"] = "testmaxage"
    assert c.__str__() == "simplecookie=testvalue; Max-Age=testmaxage"

    c["max-age"] = 0
    assert c.__str__() == "simplecookie=testvalue; Max-Age=0"

    c["domain"] = "testdomain"
    assert c.__str__() == "simplecookie=testvalue; Max-Age=0; Domain=testdomain"

    c["domain"] = "testdomain123"
    assert c.__str__() == "simplecookie=testvalue; Max-Age=0; Domain=testdomain123"


# Generated at 2022-06-14 07:00:48.176309
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Initialize headers
    headers = MultiHeader()
    jar = CookieJar(headers)

    # Add a new cookie to the jar
    jar.__setitem__('test', 'value')
    assert jar.__getitem__('test')

    # Delete the cookie from the jar
    jar.__delitem__('test')
    assert 'test' not in jar


# Generated at 2022-06-14 07:00:58.703268
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    assert cookie.key == "key"
    assert cookie.value == "value"
    assert cookie["key"] == "value"
    cookie["key"] = "new value"
    assert cookie["key"] == "new value"
    with pytest.raises(KeyError, match="Cookie name is a reserved word"):
        cookie["expires"] = 1
    with pytest.raises(KeyError, match="Unknown cookie property"):
        cookie["gottagofast"] = 1
    with pytest.raises(ValueError, match="Cookie max-age must be an integer"):
        cookie["max-age"] = "abc"
    with pytest.raises(TypeError, match="Cookie 'expires' property must be a datetime"):
        cookie["expires"]

# Generated at 2022-06-14 07:01:10.258393
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("key", "value")
    with pytest.raises(KeyError):
        c["path"] = "path"
    c["path"] = "/"
    with pytest.raises(KeyError):
        c["domain"] = "domain"
    c["domain"] = "domain"
    with pytest.raises(KeyError):
        c["comment"] = "comment"
    c["comment"] = "comment"
    with pytest.raises(TypeError):
        c["expires"] = "expires"
    c["expires"] = datetime(2019, 2, 11, 0, 0, 0)
    c["max-age"] = "max-age"
    with pytest.raises(ValueError):
        c["max-age"] = "0.1"

# Generated at 2022-06-14 07:01:21.647526
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Initialize
    headers_simplified = {'Set-Cookie': 'fruit: apple\r\nSet-Cookie: fruit: banana\r\n'}
    headers = MultiHeader(headers_simplified)
    jar = CookieJar(headers)
    # Set up cookie
    jar['fruit'] = 'apple'
    # Print cookies
    for key, val in jar.items():
        print(key, val, '\n')
    # Remove the cookie
    del jar['fruit']
    # Print cookies
    for key, val in jar.items():
        print(key, val, '\n')

    assert not 'fruit' in jar


# Generated at 2022-06-14 07:01:27.577094
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar(MultiHeader())
    cookies["test"] = "test"

    assert cookies["test"] == "test"
    assert cookies.cookie_headers["test"] == "Set-Cookie"
    assert cookies.headers["Set-Cookie"].value == "test"

    del cookies["test"]
    assert cookies.cookie_headers == {}
    assert cookies.headers == {}

    # Test deleting no existing cookie
    del cookies["test"]
    assert cookies.cookie_headers == {}
    assert cookies.headers == {}



# Generated at 2022-06-14 07:01:38.092426
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    headers.add('Set-Cookie', 'name=value;Domain=domain;Max-Age=500')
    headers.add('Set-Cookie', 'name2=value;Domain=domain;Max-Age=500')
    headers.add('Set-Cookie', 'name3=value;Domain=domain;Max-Age=500')
    c = CookieJar(headers)
    del c['name2']
    assert headers.getlist('Set-Cookie') == ['name=value;Domain=domain;Max-Age=500', 'name3=value;Domain=domain;Max-Age=500']

# Generated at 2022-06-14 07:01:41.277998
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    try:
        cookie = Cookie('name', 'value')
        cookie['new_key'] = 'new_value'
        assert False
    except KeyError:
        assert True



# Generated at 2022-06-14 07:01:55.000227
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar({})
    print("Test '__delitem__' method of class CookieJar:")
    print("Instruction: Create a cookie, change it and delete it from the header")
    print("Expected result: No header key is returned for the cookie")
    cookie_jar["testing"] = "testing-value"
    print("Result: ", end = '')
    print(cookie_jar["testing"])
    cookie_jar["testing"] = "abd"
    print("Result: ", end = '')
    print(cookie_jar["testing"])
    del cookie_jar["testing"]
    print("Result: ", end = '')
    print(cookie_jar["testing"])
    print("Result: ", end = '')
    print("testing" in cookie_jar)
    print("Result: ", end = '')

# Generated at 2022-06-14 07:01:58.427721
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    h = Headers()
    c = CookieJar(h)
    c["a"] = "1"
    assert len(h) == 2
    del c["a"]
    assert len(h) == 2

# Generated at 2022-06-14 07:02:04.748318
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("my_cookie", "my_value")
    assert str(c) == "my_cookie=my_value"
    c["path"] = "/"
    c["max-age"] = 1
    assert str(c) == "my_cookie=my_value; Path=/; Max-Age=1"


# ------------------------------------------------------------ #
#  Cookies
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:02:17.313682
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    key1 = "expires"
    value0 = "23-Apr-2020 20:04:50.0"
    value1 = "23-Apr-2020 20:04:50"
    value2 = "Mon, 23-Apr-2020 20:04:50 GMT"
    value3 = "Monday, 23-Apr-2020 20:04:50 GMT"
    value4 = "Mon, 23-Apr-2020 20:04:50"
    value5 = ValueError
    value6 = "Mon, 23-Apr-2020 20:04:50.0"
    value7 = TypeError
    value8 = "Mon, 23-Apr-2020 20:04:50.0 GMT"
    value9 = ValueError
    value10 = "<3"
    value11 = "3"
    value12 = "3.0"

# Generated at 2022-06-14 07:02:21.652155
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("cookie_name", "cookie_value")
    cookie["path"] = "/"
    cookie["max-age"] = 3600
    cookie["httponly"] = True
    print(cookie)



# Generated at 2022-06-14 07:02:33.628314
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    jar = CookieJar(headers)
    jar["name"] = "John"
    jar["age"] = "21"
    jar["name"] = "Julia"
    assert jar["name"] == "Julia"
    assert "Julia" in headers.getall("Set-Cookie")

    # Delete cookie
    del jar["name"]
    assert "Julia" not in headers.getall("Set-Cookie")
    assert "name=Julia" not in headers.getall("Set-Cookie")

    # Delete cookie without a value
    jar["favorite_color"]
    del jar["favorite_color"]
    assert "favorite_color=;" in headers.getall("Set-Cookie")
    assert len(headers.getall("Set-Cookie")) == 1


# Generated at 2022-06-14 07:02:45.950663
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Test encoding with max-age that is int
    testCookie = Cookie("key", "value")
    testCookie["max-age"] = 2
    assert str(testCookie) == "key=value; Max-Age=2"

    # Test encoding with max-age that is str
    testCookie = Cookie("key", "value")
    testCookie["max-age"] = "2"
    assert str(testCookie) == "key=value; Max-Age=2"

    # Test encoding with expires that is integer
    testCookie = Cookie("key", "value")
    testCookie["expires"] = datetime.today()
    assert str(testCookie) == f"key=value; Expires={datetime.today().strftime('%a, %d-%b-%Y %T GMT')}"



# Generated at 2022-06-14 07:02:59.880769
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookie_jar = CookieJar(headers)
    cookie_jar['test_key'] = 'test_value'
    # Assert that a cookie with key name test_key and value test_value exist
    # in the cookie jar
    assert(cookie_jar['test_key'].value == 'test_value')
    # Assert that a cookie with key name test_key and value test_value exist
    # in the set of headers
    assert(headers['Set-Cookie'].split('=')[0] == 'test_key')
    # Assert that value of key Set-Cookie in the set of headers is equal
    # to the stringified cookie
    assert(headers['Set-Cookie'] == str(cookie_jar['test_key']))
    # Delete the cookie using cookie_jar.__delitem__

# Generated at 2022-06-14 07:03:07.338126
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict()
    cookie_jar = CookieJar(headers)
    cookie_jar["user"] = "123"
    assert "user=123" in headers["Set-Cookie"]

    cookie_jar["password"] = "456"
    assert "password=456" in headers["Set-Cookie"]

    cookie_jar["user"] = "abc"
    assert "user=abc" in headers["Set-Cookie"]
    assert "user=123" not in headers["Set-Cookie"]

    del cookie_jar["user"]
    assert "user=abc" not in headers["Set-Cookie"]



# Generated at 2022-06-14 07:03:20.250602
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cj = CookieJar(headers)
    cookie_name = "cookie"
    # Test CookieJar.__delitem__ with key that doesn't exist in CookieJar
    cj[cookie_name] = "cookie"
    cj[cookie_name]
    assert_equal(headers.getall("Set-Cookie"), ["cookie=cookie; Path=/"])
    del cj[cookie_name]
    assert_not_in(cookie_name, cj)
    assert_equal(headers.getall("Set-Cookie"), ["cookie=; Path=/; Max-Age=0"])
    # Test CookieJar.__delitem__ with key that exists in CookieJar
    cj[cookie_name] = "cookie"
    cj[cookie_name]

# Generated at 2022-06-14 07:03:33.881019
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key="key", value="value")
    assert str(cookie) == "key=value"
    cookie["path"] = "path"
    assert str(cookie) == "key=value; Path=path"
    cookie["max-age"] = "max-age"
    assert str(cookie) == "key=value; Path=path; Max-Age=max-age"
    cookie["key"] = "value"
    assert str(cookie) == "key=value; Path=path; Max-Age=max-age; Version=value"
    cookie["comment"] = "comment"
    assert str(cookie) == "key=value; Path=path; Max-Age=max-age; Version=value; Comment=comment"
    cookie["domain"] = "domain"

# Generated at 2022-06-14 07:03:46.861406
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert(str(Cookie('foo','bar')) == 'foo=bar')
    assert(str(Cookie('foo','bar')) == 'foo=bar')
    assert(str(Cookie('foo','bar',path='/foo')) == 'foo=bar; Path=/foo')
    assert(str(Cookie('foo','bar',path='/foo',comment='foo')) == 'foo=bar; Path=/foo; Comment=foo')
    assert(str(Cookie('foo','bar',path='/foo',comment='foo',max_age=1)) == 'foo=bar; Path=/foo; Comment=foo; Max-Age=1')

# Generated at 2022-06-14 07:03:59.559302
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('name', 'value')
    c['max-age'] = 10
    assert str(c) == 'name=value; Max-Age=10'
    c.clear()
    c['expires'] = datetime(2020, 1, 1, 0, 0, 0)
    assert str(c) == 'name=value; Expires=Wed, 01-Jan-2020 00:00:00 GMT'
    c.clear()
    c['secure'] = True
    assert str(c) == 'name=value; Secure'
    c.clear()
    c['httponly'] = True
    assert str(c) == 'name=value; HttpOnly'
    c.clear()
    c['samesite'] = 'lax'
    assert str(c) == 'name=value; SameSite=lax'
   

# Generated at 2022-06-14 07:04:12.120226
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {}
    cookie = CookieJar(headers)
    cookie["test"] = "ololo"
    cookie["test"] = "trololo"
    cookie["test"] = "pizdec"
    cookie["pizda"] = "buhahahaha"
    cookie["pizda"] = "buhahahaha2"
    del cookie["pizda"]
    assert cookie["test"] == "pizdec"
    assert "pizda" not in cookie
    assert headers["Set-Cookie"] == "pizda=buhahahaha2; Path=/; HttpOnly"
    del cookie["test"]
    assert headers["Set-Cookie"] == "test=pizdec; Path=/; HttpOnly"

if __name__ == '__main__':
    test_CookieJar___delitem__()

# Generated at 2022-06-14 07:04:15.843366
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookiejar = CookieJar(headers)
    cookiejar["test"] = "test_value"
    assert len(cookiejar) == 1
    del cookiejar["test"]
    assert len(cookiejar) == 0


# Generated at 2022-06-14 07:04:21.366680
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    print("Unit test for method __setitem__ of class CookieJar")
    headers = Headers()
    headers.add("Authorization", "Bearer token")
    cookies = CookieJar(headers)
    cookies["name"] = "user"
    cookies["password"] = "password"
    cookies["sessionId"] = "sessionId"
    assert "user" in cookies
    assert "password" in cookies
    assert "sessionId" in cookies
    assert "Authorization" in headers
    assert "Set-Cookie" in headers
    print("passed")


# Generated at 2022-06-14 07:04:32.716314
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    expected = "; ".join([
        "%s=%s" % ("key", '"value') ,
        "%s=%d" % ("Max-Age", 10),
        "%s=%s" % ("Path", "path"),
        "%s=%s" % ("Expires", "Mon, 13-Jan-2020 00:00:00 GMT"),
        "Secure",
        "HttpOnly",
    ])
    cookie = Cookie("key", "value")
    cookie["max-age"] = 10
    cookie["path"] = "path"
    cookie["expires"] = datetime(2020, 1, 13)
    cookie["secure"] = True
    cookie["httponly"] = True

    assert str(cookie) == expected

# ------------------------------------------------------------ #
#  Tests
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:04:36.053847
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookiejar = CookieJar(headers)

    cookie1 = Cookie("cookie1", "value")
    cookiejar[cookie1.key] = cookie1
    assert cookie1.key in cookiejar.headers

    cookiejar.__delitem__("cookie1")
    assert cookie1.key not in cookiejar.headers



# Generated at 2022-06-14 07:04:47.731550
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key="key", value="value")
    assert cookie.__str__() == "key=value"
    cookie["path"] = "/path"
    assert cookie.__str__() == "key=value; Path=/path"
    cookie["max-age"] = 10
    cookie["expires"] = datetime.now()
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 1
    cookie["comment"] = "comment"
    cookie["domain"] = "domain.com"
    cookie["samesite"] = "Lax"
    str = cookie.__str__()

    assert str == "key=value; Path=/path; Max-Age=10; Secure; HttpOnly; Version=1; Comment=comment; Domain=domain.com; SameSite=Lax; Expires="

# Generated at 2022-06-14 07:04:50.137926
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

# Generated at 2022-06-14 07:05:02.097194
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():

    headers = CIMultiDict()
    cookie_jar = CookieJar(headers)

    # test adding a new cookie
    cookie_jar["newkey"] = "newvalue"
    assert headers.get("Set-Cookie") == "newkey=newvalue; Path=/"
    assert cookie_jar.get("newkey") == "newvalue"

    # test adding a new cookie that has a reserved word as a key
    # cookie_jar["expires"] = "2028-01-01"
    # assert "expires=2028-01-01; Path=/" in headers.get("Set-Cookie")
    # assert cookie_jar.get("expires") == "2028-01-01"

    # test adding a second cookie
    cookie_jar["anotherkey"] = "anothervalue"

# Generated at 2022-06-14 07:05:12.539875
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    print('Running unit test for method __setitem__ of class CookieJar')
    headers = {}
    cookiejar = CookieJar(headers)
    valid_cookie = 'valid_cookie'
    valid_value = 'valid_value'
    cookiejar[valid_cookie] = valid_value # Setting the value
    assert headers['Set-Cookie'] == 'valid_cookie=valid_value; Version=1; Path=/;'
    assert valid_value in headers['Set-Cookie']
    assert valid_cookie in headers['Set-Cookie'] 
    return 'Success'


# Generated at 2022-06-14 07:05:18.114143
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookies = CookieJar(headers)
    cookies["user"] = "Jon Doe"
    assert "user" in cookies
    cookies["user"] = ""
    cookies["user"]["max-age"] = 0
    assert "user" in cookies
    cookies["user"]["path"] = "/"
    assert "user" in cookies
    del cookies["user"]
    assert "user" not in cookies
    assert "user" not in cookies.cookie_headers

# Generated at 2022-06-14 07:05:32.682224
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers(None)
    headers.add("set-cookie", "key=value", replace=True)
    headers.add("set-cookie", "key1=value1", replace=True)
    headers.add("set-cookie", "key2=value2", replace=True)
    cookie_jar = CookieJar(headers)
    assert cookie_jar['key'].value == 'value'
    assert cookie_jar['key1'].value == 'value1'
    assert cookie_jar['key2'].value == 'value2'

    assert 'key' in cookie_jar.headers['set-cookie'][0]
    assert 'key1' in cookie_jar.headers['set-cookie'][1]
    assert 'key2' in cookie_jar.headers['set-cookie'][2]
    
    del cookie_jar

# Generated at 2022-06-14 07:05:43.573807
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():

    from tempest import testing

    jar = CookieJar(headers=testing.DummyHeaders())
    jar["mars"] = "bar"
    assert "mars=bar" in jar.headers["set-cookie"]
    assert jar.get("mars", "").value == "bar"

    jar["mars"] = "baz"
    assert jar.get("mars", "").value == "baz"

    jar["mars"] = None
    assert jar.get("mars") is None
    assert jar.get("mars", "").value == "baz"


# Generated at 2022-06-14 07:05:55.846591
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from .multiheaders import MultiHeader
    from .exceptions import CookieHeaderAlreadyExists

    key_1 = "key_1"
    value_1 = "value_1"
    key_2 = "key_2"
    value_2 = "value_2"
    key_3 = "key_3"
    value_3 = "value_3"
    key_4 = "key_4"
    value_4 = "value_4"
    key_5 = "key_5"
    value_5 = "value_5"

    cookie_header = "Cookie"
    set_cookie_header = "Set-Cookie"
    x_set_cookie_header = "X-Set-Cookie"

    claim_1 = "false"
    claim_2 = "true"

    now = datetime.now()

# Generated at 2022-06-14 07:06:08.179557
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('key', 'value')
    assert str(c) == 'key=value'
    c['version'] = '1'
    assert str(c) == 'key=value; Version=1'
    c['version'] = False
    assert str(c) == 'key=value'
    c['expires'] = datetime(2020, 1, 1)
    assert str(c) == 'key=value; Expires=Wed, 01-Jan-2020 00:00:00 GMT'
    c['max-age'] = '123'
    assert str(c) == 'key=value; Expires=Wed, 01-Jan-2020 00:00:00 GMT; Max-Age=123'
    c['max-age'] = 123.0

# Generated at 2022-06-14 07:06:18.649410
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar['key1'] = "value1"
    jar['key2'] = "value2"
    assert jar['key2'] == "value2"
    assert list(headers.headers) == [('Set-Cookie', 'key1=value1; Path=/'), ('Set-Cookie', 'key2=value2; Path=/')]
    del jar['key2']
    assert list(headers.headers) == [('Set-Cookie', 'key1=value1; Path=/')]


# Generated at 2022-06-14 07:06:22.025252
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiDict()
    jar = CookieJar(headers)
    jar["key"] = "value"
    header = headers["Set-Cookie"]
    assert header == ["key=value; Path=/"]


# Generated at 2022-06-14 07:06:31.602759
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("mycookie", "myvalue")
    assert str(cookie) == "mycookie=myvalue"

    cookie["httponly"] = True
    assert str(cookie) == "mycookie=myvalue; HttpOnly"

    cookie["max-age"] = 5
    assert str(cookie) == "mycookie=myvalue; HttpOnly; Max-Age=5"

    cookie["expires"] = datetime(year=2020, month=2, day=14, hour=12, minute=0)
    assert str(cookie) == "mycookie=myvalue; HttpOnly; Max-Age=5; expires=Fri, 14-Feb-2020 12:00:00 GMT"

    cookie = Cookie("mycookie", "myvalue")
    cookie["secure"] = True

# Generated at 2022-06-14 07:06:34.437222
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('myCookie', 'myValue')
    result = c.__str__()
    expected = 'myCookie=myValue; Path=; Domain=; Max-Age=; Secure; HttpOnly'
    assert result == expected


# Generated at 2022-06-14 07:06:40.766371
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    cookie_obj = CookieJar(headers)
    cookie_name, cookie_value = 'username', 'admin'
    cookie_obj[cookie_name] = cookie_value
    assert headers[cookie_name].value == cookie_value


# Generated at 2022-06-14 07:06:47.735866
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    response_headers = MultiHeader()
    cookies = CookieJar(response_headers)
    cookies["foo"] = "bar"
    assert response_headers["Set-Cookie"]["foo"] == "bar"
    assert cookies["foo"].value == "bar"

    del cookies["foo"]

    assert "Set-Cookie" not in response_headers
    with pytest.raises(KeyError):
        cookies["foo"]

# Generated at 2022-06-14 07:06:53.552389
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = {}
    cookie = CookieJar(headers)
    cookie["key"] = "value"
    assert len(headers) == 1
    assert headers == {"Set-Cookie": "key=value; Path=/"}


# Generated at 2022-06-14 07:07:00.360925
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key='mycookie', value='myvalue')
    cookie['max-age'] = DEFAULT_MAX_AGE
    cookie['secure'] = True
    cookie['expires'] = datetime.now()
    expected_str = 'mycookie=myvalue; Max-Age=0; Secure; Expires=%s' % cookie['expires'].strftime(
        "%a, %d-%b-%Y %T GMT"
    )
    assert expected_str == str(cookie)

# Generated at 2022-06-14 07:07:05.089229
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar({})
    assert {} == cookies

    cookies['key'] = 'value'
    assert 1 == len(cookies)
    cookies.__delitem__('key')
    assert {} == cookies


# Generated at 2022-06-14 07:07:09.571464
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    assert cookie["path"] == "/"
    cookie["max-age"] = "eight"
    assert cookie["max-age"] == "eight"


# Generated at 2022-06-14 07:07:17.289250
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    assert headers[0] == ""
    cookie_jar["key1"] = "value1"
    cookie_jar["key2"] = "value2"
    assert "Set-Cookie" in headers.keys()
    assert len(headers["Set-Cookie"]) == 2
    del cookie_jar["key2"]
    assert "Set-Cookie" in headers.keys()
    assert len(headers["Set-Cookie"]) == 1
    assert "key1" in cookie_jar
    assert "key2" not in cookie_jar
    del cookie_jar["key1"]
    assert "key1" not in cookie_jar
    assert not headers["Set-Cookie"]

