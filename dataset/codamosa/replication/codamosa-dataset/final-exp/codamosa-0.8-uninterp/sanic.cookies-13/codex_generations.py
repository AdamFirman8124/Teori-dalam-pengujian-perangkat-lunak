

# Generated at 2022-06-14 06:57:35.538852
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    dict_ = {
        "expires": "expires",
        "path": "Path",
        "comment": "Comment",
        "domain": "Domain",
        "max-age": "Max-Age",
        "secure": "Secure",
        "httponly": "HttpOnly"
    }
    
    cookie = Cookie("test_key", "test_value")
    cookie.update(dict_)

    # result of the function:
    result = cookie.__str__()

    # expected output
    expected_result = "test_key=test_value; expires=expires; Path=Path; comment=Comment; Domain=Domain; Max-Age=Max-Age; Secure; HttpOnly"

    # compare results
    assert result == expected_result


# Generated at 2022-06-14 06:57:49.091737
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    from datetime import datetime

    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"

    cookie["expires"] = datetime(2018, 1, 1)
    assert str(cookie) == "name=value; Expires=Mon, 01-Jan-2018 00:00:00 GMT"

    cookie["max-age"] = 123
    assert str(cookie) == "name=value; Expires=Mon, 01-Jan-2018 00:00:00 GMT; Max-Age=123"

    cookie["max-age"] = "abc"
    assert str(cookie) == "name=value; Expires=Mon, 01-Jan-2018 00:00:00 GMT; Max-Age=abc"

    cookie["domain"] = "example.com"

# Generated at 2022-06-14 06:57:58.362053
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    test_cases = [
        ('expires', datetime(2020, 8, 15)),
        ('max-age', 12),
        ('comment', "Hello World"),
        ('domain', "localhost"),
        ('path', "/"),
        ('secure', True),
        ('httponly', True),
        ('version', 1),
        ('samesite', "lax"),
    ]

    for key, value in test_cases:
        c = Cookie("key", "val")
        c[key] = value
        assert c[key] == value
        assert c[key.lower()] == value



# Generated at 2022-06-14 06:58:04.903707
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    EXPECTED = "name=value; path=path; domain=domain; max-age=10; expires=expires; secure; HttpOnly"
    cookie = Cookie("name", "value")
    cookie["path"] = "path"
    cookie["domain"] = "domain"
    cookie["max-age"] = 10
    cookie["expires"] = "expires"
    cookie["secure"] = True
    cookie["httponly"] = True

    assert str(cookie) == EXPECTED

# Generated at 2022-06-14 06:58:18.013391
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from hypercorn.asyncio.trio import serve as trio_serve
    from hypercorn.config import Config
    from hypercorn.trio.run import serve as run_serve
    from hypercorn.trio.base import TrioStarter

    # pragma: no cover
    import trio
    import uvicorn

    port = 8900

    @uvicorn.middleware("request")
    async def clear_cookies_middleware(request):
        if "clear-cookies" in request.query_params:
            # clear cookie jar
            request.scope["cookie_jar"].clear()
            # clear individual cookies
            if "clear-foo" in request.query_params:
                del request.scope["cookie_jar"]["foo"]
            if "clear-bar" in request.query_params:
                del request

# Generated at 2022-06-14 06:58:21.893364
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():

    headers = {"Set-Cookie": ["name=Julien"]}
    cj = CookieJar(headers)
    del cj["name"]

    assert cj.headers["Set-Cookie"] == []



# Generated at 2022-06-14 06:58:35.263552
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    cj = CookieJar(headers)

    # Case when the cookie doesn't exist and its attempted deletion
    # (should act as if cookie has expired)
    cj["non-existent"] = "value"
    assert headers.get("set-cookie") == "non-existent=value"
    del cj["non-existent"]
    assert cj.get("non-existent") == None
    assert headers.get("set-cookie") == "non-existent=; Max-Age=0"

    # Case when the cookie does exist and its deletion
    cj["existent"] = "value"
    assert headers.get("set-cookie") == "existent=value"
    del cj["existent"]
    assert cj.get("existent") == None
    assert headers.get("set-cookie") == None

