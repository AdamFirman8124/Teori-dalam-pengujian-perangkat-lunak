

# Generated at 2022-06-14 07:40:34.182277
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.exceptions import InvalidUsage
    from sanic.response import json
    from sanic.views import HTTPMethodView
    from sanic.router import Route

    class ExampleView(HTTPMethodView):
        def get(self, request):
            return json({"received": True})

    # Class to test
    class RouteMixinMock:
        def __init__(self):
            self.router = Mock()
            self.exception_handler = Mock()
            self.response_class = Mock()
            self.error_handler = Mock()

        def add_route(self, uri, methods, *args, **kwargs):
            return uri, methods

        def add_websocket_route(self, uri, *args, **kwargs):
            return uri

    # Tests

# Generated at 2022-06-14 07:40:40.508334
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    b = Sanic()
    c = RouteMixin()
    c.add_route(b.add_route, route='/', handler=b, host=None,
                methods=['GET', 'OPTIONS'], strict_slashes=None,
                stream=False, version=None, name='root',
                websocket=False,
                apply=True)
    if b._routes['GET'] != []:
        assert True
    else:
        assert False


# Generated at 2022-06-14 07:40:53.010752
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.constants import DEFAULT_HTTP_BODY_SIZE_LIMIT
    # memnonic: kybrd kat
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    class MockSanic:
        def __init__(self):
            self.router = Router()
            self.blueprints = []
            self.config = {"MAX_REQUEST_ARGUMENT_SIZE": DEFAULT_HTTP_BODY_SIZE_LIMIT}
            self.websocket_enabled = False
            self.websocket_max_size = None
            self.websocket_max_queue = 128
            self.websocket_max_http_version = "1.1"
            self.websocket_compression

# Generated at 2022-06-14 07:41:05.600505
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class Sanic(RouteMixin):
        @property
        def routes(self):
            return []

    sanic = Sanic()
    sanic.add_route(uri='uri', methods=['methods'], name='name', host='host', strict_slashes='strict_slashes', version='version', errors='errors', stream='stream', register_scheme='register_scheme', register_ext='register_ext', blueprint='blueprint', blueprint_group='blueprint_group', strict_slashes='strict_slashes')
    sanic.add_websocket_route(handler='handler', uri='uri', host='host', strict_slashes='strict_slashes', subprotocols='subprotocols', version='version', name='name')

# Generated at 2022-06-14 07:41:13.274331
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic()
    @app.route('/')
    def handler(request):
        return response.text('OK')
    assert app.add_route(handler, '/')
    # Test for arbitrary arguments
    assert app.add_route(handler, '/', 'GET', None, None, False, False, False, 0, 'handler', 777, None)
    # Test for arbitrary keyword arguments
    assert app.add_route(handler, uri='/', version=100, name='handler')


# Generated at 2022-06-14 07:41:19.413261
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    rm = RouteMixin()
    rm.add_route("/", lambda request: text("OK"))
    assert rm.routes[0].name == "default-route"
    rm.add_route("/", lambda request: text("OK"))
    assert rm.routes[1].name == "default-route-1"

# Generated at 2022-06-14 07:41:28.794826
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from gidgethub.sansio import Event
    from src.sanic_app import app
    from src.route_mixin import RouteMixin
    from src.handlers import handle_issue_opened

    class DummyEvent(Event):
        payload = {
            "action": "opened",
            "issue": {"title": "Pregunta"},
        }

    rm = RouteMixin(app)
    rm.add_route("/", handle_issue_opened, "POST")
    response = rm.app.handle_request(
        DummyEvent(
            method="POST",
            body=json.dumps(DummyEvent().payload),
            headers={"content-type": "application/json"})
    )
    assert response.status_code == 200

