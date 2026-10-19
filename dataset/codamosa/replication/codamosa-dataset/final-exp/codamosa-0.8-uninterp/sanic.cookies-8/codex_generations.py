

# Generated at 2022-06-14 06:57:33.861181
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('foo', 'bar')
    assert str(cookie) == "foo=bar"
    cookie['path'] = '/'
    assert str(cookie) == "foo=bar; Path=/"
    cookie['max-age'] = 1800
    assert str(cookie) == "foo=bar; Max-Age=1800; Path=/"
    cookie['version'] = 1
    assert str(cookie) == "foo=bar; Version=1; Max-Age=1800; Path=/"
    cookie['secure'] = True
    assert str(cookie) == "foo=bar; Version=1; Secure; Max-Age=1800; Path=/"
    cookie['httponly'] = True
    assert str(cookie) == "foo=bar; Version=1; Secure; HttpOnly; Max-Age=1800; Path=/"
    cookie['samesite']

# Generated at 2022-06-14 06:57:35.058135
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    cookie["expires"] = 1
    assert str(cookie) == "foo=bar; Max-Age=1"

# Generated at 2022-06-14 06:57:38.143844
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('testkey', 'testvalue')
    assert cookie['testkey'] == 'testvalue'
    cookie['testkey'] = 'newtestvalue'
    assert cookie['testkey'] == 'newtestvalue'


# Generated at 2022-06-14 06:57:46.744566
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie('foo','bar')
    with pytest.raises(KeyError):
        c['expires'] = 'bar'
    with pytest.raises(KeyError):
        c['comment'] = 'bar'
    with pytest.raises(KeyError):
        c['domain'] = 'bar'
    with pytest.raises(KeyError):
        c['max-age'] = 'baz'
    with pytest.raises(KeyError):
        c['secure'] = 'bar'
    with pytest.raises(KeyError):
        c['httponly'] = 'bar'
    with pytest.raises(KeyError):
        c['version'] = 'bar'
    with pytest.raises(KeyError):
        c['samesite'] = 'bar'

# Generated at 2022-06-14 06:57:59.226564
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("foo", "bar")
    c["path"] = "/"
    c["max-age"] = 10
    assert str(c) == "foo=bar; Max-Age=10; Path=/"
    c["httponly"] = True
    assert str(c) == "foo=bar; Max-Age=10; Path=/; HttpOnly"
    d = Cookie("foo", "bar")
    d["domain"] = "google.com"
    assert str(d) == "foo=bar; Domain=google.com"
    e = Cookie("foo", "bar")
    e["samesite"] = "Strict"
    assert str(e) == "foo=bar; SameSite=Strict"


# ------------------------------------------------------------ #
#  test_cookies
# ------------------------------------------------------------ #

# Tests are run with py

# Generated at 2022-06-14 06:58:07.130918
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("hello", "world")
    print(cookie)
    assert cookie.__str__() == "hello=world"
    cookie["expires"] = datetime(year=2019, month=8, day=9, hour=10, minute=11)
    assert cookie.__str__() == "hello=world; expires=Fri, 09-Aug-2019 10:11:00 GMT"
    cookie["httponly"] = True
    assert cookie.__str__() == "hello=world; httponly; expires=Fri, 09-Aug-2019 10:11:00 GMT"
    cookie["secure"] = True
    assert cookie.__str__() == "hello=world; httponly; secure; expires=Fri, 09-Aug-2019 10:11:00 GMT"
    cookie["path"] = "/"

# Generated at 2022-06-14 06:58:20.523127
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookies = Cookie('name', 'value')
    assert str(cookies) == "name=value"

    cookies = Cookie('name', 'value')
    cookies["path"] = "/"
    cookies["comment"] = "some comment"
    assert str(cookies) == "name=value; Path=/; Comment=some comment"

    cookies = Cookie('name', 'value')
    cookies["expires"] = datetime.strptime("01-01-2020", "%d-%m-%Y")
    cookies["max-age"] = 3600
    cookies["comment"] = "some comment"
    assert str(cookies) == "name=value; Path=/; Max-Age=3600; Comment=some comment; Expires=Tue, 01-Jan-2020 00:00:00 GMT"

    cookies = Cookie('name', 'value')
   

