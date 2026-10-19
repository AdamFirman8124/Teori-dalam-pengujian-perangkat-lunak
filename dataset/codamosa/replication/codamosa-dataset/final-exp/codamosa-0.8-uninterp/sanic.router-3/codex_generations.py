

# Generated at 2022-06-14 07:55:32.052238
# Unit test for constructor of class Router
def test_Router():
    print("Unit test for constructor of class Router...")
    obj = Router()
    assert isinstance(obj, Router)


# Generated at 2022-06-14 07:55:43.667734
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.config import Config

    path = "/test/path"
    handler = "foobar"
    method = ["FOO", "BAR"]
    strict_slashes = True
    name = "foobar"
    hosts = ["foo", "bar"]
    version = "1"
    router = Router(Config())
    router.add(
        uri=path,
        methods=method,
        handler=handler,
        host=hosts,
        strict_slashes=strict_slashes,
        name=name,
        version=version
    )

    assert len(router.routes_all) == 2
    assert len(router.routes_static) == 2
    assert len(router.routes_dynamic) == 0

# Generated at 2022-06-14 07:55:52.690293
# Unit test for method finalize of class Router
def test_Router_finalize():
    from unittest.mock import MagicMock
    from logging import Logger
    from sanic.exceptions import RouteExists
    from sanic.router import Route, Router
    from sanic.constants import HTTP_METHODS

    def throw_exception():
        raise RouteExists('RouteExists')

    def test_method(router:Router, method: str):
        res_dynamic = router.dynamic_routes
        res_name_index = router.name_index
        res_static = router.static_routes

        setattr(router, "dynamic_routes", MagicMock())
        setattr(router, "name_index", MagicMock())
        setattr(router, "static_routes", MagicMock())

        router.dynamic_routes

# Generated at 2022-06-14 07:56:00.268401
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.name_index == {}
    assert router.patterns == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert type(router.dynamic_routes) == dict
    assert type(router.static_routes) == dict


# Generated at 2022-06-14 07:56:05.282571
# Unit test for method finalize of class Router
def test_Router_finalize():
    x = Router()
    x.add('/', ['GET'], lambda *args, **kwargs: True, strict_slashes=True, unquote='index.html', name='index', url_kwargs={})
    x.finalize()


# Generated at 2022-06-14 07:56:09.835807
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    import sys

    # setup
    router = Router()

    # exercise
    try:
        router.finalize()
    except SanicException:
        # verify
        assert True
    else:
        # verify
        assert False, "Should throw SanicException"

# Generated at 2022-06-14 07:56:12.791737
# Unit test for constructor of class Router
def test_Router():
    Router()

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 07:56:17.985623
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {
        "test": Route(handler=None, path="a/b/c/d", labels={'__file_uri__': 'e/f'}),
    }

    if len(router.dynamic_routes) == 1:
        test_result = True
    else:
        test_result = False

    assert test_result

# Generated at 2022-06-14 07:56:21.360324
# Unit test for constructor of class Router
def test_Router():
    try:
        x = Router(BaseRouter)
        assert isinstance(x, Router)
    except:
        assert False

# Generated at 2022-06-14 07:56:30.245650
# Unit test for method finalize of class Router
def test_Router_finalize():
    a = Router()
    a.add(
        uri="/",
        methods=["GET"],
        handler=None,
        host=None,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=False,
        static=False,
    )
    a.finalize()

# Generated at 2022-06-14 07:56:43.025999
# Unit test for method finalize of class Router
def test_Router_finalize():
    import inspect
    import sys
    import pytest
    
    # Collect all the functions that were defined in the module
    module_functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    # Collect the function names
    module_function_names = [m[0] for m in module_functions]
    # Collect the function objects
    module_functions = [m[1] for m in module_functions]
    # Collect the test functions
    test_functions = [m for m in module_functions if m.__name__.startswith("test_")]
    
    if test_functions:
        # Execute each test function
        for test_function in test_functions:
            test_function()
    else:
        print("No test functions were found in the module.")

# Generated at 2022-06-14 07:56:43.977642
# Unit test for constructor of class Router
def test_Router():
    assert Router.__doc__


# Generated at 2022-06-14 07:56:46.814839
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add('/test', ['GET'], lambda: "Hello World!")
    router.finalize()

