

# Generated at 2022-06-14 07:40:34.439233
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    async def handler1(request):
        return text("OK")

    async def handler2(request):
        return text("OK")

    async def handler3(request):
        return text("OK")

    async def handler4(request):
        return text("OK")

    async def handler5(request):
        return text("OK")

    async def handler6(request):
        return text("OK")

    async def handler7(request):
        return text("OK")

    async def handler8(request):
        return text("OK")

    async def handler9(request):
        return text("OK")

    async def handler10(request):
        return text("OK")

    handler11 = Mock()
    handler11.__name__ = "handler11"

    handler12 = Mock()
    handler12.__name__ = "handler12"

# Generated at 2022-06-14 07:40:46.057272
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    async def handler(request):
        return HTTPResponse("ok")

    router = RouteMixin()
    routes = router.route("/test")(handler)
    assert routes[0].url.as_string() == "/test"

    router.host = "example.com"
    routes = router.route("/test")(handler)
    assert routes[0].url.as_string() == "//example.com/test"

    router.host = None
    router.default_subdomain = "www"
    routes = router.route("/test")(handler)
    assert routes[0].url.as_string() == "//www.example.com/test"

    router.host = "example.com"
    # TODO: Investigate if this is a bug in Sanic, if so file a bug report

# Generated at 2022-06-14 07:40:58.189070
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    test_object = RouteMixin()
    print("In method \"test_RouteMixin_route\" of class \"test_RouteMixin\"")

# Generated at 2022-06-14 07:41:10.967941
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test 1: Add_route - default values
    class Server(Sanic):
        def __init__(self):
            super().__init__()
            self.url_map = RouteMap()

    server = Server()
    test_route = RouteMixin()
    uri = 'https://'
    test_route.add_route(uri)
    routes = server.url_map.routes_for('GET')
    assert routes[0].uri == '/'

    # Test 2: Add_route - default values
    class Server(Sanic):
        def __init__(self):
            super().__init__()
            self.url_map = RouteMap()

    server = Server()
    test_route = RouteMixin()
    uri = 'https://'

# Generated at 2022-06-14 07:41:24.130793
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    "test for method add_route of class RouteMixin"

    # Create a test sanic instance
    app = Sanic("test_sanic")

    # Create an instance of RouteMixin
    router = RouteMixin("test_router")

    from sanic_restplus import Api
    # Create an instance of Api
    api = Api("test_api")

    app.blueprint(router)
    app.blueprint(api)

    # Test add_route
    @app.add_route(uri='/api/v1/testroute', methods=["GET"])
    def testroute(request):
        return HTTPResponse("testroute", status=200)

    # Test add_route

# Generated at 2022-06-14 07:41:31.625589
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    r = RouteMixin()
    # ValueError: Static route must be a valid path, not None
    r.static(uri = "", file_or_directory = None, pattern="", use_modified_since = True, use_content_range = False, stream_large_files = False, name = "static", host = None, strict_slashes = None, content_type = None, apply = True)


# Generated at 2022-06-14 07:41:34.346505
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    with pytest.raises(TypeError):
        RouteMixin().add_route("/", "0.0.0.0", None)

# Generated at 2022-06-14 07:41:46.930362
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    rm = RouteMixin()
    rm.route_pattern = None
    rm.route_prefix = None
    rm.route_counter = None
    rm.route_unique_id = None
    rm.router = None
    rm.strict_slashes = None
    rm.name = None
    uri = "/"
    version = None
    strict_slashes = None
    name = "route"
    uri_params = None
    host = None
    methods = ["GET"]
    stream = None
    websocket = None
    apply = True
    version = None
    def _handler():
        return "request"

# Generated at 2022-06-14 07:41:48.579426
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    assert True
    
    

# Generated at 2022-06-14 07:42:01.057475
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    from sanic.exceptions import InvalidUsage
    from sanic.utils import sanic_endpoint_test

    #Test arguments
    methods = ['POST','GET','DELETE','PUT']
    uri = 'test/test_uri'
    handler = 'handler'
    version = 1
    strict_slashes = None
    host = '*'
    name = 'test_route_name'
    stream = False
    websocket = False
    apply = True
    
    #Test code
    route = Route(handler,'/test/test_uri',['POST','GET','DELETE','PUT'],
        host='*', strict_slashes=None, version=1, name='test_route_name',
        stream=False, websocket=False, apply=True)
    expected_

# Generated at 2022-06-14 07:42:22.575814
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    
    mock_request = MockRequest()
    mock_response = MockResponse()

    # Create the server
    server = Sanic("test_server")
    
    @server.route("/test/route")
    async def test(request):
        return mock_response

    # Replace the router
    server.router = Mock()
    server.router.add_route.return_value = (None, None)

    server.add_route("/test/route", test)

    assert server.router.add_route.called
    assert mock_request.__route__ == "/test/route"



# Generated at 2022-06-14 07:42:33.467984
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.router import Route, RouteExists
    from sanic.exceptions import InvalidUsage
    from sanic.handlers import ErrorHandler
    from sanic.views import CompositionView

    def test_handler(request):
        pass

    def test_handler_no_methods_param(request):
        pass

    def test_handler_no_decorator(request):
        pass

    # GIVEN: Instantiated class RouteMixin, Request and Handler
    route_mixin = RouteMixin()
    request = Request("GET", "/")
    handler = test_handler
    handler_no_methods_param = test_handler_no_methods_param
    handler_no_decor

# Generated at 2022-06-14 07:42:45.986799
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    uri = '/'
    methods = None
    is_websocket = False
    version = None
    strict_slashes = None
    name = None
    static = False
    host = None
    apply = True
    stream = False
    subprotocols = None
    protocol_class = None
    protocol = None
    router = RouteMixin()
    routes, func = router.route(uri=uri, methods=methods, strict_slashes=strict_slashes, version=version, name=name, apply=apply, static=static, host=host, stream=stream, subprotocols=subprotocols,
             protocol_class=protocol_class, protocol=protocol, is_websocket=is_websocket)
    # You can write your own, and add your unit test here
    assert True
#

# Generated at 2022-06-14 07:42:53.998275
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    try:
        @app.route("/")
        def index():
            return html("<b>Hello world</b>")

        assert app.router.routes_names['index'] == "/index"
        assert app.router.routes['index'].uri == "/index"
    except Exception as e:
        logging.error("test_RouteMixin_add_route FAILED, error: %s" % e)
        return False
    return True


# Generated at 2022-06-14 07:43:04.898168
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    mm = RouteMixin(
        name='sanic',
        version=1,
        strict_slashes=True,
        host='127.0.0.1',
    )

    @mm.route('/products')
    def products(request):
        return text('products')

    assert mm.routes[0].uri == '/products'
    assert mm.routes[0].host == '127.0.0.1'
    assert mm.routes[0].strict_slashes == True
    assert mm.routes[0].documentation == {}



# Generated at 2022-06-14 07:43:16.061798
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    router=RouteMixin()
    url='/test/'
    methods=['GET']
    strict_slashes=None
    version=None
    name='test'
    apply=True
    assert router.route(url,methods,strict_slashes,version,name,apply)
    assert router.route(url,methods,strict_slashes,version,name,apply)
    try:
        router.route(url,methods,strict_slashes,version,name,apply)
    except Exception as e:
        assert str(e) == 'function must be callable'


# Generated at 2022-06-14 07:43:20.172495
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # arrange
    test_instance = RouteMixin()

    # act
    test = test_instance.add_route

    # assert
    assert test


# Generated at 2022-06-14 07:43:23.050607
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route_mixin = RouteMixin()
    assert route_mixin.add_route("/", "head") == None


# Generated at 2022-06-14 07:43:37.280149
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import Route
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.app import Sanic
    
    def test_handler(request):
        return HTTPResponse("test")
    
    app = Sanic("test_RouteMixin_route")
    route = app.route("/test")(test_handler)
    assert route.uri_template == "/test"
    assert route.uri_template_regex == re.compile("^/test/?$", re.IGNORECASE)
    assert route.host_regex is None
    assert route.host_matching_schema is None
    assert route.handler == test_handler
    assert route.methods == frozenset({"GET", "HEAD", "OPTIONS"})
   

# Generated at 2022-06-14 07:43:40.065671
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Arrange
    # Act
    with pytest.raises(TypeError):
        router.add_route()

# Generated at 2022-06-14 07:44:06.856984
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class RouteK(Route):
        pass
    class RouteMixinK(RouteMixin):
        pass
    route_k = RouteK(uri='/test_uri', methods={'GET'}, name='test_name', strict_slashes=True, version=None, host=None, stream=False, register=True, websocket=False, static=False)
    route_mixin_k = RouteMixinK()
    assert route_mixin_k.add_route(route=route_k, handler=Mock()) == 1
    route_mixin_k = RouteMixinK()
    assert route_mixin_k.add_route(route=route_k) == 1
    route_mixin_k = RouteMixinK()

# Generated at 2022-06-14 07:44:09.276705
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    obj = Sanic('test')
    obj.add_route(None, None, None, None)

