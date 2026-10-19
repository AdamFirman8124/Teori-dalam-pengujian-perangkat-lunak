

# Generated at 2022-06-14 07:55:55.847212
# Unit test for method add of class Router
def test_Router_add():
    from sanic.exceptions import InvalidUsage

    router = Router()
    def handler():
        pass

    with pytest.raises(InvalidUsage) as excinfo:
        router.add(uri="", methods=['GET'], handler=handler)
    assert 'The given path is not a valid one' in str(excinfo.value)

    with pytest.raises(InvalidUsage) as excinfo:
        router.add(uri="/", methods=[], handler=handler)
    assert 'The given methods are not valid' in str(excinfo.value)

    with pytest.raises(InvalidUsage) as excinfo:
        router.add(uri="/", methods=None, handler=handler)
    assert 'The given methods are not valid' in str(excinfo.value)


# Generated at 2022-06-14 07:55:56.918072
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert 1 == 1


# Generated at 2022-06-14 07:56:01.240722
# Unit test for method finalize of class Router

# Generated at 2022-06-14 07:56:03.220677
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Arrange
    assert True

    # Act
    # Assert

# Generated at 2022-06-14 07:56:12.670201
# Unit test for method finalize of class Router
def test_Router_finalize():
    class BadRouter(Router):
        def finalize(self, app, *args, **kwargs):
            super().finalize(*args, **kwargs)

            for route in self.dynamic_routes.values():
                if any(
                    label.startswith("__") and label not in ALLOWED_LABELS
                    for label in route.labels
                ):
                    raise SanicException(
                        f"Invalid route: {route}. Parameter names cannot use '__'."
                    )
        @lru_cache(maxsize=ROUTER_CACHE_SIZE)
        def get(self, path: str, method: str, host: Optional[str]) -> Tuple[Route, RouteHandler, Dict[str, Any]]:
            return self._get(path, method, host)


# Generated at 2022-06-14 07:56:15.096730
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    # Test init router success
    assert isinstance(router, Router)



# Generated at 2022-06-14 07:56:23.648537
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []
    assert router.static_routes == []
    assert router.dynamic_routes == {}
    assert router.regex_routes == []
    assert router.name_index == {}
    assert router.ctx.app == None


# Generated at 2022-06-14 07:56:35.368442
# Unit test for constructor of class Router
def test_Router():
    import unittest
    from unittest import mock
    from urllib.parse import quote
    from contextlib import contextmanager
    from sanic import Sanic
    from sanic.constants import HTTP_METHODS
    from sanic.server import Sanic
    # test init
    app = Sanic('test_Router')
    router = Router(Sanic)
    assert router.ctx == app
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}
    assert isinstance(router.default_route, Route)
    assert router.default_route.uri == "__default_route__"
    assert router.default_route.handler == None
    assert router.default_route.method

# Generated at 2022-06-14 07:56:39.431957
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    try:
        router.finalize()
    except Exception as err:
        assert False
    else:
        assert True

# Generated at 2022-06-14 07:56:50.953570
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router as ClassRouter
    from sanic.exceptions import SanicException

    from sanic.views import HTTPMethodView
    from sanic.response import text
    from sanic.exceptions import SanicException

    uri = '/'
    methods = 'GET'
    handler = text
    host = None
    strict_slashes = False
    stream = False
    ignore_body = False
    version = None
    name = None
    unquote = False
    static = False

    router = ClassRouter()
    router.add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)

    try:
        router.finalize()
    except SanicException:
        assert True

# Generated at 2022-06-14 07:57:05.957260
# Unit test for method finalize of class Router
def test_Router_finalize():
    m = Router()

    # case 1: all labels are allowed
    route_labels = ['__host__', '__port__', '__scheme__', '__file_uri__', '__method__']
    route = Route(None, None, route_labels, None, None)
    m.dynamic_routes = {0: route}
    m.finalize()

    # case 2: not all labels are allowed
    route_labels.append('__non_allowed__')
    route = Route(None, None, route_labels, None, None)
    m.dynamic_routes = {0: route}

# Generated at 2022-06-14 07:57:07.267624
# Unit test for constructor of class Router
def test_Router():
    assert callable(Router)

# Generated at 2022-06-14 07:57:10.758141
# Unit test for constructor of class Router
def test_Router():
    # Success
    with pytest.raises(TypeError) as info:
        router = Router()
    assert 'object() takes no parameters' in str(info)


# Generated at 2022-06-14 07:57:18.815442
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router

    router = Router()
    route = router.add('/test/<test>', methods=['GET', 'POST'])

    router.finalize()

    # success
    assert router.routes == {'/test/<test>': route}
    assert router.dynamic_routes == {'/test/<test>': route}
    assert router.static_routes == {}



