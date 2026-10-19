

# Generated at 2022-06-14 07:40:34.143533
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    import types
    import inspect

    @types.coroutine
    def mock_routes(*args, **kwargs):
        return [1, 2, 3]

    '''class mock_routes:
        def __call__(self, *args, **kwargs):
            return [1, 2, 3]'''

    @types.coroutine
    def mock_run_middleware():
        return True


    class RouteMixin:
        def __init__(self, *args, **kwargs):
            self.route = mock_route
            self.run_middleware = mock_run_middleware

    class Request:
        def __init__(self, *args, **kwargs):
            pass
    class Sanic:
        def __init__(self, *args, **kwargs):
            pass

    #

# Generated at 2022-06-14 07:40:46.950488
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    class B(RouteMixin):
        def __init__(self):
            super(RouteMixin, self).__init__()
            print ("B init")
    b = B()
    @b.route("/test")
    async def test():
        return "it works"
    assert(b.get_routes()[0].uri=="/test")
    assert(b.get_routes()[0].handler.__name__=="test")
    assert(b.get_routes()[0].methods=="GET")
    assert(b.get_routes()[0].host==None)
    assert(b.get_routes()[0].strict_slashes==None)


# Generated at 2022-06-14 07:40:58.074116
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.app import Sanic
    import sanic.route
    app = Sanic('test')
    uri = '/test'
    host = None
    methods = None
    strict_slashes = None
    version = None
    name = None
    # the expected result is a function of mixins
    expected = RouteMixin.route
    # the actual result is the function object of object app
    actual = app.route
    # assert the actual result with expected result
    assert expected == actual
    # the expected result is a route object with name 'test'
    expected = sanic.route.Route(uri, methods, host, None, version, name)
    # the actual result is a route object with name 'test'

# Generated at 2022-06-14 07:41:09.461387
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    # object initialization
    obj = RouteMixin()
    uri = "/test"
    file_or_directory = "/test"
    pattern = r"/?.+"
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = "static"
    host = "127.0.0.1"
    strict_slashes = False
    content_type = "text/plain"
    obj.strict_slashes = strict_slashes
    obj.static(uri, file_or_directory, pattern, use_modified_since, use_content_range, stream_large_files, name, host, strict_slashes, content_type)


# Generated at 2022-06-14 07:41:17.119800
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic("test_RouteMixin_add_route")
    request, response = Mock(), Mock()
    @app.route("/")
    async def handler(request):
        return response
    assert app.router.routes_names["handler"] == "/"
    assert app.router.routes[0].handler == handler


# Generated at 2022-06-14 07:41:19.039960
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # TODO: implement the test
    pass


# Generated at 2022-06-14 07:41:28.616584
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    mm = RouteMixin()

    # set up
    uri = '/test'
    file_or_directory = '/path/to/file'
    pattern = r'/?.+'
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = 'static'
    host = '127.0.0.1'
    strict_slashes = True
    content_type = 'image/jpeg'
    apply = True


    # call method

# Generated at 2022-06-14 07:41:34.829016
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    @websocket('/')
    def handler(request):
        pass

    mixin = RouterMixin()
    route = mixin.route('/')(handler)
    assert(route.uri == '/') 
    assert(len(mixin.routes) == 1)



# Generated at 2022-06-14 07:41:38.304988
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    route_mixin = RouteMixin()
    decorator = route_mixin.route
    
    assert decorator is not None
    
    

# Generated at 2022-06-14 07:41:49.381895
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic()
    rm = RouteMixin()

    @rm.route('/')
    def test(request):
        return None

    assert rm.routes == []

    @rm.route('/')
    def test1(request):
        return None

    assert len(rm.routes) == 1

    rm.routes = []
    assert rm.routes == []

    @rm.route('/', methods=["GET", "POST"])
    def test2(request):
        return None

    assert len(rm.routes) == 1
    app.add_route(rm.routes[0].handler, rm.routes[0].uri, rm.routes[0].methods)
    request, response = app.test_client.post('/')
    assert response

# Generated at 2022-06-14 07:42:12.097647
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    router = Router()
    def handler1(request):
        return "handler1"
    def handler2(request):
        return "handler2"

    # Test for correct len of self._routes
    router.add_route("GET", "/", handler1)
    router.add_route("GET", "/", handler1)

    assert len(router._routes) == 2

    # Test for correct value of self._routes
    router.add_route("GET", "/", handler2)
    router.add_route("GET", "/", handler2)

    assert router._routes["/GET/"] == [
        ("handler1", {}, False),
        ("handler1", {}, False),
        ("handler2", {}, False),
        ("handler2", {}, False),
    ]

    # Test for correct

