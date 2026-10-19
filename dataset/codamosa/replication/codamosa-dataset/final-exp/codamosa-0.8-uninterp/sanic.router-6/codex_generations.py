

# Generated at 2022-06-14 07:55:49.030539
# Unit test for constructor of class Router
def test_Router():
    def say_hello(request):
        return text('{"message": "Hello!"}')

    # Test GET request
    router = Router()
    router.add('/hello', ['GET'], say_hello)
    assert router.find_route_by_view_name('hello') is not None

    # Test POST request
    router.add('/hello', ['POST'], say_hello)
    assert router.find_route_by_view_name('hello') is not None

    # Test DELETE request
    router.add('/hello', ['DELETE'], say_hello)
    assert router.find_route_by_view_name('hello') is not None


# Generated at 2022-06-14 07:55:50.235256
# Unit test for constructor of class Router
def test_Router():
    assert Router.__base__ == BaseRouter

# Generated at 2022-06-14 07:56:04.022474
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route('/user/enigma/<name>',None) # type: ignore
    route.labels = ['name', '__file_uri__']
    router = Router()
    router.dynamic_routes = [route]
    router.finalize()
    assert len(router.routes) == 1
    assert router.routes[0].labels == ['name', '__file_uri__']

    route = Route('/user/<name>', None) # type: ignore
    route.labels = ['name', '__file_uri__']
    router = Router()
    router.dynamic_routes = [route]
    try:
        router.finalize()
    except SanicException:
         raise Exception("Router.finalize should not raise SanicException")

test_R

# Generated at 2022-06-14 07:56:13.029999
# Unit test for constructor of class Router
def test_Router():
	R = Router()
	assert R.ctx == None
	assert R.all_methods == ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD']
	assert R.all_methods_set == {'GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'}
	assert R.name_index == {}
	assert R.static_routes == {}
	assert R.static_routes_prefix_index == {}
	assert R.static_routes_index == {}
	assert R.dynamic_routes == {}
	assert R.dynamic_routes_index == {}
	assert R.regex_routes == []
	assert R.regex_routes_index == []
	

# Generated at 2022-06-14 07:56:15.866307
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:56:17.192088
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r != None

# Generated at 2022-06-14 07:56:29.870834
# Unit test for constructor of class Router
def test_Router():
    from sanic.request import Request
    router = Router()
    router.add(uri='/', methods=('GET', 'HEAD'), handler=None)
    router.add(uri='/test/', methods=('GET', 'HEAD'), handler=None)
    router.add(uri='/test/12/', methods=('GET', 'HEAD'), handler=None)
    method = 'GET'
    path = '/'
    host = None
    router.get(path=path, method=method, host=host)
    # test wrong arguments
    # router.get(path=path, methods=method, host=host)
    # router.get(path=path, method=method, hosts=host)
    # router.get(paths=path, method=method, host=host)
    # router.get(path=path, methods=

# Generated at 2022-06-14 07:56:40.884664
# Unit test for method finalize of class Router
def test_Router_finalize():
    aname = '__file_uri__'
    route1 = Route(
        path='/',
        handler=RouteHandler(),
        methods=['1'],
        name='',
        strict=False,
        unquote=False
    )
    route1.labels.append(aname)
    r = Router()
    r.dynamic_routes.values().append(route1)
    r.finalize()

    route2 = Route(
        path='/',
        handler=RouteHandler(),
        methods=['1'],
        name='',
        strict=False,
        unquote=False
    )
    route2.labels.append('__file_uri')
    r.dynamic_routes.values().append(route2)

# Generated at 2022-06-14 07:56:48.636727
# Unit test for method finalize of class Router
def test_Router_finalize():
    app = Sanic(__name__)

    @app.route("/")
    def handler(request):
        return text("OK")

    singleton = Router(app)
    singleton._add_route(Route(
        name="test",
        path="/",
        handler=handler,
        methods=["GET"],
        strict=False,
        unquote=False,
        ctx=None,
        labels={"__file_uri__": "."},
    ))
    singleton.finalize()

# Generated at 2022-06-14 07:56:50.443033
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Router()
    assert route.finalize


# Generated at 2022-06-14 07:57:00.678541
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(None)
    route = Route("/", "GET", lambda x: x, "file_uri")
    route.labels.update({"__file_uri__":"/"})
    router.routes_dynamic[("GET","/")] = route
    router.finalize()
    assert router.routes_dynamic[("GET","/")] is route