# Generated at 2022-06-14 07:57:24.109415
# Unit test for constructor of class Router
def test_Router():
    route = Router()
    assert route.DEFAULT_METHOD == "GET"
    assert route.ALLOWED_METHODS == HTTP_METHODS
    assert route.MAX_PARAM_SEGMENTS == 4
    assert route.MAX_PATH_SIZE == 4096
    assert route.ROUTING_ERROR_HTTP_CODE == 400


if __name__ == "__main__":
    test = test_Router()

# Generated at 2022-06-14 07:57:26.936319
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    router = Router()
    with pytest.raises(SanicException) as e:
        router.finalize()
    assert "Invalid route: " in str(e)

# Generated at 2022-06-14 07:57:28.840062
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router


# Generated at 2022-06-14 07:57:32.463746
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ['OPTIONS', 'HEAD', 'GET', 'PUT', 'PATCH', 'POST', 'DELETE']

# Generated at 2022-06-14 07:57:45.485655
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Example: 
    #    router = Router()
    #    route = router.add('/test/route/<param>', ['GET'],None,static=False)
    #    route.ctx.labels = {'__file_uri__': '/test/route/<param>'}
    #    route.ctx.labels['__file_uri__'] = '/test/route/<param>'
    #    router.finalize() # call method
    #    assert router.dynamic_routes.values()[0].labels == {'__file_uri__': '/test/route/<param>'}
    #    assert router.dynamic_routes.values()[0].labels['__file_uri__'] == '/test/route/<param>'
    pass



# Generated at 2022-06-14 07:57:48.712942
# Unit test for constructor of class Router
def test_Router():
    r = Router(app=None)

    assert r.routes_all == []
    assert r.routes_static == []
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}


# Generated at 2022-06-14 07:57:58.066477
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    print(router)


# Generated at 2022-06-14 07:58:05.525599
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    from sanic.exceptions import NotFound, MethodNotSupported
    from functools import partial
    import types

    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

    def handler(request, *args, **kwargs):
        return request, args, kwargs, 1

    route = router.add("/1", methods={"GET"}, handler=handler)
    assert route.ctx.ignore_body == False
    assert route.ctx.stream == False
    assert route.ctx.hosts == [None]
    assert route.ctx.static == False

    with pytest.raises(NotFound):
        router._get("/2", "GET", "127.0.0.1")


# Generated at 2022-06-14 07:58:06.509640
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)



# Generated at 2022-06-14 07:58:07.204041
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 07:58:10.101087
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(RoutingNotFound):
        router.find_route_by_view_name('', name=None)

# Generated at 2022-06-14 07:58:22.205774
# Unit test for method finalize of class Router
def test_Router_finalize():
    class TestClass:
        def __init__(self, uri, methods, handler, host=None, strict_slashes=False, stream=False, ignore_body=False, version=None, name=None, unquote=False, static=False):
            self.uri = uri
            self.methods = methods
            self.handler = handler
            self.host = host
            self.strict_slashes = strict_slashes
            self.stream = stream
            self.ignore_body = ignore_body
            self.version = version
            self.name = name
            self.unquote = unquote
            self.static = static
            
            self.routes = {}
            self.static_routes = {}
            self.dynamic_routes = {}
            self.regex_routes = {}
           

# Generated at 2022-06-14 07:58:30.548626
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route(
        uri="/test",
        http_methods=["GET"],
        handler=None,
        parameter_types={
            '__file_uri__': int,
            'bar': str
        }
    )

    router = Router()
    router.dynamic_routes = {"GET": {'/test': route}}

    try:
        router.finalize()
        assert True
    except Exception:
        assert False

# Generated at 2022-06-14 07:58:37.726854
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add("/test/{{test}}", ["GET"], None)
    router.add("/test/{{test2}}", ["GET"], None)
    router.add("/test/{{__test3__}}", ["GET"], None)
    router.add("/test/{{__file_uri__}}", ["GET"], None)
    router.finalize()

# Generated at 2022-06-14 07:58:39.429331
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    assert router.finalize() == None


# Generated at 2022-06-14 07:58:40.577405
# Unit test for constructor of class Router
def test_Router():
    pass


# Generated at 2022-06-14 07:59:08.273619
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.request import Request
    from sanic import Sanic, Blueprint
    from sanic.response import text

    @Sanic.exception(SanicException)
    def on_exception(request, exception):
        return text("Error")
    
    app = Sanic()
    app.exception(SanicException)(on_exception)
    router = Router()
    router.exception(SanicException)(on_exception)
    router.add("/<__label1>", None, text("test"), {"host": "test"})
    router.add("/<__label2>/<label>", None, text("test"), {"host": "test"})
    router.finalize(app)
    request = Request("GET", "/user/name")
    response = router