# Generated at 2022-06-14 07:56:59.624672
# Unit test for method add of class Router
def test_Router_add():
    from sanic.app import Sanic
    from sanic.exceptions import MethodNotSupported
    from sanic.handlers import ErrorHandler
    from sanic.request import Request
    from sanic.response import BaseHTTPResponse
    from sanic.views import CompositionView

    app = Sanic()

    async def handler(*args, **kwargs):
        pass

    @app.route("/test")
    def handler2(*args, **kwargs):
        pass

    method = "GET"
    host = None
    strict_slashes = False
    stream = False
    name = None
    unquote = False
    static = False
    router = Router()

    # Router.DEFAULT_METHOD = "GET"
    # Router.ALLOWED_METHODS = HTTP_METHODS
    ## Test case: uri=None

# Generated at 2022-06-14 07:57:01.037361
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 07:57:02.192429
# Unit test for constructor of class Router
def test_Router():
    pass


# Generated at 2022-06-14 07:57:14.728938
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Test 1
    def f():
        pass

    r = Router()
    r.add('/', ['GET'], f)
    r.add('/<name>/<id>', ['GET'], f)

    try:
        r.add('/', ['GET'], f, name='test')
        assert False, 'No exception was raised'
    except SanicException:
        pass

    # Test 2
    try:
        r.add('/', ['GET'], f, name='_test')
        assert False, 'No exception was raised'
    except SanicException:
        pass

    # Test 3
    try:
        r.add('/', ['GET'], f, name='__test')
    except SanicException:
        assert False, 'SanicException was raised'


# Generated at 2022-06-14 07:57:21.030484
# Unit test for method finalize of class Router
def test_Router_finalize():
	from sanic.app import Sanic
	from sanic.config import Config
	from pytest import raises
	app = Sanic("test_Router_finalize")
	config = Config()
	config.KEEP_ALIVE = False
	router = Router(app, config=config)
	router.finalize()

# Generated at 2022-06-14 07:57:30.006133
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}

# Generated at 2022-06-14 07:57:36.609251
# Unit test for method finalize of class Router
def test_Router_finalize():
    with pytest.raises(SanicException, match="Invalid route"):
        router = Router()
        route = Route(r'/user', 'GET', handler=None)
        route.labels = ['__file_uri__', '__some_label__']
        router.dynamic_routes[route.path] = route
        router.finalize()

# Generated at 2022-06-14 07:57:51.727250
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.models.route import Route

    # test the case when all labels of route could be pass the judgement
    def test_pass():
        def handler(request, *args, **kwargs):
            pass
        router = Router()
        route = Route(uri="/1", methods=["GET"], handler=handler, name="name")
        router.dynamic_routes[route.name] = route
        router.finalize()
        assert len(router.dynamic_routes) == 1
    
    test_pass()

    # test the case when labels of route have a label which value is "__something__"
    def test_failed():
        def handler(request, *args, **kwargs):
            pass
        router = Router()

# Generated at 2022-06-14 07:58:01.713947
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    route = Route(uri="/hello/<name>", methods=["GET"], handler=None)
    route.labels = ["__file_uri__", "__yo_yo__", "some_label"]
    r.dynamic_routes["/hello/<name>"] = route
    with pytest.raises(Exception):
        r.finalize()
    route.labels = ["__file_uri__", "some_label"]
    r.finalize()
    assert r.routes_dynamic == r.dynamic_routes
    assert r.routes_regex == r.regex_routes
    assert r.routes_static == r.static_routes
    assert r.routes_all == r.routes


# Generated at 2022-06-14 07:58:14.879921
# Unit test for constructor of class Router
def test_Router():
    uri = "/test"
    methods = ["GET", "POST"]
    handler = RouteHandler
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False
    router = Router()
    router.add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)
    assert router.get(uri, methods[0], uri)
    assert router.find_route_by_view_name(uri)
    assert router.routes_all
    assert router.routes_static
    assert router.routes_dynamic
    assert router.routes_regex

# Generated at 2022-06-14 07:58:17.421218
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ctx.app is None
    assert r.ctx.router is r


# Generated at 2022-06-14 07:58:19.204900
# Unit test for constructor of class Router
def test_Router():
    r=Router()

    assert r is not None

# Generated at 2022-06-14 07:58:32.325167
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)
    assert isinstance(r, BaseRouter)
    assert r.ctx.app is None
    assert r.ctx.router is r
    assert r.ctx.host is None
    assert r.ctx.host_re is None
    assert r.ctx.host_re_check is None
    assert r.ctx.prefix is None
    assert r.ctx.prefix_re is None
    assert r.ctx.prefix_re_check is None
    assert r.ctx.param_names == {}
    assert r.ctx.url_format is None
    assert r.ctx.url_formats == {}
    assert r.ctx.static_files is False
    assert r.ctx.static_files_extensions is False



