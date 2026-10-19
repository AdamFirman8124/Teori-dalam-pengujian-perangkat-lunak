

# Generated at 2022-06-14 07:55:49.936613
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router
    # print(router)

# Generated at 2022-06-14 07:55:52.589944
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS

if __name__ == "__main__":
    test_Router()

# Generated at 2022-06-14 07:55:55.629556
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert isinstance(router, BaseRouter)


# Generated at 2022-06-14 07:56:03.798540
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.strict_slashes == True
    assert router.routes == []
    assert router.dynamic_routes == {}
    assert router.static_routes == {}
    assert router.regex_routes == []
    assert router.name_index == {}
    assert router.ctx == None


# Generated at 2022-06-14 07:56:08.376994
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.DEFAULT_METHOD
    assert router.DEFAULT_METHOD == 'GET'
    router.ALLOWED_METHODS
    assert router.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 07:56:18.348748
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router._get.__doc__ == Router.get.__doc__
    assert router._get.__name__ == "_get"
    assert router._get.__annotations__ == Router.get.__annotations__
    assert router.add.__doc__ == Router.add.__doc__
    assert router.add.__name__ == "add"
    assert router.add.__annotations__ == Router.add.__annotations__
    assert router.find_route_by_view_name.__doc__ == Router.find_route_by_view_name.__doc__

# Generated at 2022-06-14 07:56:23.648373
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route = Route(path="", methods=["GET"], handler=None)
    route.labels.append("__file_uri__")
    router.dynamic_routes.update({route.uuid: route})
    router.finalize()



# Generated at 2022-06-14 07:56:35.369682
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    route_1 = Route(
        "http",
        path='/test?<name>',
        handler=None,
        handler_name='Handler name',
        methods=['GET'],
        name='e.1'
    )
    route_2 = Route(
        "http",
        path='/test?<__name>',
        handler=None,
        handler_name='Handler name',
        methods=['GET'],
        name='e.2'
    )
    route_3 = Route(
        "http",
        path='/test?<__file_uri__>',
        handler=None,
        handler_name='Handler name',
        methods=['GET'],
        name='e.3'
    )


# Generated at 2022-06-14 07:56:40.563473
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.add('hello', 'POST', lambda: None)
        router.finalize()
    except SanicException as e:
        assert "Invalid route: " not in str(e)

# Generated at 2022-06-14 07:56:41.802999
# Unit test for constructor of class Router
def test_Router():
    BaseRouter()


# Generated at 2022-06-14 07:56:50.874678
# Unit test for constructor of class Router
def test_Router():
    assert Router().routes_all == {}
    assert Router().routes_static == {}
    assert Router().routes_dynamic == {}
    assert Router().routes_regex == {}
    assert Router().name_index == {}


# Generated at 2022-06-14 07:56:54.517676
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:56:55.646545
# Unit test for constructor of class Router
def test_Router():
    assert Router()


# Generated at 2022-06-14 07:57:01.254625
# Unit test for method add of class Router
def test_Router_add():
    # Set up
    uri = 'uri'
    methods= ['GET']
    handler='handler'
    host='host'
    strict_slashes=False
    stream=False
    ignore_body=False
    version=None
    name='name'
    unquote=False
    static=False

    # Exercise

    # Verify
    pass # TODO: Implement test

# Generated at 2022-06-14 07:57:09.336776
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert len(router.routes) == 0
    assert len(router.routes_all) == 0
    assert len(router.routes_static) == 0
    assert len(router.routes_dynamic) == 0
    assert len(router.routes_regex) == 0
    assert len(router.name_index) == 0



# Generated at 2022-06-14 07:57:22.748096
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from io import StringIO
    from types import ModuleType
    from sanic.router import Router, SanicException
    import re

    #############
    # Variables #
    #############
    test_module: ModuleType = ModuleType(__name__)
    old_stdout = sys.stdout
    captured_stdout = StringIO()
    sys.stdout = captured_stdout

    ###########
    # Methods #
    ###########
    def finalize_by_args() -> None:
        router = Router()
        router.finalize(None)

    def finalize_by_kwargs() -> None:
        router = Router()
        router.finalize(app=None)

    def finalize_by_args_none() -> None:
        router = Router()

# Generated at 2022-06-14 07:57:24.070544
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:57:30.549276
# Unit test for constructor of class Router
def test_Router():
    # test for constructor of class Router
    print('testing for constructor of class Router')
    try:
        router = Router()
    except Exception as e:
        print('ERROR: constructor of class Router failed: ', e)
        print('Failed')
        return
    print('Passed')
    print()


