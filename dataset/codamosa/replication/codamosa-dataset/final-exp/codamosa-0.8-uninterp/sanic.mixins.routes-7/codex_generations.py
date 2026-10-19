

# Generated at 2022-06-14 07:40:40.296163
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    '''
    Test the RouteMixin class
    
    '''
    # Test the method add_route of class RouteMixin
    def test_add_route():

        # Test add_route with parameter host is True
        def test_add_route_with_host_is_true():
            router = RouteMixin(None, [], [])
            handler = router.add_route(None, host=True)
            handler(None)
            assert False

        test_add_route_with_host_is_true()

        # Test add_route with parameter use_schema is True
        def test_add_route_with_use_schema_is_true():
            router = RouteMixin(None, [], [])
            handler = router.add_route(None, use_schema=True)
            handler(None)

# Generated at 2022-06-14 07:40:51.329644
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    router = RouteMixin(app)

    # re
    with pytest.raises(TypeError):
        router.route(
            uri="/lkj",
            methods=["GET"],
            version=1,
            name="lkj",
            host=None,
            strict_slashes=None,
            re=None,
            apply=True
        )
    
    # apply
    with pytest.raises(TypeError):
        router.route(
            uri="/lkj",
            methods=["GET"],
            version=1,
            name="lkj",
            host=None,
            strict_slashes=None,
            re=1,
            apply=None
        )

# Generated at 2022-06-14 07:40:57.329709
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class Test():
        pass
    test = Test()
    setattr(test, "name", "test")
    uri = "test"
    handler = "test"
    test.add_route(uri, handler)
    assert uri in test.routes


# Generated at 2022-06-14 07:40:58.100805
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass

# Generated at 2022-06-14 07:41:08.581692
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.response import text
    from sanic.router import Route
    from types import MethodType
    import pytest
    
    app = Sanic()
    app.listen = object()
    app.add_task = object()
    app.is_request_stream = object()
    app.blueprints = object()
    app.config = object()
    app.exception_handler = object()
    app.error_handler = object()
    app.before_start = object()
    app.before_server_start = object()
    app.after_start = object()
    app.before_stop = object()
    app.after_stop = object()
    app.exception = object()
    app.prepare = object()
    app.request_middleware = object()
   

# Generated at 2022-06-14 07:41:14.984092
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.response import json

    app = Sanic("test_route_mixin")

    @app.get("/")
    def handler(request):
        return json({"test": True})

    assert len(app.router.routes_names["GET"]) == 1
    assert app.router.routes_names["GET"][0].name == 'handler'
    assert app.router.routes_names["GET"][0].uri == '/'


# Generated at 2022-06-14 07:41:16.378161
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:41:18.846430
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
	# Initialize the class RouteMixin and call the method route
	RouteMixin().route()


# Generated at 2022-06-14 07:41:28.523170
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    route = RouteMixin
    method = RouteMixin.route
    assert method.__doc__ is not None
    assert method.__name__ == "route"

    assert len(method.cache["GET"]) == 0
    assert len(method.cache["POST"]) == 0
    assert len(method.cache["PUT"]) == 0
    assert len(method.cache["DELETE"]) == 0

    # Realize cache
    assert len(method.cache["GET"]) != 0
    assert len(method.cache["POST"]) != 0
    assert len(method.cache["PUT"]) != 0
    assert len(method.cache["DELETE"]) != 0

    # Get the first route to injection
    route_ = list(method.cache["GET"].values())[0]
    assert route.uri == "/"
   

# Generated at 2022-06-14 07:41:42.994224
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = RouteMixin()

    @router.add_route(uri='/', methods=None, host=None, 
                      strict_slashes=None, version=None, name=None, 
                      apply=None)
    def handler1(request):
        pass

    @router.add_route(uri='/user/<name>', methods=None, host=None, 
                      strict_slashes=None, version=None, name=None, 
                      apply=None)
    def handler2(request, name):
        pass

    @router.add_websocket_route(handler=None, uri='/feed', 
                                host=None, strict_slashes=None, 
                                subprotocols=None, version=None, name=None)
    def handler3():
        pass

   

