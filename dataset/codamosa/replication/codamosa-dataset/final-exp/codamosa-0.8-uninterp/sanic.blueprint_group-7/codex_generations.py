

# Generated at 2022-06-14 06:57:34.550429
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.response import text

    app = sanic.Sanic(__name__)
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    BlueprintGroup(bp1, bp2).middleware(lambda x: x)(lambda x: x)

    @bp1.middleware("request")
    async def bp1_middleware(request):
        request["bp"] = "bp1"

    @bp1.route("/bp1")
    async def bp1_route(request):
        return text(request["bp"])

    @bp2.middleware("request")
    async def bp2_middleware(request):
        request["bp"] = "bp2"


# Generated at 2022-06-14 06:57:43.129350
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    def middleware1(request):
        assert True

    @bpg.middleware('request')
    def middleware2(request):
        assert True


# Generated at 2022-06-14 06:57:55.679062
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('response')
    async def bp1_only_middleware(request):
        pass
    @bp2.middleware('response')
    async def bp2_only_middleware(request):
        pass

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    app = sanic.Sanic()
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)


# Generated at 2022-06-14 06:58:09.685159
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse

    class TestBP(Blueprint):
        def __init__(self, name, url_prefix):
            super().__init__(name, url_prefix=url_prefix)
            self.record = []

        @property
        def middlewares(self):
            return self._middlewares

        @middlewares.setter
        def middlewares(self, middlewares):
            self._middlewares = middlewares

        def add_middleware(self, fn, *args, **kwargs):
            self.record.append((fn, args, kwargs))

    bp1 = TestBP('bp1', '/bp1')

# Generated at 2022-06-14 06:58:22.281963
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg.blueprints) == 2
    @bpg.middleware('request')
    def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    @bp1.middleware('request')
    def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    assert hasattr(bp1, '_middlewares')
    assert len(bp1._middlewares) == 2

# Generated at 2022-06-14 06:58:32.543638
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # create a BlueprintGroup
    bpg = BlueprintGroup()

    # create a Blueprint
    bp1 = Blueprint("bp1")

    # add the Blueprint to the BlueprintGroup
    bpg.append(bp1)

    # test middleware registration
    @bpg.middleware("request")
    async def bp1_middleware1(request):
        assert True

    @bpg.middleware("request")
    async def bp1_middleware2(request):
        assert True

    assert len(bp1.middlewares["request"]) == 2



# Generated at 2022-06-14 06:58:45.558668
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Blueprint, Sanic

    app = Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:58:59.314722
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def middleware(request):
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp1.route(lambda req: req)(lambda req: req)
    bp2.route(lambda req: req)(lambda req: req)

    bp_g1 = BlueprintGroup(bp1, bp2)

    bp_g1.middleware(middleware)
    for bp in bp_g1.blueprints:
        assert bp.middlewares[0] == middleware

    bp_g1.middleware(middleware, attach_to='response')
    for bp in bp_g1.blueprints:
        assert bp.middlewares[1] == middleware

    b

# Generated at 2022-06-14 06:59:06.705187
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        pass

    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1

    bpg.insert(0, bp1)
    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1

    del bpg[0]

# Generated at 2022-06-14 06:59:18.035486
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')

    @bp1.middleware('request')
    def bp1_middleware(request):
        print('applied on Blueprint : bp1 Only')

    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp2.middleware('request')
    def bp2_middleware(request):
        print('applied on Blueprint : bp2 Only')

    group = BlueprintGroup(bp1, url_prefix='/api')
    assert group.middleware('request')
    assert group.middleware('request')(bp2_middleware)



# Generated at 2022-06-14 06:59:33.816616
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def _middleware_fn(request):
        pass
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    bp4 = Blueprint('bp4')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bpg)
    bpg.append(bp3)
    bpg.append(bp4)
    bpg.middleware(_middleware_fn)
    assert 4 == len(bp1.middlewares['request'])
    assert 5 == len(bp2.middlewares['request'])
    assert 4 == len(bp3.middlewares['request'])
    assert 5 == len(bp4.middlewares['request'])

# Generated at 2022-06-14 06:59:45.630040
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp1.middleware("request")(lambda request: print("bp1 middleware"))
    bp2.middleware("request")(lambda request: print("bp2 middleware"))
    bpg = BlueprintGroup("/api")
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware("request")(lambda request: print("bpg middleware"))
    assert len(bpg.blueprints) == 2
    assert len(bpg.blueprints[0].middlewares) == 1
    assert len(bpg.blueprints[1].middlewares) == 1

