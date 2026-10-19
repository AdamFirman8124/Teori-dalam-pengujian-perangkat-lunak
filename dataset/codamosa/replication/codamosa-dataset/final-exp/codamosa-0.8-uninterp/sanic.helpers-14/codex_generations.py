

# Generated at 2022-06-14 07:27:17.561153
# Unit test for function import_string
def test_import_string():
    import os
    import sys
    import pathlib
    sys.path.append(str(pathlib.Path(__file__).parent))
    from import_string_test import test_class
    from import_string_test import test_module
    os.environ["IMPORT_STRING_TEST_CLASS"] = "import_string_test.TestClass"
    os.environ["IMPORT_STRING_TEST_MODULE"] = "import_string_test"
    assert import_string(os.environ["IMPORT_STRING_TEST_CLASS"]) == test_class
    assert import_string(os.environ["IMPORT_STRING_TEST_MODULE"]) == test_module
    del os.environ["IMPORT_STRING_TEST_CLASS"]

# Generated at 2022-06-14 07:27:21.615067
# Unit test for function import_string
def test_import_string():
    """Test :func:`~.import_string`."""
    import uvicorn
    import uvicorn.config
    import uvicorn.protocols.http
    import uvicorn.config

    assert import_string("uvicorn.config") is uvicorn.config
    assert import_string("uvicorn.config.Config") is uvicorn.config.Config
    assert import_string("uvicorn.protocols.http.HttpProtocol") is uvicorn.protocols.http.HttpProtocol



# Generated at 2022-06-14 07:27:22.999294
# Unit test for function import_string
def test_import_string():
    assert import_string("unittest.case.TestCase")



# Generated at 2022-06-14 07:27:29.743201
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
        "Content-Location": "https://docs.python.org/3/",
        "content-type": "text/html",
    }

    headers_without_entities = remove_entity_headers(headers)
    assert len(headers_without_entities) == 1
    assert headers_without_entities == {
        "content-type": "text/html",
    }

# Generated at 2022-06-14 07:27:47.477964
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Connection": None,
        "Content-Length": 1,
        "Content-Type": "text/html",
        "Date": "Thu, 22 Nov 2018 11:02:49 GMT",
        "Keep-Alive": None,
        "Server": "H2O/2.2.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip",
        "User-Agent": "Go-http-client/1.1",
    }

# Generated at 2022-06-14 07:27:53.890648
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    """
    Test remove_entity_headers
    """
    headers = {
        "content-location": "/test",
        "cache-control": "no-cache",
        "X-Custom-Header": "test",
        "accept": "*/*",
        "user-agent": "python-requests/2.22.0",
    }

    headers = remove_entity_headers(headers, allowed=["content-location"])
    assert "content-location" in headers.keys()
    assert len(headers) == 4

    headers = remove_entity_headers(headers)
    assert "content-location" not in headers.keys()
    assert len(headers) == 3

# Generated at 2022-06-14 07:28:02.811489
# Unit test for function import_string
def test_import_string():
    from .app import Application as TestApplication
    from .response import Response as TestResponse
    from .request import Request as TestRequest
    from .roa import ROA as TestRoa
    pytest_assert(import_string(TestApplication.__module__), type(TestApplication))
    pytest_assert(import_string(TestResponse.__module__), type(TestResponse))
    pytest_assert(import_string(TestRequest.__module__), type(TestRequest))
    pytest_assert(import_string(TestRoa.__module__), type(TestRoa))

# Generated at 2022-06-14 07:28:14.920756
# Unit test for function remove_entity_headers

# Generated at 2022-06-14 07:28:25.291775
# Unit test for function import_string
def test_import_string():
    from .factory import Factory
    from .middleware import Middleware
    from .response import Response
    from .request import Request

    factory = import_string("arbiter.factory.Factory")
    middleware = import_string("arbiter.middleware.Middleware")
    response = import_string("arbiter.response.Response")
    request = import_string("arbiter.request.Request")

    using_factory = isinstance(factory, Factory)
    using_middleware = isinstance(middleware, Middleware)
    using_response = isinstance(response, Response)
    using_request = isinstance(request, Request)

    assert using_factory and using_middleware and using_response and using_request

# Generated at 2022-06-14 07:28:35.362324
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(100) == False
    assert has_message_body(101) == False
    assert has_message_body(102) == False
    assert has_message_body(103) == False
    assert has_message_body(199) == False
    assert has_message_body(200) == True
    assert has_message_body(201) == True
    assert has_message_body(202) == True
    assert has_message_body(203) == True
    assert has_message_body(204) == False
    assert has_message_body(205) == True
    assert has_message_body(206) == True
    assert has_message_body(207) == True
    assert has_message_body(208) == True
    assert has_message_body(226) == True
    assert has_

# Generated at 2022-06-14 07:28:40.138704
# Unit test for function import_string
def test_import_string():
    from ddd_rest_api.application import Application
    obj = import_string("ddd_rest_api.application.Application")
    assert(type(obj) is Application)