# Generated at 2022-06-14 06:58:22.956804
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("foo", "bar")
    cookie.__setitem__("max-age", "100")
    assert cookie["max-age"] == "100"



# Generated at 2022-06-14 06:58:35.600904
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict({})
    cookie_jar = CookieJar(headers)
    assert cookie_jar.headers == headers

    cookie_jar["key"] = "value"
    assert headers == MultiHeaderDict({None: ["Set-Cookie: key=value; Path=/"]})
    cookie_jar["key2"] = "value2"
    assert headers == MultiHeaderDict({None: ["Set-Cookie: key=value; Path=/", "Set-Cookie: key2=value2; Path=/"]})
    cookie_jar["key"] = "newvalue"
    assert headers == MultiHeaderDict({None: ["Set-Cookie: key=newvalue; Path=/", "Set-Cookie: key2=value2; Path=/"]})
    cookie_jar["key"] = "anothernewvalue"
    assert headers == MultiHeader

# Generated at 2022-06-14 06:58:39.638302
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Test case 1
    cookie1 = Cookie("name1", "value1")
    cookie1["max-age"] = 1
    cookie1["expires"] = datetime.fromtimestamp(0)
    cookie1["secure"] = True
    cookie1["httponly"] = False
    output1 = cookie1.__str__()
    if output1 == ("name1=value1; Max-Age=1; expires=Thu, 01-Jan-1970 01:00:00 "+
                   "GMT; Secure"):
        print("Test case 1: PASSED")
    else:
        print("Test case 1: FAILED")
    # Test case 2
    cookie2 = Cookie("name2", "value2")
    cookie2["path"] = "/"
    output2 = cookie2.__str__()

# Generated at 2022-06-14 06:58:55.828351
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie_obj = Cookie("name", "val")
    cookie_obj["expires"] = datetime(2019, 8, 1, 12, 0)
    cookie_obj["path"] = "/"
    cookie_obj["secure"] = True
    cookie_obj["httponly"] = True
    cookie_obj["samesite"] = "Lax"
    assert cookie_obj["expires"] == datetime(2019, 8, 1, 12, 0)
    assert cookie_obj["path"] == "/"
    assert cookie_obj["samesite"] == "Lax"
    assert cookie_obj["secure"] == True
    assert cookie_obj["httponly"] == True

# Generated at 2022-06-14 06:59:02.229793
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar({})
    cookies['a'] = 'b'
    cookies['c'] = 'd'
    assert cookies['a'] == 'b'
    assert cookies['c'] == 'd'
    del cookies['a']
    assert 'a' not in cookies
    assert cookies['c'] == 'd'

# Generated at 2022-06-14 06:59:06.637380
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    cookie["path"] = "/"
    assert str(cookie) == "foo=bar; Path=/"
    cookie["max-age"] = 100
    assert str(cookie) == "foo=bar; Path=/; Max-Age=100"



# Generated at 2022-06-14 06:59:16.722253
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = caseless_dict.CaselessDict()
    cookie_jar = CookieJar(headers)
    cookie_jar['hello'] = 'world'
    assert headers['Set-Cookie'] == 'hello=world; Path=/'
    del cookie_jar['hello']
    assert 'hello=world' not in headers['Set-Cookie']

    # check cookies not added to headers don't raise exception
    del cookie_jar['cookie_not_exists']
    assert 'cookie_not_exists' not in cookie_jar
    assert 'cookie_not_exists' not in headers

# Generated at 2022-06-14 06:59:28.595265
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("TestCookie", "CookieValue")
    c["Expires"] = "Wed, 09 Jun 2021 10:18:14 GMT"
    c["Max-Age"] = 3600
    c["Path"] = "/"
    c["Comment"] = "MyCookieComment"
    c["Domain"] = "example.com"
    c["Secure"] = True
    c["HttpOnly"] = True
    c["SameSite"] = "Lax"

    assert c.__str__() == (
        'TestCookie=CookieValue; Version=1; Expires=Wed, 09 Jun 2021 10:18:14 GMT; '
        'Max-Age=3600; Domain=example.com; Path=/; Comment=MyCookieComment; '
        'SameSite=Lax; Secure; HttpOnly'
    )



