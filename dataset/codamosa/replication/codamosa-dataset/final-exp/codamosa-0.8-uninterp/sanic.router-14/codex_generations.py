

# Generated at 2022-06-14 07:55:22.923311
# Unit test for constructor of class Router
def test_Router():
    try:
        r = Router()
    except Exception as e:
        assert e


# Generated at 2022-06-14 07:55:27.113411
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)
    assert r.routes_all == []
    assert r.routes_static == []
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}


# Generated at 2022-06-14 07:55:29.641009
# Unit test for constructor of class Router
def test_Router():
    import sanic
    app = sanic.Sanic()
    router = Router(app)
    assert router.ctx == app

# Generated at 2022-06-14 07:55:39.164318
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']
    assert router.ctx is None
    assert router.name_index == {}
    assert router.hosts_index == {}
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}

# Generated at 2022-06-14 07:55:41.967785
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert len(router.routes_all) == 0


system_router = Router()
app_router = Router()

# Generated at 2022-06-14 07:55:42.760620
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:55:46.444584
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 07:55:49.787873
# Unit test for constructor of class Router
def test_Router():
   router = Router("name", None)
   assert router.name == "name"
   assert router.ctx is None


# Generated at 2022-06-14 07:55:52.318339
# Unit test for constructor of class Router
def test_Router():
    """
    Unit test case to test the constructor of class Router
    """
    router = Router()
    assert isinstance(router, Router)



# Generated at 2022-06-14 07:55:54.419667
# Unit test for constructor of class Router
def test_Router():
    assert Router.__doc__ is not None


# Generated at 2022-06-14 07:56:03.220602
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 07:56:13.534212
# Unit test for method finalize of class Router
def test_Router_finalize():

    import sys
    import threading

    from unittest.mock import MagicMock, patch

    from sanic.exceptions import SanicException

    from sanic.router import Router
    from sanic.server import HttpProtocol

    from .helper import mock_handler

    def router_finalize(bad_label: bool):
        APP = MagicMock()
        APP.debug = False
        APP.auto_sanic_config = False
        APP.transports = MagicMock()

# Generated at 2022-06-14 07:56:15.354111
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.__class__.__name__ == "Router"

# Generated at 2022-06-14 07:56:16.145735
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:56:16.918700
# Unit test for constructor of class Router
def test_Router():
    Router()

# Generated at 2022-06-14 07:56:24.773679
# Unit test for method finalize of class Router
def test_Router_finalize():
    new_router = Router(None)
    new_router.dynamic_routes[1] = Route()
    new_router.dynamic_routes[1].labels = ["__file_uri__", "__label__"]
    try:
        new_router.finalize(None)
    except Exception as e:
        # this should raise an exception, since it is an invalid route
        assert True
    else:
        assert False

# Generated at 2022-06-14 07:56:26.342170
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router


# Generated at 2022-06-14 07:56:30.978491
# Unit test for method add of class Router
def test_Router_add():
    """
    Method used to test if the function add
    worked correctly
    """
    @add.route("/")
    async def add_handler(request):
        return response.text("OK")

    assert add_handler.routes == [("/", ['GET'])]

# Generated at 2022-06-14 07:56:32.508265
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:56:39.758571
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert not hasattr(router, '__weakref__')
    assert isinstance(router.routes, list)
    assert isinstance(router.name_index, dict)
    assert isinstance(router.regex_routes, dict)
    assert isinstance(router.static_routes, dict)
    assert isinstance(router.dynamic_routes, dict)
    assert isinstance(router.ctx, dict)


# Generated at 2022-06-14 07:56:52.904017
# Unit test for constructor of class Router
def test_Router():
    router = Router(app=None)
    assert isinstance(router, Router) == True


# Generated at 2022-06-14 07:56:54.334425
# Unit test for method finalize of class Router
def test_Router_finalize():
    method=Router().finalize()


# Generated at 2022-06-14 07:57:03.898765
# Unit test for method finalize of class Router
def test_Router_finalize():

    def testmethod(rq):
        return rq.raw_args["name"]

    import pathlib
    import sys

    sys.path.insert(0, str(pathlib.Path(__file__).parent.absolute()))
    import sanic.exceptions
    from sanic.router import Router

    Router.DEFAULT_METHOD = "GET"
    Router.ALLOWED_METHODS = ["GET"]

    try:
        router = Router()
        router.add("/{name:int}", ["GET"], testmethod)
        router.finalize()
    except Exception:
        raise AssertionError("Error: test_Router_finalize()")

