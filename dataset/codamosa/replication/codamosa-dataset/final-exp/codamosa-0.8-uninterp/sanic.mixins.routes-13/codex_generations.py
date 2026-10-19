

# Generated at 2022-06-14 07:40:24.216103
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test')
    app.config.REQUEST_TIMEOUT = 10
    app.config.RESPONSE_TIMEOUT = 15

    class TestRouteMixin(RouteMixin):
        """docstring for TestRouteMixin"""
        def __init__(self):
            super(TestRouteMixin, self).__init__()

    route_mixin = TestRouteMixin()
    route_mixin.config.REQUEST_TIMEOUT = app.config.REQUEST_TIMEOUT
    route_mixin.config.RESPONSE_TIMEOUT = app.config.RESPONSE_TIMEOUT

    @route_mixin.add_route('/test', methods=['GET'])
    def handler1(request):
        pass


# Generated at 2022-06-14 07:40:35.238421
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    #define parameters
    app = Sanic("test_RouteMixin_route")
    uri = "test_RouteMixin_route"
    host = None
    methods = None
    strict_slashes = None
    version = None
    name = None
    apply = True
    websocket = False
    #create instance
    routeMixin = RouteMixin()
    routeMixin.app = app
    #method run
    target = routeMixin.route(
        uri=uri,
        host=host,
        methods=methods,
        strict_slashes=strict_slashes,
        version=version,
        name=name,
        apply=apply,
        websocket=websocket)
    #assert result
    assert isinstance(target, type(route))

# Generated at 2022-06-14 07:40:38.015603
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    r = RouteMixin()
    assert isinstance(r.route(), tuple)


# Generated at 2022-06-14 07:40:52.688277
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    router = RouteMixin()
    # case 1
    uri = "/abc"
    method = "get"
    host = "host"
    strict_slashes = True
    version = 0
    name = "name"
    apply = True
    def handler():
        return 1
    route1, handler1 = router.route(uri=uri,methods=method,host=host,strict_slashes=strict_slashes,
            version=version,name=name,apply=apply)(handler)
    assert route1.uri == uri
    assert route1.methods == [method]
    assert route1.host == host
    assert route1.strict_slashes == strict_slashes
    assert route1.version == version
    assert route1.name == name
    assert route1.host_matching

# Generated at 2022-06-14 07:41:03.175831
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():    
    @websocket('/feed')
    async def feed(request, ws):
        while True:
            data = 'hello!'
            print('Sending: ' + data)
            await ws.send(data)
            data = await ws.recv()
            print('Received: ' + data)
    # Call the method under testing
    RouteMixin.add_websocket_route('/feed', feed)
    assert type(RouteMixin.add_websocket_route('/feed', feed)) is FunctionType
    # assert RouteMixin.add_websocket_route('/feed', feed) == True
    

# Generated at 2022-06-14 07:41:14.467596
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic("test_route")
    mixin = RouteMixin()
    with pytest.raises(TypeError):
        mixin.route()
    with pytest.raises(TypeError):
        mixin.route(uri=None)
    with pytest.raises(TypeError):
        mixin.route(uri="",methods=None)
    with pytest.raises(TypeError):
        mixin.route(uri="",methods=[])
    with pytest.raises(TypeError):
        mixin.route(uri="",methods=["GET"],version=None,name=None)
    with pytest.raises(TypeError):
        mixin.route(uri="",methods=["GET"],version=None,name="")

# Generated at 2022-06-14 07:41:16.546845
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class Foo(RouteMixin):
        pass
    foo = Foo()
    @foo.add_route("/", methods=['GET'])
    def bar(request):
        pass
    assert all(foo.routes)


# Generated at 2022-06-14 07:41:27.380975
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():    
    from pathlib import Path
    from main import app
    from main.routers.utils import generate_sanic_route_info
    from main.routers.utils import generate_endpoint
    
    # Run
    route_info = generate_sanic_route_info(app.config)
    app.add_route(**route_info)

    # Check
    endpoint = generate_endpoint(route_info["uri"])
    path = Path(f"{app.config.STATIC_FOLDER}/{route_info['filename']}")
    msg = "Failed to add route to sanic app"
    assert (endpoint in app.url_map) is True, msg
    msg = "Failed to add template file to static folder"
    assert path.exists(), msg
 

# Generated at 2022-06-14 07:41:28.161254
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass

# Generated at 2022-06-14 07:41:35.471571
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    '''利用mock.patch将add_route函数替换为mock函数
    '''
    from . import RouteMixin
    router = RouteMixin()
    handler = lambda x: x
    router.add_route("/abc", handler)
    assert handler == router.routes[0].handler