# Generated at 2022-06-14 07:42:06.504142
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.response import html
    from sanic.router import Route
    from sanic.views import HTTPMethodView

    app = Sanic('test_RouteMixin_route')

    @app.route('/test')
    async def handler(request):
        return html("I'm a teapot")

    methods = ['GET', 'POST', 'PUT', 'DELETE']
    uri = app.url_for('handler')
    custom_methods = ['PATCH', 'OPTIONS']

    routes = app.router.routes_all
    assert len(routes) == 1
    route = next(iter(routes))

    assert route.methods == ['GET']
    assert route.uri == uri
    assert route.name == 'handler'

# Generated at 2022-06-14 07:42:18.141092
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from unittest.mock import MagicMock
    app = MagicMock()
    app.router.routes_names.add = MagicMock()
    routes = MagicMock()
    app.router.routes = routes
    app.router.routes_all = routes
    app.router.add_route = MagicMock()
    app.websocket_tasks = []
    app.static = []
    app.expect_websocket = []
    app.error_handler = {}
    app.blueprints = []
    app.static_routes = routes
    app.router.routes_all = {}
    app.router.strict_slashes = None
    app.url_for = MagicMock()
    app.name = "app"
    ur

# Generated at 2022-06-14 07:42:29.421089
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    class MockRouteMixin(RouteMixin):
        def __init__(self):
            self.name = None # TODO: FIXME

    routeMixin = MockRouteMixin()
    result = routeMixin.static(uri = "uri_1", file_or_directory = "file_or_directory_1", pattern = "pattern_1", use_modified_since = True, use_content_range = True, stream_large_files = True, name = "name_1", host = "host_1", strict_slashes = "strict_slashes_1", content_type = "content_type_1", apply = True)
    assert True


# Generated at 2022-06-14 07:42:31.003683
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:42:44.162520
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from framework.route_mixin import RouteMixin
    from framework.route import Route
    from framework.server import Sanic
    app = Sanic("test_sanic")
    routeMixin = RouteMixin(app, "/test")
    handler = lambda: True
    name = "test"
    host = "127.0.0.1"
    strict_slashes = True
    methods = ["GET"]
    version = 1
    apply = False
    uri = "/route"
    _uri, _host, _strict_slashes, _methods, _version, _name, _apply, _handler = routeMixin.route(uri=uri, host=host, strict_slashes=strict_slashes, methods=methods, version=version, name=name, apply=apply)(handler)

# Generated at 2022-06-14 07:42:48.268552
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass
    # obj = RouteMixin()
    # route, handler = obj.route(uri=uri,methods=methods,version=version,name=name,hosts=hosts,strict_slashes=strict_slashes,apply=apply)
    # test = pass


# Generated at 2022-06-14 07:42:49.635716
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:42:51.095753
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    _result = RouteMixin.route()

# Generated at 2022-06-14 07:43:05.135408
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    request = sanic.request.Request({})
    method = request.method
    uri = request.url
    host = request.host
    strict_slashes = request.strict_slashes
    version = request.version
    name = None
    apply = True
    new_route = RouteMixin().route(method, uri, host, strict_slashes, version, name, apply)
    # Test with the default value of method (GET, HEAD, OPTIONS, PUT, PATCH and DELETE)

# Generated at 2022-06-14 07:43:19.043115
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class _RouteMixin(RouteMixin):
        def test(self):
            pass
    # __main__.RouteMixin
    assert _RouteMixin.__name__ == RouteMixin.__name__
    # True
    assert isinstance(_RouteMixin(), RouteMixin)
    # ('test', ('/test',))
    assert _RouteMixin().route('/test')(_RouteMixin().test)[1] == ('test', ('/test',))
    # ('test', ('/test',))
    assert _RouteMixin().route('/test')(_RouteMixin().test)[1] == ('test', ('/test',))
    # ('test', ('/test',))
    assert _RouteMixin().route('/test')(_RouteMixin().test)[1] == ('test', ('/test',))
   

# Generated at 2022-06-14 07:43:33.650072
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class Testmixin(RouteMixin):
        pass
    t = Testmixin()
    t.route()


