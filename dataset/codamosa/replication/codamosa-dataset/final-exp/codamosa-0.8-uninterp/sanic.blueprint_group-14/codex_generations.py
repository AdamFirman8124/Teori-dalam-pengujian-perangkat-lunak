

# Generated at 2022-06-14 06:57:29.858365
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    BlueprintGroup.insert("Blueprint Group Object","Blueprint Object")
	

# Generated at 2022-06-14 06:57:35.957060
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp_group = [bp1,bp2]
    assert bp_group[0] == bp1
    assert bp_group[1] == bp2
    assert bp_group[-1] == bp2


# Generated at 2022-06-14 06:57:49.667906
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bg = BlueprintGroup()
    bg._blueprints.append(bp1)
    bg._blueprints.append(bp2)
    assert bg[0] == bp1
    assert bg[1] == bp2
    assert bg[0].name == 'bp1'
    assert bg[1].name == 'bp2'
    assert bg.version is None
    assert bg.url_prefix is None
    assert bg.strict_slashes is None
    bg2 = BlueprintGroup(url_prefix='/', version='v3', strict_slashes=True)
    assert bg2.version == 'v3'

# Generated at 2022-06-14 06:57:55.769946
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp = Blueprint('test', url_prefix='')
    bpGroup = BlueprintGroup(bp, '', '')
    @bp.middleware('request')
    async def bp_middleware(request):
        print('bp applied')
    @bpGroup.middleware('request')
    async def bpGroup_middleware(request):
        print('bpGroup applied')


# Generated at 2022-06-14 06:58:02.416775
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    for bp in bpg:
        assert bp in [bp1, bp2]


# Generated at 2022-06-14 06:58:13.053909
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    """
    Test BlueprintGroup.insert()
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg[1] = bp4
    assert bpg[0] == bp1
    assert bpg[1] == bp4
    assert bpg[2] == bp3
    assert len(bpg) == 3


# Generated at 2022-06-14 06:58:26.154333
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp3)
    bpg.append(bp4)
    assert bpg[0] == bp3
    assert bpg[1] == bp4
    assert bpg[0].url_prefix == "/api/bp3"
    assert bpg[1].url_prefix == "/api/bp4"
    assert bpg[0].version == "v1"

# Generated at 2022-06-14 06:58:27.055492
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    pass


# Generated at 2022-06-14 06:58:28.715129
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    BlueprintGroup()


# Generated at 2022-06-14 06:58:42.984686
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    """Unit Test for BlueprintGroup->__delitem__()"""
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bg = BlueprintGroup()
    bg.append(bp1)
    bg.append(bp2)
    bg.append(bp3)
    bg[0:2]
    del bg[0]
    assert len(bg) == 2
    assert bg[0] == bg._blueprints[0]
    assert bg[0].url_prefix == bp2.url_prefix
    bp1 = Blueprint('bp1', url_prefix='/bp1')

# Generated at 2022-06-14 06:58:52.294981
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    group = Blueprint.group(bp1,bp2)

    assert group._blueprints == [bp1, bp2]
    assert bpg._blueprints == [bp3, bp4]

    del group._blueprints[0]
    del bpg._blueprints[0]

    assert group._blueprints == [bp2]
    assert bpg._blueprints == [bp4]

# Unit test

# Generated at 2022-06-14 06:58:58.469486
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    blueprints = list()
    for blueprint in bpg:
        blueprints.append(blueprint)
    assert bp1 in blueprints
    assert bp2 in blueprints
    assert len(blueprints) == 2


# Generated at 2022-06-14 06:59:10.998100
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')
    bp3 = sanic.Blueprint('bp3', url_prefix='/bp3')
    bp4 = sanic.Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    
    bpg[0] = bp1
    bpg[1] = bp2
    bpg[2] = bp3
    bpg[3] = bp4
    
    assert len(bpg) == 4
    assert bpg[0] == bp1
    assert bpg[1] == bp2
    assert bpg

# Generated at 2022-06-14 06:59:20.441983
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    app = sanic.Sanic('test_sanic_17', configure_logging=False)
    app.config['REQUEST_MAX_SIZE'] = 10

    bp1 = Blueprint('bp1', url_prefix='/bp1')

    @bp1.route('/index')
    async def bp1_index(request):
        return text('OK')

    url = app.url_for('bp1_index')
    assert url == '/bp1/index'

if __name__ == "__main__":
    pytest.main()

# Generated at 2022-06-14 06:59:27.842150
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    blueprint_group = BlueprintGroup()
    blueprint_group.append(Blueprint('testbp1'))
    blueprint_group.append(Blueprint('testbp2'))
    blueprint_group.append(Blueprint('testbp3'))

    for index, blueprint in enumerate(blueprint_group):
        assert blueprint.name == f'testbp{index + 1}'


# Generated at 2022-06-14 06:59:36.929520
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg._blueprints = [bp1, bp2]
    group_iterator = bpg.__iter__()
    first = group_iterator.__next__()
    second = group_iterator.__next__()
    assert first == bp1
    assert second == bp2



# Generated at 2022-06-14 06:59:44.198202
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg) == 2

# Generated at 2022-06-14 06:59:57.714910
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """
    Test the blueprint group's list like behavior by retrieving
    blueprint objects using index, slice, splice operations
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    group = BlueprintGroup()

    # Old behavior is to add only blueprints to the group.
    # Blueprints can be added using append and insert.
    group.append(bp1)
    group.insert(0, bp2)

    # Behavior changed, blueprint group should be able to add
    # blueprint groups as well as blueprint.
    assert len(group) == 2
    group.append(bp3)
    assert len(group) == 3

    assert group[0]