# Generated at 2022-06-14 07:58:42.427574
# Unit test for method add of class Router
def test_Router_add():
    # From main.py of sanic-admin
    @app.listener("before_server_start")
    def register_router(app, loop):
        router = app.router
        app.admin = SanicAdmin(app, router, name="admin", url_prefix="/admin")
        router.add(
            app.admin.url_prefix + "/<path:path>",
            methods=["GET", "HEAD", "POST", "DELETE", "PUT", "PATCH", "OPTIONS"],
            host=app.config.ADMIN_URL_HOST,
            handler=app.admin.handle_request,
        )
    
    # From app.py of sanic-admin

# Generated at 2022-06-14 07:58:45.518144
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert(r.DEFAULT_METHOD == "GET")
    assert(r.ALLOWED_METHODS == HTTP_METHODS)

# Generated at 2022-06-14 07:58:48.161354
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    # assert isinstance(router, Router)



# Generated at 2022-06-14 07:58:58.779256
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic.models.handler_types import RouteHandler
    from sanic.exceptions import SanicException
    from sanic_routing import Route as Route
    from sanic_routing.router import Router

    def func():
        pass

    def func1():
        pass

    def func2(a: int):
        pass
    
    def func3(a: int, b: str):
        pass
    
    def func4(a: int, b: str, c: float):
        pass

    def test_assert1():
        router = Router()
        router.add("/string/{a}", ["GET"], func1, unquote=True)
        router.add(r"/regex/{b:\d+}", ["GET"], func2, unquote=True)

# Generated at 2022-06-14 07:59:15.557658
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.routes_all == {}
    assert r.routes_static == {}
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}
    assert r.name_index == {}
    assert r.ctx is None
    assert r.origins is None
    assert r.middlewares is None
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 07:59:17.269298
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD is not None
    assert router.ALLOWED_METHODS is not None

# Generated at 2022-06-14 07:59:18.359520
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx == {"app": None}

# Generated at 2022-06-14 07:59:23.631600
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)
    assert isinstance(Router.get(Router(), "path", "method", "host"), tuple)
    assert isinstance(Router().add("uri", "methods", "handler"), list)
    assert isinstance(Router().find_route_by_view_name("view_name"), tuple)
    assert isinstance(Router().routes_all, dict)
    assert isinstance(Router().routes_static, dict)
    assert isinstance(Router().routes_dynamic, dict)
    assert isinstance(Router().routes_regex, dict)
    assert isinstance(Router().finalize(), None)

# Generated at 2022-06-14 07:59:27.213649
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router), "r is a instance of class Router"
    assert isinstance(r, BaseRouter), "r is a subclass of BaseRouter"


# Generated at 2022-06-14 07:59:32.094371
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    ALLOWED_LABELS = ("__file_uri__",)
    
    @router.get('/test')
    def test(request, **kwargs):
        return request

    router.finalize()

    assert router.routes_dynamic["test"].labels == ["__file_uri__"]