# Generated at 2022-06-14 07:43:41.327670
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic(__name__)
    path = "/test"
    uri = f"http://127.0.0.1:8000{path}"
    client = app.test_client

    @app.route(path)
    def handler(request):
        return text("OK")

    request, response = client.get(uri)
    assert response.status == 200
    assert response.text == 'OK'


# Generated at 2022-06-14 07:43:49.515125
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    uri="uri"
    file_or_directory="file_or_directory"
    pattern="pattern"
    pattern="pattern"
    use_modified_since=True
    use_content_range=False
    stream_large_files=False
    name="static"
    host=None
    strict_slashes=None
    content_type=None
    apply=True
    routeMixin = RouteMixin()
    routeMixin.static(uri,file_or_directory,pattern,use_modified_since,use_content_range,stream_large_files,name,host,strict_slashes,content_type,apply)


# Generated at 2022-06-14 07:43:59.978334
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():

	#create object of class RouteMixin
	rm1 = RouteMixin()

	#create object of Route class
	r1 = Route()
	r1.name = "r1"
	r1.host = "r1.com"

# Generated at 2022-06-14 07:44:13.822269
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Test function to test the following code
    #
    # route = RouteMixin()
    # route.route(uri,methods=methods,host=host,strict_slashes=strict_slashes,version=version,name=name,apply=apply,url_prefix=url_prefix,static=static,stream=stream)
    # (f, r) = route.route(uri,methods=methods,host=host,strict_slashes=strict_slashes,version=version,name=name,apply=apply,url_prefix=url_prefix,static=static,stream=stream)(f)
    
    
    
    
    
    
    
    
    
    
    # Get the class RouteMixin
    routeMixin_class = RouteMixin
    # Initialize an object routeMixin_inst

# Generated at 2022-06-14 07:44:26.708378
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    """Unit test for method route of class RouteMixin"""
    import sanic.server
    router=RouteMixin()
    server=sanic.server.Server(router)
    server.server_settings["REQUEST_MAX_SIZE"]=50000000
    server.server_settings["REQUEST_TIMEOUT"]=3600

    router.route(uri='/', methods=None, 
                 host=None, strict_slashes=None, 
                 version=None, name=None, 
                 apply=True, static=True, 
                 websocket=False, stream=False)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-14 07:44:34.665401
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic import response

    app = Sanic(name='testRouteMixin')
    app.config.KEEP_ALIVE = False
    app.config.KEEP_ALIVE_TIMEOUT = None
    @app.route('/testRouteMixin')
    def handler_testRouteMixin(request):
        return response.text('OK')

    # Testing
    request, response = app.test_client.get('/testRouteMixin')
    assert response.text == 'OK'
    assert response.status == 200


# Generated at 2022-06-14 07:44:38.407484
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = RouterMixin()
    assert router.add_route('hello', lambda x : x, host_name='localhost', strict_slashes=True, websocket=True, version=1, name='name', apply=True) is None


# Generated at 2022-06-14 07:44:51.641988
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class App(RouteMixin):
        def __init__(self):
            super().__init__(name="app", strict_slashes=True)
            self.route_list = []

        def route(self, *args, **kwargs):
            self.route_list.append((args, kwargs))
            return args, kwargs

        def add_route(self, handler, uri, methods=None, host=None,
                      strict_slashes=None, version=None):
            self.route(
                uri, methods, host=host, strict_slashes=strict_slashes,
                version=version
            )(handler)

    app = App()
    @app.route("/", methods=["GET"])
    def handler(request):
        return text("OK")

    assert app.route_

# Generated at 2022-06-14 07:44:57.278409
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass
    # route = Route()
    # actual = route.route(uri="", host=None, strict_slashes=False,
    #                     methods=None, version=None,
    #                     name=None, apply=True)
    # expect = Route()
    # assert actual == expect


# Generated at 2022-06-14 07:45:32.093464
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    # 1.
    router = RouteMixin(strict_slashes=True)
    router.route("/test/", methods=["GET"])(print)
    routes = router.routes_all
    assert len(routes) == 1
    route = routes[0]
    assert route.uri == "/test/"
    assert route.methods == ["GET"]
    assert route.host == None
    assert route.strict_slashes == True
    assert route.version == None
    assert route.name == None
    assert route.websocket == False
    assert route.stream is None
    assert route.static == False

    # 2.
    router = RouteMixin(strict_slashes=True)