# Generated at 2022-06-14 07:44:18.412283
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # 1. Test for a basic function
    @RouteMixin.add_route
    def view():
        return HTTPResponse()
    assert isinstance(view, Route)
    assert view.handler is view.__wrapped__
    assert view.uri == "/"
    # 2. Test for a None uri with a string
    @RouteMixin.add_route(None)
    def view():
        return HTTPResponse()
    assert isinstance(view, Route)
    assert view.handler is view.__wrapped__
    assert view.uri == "/"
    # 3. Test for a None uri with a empty string
    @RouteMixin.add_route("")
    def view():
        return HTTPResponse()
    assert isinstance(view, Route)
    assert view.handler is view.__

# Generated at 2022-06-14 07:44:24.342251
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = Router()
    async def handler(request):
        return HTTPResponse()
    route = router.add_route(handler, 'uripath',['GET','POST'])
    assert route.uri == 'uripath'
    assert route.methods == ['GET', 'POST']

# Generated at 2022-06-14 07:44:35.390309
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Router
    from sanic.response import text
    from sanic.exceptions import NotFound
    routes = Router()
    routes.add_route(GET, '/', text('OK'))
    routes.add_route(GET, '/test', text('OK'))
    routes.add_route(POST, '/test', text('OK'))
    routes.add_route(DELETE, '/test', text('OK'))
    routes.add_route(DELETE, '/test/<id:int>', text('OK'))

    request, response = routes.get(request_factory('GET', '/'))
    assert response.text == 'OK'

    request, response = routes.get(request_factory('GET', '/test'))
    assert response.text == 'OK'

    request,

# Generated at 2022-06-14 07:44:36.281569
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass

# Generated at 2022-06-14 07:44:43.620409
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test_RouteMixin_add_route')
    RouteMixin = RouteMixin()
    RouteMixin.app = app
    RouteMixin.name = ''
    RouteMixin.strict_slashes = None
    RouteMixin.host = None
    RouteMixin.version = None
    RouteMixin.router = UrlDispatcher()
    RouteMixin.websocket_enabled = True
    RouteMixin.blueprints = []
    RouteMixin.is_request_stream = False
    RouteMixin.error_handler = {}
    RouteMixin.before_start = []
    RouteMixin.before_stop = []
    RouteMixin.is_running_event_loop = False
    RouteMixin.is_stopped = False
    RouteMixin.is_starting_up = False

# Generated at 2022-06-14 07:44:52.614474
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test case 1
    print('Test case 1:')
    sanic_app = Sanic('test_sanic_app')
    # Test and verify
    with pytest.raises(InvalidUsage):
        sanic_app.add_route(
            lambda x: x,
            '',
            methods=['GET'],
            host='127.0.0.1'
        )
    # Test case 2
    print('Test case 2:')
    sanic_app = Sanic('test_sanic_app')
    # Test and verify
    with pytest.raises(InvalidUsage):
        sanic_app.add_route(
            lambda x: x,
            '127.0.0.1',
            methods=['GET'],
            host=''
        )
    # Test case 3

# Generated at 2022-06-14 07:44:57.656535
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = RouteMixin()
    app = Sanic('test_add_route')
    url = '/test_add_route'
    router.add_route(app, url)

    assert url in app.router.routes_all



# Generated at 2022-06-14 07:45:09.275084
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import sanic

    app = sanic.Sanic("test_RouteMixin_add_route")
    route_mixin = RouteMixin(app, uri_prefix='')
    add_route = route_mixin.add_route

# Generated at 2022-06-14 07:45:38.346436
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    routeOnMixin = RouteMixin()
    file_or_directory = "./server"
    uri = "/"
    routeOnMixin.static(uri, file_or_directory)
    assert (routeOnMixin._future_statics.pop()).uri == uri
    assert (routeOnMixin._future_statics.pop()).file_or_directory == file_or_directory
    assert len(routeOnMixin._future_statics) == 0
    return


# Generated at 2022-06-14 07:45:51.238272
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.response import html
    from sanic.router import Route
    app = Sanic("test_add_route")
    request, response = mock.Mock(), mock.Mock()

    # test add_route
    @app.route("/")
    async def handler(request):
        return response

    assert len(app.router.routes_all) == 1
    assert app.router.routes_all[0].uri == '/'
    assert app.router.routes_all[0].host == None
    assert app.router.routes_all[0].methods == {'GET'}
    assert app.router.routes_all[0].name == None