# Generated at 2022-06-14 07:57:11.828085
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
        path = "/"
        method = "GET"
        host = None
        ret = router._get(path, method, host)
        assert ret is not None
        assert type(ret) is tuple
        assert ret[0] is not None
        assert type(ret[0]) is Route
        assert ret[1] is not None
        assert type(ret[1]) is RouteHandler
    except Exception as e:
        print(e)



# Generated at 2022-06-14 07:57:24.026305
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic.router import Router as Router_
    from sanic.exceptions import SanicException
    from sanic.routing import Route as Route_

    router_ = Router_()
    r = Route_(path="/", methods=["GET"], handler=None)
    r.labels = ("__file_uri__", "__ok__")
    r.name = "name_"
    r.route_uri = "route_uri"
    r.strict = True
    r.unquote = False
    r.ctx.ignore_body = True
    r.ctx.stream = True
    r.ctx.hosts = [None]
    r.ctx.static = False
    # Test with ALLOWED_LABELS, should not raise exception
    router_.dynamic_routes = {"path": r}

# Generated at 2022-06-14 07:57:32.867880
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    
    route = Route(
        path="/<foo>",
        methods=["GET", "POST"],
        handler=lambda x: x,
        name="test",
        host=None,
        strict_slashes=False,
        unquote=True,
        static=False,
        stream=False,
    )
    router.dynamic_routes["test"] = route

    with pytest.raises(SanicException) as excinfo:
        router.finalize()
    assert "Invalid route: " in str(excinfo.value)

# Generated at 2022-06-14 07:57:34.814572
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.name == 'router'

# Generated at 2022-06-14 07:57:35.312611
# Unit test for constructor of class Router
def test_Router():
    router = Router()

# Generated at 2022-06-14 07:57:39.047166
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 07:57:42.313379
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert (router.DEFAULT_METHOD == "GET")
    assert (router.ALLOWED_METHODS == HTTP_METHODS)



# Generated at 2022-06-14 07:58:02.161137
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Create a route with an invalid parameter name
    class InvalidRouter(Router):
        def __init__(self):
            super().__init__()
            def handler(request, __file_uri__): pass
            self.add("/", methods=["GET"], handler=handler)

    # Test for the SanicException
    try:
        InvalidRouter().finalize()
        assert False
    except SanicException as e:
        assert e.args[0] == "Invalid route: <Route / GET>." \
                            " Parameter names cannot use '__'."

# Generated at 2022-06-14 07:58:03.558486
# Unit test for constructor of class Router
def test_Router():
    class RouterTest(Router):
        pass
    router = RouterTest()
    assert router.ctx.app is None

# Generated at 2022-06-14 07:58:07.256208
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert not router.routes
    assert not router.dynamic_routes
    assert not router.static_routes
    assert not router.name_index



# Generated at 2022-06-14 07:58:09.094521
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx is None
    assert not router.routes

# Generated at 2022-06-14 07:58:11.322054
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 07:58:14.731806
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    r.setup_routes(
        {}, [], [], [], [], [],
        False, False, False, False, False,
        False, False, False
    )

# Generated at 2022-06-14 07:58:16.942604
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router != None
    assert router is not None


# Generated at 2022-06-14 07:58:19.142694
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx is not None


# Generated at 2022-06-14 07:58:20.632684
# Unit test for constructor of class Router
def test_Router():
    router=Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:58:28.327050
# Unit test for method finalize of class Router
def test_Router_finalize():
    def f(request):
        pass

    r = Router()
    route = r.add("/<__file_uri__>", ["GET", "POST"], f)
    r.finalize()
    assert r.routes_dynamic["/<__file_uri__>"].handler == f

if __name__ == "__main__":
    test_Router_finalize()

# Generated at 2022-06-14 07:58:54.403047
# Unit test for constructor of class Router
def test_Router():
    test_Router = Router(None)
    assert isinstance(test_Router, Router)

# Generated at 2022-06-14 07:58:55.861758
# Unit test for constructor of class Router
def test_Router():
    assert type(Router()) is Router


# Generated at 2022-06-14 07:58:57.787393
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)



# Generated at 2022-06-14 07:59:10.930606
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.views import HTTPMethodView
    from sanic.exceptions import SanicException
    from sanic.request import Request
    
    class MyView(HTTPMethodView):
        def get(self, request, *args, **kwargs):
            pass
    view = MyView.as_view()
    
    router = Router()
    router.add(
        uri='/',
        methods=['GET'],
        handler=view,
    )
    router.finalize()
    

# Generated at 2022-06-14 07:59:13.987212
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.get("/asdf","GET","asdf") == None


# test add with all parameters

