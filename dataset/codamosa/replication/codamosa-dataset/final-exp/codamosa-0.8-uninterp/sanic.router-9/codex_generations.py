

# Generated at 2022-06-14 07:55:42.811530
# Unit test for constructor of class Router
def test_Router():
    try:
        router = Router()
    except Exception as e:
        print(e)
        assert False
    else:
        assert True

if __name__ == '__main__':
    test_Router()

# Generated at 2022-06-14 07:55:50.531320
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router(None)
        router.dynamic_routes["my_route"] = Route("/some/path/{param1}/abc/{param2}",None,[])
        router.dynamic_routes["my_route"].labels = ["param1","param2","__file_uri__"]
        router.finalize()
    except Exception as e:
        assert str(e) == "Invalid route: /some/path/{param1}/abc/{param2}. Parameter names cannot use '__'."

# Generated at 2022-06-14 07:55:57.814949
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic import Sanic
    from sanic.response import html

    app = Sanic(__name__)

    def test(request, *args):
        pass

    app.add_route(test, '/test/<label>')

    with pytest.raises(SanicException):
        router = Router(app)
        router.add('/test/<label>', ['GET'], test)

# Generated at 2022-06-14 07:55:59.696174
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert isinstance(r, Router)


# Generated at 2022-06-14 07:56:04.146676
# Unit test for constructor of class Router
def test_Router():
    router = Router("Test")
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == {}


# Generated at 2022-06-14 07:56:07.819406
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    router.add("/index/index", ["GET"], None)
    router.get("/index/index", "GET", None)



# Generated at 2022-06-14 07:56:09.651839
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 07:56:10.688160
# Unit test for constructor of class Router
def test_Router():
    pass

# Generated at 2022-06-14 07:56:15.866411
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.dynamic_routes == {}
    assert router.name_index == {}
    assert router.regex_routes == {}
    assert router.static_routes == {}


# Generated at 2022-06-14 07:56:26.855666
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Route
    from sanic.exceptions import SanicException
    from sanic_routing.route import Route as R
    from sanic_routing.router import Router as RTR

    r = RTR()

    # test case for Invalid route
    r.static_routes["test"] = R("test", None, None, None, None, None, None,
                                [["__file_uri__", "word_file"], ["__smth__", "tjd"]])
    
    with pytest.raises(SanicException) as ex:
        r.finalize()

    assert str(ex.value) == "Invalid route: <Route test>"

# Generated at 2022-06-14 07:56:43.734027
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        router = Router()
        router.add('/<__file_uri__:string>/<__file_uri__:string>', ['GET', 'POST'], None)
        router.finalize()
    except:
        pytest.fail('Router finalze failed')
    else:
        assert True

# Generated at 2022-06-14 07:56:45.857835
# Unit test for constructor of class Router
def test_Router():
    router = Router({"app": "app"})
    assert router.app == 'app'



# Generated at 2022-06-14 07:56:52.040638
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Set up data
    router = Router()
    router.name_index = {'hello': Route(path='/hello', methods=['GET'])}
    router.dynamic_routes = {'hello': Route(path='/hello', methods=['GET'])}
    # Run function
    router.finalize()


# Generated at 2022-06-14 07:57:00.476531
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.ctx.app is None
    assert not router.routes
    assert not router.static_routes
    assert not router.dynamic_routes
    assert not router.regex_routes
    assert not router.name_index
    assert not router.dynamic_routes_count
    assert not router.static_routes_count
    assert not router.regex_routes_count
    assert router.__class__ == Router


# Generated at 2022-06-14 07:57:01.637741
# Unit test for constructor of class Router
def test_Router():
    router = Router()


# Generated at 2022-06-14 07:57:08.151558
# Unit test for constructor of class Router
def test_Router():
    r=Router()
    r.DEFAULT_METHOD="GET"
    assert r.DEFAULT_METHOD=="GET"
    assert (r.ALLOWED_METHODS) == ("GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS")



# Generated at 2022-06-14 07:57:21.828807
# Unit test for method finalize of class Router
def test_Router_finalize():
    from typing import Any
    from sanic.exceptions import SanicException

    router = Router()
    route = type("route", (object,), {"labels": {"__file_uri__": [0]}})
    router.dynamic_routes = {"route": route}

    from unittest.mock import patch
    
    with patch.object(router.dynamic_routes.get("route").labels.items, "__iter__", return_value=["__file_uri__"]):
        assert router.finalize() is None


# Generated at 2022-06-14 07:57:30.052410
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS
    assert router.ctx.app is None
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == []
    assert router.path_index == {}
    assert router.name_index == {}

# Generated at 2022-06-14 07:57:32.272623
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    assert router.finalize() == None


# Generated at 2022-06-14 07:57:37.535525
# Unit test for constructor of class Router
def test_Router():
    def test_handler(request):
        return "hello"
    test_router = Router()
    assert test_router.DEFAULT_METHOD == "GET"
    assert test_router.ALLOWED_METHODS == HTTP_METHODS


# Generated at 2022-06-14 07:58:00.679090
# Unit test for constructor of class Router
def test_Router():
    
    router = Router()
    assert router.routes == {}
    assert router.static_routes == {}
    assert router.dynamic_routes == {}
    assert router.regex_routes == {}
    assert router.name_index == {}
    assert router.ctx is None
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == ['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']
    assert router.ROUTER_CACHE_SIZE == 1024
    assert router.ALLOWED_LABELS == ("__file_uri__",)



# Generated at 2022-06-14 07:58:01.519124
# Unit test for constructor of class Router
def test_Router():
    r = Router()
    assert r is not None

# Generated at 2022-06-14 07:58:05.157980
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, Router)


test_Router()

# Generated at 2022-06-14 07:58:09.620068
# Unit test for method finalize of class Router
def test_Router_finalize():
    def handler():
        return {
            'status': 'ok'
        }

    router = Router()
    router.add('/rest/{__file_uri__}', methods=['GET'], handler=handler)

# Generated at 2022-06-14 07:58:11.729711
# Unit test for constructor of class Router
def test_Router():
    try:
        router_instance = Router()
        assert True
    except:
        assert False

# Generated at 2022-06-14 07:58:15.247198
# Unit test for method finalize of class Router
def test_Router_finalize():
    route = Route('GET', 'uri', 'handler', 'host', name='route')
    route.labels.add('__invalid')
    route.labels.add('__file_uri__')

    router = Rou

# Generated at 2022-06-14 07:58:21.105359
# Unit test for method finalize of class Router
def test_Router_finalize():
    method = 'finalize'
    obj = Router
    args = ()
    kwargs = {}

    with pytest.raises(SanicException) as exception_info:
        obj.finalize(*args, **kwargs)
    assert str(exception_info.value) == f"Invalid route: {None}. Parameter names cannot use '__'."

# Generated at 2022-06-14 07:58:26.845898
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == 'GET'
    assert router.ALLOWED_METHODS == ('HEAD', 'OPTIONS', 'GET', 'PUT', 'PATCH', 'POST', 'DELETE')


# Generated at 2022-06-14 07:58:37.815626
# Unit test for constructor of class Router
def test_Router():
    import inspect
    import json

    inspect.isclass(Router)
    x = Router()
    print(x)

    x = Router()
    x.add_route('/get/{name}', methods=['GET'], handler='handler')
    assert x.routes == [('/get/<name>', {'GET': 'handler'})]

    x = Router()
    x.add_route('/get/{name}', methods=['GET'], handler='handler')

# Generated at 2022-06-14 07:58:40.685781
# Unit test for constructor of class Router
def test_Router():
    router=Router()
    assert router.routes_all == {}
    assert router.routes_static == {}
    assert router.routes_dynamic == {}
    assert router.routes_regex == []


# Generated at 2022-06-14 07:59:16.846247
# Unit test for method finalize of class Router
def test_Router_finalize():
    class FakeApp(object):
        def __init__(self):
            self.router = Router(FakeApp)
    
    router = Router(FakeApp())
    fake_dynamic_routes = {
        '/test/<foo>': Route(handler=None, path='/test/<foo>', regex=None,
                             ),
    }
    fake_dynamic_routes['/test/<foo>'].labels = ['foo', '__file_uri__']
    fake_routes = {
        '/test/<foo>': Route(handler=None, path='/test/<foo>', regex=None,
                             ),
    }
    fake_routes['/test/<foo>'].labels = ['foo', '__file_uri__']
    router.dynamic_r

# Generated at 2022-06-14 07:59:22.682210
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.exceptions import SanicException
    from sanic.router import Router
    router = Router()
    router.dynamic_routes = {"test": {"labels": ["__test__"]}}
    with pytest.raises(SanicException):
        router.finalize()


# Generated at 2022-06-14 07:59:30.684358
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Container to store class information
    container = {}

    # Create a route with invalid label
    route = Route(path="", handler=lambda: None, methods=["GET"], labels={'__invalid_route': None})

    # Create a Router object
    router = Router(container)

    # Add route to Router object
    router.dynamic_routes[id(route)] = route

    # Assert that exception is raised
    with pytest.raises(SanicException, match="Invalid route: /  GET  - <lambda>.* Parameter names cannot use '__'."):
        router.finalize()