# Generated at 2022-06-14 07:41:59.318274
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    my_router = RouteMixin()
    my_response_class = HTTPResponse
    my_method = "GET"
    my_uri = 'https://www.google.com/'
    my_host = '127.0.0.1'
    my_strict_slashes = True
    my_methods = ['GET']
    my_version = 1
    my_name = 'google.com'
    my_websocket = False
    my_stream = False
    actual_route = my_router.add_route(my_response_class, my_method, my_uri, my_host, my_strict_slashes, my_methods, my_version, my_name, my_websocket, my_stream)
    expected_route = Route

# Generated at 2022-06-14 07:42:10.410568
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test case 1 of 1
    test_app = Sanic("test_RouteMixin_add_route")

    @test_app.route("/", methods=["POST"])
    def handler1(request):
        pass

    @test_app.route("/", methods=["GET"])
    def handler2(request):
        pass

    @test_app.route("/", methods=["PUT"])
    def handler3(request):
        pass

    @test_app.route("/", methods=["DELETE"])
    def handler4(request):
        pass


# Generated at 2022-06-14 07:42:19.740169
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test case 1:
    # Test condition: When method is not GET or POST, it will raise excetion
    # Expected result: AttributeError should be raised
    
    # assert AttributeError is raised when method is not GET or POST
    with pytest.raises(AttributeError):
        my_mixin = RouteMixin()
        my_mixin.add_route("/", "", "ANY")
    
    # Test case 2:
    # Test condition: When host is not None, it is not a string, or it is a empty string, it will raise exception
    # Expected result: AssertionError should be raised
    
    # assert AssertionError is raised when host is not None, but it is not a string, or it is a empty string
    with pytest.raises(AssertionError):
        my_

# Generated at 2022-06-14 07:42:31.311030
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic('test_RouteMixin_route')
    test_route = RouteMixin()

    @test_route.route('/', methods = ['GET'], host = '127.0.0.1', strict_slashes = False, version = 1, name = 'test', apply = True, websocket = False, stream = False)
    def handler(request):
        return HTTPResponse("OK")

    test_route.add_route(handler, '/', host = '127.0.0.1', strict_slashes = False, version = 1, name = 'test', apply = True, websocket = False, stream = False)


# Generated at 2022-06-14 07:42:44.434161
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    router = RouteMixin()
    router.strict_slashes = True
    router._host = "host"
    def fn_factory():
        return 0
    test_route, fn = router.route(uri="uri", methods=["GET"], host="host", strict_slashes=True,
        version=1, name="name", apply=True, static=True)(fn_factory)
    assert test_route.uri == "uri"
    assert test_route.methods == ["GET"]
    assert test_route.host == "host"
    assert test_route.strict_slashes == True
    assert test_route.version == 1
    assert test_route.name == "name"
    assert test_route.static == True
    assert test_route.url == "uri"
    assert test_route.is_d

# Generated at 2022-06-14 07:42:49.843581
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Test with default argument
    test_route = RouteMixin()
    test_route.route()

    # Test with defined argument
    test_route = RouteMixin()
    test_route.route(uri, methods)
    # Test with wrong argument
    test_route = RouteMixin()
    # test_route.route(uri, methods="POST")


# Generated at 2022-06-14 07:42:55.962650
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.app import Sanic
    from sanic.response import text
    app = Sanic("test_RouteMixin_route")
    @app.route("/")
    async def handler(request):
        return text("OK")
    
    request, response = app.test_client.get('/')


# Generated at 2022-06-14 07:43:04.977749
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test Sanic app
    app = Sanic(configure_logging=False)
    # Test handler function
    async def handler(request):
        return text("ok")
    # Test RouteMixin
    mix = RouteMixin(router=app.router)
    # Test add_route method
    mix.add_route(handler, uri="/test/path")
    assert app.router.routes_all
    # Test handler URL
    assert app.router.routes_all[0].uri == "/test/path"


# Generated at 2022-06-14 07:43:06.638294
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:43:20.077210
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    import __main__
    import asyncio
    from sanic import Sanic
    from sanic.response import text
    from sanic.router import Route
    from sanic.router import RouteExists
    from sanic.router import RouteDoesNotExist
    from sanic.router import UrlNotExist
    from sanic.router import UrlPattern
    from functools import partial

    async def handler(request):
        return text("OK")

    app = Sanic()

    assert_that(app.routes, is_(empty()))
    assert_that(app.url_for("handler"), raises(UrlNotExist))

    # route
    app.route("/test", methods=["GET", "POST"])(handler)
    assert_that(app.routes, has_length(1))

