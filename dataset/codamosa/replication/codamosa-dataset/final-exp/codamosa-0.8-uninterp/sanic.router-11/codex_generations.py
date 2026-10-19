

# Generated at 2022-06-14 07:55:25.812266
# Unit test for constructor of class Router
def test_Router():
    '''
    Test for constructor of class Router
    '''
    test_router = Router()
    assert(test_router)


# Generated at 2022-06-14 07:55:30.404463
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.ctx.router == router
    assert router.ctx.router.ctx == router.ctx


# Generated at 2022-06-14 07:55:42.221348
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic

    with pytest.raises(SanicException):
        app = Sanic(__name__)
        router = Router()
        router.add('/<__file_uri__:path>', ['GET'], None, static=True)
        router.finalize(app)
        assert (router.ctx.get_route('GET', '/<__file_uri__:path>') is not None)
        router.add('/<__file_uri__:path>/<__file_uri__:path>',
                   ['GET'], None, static=True)
        router.finalize(app)
        assert (router.ctx.get_route('GET',
                                     '/<__file_uri__:path>/<__file_uri__:path>')
                is not None)


# Generated at 2022-06-14 07:55:43.474511
# Unit test for constructor of class Router
def test_Router():
    assert Router()


# Generated at 2022-06-14 07:55:52.597070
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Route
    from sanic.server import Sanic
    app = Sanic(__name__)
    uri = "test"
    handler = lambda request: "test"
    host = None
    strict_slashes = True
    stream = False
    ignore_body = True
    version = "1"
    name = "route"
    unquote = True
    static = True
    methods = ["GET"]
    router = Router(app)

# Generated at 2022-06-14 07:55:58.621271
# Unit test for constructor of class Router
def test_Router():
    "A simple test to check the function of the class"
    router = Router()
    assert router.get_routes() == {}
    assert router.routes == {}
    assert router.routes_dynamic == {}
    assert router.routes_static == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 07:56:10.849413
# Unit test for constructor of class Router
def test_Router():
	router = Router()
	assert router == {}
	assert router.ctx == {}
	assert router.name_index == {}
	assert router.parse_cache == {}
	assert router.static_routes == {}
	assert router.dynamic_routes == {}
	assert router.regex_routes == []
	assert router.routes_all == {'static_routes': {}, 'dynamic_routes': {}, 'regex_routes': []}
	assert router.routes_static == {}
	assert router.routes_dynamic == {}
	assert router.routes_regex == []
	assert router.DEFAULT_METHOD == 'GET'

# Generated at 2022-06-14 07:56:12.772106
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.add("/login", ["GET"], 1)



# Generated at 2022-06-14 07:56:13.387428
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 07:56:19.603418
# Unit test for constructor of class Router
def test_Router():
    @bp.route("/")
    async def handler(request):
        return json({"foo": "bar"})
    router = Router()
    routes = router.add(bp=bp)
    assert routes is not None
    assert len(routes) == 1
    assert isinstance(router, Router)
    return router


# Generated at 2022-06-14 07:56:32.088302
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route("/", lambda x: x, [], strict_slashes=True)
    route.labels.append("__file_uri__")
    router.dynamic_routes["dynamic_route"] = route
    try:
        router.finalize()
    except SanicException:
        assert True
    route.labels.append("__hello__")
    try:
        router.finalize()
        assert False
    except SanicException:
        assert True


# Generated at 2022-06-14 07:56:34.574855
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        Router()
    except SanicException:
        assert True
    else:
        assert False


# Generated at 2022-06-14 07:56:42.998294
# Unit test for method finalize of class Router
def test_Router_finalize():
    route_handler_test: RouteHandler = lambda request: True
    uri_test: str = "/hello"
    methods_test: Iterable[str] = ["GET"]
    host_test: Optional[Union[str, Iterable[str]]] = None
    strict_slashes_test: bool = False
    stream_test: bool = False
    ignore_body_test: bool = False
    version_test: Union[str, float, int] = None
    name_test: Optional[str] = None
    unquote_test: bool = False
    static_test: bool = False
    router_test: Router = Router()

# Generated at 2022-06-14 07:56:45.253829
# Unit test for constructor of class Router
def test_Router():
    r = Router()


