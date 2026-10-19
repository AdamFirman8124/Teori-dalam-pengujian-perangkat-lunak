

# Generated at 2022-06-14 07:56:07.409335
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router._get == router.get
    # assert router._get.cache_info().hits == 0
    # assert router._get.cache_info().misses == 0



# Generated at 2022-06-14 07:56:17.488279
# Unit test for constructor of class Router
def test_Router():
    from sanic.views import CompositionView
    from sanic.response import HTTPResponse

    def handler(request):
        return request

    view = CompositionView()
    view.add(["GET"], handler)

    router = Router()
    router.add(
        uri=view.uri_template, methods=view.methods, handler=view, static=view.is_static
    )

    # Unit test for method finalize(...) in class Router
    router.finalize()

    request = mock.MagicMock()
    request.path = "/"
    request.method = "GET"
    request.headers = {}
    request.content_type = None
    request.app = None

    # Unit test for method get(...) in class Router

# Generated at 2022-06-14 07:56:21.421440
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        Router().finalize()
    except Exception:
        return False
    else:
        return True

print(test_Router_finalize())

# Generated at 2022-06-14 07:56:33.783568
# Unit test for method finalize of class Router
def test_Router_finalize():
    # First, we import the module and create a new instance of the Router class
    from sanic.router import Router
    from sanic import Sanic
    from sanic.response import json
    app = Sanic()
    router = Router()

    def test_route_handler(request):
        return json({"msg": "hello"})
    # This is a valid path
    app.add_route(handler=test_route_handler, uri="/path/to/directory")
    # This is also a valid path
    app.add_route(handler=test_route_handler, uri="/path/to/directory/")
    # This path raises an error because the parameter name starts with __

# Generated at 2022-06-14 07:56:38.000208
# Unit test for constructor of class Router
def test_Router():
  router = Router()
  router.get("/")
  router.static("/", 'path_debug')
  router.add("/",["GET"])
  router.find_route_by_view_name("/")
  router.finalize("GET")


# Generated at 2022-06-14 07:56:43.935828
# Unit test for method add of class Router
def test_Router_add():
    from sanic import Sanic
    from sanic.response import text
    app = Sanic('test_Router_add')
    router = Router()
    route = router.add('/', ['GET'], text('Hello world'), name=None)
    assert isinstance(route, Route)


# Generated at 2022-06-14 07:56:49.825461
# Unit test for constructor of class Router
def test_Router():
    class MockRouter(Router):
        def __init__(self, *args, **kwargs):
            super(MockRouter, self).__init__(*args, **kwargs)

    # currently passing
    assert MockRouter(app=None, router=None)



# Generated at 2022-06-14 07:57:01.088019
# Unit test for constructor of class Router
def test_Router():
    class App:
        def _generate_name(self, name):
            return name
    router = Router(App())

    # Test function add()
    router.add(
        "",
        ["GET"],
        lambda x: x,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=False,
        static=False,
    )

    # Test function find_route_by_view_name()
    # Can't test this method because it's a property

    # Test function finalize()
    def func(x):
        return x

# Generated at 2022-06-14 07:57:05.488913
# Unit test for constructor of class Router
def test_Router():
    """
    Unit test for constructor of class Router
    This method is for construction test only, which is not necessary for integration test
    """
    with pytest.raises(TypeError):
        Router()

# Generated at 2022-06-14 07:57:15.986706
# Unit test for method finalize of class Router
def test_Router_finalize():
    router_test = Router(object())
    # Prepare a route object that contains allowed labels
    # note: the router object is not used for testing the finalize method
    route = Route(object(), 'POST', '/', object(), name='route_name')
    route.labels.append('__label__')
    router_test.dynamic_routes['label_route'] = route
    # Prepare a route object that contains forbidden labels
    route = Route(object(), 'POST', '/', object(), name='route_name')
    route.labels.append('__label_error__')
    router_test.dynamic_routes['label_error_route'] = route
    
    try:
        router_test.finalize()
    except SanicException:
        assert True
    else:
        assert False

