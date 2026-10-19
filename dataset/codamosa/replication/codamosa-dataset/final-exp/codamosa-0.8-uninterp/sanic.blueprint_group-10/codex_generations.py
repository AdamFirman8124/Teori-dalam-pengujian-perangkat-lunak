

# Generated at 2022-06-14 06:57:41.543450
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp3 and bp4')

    @bp3.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:57:53.549681
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    BlueprintGroup.middleware() should apply a middleware to each of the
    blueprint in the blueprint group.
    """
    app = sanic.Sanic()

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bpg1 = BlueprintGroup(url_prefix="", version="")
    bpg1.append(bp1)
    bpg1.append(bp2)

    bpg2 = BlueprintGroup(url_prefix="/bpg2", version="v1")
    bpg2.append(bp3)
    bpg2.append(bp4)
    bpg

# Generated at 2022-06-14 06:58:00.447320
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')
    bp7 = Blueprint('bp7', url_prefix='/bp7')
    bp8 = Blueprint('bp8', url_prefix='/bp8')
    bp9 = Blueprint('bp9', url_prefix='/bp9')
    bp10 = Blueprint('bp10', url_prefix='/bp10')

# Generated at 2022-06-14 06:58:06.734868
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bpg.middleware('request')(lambda x: None)
    assert bp3.middlewares[0].middleware is bpg.middlewares[0].middleware
    assert bp4.middlewares[0].middleware is bpg.middlewares[0].middleware



# Generated at 2022-06-14 06:58:20.035291
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Sanic
    from sanic import Blueprint
    from sanic.response import text
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

# Generated at 2022-06-14 06:58:29.004690
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bpg_middleware(request):
        print('bpg middleware to be applied')

    app = sanic.Sanic(__file__)

    app.blueprint(bpg)

    request, response = app.test_client

# Generated at 2022-06-14 06:58:43.268957
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Create the Blueprint Group for testing
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")
    bp5 = Blueprint("bp5", url_prefix="/bp5")

    bpg1 = BlueprintGroup(url_prefix="/bpg1")
    bpg1.append(bp1)
    bpg1.append(bp2)

    bpg2 = BlueprintGroup(url_prefix="/bpg2")
    bpg2.append(bp3)
    bpg2.append(bp4)

    bpg3 = BlueprintGroup(url_prefix="/bpg3")

# Generated at 2022-06-14 06:58:51.812999
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    url_prefix = '/api/v1'  # URL prefix for the current group of blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix='/api', version='v1')
    bpg2 = BlueprintGroup(bp3, bp4, url_prefix='/api', version='v1')


    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 06:58:59.931238
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint(__name__, url_prefix='/bp1')
    bp2 = Blueprint(__name__, url_prefix='/bp2')

    bp3 = Blueprint(__name__, url_prefix='/bp3')
    bp4 = Blueprint(__name__, url_prefix='/bp4')

    bp5 = Blueprint(__name__, url_prefix='/bp5')
    bp6 = Blueprint(__name__, url_prefix='/bp6')

    bp7 = Blueprint(__name__, url_prefix='/bp7')
    bp8 = Blueprint(__name__, url_prefix='/bp8')

    group1 = BlueprintGroup(url_prefix='/api/v1')
    group1.append(bp1)
    group1.append(bp2)

   

# Generated at 2022-06-14 06:59:06.970419
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("blueprint-group-middleware-test")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bpg = BlueprintGroup(bp1, bp2)

    @bpg.middleware("request")
    async def bpg_middleware(request):
        request.ctx.data = 1
        return await request.app.config.request_middleware(request)

    @bp1.middleware("request")
    async def bp1_middleware(request):
        assert request.ctx.data == 1
        return await request.app.config.request_middleware(request)


# Generated at 2022-06-14 06:59:24.037170
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Mock()
    bp1 = Blueprint("test", url_prefix="/test")
    bp2 = Blueprint("test1", url_prefix="/test1")
    bp_group = BlueprintGroup().append(bp1).append(bp2)
    bpg_middleware = Mock()
    bp1_middleware = Mock()
    bp2_middleware = Mock()

    bp_group.middleware(bpg_middleware)
    bp1.middleware(bp1_middleware)
    bp2.middleware(bp2_middleware)

    bp1.register(app, url_prefix="/test")
    bpg_middleware.assert_called_once()
    bp1_middleware.assert_called_once()
    bp2_middleware.assert_not_called()

   

# Generated at 2022-06-14 06:59:32.732317
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    test_bp = Blueprint('bp1', url_prefix='/bp1')

    @test_bp.middleware('request')
    def test_bp_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    test_bp2 = Blueprint('bp2', url_prefix='/bp2')

    @test_bp2.middleware('request')
    def test_bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    test_bpg = BlueprintGroup(test_bp, test_bp2, url_prefix="/api", version="v1")

    @test_bpg.middleware('request')
    def test_bp_bpg_middleware(request):
        print('applied on Blueprint : bp1 and bp2')

    expected_

# Generated at 2022-06-14 06:59:44.360435
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestGroup(BlueprintGroup):
        def __init__(self):
            super().__init__(None, None, None)
            bp1 = Blueprint("bp1", url_prefix="/bp1")
            bp2 = Blueprint("bp2", url_prefix="/bp2")
            self.blueprints.append(bp1)
            self.blueprints.append(bp2)

    group = TestGroup()

    @group.middleware("request")
    async def bp1_only_middleware(request):
        print("applied on Blueprint : bp1 Only")

    assert len(group.blueprints[0].middlewares) == 1
    assert len(group.blueprints[1].middlewares) == 0

# Generated at 2022-06-14 06:59:57.869087
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint

    class DummyMiddleware:
        def __init__(self, request):
            self.request = request

        async def __call__(self, request):
            return await self.request("Middleware Called")

    @DummyMiddleware.register("response")
    async def DummyMiddleware2(request, response):
        return await response("Middleware 2 Called ")

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")

    @bp2.route("/<param>")
    async def bp2_route(request, param):
        return text(param)

   

# Generated at 2022-06-14 07:00:09.073951
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test for middleware method of class BlueprintGroup
    """
    bp1 = Blueprint('bp1', strict_slashes=True)

    bpg = BlueprintGroup(strict_slashes=True)
    bpg.append(bp1)

    @bpg.middleware
    async def request_middleware(request):
        print('request_middleware invoked')

    assert (
        bp1._middleware['request'][0][0] == request_middleware
    ), 'Middleware function should be added in blueprint bp1'
    assert (
        bp1._strict_slashes
    ), 'strict_slashes of blueprint bp1 should be True'
    bp1_request_middleware_handler = bp1.middleware(None, 'request')[0]

# Generated at 2022-06-14 07:00:16.472004
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint = Blueprint("test", url_prefix="/test")
    blueprint_group = BlueprintGroup(url_prefix="/blueprint_group")
    blueprint_group.append(blueprint)
    blueprint_group.middleware(sanic.request_middleware)

    assert blueprint.middlewares == [sanic.request_middleware]
    assert blueprint_group.middlewares == [sanic.request_middleware]

# Generated at 2022-06-14 07:00:28.069647
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    group1 = Blueprint.group(bp3, bp4)
    group2 = Blueprint

# Generated at 2022-06-14 07:00:40.125268
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestBlueprint(sanic.Blueprint):
        def middleware(self, fn, *args, **kwargs):
            self.test_data.append(args)
            self.test_data.append(fn)

    # Setting up BlueprintGroup object with Blueprint List
    blueprint_group = BlueprintGroup()
    blueprint_group.append(bp=TestBlueprint(name="Test Blueprint 1"))
    blueprint_group.append(bp=TestBlueprint(name="Test Blueprint 2"))

    # Creating and registering the middleware
    @blueprint_group.middleware("request")
    async def my_middleware(request):
        pass

    # Validating the Test Blueprint Object to check if the middleware is applied
    for blueprint in blueprint_group.blueprints:
        assert len(blueprint.test_data) == 2

# Generated at 2022-06-14 07:00:51.659483
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @Blueprint.group.middleware()
    async def middleware(request):
        return text("Middleware Group")

    @Blueprint.middleware(middleware)
    async def middleware_bp(request):
        return text("Middleware BP")

    bp1 = Blueprint("middleware")
    bp2 = Blueprint("bp2")
    bp2.add_route(middleware_bp, "/")
    app = Sanic("test_blueprint_group")
    app.blueprint(bp1)
    app.blueprint(bp2)
    request, response = app.test_client.get("/")
    assert response.text == "Middleware BP"
    request, response = app.test_client.get("/")
    assert response.text == "Middleware BP"



