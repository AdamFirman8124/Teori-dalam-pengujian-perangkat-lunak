

# Generated at 2022-06-14 06:57:35.654271
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bg = BlueprintGroup('/api', 'v1')
    bg.append(bp1)
    bg.append(bp2)
    
    @bg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')



# Generated at 2022-06-14 06:57:49.257862
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp_a = Blueprint("test_bp_a", url_prefix='/bp-a')
    bp_b = Blueprint("test_bp_b", url_prefix='/bp-b')

    test_middleware_a = []
    test_middleware_b = []

    @bp_a.middleware('request')
    async def bp_a_middleware(request):
        test_middleware_a.append(1)

    @bp_a.middleware('request')
    async def bp_a_middleware(request):
        test_middleware_a.append(2)

    @bp_b.middleware('request')
    async def bp_b_middleware(request):
        test_middleware_b.append(1)
        test_middleware_b.append(2)

   

# Generated at 2022-06-14 06:58:01.924410
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Configure a Sanic application to test Blueprint group middleware
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bpg2 = BlueprintGroup(bp5, bp4, url_prefix="/api", version="v1")


# Generated at 2022-06-14 06:58:13.054891
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp1, bp2, url_prefix='/bpg')

    @bp3.middleware('request')
    async def bp3_only_middleware(request):
        print('bp3_only_middleware')

    @bp4.middleware('request')
    async def bp4_only_middleware(request):
        print('bp4_only_middleware')


# Generated at 2022-06-14 06:58:26.106978
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
    @bp3.middleware('request')
    async def bp3_only_middleware(request):
        print('applied on Blueprint : bp3 Only')

# Generated at 2022-06-14 06:58:34.268889
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup(bp1, bp2)
    # Test cases
    # Middleware is not defined and error is raised
    @group.middleware('response')
    def middleware(request):
        assert False

    # Middleware is defined and no error is raised
    @group.middleware('response')
    def middleware(request):
        assert True