# Generated at 2022-06-14 07:59:10.259724
# Unit test for constructor of class Router
def test_Router():
    test = Router()
    assert isinstance(test,BaseRouter)

# Generated at 2022-06-14 07:59:24.189287
# Unit test for method finalize of class Router
def test_Router_finalize():
    import unittest

    class Test(unittest.TestCase):
        def test_finalize_method_raise_exception(self):
            import re

            # Create a Router object and add a route to it
            router = Router()
            try:
                router.add("/route", methods=["GET"], handler=None)
            except Exception:
                self.fail("Exception occurred while adding a route")

            # Mock an object of class Route
            route_obj = object()
            # Set a property of type route_obj to property dynamic_routes of router
            router.dynamic_routes = {0: route_obj}

            # Add a label to the route_obj
            route_obj.labels = {"__label__"}

            # Check if finalize method raises exception

# Generated at 2022-06-14 07:59:31.934115
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.response import json
    from sanic.views import HTTPMethodView
    from sanic.app import Sanic

    test_app = Sanic("my-app")
    test_app.router.add(
        "/_test_view/<__foo>",
        "GET",
        HTTPMethodView.as_view("test_view", lambda r, __foo: json({"asd": __foo}))
    )

    try:
        test_app.router.finalize()
    except SanicException as e:
        assert e.args[0] == "Invalid route: /_test_view/<__foo>. Parameter names cannot use '__'."

# Generated at 2022-06-14 07:59:33.734271
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)


# Generated at 2022-06-14 07:59:35.360937
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router == router

# Generated at 2022-06-14 07:59:43.398643
# Unit test for method finalize of class Router
def test_Router_finalize():
    class FakeRouter:
        def __init__(self, dynamic_routes, labels, strict_slashes):
            self.dynamic_routes = dynamic_routes
            self.labels = labels
            self.strict_slashes = strict_slashes

    try:
        Router.finalize(FakeRouter("dynamic_routes", "labels", "strict_slashes"))
    except:
        raise AssertionError("The finalize method is not working properly.")


# Generated at 2022-06-14 07:59:57.325606
# Unit test for constructor of class Router
def test_Router():
    # type: () -> None
    assert Router.DEFAULT_METHOD
    assert Router.ALLOWED_METHODS

    r = Router()
    r.finalize()
    assert [i for i in r.routes] == []

    r = Router()
    r.add('/test',['GET'], lambda: None)
    r.finalize()
    assert [i for i in r.routes] == [('test',)]

    r = Router()
    r.add('/test',['GET'], lambda: None)
    r.add('/test/t',['GET'], lambda: None)
    r.finalize()
    assert [i for i in r.routes] == [('test',)]

    r = Router()
    r.add('/test',['GET'], lambda: None)


# Generated at 2022-06-14 08:00:02.139950
# Unit test for method finalize of class Router
def test_Router_finalize():
    my_router = Router()
    my_router.dynamic_routes = {
        "route1" : "route1",
        "route2" : "route2",
    }
    with pytest.raises(SanicException):
        my_router.finalize()

# Generated at 2022-06-14 08:00:06.186369
# Unit test for constructor of class Router
def test_Router():
    # Test Router constructor
    test_router = Router()
    assert isinstance(test_router, Router)


# Generated at 2022-06-14 08:00:38.578004
# Unit test for method finalize of class Router
def test_Router_finalize():
    original = Router()
    with pytest.raises(SanicException):
        original.finalize()
    

# Generated at 2022-06-14 08:00:45.845861
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.is_finalized == False

# Generated at 2022-06-14 08:00:47.481448
# Unit test for constructor of class Router
def test_Router():
    r=Router()
    assert(r is not None)

# Generated at 2022-06-14 08:00:52.453915
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.add("/", ["GET"], lambda x: None, name='test_name')
        router.finalize()
    except SanicException:
        assert True
    else:
        assert False
    



# Generated at 2022-06-14 08:00:56.353259
# Unit test for constructor of class Router
def test_Router():
    r=Router()
    assert(r.DEFAULT_METHOD=="GET")
    assert(r.ALLOWED_METHODS == HTTP_METHODS)


# Generated at 2022-06-14 08:01:01.048165
# Unit test for method finalize of class Router
def test_Router_finalize():
    my_router = Router()
    my_router.dynamic_routes = {1: 'test'}
    assert my_router.dynamic_routes == {1: 'test'}
