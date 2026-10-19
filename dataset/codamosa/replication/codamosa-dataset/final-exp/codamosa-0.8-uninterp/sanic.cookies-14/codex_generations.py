

# Generated at 2022-06-14 06:57:29.798891
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Return a string that can be used as a Set-Cookie header.
    """
    cookie = Cookie(key='dummy', value='dummy')
    cookie['max-age'] = 10
    cookie['expires'] = datetime.now()
    cookie['path'] = '/'
    cookie['comment'] = 'dummy'
    cookie['domain'] = 'example.com'
    cookie['secure'] = True
    cookie['httponly'] = True

    expected = 'dummy=dummy; Max-Age=10; Comment=dummy; Domain=example.com; Path=/; Secure; HttpOnly'
    assert str(cookie) == expected

# Generated at 2022-06-14 06:57:39.677522
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    import pytest
    cj = CookieJar(headers={})

    # Test if an existing cookie is deleted successfully
    cj["a"] = "1"
    cj["b"] = "2"
    cj[0] = "3"

    assert len(cj) == 3
    assert "a" in cj.headers
    assert "b" in cj.headers
    assert 0 in cj.headers

    del cj["a"]
    del cj["b"]
    del cj[0]

    assert len(cj) == 0
    assert "a" not in cj.headers
    assert "b" not in cj.headers
    assert 0 not in cj.headers

    # Test if a non-existing cookie is deleted successfully
    cj["a"] = "1"
    cj["b"]

# Generated at 2022-06-14 06:57:48.965668
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookie = Cookie("test_CookieJar", "test_CookieJar_value")
    cookie["test_CookieJar_path"] = "/test_CookieJar"
    cookie["test_CookieJar_max_age"] = 123
    cookie["test_CookieJar_expires"] = datetime.now()
    c = CookieJar({"test_CookieJar": cookie})


# Generated at 2022-06-14 06:57:52.334671
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie("key", "value")
    c['httponly'] = True
    c["max-age"] = 123
    assert c["httponly"] == True
    assert c["max-age"] == 123

# Generated at 2022-06-14 06:58:03.095394
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"

    cookie = Cookie("name", "value")
    cookie["max-age"] = 100
    assert str(cookie) == "name=value; Max-Age=100"

    cookie = Cookie("name", "value")
    cookie["expires"] = datetime(2010,1,1, 1, 1, 1)
    assert str(cookie) == "name=value; Expires=Fri, 01-Jan-2010 01:01:01 GMT"

    cookie = Cookie("name", "value")
    cookie["secure"] = True
    assert str(cookie) == "name=value; Secure"

# ------------------------------------------------------------ #
#  CookieStorage
# ------------------------------------------------------------ #



# Generated at 2022-06-14 06:58:12.088752
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("myname", "myvalue")
    print(cookie)

    cookie["path"] = "/"
    print(cookie)

    cookie["domain"] = "example.com"
    print(cookie)

    cookie["secure"] = True
    print(cookie)

    cookie["httponly"] = True
    print(cookie)

    cookie["max-age"] = 3600
    print(cookie)

    cookie["expires"] = datetime(2021, 9, 5, 17, 31, 59)
    print(cookie)


if __name__ == "__main__":
    test_Cookie___str__()

# Generated at 2022-06-14 06:58:23.086146
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cookie_jar = CookieJar(headers)
    cookie_jar['key1'] = 'value1'
    cookie_jar['key2'] = 'value2'
    cookie_jar['key3'] = 'value3'
    cookie_jar['key4'] = 'value4'

    del cookie_jar['key3']
    assert cookie_jar['key1'].value == 'value1'
    assert cookie_jar['key2'].value == 'value2'
    assert cookie_jar['key4'].value == 'value4'
    assert 'key3' not in cookie_jar


# Generated at 2022-06-14 06:58:31.106651
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")
    assert str(c) == "name=value"  # no cookie parameters

    c["path"] = "/path"
    assert str(c) == "name=value; Path=/path"

    c["max-age"] = "max-age"
    assert str(c) == "name=value; Path=/path; Max-Age=max-age"

    c["expires"] = "expires"
    assert str(c) == "name=value; Path=/path; Max-Age=max-age; Expires=expires"

    c["domain"] = "domain"
    assert str(c) == "name=value; Path=/path; Max-Age=max-age; Expires=expires; Domain=domain"

    c["secure"] = "secure"
    assert str(c)

# Generated at 2022-06-14 06:58:34.144506
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("Test", "Cookie")
    assert "Test=Cookie" == str(cookie)



# Generated at 2022-06-14 06:58:46.408459
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Arrange
    cookie = Cookie("key", "value")

    # Act
    cookie["expires"] = datetime(1963, 12, 4, 12, 30)
    cookie["max-age"] = 123
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["domain"] = "domain"
    cookie["path"] = "path"
    cookie["version"] = "1"
    cookie["comment"] = "comment"

    # Assert
    assert str(cookie) == (
        'key=value; expires=Mon, 04-Dec-1963 12:30:00 GMT; Max-Age=123; '
        'Secure; HttpOnly; Domain=domain; Path=path; Version=1; Comment=comment'
    )

# Generated at 2022-06-14 06:58:54.547443
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["test"] = "value"
    assert headers != []
    assert len(headers) == 1
    assert "test" in jar
    assert "test" in headers["Set-Cookie"]


# Generated at 2022-06-14 06:59:06.572504
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("test", "cookie")
    # Max age must be an integer
    try:
        cookie["Max-Age"] = "not integer"
        assert False
    except ValueError:
        pass
    # Expires must be a datetime
    try:
        cookie["Expires"] = "not datetime"
        assert False
    except TypeError:
        pass
    # Set the max-age to 10
    cookie["Max-Age"] = 10
    assert cookie["Max-Age"] == 10
    # Set the expires to now
    cookie["Expires"] = datetime.utcnow()
    assert cookie["Expires"] == datetime.utcnow()



# Generated at 2022-06-14 06:59:19.116959
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    # Assemble
    headers = Headers()
    cookie_jar = CookieJar(headers)
    # Act
    cookie_jar["key"] = "value"

    # Assert
    # Test if the key does exist
    assert "key" in cookie_jar
    # Test that the value added is the expected one
    assert cookie_jar["key"].value == "value"
    # Test to make sure that the cookie is in the headers
    assert headers.get("Set-Cookie") == "key=value; Path=/".encode("utf-8")

    # Assemble
    headers = Headers()
    cookie_jar = CookieJar(headers)

    # Act
    cookie_jar["key"] = "value"
    # Assert
    # Test to make sure that we can't overwrite an existing cookie with an illegal key

# Generated at 2022-06-14 06:59:29.432282
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    """
    Test if a CookieJar object is able to set a cookie
    """

    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["test_key"] = "test_value"
    assert "test_value" == jar["test_key"].value, "Cookie value not set correctly"
    assert "test_key" == jar["test_key"].key, "Cookie key not set correctly"
    # Check if the cookie was added to the headers
    assert "Set-Cookie" in headers, "Cookie was not added to the headers"


# Generated at 2022-06-14 06:59:30.052713
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    pass

# Generated at 2022-06-14 06:59:43.606087
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("foo", "bar")
    c["expires"] = datetime(2007, 11, 8, 1, 20, 47)
    c['max-age'] = 60
    c['domain'] = '.foo.com'
    c['path'] = '/'
    c['secure'] = False
    c['httponly'] = True
    c['version'] = 1
    c['comment'] = 'This is a comment'
    c['samesite'] = 'Strict'
    expected = '''foo=bar; expires=Fri, 09-Nov-2007 01:20:47 GMT; Max-Age=60; Domain=.foo.com; Path=/; Secure; HttpOnly; Version=1; Comment=This is a comment; SameSite=Strict'''
    assert c.__str__() == expected

# Generated at 2022-06-14 06:59:50.306645
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = pytest.Mock()
    cookies = CookieJar(headers)
    cookies["resume"] = "test cookie"
    assert headers.add.call_count == 1
    cookies["resume"] = "other-test-cookie"
    assert headers.add.call_count == 2
    del cookies["resume"]
    headers.popall.assert_called_with("Set-Cookie")
    assert cookies == {}



# Generated at 2022-06-14 06:59:58.799715
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Set a new Cookie and set some values
    cookie = Cookie("test", "cookie")
    cookie["expires"] = "test"
    cookie["comment"] = "test"
    cookie["domain"] = "test"
    cookie["max-age"] = 0
    # Create a string with the keys and values
    cookie_string = "test=cookie; Expires=test; Comment=test; Domain=test; Max-Age=0"
    assert cookie.__str__() == cookie_string


# Generated at 2022-06-14 07:00:03.151022
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
  # Unit tests for method __setitem__ of class Cookie
  cookie = Cookie("key", "value")
  cookie["expires"] = "Wed, 09 Jun 2021 10:18:14 GMT"

  assert(cookie["expires"] == "Wed, 09 Jun 2021 10:18:14 GMT")


# Generated at 2022-06-14 07:00:09.653038
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key="TestCookie", value="Testing")
    assert str(cookie) == "TestCookie=Testing"
    cookie["path"] = '/'
    cookie["version"] = 1
    assert str(cookie) == "TestCookie=Testing; Path=/; Version=1"

# ------------------------------------------------------------ #
#  SimpleCookie Tests
# ------------------------------------------------------------ #


# Generated at 2022-06-14 07:00:17.884891
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookiejar = CookieJar(headers)
    cookiejar["cookie1"] = "test"
    assert headers["Set-Cookie"] == ["cookie1=test; Path=/"]
    del cookiejar["cookie1"]
    assert headers["Set-Cookie"] == []


# Generated at 2022-06-14 07:00:31.784623
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")

    # Check if the value of the key is contained in the output
    assert ("name=value" in str(c))

    c["comment"] = "this is a comment"

    # Check if the value of the key is contained in the output
    assert ("Comment=this is a comment" in str(c))

    c["version"] = 1

    # Check if the value of the key is contained in the output
    assert ("Version=1" in str(c))

    c["secure"] = True

    # Check if the value of the key is contained in the output
    assert ("Secure" in str(c))

    c["httponly"] = True

    # Check if the value of the key is contained in the output
    assert ("HttpOnly" in str(c))

    c["max-age"] = 10



# Generated at 2022-06-14 07:00:39.106309
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    ck = Cookie("testkey", "testvalue")
    ck["domain"] = "test.com"
    ck["path"] = "/"
    ck["max-age"] = "10"
    ck["expires"] = datetime.now()
    ck["secure"] = True
    ck["httponly"] = True
    return str(ck)


# ------------------------------------------------------------ #
#  SimpleCookie
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:00:50.436938
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar['name1'] = "value1"
    cookie_jar['name2'] = "value2"
    assert len(cookie_jar) == 2
    assert len(headers) == 2
    assert "name1=value1" in headers.getlist("Set-Cookie")
    assert "name2=value2" in headers.getlist("Set-Cookie")
    del cookie_jar['name1']
    assert len(cookie_jar) == 1
    assert len(headers) == 1
    assert "name2=value2" in headers.getlist("Set-Cookie")
    assert "name1=value1" not in headers.getlist("Set-Cookie")

# Generated at 2022-06-14 07:01:01.260293
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():

    headers = MultiHeaderDict()
    cookieJar = CookieJar(headers)

    try:
        cookieJar["hello"]
        assert False, "Error expected"
    except KeyError:
        assert True

    cookieJar["hello"] = "world"

    assert cookieJar["hello"].value == "world"
    assert "hello=world" in str(cookieJar)
    assert "hello=world" in str(headers)
    assert "Set-Cookie" in headers

    cookieJar["hello"] = "world2"

    assert cookieJar["hello"].value == "world2"
    assert "hello=world2" in str(cookieJar)
    assert "hello=world2" in str(headers)
    assert "Set-Cookie" in headers



# Generated at 2022-06-14 07:01:11.309461
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import datetime
    c = Cookie('cookie_name', 'value')
    assert str(c) == 'cookie_name=value'

    c['expires'] = datetime.datetime(
        year=2015, month=5, day=1,
        hour=7, minute=9, second=22
    )
    assert str(c) == 'cookie_name=value; Expires=Thu, 01-May-2015 07:09:22 GMT'

    c['max-age'] = 60
    assert str(c) == 'cookie_name=value; Expires=Thu, 01-May-2015 07:09:22 GMT; Max-Age=60'

    c = Cookie('cookie_name', 'value')
    c['max-age'] = 'hello'

# Generated at 2022-06-14 07:01:14.381441
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookie = CookieJar({})
    cookie["key"] = "value"
    assert "value" == cookie["key"].value
    cookie["key"] = "value2"
    assert "value2" == cookie["key"].value
    assert "value2" not in cookie
    assert "Set-Cookie" in cookie.headers
    assert 1 == len(cookie)
    assert 1 == len(cookie.headers)



# Generated at 2022-06-14 07:01:24.561479
# Unit test for method __str__ of class Cookie

# Generated at 2022-06-14 07:01:37.413965
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "key"
    value = "value"
    c = Cookie(key, value)
    result = c.__str__()
    assert result == "key=value"

    key = "key"
    value = "value"
    c = Cookie(key, value)
    c["path"] = "/"
    result = c.__str__()
    assert result == "key=value; Path=/; "

    key = "key"
    value = "value"
    c = Cookie(key, value)
    c["max-age"] = 0
    result = c.__str__()
    assert result == "key=value; Max-Age=0; "

    key = "key"
    value = "value"
    c = Cookie(key, value)

# Generated at 2022-06-14 07:01:49.270968
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("k", "v")
    assert str(c) == "k=v"

    c = Cookie("k", "v ;")
    assert str(c) == r'k="v ;"'

    c["comment"] = "c"
    assert str(c) == 'k=v; Comment="c"'

    c["httponly"] = True
    assert str(c) == 'k=v; Comment="c"; HttpOnly'

    c["secure"] = True
    assert str(c) == 'k=v; Comment="c"; HttpOnly; Secure'

    c["secure"] = False
    assert str(c) == 'k=v; Comment="c"; HttpOnly'

    c["secure"] = True
    assert str(c) == 'k=v; Comment="c"; HttpOnly; Secure'



# Generated at 2022-06-14 07:02:00.584090
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    jar = CookieJar({})
    jar["key"] = "value"
    assert "key" in jar
    assert "key" in jar.cookie_headers
    assert jar.cookie_headers["key"] == "Set-Cookie"
    assert jar.headers["Set-Cookie"] == "key=value; Path=/; HttpOnly"

    del jar["key"]

    assert "key" not in jar
    assert "key" not in jar.cookie_headers
    assert jar.cookie_headers == {}
    assert jar.headers == {}



# Generated at 2022-06-14 07:02:11.780415
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("foo", "bar")
    # Testing keys that don't exist
    cookie["foo"] = "bar"
    # Testing keys that do exist
    cookie["path"] = "/"
    try:
        cookie["foo"] = "bar"
        assert False
    except:
        assert True
    try:
        cookie["expires"] = "not a datetime"
        assert False
    except:
        assert True
    try:
        cookie["max-age"] = "not an int"
        assert False
    except:
        assert True
    # Testing keys that are flags
    cookie["secure"] = False
    cookie["secure"] = True

# Generated at 2022-06-14 07:02:19.246827
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from auxify.messaging import MutableMultiDict
    headers = MutableMultiDict()
    key = "expires"
    value = "2018-11-08T22:00:00"
    headers.add(key, value)
    cj = CookieJar(headers)
    assert key in cj.headers
    del cj[key]
    assert key not in cj.headers


# Generated at 2022-06-14 07:02:31.227958
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test_cookie", "test_value")
    assert str(cookie) == "test_cookie=test_value"

    cookie = Cookie("test_cookie", "test_value")
    cookie["max-age"] = 30
    assert str(cookie) == "test_cookie=test_value; Max-Age=30"

    cookie = Cookie("test_cookie", "test_value")
    cookie["expires"] = datetime(2038, 1, 19, 3, 14, 7)
    assert (
        str(cookie)
        == "test_cookie=test_value; Expires=Thu, 19-Jan-2038 00:00:00 GMT"
    )

    cookie = Cookie("test_cookie", "test_value")
    cookie["secure"] = True

# Generated at 2022-06-14 07:02:35.815204
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["test_key"] = "test_value"
    assert headers.get("Set-Cookie") == "test_key=test_value; Path=/; Max-Age=0"


# Generated at 2022-06-14 07:02:44.316947
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookie_jar = CookieJar(headers)
    cookie_jar["test_cookie"] = "test_cookie_value"
    cookie_jar["test_cookie_2"] = "test_cookie_value_2"
    assert headers["set-cookie"] == "test_cookie=test_cookie_value; Path=/\n" \
                                   "test_cookie_2=test_cookie_value_2; Path=/"
    del cookie_jar["test_cookie_2"]
    assert headers["set-cookie"] == "test_cookie=test_cookie_value; Path=/"



# Generated at 2022-06-14 07:02:47.165568
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    header = CIMultiDict()
    cookies = CookieJar(header)
    cookies['test'] = 'test'
    assert header.getall('Set-Cookie') == ['test=test; Domain=; Path=/']


# Generated at 2022-06-14 07:02:47.979700
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
	pass

# Generated at 2022-06-14 07:03:01.356138
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('c1', 'v1')
    cookie_with_comment = Cookie('c1', 'v1')
    cookie_with_comment['comment'] = 'This is a cookie'
    cookie_with_comment['max-age'] = 3600
    cookie_with_comment['version'] = 1
    cookie_with_comment['expires'] = datetime(year=2019, month=1, day=29)

    assert(cookie['comment'] is None)
    assert(cookie['max-age'] is None)
    assert(cookie['version'] is None)
    assert(cookie['expires'] is None)

    assert(cookie_with_comment['comment'] == 'This is a cookie')
    assert(cookie_with_comment['max-age'] == 3600)
    assert(cookie_with_comment['version'] == 1)

# Generated at 2022-06-14 07:03:14.705860
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test if Cookie class returns the right String when converted to String
    """
    cookie = Cookie("test", "testing123")
    cookie["max-age"] = 123
    cookie["Path"] = "/whatever"
    cookie["Domain"] = "localhost"
    cookie["HttpOnly"] = True
    cookie["Secure"] = False
    cookie["Comment"] = "This is a comment"
    cookie["expires"] = datetime(2020, 5, 11, 15, 23, 47)
    cookie["samesite"] = "Strict"
    assert str(cookie) == 'test="testing123"; Max-Age=123; Path=/whatever; Domain=localhost; HttpOnly; Comment="This is a comment"; expires=Tue, 11-May-2020 15:23:47 GMT; SameSite=Strict'