# Generated at 2022-06-14 07:57:22.647454
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == 'GET'
    print('Constructor of class Router successfully passed')


# Generated at 2022-06-14 07:57:31.395804
# Unit test for constructor of class Router
def test_Router():
    router = Router([])
    assert router is not None
    assert len(router.routes) == 0
    assert len(router.static_routes) == 0
    assert len(router.dynamic_routes) == 0
    assert len(router.regex_routes) == 0
    assert len(router.name_index) == 0
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS is HTTP_METHODS


# Generated at 2022-06-14 07:57:34.100210
# Unit test for constructor of class Router
def test_Router():
    # Arrange
    router = Router()

    # Act
    
    # Assert
    assert router


# Generated at 2022-06-14 07:57:34.891159
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 07:57:36.820481
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == []

# Generated at 2022-06-14 07:57:48.927796
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic.router import Router
    from sanic.models.handler_types import RouteHandler

    def handler_test1(request):
        pass

    def handler_test2(request):
        pass

    router = Router()

    with pytest.raises(SanicException):
        router.add('/user-{id:d}/{name}', ['GET'], handler_test1, unquote=True, name='test1')
        router.add('/user-{id:d}/{name}', ['GET'], handler_test2, unquote=True, name='test2')
        router.finalize()


# Generated at 2022-06-14 07:57:54.956716
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.add("/test", ['GET', 'POST'], lambda: "test")
    print(router.resolve("/test", "GET"))
    print(router.resolve("/test", "POST"))
    

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 07:58:00.679341
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    Test to make sure that allowed labels are allowed
    """
    my_router = Router()
    route1 = Route("/", "handler", methods=["GET"])
    my_router.dynamic_routes[("/", "GET")] = route1
    my_router.finalize()
    return my_router


# Generated at 2022-06-14 07:58:02.054239
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:58:15.315163
# Unit test for constructor of class Router
def test_Router():
    from sanic.blueprints import Blueprint
    from sanic.router import RouteExists
    from sanic.app import Sanic

    router = Router()
    route = router.add(
        uri="/",
        methods=["GET"],
        handler=lambda request: "test",
        host="testhost.com",
        strict_slashes=True,
        stream=False,
        ignore_body=False,
        version=1.0,
        name="my_route",
        unquote=False,
        static=False,
    )

    # Test whether the constructor of Router calls the constructor of BaseRouter
    assert router.base_router == []
    assert router.static_routes.keys() == {'add'}
    assert router.dynamic_routes == {}
    assert router.regex_

# Generated at 2022-06-14 07:58:23.053678
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException):
        router.add('/<__invalid_name>')
        router.finalize()

# Generated at 2022-06-14 07:58:30.162571
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes_all == dict()
    assert router.routes_static == dict()
    assert router.routes_dynamic == dict()
    assert router.routes_regex == dict()

# Generated at 2022-06-14 07:58:33.597784
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert len(router.ALLOWED_METHODS) == 7  # len(HTTP_METHODS)

# Generated at 2022-06-14 07:58:42.803479
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    from sanic.models.route import Route
    from sanic.models.handler_types import RouteHandler
    a = [1, 2, 3]
    b = 'abc'
    c = (1, 2, 3)
    r1 = Route(a, b, c)
    
    assert a == r1.path
    assert b == r1.methods
    assert c == r1.handler
    
    uri = 'home'
    methods = ('GET', 'POST', 'DELETE')
    handler = RouteHandler
    host = ('127.0.0.1', '127.0.0.2', '127.0.0.3')
    strict_slashes = True
    stream = True
    ignore_body = True
    version = '1.0'
   

# Generated at 2022-06-14 07:58:43.742441
# Unit test for constructor of class Router
def test_Router():
    assert True

# Generated at 2022-06-14 07:58:45.688292
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router



# Generated at 2022-06-14 07:58:53.876231
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from unittest.mock import patch
    from doctest import testmod, ELLIPSIS
    with patch('sanic.log.error') as mock_log:
        testmod(Router, raise_on_error=True,
            extraglobs={"router": Router()}, optionflags=ELLIPSIS)
        assert mock_log.call_count==1, "Invalid route Parameter names cannot use '__'."

# Generated at 2022-06-14 07:58:57.132059
# Unit test for method finalize of class Router
def test_Router_finalize():
    from unittest import TestCase
    class RouterTest(TestCase):
        def test_finalize(self):
            router = Router()
            router.add(uri="test")
            router.finalize()
            self.assertTrue(router.finalized)

# Generated at 2022-06-14 07:58:59.398729
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router, "Can't create object of Router class"


# Generated at 2022-06-14 07:59:00.859334
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.app is None


# Generated at 2022-06-14 07:59:15.893240
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert hasattr(r, "DEFAULT_METHOD")
    assert hasattr(r, "ALLOWED_METHODS")
    assert hasattr(r, "routes_all")
    assert hasattr(r, "routes_static")
    assert hasattr(r, "routes_dynamic")
    assert hasattr(r, "routes_regex")



# Generated at 2022-06-14 07:59:21.000490
# Unit test for constructor of class Router
def test_Router():
    router = Router(BaseRouter.DEFAULT_CONTEXT, BaseRouter.DEFAULT_MATCHER)
    assert router.context == BaseRouter.DEFAULT_CONTEXT
    assert router.matcher == BaseRouter.DEFAULT_MATCHER
    assert router.routes.get(None) == []
    assert router.dynamic_routes.get(None) == []
    assert router.regex_routes.get(None) == []
    assert router.static_routes.get(None) == []
    assert router.name_index == {}


# Generated at 2022-06-14 07:59:32.415491
# Unit test for method finalize of class Router
def test_Router_finalize():
    class mock_Router:

        def __init__(self, dynamic_routes):
            self.dynamic_routes = dynamic_routes


    route_wrong_label = Route("/<foo__bar>/", handler=None, methods=["GET"])
    route_ok_label = Route("/<__file_uri__>/", handler=None, methods=["GET"])

    routes_wrong_labels = {
        "/<foo__bar>/": route_wrong_label,
    }

    routes_ok_labels = {
        "/<__file_uri__>/": route_ok_label,
    }

    router = mock_Router(dynamic_routes=routes_wrong_labels)

# Generated at 2022-06-14 07:59:44.955045
# Unit test for method finalize of class Router
def test_Router_finalize():
    def method_test_1():
        router = Router(prefix="", handler=None)
        route = Route(
            path="erwew",
            handler=None,
            methods=[""],
            name=None,
            strict=False,
            unquote=False,
            **{}
        )
        route.ctx = None
        route.labels = ["__fdsfs__"]
        router.dynamic_routes = {
            "erwew": route
        }
        with pytest.raises(SanicException) as info:
            router.finalize()
        assert "Invalid route" in str(info.value)
    def method_test_2():
        router = Router(prefix="", handler=None)

# Generated at 2022-06-14 07:59:47.157480
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 07:59:56.149727
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.ctx = type('', (), {})()
        router.ctx.app = type('', (), {})()
        router.ctx.app._generate_name = lambda x: x

        route = Route()
        route = Route()
        route.labels = set()
        route.labels.add('__file_uri__')
        router.dynamic_routes = {1: route}

        router.finalize()

    except Exception as e:
        raise e

# Generated at 2022-06-14 07:59:57.171967
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router == None

# Generated at 2022-06-14 08:00:07.862425
# Unit test for method finalize of class Router
def test_Router_finalize():
    import sys
    sys.path.append("../")
    from sanic.router import Router

    r = Router()  # type: ignore
    r.add("/")
    r.add("/users/<id>")
    r.finalize()

    assert len(r.routes_all) == 2
    assert len(r.routes_static) == 1
    assert len(r.routes_dynamic) == 1
    assert len(r.routes_regex) == 0
    assert r.get("/", "GET")

    r.add("/invalid/<__id>")
    try:
        r.finalize()
        assert False
    except SanicException:
        assert True


if __name__ == "__main__":
    test_Router_finalize()

# Generated at 2022-06-14 08:00:17.755537
# Unit test for constructor of class Router
def test_Router():
    @lru_cache(maxsize=ROUTER_CACHE_SIZE)
    def get(  # type: ignore
        path: str, method: str, host: Optional[str]
    ) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
        return BaseRouter.resolve(
            path=path,
            method=method,
            extra={"host": host},
        )

    @lru_cache(maxsize=ROUTER_CACHE_SIZE)
    def find_route_by_view_name(view_name, name=None):
        if not view_name:
            return None

        full_name = BaseRouter.ctx.app._generate_name(view_name)
        route = BaseRouter.name_index.get(full_name)


# Generated at 2022-06-14 08:00:20.650996
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 08:00:32.788046
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.router import Router
    from sanic.response import json
    try:
        app = Sanic()
        router = Router()
        router.finalize()
    except:
        assert True


# Generated at 2022-06-14 08:00:34.410327
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 08:00:47.369825
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic_routing.route import Route
    from sanic.constants import HTTP_METHODS


    async def handler(request, *args, **kwargs):
        return HTTPResponse(body="OK")
    async def test(request, *args, **kwargs):
        return HTTPResponse(body="OK")

    router = Router()
    router.get("/test", handler_or_coro=handler)
    route = router.get("/test", handler_or_coro=handler)
    route.GET(handler_or_coro=test)
    route.POST(handler_or_coro=test)

# Generated at 2022-06-14 08:00:59.966317
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route(
        path='/<param1>/<param2:int>',
        methods=['GET'],
        handler=lambda request: "OK",
        name=None,
        strict=True,
        unquote=False,
        ctx=None,
    )
    router.add_route(route)
    with pytest.raises(SanicException):
        router.finalize()
    route = Route(
        path='/<param1:path>/<param2:int>',
        methods=['GET'],
        handler=lambda request: "OK",
        name=None,
        strict=True,
        unquote=False,
        ctx=None,
    )
    router.add_route(route)
    router.finalize()



# Generated at 2022-06-14 08:01:03.240712
# Unit test for constructor of class Router
def test_Router():
    try:
        object = Router(None, None)
    except Exception as error:
        print(error)
        assert False
    else:
        assert True

# Generated at 2022-06-14 08:01:10.762759
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    app = "app"
    router = Router(app)
    args = "args"
    kwargs = "kwargs"
    with pytest.raises(SanicException) as exc_info:
        router.finalize(args, kwargs)
    assert(exc_info.match(".* cannot use '__'.*"))
    # TODO: assert call of super().finalize(*args, **kwargs)

# Generated at 2022-06-14 08:01:20.687553
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router
    import pytest
    from sanic.exceptions import SanicException

    def test():
        router = Router()
        uri = '/uri/<abc>/<def>'
        from sanic.app import Sanic
        app = Sanic(__name__)
        router.add(uri, ['GET'], None, app=app, static=True)
        router.finalize(None, None)

    with pytest.raises(SanicException):
        test()

# Generated at 2022-06-14 08:01:25.249698
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        route = Router().add("/<name>/<age>", "GET", lambda x: "OK")
        Router().finalize()
    except SanicException as e:
        pass
    else:
        assert False

# Generated at 2022-06-14 08:01:38.740183
# Unit test for method finalize of class Router
def test_Router_finalize():
    # create a router
    router = Router()

    @router.get("/")
    async def handler():
        pass

    # add a route
    router.add(uri="/", methods=["GET"], handler=handler)

    # add a route with an invalid label
    try:
        router.add(uri="/invalid/<__id>", methods=["GET"], handler=handler)
    except SanicException as e:
        assert "Invalid route: {uri='/invalid/<__id>', methods=['GET'], handler=<function handler at 0x7ff4f4a4b4d0>. Parameter names cannot use '__'." in str(e)
    
    # add a route with an invalid label

# Generated at 2022-06-14 08:01:48.972682
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.constants import HTTP_METHODS

    # Testcase 1: Tests with all the allowed route parameters
    router = Router()
    router.add(
        uri="test", methods=HTTP_METHODS, handler=None, host=None, strict_slashes=False, stream=False
    )

    # Testcase 2: Tests with invalid route label namespace
    router = Router()
    try:
        router.add(
            uri="test__test", methods=HTTP_METHODS, handler=None, host=None, strict_slashes=False, stream=False
        )
    except SanicException as e:
        assert True

    # Testcase 3: Tests with invalid URI parameter
    router = Router()

# Generated at 2022-06-14 08:02:18.215945
# Unit test for constructor of class Router
def test_Router():
    assert Router.DEFAULT_METHOD == "GET"
    assert all(x in Router.ALLOWED_METHODS for x in HTTP_METHODS)

    routes = Router()
    routes.add(uri="", methods=['POST'], handler=[])
    assert len(routes.dynamic_routes) == 0
    assert len(routes.static_routes) == 1

    routes.add(uri="", methods=['POST'], handler=[], static=True)
    assert len(routes.dynamic_routes) == 0
    assert len(routes.static_routes) == 1
    
    routes.add(uri="/url", methods=['POST'], handler=[])
    assert len(routes.dynamic_routes) == 1

# Generated at 2022-06-14 08:02:26.340581
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router
    assert router.ctx == {}
    assert router.routes == {}
    assert router.static_routes == {}
    assert router.regex_routes == {}
    assert router.dynamic_routes == {}
    assert router.name_index == {}
    assert router.reverse_index == {}
    assert router.ctx_index == {}


# Generated at 2022-06-14 08:02:27.525865
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert Router().finalize() is None

# Generated at 2022-06-14 08:02:32.076153
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add("/<__file_uri__>", methods=["GET"], handler=None, static=True)

    try:
        r.finalize()
        assert True
    except SanicException:
        assert False


# Generated at 2022-06-14 08:02:37.889007
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    Test the finalize method of the Router class.

    :return: None

    """
    router = Router()
    # create a route with an invalid label
    router.dynamic_routes[1] = Route('/', None, 'GET',
                                     labels=['__not_valid__'],
                                     ctx={'app': None},
                                     requirements={})
    # test that a SanicException is raised
    with pytest.raises(SanicException) as exinfo:
        router.finalize()

