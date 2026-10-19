

# Generated at 2022-06-14 06:57:09.758383
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    pass

# Generated at 2022-06-14 06:57:20.837008
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

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

    @app.route('/')
    async def app_route(request):
        return text('app')

    # Register

# Generated at 2022-06-14 06:57:33.766707
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")

    assert len(bp1.middlewares['request']) == 0
    assert len(bp2.middlewares['request']) == 0

    @bpg.middleware('request')
    def bpg_request_middleware(req):
        pass

    assert len(bp1.middlewares['request']) == 1
    assert len(bp2.middlewares['request']) == 1


# Generated at 2022-06-14 06:57:45.153000
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = Sanic(__name__)
    b1 = Blueprint('b1')
    b2 = Blueprint('b2')
    b3 = Blueprint('b3')
    b4 = Blueprint('b4')
    b5 = Blueprint('b5')
    b6 = Blueprint('b6')

    bg1 = BlueprintGroup(b1, b2)
    bg2 = BlueprintGroup(b3, b4)
    bg3 = BlueprintGroup(b5, b6)

    @bg1.middleware('request')
    async def bg_middleware(request):
        print('common middleware applied for b1 and b2')

    @bg2.middleware('request')
    async def bg_middleware(request):
        print('common middleware applied for b3 and b4')


# Generated at 2022-06-14 06:57:53.905024
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    class TestMiddleware:
        pass

    bp = Blueprint('test')

    @bp.route('/test')
    async def test_route(request):
        return text('BP Group middleware test')

    bpg = BlueprintGroup()
    bpg.append(bp)

    @bpg.middleware('request')
    async def group_middleware(request):
        pass

    assert any(
        isinstance(r.handler, TestMiddleware)
        for r in bp.registered_endpoints
    )
    assert isinstance(bp.middleware['request'][0], TestMiddleware)

# Generated at 2022-06-14 06:58:00.447430
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    class request_middleware:
        def __init__(self, app, request):
            pass

        async def __call__(self, request):
            return request

    class response_middleware:
        def __init__(self, app, request, response):
            pass

        async def __call__(self, request, response):
            return response

        def __call__(self, request, response):
            return response

    app = sanic.Sanic(__name__)

    class test_blueprint_group(BlueprintGroup):
        pass

    test_blueprint_group.middleware(request_middleware)
    test_blueprint_group.middleware(response_middleware)

    bp1 = sanic.Blueprint("bp1")
    bp2 = sanic.Blueprint("bp2")

    bpg

# Generated at 2022-06-14 06:58:07.153613
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic(__name__)
    bp = Blueprint('bp', url_prefix='/bp')
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/v1')
    bpg.append(bp1)
    bpg.append(bp2)
    app.blueprint(bp)
    app.blueprint(bpg)

    @bp1.middleware('request')
    def bp1_middleware(request):
        pass

    @bp2.middleware('request')
    def bp2_middleware(request):
        pass

    @bpg.middleware('request')
    def group_middleware(request):
        pass



# Generated at 2022-06-14 06:58:16.722330
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


# Generated at 2022-06-14 06:58:27.580102
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    # Given
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    app.config.REQUEST_MAX_SIZE = 10 << 20

    # When
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        pass

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    group = Blueprint.group(bp1, bp2)

    registered_middleware = []

# Generated at 2022-06-14 06:58:41.259638
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()

    @app.blueprint.middleware('request')
    def bp_request_middleware(request):
        pass

    @app.blueprint.middleware('request')
    def bp_request_middleware2(request):
        pass

    @app.blueprint.middleware('response')
    def bp_response_middleware(request):
        pass

    @app.blueprint.middleware('response')
    def bp_response_middleware2(request):
        pass

    @app.middleware('request')
    def app_request_middleware(request):
        pass

    @app.middleware('request')
    def app_request_middleware2(request):
        pass


# Generated at 2022-06-14 06:58:51.813874
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """Test :class:`~sanic.blueprints.BlueprintGroup`
    :meth:`~sanic.blueprints.BlueprintGroup.middleware` method
    works fine by applying the same middleware on each of the
    blueprint under the group.
    """
    from sanic.log import logger
    from sanic import Sanic

    app = Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    blueprint_group = BlueprintGroup(bp1, bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        logger.info('applied on Blueprint : bp1 Only')
        return


# Generated at 2022-06-14 06:58:59.931716
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)



# Generated at 2022-06-14 06:59:11.388149
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    expected_list_of_bp = [bp1, bp2, bp3, bp4]

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

   

# Generated at 2022-06-14 06:59:24.154574
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)

    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')


# Generated at 2022-06-14 06:59:32.758895
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic()
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)

    @group.middleware
    async def process_request(request):
        request['processed'] = True

    @bp1.route('/middleware')
    async def bp1_middleware(request):
        return text("bp1_middleware")

    @bp2.route('/middleware')
    async def bp2_middleware(request):
        return text("bp2_middleware")

    app.blueprint(group)

    request, response = app.test_client.get('/middleware')
    assert response.text == 'bp1_middleware'
    request,

# Generated at 2022-06-14 06:59:45.225965
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic('test_BlueprintGroup_middleware')

    # Create Group instance
    bpg = BlueprintGroup()

    # Create Blueprints
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')
    bp3 = Blueprint('bp3')
    bp4 = Blueprint('bp4')

    # Append Blueprint to BlueprintGroup
    bpg.append(bp1)
    bpg.append(bp2)

    # Assert BlueprintGroup has 2 Blueprint
    assert len(bpg.blueprints) == 2

    # Define request middleware for BlueprintGroup
    @bpg.middleware('request')
    async def bp_request_middleware(request):
        """
        Middleware that will be applied for all Blueprint
        in Blueprint Group

        """
        pass

    # Ass

# Generated at 2022-06-14 06:59:58.749281
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)
    group.append(bp3)
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')


# Generated at 2022-06-14 07:00:09.210023
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bp_group = BlueprintGroup()
    bp_group.append(bp1)
    bp_group.append(bp2)

    bp_group2 = BlueprintGroup()
    bp_group2.append(bp3)
    bp_group2.append(bp4)

    # bp_group2 should be applied with middleware of bp_group2
    bp_group.append(bp_group2)

    assert 'middleware' in dir(bp1)

# Generated at 2022-06-14 07:00:19.900226
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')
    app = sanic.Sanic('test_BlueprintGroup_middleware')
    bpg1 = BlueprintGroup('/api/v1')
    bpg1._blueprints = [bp1, bp2]
    bpg2 = BlueprintGroup('/api/v2')
    bpg2._blueprints = [bp3, bp4]


# Generated at 2022-06-14 07:00:34.399696
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = sanic.Blueprint("bp1")
    bp2 = sanic.Blueprint("bp2")
    bp_group = BlueprintGroup()
    bp_group.append(bp1)
    bp_group.append(bp2)

    def get_blueprints_middleware(bp, list_middleware):
        middleware = getattr(bp, "middleware", [])
        middleware = [ m[0] for m in middleware ]
        middleware = set(middleware)
        _list = [
            middleware == set(m)
            for m in list_middleware
        ]
        return all(_list)

    @bp_group.middleware("request")
    async def common_middleware(request):
        pass


# Generated at 2022-06-14 07:00:45.728536
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    blueprint_group = BlueprintGroup()
    blueprint1 = Blueprint('test')
    blueprint2 = Blueprint('test')

    blueprint_group.insert(0, blueprint1)
    assert blueprint_group[0] == blueprint1

    blueprint_group.insert(1, blueprint2)
    assert blueprint_group[1] == blueprint2

# Generated at 2022-06-14 07:00:52.937504
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    assert isinstance(bpg, BlueprintGroup)
    assert len(bpg) == 2
    del bpg[1]
    assert len(bpg) == 1
    assert isinstance(bpg._blueprints[0], Blueprint)
    del bpg[0]
    assert len(bpg) == 0
    assert len(bpg._blueprints) == 0


# Generated at 2022-06-14 07:00:58.781281
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    """Test BlueprintGroup class."""
    bp_grp = BlueprintGroup(url_prefix="/api", version="v1")
    assert bp_grp._url_prefix == "/api"
    assert bp_grp._version == "v1"


# Generated at 2022-06-14 07:01:10.288238
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1", strict_slashes=False)
    bpg.append(bp3)
    bpg.append(bp4)

    assert bpg.url_prefix == "/api"
    assert bpg.version == "v1"
    assert bpg.strict_slashes is False

    bpg1 = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1", strict_slashes=False)
    assert bpg1

# Generated at 2022-06-14 07:01:18.009624
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")



# Generated at 2022-06-14 07:01:25.752652
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = Blueprint.group(bp1, bp2)
    @group.middleware
    async def test_bp_group_middleware(request):
        pass

    assert "test_bp_group_middleware" in bp1.middlewares['request']
    assert "test_bp_group_middleware" in bp2.middlewares['request']



# Generated at 2022-06-14 07:01:32.998345
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    blueprint_group = BlueprintGroup()
    blueprint_group.append(sanic.Blueprint('bp1'))
    blueprint_group.append(sanic.Blueprint('bp2'))
    blueprint_group.append(sanic.Blueprint('bp3'))

    index = 0
    for blueprint in blueprint_group:
        index += 1
        assert blueprint.name.startswith('bp')
    assert index == 3



