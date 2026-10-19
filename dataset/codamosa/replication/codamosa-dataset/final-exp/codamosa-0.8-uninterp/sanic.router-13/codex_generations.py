

# Generated at 2022-06-14 07:56:01.411622
# Unit test for constructor of class Router
def test_Router():
    test_object = Router()
    assert not test_object.routes
    assert not test_object.static_routes
    assert not test_object.dynamic_routes


# Generated at 2022-06-14 07:56:08.551013
# Unit test for constructor of class Router
def test_Router():
    # Unit test for constructor of class Router
    router = Router()
    assert isinstance(router, Router), f"{router} not instance of Router"
    assert not isinstance(router, BaseRouter)
    assert router.routes_all
    assert router.routes_static
    assert router.routes_dynamic
    assert router.routes_regex


# Generated at 2022-06-14 07:56:12.733275
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(app=None)
    for route in router.dynamic_routes.values():
        assert not route.labels

# Generated at 2022-06-14 07:56:14.914331
# Unit test for method finalize of class Router
def test_Router_finalize():
    from model_bakery import baker
    baker.generate_recipe('sanic.routing.route')
    # TODO: test this method

# Generated at 2022-06-14 07:56:24.380290
# Unit test for method finalize of class Router
def test_Router_finalize():  # type: ignore
    r = Router()
    r.add(uri="/api/v1/path_1/", methods=["GET", "POST", "OPTIONS"], handler=None)
    r.add(uri="/api/v1/path_2/", methods=["GET", "POST", "OPTIONS"], handler=None)
    r.add(uri="/api/v1/path_3/", methods=["GET", "POST", "OPTIONS"], handler=None)
    assert isinstance(r, Router)



# Generated at 2022-06-14 07:56:31.144755
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert (
        router.DEFAULT_METHOD == "GET"
        and router.ALLOWED_METHODS == HTTP_METHODS
    )

    router_1 = Router(
        DEFAULT_METHOD="POST",
        ALLOWED_METHODS=["POST", "GET"],
    )
    assert router_1.DEFAULT_METHOD == "POST" and router_1.ALLOWED_METHODS == ["POST", "GET"]

# Generated at 2022-06-14 07:56:37.111679
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.path_index == {}
    assert router.method_index == {}
    assert router.id_index == {}
    assert router.name_index == {}
    assert router.regex_routes == []
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.routes == {}


# Generated at 2022-06-14 07:56:42.764442
# Unit test for constructor of class Router
def test_Router():
    router = Router(prefix="")

    assert router.static_routes == {}
    assert router.regex_routes == []
    assert router.dynamic_routes == {}
    assert router.name_index == {}


# Generated at 2022-06-14 07:56:46.346619
# Unit test for constructor of class Router
def test_Router():
    """
    This unit test is for the constructor of class Router
    """
    assert Router().DEFAULT_METHOD == "GET"
    assert len(Router().ALLOWED_METHODS) == 10

# Generated at 2022-06-14 07:56:58.748095
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic import Sanic
    from sanic.response import text
    from sanic.router import Router as SanicRouter
    from mock import MagicMock

    app = Sanic("test_finalize")

    @app.route("/test/")
    async def handler(_):
        return text("OK")

    app.router = SanicRouter(finalize_routes=True)
    app.router.add_route = MagicMock()

    app.finalize_routes()
    app.router.add_route.assert_called_with(
        "OPTIONS",
        "/test/",
        app.options,
        name=None,
        strict_slashes=None
    )

# Generated at 2022-06-14 07:57:10.490559
# Unit test for constructor of class Router
def test_Router():  # type: ignore
    router = Router()

    assert router.routes == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.routes_static == set()

# Generated at 2022-06-14 07:57:17.499703
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route_to_test = Route('test', 'route', [], [], None, None, None)
    router.dynamic_routes = {'test': route_to_test}
    router.finalize()
    assert router.dynamic_routes is not None
    assert route_to_test.labels is not None



# Generated at 2022-06-14 07:57:24.394416
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    # check that not error thrown if no route passed
    router.finalize()

    route = Route('/', lambda x: x)
    # check that not error thrown if route is valid
    router.finalize([route])

    route = Route('/<id>', lambda x: x)
    # check that not error thrown if route is valid
    router.finalize([route])

    route = Route('/<__id>', lambda x: x)
    with pytest.raises(SanicException):
        router.finalize([route])

# Generated at 2022-06-14 07:57:30.698931
# Unit test for method finalize of class Router
def test_Router_finalize():
    from _pytest import assert_raises
    from sanic import Sanic

    app = Sanic('test_Router_finalize')
    app.router = Router(app)

    # assert_raises(test_case): test if the test_case raises an exception
    # assert_raises(SanicException, app.router.finalize)
    


