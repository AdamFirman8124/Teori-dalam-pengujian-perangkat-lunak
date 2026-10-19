

# Generated at 2022-06-14 07:40:42.145124
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = Router()
    method = "GET"
    endpoint = "foo"
    handler = "bar"
    uri = "baz"
    host = "boo"
    strict_slashes = False
    stream = True
    version = 1
    name = "test"
    router.add_route(method, endpoint, handler, uri, host, strict_slashes, stream, version, name)


# Generated at 2022-06-14 07:40:49.240318
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    url = "/test/add_route"
    method_list = ["GET", "POST"]

    r = RouteMixin(None)
    routes = r.add_route(handler, uri=url, methods=method_list)

    assert len(routes) == len(method_list)
    for m, route in zip(method_list, routes):
        assert route.methods == [m]
        assert route.uri == url


# Generated at 2022-06-14 07:40:57.013248
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # @add_route(uri, methods, host=None, strict_slashes=None, stream=None,
    # name=None, version=None, apply=True)
    # _add_route(self, handler, uri, methods, host=None, strict_slashes=None,
    # stream=None, name=None, version=None, apply=True)
    # app = Sanic('sanic')
    # app.add_route(handler, uri, methods, host, strict_slashes, stream=stream,
    # name=name, version=version, apply=apply)
    pass


# Generated at 2022-06-14 07:41:09.816036
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    async def async_test():
        # Creating class object of class RouteMixin
        t = RouteMixin()
        # calling instance method route of class RouteMixin
        r = await t.route('/', ['GET', 'PUT'], name='name', host='host', strict_slashes=True, version=1, apply=True, websocket=True, subprotocols='subprotocols')
        assert r == (await t.make_handler(), '/', ['GET', 'PUT'], False, False, None, 1, 'name', 'host', True, False, True, 'subprotocols')
    # Runing test
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_test())

# Generated at 2022-06-14 07:41:23.756024
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic, response
    from sanic.constants import HTTP_METHODS
    from sanic.response import text

    app = Sanic("test_route_mixin")

    @app.route("/")
    async def handler(request):
        return text("OK")

    assert len(app.router.routes_all) == 1
    assert app.router.routes_all[0].uri == "/"
    assert app.router.routes_all[0].method == "GET"
    assert app.router.routes_all[0].name == "handler"
    assert app.router.routes_all[0].strict_slashes is True
    assert app.router.routes_all[0].host is None


# Generated at 2022-06-14 07:41:30.762390
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Mock an object for self
    self_obj = Mock()
    # value for self.router
    self_router = Mock()
    self_obj.router = self_router
    # value for self.strict_slashes
    self_strict_slashes = Mock()
    self_obj.strict_slashes = self_strict_slashes
    # value for self.name
    self_name = Mock()
    self_obj.name = self_name
    # Mock variables and generate the return value for self.route method
    route_method_return = (Mock(),Mock())
    self_obj.route = Mock(return_value = route_method_return)
    # Set up mock input values
    uri = Mock()
    host = Mock()
    methods = Mock()
    strict_slashes

# Generated at 2022-06-14 07:41:37.447312
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Set up
    app = Sanic(__name__)
    app.config.from_object(Config)
    # app.config.from_envvar('APP_SETTING_ENV_FILE')

    # Exercise
    # result = app.add_route('/',HTMLResponse)

    # Verify
    # assert result == True

    # Cleanup - none necessary



# Generated at 2022-06-14 07:41:46.128677
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    _route_mixin = RouteMixin()
    _handler = None
    _uri = None
    _host = None
    _methods = None
    _strict_slashes = None
    _version = None
    _name = None
    _route = _route_mixin.add_route(
        _handler,
        _uri,
        _host,
        _methods,
        _strict_slashes,
        _version,
        _name
    )
    assert _route is not None


# Generated at 2022-06-14 07:41:59.824193
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import Route

    r = RouteMixin()
    assert len(r.routes) == 0
    assert len(r._future_statics) == 0

    @r.route('/test_route')
    def _test_route():
        return 'test_result'

    assert len(r.routes) == 1
    assert len(r._future_statics) == 0

    assert r.routes[0].uri == '/test_route'
    assert r.routes[0].handler == _test_route
    assert r.routes[0].methods == ['GET']
    assert r.routes[0].strict_slashes == True
    assert r.routes[0].host == None
    assert r.routes[0].version == 1
   