if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 07:56:58.048749
# Unit test for constructor of class Router
def test_Router():
    uri = '/'
    methods = ['GET', 'POST']
    handler = ''
    host = ['127.0.0.1']
    strict_slashes = False
    stream = False
    ignore_body = False
    version = ''
    name = 'test'
    unquote = False
    static = False
    router = Router()
    route = router.add(uri, methods, handler, host, strict_slashes, stream, ignore_body,
                    version, name, unquote, static)
    assert route.uri == "/"
    assert route.methods == ['GET', 'POST']
    assert route.ctx.ignore_body == False
    assert route.ctx.hosts == ['127.0.0.1']


# Generated at 2022-06-14 07:57:11.658338
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    routes = router.add(
        uri="/about",
        methods=["GET"],
        handler=None,
        host="",
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=False,
        static=False,
    )
    assert routes.path == "/about"
    assert routes.methods == ["GET"]
    assert routes.handler == None
    assert routes.requirements == {"host": ""}
    assert routes.strict == False
    assert routes.name == None
    assert routes.unquote == False
    assert routes.ctx == {"ignore_body": False, "stream": False, "hosts": [""], "static": False}

# Generated at 2022-06-14 07:57:14.174870
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router) == True

# Generated at 2022-06-14 07:57:17.980716
# Unit test for constructor of class Router
def test_Router():
    class Application(object):
        def handle_request(self, request, write_callback, stream_callback_):
            pass

    router = Router(Application())
    assert isinstance(router, Router)



# Generated at 2022-06-14 07:57:23.734057
# Unit test for method finalize of class Router
def test_Router_finalize():
    uri = 'uri'
    route = Route('path', 'handler', 'methods', 'name', 'strict', 'unquote')
    route.labels = ['__file_uri']
    route.ctx = Mock()
    routes = {uri: route}

    with pytest.raises(SanicException):
        router = Router()
        router.dynamic_routes = routes
        router.finalize()

# Generated at 2022-06-14 07:57:26.272780
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 07:57:48.124645
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router

    router = Router()

    # Case 1: route labels are not allowed to start with '__'
    route = router._add(uri="/invalid", methods=["GET"], handler=None)
    route.labels.append("__invalid")
    with pytest.raises(SanicException):
        router.finalize()

    # Case 2: '__file_uri__' is allowed
    route = router._add(uri="/invalid", methods=["GET"], handler=None)
    route.labels.append("__file_uri__")
    assert router.finalize() is None

    # Case 3: route labels are allowed to start with '__' if not '__'
    route = router._add(uri="/invalid", methods=["GET"], handler=None)

# Generated at 2022-06-14 07:57:50.463265
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:57:55.397994
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add("/<__file_uri__>", None, None, strict_slashes=False,
          unquote=False, stream=False, ignore_body=False, version=None,
          name=None)
    r.finalize()

# Generated at 2022-06-14 07:58:04.457085
# Unit test for method finalize of class Router
def test_Router_finalize():
    def handler():
        pass
    
    def test_route(router):
        # test for method add
        route1 = router.add(
            uri='/test1',
            methods=['GET', 'POST'],
            handler=handler,
            host=None,
            strict_slashes=False,
            stream=False,
            ignore_body=False,
            version=None,
            name='test1',
            unquote=False,
            static=False,
        )

# Generated at 2022-06-14 07:58:16.650025
# Unit test for constructor of class Router
def test_Router():
    uri = [("/users/<name>", "GET", None),("/users/<name>", "POST", None)]
    methods = [("/users/<name>", "GET", None),("/users/<name>", "POST", None)]
    host = [("/users/<name>", None, None),("/users/<name>", None, "127.0.0.1")]
    strict_slashes = [("/users/<name>", "GET", None),("/users/<name>/", "GET", None)]
    stream = [("/users/<name>", "GET", None),("/users/<name>", "GET", None)]
    ignore_body = [("/users/<name>", "GET", None),("/users/<name>", "GET", None)]


# Generated at 2022-06-14 07:58:21.357557
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route(None, "/users/<id>", None, None, None)
    router = Router()
    router.dynamic_routes["users"] = route
    with pytest.raises(SanicException):
        router.finalize([])



# Generated at 2022-06-14 07:58:31.927278
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.add("/<__file_uri__:path>", [], None, static=True)
    except Exception as error:
        print("Test case 1 is failed, exception occured")
    else:
        print("Test case 1 is passed")

    try:
        router = Router()
        router.add("/<__any__:path>", [], None, static=True)
    except Exception:
        print("Test case 2 is passed")
    else:
        print("Test case 2 is failed, exception is not occured")