# Generated at 2022-06-14 06:58:39.004367
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    headers.add("Set-Cookie", "name=value")
    cookies = CookieJar(headers)
    del cookies["name"]
    assert not headers.get("Set-Cookie")


# Generated at 2022-06-14 06:58:45.296299
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    ch = dict()
    cookies = CookieJar(ch)
    cookies['key'] = 'value'

    assert 'key' in cookies
    assert ch['Set-Cookie'] == 'key=value; Path=/'

    del cookies['key']
    assert 'key' not in cookies
    assert not ch.get('Set-Cookie')


# Generated at 2022-06-14 06:58:56.660964
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"
    cookie = Cookie("key", "value")
    cookie["expires"] = datetime(
        2018, 5, 10, 14, 48, 53, 830269, tzinfo=datetime.utc
    )
    assert str(cookie) == "key=value; Expires=Thu, 10-May-2018 14:48:53 GMT"
    cookie = Cookie("key", "value")
    cookie["max-age"] = 50
    assert str(cookie) == "key=value; Max-Age=50"
    cookie = Cookie("key", "value")
    cookie["secure"] = True
    assert str(cookie) == "key=value; Secure"
    cookie["httponly"] = True

# Generated at 2022-06-14 06:59:14.869207
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('UserName', 'John Smith')
    cookie['Expires'] = 'Sun, 15-Jul-2018 00:10:00 GMT'
    cookie["Max-Age"] = 3600
    cookie["Version"] = 1
    cookie["Comment"] = "Just having some fun!"
    cookie["Path"] = "/"
    cookie["Domain"] = 'www.example.com'
    cookie["Secure"] = True
    print(cookie)
    
    cookie = Cookie('UserName', 'John Smith')
    cookie['Expires'] = 'Sun, 15-Jul-2018 00:10:00 GMT'
    cookie["Max-Age"] = 3600
    cookie["Version"] = 1
    cookie["Comment"] = "Just having some fun!"
    cookie["Path"] = "/"
    cookie["Domain"] = 'www.example.com'
   

# Generated at 2022-06-14 06:59:28.013868
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from aiohttp import web
    from aiohttp.test_utils import make_mocked_request

    headers = web.MultiDict({"Anything": "None"})
    cj = CookieJar(headers)
    req = make_mocked_request("GET", "/")

    # If this cookie doesn't exist, add it to the header keys
    cookie_name = "Cookies"
    cj[cookie_name] = cookie_name
    value = "Cookies"
    assert value == cj[cookie_name]
    assert value == req.cookies[cookie_name]

    # The cookie already exists
    cookie_name = "Waffle"
    cj[cookie_name] = cookie_name
    value = "Cookie"
    cj[cookie_name] = value

# Generated at 2022-06-14 06:59:30.808030
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('key', 'value')
    cookie['Max-Age'] = '20'   
    #assertEquals(cookie['Max-Age'], '20') 


# Generated at 2022-06-14 06:59:38.503321
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookie_jar = CookieJar(headers)

    cookie_jar["foo"] = "bar"
    assert cookie_jar["foo"].value == "bar"

    del cookie_jar["foo"]
    assert headers.get("Set-Cookie") is None

    with pytest.raises(KeyError):
        del cookie_jar["foo"]

    assert headers.get("Set-Cookie") is None

# Generated at 2022-06-14 06:59:51.381373
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from mitmproxy.http import HTTPFlow
    from mitmproxy.test import tflow
    from mitmproxy import http

    flow = tflow.tflow()
    flow.request.headers["cookie"] = "foo=bar"
    flow.request.headers["cookie"] = "bar=baz"
    cookie_jar = CookieJar(flow.request.headers)

    # ensure cookie was stored under k-v pair
    assert 'bar' in cookie_jar
    assert cookie_jar['bar'].value == 'baz'

    # ensure cookie was properly set in header
    assert 'cookie' in flow.request.headers
    assert 'bar=baz' in flow.request.headers["cookie"]

    # delete this cookie
    del cookie_jar['bar']

    # ensure cookie is gone from the jar
    assert 'bar' not in cookie

