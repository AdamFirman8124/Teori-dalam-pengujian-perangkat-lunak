

# Generated at 2022-06-14 07:55:45.045573
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {
        "/test/<param1>/<param2>:__test": "route1",
        "/test/<param1>/<param2>:__test2": "route2",
        "/test/<param1>/<param2>:__file_uri__": "route3",
        "/test/<param1>/<param2>:__file_uri__2": "route4",
    }

    # This test was moved from test_app.py
    # Exception should not be raised, since the label __file_uri__ is allowed
    router.finalize()
    assert True

# Generated at 2022-06-14 07:55:47.950902
# Unit test for constructor of class Router
def test_Router():
    test = Router()
    assert isinstance(test, Router)

# Unit tests for instance method _get of class Router

# Generated at 2022-06-14 07:55:55.074949
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    # Test get function
    path = "/uri/to"
    method = "POST"
    host = "localhost"
    assert(router.get(path, method, host) == router.get.cache_info())

    # Test add function
    uri = "/uri/to"
    methods = ["GET", "POST", "OPTIONS"]
    handler = "handler"
    router.add(uri, methods, handler)
    assert(router.routes_all == router._router.routes)
    assert(router.routes_static == router._router.static_routes)
    assert(router.routes_dynamic == router._router.dynamic_routes)

# Generated at 2022-06-14 07:56:08.853631
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    uri = "/my_api"
    methods = ["GET", "POST", "OPTIONS"]
    handler = RouteHandler
    host = "haha.com"
    strict_slashes = False
    stream = True
    ignore_body = False
    version = "1.0"
    name = "test"
    unquote = True
    result = router.add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], Route)
    assert result[0].path == uri
    assert result[0].ctx.ignore_body == ignore_body
    assert result[0].ctx.stream == stream

# Generated at 2022-06-14 07:56:19.243695
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router

    # Test when route is invalid
    router = Router()

    @router.get("/profile/<user_id>")
    def handler(request, user_id):
        return text("OK")

    with pytest.raises(SanicException):
        router.finalize()

    # Test when route is valid
    router = Router()

    @router.get("/profile/<user_id>")
    def handler(request, user_id):
        return text("OK")

    router.finalize()

# Generated at 2022-06-14 07:56:20.126910
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert True

# Generated at 2022-06-14 07:56:25.322396
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route(handler=None, path="/users/<name>", method="GET")
    route.labels = ["name"]
    router.routes_dynamic[route.path] = route
    router.finalize()
    assert True


# Generated at 2022-06-14 07:56:28.813369
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {} and router.routes_static == {} and router.routes_dynamic == {} and router.routes_regex == {}


# Generated at 2022-06-14 07:56:32.886826
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 07:56:37.576265
# Unit test for method finalize of class Router
def test_Router_finalize():
    r1 = Router()
    r2 = Router()
    r2.add('/test/<param1>/<param2>', methods=['GET'], handler=None)
    r1.GLOBAL_ROUTERS.append(r2)
    r1.finalize()
    assert True

# Generated at 2022-06-14 07:56:42.046459
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 07:56:43.427366
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 07:56:52.418620
# Unit test for method finalize of class Router
def test_Router_finalize():
    route1 = Route("/<name>", None, None)
    route1.labels = ["name", "__file_uri__"]
    route2 = Route("/<id>", None, None)
    route2.labels = ["id", "__file_uri__"]

    router = Router()
    router.dynamic_routes = {route1: route1, route2:route2}

    try:
        router.finalize()
    except SanicException:
        assert False, "Does not raise SanicException on valid route"

    route3 = Route("/<__filename>", None, None)
    route3.labels = ["__filename", "__file_uri__"]

    router.dynamic_routes[route3] = route3


# Generated at 2022-06-14 07:56:55.274251
# Unit test for constructor of class Router
def test_Router():
    test_router = Router()
    assert test_router.DEFAULT_METHOD == "GET"

# Generated at 2022-06-14 07:57:06.193385
# Unit test for method finalize of class Router
def test_Router_finalize():
    import sanic
    from sanic import Sanic, Blueprint
    from sanic.router import Router, Route
    from sanic.constants import HTTP_METHODS

    app = Sanic("test_Router_finalize")

    test_router = Router()

    for method in HTTP_METHODS:
        test_router.add(uri="/{test_route}", methods=[method], handler=None)

    handler_b = Blueprint("test_Router_finalize_handler_b")

    @handler_b.get("/<test_route>")
    async def handler_b(request):
        return text("handler_b")

    app.blueprint(handler_b)

    handler_c = Blueprint("test_Router_finalize_handler_c")


