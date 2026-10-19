

# Generated at 2022-06-14 06:57:23.464565
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = ResponseHeaders()
    jar = CookieJar(headers)
    jar["SESSIONID"] = "12345"
    del jar["SESSIONID"]
    assert "SESSIONID" not in jar
    assert "Set-Cookie" not in headers


# Generated at 2022-06-14 06:57:35.179318
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = HTTPHeaders()
    cookies = CookieJar(headers)
    cookies["name"] = "foo"
    cookies["age"] = "10"
    assert len(cookies) == 2
    assert len(cookies.cookie_headers) == 2
    assert len(cookies.headers) == 2
    assert cookies["name"] == "foo"
    assert cookies["age"] == "10"
    del cookies["name"]
    assert len(cookies) == 1
    assert len(cookies.cookie_headers) == 1
    assert len(cookies.headers) == 1
    assert cookies["age"] == "10"
    del cookies["age"]
    assert len(cookies) == 0
    assert len(cookies.cookie_headers) == 0
    assert len(cookies.headers) == 0

# Generated at 2022-06-14 06:57:41.099823
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('hello', 'there@')
    cookie['max-age'] = 3600
    cookie['expires'] = datetime(2035,1,1,1,1,1)
    cookie['domain'] = 'example.com'
    cookie['secure'] = True

    assert str(cookie) == 'hello=there%40; Max-Age=3600; expires=Wed, 01-Jan-2035 01:01:01 GMT; Domain=example.com; Secure'

# Generated at 2022-06-14 06:57:49.342321
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict()
    test_cookies = CookieJar(headers)
    test_cookies["platypus"] = "It's invovled in a lot"
    assert headers["Set-Cookie"] == 'platypus="It\\\'s invovled in a lot"'
    assert headers["set-cookie"] == 'platypus="It\\\'s invovled in a lot"'



# Generated at 2022-06-14 06:57:59.766682
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from .response import Response
    from .headers import Headers

    headers = Headers()
    CookieJar = CookieJar(headers)

    # Test 1: Test both __setitem__ and __delitem__ for cookiejar
    # Expected result: status code is 200, body is default
    # Testing point:
    #     Put a cookie in cookiejar
    #     Delete that cookie
    #     Put a cookie in cookiejar
    #     Delete that cookie
    response = Response(
        headers=Headers(
            cookie=CookieJar(
                headers,
                {
                    "first": "first",
                    "second": "second",
                }
            )
        )
    )
    # Delete first cookie
    response.headers.cookie.__delitem__('first')
    # Delete second cookie
    response.headers.cookie.__del

# Generated at 2022-06-14 06:58:02.308286
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie(key='bob', value='')
    assert c.__str__() == 'bob='



# Generated at 2022-06-14 06:58:12.751624
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from starlette.datastructures import Headers
    from starlette.testclient import TestClient
    from starlette.responses import RedirectResponse
    from starlette.endpoints import WebSocketEndpoint, WebSocketRoute
    from starlette.websockets import WebSocket

    class MyEndpoint(WebSocketEndpoint):
        encoding = "text"

        async def on_connect(self, websocket):
            await websocket.accept()

        async def on_receive(self, websocket, data):
            await websocket.send_text(data)
    
    routes = [
        WebSocketRoute("/ws", MyEndpoint)
    ]

    client = TestClient(app)
    response = client.get("/")



# Generated at 2022-06-14 06:58:23.709757
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_headers = {'shoe-size': 'http.cookies', 'birthday': 'http.cookies'}
    headers = {'http.cookies': ['shoe-size=10; Path=/', 'birthday=today']}
    cookie_jar = CookieJar(headers)
    cookie_jar.cookie_headers = cookie_headers
    assert len(headers['http.cookies']) is 2
    cookie_jar.__delitem__('shoe-size')
    assert len(headers['http.cookies']) is 1
    assert headers['http.cookies'][0] == 'birthday=today'


