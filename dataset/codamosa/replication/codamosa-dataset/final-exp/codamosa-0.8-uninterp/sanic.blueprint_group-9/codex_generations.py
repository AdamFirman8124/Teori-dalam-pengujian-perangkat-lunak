

# Generated at 2022-06-14 06:57:23.713892
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup()
    bpg.append(bp3)
    bpg.append(bp4)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp1.middleware('response')
    async def bp1_only_middleware(request):
        pass


# Generated at 2022-06-14 06:57:36.250593
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("BlueprintGroupTestSuite-test_BlueprintGroup_middleware")

    bp1 = Blueprint("bp1", url_prefix='/bp1')
    bp2 = Blueprint("bp2", url_prefix='/bp2')

    bp3 = Blueprint("bp3", url_prefix='/bp4')
    bp4 = Blueprint("bp4", url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp3)
    bpg.append(bp4)

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:57:49.718679
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestMiddleware:
        def __init__(self, request):
            pass

        async def __call__(self, request):
            pass

    test_app = sanic.Sanic("test_app")
    test_app.blueprint(Blueprint("bp1"))
    test_app.blueprint(Blueprint("bp2"))

    bp_group = BlueprintGroup()
    bp_group.append(test_app.blueprints[0])
    bp_group.append(test_app.blueprints[1])

    @bp_group.middleware(0)
    def bp_group_middleware(request):
        pass

    assert bp_group_middleware._args == (0,)
    bp_group_middleware(TestMiddleware)
    assert test_app.blueprints[0].middlew

# Generated at 2022-06-14 06:57:59.728881
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    for bp in bpg.blueprints:
        assert len(bp.middlewares['request']) == 2

# Generated at 2022-06-14 06:58:08.651068
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    group = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 06:58:21.639630
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp_list = [Blueprint('bp1', url_prefix='/bp1'), Blueprint('bp2', url_prefix='/bp2')]
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.blueprints = bp_list
    assert len(bpg.blueprints) == 2
    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    for blueprint in bpg.blueprints:
        assert len(blueprint.middlewares['request']) == 1

    bp_list = [Blueprint('bp3', url_prefix='/bp3'), Blueprint('bp4', url_prefix='/bp4')]

# Generated at 2022-06-14 06:58:35.064123
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class _app(sanic.Sanic):
        def __init__(self, *args, **kwargs):
            self.blueprints = []
            super(_app, self).__init__(*args, **kwargs)

        def blueprint(self, blueprint, *args, **kwargs):
            self.blueprints.append(blueprint)

    app = _app()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 06:58:47.632690
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    test_bp_middleware_fn_1 = lambda req: print(req)
    test_bp_middleware_fn_2 = lambda req: print(req)
    # Before applying middleware
    assert len(bp1._request_middleware)==0
    assert len(bp2._request_middleware)==0
    assert len(bp1.middleware_functions) == 0
    assert len(bp2.middleware_functions) == 0
    # After applying middleware

# Generated at 2022-06-14 06:58:59.211467
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('TestBlueprintGroup')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware(lambda request: None)

    # Check Blueprint midddleware function has been called 3
    # times: one on bpg, one on bp1 and one on bp2.
    assert bpg._middleware == [lambda request: None]
    assert bp1._middleware == [lambda request: None]
    assert bp2._middleware == [lambda request: None]

# Generated at 2022-06-14 06:59:11.141908
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:59:25.878325
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test: sanic.blueprints.BlueprintGroup - middleware
    """
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup("bpg", url_prefix="/bpg")
    bpg.append(bp1)
    bpg.append(bp2)
    mock = MagicMock()
    bpg.middleware(mock)
    mock.assert_has_calls([call(bp1, mock), call(bp2, mock)], any_order=True)
    mock.reset_mock()
    mock.side_effect = [None, AssertionError]

# Generated at 2022-06-14 06:59:33.410423
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test the method middleware of class BlueprintGroup
    """

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)


# Generated at 2022-06-14 06:59:45.567721
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp5')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:59:56.926414
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/')
    bp2 = Blueprint('bp2', url_prefix='/')
    bp3 = Blueprint('bp3', url_prefix='/')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api")

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert bp1.has_middleware('request')
    assert bp2.has_middleware('request')
    assert not bp3.has_middleware('request')


