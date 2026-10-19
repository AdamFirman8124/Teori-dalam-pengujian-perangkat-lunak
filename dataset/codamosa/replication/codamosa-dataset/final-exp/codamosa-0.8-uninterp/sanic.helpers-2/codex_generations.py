

# Generated at 2022-06-14 07:27:17.561609
# Unit test for function import_string
def test_import_string():
    assert import_string("falcon.API")
    assert import_string("falcon.API").__class__.__name__ == "API"
    assert import_string("falcon.testing.StartResponseMock").__class__.__name__ == "StartResponseMock"

# Generated at 2022-06-14 07:27:27.188899
# Unit test for function import_string
def test_import_string():
    import sys
    import os

    # Test a module
    path_to_module = ".".join(__name__.split(".")[:3]) + ".http"
    imported_module = import_string(path_to_module)
    assert imported_module == import_module(path_to_module)

    # Test a class
    path_to_class = ".".join(__name__.split(".")[:3]) + ".testing.test_http.test_import_string"
    instance_imported_class = import_string(path_to_class)
    assert instance_imported_class is test_import_string

test_import_string()

# Generated at 2022-06-14 07:27:32.429780
# Unit test for function import_string
def test_import_string():
    import aiohttp
    import handlers

    assert ismodule(import_string("os.path"))
    assert ismodule(import_string("aiohttp", package="aiohttp"))
    assert isinstance(import_string("aiohttp.web.Request"), aiohttp.web.Request)
    assert isinstance(import_string("handlers.UserHandler"), handlers.UserHandler)

# Example of how to use

# Generated at 2022-06-14 07:27:34.923165
# Unit test for function import_string
def test_import_string():
    from httpcore.server import Handler

    handler = import_string('httpcore.server.Handler')

    assert handler is Handler

# Generated at 2022-06-14 07:27:43.065049
# Unit test for function import_string
def test_import_string():
    from .middleware import BaseMiddleware
    from .handler import BaseHandler
    import_string('falcon_core.middleware.BaseMiddleware') == BaseMiddleware
    class Test1():
        x = 1
    test1 = import_string('falcon_core.utils.Test1')
    assert test1.x == 1
    assert import_string('falcon_core.handler.BaseHandler') == BaseHandler

# Generated at 2022-06-14 07:27:48.011021
# Unit test for function import_string
def test_import_string():
    module = import_string("datetime")
    assert module.datetime.utcnow()
    cls = import_string("datetime.datetime")
    assert cls
    assert cls.utcnow()


# Generated at 2022-06-14 07:27:52.589410
# Unit test for function import_string
def test_import_string():
    from .testapp.app import SimpleApp
    from .testapp.mail import Email

    assert import_string("simple_server.testapp.app.SimpleApp") == SimpleApp
    assert isinstance(import_string("simple_server.testapp.mail.Email"), Email)



# Generated at 2022-06-14 07:27:59.840008
# Unit test for function import_string
def test_import_string():
    from importlib import import_module
    from unittest.mock import patch

    def assert_import_string(string, module_path, klass=None):
        if klass is not None:
            obj = import_string(string)
            assert obj is not None
            assert isinstance(obj, module_path)
        else:
            obj = import_string(string)
            assert obj is not None
            assert obj is module_path

    assert_import_string("pyramid.threadlocal", import_module("pyramid").threadlocal)
    # Assertion simple module
    assert_import_string("http.client", import_module("http").client)
    # Assertion with package
    assert_import_string("http.client", import_module("http").client, package="http")
    # Assertion instanci

# Generated at 2022-06-14 07:28:00.788197
# Unit test for function import_string
def test_import_string():
    class Test:
        pass
    assert Test == import_string(__name__ + ".Test")
    assert Test is import_string(__name__ + ".Test")



# Generated at 2022-06-14 07:28:12.803689
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(100) is False
    assert has_message_body(101) is False
    assert has_message_body(102) is False
    assert has_message_body(103) is False
    assert has_message_body(200) is True
    assert has_message_body(201) is True
    assert has_message_body(202) is True
    assert has_message_body(203) is True
    assert has_message_body(204) is False
    assert has_message_body(205) is False
    assert has_message_body(206) is True
    assert has_message_body(207) is True
    assert has_message_body(208) is True
    assert has_message_body(226) is True
    assert has_message_body(300) is True
    assert has_

