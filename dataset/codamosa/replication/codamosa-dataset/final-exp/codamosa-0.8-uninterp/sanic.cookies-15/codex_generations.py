

# Generated at 2022-06-14 06:57:41.543915
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar=CookieJar()
    cookie_jar['username']="admin"
    cookie_jar['password']="123456"
    cookie_jar.__delitem__('username')
    assert len(cookie_jar)==1
    cookie_jar.__delitem__('password')
    assert len(cookie_jar)==0


# Generated at 2022-06-14 06:57:45.722914
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('a', 'b')
    assert c.__str__() == 'a=b'
    c['max-age'] = 10
    c['domain'] = 'example.com'
    c['httponly'] = True
    c['secure'] = True
    c['samesite'] = 'strict'
    assert c.__str__() == (
        'a=b; Max-Age=10; Domain=example.com; HttpOnly; Secure; SameSite=strict'
    )

## Unit test for method encode of class Cookie

# Generated at 2022-06-14 06:57:58.260755
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert Cookie("foo", "bar").__str__() == "foo=bar"
    assert Cookie("foo", "bar").__str__() == Cookie("foo", "bar").__str__()
    c = Cookie("foo", "bar")
    c["httponly"] = True
    assert c.__str__() == "foo=bar; HttpOnly"
    c["httponly"] = False
    c["max-age"] = 1
    assert c.__str__() == "foo=bar; Max-Age=1"
    c["max-age"] = "2"
    assert c.__str__() == "foo=bar; Max-Age=2"
    c["path"] = "/"
    assert c.__str__() == "foo=bar; Max-Age=2; Path=/"
    c["expires"] = dat

# Generated at 2022-06-14 06:58:12.318698
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    cookie1 = Cookie("cookie1", "cookie1")
    jar.setdefault("cookie1", cookie1)
    cookie2 = Cookie("cookie2", "cookie2")
    jar.setdefault("cookie2", cookie2)
    cookie3 = Cookie("cookie3", "cookie3")
    jar.setdefault("cookie3", cookie3)

    assert headers == Headers(
        {"Set-Cookie": ["cookie1=cookie1",
                        "cookie2=cookie2",
                        "cookie3=cookie3"]})

    del jar["cookie3"]

    assert headers == Headers(
        {"Set-Cookie": ["cookie1=cookie1; Path=/; Max-Age=0",
                        "cookie2=cookie2"]})

    del jar["cookie1"]

# Generated at 2022-06-14 06:58:25.505608
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cookie_jar = CookieJar(headers)
    cookie_jar['lol'] = 'yes'
    cookie_jar['lol2'] = 'yes2'
    cookie_jar['lol3'] = 'yes3'
    cookie_jar['lol4'] = 'yes4'
    cookie_jar['lol5'] = 'yes5'
    cookie_jar['lol6'] = 'yes6'
    cookie_jar['lol7'] = 'yes7'
    cookie_jar['lol8'] = 'yes8'
    cookie_jar['lol9'] = 'yes9'
    cookie_jar['lol10'] = 'yes10'
    cookie_jar['lol11'] = 'yes11'
    cookie_jar['lol12'] = 'yes12'
    cookie_jar['lol13'] = 'yes13'


# Generated at 2022-06-14 06:58:31.890556
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    cookie["expires"] = "Tue, 22-Oct-2019 09:23:18 GMT"
    cookie["secure"] = False
    cookie["httponly"] = False
    cookie["path"] = "/"
    cookie["comment"] = "this is a comment"
    cookie["domain"] = "shift.com"
    cookie["max-age"] = 123
    cookie["version"] = 1
    assert (
        str(cookie)
        == "foo=bar; Path=/; Comment=this is a comment; Domain=shift.com; Max-Age=123; Secure; HttpOnly; Version=1; Expires=Tue, 22-Oct-2019 09:23:18 GMT"
    )



