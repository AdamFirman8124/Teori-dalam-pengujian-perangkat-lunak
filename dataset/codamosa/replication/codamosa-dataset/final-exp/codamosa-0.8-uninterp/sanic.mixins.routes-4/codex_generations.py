

# Generated at 2022-06-14 07:40:40.975328
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    print('''
----------------------------------------------------
testing method static of class RouteMixin
in module src/sanic/router.py
''')
    router = RouteMixin()
    uri = "/static"
    file_or_directory = "static"
    pattern=r"/?.+"
    use_modified_since=True
    use_content_range=False
    stream_large_files=False
    name="static"
    host=None
    strict_slashes=None
    content_type=None
    apply=True
    router.static(uri, file_or_directory, pattern, use_modified_since,
        use_content_range, stream_large_files, name, host, strict_slashes,
        content_type, apply)
    # assert router._static_request_handler == None

# Generated at 2022-06-14 07:40:53.380765
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from .utils import FakeServer
    from .websocket import WebSocketProtocol

    app = WebSocketProtocol()

    # call method route of class RouteMixin
    # check return type
    assert isinstance(RouteMixin.route, functools.partial)
    assert RouteMixin.route.args == (RouteMixin, )
    assert RouteMixin.route.keywords == {
        'methods': None,
        'version': None,
        'strict_slashes': False,
        'host': None,
        'uri': None,
        'name': None,
        'apply': True,
    }

    @app.route('/')
    async def handler(request):
        return text('OK')

    server = FakeServer(app)
    response = server.request('GET', '/')
    assert response

# Generated at 2022-06-14 07:41:00.508731
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic("test_RouteMixin_add_route")
    r = RouteMixin()
    f = lambda x: x
    app.add_route(f, uri='/test/')
    assert app._routes[-1].name == "test_lambda"
    assert app._routes[-1].uri == "/test/"
    assert app._routes[-1].handler == f



# Generated at 2022-06-14 07:41:09.816033
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
  for route in [("/", None), ("/", ["GET", "HEAD"]), ("/<id>", None)]:
    try:
      RouteMixin.route(*route)
    except:
      assert False
    else:
      assert True

  try:
    RouteMixin.route("/<id>", "GET")
  except:
    assert True
  else:
    assert False

  try:
    RouteMixin.route("/", [])
  except:
    assert True
  else:
    assert False

test_RouteMixin_route()


# Generated at 2022-06-14 07:41:11.933137
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:41:20.778905
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.sanic import Sanic
    app = Sanic(__name__)
    
    def test(request):
        return text('OK')
    
    app.add_route(test, uri='/test/')
    
    assert len(app.router.routes_all) == 1
    
    assert app.router.routes_all[0].uri == '/test/'
    assert app.router.routes_all[0].handler == test
    

# Generated at 2022-06-14 07:41:30.567449
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class DummyRequest:
        def __init__(self, **kwargs):
            for (key, value) in kwargs.items():
                self.__dict__[key] = value
        def __getattr__(self, key):
            try:
                return self.__dict__[key]
            except:
                return None

    logger.debug("Generating dummy request.")
    req = DummyRequest(url = "https://www.api.com/user/1", method = "GET")
    logger.debug("Call add_route method of RouteMixin.")
    result = RouteMixin.add_route(req, None)
    assert result == None


# Generated at 2022-06-14 07:41:44.605637
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    
    # Create an instance of Sanic and test the add_route method of class Sanic
    request_handler = Sanic()
    
    # Test case 1: Test the case where arguments uri, handler, methods all are string
    routes = request_handler.add_route(uri="string", handler="string", methods="string")
    
    # Assert the returned value of method add_route
    assert isinstance(routes, Route)
    
    # Test case 2: Test the case where arguments uri, handler, methods all are string, but they are not valid

# Generated at 2022-06-14 07:41:46.491068
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:41:59.877108
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    app = Sanic()
    route_mixin = RouteMixin(app)
    uri = "/"
    file_or_directory = "/home/ubuntu/programming/sanic"
    pattern = r"/?.+"
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = "static"
    host = None
    strict_slashes = None
    content_type = None
    apply = True