# Generated at 2022-06-14 06:59:56.048287
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class FakeBlueprint:
        """Fake Blueprint"""

    bp1 = FakeBlueprint()
    bp2 = FakeBlueprint()
    bpg = BlueprintGroup()
    bpg._blueprints = [bp1, bp2]
    bpg._blueprint_middleware_registrar = Mock()
    bpg.middleware(bp1, "request", attach_to="bp")()

    bpg._blueprint_middleware_registrar.assert_has_calls(
        [call(bp1, "request", attach_to="bp")]
    )

# Generated at 2022-06-14 07:00:07.102998
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint
    from sanic.response import text

    bp1 = Blueprint("bp1", url_prefix="/bp1")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")

    bp2 = Blueprint("bp1", url_prefix="/bp2")

    @bp2.route("/")
    async def bp2_route(request):
        return text("bp2")

    app = sanic.Sanic()

    @app.middleware("request")
    async def global_middleware(request):
        print("global middleware")

    @bp1.middleware("request")
    async def bp1_middleware(request):
        print("bp1 middleware")


# Generated at 2022-06-14 07:00:18.955866
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp = Blueprint('bp', url_prefix='/')

    @bp.route('/')
    async def handler(request):
        return text('OK')

    @bp.middleware('request')
    async def bp_middleware(request):
        setattr(request, 'bp', True)

    @bp.group(url_prefix = "/api", version="v1")
    def bpg(bp):
        @bp.route('/hook1')
        async def handler(request):
            return text('OK')

        @bp.middleware('request')
        async def group_middleware(request):
            setattr(request, 'bpg', True)

    @bpg.middleware('request')
    async def bp_middleware(request):
        set

# Generated at 2022-06-14 07:00:32.877872
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    In case of Blueprints Group, the blueprint group middleware should be
    applied to any of the nested blueprint present in each of the Blueprints.

    Testing one of the case of nested blueprint only.
    """
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.route("/")
    async def dummy_handler(request):
        pass

    @bp2.route("/")
    async def dummy_handler(request):
        pass

    @bpg.middleware("request")
    async def dummy_unitary_test(request):
        pass


# Generated at 2022-06-14 07:00:43.950059
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp3', url_prefix='/bp3')
    bp6 = Blueprint('bp4', url_prefix='/bp4')
    app = sanic.Sanic()

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api1", version="v1")
    bpg2 = BlueprintGroup(bp5, bp6, url_prefix="/api2", version="v2")


# Generated at 2022-06-14 07:00:52.454173
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from unittest.mock import Mock, MagicMock
    from sanic.blueprints import Blueprint, BlueprintGroup

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp1.route('/')
    async def bp1_route(request):
        pass

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        pass


# Generated at 2022-06-14 07:01:07.029640
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestBlueprintGroup(BlueprintGroup):
        pass

    bp1 = Blueprint('test_bp1')
    bp2 = Blueprint('test_bp2')
    bp3 = Blueprint('test_bp3')
    bp4 = Blueprint('test_bp4')

    bpg1 = TestBlueprintGroup()
    bpg2 = TestBlueprintGroup()

    bpg1.append(bp1)
    bpg1.append(bp2)

    bpg2.append(bp3)
    bpg2.append(bp4)

    bpg2.append(bpg1)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:01:20.986995
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create a new Sanic app
    app = sanic.Sanic(__name__)
    # Create a Blueprint Group
    bpg = BlueprintGroup(url_prefix='/api/v1')
    # Create 2 blueprints to be used under the Blueprint Group
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    # Register the blueprint inside the blueprint group
    bpg.append(bp1)
    bpg.append(bp2)
    # create a request handler for testing
    @bp1.route('/')
    async def bp1_handler(request):
        return text('bp1')

# Generated at 2022-06-14 07:01:38.724202
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprint.Blueprint.middleware("request")
    async def bp_middleware(request):
        print("applied on Blueprint : bp1 Only")

    @sanic.blueprint.BlueprintGroup.middleware("request")
    async def bpg_middleware(request):
        print("common middleware applied for both bp1 and bp2")

    class MockApp:
        __slots__ = ("blueprints",)

        def __init__(self):
            self.blueprints = {}

        def blueprint(self, item):
            self.blueprints[item.name] = item

    # TODO: mock Blueprint.group() and call the function to test
    # the middleware function

    bp1 = sanic.Blueprint("bp1", url_prefix="/bp1")

# Generated at 2022-06-14 07:01:50.358228
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This is a method to create a test case for BlueprintGroup class's middleware
    function

    :return: None
    """
    app = sanic.Sanic()

    bp = Blueprint("test_bp", url_prefix="/test", version=1.2, strict_slashes=True)
    bp2 = Blueprint("test_bp2", url_prefix="/test2", version=1.2, strict_slashes=True)
    bp3 = Blueprint("test_bp3", url_prefix="/test3", version=1.0, strict_slashes=False)
    bp4 = Blueprint("test_bp4", url_prefix="/test4", version=None, strict_slashes=None)