# Generated at 2022-06-14 06:58:45.483572
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie(key='test_key', value='test_value')
    cookie['path'] = '/'
    cookie['comment'] = 'test_comment'
    assert str(cookie) == "test_key=test_value; Comment=test_comment; Path=/"
    cookie2 = Cookie(key='test_key2', value='test_value2')
    cookie2['comment'] = 'test_comment'
    cookie2['path'] = '/'
    cookie2['max-age'] = 10
    cookie2['secure'] = True
    cookie2['version'] = 2
    assert str(cookie2) == "test_key2=test_value2; Comment=test_comment; Max-Age=10; Path=/; Secure; Version=2"


# ------------------------------------------------------------ #
#  Secure Cookie
# ------------------------------------------------------------ #



# Generated at 2022-06-14 06:58:56.825737
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    cookies["hello"] = "world!"
    cookies["key"] = "value"
    cookies["foo"] = "bar"

    # first test deletion by index
    del cookies["hello"]
    assert len(cookies) == 2

    # then test deletion by key
    # assert that it exists in the headers
    assert "hello" not in cookies
    assert "key" in cookies
    assert "foo" in cookies
    # assert that it is still in the headers
    assert len(headers.getall("Set-Cookie")) == 2
    assert len(headers.getall("Set-Cookie1")) == 0
    # it should be set to expire
    for cookie in headers.getall("Set-Cookie"):
        assert "expires" in cookie

# Generated at 2022-06-14 06:59:08.625976
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test_headers = MultiHeader()
    test_cookie_jar = CookieJar(test_headers)
    test_cookie_jar["test_key"] = "test_value"
    test_cookie_jar["test_key2"] = "test_value2"
    test_cookie_jar["test_key3"] = "test_value3"

    test_cookie_jar.__delitem__("test_key2")

    assert test_cookie_jar["test_key"] == "test_value"
    assert "test_key2" not in test_cookie_jar
    assert test_cookie_jar["test_key3"] == "test_value3"



# Generated at 2022-06-14 06:59:09.827904
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    assert True


# Generated at 2022-06-14 06:59:18.886896
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    jar = CookieJar({})
    jar["name"] = "jojo"

    # Cleanup
    del jar["name"]
    assert len(jar.cookie_headers) == 0
    assert len(jar.headers.getall("Set-Cookie")) == 0



# Generated at 2022-06-14 06:59:23.811619
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    cookies = CookieJar(headers)
    cookies["name"] = "value"
    assert headers["Set-Cookie"] == "name=value; Path=/; expires=; HttpOnly"


# Generated at 2022-06-14 06:59:35.324920
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    """Test __delitem__ method from CookieJar"""

    # CookieJar object
    CookieJar_object = CookieJar({
        'Test': 'Test'
    })
    # Set data for CookieJar object
    CookieJar_object['test1'] = 'test1'
    CookieJar_object['test2'] = 'test2'
    CookieJar_object['test3'] = 'test3'


    # Delete a cookie from CookieJar object
    del CookieJar_object['test2']

    # Assertion to check that cookie is deleted
    assert 'test2' not in CookieJar_object

    # Assertion to check all the other cookies are still present
    assert 'test1' in CookieJar_object
    assert 'test3' in CookieJar_object

    # Assertion to check that header is added correctly when cookie is added

# Generated at 2022-06-14 06:59:39.804825
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers(cookie={"name1":"value1", "name2":"value2"})

    cookie_jar = CookieJar(headers)
    del cookie_jar["name1"]
    assert cookie_jar == {}


# Generated at 2022-06-14 06:59:52.124267
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers= {'Set-Cookie': "key1=; Domain=foo; Path=/; Expires=Wed, 08 May 2019 00:00:00 GMT\r\nkey2=; Domain=foo; Path=/; Expires=Wed, 08 May 2019 00:00:00 GMT" }
    
    cookieJar = CookieJar(headers)
    cookieJar["key1"] = "value1"
    cookieJar["key2"] = "value2"

    cookieJar.__delitem__("key2")
    
    # print(cookieJar)  #DEBUG
    # print(headers)    #DEBUG

    assert not('key2' in cookieJar)

