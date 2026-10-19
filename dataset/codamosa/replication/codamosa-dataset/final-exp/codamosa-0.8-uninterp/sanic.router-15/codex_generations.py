

# Generated at 2022-06-14 07:55:23.203966
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:55:27.379625
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Created by: Pritam Bakal
    a = Route(pattern=r"/foo", endpoint=None, methods={"GET"})
    router = Router()
    router.dynamic_routes[a] = "a"
    router.finalize()

# Generated at 2022-06-14 07:55:28.954184
# Unit test for constructor of class Router
def test_Router():
    router = Router(None, None)



# Generated at 2022-06-14 07:55:33.007729
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx == None
    assert router.dynamic_routes == {}
    assert router.regex_routes == []
    assert router.static_routes == {}


# Generated at 2022-06-14 07:55:35.818481
# Unit test for constructor of class Router
def test_Router():
    router = Router.__new__(Router)  # type: ignore
    assert router

# Generated at 2022-06-14 07:55:48.559877
# Unit test for constructor of class Router
def test_Router():
    import pytest
    router = Router()
    assert router.ctx is None
    assert router.routes == dict()
    assert router.routes_all == dict()
    assert router.routes_static == dict()
    assert router.routes_dynamic == dict()
    assert router.routes_regex == dict()
    assert router.name_index == dict()
    assert router.static_bridge == dict()
    assert router.compiled_regex_table is None
    assert router.regex_table == dict()
    assert router.dynamic_table == dict()
    assert router.compiled_dynamic_table == dict()
    assert router.compiled_regex_table is None
    assert router.nodes is None
    assert router.label_pattern is None

# Generated at 2022-06-14 07:55:51.335874
# Unit test for constructor of class Router
def test_Router():
    try:
        Router()
    except Exception:
        assert 0, 'Unable to construct a Router'
    assert 1


# Generated at 2022-06-14 07:55:59.429932
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {
        "localhost": [Route("/", None, ["__file_name__"], None)]
    }
    router.finalize("localhost")

    router1 = Router()
    router1.dynamic_routes = {
        "localhost": [Route("/", None, ["__filename__"], None)]
    }
    with pytest.raises(SanicException) as dummy:
        router1.finalize("localhost")

# Generated at 2022-06-14 07:56:02.903004
# Unit test for constructor of class Router
def test_Router():
    routes = Router()
    assert isinstance(routes, Router)
    assert isinstance(routes, BaseRouter)


# Generated at 2022-06-14 07:56:07.920260
# Unit test for method finalize of class Router
def test_Router_finalize():
    class MockRouter(BaseRouter):
        pass
    router = MockRouter()
    router.dynamic_routes = {}
    router.routes = []
    router.dynamic_routes["sfd"] = Route(None, None, None, None)
    try:
        router.finalize()
    except SanicException:
        pass

# Generated at 2022-06-14 07:56:25.945287
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest

    def test_invalid_lable():
        r = Router()
        r.dynamic_routes = [{
            'labels': ['__file'],
            'uri': '/{__file}/',
        }]
        with pytest.raises(SanicException):
            r.finalize()

    def test_invalid_lable():
        r = Router()
        r.dynamic_routes = [{
            'labels': ['__file'],
            'uri': '/{__file}/',
        }]
        with pytest.raises(SanicException):
            r.finalize()

if __name__ == "__main__":
    import os
    import sys
    pyfile = sys.modules[__name__].__file__

# Generated at 2022-06-14 07:56:36.149870
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import SanicException
    import pytest
    from sanic.router import Router
    from sanic.models.route_info import RouteInfo
    from sanic.models.route_info import RouteInfoDynamic
    from sanic.models.route_info import RouteInfoStatic

    class FakeRouter(Router):
        def __init__(self, prefix=''):
            self.prefix = prefix
            self.routes = {
                '3': RouteInfoStatic('/3'),
                '2': RouteInfoStatic('/2'),
                '1': RouteInfoStatic('/1'),
            }

# Generated at 2022-06-14 07:56:40.317670
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:56:47.826144
# Unit test for constructor of class Router
def test_Router():
    with pytest.raises(SanicException) as excinfo:
        router = Router()
        router.add(
            "/users/{id}",
            ['GEt', 'POST'],
            None
        )
    assert str(excinfo.value) == "Invalid route: Route(path='/users/{id}', method='GEt', handler=None, name=None, strict=False, unquote=False, labels=()). Parameter names cannot use '__'."

