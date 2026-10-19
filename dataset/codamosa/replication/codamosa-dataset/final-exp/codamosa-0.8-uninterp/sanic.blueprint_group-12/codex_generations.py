

# Generated at 2022-06-14 06:57:41.543925
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Sanic
    from sanic.response import text

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    # create a new Blueprint Group
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    # Create another blueprint group and add the previously created
    # blueprint group as one of the element
    bpg2 = BlueprintGroup()
    bpg2.append(bp3)
    bpg2.append(bpg)
    bpg2.append(bp4)

    # Create an application to

# Generated at 2022-06-14 06:57:52.919186
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1=Blueprint('bp1')
    bp2=Blueprint('bp2')
    bpg=BlueprintGroup(bp1,bp2)
    
    @bp1.middleware('request')
    async def middleware1(request):
        pass
    
    @bp2.middleware('request')
    async def middleware2(request):
        pass

    @bpg.middleware('request')
    async def middleware2(request):
        pass

    assert len(bp1.middlewares['request'])==2
    assert len(bp2.middlewares['request'])==2

if __name__ == "__main__":
    test_BlueprintGroup_middleware()

# Generated at 2022-06-14 06:57:55.611692
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass



# Generated at 2022-06-14 06:57:58.853475
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware()  # pylint: disable=unused-variable
    async def middleware_func(request):
        pass


# Generated at 2022-06-14 06:58:08.520161
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from .blueprint import Blueprint
    from .router import Route

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    group1 = BlueprintGroup()
    group1.append(bp3)
    group1.append(bp4)

    @group.middleware('request')
    async def group_middleware(request):
        request['group_middleware_applied'] = True


# Generated at 2022-06-14 06:58:19.528573
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class DummyMiddleware:
        def __call__(self, request):
            request["applied"] = True
            return request
    dummy_middleware = DummyMiddleware()

    blueprint = Blueprint("dummy")
    blueprint.middleware = Mock()

    blueprint_group = BlueprintGroup()
    blueprint_group._blueprints = [blueprint]

    blueprint_group.middleware(dummy_middleware)
    assert blueprint_group.blueprints[0].middleware.call_count == 1

    blueprint_group.middleware(dummy_middleware, "response")
    assert blueprint_group.blueprints[0].middleware.call_count == 2


# Generated at 2022-06-14 06:58:28.787219
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

   group = BlueprintGroup()
   group.append(bp1)
   group.append(bp2)


# Generated at 2022-06-14 06:58:31.689178
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create mock objects
    mock_fn = Mock()
    BlueprintGroup.middleware(mock_fn)
    assert mock_fn.called

# Generated at 2022-06-14 06:58:45.364821
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Check for blueprintgroup without blueprint
    bpg = BlueprintGroup()
    @bpg.middleware('request')
    def middleware_fn(request):
        return text('Middleware Text')

    # Check for blueprintgroup with single blueprint
    bp1 = Blueprint('bp1')
    bpg = BlueprintGroup(bp1)
    @bpg.middleware('request')
    def middleware_fn(request):
        return text('Middleware Text')

    # Check for blueprintgroup with multiple blueprint
    bp2 = Blueprint('bp2')
    bpg = BlueprintGroup(bp1, bp2)
    @bpg.middleware('request')
    def middleware_fn(request):
        return text('Middleware Text')

if __name__ == "__main__":
    test_BlueprintGroup_middleware()

# Generated at 2022-06-14 06:58:59.217517
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class Middleware1:
        def __init__(self, app, *args, **kwargs):  # type: ignore
            pass

        async def __call__(self, request, response=None):  # type: ignore
            pass

    class Middleware2:
        def __init__(self, app, *args, **kwargs):  # type: ignore
            pass

        async def __call__(self, request, response=None):  # type: ignore
            pass

    bp1 = Blueprint("test-bp1", url_prefix="/bp1")
    bp2 = Blueprint("test-bp2", url_prefix="/bp2")

    bp1_middleware_count = len(bp1.middlewares)
    bp2_middleware_count = len(bp2.middlewares)

    bpg = Blueprint

# Generated at 2022-06-14 06:59:07.440365
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    # noinspection PyUnresolvedReferences
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    bp4 = Blueprint('bp4')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        pass

    @bp3.middleware('request')
    async def bp3_only_middleware(request):
        pass

   