# Generated at 2022-06-14 07:42:25.566544
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import Route
    from sanic.blueprints import Blueprint
    from sanic.response import text

    blueprint = Blueprint("test", "test")

    @blueprint.route("/", strict_slashes=False)
    def handler(request):
        return text("OK")

    @blueprint.route("/", strict_slashes=False)
    @blueprint.websocket("/ws")
    async def web_socket(request, ws):
        await ws.send("Hello!")
        await ws.recv()
        

    router = blueprint.as_router()
    assert len(router.routes_all) == 3

# Generated at 2022-06-14 07:42:32.314152
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # params
    uri = "uri"
    method = "method"
    handler = "handler"
    host = "host"
    strict_slashes = "strict_slashes"
    version = "version"
    name = "name"
    # execute
    mixin = RouteMixin()
    res = mixin.add_route(uri, 'method', 'handler', host, strict_slashes, version, name)
    # verify
    assert res is None

# Generated at 2022-06-14 07:42:34.111279
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:42:48.259752
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import Route
    from sanic import Sanic
    from sanic.response import HTTPResponse
    from sanic.views import HTTPMethodView
    app = Sanic(__name__)  # instance of class Sanic
    async def handler(_request):
        return HTTPResponse()
    async def handler1(_request):
        return HTTPResponse(status=201)
    # calls the method route
    map= app.route("/test", methods=["POST"])(handler)
    # asserts the method route
    assert len(app.router.routes_names["POST"]) == 1
    route=app.router.routes_names["POST"][0]
    assert(route.uri == "/test")
    assert(route.name == "test")
   

# Generated at 2022-06-14 07:42:51.263361
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route_mixin = RouteMixin()
    app = Sanic('sanic_test')
    route_mixin.add_route('/route/test', app)
    assert(app.routes[0].websocket is False)


# Generated at 2022-06-14 07:43:01.232896
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic import Sanic
    from sanic.router import Route
    
    app = Sanic('test_RouteMixin_route')
    
    @app.route('/', methods=['GET', 'POST'])
    def handler(request):
        return text('OK')
    
    assert isinstance(app.routes[0], Route)
    assert app.routes[0].handler == handler
    assert app.routes[0].uri == '/'
    assert app.routes[0].methods == ['GET', 'POST']

# Generated at 2022-06-14 07:43:11.403431
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.server import HttpProtocol
    from sanic.response import HTTPResponse
    from sanic.request import Request
    route = RouteMixin()
    handler = HTTPResponse('foobar')
    handler_mock = MagicMock(return_value=handler)

    @route.route('/test_route/', strict_slashes=False)
    def test_handler(request):
        return HTTPResponse('foobar')

    request_mock = Request({'type': 'http'}, 'POST', '/test_route',
                           version = '1.1')

    protocol_mock = HttpProtocol(route, request_mock)

    sanic_mock = MagicMock()

    sanic_mock.on_response = MagicMock()
    sanic_m

# Generated at 2022-06-14 07:43:25.445783
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    route_mixin = RouteMixin()
    route_mixin.strict_slashes = None
    route_mixin.name = ""
    route_mixin._future_statics = set()
    route_mixin._apply_static = lambda a: a
    route_mixin.route = lambda a,b,c,d,e,f,g,h,i,j,k,l: (a, b, c, d, e, f, g, h, i, j, k, l)
    route_mixin._generate_name = lambda a: "test"
    @route_mixin.route("test", "test", ["test"], False, 0, "test")
    def test():
        return 1
    @route_mixin.get("test")
    def test1():
        return 1

# Generated at 2022-06-14 07:43:35.125385
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Init the class RouteMixin
    route_mixin = RouteMixin()
    #define the params
    handler = "a"
    uri = "b"
    host = "c"
    methods = "d"
    strict_slashes = "e"
    version = "f"
    name = "g"
    # Test
    result = route_mixin.add_route(handler, uri, host, methods, strict_slashes, version, name)
    assert result


# Generated at 2022-06-14 07:43:47.016587
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.blueprints import Blueprint
    from sanic.router import Route
    from sanic.websocket import WebSocketProtocol

    obj = RouteMixin()

    # Case 1:
    # The class RouteMixin has an attribute routes, it is a Router object.
    # test the method add_route of this attribute.
    # expected = []
    # actual = obj.routes.routes
    # assert actual == expected

    # Case 2:
    # The class RouteMixin has an attribute websocket_routes.
    # test the method add_route of this attribute.
    # expected = []
    # actual = obj.websocket_routes
    # assert actual == expected

    # Case 3:
    # Case 3.1:
    # The class RouteMixin has an attribute blueprints.