if __name__ == '__main__':
    test_Router()

# Generated at 2022-06-14 07:57:32.741951
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)

# Generated at 2022-06-14 07:57:44.447872
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    # Unit test for method add of class Router
    def test_add():
        router = Router()

        def handler(request: Request, response: Response):
            return response
        router.add('/hello', ['GET'], handler)

    # Unit test for method add of class Router
    def test_find_route_by_view_name():
        router = Router()

        def handler(request: Request, response: Response):
            return response
        router.add('/hello', ['GET'], handler, name='hello')

        route = router.find_route_by_view_name('hello')
        assert route is not None

    test_add()
    test_find_route_by_view_name()

# Generated at 2022-06-14 07:57:55.220617
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.add("/users/<user_id>", ["GET"], None)
    except SanicException:
        pass
    else:
        raise AssertionError("test_Router_finalize: 1")

    try:
        router = Router()
        router.add("/users/<user_id>", ["GET"], None)
    except SanicException:
        pass
    else:
        raise AssertionError("test_Router_finalize: 2")

# Generated at 2022-06-14 07:57:56.881529
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router


# Generated at 2022-06-14 07:57:58.576984
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 07:58:02.900717
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        # https://github.com/huge-success/sanic/issues/1046
        router.dynamic_routes = {
            "__default": []
        }
        router.finalize(app=None, skip_defaults=True)
    except Exception:
        assert False
    assert True

# Generated at 2022-06-14 07:58:12.478754
# Unit test for constructor of class Router
def test_Router():
    """
    unit test for the constructor of class Router
    :return:
    """
    router = Router()
    assert router.ctx is None
    assert router.routes == dict()
    assert router.static_routes == dict()
    assert router.dynamic_routes == dict()
    assert router.regex_routes == dict()
    assert router.name_index == dict()
    assert router.name_regex_index == dict()
    assert router.regex_index == dict()
    assert router.custom_index == dict()



# Generated at 2022-06-14 07:58:16.940569
# Unit test for constructor of class Router
def test_Router():
    uri = "/"
    methods = ["GET"]
    host = ["localhost"]
    handler = {}
    route = Router()
    route.add(
        uri=uri,
        methods=methods,
        handler=handler,
        host=host,
    )

# Generated at 2022-06-14 07:58:26.448450
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.dynamic_routes[0] = Route(router, "a/<b>/<c>", lambda *a: None,
                                     False, False, False, False, False, False)
    router.dynamic_routes[1] = Route(router, "a/<b>/<c>", lambda *a: None,
                                     False, False, False, False, False, False)
    router.dynamic_routes[2] = Route(router, "a/<b>/<c>", lambda *a: None,
                                     False, False, False, False, False, False)

# Generated at 2022-06-14 07:58:36.132373
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    route = Router()
    newRouter = route.add(
        uri="/",
        methods=['GET'],
        handler=None
    )
    assert isinstance(newRouter, list)
    assert isinstance(newRouter[0], Route)
    routeDict = {'/': newRouter[0]}
    router = Router(routeDict)
    router.finalize()
    assert isinstance(router, Router)


# Generated at 2022-06-14 07:58:40.884953
# Unit test for constructor of class Router
def test_Router():
    router_test = Router()
    expected_result = {
        "host": None,
        "handlers": {},
        "name_index": {},
        "static_routes": {},
        "dynamic_routes": {},
        "regex_routes": {},
    }
    assert expected_result == router_test.__dict__

# Generated at 2022-06-14 07:58:45.688087
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router._get.cache_info().currsize == 0


# Generated at 2022-06-14 07:58:50.874864
# Unit test for constructor of class Router
def test_Router():
    router = Router()


# Generated at 2022-06-14 07:58:59.444099
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.app import Sanic
    from sanic.models.handler_types import RouteHandler
    def test_handler(request, something):
        if something == 'ok':
            return 'success'
        else:
            return 'failure'
    app = Sanic()
    router_instance = Router()
    route_instance = router_instance.add(
        uri = '/test',
        methods = ['GET'],
        handler = test_handler,
        name = 'test'
    )
    try:
        router_instance.finalize()
    except:
        pass
    else:
        assert True

# Generated at 2022-06-14 07:59:11.416288
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    for label in ["__file_uri__"]:
        assert ALLOWED_LABELS.__contains__(label)
    for label in ["__file_uri_"]:
        assert not ALLOWED_LABELS.__contains__(label)
    for label in ["__file_uri__", "__file_uri_"]:
        assert not router.ALLOWED_LABELS.__contains__(label)
    assert router.routes_all is router.routes
    assert router.routes_static is router.static_routes
    assert router.routes_dynamic is router.dynamic_routes
    assert router.routes_regex is router.regex_routes