test_Router_finalize()

# Generated at 2022-06-14 08:01:07.312012
# Unit test for method finalize of class Router
def test_Router_finalize():
    labels = ("__param1__", "__param2__", "__file_uri__")
    assert Router.finalize(None, labels)
    assert not any(label.startswith("__") and label not in ALLOWED_LABELS for label in labels)


# Generated at 2022-06-14 08:01:12.208858
# Unit test for method add of class Router
def test_Router_add():
    router = Router()
    router.add(
        uri= "/hello",
        methods=["GET", "POST", "OPTIONS"],
        handler=None,
        host=None,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=False,
        static=False
    )


# Generated at 2022-06-14 08:01:14.006144
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router


# Generated at 2022-06-14 08:01:19.983143
# Unit test for constructor of class Router
def test_Router():
    mlist = ['GET', 'POST', 'OPTIONS']
    r = Router(methods=mlist,
               handler='handler',
               host='host',
               strict_slashes=False,
               stream=False,
               ignore_body=False,
               version=None,
               name=None,
               unquote=False)

#Unit test for get of class Router

# Generated at 2022-06-14 08:01:51.788058
# Unit test for constructor of class Router
def test_Router():
    try:
        Router()
        assert True
    except:
        assert False



# Generated at 2022-06-14 08:01:55.321281
# Unit test for constructor of class Router
def test_Router():
    try:
        assert type(Router()) == Router
    except AssertionError:
        raise AssertionError("Router class constructor is not correct")


# Generated at 2022-06-14 08:02:00.349227
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    app = Sanic('sanic')
    app.config.from_pyfile('config.py')
    router = app.router
    try:
        router.finalize()
    except Exception as e:
        print(e)
        assert False


# Generated at 2022-06-14 08:02:14.006994
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route1 = Route("/folder/<param1>", method=["GET"], handler="route1")
    route2 = Route("/folder/<param1>", method=["GET"], handler="route2")
    
    router.dynamic_routes["1"] = route1
    router.dynamic_routes["2"] = route2
    
    with pytest.raises(SanicException, match=r"Invalid route: \{\'path\': \'/folder/\<param1\>\', \'handler\': \'route1\', \'methods\': \[\'GET\'\], \'name\': None, \'strict\': False, \'unquote\': False\}. Parameter names cannot use '__'."):
        router.finalize()

# Generated at 2022-06-14 08:02:17.842846
# Unit test for constructor of class Router
def test_Router():
    print("Testing constructor of class Router...")
    r = Router()
    assert isinstance(r, Router) and isinstance(r, BaseRouter)
    print("Constructor of class Router tested successfully!")


# Generated at 2022-06-14 08:02:20.229824
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), BaseRouter)

# Generated at 2022-06-14 08:02:21.461078
# Unit test for constructor of class Router
def test_Router():
    obj = Router()
    assert type(obj) == Router

# Generated at 2022-06-14 08:02:22.700416
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 08:02:24.800905
# Unit test for constructor of class Router
def test_Router():
    assert len(Router.ALLOWED_METHODS) > 1


# Generated at 2022-06-14 08:02:27.071202
# Unit test for constructor of class Router
def test_Router():
    assert Router.DEFAULT_METHOD == "GET"
    assert Router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:03:49.554573
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:03:58.143299
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.routes == dict()
    assert r.static_routes == list()
    assert r.dynamic_routes == dict()
    assert r.regex_routes == list()
    assert r.ctx == dict()
    assert r.name_index == dict()
    assert r.index == dict()
    assert r.converters == dict()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 08:03:59.376042
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:04:01.112057
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None



# Generated at 2022-06-14 08:04:07.743801
# Unit test for constructor of class Router
def test_Router():
    _router = Router()
    _router.DEFAULT_METHOD = "GET" # type: ignore
    _router.ALLOWED_METHODS = HTTP_METHODS # type: ignore
    assert _router.DEFAULT_METHOD == 'GET'
    assert _router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:04:14.456010
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.method_routes.clear()
    method_routes = {
        "get": {},
        "post": {},
        "put": {},
        "patch": {},
        "delete": {},
        "head": {},
        "options": {},
        "trace": {},
    }
    router.method_routes = method_routes

    router.finalize()

# Generated at 2022-06-14 08:04:15.539528
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 08:04:17.089925
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None



# Generated at 2022-06-14 08:04:28.013234
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx == {}
    assert router.routes == {}
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}


if __name__ == '__main__':
    test_Router()

# Generated at 2022-06-14 08:04:33.383189
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == []
