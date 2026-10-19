

# Generated at 2022-06-14 07:55:40.531998
# Unit test for method finalize of class Router
def test_Router_finalize():
    from pytest import raises

    router = Router()
    route = router.add(
                uri="/{id}",
                methods=['GET'],
                handler=None,
            )
    with raises(SanicException, match='Parameter names cannot use'): router.finalize() 
        

# Generated at 2022-06-14 07:55:51.396999
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router
    from sanic import Sanic
    from sanic.router import Route
    # Test 1: 
    test_app = Sanic("First test")
    test_routes= {"GET": [Route("/a", None, None, None, None)],"POST": [Route("/b", None, None, None, None)]}
    test_router = Router(test_routes, test_app, None)
    test_router.finalize()
    assert test_router.ctx == test_app
    # Test 2: 
    test_app = Sanic("Second test")
    test_routes= {"GET": [Route("/a", None, None, None, None)],"POST": [Route("/b", None, None, None, None)]}


# Generated at 2022-06-14 07:55:57.604563
# Unit test for method finalize of class Router
def test_Router_finalize():

    with pytest.raises(SanicException):
        @app.get("/")
        @app.websocket()
        async def index(request, ws):
            pass

        app.router.add_websocket_route(index)
        app.router.finalize()


# Generated at 2022-06-14 07:56:09.933587
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(
        {
            "a": "b"
        },
        "c",
        "d",
    )
    try:
        router.finalize({
            "a": "b"
        }, "c", "d")
    except:
        assert False
    try:
        router.finalize({
            "a": "b"
        }, "c", "d")
    except:
        assert True
    try:
        router.add(
            "/abc",
            ["GET"],
            "d",
            strict_slashes=True,
            version="1",
            name="abc",
        )
        router.finalize({
            "a": "b"
        }, "c", "d")
    except SanicException as e:
        assert True

# Generated at 2022-06-14 07:56:14.594687
# Unit test for constructor of class Router
def test_Router():
    print("Unit test for constructor of class Router")
    # Constructor of class Router
    router = Router()
    assert router
    print("    Router initialized")


# Generated at 2022-06-14 07:56:16.412221
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:56:29.114574
# Unit test for method finalize of class Router
def test_Router_finalize():
    test_router = Router(None, None)
    route_list = [
        Route(
            None,
            None,
            None,
            {  # type: ignore
                "__file_uri__": "value1",
                "__custom_uri__": "value2",
                "__custom_uri2__": "value3",
            },
            None,
            None,
            None,
        ),
        Route(
            None,
            None,
            None,
            {  # type: ignore
                "__file_uri__": "value4",
                "__custom_uri3__": "value7",
                "__custom_uri4__": "value8",
            },
            None,
            None,
            None,
        ),
    ]  # type: ignore

# Generated at 2022-06-14 07:56:34.629877
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        r = Router()
        r._routes = { "routes": [Route("/")] }
        r.finalize()
    except Exception as e:
        assert str(e) == "Invalid route: Route(path='/'). Parameter names cannot use '__'."
        return
    assert False
test_Router_finalize()

# Generated at 2022-06-14 07:56:36.373908
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.routes == {}
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}
    assert r.routes_static == {}
    assert str(r) == '{}'
    assert repr(r) == '<Router routes:0>'


# Generated at 2022-06-14 07:56:47.485033
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.route_dict = {'get': {'/': [Route(path='/',
                                            methods={'get'},
                                            handler=None)]},
                         'post': {'/': [Route(path='/',
                                             methods={'post'},
                                             handler=None)]}}
    try:
        router.finalize()
    except Exception as e:
        assert e.__class__.__name__ == 'SanicException'
        assert str(e) == "Invalid route: /. Parameter names cannot use '__'.";


# Generated at 2022-06-14 07:56:59.915576
# Unit test for method finalize of class Router
def test_Router_finalize():
    """Unit test for method finalize of class Router"""

    test_router = Router()
    test_route = Route("/", "GET", lambda: None, "")
    test_route.labels = ["__file_uri__"]
    test_route.add_prefix("/")
    test_router.dynamic_routes[id(test_route.path)] = test_route

    test_router.finalize()

# Generated at 2022-06-14 07:57:10.965906
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Test creating a route definition with an invalid label
    router = Router()
    router.add(
        uri="/a/<b:c>/<d:int>/<__f:int>", handler=lambda request: None
    )
    with pytest.raises(SanicException):
        router.finalize()

    # Test creating a route definition with a valid label, including '__'
    router = Router()
    router.add(
        uri="/a/<b:c>/<d:int>/<__file_uri__:int>", handler=lambda request: None
    )
    router.finalize()

# Generated at 2022-06-14 07:57:14.972485
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
    except Exception as e:
        assert False, "Creation of Router object failed" + str(e)
    else:
        assert True

# Generated at 2022-06-14 07:57:22.991041
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest # type: ignore
    try:
        router = Router(None)
        router.dynamic_routes[1] = Route(
            path="/url",
            handler=None,
            methods=["GET"],
            name=None,
            strict=False,
            unquote=False,
            labels=["__file_uri__"],
        )
        router.finalize()
    except SanicException as e:
        pytest.fail(
            f"SanicException: {e}",
        )

# Generated at 2022-06-14 07:57:33.160323
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route1 = Route("/test/<parameter>", lambda: 0)
    route2 = Route("/test/<parameter>", lambda: 0)
    route2.labels.add("__file_uri__")
    router.add_route(route1)
    router.add_route(route2)
    assert router.finalize() == None

    router = Router()
    route1 = Route("/test/<parameter>", lambda: 0)
    router.add_route(route1)
    with pytest.raises(SanicException):
        assert router.finalize() == None


# Generated at 2022-06-14 07:57:35.646390
# Unit test for method add of class Router
def test_Router_add():
    r = Router()
    r.add("/", methods=["GET", "POST"], handler=None)


# Generated at 2022-06-14 07:57:37.023955
# Unit test for constructor of class Router
def test_Router():
    Router()


# Generated at 2022-06-14 07:57:46.472770
# Unit test for constructor of class Router
def test_Router():
    """
    Test if the constructor of class Router works
    """
    from sanic import Sanic
    app = Sanic("sanic-server")
    router = Router(app, "sanic-router")

    assert router.ctx.app == app
    assert router.ctx.name == "sanic-router"

    assert router.routes_all == {}
    assert router.routes_regex == {}
    assert router.routes_dynamic == {}
    assert router.routes_static == {}

    assert not router.reserved_routes


# Generated at 2022-06-14 07:57:49.825409
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 07:57:50.430847
# Unit test for constructor of class Router
def test_Router():
    assert True

# Generated at 2022-06-14 07:57:56.163338
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert True

# Generated at 2022-06-14 07:58:01.801583
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.routes_all == []
    assert r.routes_static == []
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}
    assert r.name_index == {}
    assert r.ctx.path_converter is None
    assert r.ctx.app is None

# Generated at 2022-06-14 07:58:08.789769
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.dynamic_routes = {
        "uri3": Route(r, "uri3", lambda: None, ["GET"], {"requirements": {}}),
        "uri4": Route(r, "uri4", lambda: None, ["GET"], {"requirements": {}}),
    }
    r.finalize()

# Generated at 2022-06-14 07:58:10.101088
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 07:58:14.432485
# Unit test for constructor of class Router
def test_Router():
    a = Router()
    assert a.routes_static == {}
    assert a.routes_dynamic == {}
    assert a.routes_regex == {}
    assert a.routes_all == {}
    assert a.name_index == {}


# Generated at 2022-06-14 07:58:20.786916
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.app import Sanic
    app = Sanic("test_Router_finalize")
    router = Router(app)
    try:
        router.add("/test", methods=["GET"], handler=lambda: True, name="__test__")
    except SanicException as e:
        assert "Invalid route" in str(e)

# Generated at 2022-06-14 07:58:27.015826
# Unit test for method finalize of class Router
def test_Router_finalize():
    with pytest.raises(SanicException):
        r = Router()
        route = Route(r, path="/", handler=None, methods=["GET"], name=None)
        r.dynamic_routes[route.path] = route
        r.finalize()

# Generated at 2022-06-14 07:58:32.946318
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert router.ctx.app is None
    assert router.name_index == {}
    assert router.filters == set()
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.routes == {}


