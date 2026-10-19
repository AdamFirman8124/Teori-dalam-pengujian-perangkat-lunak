

# Generated at 2022-06-14 07:27:12.366905
# Unit test for function has_message_body
def test_has_message_body():
    assert(has_message_body(100) == False)
    assert(has_message_body(200) == True)
    assert(has_message_body(300) == True)
    assert(has_message_body(400) == True)
    assert(has_message_body(500) == True)
    assert(has_message_body(204) == False)
    assert(has_message_body(304) == False)

#Unit test for function is_entity_header

# Generated at 2022-06-14 07:27:20.395127
# Unit test for function import_string
def test_import_string():
    import os
    import tempfile

# Generated at 2022-06-14 07:27:25.713703
# Unit test for function import_string
def test_import_string():
    from . import App
    class AppMock:
        def __init__(self):
            self.x = "x"
    assert App == import_string("falcon.asgi.App")
    assert AppMock().x == import_string("tests.test_asgi.AppMock").x

# Generated at 2022-06-14 07:27:38.966389
# Unit test for function has_message_body
def test_has_message_body():

    assert not has_message_body(100)
    assert not has_message_body(101)
    assert not has_message_body(101)
    assert not has_message_body(102)
    assert not has_message_body(103)
    assert not has_message_body(103)
    assert not has_message_body(104)
    assert not has_message_body(105)
    assert not has_message_body(106)
    assert not has_message_body(107)
    assert not has_message_body(108)
    assert not has_message_body(109)
    assert not has_message_body(110)
    assert not has_message_body(111)
    assert not has_message_body(112)
    assert not has_message_body(113)
    assert not has_message_

# Generated at 2022-06-14 07:27:43.582649
# Unit test for function import_string
def test_import_string():
    from .router import Router
    module = import_string("aiohttp.web.router.Router")
    assert issubclass(module, Router) is True

# Generated at 2022-06-14 07:27:56.371043
# Unit test for function import_string
def test_import_string():
    """ Unit test for import_string function """
    module = "asyncio"
    assert import_string(module) is import_module(module)

    module_2 = "http.HTTPStatus"
    assert import_string(module_2) is import_module(module_2)

    prev_import_module = import_module
    try:
        import_string_module = "http.HTTPStatus"
        assert import_string(import_string_module) is import_module(import_string_module)

        import_string_class = "http.client.HTTPResponse"
        assert isinstance(
            import_string(import_string_class), import_module(import_string_class).HTTPResponse
        )
    finally:
        import_module = prev_import_module

# Generated at 2022-06-14 07:28:02.860886
# Unit test for function import_string
def test_import_string():
    from aiohttp import web
    path_to_string = "aiohttp.web.web_runner"
    path_to_class = "aiohttp.web.web_runner.AppRunner"
    string = import_string(path_to_string)
    assert web.web_runner.__name__ == string.__name__
    obj = import_string(path_to_class)
    assert isinstance(obj, web_runner.AppRunner)

# Generated at 2022-06-14 07:28:09.186042
# Unit test for function import_string
def test_import_string():
    from unittest import mock, TestCase

    class TestClass():
        pass

    package = mock.MagicMock()
    mock.MagicMock(name="module", return_value=package)
    package.klass = TestClass

    assert import_string("module.klass") == TestClass()
    assert import_string("module.klass", "package") == TestClass()
    assert import_string("module") == package

# Generated at 2022-06-14 07:28:12.535545
# Unit test for function import_string
def test_import_string():
    from . import URL

    url_obj = import_string("aiohttp.web.URL")
    assert isinstance(url_obj, URL)
    assert url_obj.host is None



# Generated at 2022-06-14 07:28:18.294495
# Unit test for function has_message_body
def test_has_message_body():

    assert has_message_body(100) == True
    assert has_message_body(200) == True
    assert has_message_body(204) == False
    assert has_message_body(300) == True
    assert has_message_body(304) == False
    assert has_message_body(400) == True
    assert has_message_body(500) == True
    assert has_message_body(501) == True

# Generated at 2022-06-14 07:28:24.937844
# Unit test for function import_string
def test_import_string():
    from falcon import API

    api = import_string("falcon.API")
    assert isinstance(api, API)

    api = import_string("falcon.api.API")
    assert isinstance(api, API)

# Generated at 2022-06-14 07:28:26.708643
# Unit test for function import_string
def test_import_string():
    assert import_string("nefertari.utils.import_strings")



# Generated at 2022-06-14 07:28:33.924763
# Unit test for function import_string
def test_import_string():
    """
    You can create a unit test to see if import_string function
    works properly.

    """
    from starlette.testclient import TestClient
    from starlette.applications import Starlette

    async def home(request):
        return "home"

    app = Starlette()
    app.add_route("/", home, methods=["GET"])
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "home"

# Generated at 2022-06-14 07:28:39.028843
# Unit test for function import_string
def test_import_string():
    import sys, os
    from tempfile import TemporaryDirectory
    tmpdir = TemporaryDirectory()
    sys.path.append(tmpdir.name)

# Generated at 2022-06-14 07:28:44.236928
# Unit test for function import_string
def test_import_string():
    from pyathena import auth, protocol
    assert import_string("pyathena.auth.Auth") == auth.Auth
    assert import_string("pyathena.protocol.AthenaProtocol") == protocol.AthenaProtocol

# Generated at 2022-06-14 07:28:57.562390
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    from .model import Headers
    from .header import parse_headers
    from .http_parser import HttpParser

    parser = HttpParser()
    headers = Headers()

# Generated at 2022-06-14 07:29:07.924655
# Unit test for function import_string
def test_import_string():
    import_string("httptools.parser")
    import_string("httptools.parser.HttpRequestParser")
    import_string("aiohttp.web")
    import_string("aiohttp.web.Application")
    try:
        import_string("httptools.parser.A")
        assert False, "Should get exception"
    except AttributeError as e:
        assert e.args[0] == "module 'httptools.parser' has no attribute 'A'"
    try:
        import_string("httptools.parser.HttpRequestParser.a")
        assert False, "Should get exception"
    except AttributeError as e:
        assert e.args[0] == "'HttpRequestParser' object has no attribute 'a'"


# Generated at 2022-06-14 07:29:13.656647
# Unit test for function import_string
def test_import_string():
    import os

    import mock

    t = import_string("os")
    assert t == os
    with mock.patch("os.mkdir"):
        import os

    t = import_string("os.mkdir")
    assert t == os.mkdir
    return

if __name__ == "__main__":
    test_import_string()

# Generated at 2022-06-14 07:29:18.543314
# Unit test for function import_string
def test_import_string():
    import aioworker.config as configmod
    config = import_string('aioworker.config.Config')
    assert configmod.Config is config
    config = import_string('aioworker.config.Config', 'aioworker')
    assert configmod.Config is config
    config = import_string('aioworker.config.Config', 'aioworker.config')
    assert configmod.Config is config

# Generated at 2022-06-14 07:29:32.139584
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = remove_entity_headers({
        "Content-type": "text/html",
        "Content-length": "10",
        "Host": "pulsarwebserver.org",
        "Expires": "now",
        "Keep-Alive": "timeout=1",
        })
    assert headers == {
        "Host": "pulsarwebserver.org",
        "Keep-Alive": "timeout=1",
        "Expires": "now",
        }
    headers = remove_entity_headers({
        "Content-type": "text/html",
        "Content-length": "10",
        "Host": "pulsarwebserver.org",
        "Expires": "now",
        "Keep-Alive": "timeout=1",
        }, allowed=("expires",))