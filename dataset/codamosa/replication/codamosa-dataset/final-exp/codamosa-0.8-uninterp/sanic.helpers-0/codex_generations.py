

# Generated at 2022-06-14 07:27:13.685740
# Unit test for function has_message_body
def test_has_message_body():
    """
    has_message_body() returns True or False depending on the
    status given as first parameter
    """
    # Testing 1XX status
    assert not has_message_body(100)
    assert not has_message_body(101)
    assert not has_message_body(199)

    # Testing 204 status
    assert not has_message_body(204)

    # Testing 304 status
    assert not has_message_body(304)

    # Testing 200 status
    assert has_message_body(200)

    # Testing 300 status
    assert has_message_body(300)

    # Testing 400 status
    assert has_message_body(400)

    # Testing 500 status
    assert has_message_body(500)

# Generated at 2022-06-14 07:27:25.288424
# Unit test for function import_string
def test_import_string():
    import tempfile
    import sys
    from pathlib import Path

    tmp = tempfile.mkdtemp()
    with tempfile.NamedTemporaryFile(mode="w", dir=tmp, delete=False) as f:
        f.write(
            '''
        class Class:
            def func(self):
                return "value"
        '''
        )
        f.write("\n")
    sys.path.append(tmp)

    module = import_string("{}.{}".format(Path(f.name).stem, "Class"))
    instance = import_string("{}.{}".format(Path(f.name).stem, "Class"))

    assert module is None
    assert instance.func() == "value"

# Generated at 2022-06-14 07:27:38.070090
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-encoding": "gzip",
        "Content-language": "en",
        "Content-Length": "1024",
        "Content-Location": "https://example.com/index.html",
        "Content-MD5": "q2d3wfsdqwfg",
        "Content-Range": "bytes",
        "Content-Type": "application/json",
        "Expires": "Thu, 01 Dec 1994 16:00:00 GMT",
        "Last-Modified": "Tue, 15 Nov 1994 12:45:26 GMT",
        "extension-header": "new-header: new-value",
        "connection": "keep-alive",
    }
    assert not remove_entity_headers(headers)

# Generated at 2022-06-14 07:27:41.899678
# Unit test for function import_string
def test_import_string():
    from werkzeug.exceptions import NotFound

    nf = import_string('werkzeug.exceptions.NotFound')
    assert issubclass(nf(), NotFound)

# Generated at 2022-06-14 07:27:53.241046
# Unit test for function import_string
def test_import_string():
    import pytest
    from sound.core.utils.http import HTTPError

    assert isinstance(import_string("sound.core.routers.Router"), Router)

    with pytest.raises(ImportError):
        import_string("whatever.does.not.exists.class")

    with pytest.raises(AttributeError):
        import_string("sound.core.routers.Router.does.not.exists.class")

    with pytest.raises(TypeError):
        import_string("sound.core.utils.http.HTTPError.__init__")

    assert isinstance(import_string("sound.core.utils.http.HTTPError", "sound"), HTTPError)

# Generated at 2022-06-14 07:27:59.058685
# Unit test for function import_string
def test_import_string():
    import pytest
    from pydantic import ValidationError
    from uvicore.http.error_handler import ErrorHandler
    from uvicore.http.single_ton_middleware import SingleTonMiddleware

    # Test import module
    error_handler = import_string('uvicore.http.error_handler.ErrorHandler')
    assert issubclass(error_handler, ErrorHandler)

    # Test import class
    singleton_middleware = import_string('uvicore.http.single_ton_middleware.SingleTonMiddleware')
    assert issubclass(singleton_middleware, SingleTonMiddleware)
    singleton_middleware = singleton_middleware()
    assert isinstance(singleton_middleware, SingleTonMiddleware)

    # Test not found

# Generated at 2022-06-14 07:27:59.951409
# Unit test for function import_string
def test_import_string():
    assert import_string('websauna.tests.test_importstring.TestApp') is not None


# Generated at 2022-06-14 07:28:04.050429
# Unit test for function import_string
def test_import_string():
    module = import_string("http.client", "test_http")
    assert hasattr(module, "HTTPResponse")

    module = import_string("http.client.HTTPResponse", "test_http")
    assert isinstance(module, type)
    assert hasattr(module, "read")



# Generated at 2022-06-14 07:28:09.803919
# Unit test for function import_string
def test_import_string():
    assert "http" == import_string("http.client").__name__
    assert "HTTPConnection" == import_string("http.client.HTTPConnection").__name__
    assert "client" == import_string("http.client", package="http").__name__
    assert "HTTPConnection" == import_string("http.client.HTTPConnection", package="http").__name__

# Generated at 2022-06-14 07:28:20.584923
# Unit test for function remove_entity_headers