# Generated at 2022-06-14 07:58:36.838991
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {0: Route(None, 'path', None, None, None, None)}
    router.finalize()



# Generated at 2022-06-14 07:58:39.300119
# Unit test for constructor of class Router
def test_Router():
    try:
        route = Router()
        print(route)
    except Exception as error:
        print(error)

test_Router()

# Generated at 2022-06-14 07:58:59.066422
# Unit test for method finalize of class Router
def test_Router_finalize():
    # If a dynamic route uses an invalid label (with '__', but not '__file_uri__'),
    # then raise an error of class 'SanicException'
    def handler():
        pass

    router = Router()
    router.static_routes = {"/static_route"}
    router.dynamic_routes = {"/dynamic_route": Route(handler, "/dynamic_route", {}, ["__file_uri__"]),
                             "/dynamic_route2": Route(handler, "/dynamic_route2", {}, ["__filename__"])}
    router.regex_routes = {"regex_route": Route(handler, "/regex_route", {"requirements": {"test": "test"}})}
    router.ctx = {"app": {"_generate_name": lambda x: x}}

# Generated at 2022-06-14 07:59:06.494589
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ROUTER_CACHE_SIZE == 1024
    assert router.ALLOWED_METHODS == ['POST', 'DELETE', 'PUT', 'OPTIONS', 'PATCH', 'HEAD', 'GET']
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_LABELS == ('__file_uri__',)
    assert isinstance(router, BaseRouter)


# Generated at 2022-06-14 07:59:08.101247
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router) == True


# Generated at 2022-06-14 07:59:10.701110
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router

# Unit tests for method find_route_by_view_name of class Router

# Generated at 2022-06-14 07:59:24.753786
# Unit test for method finalize of class Router
def test_Router_finalize():

    router = Router()
    # router.dynamic_routes = {'a': Route('a', 'a', 'a', {}, {}, {}, [])}
    # router.dynamic_routes = {'a': Route(name='a', method='a', host='a', headers={}, handler=None, defaults={}, labels=[], requirements=[], strict_slashes=False, unquote=False, host_matching=True, ctx={})}
    router.dynamic_routes = {
        'a': Route(
            name='a', method='a', path='a', headers={}, handler=None,
            defaults={}, labels=['__file_uri__'], requirements=[],
            strict_slashes=False, unquote=False, host_matching=True, ctx={})
    }
    #

# Generated at 2022-06-14 07:59:26.741717
# Unit test for constructor of class Router
def test_Router():
    # Unit test for constructor of class Router
    router = Router()
    return router


# Generated at 2022-06-14 07:59:30.958437
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic_routing import Router as BaseRouter

    app = Sanic('test_Router_finalize')
    router = Router(app)
    try:
        router.finalize()
    except Exception:
        assert False
    router = BaseRouter(app)
    try:
        router.finalize()
    except Exception:
        assert True

# Generated at 2022-06-14 07:59:44.038809
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.blueprints import Blueprint
    from sanic.exceptions import ServerError
    from sanic.server import HttpProtocol
    from sanic.response import HTTPResponse
    from sanic.views import HTTPMethodView
    from sanic.websocket import ConnectionClosed
    from sanic.config import BaseConfig
    from sanic.handlers import ErrorHandler

    import sanic

    sanic.app = sanic.Sanic(__name__)
    sanic.app.config.TESTING = True
    sanic.app.config.CUSTOM_STATIC_PATH = '/custom_static'
    sanic.app.static(path='/custom_static', directory='.')
    sanic.app.static(path='/', directory='.')

# Generated at 2022-06-14 07:59:46.006488
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)

# Generated at 2022-06-14 07:59:49.555800
# Unit test for constructor of class Router
def test_Router():
    from sanic.router import Router
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:00:12.021717
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.constants import HTTP_METHODS
    from sanic_routing.router import Router
    from sanic.response import text

    router = Router()
    for i, route in enumerate(HTTP_METHODS):
        router.add(
            uri=f"/{route}/",
            methods=[route],
            handler=text("123456"),
            name=f"route{i}",
        )

    router.finalize()

