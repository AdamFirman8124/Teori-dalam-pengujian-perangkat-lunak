

# Generated at 2022-06-14 07:27:26.275481
# Unit test for function import_string
def test_import_string():
    import tempfile
    import os.path
    import shutil
    from .utils import create_file_structure
    from .utils import create_python_module

    path_dest = tempfile.mkdtemp()
    path_project = os.path.join(path_dest, "project")
    path_module = os.path.join(path_project, "module")
    path_klass = os.path.join(path_module, "klass.py")
    path_module_init = os.path.join(path_module, "__init__.py")

    create_file_structure(path_dest, "project", "module", "klass.py")

    create_python_module(path_module_init)
    create_python_module(path_klass, "class Klass(object): pass")



# Generated at 2022-06-14 07:27:33.853564
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {
        "Content-Type": "text/plain",
        "Content-Length": "123",
        "Content-Location": "text.txt",
        "Expires": "12312312",
    }
    exp_headers = {"Content-Location": "text.txt", "Expires": "12312312"}
    headers = remove_entity_headers(headers)
    assert headers == exp_headers



# Generated at 2022-06-14 07:27:42.207258
# Unit test for function import_string
def test_import_string():
    from meinheld.server import test_app
    module = "meinheld.server.test_app"
    assert import_string(module) ==  test_app

    module = "meinheld.server.test_app.MyWSGIApp"
    obj = import_string(module)
    assert obj.__class__.__name__ == "MyWSGIApp"

# Generated at 2022-06-14 07:27:48.180588
# Unit test for function import_string
def test_import_string():
    result = import_string("hypercorn.sockets.tcp.TCPSocket")
    assert result.__class__.__name__ == "TCPSocket"

    result = import_string("hypercorn.sockets.tcp")
    assert result.__name__ == "tcp"

# Generated at 2022-06-14 07:27:51.784419
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    headers = {"content-type": "text/html", "content-length": "1", "expires": "today"}
    assert remove_entity_headers(headers) == {"expires": "today"}



# Generated at 2022-06-14 07:27:59.816967
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    # No entities headers
    assert remove_entity_headers({b"content-type": b"text/html"}) == {b"content-type": b"text/html"}

    # Normal use case
    assert remove_entity_headers(
        {
            b"content-type": b"text/html",
            b"content-length": b"23",
            b"content-encoding": b"gzip",
        }
    ) == {b"content-type": b"text/html"}

    # Allowed headers

# Generated at 2022-06-14 07:28:11.473931
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    """Unit test for function remove_entity_headers"""
    headers = {
        b"Content-Type": b"text/plain",
        b"Content-Length": b"3",
        b"Content-Encoding": b"utf-8",
        b"Content-Language": b"en",
        b"Content-Location": b"page.html",
        b"Content-MD5": b"asdf",
        b"Content-Range": b"0-1/1",
        b"Expires": b"0",
        b"Last-Modified": b"0",
        b"Extension-Header": b"1",
    }
    headers = remove_entity_headers(headers)

# Generated at 2022-06-14 07:28:19.053391
# Unit test for function import_string
def test_import_string():
    assert(import_string('shortuuid.uuid') == import_module('shortuuid.uuid'))
    assert(import_string('shortuuid.uuid.uuid') ==
           import_module('shortuuid.uuid').uuid)

    from shortuuid.uuid import uuid
    s = uuid()
    assert(import_string('shortuuid.uuid.uuid') != s)

    from shortuuid import uuid as shortuuid_uuid
    assert(import_string('shortuuid.uuid') != shortuuid_uuid)



# Generated at 2022-06-14 07:28:23.936722
# Unit test for function has_message_body
def test_has_message_body():
    assert has_message_body(200)
    assert not has_message_body(204)
    assert not has_message_body(304)
    assert not has_message_body(100)
    assert not has_message_body(199)
    assert not has_message_body(101)

# Generated at 2022-06-14 07:28:35.063144
# Unit test for function remove_entity_headers
def test_remove_entity_headers():
    nhdict = {
        "Allow": "GET,HEAD",
        "Content-Encoding": "gzip",
        "Content-Language": "en",
        "Content-Length": "348",
        "Content-Location": "/index.html",
        "Content-MD5": "Q2hlY2sgSW50ZWdyaXR5IQ==",
        "Content-Range": "bytes 21010-47021/47022",
        "Content-Type": "text/html; charset=utf-8",
        "Expires": "Thu, 01 Dec 1994 16:00:00 GMT",
        "Last-Modified": "Tue, 10 Nov 1994 12:45:26 GMT",
        "Etag": '"1234567"',
    }