# Generated at 2022-06-14 06:59:56.048665
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    headers.add('Set-Cookie', "username=john")
    cookies = CookieJar(headers)
    del cookies['username']

    assert cookies.get('username', None) is None

# Generated at 2022-06-14 07:00:05.256465
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Test case 1:
    cookie = Cookie("cookie_key", "cookie_value")
    output = cookie.__str__()
    assert output == "cookie_key=cookie_value", "Expected output is: cookie_key=cookie_value"

    # Test case 2:
    cookie = Cookie("cookie_key", "cookie_value")
    cookie["max-age"] = 7200
    cookie["secure"] = True
    output = cookie.__str__()
    assert output == "cookie_key=cookie_value; Max-Age=7200; Secure", "Expected output is: cookie_key=cookie_value; Max-Age=7200; Secure"



# Generated at 2022-06-14 07:00:18.214524
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from mimetypes import guess_type
    from werkzeug.http import parse_cache_control_header

    def verify_cookie(header, expected_key, expected_value):
        assert len(header) == 1
        assert header[0].key == expected_key
        assert header[0].value == expected_value

    raw_headers = [
        ("Content-Type", "text/html; charset=utf-8"),
        (
            "Cache-Control",
            "no-cache, private, no-store, must-revalidate, max-stale=0, "
            "post-check=0, pre-check=0",
        ),
    ]
    headers = Headers()
    for name, value in raw_headers:
        headers.add(name, value)

    jar = CookieJar(headers)
   

# Generated at 2022-06-14 07:00:27.565198
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers(ServerSentEvent)
    jar = CookieJar(headers)
    jar["foo"] = "bar"
    assert jar.cookie_headers["foo"] == jar.header_key
    assert headers.get(jar.header_key) == "foo=bar; Path=/; Max-Age=0"
    del jar["foo"]
    assert jar.cookie_headers == {}
    assert headers.get(jar.header_key) != "foo=bar; Path=/; Max-Age=0"

# Generated at 2022-06-14 07:00:38.396711
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie1 = Cookie("name1", "value1")
    cookie1["path"] = "/"
    cookie2 = Cookie("name2", "value2")
    cookie2["path"] = "/"

    headers = MultiHeader()

    cookie_jar = CookieJar(headers)

    cookie_jar["name1"] = cookie1
    cookie_jar["name2"] = cookie2

    del cookie_jar["name1"]

    assert "name1" not in cookie_jar.cookie_headers
    assert "name2" in cookie_jar.cookie_headers

    assert "name1" not in cookie_jar
    assert "name2" in cookie_jar

    cookie_jar.headers.add(cookie_jar.header_key, cookie1)

    assert "name1" in cookie_jar.cookie_headers
    assert "name2" in cookie_

# Generated at 2022-06-14 07:00:44.170181
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "value")
    assert str(cookie) == "key=value"

# Generated at 2022-06-14 07:00:50.867959
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar(dict())
    key = "test"
    value = "test"
    cookie = cookie_jar[key] = Cookie(key, value)
    assert value == cookie.value
    del cookie_jar[key]
    assert not cookie_jar.get(key)
    cookie = cookie_jar[key] = Cookie(key, value)
    assert value == cookie.value
    cookie_jar[key]['max-age'] = 0
    del cookie_jar[key]
    assert not cookie_jar.get(key)


# Generated at 2022-06-14 07:00:54.263532
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    header = dict()
    jar = CookieJar(header)
    jar["hello"] = "world"
    assert header["Set-Cookie"] == "hello=world; Path=/"


# Generated at 2022-06-14 07:01:08.243085
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("foo", "123")
    assert str(c) == "foo=123"
    c["secure"] = True
    assert str(c) == "foo=123; Secure"
    c["path"] = "/foo"
    assert str(c) == "foo=123; Path=/foo; Secure"
    c["domain"] = "example.com"
    assert str(c) == "foo=123; Domain=example.com; Path=/foo; Secure"
    c["comment"] = "hello"
    assert str(c) == "foo=123; Domain=example.com; Path=/foo; Comment=hello; Secure"
    c["httponly"] = True
    assert str(c) == "foo=123; Domain=example.com; Path=/foo; Comment=hello; Secure; HttpOnly"

