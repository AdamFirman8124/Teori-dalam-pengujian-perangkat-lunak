

# Generated at 2022-06-14 07:27:21.783958
# Unit test for function import_string
def test_import_string():
    module_name, package = "aiohttp.web_reqrep", "aiohttp"
    module = import_string(module_name, package)
    assert module.__name__ == "aiohttp.web_reqrep"

    module_name, package = "aiohttp.web_reqrep.Response.__init__", "aiohttp"
    obj = import_string(module_name, package)
    assert str(obj) == "<bound method Response.__init__ of <class 'aiohttp.web_reqrep.Response'>>"

# Generated at 2022-06-14 07:27:31.221954
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "allow": "GET, HEAD",
        "content-type": "text/xml",
        "status": "200",
        "content-location": "http://www.example.com/index.htm",
        "content-language": "da",
        "connection": "keep-alive",
        "proxy-authenticate": "NTLM",
    }
    new_headers = remove_entity_headers(headers)
    expected_headers = {
        "status": "200",
        "content-location": "http://www.example.com/index.htm",
        "connection": "keep-alive",
        "proxy-authenticate": "NTLM",
    }
    assert new_headers == expected_headers



# Generated at 2022-06-14 07:27:37.688862
# Unit test for function import_string
def test_import_string():
    from . import http
    from . import request
    from . import response

    modules = [http, request, response]

    for module in modules:
        assert import_string(module.__name__) == module



# Generated at 2022-06-14 07:27:43.829733
# Unit test for function import_string
def test_import_string():
    import time
    from application.middlewares import LoggingMiddleware
    from http import HTTPStatus

    assert import_string("time.time") == time.time
    assert type(import_string("application.middlewares.LoggingMiddleware")) == LoggingMiddleware
    assert import_string("http.HTTPStatus").__name__ == "web"

# Generated at 2022-06-14 07:27:49.921669
# Unit test for function import_string
def test_import_string():
    module = import_string("aiohttp.test_utils.helpers")
    assert module

    from aiohttp.test_utils.helpers import make_mocked_coro
    obj = import_string("aiohttp.test_utils.helpers.make_mocked_coro")
    assert obj == make_mocked_coro

# Generated at 2022-06-14 07:28:00.734647
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "content-location": "https://github.com/pypa/setuptools",
        "content-type": "json",
        "date": "today",
        "expires": "tomorrow",
        "hello": "world",
    }

    assert remove_entity_headers(headers) == {
        "date": "today",
        "hello": "world",
    }

    headers = {
        "content-location": "https://github.com/pypa/setuptools",
        "content-type": "json",
        "date": "today",
        "expires": "tomorrow",
        "hello": "world",
    }

# Generated at 2022-06-14 07:28:12.805053
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Allow": "GET",
        "Content-Encoding": "gzip",
        "Content-Language": "en",
        "Content-Length": "348",
        "Content-Location": "index.htm",
        "Content-MD5": "Q2hlY2sgSW50ZWdyaXR5IQ==",
        "Content-Range": "bytes 21010-47021/47022",
        "Content-Type": "text/html",
        "Expires": "Tue, 15 Nov 1994 12:45:26 GMT",
        "Last-Modified": "Sun, 06 Nov 1994 08:49:37 GMT",
    }
    expected = {"Content-Location": "index.htm", "Expires": "Tue, 15 Nov 1994 12:45:26 GMT"}

# Generated at 2022-06-14 07:28:19.160487
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        'content-length': '1234',
        'content-location': '',
        'content-md5': '1234',
        'expires': '',
        'extension-header': '',
        'content-type': 'application/json'
    }

    expected = {
        'content-location': '',
        'expires': '',
        'content-type': 'application/json'
    }
    result = remove_entity_headers(headers)
    assert expected == result

# Generated at 2022-06-14 07:28:24.000254
# Unit test for function import_string
def test_import_string():
    import tests
    from tests import test_utils
    assert test_utils == import_string("tests.test_utils")
    assert tests.test_utils.TestUtils == type(
        import_string(module_name="tests.test_utils.TestUtils")
    )