# Generated at 2022-06-14 07:57:06.685151
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        
        @router.route('/test', methods=['GET'])
        def handler(request):
            return text('OK')
        
        router.finalize()
    except Exception as e:
        pytest.fail(f"Failed with: {e}")


# Generated at 2022-06-14 07:57:08.058443
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 07:57:17.257378
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic import Sanic

    def test_route():
        pass

    app = Sanic(__name__)
    app.add_route(test_route, "/test/<label>")
    app.add_route(test_route, "/test/<__file_uri__>")
    app.add_route(test_route, "/test/<__label__>")

    with pytest.raises(SanicException):
        app.router.finalize()

# Generated at 2022-06-14 07:57:20.496144
# Unit test for constructor of class Router
def test_Router():
    try:
        r = Router() # create a new instance of class Router
        r.finalize()
    except:
        assert False
    assert True


# Generated at 2022-06-14 07:57:26.912958
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.find_route_by_view_name('') == None
    assert router._DEFAULT_METHOD == "GET"

# Generated at 2022-06-14 07:57:36.872466
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.server import HttpProtocol
    app = Sanic('test_Router_finalize')
    # Initialize the app
    app.error_handler = {}
    app.listeners = defaultdict(list)
    app.before_server_start = []
    app.before_server_stop = []
    app.before_request = []
    app.after_request = []
    app.middleware = []
    app.request_middleware = []
    app.response_middleware = []
    app.config = {"REQUEST_MAX_SIZE": 104857600, "REQUEST_TIMEOUT": 60, "KEEP_ALIVE": True, "KEEP_ALIVE_TIMEOUT": 5}
    # Finalize the app
    app.router = Router(app)
   

# Generated at 2022-06-14 07:57:38.181943
# Unit test for constructor of class Router
def test_Router():
    pass


# Generated at 2022-06-14 07:57:42.463315
# Unit test for constructor of class Router
def test_Router():
    """
    Test of constructor of class Router.
    """
    router = Router()
    assert router is not None

    for method in HTTP_METHODS:
        assert hasattr(router, method.lower())


# Generated at 2022-06-14 07:57:46.137912
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    router.add("/", ["GET"], lambda r: r)
    router.add("/", ["POST"], lambda r: r)
    router.add("/", ["DELETE"], lambda r: r)


# Generated at 2022-06-14 07:58:04.390489
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.ag_sanic_routing import Route
    from unittest.mock import MagicMock, patch

    args = MagicMock()
    kwargs = dict(
        path="path",
        methods=["GET", "POST", "OPTIONS"],
        handler=MagicMock(),
        name="name",
        strict=False,
        unquote=False
    )

    # child __init__ of parent class BaseRouter
    def side_effect(cls, *args, **kwargs):
        cls.ctx = MagicMock()
        cls.ctx.app = MagicMock()
        cls.ctx.app._generate_name = MagicMock(return_value="name_full")
        cls.routes = []
        cls.static_routes = {}
       

# Generated at 2022-06-14 07:58:08.108607
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    router.add("/", ["POST", "GET"], "jdfglfd")
    assert router.routes_all.get("jdfglfd").uri == "/"

# Generated at 2022-06-14 07:58:15.899950
# Unit test for constructor of class Router
def test_Router():
    def fun(req):
        return None

    r1 = Router()
    r1.add('/', ['GET', 'POST'], fun)
    r1.add('/v1.0/', ['GET', 'POST'], fun, version='1.0')
    r1.add('/v2.0/', ['GET', 'POST'], fun, version='2.0', host='example.com')
    routes = r1.routes_all
    assert len(routes) == 3

# Generated at 2022-06-14 07:58:17.588449
# Unit test for constructor of class Router
def test_Router():
    obj = Router(None)
    assert isinstance(obj, Router)

# Generated at 2022-06-14 07:58:25.963771
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.app == None
    assert router.index == {}
    assert router.regex_routes == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.all_methods == HTTP_METHODS
    assert router.regex_routes_ordered == []
    assert router.name_index == {}
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == []
    assert router.routes_regex == []



# Generated at 2022-06-14 07:58:37.442594
# Unit test for constructor of class Router
def test_Router():
    rt = Router()
    rt.DEFAULT_METHOD = "POST"
    rt.ALLOWED_METHODS = ['POST', 'OPTIONS']

    def f1():
        return "hello"


# Generated at 2022-06-14 07:58:42.151240
# Unit test for constructor of class Router
def test_Router():
    assert Router
    router = Router()
    assert router
    assert isinstance(router, Router)
    assert router.DEFAULT_METHOD == "GET" , "Router default method must be 'GET'"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.routes_all == {}
    assert router.routes_static == {}