# ------------------------------------------------------------ #
#  main

# Generated at 2022-06-14 07:03:34.488360
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    
    cookie = Cookie("session", "2") 
    cookie["path"] = "/"
    cookie["max-age"] = DEFAULT_MAX_AGE

    assert str(cookie) == "session=2; Path=/; Max-Age=0"

    cookie["expires"] = datetime(2020, 12, 16, 11, 36, 33)
    
    assert str(cookie) == "session=2; Path=/; Max-Age=0; Expires=Fri, 16-Dec-2020 11:36:33 GMT"

    cookie["path"] = "/admin"
    cookie["domain"] = "127.0.0.1"
    
    cookie["httponly"] = True
    cookie["secure"] = True


# Generated at 2022-06-14 07:03:38.271393
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookiejar = CookieJar({})
    cookiejar["key"] = "value"
    assert cookiejar["key"] == "value"
    del cookiejar["key"]
    assert "key" not in cookiejar
    assert "Set-Cookie" not in cookiejar.headers


# Generated at 2022-06-14 07:03:43.021005
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    with pytest.raises(ValueError):
        Cookie("key", "value")["max-age"] = "-10"
    with pytest.raises(TypeError):
        Cookie("key", "value")["expires"] = 10


# Generated at 2022-06-14 07:03:53.594310
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('foo', 'bar')
    cookie['path'] = '/'
    cookie['max-age'] = 10
    cookie['expires'] = datetime.now()
    cookie['domain'] = "foo.bar.com"
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['version'] = "1.0"
    cookie['comment'] = "comment"
    cookie['samesite'] = "lax"

    assert cookie.__str__() == (
        'foo=bar; Path=/; Max-Age=10; expires=Thu, 01 Jan 1970 00:00:00 GMT; '
        'Domain=foo.bar.com; Secure; HttpOnly; Version=1.0; Comment=comment; SameSite=lax'
    )

    cookie = Cookie('foo', 'bar')
   