# Generated at 2022-06-14 06:58:35.972736
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiDict()
    my_cookie = CookieJar(headers)

    # Test cookie creation
    my_cookie['cookie_name'] = 'cookie_value'
    assert my_cookie['cookie_name'].value == 'cookie_value'
    assert my_cookie.headers['Set-Cookie'] == 'cookie_name=cookie_value; Path=/'

    # Test value update
    my_cookie['cookie_name'] = 'new_cookie_value'
    assert my_cookie['cookie_name'].value == 'new_cookie_value'
    assert my_cookie.headers['Set-Cookie'] == 'cookie_name=new_cookie_value; Path=/'

    # Test that setting the same key twice doesn't add the cookie twice
    my_cookie['cookie_name'] = 'cookie_value_again'
    assert my_

# Generated at 2022-06-14 06:58:48.649121
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test_key", "test_value")
    cookie["path"] = "/"
    cookie["domain"] = "test.test"
    cookie["max-age"] = 550000
    cookie["httponly"] = True
    cookie["secure"] = False
    cookie.set_expires(datetime.now())

    output = "%s=%s" % (cookie.key, _quote(cookie.value)) + "; "
    output += "%s=%s" % ("Path", cookie["path"]) + "; "
    output += "%s=%s" % ("Domain", cookie["domain"]) + "; "
    output += "%s=%d" % ("Max-Age", cookie["max-age"]) + "; "
    output += "%s=" % ("HttpOnly") + "; "

# Generated at 2022-06-14 06:59:07.964172
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from collections import OrderedDict
    from quart.wrappers.cookiejar import Cookie, CookieJar

    # create two CookieJar instances
    headers = [('Set-Cookie', 'a=1; Path=/'), ('Set-Cookie', 'b=2; Path=/')]

    # set the value of COOKIES_SAMESITE to None
    environ = OrderedDict()
    environ['COOKIES_SAMESITE'] = None

    # call the constructor of CookieJar
    cookiejar = CookieJar(environ)
    cookiejar.headers = list(headers)

    # set item in the cookies
    cookiejar['a1'] = '2'
    cookiejar['b1'] = '3'
    cookiejar['c1'] = '4'

    # delete c1 from the cookies
    del cookiejar['c1']

# Generated at 2022-06-14 06:59:19.485976
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name', 'value')
    cookie.update({
        'domain': '.example.com',
        'path': '/',
        'secure': True,
        'expires': datetime(2020, 12, 31, 14, 30, 30),
        'httponly': True,
        'samesite': 'Strict',
    })
    assert str(cookie) == \
        'name=value; Domain=.example.com; Path=/; Secure; HttpOnly; ' \
        'expires=Fri, 31-Dec-2020 14:30:30 GMT; SameSite=Strict'
    cookie = Cookie('name', 'value')
    cookie.update({
        'expires': datetime(2020, 12, 31, 14, 30, 30),
    })

# Generated at 2022-06-14 06:59:27.438130
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["test"] = "value"
    del cookie_jar["test"]
    assert "test" not in cookie_jar
    assert "Set-Cookie" in headers
    assert len(headers["Set-Cookie"]) == 1
    assert "Max-Age=0" in headers["Set-Cookie"][0]


# Generated at 2022-06-14 06:59:29.802872
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("bob", "bob_value")
    assert str(cookie) == "bob=bob_value"



# Generated at 2022-06-14 06:59:43.374169
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("my_cookie", "my_value")
    assert str(cookie) == "my_cookie=my_value"

    cookie["max-age"] = 60
    assert str(cookie) == "my_cookie=my_value; Max-Age=60"

    cookie["expires"] = datetime(2012, 1, 1)
    assert str(
        cookie
    ) == "my_cookie=my_value; Max-Age=60; expires=Sun, 01-Jan-2012 00:00:00 GMT"

    cookie["secure"] = True
    cookie["httponly"] = True
    assert str(
        cookie
    ) == "my_cookie=my_value; Max-Age=60; expires=Sun, 01-Jan-2012 00:00:00 GMT; Secure; HttpOnly"

# ------------------------------------------------------------ #
#