# Generated at 2022-06-14 07:41:43.224743
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    target = RouteMixin()

    decorated = target.route("/", name="test_route")(function_fixture)

    routes = target.routes

    assert isinstance(routes, list)
    assert len(routes) == 1
    route = routes[0]
    assert isinstance(route, Route)
    assert route.uri == "/"
    assert route.name == "test_route"
    assert route.handler is function_fixture
    assert route.methods is None
    assert route.strict_slashes is None
    assert route.version is None
    assert route.host is None
    assert route.static is False
    assert route.websocket is False
    assert route.apply == True
    assert route.subprotocols is None

# Generated at 2022-06-14 07:41:44.667852
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Pass
    return


# Generated at 2022-06-14 07:41:57.729591
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # arrange

    # act
    paths, method, handler, name, host, strict_slashes, version, uri_var_name, 
    response_class, stream_output, methods, subprotocols, websocket = add_route(paths=None, method=None, 
    handler=None, name=None, host=None, strict_slashes=None, version=None, 
    uri_var_name=None, response_class=None, stream_output=None, methods=None, 
    subprotocols=None, websocket=True, apply=True,)

    # assert
    assert type(paths) == list
    assert isinstance(methods, (list, set, tuple, type(None)))
    assert callable(handler) #or callable(handler.run)
    assert name == None
   

# Generated at 2022-06-14 07:42:19.311690
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    """Unit test for method route of class RouteMixin."""    
    route_obj = Router()

    # test for different cases of parameter uri
    route_obj.route(uri="/uri")
    route_obj.route(uri="/uri/")  
    route_obj.route(uri="/uri/<uri_id>")
    route_obj.route(uri="/uri/<uri_id>/")
    route_obj.route(uri="/uri/<uri_id>/<uri_name>")
    route_obj.route(uri="/uri/<uri_id>/<uri_name>/")  
    route_obj.route(uri="/uri/<uri_id>/<uri_name>/<end>")

# Generated at 2022-06-14 07:42:31.137220
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    class TestRouteMixin(RouteMixin):
        pass
    url_for_mock = Mock(return_value='mock_url')
    request_mock = Mock()
    request_mock.app.url_for = url_for_mock
    response_mock = Mock()
    response_mock.app.url_for = url_for_mock
    with patch('sanic.router.Route') as route_mock:
        route_mock.return_value = Mock()
        route = TestRouteMixin().add_route(request_mock, response_mock,
                                           name='test_route_name')
        assert route_mock.call_args[0][0] == request_mock
        assert route_mock.call_args

# Generated at 2022-06-14 07:42:44.287018
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class _Handler(object):
        def handler(self, request):
            pass

        handler.__name__ = "handler"
        handler.__qualname__ = "handler"

        def second_handler(self, request):
            pass

        second_handler.__name__ = "second_handler"
        second_handler.__qualname__ = "second_handler"
    router = Router(strict_slashes=True, version=None)
    handler = _Handler()
    # test for uri, handler, strict_slashes not given
    @router.route("/test", methods=["get", "post"])
    def test(request):
        pass
    routes = router.routes_all[0]
    assert(routes.uri == "/test")

# Generated at 2022-06-14 07:42:56.625056
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # set up
    routes = []

    class Handler:
        def __call__(self, request):
            pass

    handler = Handler()

    # call route
    routes = add_route(routes, "uri1", handler, None, None,
                       strict_slashes=False, version=None, name="name1",
                       host="host1")
    # assert_that(routes)
    assert_that('uri1' in routes[0].uri)
    assert_that('name1' in routes[0].name)
    assert_that('host1' in routes[0].host)

    # call add_websocket_route

# Generated at 2022-06-14 07:43:09.254003
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Create an instance of RouteMixin for testing
    test_instance = RouteMixin()

    # Create a test handler for use with
    # test_instance.add_route(handler, uri, host, strict_slashes, name)
    def test_handler(request):
        return HTTPResponse('<html><body>Test</body></html>')
    # Use one of test_instance's methods to test add_route
    # Case 1: test_instance.add_websocket_route
    test_instance.add_websocket_route(test_handler, '/test', None, None, None, 'test_instance.test')
    # Case 2: test_instance.add_static_route