# Generated at 2022-06-14 07:57:07.889243
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 07:57:17.562076
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        r = Router()
        r.add(
            uri="/user/{__file_uri__}/",
            methods=["GET", "OPTIONS"],
            handler=lambda req, resp: None
        )
        r.finalize()
    except Exception as e:
        assert e.__str__() == "Invalid route: 'GET,OPTIONS /user/{__file_uri__}/'. Parameter names cannot use '__'."


if __name__ == "__main__":
    test_Router_finalize()

# Generated at 2022-06-14 07:57:19.341655
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)

# Generated at 2022-06-14 07:57:26.394416
# Unit test for method finalize of class Router
def test_Router_finalize():
    class MyRouter(Router):
        def finalize(self, *args, **kwargs):
            super().finalize(*args, **kwargs)

        def get(self, path, method, host):
            return self._get(path, method, host)

        def add(self, uri, methods, handler, host=None, strict_slashes=False, stream=False, ignore_body=False, version=None, name=None, unquote=False, static=False): # noqa
            return super().add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static) # noqa

    r = MyRouter()
    r.add("/user/<id>", ["GET"], "handler")

# Generated at 2022-06-14 07:57:29.752639
# Unit test for constructor of class Router
def test_Router():
    obj = Router()
    return

if __name__ == "__main__":
    obj = Router()
    assert isinstance(obj, Router)
    print("Test succ")

# Generated at 2022-06-14 07:57:45.904082
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes["a"] = Route(
        path="/__test_key_name",
        handler=None,
        methods=["GET"],
        name="",
        strict=False,
        unquote=False,
    )
    router.dynamic_routes["b"] = Route(
        path="/__ok_key_name",
        handler=None,
        methods=["GET"],
        name="",
        strict=False,
        unquote=False,
    )
    try:
        router.finalize()
    except SanicException as e:
        assert "Invalid route: /__test_key_name. Parameter names cannot use '__'." in str(e)
        return
    raise Exception("Should raise SanicException")

# Generated at 2022-06-14 07:57:47.836261
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
    except Exception as err:
        assert type(err) == TypeError

# Generated at 2022-06-14 07:57:54.663592
# Unit test for constructor of class Router
def test_Router():
    from sanic.request import Request
    from sanic.response import HTTPResponse

    router = Router()
    router.add(uri="/home", methods=["get", "post"], handler=lambda request, name: HTTPResponse(text="OK"))
    router.add(uri="/home", methods=["put"], handler=lambda request, name: HTTPResponse(text="PUT"))
    # router.add(uri="/", methods=["get"], handler=lambda request, name: HTTPResponse(text="ROOT"))
    # router.add(uri="/home3", methods=["put"], handler=lambda request, name: HTTPResponse(text="PUT3"))
    # router.add(uri="/home4", methods=["put"], handler=lambda request, name: HTTPResponse(text="PUT4"))
   

# Generated at 2022-06-14 07:58:02.340821
# Unit test for constructor of class Router
def test_Router():
    lb = Router(None)
    assert lb.DEFAULT_METHOD == 'GET'
    assert lb.ALLOWED_METHODS == HTTP_METHODS
    assert lb.routes_all == []
    assert lb.routes_static == []
    assert lb.routes_dynamic == {}
    assert lb.static_routes == {}
    assert lb.dynamic_routes == {}
    assert lb.name_index == {}
    assert lb.regex_routes == []
    assert lb.routes_regex == []

# Generated at 2022-06-14 07:58:15.369014
# Unit test for constructor of class Router
def test_Router():
    R = Router()
    assert isinstance(R, BaseRouter)
    assert R.DEFAULT_METHOD == "GET"
    assert R.ALLOWED_METHODS == HTTP_METHODS
    assert R.routes == {}
    assert R.routes_all == {}
    assert R.routes_dynamic == {}
    assert R.routes_regex == {}
    assert R.routes_static == {}
    assert R.name_index == {}
    assert R.static_cache == {}
    assert R.MAX_RECURSION_DEPTH == 20
    assert R.DEFAULT_STATIC_STRATEGY == "file"
    assert R.static_strategy == "file"

