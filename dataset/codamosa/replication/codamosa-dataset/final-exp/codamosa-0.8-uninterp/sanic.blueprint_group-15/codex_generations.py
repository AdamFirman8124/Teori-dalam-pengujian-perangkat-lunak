

# Generated at 2022-06-14 06:57:41.543903
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():

    bp = Blueprint('bp', url_prefix='')

    @bp.middleware('request')
    async def bp_middleware(request):
        pass

    @bp.middleware('response')
    async def bp_middleware(request, response):
        pass

    bpg = BlueprintGroup()
    bpg.append(bp)

    @bpg.middleware('request')
    async def bp_middleware(request):
        pass

    @bpg.middleware('response')
    async def bp_middleware(request, response):
        pass

    assert len(bpg[0]._middleware['request']) == 2
    assert len(bpg[0]._middleware['response']) == 2

# Generated at 2022-06-14 06:57:49.396011
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup(bp1, bp2)


    @group.middleware('request')
    def group_middleware(request):
        pass

    assert len(group.blueprints[0].middleware) == 1
    assert len(group.blueprints[1].middleware) == 1

# Generated at 2022-06-14 06:57:59.803076
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Test Case 1: BlueprintGroup, Blueprint and the @middleware decorator
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup(url_prefix='/api')

    group.append(bp1)
    group.append(bp2)

    @group.middleware()
    async def test_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    # assert the middleware is registered on both the Blueprints of the group
    assert test_middleware in bp1.middlewares.values()
    assert test_middleware in bp2.middlewares.values()

    # Test Case 2: BlueprintGroup and the middleware, without Blueprint
    #             registration


# Generated at 2022-06-14 06:58:07.130777
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    from copy import copy
    from unittest.mock import Mock

    app = Mock(name="TestApp")

    def middleware(request):
        pass

    def fn(request):
        pass

    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")

    bpg = BlueprintGroup(bp1, bp2, bp3)

    assert bpg.blueprints == [bp1, bp2, bp3]

    # Method middleware should add middleware to all blueprints in group
    bpg.middleware(middleware)
    assert bp1.middleware_functions == [middleware]
    assert bp2.middleware_functions == [middleware]
    assert bp3.middleware_functions == [middleware]

# Generated at 2022-06-14 06:58:16.722147
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    # Create app and apply blueprints
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')

    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)

    # Create a blueprint group
    group = Blueprint.group(bp1, bp2)

    # Create middleware
    count = 0
    @group.middleware('request')
    async def group_middleware(request):
        nonlocal count
        count += 1

    # Create app and apply blueprints
    app = Sanic('test_BlueprintGroup_middleware')