# Generated at 2022-06-14 07:00:09.014140
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    def assert_is_list(list_):
        assert isinstance(list_, list)
        assert not isinstance(list_, BlueprintGroup)

    bp = BlueprintGroup()
    bp.append(1)
    bp.append(2)

    assert 2 == len(bp)
    assert bp[0] == 1
    assert bp[1] == 2
    assert_is_list(bp._blueprints)

    bp[0] = 3
    assert 3 == len(bp)
    assert bp[0] == 3
    assert bp[1] == 2
    assert_is_list(bp._blueprints)

    bp.insert(0, 1)
    assert 3 == len(bp)
    assert bp[0] == 1
    assert bp[1] == 3
    assert bp

# Generated at 2022-06-14 07:00:16.888345
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    from sanic import Blueprint

    blueprint = Blueprint("test_blueprint")
    blueprint_group = BlueprintGroup()
    blueprint_group.append(blueprint)

    with pytest.raises(IndexError):
        blueprint_group[5] = blueprint

    blueprint_group[0] = blueprint
    del blueprint_group[1]

    with pytest.raises(IndexError):
        del blueprint_group[2]


# Generated at 2022-06-14 07:00:26.272135
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    gp = BlueprintGroup("/api", version="v1")
    gp.append(Blueprint("bp1", url_prefix="/bp1"))
    gp.append(Blueprint("bp2", url_prefix="/bp2"))
    gp.append(Blueprint("bp2", url_prefix="/bp2"))
    assert(len(gp) == 3)

# Generated at 2022-06-14 07:00:28.076322
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    BlueprintGroup.insert(index, item)


# Generated at 2022-06-14 07:00:31.481633
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp = Blueprint("test_bp")
    bpg = BlueprintGroup()

    bpg.append(bp)

    assert bpg.blueprints == [bp]


# Generated at 2022-06-14 07:00:40.911335
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    class DummyBlueprint:
        pass
    dummy_blueprint = DummyBlueprint()
    blueprint_group = BlueprintGroup()
    blueprint_group._blueprints = [dummy_blueprint]
    assert blueprint_group[0] == dummy_blueprint
    blueprint_group[0] = dummy_blueprint
    assert blueprint_group[0] == dummy_blueprint

    blueprint_group.append(dummy_blueprint)
    assert len(blueprint_group) == 2

    blueprint_group.insert(0, dummy_blueprint)
    assert len(blueprint_group) == 3

    del blueprint_group[1]
    assert len(blueprint_group) == 2

# Generated at 2022-06-14 07:00:50.681790
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp1 = Blueprint('bp_group_route', url_prefix='/bp1')
    bp2 = Blueprint('bp2_route', url_prefix='/bp2')
    bp_group = BlueprintGroup(url_prefix='/group', version=2)
    bp_group.append(bp1)
    bp_group.append(bp2)
    bp_group[0] = bp2
    bp_group[1] = bp1
    assert bp_group[0].name == 'bp2_route'
    assert bp_group[1].name == 'bp_group_route'


# Generated at 2022-06-14 07:01:01.571491
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    """
    This method is used to test the BlueprintGroup.append method
    """
    app = sanic.Sanic()
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp3)
    bpg.append(bp4)

    assert bp3.strict_slashes is None
    assert bp3.version is None
    assert bp3.url_prefix == "/bp4"

    assert bp4.strict_slashes is None
   

# Generated at 2022-06-14 07:01:06.673181
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp = Blueprint("bp1", __name__)
    bp["user"] = User("John", "Lennon")
    assert bp["user"].first_name == "John" and bp["user"].last_name == "Lennon"


