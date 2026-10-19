

# Generated at 2022-06-14 07:27:14.644654
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(100) == False
    assert has_message_body(101) == False
    assert has_message_body(102) == False
    assert has_message_body(103) == False
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
    assert has_message_body(300) == True
    assert has_

# Generated at 2022-06-14 07:27:19.598476
# Unit test for function import_string
def test_import_string():
    import uvicorn.color

    module = import_string(__name__ + ".test_import_string")
    assert module.__name__ == __name__

    color = import_string("uvicorn.color.Colorizer")
    assert isinstance(color, uvicorn.color.Colorizer)

# Generated at 2022-06-14 07:27:27.517222
# Unit test for function import_string
def test_import_string():
    import aiohttp
    assert import_string("aiohttp.request") == aiohttp.request
    assert import_string("aiohttp.client.ClientSession") == \
        aiohttp.client.ClientSession
    assert import_string(
        "aiohttp.client.ClientSession"
    )() == aiohttp.client.ClientSession()
    assert import_string("tests.clientsession_test.func") == func

# Generated at 2022-06-14 07:27:33.917002
# Unit test for function import_string
def test_import_string():
    """
    import a module or class by string path.

    :module_name: str with path of module or path to import and
    instanciate a class
    :returns: a module object or one instance from class if
    module_name is a valid path to class

    """
    assert import_string("trio_websocket.http.http_std")
    assert not isinstance(import_string("trio_websocket.http.http_std"), type)
    assert isinstance(import_string("trio_websocket.exceptions.ErrorHTTPRequest"), type)

# Generated at 2022-06-14 07:27:42.730145
# Unit test for function import_string
def test_import_string():
    import modules.module_a as module_a
    module_a_test = import_string("modules.module_a")
    assert module_a is module_a_test

    from modules.module_a.class_a import ClassA
    class_a_test = import_string("modules.module_a.class_a.ClassA")
    assert isinstance(class_a_test, ClassA)

# Generated at 2022-06-14 07:27:56.052695
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(200) == True
    assert has_message_body(206) == True
    assert has_message_body(301) == True
    assert has_message_body(500) == True

    assert has_message_body(100) == False
    assert has_message_body(101) == False
    assert has_message_body(102) == False
    assert has_message_body(103) == False

    assert has_message_body(200) == True
    assert has_message_body(201) == True
    assert has_message_body(202) == True
    assert has_message_body(203) == True
    assert has_message_body(204) == False
    assert has_message_body(205) == False
    assert has_message_body(206) == True
    assert has_

# Generated at 2022-06-14 07:28:03.201184
# Unit test for function import_string
def test_import_string():
    import sys
    from pathlib import Path
    from . import exceptions
    import_path = "asyncio.BaseEventLoop"
    cls_path = "uvicorn.http.websocket.WebSocketProtocol"

    # given
    module_obj = import_string(import_path)
    cls_obj = import_string(cls_path)

    # then
    assert sys.modules["asyncio"] is module_obj
    assert isinstance(cls_obj, type)
    assert isinstance(cls_obj(), type)
    assert isinstance(cls_obj(), cls_obj)
    exception = None
    try:
        import_string("")
    except exceptions.ImproperlyConfigured as exc:
        exception = exc
    assert exception is not None



# Generated at 2022-06-14 07:28:05.462978
# Unit test for function import_string
def test_import_string():
    from . import http
    assert import_string("quart.serving.http") is http



# Generated at 2022-06-14 07:28:10.176555
# Unit test for function import_string
def test_import_string():
    assert import_string("falcon.test_helpers.create_environ") == create_environ
    assert import_string("falcon.test_helpers.Wsgier")().status == '200 OK'


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 07:28:20.545114
# Unit test for function import_string
def test_import_string():
    '''
    Test cases that verify the import_string function is working as expected.
    '''

    # test that the function returns a module when it is provided a valid module
    assert import_string("http.client")
    assert issubclass(import_string("http.client.HTTPResponse"), object)

    # test that the function can import a class
    assert import_string("mantisshrimp.http.HTTPRequest")

    # test that the package property of the import function is working

    assert issubclass(import_string("HTTPResponse", "http.client"), object)
    assert import_string("HTTPRequest", "mantisshrimp.http")
    assert issubclass(import_string("HTTPResponse", "http.client"), object)

# Generated at 2022-06-14 07:28:31.329334
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Host": "localhost:1234",
        "Content-Length": "0",
        "Content-Type": "text/plain",
        "Content-Location": "http://localhost:1234/",
    }
    new_headers = remove_entity_headers(headers)
    assert "Content-Length" not in new_headers
    assert "Content-Type" not in new_headers
    assert new_headers["Host"] == "localhost:1234"
    assert new_headers["Content-Location"] == "http://localhost:1234/"