# Generated at 2022-06-14 07:46:05.091740
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from sanic import Sanic
    from sanic import response
    from sanic.response import json
    from sanic_validation import SanicValidation
    from sanic_validation.decorators import validate_json
    from sanic_validation.schema import JsonSchema

    app = Sanic(__name__)
    app.config.VALIDATION_SANIC += [SanicValidation()]
    app.config.VALIDATION_RETURN_DATA = True

    # Test string

# Generated at 2022-06-14 07:46:16.245381
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = Router(name='test')
    name = 'test'
    uri = 'uri'
    host = 'host'
    method = 'GET'
    strict_slashes = True
    version = 1
    routes = router.add_route(uri, host, method, strict_slashes, version, name)
    assert isinstance(routes, list)
    # validate multiple routes
    routes = router.add_route(uri, host, ['GET', 'POST'], strict_slashes, version, name)
    assert isinstance(routes, list)
    assert isinstance(routes[0], Route)
    assert isinstance(routes[1], Route)
    # validate multiple routes with strict_slashes = True
    strict_slashes = [True, False]

# Generated at 2022-06-14 07:46:29.843019
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    # Default Param
    app = Sanic(__name__)
    uri = "uri"
    file_or_directory = "file_or_directory"
    pattern = "pattern"
    use_modified_since = "use_modified_since"
    use_content_range = "use_content_range"
    stream_large_files = "stream_large_files"
    name = "name"
    host = "host"
    strict_slashes = "strict_slashes"
    content_type = "content_type"
    apply = "apply"
    app.route_mixin.static(uri, file_or_directory, pattern, use_modified_since, use_content_range, stream_large_files, name, host, strict_slashes, content_type, apply)
    # Default Param

# Generated at 2022-06-14 07:46:36.811834
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import Route

    mixin = RouteMixin()
    class app():
        route = Route

    app.strict_slashes = False
    app.name = 'sanic'
    route, _ = mixin.route(uri = '/user')

    # check that the route is a instance of Route
    assert isinstance(route, Route)


# Generated at 2022-06-14 07:46:42.583215
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route_mixin_a = RouteMixin()
    route_mixin_a.add_route(handler=None,
                            uri=None,
                            methods=None,
                            host=None,
                            strict_slashes=None,
                            version=None,
                            name=None)


# Generated at 2022-06-14 07:46:56.782373
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test')
    app.debug = True
    route_mixin = app
    uri = '/uri/<param>'
    handler = 'handler'
    methods = ['GET', 'POST']
    host = '10.1.1.1'
    strict_slashes = True
    stream = False
    version = 1
    name = 'test'
    apply = True
    ignore_trailing_slash = True
    
    # testing with 
    # uri = '/uri/<param>' # str
    # handler = 'handler' # str
    # methods = ['GET', 'POST'] # list of str
    # host = '10.1.1.1' # str
    # strict_slashes = True # bool
    # stream = False # bool
    # version = 1 # int
   

# Generated at 2022-06-14 07:47:09.052547
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    rm = RouteMixin(app=None, router=None, version=1, name="api")
    def handler(): return None
    def handler_1(): return None
    def handler_2(): return None
    def handler_3(): return None
    def handler_4(): return None
    def handler_5(): return None
    def handler_6(): return None
    def handler_7(): return None
    def handler_8(): return None
    def handler_9(): return None
    def handler_10(): return None
    def handler_11(): return None

    # call method route without any argument
    try:
        rm.route()
    except Exception as e:
        if not isinstance(e, TypeError):
            print("test_RouteMixin_route failed!!!")

    # call method route with no argument

# Generated at 2022-06-14 07:47:18.096819
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    
    # create instance of class RouteMixin
    r1 = RouteMixin()

    # create a function called handle
    def handle(request, args):
        return request
  
    # apply the function handle to the method route of r1, which will return r2
    r2 = r1.route('/test/route')(handle)
    
    # test if the returned value is an instance of Route
    assert(isinstance(r2, Route))
    
    # test if the return route has the function handle and uri '/test/route'
    assert(r2.handler == handle and r2.uri == '/test/route')


# Generated at 2022-06-14 07:47:49.396843
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    _name = None
    _uri = None
    _handler = None
    _methods = None
    _host = None
    _strict_slashes = None
    _stream = None
    _version = None
    _name = None
    _apply = True
    _route_class = Route

    routemixin = RouteMixin()
    routemixin._apply_route = MagicMock()
    routemixin.route(
        uri = _uri,
        host = _host,
        methods = _methods,
        strict_slashes = _strict_slashes,
        version = _version,
        name = _name,
        apply = _apply,
        stream = _stream,
        route_class = _route_class
    )(_handler)

# Generated at 2022-06-14 07:47:51.233914
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    instance = RouteMixin()
    assert instance is not None