# Generated at 2022-06-14 06:58:46.478724
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    BlueprintGroup.middleware unit test
    """
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    @bp2.route('/')
    async def bp2_route(request):
        return text('bp2')

    group = Blueprint.group(bp1, bp2)


# Generated at 2022-06-14 06:58:56.301313
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        pass

    assert group.blueprints[0].has_middleware('request', 'group_middleware')
    assert group.blueprints[1].has_middleware('request', 'group_middleware')

# Generated at 2022-06-14 06:59:09.848161
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestApp(sanic.Sanic):
        def __init__(self, run_as_async=False, *args, **kwargs):
            super(TestApp, self).__init__(*args, **kwargs)
            self.run_as_async = run_as_async

            self.bp1 = Blueprint("bp1", url_prefix="/bp1")
            self.bp2 = Blueprint("bp2", url_prefix="/bp2")

            @self.bp1.route("/test")
            async def test_route(request):
                return text("This is bp1 route to test")

            @self.bp2.route("/test")
            async def test_route(request):
                return text("This is bp2 route to test")


# Generated at 2022-06-14 06:59:20.341546
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test to verify the BlueprintGroup.middleware method
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2, url_prefix="/api", version="v1")
    assert len(group.blueprints) == 2
    assert isinstance(group.blueprints, list)

    @group.middleware('request')
    async def request_middleware(request):
        """
        Sample Middleware Plugin to be injected into the Blueprint group
        """
        pass
    # Assert that the group has been injected with the middleware
    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1

# Generated at 2022-06-14 06:59:30.438929
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    @group.middleware('request')
    async def test_request(request):
        pass
    
    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1
    assert bp1.middlewares['request'] == bp2.middlewares['request']

# Generated at 2022-06-14 06:59:44.016884
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp3)
    bpg.append(bp4)

    @bp3.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp4.middleware('request')
    async def bp2_only_middleware(request):
        print

# Generated at 2022-06-14 06:59:55.271506
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix="/bp1")
    bp2 = sanic.Blueprint('bp2', url_prefix="/bp2")
    bpg = BlueprintGroup()

    class TestMiddleware:
        def __init__(self):
            self.calls = []

        def __call__(self, request):
            self.calls.append(request)

        def reset(self):
            self.calls = []

    middleware = TestMiddleware()

    @bpg.middleware('request')
    def request_middleware(request):
        middleware(request)

    bpg.append(bp2)
    bpg.append(bp1)

    @bp1.route('/')
    def bp1_route(request):
        return sanic.response.text

# Generated at 2022-06-14 07:00:04.931094
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup('bpg', url_prefix='/bpg')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bpg)

    # assert no middleware or routes exist yet
    assert len(bp1.middlewares['request']) == 0
    assert len(bp2.middlewares['request']) == 0

# Generated at 2022-06-14 07:00:17.099200
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    inner_bp = Blueprint("inner_bp")
    bp_group = BlueprintGroup(inner_bp)
    original_middleware_list = inner_bp.middlewares

    @bp_group.middleware("request")
    async def bp_group_middleware(request):
        pass

    assert inner_bp.middlewares == original_middleware_list + [bp_group_middleware]

    # should be overwritten
    @bp_group.middleware("request")
    async def bp_group_middleware_overwrite(request):
        pass

    assert inner_bp.middlewares == original_middleware_list + [
        bp_group_middleware_overwrite
    ]

# Generated at 2022-06-14 07:00:30.923517
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


# Generated at 2022-06-14 07:00:39.776084
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # set up
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware("request")
    async def request_middleware(request):
        request["bpg_middleware"] = True

    @bpg.middleware("response")
    async def response_middleware(request, response):
        response["bpg_middleware"] = True

    app = sanic.Sanic()
    app.blueprint(bpg)

    @bp1.route("/")
    async def handler1(request):
        assert request["bpg_middleware"] == True

    @bp2.route("/")
    async def handler2(request):
        assert request

# Generated at 2022-06-14 07:00:48.891224
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Register Blueprint group under the app
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        pass
    assert bp1.middleware.middlewares['request'][0].func == group_middleware
    assert bp2.middleware.middlewares['request'][0].func == group_middleware



# Generated at 2022-06-14 07:00:54.825730
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version=1)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:01:03.855331
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class Auth:
        pass
    
    @sanic.blueprints.Blueprint.middleware(Auth)
    def decorated_func(req):
        return req

    assert not hasattr(Auth, "add_resource")

    @sanic.blueprints.Blueprint.middleware()
    def decorated_func2(req):
        return req

    assert not hasattr(decorated_func2, "add_resource")


from unittest import mock



# Generated at 2022-06-14 07:01:18.294853
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    bp4 = Blueprint('bp4')

    group = BlueprintGroup(bp1, bp2)
    group2 = BlueprintGroup(bp3, bp4)

    group3 = BlueprintGroup(group, group2)

    @group3.middleware('request', 'bp1')
    async def middleware_bp1(request):
        print('applied on Blueprint : bp1 Only')

    @group3.middleware('request', 'bp2')
    async def middleware_bp2(request):
        print('applied on Blueprint : bp2 Only')


# Generated at 2022-06-14 07:01:27.927742
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class MyRequestHandler(sanic.Request):
        pass

    class MyResponseHandler(sanic.Response):
        pass

    class MySanic(sanic.Sanic):
        def __init__(self):
            self.blueprints = []
            self.error_handler = None
            self.request_class = MyRequestHandler
            self.response_class = MyResponseHandler

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp1)
    bpg.append(bp2)

    def middleware(request):
        pass
    bpg.middleware(middleware)
    assert(bp1.middlewares)

# Generated at 2022-06-14 07:01:40.633389
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class MockApp:
        def __init__(self):
            self.middlewares = [None, None, None]

    app = MockApp()

    bp1 = Blueprint("bp1", url_prefix="bp1", strict_slashes=False)
    bp2 = Blueprint("bp2", url_prefix="bp2", strict_slashes=False)
    bp1.app = app
    bp2.app = app

    class MockMiddleware:
        def __init__(self):
            self.args = None
            self.kwargs = None
            self.called = None

        def __call__(self, request):
            self.called = True

    middleware = MockMiddleware()
    g = BlueprintGroup(bp1, bp2, strict_slashes=False)

# Generated at 2022-06-14 07:01:54.229029
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    
    # Given
    @Blueprint.middleware('request')
    async def dummy_middleware_bp1(request):
        pass
    @Blueprint.middleware('request')
    async def dummy_middleware_bp2(request):
        pass
    @Blueprint.middleware('request')
    async def dummy_middleware_bp3(request):
        pass
    @Blueprint.middleware('request')
    async def dummy_middleware_bp4(request):
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

# Generated at 2022-06-14 07:02:04.275379
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    def bpg_middleware(request):
        pass

    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1
    assert bp1.middlewares['request'][0] == bpg_middleware
    assert bp2.middlewares['request'][0] == bpg_middleware


# Generated at 2022-06-14 07:02:14.962032
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestMiddleware:
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1')

    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp1.middleware(TestMiddleware)
    bp2.middleware(TestMiddleware)

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    @group.middleware('request')
    def test_middleware(request):
        pass

    assert bp1.request_middleware[0] == test_middleware
    assert bp2.request_middleware[0] == test_middleware

# Generated at 2022-06-14 07:02:27.935743
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint
    from sanic.response import HTTPResponse
    from sanic import Sanic

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    def bpg_group_middleware(request):
        request["bpg_request_processor"] = True

    @bp1.middleware
    def bp1_group_middleware(request):
        request["bp1_request_processor"] = True

    @bp2.middleware
    def bp2_group_middleware(request):
        request["bp2_request_processor"] = True



# Generated at 2022-06-14 07:02:40.021310
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert len(bp3.middlewares) == 1
    assert len(bp4.middlewares) == 1


# Generated at 2022-06-14 07:02:46.912177
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.app.Sanic(__name__)

    bp1 = Blueprint('bp1', url_prefix='/bp1')

    bp1.middleware('request', lambda req: None)

    assert len(bp1.middlewares.get('request')) == 1

    bpg = BlueprintGroup('bpg', url_prefix='/bpg')
    bpg.append(bp1)

    @bpg.middleware('request')
    def bpg_middleware(request):
        pass

    assert len(bp1.middlewares.get('request')) == 2
    assert len(bpg.middlewares.get('request')) == 1


# Generated at 2022-06-14 07:03:01.022863
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # `ensure_async_type_hint` is a decorator factory that verify the type
    # annotations for async def and returns a new decorator that wraps the
    # coroutine function.
    # The returned decorator will raise an error to the user if the wrapped
    # function doesn't match the type hints, otherwise nothing happens.
    from sanic.utils import ensure_async_type_hint

    # here we use the decorator factory to create a decorator that only allow
    # coroutine function with type annotations:
    # - async def middleware(request: Request, response: Response)
    decorated_middleware = ensure_async_type_hint(
        "request", "response"
    )(decorated_middleware)


    bp = Blueprint("test_bp", url_prefix="/test")


# Generated at 2022-06-14 07:03:06.650611
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    group = BlueprintGroup()
    @group.append
    async def middleware(request):
        request["group_middleware_called"] = True


# Generated at 2022-06-14 07:03:18.546727
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp3 = Blueprint('bp3', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')


# Generated at 2022-06-14 07:03:31.054026
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """
    bp1 = sanic.blueprints.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.blueprints.Blueprint('bp2', url_prefix='/bp2')
    group = sanic.blueprints.Blueprint.group(bp1, bp2)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert group_middleware(None) is None
    assert len(bp1.request_middleware) == 1
    assert len(bp2.request_middleware) == 1