# Generated at 2022-06-14 07:00:02.752312
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    ck = Cookie("test", "test")
    assert str(ck) == "test=test"
    ck["max-age"] = 200
    assert str(ck) == "test=test; Max-Age=200"
    ck["expires"] = datetime.utcnow()
    assert str(ck).startswith("test=test; Max-Age=200; expires=")
    ck["comment"] = "comment"
    assert str(ck).startswith("test=test; Max-Age=200; expires=")
    ck["domain"] = "domain"
    assert str(ck).startswith("test=test; Max-Age=200; expires=")
    ck["secure"] = True
    assert str(ck).startswith("test=test; Max-Age=200; expires=")
   

# Generated at 2022-06-14 07:00:08.208608
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookiejar = CookieJar(MultiHeader())
    cookiejar["unittest"] = "unittest"
    assert 'unittest' in cookiejar.cookie_headers
    assert 'unittest' in cookiejar.headers
    del cookiejar['unittest']
    assert 'unittest' not in cookiejar.cookie_headers
    assert 'unittest' not in cookiejar.headers


# Generated at 2022-06-14 07:00:19.469199
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers({"Cookie": ["mycookie1=cookie-value1", "mycookie2=cookie-value2"]})
    cookiejar = CookieJar(headers)
    assert cookiejar.cookie_headers["mycookie1"] == "Set-Cookie"
    assert cookiejar.cookie_headers["mycookie2"] == "Set-Cookie"
    assert len(headers["Set-Cookie"]) == 2

    # Test case: key exists and cookie_headers exists
    del cookiejar["mycookie1"]
    assert not cookiejar.cookie_headers.get("mycookie1")
    assert len(headers["Set-Cookie"]) == 1

    # Test case: key exists but cookie_headers doesn't exist
    del cookiejar["mycookie1"]
    assert not cookiejar.cookie_headers.get("mycookie1")

# Generated at 2022-06-14 07:00:24.678132
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("TestCookie", "value1=1; value2=2; value3=3")
    assert str(cookie) == "TestCookie=value1=1; value2=2; value3=3; Max-Age=0"

# Generated at 2022-06-14 07:00:36.812609
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
  headers = MultiHeader()
  cookiejar = CookieJar(headers)

  # set the item with a new key = key1
  cookiejar["key1"] = "value1"
  cookie = cookiejar["key1"]
  assert isinstance(cookie, Cookie)
  assert cookie.key == "key1"
  assert cookie.value == "value1"

  key = cookiejar.cookie_headers["key1"]
  assert key == "Set-Cookie"

  cookie_value = headers["Set-Cookie"]
  assert cookie_value == "key1=value1; Path=/; Max-Age=0"
  
  # set the item with existing key = key1
  cookiejar["key1"] = "value2"
  cookie = cookiejar["key1"]
  assert cookie.value == "value2"


# Generated at 2022-06-14 07:00:51.900827
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader() 
    cookies = CookieJar(headers)

    cookies["test"] = "test"

    assert "test=test; Path=/; HttpOnly" in headers["Set-Cookie"]
    assert cookies.cookie_headers["test"] == "Set-Cookie"

    del cookies["test"]

    assert cookies.cookie_headers == {}
    assert len(headers["Set-Cookie"]) == 0

    cookies["test"] = "test"

    assert cookies.cookie_headers["test"] == "Set-Cookie"
    assert "test=test; Path=/; HttpOnly" in headers["Set-Cookie"]

    cookies["test2"] = "test2"

    assert "test2=test2; Path=/; HttpOnly" in headers["Set-Cookie"]

    del cookies["test"]


# Generated at 2022-06-14 07:01:06.424081
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    cookie_jar = CookieJar(headers)

    cookie_jar["key1"] = "value1"
    cookie_jar["key2"] = "value2"
    cookie_jar["key3"] = "value3"
    assert len(headers) == 3

    # test delete by key
    del cookie_jar["key2"]
    assert len(headers) == 2
    assert headers["Set-Cookie"] == [
        "key1=value1; Path=/;",
        "key3=value3; Path=/;",
    ]

    # test delete by not exist key
    del cookie_jar["key4"]
    assert cookie_jar["key4"] == ""