# Generated at 2022-06-14 07:58:23.399266
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    uri = 'test_uri'
    methods = HTTP_METHODS
    handler = lambda x: x
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False

    router.add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)


# Generated at 2022-06-14 07:58:36.455349
# Unit test for method finalize of class Router
def test_Router_finalize():
    '''
    Test method finalize of class Router
    '''
    uri = "/"
    methods = ["POST", "GET", "OPTIONS"]
    def handler():
        return uri, methods
    route = Route(uri=uri, methods=methods, handler=handler, strict=True, unquote=False)
    test_routes = {uri: route}
    test_router = Router()
    test_router.routes = test_routes
    test_router.dynamic_routes = test_routes
    test_router._name_index["/"] = route
    test_router.finalize()
    assert test_router.app is not None
    assert test_router.ctx is not None


# Generated at 2022-06-14 07:58:41.129237
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    handler = lambda request: None
    route = router.add('/user/{name}', ['GET'], handler)
    assert not route.labels

# Unit test finalize method of class Router

# Generated at 2022-06-14 07:58:44.385842
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.resolver.cache_size == ROUTER_CACHE_SIZE



# Generated at 2022-06-14 07:58:56.607934
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic
    from sanic import response
    from sanic_routing import Route

    # Test constructor of class Router
    app = Sanic('test_Router')
    router = Router(app)

    @app.route('/')
    async def handler(request):
        return response.text('Hello world!')

    route = router.routes_all['/']

    assert type(route) == Route
    assert route.methods == {'GET'}
    assert route.path == '/'
    assert str(route) == '<Route GET / >'
    assert route.strict == False
    assert route.name == 'root'
    assert route.ctx.ignore_body == False
    assert route.ctx.stream == False
    assert route.ctx.hosts == [None]

# Generated at 2022-06-14 07:59:03.827553
# Unit test for constructor of class Router
def test_Router():
    r1 = Router()
    assert r1.ctx.app == 'Sanic'
    assert r1.ctx.router == 'Router'


# Generated at 2022-06-14 07:59:05.185967
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 07:59:09.074970
# Unit test for method finalize of class Router
def test_Router_finalize():
    class MockRouter(Router):
        def __init__(self):
            self.dynamic_routes = {"test": "test"}

    r = MockRouter()
    r.finalize()
        

# Generated at 2022-06-14 07:59:10.759019
# Unit test for constructor of class Router
def test_Router():
    assert Router() is not None, "Router constructor fails!"

# Generated at 2022-06-14 07:59:24.254075
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_openapi import doc
    from sanic_plugins import SanicPlugins

    @doc.group("Test", tags=["Test"], description="Test")
    class TestDoc:
        pass

    class Test:
        pass
    Test.plugins = SanicPlugins()

    @Test.plugins.plugin("plugin_test")
    class PluginTest:
        def register(self, app):
            raise Exception("test")

    Test.plugins.register("plugin_test")

    try:
        Test.router.finalize()
    except SanicException as e:
        assert str(e) == "Invalid route: /<__file_uri__:path> -> test. Plugin routes cannot use '__'."
    else:
        assert False




# Generated at 2022-06-14 07:59:28.560140
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add(uri=r'/test/<num:int>', methods=['GET','POST'], handler=None)
    router.add(uri=r'/test/<num>', methods=['GET','POST'], handler=None)



# Generated at 2022-06-14 07:59:29.839317
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 07:59:37.108618
# Unit test for method finalize of class Router
def test_Router_finalize():
    def test_function(arg1, arg2):
        return arg1+arg2
    router = Router()
    route = router.add("/test", "GET", test_function, name="test_route")
    assert router.finalize(route) == None
    print("testing for method finalize of class Router: pass")