# Generated at 2022-06-14 07:28:43.427402
# Unit test for function import_string
def test_import_string():
    app = import_string('http.server.WSGIServer')
    assert app.__name__ == 'WSGIServer'

# Generated at 2022-06-14 07:28:51.406750
# Unit test for function import_string
def test_import_string():
    from django.test import mock

    class MockTestClass:
        def __init__(self):
            pass

    m = mock.Mock()
    m.module_name = "guillotina.api.content.exceptions"
    m.MockTestClass = MockTestClass
    with mock.patch("importlib.import_module", return_value=m):
        obj = import_string("guillotina.api.content.exceptions.MockTestClass")
        assert isinstance(obj, MockTestClass)

# Generated at 2022-06-14 07:28:58.873841
# Unit test for function import_string
def test_import_string():
    from .uri import Request, Response
    assert import_string("httpolice.citations.Citation")
    assert import_string("httpolice.citations.Citation")
    assert import_string("httpolice.citations.Citation") == import_string("httpolice.citations.Citation")
    assert import_string("httpolice.uri.Request") == Request
    assert import_string("httpolice.uri.Response") == Response

# Generated at 2022-06-14 07:29:08.073816
# Unit test for function import_string
def test_import_string():
    import os
    import tempfile
    path_temp_file = os.path.join(tempfile.gettempdir(), "uranus_test.py")
    with open(path_temp_file, "w") as temp_file:
        temp_file.write(
            """class A:
            def __init__(self):
                self.x = "x"

            def __call__(self):
                return self.x + "y"
        """
        )

    assert import_string(path_temp_file + ".A")() == "xy"
    assert import_string(path_temp_file + ".A")().x == "x"
    assert import_string(path_temp_file) == temp_file

# Generated at 2022-06-14 07:29:20.139273
# Unit test for function import_string
def test_import_string():
    print("test_import_string")
    from .test_apps import test_app1, test_app2
    from .test_middlewares import test_middleware1, test_middleware2
    from .test_middlewares import test_middleware3
    assert import_string("sanic.test_apps.test_app1") == test_app1
    assert import_string("sanic.test_apps.test_app2") == test_app2
    assert import_string("sanic.test_middlewares.test_middleware1") == test_middleware1
    assert import_string("sanic.test_middlewares.test_middleware2") == test_middleware2
    assert import_string("sanic.test_middlewares.test_middleware3") == test_middleware3
    assert isinstance

# Generated at 2022-06-14 07:29:34.117441
# Unit test for function import_string
def test_import_string():
    from routes import Mapper
    from websauna.system.core.route import Route

    class Test:
        def __call__(self):
            return "Test"

    def test(value):
        if value == "Test":
            return True
        return False

    assert test_import_string.__name__ == "test_import_string"
    assert import_string(".websauna.system.core.route.Route") == Route
    assert import_string(".websauna.system.core.route.Route,websauna.system.core") == Route
    assert import_string("routes.Mapper") == Mapper
    assert import_string("test.test") == test
    assert test(import_string("test.Test"))
    assert import_string("test.Test")() == "Test"

# Generated at 2022-06-14 07:29:35.947132
# Unit test for function import_string
def test_import_string():
    import sys
    import_string("sys.path")
    import_string("sys", package=__name__)

# Generated at 2022-06-14 07:29:41.176056
# Unit test for function import_string
def test_import_string():
    """
    import_string should import a module and return it
    """
    from tests.constants import MODULE_NAME
    result = import_string(MODULE_NAME)
    assert result.__name__ == MODULE_NAME



# Generated at 2022-06-14 07:29:42.761564
# Unit test for function import_string
def test_import_string():
    import_string("unittest")

# Generated at 2022-06-14 07:29:47.331128
# Unit test for function import_string
def test_import_string():
    from pyt.http.server import HTTPServer
    path = "pyt.http.server.HTTPServer"
    assert import_string(path) == HTTPServer

# Generated at 2022-06-14 07:29:49.559994
# Unit test for function import_string
def test_import_string():
    import asyncio
    assert import_string("asyncio") == asyncio


# Generated at 2022-06-14 07:29:53.103949
# Unit test for function import_string
def test_import_string():
    assert import_string("jsonschema.validators") is import_module("jsonschema.validators")
    assert import_string("jsonschema.validators.Draft4Validator")() is not None

# Generated at 2022-06-14 07:29:56.291161
# Unit test for function import_string
def test_import_string():
    test_module = import_string("test_module")
    assert "test" == test_module.test_string
    assert "test_instance" == test_module.test_instance()

# Generated at 2022-06-14 07:29:59.905747
# Unit test for function import_string
def test_import_string():
    class TS:
        pass
    m = "napixd.test.test_http.TS"
    assert TS is import_string(m)