# Generated at 2022-06-14 06:59:54.204296
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    jar = CookieJar(headers)
    jar['name'] = 'joe'
    jar['age'] = '17'
    jar['name'] = 'joe2'
    del jar['name']
    assert jar.headers == CIMultiDict([
        ('Set-Cookie', Cookie('age', '17')),
        ('Set-Cookie', Cookie('name', '"joe2"')),
        ('Set-Cookie', Cookie('name', '""'))])
    del jar['age']
    assert jar.headers == CIMultiDict([
        ('Set-Cookie', Cookie('name', '"joe2"')),
        ('Set-Cookie', Cookie('name', '""'))])

# Generated at 2022-06-14 07:00:04.513023
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookies = CookieJar(headers)
    
    key = "key"
    cookie_value = "value"
    cookies[key] = cookie_value

    # Double check the header has been set
    set_cookie_header = cookies.headers["Set-Cookie"]
    assert set_cookie_header == "key=value; Path=/; Max-Age=0; HttpOnly; SameSite=Lax", "Cookie set in header is wrong"
    
    # Remove the cookie by deleting it from the Cookie Jar
    del cookies[key]

    # Check that the cookie no longer exists in the cookies
    assert key not in cookies, "Cookie is still in the Cookie Jar"

    # Check that there is no longer a Set-Cookie Header

# Generated at 2022-06-14 07:00:08.152757
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = []
    jar = CookieJar(headers)
    jar.__setitem__("key", "value")
    assert jar["key"].value == "value"



# Generated at 2022-06-14 07:00:16.532834
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from httpcore._types import Headers
    headers = Headers()
    cookie_jar = CookieJar(headers=headers)
    cookie_jar["foo"] = "bar"
    cookie_jar["baz"] = "qwerty"

    del cookie_jar["foo"]

    expected = [('Set-Cookie', 'baz=qwerty'), ('Set-Cookie', 'foo=; Max-Age=0')]
    assert headers == Headers(expected)


# Generated at 2022-06-14 07:00:28.116786
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    """
    Item deletion from a CookieJar generates an appropriate 'Set-Cookie' entry
    If a cookie is being removed from the CookieJar and it exists, then a
    'Set-Cookie' should be generated with the name of the cookie and a max-age
    of 0.

    If a cookie is being removed from the CookieJar and it does not exist, then
    it should be added as a 'Set-Cookie' with a max-age of 0.
    """
    headers = MultiHeader()
    cj = CookieJar(headers)
    cj["Cookie1"] = "Cookie1"
    cj["Cookie2"] = "Cookie2"
    cj["Cookie3"] = "Cookie3"
    assert headers.get("Set-Cookie") == "Cookie1=Cookie1"
    assert headers.get

# Generated at 2022-06-14 07:00:44.535269
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import unittest
    import datetime
    import sys

    class Cookie__str__Test(unittest.TestCase):
        """test __str__ of Cookie"""
        def test_no_key_value_expires_max_age(self):
            """test_no_key_value_expires_max_age"""
            cookie = Cookie("key", "value")
            self.assertEqual(str(cookie), "key=value")

        def test_expires(self):
            """test_expires"""
            fmt = "%a, %d-%b-%Y %T GMT"
            now = datetime.datetime.now()
            cookie = Cookie("key", "value")
            cookie["expires"] = now
            expires = now.strftime(fmt)

# Generated at 2022-06-14 07:00:52.831751
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('test', 'testing')
    assert str(cookie) == 'test=testing'

    cookie['max-age'] = 10
    assert str(cookie) == 'test=testing; Max-Age=10'

    cookie['expires'] = datetime.today()
    assert str(cookie).startswith('test=testing; Max-Age=10; Expires=')

    cookie['secure'] = True
    assert str(cookie).startswith('test=testing; Max-Age=10; Expires=; Secure')

    cookie['HttpOnly'] = True
    assert str(cookie).startswith('test=testing; Max-Age=10; Expires=; Secure; HttpOnly')


# Generated at 2022-06-14 07:01:07.198584
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("key", "value")
    assert c.__str__() == "key=value"

    c = Cookie("key", "value")
    c["path"] = "/"
    assert c.__str__() == "key=value; Path=/"

    c = Cookie("key", "value")
    c["path"] = "/"
    c["comment"] = "This is my comment"
    assert c.__str__() == "key=value; Path=/; Comment=This is my comment"

    c = Cookie("key", "value")
    c["path"] = "/"
    c["comment"] = "This is my comment"
    c["max-age"] = 100
    assert c.__str__() == "key=value; Path=/; Comment=This is my comment; Max-Age=100"