# Generated at 2022-06-14 07:28:42.891545
# Unit test for function import_string
def test_import_string():
    assert import_string("test.test_http.import_string") == import_string
    assert import_string("test.test_http.from_dict") == from_dict
    assert import_string("test.test_http.from_list") == from_list

if __name__ == "__main__":
    test_import_string()

# Generated at 2022-06-14 07:28:52.645835
# Unit test for function import_string
def test_import_string():
    """Test function import_string"""
    from pytest import raises

    from . import httpmessage

    myhttpmessage = import_string(".httpmessage", package="aiohttp.protocol")

    assert myhttpmessage.__name__ == "aiohttp.protocol.httpmessage"
    assert myhttpmessage.HttpMessage

    with raises(ImportError):
        import_string("aiohttp.protocol.httpmess", package="aiohttp.protocol")

    myhttpmessage = import_string(".httpmessage.HttpMessage", package="aiohttp.protocol")

    assert myhttpmessage.__class__ == httpmessage.HttpMessage
    assert myhttpmessage.raw_headers

# Generated at 2022-06-14 07:28:55.029000
# Unit test for function import_string
def test_import_string():
    import datetime
    assert import_string("datetime.datetime", "datetime") is datetime.datetime

# Generated at 2022-06-14 07:28:56.310996
# Unit test for function import_string
def test_import_string():
    import_string("http.client")

# Generated at 2022-06-14 07:29:01.933138
# Unit test for function import_string
def test_import_string():
    import os
    app_name = "simple_http_server.server"
    curdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(curdir)
    expected = import_module(app_name)
    result = import_string(app_name)
    assert result
    assert result == expected

# Generated at 2022-06-14 07:29:14.076840
# Unit test for function import_string
def test_import_string():
    """
    >>> import_string('foo.bar.baz') # doctest: +ELLIPSIS
    <module 'foo.bar.baz' from ...>

    >>> import_string('foo.bar.baz.MyClass') # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    <foo.bar.baz.MyClass object at 0x...>

    >>> import_string('foo.bar.baz.MyClass.my_method') # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    <bound method MyClass.my_method of <foo.bar.baz.MyClass object at 0x...>>
    """
    pass

# Generated at 2022-06-14 07:29:21.765558
# Unit test for function import_string
def test_import_string():
    """
    Test for import string function
    """
    from importlib import import_module
    from os import path
    from tempfile import gettempdir
    from typing import Any
    import sys

    import pytest

    test_module_name = "module.name"
    test_module_file_name = "test_module.py"
    test_module_class_name = "TestModuleClass"
    test_module_class_file_name = "test_module_class.py"
    test_module_method_name = "test_method"
    test_module_method_file_name = "test_module_method.py"
    test_module_method_value = "Hello world!"
    test_module_import_error = "osmodule.name"

    test_module_dir = gettempdir()
    test_

# Generated at 2022-06-14 07:29:30.933425
# Unit test for function import_string
def test_import_string():
    from pytest import main
    import sys
    import os
    from unittest.mock import patch


    class FakeModule(object):
        def __init__(self, name, path):
            self.__name__ = name
            self.__file__ = path + os.sep + '__init__.py'
            self.__path__ = path + os.sep
            self.__spec__ = name

        def __repr__(self):
            return self.__name__

    def get_fake_modules(pkg):
        pkg = pkg.replace('.', os.sep)
        path = os.sep + 'fake' + os.sep + pkg
        pkg = 'fake.' + pkg.replace(os.sep, '.')
        return FakeModule(pkg, path),

# Generated at 2022-06-14 07:29:39.688643
# Unit test for function import_string
def test_import_string():
    from pathlib import Path
    from cachetools import TTLCache
    from cachetools.keys import hashkey

    # Test for function import_string
    assert callable(import_string("cachetools.TTLCache"))
    assert import_string("pathlib.Path") == Path
    assert str(import_string("pathlib.Path", ".")) == "."
    assert isinstance(import_string("cachetools.TTLCache"), TTLCache)
    assert isinstance(import_string("cachetools.hashkey", "cachetools"), hashkey)


# Generated at 2022-06-14 07:29:49.907279
# Unit test for function import_string
def test_import_string():
    def class_a():
        pass
    class class_b:
        pass
    module_a = "tests.test_cardinal.class_a"
    module_b = "tests.test_cardinal.class_b"
    module_c = "tests.test_cardinal"
    assert import_string(module_a, package="tests") == class_a
    assert import_string(module_b, package="tests") == class_b
    assert import_string(module_c, package="tests") == sys.modules[__name__]