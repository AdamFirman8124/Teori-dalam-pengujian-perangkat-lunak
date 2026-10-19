

# Generated at 2022-06-14 07:27:07.971129
# Unit test for function import_string
def test_import_string():
    from . import common
    assert common == import_string("#.common")
    assert isinstance(import_string("#.errors.HTTPError"),
                      import_module("#.errors").HTTPError)



# Generated at 2022-06-14 07:27:10.542218
# Unit test for function import_string
def test_import_string():

    class A:
        pass

    assert import_string("inspect.ismodule", "importlib")(ismodule)
    assert import_string("test_http.test_import_string.A") == A()

# Generated at 2022-06-14 07:27:17.380624
# Unit test for function import_string
def test_import_string():
    """ Unit test for function import_string """
    import gidgethub.sansio
    import aiohttp.web
    assert(import_string("gidgethub.sansio.GitHubAPI") == gidgethub.sansio.GitHubAPI)
    assert(import_string("aiohttp.web.run_app") == aiohttp.web.run_app)


# Generated at 2022-06-14 07:27:26.882423
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(200) and has_message_body(201) and has_message_body(202) and has_message_body(203)
    assert has_message_body(205) and has_message_body(206) and has_message_body(207) and has_message_body(208)
    assert has_message_body(226) and has_message_body(300) and has_message_body(301) and has_message_body(302)
    assert has_message_body(303) and has_message_body(304) and has_message_body(305) and has_message_body(307)
    assert has_message_body(308) and has_message_body(400) and has_message_body(401) and has_message_body(402)

# Generated at 2022-06-14 07:27:30.475151
# Unit test for function import_string
def test_import_string():
    from message import Message
    assert import_string("message.Message") == Message
    assert import_string("message.Message").__class__ == Message


if __name__ == "__main__":
    test_import_string()

# Generated at 2022-06-14 07:27:41.692799
# Unit test for function import_string
def test_import_string():
    # Test is not a module
    module = import_string("falcon.status_codes")
    assert module == STATUS_CODES

    # Test is a module
    asgi_http_module = import_string("falcon.asgi_http")
    assert asgi_http_module == import_module("falcon.asgi_http")

# Generated at 2022-06-14 07:27:50.361505
# Unit test for function import_string
def test_import_string():
    module = import_string("http.cookies.SimpleCookie")
    assert callable(module)
    assert module.__name__ == "SimpleCookie"
    assert module.__module__ == "http.cookies"

    module = import_string("http.cookies.SimpleCookie", package="http.cookies")
    assert callable(module)
    assert module.__name__ == "SimpleCookie"
    assert module.__module__ == "http.cookies"

# Generated at 2022-06-14 07:27:59.820656
# Unit test for function import_string
def test_import_string():
    """Test import_string function with valid and invalid paths
    """
    # Import module by name
    assert ismodule(import_string("http.HTTPStatus"))
    # Import class by name
    assert isinstance(
        import_string("http.client.HTTPConnection"),
        import_module("http.client").HTTPConnection,
    )
    # Import module by path
    assert ismodule(import_string("aiohttp.server.request_handler"))
    # Import class by path
    assert isinstance(
        import_string("aiohttp.server.request_handler.RequestHandler"),
        import_module("aiohttp.server.request_handler").RequestHandler,
    )
    # Invalid path

# Generated at 2022-06-14 07:28:01.796274
# Unit test for function import_string
def test_import_string():
    assert not ismodule(import_string("h11._status_codes", "h11"))
    assert import_string("h11._status_codes", "h11").STATUS_CODES == STATUS_CODES
    return True


# Generated at 2022-06-14 07:28:08.655684
# Unit test for function import_string
def test_import_string():
    def _test_import_string(module):
        import_string(module)
    _test_import_string("http.server.BaseHTTPRequestHandler")
    _test_import_string("http.server")
    from http.server import HTTPServer
    assert type(import_string("http.server.HTTPServer")) == HTTPServer
    from http.server import HTTPServer
    assert type(import_string("http.server.HTTPServer")) == HTTPServer