# Generated at 2022-06-14 07:01:13.932247
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    jar["key"] = "value"
    assert jar["key"].value == "value"
    jar["key"]

    assert headers.getall(jar.header_key) == [b"key=value; Path=/"]

    del jar["key"]
    assert "key" not in jar
    assert headers.getall(jar.header_key) == []

    

# Generated at 2022-06-14 07:01:21.445888
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookiejar = CookieJar(headers)
    cookiejar["test_headers"] = "test_value"
    assert cookiejar.cookie_headers.get("test_headers") is not None
    assert headers.getall("Set-Cookie")[0] is not None
    del cookiejar["test_headers"]
    assert cookiejar.cookie_headers.get("test_headers") is None
    assert headers.getall("Set-Cookie") == []


# Generated at 2022-06-14 07:01:28.523178
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("TEST", "TEST")
    cookie["version"] = "1"
    cookie["path"] = "/"
    cookie["comment"] = "TEST COOKIE"
    cookie["domain"] = "localhost"
    cookie["expires"] = datetime.now()
    cookie["max-age"] = "3600"
    cookie["secure"] = False
    cookie["httponly"] = True
    assert str(cookie) == "TEST=TEST; Version=1; Path=/; Comment=TEST COOKIE; Domain=localhost; expires=%s; Max-Age=3600; HttpOnly" % cookie["expires"].strftime("%a, %d-%b-%Y %T GMT")

# Generated at 2022-06-14 07:01:41.166683
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar({})
    cookie_jar["a"] = "1"
    del(cookie_jar["a"]) # delete cookie with key "a"
    # Case 1: cookie "a" is not in headers
    assert len(cookie_jar) == 0 # cookie_jar is empty
    assert "a" not in cookie_jar # cookie "a" is not in cookie_jar
    assert len(cookie_jar.headers) == 0 # headers are empty
    assert "a" not in cookie_jar.headers # cookie "a" is not in headers
    assert len(cookie_jar.cookie_headers) == 0 # cookie_headers are empty
    assert "a" not in cookie_jar.cookie_headers # cookie "a" is not in cookie_headers
    # Case 2: cookie "a" is in headers

# Generated at 2022-06-14 07:01:49.620509
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = bl.MultiHeader()
    cookieJar = CookieJar(headers)
    key = "value"
    value = "test1"
    cookieJar[key] = value

    assert key in cookieJar
    assert key in headers[cookieJar.header_key]
    assert headers[cookieJar.header_key][key].value == value

    del cookieJar[key]

    assert key not in cookieJar
    assert headers[cookieJar.header_key].get(key) == None


# Generated at 2022-06-14 07:01:57.967383
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cj = CookieJar(headers)
    cj["a"] = "1"
    cj["b"] = "2"
    cj["c"] = "3"
    
    assert headers.get("Set-Cookie") == "a=1; Path=/; b=2; Path=/; c=3; Path=/"
    del cj["b"]
    assert headers.get("Set-Cookie") == "a=1; Path=/; c=3; Path=/"
    

# Generated at 2022-06-14 07:02:04.149755
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers([])
    url = URL('https://www.example.com/')
    cookies = CookieJar(headers)
    cookies['key'] = 'value'
    assert len(cookies.headers) == 1
    assert len(cookies) == 1
    assert cookies.headers[cookies.header_key] == "key=value"
    del cookies['key']
    assert len(cookies.headers) == 0
    assert len(cookies) == 0

# Generated at 2022-06-14 07:02:28.999302
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    jar = CookieJar(headers)
    assert jar == {}
    assert not headers
    jar["name"] = "Paul"
    assert jar["name"].value == "Paul"
    assert headers[jar.header_key] == "name=Paul; Path=/; Max-Age=0"
    assert jar.cookie_headers == {"name": jar.header_key}
    assert headers == {"Set-Cookie": "name=Paul; Path=/; Max-Age=0"}
    jar["name"] = "Peter"
    assert jar["name"].value == "Peter"
    assert headers[jar.header_key] == "name=Peter; Path=/; Max-Age=0"
    assert jar.cookie_headers == {"name": jar.header_key}