# Generated at 2022-06-14 06:59:41.655362
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('key', 'value')
    cookie['max-age'] = 10
    cookie['expires'] = datetime(2011, 3, 25, 12, 0, 0)
    cookie['path'] = '/'
    cookie['comment'] = 'cookie comment'
    cookie['domain'] = 'example.com'
    cookie['secure'] = True
    cookie['httponly'] = True
    expected_output = 'key=value; Max-Age=10; expires=Thu, 24-Mar-2011 12:00:00 GMT; Path=/; Comment=cookie comment; Domain=example.com; Secure; HttpOnly'
    assert cookie.__str__()==expected_output, "__str__ method of Cookie class produces different output"


# test if encode method of Cookie class produces the output in the format it is expected to produce

# Generated at 2022-06-14 06:59:49.593456
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime

    cookie = Cookie("key", "value")
    cookie["expires"] = datetime(2020, 1, 1)
    cookie["path"] = "/"
    cookie["domain"] = "example.com"
    cookie["max-age"] = 60
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 1
    cookie["comment"] = "A comment"
    cookie["samesite"] = "strict"

    assert (
        str(cookie)
        == 'key=value; expires=Wed, 01-Jan-2020 00:00:00 GMT; Path=/; Domain=example.com; Max-Age=60; Secure; HttpOnly; Version=1; Comment="A comment"; SameSite=strict'
    )



# Generated at 2022-06-14 07:00:01.630172
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("foo", "bar")
    assert cookie["path"] == None
    assert cookie["expires"] == None
    cookie["path"] = "/"
    assert cookie["path"] == "/"
    cookie["expires"] = datetime.now()
    assert cookie["expires"] > None
    cookie["secure"] = True
    assert cookie["secure"] == True
    cookie["secure"] = False
    assert cookie["secure"] == False
    try:
        cookie["max-age"] = "foo"
    except ValueError:
        pass
    else:
        assert "max-age" == False
    cookie["max-age"] = 1
    assert cookie["max-age"] == 1
    try:
        cookie["expires"] = True
    except TypeError:
        pass

# Generated at 2022-06-14 07:00:09.371565
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    """
    Cookiejar test for method __delitem__.
    :return:
    """

    headers = MultiDict()
    cookiejar = CookieJar(headers)

    # Case 1: When cookie key is deleted and cookie value is set
    cookiejar["key1"] = "value1"
    assert len(headers[CookieJar.header_key]) == 1

    del cookiejar["key1"]
    assert len(headers[CookieJar.header_key]) == 0

# Generated at 2022-06-14 07:00:19.965571
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from starlette.responses import Response
    response = Response()
    response.cookies["test_key"] = "test_value"
    # should be able to set the cookie value to an empty string
    assert response.cookies["test_key"].value == "test_value"
    del response.cookies["test_key"]
    with pytest.raises(KeyError):
        _ = response.cookies["test_key"]
    # should be able to set the cookie value to an empty string
    response.cookies["test_key"] = "test_value"
    del response.cookies["test_key"]
    assert response.cookies["test_key"].value == ""
    # should be able to set the cookie value to an empty string
    response.cookies["test_key"] = "test_value"
    response

# Generated at 2022-06-14 07:00:31.294941
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["session_id"] = "12345"

    cookie_jar.__delitem__("session_id")

    cookies = headers.items(cookie_jar.header_key)
    assert len(cookies) == 1
    assert cookies[0].value == ''
    assert cookies[0]["max-age"] == 0


# Generated at 2022-06-14 07:00:41.415014
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('a', 'b')
    cookie['expires'] = datetime(2017, 1, 1, 0, 0, 0, 0)
    cookie['path'] = '/'
    cookie['comment'] = 'c'
    cookie['domain'] = 'd'
    cookie['max-age'] = 30
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['version'] = 'e'
    cookie['samesite'] = 'Strict'
    cookie.output() == "a=b; expires=Sun, 1-Jan-2017 00:00:00 GMT; Path=/; Comment=c; Domain=d; Max-Age=30; Secure; HttpOnly; Version=e; SameSite=Strict"