# Generated at 2022-06-14 07:42:23.961968
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    print("===> test_RouteMixin_add_route")
    Q=Queue()
    F=Future()
    async def _handler(request,**kwargs):
        return request
    x= RouteMixin(Q,F,"RouteMixin")
    x.route("/")(_handler)
    routes, handler = x.route("/")(_handler)
    print(routes)
    print(handler)
    assert(routes != None)
    assert(handler != None)
    print("<=== test_RouteMixin_add_route")
    print("\n")
    print("\n")
    print("\n")

# Generated at 2022-06-14 07:42:33.731273
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    import sanic.app
    app = sanic.app.Sanic(__name__)
    args = [app]
    args[0].router = sanic.router.Router()
    args[0].router.add_route = _mock_coroutine
    args[0].routes = []
    args[0].exception_handler = {}
    kwargs = {
        "uri": "/",
        "handler": _mock_coroutine,
        "methods": None,
        "host": None,
        "strict_slashes": None,
        "version": None,
        "name": None,
        "stream": False
    }
    RouteMixin.add_route(*args, **kwargs)


# Generated at 2022-06-14 07:42:46.110114
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class MyRouteMixin(RouteMixin):
        def __init__(self):
            super().__init__()

            self.name = "MyRouteMixin"
            self.strict_slashes = True
            self._routes = []
            self._routes_all = {'GET': [], 'POST': [], 'PUT': [], 'DELETE': []}

            # Set the id of the route
            try:
                self._route_id = next(MyRouteMixin._route_id_generator)
            except AttributeError:
                # If it was the first time the decorator is used, initialize the
                # generator
                MyRouteMixin._route_id_generator = self._route_id_generator()

# Generated at 2022-06-14 07:42:59.865848
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    route_mixin = RouteMixin()
    uri = 'hello'
    handler = 'handler'
    host = "localhost"
    method = ["GET"]
    strict_slashes = False
    version = 1
    name = "hello"
    apply = True
    route, _ = route_mixin.add_route(uri, handler, host, method, strict_slashes, version, name, apply)
    assert (uri == route.uri)
    assert (host == route.host)
    assert (method == route.methods)
    assert (strict_slashes == route.strict_slashes)
    assert (version == route.version)
    assert (name == route.name)
    assert (apply == route.apply)
test_RouteMixin_add_route()

# Generated at 2022-06-14 07:43:11.930682
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    r = RouteMixin()
    path = 'examples/'
    pattern = r'/?.+'
    use_modified_since = True
    use_content_range = False
    stream_large_files = False
    name = 'static'
    host = None
    strict_slashes = None
    content_type = None
    apply = True
    r.static(path, pattern, use_modified_since, use_content_range, stream_large_files, name, host, strict_slashes, content_type, apply)
    assert r.router.routes_all == []
    assert r.router.routes_static == []
    assert r.router.static_routes == []
    assert r.router.routes_websocket == []
    assert r.router.r

# Generated at 2022-06-14 07:43:25.781083
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    m = RouteMixin("HostedApp")
    awaitable = m.garbage("/garbage")(dummy)
    assert not asyncio.iscoroutinefunction(awaitable)
    assert asyncio.iscoroutinefunction(m.dummy_handler.__wrapped__)
    assert asyncio.iscoroutinefunction(m.dummy.__wrapped__)
    assert asyncio.iscoroutinefunction(m.add_route("/uri", dummy).__wrapped__)
    assert asyncio.iscoroutinefunction(m.add_websocket_route("/uri", dummy).__wrapped__)
    assert asyncio.iscoroutinefunction(m.add_websocket_route("/uri", dummy).__wrapped__)

    assert 'dummy' == m.dummy.__name__

# Generated at 2022-06-14 07:43:37.946945
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    import asyncio
    from sanic import Sanic
    from sanic.response import text
    

    app = Sanic('test_RouteMixin_route')
    @app.route('/test_route', methods=['get'])
    async def handler1(request):
        return text('OK')
    
    request, response = app.test_client.get('/test_route')
    assert response.text == 'OK'
    request, response = app.test_client.post('/test_route')
    assert response.status == 405
    request, response = app.test_client.options('/test_route')
    assert response.status == 200


# Generated at 2022-06-14 07:43:44.513377
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    router = RouteMixin()
    Route = Route()
    Uri ='/test'
    Version = 1
    Strict_slashes = True
    Methods = ['GET']
    Name = 'test'
    Apply = True
    Host = None
    result = router.route(Uri=Uri,Methods=Methods,Strict_slashes=Strict_slashes,Version=Version,Name=Name,Apply=Apply,Host=Host)
    assert result == Route._decorate

