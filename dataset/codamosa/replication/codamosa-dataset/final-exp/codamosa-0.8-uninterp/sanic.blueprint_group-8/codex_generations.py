

# Generated at 2022-06-14 06:57:35.325132
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class _app(sanic.Sanic):
        pass

    app = _app()
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    group = BlueprintGroup(bp1, bp2)

    @group.middleware("request")
    async def group_middleware(request):
        print("applied on BlueprintGroup")

    @bp1.middleware("request")
    async def bp1_middleware(request):
        print("applied on Blueprint : bp1")

    @bp2.middleware("request")
    async def bp2_middleware(request):
        print("applied on Blueprint : bp2")

    # Register Blueprint group under the app
    app.blueprint(group)


# Generated at 2022-06-14 06:57:43.998105
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    count = []
    @bpg.middleware
    async def bpg_middleware(request):
        count.append(1)
    for blueprint in bpg.blueprints:
        blueprint.app = Application()
        blueprint.app._middleware.append(blueprint.middleware)
    blueprint = bpg.blueprints[0]
    blueprint.app._request_middleware.append(bpg_middleware)
    blueprint.app._request_middleware.append(bpg_middleware)
    request, __ = blueprint.app.test_client.get(blueprint.url_prefix)

# Generated at 2022-06-14 06:57:56.829872
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("BlueprintGroup_middleware_test")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.middleware("request")
    async def bp1_only_middleware(request):
        print("BP1 Only")

    @bp2.middleware("request")
    async def bp2_only_middleware(request):
        print("BP2 Only")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")


# Generated at 2022-06-14 06:58:10.506787
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bpg1 = BlueprintGroup(bp1,bp2,bp3,bp4,bp5)
    bpg2 = BlueprintGroup(bp1,bp2,bp3,bp4,bp5,url_prefix='/bpg2')
    bpg3 = BlueprintGroup(bpg1,bpg2,url_prefix='/bpg3')
    c = 0