# Generated at 2022-06-14 07:56:49.181667
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 07:56:50.216450
# Unit test for method finalize of class Router
def test_Router_finalize():
    Router().finalize()

# Generated at 2022-06-14 07:57:00.450461
# Unit test for constructor of class Router
def test_Router():
    """
    Unit test for Router class
    """
    # Create a new Router object with acceptable values
    router = Router()
    # Check if the router has been created successfully
    assert router
    # Check if the allowed methods of the router are a subset of HTTP_METHODS
    assert set(router.ALLOWED_METHODS).issubset(set(HTTP_METHODS))
    # Check if the default method of the router is GET
    assert router.DEFAULT_METHOD == 'GET'
    # Check if the route cache size of the router is 1024
    assert router.route_cache_size == '1024'
    # Check if the method cache size of the router is 1024
    assert router.method_cache_size == '1024'

# Generated at 2022-06-14 07:57:05.294710
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == 'GET'
    assert r.ALLOWED_METHODS == ['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'TRACE']

# Generated at 2022-06-14 07:57:06.167500
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 07:57:16.258884
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route(handler=lambda *args, **kwargs: "", **{'path': "/",
                                                          'methods': [
                                                              "GET", "POST"
                                                          ]})
    with pytest.raises(SanicException):
        router.dynamic_routes = {'__hello': route}
        
    route = Route(handler=lambda *args, **kwargs: "", **{'path': "/",
                                                          'methods': [
                                                              "GET", "POST"
                                                          ],
                                                          'labels': [
                                                              '__hello'
                                                          ]})

# Generated at 2022-06-14 07:57:23.932995
# Unit test for constructor of class Router
def test_Router():
    router = Router(None)
    assert router


# Generated at 2022-06-14 07:57:30.840071
# Unit test for constructor of class Router
def test_Router():
    # Fixture
    methods = list(HTTP_METHODS)
    handler = lambda: None

    # Test
    router = Router(False)
    router.add("/", methods, handler)

    # Verify
    assert router.routes_all
    assert not router.routes_static
    assert router.routes_dynamic
    assert router.routes_regex


# Generated at 2022-06-14 07:57:44.448535
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(router_ctx={}, router_name="test/Router")
    def handler():pass
    class Route:
        def __init__(self, route_ctx, path, uri, handler, methods, name, strict, unquote):
            self.ctx = route_ctx
            self.path = path
            self.uri = uri
            self.handler = handler
            self.methods = methods
            self.name = name
            self.strict = strict
            self.unquote = unquote


# Generated at 2022-06-14 07:57:45.974498
# Unit test for constructor of class Router
def test_Router():
    obj = Router()
    assert obj is not None


# Generated at 2022-06-14 07:57:52.344923
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(app=App())
    path = "/test/:id"
    route = router.add(
        uri=path,
        methods=["GET"],
        handler=None,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name=None,
        unquote=False,
    )
    router.finalize()
    assert route in router.dynamic_routes.values()

# Generated at 2022-06-14 07:58:03.151580
# Unit test for method finalize of class Router
def test_Router_finalize():
    import sanic
    import sanic.routing

    app = sanic.Sanic(__name__)
    router = sanic.routing.Router(app)
    class TestRoute(object):
        def __init__(self,labels):
            self.labels = labels

    # Case 1: no parameters
    labels = []
    route = TestRoute(labels = labels)
    router.dynamic_routes = {1:route}
    router.finalize()

    # Case 2: parameters start with __
    labels = ["__file_uri__"]
    route = TestRoute(labels = labels)
    router.dynamic_routes = {1:route}
    router.finalize()

    # Case 3: parameters do not start with __
    labels = ["ABC"]

# Generated at 2022-06-14 07:58:04.250862
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 07:58:16.418310
# Unit test for constructor of class Router
def test_Router():
    from sanic.response import json
    from sanic.server import HttpProtocol
    from sanic.exceptions import InvalidUsage
    from sanic.router import Router
    from sanic.route import Route
    from sanic.server import HttpProtocol
    from sanic.websocket import WebSocketProtocol
    from sanic.response import json
    from sanic.exceptions import InvalidUsage

    router=Router()
    router.add_route(Route(uri='/',methods=['get']))
    router.add(None,['get'],'/')
    router.hosts
    router.hosts.add('test_host')
    router.hosts
    router.hosts.add('http://a.com')
    router.hosts
    router.hosts.add('http://b.com')

# Generated at 2022-06-14 07:58:17.567362
# Unit test for constructor of class Router
def test_Router():
    obj = Router()
    assert obj

# Generated at 2022-06-14 07:58:25.636522
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}

    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}

    assert router.name_index == {}
    assert router.scheme_index == {}
    assert router.paths == {}