# Generated at 2022-06-14 06:59:19.417502
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    app = sanic.Sanic("test_BlueprintGroup_middleware")

    bp1 = Blueprint("bp1", url_prefix="/bp1")

    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bp3 = Blueprint("bp3", url_prefix="/bp3")

    group = Blueprint.group(bp1, bp2)

    bp1.middleware("request")(lambda request: print("bp1"))

    bp2.middleware("request")(lambda request: print("bp2"))

    @group.middleware("request")
    def group_middleware(request):
        print("group request")

    @bp3.middleware("request")
    def bp3_middleware(request):
        print("bp3")


# Generated at 2022-06-14 06:59:32.873794
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    group = Blueprint.group(bp1, bp2)

    @bp1.route("/")
    async def bp1_route(request):
        return text("Test bp1")

    @bp2.route("/")
    async def bp2_route(request):
        return text("Test bp2")

    @bp1.middleware("request")
    async def test_bp1_middleware(request):
        request["bp1_middleware"] = True


# Generated at 2022-06-14 06:59:45.295922
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class MockApp(sanic.Sanic):
        pass
    from sanic.response import text
    app = MockApp()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 06:59:56.109873
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    assert bp1.app_middleware['request'][0][0] == group_middleware
    assert bp2.app_middleware['request'][0][0] == group_middleware


# Generated at 2022-06-14 07:00:05.214396
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4)

    @bpg.middleware('request')
    async def bpg_only_middleware(request):
        print('applied on Blueprint Group')

    assert bpg_only_middleware.__name__ == "bpg_only_middleware"
    assert bpg_only_middleware.__module__ == "tests.test_class_blueprintgroup"

# Generated at 2022-06-14 07:00:18.214062
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup()
    bpg.append(bp3)
    bpg.append(bp4)

    @bp3.middleware('request')
    async def bp_middleware(request):
        print('bp3 only')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return

# Generated at 2022-06-14 07:00:32.196984
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix='/api')

    @bpg.middleware('request')
    async def bpg_middleware(request):
        print('BPG Middleware')

    @bp1.middleware('request')
    async def bp1_middleware(request):
        print('BP1 Middleware')

    @bp2.middleware('request')
    async def bp2_middleware(request):
        print('BP2 Middleware')


    bp1_middleware.__wrapped__ = bp1_middleware
    bp1.middlewares['request'].append(bp1_middleware)

# Generated at 2022-06-14 07:00:43.548313
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


# Generated at 2022-06-14 07:00:53.006412
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bpg2 = BlueprintGroup(bp5, bp6, url_prefix="/api", version="v2")

    assert len(bpg.blueprints) == 2
    assert len(bpg2.blueprints) == 2


# Generated at 2022-06-14 07:01:08.950591
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        assert True

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        assert True

    # Create a new group
    group = BlueprintGroup()

    # Insert two Blueprint object into the group object.
    group.append(bp1)
    group.append(bp2)

    @group.middleware('request')
    async def group_common_middleware(request):
        assert True


# Generated at 2022-06-14 07:01:21.860055
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Get a sanic application instance
    sanic_app = sanic.Sanic(__name__)

    # Create a test blueprint
    test_bp = sanic.Blueprint('test_bp', url_prefix='/test_bp')

    # Create a test blueprint group
    test_bp_group = BlueprintGroup()

    # Add test blueprint to group
    test_bp_group.append(test_bp)

    # Configure middleware for blueprint group
    @test_bp_group.middleware('request')
    async def test_bp_group_middleware(request):
        assert request is not None

    # Configure middleware for blueprint
    @test_bp.middleware('request')
    async def test_bp_middleware(request):
        assert request is not None

    # Register blueprint to test application
    sanic_app

# Generated at 2022-06-14 07:01:27.222600
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on BlueprintGroup : bp1 Only')