# Generated at 2022-06-14 07:28:42.768258
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {'content-encoding': 'gzip', 'server': 'nginx', 'content-length': '222', 'date': 'Sun, 21 Jun 2015 023:55:18 GMT', 'connection': 'keep-alive', 'content-type': 'text/html; charset=utf-8'}
    assert remove_entity_headers(headers) == {'server': 'nginx', 'date': 'Sun, 21 Jun 2015 023:55:18 GMT', 'connection': 'keep-alive'}
    assert remove_entity_headers(headers, allowed=["content-length"]) == {'server': 'nginx', 'content-length': '222', 'date': 'Sun, 21 Jun 2015 023:55:18 GMT', 'connection': 'keep-alive'}


# Generated at 2022-06-14 07:28:53.715444
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Allow": "GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE",
        "Content-Encoding": "gzip",
        "Content-Language": "en-US",
        "Content-Length": "15",
        "Content-Location": "http://www.gnu.org/licenses/gpl-2.0.html",
        "Content-MD5": "",
        "Content-Range": "",
        "Content-Type": "text/html; charset=utf-8",
        "Expires": "Fri, 30 Oct 1998 14:19:41 GMT",
        "Last-Modified": "Tue, 15 Nov 1994 12:45:26 GMT",
        "Extension-Header": "",
    }
    headers_without_entity_headers = remove_entity_

# Generated at 2022-06-14 07:29:02.233480
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Type": "text/html",
        "Content-Length": 10,
        "Content-Language": "fr",
        "Content-Encoding": "gzip",
        "Content-Range": "bytes 0-10/100",
        "Expires": "Wed, 09 Sep 2020 15:30:00 GMT",
        "Last-Modified": "Wed, 09 Sep 2020 15:30:00 GMT",
        "test": "teste",
    }
    headers = remove_entity_headers(headers)
    assert headers == {"test": "teste"}

# Generated at 2022-06-14 07:29:05.816684
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"Content-Location": "/file.html", "Date": "today"}
    assert remove_entity_headers(headers) == headers

# Generated at 2022-06-14 07:29:18.521409
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Length": "32",
        "Cache-Control": "public, max-age=60",
        "Content-MD5": "Q2hlY2sgSW50ZWdyaXR5IQ==",
        "Content-Type": "text/html; charset=utf-8",
        "Expires": "Thu, 19 Nov 1981 08:52:00 GMT",
        "Last-Modified": "Tue, 10 Nov 1981 23:00:00 GMT",
    }
    headers = remove_entity_headers(headers)
    assert "Content-Length" not in headers
    assert "Content-MD5" not in headers
    assert "Content-Type" not in headers
    assert "Expires" in headers
    assert "Last-Modified" in headers
    assert "Cache-Control" in headers

# Generated at 2022-06-14 07:29:32.080371
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    all_headers = {
        "Cache-Control": "private",
        "Connection": "close",
        "Content-Type": "application/json",
        "Date": "Tue, 05 Jun 2018 09:57:53 GMT",
        "Expires": "Tue, 05 Jun 2018 09:57:53 GMT",
        "Last-Modified": "Tue, 05 Jun 2018 09:57:53 GMT",
        "Location": "None",
        "Server": "Werkzeug/0.14.1 Python/3.4.4",
        "Content-Length": "0",
    }

# Generated at 2022-06-14 07:29:39.779784
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "content-encoding": "deflate",
        "content-length": "deflate",
        "content-location": "deflate",
        "content-md5": "deflate",
        "content-range": "deflate",
        "content-type": "deflate",
        "expires": "deflate",
        "last-modified": "deflate",
        "extension-header": "deflate",
    }

    assert remove_entity_headers(headers) == {"content-location": "deflate", "expires": "deflate"}

# Generated at 2022-06-14 07:29:46.779498
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Length": "200",
        "Content-Type": "text/html",
        "Content-Location": "http://www.google.es",
        "Expires": "Thu, 29 Oct 2020 00:57:00 GMT",
    }
    headers = remove_entity_headers(headers)
    assert headers == {
        "Content-Location": "http://www.google.es",
        "Expires": "Thu, 29 Oct 2020 00:57:00 GMT",
    }

# Generated at 2022-06-14 07:29:56.844807
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    from pytest import approx

    headers = {}
    assert remove_entity_headers(headers) == {}

    headers = {"Content-length": 3}
    assert remove_entity_headers(headers) == {}

    headers = {"Content-Length": 25, "x-random": "coco"}
    assert remove_entity_headers(headers) == {"x-random": "coco"}

    headers = {
        "Content-Length": 25,
        "x-random": "coco",
        "Content-type": "text/html",
    }
    assert remove_entity_headers(headers) == {"x-random": "coco"}
