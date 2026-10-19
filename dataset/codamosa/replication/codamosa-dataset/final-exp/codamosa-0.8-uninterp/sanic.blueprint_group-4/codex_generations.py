

# Generated at 2022-06-14 06:57:17.975792
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class App:
        def register_blueprint(app, blueprint):
            pass

    class Blueprint:
        def __init__(self, name: str, url_prefix: str):
            self.name = name
            self.url_prefix = url_prefix
            self.middlewares = []

        def middleware(self, fn, *args, **kwargs):
            self.middlewares.append(fn)
            return fn

    bp1 = Blueprint(name="bp1", url_prefix="/bp1")
    bp2 = Blueprint(name="bp2", url_prefix="/bp2")

    bpg = BlueprintGroup()

    @bpg.middleware
    async def middleware1(request):
        pass

    @bpg.middleware('request')
    async def middleware2(request):
        pass

    b

# Generated at 2022-06-14 06:57:26.350929
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")
    bp4 = Blueprint("bp4")
    bpg = BlueprintGroup(bp3, bp4)
    @bpg.middleware()
    def test_middleware(req):
        pass
    assert len(bp3.middlewares["request"]) == 1
    assert len(bp4.middlewares["request"]) == 1

# Generated at 2022-06-14 06:57:36.535437
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('bp1', url_prefix='/bp1')
    called = False
    def middleware_fn(request):
        nonlocal called
        called = True
    bpg = BlueprintGroup()
    bpg.append(bp)

    @bpg.middleware
    def mw_fn(request):
        request['mw_called'] = 'called'

    response = bp.handle_request(sanic.request.Request(
        uri=b'/bp1/',
        method='GET',
        headers=None,
        transport=sanic.request.Connection(),
        app=bp.app
    ))

    assert response['mw_called'] == 'called'



# Generated at 2022-06-14 06:57:49.806341
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Setup a test Sanic app
    app = sanic.Sanic(__name__)
    bp = Blueprint('bp')

    # Sanic doesn't ensure that the Sanic app in a blueprint is immutable
    # so we need to reset it to the correct app after it's been set
    bp.app = app


    class Controller:
        app = app

    @bp.middleware('request')
    async def bp_middleware(request):
        print('bp_middleware')

    @bp.exception(sanic.exceptions.NotFound)
    async def ignore_404s(request, exception):
        pass

    @bp.route('/')
    async def handler(request):
        return text('works')

    bpg = BlueprintGroup()
    bpg.append(bp)

# Generated at 2022-06-14 06:58:02.540495
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_middleware1(request):
        print('bp1_middleware1')
        return

    @bp2.middleware('request')
    async def bp2_middleware1(request):
        print('bp2_middleware1')
        return

    @bpg.middleware('request')
    async def bp_group_middleware1(request):
        print('bp_group_middleware1')
        return

    assert len(bp1.middlewares['request']) == 2

# Generated at 2022-06-14 06:58:13.333652
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    @async_generator
    async def middleware(request):
        request.ctx["name"] = "bpg"
        await asyncio.sleep(0)

    request = sanic.request.Request("GET", "/v1/bp1")
    request.ctx = dict()
    bp1 = Blueprint("bp1", version="v1")
    bp2 = Blueprint("bp2", version="v1")

    bpg = BlueprintGroup(url_prefix="/v1", version="v1")
    bpg.extend([bp1, bp2])

    @bp1.route("/bp1")
    async def bp1_route(request):
        return text(request.ctx.get("name", ""))


# Generated at 2022-06-14 06:58:25.444129
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    class BlueprintGroupMock(BlueprintGroup):
        def __init__(self, url_prefix=None, version=None, strict_slashes=None):
            super().__init__(url_prefix, version, strict_slashes)
            self._blueprints = [BlueprintMock(url_prefix='/bp1'),
                                BlueprintMock(url_prefix='/bp2')]

    class BlueprintMock(sanic.Blueprint):
        """
        Mock class to replace sanic.Blueprint inside of the BlueprintGroup
        class
        """

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.middleware_list = []

        def middleware(self, middleware, *args, **kwargs):
            self.middleware_list.append