# Generated at 2022-06-14 07:01:42.865747
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    b1 = Blueprint('bp1', url_prefix='/bp1')
    b2 = Blueprint('bp2', url_prefix='/bp2')
    b3 = Blueprint('bp3', url_prefix='/bp3')
    b4 = Blueprint('bp4', url_prefix='/bp4')
    bp_group = BlueprintGroup()
    bp_group.append(b1)
    bp_group.append(b2)
    bp_group.append(b3)
    bp_group.append(b4)
    bp_group.__delitem__(1)
    assert bp_group.__len__() == 3
    assert bp_group.__getitem__(1).name == "bp3"
    assert bp_group.__getitem__(0).name == "bp1"

# Generated at 2022-06-14 07:01:51.646733
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")
    bpg = BlueprintGroup()
    bpg.extend([bp3, bp4])
    assert len(bpg) == 2
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg) == 4



# Generated at 2022-06-14 07:02:03.574163
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg1 = BlueprintGroup(bp3, bp4, url_prefix='/api/v1')
    bpg2 = BlueprintGroup(bpg1, bp2, url_prefix='/api/v1')
    bpg3 = BlueprintGroup(bpg2, bp1, url_prefix='/api/v1')

    request = MockRequest()

    @bpg3.middleware('request')
    async def bpg_middleware(req):
        req.bpg_middleware_called = True

# Generated at 2022-06-14 07:02:17.986398
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    group = Blueprint.group(bp1, bp2)

    for i in range(2):
        @group.middleware('request')
        async def group_middleware(request):
            pass
    assert len(bp1.middlewares["request"]) == 2
    assert len(bp2.middlewares["request"]) == 2

    @group.middleware('request')
    async def group_middleware(request):
        pass
    assert len(bp1.middlewares["request"]) == 3
    assert len(bp2.middlewares["request"]) == 3

    @group.middleware('request')
    async def group_middleware(request):
        pass

# Generated at 2022-06-14 07:02:30.342090
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    
    class App(sanic.Sanic):
        pass

    app = App()
    b1 = Blueprint("b1", version="v1", strict_slashes=True)
    b2 = Blueprint("b2", version="v2", strict_slashes=False)
    b3 = Blueprint("b3", version="v2", strict_slashes=False)
    
    b1.route("/", methods=["GET"])(lambda r: text("1"))
    b2.route("/", methods=["GET"])(lambda r: text("2"))
    b3.route("/", methods=["GET"])(lambda r: text("3"))
    
    bg = BlueprintGroup(url_prefix="/api", version="v1")
    bg.append(b1)
    bg.insert(0,b2)


# Generated at 2022-06-14 07:02:37.362087
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    """
    Unit test to check the functionality of the `BlueprintGroup` append
    operation.

    :return: None
    """
    from sanic.blueprints import Blueprint
    bp_group = BlueprintGroup(url_prefix="/api", version="v1")
    for _ in range(0, 5):
        bp = Blueprint(__name__)
        bp.strict_slashes = True
        bp_group.append(bp)
    assert len(bp_group) == 5
    for bp in bp_group:
        assert bp.url_prefix == "/api"
        assert bp.version == "v1"
        assert bp.strict_slashes is True



# Generated at 2022-06-14 07:02:43.237063
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp1.middleware('request')(lambda x: x)
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)
    assert len(bpg.blueprints) == 4
    assert bpg.blueprints[0] == bp1
    assert bpg.blueprints[1] == bp2
    assert bpg

# Generated at 2022-06-14 07:02:52.020683
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """Test Method __getitem__ of class BlueprintGroup"""
    blueprint_group = BlueprintGroup()
    bp1 = Blueprint("test", url_prefix="/test")
    bp2 = Blueprint("test2", url_prefix="/test2")
    blueprint_group.append(bp1)
    blueprint_group.append(bp2)
    assert blueprint_group[0] == bp1
    assert blueprint_group[1] == bp2
    assert isinstance(blueprint_group[0], Blueprint)
    assert isinstance(blueprint_group[1], Blueprint)

# Generated at 2022-06-14 07:02:56.886982
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """
    Test Method __getitem__ from class BlueprintGroup
    """
    bp = Blueprint("test")
    group = BlueprintGroup()
    group.append(bp)

    assert group[0] == bp


# Generated at 2022-06-14 07:03:04.592353
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup()
    bpg.insert(0, bp1)

    assert bpg[0].name == bp1.name


# Generated at 2022-06-14 07:03:14.259206
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    group = BlueprintGroup()
    assert group.url_prefix is None
    assert group.version is None
    assert group.strict_slashes is None
    assert len(group) == 0

    group = BlueprintGroup("/test", "v1")
    assert group.url_prefix == "/test"
    assert group.version == "v1"
    assert group.strict_slashes is None
    assert len(group) == 0

    group = BlueprintGroup("/test", "v1", True)
    assert group.url_prefix == "/test"
    assert group.version == "v1"
    assert group.strict_slashes is True



