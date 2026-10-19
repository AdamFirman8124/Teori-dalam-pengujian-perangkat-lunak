

# Generated at 2022-06-14 06:57:23.339883
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)


# Generated at 2022-06-14 06:57:35.995788
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    b = Blueprint("b", url_prefix="/b")
    b.strict_slashes = True
    b.version = "v1"

    bg = BlueprintGroup(url_prefix="/api", strict_slashes=False, version="v2")
    bg.append(b)

    @bg.middleware("request")
    async def mw(request):
        assert request.blueprint == "b"
        assert request.url_rule == "/api/b/"
        assert request.version == "v2"
        assert request.strict_slashes == False
        return

    app = Sanic("test_BlueprintGroup_middleware")
    app.blueprint(bg)
    request, response = app.test_client.get("/api/b?x=y")
    assert response.status == 200

# Generated at 2022-06-14 06:57:49.667681
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('apply middleware to bp1 only')

    @bp2.middleware('request')
    async def bp1_only_middleware(request):
        print('apply middleware to bp2 only')

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('apply middleware to bp1 only')

    assert bp1._middle

# Generated at 2022-06-14 06:57:56.992854
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint_group = BlueprintGroup()
    blueprint = Blueprint('Blueprint', url_prefix='/Blueprint')
    blueprint_group.append(blueprint)

    @blueprint_group.middleware('request', 'response')
    def middleware(request, response):
        pass

    assert hasattr(blueprint, '_middlewares')
    assert len(blueprint._middlewares['request']) == 1
    assert len(blueprint._middlewares['response']) == 0



# Generated at 2022-06-14 06:58:10.629094
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_sanic')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    @bpg.middleware
    async def middleware(request):
        print('middleware applied')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    # Test middleware
    request, response = app.test_client.get('/bp1')
    assert response.text

# Generated at 2022-06-14 06:58:22.956842
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


