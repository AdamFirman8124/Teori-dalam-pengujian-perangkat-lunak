

# Generated at 2022-06-14 06:57:41.543833
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar(MultiDict())
    # Delete a cookie that doesn't exist
    cookie_jar['cookie1'] = 'test'
    del cookie_jar['cookie1']
    assert cookie_jar.get('cookie1') is None

    # Delete a cookie that does exist
    cookie_jar['cookie2'] = 'test'
    assert cookie_jar.get('cookie2') is not None
    del cookie_jar['cookie2']
    assert cookie_jar.get('cookie2') is None

# Generated at 2022-06-14 06:57:48.648328
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiDict()
    cookies = CookieJar(headers)

    # The following line raises an error if the cookie name is a reserved word
    cookies["expires"] = "test"

    # The following line raises an error if the cookie name contains illegal characters
    cookies["test!"] = "test"

    assert '"test"' == cookies["expires"]


# ------------------------------------------------------------ #
#  MultiDict
# ------------------------------------------------------------ #


# Generated at 2022-06-14 06:58:01.202981
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()

    # case 1: cookie exists
    cookie_jar = CookieJar(headers)
    cookie_jar["test1"] = "1"
    assert "test1" in cookies
    assert cookies["test1"].value == "1"
    assert headers.get("Set-Cookie") == "test1=1; Path=/; Domain=; Version=1"
    del cookies["test1"]
    assert "test1" not in cookies
    assert headers.get("Set-Cookie") == "test1=; Path=/; Max-Age=0"
    headers.clear()
    cookie_jar.clear()

    # case 2: cookie does not exist
    cookie_jar = CookieJar(headers)
    assert "test1" not in cookies
    del cookies["test1"]
    assert "test1" not in cookies


# Generated at 2022-06-14 06:58:02.480605
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    pass


# Generated at 2022-06-14 06:58:13.307846
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Create a sample Cookie object
    sampleCookie = Cookie("sampleCookie", "sampleValue")
    sampleCookie["expires"] = datetime.now()
    sampleCookie["max-age"] = 100
    sampleCookie["path"] = "/"
    sampleCookie["domain"] = "www.domain.com"
    sampleCookie["comment"] = "Sample comment"
    sampleCookie["version"] = 1
    sampleCookie["secure"] = True
    sampleCookie["httponly"] = True
    sampleCookie["samesite"] = "lax"
    # Test if the string is as expected

# Generated at 2022-06-14 06:58:26.213683
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import pytest
    from datetime import timedelta
    #import datetime

    # test normal cookie
    cookie = Cookie("test_key", "test_value")
    assert str(cookie) == 'test_key="test_value"'

    # test with different fields
    cookie["path"] = "/"
    assert str(cookie) == 'test_key="test_value"; Path="/"'
    cookie["domain"] = "localhost"
    assert str(cookie) == 'test_key="test_value"; Path="/" ; Domain="localhost"'
    cookie["secure"] = True
    assert str(cookie) == 'test_key="test_value"; Path="/" ; Domain="localhost"; Secure'
    cookie["httponly"] = True

# Generated at 2022-06-14 06:58:31.697445
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    cookie["domain"] = "example.com"
    cookie["path"] = "/"
    cookie["max-age"] = 3600
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 1
    cookie["comment"] = "foobar"
    cookie["samesite"] = "strict"

    assert (
        str(cookie)
        == "foo=bar; Path=/; Max-Age=3600; Domain=example.com; Secure; HttpOnly; Version=1; SameSite=strict; Comment=foobar"
    )



# Generated at 2022-06-14 06:58:45.367346
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cookie_jar = CookieJar(headers)
    print("cookie_jar:", cookie_jar)
    cookie_jar["name"] = "Dongxu"
    cookie_jar["age"] = "24"
    cookie_jar["gender"] = "male"
    print("cookie_jar:", cookie_jar)
    cookie_jar.__delitem__("age")
    print("cookie_jar:", cookie_jar)
    print("headers:", headers)
    cookie_jar.__delitem__("name")
    print("cookie_jar:", cookie_jar)
    print("headers:", headers)
    cookie_jar.__delitem__("gender")
    print("cookie_jar:", cookie_jar)
    print("headers:", headers)


# Generated at 2022-06-14 06:58:52.107405
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {}
    cookies = CookieJar(headers)
    cookie = Cookie("name", "value")
    cookies.cookie_headers = {"name": "Set-Cookie"}
    cookies.headers["Set-Cookie"] = cookie
    cookies["name"] = "value"
    assert "Set-Cookie" in cookies.headers
    cookies.__delitem__("name")
    assert "name" not in cookies.cookie_headers