# Generated at 2022-06-14 07:02:42.400187
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"
    cookie["httponly"] = True
    assert str(cookie) == "name=value; HttpOnly"
    cookie["path"] = "/"
    assert str(cookie) == "name=value; Path=/; HttpOnly"
    cookie["domain"] = "example.com"
    assert str(cookie) == "name=value; Domain=example.com; Path=/; HttpOnly"
    cookie["max-age"] = 3600
    assert str(cookie) == (
        "name=value; Domain=example.com; Path=/; "
        "Max-Age=3600; HttpOnly"
    )
    cookie["expires"] = datetime(2020, 1, 1, 0, 0, 0)

# Generated at 2022-06-14 07:02:54.212738
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("cookie_key", "cookie_value")
    cookie["max-age"] = 1
    cookie["expires"] = datetime(year=2015, month=3, day=7, hour=15, minute=50, second=20)

    assert str(cookie) == "cookie_key=cookie_value; Max-Age=1; expires=Sun, 07-Mar-2015 15:50:20 GMT"


# ------------------------------------------------------------ #
#  Request/Response Interface
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:03:01.955872
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    """test_Cookie.__delitem__"""

    headers = MultiDict([])
    cookie_jar = CookieJar(headers)
    cookie_jar["key"] = "value"
    cookie_jar["key2"] = "value"
    del cookie_jar["key2"]
    assert "key2" not in cookie_jar
    assert headers["Set-Cookie"] == ["key=value"]


# Generated at 2022-06-14 07:03:15.735438
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Testing deleting a cookie from an empty CookieJar
    cookiejar = CookieJar(headers={})
    cookiejar['secret_cookie'] = 'some_secret'
    del cookiejar['secret_cookie']
    assert cookiejar.headers == {'Set-Cookie': ['']}
    # Testing removing a cookie, that was initially added to the header
    cookiejar = CookieJar(headers={})
    cookiejar['secret_cookie'] = 'some_secret'
    del cookiejar['secret_cookie']
    cookiejar['other_cookie'] = 'some_other'
    assert cookiejar.headers == {'Set-Cookie': ['other_cookie=some_other']}
    # Testing normal removal from a CookieJar with pre-existing cookies
    cookiejar = CookieJar(headers={})
    cookiejar['secret_cookie'] = 'some_secret'
   

# Generated at 2022-06-14 07:03:23.700643
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    content = {
        'key': 'username',
        'value': 'python',
        'max-age': 3,
        'expires': datetime.utcnow(),
        'path': '/',
        'comment': 'this is a comment',
        'domain': 'python.org',
        'secure': True,
        'httponly': False,
        'version': 1,
        'samesite': None,
    }

    cookie = Cookie(**content)
    actual = cookie.__str__()
    expected = 'username=python; expires=%s; max-age=3; Path=/; Comment=this is a comment; Domain=python.org; Secure' % (
        datetime.utcnow()
    )
    assert actual == expected



# ------------------------------------------------------------ #
#  Headers
# ------------------------------------------------------------

# Generated at 2022-06-14 07:03:29.251941
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # create a mock response object that can have headers added
    response = Response()
    CookieJar(response.headers)['cookieName'] = 'cookieValue'
    assert response.headers['Set-Cookie'] == 'cookieName=cookieValue'

if __name__ == "__main__":
    test_Cookie___str__()

# Generated at 2022-06-14 07:03:40.537300
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    header = Headers({"Content-Type": "text/plain"})
    cookies = CookieJar(header)
    cookies['key'] = "value"
    assert len(cookies) == 1
    assert len(header) == 1

    cookies['key2'] = "value2"
    assert len(cookies) == 2
    assert len(header) == 1

    cookies['key3'] = "value3"
    assert len(cookies) == 3
    assert len(header) == 1

    cookies['key4'] = "value4"
    assert len(cookies) == 4
    assert len(header) == 1

    del cookies['key']
    assert len(cookies) == 3
    assert len(header) == 1

    del cookies['key2']
    assert len(cookies) == 2
    assert len(header)