# Generated at 2022-06-14 06:58:21.124443
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test case to check that the middleware can be applied on Blueprint Group.

    :return: None
    """
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bpg = BlueprintGroup(bp1, bp2)
    assert bp1.middlewares == []
    assert bp2.middlewares == []
    @bpg.middleware('request')
    async def fn(request):
        pass
    assert bp1.middlewares == [fn]
    assert bp2.middlewares == [fn]
test_BlueprintGroup_middleware()



# Generated at 2022-06-14 06:58:34.869218
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)


# Generated at 2022-06-14 06:58:47.459852
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Blueprint group setup
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    # Middleware function
    flag = False

    @bpg.middleware('request')
    async def middleware(request):
        nonlocal flag
        flag = True

    assert middleware.__closure__[0].cell_contents == bpg
    assert middleware.__closure__[1].cell_contents == "request"
    assert middleware.__closure__[2].cell_contents == {}

    @bpg.middleware('request', foo="bar")
    async def middleware(request):
        nonlocal flag


# Generated at 2022-06-14 06:58:56.882475
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint1 = Blueprint('bp1', url_prefix='/bp1')
    blueprint2 = Blueprint('bp1', url_prefix='/bp2')
    blueprint_group = BlueprintGroup(blueprint1, blueprint2, url_prefix="/api", version="v1")
    @blueprint_group.middleware
    def middleware(request):
        print('common middleware applied for both bp1 and bp2')
    assert blueprint1.middlewares == [middleware]
    assert blueprint2.middlewares == [middleware]
    assert blueprint_group.middleware == BlueprintGroup.middleware

# Generated at 2022-06-14 06:59:10.365603
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Use two groups containing two blueprints each
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    group = Blueprint.group(bp1, bp2)

    # try to apply middleware to both inners blueprints
    @group.middleware("request")
    async def middleware_bp1_and_bp2(request):
        pass

    # check that it works
    for blueprint in [bp1, bp2]:
        assert blueprint.middlewares["request"] == [middleware_bp1_and_bp2]

    # try to apply middleware only to bp1
    @bp1.middleware("response")
    async def middleware_bp1(request):
        pass

    # check that it works
    assert b

# Generated at 2022-06-14 06:59:21.751477
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        request['mw_applied'] = 'OK'

    assert len(bpg.blueprints) == 2
    assert bpg.blueprints[0].middlewares['request'] == [group_middleware]
    assert bpg.blueprints[1].middlewares['request'] == [group_middleware]

# Generated at 2022-06-14 06:59:33.548573
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    for blueprint in group.blueprints:
        assert blueprint.middlewares['request'][0].partial_func == group_middleware



# Generated at 2022-06-14 06:59:40.733021
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_group = BlueprintGroup()
    blueprint_group.append(Blueprint('bp1', url_prefix='/bp1'))
    blueprint_group.append(Blueprint('bp2', url_prefix='/bp2'))

    @blueprint_group.middleware('request')
    async def bp1_only_middleware(request):
        print('common middleware applied for both bp1 and bp2')

# Generated at 2022-06-14 06:59:51.347337
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    # assert that the middleware of bp1 is not empty
    assert len(bp1.middleware) == 1

    # assert that the middleware of bp2 is not empty
    assert len(bp2.middleware) == 1



# Generated at 2022-06-14 07:00:03.234345
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup(bp1, bp2, url_prefix='/api', version='v1')
    bpg2 = BlueprintGroup(bpg1, bp3, bp4, url_prefix='/api', version='v1')
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

# Generated at 2022-06-14 07:00:11.531698
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("TestBlueprintGroup_middleware")
    blueprint_group = BlueprintGroup(url_prefix='/api', version='v1')
    blueprint = Blueprint("test_bp")
    blueprint_group._blueprints.append(blueprint)

    app.blueprint(blueprint_group)

    @blueprint_group.middleware('request')
    async def bp_middleware(request):
        print("Test Unit Middleware applied with bp")


# Generated at 2022-06-14 07:00:15.044182
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:00:27.769942
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # This function is used to test the BlueprintGroup.middleware method
    # 1. Create a dummy sanic app and blueprint
    # 2. Attach the dummy middleware to the blueprint
    # 3. group the blueprint and fetch the middleware set
    # 4. assert the count of middleware set to be 1.
    # Expected result: count of middleware set to be 1
    bp1 = Blueprint('bp1', url_prefix='/bp1')

    @bp1.middleware('request')
    async def dummy_middleware(request):
        pass

    assert len(bp1.middlewares['request']) == 1

    group = Blueprint.group(bp1)

    @group.middleware('request')
    async def dummy_middleware(request):
        pass


# Generated at 2022-06-14 07:00:39.818401
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Blueprint
    from sanic import response
    from sanic.exceptions import NotFound

    from sanic.response import HTTPResponse
    from sanic.testing import assert_is_not, assert_is_instance, SanicTestClient

    # Verify a middleware added to the blueprint group is applied to each of the
    # blueprint instance.
    async def bp_middleware_test(request, func):
        if request.method == "GET":
            request._test_var = "middleware_test"
        # On GET Request set a new request attribute
        return await func(request)

    bp_a = Blueprint("bp_a", url_prefix="/a")
    bp_b = Blueprint("bp_b", url_prefix="/b")


# Generated at 2022-06-14 07:00:49.935881
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BluePrint_Group")
    bp1 = Blueprint("bp1", url_prefix='/bp1')
    bp2 = Blueprint("bp2", url_prefix='/bp2')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/')
    async def bp2_route(request):
        return text('bp2')

    group = Blueprint.group(bp1, bp2, url_prefix="/api", version="v1")

    @group.middleware('request')
    async def group_middleware(request):
        request['group_middleware'] = True

    @bp1.middleware('request')
    async def bp1_middleware(request):
        request

# Generated at 2022-06-14 07:01:00.179564
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1')
    bp2 = sanic.Blueprint('bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bp_request_middleware(request):
        pass

    assert len(bp1.middleware['request']) == 1
    assert len(bp2.middleware['request']) == 1

    def fn(request):
        pass
    bpg.middleware(fn, 'request')

    assert len(bp1.middleware['request']) == 2
    assert len(bp2.middleware['request']) == 2



# Generated at 2022-06-14 07:01:11.927014
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp3)
    bpg.append(bp4)
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:01:24.484895
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test case for middleware decorator method for BlueprintGroup class.
    """
    mg = Blueprint.group("test1", "test2", "test3")
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    assert len(mg.blueprints) == 3
    assert len(mg.blueprints[0].middlewares) == 0
    assert len(mg.blueprints[1].middlewares) == 0
    assert len(mg.blueprints[2].middlewares) == 0

    @mg.middleware("request")
    async def for_test(request):
        """ Test middleware """
        return

    assert len(mg.blueprints[0].middlewares) == 1
    assert len(mg.blueprints[1].middlewares) == 1

# Generated at 2022-06-14 07:01:28.328648
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware('request')
    def bp_middleware(request):
        print('Executing Blueprint Middleware')
        return

# Generated at 2022-06-14 07:01:40.947704
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Sanic('test_BlueprintGroup_middleware')

    @app.route('/')
    async def handler(request):
        return text('OK')

    bp1 = Blueprint('bp1', url_prefix='/test')
    bp2 = Blueprint('bp2', url_prefix='/test')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    result = []
    @bpg.middleware('request')
    async def common_middleware(request):
        result.append(request.args["a"])

    app.blueprint(bpg)
    request, response = app.test_client.get('/api/test?a=1')
    assert response.text == 'OK'
    assert result == ['1']

    result = []
   

# Generated at 2022-06-14 07:01:49.358004
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bpg = BlueprintGroup()
    bpg.extend([bp1,bp2])

    @bpg.middleware
    async def test_middleware(request):
        pass

    assert bp1.middlewares['request'][-1] == test_middleware
    assert bp2.middlewares['request'][-1] == test_middleware



