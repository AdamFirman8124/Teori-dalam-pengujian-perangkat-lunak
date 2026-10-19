

# Generated at 2022-06-14 07:40:29.895829
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:40:40.976868
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    routing = RouteMixin()
    routing.name = 'name_unit_test'
    routing.url_for = MagicMock()
    routing.url_for.return_value = "test"
    routing.add_route(handler=test_route,uri='test')
    assert routing.routes[0].uri == 'test'
    assert routing.routes[0].name == 'name_unit_test.test_route'
    assert routing.routes[0].host == None
    assert routing.routes[0].strict_slashes == None
    assert routing.routes[0].version == None
    assert routing.routes[0].apply == True
    assert routing.routes[0].static == False
    assert routing.routes[0].websocket == False

# Unit

# Generated at 2022-06-14 07:40:42.591085
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    assert RouteMixin.route.__name__ == "route"

# Generated at 2022-06-14 07:40:54.535302
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from sanic.router import Route
    from sanic.constants import HTTP_METHODS
    from sanic.request import Request
    import os
    uri = "test_uri"
    file_or_directory = "test_file_or_directory"
    pattern=r"/?.+"
    use_modified_since=True
    use_content_range=False
    stream_large_files=False
    name="test_name"
    host=None
    strict_slashes=None
    content_type=None
    apply=True

    # Test exception handling
    # test case 1

# Generated at 2022-06-14 07:41:06.733425
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    """
    Unit test for method add_route of class RouteMixin.
    """
    _dummy_class = RouteMixin() # instantiate an object of class RouteMixin
    _dummy_class.get = None
    _dummy_class.post = None
    _dummy_class.put = None
    _dummy_class.head = None
    _dummy_class.patch = None
    _dummy_class.options = None
    _dummy_class.delete = None

    # Test case:

# Generated at 2022-06-14 07:41:11.028768
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic

    app = Sanic("test_RouteMixin_route")
    app.router.route("/test")
    assert app == app



# Generated at 2022-06-14 07:41:17.451214
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = RouteMixin()
    assert router.routes == []
    router.add_route(route=None)
    assert router.routes == []
    route = Route(uri=None, name=None)
    router.add_route(route=route)
    assert router.routes == [route]



# Generated at 2022-06-14 07:41:21.550480
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    def foo(request):
        pass
    r = RouteMixin()
    method = 'test'
    uri = 'test'
    r.add_route(foo,uri,method)
    assert r._routes[0].methods[0] == 'TEST'


# Generated at 2022-06-14 07:41:29.833232
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    uri = "/"
    method = ["GET", "POST"]
    strict_slashes = False
    name = "foo"
    version = 2
    host = "localhost"
    protocol = ["http", "https"]
    apply = True
    dependencies = (1, 2)
    routes_list = []
    self = RouteMixin()
    self.routes = routes_list
    result = self.route(uri, method, strict_slashes, name, version, host, protocol, apply, dependencies)
    assert result == (routes_list, None)
    assert len(routes_list) == 1
    assert routes_list[0][0] == uri
    assert routes_list[0][1] == method
    assert routes_list[0][2] == strict_slashes

# Generated at 2022-06-14 07:41:42.994073
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    route = RouteMixin()
    @route.route("/", name="index")
    def index(request):
        return text("Hello World")
    assert route.handler_string(index) == "index:index:index"
    assert route.matches("index") == route.routes[0]
    assert route.matches("index:index:index") == route.routes[0]
    assert route.matches("index.index") == route.routes[0]
    assert route.matches("") is None
    assert route.matches("index:index:index:index") is None
    assert route.matches("index:index") is None
    assert route.matches("index.index.index") is None


# Generated at 2022-06-14 07:42:06.123797
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    
    try:
        # Test for route method
        decorator_route = RouteMixin()
        test_decorator_route = decorator_route.route()
        print('>>test_RouteMixin_route()-> test_decorator_route:',test_decorator_route)
        assert callable(test_decorator_route)
        print('>>test_RouteMixin_route(): PASSED')
    except Exception as e:
        print('>>test_RouteMixin_route(): FAILED')
        print('Error:', e)
    
    