# Generated at 2022-06-14 07:57:34.538071
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

if __name__ == "__main__":
    router = Router()
    print(router)

# Generated at 2022-06-14 07:57:36.472425
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 07:57:37.906589
# Unit test for constructor of class Router
def test_Router():
    assert Router(None).ctx==None

# Generated at 2022-06-14 07:57:39.175392
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert type(router) == Router

# Generated at 2022-06-14 07:57:45.869926
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ALLOWED_METHODS == router.DEFAULT_METHOD == router.routes == router.routes_static == router.routes_dynamic == router.routes_regex == router.routes_all == router.get == router.find_route_by_view_name == router.add == router.finalize == HTTP_METHODS == 'GET'

test_Router()

# Generated at 2022-06-14 07:57:48.060928
# Unit test for constructor of class Router
def test_Router():
    class TestRouter(Router):
        pass
    assert TestRouter.DEFAULT_METHOD == "GET"
    assert TestRouter.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:58:03.008408
# Unit test for method finalize of class Router
def test_Router_finalize():
    from prefect.utilities.sanic import router
    from prefect.utilities.exceptions import SanicException
    from prefect.utilities.sanic.router import Router
    from prefect.utilities.sanic.constants import HTTP_METHODS

    router = Router()
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.routes_all == {}
    # test add routes with hosts, version, route handler
    router.add(
        "/",
        ["GET", "POST"],
        lambda: None,
        host="example.com",
        static=True,
        version="1.1",
        name="test",
    )

# Generated at 2022-06-14 07:58:13.813309
# Unit test for method add of class Router
def test_Router_add():
    uri = '/'
    methods = 'get'
    handler = 'handler'
    host = 'host'
    strict_slashes = True
    stream = False
    ignore_body = False
    version = 'version'
    name = 'name'
    unquote = True

    router = Router()
    router.add(
        uri=uri,
        methods=methods,
        handler=handler,
        host=host,
        strict_slashes=strict_slashes,
        stream=stream,
        ignore_body=ignore_body,
        version=version,
        name=name,
        unquote=unquote
    )
    return router

# Generated at 2022-06-14 07:58:17.422337
# Unit test for constructor of class Router
def test_Router():
    inner: Router = Router(None, {})
    # assert that the inner is of type Router
    assert isinstance(inner, Router)
    # assert that a return value exists
    assert inner is not None


# Generated at 2022-06-14 07:58:21.720324
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route("/home/<name>", handler=None, name="hello", labels={"__a__": "a"})
    router = Router()
    router.dynamic_routes["/home/<name>"] = route
    try:
        router.finalize()
    except:
        pass
    else:
        raise AssertionError("test_Router_finalize failed")

# Generated at 2022-06-14 07:58:25.276663
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:58:31.007880
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    setattr(router, 'dynamic_routes', {'hello': "path/index.html"})
    try:
        router.finalize()
    except SanicException as e:
        assert "Invalid route: path/index.html. Parameter names cannot use '__'."

# Generated at 2022-06-14 07:58:37.014553
# Unit test for constructor of class Router
def test_Router():
    # Parameters
    app = None
    print("test Router\n")

    try:
        # Objet Router
        router = Router(app)
        print("Router:", router)
    except Exception as inst:
        print("Error while loading Router: " + str(inst))

    print("End of test Router\n")

# Generated at 2022-06-14 07:58:50.949449
# Unit test for method finalize of class Router
def test_Router_finalize():
    def check_valid_route(route):
        assert hasattr(route, '_methods')
        assert hasattr(route, '_path')
        assert hasattr(route, '_hosts')
        assert hasattr(route, '_host_regex')
        assert hasattr(route, '_dynamic_params')
    
    router = Router()
    # first try a route without dynamic_params
    uri = 'uri'
    methods = ["GET", "POST", "OPTIONS"]
    handler = RouteHandler
    host = 'host'
    route = router.add(
        uri,
        methods,
        handler,
        host
    ) 
    check_valid_route(route)

    # second try a route with dynamic_params
    uri = '/uri/<var>'
    route = router

# Generated at 2022-06-14 07:58:55.932097
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    a = Router()
    a.add('/', ['GET'], None)
    with pytest.raises( SanicException ) as excinfo:
        a.finalize()
    assert 'Invalid route' in str( excinfo.value )

# Generated at 2022-06-14 07:59:00.709502
# Unit test for constructor of class Router
def test_Router():
    import unittest

    class TestRouter(unittest.TestCase):
        def setUp(self):
            self.router = Router()

        def test_run(self):
            self.assertIsInstance(self.router, Router)

    unittest.main()

