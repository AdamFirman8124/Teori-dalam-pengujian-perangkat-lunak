

# Generated at 2022-06-14 07:55:47.365719
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import SanicException
    from sanic.router import Router
    from sanic.models.route import Route
    from sanic_routing.route import Route
    router = Router()
    route = Route("")
    route.name = "__test__"
    route.labels.append("__test__")
    router.dynamic_routes[route.name] = route
    with pytest.raises(SanicException):
        assert router.finalize()

# Generated at 2022-06-14 07:55:50.511001
# Unit test for method finalize of class Router
def test_Router_finalize():
    _finalize = Router.finalize.__func__
    _Router__finalize = Router.__finalize__.__func__
    return _finalize, _Router__finalize

# Generated at 2022-06-14 07:55:59.937396
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    class _Route():
        labels = ["__file_label__", "__file_uri__"]
    route = _Route()
    route.labels = ["__file_label__", "__file_uri__"]
    router.dynamic_routes[""] = route
    with pytest.raises(SanicException):
        route.labels = ["__file_label__", "__file_uri__", "__invalid__"]
        router.dynamic_routes[""] = route
        router.finalize()

# Generated at 2022-06-14 07:56:00.684024
# Unit test for constructor of class Router
def test_Router():
    assert Router


# Generated at 2022-06-14 07:56:03.162935
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    try:
        router.finalize()
    except ValueError:
        return True
    return False

# Generated at 2022-06-14 07:56:03.857066
# Unit test for constructor of class Router
def test_Router():
    r = Router()

# Generated at 2022-06-14 07:56:08.418728
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == ('GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE')


# Generated at 2022-06-14 07:56:12.400864
# Unit test for constructor of class Router
def test_Router():
    router=Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:56:22.831863
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    router.add("/", ['GET'], None, None, False, False, False, None)
    assert router.static_routes != None
    assert router.static_routes != {}
    assert router.static_routes != []
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.all_routes == {}
    assert router.routes_all != None
    assert router.routes_all != []
    assert router.routes_all != {}
    assert router.routes_static != None
    assert router.routes_static != []
    assert router.routes_static != {}
    assert router.routes_dynamic != None
    assert router.routes_dynamic

# Generated at 2022-06-14 07:56:28.593439
# Unit test for method finalize of class Router
def test_Router_finalize():
    routes = {}
    static_routes = {}
    regex_routes = {}
    name_index = {}
    ctx = {}
    finalize = Router.finalize
    finalize(Router, routes, static_routes, regex_routes, name_index, ctx)


# Generated at 2022-06-14 07:56:34.745206
# Unit test for constructor of class Router
def test_Router():
    test = Router()
    assert test.DEFAULT_METHOD == "GET"



# Generated at 2022-06-14 07:56:43.066288
# Unit test for constructor of class Router
def test_Router():
    from pytest import raises

    from sanic_routing.route import Route

    router = Router()
    route = Route(
        uri='/',
        ctx={},
        handler=None,
        methods=['GET'],
        name=None,
        strict=False,
        unquote=False,
        exists_conflict=None,
    )
    router.dynamic_routes[route.uri] = route
    assert len(router.dynamic_routes) == 1
    assert router.dynamic_routes[route.uri] == route

    assert router.routes_all == router.routes
    assert router.routes_static == router.static_routes
    assert router.routes_dynamic == router.dynamic_routes

# Generated at 2022-06-14 07:56:47.583295
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx is None
    assert router.routes == router.dynamic_routes == router.static_routes == router.regex_routes == {}
    assert router.name_index == {}



# Generated at 2022-06-14 07:56:49.352964
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert(type(r) == Router)


# Generated at 2022-06-14 07:57:00.841870
# Unit test for constructor of class Router
def test_Router():
    uri="/"
    methods=["POST"]
    handler="__"
    host="localhost"
    strict_slashes=False
    stream=False
    ignore_body=False
    version="v1"
    name="__"
    unquote=False
    static=False
    router=Router()
    new_router=router.add(uri,methods,handler,host,strict_slashes,stream,ignore_body,version,name,unquote,static)

# Generated at 2022-06-14 07:57:01.955406
# Unit test for constructor of class Router
def test_Router():
    return Router()

# Generated at 2022-06-14 07:57:13.439685
# Unit test for method finalize of class Router
def test_Router_finalize():

    """
    Test for the method finalize of class Router
    It should raise Exception when there are parameter names with '__'
    """
    import sys
    import os
    import inspect

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))

    from sanic.router import Router

    route = "<Route GET: /users/{__id}>"
    router = Router()
    try:
        router._find_dynamic_route(route, {})
    except:
        pass
    else:
        assert False

test_Router_finalize()

# Generated at 2022-06-14 07:57:14.668224
# Unit test for constructor of class Router
def test_Router():
    pass


# Generated at 2022-06-14 07:57:15.935180
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 07:57:17.254700
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 07:57:26.216134
# Unit test for constructor of class Router
def test_Router():
    r=Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:57:36.537046
# Unit test for method add of class Router
def test_Router_add():
  router=Router()
  def test_handler():
    return 'test_handler'
  router.add(uri='/',
             methods=['GET'],
             handler=test_handler,
             host=None,
             strict_slashes=False, 
             stream=False,
             ignore_body=False, 
             version=None,
             name=None,
             unquote=False,
             static=False)
  
  assert len(router.routes[None])==1
  assert len(router.routes[None]['GET'])==1
  assert router.routes[None]['GET'][0].handler is test_handler
  

# Generated at 2022-06-14 07:57:48.740069
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.constants import HTTP_METHODS

    @lru_cache(maxsize=ROUTER_CACHE_SIZE)
    def get(  # type: ignore
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

# Generated at 2022-06-14 07:58:01.111180
# Unit test for method finalize of class Router
def test_Router_finalize():
    class TestRouter(Router):
        def __init__(self):
            # we need to access to BaseRouter.static_routes
            # because it's a property.
            super().__init__()

    from sanic.app import Sanic
    from sanic.router import RouteExists
    from sanic.views import HTTPMethodView
    import warnings

    # RouteExists is raised if the view is added twice.
    app = Sanic(__name__)
    router = TestRouter()
    router.add(routes=[HTTPMethodView.as_view("test")])

    # This is a test right?
    app.config.set("USE_ARGUMENT_FOR_WEBSOCKET", True)


# Generated at 2022-06-14 07:58:08.166062
# Unit test for method finalize of class Router
def test_Router_finalize():
    test_router = Router()
    test_route = Route(["x"], "a", "b", "c", "d")
    test_router.dynamic_routes[0] = test_route
    test_router.finalize()
    assert all(
        label.startswith("__") and label not in ALLOWED_LABELS for label in test_route.labels
    )

# Generated at 2022-06-14 07:58:10.746806
# Unit test for constructor of class Router
def test_Router():

    assert callable(Router)

# Generated at 2022-06-14 07:58:21.069194
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Init Router
    urls = {}
    router = Router()

    # Add route with no label
    urls["test"] = "/test"
    router.add(urls["test"], methods=["GET", "HEAD", "OPTIONS"])

    # Add route with labels
    urls["test_label"] = "/test/<a>"
    router.add(urls["test_label"], methods=["GET", "HEAD", "OPTIONS"])

    # Add route with allowed label
    urls["test_label_allowed"] = "/test/<__file_uri__>"
    router.add(urls["test_label_allowed"], methods=["GET", "HEAD", "OPTIONS"])

    router.finalize()

    # Add route with not allowed label

# Generated at 2022-06-14 07:58:34.984269
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == ['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'PATCH',
                                 'DELETE', 'TRACE']

    uri = "/"
    methods = ['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'TRACE']
    handler = "abc"
    host = "abc"
    strict_slashes = False
    stream = False
    ignore_body = False
    version = 1
    name = "default name"


    # test add
    r.add(uri, methods, handler, host, strict_slashes, stream, ignore_body,
          version, name)

    # test find_route_by_view

# Generated at 2022-06-14 07:58:42.004825
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    if router.routes_all != {}:
        raise AssertionError
    if router.routes_static != set():
        raise AssertionError
    if router.routes_dynamic != {}:
        raise AssertionError
    if router.routes_regex != set():
        raise AssertionError
    if router.DEFAULT_METHOD != "GET":
        raise AssertionError
    if router.ALLOWED_METHODS != HTTP_METHODS:
        raise AssertionError
    
    

# Generated at 2022-06-14 07:58:55.306579
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic import Sanic
    from sanic.router import Router
    from sanic.constants import HTTP_METHODS
    from sanic.handlers import ErrorHandler, NotFound

    app = Sanic("test_router")

    router = Router(app)

    assert not router.routes

    for method in HTTP_METHODS:
        router.add("/0", {method}, ErrorHandler())

    for http_method in HTTP_METHODS:
        router.add("/1", {http_method}, NotFound())

    router.finalize()

    assert len(router.routes) == 0
    assert len(router.routes_all) == 0
    assert len(router.routes_static) == 0

# Generated at 2022-06-14 07:59:10.466711
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router


# Generated at 2022-06-14 07:59:16.757430
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route('/:a')
    router = Router(None, {})
    router.dynamic_routes[route.path] = route

    try:
        router.finalize()
    except SanicException:
        pass
    else:
        print('Able to finalize with invalid route')


# Generated at 2022-06-14 07:59:21.457108
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic

    app = Sanic("app")
    router = Router("app")

    assert router.ctx.app == app
    assert router.ctx.router == router
    assert router.ctx.name == "app"

# Generated at 2022-06-14 07:59:25.769213
# Unit test for constructor of class Router
def test_Router():
    # test construction of Router class
    r = Router(host='host')

    # test construction of Router class
    r = Router(host='host', name='name')

# Generated at 2022-06-14 07:59:33.002395
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.models.route import Route
    route = Route(None, None, None, None, None, None, None)
    # route.labels = ["__file_uri__", "__file__"]
    route.labels = ["__file_uri__", "__file_uri__", "__file__"]
    router = Router()
    router.dynamic_routes["a"] = route
    try:
        router.finalize()
    except SanicException as e:
        pass
        # print("test_Router_finalize: " + str(e))
    else:
        raise Exception("No SanicException is thrown!")

    route.labels = ["__file_uri__", "__file_uri__"]
    try:
        router.finalize()
    except Exception as e:
        raise e

# Generated at 2022-06-14 07:59:37.997168
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(None)
    with pytest.raises(SanicException):
        router.finalize()
        
    # pass
    router.finalize(lambda x: True)
    # fail
    router.finalize(lambda x: False)

# Generated at 2022-06-14 07:59:47.311209
# Unit test for method finalize of class Router
def test_Router_finalize():
    class ctx:
        class app:
            def _generate_name(self, _):
                return ""

    _ctx = ctx()
    
    @lru_cache(maxsize=ROUTER_CACHE_SIZE)
    def find_route_by_view_name(self, view_name, name=None):
        """
        Find a route in the router based on the specified view name.

        :param view_name: string of view name to search by
        :param kwargs: additional params, usually for static files
        :return: tuple containing (uri, Route)
        """
        if not view_name:
            return None

        route = self.name_index.get(view_name)
        if not route:
            full_name = self.ctx.app._generate_name(view_name)

# Generated at 2022-06-14 07:59:50.092407
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.allowed_methods == HTTP_METHODS


# Generated at 2022-06-14 07:59:58.730740
# Unit test for method finalize of class Router
def test_Router_finalize():
    class MockRouter(Router):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.dynamic_routes = {
                'dynamic_route': Route('/posts', lambda request: None, 'GET',
                    strict=False, name='posts'),
            }
            self.name_index = {
                'posts': Route('/posts', lambda request: None, 'GET',
                    strict=False, name='posts'),
            }

    with pytest.raises(SanicException, match="'__' is not allowed"):
        router = MockRouter()
        router.finalize()


# Generated at 2022-06-14 08:00:03.372198
# Unit test for method add of class Router
def test_Router_add():
    from sanic.request import Request

    def handler(request: Request):
        return 'handler'

    router = Router()
    route = router.add('/', 'GET', handler)
    assert type(route) == Route
    assert route.path == '/'
    assert route.method == 'GET'
    assert route.handler == handler

# Generated at 2022-06-14 08:00:38.591269
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from thespian.system.system import ThespianActorSystem
    from thespian.actors import ActorSystemMessage
    from thespian.actors import PoisonMessage
    class BaseActor:
        async def receive(self, message):
            #print("BaseActor received: {}".format(message))
            if isinstance(message, ActorSystemMessage):
                self.handleSystemMessage(message)
            else:
                self.handleUserMessage(message)

        def handleSystemMessage(self, message):
            if message.messageType == PoisonMessage:
                self.handlePoisonMessage(message)

        def handlePoisonMessage(self, message):
            pass

        def handleUserMessage(self, message):
            pass

# Generated at 2022-06-14 08:00:47.812413
# Unit test for method add of class Router
def test_Router_add():
    from sanic.request import Request
    from sanic.response import HTTPResponse

    async def handler(request: Request) -> HTTPResponse:
        return HTTPResponse(status=200, body="test")

    router = Router(None)
    result = router.add(uri="/test", methods=["GET"], handler=handler)
    assert result.path == "/test"
    assert result.handler == handler
    assert result.ctx.methods == ["GET"]
    assert result.ctx.ignore_body == False


# Generated at 2022-06-14 08:01:00.268342
# Unit test for constructor of class Router
def test_Router():
    from sanic.app import Sanic
    from sanic.request import Request

    # test creating instance of class Router
    router = Router(
        Sanic()
    )

    # test router.routes_all
    router.routes_all
    # test router.routes_static
    router.routes_static
    # test router.routes_dynamic
    router.routes_dynamic
    # test router.routes_regex
    router.routes_regex

    # test router.get
    router.get(path='/', method='GET', host='127.0.0.1')

    # test router.add
    router.add(uri='/', methods='GET', handler=None)

    # test router.find_route_by_view_name
    router

# Generated at 2022-06-14 08:01:11.269237
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.constants import HTTP_METHODS
    from sanic.models.handler_types import RouteHandler
    import pytest
    from sanic.router import Router
    from sanic.sanic import Sanic

    def foo(request):
        pass

    app = Sanic("test_Router_finalize")
    app.router.add("/foo", [HTTP_METHODS], foo)
    # pytest.raises(SanicException, app.router.add, "/foo", HTTP_METHODS, foo, [])
    app.router.add("/foo", [HTTP_METHODS], foo, [])

# Generated at 2022-06-14 08:01:15.368685
# Unit test for method finalize of class Router
def test_Router_finalize():
    path = 'http://127.0.0.1:8000'
    r = Router(path)
    assert r.finalize(path) == 'http://127.0.0.1:8000/'



# Generated at 2022-06-14 08:01:16.642082
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r

# Generated at 2022-06-14 08:01:18.236580
# Unit test for constructor of class Router
def test_Router():
    router = Router()


# Generated at 2022-06-14 08:01:21.941145
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    route = router.add('/hello/<test>', ['GET'], 'test')

test_Router_add()

# Generated at 2022-06-14 08:01:28.563830
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router

    # Testing initialization of an Router object
    router = Router()
    assert router.__class__ == Router
    assert router.routes_all == []
    assert router.routes_static == set()
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}

# Generated at 2022-06-14 08:01:30.433168
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:02:35.438887
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Case 1: Testing no error when route is as required
    router = Router()
    uri="/items/<int:item_id>"
    name="items.get_item"
    method="GET"
    handler = None
    strict_slashes=False
    router.add(uri=uri, methods=[method], handler=handler, name=name, strict_slashes=strict_slashes)
    try:
        router.finalize()
        assert True
    except Exception as e:
        assert False

    # Case 2: Testing error when route is not as required
    router = Router()
    uri="/items/<__item_id>"
    name="items.get_item"
    method="GET"
    handler = None
    strict_slashes=False

# Generated at 2022-06-14 08:02:36.766553
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 08:02:42.101700
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ["GET", 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']


# Generated at 2022-06-14 08:02:53.095302
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes['route_1'] = Route(
        '/',
        handler=None,
        methods=['GET'],
        name='',
        strict=False,
        unquote=False,
        ctx={'ignore_body': False, 'stream': False, 'hosts': [None], 'static': False},
        labels=['', ''])
    with pytest.raises(SanicException) as exception_info :
        router.finalize()
    assert str(exception_info.value) == "Invalid route: /=[GET], route_1. Parameter names cannot use '__'."

# Generated at 2022-06-14 08:03:06.976922
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    for method in HTTP_METHODS:
        router.add(
            "/path",
            methods=[method],
            handler=None,
        )

    router.finalize()

    for route in router.routes_static.values():
        assert isinstance(route, Route)

    for route in router.routes_dynamic.values():
        assert isinstance(route, Route)

    for route in router.routes_regex.values():
        assert isinstance(route, Route)

    assert len(router.routes_static) == 1
    assert len(router.routes_dynamic) == 0
    assert len(router.routes_regex) == 0


# Generated at 2022-06-14 08:03:11.050054
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {
        1: Route("example", path="/{foo}/{bar}", handler=lambda: None)
    }

# Generated at 2022-06-14 08:03:12.318609
# Unit test for constructor of class Router
def test_Router():
    obj = Router()
    assert obj


# Generated at 2022-06-14 08:03:19.957151
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    try:
        router = Router()
        router.add('/home', ['POST', 'GET'], lambda x: x)
        router.add('/home/<name>', ['POST', 'GET'], lambda x: x)
        router.add('/home/<name__file_uri__>', ['POST', 'GET'], lambda x: x)
        router.add('/home/<name__>', ['POST', 'GET'], lambda x: x)
        router.finalize()
    except Exception as ex:
        print('Exception Caught: ', ex)


# Generated at 2022-06-14 08:03:28.654781
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    router.add(uri='/',methods='GET',handler='handler',host='host',strict_slashes=False,stream=False,ignore_body=False,version=None,name=None,unquote=False,static=False)
    assert router.routes_all == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []
    assert router.routes_static == []


# Generated at 2022-06-14 08:03:32.012326
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert router.routes == []
    assert router.static_routes == []
    assert router.dynamic_routes == {}
    assert router.regex_routes == []

# Generated at 2022-06-14 08:05:20.849021
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)

# Generated at 2022-06-14 08:05:25.153223
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router != None
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 08:05:27.450712
# Unit test for constructor of class Router
def test_Router():
    # no error
    router = Router(ctx=None)


# Generated at 2022-06-14 08:05:30.609342
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {'dynamic_route': 2}

    with raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 08:05:34.016120
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS