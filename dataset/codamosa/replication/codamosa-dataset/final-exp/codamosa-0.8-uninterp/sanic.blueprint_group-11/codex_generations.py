

# Generated at 2022-06-14 06:57:33.845727
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("BlueprintGroup")
    bp1 = Blueprint("bp1", url_prefix='/bp1')

    @bp1.route("/bp1")
    async def bp1_handler(request):
        return text("I am bp1")

    bp2 = Blueprint("bp2", url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/group')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.blueprints[0].url_prefix = "/bp1"
    bpg.blueprints[1].url_prefix = "/bp2"

    @bpg.middleware('request')
    async def bp_middleware(request):
        print("applied on Blueprint : bp1 and bp2")

   

# Generated at 2022-06-14 06:57:45.162802
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Mock()
    bp1 = sanic.Blueprint('bp1')
    bp2 = sanic.Blueprint('bp2')
    bp3 = sanic.Blueprint('bp3')
    bp4 = sanic.Blueprint('bp4')
    group = BlueprintGroup('/api/v1')
    group.append(bp1)
    group.append(bp2)
    group.append(BlueprintGroup('/api/v2', version='v2'))
    group[-1].append(bp3)
    group[-1].append(bp4)
    @group.middleware('request')
    def group_middleware(request):
        print('common middleware applied for all groups')

    group_middleware(None)

    assert app.add_route.called

# Generated at 2022-06-14 06:57:55.204606
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class BluePrintGroupTest(BlueprintGroup):
        pass

    bp = sanic.Blueprint('bp', url_prefix='/bp')
    bp_group = BluePrintGroupTest(bp, url_prefix='/group')

    @bp.route('/test')
    async def test(request):
        pass

    @bp_group.middleware('request')
    async def bp_group_middleware(request):
        pass

    assert bp_group.middleware == bp.middleware
    assert 'bp_group_middleware' in bp.middlewares['request']


# Generated at 2022-06-14 06:58:05.762587
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Initialize the application
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    # Define Blueprint
    bp = Blueprint('bp', url_prefix='/bp')
    bpg = BlueprintGroup()
    bpg.append(bp)
    @bpg.middleware('request')
    async def bp_middleware(request):
        pass
    # Assign to app
    app.blueprint(bpg)
    # Assert
    assert len(bp.middlewares['request']) == 1
    assert len(bpg.middlewares['request']) == 0


# Generated at 2022-06-14 06:58:18.666500
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprint.Blueprint.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @sanic.blueprint.Blueprint.route('/')
    async def bp1_route(request):
        return text('bp1')

    @sanic.blueprint.Blueprint.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 06:58:29.054796
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    class MockRequest:
        pass

    class MockBlueprint:
        def __init__(self, url_prefix=None, strict_slashes=None, name=None):
            self._url_prefix = url_prefix
            self._strict_slashes = strict_slashes
            self.name = name
            self.middleware_list = []

        @property
        def url_prefix(self):
            return self._url_prefix

        @property
        def strict_slashes(self):
            return self._strict_slashes

        def middleware(self, fn, *args, **kwargs):
            self.middleware_list.append(fn)

    def middleware_plugin(request: sanic.request.Request) -> None:
        pass


# Generated at 2022-06-14 06:58:38.709761
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def middleware_fn(request):
        return request

    class BlueprintMock:
        def middleware(self, fn, *args, **kwargs):
            assert fn is middleware_fn
            assert args == ('request', )
            assert kwargs == dict(name='middleware_fn')

    bp = BlueprintMock()
    bpg = BlueprintGroup()
    bpg.append(bp)

    @bpg.middleware('request', name='middleware_fn')
    def middleware_fn(request):
        return request

# Generated at 2022-06-14 06:58:51.617353
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    # Blueprint group with url prefix and version
    bpg1 = BlueprintGroup (bp1, url_prefix="/api", version="v1")
    # Blueprint group with url prefix and strict_slashes
    bpg2 = BlueprintGroup (bp2, url_prefix="/api", strict_slashes=True)
    # Blueprint group with version and strict_slashes
    bpg3 = BlueprintGroup (bp3, version="v1", strict_slashes=True)

    # Blueprint group with all parameters

# Generated at 2022-06-14 06:59:02.979768
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bp5 = Blueprint("bp5", url_prefix="/bp5")
    bp6 = Blueprint("bp6", url_prefix="/bp6")

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bpg = BlueprintGroup(bp5, bp6, url_prefix="/api2", version="v2")


# Generated at 2022-06-14 06:59:15.938822
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    bp1 = Blueprint(name='bp1', url_prefix='/bp1')
    bp2 = Blueprint(name='bp2', url_prefix='/bp2')
    bp3 = Blueprint(name='bp3', url_prefix='/bp3')
    bp4 = Blueprint(name='bp4', url_prefix='/bp4')

    bp1.middleware('request', lambda request: True)
    bp2.middleware('request', lambda request: True)
    bp3.middleware('request', lambda request: True)
    bp4.middleware('request', lambda request: True)

    bpg = BlueprintGroup(url_prefix='/bp')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware

# Generated at 2022-06-14 06:59:31.652428
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint
    from sanic import Sanic

    # BlueprintGroup with middleware
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp1, bp2, bp3, bp4)
    app = Sanic(__name__)

    @bp3.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp3 Only')