# Generated at 2022-06-14 07:58:32.834011
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 07:58:39.363236
# Unit test for method finalize of class Router
def test_Router_finalize():
    methods = ["GET", "POST"]
    def my_handler():
        pass
    router = Router()
    router.add("/test", methods, my_handler)
    with pytest.raises(SanicException):
        router.finalize()
    router.static_routes[0].labels.append("__file_uri__")
    router.finalize()

# Generated at 2022-06-14 07:58:43.863980
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    

# Generated at 2022-06-14 07:58:55.925668
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.default_method == "GET"
    assert router.allowed_methods == HTTP_METHODS


# Generated at 2022-06-14 07:58:59.840956
# Unit test for constructor of class Router
def test_Router():
    # Test the constructor
    # @TODO: update test
    # router1 = Router()
    # assert router1 is not None
    return

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 07:59:07.699422
# Unit test for constructor of class Router
def test_Router():
    router = Router(app=None)
    assert router

    router.ctx = None
    router.DEFAULT_METHOD = None
    router.ALLOWED_METHODS = None
    router.routes = None
    router._routes = None
    router.builder = None
    router.cache_size = None
    router.get = None
    router.add = None
    router.add_route = None
    router.name_index = None


# Generated at 2022-06-14 07:59:11.519772
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 07:59:12.558661
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 07:59:18.346296
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_dynamic is not None
    assert router.routes_static is not None
    assert router.routes_regex is not None
    assert router.routes_all is not None
    assert router.ctx is not None


# Generated at 2022-06-14 07:59:21.277894
# Unit test for constructor of class Router
def test_Router():
    # Create an instance of Router for testing
    object = Router()

    # Create an instance of Route for testing
    object = Route()

# Generated at 2022-06-14 07:59:32.598363
# Unit test for method add of class Router
def test_Router_add():

    import pytest

    def test_handler():
        pass

    router = Router()
    router.add("/123/", ["GET"], test_handler, static=True)
    assert router.routes_all
    assert "GET:/123/" in router.routes_all
    assert "GET:/123/" in router.routes_static
    assert "GET:/123/" not in router.routes_dynamic
    assert "GET:/123/" not in router.routes_regex

    router.add("/<cat>/", ["GET"], test_handler, static=False)
    assert "GET:/<cat>/" in router.routes_all
    assert "GET:/<cat>/" in router.routes_dynamic
    assert "GET:/<cat>/" not in router.routes_static


# Generated at 2022-06-14 07:59:33.950494
# Unit test for constructor of class Router
def test_Router():
    assert Router(host='host')

# Generated at 2022-06-14 07:59:36.135181
# Unit test for constructor of class Router
def test_Router():
    result = Router(None)
    assert isinstance(result, Router)

# Generated at 2022-06-14 07:59:56.863815
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert router.routes_all == {}
    assert router.routes_dynamic == {}
    assert router.routes_static == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 08:00:07.824983
# Unit test for method add of class Router
def test_Router_add():
    from Routes import Router
    from sanic.constants import HTTP_METHODS
    from unittest import TestCase, main

    class Test_Router_add(TestCase):
        def test_partial_methods_is_set_with_only_valid_http_methods(self):
            """
            Test that parameter methods of method add of class Router is set with
            only valid HTTP methods.
            """
            for method in HTTP_METHODS:
                router = Router()

                assert(len(router.routes_dynamic) == 0)
                assert(len(router.routes_static) == 0)
                assert(len(router.routes_regex) == 0)
                assert(len(router.routes_all) == 0)


# Generated at 2022-06-14 08:00:10.532406
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 08:00:22.383117
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    # Test with certain 'uri'.
    def my_handler(request, *args, **kwargs):
        pass
    router.add('/', ['GET'], my_handler)
    assert router.routes_dynamic['/'] != None and router.routes_static['/'] != None and router.routes_regex['/'] != None

    # Test with certain 'uri'.
    def my_handler2(request, *args, **kwargs):
        pass
    router.add('/test', ['GET'], my_handler2)
    assert router.routes_dynamic['/test'] != None and router.routes_static['/test'] != None and router.routes_regex['/test'] != None

    # Test with 'uri'=None. 
   

# Generated at 2022-06-14 08:00:30.409508
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.ctx == None
    assert router.name_index == {}
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 08:00:31.092930
# Unit test for constructor of class Router
def test_Router():
    r = Router()

# Generated at 2022-06-14 08:00:33.972031
# Unit test for constructor of class Router
def test_Router():
    assert callable(Router)
    assert Router.__doc__ is not None

# Generated at 2022-06-14 08:00:37.329374
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:00:41.457946
# Unit test for constructor of class Router
def test_Router():
    def handler_get():
        pass

    def handler_post():
        pass

    router = Router()
    router.add(uri="/test_router", methods=["GET","POST"], handler_post=handler_post, handler_get=handler_get)

# Generated at 2022-06-14 08:00:43.865073
# Unit test for constructor of class Router
def test_Router():
    router = Router(app=None)
    assert(isinstance(router, Router))
    return router


# Generated at 2022-06-14 08:01:02.663837
# Unit test for constructor of class Router
def test_Router():
    class TestRouter(Router):
        pass

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 08:01:10.726729
# Unit test for constructor of class Router
def test_Router():
    base = Router("Router", None)
    assert base.ctx.app == None
    assert base.ctx.name == "Router"
    assert base.routes == {}
    assert base.dynamic_routes == {}
    assert base.static_routes == {}
    assert base.name_index == {}
    assert base.regex_routes == []
    assert base._regex_cache == {}
    assert base.route_order == []



# Generated at 2022-06-14 08:01:22.685700
# Unit test for method add of class Router
def test_Router_add():
    import pytest
    import anytest

    uri = "my_uri"
    methods = ["GET", "POST", "OPTIONS"]
    handler = (lambda t, r: r)
    host = ["www.example.com", "www.example.com"]
    strict_slashes = False
    stream = False
    ignore_body = False
    version = "v1"
    name = "my_name"

    route = Router()
    routes = route.add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name)
    assert route.name_index[name] == routes

    uri2 = "my_uri/<name>"
    route.add(uri2, methods, handler, host, strict_slashes, stream, ignore_body, version, name + '_2')

# Generated at 2022-06-14 08:01:26.015693
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.routes_all
    router.routes_static
    router.routes_dynamic
    router.routes_regex

    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 08:01:30.375745
# Unit test for constructor of class Router
def test_Router():
    # Dummy class object for demonstration purposes
    class DummyComponent:
        pass

    component = DummyComponent()

    router = Router(component)
    assert router.ctx is component

# Generated at 2022-06-14 08:01:35.862654
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert router.ctx.app == None
    assert router.ctx.router == router
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALOWED_METHODS == ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]


# Generated at 2022-06-14 08:01:38.039404
# Unit test for constructor of class Router
def test_Router():
    assert issubclass(Router, BaseRouter)
    # test create
    assert Router()


# Generated at 2022-06-14 08:01:40.790581
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
        print("Router constructor is a success")
    except Exception as e:
        print(e)



# Generated at 2022-06-14 08:01:48.096679
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router
    assert isinstance(router, BaseRouter) == True
    assert router.ALLOWED_METHODS == ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']
    assert router.DEFAULT_METHOD == 'GET'
    assert router.allowed_methods == ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS']
    assert router.default_method == 'GET'
    assert type(router) == Router


# Generated at 2022-06-14 08:02:01.106655
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == Router.DEFAULT_METHOD
    assert router.ALLOWED_METHODS == Router.ALLOWED_METHODS
    assert router.name_index == {}
    assert router.ctx.app == None
    assert router.ctx.router == router
    assert router.ctx.debug == None
    assert router.ctx.host == None
    assert router.ctx.port == None
    assert router.ctx.ssl == None
    assert router.ctx.request is None
    assert router.ctx.server == None
    assert router.ctx.protocol == None
    assert router.ctx.websocket == None
    assert router.ctx.websocket_protocol == None
    assert router.ctx.request_headers == None
    assert router.ctx.request_body == None

# Generated at 2022-06-14 08:02:35.054010
# Unit test for constructor of class Router
def test_Router():
    test_router = Router()
    assert(test_router != None)


# Generated at 2022-06-14 08:02:40.500832
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router
    assert isinstance(router, Router)
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router._get == router.get
    assert router.add

# Generated at 2022-06-14 08:02:45.861678
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []

# Generated at 2022-06-14 08:02:53.159560
# Unit test for constructor of class Router
def test_Router():
    """
    Testing the constructor of class Router
    """
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes_all == {}
    assert router.routes_regex == {}
    assert router.routes_dynamic == {}
    assert router.routes_static == {}
    assert router.name_index == {}
    assert router.ctx is None