# Unit tests for method get of class Router

# Generated at 2022-06-14 08:02:47.866056
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.route import Route

    router = Router()
    router.add(
        uri="/",
        methods=["get"],
        handler=None,
        host=None,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=False,
    )
    route = router.routes_dynamic["__root__"]
    assert isinstance(route, Route)


# Generated at 2022-06-14 08:02:54.844879
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert router.ctx is None
    assert router.dynamic_routes == {}
    assert router.routes == {}
    assert router.name_index == {}
    assert router.regex_routes == []
    assert router.static_routes == []

# Generated at 2022-06-14 08:02:55.669653
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 08:02:58.944659
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    r.DEFAULT_METHOD = 'GET'
    assert r.DEFAULT_METHOD == 'GET'


# Generated at 2022-06-14 08:03:02.610488
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    if not (isinstance(Router(collections.ChainMap()), Router)):
        raise AssertionError()


# Generated at 2022-06-14 08:03:34.165813
# Unit test for constructor of class Router
def test_Router():
    Router()


# Generated at 2022-06-14 08:03:41.309156
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.routes_all == router.routes
    assert router.routes_static == router.static_routes
    assert router.routes_static == {}
    assert router.routes_dynamic == router.dynamic_routes
    assert router.routes_dynamic == {}
    assert router.routes_regex == router.regex_routes
    assert router.routes_regex == {}