# Generated at 2022-06-14 07:59:25.561442
# Unit test for constructor of class Router
def test_Router():
    def handler():
        return "Hello World"
    r = Router()
    r.add("/abc/def", ["GET"], handler)
    r.add("/abc/def", ["POST"], handler)
    assert r.routes_all.keys() == {"/abc/def"}
    assert r.routes_regex.keys() == set()
    assert isinstance(r.routes_regex, Dict)
    assert isinstance(r.routes_all, Dict)
    assert isinstance(r.name_prefix, str)
    assert isinstance(r.name_index, Dict)
    assert isinstance(r.param_index, Dict)
    assert isinstance(r.static_routes, Dict)

# Generated at 2022-06-14 07:59:26.220578
# Unit test for method finalize of class Router
def test_Router_finalize():
    pass

# Generated at 2022-06-14 07:59:31.948568
# Unit test for method finalize of class Router
def test_Router_finalize():
    # No Exception
    r = Router(None)
    route = Route("/test", None)
    r.dynamic_routes[0] = route
    r.finalize()
    del r

    # Exception
    r = Router(None)
    route = Route("/test/<__wrong:int>", None)
    r.dynamic_routes[0] = route
    try:
        r.finalize()
        assert False
    except SanicException:
        assert True

test_Router_finalize()


# Generated at 2022-06-14 07:59:37.306053
# Unit test for method finalize of class Router
def test_Router_finalize():
    def test_handler():
        pass

    router = Router()
    router.add('/test/<__param1:int>/<param2>', 'GET', test_handler)
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 07:59:39.497782
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None

# Generated at 2022-06-14 07:59:49.275727
# Unit test for method add of class Router
def test_Router_add():
    from sanic.views import HTTPMethodView
    from sanic.response import json

    class HTTPTest(HTTPMethodView):
        def get(self, request):
            return json({"method": "get"})

        def post(self, request):
            return json({"method": "post"})

        def put(self, request):
            return json({"method": "put"})

        def options(self, request):
            return json({"method": "options"})

        def head(self, request):
            return json({"method": "head"})

        def delete(self, request):
            return json({"method": "delete"})

        def trace(self, request):
            return json({"method": "trace"})


# Generated at 2022-06-14 07:59:53.898698
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add("/v{version}/test", ["GET"], print)
    r.finalize()
    assert r.routes_all[0].path == "/v{version}/test"


# Generated at 2022-06-14 08:00:15.470854
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.response import json
    from sanic.router import Router
    from sanic.request import Request
    import unittest

    class TestRouter(unittest.TestCase):
        def setUp(self):
            app = Sanic("test_router")
            self.router = Router()
            self.router.ctx = type("_ctx", (object, ), dict(app=app))
            self.req = Request("POST", "/")
            self.res = dict()

        def test_Router_finalize(self):
            def handler(x):
                return json({"test": True})

            app = self.router.ctx.app

# Generated at 2022-06-14 08:00:22.468242
# Unit test for method finalize of class Router
def test_Router_finalize():
    from .router_test_helper import get_router
    from .router_test_helper import get_check_router_finalize_result

    router = get_router()
    check_router_finalize_result = get_check_router_finalize_result()

    router.finalize()
    check_router_finalize_result(router)

# Generated at 2022-06-14 08:00:26.400598
# Unit test for method finalize of class Router
def test_Router_finalize():
    rt = Router()
    rt.add(uri='/', methods=['GET'], handler=None)
    rt.finalize()

# Generated at 2022-06-14 08:00:30.607042
# Unit test for constructor of class Router
def test_Router():
    route=Router()
    assert "Router" == route.__class__.__name__
    assert route.DEFAULT_METHOD == "GET"
    assert route.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:00:39.530725
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.app import Sanic

    app = Sanic("test_sanic")
    uri = "{__file_uri__}"
    methods = ["GET", "POST", "OPTIONS"]
    host = "example.com"
    static = False
    strict_slashes = False
    stream = False
    ignore_body = False
    version = 1
    name = None
    unquote = False
    handler = lambda request: None


# Generated at 2022-06-14 08:00:41.997714
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:00:45.567538
# Unit test for constructor of class Router
def test_Router():
    obj = Router()
    obj = Router()
    assert obj.__class__.__name__ == "Router"

# Generated at 2022-06-14 08:00:50.694894
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert router is not None
    assert router.routes == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}