# Generated at 2022-06-14 07:45:41.121085
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    """
    Test Add_route method of class RouteMixin
    """

    class TestSanic(RouteMixin):
        pass

    sanic = TestSanic()
    handler = lambda request: "test"

    with patch.object(RouteMixin, "_generate_name", return_value="test"):
        with patch.object(RouteMixin, "_add_route") as mock:
            sanic.add_route(handler, "/test")

    assert mock.call_count == 1
    assert mock.call_args == call(handler, "/test", methods=None, strict_slashes=None, name="test")


# Generated at 2022-06-14 07:45:49.012210
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    @RouteMixin.static(uri="/static/test",file_or_directory="test")
    @RouteMixin.static(uri="/static/test2",file_or_directory="test2")
    def test_static(self):
        self.assertEqual(self._static_request_handler("test"),HTTPResponse(status=304))
        self.assertEqual(self._static_request_handler("test2"),HTTPResponse(status=304))
    RouteMixin("test").test_static()

# Generated at 2022-06-14 07:45:59.573534
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.app import Sanic
    from sanic import exceptions
    from sanic.response import json
    from sanic.router import Route
    from sanic.router import RouteExists
    from sanic.router import RouteReset
    
    
    class _RouteMixin(object):
        def __init__(self, app: Sanic):
            self.app = app
            self.strict_slashes = False
            self.routes = []
            self.host = None
            self.ignored_routes = set()
            self.name = "RouteMixin"
            self.routes_names = {}
            self.routes_regex = {}
            self.compiled_routes = {}
            self._static = set()
            self._static_routes = set

# Generated at 2022-06-14 07:46:10.523102
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.app import Sanic
    app_test = Sanic('test_RouteMixin_add_route')
    app_test.config.REQUEST_MAX_SIZE = 100000000
    app_test.config.REQUEST_BUFFER_QUEUE_SIZE = 100
    app_test.config.RESPONSE_TIMEOUT = 60
    app_test.config.KEEP_ALIVE = True
    app_test.config.KEEP_ALIVE_TIMEOUT = 5
    app_test.config.REQUEST_TIMEOUT = 60

# Generated at 2022-06-14 07:46:17.062676
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # 1) Set up
    # 1.1) Setup mocked RouteMixin class
    RouteMixin_class = RouteMixin()
    RouteMixin.add_route = MagicMock()
    RouteMixin.add_route.return_value = None
    # 1.2) Set the initial values for the parameters
    uri = "/test"
    methods = ["GET"]
    host = "test.test.test"
    strict_slashes = True
    version = 1
    name = "test"
    apply = True
    websocket = True
    subprotocols = ["test"]
    # 2) Execute
    result = RouteMixin_class.route(uri, host, strict_slashes, methods, version, name, apply, websocket, subprotocols)
    # 3) Verify the results

# Generated at 2022-06-14 07:46:30.005966
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # We use two handlers, one is a coroutine and the other is an async def 
    def handler1(request):
        return text('OK1!')
    async def handler2(request):
        return text('OK2!')

    app = Sanic('test_RouteMixin_route')
    mixin = RouteMixin(app)

    # Call route for handler1 and handler2 respectively
    routes1, _ = mixin.route(uri='/test_route1', methods=['GET'])(handler1)
    routes2, _ = mixin.route(uri='/test_route2', methods=['GET'])(handler2)

    assert routes1[0].uri == '/test_route1' and routes2[0].uri == '/test_route2'


# Generated at 2022-06-14 07:46:36.560573
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # mock object Router
    router = Router()
    mixin = RouteMixin(router)
    # mock object Route
    handler = lambda: None
    route = Route(handler, "GET", "/", None, None)
    mixin.add_route(route)

    assert mixin._routes["GET"] == [route]


# Generated at 2022-06-14 07:46:40.085424
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    try:
        _route = RouteMixin().add_route(handler=None, uri=None)
    except Exception:
        assert True
    