# Generated at 2022-06-14 07:43:39.601180
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class _TestRouteMixin(RouteMixin):
        def __init__(self):
            super().__init__()
            self.routes = []

        def add_route(self, uri, handler, host=None, methods=None, strict_slashes=None, version=None, name=None):
            route = Route(uri, handler, host=host, methods=methods, strict_slashes=strict_slashes, version=version, name=name)
            self.routes.append(route)
            return route

    _TestRouteMixin()


# Generated at 2022-06-14 07:43:42.062540
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
  routeMixin = RouteMixin()
  assert isinstance(routeMixin, object)
  assert isinstance(routeMixin.add_route, object)

# Generated at 2022-06-14 07:43:48.024942
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # TestCase 1:
    request = MockRequest('/')
    response = HTTPResponse()

    handler = MockHandler(request, response)

    ut = RouteMixin()
    assert ut.add_route(handler, '/', ['GET']) == (('/', 'GET'), handler)



# Generated at 2022-06-14 07:43:59.388018
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic, response
    from sanic.response import json
    from sanic.router import Route
    from sanic.exceptions import RequestTimeout

    def test():
        return 1

    app = Sanic('test_RouteMixin_route')

    @app.route('/')
    async def handler(request):
        return response.json({"test": True})

    @app.route('/1')
    async def post_handler(request):
        return response.json({"test": True})

    @app.route('/2')
    async def head_handler(request):
        return response.json({"test": True})

    @app.route('/3')
    async def patch_handler(request):
        return response.json({"test": True})


# Generated at 2022-06-14 07:44:13.253095
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route1=Route("/a/b/c/:d","GET","hello world","1.0",None,None,None,None,True,None)
    route2=Route("/a/b/c/:d","POST","hello world2","2.0",None,None,None,None,True,None)
    route3=Route("/a/b/c/:d","PUT","hello world2","2.0",None,None,None,None,True,None)
    routes=[route1,route2,route3]
    router=Router(None)
    router.add_route(route1)
    router.add_route(route2)
    router.add_route(route3)

    assert router.routes==routes
test_RouteMixin_add_route()
#Unit test for method

# Generated at 2022-06-14 07:44:15.808877
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    assert RouteMixin.add_route.__name__ == 'add_route'


# Generated at 2022-06-14 07:44:29.171897
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Init class
    route_mixin = RouteMixin()
    assert route_mixin.name == "sanic"
    assert route_mixin.strict_slashes == True

    # Init class throught class method
    assert RouteMixin.__new__(RouteMixin) == route_mixin
    assert RouteMixin.__new__.__defaults__ == (True,)

    # Test add route
    @route_mixin.route("/")
    def index(request):
        pass

    route, handler = route_mixin.routes[0]
    assert route.methods == ["GET"]
    assert route.uri == "/"
    assert route.name == "index"
    assert handler.__name__ == "index"

    # Test add route with two methods

# Generated at 2022-06-14 07:44:40.135159
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Initialization
    R = RouteMixin()

    @R.route("/")
    def handler(request, name=None):
        return text("hello")

    class Test:
        def __init__(self):
            self.name = "hello"

        def __call__(self):
            return self.name

    # check that the decorator works with a function
    assert handler() == "hello"
    # check that the decorator works with a callable class
    assert Test() == "hello"

    class Test2:
        def __init__(self, name=None):
            self.name = name

        def __call__(self):
            return self.name

    # check that the decorator works with a class
    assert Test2(name="bob").name == "bob"

# Generated at 2022-06-14 07:44:47.159599
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    path = os.path.dirname(os.path.realpath(__file__))+"/test_RouteMixin_route.py"
    os.system(f"pylint --python-version=3.7 {path} > pylint_RouteMixin_route_output.txt")
    os.system(f"pytest {path} > pytest_RouteMixin_route_output.txt")

# Generated at 2022-06-14 07:44:56.934808
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test_RouteMixin_add_route')
    app.router = RouteMixin(app)

    async def handler(request, *args, **kwargs):
        pass
    
    route = app.router.add_route(
        handler = handler,
        uri = 'test_uri',
        host = None,
        strict_slashes = None,
        methods = [],
        version = None,
        name = None,
    )
    assert route.uri == 'test_uri'
    assert route.name == handler.__name__
    