# Generated at 2022-06-14 07:03:46.981263
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert str(Cookie("foo", "bar")) == "foo=bar"
    assert str(Cookie("foo", "bar", {"max-age": 0})) == "foo=bar; Max-Age=0"
    assert str(Cookie("foo", "bar", {"max-age": 42})) == "foo=bar; Max-Age=42"



# Generated at 2022-06-14 07:03:53.897552
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaders()
    cookies = CookieJar(headers)
    cookies["1"] = "1"
    cookies["2"] = "2"
    cookies["3"] = "3"
    cookies["4"] = "4"
    del cookies["2"]
    assert "2" not in cookies
    cookies["5"] = "5"
    assert "5" in cookies


# Generated at 2022-06-14 07:04:08.569467
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Instanciating the required objects
    headers = {}
    cookieJar = CookieJar(headers)

    # Adding a key-value pair inside cookieJar
    cookieJar["key"] = "value"

    # Deleting an existing key
    cookieJar.__delitem__("key")

    # Deleting an non existing key
    cookieJar.__delitem__("nonExistentKey")

# Generated at 2022-06-14 07:04:17.735430
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    h: Dict[str, str] = {}
    jar = CookieJar(h)
    jar["a"] = "1"
    assert len(h) == 1
    jar["a"] = "2"
    assert len(h) == 1
    del jar["a"]
    assert len(h) == 1
    assert h["Set-Cookie"] == "a=; Max-Age=0"
    jar["b"] = "3"
    assert len(h) == 1
    assert h["Set-Cookie"] == "a=; Max-Age=0;b=3;Path=/;Max-Age=0"

if __name__ == "__main__":
    test_CookieJar___delitem__()

# Generated at 2022-06-14 07:04:19.065093
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    pass


# Generated at 2022-06-14 07:04:30.934180
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    cookies = CookieJar(headers)
    cookies["test"] = "test"
    assert "test" in cookies
    assert cookies["test"].value == "test"
    assert "Set-Cookie" in headers
    headers.pop("Set-Cookie", None)
    cookies["test"] = "new_value"
    assert "test" in cookies
    assert cookies["test"].value == "new_value"
    assert "Set-Cookie" in headers
    cookies["new_cookie"] = "new_cookie"
    assert "new_cookie" in cookies
    assert cookies["new_cookie"].value == "new_cookie"
    assert "new_cookie" in headers["Set-Cookie"]
    headers.pop("Set-Cookie", None)
    cookies["test"] = ""

# Generated at 2022-06-14 07:04:31.577088
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    assert 1 == 1

# Generated at 2022-06-14 07:04:41.550411
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = "key"
    value = "value"
    path = "path"
    max_age = "max_age"
    expires = "expires"
    secure = "secure"
    httponly = "httponly"
    cookie = Cookie(key, value)
    cookie["path"] = path
    cookie["max-age"] = max_age
    cookie["expires"] = expires
    cookie["secure"] = secure
    cookie["httponly"] = httponly
    result = cookie.__str__()
    assert result == f"{key}={_quote(value)}; Max-Age={max_age}; Path={path}; Expires={expires}; Secure; HttpOnly"

# Generated at 2022-06-14 07:04:47.327790
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cj = CookieJar(headers)

    cj['test'] = 1
    assert cj['test'].value == '1'
    assert headers['Set-Cookie'][0] == 'test=1; Path=/'
    assert cj.cookie_headers['test'] == 'Set-Cookie'
    assert headers.multi_headers['Set-Cookie'] >= 1

    cj['test'] = 2
    assert cj['test'].value == '2'
    assert headers['Set-Cookie'][0] == 'test=2; Path=/'
    assert cj.cookie_headers['test'] == 'Set-Cookie'
    assert headers.multi_headers['Set-Cookie'] >= 1

    cj['test'] = ''
    assert cj['test'].value == ''
   

