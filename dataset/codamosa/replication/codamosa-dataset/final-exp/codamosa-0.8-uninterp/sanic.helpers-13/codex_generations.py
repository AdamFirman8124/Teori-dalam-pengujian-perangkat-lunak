

# Generated at 2022-06-14 07:27:17.560856
# Unit test for function import_string
def test_import_string():
    m = import_string("marshmallow.Schema")
    assert m.__name__ == "Schema"
    assert issubclass(m, object)

    class A(object):
        pass

    module_name = "yarl.http.http.A"
    module, klass = module_name.rsplit(".", 1)
    module = import_module(module)
    obj = getattr(module, klass)
    instance = obj()
    assert isinstance(instance, A)

# Generated at 2022-06-14 07:27:24.480366
# Unit test for function import_string
def test_import_string():
    from .app import App
    from .server import Server
    from .logging import logger_conf

    m = import_string(".app", __name__)
    assert m == App

    m = import_string(".server", __name__)
    assert m == Server

    m = import_string(".logging", __name__)
    assert m == logger_conf

    m = import_string(".logging.logger_conf", __name__)
    assert isinstance(m, dict)


if __name__ == "__main__":
    test_import_string()

# Generated at 2022-06-14 07:27:30.994735
# Unit test for function import_string
def test_import_string():
    from nanohttp.configuration import Configuration

    assert import_string("nanohttp.configuration.Configuration") is Configuration
    assert type(import_string("nanohttp.configuration.Configuration")) is Configuration



# Generated at 2022-06-14 07:27:36.742463
# Unit test for function import_string
def test_import_string():
    module = 'falcon.asgi.request'
    klass = 'Request'
    obj = import_string(f'{module}.{klass}')
    assert isinstance(obj, type) and obj.__name__ == klass
    obj = import_string(f'{module}')
    assert isinstance(obj, module)
    obj = import_string(f'modules.web.middleware.csrf')
    assert obj.__name__ == 'csrf'

# Generated at 2022-06-14 07:27:40.331523
# Unit test for function import_string
def test_import_string():
    assert import_string("tests.test_http_helpers.TestImportedClass") == "value"
    assert import_string("tests.test_http_helpers") is not None

# Generated at 2022-06-14 07:27:46.269876
# Unit test for function has_message_body
def test_has_message_body():
    status_list = [104, 200, 300, 400, 500, 200]
    for status in status_list:
        if status in [104, 200, 300, 400, 500] and not has_message_body(status):
            raise AssertionError
        elif status == 100 and has_message_body(status):
            raise AssertionError


# Generated at 2022-06-14 07:27:58.367871
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
    assert has_message_body(205) is True
    assert has_message_body(206) is True
    assert has_message_body(207) is True
    assert has_message_body(208) is True
    assert has_message_body(226) is True
    assert has_message_body(300) is True
    assert has_

# Generated at 2022-06-14 07:28:06.030043
# Unit test for function import_string
def test_import_string():
    import datetime
    from .test_server import Demo
    from ..middlewares import HTTPAcceptMiddleware
    assert import_string('pytis.server') == __import__('pytis.server')
    assert import_string('datetime.datetime') == datetime.datetime
    assert import_string('pytis.server.test_server.Demo') == Demo
    assert isinstance(
        import_string('pytis.middlewares.HTTPAcceptMiddleware'),
        HTTPAcceptMiddleware
    )

DATA = None

# Generated at 2022-06-14 07:28:12.636287
# Unit test for function import_string
def test_import_string():
    assert import_string('unittest.TestCase') == import_module('unittest').TestCase
    from .http_version import HttpVersion
    assert isinstance(import_string('http.http_version.HttpVersion'), HttpVersion)
    assert import_string('http.http_version.NON_HTTP') == import_module('http').http_version.NON_HTTP

# Generated at 2022-06-14 07:28:16.667824
# Unit test for function import_string
def test_import_string():
    assert import_string("os.path") is os.path
    assert import_string("os.path.abspath") is os.path.abspath
    assert import_string("tests.test_import_string.test_import_string")() is test_import_string

# Generated at 2022-06-14 07:28:23.810826
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Length": "10",
        "Content-Location": "http://example.com/",
        "Content-Type": "text/html; charset=utf-8",
    }
    assert remove_entity_headers(headers) == {"Content-Location": "http://example.com/"}



# Generated at 2022-06-14 07:28:26.950182
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = dict(foo="bar", content_length=10, content_type="text/plain")
    headers = remove_entity_headers(headers)
    assert headers == {"foo": "bar"}



# Generated at 2022-06-14 07:28:33.279465
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"Date": "Tue, 26 Jan 2020 00:12:04 GMT", "Content-Length": "18"}
    headers = remove_entity_headers(headers)
    assert not (is_entity_header("Date") or is_entity_header("Content-Length"))

if __name__ == "__main__":
    test_remove_entity_headers()

# Generated at 2022-06-14 07:28:39.374863
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {b"content-location": b"local", b"expires": b"123"}
    assert remove_entity_headers(headers) == headers

    headers = {b"content-location": b"local", b"expires": b"123", b"content-type": b"text/html"}
    assert remove_entity_headers(headers) == {b"content-location": b"local", b"expires": b"123"}

# Generated at 2022-06-14 07:28:51.284924
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"Content-Type": "text/plain",
               "Content-Length": "0",
               "Content-Location": "http://www.example.com/index.htm",
               "Expires": "Wed, 21 Oct 2015 07:28:00 GMT"}
    assert remove_entity_headers(headers) == \
        {"Content-Location": "http://www.example.com/index.htm",
         "Expires": "Wed, 21 Oct 2015 07:28:00 GMT"}
    assert remove_entity_headers(headers, allowed=("content-location",)) == \
        {"Content-Location": "http://www.example.com/index.htm"}
    assert remove_entity_headers(headers, allowed=[]) == {}

# Generated at 2022-06-14 07:28:59.326100
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "content-length": "1",
        "content-encoding": "gzip",
        "content-location": "File",
        "other-header": "other",
    }
    headers = remove_entity_headers(headers, allowed=("content-location",))
    assert headers == {"content-location": "File", "other-header": "other"}
    headers = remove_entity_headers(headers)
    assert headers == {"other-header": "other"}

# Generated at 2022-06-14 07:29:09.517105
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers1 = {
        "Content-Type": "text/html",
        "Content-Length": "15",
        "Content-Encoding": "gzip",
        "Content-Language": "de",
        "Content-Location": "ISO-8859-1",
        "Content-Range": "bytes 21010-47021/47022",
        "Content-MD5": "Q2hlY2sgSW50ZWdyaXR5IQ==",
        "Expires": "Thu, 01 Dec 1994 16:00:00 GMT",
        "Last-Modified": "Thu, 01 Dec 1994 16:00:00 GMT",
        "test-header": "my-test-header",
    }

# Generated at 2022-06-14 07:29:19.122516
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    """Test headers removal."""
    import pytest

    input_headers = {'Expires': 'datetime',
                     'Last-Modified': 'datetime',
                     'Content-Location': 'URL',
                     'Content-Type': 'string',
                     'Content-Encoding': 'string',
                     'Content-Language': 'string',
                     'Content-Length': 'string',
                     'Content-MD5': 'string',
                     'Content-Range': 'string',
                     'Trailer': 'string',
                     'Transfer-Encoding': 'string',
                     'Upgrade': 'string'}
    expected_headers = {'Expires': 'datetime',
                        'Content-Location': 'URL',
                        'Trailer': 'string',
                        'Transfer-Encoding': 'string',
                        'Upgrade': 'string'}
    assert remove_

# Generated at 2022-06-14 07:29:32.822266
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"content-location": "abc.mp4", "expires": "abc.mp4"}
    expected = {"content-location": "abc.mp4", "expires": "abc.mp4"}
    assert remove_entity_headers(headers) == expected

    headers = {"content-location": "abc.mp4", "expires": "abc.mp4", "age": "12"}
    expected = {"content-location": "abc.mp4", "expires": "abc.mp4"}
    assert remove_entity_headers(headers) == expected

    headers = {"content-location": "abc.mp4"}
    expected = {"content-location": "abc.mp4"}
    assert remove_entity_headers(headers) == expected

    headers = {}
    expected = {}
    assert remove_entity_headers(headers) == expected

# Generated at 2022-06-14 07:29:37.114749
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"Content-Type": "text/html", "Content-Length": "28",
               "Connection": "keep-alive", "Content-Location": "test"}
    assert remove_entity_headers(headers) == \
        {"Content-Location": "test"}