# Generated at 2022-06-14 07:01:59.818658
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprint.middleware
    def middleware(request): ...

    app = sanic.Sanic()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)

    bp1_middleware_fn = group.middleware(middleware)
    bp2_middleware_fn = group.middleware(middleware)

    assert bp1_middleware_fn == bp2_middleware_fn

    assert bp1_middleware_fn in app.request_middleware
    assert bp2_middleware_fn in app.request_middleware

# Generated at 2022-06-14 07:02:12.797408
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1')
    bp2 = sanic.Blueprint('bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    def bp1_mw1(request):
        pass

    def bp1_mw2(request):
        pass

    def bp2_mw1(request):
        pass

    def bp2_mw2(request):
        pass

    @bpg.middleware('request')
    def bpg_mw1(request):
        pass

    @bpg.middleware('request')
    def bpg_mw2(request):
        pass

    @bpg.middleware('request')
    def bpg_mw3(request):
        pass

# Generated at 2022-06-14 07:02:26.659229
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_app = Blueprint("test_bp", url_prefix='/bp1')

    @blueprint_app.middleware("response")
    async def custom_middleware(request, response):
        print("Appied middleware")

    @blueprint_app.route("/")
    async def test_handler(request):
        pass
        
    blueprint_group = BlueprintGroup("/bp", "v1", True)
    blueprint_group.append(blueprint_app)

    @blueprint_group.middleware("response")
    async def custom_middleware_for_group(request, response):
        print("Appied middleware for group")

    assert len(blueprint_app._middlewares) == 1, "number of middlewares of blueprint app should be 1"

# Generated at 2022-06-14 07:02:34.902166
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    # Create a Blueprint Group with 2 blueprints
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    @bpg.middleware('request')
    async def bpg_only_middleware(request):
        print('applied on Blueprint Group : bpg')

    assert len(bp1.middlewares['request']) == 0
    assert len(bp2.middlewares['request']) == 0
    assert len(bp3.middlewares['request'])

# Generated at 2022-06-14 07:02:43.912740
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    
    blueprints = [sanic.Blueprint("bp1"),
                  sanic.Blueprint("bp2")]

    bp = BlueprintGroup(blueprints[0], blueprints[1])

    @bp.middleware("request")
    async def test_middleware(request):
        pass

    assert len(blueprints[0].middlewares["request"]) == 1
    assert len(blueprints[1].middlewares["request"]) == 1

    assert blueprints[0].middlewares["request"][0] == test_middleware
    assert blueprints[1].middlewares["request"][0] == test_middleware

# Generated at 2022-06-14 07:02:50.605752
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    original_handler = asyncio.coroutine(lambda x:x)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    middleware_function = MagicMock()
    mock_app = MagicMock()
    mock_app.blueprints = {bp1.name: bp1, bp2.name: bp2}
    route_name = 'route1'
    bp1.add_route(original_handler, '/', route_name)
    bp2.add_route(original_handler, '/', route_name)
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware(middleware_function)
    assert len

# Generated at 2022-06-14 07:03:03.598879
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp_list = [bp1, bp2, bp3]

    bpg = BlueprintGroup('/api')
    bpg += bp_list

    @bpg.middleware('request')
    async def bp_common_middleware(request):
        print('Common Middleware applied')

    for bp in bp_list:
        for middleware in bp._request_middleware:
            assert middleware == bp_common_middleware

# Generated at 2022-06-14 07:03:14.221163
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp = Blueprint(__name__, url_prefix='test_BlueprintGroup_middleware')
    bpg = BlueprintGroup(bp, url_prefix='/test_BlueprintGroup_middleware')
    bpg.middleware(lambda request: None)
    bp.register(app)
    assert len(bp.middlewares['request']) == 1
    assert len(bp.middlewares['response']) == 0
    assert len(bp.middlewares['websocket']) == 0


if __name__ == '__main__':
    test_BlueprintGroup_middleware()

# Generated at 2022-06-14 07:03:35.456943
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    class MyMiddleware:
        pass

    app = sanic.Sanic()

    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    async def my_middleware(request):
        pass

    assert len(bp1.middlewares) == 1
    assert bp1.middlewares[0]._middleware.func == my_middleware.__func__
    assert isinstance(bp1.middlewares[0]._middleware.instance, MyMiddleware)
    assert len(bp2.middlewares) == 1
    assert bp2.middlewares[0]._middleware.func == my_middleware.__func__


# Generated at 2022-06-14 07:03:49.014927
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup(bp1, bp2, url_prefix="/api")

    @group.middleware('request')
    async def group_middleware(request):
        assert "group_middleware_called" not in request.app.config
        request.app.config["group_middleware_called"] = True

    # for Blueprint in BlueprintGroup
    for blueprint in group:
        assert blueprint.blueprint_middleware_names is not None
        assert len(blueprint.blueprint_middleware_names) == 1
        assert blueprint.blueprint_middleware_names[0] == "request"

    # prepare app with BlueprintGroup
    app = sanic.Sanic()


# Generated at 2022-06-14 07:04:00.016965
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Simple blueprint group with a single blueprint under it
    blueprint_group = BlueprintGroup("/api", "v1", False)  # type: BlueprintGroup
    blueprint = Blueprint("blueprint1", "/blueprint1", "v2", False)
    blueprint_group.append(blueprint)

    # Test decorator applied on method
    @blueprint_group.middleware("request")
    async def bp1_only_middleware(request):
        pass

    assert len(blueprint_group.blueprints[0].middlewares) == 1

    # Test decorator applied on function
    @blueprint_group.middleware
    async def bp1_only_middleware(request):
        pass

    assert len(blueprint.middlewares) == 2

# Generated at 2022-06-14 07:04:13.204298
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(
        url_prefix='/api',
        version='v1',
        strict_slashes=True)

    bpg.append(bp1)
    bpg.append(bp2)

    assert bp1._middleware_stack == []
    assert bp2._middleware_stack == []

    @bpg.middleware('request')
    async def bp3_middleware(request):
        """Doc String"""
        pass

    assert bp1._middleware_stack[0]['middleware'] == bp3_middleware
    assert bp1._middleware_stack[0]['args']

# Generated at 2022-06-14 07:04:26.071748
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Test Blueprint Group - URL Prefix
    bp_group_url_prefix = BlueprintGroup(url_prefix="/group_bp")

    # Test Blueprint Group - Version
    bp_group_version = BlueprintGroup(version="v1")

    # Test Blueprint Group - Strict slash
    bp_group_strict_slashes = BlueprintGroup(strict_slashes=False)

    # Test Blueprint Group - One Blueprint
    bp_group_one_bp = BlueprintGroup()
    bp_group_one_bp.append(Blueprint("bp1"))

    # Test Blueprint Group - Two Blueprints
    bp_group_two_bp = BlueprintGroup()
    bp_group_two_bp.append(Blueprint("bp1"))
    bp_group_two_bp.append(Blueprint("bp2"))


# Generated at 2022-06-14 07:04:39.707364
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test should cover the following:
        - Middleware should be registered on each of the Blueprint
        - Blueprint group middleware should be applied on each of the
            blueprint present in nested blueprint group.
    """
    app = sanic.Sanic()

    class MiddlewarePlugin:
        async def __call__(self, request, call_next):
            return await call_next(request)

    # bp1 = Blueprint('bp1', url_prefix='/bp1')
    # bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")


# Generated at 2022-06-14 07:04:47.652533
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint("bp1", url_prefix='/bp1')
    bp2 = Blueprint("bp2", url_prefix='/bp2')
    bp3 = Blueprint("bp3", url_prefix='/bp3')
    bp4 = Blueprint("bp4", url_prefix='/bp4')
    bp5 = Blueprint("bp5", url_prefix='/bp5')
    bg = BlueprintGroup()
    bg.append(bp1)
    bg.append(bp2)
    bg.append(bp3)
    bg.append(bp4)
    bg.append(bp5)

    @bg.middleware('request')
    async def bg_middleware(request):
        print('bg_middleware')


# Generated at 2022-06-14 07:04:59.606126
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # type: () -> None
    from sanic.server import HttpProtocol
    from sanic.response import text
    from sanic.testing import SanicTestClient
    from sanic.blueprints import Blueprint

    app = sanic.Sanic("test_BlueprintGroup_middleware")

    # Create some blueprints
    bp1 = Blueprint("test_bp1", url_prefix="/bp1")
    bp2 = Blueprint("test_bp2", url_prefix="/bp2")

    # Create the BlueprintGroup
    bp_group = BlueprintGroup()

    # Add the blueprints to the group
    bp_group.append(bp1)
    bp_group.append(bp2)

    # Setup some routes

# Generated at 2022-06-14 07:05:05.574816
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from .blueprint import Blueprint
    from .route import Route
    from .websocket import WebSocketRoute

    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    bg = BlueprintGroup()
    bg.append(bp1)
    bg.append(bp2)

    @bg.middleware('request')
    def middleware_function(request):
        pass

    assert len(bp1.request_middleware) == 1
    assert bp1.request_middleware[0] == middleware_function
    assert len(bp2.request_middleware) == 1
    assert bp2.request_middleware[0] == middleware_function



# Generated at 2022-06-14 07:05:09.343623
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware
    async def test_middleware(request):
        pass
test_BlueprintGroup_middleware.__module__ = Blueprint.__module__ + ".group"


# Generated at 2022-06-14 07:05:23.544273
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint(url_prefix="/bp")
    bpg = BlueprintGroup()
    bpg.append(bp)
    @bp.middleware("request")
    async def bp_request(request): pass
    bpg.middleware("request")(lambda x: None)
    assert bp.middlewares["request"][0]() == None

# Generated at 2022-06-14 07:05:34.895764
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Middleware can be used to add a plugin to the Blueprint Group. The same
    middleware is applied across the blueprint group and its sub-blueprint
    groups.

    :return: None
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:05:47.402771
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        request['middleware'] = True
        return text('test_BlueprintGroup_middleware')

    @bp1.route('/')
    async def bp1_route(request):
        if request.get('middleware'):
            return text('bp1')
        else:
            return text('error', status=503)


# Generated at 2022-06-14 07:05:55.045216
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bg = BlueprintGroup(bp1, bp2)
    assert not bp1.middlewares["request"]
    assert not bp2.middlewares["request"]

    @bg.middleware("request")
    async def handler(request):
        pass

    assert handler in bp1.middlewares["request"]
    assert handler in bp2.middlewares["request"]


# Generated at 2022-06-14 07:06:07.891479
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:06:22.166449
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    
    class MockSanicApp:
        """
        Mock class for Sanic App. This will mock only the blueprint registration
        function.
        """

        def __init__(self):
            """
            Constructor
            """
            self.blueprints = []

        def register_blueprint(self, blueprint):
            """
            Mock the register blueprint function of Sanic. This will not
            actually register anything. Instead it will append in the mock
            blueprint list for assertion.
            """
            self.blueprints.append(blueprint)

    app = MockSanicApp()
    
    
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    b

# Generated at 2022-06-14 07:06:31.390444
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class app:
        async def factory(self):
            return self

        def register_blueprint(self, bp):
            self.bp = bp

    app = app()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        pass

    bp1.register(app, url_prefix='/bp1')
    assert len(app.bp.middlewares['request']) == 1
    assert bp1_only_middleware.__name__ in app.bp.middlewares['request']

# Generated at 2022-06-14 07:06:37.444572
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Type Hinting imports
    from sanic.blueprints import Blueprint
    from sanic.response import text

    # Test fixtures
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    url_prefix = "/test_BlueprintGroup_middleware"
    bp1 = Blueprint("bp1", url_prefix="/test_bp1", version="v1")
    bp2 = Blueprint("bp2", url_prefix="/test_bp2", version="v1")
    bpg = BlueprintGroup(bp1, bp2, url_prefix=url_prefix, version="v1")

    # Disable strict slash behavior for the Blueprint group
    assert bpg.strict_slashes is None
    assert bp1.strict_slashes is None
    assert bp2.strict_slashes is None
    b

# Generated at 2022-06-14 07:06:47.077395
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    group = BlueprintGroup()

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')


# Generated at 2022-06-14 07:06:58.322377
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class App(sanic.Sanic):
        pass

    app = App()

    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")
    bp4 = Blueprint("bp4")

    group1 = Blueprint.group(bp1, bp2, url_prefix="/base")
    group2 = Blueprint.group(bp3, bp4, url_prefix="/api", version="v1")
    group2.middleware(app.request_middleware)

    @bp1.route("/")
    async def bp1_route(request):
        pass

    @bp3.route("/")
    async def bp3_route(request):
        pass

    # Check if the middleware is applied to all the Blueprints recursively
    assert b

# Generated at 2022-06-14 07:07:16.053050
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    group = BlueprintGroup("/group", version="1.0")
    group.append(bp1)
    group.append(bp2)
    assert group[0] == bp1
    assert group[1] == bp2
    with pytest.raises(IndexError):
        group[2]


# Generated at 2022-06-14 07:07:22.010489
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    blueprint_group = BlueprintGroup('/api', 'v1', True)
    blueprint_group.append(Blueprint('bp1', '/bp1'))
    blueprint_group.append(Blueprint('bp2', '/bp2'))
    assert len(blueprint_group) == 2
