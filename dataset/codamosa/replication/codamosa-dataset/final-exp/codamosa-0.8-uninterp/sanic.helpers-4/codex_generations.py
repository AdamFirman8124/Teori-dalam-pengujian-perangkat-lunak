

# Generated at 2022-06-14 07:27:23.410356
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    valid_headers = [
        "Allow",
        "Content-Encoding",
        "Content-Language",
        "Content-Length",
        "Content-Location",
        "Content-MD5",
        "Content-Range",
        "Content-Type",
        "Expires",
        "Last-Modified",
        "Extension-Header",
    ]
    lower_valid_headers = [header.lower() for header in valid_headers]
    header = {"test": "test"}
    assert remove_entity_headers(header) == header

    header = {"content-type": "test"}
    assert remove_entity_headers(header) == header


# Generated at 2022-06-14 07:27:33.205274
# Unit test for function import_string
def test_import_string():
    from .response import Response
    from .request import Request

    assert (
        import_string("aiohttp.web.Response") == Response
    ), "import_string fail with module path"
    assert (
        import_string("aiohttp.web.Response")() == Response()
    ), "import_string fail with class path"
    assert (
        import_string("aiohttp.web.Request") == Request
    ), "import_string fail with module path"
    assert (
        import_string("aiohttp.web.Request")() == Request()
    ), "import_string fail with class path"

if __name__ == "__main__":
    for funcname in dir():
        if not funcname.startswith("test_"):
            continue
        print(f"running {funcname}")
        locals()

# Generated at 2022-06-14 07:27:47.478661
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    assert {'a': 1} == remove_entity_headers({'a': 1})
    assert {'a': 1} == remove_entity_headers({'a': 1, 'content-length': 3})
    assert {'a': 1} == remove_entity_headers({'a': 1, 'content-length': 3, 'content-type': 'text/html'})
    assert {'a': 1, 'content-type': 'text/html'} == remove_entity_headers({'a': 1, 'content-length': 3, 'content-type': 'text/html', 'content-location': 'test'})

# Generated at 2022-06-14 07:27:49.674746
# Unit test for function import_string
def test_import_string():
    assert import_string("visio.app") == import_module("visio.app")
    assert import_string("visio.middleware.proxy.ProxyMiddleware") == import_module("visio.middleware.proxy").ProxyMiddleware()


# Generated at 2022-06-14 07:27:53.784667
# Unit test for function import_string
def test_import_string():
    """Test for function import_string"""
    from . import __version__
    from . import http
    assert import_string("falcon.http") == http
    assert import_string("falcon.__version__") == __version__

# Generated at 2022-06-14 07:28:00.733979
# Unit test for function import_string
def test_import_string():
    module = import_string("tests.test_util.test_import_string")
    assert module.__name__ == "tests.test_util.test_import_string"
    assert module.name == "test_import_string"

    class_obj = import_string("tests.test_util.test_import_string.Test_import_string")
    assert class_obj.__name__ == "tests.test_util.test_import_string.Test_import_string"
    assert class_obj.name == "Test_import_string"


# Generated at 2022-06-14 07:28:11.566633
# Unit test for function import_string
def test_import_string():
    """
    test import_string function
    """
    from niolabs.http.standard import import_string
    assert import_string.__doc__ is not None
    mod = import_string("niolabs.http.standard")
    assert mod.__name__ == "niolabs.http.standard"
    obj = import_string("niolabs.http.standard.import_string")
    assert obj.__name__ == "import_string"
    assert callable(obj)
    obj2 = import_string("niolabs.http.standard.import_string.import_string")
    assert obj2.__name__ == "import_string"
    assert callable(obj2)



# Generated at 2022-06-14 07:28:14.781461
# Unit test for function import_string
def test_import_string():
    assert import_string("aiohttp.web.Application") == import_module("aiohttp.web").Application
    assert import_string("aiohttp.abc") == import_module("aiohttp.abc")