# Generated at 2022-06-14 07:58:37.094841
# Unit test for constructor of class Router
def test_Router():
    """
    Tests for Router class
    """
    router = Router()
    assert router is not None

# Generated at 2022-06-14 07:58:48.758123
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    from collections import namedtuple
    from typing import Type

    app: Type[Sanic] = Sanic("test_Router_finalize")
    app.config.KEEP_ALIVE = 5

    class _Mock(namedtuple("_Mock", ["name"])):
        def __repr__(self):
            return f"<route {self.name}>"

    Mock = _Mock(name="Mock")

    router = Router(app)
    router.regex_routes[""] = Mock

    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 07:58:58.984706
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Router()

# Generated at 2022-06-14 07:59:08.730538
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ALLOWED_METHODS == ["OPTIONS", "HEAD",
                                    "GET", "PUT",
                                    "POST", "PATCH",
                                    "DELETE", "TRACE",
                                    "CONNECT", "PROPFIND"]
    assert r.DEFAULT_METHOD == "GET"
    assert r.routes == {}
    assert r.ctx is None
    assert r.name_index == {}
    assert r.regex_routes == {}
    assert r.static_routes == {}
    assert r.dynamic_routes == {}

# Generated at 2022-06-14 07:59:14.823149
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route(path="/", handler=None, methods=None, name=None)
    route.labels = ("__file_uri__", "_xx", "name")
    router.dynamic_routes[route.path] = route
    router.finalize()

if __name__ == '__main__':
    test_Router_finalize()

# Generated at 2022-06-14 07:59:17.791604
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert len(router.routes_all) == 0


# Generated at 2022-06-14 07:59:25.125484
# Unit test for method finalize of class Router
def test_Router_finalize():
    app_obj = sanic.Sanic(__name__)
    router_obj = Router()

    def good_handler():
        pass

    def bad_handler():
        pass

    router_obj.add('foo/<__good_param>', [], good_handler)
    router_obj.add('bar/<__bad_param>', [], bad_handler)

    router_obj.finalize(app_obj)

# Generated at 2022-06-14 07:59:32.787841
# Unit test for method finalize of class Router
def test_Router_finalize():

    # *************************************************************************
    # Create a Router object
    router = Router(None)

    # Add a route
    route1 = router.add(
        uri='/',
        methods=('GET', 'POST'),
        handler=None,
        host=None,
        strict_slashes=False,
        stream=False,
        ignore_body=False,
        version=None,
        name='index',
        unquote=False,
        static=False,
    )

    # Save the route in the dynamic_routes attribute of the object
    router.dynamic_routes = { '/': route1 }

    # *************************************************************************
    # Create a different Router object
    router2 = Router(None)

    # Add a route

# Generated at 2022-06-14 07:59:38.850749
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic
    app = Sanic("test_Router_finalize")

    @app.route("/")
    async def foo(request):
        pass

    try:
        Router.finalize(app)
    except Exception as e:
        app.stop()
        raise e

# Generated at 2022-06-14 07:59:40.122058
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert router


# Generated at 2022-06-14 07:59:59.675147
# Unit test for method finalize of class Router
def test_Router_finalize():
    class Router(object):
        def __init__(self):
            pass

        def __getattr__(self, name):
            if name == 'name_index':
                return {
                    "foo": {"labels": set(["bar", "__baz__"])},
                    "baz": {"labels": set(["foo", "__bar__"])},
                }
            elif name == 'dynamic_routes':
                return {
                    "foo": {"labels": set(["bar", "__baz__"])},
                    "baz": {"labels": set(["foo", "__bar__"])},
                }

    router = Router()

# Generated at 2022-06-14 08:00:01.430250
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:00:09.833121
# Unit test for constructor of class Router
def test_Router():
    assert(Router.ALLOWED_METHODS == HTTP_METHODS)
    assert(Router.DEFAULT_METHOD == "GET")
    assert(Router.routes_all == {})
    assert(Router.routes_static == {})
    assert(Router.routes_dynamic == {})
    assert(Router.routes_regex == {})

# Generated at 2022-06-14 08:00:10.385967
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 08:00:12.746357
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert(router.routes == {})
    assert(router.dynamic_routes == {})
    assert(router.regex_routes == {})