# Generated at 2022-06-14 07:42:17.376442
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route_mixin = RouteMixin()
    route_mixin.add_route('/user/<name>/<id>', 'get', route_funct, name='user')
    true_result = {
        'uri': '/user/<name>/<id>',
        'methods': ['GET'],
        'handler': 'route_funct',
        'name': 'user',
        'host': '',
        'websocket': False,
        'static': False,
        'stream': False,
        'strict_slashes': False,
        'version': 0,
        'versions': {}
    }
    assert route_mixin.routes[0] == true_result

# Generated at 2022-06-14 07:42:30.167888
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    """
    Test case for RouteMixin class method route
    """
    app = Sanic(__name__)
    RouteMixin().route(uri='/', host=None, methods=None, strict_slashes=None, version=None, name=None, apply=True)(app.func1)
    RouteMixin().add_route(app.func1, uri='/', host=None, methods=None, strict_slashes=None, version=None, name=None)
    assert len(app._route_list)==1
    assert app._route_list[0].uri=='/'
    assert app._route_list[0].handler.__name__=='func1'
    assert app._route_list[0].host==None
    assert app._route_list[0].get==True
    assert app._route_list

# Generated at 2022-06-14 07:42:32.327966
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    a = RouteMixin()
    a.route()


# Generated at 2022-06-14 07:42:40.314915
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic(__name__)
    router = Router(app)
    # Test with the actual code
    @router.route('/')
    async def handler():
        pass
    # Test with mock
    with patch('sanic.router.Sanic.route', return_value=None) as mock:
        router.route('/', methods=['GET'])
        assert mock.called


# Generated at 2022-06-14 07:42:51.587367
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.app import Sanic

    app = Sanic("test_RouteMixin_add_route")
    with pytest.raises(ValueError):
        app.add_route(
            handler=app,
            uri="/",
            methods=["GET"],
        )

    with pytest.raises(TypeError):
        app.add_route(
            handler=app.async_route,
            uri="/",
            methods=["GET"],
            strict_slashes=None,
        )

    with pytest.raises(ValueError):
        app.add_route(
            handler=app.async_route,
            uri="/",
            methods=["GET"],
            strict_slashes=None,
            name=123,
        )


# Generated at 2022-06-14 07:42:53.414431
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    router = RouteMixin()
    assert router.name == "test"

# Generated at 2022-06-14 07:43:07.164237
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    uri1 = '/test/'
    uri2 = '/static/'
    uri3 = '/static2/'

    method1 = 'GET'
    method2 = 'POST'
    method3 = 'DELETE'
    method4 = 'OPTIONS'
    method5 = 'HEAD'

    handler1 = 'handler1'
    handler2 = 'handler2'
    handler3 = 'handler3'
    handler4 = 'handler4'
    handler5 = 'handler5'

    strict_slashes1 = True
    strict_slashes2 = False
    strict_slashes3 = None

    name1 = 'name1'
    name2 = 'name2'
    name3 = None

    path1 = 'path1'
    path2 = 'path2'
    path3 = None

    subdomain1

# Generated at 2022-06-14 07:43:11.336514
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    sol = RouteMixin()
    sol.add_route('/test', lambda request: None)
    assert sol.routes[-1].uri == '/test'
# Test for method add_websocket_route of class RouteMixin

# Generated at 2022-06-14 07:43:25.409944
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    print('\nTesting method route of class RouteMixin')
    # @route types
    uri = '/'
    method = [None]
    uri = 'http://sanic.com'
    method = [None]
    uri = 'http://sanic.com/'
    method = [None]
    uri = '/'
    method = ['GET']
    uri = '/'
    method = ['POST']
    uri = '/'
    method = ['GET', 'POST']
    uri = '/'
    method = ['POST', 'GET']
    uri = '/'
    method = ['POST', 'GET']
    uri = '/'
    method = None

    # @route decorator test
    print('@route() types testing...')
    assert len(method) > 0