# Generated at 2022-06-14 07:03:23.207182
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    url_prefix = '/test'
    bp1, bp2, bp3, bp4 = (
        Blueprint('bp', url_prefix='/bp1'),
        Blueprint('bp', url_prefix='/bp2'),
        Blueprint('bp', url_prefix='/bp3'),
        Blueprint('bp', url_prefix='/bp4'),
    )
    bpg = BlueprintGroup(url_prefix=url_prefix)

    bpg.append(bp1)
    assert bpg[0] == bp1

    bpg.append(bp2)
    assert bpg[1] == bp2

    bpg.append(bp3)
    assert bpg[2] == bp3

    bpg.append(bp4)
    assert bpg[3] == bp4



# Generated at 2022-06-14 07:03:31.780792
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp = Blueprint('testBp', url_prefix='test')
    bp.strict_slashes = True
    blueprints_group = BlueprintGroup()

    blueprints_group.append(bp)
    assert blueprints_group[0] is bp

    # set a new item: 
    new_bp = Blueprint('testBp2', url_prefix='test2')
    blueprints_group[0] = new_bp
    assert blueprints_group[0] is new_bp


# Generated at 2022-06-14 07:03:51.261385
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bp = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    assert len(bp) == 2
    assert next(iter(bp)) == bp3


# Generated at 2022-06-14 07:03:59.746906
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    # pylint: disable=redefined-outer-name
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")

    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp1)
    bpg.append(bp2)

    assert bpg.url_prefix == "/api"
    assert bpg[0].url_prefix == "/api/bp1"
    assert bpg[1].url_prefix == "/api/bp2"


# Generated at 2022-06-14 07:04:11.136479
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp1.route('/')(lambda request: text('bp1'))
    bp2.route('/<param>')(lambda request, param: text(param))
    bpg = BlueprintGroup()
    assert len(bpg) == 0
    bpg.append(bp1)
    assert len(bpg) == 1
    bpg.append(bp2)
    assert len(bpg) == 2
    del bpg[1]
    assert len(bpg) == 1


# Generated at 2022-06-14 07:04:23.322190
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2/")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4/")

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)

    assert bpg.url_prefix == "/api"
    assert bpg.version == "v1"
    assert isinstance(bpg, BlueprintGroup)
    assert isinstance(bpg.blueprints, list)
    assert len(bpg.blueprints) == 4


# Generated at 2022-06-14 07:04:32.475142
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    """Test the insert method of class BlueprintGroup.

    Test if the Blueprint can be inserted into BlueprintGroup.

    :return: `None`
    """
    blueprint_group_one = BlueprintGroup()
    blueprint_one = Blueprint(name='bp1')
    blueprint_two = Blueprint(name='bp2')
    blueprint_three = Blueprint(name='bp3')
    blueprint_group_one.insert(0, blueprint_one)
    blueprint_group_one.insert(0, blueprint_two)
    blueprint_group_one.insert(0, blueprint_three)
    assert blueprint_group_one[0] == blueprint_three
    assert blueprint_group_one[1] == blueprint_two
    assert blueprint_group_one[2] == blueprint_one
    blueprint_group_one.insert(1, blueprint_one)
    assert blueprint_

# Generated at 2022-06-14 07:04:40.921412
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    app = sanic.Sanic(__name__)
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bpg = BlueprintGroup(bp1, bp2, bp3)
    bpg.__delitem__(1)
    assert bpg.blueprints == [bp1, bp3]

# Generated at 2022-06-14 07:04:43.300510
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    # BlueprintGroup.__delitem__ doesn't takes argument(s), so
    # just using this for testing purpose.
    _ = BlueprintGroup()



# Generated at 2022-06-14 07:04:54.825587
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1', strict_slashes=True)
    bpg = BlueprintGroup(url_prefix='/bpg', version='v1')

    bp1.route('/bp1_route')(lambda x: x)
    bpg.insert(0, bp1)

    assert bpg.url_prefix == '/bpg'
    assert bpg.version == 'v1'
    assert bp1.url_prefix == '/bpg/bp1'
    assert bp1.version == 'v1'



# Generated at 2022-06-14 07:05:04.011286
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix='/api')
    bpg.extend([bp1, bp2])
    len(bpg) == 2
    bpg.append(bp3)
    len(bpg) == 3
    bpg.insert(0,bp4)
    len(bpg) == 4
    bpg.remove(bp3)
    len(bpg) == 3
    bpg.clear()
    len(bpg) == 0


# Generated at 2022-06-14 07:05:11.350858
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup(url_prefix='/api')

    group.append(bp1)
    group.append(bp2)

    assert len(group) == 2