# Generated at 2022-06-14 06:58:35.601272
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Unit test for method middleware of class BlueprintGroup
    """
    # create a BlueprintGroup object
    bg = BlueprintGroup()
    # create Blueprints
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")
    # register Blueprints to BlueprintGroup
    bg.append(bp1)
    bg.append(bp2)
    # create a request object
    request = sanic.request.Request(
        {"type": "http", "headers": [], "body": b"", "url": ""}
    )
    # create a response object
    response = sanic.response.HTTPResponse()

    # create a middleware function

# Generated at 2022-06-14 06:58:48.332693
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)
    group.middleware(bp1_only_middleware)

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    app = Sanic('test_BlueprintGroup_middleware')
    app.blueprint(group)

    request,

# Generated at 2022-06-14 06:58:58.563236
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    def bp_blueprint_middleware(request):
        return text("bp blueprint middleware")
    
    def bpg_blueprint_middleware(request):
        return text("bpg blueprint middleware")

    bp = Blueprint("bp", url_prefix="/bp")

    # bp.middleware(bp_blueprint_middleware)
    bp.middleware(bp_blueprint_middleware)

    bpg = BlueprintGroup(url_prefix="/bpg")
    bpg.append(bp)
    # bpg.middleware(bpg_blueprint_middleware)
    bpg.middleware(bpg_blueprint_middleware)


# Generated at 2022-06-14 06:59:06.379114
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    sanic_app = sanic.Sanic(__name__)

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api/v1")

    # bp1.middleware('request')(bp1_only_middleware)
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    # bp1.add_route(bp1_route, '/')

# Generated at 2022-06-14 06:59:23.937639
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This test is to ensure that the BlueprintGroup.middleware() is able to
    register middleware across all the blueprints in the BlueprintGroup
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')
    bp7 = Blueprint('bp7', url_prefix='/bp7')
    bp8 = Blueprint('bp8', url_prefix='/bp8')


# Generated at 2022-06-14 06:59:35.374854
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class AppRef(object):
        """
        A reference to the app
        """

        def __init__(self):
            self.middleware = []

    class ContextRef(object):
        """
        A reference to the context
        """

        def __init__(self):
            self.middlewares = []

    def set_middleware(fn, name=None, attach_to=None, context=None):
        """
        Set the middleware for the app
        """
        app_ref.middleware.append(fn)

    _app_ref = AppRef()
    _context_ref = ContextRef()
    _blueprint = Blueprint(name="test", url_prefix="/test")
    _blueprint2 = Blueprint(name="test2", url_prefix="/test2")
    _blueprint_group = BlueprintGroup()



# Generated at 2022-06-14 06:59:49.422930
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.blueprints import Blueprint
    from sanic.response import text
    from sanic.server import HttpProtocol
    from sanic.websocket import WebSocketProtocol
    class TestHttpProtocol(HttpProtocol):
        def get_handler(self):
            return None

        def write_response(self, response):
            return None

    class TestWebsocketProtocol(WebSocketProtocol):
        def websocket_handshake(self):
            return None

        def write_response(self, response):
            return None

    async def test_middleware(request):
        return text("applied on blueprint")

    bp = Blueprint("test_bp", url_prefix="/test")

    @bp.route("/")
    async def test_handler(request):
        return text("ok")

    bpg = Blueprint

# Generated at 2022-06-14 07:00:01.545081
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic.response import text

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
    async def bpg_only_middleware(request):
        print('applied on Blueprint : bp1 Only')


# Generated at 2022-06-14 07:00:07.327982
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Arrange
    bp = Blueprint('bp', url_prefix='/bp')
    bp_group = BlueprintGroup(bp)

    # Act
    bp_group.middleware(sanic.request_middleware, attach_to="request")

    # Assert
    assert len(bp.middlewares['request']) == 1



# Generated at 2022-06-14 07:00:19.072714
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Patch the target function to be executed via middleware
    target = MagicMock(wraps=lambda x, y, z: x + y + z)

    bp1 = Blueprint('bp1', url_prefix='/bp1')

    @bp1.route('/<param>')
    async def bp1_route(request, param):
        return text(target(1, 2, 3))

    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(target(1, 2, 3))

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)


# Generated at 2022-06-14 07:00:32.986746
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint1 = Blueprint('bp1', url_prefix='/bp1')
    blueprint2 = Blueprint('bp2', url_prefix='/bp2')
    blueprint3 = Blueprint('bp3', url_prefix='/bp3')
    blueprint4 = Blueprint('bp4', url_prefix='/bp4')

    blueprint_group = BlueprintGroup()
    blueprint_group.append(blueprint1)
    blueprint_group.append(blueprint2)

    blueprint_group.middleware(bp1_request_middleware_fn, 'request')

    assert bp1_request_middleware_fn in blueprint_group.blueprints[0].request_middleware
    assert bp1_request_middleware_fn not in blueprint_group.blueprints[1].request_middleware

    blueprint_group.append(blueprint3)

# Generated at 2022-06-14 07:00:43.994740
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bpg = BlueprintGroup()
    for bp in [bp1, bp2]:
        bpg.append(bp)

    @bpg.middleware("request")
    def common_middleware(req):
        pass

    @bp1.route("/")
    async def bp1_handler(req):
        return text("bp1")

    @bp2.route("/")
    async def bp2_handler(req):
        return text("bp2")

    app.blueprint(bpg)

    request, response = app.test_client.get("/")
    assert request.path == "/"
    assert response.text == "bp1"

    request, response = app

# Generated at 2022-06-14 07:00:52.480818
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    _url_prefix = "/bp_group"
    _version = 0.1
    _strict_slashes = True
    _bp_prefix = "/bp"

    _app = sanic.Sanic()
    _bp1 = Blueprint("bp1", url_prefix=_bp_prefix)
    _bp2 = Blueprint("bp2", url_prefix=_bp_prefix)
    _bp_group = BlueprintGroup(url_prefix=_url_prefix,
                               version=_version,
                               strict_slashes=_strict_slashes)
    _bp_group.append(_bp1)
    _bp_group.append(_bp2)

    @_bp_group.middleware()
    async def bp_group_middleware(request):
        print('bp_group_middleware')

    # Check middleware


# Generated at 2022-06-14 07:01:07.039502
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # construct BlueprintGroup
    bpg = BlueprintGroup()

    # construct Blueprint
    bp = Blueprint(name='test_bp')
    bpg.append(bp)
    # construct another Blueprint
    bp = Blueprint(name='test_bp_1')
    bpg.append(bp)

    # register common request middleware 
    @bpg.middleware('request')
    async def bp_request(request):
        assert isinstance(request, sanic.request.Request), "type of param request is not Request"

    # register common response middleware 
    @bpg.middleware('response')
    async def bp_response(request, response):
        assert isinstance(request, sanic.request.Request), "type of param request is not Request"

# Generated at 2022-06-14 07:01:28.313132
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp = Blueprint('test', url_prefix='/test')
    bpg = BlueprintGroup(url_prefix='/test')
    bpg.append(bp)
    bpg.append(bp)
    bpg.append(bp)
    del bpg[:2]
    assert len(bpg)==1
    assert bpg[0].name==bp.name


# Generated at 2022-06-14 07:01:33.972726
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    assert len(group) == 2



# Generated at 2022-06-14 07:01:39.900007
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    assert bpg[0] == bp1
    assert bpg[1] == bp2


# Generated at 2022-06-14 07:01:46.539731
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup('/api', 'v1')
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg) == 2


# Generated at 2022-06-14 07:01:58.553887
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def request_middleware_bp1(request):
        request['bp1'] = 'request_middleware_bp1'
        request['bp_group'] = 'request_middleware_bp_group'


# Generated at 2022-06-14 07:02:03.733805
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bg = BlueprintGroup()
    assert len(bg) == 0
    bg.append(bp1)
    assert len(bg) == 1
    bg.append(bp2)
    assert len(bg) == 2


# Generated at 2022-06-14 07:02:10.157980
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)
    blueprint_list = list(group)
    assert blueprint_list == [bp1, bp2]


# Generated at 2022-06-14 07:02:18.366138
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    app = sanic.Sanic("test_BlueprintGroup_insert")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    # Test with blueprint
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg) == 2

    bpg.insert(1, bp1)
    assert len(bpg) == 3

    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bpg.insert(0, bp3)
    assert bpg[0] == bp3

    # Test with blueprint group
    bpg2 = BlueprintGroup()
    bpg2.append(bp1)

# Generated at 2022-06-14 07:02:24.777453
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    # Create a Blueprint group
    group = BlueprintGroup()

    # Insert 2 Blueprints
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    group.append(bp1)
    group.append(bp2)

    # Check if Iteration matches all the blueprints
    assert tuple(group) == (bp1, bp2)



# Generated at 2022-06-14 07:02:33.660092
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    # Test we can access a blueprint in a group like a list
    assert bpg[0] == bp1
    assert bpg[1] == bp2
    # Test we can iterate over the group
    assert list(iter(bpg)) == [bp1, bp2]
    # Test the length
    assert len(bpg) == 2
    # Test that we can delete items
    del bpg[0]
    assert bpg._blueprints == [bp2]
    del bpg[0]

# Generated at 2022-06-14 07:02:55.865941
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()

    group.append(bp1)
    group.append(bp2)

    assert [bp1, bp2] == list(group)



# Generated at 2022-06-14 07:03:06.200139
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1', version="v1")
    bp2 = Blueprint('bp2', url_prefix='/bp2', version="v2")
    bp3 = Blueprint('bp3', url_prefix='/bp3', version="v3")
    bp4 = Blueprint('bp4', url_prefix='/bp4', version="v4")

    bpg = BlueprintGroup(bp1, bp2, bp3, bp4, url_prefix="/api")

    assert len(bpg) == 4
    assert [bp for bp in bpg] == [bp1, bp2, bp3, bp4]


# Generated at 2022-06-14 07:03:18.047454
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp_one = Blueprint('bp1', url_prefix='/bp1')
    bp_two = Blueprint('bp2', url_prefix='/bp2')

    bp_three = Blueprint('bp3', url_prefix='/bp3')
    bp_four = Blueprint('bp4', url_prefix='/bp4')

    group = BlueprintGroup()
    group.append(bp_three)
    group.append(bp_four)

    request_function_call_count = 0
    request_function_param = None

    @group.middleware('request')
    async def common_middleware(request):
        nonlocal request_function_call_count
        request_function_call_count += 1
        request_function_param = request


# Generated at 2022-06-14 07:03:30.242619
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    _bp1 = Blueprint('bp1', url_prefix='/bp1')
    _bp1_1 = Blueprint('bp1.1', url_prefix='/bp1.1')
    _bp2 = Blueprint('bp2', url_prefix='/bp2')

    _bpg = BlueprintGroup()
    _bpg.append(_bp1)
    _bpg.append(_bp2)

    assert _bp1.url_prefix is '/bp1'
    assert _bp2.url_prefix is '/bp2'

    _bpg.append(_bp1_1)

    assert _bp1_1.url_prefix is '/bp1/bp1.1'


# Unit test implementation to validate blueprint-group url prefix

# Generated at 2022-06-14 07:03:37.601810
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.insert(0, bp1)
    assert bp1.version is None
    assert bp1.strict_slashes is None
    bpg.insert(1, bp2)
    assert bp1.version is None
    assert bp1.strict_slashes is None



# Generated at 2022-06-14 07:03:50.937948
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from sanic import Sanic
    from sanic.blueprints import Blueprint

    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bpg = BlueprintGroup(bp1, bp2, url_prefix="/bpg")
    app = Sanic("test_BlueprintGroup")

    @bpg.middleware('request')
    def common_middleware_all_blueprints(request):
        pass

    @bp1.middleware('request')
    def bp1_middleware(request):
        pass

    @bp2.middleware('request')
    def bp2_middleware(request):
        pass

    @bp1.route('/')
    async def bp1_handler(request):
        return text('')



# Generated at 2022-06-14 07:04:00.166796
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    # unit test for method insert of class BlueprintGroup
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)

    assert bpg._blueprints == [bp1]

    bpg.append(bp2)
    assert bpg._blueprints == [bp1, bp2]

    bpg.insert(0, bp1)
    assert bpg._blueprints == [bp1, bp1, bp2]


# Generated at 2022-06-14 07:04:09.794715
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    app = Sanic('test_BlueprintGroup___delitem__')
    bp1 = Blueprint('bp1', url_prefix='bp1')
    bp2 = Blueprint('bp2', url_prefix='bp2')

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


# Generated at 2022-06-14 07:04:22.757318
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')
    bp7 = Blueprint('bp7', url_prefix='/bp7')

    bpg1 = BlueprintGroup(url_prefix='/bpg1')
    bpg1.append(bp1)
    bpg1.append(bp2)

    bpg2 = BlueprintGroup(url_prefix='/bpg2')

# Generated at 2022-06-14 07:04:26.966358
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    blueprint_group = BlueprintGroup('/api', 1, True)
    blueprint = Blueprint('bp1', url_prefix='/bp1')
    blueprint_group.append(blueprint)

    blueprint_group[0] = blueprint
    assert blueprint_group[0] == blueprint


# Generated at 2022-06-14 07:05:07.688891
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp_one = Blueprint('bp1', url_prefix="/bp1", strict_slashes=False)
    bp_two = Blueprint('bp2', url_prefix="/bp2", strict_slashes=False)

    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp_one)
    bpg.append(bp_two)

    assert bp_one.url_prefix == "/api/bp1"
    assert bp_two.url_prefix == "/api/bp2"


# Generated at 2022-06-14 07:05:18.208707
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp5')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    assert isinstance(bpg, MutableSequence)
    assert isinstance(bpg, BlueprintGroup)
    assert isinstance(bpg, object)

    for b in [bp1, bp2, bp3, bp4]:
        assert isinstance(b, Blueprint)
        assert isinstance(b, object)

    bpg_list = [i for i in bpg]

    assert isinstance

# Generated at 2022-06-14 07:05:20.317514
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    assert BlueprintGroup().__len__() == 0



# Generated at 2022-06-14 07:05:25.757481
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()

    group.append(bp1)
    group.append(bp2)

    assert group[0] == bp1
    assert group[1] == bp2


# Generated at 2022-06-14 07:05:28.115496
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    """
    Test case for method __delitem__ of class BlueprintGroup
    """
    pass



# Generated at 2022-06-14 07:05:34.565111
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():

    blueprint_group = BlueprintGroup()
    blueprint = Blueprint('bp1', url_prefix='/bp1')

    blueprint_group.insert(0, blueprint)

    assert blueprint_group.url_prefix is None
    assert blueprint_group.version is None
    assert blueprint_group.strict_slashes is None
    assert blueprint_group[0] == blueprint
    assert blueprint_group.blueprints == [blueprint]


# Generated at 2022-06-14 07:05:40.621004
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2)
    assert type(bpg) == BlueprintGroup
    assert type(bpg.__iter__()) == type(iter([]))



# Generated at 2022-06-14 07:05:50.347078
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    from sanic.blueprints import Blueprint
    from sanic.request import Request

    bp1 = Blueprint("bp1", url_prefix="/bp1", version="v1")
    bp2 = Blueprint("bp2", url_prefix="/bp2", version="v2")

    bpg = BlueprintGroup("/api", "v1", strict_slashes=False)
    bpg.append(bp1)
    bpg.append(bp2)

    assert bpg.url_prefix == "/api"
    assert bpg.version == "v1"
    assert bpg.strict_slashes == False

    @bp1.middleware("request")
    async def bp1_only_middleware(request):
        print("applied on Blueprint : bp1 Only")


# Generated at 2022-06-14 07:06:03.182162
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    from sanic.blueprints import Blueprint

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)

    assert list(bpg) == [bp1, bp2, bp3, bp4]


# Generated at 2022-06-14 07:06:09.585915
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    """
    Unit test for method __setitem__ of class BlueprintGroup
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg[0] = bp1
    assert bpg[0] == bp1
    bpg[1] = bp2
    assert bpg[1] == bp2
    assert bpg.blueprints == [bp1, bp2]