# Generated at 2022-06-14 07:01:20.920799
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    expected_output = "test_name=test_value; Path=/; expires=expires_value; \
    Domain=domain_value; Max-Age=max-age_value; Secure; HttpOnly; \
    Version=version_value; SameSite=samesite_value"
    d = {"expires": 'expires_value', "path": "/", "domain": "domain_value",
         "max-age": "max-age_value", "secure": True, "httponly": True,
         "version": "version_value", "samesite": "samesite_value"}
    c = Cookie("test_name", "test_value")
    for key in d:
        c[key] = d[key]
    assert str(c) == expected_output

# Generated at 2022-06-14 07:01:23.378750
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    cookies = CookieJar(headers)
    cookies["test"] = "test"
    del cookies["test"]

# Generated at 2022-06-14 07:01:29.754461
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value", "Cookie.__str__ should return value for Set-Cookie"
    
    cookie["path"] = "/"
    assert str(cookie) == "name=value; Path=/", "Cookie.__str__ should return value for Set-Cookie with extra Set-Cookie field"


# Generated at 2022-06-14 07:01:36.764578
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    jar = CookieJar(headers)
    jar['key1'] = 'value1'
    jar['key2'] = 'value2'
    assert jar['key1'].value == 'value1'
    assert jar['key2'].value == 'value2'
    del jar['key1']
    del jar['key2']
    assert jar.keys() == set()

# Generated at 2022-06-14 07:01:42.528795
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {'Set-Cookie': ['key=value; Path=/']}
    cookiejar = CookieJar(headers)
    assert "key" in cookiejar.cookie_headers
    del cookiejar["key"]
    assert "key" not in cookiejar.cookie_headers
    assert "key=value; Path=/" not in cookiejar.headers
    assert "key" not in cookiejar.cookie_headers


# Generated at 2022-06-14 07:01:50.157120
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict()
    cookies = CookieJar(headers)
    cookies["name"] = "value"
    cookies["name"] = "value"
    assert str(cookies) == "name=value"
    assert headers.getlist("Set-Cookie") == ["name=value"]

    cookies["name2"] = "value2"
    assert headers.getlist("Set-Cookie") == ["name=value", "name2=value2"]



# Generated at 2022-06-14 07:01:59.541114
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_1 = Cookie("name_1", "value_1")
    cookie_jar = CookieJar({})
    cookie_jar["name_1"] = cookie_1
    assert len(cookie_jar.keys()) == 1

    cookie_jar.__delitem__("name_1")
    assert len(cookie_jar.keys()) == 0
    assert len(cookie_jar.cookie_headers.keys()) == 0


# Generated at 2022-06-14 07:02:04.488910
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
  test_headers = dict()
  test_cookieJar = CookieJar(test_headers)
  test_cookieJar['foo'] = 'bar'
  assert('Set-Cookie' in test_headers)
  assert('foo=bar' in test_headers['Set-Cookie'])
  return True


# Generated at 2022-06-14 07:02:16.159532
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class FakeHeaders:
        def __init__(self):
            self.headers = {}

        def add(self, key, value):
            if key not in self.headers:
                self.headers[key] = []
            self.headers[key].append(value)

        def popall(self, key):
            if key not in self.headers:
                return []
            cookies = self.headers.get(key)
            del self.headers[key]
            return cookies

    fh = FakeHeaders()
    cj = CookieJar(fh)
    cj["test_cookie"] = "test_value"
    cj["test_cookie2"] = "test_value2"
    cj["test_cookie3"] = "test_value3"

