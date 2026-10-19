

# Generated at 2022-06-14 06:57:41.710073
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from starlette.requests import Request
    from starlette.responses import Response
    request = Request(
        scope="",
        headers={"Cookie": "foo=bar; baz=qux"},
        media_type="application/json",
    )
    response = Response()
    cookie_jar = CookieJar(response.headers)
    cookie_jar["foo"] = "bar"
    cookie_jar["hello"] = "world"
    cookie_jar["hello"] = "harold"
    del cookie_jar["hello"]
    cookie_jar["max_age"] = "some_value"
    cookie_jar["hello"] = "world"
    cookie_jar["max_age"] = 5
    cookie_jar["expires"] = datetime.now()
    cookie_jar.encode("utf-8")

# Generated at 2022-06-14 06:57:45.751326
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    c = Cookie('key','value')
    c['max-age'] = 0
    c.value = 'newValue'
    assert c.value == 'newValue'
    assert c['max-age'] == 0
    c['expires'] = datetime.now()


# Generated at 2022-06-14 06:57:52.442093
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    c = Cookie('test', '12345')
    c['comment'] = 'test'
    c['max-age'] = 7
    c['secure'] = True
    c['httponly'] = False
    assert c.__str__() == 'Comment=test; httponly; max-age=7; secure; test=12345'


# Generated at 2022-06-14 06:58:00.447416
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('name', 'val')
    
    cookie['expires'] = 'time'
    expected_dictionary = {'expires': 'time'}
    assert cookie == expected_dictionary

    cookie['path'] = 'path'
    expected_dictionary = {'path': 'path', 'expires': 'time'}
    assert cookie == expected_dictionary

    cookie['comment'] = 'comment'
    expected_dictionary = {'path': 'path', 'expires': 'time', 'comment': 'comment'}
    assert cookie == expected_dictionary

    cookie['domain'] = 'domain'
    expected_dictionary = {'path': 'path', 'expires': 'time', 'comment': 'comment', 'domain': 'domain'}
    assert cookie == expected_dictionary


# Generated at 2022-06-14 06:58:11.291469
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = CIMultiDict()
    headers["Set-Cookie"] = "cookiename0=cookievalue0"
    headers["Set-Cookie"] = "cookiename1=cookievalue1"
    headers["Set-Cookie"] = "cookiename2=cookievalue2"
    cookiejar = CookieJar(headers)
    for key, value in cookiejar.items():
        if key == "cookiename1":
            del cookiejar[key]
    assert "cookiename1" not in cookiejar
    assert "cookiename0" in cookiejar
    assert "cookiename2" in cookiejar
    assert len(cookiejar) == 2


# Generated at 2022-06-14 06:58:16.870444
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = {}
    cookiejar = CookieJar(headers)
    cookiejar["name"] = "Rendhag"
    assert headers["Set-Cookie"] == "name=Rendhag; Path=/; HttpOnly"


# Generated at 2022-06-14 06:58:27.659293
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('hello', '123')
    assert str(cookie) == 'hello=123'

    cookie['max-age'] = 12
    cookie['expires'] = datetime(2018, 11, 1)
    cookie['path'] = 'path'
    cookie['comment'] = 'comment'
    cookie['domain'] = 'domain'
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['version'] = 'version'
    cookie['samesite'] = 'samesite'

    assert str(cookie) == 'hello=123; Max-Age=12; expires=Thu, 01-Nov-2018 17:00:00 GMT; Path=path; Comment=comment; Domain=domain; Secure; HttpOnly; Version=version; SameSite=samesite'

    cookie = Cookie('hello', None)
    assert str

# Generated at 2022-06-14 06:58:29.889311
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    """
    Test case for method CookieJar.__setitem__
    """
    pass

# Generated at 2022-06-14 06:58:37.066690
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers(str)
    cookies = CookieJar(headers)
    cookie_name = "cookieName"
    cookies[cookie_name] = "cookieValue"

    headers_set = headers.getall("Set-Cookie")
    assert len(headers_set) == 1
    assert headers_set[0] == f"{cookie_name}=cookieValue; Path=/;"