# Generated at 2022-06-14 07:59:44.674104
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    Unit test for finalize method of class Router
    """

# Generated at 2022-06-14 07:59:53.840258
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.routing import Router as RouterClass
    class MockRouter(RouterClass):
        def __init__ (self, *args) :
            self.dynamic_routes = {'a': 'a'}
    mock_router = MockRouter()
    with pytest.raises(Exception) as ex:
        mock_router.finalize()
    assert str(ex.value) == 'Invalid route: a. Parameter names cannot use \'__\'.'

# Generated at 2022-06-14 07:59:57.674602
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router
    assert router.routes_all
    assert router.routes_static
    assert router.routes_dynamic
    assert router.routes_regex



# Generated at 2022-06-14 08:00:02.097674
# Unit test for constructor of class Router
def test_Router():
    ctx = {'app': 12345}

    r = Router(ctx=ctx)
    assert r.ctx == ctx

    with pytest.raises(Exception) as e:
        r = Router()
    assert "ctx" in str(e.value)


# Generated at 2022-06-14 08:00:26.158178
# Unit test for constructor of class Router
def test_Router():
  router = Router()
  assert router
  assert len(router.routes_all) == 0
  assert len(router.routes_static) == 0
  assert len(router.routes_dynamic) == 0
  assert len(router.routes_regex) == 0
  assert not router.finalized
  assert router.ctx.hosts == ["*"]
  assert router.ctx.host_matcher == re.compile("^\\*$")
  assert not router.ctx.get("hosts")
  assert not router.ctx.get("host_matcher")

# Generated at 2022-06-14 08:00:28.478503
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.is_request_stream is False


# Generated at 2022-06-14 08:00:38.438051
# Unit test for constructor of class Router
def test_Router():
    class SanicRouter(Router):
        pass
    router = SanicRouter()
    assert isinstance(router, SanicRouter)
    assert isinstance(router.ctx, SanicRouter.ctx.__class__)
    assert isinstance(router.resolver, SanicRouter.resolver.__class__)
    assert isinstance(router.routes, SanicRouter.routes.__class__)
    assert isinstance(router.static_routes, SanicRouter.static_routes.__class__)
    assert isinstance(router.dynamic_routes, SanicRouter.dynamic_routes.__class__)

# Generated at 2022-06-14 08:00:49.680425
# Unit test for method finalize of class Router
def test_Router_finalize():
    uri = "/"
    route = Route(
        method='POST',
        handler=lambda route: "ok",
        path_params=None,
        path=uri,
        name=None,
        path_regex=uri,
        path_tokens=None,
        strict=False,
        unquote=False,
        registers=None,
        host=None,
        requirements=None,
        ctx=None,
    )
    router = Router()
    try:
        router.dynamic_routes = {0: route}
        router.finalize()
    except SanicException as e:
        assert "Parameter names cannot use '__'" in str(e)

# Generated at 2022-06-14 08:01:02.312411
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    Test case for method finalize of class Router.
    """
    # Test case when a parameter in the dynamic_routes is not allowed
    # Input:
    #   route_str:   '<__file_uri__:[^/]+>/'
    #   labels:      ('__file_uri__',)
    #   route_len:   2
    #   label:       '__file_uri__'
    # Expected output:
    # No error occurs
    route_str = '<__file_uri__:[^/]+>/'
    labels = ('__file_uri__',)
    route = Route(route_str, labels)
    router = Router()
    router.add_route(route)
    router.finalize()

    # Test case when a parameter in the dynamic_routes is not

# Generated at 2022-06-14 08:01:12.989414
# Unit test for constructor of class Router
def test_Router():
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.views import CompositionView

    app = Application()

    @app.route("/")
    def handler(request):
        return request

    app.router.add(
        uri="url",
        methods=['GET'],
        handler=handler,
        host=None,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=True,
        static=True,
    )

    request, response = app.test_client.get("/")  # type: ignore
    assert request
    assert isinstance(response, HTTPResponse)


# Generated at 2022-06-14 08:01:17.429330
# Unit test for constructor of class Router
def test_Router():
    """
    A test for the constructors of Router class
    """
    router = Router()
    assert router.DEFAULT_METHOD == "GET", "Unexpected default method"
    assert router.ALLOWED_METHODS == HTTP_METHODS, "Unexpected allowed methods"


# Generated at 2022-06-14 08:01:18.990099
# Unit test for constructor of class Router
def test_Router():
    url_router = Router
    assert isinstance(url_router, type)

# Generated at 2022-06-14 08:01:25.567808
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.exceptions import NotFound
    @Router.get('/')
    def handler(request):
        return request.args

    router = Router()
    router.add(uri='/', methods=["GET"], handler=handler)
    router.finalize()
    result = router.get('/', 'GET', None)
    assert len(result) == 3
    assert result[0].uri == '/'
    assert result[1](None, None) == {}

# Generated at 2022-06-14 08:01:39.073384
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(app=None)
    route = Route(
        path="/test/<param>",
        methods=["GET"],
        handler=None,
        name=None,
        strict=True,
    )
    route.ctx = Route.Context()
    router.dynamic_routes["/test/<param>"] = route

    try:
        router.finalize()
    except SanicException:
        assert True
    else:
        assert False

    router.dynamic_routes["/test/<param>"] = Route(
        path="/test/<param>",
        methods=["GET"],
        handler=None,
        name=None,
        strict=True,
    )

    try:
        router.finalize()
    except SanicException:
        assert False


# Unit test

# Generated at 2022-06-14 08:02:01.214811
# Unit test for constructor of class Router
def test_Router():
    builder = Router()
    assert isinstance(builder, Router)
    assert builder.DEFAULT_METHOD == 'GET'
    assert builder.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 08:02:02.628083
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router != None

# Generated at 2022-06-14 08:02:14.670022
# Unit test for method finalize of class Router
def test_Router_finalize():
    mock_args = []
    mock_kwargs = {}

    route = Route(
        path="/",
        handler=None,
        methods={},
        name=None,
        strict=False,
        unquote=False,
    )
    route.labels = ["__file_uri__"]

    router = Router()
    router.ctx = type("Context", (), {})
    router.ctx.app = type("App", (), {"_generate_name": lambda route: ""})

    router.dynamic_routes = {None: route}

    try:
        router.finalize(*mock_args, **mock_kwargs)
    except:
        assert False

