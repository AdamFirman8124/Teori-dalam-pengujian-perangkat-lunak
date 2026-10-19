

# Generated at 2022-06-14 07:55:25.812232
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic import Sanic
    from sanic.response import json
    def test_get_route(sanic, uri, route):
        assert route in sanic.router.routes_all
        assert route in sanic.router.routes_dynamic
        assert sanic.router.routes_static == {}
        assert sanic.router.routes_regex == {}
        request, response = sanic.test_client.get(uri)
        assert response.status == 200
        assert response.json == {'result':'test'}
    def test_get_static_route(sanic, uri, route):
        assert route in sanic.router.routes_all
        assert route in sanic.router.routes_static
        assert san

# Generated at 2022-06-14 07:55:27.732202
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()

    # normal case
    r.add(uri='/', methods=['POST'], handler='handler')
    r.finalize()

    # special case, custom parameter names
    try:
        r.add(uri='/<__file_uri__:path>', methods=['POST'], handler='handler')
        r.finalize()
    except SanicException:
        assert False

# Generated at 2022-06-14 07:55:30.205131
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 07:55:31.460552
# Unit test for constructor of class Router
def test_Router():
    Router()


# Generated at 2022-06-14 07:55:36.639924
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    

# Unit tests for property routes_all of class Router

# Generated at 2022-06-14 07:55:39.112252
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    from sanic_routing.router import BaseRouter
    assert issubclass(Router, BaseRouter)

# Generated at 2022-06-14 07:55:42.063589
# Unit test for constructor of class Router
def test_Router():
    test_router = Router(None)
    assert test_router.__class__.__name__ == "Router"

# Generated at 2022-06-14 07:55:47.936545
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Parameters
    @lru_cache(maxsize=ROUTER_CACHE_SIZE)
    def get(path, method, host):
        return path, method, host
    routes_dynamic = {'index.index': ('/index/index', ['GET'])}
    # Return
    # ReturnResult
    # None
    pass


# Generated at 2022-06-14 07:55:52.788919
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.response import empty

    router = Router(
        {},
    )
    router.add(
        uri="/hello/{name}/{__file_uri__:path}",
        methods=["GET"],
        handler=empty,
    )
    try:
        router.finalize()
    except Exception:
        assert False



# Generated at 2022-06-14 07:56:01.383930
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r.DEFAULT_METHOD, str)
    assert isinstance(r.ALLOWED_METHODS, (tuple, list))
    assert r._get.cache_info().hits == 0
    assert r._get.cache_info().misses == 0
    assert r.find_route_by_view_name.cache_info().hits == 0
    assert r.find_route_by_view_name.cache_info().misses == 0


# Generated at 2022-06-14 07:56:12.640342
# Unit test for method finalize of class Router
def test_Router_finalize():
    class A(Router):
        pass
    router = A()
    try:
        router.dynamic_routes["abc"].labels.append("__file_uri__")
        router.finalize()
    except SanicException:
        assert False
    try:
        router.dynamic_routes["abc"].labels.append("__file")
        router.finalize()
        assert False
    except SanicException:
        assert True

##############################################################################
# test_router.py execution
##############################################################################

if __name__ == "__main__":
    test_Router_finalize()

# Generated at 2022-06-14 07:56:25.166049
# Unit test for method finalize of class Router
def test_Router_finalize():
    def handler(request):
        pass

    # Case: A route contains labels with prefix '__'
    try:
        router = Router()
        router.add('/<__parameter:str>/<__parameter:str>', ['GET'], handler)
        router.finalize()
        print('Test case 1 succeed!')
    except Exception:
        print('Test case 1 failed!')

    # Case: A route contains labels without prefix '__'
    try:
        router = Router()
        router.add('/<parameter:str>/<parameter:str>', ['GET'], handler)
        router.finalize()
        print('Test case 2 succeed!')
    except Exception:
        print('Test case 2 failed!')

# Generated at 2022-06-14 07:56:35.830910
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.request import Request

    r = Router()

    r.add("/", 'GET', lambda x: x, name="tests")
    r.add("/<param1>/<param2>", 'GET', lambda x: x)
    r.add("/<param1>/<param2>", 'POST', lambda x: x)

    class MockApp:
        def _generate_name(self, view_name):
            return view_name

    class MockRequest(Request):
        pass

    r.finalize(MockApp())
    request = MockRequest(uri='', method='GET', app=MockApp())
    assert r.find_route_by_view_name('tests', request).uri == '/'

    # False positive:

# Generated at 2022-06-14 07:56:36.500672
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 07:56:39.132923
# Unit test for constructor of class Router
def test_Router():
    pass