# Generated at 2022-06-14 06:58:27.764168
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    This test case will exercise the BlueprintGroup.middleware method.
    """
    # Create a blue print object
    bp = Blueprint('bp1', url_prefix='/bp1')

    # Declare a sample middleware
    @bp.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    # Create a BlueprintGroup object and apply middleware
    bpg = BlueprintGroup()
    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    # Append Blueprint to the BlueprintGroup
    bpg.append(bp)

    # Test if the blueprint middleware were applied
    assert len(bp.request_middleware) == 2


# Generated at 2022-06-14 06:58:41.648243
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup_middleware")
    parent_bp = Blueprint('parent_bp', url_prefix='/parent_bp')
    child_bp = Blueprint('child_bp', url_prefix='/child_bp')
    parent_bp.group(child_bp)

    async def middleware_handler(request):
        return text("parent middleware")

    @parent_bp.middleware('response')
    async def parent_response_middleware(request):
        return text("parent middleware")

    @child_bp.middleware('request')
    async def child_request_middleware(request):
        return text("child middleware")


# Generated at 2022-06-14 06:58:49.389632
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    """
    Test Case to test the Middleware registration of Blueprint Group.
    """
    blueprint_group_stub = BlueprintGroup()
    blueprint_group_stub.append(Blueprint("bp1", url_prefix="bp1"))
    blueprint_group_stub.append(Blueprint("bp2", url_prefix="bp2"))

    def outer_middleware():
        pass

    blueprint_group_stub.middleware(outer_middleware)(outer_middleware)



# Generated at 2022-06-14 06:58:59.104324
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(bp1, bp2)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    assert(bpg.blueprints[0].middleware_functions['request'] == [group_middleware])
    assert(bpg.blueprints[1].middleware_functions['request'] == [group_middleware])


# Generated at 2022-06-14 06:59:05.965810
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    blueprint1 = sanic.Blueprint('test1')
    blueprint2 = sanic.Blueprint('test2')

    blueprint_group = BlueprintGroup()
    blueprint_group.append(blueprint1)
    blueprint_group.append(blueprint2)

    blueprint_group.middleware(lambda request: request)

    for blueprint in blueprint_group.blueprints:
        assert blueprint.middlewares == [lambda request: request]

# Generated at 2022-06-14 06:59:18.209212
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg) == 2
    assert [bp for bp in bpg] == [bp1, bp2]


# Generated at 2022-06-14 06:59:30.421438
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/api', version='v1')
    bpg.insert(0, bp1)
    bpg.insert(0, bp2)
    assert bpg.url_prefix == '/api'
    assert bpg.version == 'v1'
    assert bp1.url_prefix == '/api/bp1'
    assert bp2.url_prefix == '/api/bp2'
    assert bp1.version == 'v1'
    assert bp2.version == 'v1'


# Generated at 2022-06-14 06:59:39.988435
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4)
    bpg.__delitem__(0)
    assert bpg[0] == bp4
    assert len(bpg) == 1


# Generated at 2022-06-14 06:59:49.366464
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.insert(0, bp3)
    bpg.insert(1, bp4)
    assert bpg._blueprints == [bp3, bp4]


# Generated at 2022-06-14 07:00:01.484146
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    """
    Test the BlueprintGroup object initialization
    :return: None
    """
    # Create an empty BlueprintGroup
    bpg1 = BlueprintGroup()

    # Test that we have empty blueprint list
    assert len(bpg1.blueprints) == 0

    # Test for initialization with various parameters
    bpg2 = BlueprintGroup(url_prefix="/api")
    assert bpg2.url_prefix == "/api"
    assert bpg2.version is None
    assert bpg2.strict_slashes is None

    # Test for initialization with various parameters
    bpg3 = BlueprintGroup(url_prefix="/bpg3")
    assert bpg3.url_prefix == "/bpg3"
    assert bpg3.version is None
    assert bpg3.strict_slashes is None

    # Test for initialization with various parameters
   

# Generated at 2022-06-14 07:00:14.918863
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = mock.MagicMock(name="app")
    bp1 = mock.MagicMock(name="bp1")
    bp2 = mock.MagicMock(name="bp2")
    bp3 = mock.MagicMock(name="bp3")
    bp4 = mock.MagicMock(name="bp4")

    bg = BlueprintGroup()
    bg._blueprints = [bp1, bp2]
    bg2 = BlueprintGroup()
    bg2._blueprints = [bp3, bp4]
    bp1._blueprints = [bg2]

    fn = mock.MagicMock(name="fn")

# Generated at 2022-06-14 07:00:20.574373
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    blueprint_group = BlueprintGroup()
    blueprint_group.append(sanic.Blueprint(name="test", url_prefix="/test"))
    blueprint_group[0]["value"] = 1
    assert blueprint_group[0]["value"] == 1



# Generated at 2022-06-14 07:00:29.964404
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    from sanic import Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    assert len(bpg) == 2


# Generated at 2022-06-14 07:00:39.426903
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("BlueprintGroup")
    bp1 = sanic.Blueprint("bp1", url_prefix="/bp1")
    bp2 = sanic.Blueprint("bp2", url_prefix="/bp2")

    bp1.register_middleware(blueprint_group_middleware,
                            attach_to='bp2')  # middleware does not attach to bp2, since bp1 is not in bp2
    bp2.register_middleware(blueprint_group_middleware)
    bp2.register_middleware(blueprint_group_middleware)  # Duplicated middleware should be registered
    bpg = BlueprintGroup(bp1, bp2)
    bp1.register_blueprint(bpg, url_prefix="/bp1")  # Nested Blueprint group
   

# Generated at 2022-06-14 07:00:51.050328
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """
        Unit test for method __getitem__ of class BlueprintGroup
    """
    blueprint_group = BlueprintGroup()
    blueprint_group.append(sanic.Blueprint("bp1", url_prefix="/bp1"))
    blueprint_group.append(sanic.Blueprint("bp2", url_prefix="/bp2"))
    blueprint_group.append(sanic.Blueprint("bp3", url_prefix="/bp3"))
    blueprint_group.append(sanic.Blueprint("bp4", url_prefix="/bp4"))
    assert blueprint_group[0].name == "bp1"
    assert blueprint_group[1].name == "bp2"
    assert blueprint_group[2].name == "bp3"
    assert blueprint_group[3].name == "bp4"


# Generated at 2022-06-14 07:01:08.769859
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1', version="v1")
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')

    bp4 = Blueprint('bp2', url_prefix='/bp4', version="v2")

    bpg = BlueprintGroup(url_prefix="/api")
    bpg.append(bp1)
    bpg.append(bp2)

    assert bp1.url_prefix == "/api/bp1"
    assert bp2.url_prefix == "/api/bp2"
    assert bp1.version == "v1"
    assert bp2.version == "v1"
    assert bp1.strict_slashes == None
    assert bp2

# Generated at 2022-06-14 07:01:14.051538
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    assert len(BlueprintGroup()) == 0

    bp1 = Blueprint("bp1")
    assert len(BlueprintGroup(bp1)) == 1

    bp2 = Blueprint("bp2")
    assert len(BlueprintGroup(bp1, bp2)) == 2


# Generated at 2022-06-14 07:01:18.886998
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    blueprint = Blueprint("", url_prefix="/")
    blueprint_group = BlueprintGroup()
    blueprint_group.append(blueprint)
    blueprint_1 = Blueprint("", url_prefix="/")
    blueprint_group[0] = blueprint_1
    assert blueprint_group._blueprints[0] == blueprint_1


# Generated at 2022-06-14 07:01:28.203887
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    bpg2 = BlueprintGroup(bpg1, bp3, bp4, url_prefix="/api2", version="v2")
    it = iter(bpg2)
    assert next(it) == bpg1
    assert next(it) == bp3
    assert next(it) == bp4

# Generated at 2022-06-14 07:01:36.835180
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp2.version = "v2"
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.insert(0, bp2)
    assert bpg.blueprints[0].version == "v2"
    assert bpg.blueprints[1].url_prefix == "/bp1"


# Generated at 2022-06-14 07:01:41.411869
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1')
    bp2 = Blueprint('bp2')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    assert bpg[0] == bp1
    assert bpg[1] == bp2


# Generated at 2022-06-14 07:01:55.182077
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bpg1 = BlueprintGroup(bp3, bp4, url_prefix="/bpg1", version="v1")
    bpg2 = BlueprintGroup(bpg1, bp1, bp2, url_prefix="/bpg2", version="v2")

    assert bp1.url_prefix == "/bp1"
    assert bp2.url_prefix == "/bp2"
    assert bp3.url_prefix == "/bpg1/bp3"

# Generated at 2022-06-14 07:02:03.493151
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """
    Test cases for method `__getitem__` of class `BlueprintGroup`
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    assert bpg[1] == bp2