# Generated at 2022-06-14 06:58:32.578069
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    BlueprintGroup.middleware decorator adds middlewares to
    every blueprint in a blueprint group.
    """
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')
    group1 = BlueprintGroup()
    group2 = BlueprintGroup()
    group1.append(bp1)
    group1.append(bp2)
    group1.append(bp3)


# Generated at 2022-06-14 06:58:44.728799
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")
    bp4 = Blueprint("bp4")
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert len(bpg._blueprints) == 0
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg._blueprints) == 2
    bpg.append(bpg)
    assert len(bpg._blueprints) == 3
    assert bpg[-1] is bpg

    @bp3.middleware("request")
    async def bp_middleware_1(request):
        assert request


# Generated at 2022-06-14 06:58:54.118114
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('bp', url_prefix='/bp')
    bp_group = BlueprintGroup(url_prefix='/group')
    bp_group_child = BlueprintGroup(url_prefix='/child')
    bp_group.blueprints.append(bp)
    bp_group_child.blueprints.append(bp_group)

    @bp_group_child.middleware('request')
    async def bp_group_middleware(request):
        request['a'] = 1

    mw_list = bp.get_middleware('request')

    assert mw_list is not None
    assert len(mw_list) == 1



# Generated at 2022-06-14 06:59:09.747175
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprint.middleware()
    def mw_1(request):
        request['mw_1'] = True

    class MockBlueprint:
        def __init__(self, name):
            self.middleware = []
            self.name = name

        def middleware(self, fn, *args, **kwargs):
            self.middleware.append((fn, args, kwargs))

    bp1 = MockBlueprint('bp1')
    bp2 = MockBlueprint('bp2')
    bp3 = MockBlueprint('bp3')
    bp4 = MockBlueprint('bp4')

    bpg = BlueprintGroup(url_prefix='/bpg')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
   

# Generated at 2022-06-14 06:59:20.312730
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    @bp3.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:59:33.709223
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = sanic.Blueprint('bp1', url_prefix='/api/v1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/api/v2')

    @bp1.route('/')
    async def bp1_route(request):
        return sanic.response.json({"foo": "bar"})

    @bp2.route('/')
    async def bp2_route(request):
        return sanic.response.json({"foo": "bar"})

    group = BlueprintGroup(bp1, bp2, url_prefix='/api')

    @group.middleware('request')
    async def middleware_executed_for_all(request):
        request['test_middleware'] = 'executed'



# Generated at 2022-06-14 06:59:45.605015
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg2 = BlueprintGroup(url_prefix="/api2", version="v2")

    bpg.append(bp1)
    bpg.append(bp2)
    bpg2.append(bpg)
    bpg2.append(bp3)
    bpg2.append(bp4)


# Generated at 2022-06-14 06:59:59.154162
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test case for the BlueprintGroup.middleware decorator to apply
    middleware across all blueprints inside the blueprint group
    """
    bp = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup("/api/v1")
    bpg.append(bp)
    bpg.append(bp2)

    @bp.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text

# Generated at 2022-06-14 07:00:09.552946
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_group = BlueprintGroup()
    blueprint_group.append(Blueprint('test', 'test_b1'))
    blueprint_group.append(Blueprint('test', 'test_b2'))

    @blueprint_group.middleware('request')
    async def test_middleware(request):
        print('test middleware')

    assert len(blueprint_group.blueprints[0].middlewares['request']) == 1
    assert len(blueprint_group.blueprints[1].middlewares['request']) == 1

    @blueprint_group.middleware()
    async def test_middleware(request):
        print('test middleware')

    assert len(blueprint_group.blueprints[0].middlewares['request']) == 2

# Generated at 2022-06-14 07:00:20.002192
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg1 = BlueprintGroup('/bpg1')
    bpg1.append(bp1)
    bpg1.append(bp2)

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg2 = BlueprintGroup('/bpg2')
    bpg2.append(bp3)
    bpg2.append(bp4)

    bpg3 = BlueprintGroup('/bpg3')
    bpg3.append(bpg1)
    bpg3.append(bpg2)


# Generated at 2022-06-14 07:00:34.483703
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # init Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    # create BlueprintGroup
    bpg = BlueprintGroup(
        url_prefix="/api", version="v1", strict_slashes=False)
    bpg.append(bp3)
    bpg.append(bp4)

    # define middleware
    @bpg.middleware('request')
    async def bpg_middleware(request):
        print('applied for BlueprintGroup : bpg')


# Generated at 2022-06-14 07:00:38.576123
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware('request')
    def bp_group_middleware(request):
        print('applied on Blueprint Group : bp1 Only')



