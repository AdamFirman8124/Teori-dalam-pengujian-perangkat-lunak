

# Generated at 2022-06-14 07:55:55.847200
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:55:58.443666
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router
    import types
    import sanic
    sanic.__version__ = "19.12.2"
    router = Router()
    @router.add("/")
    def func():
        pass
    r = router.get("/", "GET", None)
    assert isinstance(r, types.GeneratorType)
    assert r.gi_code.co_name == "handler"

# Generated at 2022-06-14 07:56:09.241640
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest

    router = Router()
    route = Route('/<name>', lambda: None)
    route.labels.add('__file_uri__')
    router.dynamic_routes[route.path] = route
    router.finalize()

    # router is not None
    assert router is not None

    # invalid route
    route = Route('/<name>', lambda: None)
    route.labels.add('__name__')
    router.dynamic_routes[route.path] = route 

    with pytest.raises(SanicException) as excinfo:
        router.finalize()
    assert excinfo.type == SanicException

# Generated at 2022-06-14 07:56:10.681065
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 07:56:15.868527
# Unit test for constructor of class Router
def test_Router():
    assert Router.DEFAULT_METHOD == "GET"
    assert Router.ALLOWED_METHODS == ['HEAD', 'OPTIONS', 'GET', 'POST',
                    'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']

# Generated at 2022-06-14 07:56:17.221815
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:56:20.341771
# Unit test for constructor of class Router
def test_Router():
    """
    Test case for constructor of class Router.
    
    Arguments:
        None
    
    Returns:
        None
    """
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 07:56:22.405141
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router) == True


# Generated at 2022-06-14 07:56:24.408868
# Unit test for constructor of class Router
def test_Router():
    router=Router()
    assert router

# Generated at 2022-06-14 07:56:30.192556
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 07:56:41.556022
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = mock.Mock()
    route.labels = ['__foo__']
    router = Router()
    router.dynamic_routes = {0: route}
    with pytest.raises(SanicException):
        router.finalize()


# Generated at 2022-06-14 07:56:51.368805
# Unit test for constructor of class Router
def test_Router():
    print("test_Router")

    # test router = Router()
    router = Router()
    print(router)

    # test router = Router(labels=["test_label", "test_label_2"])
    router = Router(labels=["test_label", "test_label_2"])
    print(router)

    # test router = Router(labels={'test_label_3': 'test_label_3', 'test_label_4': 'test_label_4'})
    router = Router(labels={'test_label_3': 'test_label_3', 'test_label_4': 'test_label_4'})
    print(router)

# Generated at 2022-06-14 07:57:03.615018
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.route import Route
    from sanic.constants import HTTP_METHODS
    from sanic_routing.exceptions import RouteAlreadyRegistered

    router = Router(None)

    route = Route(router, "/", HTTP_METHODS, lambda x: "match")
    route.labels.update({"__bob__": "frog"})
    router.dynamic_routes[route.path] = route

    # Test with a parameter name that starts with __
    with pytest.raises(SanicException):
        route2 = Route(router, "/:__bob__", HTTP_METHODS, lambda x: "match")
        router.add_route(route2)
        router.finalize()

    router = Router(None)

# Generated at 2022-06-14 07:57:05.003636
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 07:57:09.469791
# Unit test for constructor of class Router
def test_Router():
    a = Router()
    assert a.DEFAULT_METHOD == "GET"
    assert a.ALLOWED_METHODS == ["HEAD", "OPTIONS", "GET", "POST", "PUT", "PATCH", "DELETE"]



# Generated at 2022-06-14 07:57:15.032498
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    A unit test for method finalize of class Router
    """
    def mock_method_finalize(self, *args, **kwargs):
        pass

    router = Router()
    router.finalize = mock_method_finalize
    router.finalize()

# Generated at 2022-06-14 07:57:24.026364
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Test 1
    router = Router()
    router.add("/", ["GET"])
    assert len(router.finalize()) == 2
    # Test 2
    router = Router()
    router.add("/__test__", ["GET"])
    try:
        router.finalize()
        assert False
    except SanicException as e:
        assert str(e) == "Invalid route: /__test__. Parameter names cannot use '__'."
    # Test 3
    router = Router()
    router.add("/__file_uri__", ["GET"])
    assert len(router.finalize()) == 2

# Generated at 2022-06-14 07:57:25.448402
# Unit test for constructor of class Router
def test_Router():
    route = Router()


# Generated at 2022-06-14 07:57:27.617900
# Unit test for constructor of class Router
def test_Router():
    x = Router()
    assert isinstance(x,Router)

# Generated at 2022-06-14 07:57:29.855005
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.method_not_allowed == 405
    assert router.not_found == 404

# Generated at 2022-06-14 07:57:41.718785
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert router.router_cache_size == Router.ROUTER_CACHE_SIZE

# Generated at 2022-06-14 07:57:52.543107
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.handlers import ErrorHandler
    from sanic.router import Router as Router_parent
    from sanic.server import HttpProtocol
    from sanic.views import HTTPMethodView
    from sanic.constants import HTTP_METHODS
    from sanic.response import HTTPResponse
    from sanic.exceptions import InvalidUsage, NotFound, ServerError
    from sanic.log import logger
    from sanic.request import Request as SanicRequest

    class Router(Router_parent):
        def finalize(self, *args, **kwargs):
            super().finalize(*args, **kwargs)

    app = Sanic("test_Router_finalize")

    router = Router(app)


# Generated at 2022-06-14 07:58:02.024102
# Unit test for constructor of class Router
def test_Router():
    router = Router("GET", "/", 0)
    assert router.ctx.route_name is None
    assert router.ctx.route_handler is 0
    assert router.ctx.methods == ['GET']
    assert isinstance(router.ctx.app, object)
    assert isinstance(router.ctx.router, object)
    assert isinstance(router.ctx.path, str)
    assert isinstance(router.ctx.host_matches, tuple)
    assert isinstance(router.ctx.host_pattern, str)
    assert isinstance(router.ctx.host_match_dict, dict)


# Generated at 2022-06-14 07:58:09.274328
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    class DummyRoute:
        def __init__(self, labels):
            self.labels = labels
    r.dynamic_routes = { "a": DummyRoute(["a", "__a__"]), "b": DummyRoute(["a"]) }
    try:
        r.finalize()
    except:
        assert False
    assert True

# Generated at 2022-06-14 07:58:15.098361
# Unit test for constructor of class Router
def test_Router():
    class TestClass:
        def __init__(self):
            self.router = Router()
        def test_func(self, request):
            print("hello world")
            return
    obj = TestClass()
    assert isinstance(obj.router, Router)
    assert callable(obj.test_func)
    return

test_Router()


# Generated at 2022-06-14 07:58:21.316612
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    
    @router.view("/", methods=["GET"])
    def get_handler(request):
        return "Hello"

    router.finalize()
    assert router.find_route_by_view_name("get_handler")
    assert not router.find_route_by_view_name("test_handler")

test_Router_finalize()

# Generated at 2022-06-14 07:58:28.154411
# Unit test for method finalize of class Router
def test_Router_finalize():
    # pylint: disable=unexpected-keyword-arg, no-value-for-parameter
    try:
        Router().finalize()
    except SanicException:
        raise SanicException('Invalid route: <Route GET:/>.' +
                             ' Parameter names cannot use __.')

# Generated at 2022-06-14 07:58:30.368571
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ALLOWED_METHODS is HTTP_METHODS

# Generated at 2022-06-14 07:58:36.956607
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = router.add("/", ["GET"], lambda *args, **kwargs: True)
    route.labels.add("__file_uri__")
    route.labels.add("__other_uri__")
    router.finalize()
    assert not router.dynamic_routes


# Generated at 2022-06-14 07:58:40.316550
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 07:59:10.323043
# Unit test for method finalize of class Router
def test_Router_finalize():
    # arrange
    from sanic.response import text

    def bad_route():
        pass

    # act and assert
    try:
        router = Router()
        router.add("/", ("GET", "POST"), bad_route, name="__foo")
        router.finalize()
    except SanicException as e:
        assert e.message == "Invalid route: / (GET, POST) -> bad_route. Parameter names cannot use '__'."
    else:
        assert False, "SanicException was not thrown."


# Generated at 2022-06-14 07:59:15.450193
# Unit test for constructor of class Router
def test_Router():
    router = Router(
            allowed_methods=["GET", "POST", "PUT", "DELETE"],
            strict_slashes=True
        )
    print(router)

if __name__ == '__main__':
    test_Router()

# Generated at 2022-06-14 07:59:17.436079
# Unit test for constructor of class Router
def test_Router():
    router = Router(app=None)
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 07:59:23.732046
# Unit test for method add of class Router
def test_Router_add():
    
    from .sanic import Sanic
    from .request import Request
    from .response import HTTPResponse

    # Test default values
    app = Sanic('test_sanic')
    router = app.router

    @app.route('/test')
    def handler(request):
        return request.uri

    assert isinstance(router.routes_all, dict)
    assert isinstance(router.routes_static, dict)
    assert isinstance(router.routes_dynamic, dict)
    assert isinstance(router.routes_regex, dict)

    # Test handler
    request, response = app.test_client.get('/test')
    assert response.text == '/test'
    assert str(response) == '<Response streamed [200 OK]>'

   

# Generated at 2022-06-14 07:59:25.058712
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 07:59:32.767810
# Unit test for method finalize of class Router
def test_Router_finalize():
    import sanic.router as router
    from sanic.response import HTTPResponse
    from sanic.server import HttpProtocol
    from sanic.app import Sanic
    from sanic.exceptions import SanicException
    from sanic.handlers import ErrorHandler
    app = Sanic()
    app.error_handler = ErrorHandler()
    app.router = router.Router()
    app.error_handler.add(Exception, lambda r,e: HTTPResponse(status=500))
    # Test 1
    try:
        @app.route("/test", methods=["GET"])
        async def test(request):  # pylint: disable=unused-variable
            return HTTPResponse(status=200)
    except SanicException as e:
        e.__str__()

# Generated at 2022-06-14 07:59:39.795569
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import DynamicRoute
    from sanic.router import Router
    from sanic.app import Sanic

    app = Sanic()

    router = Router()

    router.add(DynamicRoute('/{user_id}', 'GET', app.async_handler))

    with pytest.raises(SanicException):
        router.finalize()



# Generated at 2022-06-14 07:59:43.742949
# Unit test for constructor of class Router
def test_Router():
    # Arrange
    router = Router()
    methods_allowed = ["POST", "GET"]

    # Act
    handler = lambda: None
    route = router.add("/test", methods_allowed, handler)

    # Assert
    assert route.labels == ["test"]

# Generated at 2022-06-14 07:59:48.470615
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add("/id/{var}", ["GET"], lambda x: x)
    r.finalize()
    assert r.dynamic_routes is not None


# Generated at 2022-06-14 07:59:51.024355
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-14 08:00:37.336946
# Unit test for constructor of class Router

# Generated at 2022-06-14 08:00:46.336118
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    router.add(
        uri="",
        methods=["GET"],
        handler=lambda *args, **kwargs: None,
        host="",
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name="",
        unquote=False,
        static=False,
    )
    assert router.dynamic_routes.values()

    router.finalize()

# Generated at 2022-06-14 08:00:54.899611
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes_all == {}
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.param_rules == {}
    assert router.name_index == {}
    assert router.ctx.app == None
    assert router.ctx.router == router



# Generated at 2022-06-14 08:00:55.695995
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 08:00:57.869356
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router(None)
    with pytest.raises(SanicException):
        r.finalize()

# Generated at 2022-06-14 08:01:11.292139
# Unit test for method finalize of class Router
def test_Router_finalize():
    from pytest import raises

    from sanic import Sanic
    from sanic import exceptions
    from sanic.router import Router
    from sanic.views import CompositionView

    router = Router()

    def handler():
        pass

    router.add("/test/<parameter>", ["GET"], handler, name="test")

    view = CompositionView()
    view.add(["GET"], "/test/<parameter>", handler)

    router.add(view, strict_slashes=True, name="test_view")
    app = Sanic("test_sanic")
    router.finalize(app, app.error_handler)

    with raises(SanicException) as exc_info:
        router.add("/test/<__parameter>", ["GET"], handler, name="test")


# Generated at 2022-06-14 08:01:18.684214
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    router.finalize()


# Generated at 2022-06-14 08:01:27.413226
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route1 = Route(router, 'GET', '/task/<__task_id>', None, [], None, None, None)
    route2 = Route(router, 'GET', '/task/<task_id>', None, [], None, None, None)
    route3 = Route(router, 'GET', '/task/<__task_id>', None, [], None, None, None)
    route4 = Route(router, 'GET', '/task/<task_id>', None, [], None, None, None)
    route5 = Route(router, 'GET', '/task/<__file_uri__>', None, [], None, None, None)

# Generated at 2022-06-14 08:01:37.004544
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    try:
        r.finalize()
    except SanicException:
        assert False
    else:
        assert True
    try:
        r.dynamic_routes={'a':{}}
        r.finalize()
    except SanicException:
        assert False
    else:
        assert True
    try:
        r.dynamic_routes['a']='a'
        r.finalize()
    except SanicException:
        assert False
    else:
        assert True


# Generated at 2022-06-14 08:01:40.307952
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:03:04.314530
# Unit test for constructor of class Router
def test_Router():
	router = Router()
	uri = '/sanic'
	methods = ['GET']
	def handler(request):
		pass
	strict_slashes = False
	stream = False
	ignore_body = False
	version = None
	name = None
	unquote = False
	static = False
	host = None
	route = router.add(uri,methods,handler,host,strict_slashes,stream,ignore_body,version,name,unquote,static)
	print(route)
	assert not route is None


# Generated at 2022-06-14 08:03:05.957154
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert(isinstance(router, Router))

# Generated at 2022-06-14 08:03:12.915854
# Unit test for constructor of class Router
def test_Router():
    a = Router()
    assert len(a.name_index) == 0
    assert len(a.host_index) == 0
    assert len(a.static_routes) == 0
    assert len(a.dynamic_routes) == 0
    assert len(a.regex_routes) == 0
    assert len(a.routes) == 0

# Generated at 2022-06-14 08:03:14.019349
# Unit test for constructor of class Router
def test_Router():
    assert Router()


# Generated at 2022-06-14 08:03:27.014280
# Unit test for constructor of class Router
def test_Router():
    test = Router()
    assert test.DEFAULT_METHOD == "GET"
    assert test.ALLOWED_METHODS == HTTP_METHODS
    test.add("/test/", ["GET", "POST"], None)
    test.get("/test/", "GET", None)
    test.find_route_by_view_name("None")
    assert test.routes_all == test.routes
    assert test.routes_static == test.static_routes
    assert test.routes_dynamic == test.dynamic_routes
    assert test.routes_regex == test.regex_routes
    test.finalize()

if __name__ == "__main__":
    test_Router()
    print("All tests passed.")

# Generated at 2022-06-14 08:03:28.584427
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 08:03:37.977327
# Unit test for method finalize of class Router
def test_Router_finalize():
    import re
    import pytest
    from sanic.response import json
    from sanic.views import HTTPMethodView

    class MyView(HTTPMethodView):
        def get(self, request):
            return json({"test": True})

        def post(self, request):
            return json({"test": True})

    router = Router()
    router.add(
        re.compile(r'^/api/mymethod/$'),
        host=None,
        handler=None,
        methods=['GET', 'POST'],
        name='my_route',
    )


# Generated at 2022-06-14 08:03:40.439159
# Unit test for constructor of class Router
def test_Router():
    route = Router(None)
    assert isinstance(route, Router)

# Generated at 2022-06-14 08:03:41.232446
# Unit test for constructor of class Router
def test_Router():
    assert Router

# Generated at 2022-06-14 08:03:43.058536
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