# Generated at 2022-06-14 07:00:07.753274
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        pass

    @bpg.middleware('request')
    async def group_middleware(request):
        pass

    assert not bp1.has_middleware('request', bp1_only_middleware)
    assert not bp2.has_middleware('request', bp2_only_middleware)

# Generated at 2022-06-14 07:00:17.658848
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    method: test_BlueprintGroup_middleware (class: BlueprintGroup)
    what: test methods middleware in class BlueprintGroup
    expected: 
        - call the func in Blueprint middleware
    """
    # Given
    bp = Blueprint("bp")
    bp_group = BlueprintGroup()
    bp_group.append(bp)
    called = False

    @bp.middleware("request")
    def mid_wrapped():
        nonlocal called
        called = True

    # When
    bp_group.middleware()()

    # Then
    assert called == True



# Generated at 2022-06-14 07:00:31.481799
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class FakeApp(sanic.Sanic):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.middleware = []

        def register_middleware(self, *args, **kwargs):
            self.middleware.append((args, kwargs))

    app = FakeApp()

    middleware_function_a = asyncio.coroutine(lambda x: x)

    # Registers the middleware function for all the blueprints
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = BlueprintGroup()
    bpg = Blueprint.group(bp1, bp2, bp3)


# Generated at 2022-06-14 07:00:42.143499
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    group1 = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    group2 = BlueprintGroup(group1, bp3, url_prefix="/app", version="v2")

    async def bp1_only_middleware(request):
        print('applied on Blueprints : bp1, bp2')


# Generated at 2022-06-14 07:00:52.628665
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    class MockBlueprint:
        def __init__(self):
            self.middlewares = []

        def middleware(self, fn, *args, **kwargs):
            self.middlewares.append((fn, args, kwargs))

    # Create Mock Blueprints
    bp1 = MockBlueprint()
    bp2 = MockBlueprint()

    # Create Blueprint Group
    bpg = BlueprintGroup()

    # Create a dummy middleware
    async def dummy_middleware(request):
        print("dummy middleware executed")
        return True

    # Register middleware
    bpg.middleware(dummy_middleware)

    # Append blueprints
    bpg.append(bp1)
    bpg.append(bp2)

    print(bpg.middlewares)
    assert bpg.middlew

# Generated at 2022-06-14 07:01:07.083707
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.response import text
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1', version=1)
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3', version=2)
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:01:23.497413
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

# Generated at 2022-06-14 07:01:24.492947
# Unit test for method middleware of class BlueprintGroup

# Generated at 2022-06-14 07:01:37.321529
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    def dummy_middleware(request):
        return None

    @bpg.middleware('request')
    def dummy_middleware_request(request):
        return None

    @bpg.middleware('response')
    def dummy_middleware_response(request, response):
        return None

    @bpg.middleware('request', 'response')
    def dummy_middleware_req_response(request, response):
        return None

    assert len(bp1._middleware['request']) == 2
    assert len(bp2._middleware['request']) == 2

# Generated at 2022-06-14 07:01:49.175499
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Verify that we are able to register a middleware
    # for blueprint group with no blueprint registered
    bpg = BlueprintGroup()
    assert len(bpg) == 0
    called = False
    @bpg.middleware()
    def test_middleware(*args, **kwargs):
        nonlocal called
        called = True
    assert called == False

    # Verify that we are able to register a middleware
    # for blueprint group with multiple blueprint registered
    bpg = BlueprintGroup()
    assert len(bpg) == 0
    called = False
    @bpg.middleware()
    def sample_middleware(*args, **kwargs):
        nonlocal called
        called = True
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bpg.append(bp1)
    bpg

# Generated at 2022-06-14 07:01:57.397575
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = sanic.Blueprint("bp1", url_prefix="/bp1", version="v1")
    bp2 = sanic.Blueprint("bp2", url_prefix="/bp2", version="v2")

    bp3 = sanic.Blueprint("bp3", url_prefix="/bp3", version="v3")
    bp4 = sanic.Blueprint("bp4", url_prefix="/bp4", version="v4")

    bpg1 = BlueprintGroup(url_prefix="/api", version="v1")
    bpg1.append(bp3)
    bpg1.append(bp4)

    bpg2 = BlueprintGroup(url_prefix="/api/v1", version="v2")
    bpg2.append(bpg1)
    bpg2

# Generated at 2022-06-14 07:02:05.520635
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bpg_middleware(request):
        pass

    assert len(bp1.handler_functions['request']) == 1
    assert len(bp2.handler_functions['request']) == 1
    assert bpg.middleware.__name__ == 'middleware'
    assert bpg_middleware.__name__ == 'bpg_middleware'



# Generated at 2022-06-14 07:02:16.634091
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def test_function_A(request):
        pass

    def test_function_B(request):
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1', version='v1')
    bp2 = Blueprint('bp2', url_prefix='/bp2', version='v2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v3")

    a_mw = bpg.middleware(test_function_A)
    b_mw = bpg.middleware(test_function_B)
    b_mw = bpg.middleware(test_function_B)

    assert len(bp1.middlewares['request']) == 2
    assert len(bp2.middlewares['request']) == 2


# Generated at 2022-06-14 07:02:25.880018
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    async def bp_middleware(request):
        print('bp_middleware')
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)
    group.middleware(bp_middleware)

    assert bp1.middleware_stack
    assert bp2.middleware_stack

# Generated at 2022-06-14 07:02:34.378655
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bp1_middleware_invoked = False
    bp2_middleware_invoked = False

    bpg = BlueprintGroup('/api', version='v1')
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        nonlocal bp1_middleware_invoked
        bp1_middleware_invoked = True

# Generated at 2022-06-14 07:02:43.044699
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        pass
    assert group_middleware.__name__ == 'group_middleware'
    assert bp1.middlewares['request'] == [group_middleware]
    assert bp2.middlewares['request'] == [group_middleware]

# Generated at 2022-06-14 07:03:00.411897
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    import sanic
    from sanic import Blueprint, response
    from sanic.request import Request


# Generated at 2022-06-14 07:03:09.057047
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.middleware('request')
    def middleware(request):
        pass
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    bpg.append(bp3)
    bpg.append(bp4)

    bpg.middleware(middleware)
    assert middleware in bp1.middlewares['request']
    assert middleware in bp2.middle

# Generated at 2022-06-14 07:03:21.081648
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Blueprint
    app = sanic.Sanic()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version=1)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:03:34.433230
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This test-case is used to verify the Blueprint Group's method
    middleware's functionality.
    """
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")
    bp4 = Blueprint("bp4")
    bpg1 = BlueprintGroup(bp3, bp4)
    bpg2 = BlueprintGroup(bp1, bp2, bpg1)

    @bpg2.middleware("request")
    async def bpg2_middleware(request):
        pass

    for bp in [bp1, bp2, bp3, bp4]:
        assert bp.middleware_handlers["request"]["func"] == bpg2_