# Generated at 2022-06-14 07:56:44.714341
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic

    debuginfo = """assert self.ctx.app == app
assert self.ctx.router == self
assert self.ctx.resource == self"""
    my_router = Router()
    my_app = Sanic()
    exec(debuginfo)



# Generated at 2022-06-14 07:56:58.237513
# Unit test for constructor of class Router
def test_Router():
    from sanic_routing.route import Route
    from sanic_routing.router import Router
    from sanic_routing.compiler import RegexConverter

    parameters_list = [
        (None,),
        (None, None,),
        ([],),
        ([], None,),
        (None, RegexConverter()),
        (None, None, RegexConverter()),
        ([], RegexConverter()),
        ([], None, RegexConverter()),
    ]

    def function1():
        pass

    def function2():
        pass

    def function3():
        pass

    def function4():
        pass

    def function5():
        pass

    def function6():
        pass


# Generated at 2022-06-14 07:57:08.464848
# Unit test for method finalize of class Router
def test_Router_finalize():
    def test_handler():
        pass

    # Test with correct RouteHandler
    router = Router()
    router.add(uri="/r1", methods=["GET"], handler=test_handler)
    assert isinstance(router.routes[0], Route)
    router.finalize()

    # Test with wrong RouteHandler
    with pytest.raises(SanicException):
        router = Router()
        router.add(uri="/r1", methods=["GET"], handler="not a handler")
        assert isinstance(router.routes[0], Route)
        router.finalize()

# Generated at 2022-06-14 07:57:16.192058
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.ctx import RequestContext

    router = Router(RequestContext())
    router.add(uri='/test', methods=['GET'])
    try:
        router.add(uri='/test/<__name>', methods=['GET'])
    except SanicException as e:
        assert e.args[0] == "Invalid route: /test/<__name>. Parameter names cannot use '__'."

# Generated at 2022-06-14 07:57:25.426878
# Unit test for method finalize of class Router
def test_Router_finalize():
    from . import Route, Router, RouteHandler
    from .models.handler_types import RouteHandler

    routes = dict(
        ("/", RouteHandler(lambda a: a)),
        ("/a/b/c/d/e", RouteHandler(lambda a: a)),
        ("/f", RouteHandler(lambda a: a)),
        ("/g", RouteHandler(lambda a: a)),
    )

    router = Router()
    assert router.dynamic_routes == dict()
    assert router.regex_routes == dict()
    assert router.static_routes == dict()

    router.routes = routes
    router.finalize()
    assert len(router.dynamic_routes) == 4
    assert len(router.regex_routes) == 0

# Generated at 2022-06-14 07:57:35.578972
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:57:42.338050
# Unit test for constructor of class Router
def test_Router():
    # test if the attributes initialized correctly
    router = Router()

    assert router.ROUTE_CLASS == Route
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == []
    assert router.name_index == {}
    assert router.ctx == None



# Generated at 2022-06-14 07:57:52.252798
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.route import Route

    uri = "test_uri"
    methods = ["GET"]
    handler = "test_handler"
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False

    router = Router()
    route = Route(
        uri=uri,
        methods=methods,
        handler=handler,
        strict_slashes=strict_slashes,
        stream=stream,
        ignore_body=ignore_body,
        version=version,
        name=name,
        unquote=unquote,
    )
    router.dynamic_routes[name] = route
    assert router.finalize()

# Generated at 2022-06-14 07:57:55.786732
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    app = Sanic("sanic-test")
    router = Router(app)
    with pytest.raises(Exception) as e:
        router.finalize()

# Generated at 2022-06-14 07:58:00.183722
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)
    assert len(router.__dict__) == 4
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 07:58:02.518782
# Unit test for constructor of class Router
def test_Router():
    route_handler = None
    response = Router.get(
        path='/',
        method='GET',
        host='127.0.0.1',
        route_handler=route_handler
    )
    pass

# Generated at 2022-06-14 07:58:06.233685
# Unit test for constructor of class Router
def test_Router():
    r1 = Router()
    assert r1.get('/', 'GET', 'a.com') == ()
    assert isinstance(r1.routes_all, list)
    assert isinstance(r1.routes_static, list)
    assert isinstance(r1.routes_dynamic, dict)
    assert isinstance(r1.routes_regex, list)
    assert r1.find_route_by_view_name('') == None


# Generated at 2022-06-14 07:58:13.303066
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ['GET', 'POST', 'PUT', 'HELP', 'HEAD', 'OPTIONS', 'PATCH', 'DELETE', 'TRACE', 'CONNECT']
    res = (router.resolve)(path='test', method='test', extra={"host": "test"})
    assert res == res

# Generated at 2022-06-14 07:58:25.212525
# Unit test for method finalize of class Router
def test_Router_finalize():
    instance = Router()
    labels = []
    def foo():
        pass
    instance.add(uri = "abc", methods = [], handler = foo, name = "abc", strict_slashes = False, unquote = False, host = None, version = None, stream = False, ignore_body = False, static = False)
    instance.add(uri = "abc", methods = [], handler = foo, name = "abc", strict_slashes = False, unquote = False, host = None, version = None, stream = False, ignore_body = False, static = False)
    instance.add(uri = "abc", methods = [], handler = foo, name = "abc", strict_slashes = False, unquote = False, host = None, version = None, stream = False, ignore_body = False, static = False)

# Generated at 2022-06-14 07:58:27.580701
# Unit test for constructor of class Router
def test_Router():
    route = Router(*args, **kwargs)
    print(route)

# Generated at 2022-06-14 07:58:37.784342
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 07:58:42.571204
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert(type(router) == Router)
    assert(router.DEFAULT_METHOD == "GET")
    assert(router.ALLOWED_METHODS == HTTP_METHODS)

if __name__ == '__main__':
    test_Router()

# Generated at 2022-06-14 07:58:48.561799
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}



# Generated at 2022-06-14 07:58:58.940933
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Test the case that the path of the route is invalid:
    # In the path of the route, the parameter names cannot use "__",
    # or the route is invalid.

    # Create the router to be tested:
    router = Router()

    # Create a route whose path is invalid:
    # The path contains the parameter name: "__test"
    @router.add("/test/{__test}", methods=["GET"])
    def handler(request, __test):
        pass

    # Test the finalize method of router
    # Since the path of the route is invalid,
    # SanicException should be thrown
    with pytest.raises(SanicException) as excinfo:
        router.finalize()

    # Check the message of the exception

# Generated at 2022-06-14 07:59:06.381159
# Unit test for method finalize of class Router
def test_Router_finalize():
    # test that finalize raises exception for route with __-label
    #    
    router = Router()
    router.dynamic_routes['key'] = Route(uri='/test', method='get', handler='test', name='test')
    router.dynamic_routes['key'].labels = ['__file_uri__', '__label_uri__']
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 07:59:17.573793
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.constants import SERVER_NAME
    from sanic.server import HttpProtocol
    from sanic.response import json
    from sanic.request import Request

    @async_generator
    async def gen():
        yield 'a'

    router = Router(
        async_mode=True,
        host=None,
        port=None,
        server_name=SERVER_NAME,
        protocol=HttpProtocol,
        request_class=Request,
        response_class=json,
    )

    router.add(uri='/', methods=('GET',), handler=gen, static=False)
    router.finalize()

    res = router.routes_all
    assert len(res) == 1

# Generated at 2022-06-14 07:59:18.563447
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)

# Generated at 2022-06-14 07:59:19.835885
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:59:22.230819
# Unit test for constructor of class Router
def test_Router():
    assert (Router.DEFAULT_METHOD == HTTP_METHODS[0])
    assert (Router.DEFAULT_METHOD == "GET")
    assert (Router.ALLOWED_METHODS == HTTP_METHODS)



# Generated at 2022-06-14 07:59:33.191688
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic.app import Sanic
    from sanic.router import Router
    from sanic.constants import HTTP_METHODS
    from inspect import iscoroutinefunction

    from sanic_routing.route import Route  # type: ignore
    from sanic_routing.exceptions import NotFound as RoutingNotFound  # type: ignore
    from sanic_routing.exceptions import NoMethod  # type: ignore

    def add_route(router, uri, handler, methods=None, stream=False, static=False):
        methods_to_add = HTTP_METHODS if (
            methods is None and not static
        ) else methods
        if not isinstance(methods_to_add, (list, tuple)):
            methods_to_add = [methods_to_add]

# Generated at 2022-06-14 07:59:58.405430
# Unit test for method finalize of class Router
def test_Router_finalize():
    with pytest.raises(SanicException) as exception_info:
        # Method get of class Router
        router = Router()
        route = Route(path="test_route", handler=None, methods=None)
        route.labels = ["file_uri", "__test__"]
        router.dynamic_routes["test_key"] = route
        router.finalize()
    assert str(exception_info.value) == "Invalid route: <sanic_routing.route.Route object at 0x104d5b8e0>. Parameter names cannot use '__'."

# Generated at 2022-06-14 08:00:00.397975
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:00:04.287681
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    r_1 = Router()
    # test two router objects are different
    assert r != r_1