# Generated at 2022-06-14 07:02:29.705532
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('key', 'value')
    assert(str(cookie) == 'key=value')
    cookie['max-age'] = '10'
    assert(str(cookie) == 'key=value; Max-Age=10')
    cookie['path'] = '/'
    assert(str(cookie) == 'key=value; Max-Age=10; Path=/')
    cookie['domain'] = 'localhost'
    assert(str(cookie) == 'key=value; Max-Age=10; Path=/; Domain=localhost')
    cookie['secure'] = True
    assert(str(cookie) == 'key=value; Max-Age=10; Path=/; Domain=localhost; Secure')
    cookie['domain'] = 'example.com'

# Generated at 2022-06-14 07:02:37.670005
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test", "test value")
    assert str(cookie) == "test=test value"

    cookie["max-age"] = 123
    cookie["path"] = "/"
    cookie["secure"] = True
    assert str(cookie) == "test=test value; Max-Age=123; Path=/; Secure"

    cookie["expires"] = datetime(2019, 6, 1, 11, 3, 47)
    assert str(cookie) == "test=test value; Max-Age=123; Path=/; Expires=Sat, 01-Jun-2019 11:03:47 GMT; Secure"

    cookie["httponly"] = True
    assert str(cookie) == "test=test value; Max-Age=123; Path=/; Expires=Sat, 01-Jun-2019 11:03:47 GMT; Secure; HttpOnly"

   

# Generated at 2022-06-14 07:02:48.136702
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("CookieName", "Value")
    assert (
        c.__str__() == "CookieName=Value"
    ), "expected CookieName=Value, got {}".format(c.__str__())
    c = Cookie("CookieName", "Value")
    c["max-age"] = 0
    assert (
        c.__str__() == "CookieName=Value; Max-Age=0"
    ), "expected CookieName=Value; Max-Age=0, got {}".format(c.__str__())
    c = Cookie("CookieName", "Value")
    c["expires"] = datetime.utcnow()

# Generated at 2022-06-14 07:02:59.617146
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("example_name", "example_value")
    cookie["path"] = "/"
    cookie["comment"] = "test comment"
    cookie["domain"] = "example.com"
    cookie["max-age"] = str(DEFAULT_MAX_AGE)
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 2
    cookie["samesite"] = "strict"

    assert (
        str(cookie)
        == 'example_name=example_value; Path=/; Comment=test comment; Domain=example.com; Max-Age=0; Secure; HttpOnly; Version=2; SameSite=strict'
    )

# Generated at 2022-06-14 07:03:02.742078
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # GIVEN a cookie
    cookie = Cookie("test", "cookie")
    # WHEN converting to str
    result = str(cookie)
    # THEN it must match the correct value
    assert result == "test=cookie"



# Generated at 2022-06-14 07:03:12.831180
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    co = Cookie('name', 'value')
    co['path'] = '/test'
    co['expires'] = 'Tue, 19 Jan 2038 03:14:07 GMT'
    co['secure'] = True
    co['HttpOnly'] = True
    co['max-age'] = 0
    co['SameSite'] = 'None'
    assert str(co) == (
        'name=value; Path=/test; expires=Tue, 19 Jan 2038 03:14:07 GMT; '
        'Secure; HttpOnly; SameSite=None; max-age=0'
    )



# Generated at 2022-06-14 07:03:18.644402
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Initialize instance of Cookie
    cookie = Cookie("cookie_name", "cookie_value")
    # Call method under test
    output = str(cookie)
    # Ensure the output is correct
    assert output == "cookie_name=cookie_value", (
        "Cookie output is not correct"
    )

# Generated at 2022-06-14 07:03:23.749404
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie("Hello","World")
    c["max-age"] = 10

    pass

# Generated at 2022-06-14 07:03:27.635392
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie("myname", "myvalue")
    c["path"] = "/"
    assert c["path"] == "/"
    assert c.value == "myvalue"


# Generated at 2022-06-14 07:03:39.054833
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"
    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    assert str(cookie) == "name=value; Path=/"
    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    cookie["domain"] = "darkmagic.com"
    assert str(cookie) == "name=value; Path=/; Domain=darkmagic.com"
    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    cookie["domain"] = "darkmagic.com"
    cookie["expires"] = datetime.utcnow()
    assert str(cookie).startswith("name=value; Path=/; Domain=darkmagic.com; Expires=")