# Generated at 2022-06-14 07:01:40.009128
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    BlueprintGroup.middleware should behave exactly like Blueprint.middleware
    """
    app = sanic.Sanic("test_BlueprintGroup_middleware")

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api/v1")

    @bpg.middleware("request")
    async def bpg_middleware(request):
        pass

    @bp1.middleware("request")
    async def bp1_middleware(request):
        pass

    @bp2.middleware("request")
    async def bp2_middleware(request):
        pass

    fns = bpg.blueprints[0].middlewares["request"]


# Generated at 2022-06-14 07:01:44.466530
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprints = BlueprintGroup()
    @blueprints.middleware
    async def sample(request):
        pass
    for blueprint in blueprints:
        for middleware in blueprint.middlewares["request"]:
            assert middleware == sample


# Generated at 2022-06-14 07:01:54.238007
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Create Blueprint Group
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bps = BlueprintGroup(bp1, bp2)

    # create a fake app
    app = sanic.Sanic()

    # add a few routes to the Blueprints
    @bp1.route('/')
    async def bp1_route(request):
        pass

    @bp1.route('/bp1/<param>')
    async def bp1_route(request, param):
        pass

    @bp2.route('/')
    async def bp2_route(request):
        pass


# Generated at 2022-06-14 07:02:04.905651
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Testing Middleware expectation when handling Blueprints in groups
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg1 = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    bpg2 = BlueprintGroup(bp3, bpg1, url_prefix="/api/v2", version="v2")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:02:05.643702
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass

# Generated at 2022-06-14 07:02:16.690962
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @sanic.blueprint.group(url_prefix='/group', version='1.0')
    def group():
        return BlueprintGroup(url_prefix='/group', version='1.0')


    @group.middleware('request')
    async def bp1_middleware(request):
        pass


    @group.route('/')
    async def bp1_route(request):
        return text('bp1')


    app = sanic.Sanic('test_BlueprintGroup_middleware')
    app.blueprint(group)

# Generated at 2022-06-14 07:02:29.975811
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Issue #867
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    @bp1.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    group

# Generated at 2022-06-14 07:02:38.190551
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @Blueprint.middleware("request")
    async def middleware_test(request):
        pass

    Blueprint.middleware("test1")(middleware_test)
    Blueprint.middleware(test2="test2")(middleware_test)



# Generated at 2022-06-14 07:02:45.198645
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('test_middleware', url_prefix='/')
    bp.middleware(lambda: (yield))   # we register a dummy middleware for the bp
    bpg = BlueprintGroup()
    bpg.append(bp)

    def dummy_middleware(request):
        pass

    bpg.middleware(dummy_middleware)
    assert bp.middlewares == [dummy_middleware]



# Generated at 2022-06-14 07:02:59.216474
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    app = sanic.Sanic("test-blueprintgroup-middleware")

    @sanic.exception(Exception)
    async def exception_handler(request, exception):
        return sanic.response.text("Generic App Error")

    app.handle_exception(Exception, exception_handler)

    bp1 = Blueprint("bp1", url_prefix="/bp1", version="v1")

    @bp1.route("/")
    async def bp1_route(request):
        return sanic.response.text("bp1_route")

    bp2 = Blueprint("bp2", url_prefix="/bp2", version="v2")

    @bp2.route("/")
    async def bp2_route(request):
        return sanic.response.text("bp2_route")


# Generated at 2022-06-14 07:03:09.952693
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """Test the middleware method of class BlueprintGroup."""

    app = sanic.Sanic('test_Blueprint_middleware')

    @app.middleware('request')
    async def before_request(request):
        request['test'] = 'test'

    bp1 = Blueprint('test_bp')
    bp2 = Blueprint('test_bp2')
    bp1.middleware('response', is_list=False)
    bp2.middleware('response', is_list=False)

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('response', is_list=False)
    async def before_response(request, response):
        assert request['test'] == 'test'
        response.headers['TEST'] = request

# Generated at 2022-06-14 07:03:21.450751
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup.middleware('request')
    async def group_mw(request):
        """
        Group Middleware
        :param request:
        :return:
        """
        pass

    @BlueprintGroup.middleware('request', name='my_middleware', attach_to=Blueprint)
    def group_mw(request):
        """
        Group Middleware
        :param request:
        :return:
        """
        pass

    @BlueprintGroup.middleware('request')
    def group_mw_without_name(request):
        """
        Group Middleware
        :param request:
        :return:
        """
        pass


# Generated at 2022-06-14 07:03:34.488318
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @BlueprintGroup(url_prefix='test', version='test').middleware('request')
    @BlueprintGroup(url_prefix='test', version='test').middleware('response')
    async def test_middleware_fn(request):
        pass

    app = sanic.Sanic()
    bp = Blueprint('test')
    bp.group(bp1, bp2).register(app)
    route = bp.group(bp1, bp2).add_route('/test', test_handler)

    assert route.blueprint_group is not None
    assert len(route.blueprint_group.middlewares) == 2
    assert route.blueprint_group.middlewares[0].name == 'test_middleware_fn'

# Generated at 2022-06-14 07:03:45.886240
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

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

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    group = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 07:03:58.232534
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def middleware_fn(req):
        pass

    bp_group = BlueprintGroup()
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp_group.append(bp1)
    bp_group.append(bp2)
    bp_group.middleware(middleware_fn)
    assert len(bp1.middlewares) == 1
    assert len(bp2.middlewares) == 1
    assert middleware_fn in bp1.middlewares
    assert middleware_fn in bp2.middlewares
    bp_group.middleware(middleware_fn, attach_to='request')
    assert middleware_fn in bp1.request_middlewares



# Generated at 2022-06-14 07:04:03.293568
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def bp1_middleware(request):
        print('applied on Blueprint : bp1 Only')
    assert bp1.request_middleware, 'Test 1 failed'
    assert bp2.request_middleware, 'Test 1 failed'
    
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')


# Generated at 2022-06-14 07:04:16.181114
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    @bpg.middleware('request')
    async def bpg_middleware(request):
        print('common middleware applied for both bp1 and bp2')


# Generated at 2022-06-14 07:04:28.024730
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('bp', url_prefix='/bp')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp)

    @bpg.middleware('request')
    async def bp_only_middleware(request):
        print('applied on Blueprint Group')

    assert bp.middleware_funcs['request'][0] == bp_only_middleware



# Generated at 2022-06-14 07:04:39.152403
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    @bpg.middleware
    async def bp_middleware(request):
        print(f"BlueprintGroup middleware called with request : {request}")

    request_list = [f"Request payload - {i}" for i in range(10)]
    for payload in request_list:
        bp_middleware(payload)


# Generated at 2022-06-14 07:04:46.551248
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test case for method middleware of class BlueprintGroup
    """
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")

    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    @bpg.middleware("request")
    async def request_middleware(request):
        request["mw"] = True

    @bp1.middleware("request")
    async def request_middleware_bp1(request):
        request["bp1"] = True