# Generated at 2022-06-14 07:03:40.692065
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.app import Sanic

    app = Sanic('sanic')
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


# Generated at 2022-06-14 07:03:52.482518
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Given
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    mock_app = sanic.Sanic("test_BlueprintGroup_middleware")

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    # When
    @bpg.middleware("request")
    async def bpg_mw(request):
        pass

    # Then
    assert len(bp1.middlewares["request"]) == 1
    assert len(bp2.middlewares["request"]) == 1

    # Given
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")
    mock_app

# Generated at 2022-06-14 07:04:01.436934
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bpg = BlueprintGroup()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def middleware(request):
        pass

    assert bp1._middleware == [middleware]
    assert bp2._middleware == [middleware]

# Generated at 2022-06-14 07:04:08.748696
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    app = sanic.Sanic()
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    
    bpg = BlueprintGroup(bp3)
    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    assert bp3.middleware is not None
    # assert bp3.middleware == bpg.middleware


# Generated at 2022-06-14 07:04:18.810785
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("sanic-blueprint-group-middleware")

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")

    @bp2.route("/<param>")
    async def bp2_route(request, param):
        return text(param)

    group = Blueprint.group(bp1, bp2)

    @group.middleware("request")
    async def group_middleware(request):
        print("common middleware applied for both bp1 and bp2")

    app.blueprint(group)