# Generated at 2022-06-14 06:58:55.265917
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar({})
    cookies["test"] = "test"

    assert cookies.get('test') is not None

    del cookies["test"]

    assert cookies.get('test') is None



# Generated at 2022-06-14 06:58:59.630637
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('Hello', 'world')
    cookie['max-age'] = 'hi'
    assert cookie['max-age'] == 'hi'


# Generated at 2022-06-14 06:59:03.471964
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers({"Content-Type":"text/html"})
    cookies = CookieJar(headers)
    cookies["name"] = "hello"
    assert cookies["name"].value == "hello"


# Generated at 2022-06-14 06:59:16.337567
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "key"
    value = "value"

    # def __init__(self, key, value, max_age=None, expires=None, path='/',
    #              domain=None, secure=False, httponly=False,
    #              samesite=None, comment=None):

    # set max_age and expires
    max_age_test = 1000
    expires_test = datetime.now()
    cookie_test1 = Cookie(key, value)
    cookie_test1["max-age"] = max_age_test
    cookie_test1["expires"] = expires_test
    # should return "key=value; Max-Age=1000; Expires={{datetime}}"

# Generated at 2022-06-14 06:59:27.793612
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    header = MultiHeader("Set-Cookie")
    header.add("Set-Cookie", "name=value; SameSite=Lax")
    jar = CookieJar(header)

    jar.headers["Set-Cookie"] = header
    assert jar.headers["Set-Cookie"] == "name=value; SameSite=Lax"
    jar.cookie_headers["name"] = "Set-Cookie"
    assert jar.cookie_headers['name'] == "Set-Cookie"
    assert jar["name"].value == "value"

    del jar["name"]
    assert jar.headers["Set-Cookie"] == ""
    assert jar.cookie_headers['name'] == ""
    assert jar.get("name") is None


# Generated at 2022-06-14 06:59:40.848173
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('key', 'value')
    assert str(cookie) == "key=value"

    cookie['max-age'] = 0
    cookie['expires'] = datetime(1970, 1, 1, 0, 0, 0)
    cookie['path'] = '/'
    cookie['comment'] = 'comment'
    cookie['domain'] = 'domain'
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['version'] = 'version'
    cookie['samesite'] = 'samesite'

    assert str(cookie) == \
        "key=value; Max-Age=0; expires=Thu, 01-Jan-1970 00:00:00 GMT; Path=/;" \
        " Comment=comment; Domain=domain; Secure; HttpOnly; Version=version; SameSite=samesite"

# Generated at 2022-06-14 06:59:49.759084
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()

    c = CookieJar(headers)

    c["foo"] = "bar"
    assert c["foo"] == "bar"

    headers.add("Foo", "hi")

    c["foo"] = "bar"
    assert c["foo"] == "bar"
    assert headers["Set-Cookie"] == "foo=bar"

    c["foo"] = "bar2"
    assert c["foo"] == "bar2"
    assert headers["Set-Cookie"] == "foo=bar2"



# Generated at 2022-06-14 07:00:01.385536
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers({"Content-Type": "text/plain"})
    jar = CookieJar(headers)
    jar["key-1"] = "value-1"
    jar["key-2"] = "value-2"
    del jar["key-1"]
    assert jar["key-1"]["max-age"] == DEFAULT_MAX_AGE
    assert "value-1" not in jar
    assert "key-1" not in jar
    assert "key-2" in jar
    del jar["key-2"]
    assert jar["key-2"]["max-age"] == DEFAULT_MAX_AGE
    assert "value-2" not in jar
    assert "key-2" not in jar
    assert "Set-Cookie" not in jar.headers



# Generated at 2022-06-14 07:00:03.388041
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('foo', 'bar')
    assert str(cookie) == 'foo=bar'


# Generated at 2022-06-14 07:00:11.218949
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    assert (cookie_jar == {})
    cookie_jar["name"] = "value"
    assert (cookie_jar == {"name": "value"})
    assert (cookie_jar.headers == {"Set-Cookie": ["name=value; Path=/"]})
    assert (cookie_jar.cookie_headers == {"name": "Set-Cookie"})