# Generated at 2022-06-14 07:00:52.305500
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name1', 'value1')
    cookie['expires'] = datetime.strptime('Wed, 21 Oct 2015 07:28:00 GMT',
                                          '%a, %d %b %Y %H:%M:%S GMT')
    cookie['path'] = '/'
    cookie['comment'] = 'test cookie to verify the encoding'
    cookie['domain'] = 'www.example.com'
    cookie['max-age'] = 1000
    cookie['version'] = 1
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['samesite'] = 'Lax'


# Generated at 2022-06-14 07:01:01.016511
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
  
  print("\nUnit test for method __delitem__ of class CookieJar")
  myHeaders = MultiHeader()
  myCookies = CookieJar(myHeaders)
  myCookies['USER_ID'] = '1234'
  myCookies['PASSWORD'] = '5678'
  del myCookies['USER_ID']
  print(myHeaders.get_all('Set-Cookie'))




# Generated at 2022-06-14 07:01:11.205138
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")
    assert str(c) == "name=value"
    c["max-age"] = "value"
    assert str(c) == "name=value; Max-Age=value"
    c["max-age"] = "value"
    c["max-age"] = 0
    assert str(c) == "name=value; Max-Age=0"
    c["max-age"] = 0
    c["max-age"] = datetime.now()
    assert str(c) == "name=value; Max-Age=0"
    c["max-age"] = False
    assert str(c) == "name=value"
    c["max-age"] = False
    c["expires"] = datetime.now()
    assert str(c) == "name=value"
   

# Generated at 2022-06-14 07:01:24.432742
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("test", "value")
    assert c.__str__() == "test=value"
    c["version"] = 1
    assert c.__str__() == "test=value; Version=1"
    c["secure"] = True
    assert c.__str__() == "test=value; Version=1; Secure"
    c["httponly"] = True
    assert c.__str__() == "test=value; Version=1; Secure; HttpOnly"
    c["expires"] = datetime(2017, 11, 29, 23, 0)
    assert c.__str__() == "test=value; Version=1; Secure; HttpOnly; expires=Thu, 30-Nov-2017 00:00:00 GMT"
    # Test max-age is an integer
    c["max-age"] = "bad"

# Generated at 2022-06-14 07:01:37.285574
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from http import cookies
    import pytest
    from datetime import datetime

    cookies_dict = {
        "language": "Python",
        "max-age": 10000,
        "HttpOnly": False,
        "Secure": True,
        "expires": datetime.now(),
        "version": 1,
        "comment": "This is a comment",
        "Path": "/",
        "another key": "this is a value",
        "Domain": "localhost:5000",
        "SameSite": "Strict",
    }


# Generated at 2022-06-14 07:01:42.934900
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["first"] = "first"
    cookie_jar["second"] = "second"
    del cookie_jar["second"]
    assert "second" not in cookie_jar
    assert "second" not in headers["Set-Cookie"]
    assert headers["Set-Cookie"][0]["first"] == "first"


# Generated at 2022-06-14 07:01:53.885228
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('user', 'michael')
    cookie['max-age'] = 3600
    cookie['path'] = '/'
    assert(str(cookie) == "user=michael; Max-Age=3600; Path=/")
    cookie['expires'] = datetime(2017, 9, 5, 8, 52, 15, 538225)
    assert(str(cookie) == "user=michael; Max-Age=3600; Path=/; Expires=Mon, 05-Sep-2017 08:52:15 GMT")
    cookie['secure'] = True
    assert(str(cookie) == "user=michael; Max-Age=3600; Path=/; Expires=Mon, 05-Sep-2017 08:52:15 GMT; Secure")
    cookie['httponly'] = True