# Generated at 2022-06-14 07:04:00.458833
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cj = CookieJar({})
    cj['peterpan'] = 'fairytail'
    cj['peterpan'] = 'fairytail2'
    cj['harold'] = 'maude'
    del cj['peterpan']
    assert cj['peterpan'] is None
    assert cj['harold'] == 'maude'



# Generated at 2022-06-14 07:04:02.109770
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"



# Generated at 2022-06-14 07:04:09.385714
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("hello", "world")
    cookie["max-age"] = 3600
    cookie["domain"] = ".example.com"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["samesite"] = "Strict"
    # test joined into a string
    assert (
        cookie.__str__()
        == "hello=world; Max-Age=3600; Domain=.example.com; Secure; HttpOnly; SameSite=Strict"
    )


# ------------------------------------------------------------ #
#  Custom SimpleCookie
# ------------------------------------------------------------ #

# Generated at 2022-06-14 07:04:17.575234
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    jar['hello'] = 'world'
    jar['hello'] = 'Mars'
    assert headers == {'Set-Cookie': ['hello=world', 'hello=Mars']}
    del jar['hello']
    assert headers == {'Set-Cookie': ['hello=', 'hello=Mars']}
    del jar['hello']
    assert headers == {'Set-Cookie': ['hello=', 'hello=Mars']}
    assert jar == {}



