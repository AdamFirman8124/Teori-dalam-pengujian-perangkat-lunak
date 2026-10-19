

# Generated at 2022-06-14 06:57:18.048465
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This test is used for testing the functionality of middleware() method
    of class BlueprintGroup.
    """

    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        """
        This is a test method to test middleware() method of class BlueprintGroup.
        This is blue print middleware which is registered to only blue print 1.
        """
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 06:57:29.176319
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Setup for the test
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    # Test Cases
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert bp1.middlewares_names.get('request')[0] == group_middleware
    assert bp2.middlewares_names.get('request')[0] == group_middleware

    # Teardown for the test

# Generated at 2022-06-14 06:57:37.392375
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint(name="bp1")
    bp2 = sanic.Blueprint(name="bp2")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        pass

    assert len(bp1.request_middleware) == 2
    assert len(bp2.request_middleware) == 1



# Generated at 2022-06-14 06:57:54.257437
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    original_register_middleware = Blueprint.register_middleware

    def dummy_register_middleware(self, fn):
        self.middleware_stack.append(fn)
        return fn

    Blueprint.register_middleware = dummy_register_middleware

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    def test_middleware(request):
        pass

    group = Blueprint.group(bp1, bp2)

    @group.middleware(*['request'])
    def middleware1(request):
        pass

    @group.middleware('request')
    def middleware2(request):
        pass


# Generated at 2022-06-14 06:57:55.844719
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware
    def _():pass


# Generated at 2022-06-14 06:58:09.847570
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Function to Test `BlueprintGroup` Middleware
    """
    bp1 = sanic.blueprints.Blueprint("bp1", version="v1", url_prefix="/bp1")
    bp2 = sanic.blueprints.Blueprint("bp2", version="v1", url_prefix="/bp2")

    bp3 = sanic.blueprints.Blueprint("bp3", version="v1", url_prefix="/bp4")
    bp4 = sanic.blueprints.Blueprint("bp4", version="v1", url_prefix="/bp5")

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")


# Generated at 2022-06-14 06:58:22.354832
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()

    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    @bpg.middleware('request')
    async def test_middleware(request):
        return text('add_middleware_to_blueprint')

    request, response = app.test_client.get('/bp1')
    assert response