# Generated at 2022-06-14 07:59:40.222900
# Unit test for method finalize of class Router
def test_Router_finalize():
    app =Sanic("test_Router_finalize")
    router = Router.from_iterable(
        app,
        [
            (
                "/valid/<label>",
                app.route("/valid/<label>")(lambda x: 0),
            ),
            (
                "/invalid/<__label>",
                app.route("/invalid/<__label>")(lambda x: 0),
                {},
            ),
        ],
    )
    router.finalize()


# Generated at 2022-06-14 07:59:42.851016
# Unit test for constructor of class Router
def test_Router():
    # should be declarative
    my_router = Router()
    assert my_router is not None


# Generated at 2022-06-14 07:59:44.555725
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 07:59:45.560065
# Unit test for constructor of class Router
def test_Router():
    assert Router is not None

# Generated at 2022-06-14 07:59:58.799367
# Unit test for method finalize of class Router
def test_Router_finalize():
    routes = [
        Route(**{
            "path": "/user",
            "methods": ["PUT"],
            "name": None,
            "strict": False,
            "unquote": False,
            "ctx": None,
        }),
        Route(**{
            "path": "/user",
            "methods": ["GET"],
            "name": None,
            "strict": False,
            "unquote": False,
            "ctx": None,
        }),
    ]
    route_index = {
        "GET": [routes[1]],
        "PUT": [routes[0]],
    }

    def _prepare_routes():
        pass

    router = Router(
        routes,
        _prepare_routes,
        {},
    )



# Generated at 2022-06-14 08:00:03.412942
# Unit test for method finalize of class Router
def test_Router_finalize():
    import json
    from sanic.constants import HTTP_METHODS

    router = Router()
    for label in HTTP_METHODS:
        router.add(f'/{label}', label, 'hello_world')
    
    router.finalize()

if __name__ == "__main__":
    test_Router_finalize()

# Generated at 2022-06-14 08:00:14.548267
# Unit test for method finalize of class Router
def test_Router_finalize():
    # Assert comments:
    # - route.labels contains a dict of all parameter names
    # - ALLOWED_LABELS contains a tuple of valid parameter names (currently only one)
    # - ALLOWED_LABELS[0] starts with "__"
    # - loop over all parameter names provided by the test route and assert
    #   that each parameter name has to be one of the allowed ones
    route = mock.MagicMock()
    route.labels = {"__file_uri__": None}
    router = Router()
    router.dynamic_routes = {"some route": route}
    router.finalize()

# Generated at 2022-06-14 08:01:03.508148
# Unit test for method finalize of class Router
def test_Router_finalize():
    r = Router()
    r.add("/<name:end>", "GET", None)
    r.finalize()
    r = Router()
    r.add("/<name:end>", "GET", None)
    r.finalize()

# Generated at 2022-06-14 08:01:09.824470
# Unit test for constructor of class Router
def test_Router():
    router_ = Router(None, None)
    assert router_.DEFAULT_METHOD == "GET"
    assert router_.ALLOWED_METHODS == HTTP_METHODS
    assert router_.ctx == None
    assert router_.routes == {}
    assert router_.routes_all == {}
    assert router_.routes_static == {}
    assert router_.routes_dynamic == {}
    assert router_.routes_regex == {}
    assert router_.name_index == {}
    assert router_.url_to_route == {}
    assert router_.regex_cache == {}
    assert router_.dynamic_cache == {}
    assert router_.hash_ring == {}


# Generated at 2022-06-14 08:01:11.732937
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router is not None


# Generated at 2022-06-14 08:01:16.362685
# Unit test for method finalize of class Router
def test_Router_finalize():
    router = Router()
    router.add_route = Mock()
    router.add = Mock()
    router.finalize()

    assert router.add_route.call_count == 0
    assert router.add.call_count == 0

# Generated at 2022-06-14 08:01:18.810325
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert isinstance(router, BaseRouter)


# Generated at 2022-06-14 08:01:19.882538
# Unit test for constructor of class Router
def test_Router():
    assert Router() is not None

# Generated at 2022-06-14 08:01:27.768732
# Unit test for method finalize of class Router
def test_Router_finalize():
    try:
        class MyRouter(Router):
            def __init__(self, *args, **kwargs):
                self.routes = {
                    "GET": {
                        "__": {
                            "__": {
                                "__": {
                                    "__": [
                                        Route(
                                            uri="",
                                            method="GET",
                                            handler="",
                                            labels=["__flow__", "__method__"],
                                        )
                                    ],
                                }
                            }
                        }
                    }
                }
                super().__init__(*args, **kwargs)

        router = MyRouter()
        router.finalize()
        assert False, "exception not raised"
    except SanicException:
        pass