# Generated at 2022-06-14 08:02:54.980295
# Unit test for constructor of class Router
def test_Router():
	router = Router()
	assert router


# Generated at 2022-06-14 08:02:59.651698
# Unit test for constructor of class Router
def test_Router():
  router = Router()
  assert router.routes_all == {}
  assert router.routes_static == []
  assert router.routes_dynamic == {}
  assert router.routes_regex == []

# Generated at 2022-06-14 08:03:02.801798
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:03:05.801320
# Unit test for constructor of class Router
def test_Router():
    print("Test for constructor of class Router")
    router = Router()
    assert isinstance(router, Router)
    print("Pass test for constructor of class Router")


# Generated at 2022-06-14 08:03:18.254189
# Unit test for constructor of class Router
def test_Router():

   # Case 1: Passing an empty list of routes
    router = Router([])

    assert router.routes == {}
    assert router.name_index == {}

   # Case 2: Passing a list of routes with one route
    router = Router(
        [Route(
            "GET",
            "/test",
            None,
            name="test",
            host="testhost.com",
            strict_slashes=True,
            unquote=True,
            stream=True,
            ignore_body=True,
            version=1.0
        )]
    )

    routes = router.routes
    assert len(routes) == 1
    for route in routes.values():
        assert route.ctx.ignore_body
        assert route.ctx.stream
        assert route.ctx.version == "1"

# Generated at 2022-06-14 08:03:26.136526
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.routes == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.name_index == {}
    assert router.regex_routes == {}
    assert router.ctx == {}



# Generated at 2022-06-14 08:04:39.415118
# Unit test for constructor of class Router
def test_Router():
    test_router = Router(None)
    assert test_router.ctx == None
    assert test_router.static_routes == {}
    assert test_router.dynamic_routes == {}
    assert test_router.regex_routes == {}
    assert test_router.name_index == {}
    assert test_router.finalized == False
    assert test_router.prefix == ""
    assert test_router.custom_converters == {}
    assert test_router.trie == {}


# Generated at 2022-06-14 08:04:40.653092
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)

# Generated at 2022-06-14 08:04:54.022588
# Unit test for constructor of class Router
def test_Router():
    # Constructor with no argument
    router = Router()
    router._get("http://127.0.0.1/", "GET", None)
    test_route, test_handler, test_params = router.get("http://127.0.0.1/", "GET", None)
    assert isinstance(test_route, Route)
    assert isinstance(test_handler, RouteHandler)
    assert isinstance(test_params, Dict[str, Any])
    assert router.get("http://127.0.0.1/", "GET") == router.get("http://127.0.0.1/", "GET")

# Generated at 2022-06-14 08:05:04.198370
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    r.add(uri='/', methods=['GET'], handler=None)
    # test the router_cache
    r.get('/', 'GET', '')
    r.add(uri='/python', methods=['GET'], handler=None)
    r.add(uri='/python', methods=['GET'], handler=None, static=True)
    r.add(uri='/python', methods=['GET'], handler=None)
    r.add(uri='/java', methods=['GET'], handler=None)
    r.add(uri='/python', methods=['GET'], handler=None, static=True)
    r.add(uri='/python', methods=['GET'], handler=None)

# Generated at 2022-06-14 08:05:05.921927
# Unit test for constructor of class Router
def test_Router():
    test=Router()
    assert test!=None

# Generated at 2022-06-14 08:05:07.488983
# Unit test for constructor of class Router
def test_Router():
    assert True == True

# Generated at 2022-06-14 08:05:14.841308
# Unit test for method add of class Router
def test_Router_add():
    router=Router()
    methods=["GET", "POST", "OPTIONS"]
    def handler():
        return "Hello"
    host=None
    strict_slashes=False
    stream=False
    ignore_body=False
    version=None
    name=None
    unquote=False
    static=False
    route=router.add("/test/add", methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)

# Generated at 2022-06-14 08:05:22.597296
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r is not None
    assert r._routes_all == {} # pylint: disable=W0212
    assert r._routes_static == {} # pylint: disable=W0212
    assert r._routes_dynamic == {} # pylint: disable=W0212
    assert r._routes_regex == {} # pylint: disable=W0212
    assert r.name_index == {}
    assert r._inject_ctx # pylint: disable=W0212
    assert r.DEFAULT_METHOD == 'GET'
    assert r.ALLOWED_METHODS == ('OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE')
    assert r._ROUTER_CACHE_SIZE == 1024