# Generated at 2022-06-14 06:58:27.737645
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Dummy function for unit test
    """


@pytest.mark.asyncio
async def test_BlueprintGroup_middleware_async():
    """
    Dummy async function for unit test
    """

# Generated at 2022-06-14 06:58:41.647307
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup()
    bpg.append(bp3)
    bpg.append(bp4)

    def request_middleware(request):
        request.test = 'test'
    def response_middleware(request, response):
        assert request.test == 'test'

    bpg.middleware(request_middleware)
    bpg.middleware(response_middleware)

    @bp3.route('/')
    async def bp1_route(request):
        assert request.test == 'test'
        return text('bp3')


# Generated at 2022-06-14 06:58:48.949468
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('sanic')
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')

    bpg = BlueprintGroup(bp1)
    bpg.version = '1.0.0'

    @bpg.middleware
    async def middleware(request):
        print('applied on Blueprint : bp1 Only')

    app.blueprint(bpg)


# Generated at 2022-06-14 06:58:57.431746
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup(bp1, bp2)
    @bpg.middleware('request')
    def test_middleware(request):
        pass
    assert bp1.middlewares['request'][0] == test_middleware
    assert bp2.middlewares['request'][0] == test_middleware


# Generated at 2022-06-14 06:59:08.405774
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    from sanic import Blueprint

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert len(bp1.middleware['request']) == 1
    assert len(bp2.middleware['request']) == 1



# Generated at 2022-06-14 06:59:19.649346
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp_group_a = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    bp_group_b = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bp_group_c = BlueprintGroup(bp_group_a, bp_group_b, url_prefix="/api", version="v1")

# Generated at 2022-06-14 06:59:33.089671
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    # BlueprintGroup.middleware method shall try to call middleware method
    # of each of the blueprints that are part of the group.
    # This test ensures that the method middleware of the class Blueprint
    # is called with the passed arguments and below unit test implements
    # the same.
    app = sanic.Sanic()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup('bpg', url_prefix='/bpg')

    #

# Generated at 2022-06-14 06:59:45.399390
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')

    bp = Blueprint(name='fake_blueprint', url_prefix='/fake', version='1.1')
    bp2 = Blueprint(name='fake_blueprint2', url_prefix='/fake2', version='1.2')

    bpg = BlueprintGroup(
        url_prefix='/api', version='1.0', strict_slashes=None
    )
    bpg.append(bp)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def fake_bp_middleware(*args, **kwargs):
        pass

    @bpg.middleware('request', stream=True)
    async def fake_bp_middleware2(*args, **kwargs):
        pass


# Generated at 2022-06-14 06:59:58.950877
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprints.Blueprint.middleware('request')
    async def bad_middleware(request):
        return text('bad middleware')

    @sanic.blueprints.Blueprint.middleware('request')
    async def good_middleware(request):
        return text('good middleware')

    # Create a Sanic application and add blueprints
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp1.middleware(bad_middleware)
    bp2.middleware(good_middleware)
    bp1.add_route(good_middleware, '/', strict_slashes=True)

# Generated at 2022-06-14 07:00:09.356480
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    @app.middleware("request")
    async def common_middleware(request):
        request["scope"]["foo"] = "bar"

    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")

    @bp1.middleware("request")
    async def bp1_middleware(request):
        request["scope"]["foo"] = "bar"

    @bp2.middleware("request")
    async def bp2_middleware(request):
        request["scope"]["foo"] = "bar"

    group = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 07:00:19.955066
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint("bp1")
    bp2 = sanic.Blueprint("bp1")

    bpg = BlueprintGroup("/api")
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware("request")
    async def bp_req_mw(request):
        pass

    @bpg.middleware("response")
    async def bp_res_mw(request, response):
        pass

    assert isinstance(bp1.middlewares["request"], list)
    assert isinstance(bp1.middlewares["response"], list)
    assert isinstance(bp2.middlewares["request"], list)
    assert isinstance(bp2.middlewares["response"], list)
    assert bp_req_mw in bp

# Generated at 2022-06-14 07:00:34.441720
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    @group.middleware()
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 07:00:45.093428
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)
    count = 0

    @group.middleware('request')
    async def bp1_only_middleware(request):
        nonlocal count
        count += 1

    assert len(bp1.middlewares) == 1
    assert len(bp2.middlewares) == 1
    assert count == 0

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        nonlocal count
        count += 1


# Generated at 2022-06-14 07:00:54.170487
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('middleware-test')
    bp = Blueprint('bp')

    @bp.middleware('request')
    async def bp_middleware(request):
        print('applied on Blueprint : bp Only')

    @bp.route('/')
    async def bp_route(request):
        return text('bp')

    group = BlueprintGroup()
    group.append(bp)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp and bp2')

    app.blueprint(group)

    request, response = app.test_client.get('/')
    assert response.status == 200



# Generated at 2022-06-14 07:01:08.200806
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


# Generated at 2022-06-14 07:01:20.482085
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')

    bp = Blueprint('test_BlueprintGroup_middleware_bp', url_prefix='/test_bp')

    bp.middleware('request')(lambda x: x)

    bpGroup = BlueprintGroup(url_prefix='/test_bpGroup')

    bpGroup.append(bp)

    bpGroup.middleware('request')(lambda x: x)

    assert bp.middleware['request'][0]['handler'] == \
        bpGroup.middleware['request'][0]['handler']

    assert isinstance(bpGroup.middleware, dict)
    assert isinstance(bpGroup.middleware['request'], list)


# Generated at 2022-06-14 07:01:28.666567
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp4')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:01:41.204546
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class MockBlueprint(sanic.Blueprint):
        def __init__(self):
            super().__init__("mock")
            self.registered_middleware = []

        def middleware(self, fn, *args, **kwargs):
            self.registered_middleware.append((fn, args, kwargs))

    bp1 = MockBlueprint()
    bp2 = MockBlueprint()
    bp3 = MockBlueprint()
    bp_group = BlueprintGroup()
    bp_group.append(bp1)
    bp_group.append(bp2)

    @bp_group.middleware("request")
    def request_middleware(request):
        pass


# Generated at 2022-06-14 07:01:54.936289
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This test case will test the Blueprint group middleware decorator
    implementation to ensure that the same middleware is applied to
    all the blueprints available in a blueprint group.

    :return: None
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    # Create a BlueprintGroup including bp1 and bp2
    group = BlueprintGroup(url_prefix="/api", version="v1")
    group.extend([bp1, bp2])
    # Apply a decorator using Abstract Class method
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')


# Generated at 2022-06-14 07:02:04.544691
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    blueprint_group = BlueprintGroup()

    blueprint_group.blueprints.append(sanic.Blueprint("test", url_prefix="/test"))

    @blueprint_group.middleware('request')
    async def bp1_only_middleware(request):
        pass

    assert len(blueprint_group.blueprints[0]._middleware['request']) == 1

    blueprint_group = BlueprintGroup()

    blueprint_group.blueprints.append(sanic.Blueprint("test", url_prefix="/test"))

    blueprint_group.middleware(bp1_only_middleware, 'request')

    assert len(blueprint_group.blueprints[0]._middleware['request']) == 1


# Generated at 2022-06-14 07:02:16.201588
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestApp(sanic.Sanic):
        pass

    app = TestApp()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg1 = BlueprintGroup(url_prefix='/group1')
    bpg2 = BlueprintGroup(bp1, bp2, url_prefix='/group2')

    bpg1.append(bp1)
    bpg1.append(bp2)

    @bpg1.middleware('request')
    async def bpg1_only_middleware(request):
        print('applied on Blueprint : bpg1 Only')


# Generated at 2022-06-14 07:02:29.705165
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_blueprint_group')

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/')
    async def bp2_route(request):
        return text('bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        assert request.method == 'GET'

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)


# Generated at 2022-06-14 07:02:37.670496
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    assert len(bp1.middleware_stack) == 0
    assert len(bp2.middleware_stack) == 0


    @bpg.middleware('request')
    async def bp_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert len(bp1.middleware_stack) == 1
    assert len(bp2.middleware_stack) == 1



# Generated at 2022-06-14 07:02:50.331851
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    foo_counter = 0
    bar_counter = 0

    @bpg.middleware('request')
    async def foo_middleware(request):
        nonlocal foo_counter
        foo_counter += 1

    @bpg.middleware('request')
    async def bar_middleware(request):
        nonlocal bar_counter
        bar_counter += 1

    assert foo_counter == 0
    assert bar_counter == 0

    for bp in bpg.blueprints:
        assert bp.middleware_stack["request"][0] == foo_middle

# Generated at 2022-06-14 07:02:56.190590
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    #try to use blueprintGroup's method middleware to register a middleware
    def bp_middleware(request):
        print('bp_middleware')
    bp = BlueprintGroup()
    bp.middleware(bp_middleware)

#add @bp.middleware('request') into middleware method of BlueprintGroup

# Generated at 2022-06-14 07:03:07.271957
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    bp3 = Blueprint('bp3', url_prefix='/bp3')

    @bp3.route('/')
    async def bp3_route(request):
        return text('bp3')


# Generated at 2022-06-14 07:03:17.067599
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class MyBlueprint(sanic.Blueprint):
        def __init__(self):
            super().__init__('my_blueprint')

    bp = MyBlueprint()
    bpg = BlueprintGroup()
    bpg.append(bp)

    @bpg.middleware
    async def bp1_middleware(request):
        print('applied on bp1')

    @bpg.middleware
    async def bp2_middleware(request):
        print('applied on bp2')

    assert len(bp.middlewares['request']) == 2

# Generated at 2022-06-14 07:03:24.120731
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class CustomMiddleware(BaseHTTPMiddleware):
        def __init__(self, request, custom_param=None):
            super().__init__(request)
            self.custom_param = custom_param

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    group = BlueprintGroup(url_prefix='/api', version="v1")
    group.append(bp1)
    group.append(bp2)

    def middleware_fn(request):
        pass

    group.middleware(middleware_fn)
    assert len(bp1.middlewares) == 1
    assert len(bp2.middlewares) == 1


# Generated at 2022-06-14 07:03:36.002296
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Sanic
    from sanic.request import Request
    from sanic.response import HTTPResponse

    app = Sanic()

    class Blueprint(sanic.Blueprint):
        pass

    @app.route("/")
    async def handler(request: Request) -> HTTPResponse:
        return sanic.response.html("Hello")

    blueprint = Blueprint()
    blueprint_group = BlueprintGroup()
    blueprint_group.append(blueprint)

    @blueprint_group.middleware('request')
    async def blueprint_group_middleware(request):
        request["User"] = "Alex"

    @blueprint_group.middleware('response')
    async def blueprint_group_middleware_response(request, response):
        response.text = response.text.replace('World', 'Alex')

   

# Generated at 2022-06-14 07:03:49.624420
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    import asyncio

    class MiddleWare(object):
        def __init__(self):
            self.execution_time = 0

        async def __call__(self, request):
            await asyncio.sleep(0.1)
            self.execution_time += 1
            return

    middleware = MiddleWare()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp1.middleware(middleware)
    bp2.middleware(middleware)

    assert (middleware.execution_time == 0)

    bp1.route('/')(lambda x: None)
    bp2.route('/')(lambda x: None)

    assert (middleware.execution_time == 0)



# Generated at 2022-06-14 07:03:52.742405
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware
    def middleware(request):
        print('middleware')
        return request
    assert middleware is not None

## Unit test for method _sanitize_blueprint of class BlueprintGroup

# Generated at 2022-06-14 07:04:07.247879
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

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

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    app = Sanic('test_BlueprintGroup')

# Generated at 2022-06-14 07:04:17.992454
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Create a Fake App instance to use it with implementation
    """
    app = sanic.Sanic("test_BlueprintGroup_middleware")

    """
    This is a fake implementation of the Blueprint
    """
    class Blueprint:
        def __init__(self, name, url_prefix=None, version=None, strict_slashes=None):
            pass

        def add_middleware(self, middleware, *args, **kwargs):
            pass

    """
    This is a fake implementation of the implementation of
    method middleware of class BlueprintGroup
    """