# Generated at 2022-06-14 07:59:10.532726
# Unit test for method finalize of class Router
def test_Router_finalize():
    ROUTER_CACHE_SIZE=1024
    ALLOWED_LABELS=("__file_uri__",)
    class MockRouter(Router):
        pass
    mock_router = MockRouter()
    with pytest.raises(SanicException):
        mock_router.dynamic_routes = {"test_route": "test_route"}
        mock_router.finalize()


# Generated at 2022-06-14 07:59:24.576721
# Unit test for constructor of class Router
def test_Router():
    assert router.ALLOWED_METHODS[0] == 'DELETE' 
    assert router.ALLOWED_METHODS[7] == 'PATCH' 
    assert router.ALLOWED_METHODS[10] == 'TRACE' 
    assert router.ALLOWED_METHODS[14] == 'HEAD' 
    assert router.ALLOWED_METHODS[15] == 'OPTIONS' 
    assert router.ALLOWED_METHODS[18] == 'CONNECT' 
    assert router.ALLOWED_METHODS[19] == 'PURGE' 
    assert router.ALLOWED_METHODS[20] == 'LOCK' 
    assert router.ALLOWED_METHODS[21] == 'UNLOCK' 
    assert router.ALLOWED_METHODS[22] == 'MOVE'

# Generated at 2022-06-14 07:59:32.565948
# Unit test for method finalize of class Router
def test_Router_finalize():
    def handler(request):
        return text("OK")
    uri = '/'
    methods = ['GET']
    router = Router()
    router.add(uri, methods, handler)
    assert router.routes_all == {
        uri: [Route(uri, methods, handler,
                    method_map={'GET': handler},
                    strict=False, name=None, unquote=False,
                    ctx=Route.Context(ignore_body=False,
                                      stream=False,
                                      hosts=None,
                                      static=False))]
    }
    # normal case
    router.finalize()

# Generated at 2022-06-14 07:59:44.719880
# Unit test for method finalize of class Router
def test_Router_finalize():
    from unittest import TestCase, mock

    class TestRouterFinalize(TestCase):
        def test_routes_are_valid(self):
            route = mock.Mock()
            route.labels = [True, False]
            router = Router()
            router.dynamic_routes.values = lambda: [route]
            router.finalize()

        def test_routes_are_not_valid(self):
            route = mock.Mock()
            route.labels = ["__test__"]
            router = Router()
            router.dynamic_routes.values = lambda: [route]
            with self.assertRaises(SanicException):
                router.finalize()

    TestRouterFinalize().run()

# Generated at 2022-06-14 07:59:58.305376
# Unit test for method finalize of class Router
def test_Router_finalize():
    from typing import List, Tuple
    from sanic.router import Router
    from sanic_routing.route import Route
    from sanic.exceptions import SanicException
    
    # case 1: pass
    dynamic_routes: List[Tuple[Route, str]] = []
    router = Router()
    router.dynamic_routes = dynamic_routes
    router.finalize()

    # case 2: raise

# Generated at 2022-06-14 08:00:02.746051
# Unit test for constructor of class Router
def test_Router():
    router = Router(ctx={})
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.ctx == {}


# Generated at 2022-06-14 08:00:14.303635
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.models.handler_types import RouteHandler
    from sanic.exceptions import SanicException
    r = Router()
    r.add(uri="/test/{__test_var}",methods=["GET"],handler=RouteHandler(None,None,None),host=None,strict_slashes=False,stream=False,ignore_body=False,version=None,name=None,unquote=False)
    try:
        r.finalize()
    except SanicException as err:
        print(err)
    else:
        assert False



# Generated at 2022-06-14 08:00:25.192793
# Unit test for method finalize of class Router
def test_Router_finalize():
    import unittest

    class A(unittest.TestCase):
        def test_01(self):
            router = Router()
            try:
                router.finalize()
            except SanicException:
                self.assertTrue(True)
            else:
                self.assertTrue(False)

        def test_02(self):
            router = Router()
            router.add(uri="/test", methods=["GET"], handler=None)
            router.finalize()
            self.assertTrue(True)
            
        def test_03(self):
            router = Router()
            router.add(uri="/test", methods=["GET"], handler=None)
            router.add(uri="/test2/<__id>", methods=["GET"], handler=None)
            router.finalize()
            self.assertTrue(True)