# Generated at 2022-06-14 07:00:18.033897
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Create an instance of CookieJar
    cj: CookieJar = CookieJar({})
    cj["cookie_1"] = "cookie_1"
    del cj["cookie_1"]
    assert "cookie_1" not in cj

    # If key is not existed, create a new cookie (with value = "" and max-age = 0)
    del cj["cookie_2"]
    assert "cookie_2" not in cj


# Generated at 2022-06-14 07:00:32.485019
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("test", "1")
    assert str(c) == "test=1"
    c["max-age"] = 123
    c["path"] = "/"
    assert sorted(str(c).split("; ")) == ['max-age=123', 'path=/', 'test=1']


# Generated at 2022-06-14 07:00:43.783883
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    target = Cookie('foo', 'bar')
    assert str(target) == 'foo=bar'

    target = Cookie('foo', 'bar')
    target['path'] = '/'
    assert str(target) == 'foo=bar; Path=/'

    target = Cookie('foo', 'bar')
    target['path'] = 'a<b'
    assert str(target) == 'foo=bar; Path="a<b"'
    target = Cookie('foo', 'bar')
    target['max-age'] = 0
    assert str(target) == 'foo=bar; Max-Age=0'

    target = Cookie('foo', 'bar')
    target['expires'] = datetime(1970, 1, 1, 1, 1, 1)

# Generated at 2022-06-14 07:00:52.340111
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import datetime
    cookie = Cookie("myCookie", "myCookieValue")
    s = str(cookie)
    assert s == "myCookie=myCookieValue"

    cookie["max-age"] = "5"
    s = str(cookie)
    assert s == "myCookie=myCookieValue; Max-Age=5"

    cookie["expires"] = datetime.datetime(2019, 12, 26)
    s = str(cookie)
    assert s == "myCookie=myCookieValue; Max-Age=5; Expires=Sat, 26-Dec-2019 00:00:00 GMT"

    cookie["secure"] = True
    s = str(cookie)

# Generated at 2022-06-14 07:01:05.388705
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers([('Content-Type', 'text/html')])
    cookies = CookieJar(headers)
    cookies['key1'] = 'value1'
    cookies['key2'] = 'value2'
    assert 'key1=value1' in cookies['key1'].encode('utf-8')
    assert 'key2=value2' in cookies['key2'].encode('utf-8')
    cookies.__delitem__('key1')
    assert not cookies.get('key1')
    cookies.__delitem__('key2')
    assert not cookies.get('key2')

if __name__ == '__main__':
    test_CookieJar___delitem__()

# Generated at 2022-06-14 07:01:13.597855
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test_Cookie___setitem__", "test")
    cookie["path"] = "/"
    cookie["expires"] = datetime.utcnow()
    cookie["size"] = "123"
    assert len(cookie) == 3
    assert cookie["size"] == "123"
    assert cookie["path"] == "/"
    cookie["size"] = None
    assert len(cookie) == 2
    assert cookie["size"] is None
    assert cookie["path"] == "/"



# Generated at 2022-06-14 07:01:22.010302
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["name"] = "Bob"
    assert jar["name"] == "Bob"
    assert "name" in jar
    assert headers["Set-Cookie"] == "name=Bob; Path=/; HttpOnly; SameSite=Strict"
    del jar["name"]
    assert "name" not in jar
    assert headers["Set-Cookie"] == "name=; Max-Age=0; Path=/; HttpOnly; SameSite=Strict"



# Generated at 2022-06-14 07:01:29.754610
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookieJar = CookieJar( headers=dict() )
    
    cookieHeaderKey = "Set-Cookie"
    cookieKey = "foo"
    cookieValue = "bar"
    cookieJar[cookieKey] = cookieValue
    assert len(cookieJar) == 1
    assert len(cookieJar.headers) == 1

    del cookieJar[cookieKey]
    assert len(cookieJar) == 0
    assert len(cookieJar.headers) == 0



# Generated at 2022-06-14 07:01:39.755550
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    test_cookie = Cookie("hello", "world")
    assert test_cookie.__str__() == 'hello=world'
    test_cookie['max-age'] = 100
    assert test_cookie.__str__() == 'hello=world; Max-Age=100'
    test_cookie['path'] = 'abc'
    assert test_cookie.__str__() == 'hello=world; Max-Age=100; Path=abc'
    test_cookie['domain'] = 'example.com'
    assert test_cookie.__str__() == 'hello=world; Max-Age=100; Path=abc; Domain=example.com'
    test_cookie['comment'] = 'hello comment'