# Generated at 2022-06-14 08:00:20.193666
# Unit test for method finalize of class Router
def test_Router_finalize():
    _uri: str = ""
    _methods: Iterable[str] = ["test_method"]
    _handler: RouteHandler = "test_handler"
    _host: Optional[Union[str, Iterable[str]]] = "test_host"
    _strict_slashes: bool = False
    _stream: bool = False
    _ignore_body: bool = False
    _version: Union[str, float, int] = 0
    _name: Optional[str] = "test_name"
    _unquote: bool = False
    _static: bool = False
    router = Router()
    router.add(_uri, _methods, _handler, _host, _strict_slashes, _stream, _ignore_body, _version, _name, _unquote, _static)
    route = router.find_route_

# Generated at 2022-06-14 08:00:28.608491
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.models.route_branches import RouteBranch
    from sanic.models.route_node import RouteNode
    
    route = RouteNode(RouteBranch('/path1/path2/:param'), RouteNode(RouteBranch('/path3/:param')))
    router = Router()
    try:
        router.finalize([route])
    except SanicException:
        assert True
    else:
        assert False and 'Should raise SanicException'


# Generated at 2022-06-14 08:00:29.918549
# Unit test for constructor of class Router
def test_Router():
    pass


# Generated at 2022-06-14 08:00:44.034011
# Unit test for method finalize of class Router

# Generated at 2022-06-14 08:00:44.751629
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 08:01:01.515121
# Unit test for constructor of class Router
def test_Router():
    r = Router()

# Generated at 2022-06-14 08:01:09.617007
# Unit test for method finalize of class Router
def test_Router_finalize():
    class App:
        def __init__(self) -> None:
            self.router = Router()

        @staticmethod
        def _generate_name(name: str) -> str:
            return name

    app = App()
    app.router.finalize()

    route = Route(
        path="/",
        handler=None,
        methods=None,
        name=None,
        strict=False,
        ctx=app.router.ctx,
        unquote=False,
        host=None,
        parameters={},
        labels={'__file_uri__': '<builtin>', '__module__': '<builtin>'},
    )

    assert route.labels == {"__file_uri__": "<builtin>", "__module__": "<builtin>"}


# Generated at 2022-06-14 08:01:11.431941
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)


# Generated at 2022-06-14 08:01:14.391067
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    router = Router()
    # router.dynamic_routes = {"a": {}}  # this is dummy
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 08:01:19.497337
# Unit test for method finalize of class Router
def test_Router_finalize():
    def foo_bar(request):
        pass
    router = Router()
    router.add("/foo/<bar>", ["GET"], foo_bar)
    try:
        router.finalize()
    except:
        assert False, 'fail to finalize'
    assert True

# Generated at 2022-06-14 08:01:22.727602
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 08:01:23.627722
# Unit test for constructor of class Router
def test_Router():
    Router()


# Generated at 2022-06-14 08:01:28.615032
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException) as e:
        router.finalize()
    assert e.value.args[0] == "No instances of application were found. Did you inherit from Sanic?"

# Generated at 2022-06-14 08:01:35.177002
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add_route(path='/', handler=None, methods=['GET'])

    with pytest.raises(SanicException) as ex:
        r.finalize()

    assert str(ex.value) == "Invalid route: [GET] /. Parameter names cannot use '__'."


# Unit tests for method get of class Router

# Generated at 2022-06-14 08:01:36.433435
# Unit test for constructor of class Router
def test_Router():
    router = Router()



# Generated at 2022-06-14 08:02:09.416859
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:02:11.897464
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.app is None
    assert router.ctx.hosts is None

# Generated at 2022-06-14 08:02:22.850801
# Unit test for constructor of class Router
def test_Router():
    a = Router() # correct
    b = Router(name = "Router1") # correct
    c1 = Router(name = 2) # wrong, name should be string
    c2 = Router(name = None) # wrong, name should be string
    c3 = Router(name = "") # correct

    a = Router(default_method = "GET") # correct
    b = Router(allowed_methods = ALLOWED_METHODS) # correct
    c = Router(default_method = "GET", allowed_methods = ALLOWED_METHODS) # correct
    d1 = Router(default_method = None) # wrong, default_method should be string
    d2 = Router(default_method = "") # correct
    e1 = Router(allowed_methods = None) # wrong, allowed_methods should be iterable of str
   