# Generated at 2022-06-14 07:03:42.414706
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    async def fake_middleware(*args, **kwargs):
        print("fake_middleware is called")

    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)

    bpg2 = BlueprintGroup(url_prefix="/api2", version="v1")
    bpg2.append(bp3)
    bpg2.append(bp4)

    bpg.append

# Generated at 2022-06-14 07:03:53.316525
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # create a dummy sanic app
    app = sanic.Sanic()
    # create a Blueprint instance
    bp1 = Blueprint('bp1')
    # create a BlueprintGroup instance
    bpg = BlueprintGroup()
    # append Blueprint instance to BlueprintGroup
    bpg.append(bp1)

    # assert method exists
    assert hasattr(bpg, 'middleware')
    # assert middleware method exists and is callable
    assert callable(bpg.middleware)

    # create dummy middleware functions
    async def middleware_a(request):
        pass

    async def middleware_b(request):
        pass

    # call Blueprint.middleware for BlueprintGroup
    bp = bpg.middleware(middleware_a)
    # assert the return value is a partial function
    assert isinstance(bp, partial)


# Generated at 2022-06-14 07:04:02.926049
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    def middleware_func(req):
        return "success"

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    bpg.middleware(middleware_func)

    assert bp1._middleware == [middleware_func]
    assert bp2._middleware == [middleware_func]



# Generated at 2022-06-14 07:04:11.523311
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()

    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    async def group_middleware(request, *args, **kwargs):
        print('common middleware applied for both bp1 and bp2')

    assert len(bp1.middleware_stack) == 1
    assert len(bp2.middleware_stack) == 1

    @bpg.middleware('request')
    async def group_middleware2(request):
        print('common middleware applied for both bp1 and bp2')

    assert len(bp1.middleware_stack) == 2
    assert len

# Generated at 2022-06-14 07:04:17.867093
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api")
    @bpg.middleware('request')
    def bpg_middleware(request):
        pass
    assert hasattr(bp1, 'middlewares')
    assert hasattr(bp2, 'middlewares')

# Generated at 2022-06-14 07:04:28.934600
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/api')
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def middleware_wrapper(request):
        request['middleware'] = True

    assert len(bp1._middleware['request']) == 1
    assert len(bp2._middleware['request']) == 1
    assert bp1._middleware['request'][0]['handler'] == middleware_wrapper
    assert bp2._middleware['request'][0]['handler'] == middleware_wrapper

# Generated at 2022-06-14 07:04:41.978628
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    async def example_middleware(request):
        return response.text("")

    @BlueprintGroup.middleware(name="example_middleware")
    async def example_middleware_2(request):
        return response.text("")

    # test assert
    assert example_middleware.__name__ == "example_middleware"
    assert example_middleware_2.__name__ == "example_middleware_2"


# Generated at 2022-06-14 07:04:47.836754
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
        return

    assert len(bp1.middlewares) == 1
    assert group_middleware in bp1.middlewares['request']

    assert len(bp2.middlewares) == 1
    assert group_middleware in bp2.middlewares['request']


# Generated at 2022-06-14 07:05:01.008880
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    assert bp1._middleware['request'][0] == group_middleware
    assert bp2._middleware['request'][0] == group_middleware

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')
    assert bp2._middleware['request'][0] == group_middleware
    assert bp2._middle

# Generated at 2022-06-14 07:05:14.632899
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')

    group = BlueprintGroup(url_prefix='/group')

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return

# Generated at 2022-06-14 07:05:28.143455
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestMiddlewareClass:
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def middleware(request):
        pass

    assert len(bpg.middlewares.keys()) == 2
    assert len(bpg.middlewares['request']) == 1
    assert bpg.middlewares['request'][0] == middleware

    @bpg.middleware('request')
    async def middleware2(request):
        pass

    assert len(bpg.middlewares['request']) == 2

# Generated at 2022-06-14 07:05:37.446767
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint("bp")
    bpg = BlueprintGroup()
    bpg.append(bp)

    @bp.middleware("request")
    async def bp_middleware(request):
        print("bp_middleware")

    @bpg.middleware("request")
    async def bpg_middleware(request):
        print("bpg_middleware")

    assert len(bp.middlewares["request"]) == 2
    assert len(bpg.middlewares["request"]) == 0

    """
    bpg.middleware("request") is equal to bp.middleware("request")
    bpg.middleware("request")(bp_middleware) is equal to bp.middleware("request")(bp_middleware)
    """
    assert bpg.middlewares["request"] == bp.middle

# Generated at 2022-06-14 07:05:50.069213
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')

    bp1.middleware('request')(lambda request: None)
    bp2.middleware('request')(lambda request: None)

    # Will not get applied here
    bp3.middleware('request')(lambda request: None)

    Blueprint.group(bp1, bp2).middleware('request')(lambda request: None)

    app.blueprint(bp1)
    app.blueprint(bp2)
    app.blueprint(bp3)

    # Apply middleware to the group bp1 and bp2
    assert(len(bp1.middlewares['request']) == 2)

# Generated at 2022-06-14 07:06:04.923036
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This method performs the unit test for `BlueprintGroup.middleware` method

    :return: None
    """
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")


# Generated at 2022-06-14 07:06:13.920019
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    app.config.from_object(__name__)
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    group = BlueprintGroup("/api")
    group.append(bp1)
    group.append(bp2)

    @bp1.route("/route1")
    def test_bp1(request):
        return text("bp1")

    @bp2.route("/route2")
    def test_bp2(request):
        return text("bp2")


# Generated at 2022-06-14 07:06:26.399669
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('bp1_only_middleware')
        request['x'] = 1

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

