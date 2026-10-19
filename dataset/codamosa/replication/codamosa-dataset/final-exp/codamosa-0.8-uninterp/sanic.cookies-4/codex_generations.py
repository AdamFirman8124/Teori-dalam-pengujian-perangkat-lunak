

# Generated at 2022-06-14 06:57:29.095578
# Unit test for method encode of class Cookie
def test_Cookie_encode():
    cookie = Cookie("username", "bob")
    assert cookie.encode("utf-8") == b"username=bob"
    assert cookie.encode("latin1") == b"username=bob"
    cookie = Cookie("username", "å∫ç")
    assert cookie.encode("utf-8") == b"username=\xc3\xa5\xe2\x88\xab\xc3\xa7"
    assert cookie.encode("latin1") == b"username=\xe5\x88\xab\xe7"



# Generated at 2022-06-14 06:57:38.955561
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import time

    # given
    cookie_value = "test"

    # when
    cookie = Cookie("test", cookie_value)
    # and
    cookie["domain"] = "www.test.com"
    # and
    cookie["max-age"] = 60
    # and
    cookie["path"] = "/test"
    # and
    cookie["secure"] = True
    # and
    cookie["version"] = 1
    # and
    cookie["expires"] = datetime.utcfromtimestamp(time.time() + 60)
    # and
    cookie["comment"] = "this is a comment"
    # and
    cookie["httponly"] = True
    # and
    cookie["samesite"] = "strict"
    # and

# Generated at 2022-06-14 06:57:46.330534
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict()
    cookiejar = CookieJar(headers)
    cookiejar["Python"] = "best lang ever"
    assert headers["Set-Cookie"] == "Python=best lang ever; Path=/; Max-Age=0"
    cookiejar["Java"] = "worst lang ever"
    assert headers["Set-Cookie"] == "Java=worst lang ever; Path=/; Max-Age=0"
    # what if they're the same??
    cookiejar["Python"] = "best lang ever"
    assert headers["Set-Cookie"] == "Python=best lang ever; Path=/; Max-Age=0"
    assert len(headers["Set-Cookie"]) == 1



# Generated at 2022-06-14 06:57:54.006215
# Unit test for method encode of class Cookie
def test_Cookie_encode():
    cookie = Cookie(key='session_id', value='secret')
    try:
        encoded_cookie = cookie.encode(encoding='utf-8')
    except UnicodeEncodeError:
        assert False, 'encoding must not throw error'
    assert encoded_cookie == b'session_id=secret', 'encoded value must be b\'session_id=secret\''


# Generated at 2022-06-14 06:58:03.598472
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    h = DictHeaders(0)
    j = CookieJar(h)
    cookie0 = Cookie("Cookie0", "value0")
    cookie1 = Cookie("Cookie1", "value1")
    cookie2 = Cookie("Cookie2", "value2")
    j.headers.add("Set-Cookie", cookie0)
    j.headers.add("Set-Cookie", cookie1)
    j.headers.add("Set-Cookie", cookie2)
    j.cookie_headers = {"Cookie0": "Set-Cookie", "Cookie1": "Set-Cookie", "Cookie2": "Set-Cookie"}
    j._update()

# Generated at 2022-06-14 06:58:17.679874
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    # print(cookie)
    cookie["expires"] = datetime.utcnow()
    # print(cookie)
    cookie["secure"] = False
    # print(cookie)
    cookie["secure"] = True
    # print(cookie)
    cookie["max-age"] = 0
    # print(cookie)
    cookie["max-age"] = 1
    # print(cookie)
    cookie["max-age"] = "2"
    # print(cookie)
    cookie["max-age"] = "a"
    # print(cookie)
    cookie["path"] = "/path/to"
    # print(cookie)
    cookie["httponly"] = True
    # print(cookie)
    cookie["samesite"] = "strict"
    # print(cookie)
    cookie

# Generated at 2022-06-14 06:58:20.297340
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    assert cookie["path"] == "/"


# Generated at 2022-06-14 06:58:25.142748
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "val")
    print(cookie["expires"])
    cookie["expires"] = "123"
    print(cookie["expires"])
    cookie["expires"] = datetime(2019,5,5)
    print(cookie["expires"])