# Generated at 2022-06-14 07:58:55.643398
# Unit test for constructor of class Router

# Generated at 2022-06-14 07:58:59.519482
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == 'GET'
    assert r.ALLOWED_METHODS == HTTP_METHODS
    print("Test Success!\n")


# Generated at 2022-06-14 07:59:00.166088
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:59:10.996748
# Unit test for constructor of class Router
def test_Router():
    pass



# Generated at 2022-06-14 07:59:16.273802
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    # Test: Should run without errors
    router.finalize()

    # Test: Should raise SanicException
    router.dynamic_routes = {'test': None}
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 07:59:25.774400
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    route1 = Route(path='/test1', handler=None, methods=['GET'])
    router.dynamic_routes['test1'] = route1
    router.finalize()

    assert router.dynamic_routes['test1'] == route1

    route2 = Route(path='/test2', handler=None, methods=['GET'])
    router.dynamic_routes['test2'] = route2
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 07:59:27.922923
# Unit test for constructor of class Router
def test_Router():
# Create instance of class Router
    router = Router()
print("Instance of class Router created")

# Generated at 2022-06-14 07:59:29.682372
# Unit test for constructor of class Router
def test_Router():
    """Unit test for constructor of class Router."""
    assert 'Router' == Router.__name__

# Generated at 2022-06-14 07:59:41.051913
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.app is None
    assert router.ctx.name is None
    assert router.ctx.hosts is None
    assert router.ctx.stream is None
    assert router.ctx.ignore_body is None
    assert router.ctx.static is None
    assert router.ctx.strict_slashes is None
    assert router.ctx.unquote is None
    assert router.ctx.methods is None
    assert router.ctx.name_index is None
    assert router.ctx.strict_slashes is not None
    assert router.ctx.unquote is not None



# Generated at 2022-06-14 07:59:42.905748
# Unit test for constructor of class Router
def test_Router():
    """
    Test construction of class Router
    """
    x = Router()
    assert x is not None


# Generated at 2022-06-14 07:59:56.864604
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.api import SanicAPI, Blueprint
    from sanic.exceptions import SanicException

    app = SanicAPI(__name__)
    app_bp = Blueprint('app')
    app_bp.add_route(app.get, '/test', {})
    app.blueprint(app_bp)

    try:
        app_bp._router.finalize()
    except SanicException as exc:
        assert '__' in str(exc)
        assert 'Param' in str(exc)
        assert 'names' in str(exc)
        assert 'cannot use' in str(exc)

    app = SanicAPI(__name__)
    app.add_route(app.get, '/test', {})

# Generated at 2022-06-14 08:00:07.827326
# Unit test for method finalize of class Router
def test_Router_finalize():
    route_1=Route(uri='/', methods=['GET'], handler=lambda request : print(request), name='a', strict=False, unquote=False)
    route_2=Route(uri='/', methods=['GET'], handler=lambda request : print(request), name='b', strict=False, unquote=False)
    
    routes = {'a':route_1,'b':route_2}
    routes_regex = {}
    routes_static = {}
    
    #check exception
    router = Router(None)
    router.routes_dynamic = routes
    router.routes_regex = routes_regex
    router.routes_static = routes_static

# Generated at 2022-06-14 08:00:12.708739
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.response import text
    app = Sanic(__name__)

    @app.route('/route/<param:string>')
    async def route(request, param):
        return text(param)

    router = Router(app, strict_slashes=False)
    router.add("/route/<param:string>", ["GET"], route)
    # the test should pass
    router.finalize()

test_Router_finalize()

# Generated at 2022-06-14 08:00:35.599407
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add("/", ["GET"], None)
    router.add("/<param>", ["GET"], None)

    router.finalize()

# Generated at 2022-06-14 08:00:37.541630
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 08:00:44.032872
# Unit test for constructor of class Router
def test_Router():
    obj=Router()
    assert isinstance(obj.routes, dict)
    assert isinstance(obj.static_routes, dict)
    assert isinstance(obj.dynamic_routes, dict)
    assert isinstance(obj.regex_routes, dict)
    assert isinstance(obj.name_index, dict)
    assert isinstance(obj.ctx, object)


# Generated at 2022-06-14 08:00:49.874793
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.get is not None
    assert r.add is not None
    assert r.routes_all is not None
    assert r.routes_static is not None
    assert r.routes_dynamic is not None
    assert r.routes_regex is not None
    assert r.finalize is not None