# Generated at 2022-06-14 07:43:21.415866
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    s = RouteMixin()
    url = '<name:string>'
    methods = ['GET', 'HEAD']
    host = None
    strict_slashes = None
    version = None
    name = None
    apply = False
    expected = [
    {
        'host': None, 
        'methods': ['GET', 'HEAD'], 
        'name': None, 
        'strict_slashes': None, 
        'uri': '<name:string>', 
        'version': None
    }]
    actual = s.add_route(uri=url,methods=methods, host=host, strict_slashes=strict_slashes, version=version, name=name, apply=apply)
    assert actual==expected
test_RouteMixin_add_route()


# Generated at 2022-06-14 07:43:35.846840
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    print("launching unit test for method add_route of class RouteMixin")

    app = Sanic("test")
    app.routes = [
        Route(
            "GET",
            "/",
            handler=None,
            host=None,
            strict_slashes=None,
            version=None,
            name=None,
            subprotocols=None,
            websocket=False,
            static=False,
        )
    ]
    print("\n1) Testing with uri, method, handler and name as parameters")
    print("Expected output: method=GET, uri=/test, name=test")

    app.add_route(handler=None, method="GET", uri="/test", name="test")


# Generated at 2022-06-14 07:43:40.362447
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():

    import sanic.app
    import asyncio

    async def handle_request(request):
        return sanic.response.text("OK")

    app = sanic.app.Sanic(name="san")

    # Function
    app.add_route(handle_request, uri="/")
    assert len(app.router.routes_all) == 1

    # Class
    class HandleClass:
        async def handle_request(self, request):
            return sanic.response.text("OK")
    app.add_route(HandleClass().handle_request, uri="/")
    assert len(app.router.routes_all) == 2

    class HandleClassWithoutHandleRequest:
        pass

# Generated at 2022-06-14 07:43:46.874364
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from sanic import Sanic
    app = Sanic()
    
    # Test with empty inputs
    
    assert app.static(uri=None) is None,"The function did not return the expected output"
    assert app.static(file_or_directory=None) is None,"The function did not return the expected output"
    assert app.static(uri=None,file_or_directory=None) is None,"The function did not return the expected output"


# Generated at 2022-06-14 07:43:48.799335
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    route = RouteMixin()
    pass


# Generated at 2022-06-14 07:44:03.628581
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    result_route = RouteMixin().add_route(handler,uri)
    assert result_route is not None
    pass


# Generated at 2022-06-14 07:44:16.179848
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class TestRouteMixin:
        def __init__(self):
            self.routes = []
            self.handler = handler
            self.strict_slashes = strict_slashes
            self.uri = uri
            self.methods = methods
            self.host = host
            self.version = version
            self.name = name
            self.stream = stream
            self._future_statics = _future_statics
            self.websocket = websocket
            self.uri_template = uri_template
            self.register_route = register_route
            self.before_start = before_start

        def apply(self, func, *args, **kwargs):
            self.func = func
            self.args = args
            self.kwargs = kwargs


# Generated at 2022-06-14 07:44:28.488914
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic(__name__)

    @app.route('/')
    def handler(request):
        pass

    @app.route('/foo/<bar>')
    @app.route('/foo/<bar>/<baz>')
    def handler_multi(request, bar, baz=None):
        pass

    @app.websocket('/feed')
    def feed(request, ws):
        pass

    @app.static('/image', './test.png')
    def static(request):
        pass

    @app.route('/', methods=['GET'])
    def handler(request):
        pass

    @app.route('/foo/<bar>', methods=['GET', 'POST'])
    def handler_multi(request, bar, baz=None):
        pass

# Generated at 2022-06-14 07:44:39.491234
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    SanicApp = RouteMixin(name="test_route_mixin")
    SanicApp.add_route(handler=None, uri="/", host=None, strict_slashes=None, methods=None, version=None, name=None)
    SanicApp.add_route(handler=None, uri="/b", host=None, strict_slashes=None, methods=None, version=None, name=None)
    SanicApp.add_route(handler=None, uri="/c", host=None, strict_slashes=None, methods=None, version=None, name=None)