# Generated at 2022-06-14 07:01:53.258807
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_1 = Cookie("cookie_1", "cookie_1_value")
    cookie_1["domain"] = "localhost"
    cookie_jar["cookie_1"] = cookie_1
    cookie_2 = Cookie("cookie_2", "cookie_2_value")
    cookie_2["domain"] = "localhost"
    cookie_jar["cookie_2"] = cookie_2
    cookie_3 = Cookie("cookie_3", "cookie_3_value")
    cookie_3["domain"] = "localhost"
    cookie_jar["cookie_3"] = cookie_3
    del cookie_jar["cookie_2"]

# Generated at 2022-06-14 07:02:04.172623
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "cookie_name"
    cookie = Cookie(key, "cookie_value")
    assert str(cookie) == f"{key}={_quote('cookie_value')}"
    cookie["secure"] = True
    assert str(cookie) == f"{key}={_quote('cookie_value')}; Secure"
    cookie["secure"] = False
    cookie["expires"] = datetime(2020, 9, 2)
    assert str(cookie) == f"{key}={_quote('cookie_value')}; expires=Wed, 02-Sep-2020 00:00:00 GMT"
    cookie["path"] = "/"
    cookie["secure"] = True
    cookie["HttpOnly"] = True

# Generated at 2022-06-14 07:02:45.269697
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test function for method __str__ of class Cookie
    """
    assert 'test=test' == str(Cookie('test', 'test'))
    assert 'test=test; HttpOnly; Secure' == str(Cookie('test', 'test'))
    assert 'test=test; HttpOnly; Secure' == str(Cookie('test', 'test'))
    assert 'test=test; HttpOnly; Secure; Path=/' == str(Cookie('test', 'test'))
    assert 'test=test; HttpOnly; Secure; Path=/' == str(Cookie('test', 'test'))
    assert 'test=test; HttpOnly; Secure; Path=/' == str(Cookie('test', 'test'))

# Generated at 2022-06-14 07:02:57.722228
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    # Test case 1: key already exists (we assume key is legal)
    # If this cookie doesn't exist, add it to the header keys
    dict1 = CookieJar(headers)
    dict1['something'] = "hello!"
    assert dict1['something'] == "hello!"
    assert dict1.headers.get("Set-Cookie") == "something=hello!"
    # Test case 2: key does not already exist (we assume key is legal)
    dict2 = CookieJar(headers)
    dict2['something'] = "hello!"
    assert dict2['something'] == "hello!"
    assert dict2.headers.get("Set-Cookie") == "something=hello!"


# Generated at 2022-06-14 07:03:08.003571
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test the __str__ method of the Cookie class.
    """
    from datetime import datetime

    cookie = Cookie(
        "c", "test"
    )  # 'test' should be quoted as it is not a legal char
    assert str(cookie) == "c=test"

    # Test flag and basic
    cookie = Cookie("c", "test")
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = "1"
    assert str(cookie) == "c=test; HTTPOnly; Secure; Version=1"

    # Test basic args in a different order, should still work
    cookie = Cookie("c", "test")
    cookie["version"] = "1"
    cookie["secure"] = True
    cookie["httponly"] = True

# Generated at 2022-06-14 07:03:20.368234
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cs = CookieJar(headers)
    cs['a'] = '1'
    cs['b'] = '2'
    print(headers)
    assert headers == CIMultiDict([('Set-Cookie', 'a=1'), ('Set-Cookie', 'b=2')])
    cs.__delitem__('b')
    print(headers)
    assert headers == CIMultiDict([('Set-Cookie', 'a=1')])
    cs['b'] = '2'
    cs.__delitem__('b')
    cs.__delitem__('b')
    print(headers)
    assert headers == CIMultiDict([('Set-Cookie', 'a=1')])

# Generated at 2022-06-14 07:03:33.937252
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():

    def _basic_test(key, value, expected):
        # Test the basic function
        c = Cookie(key, value)
        actual = c.__str__()
        assert actual == expected

    def _advanced_test(key, value, max_age, path, expected):
        # Test the advanced function
        c = Cookie(key, value)
        c["max-age"] = max_age
        c["path"] = path
        actual = c.__str__()
        assert actual == expected

    _basic_test("good_name", "good_value", "good_name=good_value")
    _advanced_test(
        "good_name", "good_value", 86400, "/", "good_name=good_value; Max-Age=86400; Path=/"
    )


# ------------------------------------------------------------

# Generated at 2022-06-14 07:03:45.091156
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("cookieKey", "cookieValue")
    print('cookie.__str__() = "%s"' % cookie.__str__())
    cookie["max-age"] = 0
    print('cookie.__str__() = "%s"' % cookie.__str__())
    cookie["expires"] = datetime(2020, 1, 27, 13, 30)
    print('cookie.__str__() = "%s"' % cookie.__str__())
    cookie["secure"] = True
    print('cookie.__str__() = "%s"' % cookie.__str__())
    cookie["httponly"] = True
    print('cookie.__str__() = "%s"' % cookie.__str__())
    cookie["samesite"] = "Strict"
    print('cookie.__str__() = "%s"' % cookie.__str__())

# Generated at 2022-06-14 07:03:54.379948
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    key1 = "name1"
    value1 = "value1"
    key2 = "name2"
    value2 = "value2"
    mh = MultiHeader("Set-Cookie", k1=key1, v1=value1, k2=key2, v2=value2)
    # case 1: delete first cookie
    cj = CookieJar(headers)
    cj.cookie_headers = {key1: mh, key2: mh}
    cj[key1] = value1
    cj[key2] = value2
    cj.headers.add(mh)
    del(cj[key1])
    assert key1 not in cj.cookie_headers
    assert key2 in cj.cookie_headers

# Generated at 2022-06-14 07:04:08.436851
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    mock_expires = datetime(1968, 4, 4, 16, 16, 16)
    cookie = Cookie(key='key', value='value')
    cookie['path'] = '/'
    cookie['domain'] = 'test.com'
    cookie['max-age'] = '42'
    cookie['expires'] = mock_expires
    cookie['httponly'] = False
    cookie['secure'] = False
    cookie['version'] = '1'
    cookie['comment'] = 'It\'s just a test'
    cookie['samesite'] = 'Strict'


# Generated at 2022-06-14 07:04:18.645009
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    # Test Case 1: correct cookie
    cookiejar = CookieJar({})
    cookiejar["lang"] = "fr"
    # print(cookiejar)
    assert cookiejar["lang"] == "fr"
    assert cookiejar.headers["Set-Cookie"] == "lang=fr; Path=/\n"
    
    # Test Case 2: incorrect cookie name
    cookiejar = CookieJar({})
    cookiejar["l"] = "fr"
    # print(cookiejar)
    assert cookiejar.headers["Set-Cookie"] is None
    
    # Test Case 3: incorrect cookie value
    cookiejar = CookieJar({})
    cookiejar["lang"] = "<script>alert('hi')</script>"
    # print(cookiejar)

# Generated at 2022-06-14 07:04:27.653005
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookie_jar = CookieJar(headers)
    cookie_jar["hello"] = "world"
    headers["X-Custom"] = "Custom Value"
    assert headers["X-Custom"] == "Custom Value"
    assert headers["Set-Cookie"] == "hello=world; Path=/; Max-Age=0"
    del cookie_jar["hello"]
    with pytest.raises(KeyError) as e:
        assert headers["Set-Cookie"]
    with pytest.raises(KeyError) as e:
        assert headers["X-Custom"]



# Generated at 2022-06-14 07:05:01.623234
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    h = MultiHeaders()
    c = CookieJar(h)
    c["one"] = "1"
    c["two"] = "2"
    c["three"] = "3"
    assert h.getall("Set-Cookie") == ['one=1; Path=/', 'two=2; Path=/',
                                      'three=3; Path=/']
    del c["three"]
    assert h.getall("Set-Cookie") == ['one=1; Path=/', 'two=2; Path=/']
    assert c.getall("Set-Cookie") == []