# Generated at 2022-06-14 07:28:33.626113
# Unit test for function import_string
def test_import_string():
    """
    used to run test on function import_string
    """
    from werkzeug.http import dump_cookie
    import quart
    import quart.templating
    import quart.cli

    q = import_string("quart.Quart")
    assert isinstance(q, quart.Quart)

    m = import_string("quart.templating")
    assert m is quart.templating

    cli = import_string("quart.cli.Command")
    assert cli is quart.cli.Command

    cookie_dump = import_string("werkzeug.http.dump_cookie")
    assert cookie_dump is dump_cookie

# Generated at 2022-06-14 07:28:38.123896
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(200) == True
    assert has_message_body(204) == False
    assert has_message_body(304) == False
    assert has_message_body(100) == False


# Generated at 2022-06-14 07:28:51.486803
# Unit test for function has_message_body
def test_has_message_body():
    assert(has_message_body(100) == False)
    assert(has_message_body(101) == False)
    assert(has_message_body(102) == False)
    assert(has_message_body(103) == False)
    assert(has_message_body(200) == True)
    assert(has_message_body(201) == True)
    assert(has_message_body(202) == True)
    assert(has_message_body(203) == True)
    assert(has_message_body(204) == False)
    assert(has_message_body(205) == True)
    assert(has_message_body(206) == True)
    assert(has_message_body(207) == True)
    assert(has_message_body(208) == True)

# Generated at 2022-06-14 07:28:54.903142
# Unit test for function import_string
def test_import_string():
    import dataclasses
    class User:
        pass
    assert dataclasses == import_string('dataclasses')
    assert User() == import_string('__main__.User')

# Generated at 2022-06-14 07:29:03.333405
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(200)
    assert has_message_body(201)
    assert has_message_body(206)
    assert has_message_body(301)
    assert has_message_body(302)
    assert has_message_body(400)
    assert has_message_body(404)
    assert has_message_body(409)
    assert has_message_body(418)
    assert not has_message_body(204)
    assert not has_message_body(304)
    assert not has_message_body(100)
    assert not has_message_body(102)
    assert not has_message_body(105)

# Generated at 2022-06-14 07:29:06.662945
# Unit test for function import_string
def test_import_string():
    from .wsgi import wsgi_app
    assert import_string("muffin.wsgi.wsgi_app") == wsgi_app



# Generated at 2022-06-14 07:29:10.297336
# Unit test for function import_string
def test_import_string():
    string = "oarepo_taxonomy.api.Taxonomy"
    assert import_string(string)
    string = "oarepo_taxonomy.api.Taxonomy:Taxonomy"
    assert import_string(string)

# Generated at 2022-06-14 07:29:15.866219
# Unit test for function import_string
def test_import_string():
    assert hasattr(import_string("falcon.request.Request.from_wsgi"), "__call__")

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))
    from falcon.request import Request
    test_import_string()

# Generated at 2022-06-14 07:29:22.477852
# Unit test for function import_string
def test_import_string():
    # importing a class:
    from sanic_motor import BaseModel

    model1 = import_string("sanic_motor.BaseModel")
    model2 = import_string("BaseModel", package="sanic_motor")

    assert isinstance(model1, BaseModel)
    assert isinstance(model2, BaseModel)

    # importing a module:
    import sanic_motor

    assert import_string("sanic_motor") == sanic_motor

# Generated at 2022-06-14 07:29:27.890747
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(200) is True
    assert has_message_body(199) is True
    assert has_message_body(301) is True
    assert has_message_body(204) is False
    assert has_message_body(304) is False
    assert has_message_body(100) is False
    assert has_message_body(199) is True
    assert has_message_body(101) is False