# Generated at 2022-06-14 07:44:50.743184
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from unittest import TestCase

    from asynctest import patch, CoroutineMock

    from asgiref.sync import AsyncToSync
    from asgiref.sync import sync_to_async

    with patch("sanic.router.Router") as MockRouter:
        instance = MockRouter.return_value
        instance.url_for = CoroutineMock()

        # __main__.RouteMixin
        class RouteMixin(AsyncToSync):
            def add_route(self, route: "Sanic", *args, **kwargs):
                pass

        class SanicMock:
            router_class = MockRouter
            router = MockRouter.return_value

        # __main__.RequestParameters

# Generated at 2022-06-14 07:45:05.254931
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class Sanic(RouteMixin):
        def __init__(self, name, strict_slashes):
            self.name = name
            self.strict_slashes = strict_slashes

    # self.name can be any string
    self = Sanic('sanic', strict_slashes=None)

    name = None
    host = None
    strict_slashes = None
    version = None
    apply = False
    uri = '/sanic'
    methods = ['GET', 'POST']
    # Check uri is mandatory parameter

# Generated at 2022-06-14 07:45:17.978738
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class Sanic:
        exception_handler = None
        def __init__(self, name):
            self.name = name
            self.router = Router()

    app = Sanic("sanic")
    mixin = RouteMixin(app)

    @mixin.route("/", strict_slashes=None, version=None, name=None, apply=True, websocket=False)
    def test_1(request):
        return text("success")

    @mixin.route("/", strict_slashes=False, version=None, name=None, apply=True, websocket=False)
    def test_2(request):
        return text("success")


# Generated at 2022-06-14 07:45:32.272621
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    request = Request({'type': 'http', 'path': '/', 'headers': {}, 'raw_uri': '/'}, b'', '127.0.0.1', 8000, False, False)
    class Node:
        def __init__(self, path, pattern, handler, strict_slashes, name=None):
            self.path = path
            self.pattern = pattern
            self.handler = handler
            self.strict_slashes = strict_slashes
            self.name = name
    class Router(RouteMixin):
        def __init__(self):
            self.routes = [Node('/', '^/$', lambda request: HTTPResponse("OK"), False)]
            self.statics = {}
    router = Router()

# Generated at 2022-06-14 07:45:35.801074
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    with pytest.raises(ValueError):
        router = RouterMixin(app=None)
        router.add_route(None, None, None, None)


# Generated at 2022-06-14 07:45:49.013031
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    from sanic.exceptions import InvalidUsage
    from sanic.request import Request
    from unittest.mock import patch, MagicMock
    # A mock class with routes
    class MockRouteMixin():
        routes = []
        subdomain = None
        host_name = None
        version = None
        prefix = None
        name = None
        # A mock method to return routes
        def get_routes(self):
            return self.routes
    mock_route_mixin = MockRouteMixin()
    # A mock class with a route to be added
    class MockRoute():
        def __init__(self, uri, host):
            self.uri = uri
            self.host = host
        # Property to return the uri

# Generated at 2022-06-14 07:46:11.638295
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:46:14.526870
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
	
	# 1.test_route_has_no_parent
	# Not implemented
	pass


# Generated at 2022-06-14 07:46:26.827617
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    def method_test_RouteMixin_static(self):
        app = Sanic("test_RouteMixin_static")
        router = app.router
        router.static(uri='/test', file_or_directory='test', pattern=None, use_modified_since=True, use_content_range=False, stream_large_files=False, name='test', host=None, strict_slashes=None, content_type='html')
        assert router._future_statics != None

    def method_test_RouteMixin_static_uri_none(self):
        app = Sanic("test_RouteMixin_static_uri_none")
        router = app.router