test_Cookie___setitem__()


# Generated at 2022-06-14 06:58:34.664204
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():

    # Set-Cookie: bar=baz; Secure; HttpOnly; path=/; expires=Wed, 21-Oct-2020 07:28:00 GMT
    cookie = Cookie("bar", "baz")
    cookie["path"] = "/"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["expires"] = datetime(2020, 10, 21, 7, 28, 0)

    assert str(cookie) == (
        "bar=baz; Path=/; Secure; HttpOnly; "
        "expires=Wed, 21-Oct-2020 07:28:00 GMT"
    )



# Generated at 2022-06-14 06:58:42.161515
# Unit test for method encode of class Cookie
def test_Cookie_encode():
    c = Cookie(key="key", value="value")
    if c.encode("utf-8").decode("utf-8") != "key=value":
        raise AssertionError("encode method of Cookie class failed")
    else:
        print("Cookie encode() method works fine")

test_Cookie_encode()

# ------------------------------------------------------------ #
#  Tests
# ------------------------------------------------------------ #



# Generated at 2022-06-14 06:58:52.107039
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader(2)
    myCookieJar = CookieJar(headers)
    cookieName = "test"
    myCookieJar[cookieName] = "test"
    assert cookieName in myCookieJar.cookie_headers
    del myCookieJar[cookieName]
    assert not cookieName in myCookieJar.cookie_headers
    assert not cookieName in myCookieJar


# Generated at 2022-06-14 06:59:03.282343
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test", "test")
    cookie["max-age"] = 15
    assert cookie["max-age"] == 15
    cookie["max-age"] = "15"
    assert cookie["max-age"] == "15"
    cookie["expires"] = datetime.now()
    assert isinstance(cookie["expires"], datetime)
    with pytest.raises(TypeError) as excinfo:
        cookie["expires"] = "test"
    assert 'must be a datetime' in str(excinfo.value)
    with pytest.raises(KeyError) as excinfo:
        cookie["test"] = 15
    assert 'Unknown cookie property' in str(excinfo.value)
    with pytest.raises(KeyError) as excinfo:
        cookie["path"] = 15

# Generated at 2022-06-14 06:59:16.187718
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Testing output
    cookie = Cookie("test", "1234")
    assert str(cookie) == "test=1234"

    # Testing output with a space
    cookie = Cookie("test cookie", "4321")
    assert str(cookie) == "test cookie=4321"

    # Testing output with a semi-colon
    cookie = Cookie("test;cookie", "4321")
    assert str(cookie) == 'test\\;cookie=4321'

    # Testing output with an ampersand
    cookie = Cookie("test&cookie", "4321")
    assert str(cookie) == 'test\\&cookie=4321'

    # Testing output with an double quote
    cookie = Cookie("test\"cookie", "4321")
    assert str(cookie) == 'test\\"cookie=4321'

    # Testing output with an backslash

# Generated at 2022-06-14 06:59:20.326976
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    key = "key"
    value = "value"
    cookie = Cookie(key, value)

    assert cookie.key == key
    assert cookie.value == value
    assert cookie["key"] == key
    assert cookie["value"] == value


# Generated at 2022-06-14 06:59:32.765538
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    test_cookie = Cookie('test', 'test')
    assert str(test_cookie) == 'test=test'
    test_cookie['Expires'] = 'Tue, 01 Feb 2018 08:30:00 GMT'
    assert str(test_cookie) == 'test=test; Expires=Tue, 01 Feb 2018 08:30:00 GMT'
    test_cookie['Max-Age'] = 5
    assert str(test_cookie) == 'test=test; Max-Age=5; Expires=Tue, 01 Feb 2018 08:30:00 GMT'
    test_cookie['Secure'] = True
    assert str(test_cookie) == 'test=test; Max-Age=5; Expires=Tue, 01 Feb 2018 08:30:00 GMT; Secure'

# Generated at 2022-06-14 06:59:40.163805
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["test_cookie"] = "value"
    assert headers["Set-Cookie"] == "test_cookie=value"
    del cookie_jar["test_cookie"]
    assert headers["Set-Cookie"] == "test_cookie=; Max-Age=0"
    assert not headers.getall("Cookie")