# Generated at 2022-06-14 07:46:49.262661
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    view = mock.MagicMock()
    request = mock.MagicMock()
    request.args = {}
    request.headers = {}
    request.json = {}
    request.form = {}
    request.files = {}
    request.parsed_json = {}
    request.parsed_args = {}
    
    m_routes_routes = mock.MagicMock()
    m_routes_routes.append.return_value = None
    m_routes_routes.extend.return_value = None
    
    m_routes_routes.routes = [mock.MagicMock()]
    m_routes_routes.routes[0].uri = "/test"
    

# Generated at 2022-06-14 07:47:19.481534
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.response import json
    import pytest
    app = Sanic(__name__)
    """
    Test for the method add_route of class RouteMixin
    """
    # case 1: static without being decorated
    with pytest.raises(TypeError) as excinfo0:
        app.add_route(handler=None,uri=None)
    assert "the view function" in str(excinfo0.value)

    # case 2: static without being decorated
    @app.route('/test', methods=["GET", "POST"])
    async def handler(request):
        return json({'test': 'passes'})

# Generated at 2022-06-14 07:47:30.561390
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class RouteMixin1(object):
        """Test class RouteMixin"""

        @staticmethod
        def get_route_list():
            return []

    route_mixin1 = RouteMixin1()

    def func():
        pass

    def apply_route(route):
        return route

    def register_route(route):
        return route

    # Test
    routes = route_mixin1.route(apply_route, register_route, uri="test", host="test", methods=["GET","POST"], strict_slashes=True, version=1, name="test", apply=True, static=True)
    assert type(routes) == tuple


# Generated at 2022-06-14 07:47:38.676739
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic("test_app_name")
    # test for no param
    uri = "test_uri"
    method = "test_method"
    route_test = Route("test_uri", "test_method")
    assert route_test == Route("test_uri", "test_method")
    app.router.add_route("test_method", "test_uri", route_test)
    assert app.router.routes_all[method][uri].uri == route_test.uri
    assert app.router.routes_all[method][uri].method == route_test.method
    assert app.router.routes_all[method][uri].name == route_test.name
    # test for param host
    host = "test_host"

# Generated at 2022-06-14 07:47:47.680999
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    with pytest.raises(ValueError):
        RouteMixin().add_route(None, "a", None, None, None)
    with pytest.raises(ValueError):
        RouteMixin().add_route("a", None, None, None, None)
    with pytest.raises(ValueError):
        RouteMixin().add_route("a", "a", None, None, None)
    with pytest.raises(ValueError):
        RouteMixin().add_route("a", "a", "a", None, None)


# Generated at 2022-06-14 07:47:53.760949
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    aio_sanic_app = AioYMZSanicApp()
    result = aio_sanic_app.add_route(handler=test_generate_route_name, uri="/test_generate_route_name", methods=["GET", "POST"], host=None, port=None, strict_slashes=False, stream=False, version=None, name=None, body_timeout=None, websocket=False, apply=False)
    assert isinstance(result, _aiohttp.web.RouteDef)


# Generated at 2022-06-14 07:48:05.962560
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Create a new Router instance
    router = Router()
    # Create a new TestRouteHandler instance
    handler = TestRouteHandler()
    # Create a new TestRouteHandler instance
    raw_handler = TestRouteHandler()
    # Create a new TestRouteHandler instance
    websocket_handler = TestRouteHandler()
    # Create a new TestRouteHandler instance
    raw_websocket_handler = TestRouteHandler()
    # Create a new TestRouteHandler instance
    future_handler = TestRouteHandler()
    
    # Register route 
    route = router.add_route("/", TestRouteHandler.handle)
    assert route.uri == "/"
    assert route.version is None
    assert route.methods == ["GET"]
    assert route.host is None
    assert route.strict_slashes is None

# Generated at 2022-06-14 07:48:19.431358
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # arrange
    mixer = Mixer()
    uri = mixer.faker.pystr()
    handler = mixer.faker.pyfunc()
    methods = mixer.faker.pylist()
    strict_slashes = mixer.faker.pybool()
    version = mixer.faker.pyint()
    name = mixer.faker.pysrt()
    prefix = mixer.faker.pystr()
    host = mixer.faker.pystr()
    uri_prefix = mixer.faker.pystr()
    routes = mixer.faker.pylist()
    result = mixer.faker.pylist()
    rm = RouteMixin()
    rm.routes = routes