# Generated at 2022-06-14 07:02:15.681572
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    assert bpg[0] == bp1
    assert bpg[1] == bp2

    bpg.__setitem__(0, bp3)

    assert bpg[0] == bp3
    assert bpg[1] == bp2

    bpg.__setitem__(1, bp4)

    assert bpg[0] == bp3
    assert b

# Generated at 2022-06-14 07:02:28.237577
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint("bp1")
    bp1.route("/")(lambda r: "bp1")

    bp2 = Blueprint("bp2")
    bp2.route("/")(lambda r: "bp2")

    bp3 = Blueprint("bp3")
    bp3.route("/")(lambda r: "bp3")

    bp4 = Blueprint("bp4")
    bp4.route("/")(lambda r: "bp4")

    bpg = BlueprintGroup()

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    # test1: object bp3 should be deleted
    bpg.__delitem__(2)

    assert len(bpg) == 2

    # test2: object bp2 should

# Generated at 2022-06-14 07:02:47.318527
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg1 = BlueprintGroup()
    bpg2 = BlueprintGroup(url_prefix='/parent')

    bpg1.append(bp1)
    bpg1.append(bp2)

    bpg2.append(bp3)
    bpg2.append(bp4)

    assert len(bpg1) == 2
    assert len(bpg2) == 2
    assert bp1.url_prefix == '/bp1'
    assert bp2.url_prefix == '/bp2'

# Generated at 2022-06-14 07:03:01.471354
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert len(bpg) == 0

    bpg.append(bp1)
    assert len(bpg) == 1
    assert bpg[0] == bp1

    bpg.insert(1, bp2)
    assert len(bpg) == 2
    assert bpg[1] == bp2

    bpg.insert(1, bp3)
    assert len(bpg) == 3
    assert bpg

# Generated at 2022-06-14 07:03:08.604826
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = BlueprintGroup()
    group.append(bp1)
    group.append(bp2)
    assert len(group) == 2
    assert group[0] == bp1
    assert group[1] == bp2


# Generated at 2022-06-14 07:03:15.802026
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup()
    assert len(bpg) == 0

    bpg.append(bp1)
    assert len(bpg) == 1

    bpg.append(bp2)
    assert len(bpg) == 2



# Generated at 2022-06-14 07:03:23.721226
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="1.0")
    assert bpg.version == "1.0"
    assert len(bpg.blueprints) == 2
    assert bpg.blueprints[0].version == "1.0"
    assert not bpg.blueprints[0].strict_slashes
    assert bpg.blueprints[0].url_prefix == "/api/bp3"

    bpg.append(bp1)
    bpg.insert(1, bp2)


# Generated at 2022-06-14 07:03:33.392497
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup(bp1, bp2, url_prefix="/api",
                           version="v1", strict_slashes=True)
    assert bp1 in group.blueprints
    assert bp2 in group.blueprints

    assert group.url_prefix == "/api"
    assert group.version == "v1"
    assert group.strict_slashes is True