# Generated at 2022-06-14 08:00:26.948684
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:00:31.227200
# Unit test for constructor of class Router
def test_Router():
    try:
        Router()
    except AssertionError:
        # do nothing
        print("Rerun the failed test success.")  
        return True

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 08:00:39.820503
# Unit test for method finalize of class Router
def test_Router_finalize():
    import click
    import click.testing

    runner = click.testing.CliRunner()

    result = runner.invoke(
        cli,
        [
            "run",
            "tests/apps/router_test.py",
            "--quiet",
            "--log-level=warning",
            "-h127.0.0.1",
        ],
    )

    assert result.exit_code == 1
    assert "Invalid route" in result.output

# Generated at 2022-06-14 08:00:42.306059
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    with pytest.raises(SanicException, match="Invalid route"):
        r.finalize()

# Generated at 2022-06-14 08:00:44.914599
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    # assert isinstance(router, Router)


# Generated at 2022-06-14 08:00:48.582217
# Unit test for constructor of class Router
def test_Router():
    class DummyRouter(Router):
        def __init__(self):
            super().__init__()

    router = DummyRouter()
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:00:50.356742
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:00:51.484321
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 08:00:54.512269
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.resolve
    assert router.asgi

# Generated at 2022-06-14 08:00:55.395183
# Unit test for constructor of class Router
def test_Router():
    assert Router()

# Generated at 2022-06-14 08:00:58.074589
# Unit test for constructor of class Router
def test_Router():
    """
    Test function `test_Router` for class Router
    """
    assert isinstance(Router(), Router)

    return True

# Generated at 2022-06-14 08:00:59.766435
# Unit test for constructor of class Router
def test_Router():
    r1 = Router()
    assert isinstance(r1, Router)

# Generated at 2022-06-14 08:01:16.149186
# Unit test for constructor of class Router
def test_Router():
    from sanic import Sanic
    from sanic.response import text

    app = Sanic()
    router = Router(app)

    @app.route("/")
    async def handler(request):
        return text("OK")

    request, response = app.test_client.get("/")
    assert response.text == 'OK'

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 08:01:18.083436
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:01:22.840370
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.routes == {}
    assert r.static_routes == {}
    assert r.dynamic_routes == {}
    assert r.regex_routes == {}


# Generated at 2022-06-14 08:01:26.101284
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None
    assert type(router) == Router


# Generated at 2022-06-14 08:01:34.154268
# Unit test for method add of class Router
def test_Router_add():
  router = Router()
  def handler():
    pass

  path = "/items"
  methods = ["GET", "POST"]
  strict_slashes = False
  stream = False
  ignore_body = False
  version = None
  name = None
  route = router.add(path, methods, handler, "localhost", strict_slashes, stream, ignore_body, version, name)
  assert type(route) == Route

# Generated at 2022-06-14 08:01:44.410892
# Unit test for constructor of class Router
def test_Router():
    # Create an object of class Sanic
    app = Sanic()

    # Create an object of class Router
    router = Router()

    # Create a name of the route as string
    name_of_route = "test_router"

    # Create the whole path of the route as string
    path_of_route = "test_router"

    # Create a route handler as function
    def route_handler(request):
        # Create a return value as dict
        return_value = dict()

        # Add the entry name to the return value as string
        return_value["name"] = request.args.get("name", None)

        # Return the return value as response
        return response.json(return_value)

    # Add the route handler for the given path to the router

# Generated at 2022-06-14 08:01:46.762029
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)



# Generated at 2022-06-14 08:01:53.194158
# Unit test for constructor of class Router
def test_Router():

    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS
    assert r.routes_all == {}
    assert r.routes_static == {}
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}

# Generated at 2022-06-14 08:01:58.695232
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE']


# Generated at 2022-06-14 08:02:01.008725
# Unit test for constructor of class Router
def test_Router():

    router = Router()
    assert router.routes_dynamic == {}
    assert router.routes_static  == {}


# Generated at 2022-06-14 08:02:31.018706
# Unit test for method add of class Router
def test_Router_add():
    router: Router = Router(None)
    uri:str = '/'
    methods: tuple = ('GET','POST','DELETE','OPTION','PUT','HEAD','CONNECT','TRACE')
    handler: RouteHandler = {}
    host: Optional[Union[str, Iterable[str]]] = '0.0.0.0'
    strict_slashes: bool = True
    stream: bool = True
    ignore_body: bool = True
    version: Union[str, float, int] = 0
    name: Optional[str] = None
    unquote: bool = False
    static: bool = False
    result = router.add(
        uri, methods, handler,
        host, strict_slashes,
        stream, ignore_body,
        version, name, unquote, static)

# Generated at 2022-06-14 08:02:32.552054
# Unit test for constructor of class Router
def test_Router():
    assert Router(app=app)