# Generated at 2022-06-14 08:01:02.510466
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    # test for forbidden labels
    route = Route(
        uri="/foo/bar",
        methods=["GET", "POST"],
        handler=lambda: "OK",
        strict_slashes=False,
        name="__file_uri__",
    )

    router.dynamic_routes = {b"best": route}
    router.finalize()

    # test for forbidden labels
    route = Route(
        uri="/foo/bar",
        methods=["GET", "POST"],
        handler=lambda: "OK",
        strict_slashes=False,
        name="__something",
    )

    router.dynamic_routes = {b"best": route}

    with pytest.raises(SanicException) as excinfo:
        router.finalize()

# Generated at 2022-06-14 08:01:05.915169
# Unit test for constructor of class Router
def test_Router():
  
    # Setup
    '''
    r = Router()
    r.finalize()
    '''
    
    # Assert
    '''
    assert r != None, "Router instance cannot be created."
    '''

# Generated at 2022-06-14 08:01:14.295057
# Unit test for method finalize of class Router
def test_Router_finalize():
    with pytest.raises(SanicException):
        router = Router()
        route = Route(
            path=r"/",
            methods={"GET"},
            handler=lambda req: None,
            name=None,
            strict=False,
            unquote=False,
            labels=["__file_uri__"],
        )

        # Unit test for method new of class Route
        def test_Route_new():
            assert getattr(route, "path") == r"/"
            assert getattr(route, "methods") == {"GET"}
            assert getattr(route, "handler")(None) == None
            assert getattr(route, "name") == None
            assert getattr(route, "strict") == False
            assert getattr(route, "unquote") == False

# Generated at 2022-06-14 08:01:25.495571
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic_routing.route import Route
    from sanic_routing.constants import HttpMethods

    # set up a router
    router = Router()

    # add a route with a parameter label starting with '__'
    uri = "/invalid/<__foo>"
    method = HttpMethods.GET
    handler = None
    route = Route(uri, method, handler, router)
    router.dynamic_routes[uri] = route

    try:
        # call finalize
        router.finalize()
    except SanicException as exception:
        # assert that the expected exception is raised
        assert "Parameter names cannot use '__'." == str(exception)
    else:
        # assert that the exception is raised
        pytest.fail("Exception not raised")


# Generated at 2022-06-14 08:01:31.146717
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add('/users/<id:int>', ['GET'], None)
    assert r.finalize() == None
    # r.add('/users/<id:int>', ['GET'], None)
    # assert r.finalize() == None

# Generated at 2022-06-14 08:01:32.893340
# Unit test for constructor of class Router
def test_Router():
    assert Router()


# Generated at 2022-06-14 08:01:50.841150
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(app_ctx=None)
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 08:01:52.199917
# Unit test for constructor of class Router
def test_Router():
    _ = Router()
    return

# Generated at 2022-06-14 08:02:02.254652
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.ctx = Router.Ctx(app=None)
    r.ctx.app.config.RESPONSE_TIMEOUT = 30
    r.ctx.app.config.REQUEST_TIMEOUT = 15
    r.routes_all = {
        "http://example/get": Route(
            path="/get",
            handler=None,
            methods=['GET'],
            name=None,
            strict=False,
            unquote=False,
            uri='/get',
            regex=re.compile(r'^/get$'),
            regex_str='^/get$',
            labels=set(),
            param_count=0,
            param_tokens=tuple(),
            static=True,
            ctx=Route.Ctx(),
        )
    }

# Generated at 2022-06-14 08:02:05.236162
# Unit test for constructor of class Router
def test_Router():
    test = Router()
    assert test.DEFAULT_METHOD == "GET"
    assert test.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:02:17.235963
# Unit test for constructor of class Router
def test_Router():
    from sanic.response import json

    router = Router()
    route1 = router.add(uri='/test1', methods=["GET"], handler=json({"a": "b"}))
    route2 = router.add(uri='/test2', methods=["GET"], handler=json({"a": "b"}))
    router.add(uri='/test3', methods=["GET"], handler=json({"a": "b"}))
    assert router.routes_all == [route1, route2]
    assert router.routes_static == [route1]
    assert router.routes_dynamic == [route2]
    assert router.routes_regex == []

# Generated at 2022-06-14 08:02:20.460539
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router), "Failed to initialize router."

# Generated at 2022-06-14 08:02:23.798878
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.exceptions import SanicException

    router = Router

    assert router.finalize(router) == True