# Generated at 2022-06-14 07:00:47.826960
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    @bp1.middleware('request')
    def middleware_test(request):
        return True

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    assert not bp2.request_middleware
    assert not bp2.response_middleware

    @group.middleware('request')
    def middleware_test(request):
        return True

    assert bp2.request_middleware  # type: ignore



# Generated at 2022-06-14 07:01:06.371199
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bp_group1 = BlueprintGroup(bp1, bp2)
    bp_group2 = BlueprintGroup(bp3, bp4)

    @bp_group1.middleware('request')
    async def bp_group1_middleware(request):
        print('bp_group1_middleware')
        request.ctx.bp_group1.add(1)


# Generated at 2022-06-14 07:01:18.347961
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class FakeBlueprint:
        def __init__(self):
            self.middleware_functions = []
            self.middleware_args = []
            self.middleware_kwargs = []
            self.url_prefix = None

        def middleware(self, *args, **kwargs):
            if not callable(args[0]):
                raise TypeError
            self.middleware_functions.append(args[0])
            self.middleware_args.append(list(args[1:]))
            self.middleware_kwargs.append(kwargs)

    test_list = []
    for i in range(10):
        bp = FakeBlueprint()
        bp.url_prefix = str(i)
        test_list.append(bp)

    bpg = BlueprintGroup()
    bpg.blue

# Generated at 2022-06-14 07:01:27.979142
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Sanic
    from sanic.blueprints import Blueprint
    app = Sanic()
    a = Blueprint('a', url_prefix='/a')
    b = Blueprint('b', url_prefix='/b')
    bg1 = BlueprintGroup(url_prefix='/a')
    bg1.append(a)
    bg1.append(b)

    @bg1.middleware('request')
    async def request(request):
        return request


    @a.route('/')
    async def test(request):
        return text('OK')


    app.blueprint(bg1)

    _, response = app.test_client.get('/a/')
    assert response.text == 'OK'

BlueprintGroup.test_BlueprintGroup_middleware = test_BlueprintGroup_middle

# Generated at 2022-06-14 07:01:37.224900
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test for `BlueprintGroup.middleware` decorator.
    """

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup("/api", "v1")
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware("request")
    async def middleware(request):
        pass

    assert bp1.has_middleware("request", middleware)
    assert bp2.has_middleware("request", middleware)



# Generated at 2022-06-14 07:01:49.072748
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')
    bp3 = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    def func(req):
        return req

    bp3.middleware(func)

    assert len(bp3.blueprints) == 2
    assert len(bp3.blueprints[0].middlewares) == 1
    assert len(bp3.blueprints[1].middlewares) == 1


# Generated at 2022-06-14 07:02:00.604221
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This unit test tests if the middleware method of BlueprintGroup class
    works properly
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:02:13.661853
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup("/api")
    group.append(bp1)
    group.append(bp2)

    counter = 0
    @group.middleware("request")
    async def bp1_middleware(request):
        nonlocal counter
        counter += 1
        print(request)

    @bp1.middleware("request")
    async def bp1_sub_middleware(request):
        nonlocal counter
        counter += 1
        print(request)


# Generated at 2022-06-14 07:02:20.540912
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        pass

    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1

# Generated at 2022-06-14 07:02:32.373742
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/api', version='v1')
    bpg.append(bp1)
    bpg.append(bp2)
    @bpg.middleware()
    async def middleware_for_bpg_only(request): pass
    @bp1.middleware()
    async def middleware_for_bp1_only(request): pass
    for bp in [bp1, bp2]:
        assert len(bp.middlewares['request']) == 2
    assert len(bp1.middlewares['request']) == 2

# Generated at 2022-06-14 07:02:44.015224
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_Blueprint_middleware")

    bp = Blueprint("test_bp")

    @bp.middleware("request")
    async def test_bp_register_middleware(request):
        pass

    group = BlueprintGroup()

    @group.middleware("request")
    async def test_group_register_middleware(request):
        pass

    group.append(bp)

    for blueprint in group:
        for reg_middleware in blueprint.middleware_stack["request"]:
            assert reg_middleware == test_group_register_middleware

    @bp.middleware("response")
    async def test_bp_register_middleware_2(request):
        pass

    for blueprint in group:
        for reg_middleware in blueprint.middleware_stack["response"]:
            assert reg