# Generated at 2022-06-14 07:59:17.028598
# Unit test for constructor of class Router
def test_Router():
    router=Router()
    assert isinstance(router, Router)
    #assert isinstance(router, BaseRouter)

# Generated at 2022-06-14 07:59:26.890267
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route('/test/<name>/<__file_uri__>', None, ['GET'], None)
    try:
        router.dynamic_routes = {'/test/<name>/<__file_uri__>': route}
        router.finalize()
    except Exception as e:
        assert str(e) == "Invalid route: Route('/test/<name>/<__file_uri__>', None, ['GET'], None). Parameter names cannot use '__'."

test_Router_finalize()

# Generated at 2022-06-14 07:59:32.183967
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    with pytest.raises(SanicException):
        router.add(
            uri='/',
            methods='GET',
            handler='handler',
            host='host',
            strict_slashes=False,
            stream=False,
            ignore_body=False,
            version=None,
            name='name',
            unquote=False,
            static=False,
        )

# Generated at 2022-06-14 07:59:38.723675
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        r = Router()
        r.add(
            uri="/foo/<bar:test>/<test2>",
            methods=["GET"],
            handler=None,
            static=False,
        )
    except SanicException:
        pass
    else:
        assert 0, "The sanic exception didn't raise"

# Generated at 2022-06-14 07:59:48.568641
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    # Init an app mock
    app = MagicMock()
    app.router = router

    router.add_regex_route(
        path = '/<param:re:\\w+>',
        methods = ['GET'],
        handler = 'handler.handle',
        name = 'sample-route'
    )
    router.finalize(app)
    assert router.routes['sample-route'].labels == ['param']
    with pytest.raises(SanicException):
        router.add_regex_route(
            path = '/<param:re:\\w+>',
            methods = ['GET'],
            handler = 'handler.handle',
            name = 'sample-route'
        )
        router.finalize(app)


# Generated at 2022-06-14 08:00:46.050076
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route("/", None, ["GET"])
    route.labels = ["hello"]
    router.dynamic_routes = {0: route}
    try:
        router.finalize()
    except Exception as e:
        assert str(e) == "Invalid route: Route(path='/', methods=['GET'], " \
            "handler=None, name=None, host=None, strict=False, unquote=False). " \
            "Parameter names cannot use '__'."

    route.labels = ["__hello__"]

# Generated at 2022-06-14 08:00:51.940715
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes["sanic.test"] = Route(
        path="sanic.test",
        handler=object,
        methods=["GET"],
        name=None,
        strict=False,
        ctx=router.ctx,
        labels=["sanic", "test"],
        unquote=False,
    )

    with pytest.raises(SanicException, match=r'Invalid route.*'):
        router.finalize()

# Generated at 2022-06-14 08:00:58.616483
# Unit test for constructor of class Router
def test_Router():
    import pytest
    router=Router()
    with pytest.raises(Exception):
        router.finalize()

    assert router.DEFAULT_METHOD == "GET"
    assert len(router.ALLOWED_METHODS) == len(HTTP_METHODS)
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:00:59.829658
# Unit test for method add of class Router
def test_Router_add():
    pass



# Generated at 2022-06-14 08:01:01.116007
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router) == True

# Generated at 2022-06-14 08:01:12.833193
# Unit test for constructor of class Router
def test_Router():
    """Test the constructor of class Router"""
    router = Router()
    assert router
    assert router.routes == {}
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.static_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}
    assert router.ctx.router == router
    assert router.ctx.app is None
    assert not router.ctx.static
    assert not router.ctx.stream
    assert not router.ctx.ignore_body
    assert not router.ctx.strict
    assert not router.ctx.unquote
    assert router.DEFAULT_METHOD == 'GET'
   

# Generated at 2022-06-14 08:01:22.846336
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    try:
        router.add(r'/a/{__file_uri__}', ["GET"], None)
    except:
        raise AssertionError("Router.add() not working as expected.")
    try:
        router.add(r'/a/{__foo__}', ["GET"], None)
        raise AssertionError("Router.add() not working as expected.")
    except SanicException as ex:
        assert ex.__str__().startswith("Invalid route: ")

# Check if Router.add can be called correctly
Router().add(r'/a/{__file_uri__}', ["GET"], None)

# Generated at 2022-06-14 08:01:31.481859
# Unit test for method finalize of class Router
def test_Router_finalize():
    """
    Unit test for method finalize of class Router
    """
    nr.assert_equal(
        [route.path for route in Router().finalize().dynamic_routes.values()],
        [],
    )
    nr.assert_equal(
        [
            route.path
            for route in Router().add("/", ["GET"], 1).finalize().dynamic_routes.values()
        ],
        [""],
    )
    nr.assert_equal(
        [
            route.path
            for route in Router().add("/route", ["GET"], 1).finalize().dynamic_routes.values()
        ],
        ["/route"],
    )