# Generated at 2022-06-14 07:45:31.932333
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from .app import Sanic
    from .router import Route
    
    app = Sanic('test_RouteMixin_add_route')
    route = Route(
        app,
        'get',
        '/',
        [],
        {},
        'root',
        None,
        False,
        True,
        None,
        None,
    )
    app.routes.append(route)
    app.routes_all.append(route)
    
    app.add_route(None, '/', None, None, None, None, None, None)
    assert app.routes == [route]
    assert app.routes_all == [route]
    
    app.add_route(None, '/', None, None, None, None, None, None, True)
    assert app

# Generated at 2022-06-14 07:45:42.168370
# Unit test for method add_route of class RouteMixin

# Generated at 2022-06-14 07:45:43.463737
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:45:56.940160
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.response import json, text
    from sanic.router import Route
    from sanic.router import RouteParameters
    from sanic.router import Url
    from sanic.exceptions import NotFound, MethodNotSupported
    from sanic import response
    # case 1: method not in the allow list
    sanic = Sanic('./test_configs/sanic.json')
    uri = r'/'
    methods = ['POST', 'DELETE']
    allow_headers = set()
    version = 1
    strict_slashes = None
    host = None
    name = 'root'
    expect_uri = '/'
    expect_methods = ['POST', 'DELETE']
    expect_allow_headers = set()
    expect_version = 1
   

# Generated at 2022-06-14 07:46:05.374221
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # test route of class RouteMixin
    _RouteMixin = RouteMixin()

    def test_handler():
        pass

    _RouteMixin.route("/a", None, None, None, None, None)(test_handler)
    _RouteMixin.route(None, "a", None, None, None, None)(test_handler)
    # test empty function name
    _RouteMixin.route(None, None, None, None, None, None)(test_handler)


# Generated at 2022-06-14 07:46:15.318393
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.exceptions import SanicException
    from sanic.server import HttpProtocol

    async def handler(request):
        return HTTPResponse(text="OK")
    
    # Route the url to its handler
    app = Sanic()
    route, _ = app.route(uri='/', methods=['GET'])(handler)
    # Get the tuple of route object and decorated function
    assert (route, handler) == app.router.routes_all[('GET', '/')]
    # Register the route to its handler
    app.router.add_route('GET', '/', handler)
    
    # If a route object is not passed, create a new Route object
    route

# Generated at 2022-06-14 07:46:27.272411
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.response import json

    app = Sanic("test_RouteMixin_route")

    async def handler1(request):
        return json({"test_RouteMixin_route_handler1": True})

    @app.get("/hello")
    async def handler2(request):
        return json({"test_RouteMixin_route_handler2": True})

    app.route("/handler3", methods=["POST"])(handler1)
    app.add_route(handler1, "/handler4", methods=["DELETE"])

    _, handler = app.route(
        "/handler5", methods=["DELETE"], version=1
    )(handler1)
    app.add_route(handler, "/handler5", methods=["DELETE"], version=1)


# Generated at 2022-06-14 07:46:29.830277
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # TODO: generate mock
    data = None
    assert RouteMixin().route(data)
    return

# Generated at 2022-06-14 07:46:37.450355
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    """
    Test method RouteMixin.add_route
    """
    router = RouteMixin(None)
    handler = object()
    router.add_route('/', 'GET', handler)
    assert router.routes[0].uri == '/'
    assert router.routes[0].methods == ['GET']
    assert router.routes[0].handler == handler



# Generated at 2022-06-14 07:46:48.209482
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # create RouteMixin
    routemixin = RouteMixin()
    # noinspection PyTypeChecker
    assert routemixin.route == RouteMixin.route
    assert isinstance(routemixin, RouteMixin)
    assert routemixin.name == 'routemixin'
    # noinspection PyTypeChecker
    routemixin.route(uri='/', host=None, methods=None, strict_slashes=None, version=None, name=None,
                     apply=True, static=False, websocket=False)
    # noinspection PyTypeChecker
    routemixin.route(uri='/', host=None, methods=None, strict_slashes=None, version=None, name=None,
                     apply=True, static=False, websocket=False)

# Generated at 2022-06-14 07:47:19.365168
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic_compress import Compress
    from sanic.response import text
    class RouteMixinTest(RouteMixin):
        def __init__(self):
            RouteMixin.__init__(self)

    r = RouteMixinTest()
    r.compress = Compress()

    @r.route("/")
    async def handler(request):
        return text("OK")

    assert isinstance(r.routes[0], Route)
    assert r.routes[0].uri == "/"
    assert r.routes[0].handler == handler
    assert r.routes[0].host == None
    assert r.routes[0].methods == ["GET"]
    assert r.routes[0].version == None
    assert r.routes[0].strict_