# Generated at 2022-06-14 06:58:49.853153
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import datetime
    c = Cookie("foo", "bar")
    c["domain"] = "www.example.com"
    c["expires"] = datetime.datetime(2017, 5, 27, 21, 24, 33)
    c["secure"] = True
    c["httponly"] = True
    assert str(c) == 'foo=bar; Path=/; Domain=www.example.com; Expires=Sun, 27-May-2017 21:24:33 GMT; Secure; HttpOnly'

    c["max-age"] = 3600
    assert str(c) == 'foo=bar; Path=/; Domain=www.example.com; Expires=Sun, 27-May-2017 21:24:33 GMT; Max-Age=3600; Secure; HttpOnly'

    c["samesite"] = "lax"
   

# Generated at 2022-06-14 06:59:05.663997
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    import pytest
    # Dummy header to satisfy the constructor
    headers = {"Set-Cookie" : "dummy"}
    # Create a new CookieJar with the headers
    cookie_jar = CookieJar(headers)

    # Add the cookie to the jar
    cookie_jar["name"] = "Alex"
    assert cookie_jar["name"] == "Alex"
    # Delete the cookie
    del cookie_jar["name"]
    # Check if the cookie is deleted
    with pytest.raises(KeyError):
        cookie_jar["name"]
    assert cookie_jar == {}
    # Check that the cookie headers are empty
    assert cookie_jar.cookie_headers == {}

# Generated at 2022-06-14 06:59:12.672174
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert "name=value" == str(Cookie("name", "value"))
    assert "name=value; Path=/; Domain=localhost; " \
    "Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Secure; HttpOnly" == str(Cookie("name", "value"))

test_Cookie___str__()

# Generated at 2022-06-14 06:59:25.708231
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("foo", "bar")
    assert str(cookie) == "foo=bar"

    cookie["path"] = "/"
    assert str(cookie) == "foo=bar; Path=/;"

    cookie["path"] = "baz"
    assert str(cookie) == "foo=bar; Path=baz;"

    cookie["secure"] = True
    assert str(cookie) == "foo=bar; Path=baz; Secure"

    cookie["httponly"] = True
    assert str(cookie) == "foo=bar; Path=baz; HttpOnly; Secure"

    cookie["max-age"] = 60
    assert str(cookie) == "foo=bar; Path=baz; HttpOnly; Secure; Max-Age=60"

    cookie["comment"] = "test"

