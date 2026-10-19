

# Generated at 2022-06-14 07:27:26.275351
# Unit test for function has_message_body
def test_has_message_body():
    assert not has_message_body(200)
    assert not has_message_body(204)
    assert not has_message_body(304)
    assert has_message_body(500)
    assert not has_message_body(100)
    assert not has_message_body(101)
    assert not has_message_body(102)
    assert not has_message_body(103)
    assert not has_message_body(199)
    assert not has_message_body(203)
    assert has_message_body(400)
    assert has_message_body(401)
    assert has_message_body(402)
    assert has_message_body(403)
    assert has_message_body(404)
    assert has_message_body(405)
    assert has_message_body(406)
    assert has

# Generated at 2022-06-14 07:27:31.260683
# Unit test for function import_string
def test_import_string():
    class A:pass
    class B:pass
    import sys, types
    sys.modules['test'] = types.ModuleType('test')
    sys.modules['test'].A = A
    sys.modules['test'].B = B
    assert import_string('test.A') == A
    assert import_string('test.B') ==  B()

# Generated at 2022-06-14 07:27:47.478702
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    # Check if the keys are being removed
    headers = {
        "content-length": "0",
        "content-md5": "foo",
    }
    assert remove_entity_headers(headers) == {}

    # Check that other headers are ignored
    headers = {
        "allow": "GET",
        "content-length": "0",
        "content-md5": "foo",
    }
    assert remove_entity_headers(headers) == {"allow": "GET"}

    # Check that the allowed headers are kept
    headers = {
        "content-location": "/foo/bar",
        "content-length": "0",
        "content-md5": "foo",
    }
    assert remove_entity_headers(headers) == {"content-location": "/foo/bar"}

    # Check that the allowed headers with lowercase

# Generated at 2022-06-14 07:27:58.312187
# Unit test for function import_string
def test_import_string():
    assert hasattr(import_string("aiohttp.web.StreamResponse"), "keep_alive")
    assert import_string("aiohttp.web.StreamResponse").keep_alive is False
    # TODO: Do not depend on aiohttp framework
    assert (
        import_string("aiohttp.web.StreamResponse").keep_alive is False
    )  # noqa: E501
    assert hasattr(
        import_string("aiohttp.web.StreamResponse"), "keep_alive"
    )  # noqa: E501
    assert hasattr(import_string("aiohttp.web.StreamResponse"), "keep_alive")
    assert hasattr(import_string("aiohttp.web.StreamResponse"), "keep_alive")

# Generated at 2022-06-14 07:28:02.279212
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(501)
    assert not has_message_body(204)
    assert not has_message_body(100)
    assert not has_message_body(200)



# Generated at 2022-06-14 07:28:03.940071
# Unit test for function import_string
def test_import_string():
    import_string("mock_class.MockClass")



# Generated at 2022-06-14 07:28:16.085781
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    import pytest
    from starlette.testclient import TestClient

    from starlette_wsgi_headers.middleware import EntityHeadersRemovalMiddleware

    headers = {"Content-Type": "text/plain", "Custom-Header": "value"}

    middleware = EntityHeadersRemovalMiddleware(app=lambda x: None)
    removed_headers = middleware.remove_entity_headers(headers)

    assert "Content-Type" not in removed_headers
    assert "Custom-Header" in removed_headers

    app = EntityHeadersRemovalMiddleware(lambda x: None)
    client = TestClient(app=app)

    response = client.get("/", headers=headers)
    assert "Content-Type" not in dict(response.headers)
    assert "Content-Type" not in dict(response.history[0].headers)



# Generated at 2022-06-14 07:28:19.724699
# Unit test for function import_string
def test_import_string():
    from os.path import dirname, join
    import this_package
    import_string("this_package", package=dirname(__file__))
    import_string("this_package.this_package")
    import_string("this_package.__main__.this_package")
    import_string("this_package.meta.Meta.__init__")
    import_string("this_package.meta.Meta")(this_package)