# Generated at 2022-06-14 07:04:29.083390
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie("foo", "bar")
    c["expires"] = datetime.now()
    c["max-age"] = "15"
    c["secure"] = True
    c["httponly"] = False
    c["version"] = 1
    c["samesite"] = "Lax"
    c["path"] = "/"
    c["comment"] = "I'm a comment"
    c["domain"] = "test.test"
    out = str(c)

    # Should have the fields
    for field in ("expires", "max-age", "secure", "httponly", "version"):
        assert field in out

    # Should not have these fields
    for field in ("foo", "bar", "path"):
        assert field not in out


# Generated at 2022-06-14 07:04:42.057213
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    If the Content-Type header is set to "text/html", then the trailing
    newline is stripped.
    """
    c = Cookie("key", "value")
    assert c.__str__() == 'key=value'

    c = Cookie("key", "value")
    c["expires"] = datetime.now()
    assert 'expires' in c.__str__()

    c = Cookie("key", "value")
    c["expires"] = "foo"
    assert 'expires' not in c.__str__()

    c = Cookie("key", "value")
    c["path"] = "/"
    assert 'path' not in c.__str__()

    c = Cookie("key", "value")
    c["comment"] = "foo"
    assert 'comment' in c.__str__

# Generated at 2022-06-14 07:05:03.273362
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    start_str1 = 'new_session=\'\'\n'
    start_str2 = 'old_session=\'\'\n'
    cookie1 = Cookie('new_session', '')
    cookie2 = Cookie('old_session', '')
    print(cookie1 + cookie2)



# Generated at 2022-06-14 07:05:14.414357
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    # test add with key-value pair
    cookies['key'] = 'value'
    assert cookies['key'] == 'value'
    assert cookies['key'].value == 'value'
    # test set with key-value pair
    cookies['key'] = 'value2'
    assert cookies['key'] == 'value2'
    assert cookies['key'].value == 'value2'
    # test remove with del
    del cookies['key']
    assert not cookies.get('key')
    assert not cookies.cookie_headers.get('key')


# Generated at 2022-06-14 07:05:28.143638
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name', 'value')
    assert str(cookie) == 'name=value'

    cookie['Version'] = 0
    cookie['Max-Age'] = 'Max-Age'
    assert str(cookie) == 'name=value; Version=0; Max-Age=Max-Age'

    cookie['Max-Age'] = 123  # max-age must be integer type
    assert str(cookie) == 'name=value; Version=0; Max-Age=123'

    cookie['Expires'] = 'Expires'
    assert str(cookie) == 'name=value; Version=0; Max-Age=123; Expires=Expires'

    expires = datetime(year=2019, month=12, day=20)
    cookie['Expires'] = expires

# Generated at 2022-06-14 07:05:37.448855
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from hypercorn.config import Config
    from hypercorn.header import Headers
    test_key = "test-cookie"
    test_value = "value"
    headers = Headers()
    config = Config()
    cj = CookieJar(headers)
    cj[test_key] = test_value

    # check test_key is in the dictionary of headers
    assert headers.get(cj.header_key) is not None

    # check cookie_header dictionary is not empty
    assert len(cj.cookie_headers) == 1

    del cj[test_key]

    # check test_key is no longer in the dictionary of headers
    assert headers.get(cj.header_key) is None

    # check cookie_header dictionary is empty
    assert len(cj.cookie_headers) == 0


# Generated at 2022-06-14 07:05:42.118464
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():

    # Arrange
    key = "key"
    value = "value"
    cd = Cookie(key, value)

    # Act
    actual = str(cd)

    # Assert
    assert actual == "%s=%s" % (key, _quote(value))


# Generated at 2022-06-14 07:05:50.834533
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('test', 'asdf')
    cookie['expires'] = datetime.now()
    cookie['path'] = '/'
    cookie['comment'] = 'test'
    cookie['domain'] = 'test.com'
    cookie['max-age'] = 1
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['version'] = '0.0'
    cookie['samesite'] = 'none'
    assert cookie['expires'] == datetime.now()
    assert cookie['path'] == '/'
    assert cookie['comment'] == 'test'
    assert cookie['domain'] == 'test.com'
    assert cookie['max-age'] == 1
    assert cookie['secure'] == True
    assert cookie['httponly'] == True
    assert cookie['version'] == '0.0'
   

# Generated at 2022-06-14 07:06:05.586434
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("test", "test")
    assert str(c) == "test=test"

    c = Cookie("test", "this is a test")
    assert str(c) == 'test="this is a test"'

    c = Cookie("test", "this is a test")
    c["path"] = "/"
    assert str(c) == 'test="this is a test"; Path=/'

    c = Cookie("test", "this is a test")
    c["domain"] = "test.com"
    assert str(c) == 'test="this is a test"; Domain="test.com"'

    c = Cookie("test", "this is a test")
    c["version"] = 1
    assert str(c) == 'test="this is a test"; Version=1'

    c = Cookie("test", "this is a test")

# Generated at 2022-06-14 07:06:11.035729
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "TESTKEY"
    value = "TESTVALUE"
    cookie = Cookie(key, value)
    cookie["path"] = "/"
    cookie["samesite"] = "STrict"
    assert(str(cookie) == "TESTKEY=TESTVALUE; Path=/; SameSite=Strict")
# ------------------------------------------------------------ #
#  Getter/Setter
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:06:24.923785
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():

    headers = CIMultiDict({
        "content-type": "text/plain",
        "content-length": "12",
        "cookie": "key1=value1; key2=value2; key3=value3"
    })
    cookies = CookieJar(headers)

    # Initialise cookies with the cookies from the request
    for morsel in cookies.iter_parsed():
        cookies[morsel.key] = morsel.value

    # Assert all the cookies were read in
    assert len(cookies) == 3
    assert cookies["key1"] == "value1"
    assert cookies["key2"] == "value2"
    assert cookies["key3"] == "value3"

    assert not cookies.cookie_headers.get("key2")

    # Delete cookie
    del cookies["key2"]

    #

# Generated at 2022-06-14 07:06:33.305223
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie(key="test", value="test")
    from pytest import raises

    with raises(KeyError):
        cookie["expires"] = ""
    with raises(KeyError):
        cookie["path"] = ""
    with raises(KeyError):
        cookie["comment"] = ""
    with raises(KeyError):
        cookie["domain"] = ""
    with raises(KeyError):
        cookie["max-age"] = ""
    with raises(KeyError):
        cookie["secure"] = ""
    with raises(KeyError):
        cookie["httponly"] = ""
    with raises(KeyError):
        cookie["version"] = ""
    with raises(KeyError):
        cookie["samesite"] = ""
    with raises(KeyError):
        cookie["expires"] = ""