# Generated at 2022-06-14 07:44:13.456134
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    # construct a mock class for RouteMixin
    route_mixin = RouteMixin()
    # construct a parameter for method static
    uri: str = 'http://localhost/'
    file_or_directory: Union[str, bytes, PurePath] = 'http://localhost/'
    pattern: str = r'/?.+'
    use_modified_since: bool = True
    use_content_range: bool = False
    stream_large_files: bool = False
    name: str = 'static'
    host: Optional[str] = None
    strict_slashes: Optional[bool] = None
    content_type: None = None
    apply: bool = True
    # call method static of class RouteMixin

# Generated at 2022-06-14 07:44:23.756339
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Create empty object of test class
    test_class = RouteMixin()

    # Create empty object of test class
    test_handler = RequestHandler()

    # Add a test route
    test_class.add_route(
        handler = test_handler,
        uri = '/',
        host = None,
        methods = ['GET', 'POST','DELETE','PUT'],
        strict_slashes = None,
        version = None,
        name = None,
    )

    # Assert that the test route has been added
    assert test_class.route._rules 


# Generated at 2022-06-14 07:44:35.020339
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():

    router = RouteMixin()
    def handler():
        return
    router.route(uri='/', methods=None, strict_slashes=None, version=None, name=None, apply=True, subprotocols=None, websocket=False)(handler)
    assert router.routes_names.get('static')

    router.route(uri='/', methods=None, strict_slashes=None, version=None, name=None, apply=True, subprotocols=None, websocket=False)(handler)
    assert router.routes_names.get('static')

    router.route(uri='/home/<name>/', methods=None, strict_slashes=None, version=None, name=None, apply=True, subprotocols=None, websocket=False)(handler)
    assert router.rout

# Generated at 2022-06-14 07:44:48.481662
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    ROUTE_MIXIN = RouteMixin()
    ROUTE_MIXIN.strict_slashes = True
    ROUTE_MIXIN.name = "TestSanic"
    ROUTE_MIXIN.router = Router()
    # ROUTE_MIXIN.url_prefix = None
    ROUTE_MIXIN.blueprint = None
    ROUTE_MIXIN.forbidden_ips = {}
    ROUTE_MIXIN._named_handlers = {}
    ROUTE_MIXIN._routes = []
    ROUTE_MIXIN._host_routes = {}

    @ROUTE_MIXIN.add_route("/test")
    async def test(request):
        return text("OK")

    assert type(test) == partial


# Generated at 2022-06-14 07:44:59.498197
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    """Unit test for method static of class RouteMixin"""

    # Create an instance of RouteMixin
    route_mixin = RouteMixin()
    # Test if method static of class RouteMixin could be called successfully.

# Generated at 2022-06-14 07:45:13.218352
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.response import json
    from sanic.views import HTTPMethodView

    async def async_handler(request):
        assert isinstance(request, Request)
        return json({"test": True})

    async def async_handler_arg(args):
        return json({"test": True})

    def handler(request):
        assert isinstance(request, Request)
        return json({"test": True})

    def handler_arg(args):
        return json({"test": True})

    bp = Blueprint("test_blueprint")

    async_handler = bp.add_route(async_handler, "/a", methods=["GET"])

# Generated at 2022-06-14 07:45:24.202652
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route, MatchInfo
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from inspect import isroutine
    app = Sanic('test_RouteMixin_add_route')
    # case 1:
    @app.route('/test_RouteMixin_add_route/case1')
    async def handler_case1(request):
        return HTTPResponse(text='OK', status=200)
    # case 2:
    handler_case2 = lambda request: HTTPResponse(text='OK', status=200)
    app.add_route(handler_case2, '/test_RouteMixin_add_route/case2')
    
    # case 3:

# Generated at 2022-06-14 07:45:27.307540
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    assert_raises(
        ValueError,
        RouteMixin().add_route,
        lambda x: x,
        "POST",
        "/"
    )


# Generated at 2022-06-14 07:45:36.011421
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.response import json

    app = Sanic('test_RouteMixin_add_route')

    @app.listener('before_server_start')
    def setup(app, loop):
        pass
    
    @app.listener('after_server_stop')
    def close(app, loop):
        pass

    def handler(request):
        return json({'test': 'OK'})
    
    routes = app.add_route(handler, 'test/route')

    assert isinstance(routes, list)
    assert len(routes) == 1
    assert routes[0].rule == '/test/route'