# Generated at 2022-06-14 07:01:06.110912
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.constants import HTTP_METHODS, HTTP_METHODS_BLACKLIST
    from sanic import Blueprint
    from sanic.request import Request
    from sanic.response import HTTPResponse
    from sanic.router import RouteExists

    app = sanic.Sanic("test")

    bp1 = Blueprint("bp1", url_prefix='/bp1')
    bp2 = Blueprint("bp2", url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        request['bp_group'] = 'group'
        assert request['bp_group']


# Generated at 2022-06-14 07:01:25.741690
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """ Test case for blueprint group's method middleware
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = BlueprintGroup(bp1, bp2, url_prefix='/api', version='v1')

    @bp3.middleware('request')
    async def bp3_middleware(request):
        print('applied on Blueprint : bp3')

    assert(len(bp1.middlewares['request']) == 1)
    assert(len(bp2.middlewares['request']) == 1)
    assert(len(bp1.middlewares['response']) == 0)
    assert(len(bp2.middlewares['response']) == 0)


# Generated at 2022-06-14 07:01:38.780285
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp_all = Blueprint('all', url_prefix='/all')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp_group = BlueprintGroup(bp1, bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    @bp_group.middleware('request')
    async def bp_group_only_middleware(request):
        print('applied on Blueprint : bp_group only')


# Generated at 2022-06-14 07:01:50.453942
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from unittest import TestCase, mock
    from sanic import Blueprint
    from sanic.response import text

    class TestBlueprintGroupMiddleware(TestCase):
        def setUp(self):
            self.app = sanic.Sanic("test_BlueprintGroup_middleware")
            self.bp1 = Blueprint("bp1")
            self.bp2 = Blueprint("bp2")
            self.bp_group = BlueprintGroup()
            self.bp_group.append(self.bp1)
            self.bp_group.append(self.bp2)


        @self.bp1.route("/<param>")
        async def bp1_route(request, param):
            return text(param)


# Generated at 2022-06-14 07:02:01.755682
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Sanic('test_BlueprintGroup_middleware')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = BlueprintGroup(bp3, bp4, url_prefix="/bp5")
    bp6 = BlueprintGroup(bp5, bp1, bp2, url_prefix="/bp6")

    group = bp6
    @group.middleware('request')
    async def group_middleware_1(request):
        pass


# Generated at 2022-06-14 07:02:14.675076
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class DummyMiddleware:
        async def __call__(request):
            return True

    app = sanic.Sanic("test_BlueprintGroup_middleware")

    def dummy_func():
        pass

    bp1 = Blueprint("test_bp1")
    bp2 = Blueprint("test_bp2")
    bp3 = Blueprint("test_bp3")

    dummy_group = BlueprintGroup("/api/v1")
    dummy_group.append(bp1)
    dummy_group.append(bp2)

    dummy_group2 = BlueprintGroup("/api/v2")
    dummy_group2.append(bp1)
    dummy_group2.append(bp3)

    dummy_group.middleware(DummyMiddleware)
    dummy_group2.middleware(dummy_func)

    assert b

# Generated at 2022-06-14 07:02:27.900396
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    """
    bp0 = Blueprint('bp0', url_prefix='/bp0')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bpg = BlueprintGroup(bp0, bp1, url_prefix="/api", version="v1")

    @bp0.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp0 Only')

    @bp1.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp0 and bp1')
        assert(bp0.middleware)

# Generated at 2022-06-14 07:02:41.406665
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
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


# Generated at 2022-06-14 07:02:47.858961
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bpg = BlueprintGroup(url_prefix='/test')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg.extend([bp1, bp2])

    @bpg.middleware('request')
    async def my_middleware(request):
        pass

    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1

# Generated at 2022-06-14 07:03:01.275710
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()

    @bp1.route('/<param>')
    async def bp1_route(request, param):
        return text(param)

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert bp1._request_middleware[-1] == group_middleware
    assert bp2

# Generated at 2022-06-14 07:03:14.574061
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp1.middleware_list = []
    bp2.middleware_list = []
    bp_group = BlueprintGroup(bp1,bp2)

    assert bp_group.middleware_list == []
    assert bp1.middleware_list == []
    assert bp2.middleware_list == []

    @bp_group.middleware('request')
    def handler(request):
        return

    assert bp_group.middleware_list == [handler]
    assert bp1.middleware_list == [handler]
    assert bp2.middleware_list == [handler]

    bp_group.middleware_list = []



# Generated at 2022-06-14 07:03:38.382258
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This test verifies the functionality of the `middleware` method of class
    `BlueprintGroup`.
    """
    #
    # Create a Mock object to hook into and verify the expected sequence of
    # method call and the associated arguments.
    #
    mock_blueprint_method_mock = Mock()
    mock_middleware_callable_mock = Mock(return_value="modified_request")

    #
    # Mock the Blueprint prototype to have the `middleware` method
    #
    sanic.blueprints.Blueprint.middleware = mock_blueprint_method_mock
    mock_blueprint_method_mock.return_value = lambda x: x

    #
    # Create a Blueprint Group with two blueprint in it.
    #
    bp1 = Blueprint("bp1")
    bp2 = Blueprint

# Generated at 2022-06-14 07:03:51.261639
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class SanicMock(sanic.Sanic):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.blueprints = None
            self.blueprint = self._blueprint

        def _blueprint(self, bp: "sanic.Blueprint"):
            self.blueprints = bp
            return bp

    def foo_middleware(request):
        pass

    def bar_middleware(request):
        pass

    app = SanicMock()
    bp = BlueprintGroup('bp-group', url_prefix='/api', version="v1")
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp.append

# Generated at 2022-06-14 07:04:02.154070
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    test_app = sanic.Sanic('test_BlueprintGroup_middleware')
    blueprint_group = BlueprintGroup(url_prefix='/bp_one')
    blueprint_group2 = BlueprintGroup(url_prefix='/bp_group2')
    bp = Blueprint('bp1', url_prefix='/bp1', version="v1")
    bp2 = Blueprint('bp2', url_prefix='/bp2', version="v2")

    @blueprint_group.middleware('request')
    async def bp_group_only_middleware(request):
        print('applied on Blueprint Group : bp_group_only_middleware')

    @bp.route('/')
    async def bp_root(request):
        return text('bp_root')


# Generated at 2022-06-14 07:04:10.899123
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        pass

    assert group_middleware in bp1.middlewares['request']
    assert group_middleware in bp2.middlewares['request']

    @group.middleware('response')
    async def group_middleware_response(request, response):
        pass

    assert group_middleware_response in bp1.middlewares['response']
    assert group_middleware_response in bp2.middlewares['response']

# Generated at 2022-06-14 07:04:20.389801
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3)
    bpg.append(bp4)
    bpg.append(bp1)
    bpg.insert(0, bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:04:25.897903
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    bp = Blueprint('bp')
    bpGroup = BlueprintGroup()

    bpGroup.append(bp)

    @bpGroup.middleware
    def method(request):
        pass

    @bpGroup.middleware('request')
    def method(request):
        pass

# Generated at 2022-06-14 07:04:36.485658
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class FakeBlueprint:
        def __init__(self):
            self.middleware = []

        @sanic.blueprints.Blueprint.middleware(self)
        def _middleware(self, fn):
            self.middleware.append(fn)
    bp_list = [FakeBlueprint() for _ in range(5)]
    bpg = BlueprintGroup()
    bpg._blueprints.extend(bp_list)

    @bpg.middleware
    async def middleware():
        pass
    for bp in bpg.blueprints:
        assert len(bp.middleware) == 1

# Generated at 2022-06-14 07:04:45.703573
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bh1 = Blueprint('bp1', url_prefix='/bp1')
    bh2 = Blueprint('bp2', url_prefix='/bp2')

    bh3 = Blueprint('bp3', url_prefix='/bp4')
    bh4 = Blueprint('bp4', url_prefix='/bp4')

    bh5 = Blueprint('bp5', url_prefix='/bp5')
    bh6 = Blueprint('bp6', url_prefix='/bp6')

    bpg_1 = BlueprintGroup(url_prefix="/api", version="v1")
    bpg_1.append(bh1)
    bpg_1.append(bh2)

    bpg_2 = BlueprintGroup(url_prefix="/api", version="v1")
    bpg_2.append(bh3)
    bpg_2.append

# Generated at 2022-06-14 07:04:59.973847
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestApp(sanic.Sanic):
        def test_blueprint_group(self, loop, test_client):
            bp1 = Blueprint("bp1", url_prefix='/bp1')
            bp2 = Blueprint("bp2", url_prefix='/bp2')

            bp3 = Blueprint("bp3", url_prefix='/bp3')
            bp4 = Blueprint("bp4", url_prefix='/bp4')

            bpg = BlueprintGroup(url_prefix="/api", version="v1")
            bpg.append(bp1)
            bpg.append(bp2)
            bpg.append(BlueprintGroup(bp3, bp4, url_prefix="/api/v2"))


# Generated at 2022-06-14 07:05:06.202653
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bg = BlueprintGroup()
    b1 = Blueprint('test1')
    b2 = Blueprint('test2')
    bg.append(b1)
    bg.append(b2)

    # try registering middleware as function
    @bg.middleware
    async def m1(request):
        pass

    assert len(b1.middlewares['request']) == 1
    assert len(b2.middlewares['request']) == 1
    assert b1.middlewares['request'][0].__name__ == 'm1'
    assert b2.middlewares['request'][0].__name__ == 'm1'

    # try registering middleware as decorator