# Generated at 2022-06-14 07:03:40.227548
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = [bp3, bp4]
    assert len(bpg) == 2
    assert bp3 in bpg and bp4 in bpg
    del bpg[1]
    assert bp3 in bpg and bp4 not in bpg


# Generated at 2022-06-14 07:03:48.505992
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    assert list(bpg) == [bp3, bp4]


# Generated at 2022-06-14 07:03:56.235421
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp_group = BlueprintGroup('/test-group', version='v1', strict_slashes=True)
    bp_group.append(Blueprint('test1'))
    bp_group.append(Blueprint('test2'))
    del bp_group[0]
    assert len(bp_group) == 1
    assert isinstance(bp_group, BlueprintGroup)
    assert bp_group[0].name == 'test2'


# Generated at 2022-06-14 07:04:03.206302
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    group = Blueprint.group(bp1, bp2)
    #group.__delitem__(1)
    del group[1]
    assert group.blueprints[0].name == 'bp1'


# Generated at 2022-06-14 07:04:27.467413
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    assert bpg[0] == bp3
    assert bpg[1] == bp4


# Generated at 2022-06-14 07:04:36.851927
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/api', version="v1")
    bpg.append(bp1)
    assert len(bpg) == 1
    bpg.append(bp2)
    assert len(bpg) == 2
    del bpg[0]
    assert len(bpg) == 1
    bpg[0] = bp1
    assert len(bpg) == 1


# Generated at 2022-06-14 07:04:45.844771
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp1/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp1/bp3/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp1/bp5')
    bg1 = BlueprintGroup('/api', version='v1')
    bg1.append(bp3)
    bg1.append(bp4)
    bg1.append(bp5)
    bg1.append(bp1)
    bg1.append(bp2)

# Generated at 2022-06-14 07:05:00.087815
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    def test_insert_func1(object, index, item):
        object.insert(index=index, item=item)
        assert object[index] == item

    # Test Case: Test insertion of Blueprint group
    test_obj = BlueprintGroup()
    test_insert_func1(test_obj, 0, Blueprint(url_prefix="test"))

    # Test Case: Test insertion of Blueprint group after an existing item.
    test_obj = BlueprintGroup()
    test_obj.append(Blueprint(url_prefix="test1"))
    test_obj.append(Blueprint(url_prefix="test2"))
    test_insert_func1(test_obj, 2, Blueprint(url_prefix="test3"))

    # Test Case: Test insertion of Blueprint group before and existing item
    test_obj = BlueprintGroup()

# Generated at 2022-06-14 07:05:05.460458
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    b = BlueprintGroup()
    b.append(Blueprint('bp1', url_prefix='/bp1'))
    b.append(Blueprint('bp2', url_prefix='/bp2'))
    assert b[0].name == 'bp1'
    assert b[1].name == 'bp2'
    assert len(b) == 2


# Generated at 2022-06-14 07:05:17.534417
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    url_prefix = "/some_prefix"
    version = "v1"
    strict_slashes = True
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix=url_prefix, version=version,
                        strict_slashes=strict_slashes)
    bpg.append(bp3)
    bpg.append(bp4)

    # Check for len of blueprints
    assert len(bpg._blueprints) == 2

    # Check for url_prefix is set correctly
    assert bpg.url_prefix == url_prefix

    # Check for version added correctly
    assert bpg.version == version

    # Check for strict_slashes is set correctly
    assert bpg.st

# Generated at 2022-06-14 07:05:25.315554
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    url_prefix = '/abc'
    bp = Blueprint('bp', url_prefix=url_prefix)
    bpg = BlueprintGroup(url_prefix=url_prefix)
    bpg.append(bp)
    bpg[0] = bp

    expected_url_prefix = '/abc/abc'
    actual_url_prefix = bpg.url_prefix
    assert expected_url_prefix == actual_url_prefix


# Generated at 2022-06-14 07:05:34.411074
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.insert(0,bp2)
    assert bpg._blueprints[0].url_prefix == '/api/bp2'
    assert bpg._blueprints[1].url_prefix == '/api/bp1'
    assert bpg.url_prefix == '/api'
    assert bpg.version == 'v1'

# Generated at 2022-06-14 07:05:47.090010
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bpg1 = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    bpg2 = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    assert bpg2[0] == bp3
    assert bpg2[1] == bp4

    bpg2[0] = bp1
    bpg2[1] = bp2

    assert bpg2[0] == bp1
    assert bpg2[1] == b

# Generated at 2022-06-14 07:05:52.671421
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')

    bpg = BlueprintGroup(url_prefix='/bp1')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)
    bpg.append(bp5)

    assert isinstance(bpg, BlueprintGroup)
    assert bpg[0] == bp1
    assert bpg[1] == bp2