# Generated at 2022-06-14 07:04:42.758615
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup(bp1, bp2, url_prefix='/api/v1')
    bpg2 = BlueprintGroup(bp3, bp4, url_prefix='/api/v2')
    
    @bpg1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:04:45.952989
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @Blueprint.middleware("request")
    def middleware_fn():
        pass

    assert Blueprint.middlewares["request"] is middleware_fn


# Generated at 2022-06-14 07:04:58.769745
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bpg_only_middleware(request):
        print('applied on BlueprintGroup : bpg Only')

    assert 'bpg_only_middleware' in bp1._middleware['request']
    assert 'bpg_only_middleware' in bp2._middleware['request']
    assert 'bpg_only_middleware' not in bpg._middleware['request']

# Generated at 2022-06-14 07:05:11.566548
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("BlueprintGroupMiddleware")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")
    bp_list = [bp1, bp2]
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.extend(bp_list)
    bpg.append(bp3)
    bpg.insert(3, bp4)

    @bpg.middleware('request')
    async def middleware_for_group(request):
        print('Middleware: middleware_for_group')


# Generated at 2022-06-14 07:05:19.497945
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint

    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    bp4 = Blueprint('bp4')
    bpg = BlueprintGroup()
    bpg.extend([bp1, bp2, bpg])
    bpg.append(bp3)
    bpg.insert(3, bp4)

    @bpg.middleware('response')
    def bpg_middleware(request, response):
        print('response middleware applied for each of blueprints')

    @bpg.middleware('request')
    def bpg_middleware1(request):
        print('request middleware applied for each of blueprints')
        return None