# Generated at 2022-06-14 06:59:52.419373
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    
    # Case 0: Test deleting a cookie by key
    cookie_jar = CookieJar(headers)
    cookie_jar["cookie"] = "value"
    assert headers.getall("Set-Cookie") == ["cookie=value; Path=/; Max-Age=0"]
    del cookie_jar["cookie"]
    assert headers.getall("Set-Cookie") == []

    # Case 1: Test deleting a cookie by key when there are multiple cookies with different keys
    cookie_jar = CookieJar(headers)
    cookie_jar["cookie"] = "value"
    assert headers.getall("Set-Cookie") == ["cookie=value; Path=/; Max-Age=0"]
    cookie_jar["cookie2"] = "value2"

# Generated at 2022-06-14 07:00:02.988016
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():

    def __delitem__(self, key):
        if key not in self.cookie_headers:
            self[key] = ""
            self[key]["max-age"] = 0
        else:
            cookie_header = self.cookie_headers[key]
            # remove it from header
            cookies = self.headers.popall(cookie_header)
            for cookie in cookies:
                if cookie.key != key:
                    self.headers.add(cookie_header, cookie)
            del self.cookie_headers[key]
            return super().__delitem__(key)

    # ------------------------ #
    # Unit test code starts here
    # ------------------------ #
    # 1. Create an instance of the class (I use `cookiejar` as the variable name)
    cookiejar = CookieJar()
    # 2. Set a value (I use

# Generated at 2022-06-14 07:00:12.388484
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    cookie["max-age"] = 1
    assert cookie["max-age"] == 1
    cookie["expires"] = datetime.now()
    assert isinstance(cookie["expires"], datetime)
    try:
        cookie["expires"] = "string"
    except TypeError:
        pass
    else:
        assert False, "Should throw TypeError"
    cookie["max-age"] = "string"
    assert "max-age" not in cookie, "Should not set max-age to 'string'"

# Generated at 2022-06-14 07:00:20.769872
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import pytest


# Generated at 2022-06-14 07:00:31.470971
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    # Arrange
    key = "SomeKey"
    value = "SomeValue"
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    # Act
    cookie_jar[key] = value
    # Assert
    assert cookie_jar[key].value == value
    assert cookie_jar[key]['path'] == "/"
    assert headers[cookie_jar.header_key][0].value == f"{key}={value}"


# Generated at 2022-06-14 07:00:42.098717
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():

    from datetime import datetime
    from falcon import testing
    import pytest

    # Test creation of cookie
    cookie = Cookie("TestCookieKey", "TestCookieValue")
    assert str(cookie) == "TestCookieKey=TestCookieValue"

    # Test adding and removing of key, value pairs to dictionary
    cookie["TestKey"] = "TestValue"
    assert str(cookie) == "TestCookieKey=TestCookieValue; TestKey=TestValue"

    # Test setting of value as a Cookie object
    cookie["TestKey"] = Cookie("TestKey2", "TestValue2")
    assert (
        str(cookie)
        == "TestCookieKey=TestCookieValue; TestKey2=TestValue2; TestKey=TestKey2"
    )

    # Test setting of value as a list

# Generated at 2022-06-14 07:00:49.802689
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    # Setup
    headers = MultiHeaderDict()
    sut = CookieJar(headers)
    key = "foo"
    value = "bar"

    # Exercise
    sut[key] = value
    actual = sut[key]

    # Verify
    assert actual == value
    assert sut.cookie_headers[key] == "Set-Cookie"
    assert sut.headers["Set-Cookie"][0].value == value
    assert sut.headers["Set-Cookie"][0].key == key


# Generated at 2022-06-14 07:00:55.909588
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from uvicorn.middleware.proxy_headers import ProxyHeaders
    headers = ProxyHeaders({})
    cookie_jar = CookieJar(headers)
    test_cookie = Cookie("test", "test")
    test_cookie["path"] = "/"
    cookie_jar["test"] = test_cookie
    # Test
    del cookie_jar["test"]
    # Assertion
    assert cookie_jar == {}

# Generated at 2022-06-14 07:01:00.548883
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test", "value")
    cookie["expires"] = 0
    assert cookie["expires"] == 0