# Generated at 2022-06-14 07:28:19.295972
# Unit test for function import_string
def test_import_string():
    """Testing function import_string"""
    import sys
    from .response import Response

    assert import_string('http.server.SimpleHTTPRequestHandler') == sys.modules['http.server'].SimpleHTTPRequestHandler
    assert import_string('http.response.Response').__class__ == Response

if __name__ == '__main__':
    test_import_string()

# Generated at 2022-06-14 07:28:25.699222
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    assert remove_entity_headers({"Content-Type": "application/json"}) == {}
    assert remove_entity_headers(
        {"Content-Type": "application/json", "Content-Location": "http://example.com"},
        allowed=("content-location",),
    ) == {"Content-Location": "http://example.com"}



# Generated at 2022-06-14 07:28:34.139552
# Unit test for function import_string
def test_import_string():
    import requests_mock
    test_module = "requests_mock.Adapter"
    result = import_string(test_module)
    assert result == requests_mock.Adapter
    test_class = "marshmallow.Schema"
    result = import_string(test_class)
    assert type(result) is type
    assert result.__name__ == "Schema"

# Generated at 2022-06-14 07:28:41.095068
# Unit test for function import_string
def test_import_string():
    from .message import Message

    msg_class = import_string("hypercorn.message.Message")
    assert isinstance(msg_class, Message) == True

    msg_class = import_string("hypercorn.message.Message")()
    assert isinstance(msg_class, Message) == True

    import_string("os.path")
    import_string("os.path")()

test_import_string()

# Generated at 2022-06-14 07:28:41.951053
# Unit test for function import_string
def test_import_string():
    pass


# Generated at 2022-06-14 07:28:45.885063
# Unit test for function import_string
def test_import_string():
    from sanic.server import Serve
    assert import_string("sanic.server.Serve") == Serve
    assert isinstance(import_string("sanic.server.Serve"), Serve)



# Generated at 2022-06-14 07:28:48.049810
# Unit test for function import_string
def test_import_string():
    import_obj = import_string("falcon.util.helpers")
    assert ismodule(import_obj)



# Generated at 2022-06-14 07:28:58.569407
# Unit test for function import_string
def test_import_string():
    from sanic.request import Request
    from sanic.testing import HOST, PORT

    import_str = import_string('sanic.request.Request')
    assert isinstance(import_str, Request) is True

    import_str = import_string('sanic.request.Request', 'sanic')
    assert isinstance(import_str, Request) is True

    import_str = import_string('sanic.request.Request', 'sanic.request')
    assert isinstance(import_str, Request) is True
    assert import_str.host == HOST
    assert import_str.port == PORT

# Generated at 2022-06-14 07:29:02.340859
# Unit test for function import_string
def test_import_string():
    from .cases import CaseProtocol

    module_class = CaseProtocol.__module__+'.'+CaseProtocol.__name__
    obj = import_string(module_class)
    assert isinstance(obj, CaseProtocol)
    assert isinstance(obj(), CaseProtocol)

# Generated at 2022-06-14 07:29:07.742100
# Unit test for function import_string
def test_import_string():
    import http.server
    import imp

    assert import_string("http.server") == http.server
    assert import_string("imp.load_source") == imp.load_source
    assert import_string("io.open").__name__ == "open"



# Generated at 2022-06-14 07:29:13.962157
# Unit test for function import_string
def test_import_string():
    from .auth import create_basic_auth_response

    assert import_string("homehub.http.auth.create_basic_auth_response") is create_basic_auth_response

    from .auth import BasicAuth

    assert import_string("homehub.http.auth.BasicAuth") is not BasicAuth
    assert isinstance(import_string("homehub.http.auth.BasicAuth"), BasicAuth)

# Generated at 2022-06-14 07:29:17.533617
# Unit test for function import_string
def test_import_string():
    assert ismodule(import_string("mock.Mock"))
    assert callable(import_string("mock.Mock.return_value"))
    assert ismodule(import_string("mock", package="mock"))
    assert callable(import_string("Mock.return_value", package="mock"))