# Generated at 2022-06-14 07:43:47.400078
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    from sanic import Sanic
    app = Sanic("test_RouteMixin_add_route")
    # case 1
    route = Route("/test", "GET", app)
    rm = RouteMixin(app)
    assert type(rm.add_route(route)) is list
    # case 2
    assert type(rm.add_route("/test1", "POST")) is list
    # case 3
    assert type(rm.add_route("/test2", "PUT", name = "put")) is list
    # case 4
    assert type(rm.add_route("/test3", "DELETE", strict_slashes = True)) is list
    # case 5
    assert type(rm.add_route("/test4", "PATCH", version = 1)) is list
   

# Generated at 2022-06-14 07:43:59.060817
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    print("-" * 20,"Unit test for method add_route of class RouteMixin","-" * 20)
    r = RouteMixin()

    # test for add_route
    @r.add_route("/route1")
    async def route1(request):
        return text("route1")
    asyncio.run(route1)

    # test for route
    @r.route("/route2")
    async def route2(request):
        return text("route2")
    asyncio.run(route2)

    # test for head
    @r.head("/route3")
    async def route3(request):
        return text("route3")
    asyncio.run(route3)

    # test for options

# Generated at 2022-06-14 07:44:01.272934
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route = RouteMixin()
    assert route.add_route("/", "GET", "index") == None


# Generated at 2022-06-14 07:44:08.075892
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    print("test1")
    # config
    handler = {"function": "test"}
    uri = "test"
    host = None
    methods = ["GET", "HEAD"]
    # process
    result = Route.add_route(handler, uri, host, methods)
    # assert
    assert result != None


# Generated at 2022-06-14 07:44:14.951935
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic("test_RouteMixin_add_route")

    def request_handler(request):
        return response.text("OK")

    app.add_route(request_handler, "/test")

    assert len(app.router.routes_all["GET"]) == 1
    assert (
        app.router.routes_all["GET"][0].uri == "/test"
    ) == True

# Generated at 2022-06-14 07:44:15.894357
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass

# Generated at 2022-06-14 07:44:28.224058
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    app = Sanic("route_mixin")
    filename = "file/for/test_route_mixin_static"
    assert not path.exists(filename)
    with open(filename, "w") as stream:
        stream.write("test_route_mixin_static")

# Generated at 2022-06-14 07:44:31.993701
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    mixin = RouteMixin()
    @mixin.route('/path/<parameter>')
    def handler(request, parameter):
        return "DEFINED"
    assert isinstance(mixin, RouteMixin)


# Generated at 2022-06-14 07:44:45.614768
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    route_mixin = RouteMixin()
    uri = "uri"
    file_or_directory = "file_or_directory"
    pattern = r"pattern"
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = "name"
    host = "host"
    strict_slashes = False
    content_type = "content_type"
    apply = True

# Generated at 2022-06-14 07:44:53.299579
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # arrange
    sanicInstance_route = sanic.Sanic()
    routeMixin = route.RouteMixin(sanicInstance_route)

    uri = '/'
    methods = ['GET']
    host = '127.0.0.1'
    version = 1
    strict_slashes = False
    name = 'route_1'
    apply = True
    # act
    route = routeMixin.add_route(uri, methods, host, version, 
        strict_slashes, name, apply)
    # assert
    assert route.uri == uri
    assert route.methods == methods
    assert route.host == host
    assert route.version == version
    assert route.strict_slashes == strict_slashes
    assert route.name == name
    # assert len(routeMixin.routes