# Generated at 2022-06-14 07:03:46.496554
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("my_key", "my_value")

    assert str(cookie) == "my_key=my_value"

    cookie["SameSite"] = "Lax"
    cookie["secure"] = True
    cookie["HttpOnly"] = True
    cookie["Path"] = "/some/path"

    assert str(cookie) == "my_key=my_value; SameSite=Lax; Secure; HttpOnly; Path=/some/path"

# Generated at 2022-06-14 07:03:59.463398
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == 'name=value'

    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    assert str(cookie) == 'name=value; Path=/'

    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    cookie["max-age"] = 3600
    assert str(cookie) == 'name=value; max-age=3600; Path=/'

    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    cookie["max-age"] = 3600
    cookie["secure"] = True
    assert str(cookie) == 'name=value; max-age=3600; Path=/; Secure'

    cookie = Cookie("name", "value")
    cookie["path"] = "/"
   

# Generated at 2022-06-14 07:04:04.201291
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie = CookieJar({})
    cookie.__delitem__('key')
    assert 'key' not in cookie
    cookie['key'] = 'value'
    assert cookie['key'] == 'value'
    cookie.__delitem__('key')
    assert 'key' not in cookie


# Generated at 2022-06-14 07:04:05.315161
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    pass


# Generated at 2022-06-14 07:04:10.877364
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers: Dict[str, str] = {}
    jar = CookieJar(headers)
    jar["foo"] = "bar"
    jar["foobar"] = "foo"
    del jar["foo"]
    assert not jar
    assert len(jar) == 0
    assert jar.cookie_headers == {}

# Generated at 2022-06-14 07:04:15.195001
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie_name = "cookie_name"
    cookie_value = "cookie_value"
    cookie = Cookie(cookie_name, cookie_value)
    assert str(cookie) == f"{cookie_name}={cookie_value}"


# ------------------------------------------------------------ #
#  Cookie Header
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:04:16.345469
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    pass # Build your own test


# Generated at 2022-06-14 07:04:31.040709
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from quart.wrappers import Headers
    from quart.signals import request_started

    async def app(environ, start_response):
        response = Response("Hello World!")
        response.set_cookie("testing", "Hello", max_age=10)
        response.delete_cookie("testing")
        return response

    headers = Headers()
    c = CookieJar(headers)

    def request_started_(sender, **kwargs):
        assert c["testing"] == ""
        assert "max-age=0" in c.headers["Set-Cookie"]

    request_started.connect(request_started_)
    with Quart(app).test_client() as client:
        response = client.get("/")
        assert response.status_code == 200



# Generated at 2022-06-14 07:04:37.800684
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeaderDict()
    test_cookiejar = CookieJar(headers)
    assert len(list(test_cookiejar.cookie_headers.keys())) == 0
    assert len(list(test_cookiejar.headers.keys())) == 0
    assert len(list(test_cookiejar.keys())) == 0
    test_cookiejar["test_key"] = "test_value"
    assert test_cookiejar["test_key"] == "test_value"
    assert len(list(test_cookiejar.cookie_headers.keys())) == 1
    assert len(list(test_cookiejar.headers.keys())) == 1
    assert len(list(test_cookiejar.keys())) == 1
    test_cookiejar["test_key"]
    test_cookiejar["test_key"]["max-age"] = 0

# Generated at 2022-06-14 07:04:46.065341
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():

    # testing CookieJar.__delitem__()
    # case 1, remove value from CookieJar
    # case 2, remove value from headers
    # case 3, cookies have multiple keys
    # case 4, key does not exist in CookieJar
    # case 5, key does not exist in headers
    # case 6, delete last cookie in cookies
    # case 7, delete last cookie in headers

    # set up
    # case 1, remove value from CookieJar
    cookies = CookieJar({})

    cookies["key2"] = "value2"
    cookies.headers["key1"] = "value1"

    # test
    cookies.__delitem__("key2")

    # assert
    # case 1, remove value from CookieJar
    assert cookies.__getitem__("key1") == "value1"

# Generated at 2022-06-14 07:04:54.188309
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('CookieName', 'CookieValue')
    assert str(cookie) == 'CookieName=CookieValue'
    cookie['expires'] = datetime.now()
    assert 'expires' in str(cookie)
    cookie['max-age'] = '3600'
    assert 'max-age' in str(cookie)
    cookie['secure'] = True
    assert 'secure' in str(cookie)

# Generated at 2022-06-14 07:05:01.036937
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = wsgiserve.headers.Headers()
    jar = CookieJar(headers)

    jar["key"] = "value"
    assert jar["key"] == "value"
    x = jar.headers["Set-Cookie"]
    assert len(x) == 1
    assert x[0].key == "key"

    del jar["key"]
    assert not jar
    assert x[0]["max-age"] == DEFAULT_MAX_AGE

# Generated at 2022-06-14 07:05:13.164605
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    # Example set of headers and cookie content
    headers = MultiHeader()
    jar = CookieJar(headers)
    jar["one"] = "some value"
    jar["two"] = "some other value"
    jar["two"]["max-age"] = DEFAULT_MAX_AGE

    # Test deletion of non-existing cookie
    with pytest.raises(KeyError):
        del jar["not_existing_cookie"]

    # Test deletion of a cookie
    del jar["two"]
    assert "two" not in jar
    assert "two" not in jar.cookie_headers

    # Test deletion of a cookie with a different format
    headers.add("Set-Cookie", "two=some other value")
    assert "two" in jar
    assert "two" in jar.cookie_headers
    del jar["two"]

# Generated at 2022-06-14 07:05:18.708313
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test", "cookie")
    cookie["httponly"] = True
    cookie["secure"] = True
    assert str(cookie) == "test=cookie; Secure; HttpOnly"

    cookie = Cookie("test", "cookie")
    cookie["max-age"] = 0
    cookie["expires"] = datetime(year=2020, month=1, day=1)
    assert str(cookie) == "test=cookie; Max-Age=0; expires=Wed, 01-Jan-2020 00:00:00 GMT"

# Generated at 2022-06-14 07:05:31.101351
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("name", "value")
    assert c.__str__() == "name=value"
    c["max-age"] = 3000
    assert c.__str__() == "name=value; Max-Age=3000"
    c["expires"] = datetime(2016, 2, 3, 4, 5)
    assert c.__str__() == "name=value; Max-Age=3000; expires=Wed, 03-Feb-2016 04:05:00 GMT"
    c.pop("max-age")
    assert c.__str__() == "name=value; expires=Wed, 03-Feb-2016 04:05:00 GMT"
    c.pop("expires")
    assert c.__str__() == "name=value"


# Generated at 2022-06-14 07:05:37.417140
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test_headers = MultiHeaderDict()
    test_cookie_jar = CookieJar(test_headers)
    test_cookie_jar[b"testkey"] = b"testvalue"
    initial_headers_dict = test_headers.dict()
    test_cookie_jar.__delitem__(b"testkey")
    final_headers_dict = test_headers.dict()
    assert final_headers_dict.get("Set-Cookie")[0] != initial_headers_dict.get("Set-Cookie")[0]
    assert not dict.get(test_headers, "Set-Cookie")
    return True


# Generated at 2022-06-14 07:05:43.897742
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["name"] = "123"
    assert "name=123" in headers["Set-Cookie"]
    del cookie_jar["name"]
    assert "name=123" not in headers["Set-Cookie"]
    assert headers.cookie_jar.cookie_headers == {}



# Generated at 2022-06-14 07:06:05.317894
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie("key", "value")
    assert c.__str__() == "key=value"

    c["expires"] = datetime(2050, 12, 31, 0, 0, 0)
    assert c.__str__() == "key=value; Expires=Sun, 31-Dec-2050 00:00:00 GMT"

    c["max-age"] = 86400
    assert c.__str__() == "key=value; Expires=Sun, 31-Dec-2050 00:00:00 GMT; Max-Age=86400"

    c["max-age"] = "86400"
    assert c.__str__() == "key=value; Expires=Sun, 31-Dec-2050 00:00:00 GMT; Max-Age=86400"

    c["max-age"] = "one"