# Generated at 2022-06-14 07:04:26.975048
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
  # Test Code Start
  bp1 = Blueprint('bp1', url_prefix='/bp1')
  bp2 = Blueprint('bp2', url_prefix='/bp2')

  bpg = BlueprintGroup(url_prefix="/api", version="v1")
  bpg.append(bp1)
  bpg.append(bp2)

  @bpg.middleware('request')
  async def group_middleware(request):
      print('common middleware applied for both bp1 and bp2')

  # Test Code End


# Generated at 2022-06-14 07:04:30.933519
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # blueprint_group = BlueprintGroup()
    @BlueprintGroup.middleware
    def test_function(request):
        print("test function called")

    # blueprint_group.blueprints.append()
    test_function(None)



# Generated at 2022-06-14 07:04:45.813779
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1", url_prefix="/")
    bp2 = Blueprint("bp2", url_prefix="/")
    my_bp_group = BlueprintGroup()
    my_bp_group.append(bp1)
    my_bp_group.append(bp2)
    my_bp_group.middleware(lambda request: text(""))

    assert (
        my_bp_group.blueprints[0].middlewares[sanic.request][0].__name__
        == "applied_for_all_blueprints"
    )
    assert (
        my_bp_group.blueprints[1].middlewares[sanic.request][0].__name__
        == "applied_for_all_blueprints"
    )


# Generated at 2022-06-14 07:05:00.029626
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create a new Blueprint Group with 2 Blueprints and middleware registration
    bp1 = sanic.Blueprint('bp1')
    bp2 = sanic.Blueprint('bp2')
    bpG = BlueprintGroup()
    bpG.append(bp1)
    bpG.append(bp2)
    bpG.middleware(lambda r:r)
    # The middleware should be applied on both the blueprints
    assert len(bpG.blueprints[0].middleware_stack) == 1
    assert len(bpG.blueprints[1].middleware_stack) == 1
    # Ensure that the same middleware isn't applied twice
    bpG.middleware(lambda r:r, 'request')
    assert len(bpG.blueprints[0].middleware_stack) == 1

# Generated at 2022-06-14 07:05:04.730879
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def mw():
        pass

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bg = BlueprintGroup()
    bg.append(bp1)
    bg.append(bp2)

    bg.middleware(mw)

    assert mw in bp1._middlewares['request']
    assert mw in bp2._middlewares['request']



# Generated at 2022-06-14 07:05:16.021375
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    bpg2 = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bp1.middleware(bp1, sanic.request, ordering=0)(bp1.route)
    bp2.middleware(bp2, sanic.request, ordering=0)(bp2.route)

# Generated at 2022-06-14 07:05:24.795998
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class App():
        pass
    app = App()
    app.blueprint = BlueprintGroup()
    b1 = Blueprint('b1')
    b2 = Blueprint('b2')
    app.blueprint.append(b1)
    app.blueprint.append(b2)
    def fn():
        pass
    # app.blueprint.middleware()
    app.blueprint.middleware(fn)
    assert hasattr(b1, 'middleware')
    assert hasattr(b2, 'middleware')