# Generated at 2022-06-14 07:42:10.924954
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    rm = RouteMixin()
    assert_raises(AttributeError, rm.route, uri="", methods=["GET"])
    assert_raises(AttributeError, rm.route, uri="", methods=["GET"], strict_slashes=True)
    assert_raises(AttributeError, rm.route, uri="", methods=["GET"], strict_slashes=False)
    assert_raises(AttributeError, rm.route, uri="", methods=["GET"], host="")
    assert_raises(AttributeError, rm.route, uri="", methods=["GET"], host="127.0.0.1")
    assert_raises(AttributeError, rm.route, uri="", methods=["GET"], host="localhost")

# Generated at 2022-06-14 07:42:33.076868
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():

    # Fixture
    class Router(RouteMixin):
        pass

    # Test
    router = Router()
    router.add_route(
        handler=lambda req:req,
        uri="/",
        host="",
        strict_slashes=False,
        version=None,
        methods=["GET"],
        name="",
        stream=False,
        status_code=200,
    )
    # Assertions
    assert len(router.routes_names["GET"]) == 1
    assert len(router.routes_all) == 1



# Generated at 2022-06-14 07:42:38.112628
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    RouteMixin = RouteMixin()
    RouteMixin.route(uri="", host=None, methods=None, strict_slashes=None, version=None, name=None, apply=True, subprotocols=None, websocket=True)



# Generated at 2022-06-14 07:42:47.978403
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    opt = copy.deepcopy(options)
    opt.update({'app_name': 'main'})
    app_instance = Application(name=opt['app_name'])
    print('\n test: RouteMixin_route')
    print("input parameters:")
    print("\t{}".format("uri: '/'"))
    print("\t{}".format("methods: None"))
    print("\t{}".format("host: None"))
    print("\t{}".format("strict_slashes: None"))
    print("\t{}".format("version: None"))
    print("\t{}".format("name: None"))
    print("\t{}".format("apply: True"))

    @app_instance.route("/")
    def handler(request):
        pass

# Generated at 2022-06-14 07:42:48.876295
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass

# Generated at 2022-06-14 07:43:02.851130
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Using mock object to unit test that doesn't depend on any external
    # component.
    mock_app = MagicMock()
    route_mixin = RouteMixin(mock_app)
    # Here, we test add_route with given URL and handler objects
    url_str = '/user/<user>'
    handler = Mock()
    route_mixin.add_route(handler, url_str, None, None, None, None)
    # Call assert_called_once method to check that
    # route method of mock_app is called once.
    mock_app.route.assert_called_once()
    # Call assert_called_once method to check that
    # route method of mock_app take the handler and URL as first argument.
    mock_app.route.assert_called_with(handler, url_str)
   

# Generated at 2022-06-14 07:43:11.974732
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import os
    import sys
    import json
    import asyncio
    import tempfile
    import logging
    import datetime
    import unittest
    import unittest.mock
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from sanic import Sanic
    from sanic.router import RouteExists, RouteExists

    from chanel.log import logger
    from chanel.config import config

    from helpers import init, teardown  # noqa E402
    from common import async_test  # noqa E402

    # Unit test for method add_route of class RouteMixin

# Generated at 2022-06-14 07:43:25.780919
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from sanic import router
    from sanic import Sanic
    from sanic import response
    from sanic.exceptions import NotFound
    from sanic.exceptions import RequestTimeout
    from sanic.exceptions import ProxyConnectionError
    from sanic.exceptions import InvalidUsage
    from sanic.exceptions import ServerError
    from sanic.exceptions import PayloadTooLarge
    from sanic.exceptions import PayloadExpected

    from sanic.constants import DEFAULT_HTTP_BODY_SIZE_LIMIT
    from sanic.constants import DEFAULT_HTTP_CONTENT_TYPE

    app = Sanic()
    router = RouteMixin(app)


    @router.static('/static', '/home/ubuntu/bak')
    def static_handler():
        return response.empty()
    assert router._

# Generated at 2022-06-14 07:43:38.602378
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import unittest

    class DummyApplication:
        def add_route(self, uri, handler):
            self.uri = uri
            self.handler = handler

        def get(self, uri, handler=None, host=None, strict_slashes=False, name=None):
            self.uri = uri
            self.handler = handler
            
    clazz = RouteMixin()
    obj = DummyApplication()
    clazz.add_route(obj, uri='/', handler=handler)
    assert obj.uri == '/'
    assert obj.handler == handler

    obj.get(uri='/', handler=handler)
    assert obj.uri == '/'
    assert obj.handler == handler



