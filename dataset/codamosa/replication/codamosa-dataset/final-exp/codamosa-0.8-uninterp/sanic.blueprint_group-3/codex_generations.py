

# Generated at 2022-06-14 06:57:33.845747
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # create BlueprintGroup bpg
    bpg = BlueprintGroup("one", 1, True)

    # create blueprint
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp1.route("/", name="bp1")(lambda x: x)
    bp2.route("/", name="bp2")(lambda x: x)
    bp3.route("/", name="bp3")(lambda x: x)

    # add to BlueprintGroup
    # call method middleware,
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

# Generated at 2022-06-14 06:57:34.475393
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass


# Generated at 2022-06-14 06:57:43.763028
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")
    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    @bp1.middleware("request")
    def bp1_request_middleware(request):
        print("bp1 only middleware applied")

    @bp1.middleware("response")
    def bp1_response_middleware(request, response):
        print("bp1 only middleware applied")


# Generated at 2022-06-14 06:57:56.663728
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 06:58:10.385774
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    # Unit Test for Blueprint Group : middleware
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert bp1.middleware_funcs
    assert len(bp1.middleware_funcs) == 1

# Generated at 2022-06-14 06:58:22.639786
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp4')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 06:58:35.551680
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Sanity test for BlueprintGroup Middleware method

    This test ensures that middleware can be applied across each
    blueprint inside the blueprint group and also ensures that
    the blueprint's own middleware is not broken as well.
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        pass


# Generated at 2022-06-14 06:58:48.272319
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup")
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bpg = BlueprintGroup("bpg")
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware("request")
    async def bpg_middleware(request):
        request["a"] = 1

    @bp1.middleware("request")
    async def bp1_middleware(request):
        request["b"] = 2

    @bp2.middleware("request")
    async def bp2_middleware(request):
        request["c"] = 3

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")


# Generated at 2022-06-14 06:59:00.219425
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


# Generated at 2022-06-14 06:59:05.339709
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        assert True

    assert bp1.has_middleware('request')
    assert bp2.has_middleware('request')
    assert not bp1.has_middleware('response')


# Generated at 2022-06-14 06:59:14.449724
# Unit test for method middleware of class BlueprintGroup

# Generated at 2022-06-14 06:59:27.758003
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    app = sanic.Sanic()
    app.blueprint(bp1)
    app.blueprint(bp2)

    bpg = BlueprintGroup()
    bpg.append(bp3)
    bpg.append(bp4)
    app.blueprint(bpg)
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

# Generated at 2022-06-14 06:59:40.790653
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    @BlueprintGroup.middleware('request')
    async def mw1(request):
        return 'ok'

    @BlueprintGroup.middleware('request')
    @BlueprintGroup.middleware('response')
    async def mw2(request):
        return 'ok'

    @BlueprintGroup.middleware('request')
    async def mw3(request):
        return 'ok'

    @BlueprintGroup.middleware('request')
    @BlueprintGroup.middleware('response')
    async def mw4(request):
        return 'ok'

    @BlueprintGroup.middleware('request', attach_to=app)
    @BlueprintGroup.middleware('response', attach_to=app)
    async def mw5(request):
        return 'ok'

   