# Generated at 2022-06-14 07:06:14.140640
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test_headers = lambda name, value: {"set-cookie": f"{name}={value}"}
    test_cookies = CookieJar(test_headers)

    # Test deletion of unexisting cookie
    test_cookies["session"] = "0123456789"
    test_cookies["session"] = ""
    del test_cookies["session"]
    assert test_cookies["session"]["max-age"] == 0
    assert test_cookies["session"].value == ""

    del test_cookies["session"]
    assert "session" not in test_cookies

    # Test deletion of existing cookie
    test_cookies["session"] = "0123456789"
    test_cookies["other_session"] = "9876543210"
    del test_cookies["session"]
    assert test_cookies

# Generated at 2022-06-14 07:06:19.248948
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """Test Cookie.__str__()."""
    cookie = Cookie("key", "value")
    test_str = cookie.__str__()
    assert test_str == "key=value"
    assert isinstance(test_str, str)



# Generated at 2022-06-14 07:06:29.282505
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar['k'] = 'v'
    cookie_jar['k']
    cookie_jar['k'] = 'v'
    assert 'k' in cookie_jar
    assert cookie_jar.get('k')
    assert len(headers) == 1
    del cookie_jar['k']
    assert not cookie_jar.get('k')
    assert not 'k' in cookie_jar
    # Now add a cookie and delete it
    cookie_jar['k'] = 'v'
    assert 'k' in cookie_jar
    assert cookie_jar.get('k')
    assert len(headers) == 1
    del cookie_jar['k']
    assert not cookie_jar.get('k')
    assert not 'k' in cookie_jar


# Unit

# Generated at 2022-06-14 07:06:32.900944
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar(MultiDict())
    cookie_jar["name"] = "value"
    cookie_jar["name1"] = "value"
    assert "name" in cookie_jar
    del cookie_jar["name"]
    assert "name" not in cookie_jar
    assert False not in cookie_jar


# Generated at 2022-06-14 07:06:36.412431
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie = CookieJar()
    cookie['url'] = '127.0.0.1'
    del cookie['url']
    assert cookie == {}
    cookie['url'] = '127.0.0.1'
    cookie['url'] = '127.0.0.2'
    assert cookie == {}
    cookie['url'] = '127.0.0.1'
    del cookie['url']
    assert cookie == {}

# Generated at 2022-06-14 07:06:40.477118
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # Arrange
    key = 'key'
    value = 'value'
    cookie = Cookie(key, value)

    # Act
    result = cookie.__str__()

    # Assert
    assert result == 'key=value'


# Generated at 2022-06-14 07:06:44.552386
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    jar["test"]
    assert jar.get("test")
    del jar["test"]
    assert not jar.get("test")
    assert not headers.set_cookie



# Generated at 2022-06-14 07:06:57.417814
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    test_cookie = Cookie('name', 'value')
    test_cookie['expires'] = datetime.now()
    assert test_cookie['expires'] != False
    test_cookie['path'] = '/'
    assert test_cookie['path'] != False
    test_cookie['comment'] = 'comment'
    assert test_cookie['comment'] != False
    test_cookie['domain'] = 'domain'
    assert test_cookie['domain'] != False
    test_cookie['max_age'] = 123
    assert test_cookie['max_age'] != False
    test_cookie['secure'] = True
    assert test_cookie['secure'] != False
    test_cookie['httponly'] = True
    assert test_cookie['httponly'] != False
    test_cookie['version'] = 'version'
    assert test_cookie['version'] != False

# Generated at 2022-06-14 07:06:59.515000
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    assert str(cookie) == "foo=bar"


# Generated at 2022-06-14 07:07:14.238889
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    s = Cookie("key", "value")
    assert s.__str__() == "key=value"