# Generated at 2022-06-14 08:00:55.778814
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert isinstance(router, Router)
    assert router.default_method == "GET"
    assert router.allowed_methods == ["OPTIONS", "GET", "HEAD", "POST", "PUT", "PATCH",
                                      "DELETE", "TRACE"]

# Generated at 2022-06-14 08:00:57.456825
# Unit test for constructor of class Router
def test_Router():
    r = Router(None)
    assert isinstance(r, Router)


# Generated at 2022-06-14 08:01:14.439042
# Unit test for constructor of class Router
def test_Router():
    router = Router("class")
    assert router.ctx.__class__.__name__ == "Class"
    assert len(router.routes) == 0


# Generated at 2022-06-14 08:01:15.244167
# Unit test for method finalize of class Router
def test_Router_finalize():
    Router.finalize()

# Generated at 2022-06-14 08:01:21.690508
# Unit test for constructor of class Router
def test_Router():
    # Test case 1a
    # Test 1a.1: Initialize Router object with no args
    router1a1 = Router()
    # Test 1a.2: Type and value of router1a1
    assert isinstance(router1a1, Router) is True
    assert router1a1.routes_all == {}


# Generated at 2022-06-14 08:01:28.402755
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.route import Route
    from sanic.exceptions import SanicException
    import pytest
    @pytest.fixture(scope="function", params=[
        ("/", ["GET"], lambda request: None, []),
        ("/", ["GET"], lambda request: None, ["__param__"]),
        ("/", ["GET"], lambda request: None, ["__param__", "__file__"]),
        ("/", ["GET"], lambda request: None, ["__param__", "__file__", "__file_uri__"]),
        ("/", ["GET"], lambda request: None, ["a", "b", "c"]),
    ])
    def prepare_finalize(request):
        router = Router()
        route_uri, route_methods, handler, labels = request.param

# Generated at 2022-06-14 08:01:35.502981
# Unit test for constructor of class Router
def test_Router():
    a = Router()
    assert a.router_cache_size == 1024
    a.router_cache_size = 0
    assert a.router_cache_size == 0
    b = Router(router_cache_size = 3)
    assert b.router_cache_size == 3
    b.router_cache_size = 2
    assert b.router_cache_size == 2


# Generated at 2022-06-14 08:01:42.570066
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router_methods = '''
    DEFAULT_METHOD
    ALLOWED_METHODS
    _get
    get
    add
    find_route_by_view_name
    routes_all
    routes_static
    routes_dynamic
    routes_regex
    finalize
    '''
    for method in router_methods.strip().split('\n'):
        assert getattr(router, method.strip()) is not None


# Generated at 2022-06-14 08:01:53.472726
# Unit test for method add of class Router
def test_Router_add():
    from sanic.router import Route, RouteHandler, Router

    router = Router()

    @router.add('/test/1/', ['GET'], RouteHandler)
    def handler_func():
        pass

    assert isinstance(router.routes_dynamic[1], Route)
    assert router.routes_dynamic[1].url == '/test/1/'
    assert router.routes_dynamic[1].handler == handler_func()
    assert set(router.routes_dynamic[1].methods) == set(['GET'])



# Generated at 2022-06-14 08:01:53.846673
# Unit test for method finalize of class Router
def test_Router_finalize():
    assert False

# Generated at 2022-06-14 08:02:05.236990
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)



# Generated at 2022-06-14 08:02:10.089709
# Unit test for constructor of class Router
def test_Router():
    r=Router()
    assert r.routes_all == {}
    assert r.routes_dynamic == {}
    assert r.routes_regex == {}
    assert r.routes_static == {}


# Generated at 2022-06-14 08:02:49.512796
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router

    r = Router()

    r.regex_routes = {
        '/': '''re.compile('/$')''',
        '/requests': '''re.compile('/requests$')'''
    }

    for route in r.dynamic_routes.values():
        if any(
                label.startswith("__") and label not in ALLOWED_LABELS
                for label in route.labels
        ):
            raise SanicException(
                f"Invalid route: {route}. Parameter names cannot use '__'."
            )

# Generated at 2022-06-14 08:03:01.987303
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router(app=None)
    route_1 = Route(
        method = "POST",
        path = "/",
        handler = "",
        strict_slashes = False,
    )
    route_1.labels = ["__file_uri__", "1234"]
    route_2 = Route(
        method = "GET",
        path = "/",
        handler = "",
        strict_slashes = False,
    )
    route_2.labels = ["__file_uri__", "56", "__file_uri__"]

    router.dynamic_routes[("", "")] = [route_1]
    router.dynamic_routes[("", "")].append(route_2)
    router.finalize()