# Generated at 2022-06-14 06:59:52.568714
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    The method middleware of the class BlueprintGroup is tested here. The test
    is done by checking the length of the middleware function list against the
    expected length for the blueprint group and blueprint.

    The blueprint object is created with the blueprint group to simulate the
    blueprint group object. The blueprint and blueprint group method is called
    with mock middleware function and the length of the middleware function list
    is captured for assertion.
    """
    blueprint = Blueprint('test')
    blueprint_group = BlueprintGroup(blueprint)
    blueprint_group.middleware(lambda r: 1)
    blueprint.middleware(lambda r: 1)
    assert len(blueprint_group.blueprints[0].middlewares['request']) == 1
    assert len(blueprint.middlewares['request']) == 1

# Generated at 2022-06-14 07:00:00.812318
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_mock = MagicMock()
    blueprint_mock.middleware = MagicMock()
    blueprint_mock2 = MagicMock()
    blueprint_mock2.middleware = MagicMock()
    blueprint_group_mock = BlueprintGroup()
    blueprint_group_mock.blueprints = [blueprint_mock, blueprint_mock2]
    assert blueprint_group_mock.middleware("request")(lambda f: f)
    blueprint_mock.middleware.assert_called_with("request")
    blueprint_mock2.middleware.assert_called_with("request")

# Generated at 2022-06-14 07:00:13.976436
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # arrange
    url_prefix = '/api'
    version = 'v1'
    strict_slashes = True
    blueprints =[
        Blueprint('bp3', url_prefix='/bp3'),
        Blueprint('bp4', url_prefix='/bp4')
    ]
    bpg = BlueprintGroup(url_prefix=url_prefix, version=version, strict_slashes=strict_slashes)
    bpg.append(blueprints[0])
    bpg.append(blueprints[1])
    args = list()
    kwargs = dict()
    def print_middleware(request):
        print("Middleware")
    # act
    bpg.middleware(print_middleware)(*args, **kwargs)
    # assert

# Generated at 2022-06-14 07:00:18.874498
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class MyMiddleware:
        pass
    test_bp = Blueprint("test_bp", url_prefix="/test_bp")
    bpg = BlueprintGroup()
    bpg.append(test_bp)

    @bpg.middleware
    def my_middleware():
        pass

    assert test_bp.handlers["request"][0].__self__ is MyMiddleware

# Generated at 2022-06-14 07:00:32.770157
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint
    from sanic import Sanic

    app = Sanic("test_BlueprintGroup_middleware")

    bpg = BlueprintGroup()

    bp1 = Blueprint("bp1", url_prefix="bp1")
    bp2 = Blueprint("bp2", url_prefix="bp2")
    bp3 = Blueprint("bp3", url_prefix="bp3")
    bp4 = Blueprint("bp4", url_prefix="bp4")

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)

    @bpg.middleware("response")
    async def middleware(request, response):
        response.append_header("Content-Type", "application-json")

    bp1.add

# Generated at 2022-06-14 07:00:43.950286
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    group = Blueprint.group(bp1, bp2)

    # Register Blueprint group under the app
    app.blueprint(group)

    bpg = Blueprint.group(bp3, bp4, url_prefix='/api', version='v1')

    app.blueprint(bpg)

    @app.middleware('request')
    async def bp1_middleware(request):
        print('applied on app')


# Generated at 2022-06-14 07:00:52.453545
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test the BlueprintGroup middleware method to use it as a blueprint
    middleware registration mechanism.
    :return: None
    """

    # Create two fake middleware function
    async def m1(request):
        return text("m1")

    async def m2(request):
        return text("m2")

    # Create new blueprint group
    bp_g = BlueprintGroup()

    # Create Two new blueprint
    bp1 = Blueprint("bp_test")
    bp2 = Blueprint("bp_test2")

    # Add the blueprint to group
    bp_g.append(bp1)
    bp_g.append(bp2)

    # Register middleware for the group
    bp_g.middleware(m1)
    bp_g.middleware(m2)

# Generated at 2022-06-14 07:01:04.467225
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    async def test_middleware(request):
        return

    bp1 = Blueprint('bp1', url_prefix='/bp1')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')
    
    group = Blueprint.group(bp1)

    assert not group.middleware.has_middlewares('request')

    group.middleware(test_middleware)

    assert group.middleware.has_middlewares('request')