# Generated at 2022-06-14 07:01:18.348076
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    # Test exception
    key = "expires"
    value = "Sat, 13 Oct 2018 12:00:00 GMT"
    cookie = Cookie("name", "value")
    try:
        cookie[key] = value
    except KeyError as e:
        assert str(e) == "Cookie name is a reserved word"
    else:
        assert 1 == 0

    # Test exception 2
    key = "alpha"
    value = "Sat, 13 Oct 2018 12:00:00 GMT"
    cookie = Cookie("name", "value")
    try:
        cookie[key] = value
    except KeyError as e:
        assert str(e) == "Unknown cookie property"
    else:
        assert 1 == 0

    # Test exception 3
    key = "max-age"
    value = '"10"'
    cookie = Cookie

# Generated at 2022-06-14 07:01:27.952963
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    A test to try if Cookie class's __str__ method behaves correctly.
    This test uses a predefined cookie, and then compares its string
    conversion with a pre-constructed cookie.
    """
    # this is the pre-constructed string, that we're going to compare
    # to the one we get from the cookie
    expected_cookie_str = "key=value; Domain=domain; Path=path; Comment=comment; Max-Age=50; Expires=Thu, 01-Jan-1970 00:00:00 GMT; HttpOnly; Secure; Version=1; SameSite=Strict"
    # this is the Cookie that we're going to test
    test_cookie = Cookie("key","value")
    # assigning a value to all of its properties
    test_cookie["domain"] = "domain"

# Generated at 2022-06-14 07:01:40.644067
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    cookies = CookieJar(headers)
    cookies["foo"] = "bar"
    cookies["baz"] = "bar"
    cookies["baz"]["path"] = "/"
    cookies["baz"]["max-age"] = 0
    assert headers.get("Set-Cookie") == "foo=bar; Path=/; baz=bar; Path=/; Max-Age=0"
    del cookies["foo"]
    assert headers.get("Set-Cookie") == "baz=bar; Path=/; Max-Age=0"
    del cookies["baz"]
    cookies["foo"] = "bar"
    del headers["Set-Cookie"]
    assert headers.get("Set-Cookie") == None
    assert "foo" not in cookies
    assert "baz" in cookies
   

# Generated at 2022-06-14 07:01:46.262631
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookieJar = CookieJar(headers)
    cookieJar["content"] = "test"
    assert headers["Set-Cookie"] == [
        'content="test"; Path=/; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:00 GMT'
    ]

# Generated at 2022-06-14 07:01:57.893722
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime as dt

    header = Cookie('foo', 'bar')
    header['secure'] = True
    header['expires'] = dt.now()
    header['max-age'] = 100
    header['domain'] = 'localhost'
    header['path'] = '/'
    header['comment'] = 'this is a comment'
    header['version'] = '1'
    header['httponly'] = True

    assert str(header) == (
        'foo=bar; Path=/; Domain=localhost; Max-Age=100; Expires=%s; '
        'Version=1; HttpOnly; Secure' % (header['expires'].strftime('%a, %d-%b-%Y %T GMT'))
    )

# Generated at 2022-06-14 07:02:06.756135
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookies = CookieJar(headers)
    cookies["name"] = "value"

    assert cookies["name"] == "value"
    assert headers["Set-Cookie"] == "name=value; httponly; Path=/; SameSite=Lax"

    assert "name" in cookies
    assert "name" in cookies.cookie_headers

    del cookies["name"]

    assert "name" not in cookies
    assert "name" not in cookies.cookie_headers

    assert headers["Set-Cookie"] == ""

    cookies["name1"] = "value1"
    cookies["name2"] = "value2"
    cookies["name3"] = "value3"

    cookies["name1"]["path"] = "/1"
    cookies["name2"]["path"] = "/2"

# Generated at 2022-06-14 07:02:17.101599
# Unit test for method __delitem__ of class CookieJar

# Generated at 2022-06-14 07:02:22.659783
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie = CookieJar(None)
    cookie["id"] = "1234"
    cookie["id"] = "1234"
    assert cookie["id"]=="1234"
    assert isinstance(cookie, CookieJar)


test_CookieJar___delitem__()

# Generated at 2022-06-14 07:02:37.896617
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    # Test the case when the cookie doesn't exist
    cookie_jar["cookie_name"] = "cookie_value"
    assert "cookie_name=cookie_value" in headers["Set-Cookie"], "cookie not existing"
    del cookie_jar["cookie_name"]
    assert "cookie_name" not in headers, "cookie not deleted."
    # Test the case when the cookie exists
    cookie_jar["cookie_name"] = "cookie_value"
    cookie_jar["cookie_name2"] = "cookie_value2"
    assert "cookie_name=cookie_value" in headers["Set-Cookie"], "cookie existing"
    del cookie_jar["cookie_name"]

# Generated at 2022-06-14 07:02:48.240497
# Unit test for method __str__ of class Cookie

# Generated at 2022-06-14 07:02:50.353026
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name', 'value')
    assert cookie.__str__()=='name=value'

# Generated at 2022-06-14 07:03:01.395283
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    def my_test():
        headers = CIMultiDict()
        cookiejar = CookieJar(headers)
        cookiejar["key"] = "value"
        assert cookiejar["key"] == "value"
        assert headers["Set-Cookie"] == "key=value"
        assert headers.getall("Set-Cookie") == ["key=value"]
        assert headers["Set-Cookie"] == "key=value"
        # This step is the purpose of the test
        del cookiejar["key"]
        assert headers.getall("Set-Cookie") == []
        assert cookiejar.get("key") == None
    my_test()

# Generated at 2022-06-14 07:03:13.226657
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Create a cookie as follows:
    # Cookie: foo=bar; Path=/; HttpOnly; Version=1; SameSite=strict; Secure;
    cookie = Cookie('foo', 'bar')
    cookie['path'] = '/'
    cookie['httponly'] = True
    cookie['version'] = 1
    cookie['samesite'] = 'strict'
    cookie['secure'] = True
    output = cookie.__str__()
    assert output == 'foo=bar; Path=/; HttpOnly; Version=1; SameSite=strict; Secure', '__str__ output: %s != %s' % (output, 'foo=bar; Path=/; HttpOnly; Version=1; SameSite=strict; Secure')

# Generated at 2022-06-14 07:03:20.729562
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("foo", "bar")
    assert cookie.__setitem__("expires", "Tue, 04-May-2022 12:42:42 GMT")
    assert not cookie.__setitem__("expires", False)
    assert cookie.__setitem__("max-age", "123")
    assert cookie.__setitem__("version", "1")
    assert not cookie.__setitem__("secure", False)
    assert not cookie.__setitem__("httponly", False)


# Generated at 2022-06-14 07:03:34.266247
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    # Test when the input key is not a valid key
    # Check that a KeyError is raised when a non-existent key is set
    cookie = Cookie("myCookie", "myCookieValue")
    try:
        cookie["myCookieNonExistentKey"] = "myCookieNonExistentValue"
        # Should not reach here
        assert False
    except KeyError:
        pass

    # Test when input is a valid key
    # Check that a ValueError is raised when a max-age is not an integer
    cookie = Cookie("myCookie", "myCookieValue")
    try:
        cookie["max-age"] = "myCookieNonExistentValue"
        # Should not reach here
        assert False
    except ValueError:
        pass

    # Test when input is a valid key
    # Check that a ValueError is raised

# Generated at 2022-06-14 07:03:39.609788
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('key', 'value')
    cookie['expires'] = datetime(1970, 1, 1, 0, 0)
    assert cookie['expires'] == datetime(1970, 1, 1, 0, 0)

    cookie['max-age'] = '1'
    assert cookie['max-age'] == '1'

    cookie['comment'] = 'This is a comment.'
    assert cookie['comment'] == 'This is a comment.'


# Generated at 2022-06-14 07:03:51.906812
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    new_headers = {}
    cookie_jar = CookieJar(new_headers)

    # if the item is not found in header, use default way to set the cookie to delete it
    cookie_jar["key1"] = "value1"
    assert "key1" in cookie_jar
    assert cookie_jar["key1"].value == "value1"
    assert new_headers["Set-Cookie"] == "key1=value1; Path=/; Max-Age=0"

    # if the item is found in header, then delete the item directly
    new_headers = {}
    cookie_jar = CookieJar(new_headers)
    cookie_jar["key1"] = "value1"
    new_headers["Set-Cookie"] = "key1=value1; Path=/; Max-Age=0"
    assert "key1" in cookie

# Generated at 2022-06-14 07:04:06.153879
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from multipart.multipart import MultiValueHeaders
    headers: MultiValueHeaders = MultiValueHeaders(
        {
            "Set-Cookie": [
                "foo=bar;path=/;expires=Fri, 21 Mar 2014 10:37:37 GMT",
                "boo=far;path=/;expires=Fri, 21 Mar 2014 10:37:37 GMT"
            ]
        }
    )
    cookie_jar = CookieJar(headers)
    headers: MultiValueHeaders = MultiValueHeaders(
        {
            "Set-Cookie": [
                "foo=bar;path=/;expires=Fri, 21 Mar 2014 10:37:37 GMT",
                "boo=far;path=/;expires=Fri, 21 Mar 2014 10:37:37 GMT"
            ]
        }
    )

# Generated at 2022-06-14 07:04:21.187289
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():

    headers = MultiHeader()

    cookies = CookieJar(headers)
    cookies["test_cookie"] = "test_value"
    cookies["test_cookie"] = "test_value"
    cookies["test_cookie"] = "test_value"
    cookies["test_cookie"] = "test_value"
    
    assert len(cookies) == 1
    assert len(headers) == 1

    cookies["test_cookie"] = "test_value2"
    
    assert len(cookies) == 1
    assert len(headers) == 1

    cookies["test_cookie2"] = "test_value"
    cookies["test_cookie2"] = "test_value"
    
    assert len(cookies) == 2
    assert len(headers) == 2



# Generated at 2022-06-14 07:04:27.765337
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookie_jar = CookieJar([])
    assert list(cookie_jar.keys()) == []
    cookie_jar["test"] = "abc"
    assert list(cookie_jar.keys()) == ["test"]
    assert cookie_jar["test"].value == "abc"
    assert list(cookie_jar["test"].keys()) == ["path"]
    assert cookie_jar["test"]["path"] == "/"


# Generated at 2022-06-14 07:04:33.467961
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """Test for method __str__ of class Cookie"""

    # Test basic initialization
    my_cookie = Cookie("key", "value")
    expected = "key=value"
    result = str(my_cookie)

    # Assert equality
    assert (
        result == expected
    ), "Expected '{}' but received '{}' instead".format(expected, result)



# Generated at 2022-06-14 07:04:44.977170
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('test', 'hello')
    cookie['path'] = '/'
    assert str(cookie) == "test=hello; Path=/"

    cookie['max-age'] = 10
    assert str(cookie) == "test=hello; Path=/; Max-Age=10"

    cookie['expires'] = datetime(2029, 11, 17, 22, 54, 00)
    assert str(cookie) == "test=hello; Path=/; Max-Age=10; expires=Sat, 17-Nov-2029 22:54:00 GMT"

    cookie['comment'] = 'test comment'
    assert str(cookie) == "test=hello; Path=/; Max-Age=10; expires=Sat, 17-Nov-2029 22:54:00 GMT; Comment=test comment"


# Generated at 2022-06-14 07:04:54.253117
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Create an instance of CookieJar to test
    t_CookieJar_instance = CookieJar({})
    # Assign dict to instance attributes
    t_CookieJar_instance.headers = {}
    t_CookieJar_instance.cookie_headers = {}
    t_CookieJar_instance.header_key = "Set-Cookie"
    # Call __delitem__ method of instance
    t_CookieJar_instance.__delitem__("test")



# Generated at 2022-06-14 07:05:04.098710
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    x = Cookie("c1", "v1")
    assert str(x) == "c1=v1"
    x["max-age"] = 200
    assert str(x) == "c1=v1; Max-Age=200"
    x["expires"] = datetime(2018, 9, 2, 22, 2, 15)
    assert str(x) == "c1=v1; Max-Age=200; Expires=Sun, 02-Sep-2018 22:02:15 GMT"
    x["secure"] = True
    assert str(x) == "c1=v1; Max-Age=200; Expires=Sun, 02-Sep-2018 22:02:15 GMT; Secure"
    x["httponly"] = True

# Generated at 2022-06-14 07:05:13.523194
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('foo', 'bar')
    # Test invalid key
    with pytest.raises(KeyError):
        cookie["this is invalid"] = 'foo'
    # Test valid keys
    cookie["Path"] = 'foo'
    cookie["path"] = 'foo'
    cookie["PATH"] = 'foo'
    cookie["comment"] = 'foo'
    with pytest.raises(ValueError):
        cookie["max-age"] = 'test'


# Generated at 2022-06-14 07:05:22.782809
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookies = CookieJar({"name1":"value1", "name2":"value2"})
    assert(cookies["name1"] == "value1")
    assert(cookies["name2"] == "value2")
    cookies["name1"] = "newvalue1"
    assert(cookies["name1"] == "newvalue1")
    cookies["name3"] = "value3"
    assert(cookies["name3"] == "value3")
    cookies["name1"] = "newvalue1"
    assert(cookies["name1"] == "newvalue1")
    cookies["name2"] = "value2"
    assert(cookies["name2"] == "value2")
    cookies["name3"] = "newvalue3"
    assert(cookies["name3"] == "newvalue3")



# Generated at 2022-06-14 07:05:29.429962
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # set up
    headers = Headers()
    cookieJar = CookieJar(headers)
    # test
    cookieJar['cookie-name'] = 'cookie-value'
    cookieJar['cookie-name2'] = 'cookie-value2'
    cookieJar.__delitem__('cookie-name')
    expected = {"cookie-name2": "cookie-value2"}
    assert cookieJar == expected

test_CookieJar___delitem__()

# Generated at 2022-06-14 07:05:37.858912
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('test', 'value')

    assert cookie.__str__() == 'test=value'

    cookie['max-age'] = 1
    cookie['path'] = '/'
    cookie['secure'] = False

    assert cookie.__str__() == 'test=value; Path=/; Max-Age=1'

    cookie['Max-Age'] = 0
    cookie['path'] = '/path'
    cookie['secure'] = True

    assert cookie.__str__() == 'test=value; Max-Age=0; Path=/path; Secure'

    cookie['expires'] = datetime(2019, 8, 6, 15, 22, 23)
    cookie['max-age'] = 2
    cookie['secure'] = False


# Generated at 2022-06-14 07:05:56.150378
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("additional_data", "value")
    assert str(cookie) == "additional_data=value"

    cookie = Cookie("session_id", "1")
    assert str(cookie) == "session_id=1"

    # max-age property
    cookie = Cookie("session_id", "1")
    cookie["max-age"] = 100
    assert str(cookie) == "session_id=1; Max-Age=100"

    cookie = Cookie("session_id", "1")
    cookie["max-age"] = "100"
    assert str(cookie) == "session_id=1; Max-Age=100"

    # secure property
    cookie = Cookie("session_id", "1")
    cookie["secure"] = True
    assert str(cookie) == "session_id=1; Secure"

   

# Generated at 2022-06-14 07:06:08.278916
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("key", "value")
    cookie["path"] = "/"
    cookie["samesite"] = False
    cookie["expires"] = datetime(2020, 1, 1)
    assert cookie["path"] == "/"
    assert cookie["expires"] == datetime(2020, 1, 1)
    assert cookie["samesite"] == False
    assert cookie["max-age"] == None
    assert cookie["expires"] == None

    try:
        cookie["unknown-key"] = "unknown"
        assert False
    except KeyError:
        assert True
    except:
        assert False, "Unexpected exception"

    cookie["expires"] == None
    try:
        cookie["expires"] = "bad"
        assert False
    except TypeError:
        assert True

# Generated at 2022-06-14 07:06:17.722759
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = dict()
    CookieJar(headers)["test-key"] = "test-val"
    CookieJar(headers)["test-key2"] = "test-val2"
    CookieJar(headers)["test-key3"] = "test-val3"
    del CookieJar(headers)["test-key2"]

    assert "test-key" in CookieJar(headers) and "test-key2" not in CookieJar(headers) and "test-key3" in CookieJar(headers)


# Generated at 2022-06-14 07:06:24.068840
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Setup
    headers = Headers()
    cookies = CookieJar(headers)
    cookies["a"] = "a"

    # Exercise
    del cookies["a"]
    # Verify
    assert "Set-Cookie" not in cookies.headers.keys()
    assert "a" not in cookies.cookie_headers.keys()


# Generated at 2022-06-14 07:06:37.760673
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class Headers(dict):
        def popall(self, key):
            return dict.pop(self, key)

    cookies = CookieJar(Headers())
    cookies["key1"] = "value1"
    cookies["key2"] = "value2"
    cookies["key3"] = "value3"
    cookies["key4"] = "value4"
    cookies["key5"] = "value5"
    cookies["key6"] = "value6"
    cookies["key7"] = "value7"
    cookies["key8"] = "value8"
    cookies["key9"] = "value9"

# Generated at 2022-06-14 07:06:45.729675
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from quart.datastructures import Headers
    from quart.wrappers import Request

    headers = Headers()
    request = Request(
        "GET",
        "http://localhost",
        headers=headers,
        max_content_length=None,
        content_type=None,
    )
    cookies = CookieJar(headers)
    cookies["hello"] = "world"
    cookies["foo"] = "bar"
    del cookies["hello"]
    assert "hello" not in cookies
    assert "hello" not in cookies.cookie_headers
    assert "foo" in cookies
    assert "foo" in cookies.cookie_headers

# Generated at 2022-06-14 07:06:51.190960
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["testcookie"] = "testcookievalue"
    assert jar["testcookie"].value == "testcookievalue"
    del jar["testcookie"]
    with pytest.raises(KeyError):
        jar["testcookie"]

# Generated at 2022-06-14 07:07:00.934907
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"

    cookie["path"] = "/"
    cookie["httponly"] = True
    assert str(cookie) == "name=value; Path=/; HttpOnly"

    cookie["max-age"] = 60
    assert str(cookie) == "name=value; Path=/; HttpOnly; Max-Age=60"

    cookie["expires"] = datetime(year=2019, month=11, day=1)
    assert str(cookie) == "name=value; Path=/; HttpOnly; Max-Age=60; " + \
        "Expires=Fri, 01-Nov-2019 00:00:00 GMT"



# Generated at 2022-06-14 07:07:05.716012
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie("name", "value")
    with pytest.raises(KeyError):
        cookie["expires"] = 10
    with pytest.raises(KeyError):
        cookie["unknown"] = 10


# Generated at 2022-06-14 07:07:15.356145
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    cookie["max-age"] = 0
    cookie["expires"] = datetime(1970, 1, 1, tzinfo=datetime.utcnow().tzinfo)
    cookie["path"] = ""
    cookie["comment"] = ""
    cookie["domain"] = ""
    cookie["secure"] = False
    cookie["httponly"] = False
    cookie["version"] = 0
    cookie["samesite"] = ""
    assert str(cookie) == "key=value; Max-Age=0; expires=Thu, 01-Jan-1970 00:00:00 GMT; Path=; Comment=; Domain=; Secure; HttpOnly; Version=0; SameSite"