# Generated at 2022-06-14 08:01:43.207548
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes = {
        'route': Route(
            path='/',
            handler='handler',
            methods=['GET', 'POST', 'OPTIONS'],
            ctx={},
            version=None,
            name='name',
            strict=False,
            unquote=False,
            host=None,
            labels={'__file_uri__': 'categories/[category]'}
        )
    }
    router.finalize()

    # Assert dynamic_routes is unchanged

# Generated at 2022-06-14 08:01:46.051616
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router
    assert len(router.routes) == 0


# Generated at 2022-06-14 08:03:15.946669
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DYNAMIC_ROUTES_PREFIX == '__sanic_dynamic_route:'
    assert r.STATIC_ROUTES_PREFIX == '__sanic_static:'
    assert Router.DYNAMIC_ROUTES_PREFIX == '__sanic_dynamic_route:'
    assert Router.STATIC_ROUTES_PREFIX == '__sanic_static:'



# Generated at 2022-06-14 08:03:27.689833
# Unit test for method finalize of class Router
def test_Router_finalize():
    class FakeApp:
        @staticmethod
        def _generate_name(view_name):
            return f'{view_name}_gen'

    fake_app = FakeApp()
    fake_ctx = object()
    fake_routes = [
        Route(
            fake_ctx,
            path="fake",
            handler=object,
            methods={"GET"},
            name="fake_route",
            strict=False,
            unquote=False,
        ),
        Route(
            fake_ctx,
            path="fake_gen",
            handler=object,
            methods={"GET"},
            name="fake_route",
            strict=False,
            unquote=False,
        ),
    ]
    for r in fake_routes:
        r.ctx.hosts = []
        r.ctx

# Generated at 2022-06-14 08:03:40.470403
# Unit test for method finalize of class Router
def test_Router_finalize():
    import sys
    import os
    import pytest
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    myPath = os.path.join(THIS_FOLDER, '../../')
    sys.path.insert(0, myPath)
    from sanic_routing.router import Router
    from sanic_routing import Route

    @Route("/", methods="GET")
    async def test_handler(request):  # type: ignore
        pass

    router = Router(None)

# Generated at 2022-06-14 08:03:51.640948
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router
    from sanic.constants import ROUTE_STATIC, ROUTE_DYNAMIC, ROUTE_REGEX
    from sanic_routing.route import Route
    from sanic.constants import HTTP_METHODS

    router = Router()
    router.ctx = object()
    router.routes = {
        ROUTE_STATIC: {},
        ROUTE_DYNAMIC: {},
        ROUTE_REGEX: {},
    }
    router.dynamic_routes = {}
    router.name_index = {}
    router.regex_routes = {}
    router.static_routes = {}


# Generated at 2022-06-14 08:03:57.193539
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']
    assert router._get == router.get
    assert router.add == router.ad

# Generated at 2022-06-14 08:04:07.383898
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(app=None)

    route = Route(
        path=None,
        handler=None,
        methods=None,
        name=None,
        strict=False,
        unquote=False
    )

    route.ctx.labels = {'__file_uri__': 'sanic.py'}

    router.dynamic_routes[route.ctx.name] = route

    assert router.finalize() is None

    route.ctx.labels = {'__file_uri__': 'sanic.py', '__test__': 'sanic.py'}

    router.dynamic_routes[route.ctx.name] = route

    assert router.finalize() is not None

# Generated at 2022-06-14 08:04:16.273158
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route_1 = Route(
        ("GET", "*", "test_1"), None,
        [("test_1", None)], {"test_1": None},
    )
    route_2 = Route(
        ("GET", "*", "test_2"), None,
        [("__test_2", None)], {"__test_2": None},
    )
    router.dynamic_routes = {
        "test_1": route_1,
        "test_2": route_2,
    }
    router.finalize()
    assert router.dynamic_routes == {
        "test_1": route_1,
    }

# Generated at 2022-06-14 08:04:17.342658
# Unit test for constructor of class Router
def test_Router():
    router = Router()


# Generated at 2022-06-14 08:04:24.339393
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.dynamic_routes == dict()
    assert router.static_routes == dict()
    assert router.regex_routes == dict()
    assert router.ctx.app == None
    assert router.name_index == dict()


# Generated at 2022-06-14 08:04:34.520007
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.views import CompositionView
    from sanic_routing.route import Route