# Generated at 2022-06-14 08:00:23.971068
# Unit test for constructor of class Router
def test_Router():
    baseRouter = Router()
    assert baseRouter.DEFAULT_METHOD == 'GET'
    assert baseRouter.ALLOWED_METHODS == HTTP_METHODS
    assert baseRouter.routes_all == {}
    assert baseRouter.routes_static == {}
    assert baseRouter.routes_dynamic == {}
    assert baseRouter.routes_regex == {}

    baseRouter.finalize()
    assert baseRouter.DEFAULT_METHOD == 'GET'
    assert baseRouter.ALLOWED_METHODS == HTTP_METHODS
    assert baseRouter.routes_all == {}
    assert baseRouter.routes_static == {}
    assert baseRouter.routes_dynamic == {}
    assert baseRouter.routes_regex == {}


# Generated at 2022-06-14 08:00:31.676558
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = BaseRouter()
    route = Route(path='/a/1/b/1', handler=None, methods=None)
    route.labels = ['a', 'b']
    router.dynamic_routes['/a/1/b/1'] = route
    router.finalize()
    assert len(router.dynamic_routes) == 0


# Generated at 2022-06-14 08:00:45.951200
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS
    assert r._get.__name__ == "_get"
    assert r.get.__name__ == "get"
    assert r.get.cache_info().__name__ == "CacheInfo"
    assert r.get.cache_clear.__name__ == "cache_clear"
    assert r.get.__annotations__ == {
            "path": str,
            "method": str,
            "host": Optional[str],
            "return": Tuple[Route, RouteHandler, Dict[str, Any]]
        }

# Generated at 2022-06-14 08:00:53.286235
# Unit test for constructor of class Router
def test_Router():
    # Given
    path = '/'
    method = 'GET'
    host = '127.0.0.1'

    try:
        router = Router()
        router.get(path, method, host)
    except NotFound as e:
        assert True

    try:
        router = Router()
        router.get(path, method, host)
    except MethodNotSupported as e:
        assert True


# Generated at 2022-06-14 08:00:56.506339
# Unit test for constructor of class Router
def test_Router():
    """
    Testing the __init__() constructor of the Router
    """
    # Parameters for the constructor
    _router = Router()

    # Check instance of type Router
    assert isinstance(_router, Router)

# Generated at 2022-06-14 08:00:58.177593
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None



# Generated at 2022-06-14 08:00:59.910523
# Unit test for constructor of class Router
def test_Router():
    # unit test for constructor
    result = Router()
    assert(result is not None)

# Generated at 2022-06-14 08:01:01.159855
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 08:01:09.266875
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None
    assert router.routes_all == []
    assert router.dynamic_routes == dict()
    assert router.static_routes == dict()
    assert router.name_index == dict()
    assert router.routes_by_endpoint == dict()
    assert router.routes_regex == []


# Generated at 2022-06-14 08:01:59.544674
# Unit test for constructor of class Router
def test_Router():
    from sanic.blueprints import Blueprint
    from sanic.router import Router


    bp = Blueprint("bla")

    bp.route("/", methods=["GET"])(lambda x: x)
    bp.add_route(bp.router.routes[0], "/bla/<param_name>")

    r = Router(
        router_name="bla",
        blueprint=bp,
        host="example.com",
        base_url="base_url",
        strict_slashes=True,
        name="test",
    )

    assert bp.router.router_name == "bla"
    assert bp.router.host == "example.com"
    assert bp.router.base_url == "base_url"
    assert bp.router.st

# Generated at 2022-06-14 08:02:03.343047
# Unit test for constructor of class Router
def test_Router():
    # Create new object
    my_router = Router()
    # Test if the object is type Router
    assert isinstance(my_router, Router)

# Test if the property routes_all is return type dict

# Generated at 2022-06-14 08:02:14.277757
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic

    from sanic.response import json

    app = Sanic(__name__)

    @app.route('/<__file_uri__>')
    def handler(request, __file_uri__):
        return json({'test': 'success'})

    app.add_route(handler, '/<__file_uri__>')

    route = app.router.routes_all[0]
    assert any(
        label.startswith("__") and label not in ALLOWED_LABELS
        for label in route.labels
    ) is False