# Generated at 2022-06-14 07:43:49.084014
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.response import json, text, html
    from sanic import RouteMixin

    app = Sanic(__name__)

    @app.route("/")
    async def test(request):
        return text("Hello")

    obj = RouteMixin()
    routes, handler = obj.route(uri="/", methods=None, strict_slashes=None,
                                version=None, name=None, apply=True, static=True)()

    route_test = app.router.routes_names.get("test")
    routes_test = routes.get("test")

    assert_equal(routes_test, route_test)

    # Test a handler that returns a json
    @app.route("/json")
    async def return_json(request):
        return json

# Generated at 2022-06-14 07:43:59.797851
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic()
    @app.route('/')
    def f():
        pass
    assert len(app.router.routes_all) == 1
    assert app.router.routes_all[0].uri == '/'
    assert app.router.routes_all[0].name == '/'
    assert app.router.routes_all[0].handler == f
    assert len(app.router.routes_static) == 0
    assert len(app.router.routes_simple) == 0
    assert len(app.router.routes_dynamic) == 0
    assert len(app.router.routes_websocket) == 0

    # unit test for method add_route of class RouteMixin


# Generated at 2022-06-14 07:44:33.949343
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    print("test")
    app = Sanic("test")
    app.router.add_route(
        "get",
        "test_1",
        "<user_name:string>/<other_name:string>",
        "http://localhost",
        1,
        {"subprotocols": None},
        "test_2",
        True)
    assert app.router.routes is not None
    assert len(app.router.routes) == 1



# Generated at 2022-06-14 07:44:43.351800
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    app = Sanic()
    bp = Blueprint('bp')

    @bp.add_route('/')
    async def bp_index(request):
        return text('OK')
        
    url, handler = bp.routes[0]
    assert(url == '/')
    assert(handler == bp_index)
    assert(bp_index.__name__ == 'bp_index')
test_RouteMixin_add_route()


# Generated at 2022-06-14 07:44:44.644474
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:44:57.408639
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    uri = "uri"
    host = "host"
    strict_slashes = "strict_slashes"
    version = "version"
    name = "name"
    apply = "apply"
    uri = "uri"
    method = "method"
    host = "host"
    strict_slashes = "strict_slashes"
    version = "version"
    name = "name"
    apply = "apply"

    # arrange
    router = Sanic()
    router.get = MagicMock()
    router.post = MagicMock()
    router.put = MagicMock()
    router.patch = MagicMock()
    router.delete = MagicMock()
    router.head = MagicMock()
    router.options = MagicMock()

    # act

# Generated at 2022-06-14 07:45:10.804762
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    print("Method route of class RouteMixin")
    app = Sanic("sanic-router")
    router = RouteMixin(app)
    @router.route("/index", strict_slashes=True)
    async def index(request):
        pass
    @router.route("/index2", strict_slashes=True, host="www.example.com")
    async def index2(request):
        pass
    @router.route("/index3", methods=["POST"])
    async def index3(request):
        pass
    @router.route("/index4", methods=["POST"], version=1)
    async def index4(request):
        pass

# Generated at 2022-06-14 07:45:21.103691
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class RouteMixinClass(RouteMixin):
        pass
    ins = RouteMixinClass()
    ins.strict_slashes = None
    ins._future_handlers = set()
    ins._future_static = set()
    handler = lambda req: False
    uri = '/test'
    host = None
    methods = ['PUT', 'GET']
    strict_slashes = None
    version = 1
    name = 'test_route'
    apply = True
    ins.add_route(handler, uri, host, methods, strict_slashes, version, name, apply)
    assert len(ins._future_handlers) == 1



# Generated at 2022-06-14 07:45:23.218020
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    # Currently there is no unit test for this method
    pass


# Generated at 2022-06-14 07:45:28.038690
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic(__name__)
    protocol = SanicProtocol()
    # No value passed to parameter, and it is not required
    try:
        RouteMixin.route()
    except TypeError as err:
        assert str(err) == "route() missing 1 required positional argument: 'uri'"
    # When the first parameter is uri
    # If a list is passed to parameter, should raise TypeError
    try:
        RouteMixin.route(['/test2'])
    except TypeError as err:
        assert str(err) == "uri should be a str or bytes, not a list"
    # If a dict is passed to parameter, should raise TypeError