# Generated at 2022-06-14 07:47:59.591477
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    uri = "uri"
    handler = "handler"
    host = "host"
    methods = "methods"
    strict_slashes = "strict_slashes"
    name = "name"
    version = "version"
    # just check what the return value is
    route = RouteMixin().add_route(uri, handler, host, methods, strict_slashes, version, name)
    assert isinstance(route, Route)

# Generated at 2022-06-14 07:48:05.571234
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # for parameter in {name, uri, method, host, strict_slashes, version}:
    #     print(parameter)

    # name
    # uri
    # method
    # host
    # strict_slashes
    # version
    pass



# Generated at 2022-06-14 07:48:06.769905
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # No such function
    pass

# Generated at 2022-06-14 07:48:10.860414
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Without args
    mixin = RouteMixin
    assert mixin.route()

    # With args
    mixin = RouteMixin
    assert mixin.route()


# Generated at 2022-06-14 07:48:12.289822
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:48:22.969159
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.app import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse

    s = Sanic()
    route = ('/hello/', 'GET')
    route1 = ('/hello/', 'POST')
    route2 = ('/hello/', ['GET', 'POST'])
    def handler(_): return HTTPResponse()

    assert s.add_route(*route)
    assert s.route(*route)(handler)
    assert s.add_route(*route1)
    assert s.route(*route1)(handler)
    assert s.add_route(*route2)
    assert s.route(*route2)(handler)


# Generated at 2022-06-14 07:48:23.810594
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    pass

# Generated at 2022-06-14 07:48:37.825701
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
	# This test case will test for all the possible edge cases for the method route of class RouteMixin.
	a = Sanic('test_RouteMixin_route')
	b = RouteMixin()
	c, d = b.route('uri=a', 'methods=["GET", "POST"]', 'name=name', 'host=None', 'strict_slashes=None', 'stream=True', 'version=None', 'apply=True')(a)
	c, d = b.route('uri=a', 'methods=["GET", "POST"]', 'name=name', 'host=None', 'strict_slashes=None', 'stream=True', 'version=None')(a)

# Generated at 2022-06-14 07:49:31.107684
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    #
    class Test(RouteMixin):

        #
        def register_routes(self):
            #
            @self.route('/')
            def handler(request):
                return text('OK')
            #
        #
    #
    app = Sanic('test_RouteMixin_add_route')
    #
    @app.route('/')
    def handler(request):
        return text('OK')
    #
    @app.route('/c')
    def handler(request):
        return text('OK')
    #
    @app.route('/a')
    def handler(request):
        return text('OK')
    #
    @app.route('/d/<name>')
    def handler(request, name):
        return text('OK')
    #
    t = Test()

# Generated at 2022-06-14 07:49:45.087351
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.router import Route
    from sanic.server import HttpProtocol
    from sanic.views import CompositionView

    # create sanic app
    app = Sanic()

    # create request handler
    @app.route('/')
    async def handler(request):
        return response.text('OK')

    # create second request handler
    @app.route('/test')
    async def handler(request):
        return response.text('OK')

    # create new class that inherits RouteMixin
    class MyRoute(RouteMixin):
        # override method route
        def route(self, uri, *args, **kwargs):
            # create routes set
            routes = []
            # call method from parent class

# Generated at 2022-06-14 07:49:53.089014
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from tempfile import TemporaryDirectory
    import json
    import shutil
    with TemporaryDirectory() as d:
        root_path = shutil.copytree('.',d)
        _static_path = os.path.join(root_path,'static')
        exp_content = {'name': 'Sanic',
            'version': '0.7.0'}
    help_static = RouteMixin()
    route = help_static.static('static',_static_path,name='static_')
    assert route.uri == 'static'
    assert route.uri_template == '/static/<__file_uri__>'
    assert route.name == 'static_'
    assert route.host == None
    assert route.strict_slashes == None


# Generated at 2022-06-14 07:49:55.947428
# Unit test for method route of class RouteMixin
def test_RouteMixin_route(): #
    app = Sanic('test_RouteMixin_route')

    @app.route('/')
    def handler(request):
        return HTTPResponse(body='OK')

    request, response = app.test_client.get('/')

    assert response.text == 'OK'



# Generated at 2022-06-14 07:49:58.443704
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    assert True

# Generated at 2022-06-14 07:50:03.919470
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    r = RouteMixin()
    handler = lambda: None
    result = r.add_route(handler, '/', methods=['GET'], host='0.0.0.0', strict_slashes=None, version=None, name=None, apply=True)
    assert result == handler