# Generated at 2022-06-14 08:00:17.481920
# Unit test for constructor of class Router
def test_Router():
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic import Sanic
    from sanic.exceptions import InvalidUsage
    from sanic.constants import HTTP_METHODS
    import pytest
    import asyncio
    import itertools

    app = Sanic('test_router')

    @app.route('/')
    async def handler(request):
        return HTTPResponse(b'OK')

    @app.route('/test')
    async def handler(request):
        return HTTPResponse(b'OK')

    @app.route('/longer')
    async def handler(request):
        return HTTPResponse(b'OK')

    @app.route('/longer/test')
    async def handler(request):
        return HT

# Generated at 2022-06-14 08:00:30.930704
# Unit test for method finalize of class Router
def test_Router_finalize():
    class TestRouter(Router):
        def finalize(self, *args, **kwargs):
            super().finalize(*args, **kwargs)
            for route in self.dynamic_routes.values():
                if any(
                    label.startswith("__") and label not in ALLOWED_LABELS
                    for label in route.labels
                ):
                    raise SanicException(
                        f"Invalid route: {route}. Parameter names cannot use '__'."
                    )

    test_router = TestRouter()
    try:
        test_router.add("/invalid_route/<__test>", ["GET"], lambda *args, **kwargs: None)
    except SanicException as ex:
        assert True
        return
    assert False

# Generated at 2022-06-14 08:00:36.108870
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.router == router
    assert router.ctx.app == None
    assert router.ctx.prefix == None
    assert router.ctx.blueprint == None

# Generated at 2022-06-14 08:00:48.763151
# Unit test for constructor of class Router
def test_Router():

    @staticmethod
    def is_stream_true(path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
        router = Router()
        route = router.add('/notification', ['POST'], is_stream_true, stream=True)
        router.add_route(route)
        return router.get(path, method, host)
    test_is_stream_true = test_Router.is_stream_true('/notification', 'POST', None)

    @staticmethod
    def is_stream_false(path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
        router = Router()

# Generated at 2022-06-14 08:01:01.660580
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add(uri="/", methods=["GET"], handler=lambda request: "OK", name="index")
    router.add(uri="/forward/<name>", methods=["GET"], handler=lambda request: "OK", name="forward")
    router.add(uri="/<name>", methods=["GET"], handler=lambda request: "OK", name="index1")
    router.add(uri="/<name>", methods=["POST"], handler=lambda request: "OK", name="index2")
    router.add(uri="/", methods=["POST"], handler=lambda request: "OK", name="index3")
    router.add(uri="/forward", methods=["GET"], handler=lambda request: "OK", name="forward1")

    assert router.find_route_by_view_name("index") != None

# Generated at 2022-06-14 08:01:03.896861
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert isinstance(router, BaseRouter)


# Generated at 2022-06-14 08:01:07.893902
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.dynamic_routes['route'] = Route('/', None, None, None, ['__file_uri__', '__something'])
        router.finalize()
        assert False
    except SanicException:
        assert True
    except:
        assert False

# Generated at 2022-06-14 08:01:50.182346
# Unit test for method add of class Router
def test_Router_add():
    """Router.add

    Arguments:
        path: path of the route
        methods: types of HTTP methods that should be attached
        handler: the handler to be executed
        host: host that the route should be on
        strict_slashes: whether to apply strict slashes
        stream: whether to stream the response
        ignore_bo: whether the incoming request body should be read
        version: a version modifier for the uri
    """

    def check_methods(methods: Iterable[str]):
        if any([m.isalpha() and m not in HTTP_METHODS for m in methods]):
            raise MethodNotSupported("Invalid HTTP method")


    def check_content(content: str, stream: bool):
        if stream:
            pass

# Generated at 2022-06-14 08:01:59.832957
# Unit test for method finalize of class Router
def test_Router_finalize():
    from .test_utils import Sanic
    from .test_router import Router as SanicRouter
    from .test_router import ROUTE_CACHE_SIZE
    from .test_websocket import websocket_test

    app = Sanic('test_finalize')
    app.config.ROUTE_CACHE_SIZE = ROUTE_CACHE_SIZE
    router = SanicRouter(app, [])
    router.add(uri = '/test/url', methods = ['GET'], handler = websocket_test)
    router.finalize()

# Generated at 2022-06-14 08:02:01.516002
# Unit test for method finalize of class Router
def test_Router_finalize():
    obj = Router()
    res = obj.finalize()
    assert res == False

# Generated at 2022-06-14 08:02:03.525117
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:02:09.461175
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    app = Sanic(__name__)
    router = app.router.routes  # type: ignore
    router.add("/test/<one>/<two>", ["GET"], lambda x: x, name="test")
    router.add("/test/<__file_uri__>/<two>", ["GET"], lambda x: x, name="test1")
    router.finalize()

    assert router.routes_regex == []



# Generated at 2022-06-14 08:02:10.769231
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 08:02:20.548893
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    def _get(path, method, host):
        return [path, method, host]
    router._get = _get
    path = '/'
    method = 'GET'
    host = 'localhost'
    expected = ['/', 'GET', 'localhost']
    assert router.get('/', 'GET', 'localhost') == expected
    assert router.get('/', 'GET', 'localhost') == expected
    assert router.get('/', 'GET', 'localhost') == expected
    path = '/1'
    method = 'GET'
    host = 'localhost'
    expected = ['/1', 'GET', 'localhost']
    assert router.get('/1', 'GET', 'localhost') == expected
    assert router.get('/1', 'GET', 'localhost') == expected

# Generated at 2022-06-14 08:02:25.135427
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    uri = "test"
    methods = ["GET"]
    handler = lambda: 0
    def test():
        router.add(uri, methods, handler)
        router.finalize() 
    test()

# Generated at 2022-06-14 08:02:29.672512
# Unit test for constructor of class Router
def test_Router():
    import pytest
    from sanic.exceptions import NotFound
    route = Router(app=None)
    path = "http://localhost"
    with pytest.raises(NotFound):
        route._get(path=path, method="wrong", host="localhost")

# Generated at 2022-06-14 08:02:38.295129
# Unit test for constructor of class Router
def test_Router():
    # Given
    uri = "res/"
    methods = ["GET"]
    handler = RouteHandler()
    # When
    router = Router(uri, methods, handler)
    # Then
    assert router.uri == uri
    assert router.methods == methods
    assert router.handler == handler
    assert router.host == None
    assert router.strict_slashes == False
    assert router.stream == False
    assert router.ignore_body == False
    assert router.version == None
    assert router.name == None

# Generated at 2022-06-14 08:03:42.793075
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 08:03:45.136466
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    if router is None:
        assert False
    assert router is not None


# Generated at 2022-06-14 08:03:57.409446
# Unit test for method add of class Router
def test_Router_add():
    # Create a new instance of a Sanic application
    app = Sanic()
    # Let Router know where the views are
    app.config.from_pyfile('/Users/avinashpasupuleti/PycharmProjects/Jumbotron/src/app/views.py')

    # Set up a URL endpoint for a handler function
    @app.route('/')
    # Define a handler from the application
    async def hello(request):
        return response.text('Hello world!')

    # When a URL is requested from the server, the associated handler will be called.
    # This will automatically compare the request method (GET, POST, etc.) and the URL path.
    # The return value of the function will be used as the response to the request.

# Generated at 2022-06-14 08:04:02.846923
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    try:
        router = Router()
        router.add(uri='/', methods=['GET'], handler=None, host=None, strict_slashes=True,
                   stream=False, ignore_body=False, version=None, name='index')
        router.finalize()
        assert True
    except:
        assert False



# Generated at 2022-06-14 08:04:08.825201
# Unit test for method finalize of class Router
def test_Router_finalize():
    route_table = Router.get_routes()
    route_table.add_route('/test', methods=['GET', 'POST'], handler='test')
    try:
        route_table.finalize()
        assert False
    except SanicException as err:
        assert True

# Generated at 2022-06-14 08:04:13.553188
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    expected_method_allowed = router.ALLOWED_METHODS
    expected_default_method = router.DEFAULT_METHOD
    assert expected_method_allowed == HTTP_METHODS
    assert expected_default_method == "GET"

# Generated at 2022-06-14 08:04:17.823831
# Unit test for constructor of class Router
def test_Router():
    """
    >>> test_Router() # doctest: +ELLIPSIS
    <sanic.router.Router object at 0x...>
    """
    router = Router()
    return router

# Generated at 2022-06-14 08:04:25.453437
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Router()
    route.ctx = Dict[str, Any]()
    route.dynamic_routes = Dict[str, Any]()
    route.dynamic_routes = {
        "test": {
            "labels": ["__file_uri__"],
        }
    }
    route.finalize()

# Generated at 2022-06-14 08:04:27.327935
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:04:34.101874
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import SanicException
    from sanic import Sanic
    
    app = Sanic('test_Router_finalize')
    with pytest.raises(SanicException):
        pass
        #TODO: What does this line do?
        # app.add_route(lambda r: 'OK', '/')