# Generated at 2022-06-14 06:59:44.651506
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    mock_app = sanic.Sanic()
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    # This middleware should be apply to each of the blueprint
    @bpg.middleware
    async def group_middleware(request):
        print('group middleware applied for Blueprint group')

    mock_app.blue

# Generated at 2022-06-14 06:59:57.272737
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    app = sanic.Sanic(__name__)

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def request_middleware(request):
        pass

    @group.middleware('response')
    async def response_middleware(request, response):
        pass

    assert 1 == len(bp1.request_middleware)
    assert 1 == len(bp2.request_middleware)
    assert 1 == len(bp1.response_middleware)
    assert 1 == len(bp2.response_middleware)

# Generated at 2022-06-14 07:00:00.657678
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware()
    def middleware():
        pass

    assert hasattr(middleware, "__call__")



# Generated at 2022-06-14 07:00:13.778190
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg1 = BlueprintGroup('/api')
    bpg1.append(bp1)
    bpg1.append(bp2)

    @sanic.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint Group : bpg1 Only')

    assert bpg1.middleware == Blueprint.middleware
    bpg1.middleware(bp1_only_middleware)
    assert len(bp1.middleware_functions['request']) == 1
    assert bp1.middleware_functions['request'][0].__name__ == 'bp1_only_middleware'

# Generated at 2022-06-14 07:00:14.605422
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    assert True

# Generated at 2022-06-14 07:00:27.474330
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class ApplicationMock():
        def __init__(self):
            self.middlewares = []
        def add_middleware(self, mw, *args, **kwargs):
            self.middlewares.append((mw, args, kwargs))
        def register_middleware(self, mw, *args, **kwargs):
            self.middlewares.append((mw, args, kwargs))

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp1.app = ApplicationMock()

    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp2.app = ApplicationMock()

    bp2_1 = Blueprint('bp2', url_prefix='/bp2_1')
    bp2_1.app = ApplicationM

# Generated at 2022-06-14 07:00:38.326497
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")

    bp1 = Blueprint("bp1")

    bp2 = Blueprint("bp2")

    bp3 = Blueprint("bp3")

    bp4 = Blueprint("bp4")

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    bpg2 = BlueprintGroup()
    bpg2.append(bp3)
    bpg2.append(bp4)

    bpg.append(bpg2)

    print("=== Test BlueprintGroup.middleware ===")
    @bp2.middleware('request')
    async def bp2_middleware(request):
        print('applied on Blueprint : bp2 Only')