# Generated at 2022-06-14 07:02:04.654294
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Unit tests for method __str__ of class Cookie
    """
    c = Cookie("test", "value")
    assert str(c) == "test=value"

    c["max-age"] = "test"
    assert "test=value; Max-Age=test" in str(c)

    c["max-age"] = 10
    assert "test=value; Max-Age=10" in str(c)

    assert "test=value; Path=/; Max-Age=10" in (
        str(
            Cookie(
                "test",
                "value",
                path="/",
                secure=True,
                max_age="10",
                httponly=True,
            )
        )
    )


# Generated at 2022-06-14 07:02:17.556378
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    header = MultiHeader()
    header.add("Set-Cookie", "a=b")
    header.add("Set-Cookie", "c=d")
    header.add("Content-Type", "text/html")
    jar = CookieJar(header)
    jar["a"]
    jar["c"]
    assert jar["a"].value == "b"
    del jar["a"]
    assert "Set-Cookie" not in jar.headers
    assert ("Set-Cookie", "c=d") not in jar.headers.raw
    assert ("Set-Cookie", "c=d") in jar.headers.multi_items()
    assert jar["c"].value == "d"
    del jar["c"]
    assert "Set-Cookie" not in jar.headers

# Generated at 2022-06-14 07:02:18.592812
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('test', 'cookie')
    assert str(c) == "test=cookie"



# Generated at 2022-06-14 07:02:28.677514
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test Cookie's __str__ method by ensuring cookie values are properly
    quoted when encoded
    """
    test_val = "abcdefg"
    assert Cookie(test_val, test_val).__str__() == test_val + "=" + _quote(test_val)

    test_val = "abc defg"
    assert Cookie(test_val,test_val).__str__() == test_val + "=" + _quote(test_val)

    test_val = "abcde\"f"
    assert Cookie(test_val,test_val).__str__() == test_val + "=" + _quote(test_val)

# Generated at 2022-06-14 07:02:33.574385
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = CIMultiDict()
    jar = CookieJar(headers)
    jar['key'] = 'value'
    assert headers['Set-Cookie'] == 'key=value; Max-Age=0; Path=/'


# Generated at 2022-06-14 07:02:40.737033
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    co = Cookie('key', 'value')
    co['max-age'] = 200
    co['expires'] = datetime(year=2019, month=7, day=12, hour=12, minute=12)
    co['secure'] = True
    co['httponly'] = True
    assert str(co) == 'key=value; Max-Age=200; expires=Fri, 12-Jul-2019 12:12:00 GMT; Secure; HttpOnly'



# Generated at 2022-06-14 07:02:44.265976
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaders()
    cookie_jar = CookieJar(headers)
    cookie_jar["foo"] = "bar"

    assert headers.get("Set-Cookie") == "foo=bar; Path=/; HttpOnly"


# Generated at 2022-06-14 07:02:50.720404
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # format as a Set-Cookie header value
    output = ["%s=%s" % ('key', _quote('value'))]
    for key, value in {'max-age': 0}.items():
        if key == "max-age":
            try:
                output.append("%s=%d" % ('Max-Age', value))
            except TypeError:
                output.append("%s=%s" % ('Max-Age', value))
        elif key == "expires":
            output.append(
                "%s=%s"
                % ('Expires', value.strftime("%a, %d-%b-%Y %T GMT"))
            )
        elif key in {'secure'} and {'secure': False}:
            output.append('Secure')
        else:
            output.append