# Generated at 2022-06-14 08:03:03.241009
# Unit test for constructor of class Router
def test_Router():
    Router(None)


# Generated at 2022-06-14 08:03:03.938648
# Unit test for constructor of class Router
def test_Router():
    return Router()

# Generated at 2022-06-14 08:03:05.596011
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:03:12.561861
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    from sanic.router import Router
    # TypeError
    with pytest.raises(TypeError):
        route = Router().add('/', ['GET'], lambda request: 'OK')
    # SanicException
    with pytest.raises(SanicException):
        route = Router().add('/', ['GET'], lambda request: 'OK')

# Generated at 2022-06-14 08:03:14.191818
# Unit test for constructor of class Router
def test_Router():
    assert isinstance(Router(), Router)



# Generated at 2022-06-14 08:03:21.841905
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.route import Route
    from sanic import Sanic
    from sanic.response import text

    app = Sanic("test")
    router = Router(app)
    router.add("/", methods=["GET"], handler=app)
    router.add("/{}".format("__hello__"), methods=["GET"], handler=app)
    with pytest.raises(SanicException):
        router.finalize()

# Generated at 2022-06-14 08:03:30.813901
# Unit test for method finalize of class Router
def test_Router_finalize():
    class TestRoute(Route):
        pass

    class TestRouter(Router):
        pass

    router = TestRouter()
    router.register(TestRoute)
    router.add('/{cid}/{uid}/{role}', None, None, finalize=False)
    with pytest.raises(SanicException):
        router.finalize()
    router.add('/{cid}/{uid}/{__file_uri__}', None, None, finalize=False)
    router.finalize()



# Generated at 2022-06-14 08:03:36.804073
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert len(router.routes) == 0
    assert len(router.regex_routes) == 0
    assert len(router.static_routes) == 0
    assert len(router.dynamic_routes) == 0
    assert len(router.name_index) == 0


# Generated at 2022-06-14 08:04:44.906994
# Unit test for constructor of class Router
def test_Router():
    class app:
        _config = None
    import sanic
    sanic_app = sanic.Sanic("test")
    sanic_app._config = app._config
    # First run
    router = Router(sanic_app)
    assert isinstance(router, Router)
    # Second run
    router = Router(sanic_app)
    assert isinstance(router, Router)

# Generated at 2022-06-14 08:04:48.598345
# Unit test for constructor of class Router
def test_Router():
    try:
        Router()
    except Exception as e:
        assert False, f'constructor of class Router failed, got exception {e}'
    else:
        assert True


# Generated at 2022-06-14 08:04:57.236267
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert not r.name_index
    assert not r.routes
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS
    assert r.routes_all == r.routes
    assert r.routes_static == r.static_routes
    assert r.routes_dynamic == r.dynamic_routes
    assert r.routes_regex == r.regex_routes


# Generated at 2022-06-14 08:05:06.044436
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest
    with pytest.raises(SanicException) as excinfo:
        # pytest.set_trace()
        router.finalize(*(None,))
        assert 'Invalid route: <Route GET /test/<parameter> -> handler>.' in str(excinfo.value)

router = Router()
router.add(uri='/test/<parameter>', methods=['GET'], handler=None)
test_Router_finalize()
del router

# Generated at 2022-06-14 08:05:09.039558
# Unit test for constructor of class Router
def test_Router():
    r=Router()
    assert r.DEFAULT_METHOD == "GET"
    assert r.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:05:15.406173
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    import json
    with open("tests/sample_data/sanic_routes.json", "r") as json_file:
        data = json.load(json_file)
        routes = []
        for route in data:
            r = json.loads(route)
            routes.append(r)
    r = Router(routes)
    r.finalize()

# Generated at 2022-06-14 08:05:17.899527
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r.ctx is None
    assert r.name_index == {}

# Generated at 2022-06-14 08:05:23.149975
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert hasattr(router, 'DEFAULT_METHOD')
    assert hasattr(router, 'ALLOWED_METHODS')
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 08:05:26.067159
# Unit test for method add of class Router
def test_Router_add():
    a1 = Router()
    assert a1 == None


# Generated at 2022-06-14 08:05:32.269851
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.routes == {}
    assert router.simple_routes is None
    assert router.dynamic_routes == {}
    assert router.static_routes == {}
    assert router.ctx.default_method == 'GET'
    assert isinstance(router.ctx.allowed_methods, set)