# Generated at 2022-06-14 07:29:34.814601
# Unit test for function has_message_body
def test_has_message_body():
    # Test 1XX
    assert not has_message_body(100)
    assert not has_message_body(101)
    assert not has_message_body(102)
    # Test 2XX
    assert has_message_body(200)
    assert has_message_body(201)
    assert has_message_body(202)
    # Test 3XX
    assert has_message_body(300)
    assert has_message_body(301)
    assert has_message_body(302)
    # Test 4XX
    assert has_message_body(400)
    assert has_message_body(401)
    assert has_message_body(403)
    # Test 5XX
    assert has_message_body(500)
    assert has_message_body(501)
    assert has_message_body(502)
   

# Generated at 2022-06-14 07:29:40.889042
# Unit test for function import_string
def test_import_string():
    from pyhttp2.server import HttpServer

    class Test:
        pass

    assert import_string("pyhttp2.server.HttpServer") == HttpServer
    assert import_string("__main__.Test") == Test



# Generated at 2022-06-14 07:29:46.135104
# Unit test for function import_string
def test_import_string():
    def test(module_name, result):
        assert import_string(module_name) == result

    test("http.server.BaseHTTPRequestHandler", BaseHTTPRequestHandler)
    import http.client
    test("http.client.HTTPConnection", http.client.HTTPConnection)



# Generated at 2022-06-14 07:29:50.150447
# Unit test for function import_string
def test_import_string():
    from httpcat import __version__ as version
    assert import_string("httpcat.__version__") == version
    assert (
        import_string("httpcat.__version__")
        == import_string("httpcat.__version__.__str__")
    )

# Generated at 2022-06-14 07:29:52.512113
# Unit test for function import_string
def test_import_string():
    import sys
    assert sys.version_info == import_string("sys.version_info")


# Generated at 2022-06-14 07:29:56.757098
# Unit test for function import_string
def test_import_string():
    """
    Test if the function import_string works as expected
    """
    import http
    import time
    assert import_string("http.HTTPStatus") == http.HTTPStatus
    assert isinstance(import_string("time.time"), float)



# Generated at 2022-06-14 07:30:02.328743
# Unit test for function import_string
def test_import_string():
    """Test import_string(module_name: str) -> object"""
    from simpleserverhttp.http.clientconnection import ClientConnection
    obj = import_string("simpleserverhttp.http.clientconnection.ClientConnection")
    assert obj.__class__.__name__ == ClientConnection.__name__

# Generated at 2022-06-14 07:30:06.930922
# Unit test for function import_string
def test_import_string():
    import sys
    import os
    import_string('os.path')
    import_string('typing.Any')
    import_string('test_base.test_import_string')


if __name__ == "__main__":
    test_import_string()

# Generated at 2022-06-14 07:30:16.037692
# Unit test for function import_string
def test_import_string():
    import bar
    import foo
    assert import_string("foo") == foo
    assert import_string("foo.bar") == bar
    assert import_string("foo.bar.baz") == bar.baz
    assert import_string("foo.bar.Baz") == bar.Baz()
    assert import_string("foo.bar.Baz", "foo") == bar.Baz()
    assert import_string("qux.Bar", "foo") == foo.qux.Bar()
    assert import_string("Leaf", "foo.bar") == foo.bar.Leaf()



# Generated at 2022-06-14 07:30:20.908900
# Unit test for function import_string
def test_import_string():
    obj = import_string('aiohttp.web_app.Application')
    assert obj().__class__.__name__ == 'Application'

    obj = import_string('aiohttp.web_app.Application', package='aiohttp')
    assert obj().__class__.__name__ == 'Application'

# Generated at 2022-06-14 07:30:29.228599
# Unit test for function import_string
def test_import_string():
    """
    Run unit test for import_string
    """
    from unittest import TestCase, main
    from base64 import b64encode
    from io import BytesIO

    class TestImportString(TestCase):
        def test_import_string(self):
            from dgas.http import Request, Response
            from dgas.http import HttpProtocol
            
            self.assertRaises(AttributeError, import_string, "dgas.http.invalid")
            self.assertIsInstance(import_string("dgas.http.HttpProtocol"), HttpProtocol)
            self.assertIsInstance(import_string("dgas.http.Request"), Request)
            self.assertIsInstance(import_string("dgas.http.Response"), Response)