# Generated at 2022-06-14 07:46:40.759210
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    """Unit test for method static of class RouteMixin"""

    r = RouteMixin()
    # Test for when len(args) == 1 and len(kwargs) == 0
    r.static("/static", "static.html")
    
    # Test for when len(args) == 1 and len(kwargs) > 0
    r.static("/static", "static.html", pattern="r")
    
    # Test for when len(args) > 1 and len(kwargs) > 0
    r.static("/static", "static.html", pattern="r", use_modified_since = True)
    
    # Test for when len(args) > 1 and len(kwargs) == 0
    r.static("/static", "static.html", use_modified_since = True)
    

# Generated at 2022-06-14 07:46:49.522850
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.response import text
    from sanic.router import Route, RouteExists

    def handler(request):
        return text("OK")

    app = Sanic(__name__)

    # test 1
    app.route("/", methods=["GET", "POST"])(handler)
    assert len(app.router.routes_all) == 1

    # test 2
    try:
        app.route("/")(handler)
    except RouteExists as e:
        assert str(e) == "/"
    else:
        assert False, "test_RouteMixin2 failed; except RouteExists not raised"

    # test 3
    try:
        app.route("/", methods=["GET"])(handler)
    except RouteExists as e:
        assert str

# Generated at 2022-06-14 07:47:01.952100
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    ################################################################################
    # Required parameters for route instantiation
    ################################################################################
    uri = "/test_add_route/<test_param>"
    handler = not_found_handler
    name = "test_add_route"

    ################################################################################
    # Optional parameters for route instantiation
    ################################################################################
    host = "sanic.com"
    methods = ["POST", "GET"]
    strict_slashes = True
    version = 1
    stream = True
    requirements = {}
    raw_strings = True
    versioned_methods = []
    register_uri_template = True
    static = True
    websocket = True

    ################################################################################
    # Testing parameters that is not None or an empty list or dictionary
    ################################################################################
    #

# Generated at 2022-06-14 07:47:13.762268
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():

    from sanic.router import RouteMixin

    from sanic.static import FutureStatic

    from sanic.utils import sanic_endpoint_test
    api = RouteMixin()

    # TODO: find a canonical way to get the TEMP_PATH
    file_or_directory = 'D:\\Temp\\sanic_test_folder'
    # TODO: find a canonical way to get the TEMP_PATH
    uri = '/sanic_test_folder'
    pattern = r"/?.+"
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = "static"
    host = None
    strict_slashes = None
    content_type = None
    apply = True

    # Test function with no parameters

# Generated at 2022-06-14 07:47:20.970937
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Arrange
    def handler():
        pass

    router = RouteMixin()
    host = None
    uri = "test"
    methods = None
    strict_slashes = None
    version = None
    name = None
    apply = True
    websocket = False

    # Act
    route = router.route(
        uri=uri,
        host=host,
        methods=methods,
        strict_slashes=strict_slashes,
        version=version,
        name=name,
        apply=apply,
        websocket=websocket,
    )(handler)

    # Assert
    assert isinstance(route, namedtuple)
    assert route.uri == ""



# Generated at 2022-06-14 07:47:33.975605
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    '''
    Unit test for method route of class RouteMixin
    
    '''
    
    args = []
    if len(args) == 0:
        print('Testing function name: test_RouteMixin_route')
        print('No input args')
        print('Expected <class \'sanic.router.Route\'> as return type')
        
        # Test with default args
        # Function set up
        sanic_route = RouteMixin()
        
        # Function to be tested
        print('Testing with default args')
        sanic_route.route()
        
        # Assertion
        #self.assertEqual()
        print('<class \'sanic.router.Route\'> == <class \'sanic.router.Route\'>? ')

# Generated at 2022-06-14 07:47:47.050358
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route, RouteExists

    router = RouteMixin()
    try:
        router.add_route(
            Route(None, None, None, None, None, None, None, None)
        )
    except BaseException:
        pass
    else:
        raise Exception(
            "Should not have been able to add a Route without a path."
        )

    try:
        router.add_route(
            Route("/", None, None, None, None, None, None, None)
        )
    except RouteExists as e:
        if str(e) != "/":
            raise Exception(
                "Should not have been able to add a Route without a path."
            )
    else:
        raise Exception(
            "Should not have been able to add a Route without a path."
        )