# ------------------------------------------------------------ #
#  MultiHeader
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:01:10.839393
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from starlette.responses import PlainTextResponse
    from starlette.testclient import TestClient

    test_client = TestClient(app)
    test_client.set_cookie("foo", "bar")
    result = test_client.get("/__cookie_remove_foo")
    assert result.headers["Set-Cookie"] == "foo=; Max-Age=0; Path=/"
    assert result.status_code == 200
    assert result.content == b"foo has been removed"

    result = test_client.get("/__cookie_foo_not_exists")
    assert result.headers["Set-Cookie"] == "foo=; Max-Age=0; Path=/"
    assert result.status_code == 200
    assert result.content == b"foo does not exist"

# Generated at 2022-06-14 07:01:15.319108
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    h = headers.Headers()
    jar = CookieJar(h)
    jar['test'] = 'test'

    # Test if cookie is deleted properly
    jar.__delitem__('test')
    assert 'test' not in jar
    

# Generated at 2022-06-14 07:01:22.909370
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    headers["Set-Cookie"] = ["a=b", "c=d"]
    cookieJar = CookieJar(headers)
    cookieJar["a"] = "b"
    cookieJar["c"] = "d"
    cookieJar["b"] = "c"
    expected = [
        "a=",
        "c=d",
        "b=c",
    ]
    actual = list(headers["Set-Cookie"])
    assert expected == actual



# Generated at 2022-06-14 07:01:35.943755
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    assert str(cookie) == "foo=bar"
    cookie.update({"path": "/", "secure": True, "foo": "bar"})
    assert str(cookie) == "foo=bar; Path=/; Secure"
    cookie = Cookie("foo", "bar")
    cookie["path"] = "/"
    cookie["max-age"] = 100
    assert str(cookie) == "foo=bar; Path=/; Max-Age=100"
    cookie = Cookie("foo", "bar")
    cookie["expires"] = datetime(2020, 1, 1, 12, 12, 12, 12)
    assert str(cookie) == "foo=bar; Expires=Wed, 01-Jan-2020 12:12:12 GMT"
    cookie["comment"] = "comment"

# Generated at 2022-06-14 07:01:41.052360
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('cookie', 'value')
    c['path'] = '/'
    c['max-age'] = 0

    # Note: SimpleCookie.output() adds a trailing '\n'
    assert str(c) == 'cookie=value; Path=/; Max-Age=0'



# Generated at 2022-06-14 07:01:56.178264
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test", "value")
    str(cookie)
    cookie = Cookie("test", "value")
    cookie["path"] = "/"
    str(cookie)
    cookie = Cookie("test", "value")
    cookie["expires"] = datetime(2017, 2, 4, 2, 6, 4, 722774)
    str(cookie)
    cookie = Cookie("test", "value")
    cookie["max-age"] = 0
    str(cookie)
    cookie = Cookie("test", "value")
    cookie["max-age"] = "86400"
    str(cookie)
    cookie = Cookie("test", "value")
    cookie["secure"] = "secure"
    str(cookie)
    cookie = Cookie("test", "value")
    cookie["secure"] = True
    str(cookie)

# Unit

# Generated at 2022-06-14 07:02:02.724304
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["name"] = "Patrick"
    assert headers["Set-Cookie"] == "name=Patrick; Path=/"
    cookie_jar["name"] = "Patrick"
    assert headers["Set-Cookie"] == "name=Patrick; Path=/"
    cookie_jar["name"] = "Patrick"
    assert headers["Set-Cookie"] == "name=Patrick; Path=/"


# Generated at 2022-06-14 07:02:05.766015
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = dict()
    CookieJar(headers)
    assert headers['Set-Cookie'] == 'key=value; path=/'


# Generated at 2022-06-14 07:02:13.880313
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    ck = Cookie("key", "value")
    ck["domain"] = ".example.com"
    ck["secure"] = True
    ck["httponly"] = True
    ck["max-age"] = 3600
    ck["path"] = "/"

    assert str(ck) == (
        "key=value; Domain=.example.com; Path=/; Max-Age=3600; Secure; " "HttpOnly"
    )