# Generated at 2022-06-14 08:02:19.321444
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    class TestRoute:
        pass
    TestRoute.labels = ["__file_uri__"]
    assert router.finalize(TestRoute) is None

    class TestRoute:
        pass
    TestRoute.labels = ["__test"]
    with pytest.raises(SanicException):
        router.finalize(TestRoute)

# Generated at 2022-06-14 08:02:29.316970
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router._get is None
    assert router.DEFAULT_METHOD == "GET"
    assert router.get is None
    assert router.add is None
    assert router.find_route_by_view_name is None
    assert router.routes_all is None
    assert router.routes_static is None
    assert router.routes_dynamic is None
    assert router.routes_regex is None
    assert router.finalize is None
    return router

# Generated at 2022-06-14 08:02:30.468873
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 08:02:38.598562
# Unit test for constructor of class Router
def test_Router():
    from functools import partial
    from typing import Callable
    from sanic.request import Request
    from sanic.response import HTTPResponse, text
    from sanic.views import CompositionView

    async def _(request: Request) -> HTTPResponse:
        pass

    @lru_cache(maxsize=ROUTER_CACHE_SIZE)
    def _get(
        self, path: str, method: str, host: Optional[str]
    ) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
        try:
            return self.resolve(
                path=path,
                method=method,
                extra={"host": host},
            )
        except RoutingNotFound as e:
            raise NotFound("Requested URL {} not found".format(e.path))

# Generated at 2022-06-14 08:02:44.740214
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ["DELETE", "GET", "HEAD", "OPTIONS",
                                      "PATCH", "POST", "PUT"]


# Generated at 2022-06-14 08:02:46.056674
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 08:02:51.808974
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add('/test', ["GET"], None)
    # Normal case
    r.finalize()
    
    # ValueError case
    for route in r.dynamic_routes.values():
        route.labels = ['__test__', '__file_uri__']
    r.finalize()

# Generated at 2022-06-14 08:03:31.190119
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.get('/', 'GET')
    assert router


# Generated at 2022-06-14 08:03:36.692726
# Unit test for constructor of class Router
def test_Router():
    class TestRouter(Router):
        pass

    router = TestRouter()
    assert router.routes == []
    assert router.routes_all == []
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == []

# Generated at 2022-06-14 08:03:48.648813
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import SanicException
    from sanic_routing.router import Route

    class RouteMock(Route):
        pass

    class RouterMock(Router):
        class RouteMock(Route):
            def __init__(self):
                super().__init__()
                self.labels = ("__test__", )

        def __init__(self):
            super().__init__()
            self.dynamic_routes = {"test": self.RouteMock()}

    r = RouterMock()
    try:
        r.finalize()
        raise AssertionError("Expected exception SanicException not thrown")
    except SanicException:
        pass

# Generated at 2022-06-14 08:03:49.401931
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 08:03:50.740918
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert Router.finalize


# Generated at 2022-06-14 08:03:51.986925
# Unit test for constructor of class Router
def test_Router():
    assert Router


# Generated at 2022-06-14 08:03:53.138429
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)

# Generated at 2022-06-14 08:03:59.938288
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Test that route raises exception on invalid parameter name
    try:
        router = Router(ctx="ctx")
        route = Route("path", "handler", labels=("__route__", "__params__"))
        router.routes_dynamic["path"] = route
        router.finalize()
    except SanicException as e:
        assert str(e) == "Invalid route: %s. Parameter names cannot use '__'." % route

# Generated at 2022-06-14 08:04:13.265909
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router._requirements) is dict
    assert router._requirements == {}
    assert type(router.base_paths.keys()) is set
    assert len(router.base_paths.keys()) == 0
    assert type(router.dynamic_routes.keys()) is set
    assert len(router.dynamic_routes.keys()) == 0
    assert type(router.name_index.keys()) is set
    assert len(router.name_index.keys()) == 0
    assert type(router.regex_routes.keys()) is set
    assert len(router.regex_routes.keys()) == 0
    assert type(router.routes.keys()) is set
    assert len(router.routes.keys())

# Generated at 2022-06-14 08:04:24.002076
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.static_routes == {}
    assert router.static_routes_by_host == {}
    assert router.static_host_matching == {}
    assert router.regex_routes == {}
    assert router.regex_routes_by_host == {}
    assert router.regex_host_matching == {}
    assert router.ctx == {}
    assert router.name_index == {}
    assert router.DEFAULT_METHOD == "GET"