# Generated at 2022-06-14 07:04:55.987150
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = CIMultiDict()
    cookie_jar = CookieJar(headers)

    cookie_jar["session"] = "token"
    print(str(cookie_jar["session"]))
    print(cookie_jar.headers.get(cookie_jar.header_key))

    cookie_jar["session"] = "new_token"
    print(str(cookie_jar["session"]))
    print(cookie_jar.headers.get(cookie_jar.header_key))


# Generated at 2022-06-14 07:05:04.441015
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookies = [{},
        {"max-age": 0},
        {"max-age": DEFAULT_MAX_AGE},
        {"expires": datetime.utcnow()},
        {"path": "/"},
        {"comment": "Test"},
        {"domain": "localhost"},
        {"secure": True},
        {"secure": False},
        {"httponly": True},
        {"httponly": False},
        {"version": "1"},
        {"samesite": "Strict"},
        {"max-age": 0, "expires": datetime.utcnow(), "path": "/", "comment": "Test", "domain": "localhost", "secure": True, "httponly": True, "version": "1", "samesite": "Strict"}]

# Generated at 2022-06-14 07:05:17.457428
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():

    c = Cookie(key="name", value="value")
    c["expires"] = "expires"
    c["path"] = "path"
    c["comment"] = "comment"
    c["domain"] = "domain"
    c["max-age"] = "max-age"
    c["secure"] = "secure"
    c["httponly"] = "httponly"
    c["version"] = "version"
    c["samesite"] = "samesite"
    assert str(c) == "name=value; expires=expires; Path=path; Comment=comment; Domain=domain; Max-Age=max-age; Secure; HttpOnly; Version=version; SameSite=samesite"

    c = Cookie(key="name", value="value")
    assert str(c) == "name=value"

   

# Generated at 2022-06-14 07:05:31.061814
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cookies = CookieJar(headers)
    # Add cookies
    cookies['abc'] = 'abc'
    cookies['xyz'] = 'xyz'
    cookies['foo'] = 'foo'
    cookies['bar'] = 'bar'
    # Sanity check
    assert len(cookies) == 4
    assert len(cookies.cookie_headers) == 4
    assert len(cookies.headers) == 4
    assert len(headers) == 4
    # Now delete cookies
    del cookies['foo']
    del cookies['xyz']
    # Sanity check
    assert len(cookies) == 2
    assert len(cookies.cookie_headers) == 2
    assert len(cookies.headers) == 2
    assert len(headers) == 2
    # Delete more cookies
    del cookies

# Generated at 2022-06-14 07:05:37.595923
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    def _str(str_cookie):
        return str(Cookie('name', str_cookie))
    
    assert _str('') == 'name='
    assert _str('abcdefghijklmnopqrstuvwxyz') == 'name=abcdefghijklmnopqrstuvwxyz'
    assert _str('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') == 'name=!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    assert _str('abcd efgh') == 'name="abcd efgh"'

# Generated at 2022-06-14 07:05:49.266483
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    h = MultiHeader()
    c = CookieJar(h)
    c["haha"] = "foo"
    assert c["haha"].value == "foo"
    assert len(h) == 1
    assert "Set-Cookie" in h
    assert h.get("Set-Cookie") == "haha=foo; Path=/; SameSite=Strict"
    c["haha"].value = "bar"
    assert c["haha"].value == "bar"
    assert "Set-Cookie" in h
    assert h.get("Set-Cookie") == "haha=bar; Path=/; SameSite=Strict"
    assert c["haha"]["path"] == "/"
    assert c["haha"]["samesite"] == "Strict"
    del c["haha"]

# Generated at 2022-06-14 07:05:50.707598
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    pass