# Generated at 2022-06-14 07:45:34.298074
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic

    app = Sanic("test_RouteMixin_route")

    @app.route("/")
    async def handler(request):
        return text("OK")

    assert len(app.router.routes_all) == 1


# Generated at 2022-06-14 07:45:48.188592
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import logging

    logger = logging.getLogger()

    class Test:
        pass

    test = Test()
    test.logger = logger

    from .router import Route
    from .router import Router

    router = Router()

    async def my_handler1(request):
        return text("OK")

    async def my_handler2(request):
        return text("OK")

    uri = "my_uri"
    methods = ["GET"]
    host = "my_host"
    strict_slashes = True
    version = 1
    name = "my_name"
    # apply = True
    router.add_route(
        my_handler1, uri, methods, host, strict_slashes, version, name
    )


# Generated at 2022-06-14 07:46:28.086219
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.router import Route
    from sanic.response import text
    from sanic.server import HttpProtocol
    from sanic.exceptions import NotFound, InvalidUsage, ServerError, URLBuildError
    from sanic.handlers import ErrorHandler
    import re
    import traceback
    import logging
    import json
    import os
    import httpx
    import signal
    import asyncio
    import socket
    import sys
    import platform
    import warnings
    import types
    import weakref
    import abc
    import re
    import time
    import argparse
    import inspect
    import copy
    import subprocess
    import tempfile
    import contextlib
    import functools
    import base64
    import threading
    import multiprocessing
    import urll

# Generated at 2022-06-14 07:46:39.726538
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    """
    Test add_route method
    """
    from sanic.router import Route

    _route = Route(
        'GET',
        '/',
        None,
        'root',
        host=None,
        strict_slashes=None,
        version=None,
        name=None,
        stream=False,
        status_code=None,
        websocket=False,
    )

    app_instance = Sanic("app-instance")
    app_instance.router.add_route(_route)

    actual = app_instance.router.routes_all
    expected = {'root' : [_route]}
    assert actual == expected


# Generated at 2022-06-14 07:46:42.534798
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # t = RouteMixin(app=app)
    # t.app = app
    assert True == True


# Generated at 2022-06-14 07:46:46.343550
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # connect
    test_RouteMixin = RouteMixin()

    # run
    test_RouteMixin.route("uri", methods=["GET", "POST"])
    # assert

# Generated at 2022-06-14 07:46:54.014459
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    with pytest.raises(ValueError):
        # AssertionError: Expected <class 'ValueError'> to be raised.
        Sanic("test_route").route(uri="", methods=None, version=None)(None)

    with pytest.raises(ValueError):
        Sanic("test_route").route(uri="", methods=None, version=None, websocket=True)(None)


# Generated at 2022-06-14 07:47:05.953808
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic

    app = Sanic('test_RouteMixin_add_route')
    @app.route('/')
    def handler(request):
        return response.text('OK')
    @app.route('/')
    @app.route('/test')
    def handler1(request):
        return response.text('OK')
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/test', methods=['GET', 'POST'])
    def handler2(request):
        return response.text('OK')
    @app.route('/', methods=['GET', 'PUT'])
    @app.route('/test', methods=['GET', 'PUT'])
    def handler3(request):
        return response.text('OK')

# Generated at 2022-06-14 07:47:17.579341
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    import json
    with SanicRouter() as router:
        data = dict(
            kvm='kvm',
            kvm2='kvm2',
            kvm3='kvm3',
            kvm4='kvm4',
            kvm5='kvm5',
            kvm6='kvm6',
        )

        @router.route('/sanic', methods=['GET'])
        async def handler(request):
            return json(data)

        @router.route('/sanic', methods=['GET'])
        async def handler2(request):
            return json(data)

        request, response = router.test_client.get(
            '/sanic'
        )
        # Test response status
        assert response.status == 200
        # Test response body

# Generated at 2022-06-14 07:47:29.892324
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from sanic.constants import HTTP_METHODS

    class TestRouterMux(RouterMux):
        def __init__(self):
            super(TestRouterMux, self).__init__(name="TestRouterMux")

        async def test_websocket_request_handler(self, request):
            return request

        async def test_request_handler(self, request):
            return request

    router_mux = TestRouterMux()
    try:
        router_mux.static(
            uri="/static",
            file_or_directory=None,
        )
    except ValueError:
        pass
    else:
        assert False

    router_mux.static(
        uri="/static",
        file_or_directory=__file__,
    )