# Generated at 2022-06-14 07:05:20.245076
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass

# Generated at 2022-06-14 07:05:30.103498
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1')
    bp2 = sanic.Blueprint('bp2')
    bp_list = [bp1, bp2]
    bpg = BlueprintGroup()
    bpg._blueprints = bp_list
    @bpg.middleware
    async def bp_middleware(request):
        pass

    for blueprint in bp_list:
        for mw in blueprint._middleware[sanic.request]:
            assert mw.middleware == bp_middleware
            assert mw.args == ()
            assert mw.kwargs == {}


# Generated at 2022-06-14 07:05:38.265966
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp = Blueprint(name ="bp1", url_prefix ="/bp1")
    bp2 = Blueprint(name ="bp2", url_prefix ="/bp2")
    bpg = BlueprintGroup(url_prefix ="/api", version="v1", strict_slashes=True)
    bpg.append(bp)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        pass


# Generated at 2022-06-14 07:05:49.546223
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')
    

# Generated at 2022-06-14 07:06:04.512598
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("Test_BlueprintGroup")

    def upper_case(request):
        return "hello"

    @app.middleware("request")
    def lower_case(request):
        return "hello"

    @app.middleware("request")
    def custom_case(request, config_param):
        return "hello"

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup(bp1, bp2)
    # register a middleware for each blueprint in the blueprint group
    bpg.middleware(upper_case)
    bpg.middleware(lower_case, config_param="yolo")
    bpg.middleware(custom_case, config_param="yolo")

# Generated at 2022-06-14 07:06:45.868499
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    # Create Blueprint Group
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    # Define middleware function
    @bp1.middleware('request')
    def stub(request):
        pass
    # Define middleware function
    @bpg.middleware('request')
    def stub(request):
        pass

    # Assert
    assert len(bp1.listeners['request']) == 2
    assert len(bp2.listeners['request']) == 1


# Generated at 2022-06-14 07:06:58.554173
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1', version='v1')
    bp2 = Blueprint('bp2', url_prefix='/bp2', version='v2')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    group = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v0")


# Generated at 2022-06-14 07:07:11.973113
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp3.middleware('request')
    async def bp3_only_middleware(request):
        print('applied on Blueprint : bp3 Only')