# Generated at 2022-06-14 07:05:35.590840
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.exceptions import NotFound, ServerError
    from sanic.wrappers import Response
    from sanic.request import Request
    from sanic.response import HTTPResponse, text

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")

    @bp2.route("/")
    async def bp2_route(request):
        return text("bp2")

    @bp1.exception(NotFound)
    async def bp1_404_handler(request, exception):
        return Response("bp1 not found", status=404)


# Generated at 2022-06-14 07:05:48.504086
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("BlueprintGroup_middleware")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    @bp1.route("/")
    async def bp1_route(request):
        return text("bp1")

    @bp2.route("/")
    async def bp2_route(request):
        return text("bp2")

    @bp3.route("/")
    async def bp3_route(request):
        return text("bp3")


# Generated at 2022-06-14 07:06:03.113271
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    group = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:06:13.339799
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BluePrintGroup_middleware")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    @bp1.route("/bp1")
    def handler1(request):
        return text("OK")

    @bp2.route("/bp2")
    def handler2(request):
        return text("OK")

    @Blueprint.group(bp1, bp2)
    def group_middleware_fn(request):
        pass

    group = Blueprint.group(bp1, bp2)

    @group.middleware("request")
    def group_middleware_fn(request):
        pass


# Generated at 2022-06-14 07:06:26.105508
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix = "/api", version = "v1")
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware('request')
    async def bpg_middleware(request):
        return

    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1
    assert bp1.middlewares['request'][0].__name__ == 'bpg_middleware'

# Generated at 2022-06-14 07:06:44.837233
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create a dummy app
    app = sanic.Sanic(__name__)

    # Blueprint declarations
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    # Blueprint group
    group = Blueprint.group(bp1, bp2)

    # Register Blueprint group under the app
    app.blueprint(group)

    # Create a dummy middleware
    @bp1.middleware("request")
    async def dummy_middleware(request):
        pass

    # Get the middleware registered on bp1
    registered_middleware = bp1._middleware["request"]

    # Get the blueprint from blueprint group
    blueprint = group.blueprints[0]

    # bp1 middleware should be equal to blueprint middleware as it belongs to

# Generated at 2022-06-14 07:06:58.077351
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        raise Exception('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        raise Exception('applied on Blueprint : bp2 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    group = BlueprintGroup()
    group.append(bp1)

# Generated at 2022-06-14 07:07:11.628600
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Create a Pair of Blueprints to use for test
    bp = Blueprint(__name__ + ".blueprint")
    bp1 = Blueprint(__name__ + ".blueprint1")

    # Create a BlueprintGroup from Blueprint list
    bpg = BlueprintGroup()
    bpg.append(bp)
    bpg.append(bp1)

    # Test middleware applied to blueprint group
    request_ctx = []

    @bp.middleware("request")
    async def blueprint_middleware(request):
        request_ctx.append(request)

    @bp1.middleware("request")
    async def blueprint1_middleware(request):
        request_ctx.append(request)

    @bpg.middleware("request", attach_to=bp)
    async def blueprint_group_middleware(request):
        request_ctx.append

# Generated at 2022-06-14 07:07:18.981179
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Sanic BlueprintGroup - Blueprint Group Middleware
    """
    class DummyMiddleware(object):
        """
        Dummy Middleware for testing the examples
        """

        def __init__(
            self,
            app: sanic.Sanic,
            test_attribute: Optional[str] = None,
            test_parameter: Optional[str] = None,
        ):
            self.app = app
            self.test_attribute = test_attribute or "Test Attribute"
            self.test_parameter = test_parameter or "Test Parameter"

        async def __call__(self, request: sanic.request, handler: callable):
            return await handler(request)


# Generated at 2022-06-14 07:07:31.010492
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bpg = BlueprintGroup(url_prefix='/api')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    def middleware(request):
        pass

    @bp1.middleware('request')
    @bp2.middleware('request')
    @bp3.middleware('request')
    def local_middleware(request):
        pass

    # Test using the decorator
    bpg.middleware(middleware, 'request')