# Generated at 2022-06-14 07:05:00.522418
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    # Create a Blueprint Group
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bpg.middleware('response')
    async def bpg_only_middleware(request, response):
        print('applied on Blueprint Group : bpg')

    # Assert Blueprint Group is attached with Middleware
    assert bg.has_middleware('response')

    # Assert Middleware is NOT attached to individiual Blueprint
    assert bp1.has_middleware('response') == False
    assert bp2.has_middleware('response') == False

    # Run the Middleware and check results

# Generated at 2022-06-14 07:05:12.582339
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

    bpg = BlueprintGroup(bp3, bp4, bp5, url_prefix="/api", version="v1")

# Generated at 2022-06-14 07:05:21.971668
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    @Blueprint.middleware('request')
    async def bm_fn1(request):
        pass

    @Blueprint.middleware('request')
    async def bm_fn2(request):
        pass

    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware(bm_fn1)
    bpg.middleware(bm_fn2, attach_to='response')
    assert len(bp1.middlewares['request']) == 2
    assert len(bp2.middlewares['request']) == 2
    assert bm_fn1 == bp1.middlewares['request'][1]
    assert bm_fn2 == b

# Generated at 2022-06-14 07:05:27.347875
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('bp', url_prefix='/bp')

    class MyTestMiddleware:
        def __init__(self, arg1, arg2):
            pass

    bp.middleware(MyTestMiddleware, arg1=1, arg2=2)

    assert MyTestMiddleware in bp._middlewares['request']



# Generated at 2022-06-14 07:05:34.141029
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    application = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    application.blueprint(group)