# Generated at 2022-06-14 08:01:29.768449
# Unit test for constructor of class Router
def test_Router():

    router = Router()
    print(router)

# Generated at 2022-06-14 08:01:30.427169
# Unit test for constructor of class Router
def test_Router():
    assert Router

# Generated at 2022-06-14 08:01:31.768523
# Unit test for constructor of class Router
def test_Router():
    a=Router()


# Generated at 2022-06-14 08:02:47.002626
# Unit test for constructor of class Router
def test_Router():
    route = Route("/", "GET", "index")
    router = Router(route)
    assert router.routes == {
        None: {
            '/': route
        }
    }


# Generated at 2022-06-14 08:02:51.780625
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic_routing.router import Router
    from sanic_routing.route import Route
    import unittest

    class RouterTest(unittest.TestCase):

        pass

    def setUpClass(cls):
        cls.router = Router()
        cls.raises_handler = lambda: 0
        cls.raises_route = Route(
            "GET", "/", cls.raises_handler, cls.router.ctx
        )
        cls.raises_route._labels = ["__a", "__b", "__c"]
        cls.raises_route._match = lambda: 0


# Generated at 2022-06-14 08:02:54.185962
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    print(router)


# Generated at 2022-06-14 08:03:02.228334
# Unit test for method finalize of class Router
def test_Router_finalize():
    from sanic.router import Router
    from sanic.exceptions import SanicException
    Router.dynamic_routes = {'test_route': 'hello'}

    with pytest.raises(SanicException):
        for route in Router.dynamic_routes.values():
            if any(
                label.startswith("__") and label not in ALLOWED_LABELS
                for label in route
            ):
                raise SanicException(
                    f"Invalid route: {route}. Parameter names cannot use '__'."
                )



# Generated at 2022-06-14 08:03:12.091538
# Unit test for constructor of class Router
def test_Router():
    uri = "test_uri"
    methods = ["GET","POST","PUT"]
    handler = RouteHandler
    host = "test_host"
    strict_slashes = False
    stream = False
    ignore_body = False
    version = 1.0
    name = "test_name"
    unquote = False
    static = False

    router = Router()
    router.add(uri=uri, methods=methods, handler=handler, host=host,
               strict_slashes= strict_slashes, stream= stream,
               ignore_body = ignore_body, version=version, name=name,
               unquote=unquote, static=static)



# Generated at 2022-06-14 08:03:19.692630
# Unit test for method add of class Router
def test_Router_add():
    uri = '/'
    methods = ['GET']
    handler = print
    host = 'myhost.com'
    strict_slashes = True
    stream= False
    ignore_body = True
    version = 1.0
    name = 'test_name'
    unquote = False
    static = False
    try:
        routes = Router().add(uri, methods, handler, host, strict_slashes, stream, ignore_body, version, name, unquote, static)
        return True
    except Exception as e:
        print(str(e))
        return False


# Generated at 2022-06-14 08:03:23.803523
# Unit test for constructor of class Router
def test_Router():
    router = Router()

    assert router.DEFAULT_METHOD == 'GET'

    assert router.ALLOWED_METHODS == HTTP_METHODS



# Generated at 2022-06-14 08:03:26.724145
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert router.DEFAULT_METHOD == "GET"
    assert router.ALLOWED_METHODS == HTTP_METHODS

# Generated at 2022-06-14 08:03:37.111634
# Unit test for constructor of class Router
def test_Router():
    router = Router()
    assert hasattr(router, "_routes")
    assert isinstance(router._routes, dict)
    assert len(router._routes) == 0
    #         assert len(router.routes_all) == 0
    assert len(router.routes_static) == 0
    assert len(router.routes_dynamic) == 0
    assert len(router.routes_regex) == 0
    assert len(router.regex_to_uri) == 0
    assert len(router.name_index) == 0
    assert hasattr(router, "_uri_to_regex")
    assert isinstance(router._uri_to_regex, dict)
    assert len(router._uri_to_regex) == 0

# Generated at 2022-06-14 08:03:44.452542
# Unit test for method finalize of class Router
def test_Router_finalize():
    import pytest

    st = Router()
    rt = Route("/test/<__test>/<test2>", None, None)
    rt.labels = ["__test", "test2"]
    st.dynamic_routes[""] = rt
    with pytest.raises(SanicException):
        st.finalize()