# Generated at 2022-06-14 07:48:23.365602
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Construct the object to be tested
    # app = Sanic()
    # route_mixin = RouteMixin(app)
    # route_mixin.add_route()
    assert True

# Generated at 2022-06-14 07:48:36.418798
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Create a sanic server and
    sanic_app = Sanic('test_sanic_server')
    # Test with use_reloader = True
    sanic_app.config.use_reloader = True
    # Test with log_config = None
    sanic_app.config.log_config = None
    # Test with error_logger = None
    sanic_app.error_logger = None
    # Test with configure_logging = False
    sanic_app.configure_logging = False
    # Create a instance of class RouteMixin
    route_mixin_ins = RouteMixin(sanic_app)
    # Test with result = None

# Generated at 2022-06-14 07:48:38.115534
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # TODO
    pass

# Generated at 2022-06-14 07:49:07.730069
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    import sys
    import os

    sys.path.append(os.path.dirname(sys.path[0]))

    from Route.RouteMixin import RouteMixin

    #test Object
    obj = RouteMixin()

    #test args and type
    def _handler(args):
        print(args)
        return int

    assert isinstance(obj.route(uri="test_uri",methods="test_methods",strict_slashes=True),tuple)
    assert isinstance(obj.route(uri="test_uri",methods="test_methods",strict_slashes=True)(_handler),tuple)


# Generated at 2022-06-14 07:49:16.997987
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    app = Sanic("test_RouteMixin_static")
    server_host = "127.0.0.1"
    server_port = "8080"
    routeMixin = RouteMixin()
    routeMixin.static(app, "/static", "../", pattern=r"/?.+", name="static_1", use_modified_since=True, strict_slashes=True, host=server_host, use_content_range=False, stream_large_files=False, content_type=None, apply=True)

# Generated at 2022-06-14 07:49:29.192438
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test_RouteMixin_add_route')
    # 1. normal use case
    def handler(request, id): pass
    with app.create_task_group():
        assert app._add_route("GET", "/test/<id>", handler) == 0
        # 2. route not added to routes when task_group
    # 3. Confirm that app.router can be accessed by the function
    #    add_route.  This is required for mocking.
    _router = RouteMixin._router # pylint: disable=protected-access
    RouteMixin._router = None # pylint: disable=protected-access
    with pytest.raises(Exception):
        app._add_route("GET", "/test/<id>", handler)
    RouteMixin._router = _router #

# Generated at 2022-06-14 07:49:32.873630
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Init object
    sanic = RouteMixin()

    assert sanic.add_route() != None, "Fail to execute method add_route"


# Generated at 2022-06-14 07:49:45.109008
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    my_route_mixin = RouteMixin()
    my_route_mixin = RouteMixin(
        router = None,
        add_route = mock_decorator,
        blueprints = [],
        host = '10.0.0.1',
        strict_slashes = None,
        version = 1,
        websocket = False)
    my_route_mixin.route(
        uri = '',
        methods = None,
        host = '10.0.0.1',
        strict_slashes = None,
        version = 1,
        name = '',
        apply = True,
        subprotocols = None,
        websocket = False,
        strict_methods = False)



# Generated at 2022-06-14 07:49:55.123793
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    arg_name = "arg_name"
    arg_methods = ["GET"]
    arg_host = "localhost"
    arg_uri = "/"
    arg_strict_slashes = False
    arg_version = 0
    arg_name = "arg_name"
    
    class TestClass():
        def __init__(self):
            self.__class__.name = "asdf"
            self.strict_slashes = False

        def add_route_wrapper(self,handler,*args,**kwargs):
            return self.add_route(handler,*args,**kwargs)

    test_obj = TestClass()


# Generated at 2022-06-14 07:50:04.779620
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    uri = "/"
    strict_slashes = None
    name = "static"
    def _app():
        pass
    _app.blueprint = None
    bp = Blueprint("test", url_prefix="/test")
    _app.blueprint = bp
    return RouteMixin().route(uri, methods=None, version=None,
                        strict_slashes=strict_slashes, name=name, apply=True, app=_app,
                        websocket=False, stream=False, enable_async=False,
                        content_type=None, host=None)