# Generated at 2022-06-14 07:05:47.038694
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    # Case1: Using Blueprint group middleware with Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    blueprint_group = BlueprintGroup(bp1, bp2, url_prefix="/api")

    # Call Blueprint group middleware with Blueprint
    blueprint_group.middleware(bp1)

    # Case2: Using Blueprint group middleware with Blueprint and BlueprintGroup
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    blueprint_group = BlueprintGroup(bp1, bp2, url_prefix="/api")

    bp3 = Blueprint('bp3', url_prefix='/bp3')

# Generated at 2022-06-14 07:05:57.754631
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


# Generated at 2022-06-14 07:06:17.396299
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    assert BlueprintGroup()

# Generated at 2022-06-14 07:06:26.225838
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp_group = BlueprintGroup()
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp_group.append(bp1)
    bp_group.append(bp2)
    bp3 = Blueprint("bp3")
    bp_group[2] = bp3
    bp4 = Blueprint("bp4")
    bp_group[3] = bp4
    assert bp_group[2] == bp3
    assert bp_group[3] == bp4


# Generated at 2022-06-14 07:06:32.290947
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """
    Test BlueprintGroup.__getitem__ method
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()

    group.append(bp1)
    group.append(bp2)

    assert len(group) == 2
    assert group[0] is bp1
    assert group[1] is bp2
    with pytest.raises(IndexError):
        assert group[2]


# Generated at 2022-06-14 07:06:37.904993
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    from sanic.blueprints import Blueprint

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bp5 = Blueprint("bp5", url_prefix="/bp5")
    bp6 = Blueprint("bp6", url_prefix="/bp6")

    bp7 = Blueprint("bp7", url_prefix="/bp7")
    bp8 = Blueprint("bp8", url_prefix="/bp8")

    bp9 = Blueprint("bp9", url_prefix="/bp9")
    bp10 = Blueprint("bp10", url_prefix="/bp10")


# Generated at 2022-06-14 07:06:47.147368
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Define a dummy Blueprint object
    class Blueprint:
        def __init__(self, url_prefix):
            self.url_prefix = url_prefix
            self._middleware = []

        def middleware(self, fn, *args, **kwargs):
            self._middleware.append({
                "fn": fn,
                "args": list(args),
                "kwargs": kwargs
            })

    # Define a dummy BlueprintGroup object
    class BlueprintGroup(sanic.blueprints.BlueprintGroup):
        def __init__(self, *blueprints, **kwargs):
            self.blueprints = []
            self.url_prefix = kwargs.get("url_prefix", None)
            for blueprint in blueprints:
                self.blueprint(blueprint)

    bp1 = Blueprint('bp1')

# Generated at 2022-06-14 07:06:59.019100
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)
    assert len(bpg) == 4
    del bpg[2]
    assert len(bpg) == 3
    assert bpg[2] == bp4
    assert bpg._blueprints == [bp1, bp2, bp4]



# Generated at 2022-06-14 07:07:12.488482
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1", strict_slashes=1)

    del bpg[0]
    assert len(bpg) == 1
    assert bpg[0].name == bp2.name
    assert bpg[0].url_prefix == bp2.url_prefix

    bpg.append(bp3)
    del bpg[1]
    assert len(bpg) == 1
    assert bpg[0].name == bp2.name
    assert bpg[0].url_prefix == bp2.url_

# Generated at 2022-06-14 07:07:18.106355
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    # Scenario 1: change a blueprint item
    blueprint_group = BlueprintGroup()
    bp_a = Blueprint("test_a")
    bp_b = Blueprint("test_b")
    blueprint_group.append(bp_a)
    blueprint_group.append(bp_b)

    blueprint_group[0] = bp_b
    blueprint_group[1] = bp_a

    assert blueprint_group[0] == blueprint_group[1]
    assert blueprint_group[0] == blueprint_group[1]


# Generated at 2022-06-14 07:07:30.675924
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp1.strict_slashes = True
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp2.strict_slashes = None
    bp2.version = 2
    bpg = BlueprintGroup(url_prefix="/api", version="v1", strict_slashes=False)
    bpg.insert(1,bp1)
    bpg.insert(0,bp2)
    assert bpg.blueprints[1].url_prefix == '/api/bp2'
    assert bpg.blueprints[0].url_prefix == '/api/bp1'
    assert bpg.blueprints[0].version == 'v1'
    assert bpg.blueprints[1].version == 2
    assert b