# Generated at 2022-06-14 07:47:38.898729
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic

    app = Sanic('test_RouteMixin_route')

    @app.route('/test_RouteMixin_route')
    def handler1(request):
        pass

    @app.route('/test_RouteMixin_route', 'GET')
    def handler2(request):
        pass

    @app.route('/test_RouteMixin_route', 'GET', 'POST')
    def handler3(request):
        pass

    app.route('/test_RouteMixin_route', 'GET', 'POST')(handler3)

    @app.route('/test_RouteMixin_route', methods=['GET', 'POST'])
    def handler4(request):
        pass

    assert len(app.router.routes_all) > 3


# Generated at 2022-06-14 07:47:51.255459
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.app import Sanic
    from sanic.router import Route
    from sanic.server import HttpProtocol

    # GIVEN
    app = Sanic(__name__)
    app.router = RouteMixin()
    handler = lambda: True
    methods = ["GET"]
    uri = "test_uri"
    host = "test_host"
    strict_slashes = True
    version = 1
    name = "test_name"
    apply = True
    web_socket = False

    # WHEN

# Generated at 2022-06-14 07:48:41.849087
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    assert True == False, "Test not implemented"


# Generated at 2022-06-14 07:48:47.273301
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Setup
    sanic = Sanic(__name__)
    expected_result = []

    # Exercise SUT
    sanic.add_route(handler, uri, methods, host, strict_slashes, version, name)
    actual_result = sanic.routes

    # Verify
    print(actual_result)
    print(expected_result)
    assert actual_result == expected_result


# Generated at 2022-06-14 07:48:53.146684
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # TODO - Test attributes
    test_obj = RouteMixin()
    test_obj.route(uri="test_uri", strict_slashes="test_strict_slashes", version="test_version", name="test_name", apply="test_apply", handler="test_handler")



# Generated at 2022-06-14 07:49:02.448339
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import json
    import os
    import socket
    import tempfile
    import threading
    import unittest
    from unittest import mock
    from urllib.parse import urlparse
    from wsgiref.validate import assert_
    import contextlib
    import errno
    import inspect
    import re
    import sys
    import warnings
    from functools import partial, wraps
    from http import HTTPStatus
    from io import StringIO
    from types import coroutine
    from unittest import mock
    from urllib.parse import quote_plus
    from types import ModuleType
    from warnings import warn

    from sanic import Sanic
    from sanic import exceptions
    from sanic import response

    from sanic.request import RequestParameters
    from sanic.response import HTTPResponse, StreamingHTTPR

# Generated at 2022-06-14 07:49:05.532371
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    rmc = RouteMixin()
    rmc.route()
    print("Complete test of RouteMixin.route")



# Generated at 2022-06-14 07:49:16.332112
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    m = RouteMixin()
    # 
    @m.route("/test", name = "test")
    async def test1():
        return Response("test")
    # 
    # @m.route("/test2", host="127.0.0.1", version=1)
    # async def test2():
    #     return Response("test")
    # 
    # @m.route("/test3", host="127.0.0.1", methods=["GET"])
    # async def test3():
    #     return Response("test")
    # 
    # @m.route("/test4", strict_slashes=True)
    # async def test4():
    #     return Response("test")
    # 
    # @m.route("/test5", name = "test_route2

# Generated at 2022-06-14 07:49:19.654443
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = Sanic('test')
    router.add_route(None, '', '', [], [])
    assert True
    

# Generated at 2022-06-14 07:49:22.147403
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    r = RouteMixin()
    r.route()
    pass


# Generated at 2022-06-14 07:49:23.359929
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # TODO
    pass


# Generated at 2022-06-14 07:49:35.657793
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class SanicAppStub(App):
        def __init__(self, config):
            pass

    sanic_app = SanicAppStub(config={})
    route_mixin = RouteMixin(app=sanic_app)

    @route_mixin.add_route('/', host='127.0.0.1', methods=["GET"], strict_slashes=False, version=1)
    def handler():
        pass

    assert len(route_mixin.routes) == 1
    assert route_mixin.routes[0].name == 'handler'
    assert route_mixin.routes[0].uri == '/'
    assert route_mixin.routes[0].host == '127.0.0.1'
    assert route_mixin.routes[0].method