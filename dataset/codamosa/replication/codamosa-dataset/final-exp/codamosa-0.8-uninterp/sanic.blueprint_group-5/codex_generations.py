

# Generated at 2022-06-14 06:57:25.506130
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)

    bp1 = Blueprint("bp1", url_prefix = "/bp1")
    bp2 = Blueprint("bp2", url_prefix = "/bp2")

    bp3 = Blueprint("bp3", url_prefix = "/bp3")
    bp4 = Blueprint("bp4", url_prefix = "/bp4")

    bpg = BlueprintGroup(bp3, bp4, url_prefix = "/api", version = "v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:57:37.390916
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create Blueprint Group
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    # Define Route for all the blueprints
    @bp1.route('/bp1route')
    async def bp1_route(request):
        bp1.app.bp1_route = True
        return text('bp1')
    @bp2.route('/bp2route')
    async def bp2_route(request):
        bp2.app.bp

# Generated at 2022-06-14 06:57:54.257794
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestMiddleware:
        def __init__(self):
            self.name = "Test"
            self.applied = False

        async def __call__(self, request, handler):
            self.applied = True

    @sanic.blueprint.blueprint
    class B1(sanic.Blueprint):
        pass

    @sanic.blueprint.blueprint
    class B2(sanic.Blueprint):
        pass

    b1 = B1('b1', url_prefix='/b1')
    b2 = B2('b2', url_prefix='/b2')
    bg = BlueprintGroup()
    bg.append(b1)
    bg.append(b2)

    middleware = TestMiddleware()


# Generated at 2022-06-14 06:58:08.115209
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp1_bp2_middleware = BlueprintGroup(bp1, bp2)

    @bp1_bp2_middleware.middleware('request')
    async def bp1_bp2_req_middleware(request):
        pass

    @bp1_bp2_middleware.middleware('response')
    async def bp1_bp2_res_middleware(request, response):
        pass

    assert len(bp1.middleware_stack) == 1
    assert len(bp2.middleware_stack) == 1

    # Test that middleware decorator can be used with function parameters

# Generated at 2022-06-14 06:58:21.298253
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint

    bp1 = Blueprint("bp1", url_prefix="/bp1", version="v1")
    bp2 = Blueprint("bp2", url_prefix="/bp2", version="v1")
    bp3 = Blueprint("bp3", url_prefix="/bp3", version="v2")
    bp4 = Blueprint("bp4", url_prefix="/bp4", version="v2")

    bp5 = Blueprint("bp3", url_prefix="/bp3", version="v2")
    bp6 = Blueprint("bp4", url_prefix="/bp4", version="v2")

    bpg = BlueprintGroup()
    bpg.append(bp5)
    bpg.append(bp6)

    app = sanic.Sanic("unit-test-sanic")

    bpg.middleware

# Generated at 2022-06-14 06:58:34.965414
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test case to make sure that middleware decorator of `BlueprintGroup`
    is working as expected.
    """

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup(url_prefix="/api", version="v1")
    group.append(bp1)
    group.append(bp2)

    @group.middleware('request')
    async def group_middleware(request):
        assert request == "request"
        return "middleware"

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 06:58:46.556833
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    async def test_middleware(request):
        pass

    assert bp1.middlewares[0] == test_middleware
    assert bp2.middlewares[0] == test_middleware


# Generated at 2022-06-14 06:58:59.469737
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint("bp", url_prefix="bp")

    bp1 = Blueprint("bp1", url_prefix="bp1")
    bp2 = Blueprint("bp2", url_prefix="bp2")

    bpg = BlueprintGroup(bp1, bp2, url_prefix="bpg")

    @bp.middleware('request')
    async def bp_middleware(request):
        print('applied on Blueprint : bp')

    @bp1.middleware('request')
    async def test_blueprint_middleware(request):
        print('applied on Blueprint : bp1')

    @bp2.middleware('request')
    async def test_blueprint_middleware(request):
        print('applied on Blueprint : bp2')


# Generated at 2022-06-14 06:59:11.188373
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup(bp1,bp2)
    bpg2 = BlueprintGroup(bp3,bp4)
    bpg3 = BlueprintGroup(bpg1,bpg2)

    @bpg1.middleware('request')
    async def bpg1_only_middleware(request):
        print('applied on Blueprint Group : bp1 Only')


# Generated at 2022-06-14 06:59:23.989574
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')


# Generated at 2022-06-14 06:59:41.492782
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    print(__name__)
    app = sanic.Sanic()
    app.config.KEEP_ALIVE = False

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

   

# Generated at 2022-06-14 06:59:49.561229
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg1 = BlueprintGroup(bp1, bp2, url_prefix='/bpg1')
    bpg2 = BlueprintGroup(bp3, bp4, url_prefix='/bpg2')

    item = {}

    @bpg1.middleware('request')
    def middleware_for_blueprint_group1(request):
        item['bpg1'] = True

    @bpg2.middleware('request')
    def middleware_for_blueprint_group2(request):
        item

# Generated at 2022-06-14 07:00:01.629608
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    async def middleware_plugin(request):
        return text('middleware_plugin')

    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware(middleware_plugin)

    assert len(bp1.middlewares) == 1
    assert len(bp2.middlewares) == 1

    # The assertion has to be separated for each custom exception handler.
    assert middleware_plugin == bp1.middlewares[0]["request"][0][1]
    assert middleware_plugin == bp2.middlewares[0]["request"][0][1]

    bpg.middleware(middleware_plugin, 'request', 'error')
   

# Generated at 2022-06-14 07:00:15.044408
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test")

    # Create the BlueprintGroup
    bpg = BlueprintGroup("/api", "v1")

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp1.middleware("request")(lambda x: "1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp2.middleware("request")(lambda x: "2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp3.middleware("request")(lambda x: "3")

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    # Add the BlueprintGroup to the APP
    app.blueprint(bpg)
    # Now apply the middleware

# Generated at 2022-06-14 07:00:27.768869
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test BlueprintGroup middleware
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    @bp1.route('/1')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/2')
    async def bp2_route(request):
        return text('bp2')    

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bpg_middleware(request):
        return text('bpg')


# Generated at 2022-06-14 07:00:36.734043
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bpg = BlueprintGroup()

    # Create a new blueprint for unit testing
    bp1 = Blueprint('bp1', url_prefix='/bp1')

    # Associate the created blueprint with the blueprint group
    bpg.append(bp1)

    # Unit test if the blueprint's middleware is registered
    async def middleware_func(request):
        print('applied on Blueprint : bp1 Only')

    assert 0 == len(bp1._middlewares['request'])
    bpg.middleware(middleware_func)
    assert 1 == len(bp1._middlewares['request'])



# Generated at 2022-06-14 07:00:50.023595
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class _test_bp(sanic.Blueprint):
        pass

    bp = _test_bp("test")

    @bp.middleware("request")
    async def middleware(request):
        pass

    # sanity check - it should be one middleware
    data = bp.get_middlewares("request")
    assert len(data) == 1

    @bp.middleware("request")
    async def middleware2(request):
        pass

    # sanity check - it should be two middleware now
    data = bp.get_middlewares("request")
    assert len(data) == 2

    bpg = BlueprintGroup()
    bpg.append(bp)

    @bpg.middleware("request")
    async def middleware3(request):
        pass

    # sanity check - it should be three middleware

# Generated at 2022-06-14 07:01:01.455715
# Unit test for method middleware of class BlueprintGroup

# Generated at 2022-06-14 07:01:11.383910
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = sanic.Blueprint('bp1')
    bp2 = sanic.Blueprint('bp2')
    bpg1 = BlueprintGroup()
    bpg1.append(bp1)
    bpg1.append(bp2)

    @bpg1.middleware('request')
    async def middleware(request):
        print('applied on Blueprint : bp1 and bp2')

    bp3 = BlueprintGroup()
    bpg2 = BlueprintGroup()
    bp3.append(bp1)
    bp3.append(bp2)

    @bp3.middleware('request')
    async def bp3_middleware(request):
        print('applied on Blueprint : bp1 and bp2')


# Generated at 2022-06-14 07:01:17.494769
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp_a = Blueprint("bp_a")
    bp_b = Blueprint("bp_b")
    bp_c = Blueprint("bp_c")

    bp_g_a = BlueprintGroup(bp_a, bp_b)
    bp_g_b = BlueprintGroup(bp_c, bp_g_a)

    @bp_g_b.middleware()
    def middleware(request):
        pass

    @bp_b.middleware()
    def middleware_b(request):
        pass

    @bp_c.middleware()
    def middleware_c(request):
        pass

    assert bp_a.middlewares == [middleware]
    assert bp_b.middlewares == [middleware, middleware_b]
    assert bp_c.middlewares

# Generated at 2022-06-14 07:01:39.637166
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_group = BlueprintGroup(url_prefix='/api')
    blueprint_group.append(Blueprint('bp1', url_prefix='/bp1'))
    blueprint_group.append(Blueprint('bp2', url_prefix='/bp2'))

    @blueprint_group.middleware('request')
    async def modify_request(request):
        """This is a testing method"""
        request['test'] = 'test_modify_request'

    assert blueprint_group[0].middlewares['request'][0][0] == modify_request
    assert blueprint_group[0].middlewares['request'][0][1] == []
    assert blueprint_group[0].middlewares['request'][0][2] == {}

    assert blueprint_group[1].middlewares['request'][0][0] == modify_

# Generated at 2022-06-14 07:01:53.117327
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
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


# Generated at 2022-06-14 07:02:04.047050
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create a blueprint group
    group = BlueprintGroup()
    app = sanic.Sanic()

    # Create two blueprints to be added to group
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    # Register blueprint group in the app
    app.blueprint(group)

    # Create a fake request handler
    @bp1.route('/')
    async def bp1_route(request):
        pass

    @bp2.route('/')
    async def bp2_route(request):
        pass

    # Define a fake middleware
    async def fake_middleware(request):
        pass

    # Apply middleware to blueprint group
    group.middleware(fake_middleware)

    # Add blueprints

# Generated at 2022-06-14 07:02:15.958174
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_group = BlueprintGroup()

    blueprint_group.blueprints = [
        sanic.blueprints.Blueprint('bp1', url_prefix='/bp1'),
        sanic.blueprints.Blueprint('bp2', url_prefix='/bp2'),
        sanic.blueprints.Blueprint('bp3', url_prefix='/bp3')
    ]

    @blueprint_group.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @blueprint_group.middleware('response')
    async def bp2_only_middleware(request, response):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:02:17.516175
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass

# Generated at 2022-06-14 07:02:19.543785
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware('request')
    def test_middleware(request):
        pass
    assert isinstance(test_middleware, partial)
    assert len(test_middleware.args) == 1
    assert test_middleware.keywords == {'event_type': 'request'}

# Generated at 2022-06-14 07:02:31.524574
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprint()
    def bp1():
        return sanic.Blueprint('bp1', url_prefix='/bp1')

    @sanic.blueprint()
    def bp2():
        return sanic.Blueprint('bp2', url_prefix='/bp2')


    @sanic.blueprint()
    def bp3():
        return sanic.Blueprint('bp3', url_prefix='/bp3')

    @sanic.blueprint()
    def bp4():
        return sanic.Blueprint('bp4', url_prefix='/bp4')

    bp1 = bp1() 
    bp2 = bp2()
    bp3 = bp3()
    bp4 = bp4()
    

    # step 1: sanity the blueprint group
   

# Generated at 2022-06-14 07:02:34.433542
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    BlueprintGroup.middleware.__code__ == sanic.blueprints.Blueprint.middleware.__code__


# Generated at 2022-06-14 07:02:46.453489
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

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:03:00.546694
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bp3 = sanic.Blueprint('bp3', url_prefix='/bp1')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp2')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print(
            'applied on Blueprint : bp1 Only'
        )  # pragma: no cover


# Generated at 2022-06-14 07:03:18.933500
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    tbg = BlueprintGroup(bp1, bp2)
    del tbg[0]
    return len(tbg)


# Generated at 2022-06-14 07:03:26.726198
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    """
    Test method __len__ of class BlueprintGroup
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()

    bpg.append(bp1)
    bpg.append(bp2)

    assert len(bpg) == 2



# Generated at 2022-06-14 07:03:33.874508
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    """
    Test Blueprint group constructor to validate the attributes
    """
    bpg = BlueprintGroup(url_prefix="/api", version="v1", strict_slashes=True)

    assert bpg.url_prefix == "/api"
    assert bpg.version == "v1"
    assert bpg.strict_slashes is True

# Unit Test for custom iter implementation used by the class Blueprint Group

# Generated at 2022-06-14 07:03:39.004388
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bpg = BlueprintGroup()

    assert len(bpg) == 0

    bpg.append(bp1)
    assert len(bpg) == 1

    bpg.append(bp2)
    assert len(bpg) == 2

# Generated at 2022-06-14 07:03:42.763563
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    """
    BlueprintGroup.append() method should add the blueprint to collection
    """
    bp = Blueprint("bp", url_prefix="/bp")
    BlueprintGroup().append(bp)
    assert bp in BlueprintGroup().blueprints

# Generated at 2022-06-14 07:03:54.394727
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    BlueprintGroup.middleware()
    """
    from sanic.blueprints import Blueprint

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp3', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print("applied on Blueprint : bpg Only")

    return bpg.middleware


# Generated at 2022-06-14 07:04:06.123815
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    """
    Unit test for method __delitem__ of class BlueprintGroup
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    assert bpg[0] is bp1
    assert bpg[1] is bp2
    del bpg[0]
    assert bpg[0] is bp2
    del bpg[0]
    assert len(bpg) is 0
    assert bpg.url_prefix is '/api'
    assert bpg.version is 'v1'
    assert bpg.strict_slashes is None

#

# Generated at 2022-06-14 07:04:18.878097
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    """
    Create a new Blueprint Group
    """
    bp = BlueprintGroup(url_prefix="/api/v1", version="v1", strict_slashes=True)
    assert bp.url_prefix == "/api/v1"
    assert bp.version == "v1"
    assert bp.strict_slashes == True
    bp = BlueprintGroup(url_prefix="/api/v2", version="v2", strict_slashes=False)
    assert bp.url_prefix == "/api/v2"
    assert bp.version == "v2"
    assert bp.strict_slashes == False
    bp = BlueprintGroup()
    assert bp.url_prefix == None
    assert bp.version == None
    assert bp.strict_slashes == None


# Generated at 2022-06-14 07:04:29.738820
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    assert bpg.__getitem__(0) == bp1
    assert bpg.__getitem__(1) == bp2
    assert bpg.__getitem__(2) == bp3


# Generated at 2022-06-14 07:04:42.651332
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    from sanic.testing import SanicTestClient
    from sanic import Sanic

    app = Sanic("sanic-blueprint-group-test")

    @app.route("/")
    async def handler(request):
        return text("OK")

    bp1 = Blueprint("bp1", url_prefix="/bp1")

    # Add the route to bp1
    @bp1.route("/")
    async def bp1_handler(request):
        return text("BP1")

    bp2 = Blueprint("bp2", url_prefix="/bp2", strict_slashes=False)

    # Add the route to bp2
    @bp2.route("/v1")
    async def bp2_handler(request):
        return text("BP2")

    # Use BlueprintGroup to combine bp1 and bp

# Generated at 2022-06-14 07:05:03.986000
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    bpg = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 07:05:15.157906
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    """
    The blueprint group should be iterable as a list/tuple
    """
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    iterator = iter(bpg)
    assert iterator == iter(bpg._blueprints)



# Generated at 2022-06-14 07:05:23.543526
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert bpg.__len__() == 0

    bpg.append(bp1)
    bpg.append(bp2)
    assert bpg.__len__() == 2
    assert len(bpg) == 2


# Generated at 2022-06-14 07:05:34.673583
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    from sanic.blueprints import Blueprint

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()

    bpg.append(bp1)
    assert bpg.blueprints == [bp1]

    bpg.append(bp2)
    assert bpg.blueprints == [bp1, bp2]

    bpg.insert(0, bp2)
    assert bpg.blueprints == [bp2, bp1, bp2]

    bpg.insert(2, bp1)
    assert bpg.blueprints == [bp2, bp1, bp1, bp2]

test_BlueprintGroup_insert()

# Generated at 2022-06-14 07:05:39.302949
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    assert BlueprintGroup(url_prefix="/bp1").url_prefix == "/bp1"
    assert BlueprintGroup(version="v1").version == "v1"
    assert BlueprintGroup(strict_slashes=True).strict_slashes is True
    assert BlueprintGroup().strict_slashes is None


# Generated at 2022-06-14 07:05:48.280366
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    group = BlueprintGroup(bp1, bp2, url_prefix="/api")
    assert group[0].name == "bp1"
    assert group[1].name == "bp2"
    assert group[0].url_prefix == "/api/bp1"
    assert group[1].url_prefix == "/api/bp2"


# Generated at 2022-06-14 07:06:02.765955
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1', version="v1")
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp1.route('/')
    async def bp1_route(request):
        pass

    bp1._add_route(bp1._get_route_from(bp1_route), bp1_route)

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        pass

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        pass


# Generated at 2022-06-14 07:06:13.171376
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    url_prefix = "/v1/api/test"
    bg = BlueprintGroup(url_prefix=url_prefix, version="v1", strict_slashes=True)
    assert len(bg) == 0, "Blueprint group has no blueprints to start with"
    bp = Blueprint("bp1")
    new_bp = Blueprint("bp2")
    bg.append(bp)
    bg[0] = new_bp
    assert bg[0] == new_bp
    assert bg[0].url_prefix == bp.url_prefix, "Blueprint's URL Prefix should be same"
    assert bg[0].version == "v1"
    assert bg[0].strict_slashes is True
    bg.append(Blueprint("bp3"))

# Generated at 2022-06-14 07:06:16.721754
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    group = BlueprintGroup()
    group.append(sanic.Blueprint('test_bp', url_prefix = 'test_prefix'))
    assert len(group) == 1

# Generated at 2022-06-14 07:06:27.584696
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    assert bpg[0] == bp1
    assert bpg[1] == bp2
    assert bpg[2] == bp3

    bpg[2] = bp4
    assert bpg[2] == bp4