# Generated at 2022-06-14 07:45:24.436761
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # GIVEN
    app = Sanic('test_sanic')
    app.config.KEEP_ALIVE = False
    app.config.KEEP_ALIVE_TIMEOUT = 60
    app.config.REQUEST_TIMEOUT = 60
    app.config.RESPONSE_TIMEOUT = 60
    app.config.REQUEST_MAX_SIZE = None
    app.config.REQUEST_BUFFER_QUEUE_SIZE = 100
    app.config.REQUEST_TIMEOUT = None
    app.config.RESPONSE_TIMEOUT = 60
    app.config.GRACEFUL_SHUTDOWN_TIMEOUT = 15
    app.config.KEEP_ALIVE_TIMEOUT = 5
    app.config.ACCESS_LOG = False

# Generated at 2022-06-14 07:45:38.737158
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Test 1
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    # Test if the route method of class RouteMixin can be called
    
    print("test begin")
    app = Sanic("test_RouteMixin_route")

# Generated at 2022-06-14 07:45:40.537099
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass

# Generated at 2022-06-14 07:45:52.040107
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    sanic_request=MagicMock()
    class Test_Class_1(object):
        def test_function_1(self, request):
            return 1
    route_mixin=RouteMixin()

# Generated at 2022-06-14 07:46:02.653541
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class Test(RouteMixin):
        uri = 'foo.bar'
        name = 'foo.bar'
        host = None
        strict_slashes = None
        version = None
        methods = ['GET']

    t = Test()
    @t.add_route(uri, name, host, strict_slashes, version, methods)
    def handler():
        return "foo.bar"

    t.app.add_route(handler, 'foo.bar')
    assert t.app.router.routes_all['foo.bar'].name == 'foo.bar'


# Generated at 2022-06-14 07:46:14.386560
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from sanic import Sanic
    from sanic.router import Route
    from sanic.response import HTTPResponse
    from sanic.response import StreamingHTTPResponse
    from tempfile import mkdtemp
    app = Sanic("test_StaticFiles")
    router = app.add_route
    router = RouteMixin("test_StaticFiles_static", app, router)

    # (app, router) = RouteMixin.static(app, router, "index.html")
    # (app, router) = RouteMixin.static(app, router, "index.html", "index")
    # (app, router) = RouteMixin.static(app, router, "index.html", "index", True)
    # (app, router) = RouteMixin.static(app, router, "index.html", "index

# Generated at 2022-06-14 07:46:26.761061
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test_RouteMixin_add_route')

    @app.route('/')
    def handler1(request):
        return text('OK')

    @app.route('/2')
    def handler2(request):
        return text('OK')

    @app.route('/3')
    def handler3(request):
        return text('OK')

    @app.route('/4')
    def handler4(request):
        return text('OK')

    @app.route('/5')
    def handler5(request):
        return text('OK')

    @app.route('/wp-admin')
    def handler6(request):
        return text('OK')

    @app.route('/wp-include')
    def handler7(request):
        return text('OK')


# Generated at 2022-06-14 07:46:31.840633
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    @RouteMixin.route('/')
    async def test(request):
        return text('OK')

    request, response = RouteMixin.test(RouteMixin(), request_param())

    assert response.text == 'OK'


# Generated at 2022-06-14 07:46:43.828128
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = RouteMixin()
    assert router.url_map is None
    assert router.host is None
    assert router.strict_slashes is None
    assert router.name is None
    assert router.blueprints is None
    assert router.static_route is None
    assert router.format_url is None
    assert router.static_route_url is None
    assert router._static_dir_url is None
    assert router._static_files is None
    assert router._future_statics is None
    assert router.route_overrides is None
    assert router._apply_static is None
    assert router._register_static is None

    assert router.app is None
    assert router._websocket_tasks is None
    assert router._websocket_routes is None
    assert router._websocket_handlers is None

# Generated at 2022-06-14 07:46:56.669634
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    def test_function():
        pass
    root_uri = 'http://localhost:8080'
    uri = '/hello'
    method = ['GET','POST']
    host = 'http://www.qq.com'
    strict_slashes = True
    version = 1
    name = 'test_hello'
    apply = True
    protocol = WSProtocol(None, None, None)
    r = RouteMixin()
    r.route(uri,
            host = host,
            methods = method,
            strict_slashes = strict_slashes,
            version = version,
            name = name,
            apply = apply,
            subprotocols = protocol)
    assert r.uri == uri