# Generated at 2022-06-14 07:01:09.641743
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """
    def test_func(request):
        pass

    blueprint_group = BlueprintGroup()
    blueprint_group.middleware(test_func)

    for blueprint in blueprint_group.blueprints:
        for middleware in blueprint.middlewares:
            assert middleware.handler is test_func



# Generated at 2022-06-14 07:01:19.764098
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert bp1.middlewares['request'][0] == group_middleware
    assert bp2.middlewares['request'][0] == group_middleware

# Generated at 2022-06-14 07:01:24.825490
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    def group_middleware():
        pass

    assert bp1.middleware_stack
    assert bp2.middleware_stack
    assert group.middleware_stack is None
    assert group.middleware_stack is None


# Generated at 2022-06-14 07:01:33.290450
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    def middleware_func(request):
        pass

    assert bp1.middlewares[0] == middleware_func
    assert bp2.middlewares[0] == middleware_func


# Generated at 2022-06-14 07:01:42.923111
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Blueprint

    bp_group = BlueprintGroup()
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        pass

    bp_group.append(bp1)
    bp_group.append(bp2)

    @bp_group.middleware('request')
    async def bp_group_only_middleware(request):
        pass

    assert len(bp1.middlewares['request']) == 2

# Generated at 2022-06-14 07:01:53.890713
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Sanic("Test_Sanic_Blueprint_Group_Middleware")

    bp1 = Blueprint("Test_Sanic_Blueprint_Group_Middleware_1", url_prefix='/bp1')

    bp2 = Blueprint("Test_Sanic_Blueprint_Group_Middleware_2", url_prefix='/bp2')

    bp3 = Blueprint("Test_Sanic_Blueprint_Group_Middleware_3", url_prefix='/bp3')

    bp4 = Blueprint("Test_Sanic_Blueprint_Group_Middleware_4", url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/test_blueprint_group", version="v1")

    bpg.append(bp1)

    bpg.append(bp2)

    bp1_middleware_count = 0

# Generated at 2022-06-14 07:02:04.654196
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware('request')
    async def request_middleware(request: sanic.request.Request):
        request['test_Blueprint_middleware_request'] = True

    @BlueprintGroup.middleware('response')
    async def response_middleware(request: sanic.request.Request, response):
        response.headers['test_Blueprint_middleware_response'] = True

    @BlueprintGroup.middleware('error')
    async def error_middleware(request: sanic.request.Request, exception):
        request['test_Blueprint_middleware_error'] = True

    bp_group = BlueprintGroup(url_prefix='/v1' )
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp_group.append(bp1)

    # bp1

# Generated at 2022-06-14 07:02:14.197597
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    # Register Blueprint group under the app
    app.blueprint(bpg)

# Generated at 2022-06-14 07:02:27.623810
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Init Blueprint group and blueprints
    bg = BlueprintGroup()
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp1')
    bp3 = Blueprint('bp1')
    bg.append(bp1)
    bg.append(bp2)
    bg.append(bp3)

    # Init Middleware
    middleware_list = []
    def middleware(request, response):
        middleware_list.append(request)

    # Call middleware
    bg.middleware(middleware)

    # Assert middleware applied to all blueprints
    assert middleware in bp1.middlewares['request']
    assert middleware in bp2.middlewares['request']
    assert middleware in bp3.middlewares['request']
    assert middleware not in b

# Generated at 2022-06-14 07:02:36.670353
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert bpg.version == "v1"
    assert bpg.url_prefix == "/api"
    assert bpg.strict_slashes is None



# Generated at 2022-06-14 07:02:47.551475
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    from sanic.app import Sanic
    from sanic.blueprints import Blueprint

    url_prefix = '/api'
    version = 1
    strict_slashes = True

    app = Sanic('test_BlueprintGroup___getitem__')
    bp_one = Blueprint('bp_one')
    bp_two = Blueprint('bp_two')
    bp_three = Blueprint('bp_three')

    group = BlueprintGroup(url_prefix=url_prefix, version=version,
                           strict_slashes=strict_slashes)
    group.extend([bp_one, bp_two, bp_three])

    assert bp_one == group[0]
    assert bp_two == group[1]
    assert bp_three == group[2]


# Generated at 2022-06-14 07:02:51.446465
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    blueprint_group_object = BlueprintGroup()
    blueprint_group_object.blueprints = [1, 2]
    blueprint_group__len = blueprint_group_object.__len__()
    assert blueprint_group__len == 2

# Generated at 2022-06-14 07:02:58.352756
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    bpg = BlueprintGroup(url_prefix='/api')
    bpg.append(bp1)
    bpg.append(bp2)
    
    assert len(bpg) == 2



# Generated at 2022-06-14 07:03:07.016397
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp3)
    bpg.append(bp4)
    assert bpg[0] == bp3
    assert bpg[1] == bp4
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bpg[0] =bp1
    assert bpg[0] == bp1
    assert bpg[1] == bp4


# Generated at 2022-06-14 07:03:15.648654
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp3)
    bpg.append(bp4)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bpg[0] = bp1

    assert bpg[0] == bp1
    assert len(bpg) == 2

    assert bpg._blueprints[0] == bp1


# Generated at 2022-06-14 07:03:23.655998
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    bp4 = Blueprint('bp4')
    bp5 = Blueprint('bp5')

    bp6 = Blueprint('bp6')
    bp7 = Blueprint('bp7')

    bpg_1 = BlueprintGroup()
    bpg_2 = BlueprintGroup()

    for bp in [bp1, bp2, bp3, bp4, bp5]:
        bpg_1.append(bp)

    for bp in [bp6, bp7]:
        bpg_2.append(bp)

    assert bpg_1[0] == bp1
    assert bpg_1[-1] == bp5


# Generated at 2022-06-14 07:03:29.690826
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    for _bp in [bp1, bp2]:
        bpg.append(_bp)
    assert len(bpg) == 2


# Generated at 2022-06-14 07:03:35.070078
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bg = BlueprintGroup()
    b1 = Blueprint('b1')
    b2 = Blueprint('b2')
    bg.append(b1)
    bg.append(b2)
    assert bg[0] == b1
    assert bg[1] == b2


# Generated at 2022-06-14 07:03:41.600001
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)
    assert group[0] == bp1
    assert group[1] == bp2