# Generated at 2022-06-14 07:00:50.633231
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.route('/')
    async def test_bp1_only_middleware(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def test_bp2_only_middleware(request, param):
        return text(param)


# Generated at 2022-06-14 07:01:01.570868
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Initialize Blueprints
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    # Initialize BlueprintGroup
    bpg = BlueprintGroup(bp1, bp2)
    
    # Initialize app
    app = Sanic(__name__)
    app.blueprint(bpg)

    # Define middleware
    @bpg.middleware('request')
    async def bpg_middleware_request(request):
        pass

    @bpg.middleware('response')
    async def bpg_middleware_response(request, response):
        pass

    # Define route
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    #

# Generated at 2022-06-14 07:01:12.970381
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        request['param'] = "group_middleware"

    @bp.middleware('request')
    async def bp1_only_middleware(request):
        request['param'] = "bp1_only_middleware"

    @bp.route('/')
    async def bp1_route(request):
        assert request['param'] == "group_middleware"
        assert request['bp'] == bp
        return text(request['param'])

    app = san

# Generated at 2022-06-14 07:01:24.130645
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """
    from unittest.mock import MagicMock
    from sanic import Sanic

    app = Sanic(__name__)
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2', version="v1")
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3', version="v1")

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp2)
    bpg.append(bp3)

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    bp2.middleware = MagicMock()
   

# Generated at 2022-06-14 07:01:32.878540
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    def test_middleware(request):
        return text('Hello from Blueprint Group')

    Blueprint.group(bp1, bp2).middleware(test_middleware)

    for bp in [bp1, bp2]:
        assert bp.middlewares == [test_middleware]



# Generated at 2022-06-14 07:01:42.082046
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="/api")

    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert len(bpg) == 2
    assert bp1.middlewares["request"] == [group_middleware]
    assert bp2.middlewares["request"] == [group_middleware]

# Generated at 2022-06-14 07:01:53.219475
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    bp1 = Blueprint("bp1", url_prefix="/v1")
    bp2 = Blueprint("bp2", url_prefix="/v2")
    bpg = BlueprintGroup()

    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware("request")
    async def middleware_fn1(request):
        print("MiddleWare_Fn1")

    @bp1.middleware("request")
    async def middleware_fn2(request):
        print("MiddleWare_Fn2")

    @bp2.middleware("request")
    async def middleware_fn3(request):
        print("MiddleWare_Fn3")

    app.blueprint(bpg)


# Generated at 2022-06-14 07:02:02.521118
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """

    app = sanic.Sanic()
    bp_group = BlueprintGroup()
    middleware_called = 0

    @bp_group.middleware('response')
    def response_middleware(request, response):
        nonlocal middleware_called
        middleware_called += 1

    @bp_group.route('/', methods=['GET'])
    async def test(request):
        return text('OK')

    app.blueprint(bp_group)
    _, response = app.test_client.get('/')
    assert middleware_called == 1

# Generated at 2022-06-14 07:02:15.224840
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    blueprint1 = sanic.Blueprint('bp1')
    blueprint2 = sanic.Blueprint('bp2')

    blueprint_group = BlueprintGroup()
    blueprint_group.append(blueprint1)
    blueprint_group.append(blueprint2)

    @blueprint_group.middleware('request')
    async def test_middleware(request):
        pass
    assert len(blueprint1.middlewares['request']) == 1
    assert len(blueprint2.middlewares['request']) == 1

    @blueprint_group.middleware('request')
    def test_middleware_no_async(request):
        pass
    assert len(blueprint1.middlewares['request']) == 2

# Generated at 2022-06-14 07:02:28.037401
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """

    app = sanic.Sanic()

    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bpg_middleware(request):
        print('Middleware of BlueprintGroup')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:02:39.640974
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def middleware(request):
        pass

    assert len(bp2.request_middleware) == 1
    assert len(bp2.websocket_middleware) == 0
    assert len(bp2.response_middleware) == 0


# Sanity test for BlueprintGroup

# Generated at 2022-06-14 07:02:47.376306
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create an instance of BlueprintGroup
    bpg = BlueprintGroup()
    # Create a mock BluePrint instance
    bp1 = Mock(spec=sanic.Blueprint)
    bp2 = Mock(spec=sanic.Blueprint)

    # Add them to the BlueprintGroup instance
    bpg.blueprints = [bp1, bp2]

    # Create a dummy Middleware
    async def bp_middleware(request):
        pass

    # Use the BlueprintGroup's middleware method to add a middleware
    bpg.middleware(bp_middleware)

    # Test the assertion
    # Noinspection PyUnresolvedReferences
    bp1.middleware.assert_called_with(bp_middleware, None)
    # Noinspection PyUnresolvedReferences
    bp2.middleware.assert_called_with