# Generated at 2022-06-14 08:02:15.954072
# Unit test for constructor of class Router
def test_Router():
    print("test Router")
    router = Router()
    assert router.__class__.__name__ == "Router"


# Generated at 2022-06-14 08:02:19.040732
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert len(router.ALLOWED_METHODS) == 11


# Generated at 2022-06-14 08:02:22.514958
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic
    app = Sanic('test_Router')
    router = Router(app)
    assert router
    assert router.ctx.app == app

# Generated at 2022-06-14 08:02:28.561308
# Unit test for method finalize of class Router
def test_Router_finalize():
    from . import Sanic

    app = Sanic("test_Router_finalize")

    @app.route("/")
    def handler(request):
        pass

    router = Router(app)
    with pytest.raises(SanicException):
        router.finalize()

    app.config.KEEP_ALIVE = False

# Generated at 2022-06-14 08:02:30.582022
# Unit test for method finalize of class Router
def test_Router_finalize():
    # example to implement
    return

if __name__ == "__main__":
    test_Router_finalize()

# Generated at 2022-06-14 08:02:31.242023
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 08:02:33.406047
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"

# Generated at 2022-06-14 08:03:40.895099
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router.ctx, dict)


# Generated at 2022-06-14 08:03:43.295481
# Unit test for constructor of class Router
def test_Router():
    my_router = Router()
    assert isinstance(my_router, Router) == True


# Generated at 2022-06-14 08:03:56.868491
# Unit test for method finalize of class Router
def test_Router_finalize():
    import sanic.compat
    from sanic.router import Route
    from sanic.utils import SanicException

    router = Router()

    try:
        Route(
            '/path/',
            'GET',
            lambda request: None,
            name='dummy_route',
            host='dummy_host',
            uri_template='template',
            strict_slashes=False,
            version=1.0,
            labels={'__file_uri__': 'file/uri'},
        )
    except SanicException:
        pass
    else:
        raise Exception('No exception was raised!')


# Generated at 2022-06-14 08:04:08.618938
# Unit test for constructor of class Router
def test_Router():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse

    app = Sanic('test_Router')
    bp = Blueprint('test_Router')
    @bp.route('/')
    def handler(request: Request) -> HTTPResponse:
        pass

    bp.add_route(handler, '/')
    app.blueprint(bp)
    app.router.add(uri='/', methods=['GET'], handler=handler)
    r = Router()
    assert r is not None
    try:
        r._get('/','GET','abc')
    except NotFound as e:
        assert True
    except Exception as e:
        assert False


# Generated at 2022-06-14 08:04:10.272235
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:04:20.145556
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT']
    assert router.not_found is None
    assert router.name_index == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.ctx.app is None


# Generated at 2022-06-14 08:04:33.546546
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router._get.cache_info().maxsize == 1024
    assert router.get.cache_info().maxsize == 1024
    #assert router.add.cache_info().maxsize == 1024
    assert router.find_route_by_view_name.cache_info().maxsize == 1024
    assert router.routes_all.cache_info().maxsize == 1024
    assert router.routes_static.cache_info().maxsize == 1024
    assert router.routes_dynamic.cache_info().maxsize == 1024
    assert router.routes_regex.cache_info().maxsize == 1024

# Generated at 2022-06-14 08:04:47.016437
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    A unit test for finalize method of class Router
    """
    import pytest
    from sanic.router import Router
    from sanic.exceptions import SanicException
    import re

    ROUTER_CACHE_SIZE = 1024

    router = Router(cache_size=ROUTER_CACHE_SIZE, domain=None)

    uri_1 = "/<param_1>/<param_2>/<param_3>/<param_4>/<param_5>"
    uri_2 = "/<param_1>/<param_2>/<param_3>/<param_4>/<param_5>"

    router.add(
        uri=uri_1,
        methods=["GET"],
        handler=print,
    )


# Generated at 2022-06-14 08:04:48.261405
# Unit test for constructor of class Router
def test_Router():
    assert Router()


# Generated at 2022-06-14 08:04:49.684515
# Unit test for method finalize of class Router
def test_Router_finalize():
    _test_Router_finalize()