# Generated at 2022-06-14 07:01:19.035169
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    app = sanic.Sanic("test_BlueprintGroup")
    Blueprint = app.blueprint
    BlueprintGroup = Blueprint.group
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bpg = BlueprintGroup(bp1, bp2)

    @bpg.middleware("request")
    async def test_middleware(request):
        assert request

    _, *_, fn = bp1.handlers["request"].middlewares
    assert fn is test_middleware

    _, *_, fn = bp2.handlers["request"].middlewares
    assert fn is test_middleware



# Generated at 2022-06-14 07:01:25.844990
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    # Add blueprints to group
    group = BlueprintGroup(url_prefix='/api', version='v1')
    group.append(Blueprint.group(Blueprint('bp1', url_prefix='/bp1'), Blueprint('bp2', url_prefix='/bp2')))
    group.append(Blueprint.group(Blueprint('bp3', url_prefix='/bp3'), Blueprint('bp4', url_prefix='/bp4')))
    assert len(group) == 2


# Generated at 2022-06-14 07:01:26.895703
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    BlueprintGroup.__delitem__(self=None, index=0)


# Generated at 2022-06-14 07:01:42.479865
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    """
    This test function is testing the `__init__` method
    of the class `BlueprintGroup`
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp1)
    bpg.append(bp2)

    assert len(bpg) == 2
    assert bpg[0] == bp1
    assert bpg[1] == bp2
    # Check for the URL prefix override

# Generated at 2022-06-14 07:01:53.519279
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    group = BlueprintGroup(bp1, bp2)
    assert len(group._blueprints) == 2

    del group[0]

    assert len(group._blueprints) == 1
    assert group._blueprints[0] == bp2

    bpg2 = BlueprintGroup(bp3, bp4)
    assert len(bpg2._blueprints) == 2

    del bpg2[0]

    assert len(bpg2._blueprints) == 1

# Generated at 2022-06-14 07:01:56.763826
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp = Blueprint('bp', url_prefix='/bp')
    bpg = BlueprintGroup(bp)
    bpg[0] = bp
    assert bpg[0] == bp


# Generated at 2022-06-14 07:02:00.021851
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    """
    Unit test for the class `BlueprintGroup`
    """
    BlueprintGroup(
        url_prefix="/api", version="v1", strict_slashes=True
    )  # no Exception raised



# Generated at 2022-06-14 07:02:13.029519
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bg  = BlueprintGroup()
    bg.append(bp1)
    bg.append(bp2)
    bg.insert(0,bp3)
    bg.insert(1,bp4)
    assert bg[0] == bp3 and bg[1] == bp4 and bg[2] == bp1 and bg[3] == bp2
    bg.insert(0,bp4)
    bg.insert(1,bp1)

# Generated at 2022-06-14 07:02:17.601696
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    group = BlueprintGroup()
    group.append(Blueprint)
    group.insert(0, Blueprint)
    group.append(Blueprint)
    assert len(group) == 3


# Generated at 2022-06-14 07:02:23.836665
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bpg = BlueprintGroup()
    bpg.append(bp1)
    assert bpg[0] == bp1
    bpg[0] = bp2
    assert bpg[0] == bp2

# Generated at 2022-06-14 07:02:35.651750
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._blueprints == []
    bpg.append(bp1)
    assert bpg._blueprints == [bp1]
    assert bp1.url_prefix is None
    assert bp1.version == "v1"

# Unit Test for method BlueprintGroup.middleware()

# Generated at 2022-06-14 07:02:41.262397
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup('/api', version='v1', strict_slashes=False)
    group.append(bp1)
    group.append(bp2)


# Generated at 2022-06-14 07:02:49.742157
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    bp2 = Blueprint("bp2", url_prefix="/bp2")
    bp3 = Blueprint("bp3", url_prefix="/bp3")
    bp4 = Blueprint("bp4", url_prefix="/bp4")

    bp = BlueprintGroup(bp1, bp2, bp3, bp4, version="v1")

    @bp.middleware("request")
    # pylint: disable=unused-variable
    async def bp_middleware(request: sanic.request):
        pass

    assert bp1.middlewares["request"][0].__name__ == bp_middleware.__name__
    assert bp2.middlewares["request"][0].__name__ == bp_middleware.__name

# Generated at 2022-06-14 07:03:03.531757
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    blueprint_group = BlueprintGroup()
    blueprint_group.append(Blueprint("bp1"))
    blueprint_group.append(Blueprint("bp2"))
    blueprint_group.append(Blueprint("bp3"))
    blueprint_group.append(Blueprint("bp4"))
    del blueprint_group[0]
    assert "bp1" not in blueprint_group


# Generated at 2022-06-14 07:03:16.225997
# Unit test for method middleware of class BlueprintGroup
def test_BlueprintGroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bpg = BlueprintGroup(url_prefix="api")
    bpg.append(bp1)
    bpg.append(bp2)

    assert bp1.middlewares == []
    assert bp2.middlewares == []

    @bpg.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')

    assert bp1.middlewares == [(bp1_only_middleware, 'request')]
    assert bp2.middlewares == [(bp1_only_middleware, 'request')]


# Generated at 2022-06-14 07:03:20.162010
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    from sanic.blueprints import Blueprint

    BlueprintGroup.append(Blueprint)


if __name__ == "__main__":
    import pytest

    pytest.main(["-x", "tests/test_Blueprint_Group.py"])

# Generated at 2022-06-14 07:03:33.763847
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup('bpg', url_prefix='/bpg')
    bpg.append(bp1)
    bpg.append(bp2)
    bpg.insert(1, bp3)
    bpg.insert(0, bp4)
    assert bpg[0].name == "bp4"
    assert bpg[1].name == "bp1"
    assert bpg[2].name == "bp3"
    assert bpg[3].name == "bp2"

#

# Generated at 2022-06-14 07:03:40.433826
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    url_prefix = "api"
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix=url_prefix)
    bpg.append(bp3)
    bpg.append(bp4)
    assert len(bpg) == 2


# Generated at 2022-06-14 07:03:49.078288
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    bp1 = Blueprint("bp1")
    bp2 = Blueprint("bp2")
    bp3 = Blueprint("bp3")

    bpg = BlueprintGroup()
    bpg.append(bp1)
    bpg.append(bp2)

    assert len(bpg) == 2

    bpg.insert(1, bp3)

    assert len(bpg) == 3
    assert bpg[0] == bp1
    assert bpg[1] == bp3
    assert bpg[2] == bp2



# Generated at 2022-06-14 07:03:55.669609
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    """
    Test case for __getitem__ method of class BlueprintGroup
    """
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup()

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4= Blueprint('bp4', url_prefix='/bp4')

    bpg._blueprints = [bp3, bp4]

    assert bpg[0] == bp3
    assert bpg[1] == bp4

    bpg._blueprints = [bp1, bp2]

    assert bpg[0] == bp1
    assert bpg[1] == bp2



# Generated at 2022-06-14 07:04:06.859901
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp3)
    bpg.append(bp4)
    assert bpg.url_prefix == "/api"
    assert bpg.version == "v1"
    assert type(bpg) == BlueprintGroup
    assert len(bpg) == 2
    assert bpg[0].url_prefix == "/api/bp3"
    assert bpg[0].version == "v1"

# Generated at 2022-06-14 07:04:19.071757
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    bpg.insert(0,bp1)
    bpg.insert(1,bp2)
    assert len(bpg) == 4
    del bpg[1]
    assert len(bpg) == 3
    assert len(bpg._blueprints) == 3
    assert bpg[1] == bp3
    assert bpg[2] == bp4

# Generated at 2022-06-14 07:04:26.413623
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    """
    Testing BlueprintGroup's insert method with correct parameters.
    """
    bp1 = sanic.Blueprint('bp1', url_prefix='/bp1')
    bp2 = sanic.Blueprint('bp2', url_prefix='/bp2')

    group = BlueprintGroup()

    group.append(bp1)
    group.insert(0, bp2)

    assert group[0] == bp2
    assert group[1] == bp1

# Generated at 2022-06-14 07:04:57.190924
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    class App(sanic.Sanic):

        pass

    app = App()

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    class BlueprintGroup(sanic.blueprints.BlueprintGroup):
        pass

    bpg = BlueprintGroup(url_prefix="/api", version="v1")
    bpg.append(bp1)
    print(bpg.blueprints)
    bpg[0] = bp2
    print(bpg.blueprints)

# Generated at 2022-06-14 07:04:58.968791
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    assert list(BlueprintGroup()) == []


# Generated at 2022-06-14 07:05:04.930428
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    blueprint_group = BlueprintGroup()
    blueprint_object = Blueprint('bp', url_prefix='/bp')
    blueprint_group.append(blueprint_object)
    blueprint_group[0] = Blueprint('bp', url_prefix='/bp')
    assert blueprint_group._blueprints[0] == Blueprint('bp', url_prefix='/bp')


# Generated at 2022-06-14 07:05:09.822394
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp_group = BlueprintGroup()
    assert len(bp_group) == 0
    bp_group.append(Blueprint("bp1"))
    bp_group.append(Blueprint("bp2"))
    assert len(bp_group) == 2



# Generated at 2022-06-14 07:05:11.037252
# Unit test for method __delitem__ of class BlueprintGroup
def test_BlueprintGroup___delitem__():
    pass



# Generated at 2022-06-14 07:05:17.285034
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')

    bpg = BlueprintGroup()

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    assert len(bpg) == 3


# Generated at 2022-06-14 07:05:30.630393
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    bp1 = Blueprint("bp1", url_prefix="/bp1", version="v1")
    bp2 = Blueprint("bp2", url_prefix="/bp2", version="v2")
    bp3 = Blueprint("bp3", url_prefix="/bp3", version="v3")
    bp4 = Blueprint("bp4", url_prefix="/bp4", version="v4")

    bpg = BlueprintGroup(url_prefix="/bp", version="v1", strict_slashes=True)

    @bp1.route("/")
    async def route(request):
        return text("v1-bp1")

    @bp2.route("/")
    async def route(request):
        return text("v2-bp2")


# Generated at 2022-06-14 07:05:39.303274
# Unit test for constructor of class BlueprintGroup
def test_BlueprintGroup():
    bp1 = Blueprint("bp1", url_prefix="/bp1", version=1)
    bp2 = Blueprint("bp2", url_prefix="/bp2", version=2)

    bpg = BlueprintGroup(url_prefix="/api", version=3)
    bpg.append(bp1)
    bpg.append(bp2)

    assert len(bpg) == 2
    assert bp1.url_prefix == "/api/bp1"
    assert bp2.url_prefix == "/api/bp2"
    assert bp1.version == 3
    assert bp2.version == 3



# Generated at 2022-06-14 07:05:45.317431
# Unit test for method __getitem__ of class BlueprintGroup
def test_BlueprintGroup___getitem__():
    bp1 = Blueprint('test_bp1', url_prefix='/bp1')
    bp2 = Blueprint('test_bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    assert bpg[0] == bp1
    assert bpg[1] == bp2


# Generated at 2022-06-14 07:05:48.634811
# Unit test for method append of class BlueprintGroup
def test_BlueprintGroup_append():
    group = BlueprintGroup()
    assert len(group) == 0
    group.append(Blueprint("testbp"))
    assert len(group) == 1


# Generated at 2022-06-14 07:06:41.312401
# Unit test for method insert of class BlueprintGroup
def test_BlueprintGroup_insert():
    URL_PREFIX = '/api'
    VERSION = 'v1'
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bp5 = Blueprint('bp5', url_prefix='/bp5')
    bp6 = Blueprint('bp6', url_prefix='/bp6')
    bp7 = Blueprint('bp7', url_prefix='/bp7')
    bp8 = Blueprint('bp8', url_prefix='/bp8')
    bp9 = Blueprint('bp9', url_prefix='/bp9')

# Generated at 2022-06-14 07:06:55.076938
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp4')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(url_prefix="/api", version="v1")


    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)
    bpg.append(bp4)

    # Test 1
    """assert bp1 in bpg, \
        'Unit test Failed. Should be able to append blueprint to blueprint group'"""
    # Test 2

# Generated at 2022-06-14 07:07:02.984769
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(url_prefix="/api", version="v1")

    bpg.append(bp1)
    bpg.append(bp2)
    bpg.append(bp3)

    assert bpg[2] == bp3
    assert len(bpg) == 3

    bpg[2] = bp4
    assert bpg[2] == bp4


# Generated at 2022-06-14 07:07:12.227469
# Unit test for method __setitem__ of class BlueprintGroup
def test_BlueprintGroup___setitem__():
    bp_group = BlueprintGroup()
    blueprint_list = []
    for i in range(10):
        blueprint_list.append(Blueprint(url_prefix=f'/bp{i}'))
    bp_group.__setitem__(slice(0, 5), blueprint_list[0:5])
    assert len(bp_group.blueprints) == 5

    bp_group[slice(0, 10)] = blueprint_list
    assert len(bp_group.blueprints) == 10



# Generated at 2022-06-14 07:07:16.241839
# Unit test for method __len__ of class BlueprintGroup
def test_BlueprintGroup___len__():
    bpg = BlueprintGroup()
    bpg.append(sanic.Blueprint("bp1"))
    bpg.append(sanic.Blueprint("bp2"))
    bpg.append(sanic.Blueprint("bp3"))

    assert len(bpg) == 3


# Generated at 2022-06-14 07:07:29.596089
# Unit test for method __iter__ of class BlueprintGroup
def test_BlueprintGroup___iter__():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')

    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')

    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