# Generated at 2022-06-14 06:59:33.334354
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    This method is a driver for unit test for method __str__ of class Cookie
    """
    cookie = Cookie("test_cookie", "test_value")
    # Test that the basic cookie formatting works
    assert str(cookie) == "test_cookie=test_value"
    # Test that the expires property is formatted as expected
    expires_test_datetime = datetime(2018, 5, 9, 17, 10, 48)
    cookie["expires"] = expires_test_datetime
    cookie_str = str(cookie)
    # Test the value of expires property
    assert cookie_str[12:36] == "expires=Wed, 09-May-2018 17:10:48 GMT"
    # Test that max-age is inserted properly
    cookie["max-age"] = 50
    cookie_str = str(cookie)
    assert cookie

# Generated at 2022-06-14 06:59:45.533298
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = Headers()
    cookie_jar = CookieJar(headers)
    # Check expected behavior
    cookie_jar["test_cookie"] = "test_value"
    assert headers.get("Set-Cookie") == "test_cookie=test_value; Path=/"
    cookie_jar["test_cookie"] = "new_value"
    assert headers.get("Set-Cookie") == "test_cookie=new_value; Path=/"
    # Check raising of error
    with pytest.raises(KeyError):
        cookie_jar["expires"] = "test_value"
    with pytest.raises(ValueError):
        cookie_jar["test_cookie"] = "new_value"
        cookie_jar["max-age"] = "not_int"
    with pytest.raises(TypeError):
        import dat

# Generated at 2022-06-14 06:59:51.905935
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_jar = CookieJar(headers={})
    cookie_jar.__setitem__(key="name", value="value")
    cookie_jar.__setitem__(key="name1", value="value")

    cookie_jar.__delitem__(key="name")

    assert("name" not in cookie_jar)


# Generated at 2022-06-14 07:00:02.514027
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeaderDict()
    cookies = CookieJar(headers)

    # Adding cookie
    cookies["session"] = "123"
    cookies["expires"] = datetime(2020, 1, 1, 0, 0, 0)
    cookies["path"] = "/"
    cookies["httpOnly"] = True

    # Adding another cookie
    cookies["age"] = "21"
    cookies["expires"] = datetime(2020, 1, 1, 0, 0, 0)
    cookies["path"] = "/"
    cookies["httpOnly"] = True

    # To add the third cookie with name "httpOnly"
    cookies["httpOnly"] = "protected"
    cookies["expires"] = datetime(2020, 1, 1, 0, 0, 0)
    cookies["path"] = "/"
    cookies["httpOnly"] = True

    #

# Generated at 2022-06-14 07:00:16.164974
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from aiohttp.multidict import MultiDict
    from aiohttp.formdata import FormData
    from .middlewares import SessionMiddleware

    def send_signal(app: web.Application):
        """ Send an aiohttp signal to register a restart task in the
            aiohttp loop.
            When middleware is enabled, aiohttp.web.Application.on_shutdown
            is called and hence the restart task is automatically added to
            the aiohttp loop.
            This is a workaround to manually add a restart task when
            middleware is disabled.
        """
        app["__aiohttp_on_shutdown"] = []
        signal = app.loop.create_future()
        app.register_on_shutdown(signal.set_result, None)
        return signal

    app = web.Application()
   

# Generated at 2022-06-14 07:00:22.159758
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    c = CookieJar()
    c.update({"name_1": "value_1"})
    c.update({"name_2": "value_2"})
    assert "name_1" in c
    assert "name_2" in c
    del c["name_1"]
    assert "name_1" not in c
    assert "name_2" in c

# Generated at 2022-06-14 07:00:34.546953
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie_1 = Cookie("name_1", "value_1")
    cookie_1["path"] = "/"
    cookie_1["max-age"] = DEFAULT_MAX_AGE
    assert str(cookie_1) == "name_1=value_1; Path=/; Max-Age=0"

    cookie_2 = Cookie("name_2", "value_2")
    cookie_2["path"] = "/"
    cookie_2["max-age"] = DEFAULT_MAX_AGE
    cookie_2["secure"] = "true"
    assert str(cookie_2) == "name_2=value_2; Path=/; Max-Age=0; Secure"

    cookie_3 = Cookie("name_3", "value_3")
    cookie_3["path"] = "/"
    cookie_3["max-age"] = DE

# Generated at 2022-06-14 07:00:39.585362
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    assert CookieJar(headers=None) == 0
    # TODO : Test skipped due to insufficient inputs
    return



# Generated at 2022-06-14 07:00:49.771232
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name', 'value')
    assert str(cookie) == 'name=value'

    cookie = Cookie('name', 'value')
    cookie['domain'] = '.test.com'
    assert str(cookie) == 'name=value; Domain=.test.com'

    cookie = Cookie('name', 'value')
    cookie['domain'] = 'test.com'
    assert str(cookie) == 'name=value; Domain=test.com'

    cookie = Cookie('name', 'value')
    cookie['domain'] = 'www.test.com'
    assert str(cookie) == 'name=value; Domain=www.test.com'

    cookie = Cookie('name', 'value')
    cookie['domain'] = 'dev.www.test.com'

# Generated at 2022-06-14 07:00:58.073465
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from multidict import CIMultiDict
    mock_headers: CIMultiDict = CIMultiDict()
    cookie_jar = CookieJar(mock_headers)
    key = "abc"
    cookie_jar[key] = "def"

    # Test for a cookie without a max-age property
    cookie_jar.__delitem__(key)
    assert mock_headers.getall("Set-Cookie") == [
        'abc=; max-age=0; Path=/; HttpOnly'
    ]
    assert cookie_jar.get(key) == None

# Generated at 2022-06-14 07:01:09.985885
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # setup some cookies
    c1 = Cookie("key1", "value1")
    c2 = Cookie("key2", "value2")
    c3 = Cookie("key3", "value3")
    c3["max-age"] = 100000
    c3["expires"] = datetime.utcnow()
    c4 = Cookie("key4", "value4")
    c4["path"] = "/value4/cookie4"
    c4["domain"] = "www.value4.com"
    c4["secure"] = True
    c4["httponly"] = True
    c5 = Cookie("key5", "value5")
    c5["comment"] = "Comment on the cookie value5"
    c5["version"] = "1"
    c5["samesite"] = "Strict"

    # check the

# Generated at 2022-06-14 07:01:20.377117
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    key = 'key'
    value = 'value'
    cookie = Cookie(key, value)
    cookie['path'] = '/'
    cookie['expires'] = datetime(2018, 3, 18)
    cookie['max-age'] = DEFAULT_MAX_AGE
    cookie['secure'] = True
    cookie['httponly'] = True

    str_cookie = str(cookie)
    assert str_cookie == 'key=value; Path=/; Max-Age=0; Expires=Sun, 18-Mar-2018 00:00:00 GMT; Secure; HttpOnly' 


# ------------------------------------------------------------ #
#  Request/Response
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:01:25.776134
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    jar = CookieJar(headers)

    jar["A"] = "this is cookie A"
    jar["B"] = "this is cookie B"
    jar["C"] = "this is cookie C"

    jar.__delitem__("A")
    assert("A" not in jar)
    assert("B" in jar)
    assert("C" in jar)


# Generated at 2022-06-14 07:01:33.913511
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class DummyHeaders:
        def add(self, _, __): pass
        def popall(self, _): return []

    dummy_headers = DummyHeaders()
    cookie_jar = CookieJar(dummy_headers)
    cookie_jar["key"] = "value"
    cookie_jar["key"] = "value"
    cookie_jar["key"] = "value"

    del cookie_jar["key"]
    assert ("key" not in cookie_jar.cookie_headers) == True

# Generated at 2022-06-14 07:01:43.094210
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from hypercorn.config import Config
    from hypercorn.trio.config import Config as TrioConfig
    from hypercorn.tasks import HeaderCollection
    from hypercorn.tasks import CookieJar as CookieJar_old
    from hypercorn.tasks import Cookie
    from hypercorn.constants import SERVER_SOFTWARE, SERVER_NAME, SERVER_PORT
    from hypercorn.utils import CIMultiDict
    from typing import List
    from urllib.parse import urlparse
    import re
    import string

    _LegalChars = string.ascii_letters + string.digits + "!#$%&'*+-.^_`|~:"
    _UnescapedChars = _LegalChars + " ()/<=>?@[]{}"


# Generated at 2022-06-14 07:01:54.017628
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("key", "spam")
    assert str(cookie) == "key=spam"

    cookie["path"] = "/"
    assert str(cookie) == "key=spam; Path=/"

    cookie["path"] = ""
    assert str(cookie) == "key=spam"

    cookie["path"] = False
    assert str(cookie) == "key=spam"

    cookie["max-age"] = "3"
    assert str(cookie) == "key=spam; Max-Age=3"

    cookie["max-age"] = 3
    assert str(cookie) == "key=spam; Max-Age=3"

    cookie["max-age"] = "a"
    assert str(cookie) == "key=spam; Max-Age=a"


# Generated at 2022-06-14 07:02:01.757539
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers: Dict[str, str] = {}
    cookiejar = CookieJar(headers)
    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    cookiejar.cookie_headers["name"] = "Set-Cookie"
    cookiejar.headers.add("Set-Cookie", cookie)

    cookiejar["name"] = "value"
    assert cookiejar.get("name") is not None
    del cookiejar["name"]
    assert cookiejar.get("name") is None

# Generated at 2022-06-14 07:02:16.369204
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    # If this cookie doesn't exist, add it to the header keys
    cookie_jar = CookieJar(headers)
    cookie_jar["z"] = "foo"
    assert headers["Set-Cookie"] == "z=foo; Path=/; Max-Age=0"
    del cookie_jar["z"]
    assert len(headers["Set-Cookie"] == 1)
    cookie_jar["z"] = "foo"
    assert headers["Set-Cookie"] == "z=foo; Path=/; Max-Age=0"
    cookie_jar["z"] = "foo2"
    assert headers["Set-Cookie"] == "z=foo2; Path=/; Max-Age=0"
    del cookie_jar["z"]
    assert len(headers["Set-Cookie"] == 1)



# Generated at 2022-06-14 07:02:19.524638
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("test", "value")
    assert str(cookie) == "test=value"


# Generated at 2022-06-14 07:02:31.488798
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    class FakeHeaders:
        def __init__(self, headers):
            self.headers = headers

        def add(self, key, value):
            self.headers[key] = value

        def popall(self, name):
            return [self.headers.pop(name)]

    headers = FakeHeaders({})
    c = CookieJar(headers)
    c["t"] = "token"
    c["e"] = "erase"
    assert "t" in c and "e" in c
    del c["t"]
    assert "t" not in c
    assert f'e={c["e"]}' in headers.headers["Set-Cookie"]
    del c["e"]
    assert "e" not in c
    assert headers.headers["Set-Cookie"] == None

    # Non existing key should not be a

# Generated at 2022-06-14 07:02:43.296259
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    assert str(cookie) == "name=value"
    cookie["httponly"] = True
    cookie["secure"] = True
    assert str(cookie) == "name=value; HttpOnly; Secure"
    cookie["path"] = "path"
    cookie["max-age"] = 3600
    assert str(cookie) == "name=value; HttpOnly; Secure; Path=path; Max-Age=3600"
    cookie["domain"] = "domain"
    cookie["version"] = "version"
    cookie["comment"] = "comment"
    cookie["expires"] = datetime.strptime("Wed, 09 Jun 2021 10:18:14 GMT", "%a, %d %b %Y %H:%M:%S %Z")

# Generated at 2022-06-14 07:02:49.003909
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = MultiDict()
    cookiejar = CookieJar(headers)
    cookiejar['key'] = 'value'
    # TEST
    assert 'key' in cookiejar
    cookiejar.__delitem__('key')
    # TEST
    assert 'key' not in cookiejar
    assert 'key' not in cookiejar.cookie_headers


# Generated at 2022-06-14 07:03:02.952263
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie = Cookie('c', '10')
    cookie['domain'] = 'localhost'
    cookie['max-age'] = 10
    cookie['expires'] = datetime.now()
    cookie['path'] = '/'
    cookie['version'] = '1'
    cookie['secure'] = True
    cookie['httponly'] = True
    cookie['samesite'] = 'lax'
    cookie['comment'] = 'TEST'
    assert cookie['c'] == '10'
    assert cookie['domain'] == 'localhost'
    assert cookie['max-age'] == 10
    assert cookie['expires'].__class__ == datetime
    assert cookie['path'] == '/'
    assert cookie['version'] == '1'
    assert cookie['secure'] == True
    assert cookie['httponly'] == True

# Generated at 2022-06-14 07:03:16.935713
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    from quart.wrappers import Response
    from quart.testing import QuartClient, QuartTestCase
    from quart.wrappers.cookies import CookieJar
    from quart import Quart
    from werkzeug.wrappers import Request
    app = Quart(__name__)

    client = QuartClient(app, Response)

    @app.route("/")
    async def home():
        # print(request.cookies)
        response = await client.get("/")
        # print(response.cookies)
        assert "hello" not in response.cookies, "Cookie cannot be deleted"
        assert len(list(response.cookies.keys())) == 2, "Cookies not deleted"
        return "ok"


# Generated at 2022-06-14 07:03:24.096852
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    test_headers = CIMultiDict()
    test_jar = CookieJar(test_headers)

    # test case 1, delete a key that doesn't exist
    test_key = "test-key"
    assert test_key not in test_jar
    assert test_jar.get(test_key) is None
    del test_jar[test_key]
    assert test_key in test_jar
    assert test_jar.get(test_key) is not None
    assert test_jar.get(test_key).value == ""
    assert "Max-Age" in test_jar.get(test_key)
    assert test_jar.get(test_key).get("Max-Age") == 0

    # test case 2, delete a key that does exist
    test_value = "test-value"

# Generated at 2022-06-14 07:03:37.157716
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers({"Content-Type": "text/html"})
    cookie_jar = CookieJar(headers)
    cookie_jar["test_key"] = "test_value"
    cookie_jar["test_key_1"] = "test_value_1"
    cookie_jar["test_key_2"] = "test_value_2"
    assert "test_key_1" in cookie_jar
    assert "test_key_2" in cookie_jar
    assert len(cookie_jar) == 3
    assert len(cookie_jar.headers.getall(cookie_jar.header_key)) == 3
    del cookie_jar["test_key_1"]
    assert len(cookie_jar) == 2
    assert "test_key_1" not in cookie_jar

# Generated at 2022-06-14 07:03:42.701038
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {"test" : "test"}
    jar = CookieJar(headers)
    jar["test"] = "test"
    del jar["test"]
    assert jar.headers.get("set-cookie") is None
    assert jar.get("test") is None


# Generated at 2022-06-14 07:03:58.930370
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.types import Receive, Scope, Send
    import uvicorn
    import asyncio
    import pytest
    from starlette.applications import Starlette
    
    class CookieQueryMiddleware:
        """
        A middleware to parse the request and response cookies
        """
        async def __call__(self, scope, receive, send):
            request = Request(scope, receive)
            response = Response()

            await self.process_request(request)
            await self.process_response(request, response)

            await response(scope, receive, send)

        async def process_request(self, request):
            # Populate the request.cookies object
            cookies = CookieJar(request.headers)
            cookie_strings = request.headers

# Generated at 2022-06-14 07:04:04.831941
# Unit test for method __setitem__ of class Cookie
def test_Cookie___setitem__():
    cookie1 = Cookie("cookie1", "value1")
    cookie1["httponly"] = True
    assert cookie1["httponly"] == True
    cookie1["max-age"] = 100
    assert cookie1["max-age"] == 100
    cookie1["expires"] = datetime(2030, 10, 12)
    assert cookie1["expires"] == datetime(2030, 10, 12)


# Generated at 2022-06-14 07:04:13.122685
# Unit test for method __delitem__ of class CookieJar

# Generated at 2022-06-14 07:04:21.331879
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie1 = Cookie(1, 2)
    expected = '1=2'
    assert str(cookie1) == expected
    cookie2 = Cookie(1, 2)
    cookie2['max-age'] = '2345'
    cookie2['path'] = '/'
    cookie2['domain'] = 'abc.tw'
    expected = '1=2; Max-Age=2345; Path=/; Domain=abc.tw'
    assert str(cookie2) == expected

# Generated at 2022-06-14 07:04:28.096391
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    import pytest

    with pytest.raises(ValueError):
        c = Cookie("testcookie", "testvalue")
        c["max-age"] = "abc"

        c.__str__()

    with pytest.raises(TypeError):
        c = Cookie("testcookie", "testvalue")
        c["expires"] = 1588998235.1370557

        c.__str__()

# ------------------------------------------------------------ #
#  Session
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:04:41.033666
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    jar = CookieJar(Headers())
    assert jar is not None

    jar["test1"] = "value1"
    jar["test2"] = "value2"

    set_cookie1 = 'Set-Cookie', 'test1="value1"; Path=/'
    set_cookie2 = 'Set-Cookie', 'test2="value2"; Path=/'
    assert set_cookie1 in jar.headers.items()
    assert set_cookie2 in jar.headers.items()

    assert jar["test1"] == "value1"
    assert jar["test2"] == "value2"

    del jar["test1"]

    assert "test1" not in jar
    assert set_cookie1 not in jar.headers.items()
    assert set_cookie2 in jar.headers.items()

    jar["test2"] = "value3"

# Generated at 2022-06-14 07:04:47.158639
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    """
    """
    c = Cookie("name", "value")
    assert c.__str__() == "name=value"

    c.__setitem__("path", "somepath")
    assert c.__str__() == "name=value; Path=somepath"

    c.__setitem__("expires", datetime(1985, 8, 26, 1, 22))
    assert c.__str__() == "name=value; Path=somepath; expires=Fri, 26-Aug-1985 01:22:00 GMT"

    c["max-age"] = 1000
    assert c.__str__() == "name=value; Path=somepath; expires=Fri, 26-Aug-1985 01:22:00 GMT; Max-Age=1000"

    c["secure"] = True

# Generated at 2022-06-14 07:04:51.272353
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("hello", "world")
    assert str(cookie) == "hello=world"
    cookie["max-age"] = 0
    assert str(cookie) == "hello=world; Max-Age=0"

# Generated at 2022-06-14 07:05:00.524307
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    headers["Content-Type"] = "text/plain"

    cookiejar = CookieJar(headers)
    cookiejar["foo"] = "bar"
    cookiejar["baz"] = ["hello","world"]

    assert "foo" in cookiejar.cookie_headers
    assert "baz" in cookiejar.cookie_headers

    del cookiejar["foo"]
    assert "foo" not in cookiejar.cookie_headers

    del cookiejar["baz"]
    assert "baz" not in cookiejar.cookie_headers

# Generated at 2022-06-14 07:05:08.318732
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    '''
    Used to test CookieJar class __delitem__
    '''
    headers = Headers()
    cookie = CookieJar(headers)
    cookie['name'] = 'value'
    cookie['prashant'] = 'Bhau'
    assert cookie.cookie_headers
    cookie.__delitem__('name')
    assert 'name' not in cookie.cookie_headers
    assert 'prashant' in cookie.cookie_headers


# Generated at 2022-06-14 07:05:19.325793
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie("name", "value")
    cookie["path"] = "/"
    cookie["expires"] = datetime(1999, 12, 31, 23, 59, 59)
    cookie["max-age"] = DEFAULT_MAX_AGE
    cookie["version"] = 1
    cookie["comment"] = "this is a test"
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["samesite"] = "lax"
    assert str(cookie) == (
        "name=value; Path=/; expires=Wed, 31-Dec-1999 23:59:59 GMT; "
        "Max-Age=0; Version=1; Comment=this is a test; Secure; "
        "HttpOnly; SameSite=lax"
    )



# Generated at 2022-06-14 07:05:32.165870
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie0 = Cookie('Test', 'test@test.com')
    assert str(cookie0) == 'Test=test@test.com'
    cookie1 = Cookie('ID', 'test')
    cookie1['domain'] = 'example.com'
    cookie1['path'] = '/'
    assert str(cookie1) == 'ID=test; Path=/; Domain=example.com'
    cookie3 = Cookie('ID', 'test')
    cookie3['domain'] = 'example.com'
    cookie3['path'] = '/'
    cookie3['expires'] = datetime(2014, 4, 16, 10, 10, 0)
    assert str(cookie3) == 'ID=test; Expires=Tue, 16-Apr-2014 10:10:00 GMT; Path=/; Domain=example.com'

# Generated at 2022-06-14 07:05:44.632934
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = dict()
    cookies = CookieJar(headers)
    cookies["p1"] = "v1"
    cookies["p2"] = "v2"
    cookies["p3"] = "v3"
    cookies["p4"] = "v4"

    assert len(cookies) == 4
    assert len(headers) == 1
    assert len(cookies.cookie_headers) == 4

    assert headers["Set-Cookie"] == ["p1=v1; Path=/", "p2=v2; Path=/", "p3=v3; Path=/", "p4=v4; Path=/"]

    # ensure set works
    cookies["p4"] = "p4 is new value"
    assert cookies["p4"] == "p4 is new value"

    assert len(cookies) == 4

# Generated at 2022-06-14 07:05:56.411443
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookie_header = "Set-Cookie"
    cookies = [Cookie("a", "a"), Cookie("b", "b"), Cookie("c", "c"), Cookie("d", "d")]
    headers = MultiHeader()
    for cookie in cookies:
        headers.add("Set-Cookie", cookie)
    cookiejar = CookieJar(headers)
    for cookie in cookies:
        cookiejar[cookie.key] = cookie.value
    assert len(cookiejar) == 4
    assert len(cookiejar.headers) == 4
    del cookiejar["c"]
    assert len(cookiejar) == 3
    assert len(cookiejar.headers) == 3
    assert cookiejar["b"]
    assert cookiejar.headers[cookie_header][-1] == cookiejar["b"]
    assert cookiejar["d"]
    assert cookiejar.headers

# Generated at 2022-06-14 07:05:59.901118
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    assert str(Cookie('c', 'v')) == 'c=v'
    assert str(Cookie('c', ' v')) == 'c=" v"'
    assert str(Cookie('c', 'v;')) == 'c="v;"'
    assert str(Cookie('c', '"v"')) == 'c="\\"v\\""'


# ------------------------------------------------------------ #
#  Sanic Cookie
# ------------------------------------------------------------ #



# Generated at 2022-06-14 07:06:09.447859
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    # assign
    cookie = Cookie("test","test")
    cookie["path"] = "/"
    cookie["comment"] = "test"
    cookie["domain"] = "127.0.0.1"
    cookie["max-age"] = 100
    cookie["secure"] = True
    cookie["httponly"] = True
    cookie["version"] = 1
    # act
    result = str(cookie)
    # assert
    assert result == "test=test; Path=/; Comment=test; Domain=127.0.0.1; Max-Age=100; Secure; HttpOnly; Version=1"
    # assign
    cookie = Cookie("test%","test")
    # act
    result = str(cookie)
    # assert
    assert result == "test%=test"
    # assign
    cookie = Cookie("test","test")


# Generated at 2022-06-14 07:06:15.032772
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    cookie = Cookie('name', 'value')
    assert str(cookie) == 'name=value'
    cookie['max-age'] = 1
    cookie['Comment'] = 'comment'
    assert str(cookie) == 'name=value; Max-Age=1; Comment=comment'

# Generated at 2022-06-14 07:06:24.884653
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    cookies = CookieJar()
    cookies["name"] = "foo bar"
    cookies["expires"] = datetime.now()
    cookies["path"] = "/"
    cookies["max-age"] = DEFAULT_MAX_AGE
    cookies["secure"] = False
    cookies["version"] = 0
    cookies["httponly"] = False
    cookies["samesite"] = "Lax"

    del cookies["samesite"]
    assert "samesite" not in cookies

    del cookies["name"]
    assert "name" not in cookies
    assert "samesite" in cookies

# Generated at 2022-06-14 07:06:28.343012
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers()
    jar = CookieJar(headers)
    jar['foo'] = 'bar'
    del jar['foo']
    assert 'foo' not in jar
    assert headers['Set-Cookie'] == 'foo=; Max-Age=0; Path=/'


# Generated at 2022-06-14 07:06:31.426655
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = MultiHeader()
    cookie_jar = CookieJar(headers)
    cookie_jar["test"] = "test"
    assert cookie_jar['test']['key'] == "test"
    assert cookie_jar['test']['value'] == "test"



# Generated at 2022-06-14 07:06:46.372074
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    cookies = CookieJar(headers=MultiHeader())
    # Test altering a cookie
    cookies["name"] = "value"
    assert cookies["name"] == "value"
    # Test adding a cookie
    cookies["name2"] = "value"
    assert cookies["name2"] == "value"
    # Test lowercasing keys
    cookies["Name2"] = "value"
    assert cookies["name2"] == "value"
    # Test replacing a cookie
    cookies["name"] = "value1"
    assert cookies["name"] == "value1"
    assert cookies["name2"] == "value"
    assert cookies["Name2"] == "value"

    # Test setting a cookie using kwargs
    cookies["kwargs"] = Cookie(key="kwargs", value="value")
    assert cookies["kwargs"] == "value"

    #

# Generated at 2022-06-14 07:06:55.061674
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = multidict.MultiDict()
    cookie = CookieJar(headers)
    # Test case 1: delete a key that exists
    cookie["key"] = "value"
    assert "key" in cookie.keys()
    cookie.__delitem__("key")
    assert "key" not in cookie.keys()

    # Test case 2: delete a key that does not exist
    cookie["key"] = "value"
    assert "key" in cookie.keys()
    cookie.__delitem__("key")
    assert "key" not in cookie.keys()

# Generated at 2022-06-14 07:07:02.777622
# Unit test for method __setitem__ of class CookieJar
def test_CookieJar___setitem__():
    headers = CIMultiDict()
    cookies = CookieJar(headers)
    cookies["key"] = "value"
    cookies["key2"] = "value2"
    cookies["key3"] = "value3"
    assert list(cookies.items()) == [
        ("key", "value"),
        ("key2", "value2"),
        ("key3", "value3"),
    ]
    assert cookies["key2"] == "value2"
    assert cookies["key3"] == "value3"
    assert "key" in cookies
    assert "key2" in cookies
    assert "key3" in cookies
    assert len(cookies) == 3



# Generated at 2022-06-14 07:07:12.455630
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = Headers({"Set-Cookie": "key3=value3; Path=/"})
    jar = CookieJar(headers)
    jar["key1"] = "value1"
    jar["key2"] = "value2"
    del jar["key2"]
    assert "key2" not in jar
    del jar["key1"]
    assert "key1" not in jar
    del jar["key3"]
    assert "key3" not in jar
    assert "Set-Cookie" not in jar.headers


# Generated at 2022-06-14 07:07:17.199536
# Unit test for method __str__ of class Cookie
def test_Cookie___str__():
    print("##### Start test_Cookie__str__() #####")
    cookie = Cookie("foo", "bar")
    cookie["max-age"] = 10
    assert str(cookie) == "foo=bar; Max-Age=10"
    print("Cookie.__str__: OK")

if __name__ == "__main__":
    test_Cookie___str__()

# Generated at 2022-06-14 07:07:21.211927
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    jar = CookieJar()
    jar["foo"] = "bar"
    assert jar["foo"] == "bar"
    del jar["foo"]
    assert len(jar) == 0


# Generated at 2022-06-14 07:07:29.998857
# Unit test for method __delitem__ of class CookieJar
def test_CookieJar___delitem__():
    headers = {}
    cookie = CookieJar(headers)
    cookie["cookie_key_1"] = "cookie_value_1"
    cookie["cookie_key_2"] = "cookie_value_2"
    del cookie["cookie_key_1"]

    assert headers["Set-Cookie"] == "cookie_key_2=cookie_value_2; Path=/; Max-Age=0"

    del cookie["cookie_key_2"]
    assert headers["Set-Cookie"] == "cookie_key_2=cookie_value_2; Path=/; Max-Age=0"