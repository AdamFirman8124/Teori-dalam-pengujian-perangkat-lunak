

# Generated at 2022-06-14 06:57:29.413711
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    # Adding the middleware function
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    @bp2.middleware('request')
    async def bp2_only_middleware(request):
        print('applied on Blueprint : bp2 Only')

    # Applying the middleware function to the bp1 and bp2 blueprints
    group = Blueprint.group(bp1, bp2)
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

# Generated at 2022-06-14 06:57:34.787402
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    blue1 = Blueprint('bp1', url_prefix='/bp1')
    blue2 = Blueprint('bp2', url_prefix='/bp2')

    blue1.route('/')
    blue2.route('/<param>')

    group = BlueprintGroup(blue1, blue2)

    assert len(group) == 2


# Generated at 2022-06-14 06:57:36.676762
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert isinstance(bpg, BlueprintGroup)


# Generated at 2022-06-14 06:57:49.036776
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    # BluePrint Group
    from sanic import Blueprint
    from sanic.utils import sanic_endpoint_test
    from sanic.response import text
    return_value = None
    #  Create a Blueprint Group
    bpg = BlueprintGroup()
    # Create a Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    # Create a Blueprint
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    # Add Blueprint
    bpg.append(bp1)
    # Add Blueprint
    bpg.append(bp2)
    # Append
    bpg._blueprints.append(bp1)
    # Update URL of Blueprint group
    bpg._url_prefix = "/api"



# Generated at 2022-06-14 06:57:59.580349
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    """
    Test case for the BlueprintGroup append function
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp3_2 = Blueprint("bp3_2", url_prefix="/bp3_2")
    group = BlueprintGroup("/api", "v1")
    group.append(bp1)
    group.append(bp2)

    nested_group = BlueprintGroup("/api", "v2")
    nested_group.append(bp3)
    nested_group.append(bp3_2)
    nested_group.append(group)

    assert len(nested_group) == 4


# Generated at 2022-06-14 06:58:06.486193
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.extend([bp3, bp4])
    bpg1 = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    assert bpg1[1] is bp4
    assert bpg[1] is bp4



# Generated at 2022-06-14 06:58:14.722027
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert bpg.append(bp1) == None



# Generated at 2022-06-14 06:58:26.783440
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp1.middleware('response')(lambda r, c: None)
    bp2.middleware('response')(lambda r, c: None)
    bp1.route('/', methods=['GET'], name='bp1')(lambda r: r)
    bp2.route('/', methods=['GET'], name='bp2')(lambda r: r)
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.middleware('response')(lambda r, c: None)
    bpg.registrar.get_routes()
    assert bp1.regist

# Generated at 2022-06-14 06:58:30.554685
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    # Arrange
    b1 = Blueprint('bp1', url_prefix='/bp1')
    b2 = Blueprint('bp2', url_prefix='/bp2')
    bp_group = BlueprintGroup()

    # Act
    bp_group.append(b1)
    bp_group.append(b2)

    # Assert
    assert len(bp_group) == 2


# Generated at 2022-06-14 06:58:44.721196
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup(url_prefix="/api/v1", strict_slashes=True)
    assert group.url_prefix == "/api/v1"
    assert group.version is None
    assert group.strict_slashes is True

    group.append(bp1)
    group.append(bp2)
    assert len(group) == 2
    assert group[0] == bp1
    assert group[1] == bp2

    assert bp2 in group
    assert bp1 in group
    assert Blueprint('bp3', url_prefix='/bp3') not in group

    group.insert(0, bp2)