# Generated at 2022-06-14 07:06:02.457838
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    Test Cookie.__str__(self)
    """
    cookie = Cookie("a", "b")
    cookie["max-age"] = 0
    cookie["httponly"] = True
    cookie["domain"] = ".example.com"
    cookie["path"] = "/"
    cookie["expires"] = datetime.fromtimestamp(0)
    assert str(cookie) == "a=b; Domain=.example.com; Expires=Thu, 01-Jan-1970 00:00:00 GMT; HttpOnly; Max-Age=0; Path=/"

# ------------------------------------------------------------ #
#  Multidict
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:06:08.341730
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers1 = MultiHeader()
    obj1 = CookieJar(headers1)
    key = "" # pass
    value = "" # pass
    obj1[key] = value
    var1 = obj1[key]
    del obj1[key]
    var2 = obj1[key]
    if (var1 != var2):
        print("Test Failed")
        return -1
    print("Test Passed")
    return 0


# Generated at 2022-06-14 07:06:15.600902
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from .headers import Headers
    from .cookie import CookieJar
    from .cookie import Cookie
    
    # case 1
    headers1 = Headers.from_headers(list())
    cookies1 = CookieJar(headers1)
    cookies1['a'] = 'b'
    assert isinstance(cookies1['a'], Cookie)
    assert cookies1['a']['path'] == '/'
    headers1 = cookies1.headers.get_all()
    assert headers1[0] == ('Set-Cookie', 'a=b')
    # case 2
    headers2 = Headers.from_headers(list())
    cookies2 = CookieJar(headers2)
    cookies2['c'] = 'd'
    cookies2['c'] = 'e'
    assert isinstance(cookies2['c'], Cookie)

# Generated at 2022-06-14 07:06:27.857841
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookies_list = []
    cookies_list.append(Cookie("username", "admin"))
    cookies_list.append(Cookie("password", "12345"))
    cookies_list.append(Cookie("hello", "world"))
    cookies_list[0]["path"] = "/"
    cookies_list[1]["path"] = "/"
    cookies_list[2]["path"] = "/"
    cookies_list[0]["max-age"] = DEFAULT_MAX_AGE
    cookies_list[1]["max-age"] = DEFAULT_MAX_AGE
    cookies_list[2]["max-age"] = DEFAULT_MAX_AGE
    cookies_list[0]["secure"] = True
    cookies_list[1]["secure"] = True

# Generated at 2022-06-14 07:06:31.857241
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict()
    jar = CookieJar(headers)
    jar["test"] = "value"
    assert headers["Set-Cookie"] == "test=value; Path=/; HttpOnly"
    assert headers.getall("Set-Cookie") == ["test=value; Path=/; HttpOnly"]
    assert len(jar) == 1


# Generated at 2022-06-14 07:06:35.142625
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers: Dict[str, str] = {}
    cookie_jar = CookieJar(headers)
    cookie_jar["mathy"] = "test"
    del cookie_jar["mathy"]
    cookie_jar["test"] = "test"
    cookie_jar["test1"] = "test"
    del cookie_jar["test"]



# Generated at 2022-06-14 07:06:59.614241
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime

    cookie = Cookie("test", "test")
    cookie["expires"] = datetime(
        year=2020,
        month=12,
        day=31,
        hour=23,
        minute=59,
        second=59,
    )
    cookie["httponly"] = True
    cookie["secure"] = True
    cookie["path"] = "/"

    assert str(cookie) == (
        "test=test;"
        "Expires=Wed, 31-Dec-2020 23:59:59 GMT;"
        "Path=/;"
        "HttpOnly;"
        "Secure"
    )

# Generated at 2022-06-14 07:07:05.285364
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import io
    import sys
    from contextlib import redirect_stdout

    c = Cookie("foo", "bar")
    f = io.StringIO()
    with redirect_stdout(f):
        print(str(c))

    assert f.getvalue() == "foo=bar\n"


# Generated at 2022-06-14 07:07:15.843538
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    headers.add("Set-Cookie", "name1=value1; Max-Age=120")
    headers.add("Set-Cookie", "name2=value2; Max-Age=120")
    headers.add("Set-Cookie", "name3=value3; Max-Age=120")
    cj = CookieJar(headers)
    assert headers.get_all("Set-Cookie") == ["name1=value1; Max-Age=120", "name2=value2; Max-Age=120", "name3=value3; Max-Age=120"]
    del cj["name2"]
    assert headers.get_all("Set-Cookie") == ["name1=value1; Max-Age=120", "name3=value3; Max-Age=120"]
    # Test header key disappears