# Generated at 2022-06-14 07:30:10.974486
# Unit test for function import_string
def test_import_string():
    def bar(foo):
        return foo

    assert callable(import_string("aiohttp.test_utils.test_helpers.bar"))
    assert import_string("aiohttp.test_utils.test_helpers.bar",
                         package="aiohttp")(123) == 123
    assert import_string("aiohttp.test_utils.test_helpers.bar")(123) == 123
    assert import_string("aiohttp.test_utils.test_helpers",
                         package="aiohttp").bar(123) == 123
    assert import_string("aiohttp.test_utils.test_helpers",
                         "aiohttp").bar(123) == 123
    assert import_string("test_helpers",
                         "aiohttp.test_utils").bar(123) == 123
    assert import_string

# Generated at 2022-06-14 07:30:14.587717
# Unit test for function import_string
def test_import_string():
    from radar.server.validator import Validator

    validator = import_string("radar.server.validator.Validator")
    assert isinstance(validator, Validator)

# Generated at 2022-06-14 07:30:17.100986
# Unit test for function import_string
def test_import_string():
    import_string('http.cookies.SimpleCookie')
    import_string('http.cookies.SimpleCookie')()

# Generated at 2022-06-14 07:30:23.625713
# Unit test for function import_string
def test_import_string():
    import copy

    import wsgi_micro

    assert wsgi_micro == import_string("wsgi_micro")
    assert wsgi_micro.App == import_string("wsgi_micro.App")
    assert copy == import_string("copy")
    assert deepcopy == import_string("copy.deepcopy")
    assert deepcopy == import_string("copy.deepcopy")
    assert deepcopy is import_string("copy.deepcopy")



# Generated at 2022-06-14 07:30:27.083786
# Unit test for function import_string
def test_import_string():
    import example
    assert example == import_string("example")
    assert example.foo == import_string("example.foo")


# Generated at 2022-06-14 07:30:32.496442
# Unit test for function import_string
def test_import_string():
    import sanic.server as server
    assert import_string("sanic.server") == server
    assert import_string("sanic.server.HttpProtocol") == server.HttpProtocol



# Generated at 2022-06-14 07:30:35.508950
# Unit test for function import_string
def test_import_string():
    import_string("http.client.HTTPResponse")
    import_string("http.HTTPStatus")

# Generated at 2022-06-14 07:30:37.727262
# Unit test for function import_string
def test_import_string():
    assert import_string("http.client.HTTPSConnection") == import_module("http.client").HTTPSConnection

# Generated at 2022-06-14 07:30:42.626018
# Unit test for function import_string
def test_import_string():
    from deuces.router import Router
    from deuces.wsgi import WSGI
    from deuces.worker import Worker
    assert import_string("deuces.router.Router") is Router
    assert import_string("deuces.wsgi.WSGI") is WSGI
    assert import_string("deuces.worker.Worker") is Worker

# Generated at 2022-06-14 07:30:55.227421
# Unit test for function import_string
def test_import_string():
    """Unit test for function import_string"""
    from luxa.common.wsgi import HTTPRequest
    # import module
    http_module = import_string(module_name="luxa.common.wsgi")
    # import class
    http_class = import_string(module_name="luxa.wsgi.HTTPRequest")
    # test import module
    assert http_module.__name__ == "luxa.common.wsgi"
    # test instanciate HTTPRequest class
    assert isinstance(http_class, HTTPRequest)
    # test raise exception if module does not exist
    try:
        import_string(module_name="luxa.common.that_i_do_not_exist")
    except ModuleNotFoundError:
        pass
    # test raise exception if class does not exist

# Generated at 2022-06-14 07:31:03.361324
# Unit test for function import_string
def test_import_string():
    assert import_string("os.path") == import_module("os.path")
    assert import_string("os") == import_module("os")
    assert import_string("os.path.abspath") == import_module("os.path").abspath

    from tests.test_http.test_views import MockView
    assert isinstance(import_string("tests.test_http.test_views.MockView"), MockView)

# Generated at 2022-06-14 07:31:12.495851
# Unit test for function import_string
def test_import_string():
    import pytest
    from importlib import import_module
    from typing import Tuple

    class TextArea(object):
        def __init__(self):
            pass
        def render(self):
            return "render TextArea"

    class InputText(object):
        def __init__(self):
            pass
        def render(self):
            return "render InputText"

    class InvalidClass(object):
        def __init__(self):
            pass
        def render(self):
            return "render InputText"

    class ValidClass(object):
        def __init__(self):
            pass
        def render(self):
            return "render InputText"

    class TestClass(object):
        def __init__(self):
            pass
        def render(self):
            return "render InputText"


# Generated at 2022-06-14 07:31:14.296165
# Unit test for function import_string
def test_import_string():
    assert import_string("http.client.HTTPConnection")



# Generated at 2022-06-14 07:31:18.187678
# Unit test for function import_string
def test_import_string():
    try:
        import_string("test.test")
        assert False
    except:
        assert True
    try:
        import_string("test.test.test")
        assert True
    except:
        assert False

# Generated at 2022-06-14 07:31:20.739039
# Unit test for function import_string
def test_import_string():
    from http.cookiejar import CookieJar
    assert import_string("http.cookiejar.CookieJar") is CookieJar
    assert import_string("http.cookiejar.CookieJar")() is not None