# Generated at 2022-06-14 07:06:55.867989
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp1)
    bpg.append(bp2)

    assert bpg.url_prefix == "/api"
    assert bpg.version == "v1"

    assert bpg[0].url_prefix == "/api/bp1"
    assert bpg[0].version == "v1"

    assert bpg[1].url_prefix == "/api/bp2"

# Generated at 2022-06-14 07:07:03.926455
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup(bp1, bp2, url_prefix="/v1", version="v1")
    bpg2 = BlueprintGroup(bp3, bp4, url_prefix="/v2", version="v2")
    bpg3 = BlueprintGroup(bpg1, bpg2, url_prefix="/api", version="v3")
    @bp1.middleware('request')
    def bp1_middleware(request):
        assert request == 1
        return


# Generated at 2022-06-14 07:07:15.208391
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    # Create a new Blueprint group instance
    group = BlueprintGroup("/api/v1")
    assert isinstance(group, BlueprintGroup)

    # Check the blueprint group attributes
    assert group.url_prefix == "/api/v1"
    assert group.blueprints == []
    assert group.version is None
    assert group.strict_slashes is None

    # Ensure BlueprintGroup is a mutable sequence
    assert isinstance(group, MutableSequence)

    # Check the default behavior of class Blueprint
    with pytest.raises(IndexError):
        group[0]

    # Adding a new blueprint object
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    group.append(bp1)

    # Check if the new item is added