# Generated at 2022-06-14 08:02:32.870939
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        # Code that raises an exception
        router = Router()
        route = Route(
            path="/hi",
            handler=lambda: print("hello!"),
            methods=["GET"],
            name="hello",
            strict=False,
            unquote=False,
        )
        route.labels = ['__x__y']

        router.dynamic_routes = {'__x__y': route}
        router.finalize()
    except SanicException as e:
        # The exception is expected, test passes
        return
    
    assert False  # The exception is not raised, test fails

# Generated at 2022-06-14 08:02:34.228446
# Unit test for constructor of class Router
def test_Router():
    s = Router()

# Generated at 2022-06-14 08:02:39.650734
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    path_dynamic = "/<name>"
    path_dynamic_1 = "/<name>/<name>"
    path_dynamic_2 = "/<name>"
    path_dynamic_3 = "/<name>/<name>"

    try:
        router.add(path_dynamic, ["GET"], lambda r: "", name="test")
    except Exception as e:
        raise AssertionError() from e

    try:
        router.add(path_dynamic_1, ["GET"], lambda r: "", name="test")
    except Exception as e:
        raise AssertionError() from e

    try:
        router.add(path_dynamic_2, ["GET"], lambda r: "", name="test")
    except Exception as e:
        raise AssertionError() from e

# Generated at 2022-06-14 08:02:41.226856
# Unit test for constructor of class Router
def test_Router():
    my_Router = Router()
    assert isinstance(my_Router, Router)

# Generated at 2022-06-14 08:02:53.865810
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(None)

    # Routes from sanic/test_router.py

# Generated at 2022-06-14 08:02:59.889952
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}  # test _dynamic
    assert router.static_routes == {}  # test _static
    assert router.indices == {}  # test _indices
    assert router.regex_routes == []  # test _regexes
    assert router.name_index == {}  # test _name_index


# Generated at 2022-06-14 08:03:01.493124
# Unit test for constructor of class Router
def test_Router():
    assert Router()


# Generated at 2022-06-14 08:04:21.844878
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()

    with pytest.raises(SanicException):
        # can't use for loop
        router.add('/test_Router_finalize', ["GET"], None)

        router.finalize()

    router.add('/test_Router_finalize/1', ["GET"], None)
    router.finalize()

    with pytest.raises(SanicException):
        # can't use for loop
        router.add('/test_Router_finalize/2', ["GET"], None, unquote=True)

        router.finalize()

    router.add('/test_Router_finalize/3', ["GET"], None, unquote=True)
    router.finalize()

# Generated at 2022-06-14 08:04:27.841290
# Unit test for method finalize of class Router
def test_Router_finalize():
    def handler():
        pass

    router = Router()
    router.add('/users/<id>', ['GET'], handler)
    router.add('/users/__file_uri__', ['GET'], handler)
    router.add('/users/__invalid__', ['GET'], handler)

# Generated at 2022-06-14 08:04:33.722906
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.add(uri='/test/<__test>', methods=['GET'], handler=None)
        router.finalize()
    except SanicException as e:
        assert "Invalid route: " in str(e)


# Generated at 2022-06-14 08:04:41.739980
# Unit test for constructor of class Router
def test_Router():
    router = Router(None, [], [])
    assert router.ctx == None
    assert router.routes == []
    assert router.dynamic_routes == {}
    assert router.static_routes == []
    assert isinstance(router.name_index, dict)
    assert router.name_index == {}
    assert router.regex_routes == []


# Generated at 2022-06-14 08:04:42.897962
# Unit test for constructor of class Router
def test_Router():
    assert Router.__doc__ != None



# Generated at 2022-06-14 08:04:45.754856
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    route = Router()
    assert isinstance(route, Router) == True

# Generated at 2022-06-14 08:04:50.118792
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic

    app = Sanic('test_Router_finalize')
    router = Router()
    assert(router.finalize(app) == 'no routes added')

# Generated at 2022-06-14 08:04:52.750944
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:04:55.942787
# Unit test for constructor of class Router
def test_Router():
    """
    .. versionadded:: 20.0
    """
    router = Router()
    assert isinstance(router, Router)



# Generated at 2022-06-14 08:05:04.969775
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.views import CompositionView
    from sanic.router import Router as SanicRouter

    def view_func(request):
        return request

    composition_view_a = CompositionView()
    composition_view_a.add(view_func, methods=["GET"])
    composition_view_b = CompositionView()
    composition_view_b.add(view_func, methods=["GET"])
    composition_view_c = CompositionView()
    composition_view_c.add(view_func, methods=["GET"])

    router = SanicRouter()
    router.add(
        uri="/composition_view_a",
        methods=["GET"],
        handler=composition_view_a,
    )