# Generated at 2022-06-14 07:59:45.423800
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    If a route is invalid (label starts with '__') an exception is raised.
    """
    router = Router()
    route = Route()
    route.uri = "/test"
    route.labels = ["__test"]
    router.dynamic_routes[0] = route
    with pytest.raises(SanicException):
        try:
            router.finalize()
        except Exception as e:
            assert str(e) == "Invalid route: Route(uri='/test',labels=['__test']). Parameter names cannot use '__'."
            raise

# Generated at 2022-06-14 07:59:52.244720
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic
    from sanic.response import text
    app = Sanic(__name__)

    @app.route('/test')
    async def handler(request):
        return text('I am a test')

    app.run(host="0.0.0.0", port=8000, debug=True)

# Generated at 2022-06-14 08:00:07.634606
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    import pytest

    router = Router(Sanic("test_app"))
    decorator = router.add(uri="/", methods=["GET"], handler=None)
    router.add(uri="/users/<username>", methods=["GET"], handler=None)
    router.add(
        uri="/files/<path:path>", methods=["GET"], handler=None, name="files"
    )
    router.add(
        uri="/files/<path:path>" "/<filename>",
        methods=["GET"],
        handler=None,
        name="file",
    )

    router.dynamic_routes = {0: decorator}
    router.static_routes = {0: decorator}


# Generated at 2022-06-14 08:00:12.800520
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException) as ex:
        router.finalize()
    assert (
        "Invalid route: /{variable}/test12. Parameter names cannot use '__'." 
        in str(ex.value)
    )

# Generated at 2022-06-14 08:00:15.592124
# Unit test for constructor of class Router
def test_Router():
    # Test 1
    router = Router()
    router.get('/abc')
    router.get('/abc')
    return router

# Generated at 2022-06-14 08:00:17.447567
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 08:00:30.930271
# Unit test for method finalize of class Router
def test_Router_finalize():
    # add_route calls finalize
    # add_route calls finalize
    # add_route calls finalize
    # add_route calls finalize
    # add_route calls finalize
    from ..test_helpers import Sanic
    from . import Router
    from . import add_route

    sanic_app = Sanic("sanic-router")
    router = Router()

    def f():
        pass

    add_route(router, "/", f)
    add_route(router, "/<param>", f)
    add_route(router, "/(param)", f)
    add_route(router, "/<param>/<param2>", f)
    add_route(router, "/folder/<param>/<param2>", f)

# Generated at 2022-06-14 08:00:44.967489
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    from sanic.router import Route
    app = Sanic(__name__)

    # When route with invalid labels is created the finalize method of class
    # Router raises the SanicException
    route_string = "/user/<id>"
    route_method = "GET"
    route_handler = None
    route = Route(
        app=app,
        uri=route_string,
        methods={route_method},
        handler=route_handler,
    )
    # Add the labels to the route
    route.labels = ["__file_uri__","__dir_path__","__file_path__"]
    # Set the route for the app
    app.router.add(route)
    # Finalize the app

# Generated at 2022-06-14 08:00:57.139916
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    import json
    import pytest
    import sanic_routing

    app = Sanic("test_app")
    
    async def handler(request: Request, test_arg: str) -> HTTPResponse:
        return HTTPResponse(json.dumps({"test_arg": test_arg}), status=200)

    router_test_1 = sanic_routing.Router(app)
    router_test_1.add(uri="handler_test/<test_arg:string>", methods=["GET"], handler=handler)

    router_test_2 = sanic_routing.Router(app)

# Generated at 2022-06-14 08:01:01.332563
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException) as e:
        router.finalize()
    assert e.value.args[0] == "Invalid route:  / . Parameter names cannot use '__'."

# Generated at 2022-06-14 08:01:04.094520
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router and isinstance(router, Router)

# Generated at 2022-06-14 08:01:05.521973
# Unit test for constructor of class Router
def test_Router():
    route = Router()
    assert route.route_pattern == "/"
    assert route.parent is None
    assert not route.ctx

# Generated at 2022-06-14 08:01:16.085055
# Unit test for constructor of class Router
def test_Router():
    router = Router()


if __name__ == "__main__":
    import sys
    import pytest

    pytest.main(["-s"] + sys.argv[1:])

# Generated at 2022-06-14 08:01:29.401966
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.views import HTTPMethodView

    def _sanic_app():
        sanic_app = Sanic(__name__)
        sanic_app.router = Router(sanic_app)
        from sanic.server import HttpProtocol
        from sanic.server import serve
        sanic_app.serve = serve
        sanic_app.is_request_stream = HttpProtocol.is_request_stream
        sanic_app.handle_request = HttpProtocol.handle_request
        return sanic_app

    app = _sanic_app()


# Generated at 2022-06-14 08:01:30.375511
# Unit test for constructor of class Router
def test_Router():
    assert Router().routes_all == {}

# Generated at 2022-06-14 08:01:42.607960
# Unit test for method finalize of class Router
def test_Router_finalize():

    # Allowed dynamic route
    route = Route('/test/<param>', None, None, '__file_uri__')
    result = Router()._Router__validate_dynamic_route(route)
    assert result

    # Dynamic route with forbidden labels
    route = Route('/test/<__test>', None, None, '__file_uri__')
    result = Router()._Router__validate_dynamic_route(route)
    assert isinstance(result, SanicException)

    # Forbiden dynamic route
    dynamic_routes = {"dynamic_route": Route('/test/<param>', None, None, None)}
    router = Router()
    router.dynamic_routes = dynamic_routes
    with pytest.raises(SanicException) as error:
        router.final

# Generated at 2022-06-14 08:01:43.216225
# Unit test for constructor of class Router
def test_Router():
    test = Router()

# Generated at 2022-06-14 08:01:44.563359
# Unit test for method finalize of class Router
def test_Router_finalize():
    object = Router(None)
    object.finalize()

# Generated at 2022-06-14 08:01:50.204054
# Unit test for method finalize of class Router
def test_Router_finalize():
    def test_handler(request):
        return ""
    test_router = Router()
    try:
        test_router.add("/test", "GET", test_handler)
    except SanicException:
        pass
    else:
        assert True == False


# Generated at 2022-06-14 08:01:51.054722
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 08:01:58.214643
# Unit test for constructor of class Router
def test_Router():
    # Instance of class Router
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 08:02:00.305282
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), BaseRouter)


# Generated at 2022-06-14 08:02:08.663040
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    

# Generated at 2022-06-14 08:02:11.031418
# Unit test for method finalize of class Router
def test_Router_finalize():
    # missing label __file_uri__
    with pytest.raises(SanicException):
        route = Route()
        route.labels = ["__file_uri"]
        route.finalize()

# Generated at 2022-06-14 08:02:20.596531
# Unit test for constructor of class Router

# Generated at 2022-06-14 08:02:22.346265
# Unit test for constructor of class Router
def test_Router():
    assert Router(param="router").param == "router"

# Generated at 2022-06-14 08:02:26.033607
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    # check that paths has been initialized
    assert router.paths == []
    # check that routes has been initialized
    assert router.routes == []

# Generated at 2022-06-14 08:02:36.727808
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing import Router as MockRouter
    from sanic_routing.exceptions import SanicRoutingException as MockSanicRoutingException

    def mock_finalize(*args, **kwargs):
        pass

    # Case: invalid route
    mock_router = MockRouter()
    mock_router.dynamic_routes["/user/<name:__foo__>"] = "mock"
    try:
        mock_router.finalize()
    except MockSanicRoutingException as e:
        assert str(e) == (
            "Invalid route: /user/<name:__foo__>. Parameter names "
            "cannot use '__'."
        )

    # Case: valid route
    MockRouter.finalize = mock_finalize
    mock_router = MockRouter

# Generated at 2022-06-14 08:02:44.058563
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    def handler(): pass

    try:
        router.add("/handlers", ["GET", "POST"], handler)
        assert False, 'Should raise Exception'
    except SanicException as e:
        assert str(e) == "Invalid route: /handlers. Parameter names cannot use '__'."


# Generated at 2022-06-14 08:02:47.000790
# Unit test for constructor of class Router
def test_Router():
    router=Router()
    if router:
        print("Success")
    else:
        print("Failed")



# Generated at 2022-06-14 08:02:52.121357
# Unit test for constructor of class Router
def test_Router():
    from sanic.server import HttpProtocol
    from sanic.router import Router
    from sanic import Sanic
    app = Sanic("myapp")
    http_protocol = HttpProtocol(app, None)
    assert isinstance(http_protocol.router, Router)

# Generated at 2022-06-14 08:02:53.969678
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 08:03:11.169109
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert isinstance(router, Router)
    assert router.ctx is None
    assert not router.routes

# Generated at 2022-06-14 08:03:19.330625
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    method = "POST"
    path = "test"
    handler = None
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False
    router.add(path, method, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)
    router.get(path, method, host)
    router.find_route_by_view_name(view_name=None)
    router.finalize(args, kwargs)

# Generated at 2022-06-14 08:03:32.592803
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

# Generated at 2022-06-14 08:03:39.920619
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.constants import HTTP_METHODS

    class TestRouter(Router):
        def __init__(self):
            super().__init__()

# Generated at 2022-06-14 08:03:42.938748
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ROUTER_CACHE_SIZE == 1024
    assert r.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:03:46.725737
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == 'GET'
    assert r.ALLOWED_METHODS == HTTP_METHODS
    assert r.DEFAULT_MATCHING == "simple"

# Generated at 2022-06-14 08:03:49.696257
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.add(uri="/articles/{category}/{article}")



# Generated at 2022-06-14 08:03:56.412012
# Unit test for method finalize of class Router
def test_Router_finalize():
    with pytest.raises(SanicException) as error:
        router = Router()
        router._add(
            uri="/a/<__bad_uri_label>/b/<c>",
            methods=["GET"],
            handler=None,
            name=None
        )
        router.finalize()

    assert "use '__'" in str(error.value)



# Generated at 2022-06-14 08:04:08.254265
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Preparing mock data
    uri = "/"
    methods = ["GET"]
    handler = lambda x: x
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False

    route = Route(methods, uri, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)

    # Creating a new mock object
    dynamic_routes = {"test": route}
    return_value = (route, route.handler, {})
    mock_get = MagicMock(return_value=return_value)
    mock_add = MagicMock()

    # Replacing method get with mock object
    Router.get = mock_get

    # Replacing method

# Generated at 2022-06-14 08:04:19.585634
# Unit test for method finalize of class Router
def test_Router_finalize():
    rtr = Router()

    with pytest.raises(SanicException) as exc:
        rtr.add(
            uri="/test_me/<__test_label>",
            methods=["GET"],
            handler=None,
            host=None,
            strict_slashes=False,
            stream=False,
            ignore_body=False,
            version=None,
            name="test_name",
            unquote=False,
            static=False,
        )
        rtr.finalize()

    assert str(exc.value) == "Invalid route: [GET /test_me/<__test_label>] -> None. Parameter names cannot use '__'."

# Generated at 2022-06-14 08:04:35.017129
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.app is None
    assert router.ctx.groups == []
    assert router.ctx.route == ""
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:04:38.710956
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
        assert router is not None
    except Exception as e:
        assert False, "Failed to instantiate class Router. Error = {}".format(e)


# Generated at 2022-06-14 08:04:40.696090
# Unit test for constructor of class Router
def test_Router():
    assert Router().get_name() == 'Router'

# Generated at 2022-06-14 08:04:52.727141
# Unit test for method add of class Router
def test_Router_add():
    uri = '/uri'
    methods = ['GET', 'POST']
    handler = "a"
    host = "b"
    strict_slashes = False
    stream = False
    ignore_body = False
    version = 2
    name = None
    unquote = False
    static = False
    router = Router()

    router.add(
        uri=uri,
        methods=methods,
        handler=handler,
        host=host,
        strict_slashes=strict_slashes,
        stream=stream,
        ignore_body=ignore_body,
        version=version,
        name=name,
        unquote=unquote,
        static=static,
    )


# Generated at 2022-06-14 08:04:54.751736
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r  # If r is not None, test passes.


# Generated at 2022-06-14 08:04:55.782469
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r is not None

# Generated at 2022-06-14 08:05:00.228140
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import SanicException 
    from sanic import response

    app = sanic.Sanic("test_sanic_App")
    
    @app.route("/")
    def test(request):
        return response.text("OK")
    
    # Checking for testing purpose
    app.config.from_object(__name__)
    app.config["TESTING"] = True

    router = app.router
    try:
        router.finalize()
    except Exception:
        assert isinstance(SanicException, type)
    assert router.app is app

# Generated at 2022-06-14 08:05:06.688217
# Unit test for constructor of class Router
def test_Router():
    # setup test
    testInput = "test"
    router = Router()
    assert router.ctx == None
    assert router.index == {}
    assert router.name_index == {}
    assert router.routes == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}



# Generated at 2022-06-14 08:05:10.536466
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.name_index == {}


# Generated at 2022-06-14 08:05:16.211517
# Unit test for method finalize of class Router
def test_Router_finalize():

    r = Route('/', RouteHandler, ('GET', ), None, '/', [''], True, None, '')
    r.labels.append('__file_uri__')
    r.labels.append('__something_else__')
    routes = {'/': r}
    rt = Router(routes, None)
    rt.finalize()