# Generated at 2022-06-14 08:02:35.157417
# Unit test for constructor of class Router
def test_Router():
    rout = Router()
    assert isinstance(rout, Router)

if __name__ == '__main__':
    test_Router()

# Generated at 2022-06-14 08:02:39.340827
# Unit test for constructor of class Router
def test_Router():
    try:
        # Initialize an instance of the class
        router = Router()
    except Exception as inst:
        print(inst)
        assert 0, "constructor of class Router not working."



# Generated at 2022-06-14 08:02:48.119420
# Unit test for constructor of class Router
def test_Router():
    router_test = Router()
    router_test.DEFAULT_METHOD, router_test.ALLOWED_METHODS, router_test.routing_table, router_test.routes
    router_test.static_prefixes, router_test.static_routes
    router_test.dynamic_routes, router_test.regex_routes
    router_test.name_index, router_test.id_index


# Generated at 2022-06-14 08:02:49.801831
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:02:55.858723
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ['HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE']



# Generated at 2022-06-14 08:02:58.131596
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:02:58.893621
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 08:03:03.986621
# Unit test for constructor of class Router
def test_Router():
    # Constructor of class Router
    router = Router()
    assert len(router.static_routes) == 0
    assert len(router.dynamic_routes) == 0
    assert len(router.regex_routes) == 0


# Generated at 2022-06-14 08:03:44.109768
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == []
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == []
    assert router.name_index == {}
    assert router.path_index == {}
    assert router.ctx is None


# Generated at 2022-06-14 08:03:45.408824
# Unit test for constructor of class Router
def test_Router():
  # Test the constructor of class Router
  Router()

# Generated at 2022-06-14 08:03:47.029370
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert(r.__class__ == Router)

# Generated at 2022-06-14 08:03:49.956131
# Unit test for constructor of class Router
def test_Router():
    router = Router("hello", "world")
    assert isinstance(router, Router)


# Generated at 2022-06-14 08:03:52.700677
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
    except Exception as e:
        assert False, "Exception occurred: {}".format(e)

# Generated at 2022-06-14 08:03:57.725552
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert router
    assert router.routes == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.get('/', 'GET', 'localhost') == None

# Generated at 2022-06-14 08:03:58.918288
# Unit test for constructor of class Router
def test_Router():
    assert Router(app=None).__class__==Router

# Generated at 2022-06-14 08:04:00.147718
# Unit test for constructor of class Router
def test_Router():
    x = Router()
    assert x is not None

# Generated at 2022-06-14 08:04:07.355305
# Unit test for method add of class Router
def test_Router_add():
    from sanic.sanic import Sanic
    from sanic.response import json

    app = Sanic(__name__)
    router = app.router

    async def handler(request):
        return json({})

    router.add(uri="", methods=["GET"], handler=handler)

if __name__ == "__main__":
    test_Router_add()

# Generated at 2022-06-14 08:04:08.879091
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

test_Router()

# Generated at 2022-06-14 08:05:20.500044
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert(isinstance(router.routes_all, dict)==True)
    assert(isinstance(router.routes_static, dict)==True)
    assert(isinstance(router.routes_dynamic, dict)==True)
    assert(isinstance(router.routes_regex, dict)==True)


# Generated at 2022-06-14 08:05:26.524115
# Unit test for constructor of class Router
def test_Router():
    app = None
    router = Router()
    assert router.routes_all == []
    assert router.routes_static == []
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.ctx == {}

# Generated at 2022-06-14 08:05:31.752242
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router.routes_all, list)
    assert isinstance(router.routes_static, list)
    assert isinstance(router.routes_dynamic, list)
    assert isinstance(router.routes_regex, list)

# Generated at 2022-06-14 08:05:38.744780
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}
    assert router.name_index == {}
    assert router.dynamic_paths == set()
    assert router.dynamic_routes_cache_size == 1024


# Generated at 2022-06-14 08:05:45.090375
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.root is None
    assert router.regex_routes == []
    assert router.static_routes == []
    assert router.dynamic_routes == []
    assert router.name_index == {}


# Generated at 2022-06-14 08:05:53.689529
# Unit test for method add of class Router
def test_Router_add():
    uri = "url"
    methods = list('HTTPMethods')
    handler = ""
    host = "host"
    strict_slashes = False
    stream = False
    ignore_body = False
    version = "version"
    name = "name"
    unquote = False
    static = False

    router = Router()
    router.add(uri=uri,
               methods=methods,
               handler=handler,
               host=host,
               strict_slashes=strict_slashes,
               stream=stream,
               ignore_body=ignore_body,
               version=version,
               name=name,
               unquote=unquote,
               static=static)