# Generated at 2022-06-14 07:47:32.405483
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test_RouteMixin_add_route')
    app.config.REQUEST_MAX_SIZE = 262144
    app.config.REQUEST_TIMEOUT = 60

    RouteMixin.add_route(app, handler=app.config, uri='/config', host=None, strict_slashes=None, name=None, version=None)
    RouteMixin.add_route(app, handler=app.config, uri='/config', host=None, strict_slashes=False, name=None, version=None)
    RouteMixin.add_route(app, handler=app.config, uri='/config', host=None, strict_slashes=True, name=None, version=None)

# Generated at 2022-06-14 07:47:40.389749
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # pass
    uri = 1
    methods = 2
    host = 3
    strict_slashes = 4
    version = 5
    name = 6
    apply = 7
    websocket = 8
    coroutine = 9

    route = RouteMixin.route(uri,methods,host,strict_slashes,version,name,apply,websocket,coroutine)
    assert route == 1


# Generated at 2022-06-14 07:47:48.756793
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    uri = "uri"
    handler = "handler"
    methods = ["GET"]
    host = "host"
    strict_slashes = True
    version = 1
    name = "name"
    register = True

    app = Sanic("sanic-server") 
    app.add_route = MagicMock(return_value = app)
    app.add_route(uri,
                  handler,
                  methods,
                  host,
                  strict_slashes,
                  version,
                  name,
                  register )
    app.add_route.assert_called()



# Generated at 2022-06-14 07:47:56.391976
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    test_instance = RouteMixin()
    uri = ""
    host = "localhost"
    version = 1
    name = "test_name"
    strict_slashes = False
    method = "GET"
    assert test_instance.route(uri, host, methods=method, strict_slashes = strict_slashes, version = version, name = name) == ("/<name>", {"strict_slashes": False})

# Generated at 2022-06-14 07:48:07.279406
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    model = RouteMixin()

# Generated at 2022-06-14 07:48:20.667169
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.exceptions import InvalidUsage

    def handler(request):
        pass

    def handler2(request):
        pass

    router = RouteMixin()
    routes = []

    # Create a router with single route
    router, routes = router.route(
        uri=uri,
        host=host,
        methods=methods,
        strict_slashes=strict_slashes,
        version=version,
        name=name,
        apply=apply,
        stream=stream,
        status=status,
        content_type=content_type,
    )(handler)

    assert router.routes == routes
    assert router.routes[0].uri == uri
    assert router.routes[0].host == host
    assert router.routes[0].methods == methods

# Generated at 2022-06-14 07:48:32.865250
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    
    mock_handler = Mock()
    mock_methods = Mock()
    mock_uri = Mock()
    mock_host = Mock()
    mock_strict_slashes = Mock()
    mock_stream = Mock()
    mock_name = Mock()
    mock_version = Mock()
    mock_apply = Mock()
    mock_subprotocols = Mock()
    mock_websocket = Mock()
    
    test_instance = RouteMixin()
    

# Generated at 2022-06-14 07:48:41.944182
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import text
    from sanic.views import CompositionView

    app = Sanic('test_RouteMixin_route')

    app.blueprint(app.router)
    app.blueprint(app.websocket_routes)

    # RouteMixin.route(*a, **kw)(handler)
    @app.route('/get')
    async def handler(request):
        return text('OK')

    rv = app.router.routes_all[0]

    assert rv.methods == {'GET'}
    assert rv.uri_template == '/get'
    assert rv.name == 'handler'
    assert rv.name.startswith('test_RouteMixin_route.')



# Generated at 2022-06-14 07:48:50.900510
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from .base import Sanic
    route_mixin = RouteMixin()
    method = "GET"
    uri = "uri"
    host = "host"
    strict_slashes = "strict_slashes"
    version = "version"
    name = "name"
    apply = "apply"
    # noinspection PyUnusedLocal
    def handler(request, *args, **kwargs):
        pass
    handler_tuple_0 = (handler,)
    handler_tuple_1 = handler_tuple_0 + (handler,)
    return_value = route_mixin.route(method=method, uri=uri, host=host, strict_slashes=strict_slashes, version=version,
                                     name=name,
                                     apply=apply)
    # noinspection PyUnresolvedReferences

# Generated at 2022-06-14 07:49:58.420871
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = RouteMixin(strict_slashes=False)
    router.host = "localhost"
    router.version = "127.0.0.1"
    router.blueprints = []
    router.add_route("/static/<path:path>",
                     lambda request, path: "static",
                     methods=["POST"],
                     strict_slashes=False,
                     version="127.0.0.1",
                     host="localhost",
                     name="_static_",
                     stream=True,
                     apply=True,
                     websocket=True,
                     static=True)
    return