# Generated at 2022-06-14 07:03:02.968890
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Unit test for method __str__ of class Cookie
    """
    cookie = Cookie("c", "cookie")
    result = str(cookie)
    assert result == "c=cookie"
    cookie["expires"] = datetime.utcnow()
    result = str(cookie)
    assert result.endswith("UTC")
    assert result.startswith("c=cookie; expires=")
    cookie["max-age"] = 10
    result = str(cookie)
    assert result.endswith("Cookie; expires=")
    assert result.index("max-age=10") > result.index("Cookie; expires=")
    cookie["secure"] = "secure"
    result = str(cookie)
    assert result.endswith("max-age=10; Secure")

# Generated at 2022-06-14 07:03:06.856314
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("sans", "papyrus")
    cookie["max-age"] = 100
    assert cookie["max-age"] == 100


# Generated at 2022-06-14 07:03:11.065829
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    with pytest.raises(KeyError):
        jar = CookieJar()
        jar['kevin']
        jar['max'] = 'mouse'
        assert jar.headers['Set-Cookie'] == 'kevin=""; Path=/'
        del jar['max']
        del jar['mike']



# Generated at 2022-06-14 07:03:23.279838
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test", "value")
    header = str(cookie)
    assert header == "test=value"
    cookie["max-age"] = DEFAULT_MAX_AGE
    header = str(cookie)
    assert header == "test=value; Max-Age=0"
    cookie["domain"] = "localhost"
    header = str(cookie)
    assert header == "test=value; domain=localhost; Max-Age=0"
    cookie["httponly"] = True
    header = str(cookie)
    assert header == "test=value; domain=localhost; Max-Age=0; HttpOnly"
    cookie["path"] = "/test"
    header = str(cookie)
    assert header == "test=value; domain=localhost; Max-Age=0; HttpOnly; Path=/test"

# Generated at 2022-06-14 07:03:35.558752
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cookie_jar = CookieJar(headers)
    cookie_jar["foo"] = "bar"
    cookie_jar["bacon"] = "eggs"
    cookie_jar["spam"] = "ham"
    assert "foo=bar" in headers.getall(cookie_jar.header_key)
    assert "bacon=eggs" in headers.getall(cookie_jar.header_key)
    assert "spam=ham" in headers.getall(cookie_jar.header_key)
    del cookie_jar["bacon"]
    assert "foo=bar" in headers.getall(cookie_jar.header_key)
    assert "bacon=eggs" not in headers.getall(cookie_jar.header_key)

# Generated at 2022-06-14 07:03:40.732283
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from wsgiservice import MultiHeader

    jar = CookieJar(MultiHeader())
    jar["name"] = "bob"
    cookie = jar["name"]
    assert cookie.value == "bob"


# Generated at 2022-06-14 07:03:51.622655
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test = CookieJar({})
    test["test1"] = "test2"
    test["test3"] = "test4"
    assert test.headers == {"Set-Cookie": ["Set-Cookie: test1=test2; Path=/", "Set-Cookie: test3=test4; Path=/"]}
    test.__delitem__("test1")
    assert test.headers == {"Set-Cookie": ["Set-Cookie: test3=test4; Path=/", "Set-Cookie: test1=; Max-Age=0; Path=/"]}
    return "test_CookieJar___delitem__ pass"



# Generated at 2022-06-14 07:03:58.526506
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("foo", "bar")
    assert c.__str__() == "foo=bar"
    c["path"] = "/"
    assert c.__str__() == "foo=bar; Path=/"
    c["max-age"] = 1000
    assert c.__str__() == "foo=bar; Path=/; Max-Age=1000"



# Generated at 2022-06-14 07:04:11.905115
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Tests simple case
    cookie = Cookie('name', 'value')
    assert(str(cookie) == 'name=value')

    # Tests case with max-age property
    cookie['max-age'] = DEFAULT_MAX_AGE
    assert(str(cookie) == 'name=value; Max-Age=' + str(DEFAULT_MAX_AGE))

    # Tests case with expires property
    now = datetime.now()
    cookie['expires'] = now
    cookie_str = str(cookie)
    assert(('name=value; Max-Age=' + str(DEFAULT_MAX_AGE) + 
            '; Expires=' + now.strftime('%a, %d-%b-%Y %T GMT') == cookie_str))

    # Tests case with httponly property
    cookie['httponly'] = True
    cookie_

# Generated at 2022-06-14 07:04:24.000352
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test_Cookie_key", "test_Cookie_value")
    assert cookie.__str__() == "test_Cookie_key=test_Cookie_value"
    cookie["path"] = "/"
    cookie["domain"] = "test_Cookie_domain"
    assert cookie.__str__() == "test_Cookie_key=test_Cookie_value; Path=/; Domain=test_Cookie_domain"
    cookie["max-age"] = 0
    assert cookie.__str__() == "test_Cookie_key=test_Cookie_value; Path=/; Domain=test_Cookie_domain; Max-Age=0"
    cookie["expires"] = datetime(2018, 6, 21, 9, 5, 0)

# Generated at 2022-06-14 07:04:33.383111
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from pytest import raises
    from datetime import datetime
    from email.utils import format_datetime, parsedate_tz

    # test with valid args
    cookie = Cookie("key", "value")
    expected = "key=value;"
    assert str(cookie) == expected
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    cookie["max-age"] = "123"
    expected = "key=value; Path=%s; Max-Age=%s;" % (
        "/",
        "123",
    )
    assert str(cookie) == expected
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    cookie["max-age"] = 123
    cookie["secure"] = True

# Generated at 2022-06-14 07:04:41.116324
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Test: deletion of a cookie from CookieJar
    headers = CIMultiDict()
    expected_cookie_name = 'test'
    expected_cookie_value = '123'
    cookie_jar = CookieJar(headers)
    cookie_jar[expected_cookie_name] = expected_cookie_value
    cookie_jar[expected_cookie_name] = expected_cookie_value

    del cookie_jar[expected_cookie_name]
    assert expected_cookie_name not in cookie_jar



# Generated at 2022-06-14 07:04:44.047502
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

    cookie['path'] = '/'
    assert str(cookie) == "key=value; Path=/"
    return True


# Generated at 2022-06-14 07:05:00.855333
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from quart.wrappers.base import HeaderSet
    from quart.serving import MultiHeader
    header_set = HeaderSet()
    header_set.add(MultiHeader('Set-Cookie'), Cookie('blah', 'beer'))
    header = header_set.get('Set-Cookie')
    assert isinstance(header, MultiHeader)
    assert len(header.headers) == 1
    assert header[0] == 'blah=beer; path=/'
    header_set = HeaderSet()
    header_set.add(MultiHeader('Set-Cookie'), Cookie('bleh', 'bbq'))
    header = header_set.get('Set-Cookie')
    assert isinstance(header, MultiHeader)
    assert len(header.headers) == 1
    assert header[0] == 'bleh=bbq; path=/'


# Generated at 2022-06-14 07:05:13.003509
# Unit test for method __setitem__ of class CookieJar

# Generated at 2022-06-14 07:05:17.709529
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    output = ["%s=%s" % ("testkey", "testvalue")]
    try:
        output.append("%s=%s" % ("testkey", "testvalue"))
    except TypeError:
        output.append("%s=%s" % ("testkey", "testvalue"))

# ------------------------------------------------------------ #
#  MultiHeaders
# ------------------------------------------------------------ #

# Straight up copied from werkzeug


# Generated at 2022-06-14 07:05:26.360384
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = HTTPHeaderDict()
    cookie_jar = CookieJar(headers)
    cookie_jar["test"] = "test_value"

    #delete an existing cookie
    del cookie_jar["test"]
    assert "test" not in cookie_jar
    assert headers["Set-Cookie"] == "test=; max-age=0; path=/"

    #delete an non existing cookie
    del cookie_jar["test"]
    assert headers["Set-Cookie"] == "test=; max-age=0; path=/"

# Generated at 2022-06-14 07:05:36.469858
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('mycookie', 'myvalue')
    assert str(c) == 'mycookie=myvalue'
    c['comment'] = 'blah blah'
    assert str(c) == 'mycookie=myvalue; Comment=blah blah'
    c['httponly'] = True
    assert str(c) == 'mycookie=myvalue; Comment=blah blah; HttpOnly'
    c = Cookie('mycookie', 'myvalue')
    c['max-age'] = 1
    assert str(c) == 'mycookie=myvalue; Max-Age=1'
    c = Cookie('mycookie', 'myvalue')
    c['path'] = '/abc'
    assert str(c) == 'mycookie=myvalue; Path=/abc'
    c = Cookie('mycookie', 'myvalue')
    c['path']

# Generated at 2022-06-14 07:05:48.695990
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """Test Cookie __str__.

    Returns
    -------
    None
    """

    # Test 1:
    test_1 = Cookie("yummy_cookie", b"chocolate")
    test_1["max-age"] = 600
    cookie_str = test_1.__str__()
    assert cookie_str == "yummy_cookie=chocolate; Max-Age=600"

    # Test 2:
    test_2 = Cookie("tasty_cookie", "apple")
    test_2["max-age"] = "3600"
    cookie_str = test_2.__str__()
    assert cookie_str == "tasty_cookie=apple; Max-Age=3600"

    # Test 3:
    test_3 = Cookie("yummy_cookie", b"chocolate")

# Generated at 2022-06-14 07:05:57.141291
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    cookie_jar = CookieJar(headers)
    key_value = "key"
    cookie_jar[key_value] = "value"
    header_set = headers.getlist("Set-Cookie")
    assert header_set == ["key=value; Path=/"]
    assert cookie_jar[key_value].value == "value"
    assert cookie_jar[key_value]["path"] == "/"


# Generated at 2022-06-14 07:06:06.768510
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('id', '5')
    cookie['max-age'] = '5'
    assert str(cookie) == 'id=5; Max-Age=5'
    cookie = Cookie('id', '5')
    cookie['max-age'] = 5
    assert str(cookie) == 'id=5; Max-Age=5'
    cookie = Cookie('id', '5')
    cookie['expires'] = datetime(year=2021, month=2, day=2)
    assert str(cookie) == 'id=5; Expires=Tue, 02-Feb-2021 00:00:00 GMT'


# Generated at 2022-06-14 07:06:20.711935
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    import unittest
    from . import MultiHeader
    from . import Cookie
    from . import CookieJar
    from datetime import datetime

    class MultiHeaderTest(unittest.TestCase):

        def setUp(self):
            self.headers = MultiHeader()
            self.cookie_headers: Dict[str, str] = {}

        def test__delitem__(self):
            # If this cookie doesn't exist, add it to the header keys
            key = 'foo'
            value = 'bar'
            self.cookie_headers[key] = 'cookie_header'
            cookie = Cookie(key, value)
            self.assertNotIn(key, self.headers)
            self.headers.add('cookie_header', cookie)
            self.assertIn(key, self.headers)

            del self.headers[key]


# Generated at 2022-06-14 07:06:30.955051
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('testname', 'testvalue')
    assert str(cookie) == 'testname=testvalue'

    cookie['path'] = '/'
    assert str(cookie) == 'testname=testvalue; Path=/'

    cookie['max-age'] = 60
    assert str(cookie) == 'testname=testvalue; Path=/; Max-Age=60'

    cookie['expires'] = datetime(year=2017, month=4, day=1, hour=12)
    assert str(cookie) == 'testname=testvalue; Path=/; Max-Age=60; Expires=Sat, 01-Apr-2017 12:00:00 GMT'

    cookie['secure'] = True

# Generated at 2022-06-14 07:06:46.133029
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    jar = CookieJar(headers = {})
    jar["Test"] = "Value"
    assert 'Test=Value; Path=/' in jar.headers['Set-Cookie']
    assert jar.cookie_headers.get("Test") == 'Set-Cookie'
    del jar["Test"]
    assert 'Test=Value; Path=/' not in jar.headers['Set-Cookie']
    assert jar.headers.get("Set-Cookie") is None
    assert jar.cookie_headers.get("Test") is None
    jar["Test"] = "Value2"
    assert 'Test=Value; Path=/' not in jar.headers['Set-Cookie']
    assert 'Test=Value2; Path=/' in jar.headers['Set-Cookie']
    assert jar.cookie_headers.get("Test") == 'Set-Cookie'

# Generated at 2022-06-14 07:06:51.229433
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    expected = "cookie=cookie-value; Path=/; HttpOnly"
    cookie = Cookie("cookie", "cookie-value")
    cookie["path"] = "/"
    cookie["httponly"] = True
    assert cookie.__str__() == expected

# Generated at 2022-06-14 07:07:00.997450
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key="toto", value="tata")
    assert str(cookie) == "toto=tata"
    cookie = Cookie(key="toto", value="tata")
    cookie["path"] = "toto"
    assert str(cookie) == "toto=tata; Path=toto"
    cookie = Cookie(key="toto", value="tata")
    cookie["max-age"] = 5
    assert str(cookie) == "toto=tata; Max-Age=5"
    cookie = Cookie(key="toto", value="tata")
    cookie["expires"] = datetime.fromisoformat("2018-01-01")
    assert str(cookie) == "toto=tata; Expires=Mon, 01-Jan-2018 00:00:00 GMT"

# Generated at 2022-06-14 07:07:14.016227
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():

    # Test that set in CookieJar adds a new key, with a value, to the
    # dictionary, as well as adds a cookie to the headers using cookie_headers
    # to keep track of the headers each cookie is stored in.
    headers = httpcore.Headers(default_value="dummy")
    cookies = CookieJar(headers)
    cookies["testing"] = "testing"
    assert "testing" == cookies["testing"].value
    assert "Set-Cookie" in cookies.headers
    assert "testing" in cookies.headers["Set-Cookie"]
    assert "testing" in cookies.cookie_headers

    # Test that CookieJar adds a new cookie to an existing cookie
    # header or creates a new header if the cookie header doesn't exist.
    cookies["foo"] = "bar"