# Generated at 2022-06-14 07:45:44.266505
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    with pytest.raises(TypeError):
        RouteMixin.add_route(
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
        )



# Generated at 2022-06-14 07:47:04.824294
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route
    a = RouteMixin()

    for i in range(6):
        if i == 0:
            uri = "/"
            handler = "ok"
            name = None
            host = ""
            strict_slashes = False
            version = ()
            methods = "GET"
            expect_route = Route(
                uri=uri,
                handler=handler,
                name=name,
                strict_slashes=strict_slashes,
                version=version,
                host=host,
                methods=methods,
            )
        elif i == 1:
            uri = "/1"
            handler = "ok"
            name = "aaa"
            host = "aaa"
            strict_slashes = False
            version = (1, 1)

# Generated at 2022-06-14 07:47:10.675920
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    @RouteMixin.add_route(uri='/api',methods=['GET','POST'],strict_slashes=True)
    def handler(request):
        pass
    assert(handler.route.uri=='/api')
    assert(handler.route.methods==['GET','POST'])
    assert(handler.route.strict_slashes==True)


# Generated at 2022-06-14 07:47:20.025251
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.server import serve
    app = Sanic("test_RouteMixin_add_route")

    async def handler(request):
        return text("OK")

    @app.websocket('/')
    async def feed(request, ws):
        while True:
            data = 'hello!'
            print('Sending: ' + data)
            await ws.send(data)
            data = await ws.recv()
            print('Received: ' + data)

    app.add_route(handler, '/')
    _, test_server = serve(app, port=7000)

    try:
        req = requests.get('http://127.0.0.1:7000/', )
        assert req.text == "OK"
    finally:
        test_server.close()

# Unit

# Generated at 2022-06-14 07:47:29.759356
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import sanic
    app = sanic.Sanic()
    from sanic.response import json

    async def handler(request, *args, **kwargs):
        return json({"message": "hello"})

    app.add_route(handler=handler, uri='/', methods=['GET'])

    assert handler == app.router.routes_all[0].handler
    assert '/' == app.router.routes_all[0].uri
    assert {'GET'} == app.router.routes_all[0].methods


# Generated at 2022-06-14 07:47:34.725738
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
  "RouteMixin_add_route's unti test"
  # Initializing RouteMixin
  _RouteMixin = RouteMixin()
  # Testing add_route
  _RouteMixin.add_route('GET', '/', 'test_func')
  print('test_RouteMixin_add_route success')


# Generated at 2022-06-14 07:47:36.103823
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    pass


# Generated at 2022-06-14 07:47:48.540093
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic('test_RouteMixin_route')
    class RouteMixinFake(RouteMixin):
        def __init__(self):
            self.route_list = []
            self.strict_slashes = None

# Generated at 2022-06-14 07:47:56.082970
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.router import Route

    mix = RouteMixin()
    mix.add_route(handler="test_handler", uri='/test_uri')
    
    assert mix.routes[0].uri == '/test_uri'
    assert mix.routes[0].handler == 'test_handler'
    assert mix.routes[0].__class__ == Route

# Generated at 2022-06-14 07:48:08.607109
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import unittest

    @unittest.mock.patch.object(Sanic, 'route')
    def test_helper(self, mock_route):

        # Test that the decorator is empty
        def test_handler():
            pass

        @route('/test_handler')
        def test_handler_decorator():
            pass

        # Assert that the helper functions are equivalent
        self.assertEqual(
            self.route('/test_handler')(test_handler),
            route('/test_handler')(test_handler)
        )

        # Assert that the helper functions are equivalent
        self.assertEqual(
            self.route('/test_handler')(test_handler),
            self.add_route(test_handler, '/test_handler')
        )

        # Assert that the helper functions

# Generated at 2022-06-14 07:48:22.440839
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():

    class TestRouteMixin(RouteMixin):

        def __init__(self):
            pass

    class TestHTTPMethodView(HTTPMethodView):

        def get(self, request, *args, **kwargs):
            pass

        def post(self, request, *args, **kwargs):
            pass

    # Test for default case
    trm = TestRouteMixin()
    trm.add_route(uri=URI, handler=HANDLER, methods=METHODS, **ADD_ROUTE_KWARGS)
    assert True

    # Test for case 1
    trm = TestRouteMixin()
    trm.add_route(uri=URI, handler=HANDLER, methods=METHODS, **ADD_ROUTE_KWARGS)

# Generated at 2022-06-14 07:48:55.560798
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    """Unit test for method add_route of class RouteMixin."""
    pass

# Generated at 2022-06-14 07:49:03.057331
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic('test_RouteMixin_route')
    route = app.route('/test')(lambda x: x)
    url = app.url_for('test_RouteMixin_route.test_RouteMixin_route')
    assert url == '/test'

@app.route('/')
async def index(request):
    return json({"hello": "world"})

@app.route('/url/<name:[A-z]+>')
async def handler(request, name):
    return text('Hello {}!'.format(name))

@app.route('/query')
async def query(request):
    limit = request.args.get('limit', 10)
    return json({'limit': limit})


# Generated at 2022-06-14 07:49:11.367449
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    def handler():
        pass
    test_route = RouteMixin()
    assert test_route.route("/user", methods=["GET", "POST"])(handler) == (
        [
            Route(
                uri="/user",
                methods={"GET", "POST"},
                strict_slashes=None,
                host=None,
                version=None,
                name=None,
                handler=handler,
                websocket=False,
            )
        ],
        handler,
    )


# Generated at 2022-06-14 07:49:15.649290
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class testRouteMixin(RouteMixin):
        def __init__(self):
            self._app =None
            self._strict_slashes = None
    routeMixin = testRouteMixin()
    assert routeMixin._app == None
    assert routeMixin._strict_slashes == None


# Generated at 2022-06-14 07:49:28.660604
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.router import Route, RouteExists
    from sanic.response import json
    from sanic.log import log
    route_mixin = RouteMixin()
    route_mixin.blueprint = {'_name': 'test_bp'}
    def handler(*args, **kwargs):
        pass
    result = route_mixin.add_route(url = 'url', methods = ['post', 'get'], handler = handler, name = 'name', host = 'host', strict_slashes = False, version = None, stream = False, status_codes = None)
    assert route_mixin.blueprint == {'_name': 'test_bp'}
    #assert isinstance(result, list)
    #assert len(result) == 2
    #assert isinstance(result[

# Generated at 2022-06-14 07:49:36.341042
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Test that the function route returns a tuple of the form (route, func)
    from sanic.router import Route
    from sanic.request import Request

    router = RouteMixin()
    func = lambda request: (1, 2, 3)
    route, func = router.route('/')(func)
    assert func == func
    assert isinstance(route, Route)
    assert route.uri == '/'
    assert route.handler is func
    assert route.host == None or route.host == '*'
    assert route.methods == ['GET', 'HEAD']
    assert route.strict_slashes == None or route.strict_slashes == True
    assert route.version == None
    assert route.name == 'test_' + func.__name__
    assert route.static == False


# Generated at 2022-06-14 07:49:48.534127
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test case 1
    app = Sanic('test')
    app.add_route(lambda x: x, '/test1')

    # Test case 2
    app = Sanic('test')
    app.add_route(lambda x: x, '/test2', methods=['GET'])

    # Test case 3
    app = Sanic('test')
    app.add_route(lambda x: x, '/test3', methods=['POST'])

    # Test case 4
    app = Sanic('test')
    app.add_route(lambda x: x, '/test4', methods=['PUT'])

    # Test case 5
    app = Sanic('test')
    app.add_route(lambda x: x, '/test5', methods=['PATCH'])

    # Test case 6
    app = Sanic('test')

# Generated at 2022-06-14 07:49:49.198762
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass

# Generated at 2022-06-14 07:49:52.255414
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class TestClass(RouteMixin):
        pass
    test_class = TestClass()
    result = test_class.add_route('/', 'test_handler')
    assert result == None


# Generated at 2022-06-14 07:49:59.558656
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class _test_RouteMixin(RouteMixin):
        def __init__(self):
            self.host = "host"
            self.name = "name"
            self.router = Router()
            self.router._registered_rules = OrderedSet()
            self.router._registered_handlers = OrderedDict()
            self.router._registered_blueprints = OrderedSet()
            self.url_for = UrlFor(self.router)
    # 1
    this = _test_RouteMixin()
    result = this.add_route('/1a/', 'handler_a', rename_websocket='rename_websocket', methods=['GET'], name='name', version=2)
    assert result[0]['uri'] == '/1a/'