# Generated at 2022-06-14 07:28:22.026201
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    assert remove_entity_headers({'Set-Cookie': 'name=foo', "test": "jaja"}) == {'test': b'jaja'}
    assert remove_entity_headers({'Set-Cookie': 'name=foo', "test": "jaja", 'expires': 'hola'}) == {'test': b'jaja', 'expires': b'hola'}
    assert remove_entity_headers({'Set-Cookie': 'name=foo', "test": "jaja", 'content-location': 'hola'}) == {'test': b'jaja', 'content-location': b'hola'}

# Generated at 2022-06-14 07:28:27.331620
# Unit test for function import_string
def test_import_string():
    class HelloWorld:
        pass

    hello = HelloWorld()

    # using a class
    assert import_string('tests.utils.http.test_import_string.HelloWorld') == hello

    # using a module
    assert import_string('tests.utils.http') == http

# Generated at 2022-06-14 07:28:33.569349
# Unit test for function import_string
def test_import_string():
    import tempfile

    test_module_name = "tempfile"
    module = import_string(test_module_name)
    assert test_module_name == module.__name__

    test_module_name = "tempfile.TemporaryFile"
    file = import_string(test_module_name)
    assert isinstance(file, tempfile.TemporaryFile)



# Generated at 2022-06-14 07:28:44.554227
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    assert remove_entity_headers({"allow": "GET", "content-type": "application/json"}) == {"allow": "GET"}
    assert remove_entity_headers({"allow": "GET", "content-type": "application/json"}, ["allow"]) == {"allow": "GET"}
    assert remove_entity_headers({"allow": "GET", "content-type": "application/json"}, ["content-type"]) == {"content-type": "application/json"}
    assert remove_entity_headers({"allow": "GET", "content-type": "application/json"}, ["allow", "content-type"]) == {"allow": "GET", "content-type": "application/json"}

# Generated at 2022-06-14 07:28:55.406473
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers_test = {"content-location": "here", "expires": "soon"}
    headers_test_result = remove_entity_headers(headers_test)
    assert "content-location" in headers_test_result
    assert "expires" in headers_test_result
    headers_test = {"content-location": "here", "expires": "soon", "other": "value"}
    headers_test_result = remove_entity_headers(headers_test, allowed=("other",))
    assert "content-location" in headers_test_result
    assert "expires" in headers_test_result
    assert "other" in headers_test_result

# Generated at 2022-06-14 07:29:00.306004
# Unit test for function import_string
def test_import_string():
    """
    Simple test of function import_string
    """
    assert ismodule(import_string("http.client"))
    assert import_string("http.client.HTTPConnection")
    assert import_string("http.client.HTTPConnection").__name__ == "HTTPConnection"

# Generated at 2022-06-14 07:29:04.540429
# Unit test for function import_string
def test_import_string():
    import uvicorn.config
    assert import_module("uvicorn.config") == import_string("uvicorn.config")
    assert import_module("uvicorn.config.defaults") == import_string("uvicorn.config.defaults")
    import uvicorn.config.defaults
    assert uvicorn.config.defaults.Config == import_string("uvicorn.config.defaults.Config")

# Generated at 2022-06-14 07:29:09.756466
# Unit test for function import_string
def test_import_string():
    """ https://github.com/Aurora0001/httpcore/issues/15 """
    import_string("httpcore.errors.InternalServerError")
    import_string("httpcore.errors.InternalServerError").code == 500
    import_string("httpcore.errors.InternalServerError", "httpcore").code == 500

# Generated at 2022-06-14 07:29:21.716108
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = remove_entity_headers({
        'content-type': 'application/json',
        'content-length': '1000',
        'content-location': 'http://0.0.0.0:8000/user/1/',
        'content-md5': '926f523ccc7d6e2f6b8c6ca956878044',
        'content-range': 'bytes 200-1000/67589',
        'expires': 'Tue, 01 Nov 2020 15:00:00 GMT',
        'allow': 'GET, OPTIONS, HEAD, POST',
        'date': 'Tue, 22 Sep 2020 14:00:00 GMT',
        'last-modified': 'Tue, 22 Sep 2020 13:00:00 GMT',
    })

# Generated at 2022-06-14 07:29:26.089696
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"content-length": "100", "Content-Encoding": "gzip"}
    assert not remove_entity_headers(headers)
    headers = {
        "CONTENT-LENGTH": "100",
        "Content-Encoding": "gzip",
        "CONTENT-LOCATION": "/index.html",
    }
    assert len(remove_entity_headers(headers)) == 1