# Generated at 2022-06-14 07:43:57.371219
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Check with adding one route
    result = RouteMixin().add_route("GET", "/path1", "fn1")
    expected = [Route("/path1", "fn1", "GET", None, None, None, None, None, None, None, False, False, False)]
    assert result == expected
    # Check with multiple routes
    result = RouteMixin().add_route("GET", "/path2", "fn2")
    result = result + RouteMixin().add_route("POST", "/path3", "fn3")
    result = result + RouteMixin().add_route("PUT", "/path4", "fn4")

# Generated at 2022-06-14 07:44:11.277730
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    
    from sanic.router import Route

    route = Route("/route", None, None, None, None, None)

    assert route == RouteMixin().add_route(route)

# Generated at 2022-06-14 07:44:25.040793
# Unit test for method add_route of class RouteMixin

# Generated at 2022-06-14 07:44:35.794521
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic.request import Request
    from sanic.router import Route
    from sanic.server import HttpProtocol
    from sanic.websocket import WebSocketProtocol
    from sanic.response import HTTPResponse

    app = App(__name__, route=None)
    class Test:
        async def index(self, request, a, b, c, **kwargs):
            assert 1 == a
            assert 2 == b
            assert 3 == c
            assert 'None' == str(request.args.get("q"))
            assert 'abc' == kwargs.get("test")
            return HTTPResponse("OK")

        @classmethod
        async def index_class(cls, request, a, b, c, **kwargs):
            assert 1 == a
            assert 2 == b
           

# Generated at 2022-06-14 07:44:39.410273
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
	"""
	Unit test for method route of class RouteMixin
	"""
	route = RouteMixin()
	route.route()
	# No exception thrown


# Generated at 2022-06-14 07:44:53.092777
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    # Test for correct behavior
    # Given a route_mixin 
    route_mixin = RouteMixin()
    # When uri is a valid uri
    uri = "/test"
    # And host is a valid host
    host = "testhost"
    # And strict_slashes is valid
    strict_slashes = True
    # And version is valid
    version = 1
    # And name is valid
    name = "test"
    # And apply is valid
    apply = True
    # And websocket is valid
    websocket = False
    # Then route should be applied correctly

# Generated at 2022-06-14 07:44:59.592572
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    app = Sanic()
    mixin = RouteMixin(app)
    mixin.route(uri='/test', methods=['GET'], version=1)(
        lambda request, *args, **kwargs: None)
    assert mixin.routes[0].uri == '/test'
    assert mixin.routes[0].methods == ['GET']



# Generated at 2022-06-14 07:45:06.097755
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    my_router = RouteMixin()
    route_add = my_router.route("/foo/bar") 
    route = route_add(my_handle_request)
    assert isinstance(route, Route)
    assert route._handler is my_handle_request

"""
Unit test for method add_websocket_route of class RouteMixin
"""

# Generated at 2022-06-14 07:45:19.231692
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
   test_router = RouteMixin()
   # Expectation is that below are the default values for parameters as well as to be returned
   # as output
   test_host = None
   test_uri = None
   test_strict_slashes = None
   test_methods = None
   test_version = None
   test_name = None
   output = test_router.add_route(test_uri, test_host, test_strict_slashes, test_methods, test_version, test_name)
   assert output[0] == test_router.route(test_uri, test_host, test_strict_slashes, test_methods, test_version, test_name)

# Generated at 2022-06-14 07:45:27.351401
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic('test')
    app.config.KEEP_ALIVE = False
    app.config.REQUEST_TIMEOUT = 10

    async def handler(request):
        return text('OK!')

    with app.listener('after_server_start'):
        app.add_route(handler, '/test')

    request, response = app.test_client.get('/test')

    assert response.text == 'OK!'



# Generated at 2022-06-14 07:45:36.817937
# Unit test for method route of class RouteMixin
def test_RouteMixin_route(): 
    @route('/', host='example.com')
    async def handler(request):
        pass
    @route('/', host='example.com')
    async def handler2(request):
        pass
    
    app = Sanic('test_RouteMixin_route')
    mixin = RouteMixin(app)
    
    mixin.route('/', host='example.com')
    mixin.route('/', host='example.com')
    assert len(mixin.routes) == 4
    assert handler != handler2
    assert len(mixin.routes[2].handler.__closure__) == 1
    assert handler == mixin.routes[2].handler.__closure__[0].cell_contents

# Generated at 2022-06-14 07:45:58.409228
# Unit test for method route of class RouteMixin