# Generated at 2022-06-14 07:28:32.780199
# Unit test for function import_string
def test_import_string():
    from .request import Request
    from .server import Server
    from .response import Response
    from .middlewares import DebugMiddleware
    from .adapters import WSGIAdapter
    from .router import Router, Route
    from .server import Server
    from .exceptions import HTTPError, HTTPException, HTTPStatusError
    from .helpers import FileStreamer
    from .types import JSONData
    from .client import Client
    from .lib import parse_size

    assert import_string("feather.request.Request") == Request
    assert import_string("feather.server.Server") == Server
    assert import_string("feather.response.Response") == Response
    assert import_string("feather.middlewares.DebugMiddleware") == DebugMiddleware
    assert import_string("feather.adapters.WSGIAdapter") == WSGIAdapter


# Generated at 2022-06-14 07:28:39.082794
# Unit test for function import_string
def test_import_string():
    class Abc:
        pass
    class Foo:
        pass
    assert Abc() == import_string("basics.http.Abc")
    assert Abc == import_string("basics.http.Abc", "basics")
    assert Foo() == import_string("tests.http.test_basics.Foo")
    assert Foo == import_string("tests.http.test_basics.Foo", "tests")

# Generated at 2022-06-14 07:28:46.984115
# Unit test for function import_string
def test_import_string():
    import sys
    import os.path

    main_dir = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(main_dir)

    from autobahn.protocols.http2.base_processor import test_import_string

    assert test_import_string() == "Hello world!"

# Generated at 2022-06-14 07:28:54.905684
# Unit test for function import_string
def test_import_string():
    """Unit test for function import_string"""
    assert STATUS_CODES == import_string("http.STATUS_CODES")
    assert has_message_body == import_string("http.has_message_body")
    assert is_entity_header == import_string("http.is_entity_header")
    assert is_hop_by_hop_header == import_string("http.is_hop_by_hop_header")

# Generated at 2022-06-14 07:28:56.768827
# Unit test for function import_string
def test_import_string():
    class MyTestClass:
        pass
    module = import_string(".http.MyTestClass", package="protocole")
    assert isinstance(module, MyTestClass)

# Generated at 2022-06-14 07:28:59.983877
# Unit test for function import_string
def test_import_string():
    expected = "hello"
    module_name = __name__ + ".hello"
    def hello():
        return expected
    assert import_string(module_name).hello() == expected
    assert import_string(module_name + ".hello")() == expected
    assert import_string(module_name + ".hello").__name__ == "hello"

# Generated at 2022-06-14 07:29:04.915076
# Unit test for function import_string
def test_import_string():
    assert import_string("http.client.HTTPConnection") is import_module("http.client").HTTPConnection
    assert import_string("http.client.HTTPConnection").__class__.__name__ == "HTTPConnection"
    assert import_string("http.client.HTTPConnection").__module__ == "http.client"
    assert import_string("collections.deque").__class__.__name__ == "deque"
    assert import_string("collections.deque").__module__ == "collections"

# Generated at 2022-06-14 07:29:07.138135
# Unit test for function import_string
def test_import_string():
    assert import_string("aiohttp.ClientSession") is import_module("aiohttp.ClientSession")

# Generated at 2022-06-14 07:29:12.329219
# Unit test for function import_string
def test_import_string():
    class Test:
        def __init__(self):
            self.n = 0
        def incr(self):
            self.n += 1

    inst = import_string("http.http_utils.Test")
    assert(inst.n == 0)
    inst.incr()
    assert(inst.n == 1)

# Generated at 2022-06-14 07:29:18.611507
# Unit test for function import_string
def test_import_string():
    class_name = "klein.Klein"
    klein_obj = import_string(class_name)
    assert hasattr(klein_obj, "run")
    class_name = "aiohttp.web:Application"
    aiohttp_app = import_string(class_name)
    assert hasattr(aiohttp_app, "router")

# Generated at 2022-06-14 07:29:23.551300
# Unit test for function import_string
def test_import_string():
    assert import_string("os") is os
    assert import_string("os.path") is os.path
    assert import_string("tests.test_utils.test_import_string") is test_import_string
    assert import_string("tests.test_utils") is test_utils

# Generated at 2022-06-14 07:29:29.260915
# Unit test for function import_string
def test_import_string():
    class MyClass:
        pass

    import sys
    import myapp.modules.mod1.class_import_string as module_name
    module = import_string(module_name.__name__)
    obj = getattr(module, "MyClass")
    assert ismodule(obj)

    obj2 = import_string("myapp.modules.mod1.class_import_string.MyClass")
    assert isinstance(obj2, MyClass)