# Generated at 2022-06-14 07:05:13.776219
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test the method Cookie.__str__().
    """

    cookie = Cookie('cookie_name', 'cookie_value')
    assert (
        str(cookie) == "cookie_name=cookie_value"
    ), "Test basic cookie encoding."

    cookie["path"] = "/"
    assert (
        str(cookie) == "cookie_name=cookie_value; Path=/"
    ), "Test path property."

    cookie["max-age"] = 100
    assert (str(cookie) == "cookie_name=cookie_value; Path=/; Max-Age=100"), "Test max-age property."

    cookie["expires"] = datetime(2020, 3, 8, 16, 38, 14, 0)

# Generated at 2022-06-14 07:05:20.959705
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # basic test
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

    # test reserved keys
    cookie["expires"] = 1445641500
    assert str(cookie) == "key=value; Expires=Sat, 24-Oct-2015 20:55:00 GMT"

    # test default values of reserved keys
    cookie["max-age"] = 0
    assert str(cookie) == "key=value; Max-Age=0"

    # test flags
    cookie["secure"] = True
    assert str(cookie) == "key=value; Max-Age=0; Secure"


# Generated at 2022-06-14 07:05:31.412765
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Testing when cookie exists in the headers
    headers = Headers()
    headers.add("Set-Cookie", "cookie_name=cookie_value")
    cookie_jar = CookieJar(headers)

    cookie_jar["cookie_name"] = "new_cookie_value"
    assert cookie_jar["cookie_name"] == "new_cookie_value"
    assert headers["Set-Cookie"] == "cookie_name=new_cookie_value"

    del cookie_jar["cookie_name"]
    assert "cookie_name" not in cookie_jar
    assert "cookie_name=" not in headers["Set-Cookie"]


# Generated at 2022-06-14 07:05:38.444132
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    jar = CookieJar(headers)
    cookie1 = Cookie("n1", "v1")
    cookie2 = Cookie("n2", "v2")
    cookie1["path"] = "/"
    cookie2["path"] = "/"
    jar.headers.add("Set-Cookie", cookie1)
    jar.headers.add("Set-Cookie", cookie2)
    jar["n1"] = "v1"
    jar["n2"] = "v2"
    # delete n1
    del jar["n1"]
    assert "n1" not in jar.cookie_headers
    assert "n1" not in jar
    assert headers.popall("Set-Cookie") == ["n2=v2; Path=/"], "delete n1"
    # delete n2
    del jar

# Generated at 2022-06-14 07:05:51.272525
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

    cookie = Cookie("key", "value")
    cookie["max-age"] = DEFAULT_MAX_AGE
    assert str(cookie) == "key=value; Max-Age=0"

    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    assert str(cookie) == "key=value; Path=/"

    cookie = Cookie("key", "value")
    cookie["comment"] = "Comment"
    assert str(cookie) == "key=value; Comment=Comment"

    cookie = Cookie("key", "value")
    cookie["domain"] = "Domain"
    assert str(cookie) == "key=value; Domain=Domain"

    cookie = Cookie("key", "value")
    cookie["secure"] = True

# Generated at 2022-06-14 07:06:02.904247
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name', 'value')
    assert 'name=value' == str(cookie)
    cookie['secure'] = True
    assert 'name=value; Secure' == str(cookie)
    cookie['path'] = '/path'
    assert 'name=value; Secure; Path=/path' == str(cookie)
    cookie['domain'] = 'example.com'
    assert 'name=value; Domain=example.com; Secure; Path=/path' == str(cookie)
    cookie['max-age'] = 120
    assert 'name=value; Max-Age=120; Domain=example.com; Secure; Path=/path' == str(cookie)


# Generated at 2022-06-14 07:06:13.276933
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = HeaderMap()
    cookie_key1 = "deleteme1"
    cookie_key2 = "deleteme2"
    cookie_key3 = "deleteme3"
    cookie_value = "cookie_value"
    cookie_path = "/"
    cookie_maxage = "0"
    
    cookie_jar = CookieJar(headers)
    cookie1 = Cookie(cookie_key1, cookie_value)
    cookie2 = Cookie(cookie_key2, cookie_value)
    cookie3 = Cookie(cookie_key3, cookie_value)
    cookie1["path"] = cookie_path
    cookie2["path"] = cookie_path
    cookie3["path"] = cookie_path
    cookie1["max-age"] = cookie_maxage
    cookie2["max-age"] = cookie_maxage
    cookie

# Generated at 2022-06-14 07:06:26.068395
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import pytest
    test_Cookie = Cookie('name', 'value')
    assert test_Cookie.__str__() == 'name=value'

    test_Cookie['expires'] = datetime(2019, 12, 24, 15, 34, 21)
    assert test_Cookie.__str__() == 'name=value; Expires=Tue, 24-Dec-2019 15:34:21 GMT'

    test_Cookie['expires'] = datetime(2020, 1, 7, 17, 21, 12)
    assert test_Cookie.__str__() == 'name=value; Expires=Tue, 07-Jan-2020 17:21:12 GMT'

    test_Cookie['max-age'] = 12345

# Generated at 2022-06-14 07:06:28.348263
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('name', 'value')
    cookie['max-age'] = 100
    assert cookie['max-age'] == 100