# Generated at 2022-06-14 07:01:57.616467
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_group = BlueprintGroup()

    blueprint_group.blueprints.append(Blueprint('bp', url_prefix='/bp'))

    @blueprint_group.middleware('request')
    async def common_middleware(request):
        request._group_middleware = True

    @Blueprint.middleware('request')
    async def bp_middleware(request):
        request._bp_middleware = True

    @blueprint_group.blueprints[0].middleware('request')
    async def bp1_middleware(request):
        request._bp1_middleware = True

    @blueprint_group.blueprints[0].route('/')
    async def test_common_middleware(request):
        return text("Ok")

    app = sanic.Sanic("test_BlueprintGroup_middleware")
   

# Generated at 2022-06-14 07:02:06.643484
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Create a blueprint group
    bp_group = BlueprintGroup()

    # Create a blueprint for blueprint group
    bp = Blueprint('test')

    # Set blueprint to blueprint group
    bp_group.append(bp)

    # Modify request of blueprint by applying middleware
    @bp_group.middleware('request')
    async def test_middleware(request):
        request.args['test'] = 'test'

    # Check request on blueprint
    @bp.route('/')
    async def test(request):
        return request.args

    # Create a Sanic app
    app = sanic.Sanic()

    # Register blueprint with sanic app
    app.blueprint(bp)

    # Create sanic test client
    test_client = app.test_client

    # Send a request with arguments

# Generated at 2022-06-14 07:02:13.843429
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This will test the BlueprintGroup.middleware method
    """
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

# Generated at 2022-06-14 07:02:23.101261
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('test', '/')
    bp.middleware.test = bp.middleware(test)

    bpg = BlueprintGroup()
    bpg.append(bp)
    bpg.append(bp)

    @bpg.middleware
    async def bpg_middleware(request):
        pass

    @bpg.middleware('request')
    async def bpg_middleware(request):
        pass

    for bp in bpg.blueprints:
        assert bp.middleware.test



# Generated at 2022-06-14 07:02:32.287347
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    blueprint_group = BlueprintGroup(bp1, bp2, url_prefix="", version="v1")
    blueprint_group.middleware(request_handler, name='request')

    assert isinstance(blueprint_group, BlueprintGroup)

    assert blueprint_group.url_prefix == ''
    assert blueprint_group.version == 'v1'

    blueprint_group.middleware(request_handler, name='request')
    blueprint_group.register(bp3)
    blueprint_group.register(bp4)


# Generated at 2022-06-14 07:02:47.945739
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup(url_prefix='/bpg1')
    bpg2 = BlueprintGroup(url_prefix='/bpg2')
    bpg3 = BlueprintGroup(url_prefix='/bpg3')

    bpg1.append(bp1)
    bpg1.append(bp2)
    bpg2.append(bp3)
    bpg2.append(bp4)
    bpg3.append(bpg1)
    bpg3.append(bpg2)

   

# Generated at 2022-06-14 07:03:01.944330
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Test BlueprintGroup signature.
    bp_group = BlueprintGroup()
    assert callable(bp_group.middleware)

    # Test BlueprintGroup middleware
    app = sanic.Sanic()
    bp_first = Blueprint("first", url_prefix="/first")
    bp_second = Blueprint("second", url_prefix="/second")
    bp_group.append(bp_first)
    bp_group.append(bp_second)
    registered_calls = []

    @bp_group.middleware
    async def middleware(request):
        registered_calls.append(request)

    @bp_first.route("/first")
    async def first_first(request):
        return "First"


# Generated at 2022-06-14 07:03:15.671880
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class app:
        pass

    app.blueprints = []
    app.middleware = []

    @sanic.blueprints.Blueprint.middleware("request")
    async def test_middleware(request):
        pass

    @sanic.blueprints.Blueprint.middleware("response")
    def test_middleware(request):
        pass

    bp = sanic.blueprints.Blueprint('testbp')
    bp.app = app

    bg = BlueprintGroup()
    bg.append(bp)

    @bg.middleware('request')
    async def test_middleware(request):
        pass

    assert(bp.middlewares['request'][0].handler is test_middleware)

    @bg.middleware('response')
    def test_middleware(request):
        pass


# Generated at 2022-06-14 07:03:17.001730
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass


###############################################################################



# Generated at 2022-06-14 07:03:24.055706
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint
    # bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup('/api', 'v1', True)
    bpg.extend([bp3, bp4])

    @bp2.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp3.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:03:35.974544
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint(name='bp1', url_prefix='/bp1')
    bp2 = Blueprint(name='bp2', url_prefix='/bp2')
    bp3 = Blueprint(name='bp3', url_prefix='/bp3')
    bp4 = Blueprint(name='bp4', url_prefix='/bp4')
    bp_group = Blueprint.group(bp1, bp2, url_prefix="/api")
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp_group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')


# Generated at 2022-06-14 07:03:49.624730
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test for BlueprintGroup Middleware method
    :return:
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    # noinspection PyUnusedLocal
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    # noinspection PyUnusedLocal

# Generated at 2022-06-14 07:03:56.769437
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


# Generated at 2022-06-14 07:04:04.655118
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    @group.middleware()
    async def middleware(request):
        return text('bp1')

    assert middleware in bp1.middlewares['request']
    assert middleware in bp2.middlewares['request']


# Generated at 2022-06-14 07:04:12.972183
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    flag = [0, 0]

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
        flag[0] += 1