# Generated at 2022-06-14 08:02:26.596797
# Unit test for constructor of class Router
def test_Router():
    router = Router(host="host", prefix="prefix")
    assert router.host == "host"
    assert router.prefix == "prefix"


# Generated at 2022-06-14 08:02:36.485892
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.router import Router
    from sanic.response import text
    from sanic.exceptions import SanicException

    app = Sanic('test_Router_finalize')

    @app.route('/')
    async def handler(request):
        return text('OK')

    @app.route('/<__x:int>')
    async def handler(request):
        return text('OK')

    #@app.route('/<__x:str>')
    @app.route('/<_x:str>')
    async def handler(request):
        return text('OK')

    router = Router(app)
    router.add_route(uri='/', methods=['GET'], handler=handler)
    #router.add_route(uri='/<__x

# Generated at 2022-06-14 08:02:50.991018
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from pytest import raises

    with raises(SanicException):
        # Use the default supported method
        Router().add('/', 'GET', lambda _: None)

    with raises(SanicException):
        Router().add('/', ['GET'], lambda _: None)

    with raises(SanicException):
        Router().add('/', HTTP_METHODS, lambda _: None)

    with raises(SanicException):
        Router().add('/', ['__'], lambda _: None)

    with raises(SanicException):
        Router().add('/', ['__'], lambda _: None)

    with raises(SanicException):
        Router().add('/', '__', lambda _: None)


# Generated at 2022-06-14 08:03:33.252382
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.constants import HTTP_METHODS
    from sanic.exceptions import SanicException
    # - setup -
    uri = "/test/"
    methods = HTTP_METHODS
    def handler(): return
    host = None
    router = Router()
    router.add(uri=uri, methods=methods, handler=handler, host=host)
    # - assert -
    try:
        router.finalize()
    except SanicException:
        pass
    else:
        assert False, "should raise SanicException, but not"

    # - reset -
    uri = "/test/{param}"
    router = Router()
    router.add(uri=uri, methods=methods, handler=handler, host=host)
    # - assert -

# Generated at 2022-06-14 08:03:38.374598
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    def add(a,b):
        return a+b
    router.add("/test/a",["GET"],add,name="route1")

    def add2(a,b):
        return a+b
    router.add("/test/a",["GET"],add2,name="route1")

    router.finalize()

# Generated at 2022-06-14 08:03:49.237386
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert Router.DEFAULT_METHOD == "GET"
    assert Router.ALLOWED_METHODS == HTTP_METHODS
    assert Router.ROUTER_CACHE_SIZE == 1024
    assert Router.ALLOWED_LABELS == ("__file_uri__",)
    assert router.dynamic_routes == {}
    assert router.regex_routes == []
    assert router.static_routes == {}
    assert router.routes == []
    assert router.name_index == {}
    assert router.ctx == {}
    assert isinstance(router.name_index, dict)
    assert isinstance(router.ctx, dict)


# Generated at 2022-06-14 08:03:53.867997
# Unit test for constructor of class Router
def test_Router():
    """
    Test the constructor of class Router
    """
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == {}
    assert router.routes_dynamic == []
    assert router.routes_regex == []

# Generated at 2022-06-14 08:03:59.350186
# Unit test for constructor of class Router
def test_Router():
    """
    Test constructor of class Router
    """
    router = Router()
    assert router.ctx == None
    assert router.dynamic_routes == []
    assert router.regex_routes == []
    assert router.static_routes == []


if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 08:04:11.774864
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    from sanic.router import Router

    def test_case(path):
        class App(Sanic):
            async def handle_request(self, request, *args, **kwargs):
                return

        app = App(__name__)
        app.router = Router(app)
        app.router.add(path, ["get"], lambda x: "", defaults={"__key__": 1})
        with pytest.raises(SanicException):
            app.router.finalize()
        pass

    test_case('/<__key__:int>/<num:int>')
    test_case('/<__file_uri__:path>/<num:int>')
    pass

# Generated at 2022-06-14 08:04:13.490843
# Unit test for constructor of class Router
def test_Router():
    dynamic_Router = Router()

# Generated at 2022-06-14 08:04:16.425600
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert isinstance(router, BaseRouter)

# Generated at 2022-06-14 08:04:18.351077
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:04:32.571557
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ('OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')
    assert router.routes_all == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.routes_static == []
    assert router.name_index == {}

if __name__ == '__main__':
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ('OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')
    assert router.routes_all == []
   

# Generated at 2022-06-14 08:05:35.380415
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic
    try:
        router = Router(Sanic())
    except Exception as e:
        print(e)
        assert False
    else:
        assert True