# Generated at 2022-06-14 07:46:02.712954
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # initialize router
    router = Router(name='my_router')
    router.add_route('/', '/', methods=['GET'])
    assert router.url_for('my_router.index') == '/'


# Generated at 2022-06-14 07:46:12.188078
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic("test_RouteMixin_add_route")
    with pytest.raises(TypeError):
        app.add_route("/", "something else")

    @app.route("/")
    def handler(request):
        return response.text("OK")

    with pytest.raises(TypeError):
        app.add_route("/", handler, methods=[])

    with pytest.raises(TypeError):
        app.add_route("/", handler, methods=("GET", 1))



# Generated at 2022-06-14 07:46:25.840102
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    route_mixin = RouteMixin()
    file_or_directory = '../'
    uri = '/'
    pattern = '/?.+'
    use_modified_since = 'True'
    use_content_range = 'False'
    stream_large_files = 'True'
    name = 'static'
    host = 'None'
    strict_slashes = 'None'
    content_type = 'None'
    # rtype and arg of method static
    response = route_mixin.static(
        uri,
        file_or_directory,
        pattern,
        use_modified_since,
        use_content_range,
        stream_large_files,
        name,
        host,
        strict_slashes,
        content_type,
    )
    # test_type of method static


# Generated at 2022-06-14 07:46:32.862692
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Init a Flask app
    app = Flask("testApp")
    # Stable input
    uri = "/route_Mixin/add_route"
    host = "0.0.0.0"
    version = 1
    name = "Test.name"
    # Testing function
    app.add_route(uri, host, version, name)

    return 0


# Generated at 2022-06-14 07:46:37.951240
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    # mock the static function
    @static(uri='/public/<path:path>',file_or_directory='/home/ubuntu')
    def _handler():
        return True
    # make sure that the mock works
    assert _handler() == True


# Generated at 2022-06-14 07:46:48.178092
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    import pytest
    from sanic import Sanic

    def test_function():
        return None

    def test_function1():
        return None

    def another_test_function(test_param):
        return None

    # Init and configure sanic app
    app = Sanic(__name__)
    app.config.from_object(Config())
    # Add route
    app.route(uri='/test/', methods=None, handler=test_function)
    # Add route with params
    app.route(uri='/{test_param}/', methods=None, handler=another_test_function)

    # Test function with param was added to routes list
    assert len(app.router.routes_all.get(method=None, uri='/{test_param}/')) == 1
    # Test function

# Generated at 2022-06-14 07:46:54.968095
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    def test_route(request, name):
        return text("test route")
    
    # Mock request and response
    @add_route(uri="/", host="", strict_slashes=None,
                     version=None, name="test_route")
    async def test_route(request, name):
        return text("test route")



# Generated at 2022-06-14 07:46:56.740390
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    test = 1
    assert test == 1


# Generated at 2022-06-14 07:46:59.332641
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    
    @RouteMixin.add_route('/')
    def handler(request):
        return text('OK')


# Generated at 2022-06-14 07:47:25.242716
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class MyRouteMixin(RouteMixin):
        def add_route(self, handler, uri, host=None):
            self.host = host

    myRouteMixin = MyRouteMixin()
    myRouteMixin.add_route(None, None, host='127.0.0.1')
    assert myRouteMixin.host == '127.0.0.1'


# Generated at 2022-06-14 07:47:31.315442
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    """
    add_route method of RouteMixin class returns a tuple of routes_numbers and decorated function
    """
    r=RouteMixin()
    @r.add_route('/index')
    async def index():
        pass
    assert 'index' in str(index.__name__)
    assert isinstance(index.__name__,str)
    


# Generated at 2022-06-14 07:47:32.434563
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    pass


# Generated at 2022-06-14 07:47:46.322856
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from sanic.router import RouteRegistry
    from sanic.router import Route

    mixin = RouteMixin()
    mixin.strict_slashes = False
    mixin.url_for = RouteRegistry().url_for
    mixin.name = 'name'
    mixin.id = 'id'

    uri = '/uri'
    host = 'host'
    methods = None
    strict_slashes = None
    version = None
    name = None
    apply = True
    websocket = False

    routes, _ = mixin.route(uri, host, methods, strict_slashes, version, name, apply, websocket)

    assert isinstance(routes, Tuple)
    assert isinstance(routes[0], Route)
    assert routes[0].uri == uri

# Generated at 2022-06-14 07:47:54.839712
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    from sanic import Sanic
    from sanic.response import json
    from sanic.router import Route
    from sanic.views import HTTPMethodView
    
    app = Sanic('test_RouteMixin_add_route')
    
    @app.route('/')
    async def handler(request):
        return json({'test': True})
    
    @app.route('/2')
    class Handler:
        async def get(self, request):
            return json({'test': True})
        async def post(self, request):
            return json({'test': True})
    
    class View(HTTPMethodView):
        async def get(self, request):
            return json({'test': True})
        async def post(self, request):
            return json({'test': True})

# Generated at 2022-06-14 07:48:06.575573
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    from unittest.mock import Mock
    import asyncio
    from sanic.router import Route
    from sanic.request import Request
    from sanic.response import HTTPResponse
    request = Request(
        "GET", "/hello/world",
        headers=None,
        version=None,
        transport=None,
        app="sanic:app",
        loop=asyncio.get_event_loop(),
        protocol=None,
        encoding=None,
        access_route=None)
    def get_handler(request):
        return HTTPResponse(body="Hello World")
    get_handler = Mock(return_value=HTTPResponse(body="Hello World"))
    
    response = get_handler(request)
    assert isinstance(response, HTTPResponse)

# Generated at 2022-06-14 07:48:19.960103
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # arrange
    from sanic.app import Sanic
    from sanic import response
    import re
    from unittest.mock import patch, MagicMock
    app = Sanic(__name__)
    uri_prefix = "test"
    uri = "test/route"
    methods = ["GET", "POST"]
    handler = response.text("I am a hunter, I have a gun")
    name = "test_name"
    host = "test"
    strict_slashes = "True"
    strict_slashes_default = "False"
    url_prefix = "test"
    version = 100
    apply = True
    parameters = []

    app.router.add_route = MagicMock(return_value="return_value_route")

# Generated at 2022-06-14 07:48:27.968497
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():

    class router:

        def __init__(self):
            pass

        def add(self,methods, uri, handler, host, strict_slashes):
            return 1, 2

    rm = RouteMixin()
    rm.router = router()

    route, handler = rm.route(uri='/',methods='GET', host=None, strict_slashes=False, version=None, name=None, apply=True)

    assert route == 1
    assert handler == 2


# Generated at 2022-06-14 07:48:30.571556
# Unit test for method route of class RouteMixin
def test_RouteMixin_route():
    route = RouteMixin().route('/test_route',methods=['GET','POST'])
    print(route.__name__)


# Generated at 2022-06-14 07:48:40.307891
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    # Test for method add_route
    # of class RouteMixin
    m_app = mock.Mock()
    route_obj = RouteMixin(m_app)
    handler1 = mock.Mock()
    handler2 = mock.Mock()
    uri = 'uri'
    m_app.add_route.return_value = [handler1,handler2]
    a,b = route_obj.add_route(handler1,uri)
    m_app.add_route.assert_called_with(handler1,uri,strict_slashes=None,host=None)
    assert a.handler == [handler1,handler2]
    assert b == [handler2,handler1]


# Generated at 2022-06-14 07:49:22.963201
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    app = Sanic("test_RouteMixin_add_route")

    @app.route("/")
    async def test(request):
        return text("OK")


# Generated at 2022-06-14 07:49:24.232240
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    pass


# Generated at 2022-06-14 07:49:34.394021
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class Router(RouteMixin):
        def __init__(self):
            self.routes = []
            self._static_routes = {}

    router = Router()
    assert router.routes == []
    assert not router._static_routes
    route, _ = router.route(
        uri="/ping", methods=["GET"], name="ping", host=None, strict_slashes=None, version=None, static=False
    )(lambda: "pong")

# Generated at 2022-06-14 07:49:47.372209
# Unit test for method add_route of class RouteMixin
def test_RouteMixin_add_route():
    class RouteMixinClass(RouteMixin):
        pass

    route_mixin = RouteMixinClass()
    route_mixin.name = "sanic"
    route_mixin.strict_slashes = False
    route_mixin.request_class = Request
    route_mixin.error_handler = None
    route_mixin.error_handler_spec = None
    route_mixin.middleware = None
    route_mixin.before_start = []
    route_mixin.before_stop = []
    route_mixin.after_start = []
    route_mixin.after_stop = []
    route_mixin.before_server_start = []
    route_mixin.before_server_stop = []
    route_mixin.after_server_start = []

# Generated at 2022-06-14 07:50:01.024371
# Unit test for method static of class RouteMixin
def test_RouteMixin_static():
    from pprint import pprint
    from pathlib import Path
    # path = str(Path('/Users/kalenpw/Downloads/') / 'app_static')
    path = Path('static')
    uri = '/static'
    # file_or_directory = Path()
    def test_handler(request, *args, **kwargs):
        pass

    app = Sanic('test')
    # TODO: is this a temporary method for test?
    def _generate_name(self, *objects):
        pass

    # TODO: is this a static method?