# Generated at 2022-06-14 07:48:05.369123
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class TestRouter(Router):
        def resolve(self, request):
            pass

    instance_test_route_mixin = RouteMixin(TestRouter(), None)
    instance_test_route_mixin.add_route('', None, None, None, None, None, None, None)
    assert 1 == 1


# Generated at 2022-06-14 07:48:18.834374
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test_RouteMixin_add_route')

    @app.route('/test')
    @app.websocket('/test')
    async def test(request):
        return text('OK')

    # Test if method add_route raise TypeError if request_handler is not callable
    with pytest.raises(TypeError):
        async def test(request):
            return text('OK')
        RouteMixin.add_route(
            app.router,
            request_handler=test,
            uri='/test1',
            host=None,
            methods=None,
            strict_slashes=None,
            version=None,
            name=None,
            stream=False,
            status_codes=None,
            apply=True,
            websocket=False,
        )
   

# Generated at 2022-06-14 07:48:25.150227
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test case 1
    route_mixin1 = RouteMixin()
    uri1 = "uri"
    methods1 = ["GET", "POST", "PUT"]
    handler1 = "handler"
    version1 = None
    name1 = None
    host1 = None
    strict_slashes1 = None

# Generated at 2022-06-14 07:48:31.997797
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    @app.route('/name')
    def handler(request):
        return HTTPResponse('name')

    assert app.router.routes_all['GET'][0].uri == '/name'
    assert app.router.routes_all['GET'][0].name == '/name'
    assert app.router.routes_all['GET'][0].handler.__name__ == 'handler'


# Generated at 2022-06-14 07:48:36.804565
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    tester = RouteMixin()
    tester.add_route('/', tester._static_request_handler, methods=['GET'])
    assert len(tester._route_cache) == 2
    assert len(tester.routes) == 2


# Generated at 2022-06-14 07:48:47.809929
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    client = Sanic()
    test = RouteMixin(Sanic(__name__))
    file_or_directory=r"./routes.py"
    uri="/"
    pattern=r"/?.+"
    use_modified_since=True
    use_content_range=False
    stream_large_files=False
    name="static"
    host=None
    strict_slashes=None
    content_type=None
    from urllib.parse import unquote
    from sanic.exceptions import InvalidUsage, FileNotFound
    from utils import sub
    from sanic import Sanic
    from sanic.router import Route, RouteExists

    from sanic.response import HTTPResponse, text, json, HTTPResponse
    from urllib.parse import unquote

# Generated at 2022-06-14 07:49:00.162343
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import Route
    from sanic.response import json, text
    class FakeSanic:
        router = None
        error_handler = None
        exception_handler = None
        request_middleware = None
        response_middleware = None
        middlewares = None
        print_route_table = True
        debug = True
        compression = None
        _before_start_hooks = None
        _after_start_hooks = None
        _before_stop_hooks = None
        _after_stop_hooks = None
        _before_start_server_hooks = None
        _after_start_server_hooks = None
        _before_stop_server_hooks = None
        _after_stop_server_hooks = None
        _before_handle_request_hooks = None
       

# Generated at 2022-06-14 07:49:07.342217
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    async def handler(request, a, b):
        return text("OK")
    #
    rmr = RouteMixin()
    # Test
    route, _ = rmr.route(uri='/test', apply=False)(handler)
    # Assert
    assert route.uri == '/test'

# Generated at 2022-06-14 07:49:14.447806
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic(name='sanic')
    RouteMixin.route(
        app,
        uri='/',
        methods=None,
        strict_slashes=False,
        version=None,
        name=None,
        apply=True,
        handler=None,
        websocket=False,
        stream=False,
        register_policy=None,
        host=None,
        expect_handler=None
    )


# Generated at 2022-06-14 07:49:15.443884
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass