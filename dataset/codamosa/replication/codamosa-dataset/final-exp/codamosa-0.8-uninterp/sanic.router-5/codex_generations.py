

# Generated at 2022-06-14 07:55:32.319621
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic

    app = Sanic('test')
    router = Router(app, app.exception_handler, app.router_error_handler)
    route = Route(
        app,
        handler=None,
        method='GET',
        host=None,
        strict_slashes=False,
        uri=None,
        name=None,
        path=None,
        unquote=False,
        methods=['GET'],
        params={},
        param_patterns={},
        param_converters={},
        param_types={},
        param_requirements={},
        param_defaults={},
        param_choices={},
        param_labels={}
    )
    path = '/'

# Generated at 2022-06-14 07:55:34.819565
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Router()
    try:
        route.finalize()
    except Exception as err:
        assert True
    else:
        assert False

# Generated at 2022-06-14 07:55:42.340938
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()

        def hello_world(request, name=None):
            pass

        router.add("/", ("GET", "POST"), hello_world)
        router.add("/custom/<name>", ("GET", "POST"), hello_world)

        router.finalize()
    except SanicException:
        raise AssertionError("Finalize should not fail")


# Generated at 2022-06-14 07:55:43.569624
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 07:55:45.098378
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 07:55:54.343212
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(
        None, "host",
        # host     : Union[ str, Iterable[str] ]
        "/"
        # uri      : str
    )

    # Case 1 - method finalize of class Router
    def testcase1():
        router._dynamic_routes = {
            0: Route(
                RouteHandler(None, None, None, None),
                labels={}
            )
        }
    assertRaises(SanicException, testcase1)

    # Case 2 - method finalize of class Router
    def testcase2():
        router._dynamic_routes = {
            0: Route(
                RouteHandler(None, None, None, None),
                labels={"abc": None}
            )
        }
        router.finalize()

# Generated at 2022-06-14 07:55:59.356456
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    

# Generated at 2022-06-14 07:56:05.708051
# Unit test for constructor of class Router
def test_Router():
    uri = "/post/<id>"
    methods = ["GET", "POST"]
    handler = "<id>"
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False
    router = Router()


# Generated at 2022-06-14 07:56:09.356678
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}

# Generated at 2022-06-14 07:56:10.018499
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 07:56:23.377661
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    uri = "/__test"
    route = router.add(uri, ["GET"])
    try:
        router.finalize()
    except Exception as e:
        assert e.__class__.__name__ == "SanicException"
    uri = "/test"
    route = router.add(uri, ["GET"])
    router.finalize()
    assert route.path == uri
    assert route.methods == ["GET"]
    assert len(router.routes_all) == 1

# Generated at 2022-06-14 07:56:34.961292
# Unit test for method finalize of class Router
def test_Router_finalize():
    
    # Create an instance of class DummyRoute
    class DummyRoute(object):
        def __init__(self, labels):
            self.labels = labels


    # Create an instance of class DummyRouterCtx
    class DummyRouterCtx(object):
        def __init__(self, app):
            self.app = app
    
    
    # Create an instance of class DummyApp
    class DummyApp(object):
        def _generate_name(self, view_name):
            return "__file_uri__"


    # Create an instance of class Router
    router = Router(DummyRouterCtx(DummyApp()))

    # Add a route to router
    router.dynamic_routes["/test_path"] = DummyRoute(["test_label"])

   

# Generated at 2022-06-14 07:56:35.597382
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    assert router.finalize() == None

# Generated at 2022-06-14 07:56:47.702011
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route(
        method='GET',
        host=None,
        labels=('__name__',),
        requirements=None,
        handler=None,
        name='',
        strict_slashes=False,
        unquote=True,
    )
    router.dynamic_routes = {'__name__': route}
    with pytest.raises(SanicException, match=r".* Invalid route: "
            r"\(GET, None, \('__name__',\), None, None, '', False, True\). "
            r"Parameter names cannot use '__'. *."):
        router.finalize()



# Generated at 2022-06-14 07:56:58.038841
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ('GET', 'POST', 'DELETE', 'PUT', 'OPTIONS', 'HEAD', 'PATCH')
    assert router.ctx == None
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.static_routes == {}
    assert router.routes == {}
    assert router.name_index == {}
    return router


# Generated at 2022-06-14 07:57:05.616810
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.dynamic_routes['xxx'] = Route(path='abc', handler=None, methods=['GET'], name=None, strict=False)
    r.dynamic_routes['xxx'].labels = ['__file_uri__', '__test__']
    try:
        r.finalize()
    except BaseException as e:
        raise SanicException

# Generated at 2022-06-14 07:57:06.424779
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:57:16.372689
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    Examples to test the finalize method in Router class
    """
    route = Router()
    # Test path of route
    uri_1 = "http://www.example.com/"
    # Test uri of method
    methods_1 = ["GET", "POST"]
    # Test the handler used in the method
    handler_1 = """
    def MyHandler(request):
        return json.dumps({"message": "Successfully processes the request"})
    """
    # Test the host used in the route
    host_1 = "localhost"
    # Test if path is strict
    strict_slashes_1 = True
    # Test if path is streamed
    stream_1 = True
    # Test if body is ignored
    ignore_body_1 = True
    # Test version of the route

# Generated at 2022-06-14 07:57:20.674632
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    uri = 'test'
    methods = ['GET']
    handler = None

    try:
        router.add(uri, methods, handler)
        router.finalize()
    except:
        pass

# Generated at 2022-06-14 07:57:26.546514
# Unit test for constructor of class Router
def test_Router():
    assert Router.ALLOWED_METHODS == ['OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']
    assert Router.DEFAULT_METHOD == 'GET'

# Generated at 2022-06-14 07:57:33.075449
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None, "Failed to create object of class Router"

# Generated at 2022-06-14 07:57:34.473113
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)

# Generated at 2022-06-14 07:57:40.801867
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) is Router
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.static_routes == {}
    assert router.ctx is None
    assert router.name_index == {}
    assert router.path_index == {}


# Generated at 2022-06-14 07:57:42.548043
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router, "Router constructor has not been implemented yet"

# Generated at 2022-06-14 07:57:44.058325
# Unit test for constructor of class Router
def test_Router():
    r=Router() # Creating object of class Router
    assert r


# Generated at 2022-06-14 07:57:51.261234
# Unit test for method finalize of class Router
def test_Router_finalize():
    def get_func(request, *args, **kwargs):
        pass

    with pytest.raises(SanicException) as excinfo:
        app_router = Router(None)

        # add a new route that is invalid
        app_router.add("/route/<__file_uri__>/<__file_uri__>", "GET", get_func)

        app_router.finalize()

    assert "Parameter names cannot use '__'." == str(excinfo.value)

# Generated at 2022-06-14 07:57:58.916882
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    class Request:
        def __init__(self, path, method):
            self.path = path
            self.method = method

    uri = '/'
    method = 'GET'
    request = Request(uri, method)
    route = router.resolve(request)
    router.finalize(uri, method, request)
    assert route[0] == uri
    assert route[1] == method
    assert route[2] == request

# Generated at 2022-06-14 07:58:00.899337
# Unit test for constructor of class Router
def test_Router():
    # Test for class Router
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:58:07.371276
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route("/")
    router = Router()

    # Test for with error
    try:
        route.labels.add("__file_uri__")
        router.finalize()
    except SanicException:
        pass

    # Test for with no error
    route.labels.remove("__file_uri__")
    router.finalize()


# Generated at 2022-06-14 07:58:16.530275
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add(uri="/path", methods=["GET", "POST"], handler="handler")
    router.finalize()

# Generated at 2022-06-14 07:58:32.733593
# Unit test for constructor of class Router
def test_Router():
    #Given
    from sanic.app import Sanic
    from sanic.request import Request
 
    app = Sanic(__name__)
    #When
    router = Router(app)
    #Then
    assert router.ctx.app == app
    assert router.ctx._routes == []
    assert router.ctx.router is router
    assert router.ctx.map is not None
    assert router.ctx.name_index == {}
    assert router.ctx._current_rule is None

# Generated at 2022-06-14 07:58:36.076842
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:58:37.427261
# Unit test for constructor of class Router
def test_Router():
  assert type(Router()) == Router

# Generated at 2022-06-14 07:58:38.984036
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 07:58:43.511996
# Unit test for method add of class Router
def test_Router_add():
    r = Router()
    r.add_handler = mock.Mock()
    r.add(uri='uri', methods=['get'], handler=callable, name='name')
    assert r.add_handler.called


# Generated at 2022-06-14 07:58:49.700417
# Unit test for constructor of class Router
def test_Router():
    assert issubclass(Router, BaseRouter)
    assert isinstance(Router, BaseRouter)
    assert isinstance(Router(), BaseRouter)
    assert isinstance(Router(), Router)
    assert isinstance(Router(), object)

# Unit testing for method _get

# Generated at 2022-06-14 07:58:59.201537
# Unit test for method finalize of class Router
def test_Router_finalize():
    from uuid import uuid4
    from sanic.models.route_params import RouteParameters
    from sanic.models.route_details import RouteDetails
    from sanic.models.route_handler import RouteHandler
    from sanic.router import Route

    def route_handler(): return

    u = str(uuid4())
    uri = f'/test/{u}'

    methods = ['GET', 'POST', 'OPTIONS']
    params = RouteParameters(uri=uri, methods=methods)
    details = RouteDetails(handler=route_handler)
    ctx = {}

    route = Route(params, details, ctx)

    router = Router()
    router.add(uri=uri, methods=methods, handler=route_handler)


# Generated at 2022-06-14 07:59:12.223794
# Unit test for constructor of class Router
def test_Router():
    # Test that it works with path and handler added
    router = Router()
    router.add("foo", ["GET"], "bar")
    route = router.find_route_by_path("foo", "GET", None)
    assert route
    assert route.path == "foo"
    assert route.handler == "bar"
    assert route.methods == ["GET"]

    # Test that it fails without path and handler
    router = Router()
    try:
        router.add("foo", ["GET"], "bar")
        assert False
    except: # noqa
        assert True

    # Test that it fails without path and handler
    router = Router()
    try:
        router.add("", ["GET"], "bar")
        assert False
    except: # noqa
        assert True

    # Test that it fails without path and handler
   

# Generated at 2022-06-14 07:59:18.344190
# Unit test for method finalize of class Router
def test_Router_finalize():
    routes = [
        Route(
            [(("GET", "HEAD"), None, None)],
            "",
            "",
            "",
            None,
            "",
            None,
            {},
            ["a"],
            "",
            None,
            None,
            [{}],
            [{}],
        )
    ]
    r = Router()
    r.dynamic_routes = routes

    r.finalize()

    # assert r.routes_dynamic == routes

# Generated at 2022-06-14 07:59:22.960729
# Unit test for constructor of class Router
def test_Router():
    from sanic.server import Sanic
    from sanic.server import HttpProtocol

    async def handler(request):
        return "test"

    app = Sanic("test_Router")
    router = Router(app, HttpProtocol)
    router.add("/abc", ['GET', 'POST'], handler)
    request, response = router.get("/abc", "GET")
    assert request.method == 'GET'
    assert request.path == '/abc'
    assert response == ('test', 200, {'Content-Length': len('test')})


# Generated at 2022-06-14 07:59:41.200220
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.path not in r.dynamic_routes
    assert r.path in r.routes
    assert r.path in r.routes_all


# Generated at 2022-06-14 07:59:48.017051
# Unit test for constructor of class Router
def test_Router():
    # create a router object
    router = Router()
    assert router.path_index == {}
    assert router.name_index == {}
    assert router.static_routes == {}
    assert router.static_routes_by_method == {}
    assert router.static_routes_by_host == {}
    assert router.static_routes_by_host_and_method == {}
    assert router.static_routes_by_host_and_method == {}
    assert router.static_routes_by_host_and_method == {}
    assert router.static_routes_by_host_and_method == {}

# Generated at 2022-06-14 07:59:51.083570
# Unit test for constructor of class Router
def test_Router():
    """
    try to initialize a Router instance
    """
    router = Router()
    assert isinstance(router, Router)



# Generated at 2022-06-14 07:59:55.911221
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router # type: ignore
    r = Router()
    r.add('/<a>/<b>/<c>', ['GET'], lambda: None)
    try:
        r.finalize()
        assert False
    except:
        assert True

# Generated at 2022-06-14 08:00:05.840120
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        route = Route('/a/<__file_uri__>', None)
        router.dynamic_routes['/a/<__file_uri__>'] = route
        router.finalize()
        assert True
    except:
        assert False
    
    try:
        router = Router()
        route = Route('/a/<__a__>', None)
        router.dynamic_routes['/a/<__a__>'] = route
        router.finalize()
        assert False
    except SanicException:
        assert True

# Generated at 2022-06-14 08:00:06.977387
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)


# Generated at 2022-06-14 08:00:13.033667
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ctx is None
    assert r.routes == {}
    assert r.static_routes == []
    assert r.dynamic_routes == {}
    assert r.regex_routes == []
    assert r.name_index == {}
    assert r.methods == ['HEAD', 'OPTIONS', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'TRACE']
    assert r.uri_template == '{path}{trailing_slash:trailing_slash?}'
    assert r.label_template == '{label}'


# Generated at 2022-06-14 08:00:24.764244
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.settings import KEEP_ALIVE_TIMEOUT

    r = Router(timeout=KEEP_ALIVE_TIMEOUT)
    r._routes_all = {1:1}
    r._routes_static = {2:2}
    r._routes_dynamic = {3:3}
    r._routes_regex = {4:4}
    r._ctx = {'app': {}}
    r._name_index = {'a':'a'}
    r._version_index = {'b':'b'}
    r._stream_index = {'c':'c'}
    r._methods_index = {'d':'d'}
    r.finalize()
    assert r._routes_all == r.routes_all

# Generated at 2022-06-14 08:00:36.634976
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ctx is None
    assert r._get_prepared_path("/") == "/"
    assert r._get_prepared_path("/hello") == "/hello"
    assert r._get_prepared_path("/hello?hello") == "/hello"
    assert r._get_prepared_path("/hello?hello=hello") == "/hello"
    assert r._get_prepared_path("/hello?hello/hello") == "/hello"
    assert r._get_prepared_path("/hello/") == "/hello/"
    assert r._get_prepared_path("/hello/hello") == "/hello/hello"
    assert r._get_prepared_path("/hello/hello?hello") == "/hello/hello"

# Generated at 2022-06-14 08:00:47.084514
# Unit test for constructor of class Router
def test_Router():
    import pytest

    # Call the constructor of class Router
    router = Router()

    # Check if the attributes of router are correct
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes == {}
    assert router.dynamic_routes == {}
    assert router.static_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}
    assert router.ctx == None

    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 08:01:06.917915
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []



# Generated at 2022-06-14 08:01:14.689746
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import ServerError
    from sanic.router import Router
    from sanic.response import text

    def test_handler(request):
        return text("OK")

    router = Router()
    router.add("/test", ["GET"], test_handler, "example.com")
    # Test when SanicException is raised
    try:
        router.add(
            "/test/<__file_uri__:path>", ["GET"], test_handler, "example.com"
        )
        router.finalize()
    except ServerError as e:
        assert e.status_code == 500
        assert e.args[0] == (
            "Invalid route: /test/<__file_uri__:path>?. Parameter names cannot use '__'."
        )

    # Test when everything is correct
   

# Generated at 2022-06-14 08:01:20.756109
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    with pytest.raises(Exception) as excinfo:
        r.finalize()
    assert 'Invalid route' in str(excinfo.value)
    assert 'Parameter names cannot use ' in str(excinfo.value)

# Test for method find_route_by_view_name of class Router

# Generated at 2022-06-14 08:01:27.841186
# Unit test for method add of class Router
def test_Router_add():
    def handler():
        return ""

    router = Router()

    # Test case 1
    uri = "/test"
    methods = ["GET"]
    handler = handler
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False
    returned_value = router.add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)
    expected_value = Router.add(router, uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)
    assert returned_value == expected_value

# Generated at 2022-06-14 08:01:40.659007
# Unit test for constructor of class Router
def test_Router():
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from route_handler import handle_route

    request = Request(path='/')
    router = Router()

    @router.add('/', ['GET', 'POST', 'OPTIONS'], handle_route, host='localhost', strict_slashes=False, 
    stream=False, ignore_body=False, version=None, name=None, unquote=False, static=False)
    def testing_route(request):
        return HTTPResponse(text='Testing!')

    # Add a test route to the router
    a, b, c = router.get(path=str('/'), method=str('GET'), host=str('localhost'))
    print(router.routes_all)

# Generated at 2022-06-14 08:01:43.908203
# Unit test for method add of class Router
def test_Router_add():
    # This function aims to test the Router class method add
    # If everything works well, it should return the following
    # If a error occurs, it would return the corresponding error
    router = Router()
    return router.add('/add/', 'POST', 'add')


# Generated at 2022-06-14 08:01:58.276619
# Unit test for constructor of class Router
def test_Router():
    method = "GET"
    path = "test"
    host = "localhost"
    base_router = BaseRouter()
    route = Route(
        "router", RouteHandler, base_router, "test", ("test",),
        (), {}, {}, name="test", method="GET"
    )
    router = Router()
    assert isinstance(router, Router)

    # get
    try:
        router.get(path, method, host)
    except Exception:
        pass
    except NotFound:
        pass
    except MethodNotSupported:
        pass

    # add
    try:
        router.add(
            path, (method, ), RouteHandler, host
        )
    except Exception:
        pass

    # find_route_by_view_name

# Generated at 2022-06-14 08:02:04.500870
# Unit test for constructor of class Router
def test_Router():

    # Test 1:
    # Checking if the attributes of the router are stored correctly
    router = Router()
    assert router.dynamic_routes == {}
    assert router.static_routes == {}
    assert router.regex_routes == {}
    assert router.routes == {}
    assert router.name_index == {}

    #Test 2:
    # Making sure the router is of type BaseRouter
    assert isinstance(router, BaseRouter)

# Generated at 2022-06-14 08:02:05.871697
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Generated at 2022-06-14 08:02:18.969336
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    # __eq__ & __hash__ && __repr__
    assert router.__eq__(router)
    assert isinstance(router, BaseRouter)
    assert router.__hash__() == hash(router)
    assert isinstance(router.__repr__(), str)
    # dict
    assert isinstance(router.path_index, dict)
    assert isinstance(router.dynamic_routes, dict)
    assert isinstance(router.static_routes, dict)
    assert isinstance(router.name_index, dict)
    # instance
    assert isinstance(router.regex_routes, List[Route])
    assert isinstance(router.routes, dict)

# Generated at 2022-06-14 08:02:35.193076
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:02:37.647200
# Unit test for method finalize of class Router
def test_Router_finalize():
    class MyRouter(Router):
        pass
    mr = MyRouter()
    mr.finalize()

# Generated at 2022-06-14 08:02:51.965132
# Unit test for method add of class Router
def test_Router_add():
    from sanic import Sanic
    from sanic_routing_path import SanicRoutingPath
    app = Sanic('sanic-testing')
    srp = SanicRoutingPath(app)
    
    logger = logging.getLogger() 

    class RootController:
        def get(self):
            return 'I\'m root'

    def hello():
        return 'Hello'

    # Test a
    srp.add('/', RootController.get, methods=['get'])
    route_a, handler_a, args_a = srp.get('/', 'GET', None)
    logger.debug('handler_a: %s', handler_a)
    assert True

    # Test b
    srp.add('/hello', hello, methods=['get'])
    route_b, handler_b,

# Generated at 2022-06-14 08:02:53.168271
# Unit test for constructor of class Router
def test_Router():
    global router
    router = Router(None)
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:02:55.296558
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:02:59.000397
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
        print("Create Router object successfully")
    except Exception as e:
        print("Fail to create Router object")
        print(e)


# Generated at 2022-06-14 08:03:00.933933
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:03:01.914944
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert True

# Generated at 2022-06-14 08:03:10.473418
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route("/hello/<world>", None)
    route.labels = ["world"]
    router = Router()
    router.dynamic_routes["/hello"] = [route]
    router.finalize()
    assert router.dynamic_routes["/hello"][0].labels == ["world"]

    route.labels.append("__secret")
    with pytest.raises(SanicException, match=r".*'__'."):
        router.finalize()

# Generated at 2022-06-14 08:03:23.489844
# Unit test for method finalize of class Router
def test_Router_finalize():
    def handler(request):
        pass
    uri  = "/"
    methods = ("GET", "POST", "OPTIONS")
    router = Router()
    router.add(uri, methods, handler)
    host = 'www.example.com'
    router.add(uri, methods, handler, host= host)
    try:
        router.finalize()
    except SanicException as e:
        assert "Invalid route: " in str(e)
    try:
        router.add("/__file_uri__/route", methods, handler)
        router.finalize()
    except SanicException as e:
        assert "Invalid route: " in str(e)

# Generated at 2022-06-14 08:03:54.029716
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert(router.ctx.app == None)
    assert(router.ctx.existing_router == None)


# Generated at 2022-06-14 08:03:55.693811
# Unit test for constructor of class Router
def test_Router():
    _Router = Router()
    assert _Router.ctx == {'app': None}

# Generated at 2022-06-14 08:04:03.042312
# Unit test for method add of class Router
def test_Router_add():
    from sanic import Sanic, response
    from sanic_routing import Router as RoutingRouter
    app = Sanic(__name__)
    router = RoutingRouter(app)
    
    router.add(uri='/', methods=['GET'], handler=lambda : response.text('hello'))
    request, _ = app.test_client.get('/')
    assert request.status == 200
    
    
if __name__ == '__main__':
    test_Router_add()

# Generated at 2022-06-14 08:04:11.116724
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    from sanic.response import text

    app = Sanic('name')

    @app.route("/<name:string>")
    async def handler(request, name):
        pass

    with pytest.raises(SanicException):
        app.router.find_all_routes()

    app.router.finalize()
    app.router.find_all_routes()

# Generated at 2022-06-14 08:04:22.118973
# Unit test for constructor of class Router
def test_Router():
    new_router = Router()
    assert new_router.DEFAULT_METHOD == 'GET'
    assert new_router.ALLOWED_METHODS == ('OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'TRACE')
    assert new_router.templates == {}
    assert new_router.dynamic_routes == {}
    assert new_router.static_routes == {}
    assert new_router.routes == {}
    assert new_router.name_index == {}
    assert new_router.regex_routes == {}


# Generated at 2022-06-14 08:04:26.069862
# Unit test for method finalize of class Router
def test_Router_finalize():
    class RouterTest(BaseRouter):
        pass
    routerTest = RouterTest()
    assert routerTest.finalize("*", "*", None, None) is None

# Generated at 2022-06-14 08:04:29.566363
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass
    # method = getattr(Router, "finalize", None)
    # assert callable(method), "No method 'finalize' found"

# Generated at 2022-06-14 08:04:32.894825
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)


# Generated at 2022-06-14 08:04:46.323287
# Unit test for constructor of class Router

# Generated at 2022-06-14 08:04:49.989420
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert isinstance(router, BaseRouter)
    assert isinstance(router, set)