# Generated at 2022-06-14 07:28:16.086289
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    """
    Test that remove_entity_headers() returns a new
    dictionary without the entity headers
    """
    headers = {
        "Content-Type": "text/html; charset=UTF-8",
        "Content-Length": "1000",
        "Expires": "0",
    }
    expected = {"Expires": "0"}
    result = remove_entity_headers(headers)
    assert expected == result



# Generated at 2022-06-14 07:28:18.886998
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Location": "The Land of Make-Believe",
        "Foo": "Bar",
    }
    headers = remove_entity_headers(headers)
    assert not is_entity_header(headers.popitem()[0])
    assert headers == {'foo': 'Bar'}

# Generated at 2022-06-14 07:28:27.954400
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Allow": "GET",
        "Content-Type": "application/json",
        "Content-Length": "0",
        "Content-MD5": "",
        "Last-Modified": "today",
    }
    headers = remove_entity_headers(headers)
    assert "Allow" in headers
    assert "Content-Type" in headers
    assert "Content-Length" not in headers
    assert "Content-MD5" not in headers
    assert "Last-Modified" not in headers

# Generated at 2022-06-14 07:28:39.325743
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Allow": "GET",
        "Content-Encoding": "gzip",
        "Content-Language": "en-US",
        "Content-Length": "0",
        "Content-Location": "http://www.example.com",
        "Content-MD5": "Q2hlY2sgSW50ZWdyaXR5IQ==",
        "Content-Range": "bytes 0-499/1234",
        "Content-Type": "text/html",
        "Expires": "Thu, 01 Dec 1994 16:00:00 GMT",
        "Last-Modified": "Thu, 01 Dec 1994 16:00:00 GMT",
        "Extension-Header": "My-Extension: My-Value",
    }

    remove_entity_headers(headers)

# Generated at 2022-06-14 07:28:46.076891
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Type": "text/html",
        "Content-Length": 1024,
        "Location": "http://www.example.org/index.html",
    }
    headers = remove_entity_headers(headers)
    assert headers == {"Location": "http://www.example.org/index.html"}

# Generated at 2022-06-14 07:28:59.570483
# Unit test for function remove_entity_headers

# Generated at 2022-06-14 07:29:03.233628
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    assert (
        remove_entity_headers(
            {
                "content-length": "1234",
                "content-location": "https://bing.com",
                "custom-header": "Hey",
            }
        )
        == {"content-location": "https://bing.com", "custom-header": "Hey"}
    )

# Generated at 2022-06-14 07:29:09.512325
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Type": "text/html; charset=utf-8",
        "Content-length": "1024",
        "Content-Location": "",
        "Content-language": "en",
    }
    assert remove_entity_headers(headers) == {
        "Content-Location": "",
        "Content-language": "en",
    }

# Generated at 2022-06-14 07:29:21.552419
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    import pytest
    header = {
        'Connection': 'keep-alive',
        'Last-Modified': 'Tue, 10 Mar 2020 12:30:38 GMT',
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': '0',
        'Allow': 'GET, POST',
        'Cache-Control': 'public, max-age=3600',
        'Content-Encoding': 'gzip',
        'Content-Language': 'en',
        'Transfer-Encoding': 'chunked',
        'Vary': 'Accept-Encoding',
        'X-Proxy-Cache': 'MISS',
        'Expires': 'Wed, 11 Mar 2020 14:30:32 GMT',
        'Date': 'Tue, 10 Mar 2020 14:30:38 GMT',
    }
   

# Generated at 2022-06-14 07:29:34.889093
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    """Tests for function remove_entity_headers"""
    assert remove_entity_headers({"content-length": "1024"}) == {}
    assert remove_entity_headers({"content-location": "a"}) == {
        "content-location": "a"
    }
    assert remove_entity_headers(
        {
            "Content-Type": "text/html",
            "Content-Range": "bytes",
            "Expires": "Thu, 01 Dec 1994 16:00:00 GMT",
        }
    ) == {"Expires": "Thu, 01 Dec 1994 16:00:00 GMT"}
    assert remove_entity_headers({"not a real header": "not a value"}) == {
        "not a real header": "not a value"
    }