# Generated at 2022-06-14 08:03:43.959586
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing import BaseRouter  # type: ignore
    router = Router()
    path = "/hello"
    methods = ["POST", "GET", "OPTIONS"]
    handler = lambda: "hello"
    #routes = router.add(path, methods, handler)
    routes = router.add(path, methods, handler)
    regex_routes = router.regex_routes

# Generated at 2022-06-14 08:03:51.430186
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.routes_dynamic = {
        'bla': Route(path='bla', handler=None, methods={'GET', 'POST'}, name=None, strict=False,
        unquote=False, ctx=None, requirements=None)
    }
    try:
        r.finalize()
    except SanicException:
        assert True
    else:
        assert False

# Generated at 2022-06-14 08:03:52.642805
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert Router().finalize(route_class=Route)

# Generated at 2022-06-14 08:04:00.380809
# Unit test for method add of class Router
def test_Router_add():
    # Pre-conditions for unit test
    app = Sanic(__name__)
    app.config.KEEP_ALIVE = False
    app.config.REQUEST_TIMEOUT = 15

    uri = "/uri"
    methods = ["GET"]
    handler = Sanic.get

    # Run unit test
    route = Router.add(uri, methods, handler)

    # Assert
    try:
        assert route == Router.find_route(uri, "GET")
    except KeyError:
        assert False

# Generated at 2022-06-14 08:04:02.042866
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ctx


# Generated at 2022-06-14 08:04:09.889812
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.parse("/{}/<parameter:string>/{a}")
    route = list(router.routes_dynamic.values())[0]
    router.finalize()
    try:
        assert route.regex.pattern == '/([^/.]+)/(?P<parameter>[^/]+)'
    except AssertionError:
        assert False, "Test fail"

# Generated at 2022-06-14 08:04:11.254456
# Unit test for constructor of class Router
def test_Router():
   r=Router()
   assert r.finalize()

# Generated at 2022-06-14 08:04:21.260583
# Unit test for constructor of class Router
def test_Router():

    router = Router(
        ctx=None,
        name_index=None,
        handler_index=None,
        error_handler_index=None,
        host_index=None,
        regex_index=None,
        path_index=None,
    )

    assert (router.ctx == None)
    assert (router.name_index == None)
    assert (router.handler_index == None)
    assert (router.error_handler_index == None)
    assert (router.host_index == None)
    assert (router.regex_index == None)


# Generated at 2022-06-14 08:05:29.858261
# Unit test for method finalize of class Router
def test_Router_finalize():
    class Sanic:
        def _generate_name(self,name):
            return name

    router = Router()
    router.ctx = Sanic()
    router.dynamic_routes = {'route': 'route'}
    route = {'labels': ["__file_uri", "__address", "__city"]}
    router.add_route = MagicMock(route)
    router.finalize()


# Generated at 2022-06-14 08:05:37.153098
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.dynamic_routes = {1: 'route1', 2: 'route2', 3: 'route3'}
    r.add_route = None
    with pytest.raises(SanicException) as excinfo:
        r.finalize()
    assert str(excinfo.value) == "Invalid route: route1. Parameter names cannot use '__'."



# Generated at 2022-06-14 08:05:47.958097
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        def finalize(self, *args, **kwargs):
            print('Hello, finalize')

        #test1: parameter names cannot use '__'
        router1 = Router()
        router1.dynamic_routes = {'Hello': 'World'}
        router1.finalize()

        #test1: parameter names can use '__'
        router2 = Router()
        router2.dynamic_routes = {'Hello': 'World', '__file_uri__': 'file_uri'}
        router2.finalize()
    except Exception as e:
        print(e)


# Generated at 2022-06-14 08:05:51.285027
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
    except Exception as e:
        assert False, "constructor of class Router failed, %s" % e

# Generated at 2022-06-14 08:05:58.254638
# Unit test for method finalize of class Router
def test_Router_finalize():
    with pytest.raises(
        SanicException, match=r"Invalid route: \$\^?\(\[<>.*?\]\).+"
        r"Parameter names cannot use '__'."
    ):
        router = Router()
        router.add(
            uri="/<__this_is_not_allowed>",
            methods=["GET"],
            handler=lambda request, __this_is_not_allowed: "OK",
        )
        router.finalize()