# Generated at 2022-06-14 07:48:12.411668
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    assert True


# Generated at 2022-06-14 07:48:16.177813
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic()
    app.route('/test')(lambda request: HTTPResponse())
    return len(app._routes) == 1

# Generated at 2022-06-14 07:48:24.176317
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    method_name = 'add_route'
    # Test1: call without parameters
    @sanic.Sanic.route
    def handler(request):
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    router = self.Router()
    router.add_route('/<name>', methods=['get'], handler=handler)
    # Test2: call with parameters
    router.add_route('/<name>', methods=['get'], handler=handler,
                     host='localhost', strict_slashes=False, version=None,
                     name='handler', apply=True)


# Generated at 2022-06-14 07:48:38.269154
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    rm1 = RouteMixin()
    rm2 = RouteMixin()

    handler = lambda x: x

    rm1._register_route(
        Route(
            RouteType.HTTP,
            "POST",
            "/",
            handler,
            name="Hello",
            host=None,
            version="1",
            strict_slashes=False,
            http_expect=False,
            websocket=False,
            stream=False,
            static=False,
        )
    )

# Generated at 2022-06-14 07:48:43.237353
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    assert RouteMixin.add_route.__doc__
    obj = RouteMixin()
    obj.add_route(uri,handler,methods=['GET'],host=None,strict_slashes=True,version=None,name=None,stream=False)

# Generated at 2022-06-14 07:48:51.444853
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Sanic app call
    app = Sanic('test_RouteMixin_route')
    app.router.add(Rule('a', endpoint='d', methods=['GET']))
    app.router.add(Rule('b', endpoint='d', subdomain=None, methods=['POST']))
    app.router.add(Rule('d', endpoint='d', subdomain=None, methods=['POST']))

    # test_RouteMixin_route_a
    route, _ = app.route('/a', methods=['GET'], version=None, apply=False)(app.d)
    assert route.uri == '/a' and route.endpoint == 'd' and route.host == 'test_RouteMixin_route'

    # test_RouteMixin_route_b

# Generated at 2022-06-14 07:48:53.057149
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    r = RouteMixin()
    route = r.route(uri="uri_test")
    assert 'route' in route.func.__name__

# Generated at 2022-06-14 07:49:02.009861
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    Sanic_obj = Sanic()
    assert Sanic_obj.route(uri="uri_string", host="host_string", version="version_string", methods="methods_string", name="name_string", static="static_string", strict_slashes="strict_slashes_string", websocket="websocket_string", stream="stream_string", subprotocols="subprotocols_string", apply="apply_string") == ((Route(uri="uri_string", host="host_string", version="version_string", method="methods_string", name="name_string", static=0, strict_slashes=0, websocket=0, stream=0, subprotocols="subprotocols_string", apply=0),),)

# Generated at 2022-06-14 07:49:15.045691
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    #prepare data
    uri = "test"
    host = None
    strict_slashes = None
    version = None
    name = "test"
    apply = True

    #execute function
    methods = ["GET"]
    routes = test_object.add_route(uri=uri, host=host, methods=methods, strict_slashes=strict_slashes, version=version, name=name, apply=apply)
    #assert results
    assert(len(routes) == 1)
    assert(routes[0].methods == methods)
    assert(routes[0].uri == uri)
    assert(routes[0].host == host)
    assert(routes[0].strict_slashes == strict_slashes)

# Generated at 2022-06-14 07:49:23.145340
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic(__name__)
    @app.route("/")
    async def handler(request):
        return response.text("OK")

    try:
        func_handler = app.add_route(handler, "/abc", methods=["GET", "aaa"], strict_slashes=True)
    except RuntimeError as err:
        print(err)
    else:
        assert type(func_handler) == types.CoroutineType