# Generated at 2022-06-14 07:02:21.291374
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from quart.datastructures import Headers
    headers = Headers()
    cookie_jar = CookieJar(headers)
    cookie_jar["chocolate"] = "chip"
    assert headers.get("Set-Cookie") == "chocolate=chip; Path=/"
    assert cookie_jar[
        "chocolate"
    ].value == "chip"  # test to check if the value has been set correctly


# Generated at 2022-06-14 07:02:33.268917
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from quart import Quart

    app = Quart(__name__)
    headers = app.response_class.default_headers
    jar = CookieJar(headers)
    jar["hi"] = "there"
    cookie = headers.get("Set-Cookie")
    assert "Set-Cookie: hi=there" in cookie
    assert cookie.count("Set-Cookie:") == 1
    jar["what"] = "ever"
    cookie = headers.get("Set-Cookie")
    assert "Set-Cookie: what=ever" in cookie
    assert cookie.count("Set-Cookie:") == 1
    jar["hi"] = "you"
    cookie = headers.get("Set-Cookie")
    assert "Set-Cookie: you=you" in cookie
    assert cookie.count("Set-Cookie:") == 1
    jar

# Generated at 2022-06-14 07:02:35.877823
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    cookie["comment"] = "comment"
    assert cookie["comment"] == "comment"


# Generated at 2022-06-14 07:02:47.238967
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie_str = Cookie("name1", "value1")
    cookie_str["max-age"] = 120
    # print(cookie_str.__str__())
    assert cookie_str.__str__() == "name1=value1; Max-Age=120"

    cookie_datetime = Cookie("name2", "value2")
    cookie_datetime["expires"] = datetime(2018, 10, 11, 10, 10, 10)
    # print(cookie_datetime.__str__())
    assert cookie_datetime.__str__() == "name2=value2; expires=Thu, 11-Oct-2018 10:10:10 GMT"

    cookie_flags = Cookie("name3", "value3")
    cookie_flags["secure"] = True
    cookie_flags["httponly"] = True

# Generated at 2022-06-14 07:02:51.181107
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
  headers = Headers()
  cookies = CookieJar(headers)
  cookies['hello'] = 'world'
  assert 'hello' in cookies
  del cookies['hello']
  assert 'hello' not in cookies

# Generated at 2022-06-14 07:02:58.601233
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    temp_cookie_dict = {}
    temp_cookie_jar = CookieJar(temp_cookie_dict)
    temp_cookie_jar["test_key"] = "test_value"
    try:
        assert (temp_cookie_jar["test_key"].value == "test_value")
    except AssertionError:
        raise AssertionError("test_CookieJar___setitem__ failed")


# Generated at 2022-06-14 07:03:12.635517
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers([])
    cookie_jar = CookieJar(headers)
    cookie_jar["test_key"] = "test_value"
    assert "test_key" in headers.items("Set-Cookie")
    cookie_jar.__delitem__("test_key")
    assert "test_key" not in headers.items("Set-Cookie")

    cookie_jar["test_key"] = "test_value"
    del cookie_jar["test_key"]
    assert "test_key" not in headers.items("Set-Cookie")


# Generated at 2022-06-14 07:03:18.644724
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaders()
    cookie_jar = CookieJar(headers)
    cookie_jar['test'] = 'test'
    assert('test' in cookie_jar)
    cookie_jar.__delitem__('test')
    assert('test' not in cookie_jar)


# Generated at 2022-06-14 07:03:26.408404
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers({"Content-Type": "text/plain"})
    cookie_jar = CookieJar(headers)

    # case 1
    cookie_jar["key"] = "value"
    assert headers["Set-Cookie"] == "key=value; Path=/; Max-Age=0"
    assert cookie_jar["key"] == "value"

    # case 2
    cookie_jar["key"] = 10

# Generated at 2022-06-14 07:03:35.280623
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    print("\n*** Unit Test for CookieJar ***")
    headers = Headers()
    cookieJar = CookieJar(headers)
    cookieJar.__setitem__("cookie1", "value1")
    cookieJar.__setitem__("cookie2", "value2")
    del cookieJar["cookie1"]
    # Test whether the deletion was successful
    try:
        cookieJar["cookie1"]
        assert False
    except KeyError:
        assert True
    # Test whether the header was deleted
    assert not headers.get("Set-Cookie")



# Generated at 2022-06-14 07:03:35.897365
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    assert True == True

# Generated at 2022-06-14 07:03:49.573283
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("token", "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxfQ.lT0_7hxlWY9Xdv0j0TGSg7TJ-cvCeoOd6p1_624Kj44")
    assert str(cookie) == 'token="eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxfQ.lT0_7hxlWY9Xdv0j0TGSg7TJ-cvCeoOd6p1_624Kj44"'

# Generated at 2022-06-14 07:03:56.734027
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from aiohttp.multipart import MultipartWriter
    from io import BytesIO
    from io import StringIO
    from unittest import TestCase
    from aiohttp import MultipartWriter
    from aiohttp import MultipartWriter
    from aiohttp import MultipartWriter

    class test_CookieJar___delitem__(TestCase):
        def test_002(self):
            headers = MultipartWriter()
            CookieJar(headers)["test_key"] = "test_value"
            self.assertTrue(headers.getall("Set-Cookie"))
            del CookieJar(headers)["test_key"]
            self.assertTrue(not headers.getall("Set-Cookie"))

    if __name__ == "__main__":
        import unittest
        unittest.main()

# Generated at 2022-06-14 07:04:07.167841
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("foo", "bar")
    cookie["expires"] = "expires"
    cookie["path"] = "Path"
    cookie["comment"] = "Comment"
    cookie["domain"] = "Domain"
    cookie["max-age"] = "Max-Age"
    cookie["secure"] = "Secure"
    cookie["httponly"] = "HttpOnly"
    cookie["version"] = "Version"
    cookie["samesite"] = "SameSite"
    return [
        cookie["expires"],
        cookie["path"],
        cookie["comment"],
        cookie["domain"],
        cookie["max-age"],
        cookie["secure"],
        cookie["httponly"],
        cookie["version"],
        cookie["samesite"]
    ]


# Generated at 2022-06-14 07:04:17.910990
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from starlette.headers import Headers
    headers = Headers()
    cookieJar = CookieJar(headers)
    from starlette.testclient import TestClient
    from starlette.applications import Starlette
    from starlette.responses import HTMLResponse
    
    app = Starlette()
    @app.route("/")
    def home(request):
        return HTMLResponse("Home")

    @app.route("/set_cookie")
    def set_cookie(request):
        cookieJar["user"] = "Vinh"
        return HTMLResponse("Set cookie")

    @app.route("/get_cookie")
    def get_cookie(request):
        return HTMLResponse(f"{cookieJar['user']}")

    client = TestClient(app)
    response = client.get("/set_cookie")

# Generated at 2022-06-14 07:04:29.269946
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"

    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    assert str(cookie) == "name=value; Path=/"

    cookie = Cookie("name", "value")
    cookie["expires"] = datetime(
        year=2020, month=1, day=1, hour=0, minute=0, second=0, tzinfo=None
    )
    assert (
        str(cookie) == "name=value; expires=Wed, 01-Jan-2020 00:00:00 GMT"
    )

    cookie = Cookie("name", "value")
    cookie["max-age"] = 3600
    assert str(cookie) == "name=value; Max-Age=3600"


# Generated at 2022-06-14 07:04:44.693036
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cj = CookieJar({'Set-Cookie': ['cookie1=value1']})
    cj['cookie2'] = 'value2'
    cookie_header = cj.cookie_headers['cookie2']
    cj.headers.add(cookie_header, 'cookie2=value2')
    cj['cookie2']['max-age'] = 0

    assert cj.headers.getlist('Set-Cookie') == ['cookie1=value1', 'cookie2=value2']
    assert cj.cookie_headers == {'cookie1': 'Set-Cookie', 'cookie2': 'Set-Cookie'}
    assert cj == {'cookie1': 'cookie1=value1', 'cookie2': 'cookie2=value2'}

    # delete cookie1
    del cj['cookie1']
    assert cj

# Generated at 2022-06-14 07:04:59.297865
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from datetime import datetime
    from uvicorn.config import Config
    from uvicorn.protocols.http.httptools_impl import HttpToolsProtocol

    config = Config(app=None)
    headers = MultiHeader("Set-Cookie")
    cookies = CookieJar(headers)

    assert "test" not in headers

    cookies["test"] = "test"
    assert "test" in headers
    assert "test" in cookies
    assert "test" == cookies["test"].value

    cookies["test"] = "changed"
    assert "test" in headers
    assert "test" in cookies
    assert "changed" == cookies["test"].value

    cookies["test"]["expires"] = datetime.now()
    assert "test" in headers
    assert "test" in cookies

# Generated at 2022-06-14 07:05:05.084287
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('Test', 'Value')
    cookie['path'] = '/'
    cookie['domain'] = '.test.com'
    cookie['expires'] = datetime(2019, 1, 1, 0, 0, 0)
    cookie['max-age'] = 1000
    cookie['secure'] = True
    cookie['httpOnly'] = True
    cookie['version'] = 1.0

    print(cookie)
    assert(str(cookie) == 'Test=Value; Max-Age=1000; Version=1.0; Path=/; Domain=.test.com; Expires=Tue, 01-Jan-2019 00:00:00 GMT; Secure; HttpOnly')

# Generated at 2022-06-14 07:05:08.687300
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "key"
    value = "value"
    cookie = Cookie(key, value)
    assert str(cookie) == key + "=" + value

# Generated at 2022-06-14 07:05:09.767090
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    assert True


# Generated at 2022-06-14 07:05:18.916840
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader([])
    cookie_jar = CookieJar(headers)

    # add a cookie named "empty" to the jar
    cookie_jar['empty'] = ""
    assert headers[0] == "Set-Cookie: empty=; Path=/; HttpOnly; Secure"

    # delete the cookie "empty" from the jar
    cookie_jar.__delitem__('empty')
    assert headers[0] == "Set-Cookie: empty=; Path=/; Max-Age=0"

    # delete the cookie "empty" from the jar, second time
    cookie_jar.__delitem__('empty')
    assert headers[0] == "Set-Cookie: empty=; Path=/; Max-Age=0"

    # add a cookie named "name" to the jar
    cookie_jar['name'] = "super cookie"


# Generated at 2022-06-14 07:05:31.834561
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    ts = datetime.now()
    ts = datetime(ts.year, ts.month, ts.day, ts.hour, ts.minute + 1)
    test_str = (
        "name=value; expires=%s; path=/; "
        "domain=test.com; max-age=10; secure; httponly" % (ts.strftime("%a, %d-%b-%Y %T GMT")))
    test_cookie = Cookie("name", "value")
    test_cookie["expires"] = ts
    test_cookie["path"] = "/"
    test_cookie["domain"] = "test.com"
    test_cookie["max-age"] = 10
    test_cookie["secure"] = True
    test_cookie["httponly"] = True

    assert str(test_cookie) == test_str

# Generated at 2022-06-14 07:05:32.661837
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    assert False == True

# Generated at 2022-06-14 07:05:40.741489
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"
    cookie["path"] = "/"
    assert str(cookie) == "name=value; Path=/"
    cookie["max-age"] = 300
    assert str(cookie) == "name=value; Path=/; Max-Age=300"


# ------------------------------------------------------------ #
#  SetCookie
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:05:49.544730
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    my_cookie_jar = CookieJar(headers)
    my_cookie_jar['test_cookie1'] = 'test_cookie1_val'
    my_cookie_jar['test_cookie2'] = 'test_cookie2_val'
    assert headers == {'Set-Cookie': ['test_cookie1=test_cookie1_val; Path=/', 'test_cookie2=test_cookie2_val; Path=/']}
    del my_cookie_jar['test_cookie1']
    assert headers == {'Set-Cookie': ['test_cookie2=test_cookie2_val; Path=/']}


# Generated at 2022-06-14 07:06:05.969528
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("username", "Charles")
    cookie["domain"] = "localhost"
    cookie["path"] = "/"
    cookie["comment"] = "My first cookie"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 1
    cookie["expires"] = datetime(1995, 10, 29, 0, 0, 0)
    cookie["max-age"] = 0

    assert str(cookie) == "username=Charles; Path=/; Comment=\"My first cookie\"; Domain=localhost; Secure; HttpOnly; Version=1; Expires=Sun, 29-Oct-1995 00:00:00 GMT; Max-Age=0"


# Generated at 2022-06-14 07:06:07.784803
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("a", "b")
    assert str(cookie) == "a=b"



# Generated at 2022-06-14 07:06:22.098827
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    jar = CookieJar(headers)
    jar['test_key1'] = 'test_value1'
    jar['test_key2'] = 'test_value2'
    jar['test_key3'] = 'test_value3'
    jar['test_key4'] = 'test_value4'
    jar['test_key5'] = 'test_value5'
    del jar['test_key1']
    assert 'test_key1' not in jar
    del jar['test_key2']
    assert 'test_key2' not in jar
    del jar['test_key3']
    assert 'test_key3' not in jar
    del jar['test_key4']
    assert 'test_key4' not in jar
    del jar['test_key5']

# Generated at 2022-06-14 07:06:28.450689
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaders(
        {
            "Set-Cookie": "test=test_value",
            "Connection": "close",
            "Content-Type": "application/json",
        }
    )
    cookie_jar = CookieJar(headers)
    cookie_jar["test"] = "new_value"
    assert cookie_jar["test"]["path"] == "/"
    assert cookie_jar["test"].value == "new_value"


# Generated at 2022-06-14 07:06:35.200664
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    cookies = CookieJar(headers)

    # If a cookie doesn't exist, add it
    cookies["test1"] = "hello"
    assert headers["Set-Cookie"].value == "test1=hello; Path=/", "Cookie wasn't added to headers"
    assert cookies["test1"].value == "hello", "Cookie wasn't added to cookies"

    # If a cookie already exists, update it
    cookies["test1"] = "goodbye"
    assert cookies["test1"].value == "goodbye", "Cookie wasn't updated"
    assert headers["Set-Cookie"].value == "test1=goodbye; Path=/", "Cookie wasn't updated in headers"



# Generated at 2022-06-14 07:06:38.074845
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import pytest

    with pytest.raises(KeyError):
        Cookie(None, None).__str__()

# Generated at 2022-06-14 07:06:44.335321
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test Cookie.__str__
    """
    cookie = Cookie('username', 'testuser')
    expected = 'username=testuser'
    assert str(cookie) == expected
    cookie['expires'] = datetime(2018, 7, 22, 12, 35, 35)
    expected = 'username=testuser; Expires=Sun, 22-Jul-2018 12:35:35 GMT'
    assert str(cookie) == expected


# Generated at 2022-06-14 07:06:56.023104
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from quart import make_response, request
    from quart.sessions import SecureCookieSessionInterface

    session = SecureCookieSessionInterface()
    client = app.test_client()
    with app.test_request_context():
        resp = make_response("Hello, World!")
        session.save_session(resp, {"foo": "bar"})
        headers = resp.headers
        try:
            cookies = CookieJar(headers)
            assert len(cookies) == 1

            # Test if a non-existent key is deleted from cookies
            del cookies["blah"]
            assert len(cookies) == 0
        except KeyError:
            raise AssertionError


# Generated at 2022-06-14 07:07:00.733338
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    key = "key"
    value = "value"
    cookie = Cookie(key, value)
    assert cookie[key] == value
    cookie["max-age"] = 123
    assert cookie["max-age"] == 123
    with pytest.raises(ValueError):
        cookie["max-age"] = "abc"


# Generated at 2022-06-14 07:07:03.534203
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert Cookie('HttpOnly',True).__str__() == 'HttpOnly'



# Generated at 2022-06-14 07:07:18.197103
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    # Use expected key to set a cookie that doesn't exist
    cookie_jar["my_cookie"] = "chocolate chip"
    assert cookie_jar["my_cookie"] == "chocolate chip"
    assert "Set-Cookie" in headers
    cookie_header = headers["Set-Cookie"]
    assert "my_cookie=chocolate chip" in cookie_header
    # Use expected key to update a cookie that exists
    cookie_jar["my_cookie"] = "toffee chip"
    assert cookie_jar["my_cookie"] == "toffee chip"
    assert "Set-Cookie" in headers
    cookie_header = headers["Set-Cookie"]
    assert "my_cookie=toffee chip" in cookie_header
    # Use unexpected key to set a cookie