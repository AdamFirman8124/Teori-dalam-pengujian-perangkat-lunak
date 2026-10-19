

# Generated at 2022-06-13 08:52:23.062385
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # First check the function with parameters
    meta = RoleMetadata.load({"allow_duplicates": True, "dependencies": []}, None)
    assert meta.allow_duplicates
    assert meta.dependencies == []
    # Now check the function with missing parameters
    meta = RoleMetadata.load({}, None)
    assert not meta.allow_duplicates
    assert meta.dependencies == []

# Generated at 2022-06-13 08:52:34.942313
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    collection_search_list=['my.collection1', 'my.collection2']
    r1 = RoleMetadata(owner=None)
    assert r1 == {}
    assert r1._allow_duplicates == False
    assert r1._dependencies == []
    assert r1._galaxy_info == {}
    assert r1._argument_specs == {}
    assert r1._owner == None
    r2 = RoleMetadata(owner=None)
    assert r2 == {}
    assert r2._allow_duplicates == False
    assert r2._dependencies == []
    assert r2._galaxy_info == {}
    assert r2._argument_specs == {}
    assert r2._owner == None
    r3 = RoleMetadata(owner=None)
    assert r3 == {}
    assert r3._allow_

# Generated at 2022-06-13 08:52:42.464992
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Constructor of class RoleMetadata should fill in the fields:
    # self._allow_duplicates = True
    # self._dependencies = [RoleRequirement()]
    # self._galaxy_info = GalaxyInfo()
    # self._argument_specs = dict()
    meta = RoleMetadata()
    assert meta._allow_duplicates == False
    assert meta._dependencies == []
    assert meta._galaxy_info == None
    assert meta._argument_specs == dict()

# Generated at 2022-06-13 08:52:47.721752
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """Run tests on RoleMetadata.deserialize (method)
    """
    test_data = dict(
        allow_duplicates=False,
        dependencies=[],
    )
    rm = RoleMetadata()
    rm.deserialize(test_data)
    assert rm.allow_duplicates == test_data.get('allow_duplicates', False)
    assert rm.dependencies == test_data.get('dependencies', [])

# Generated at 2022-06-13 08:52:50.943433
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {
        'allow_duplicates': False,
        'dependencies': []
    }
    role_meta = RoleMetadata()
    role_meta.deserialize(data)
    assert role_meta.allow_duplicates == False
    assert role_meta.dependencies == []

# Generated at 2022-06-13 08:52:51.561981
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:52:58.981149
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    owner = None
    variable_manager = None
    loader = None
    data = dict(
        allow_duplicates='True',
        dependencies='dependencies'
    )
    valid_m = RoleMetadata.load(data, owner, variable_manager, loader)
    assert valid_m._allow_duplicates == True
    assert valid_m._dependencies == 'dependencies'
    assert valid_m._owner == None
    assert valid_m._galaxy_info == {}
    assert valid_m._argument_specs == {}

# Generated at 2022-06-13 08:53:05.184819
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = dict(
        allow_duplicates=True,
        dependencies={'name': 'myrole', 'version': '1.0', 'scm': 'git', 'src': 'url'}
    )
    role = RoleMetadata()
    role.deserialize(data)
    assert (role._allow_duplicates is True)
    assert (role._dependencies == [{'name': 'myrole', 'version': '1.0', 'scm': 'git', 'src': 'url'}])

# Generated at 2022-06-13 08:53:06.126951
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    assert True


# Generated at 2022-06-13 08:53:09.846985
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    meta = RoleMetadata()
    meta.allow_duplicates = True
    meta.dependencies = ['role1', 'role2']
    assert meta.serialize() == dict(
        allow_duplicates=True,
        dependencies=['role1', 'role2']
    )


# Generated at 2022-06-13 08:53:19.384348
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner = Base()
    m = RoleMetadata(owner=owner)
    dependencies = [1, 2, 3]
    m.dependencies = dependencies
    data = m.serialize()
    assert data['allow_duplicates'] == False
    assert data['dependencies'] == dependencies


# Generated at 2022-06-13 08:53:24.518700
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    '''
    unit test for serialize() of class RoleMetadata
    '''
    obj= RoleMetadata()
    serialized_data = {
        'allow_duplicates': False,
        'dependencies': []
    }
    assert obj.serialize() == serialized_data

# Generated at 2022-06-13 08:53:32.823452
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    role_definition = RoleDefinition()
    role_definition._role_name = 'test_role'
    role_definition._role_path = 'test_role_path'
    role_definition.collections.append('test_collection')
    role_definition.collections.append('test_collection')
    role_metadata = RoleMetadata(role_definition)
    assert role_metadata.serialize() == {'allow_duplicates': False, 'dependencies': []}

# Generated at 2022-06-13 08:53:40.390549
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    Test Ansible RoleMetadata serialize function
    """
    r_meta = dict()
    assert RoleMetadata.serialize(r_meta) == dict(allow_duplicates=False, dependencies=[])

    r_meta = dict(allow_duplicates=None, dependencies=None)
    assert RoleMetadata.serialize(r_meta) == dict(allow_duplicates=False, dependencies=[])

    r_meta = dict(allow_duplicates='None', dependencies='foo')
    assert RoleMetadata.serialize(r_meta) == dict(allow_duplicates=False, dependencies=[])

    r_meta = dict(allow_duplicates=False, dependencies='foo')
    assert RoleMetadata.serialize(r_meta) == dict(allow_duplicates=False, dependencies=[])

    r

# Generated at 2022-06-13 08:53:49.773158
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role

    RoleMetadata()

    my_play = Play.load(dict(name='my_play'), loader=None, variable_manager=None)
    play_context = PlayContext()
    my_play._play_context = play_context

    my_role = Role.load(dict(name='my_role'), play=my_play, loader=None, variable_manager=None, use_deprecated_implicit_ipv4=False)

    RoleMetadata(owner=my_role)

    my_role_include = RoleInclude()


# Generated at 2022-06-13 08:53:52.570416
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    rolemeta = RoleMetadata()
    assert rolemeta.allow_duplicates == False
    assert rolemeta.dependencies == []

# Generated at 2022-06-13 08:53:58.745546
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition

    role_metadata = RoleMetadata(RoleDefinition())
    role_metadata._allow_duplicates = False
    role_metadata._dependencies = [{'role': "role1"}, {'role': "role2", 'name': "name2"}]

    serialized = role_metadata.serialize()
    assert serialized is not None
    assert isinstance(serialized, dict)
    assert serialized['allow_duplicates'] is False
    assert serialized['dependencies'] is role_metadata._dependencies


# Generated at 2022-06-13 08:54:07.372903
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.role.requirement import RoleRequirement
    import yaml
    yaml_data = dict(
        allow_duplicates=False,
        dependencies=[
            dict(
                role=None,
                src=None,
                name='galaxy.ansible.com,geerlingguy.nginx,1.0.0'
            ),
            'ansible-role-mariadb'
        ]
    )
    data = yaml.dump(yaml_data, default_flow_style=False)
    role_definition = RoleDefinition.load(data=data)
    m = role_definition.metadata
    assert m._allow_duplicates is False
   

# Generated at 2022-06-13 08:54:18.310574
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    class MyRoleMetadata(RoleMetadata):
        _galaxy_info = FieldAttribute(isa='GalaxyInfo')

    class MyGalaxyInfo: pass

    class MyRoleRequirement:
        role_yaml_parse = lambda x: {'name': 'galaxy.role', 'version': '1.0'}
        def __init__(self, data):
            pass

    class MyRole:
        def get_name(self):
            return 'unittest_role'

        _role_path = '/tmp/myrole'

        _play = None

        collections = []

        _role_collection = None

        @property
        def role_key(self):
            return 'unittest_role_key'


# Generated at 2022-06-13 08:54:27.803511
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    class RoleInclude:
        def __init__(self, role):
            self.role = role
    data = {
        'dependencies': [
            {
                'role': 'mgeide.foo-role',
                'version': '1.0.0',
                'name': 'roles_name',
                'collections': [],
            },
            {
                'src': 'mgeide.foo-role==1.0.0',
                'name': 'roles_name',
            },
            'test_role',
            RoleInclude('roles_name')]
    }
    role_metadata = RoleMetadata.load(data, None)
    assert len(role_metadata._dependencies) == 4
    assert role_metadata._dependencies[0].role == 'roles_name'

# Generated at 2022-06-13 08:54:49.226547
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.parsing.dataloader import DataLoader
    _loader = DataLoader()
    _variable_manager = None

    _data = {
        'dependencies': [
            {
               'role': 'test_role',
               'when': 'test_when',
               'tags': [
                   'test_tag1',
                   'test_tag2'
               ]
            },
            'test_role_2'
        ],
    }

    _role = RoleMetadata(_loader, _variable_manager)
    _role.deserialize(_data)
    assert _role.dependencies == _data['dependencies']
    assert _role._allow_duplicates == False

# Generated at 2022-06-13 08:54:57.506447
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.play import Play

    rd = RoleDefinition()
    rd.name = "foo"
    rd._role_path = "/foo/bar"
    pl = Play()
    rd._play = pl
    rm = RoleMetadata(owner=rd)
    rm._owner = rd
    rm.load({'dependencies': [{'role': 'common'}]}, owner=rd)
    assert isinstance(rm._dependencies[0], RoleRequirement)
    assert rm._dependencies[0].name == 'common'

# Generated at 2022-06-13 08:55:01.201730
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    assert RoleMetadata.load({"dependencies":["./roledef1", {"role":"roledef2"}]}, RoleDefinition("rolepath")) is not None

# Generated at 2022-06-13 08:55:02.694829
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata(owner=None)
    assert m

# Generated at 2022-06-13 08:55:06.632285
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r = RoleMetadata('data', 'allow_duplicates', 'dependencies')
    #data = r.deserialize()
    assert r.deserialize() == {'allow_duplicates': 'allow_duplicates', 'dependencies': 'dependencies'}

# Generated at 2022-06-13 08:55:15.416314
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    import yaml
    from ansible.playbook.role import Role
    ds = """
    ---
    dependencies:
      - {role: 'galaxy.role', version: 'v1.0'}
      - {role: 'galaxy.role2', version: 'v1.2', name: 'other_name'}
    allow_duplicates: true
    """
    role = Role()
    r = RoleMetadata(owner=role)
    r.load_data(yaml.safe_load(ds), None, None)
    assert r.allow_duplicates is True
    assert len(r.dependencies) == 2

# Generated at 2022-06-13 08:55:22.833038
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():

    """
    Unit test to verify that RoleMetadata class
    can deserialize information loaded from
    a file
    """
    class FakeRole(object):

        def __init__(self):
            self._role_path = None
            self._name = None
            self._play = None
            self._role_collection = None

    metadata = RoleMetadata(owner=FakeRole())
    assert metadata.deserialize({"allow_duplicates": True, "dependencies": []}) is None

# Generated at 2022-06-13 08:55:23.763823
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    role_metadata = RoleMetadata()
    assert role_metadata._allow_duplicates is False
    assert role_metadata._dependencies == []

# Generated at 2022-06-13 08:55:31.516321
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    class FakeRole(object):
        def __init__(self):
            self._role_name = 'fake_role_name'
            self._role_path = 'fake_role_path'

    class FakeVarMgr(object):
        def get_vars(self, loader=None, play=None, host=None, task=None, include_hostvars=True):
            return dict()

    class FakeLoader(object):
        def _search_paths(self, relative_paths=None, collection_list=None, include_role_paths=True):
            return ['role_search_path']


# Generated at 2022-06-13 08:55:32.458492
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    pass

# Generated at 2022-06-13 08:55:57.248461
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    setattr(m,'allow_duplicates', True)
    setattr(m,'dependencies', ['foo-role', 'bar-role'])
    assert m.serialize() == {
        'allow_duplicates': True,
        'dependencies': ['foo-role', 'bar-role']
    }


# Generated at 2022-06-13 08:56:07.489458
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    Basic sanity test to check if class RoleMetadata can be instantiated
    with valid input data and if it serializes back correctly
    '''

    # Case 1
    # Valid input data
    data = dict(
        allow_duplicates=False,
        dependencies=['geerlingguy.java']
    )
    role = dict(
        name='test_role'
    )

    metadata = RoleMetadata.load(data, role)

    assert metadata.serialize() == data



# Generated at 2022-06-13 08:56:12.880764
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rmeta = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies = ['b','a']
    )
    rmeta.deserialize(data)

    assert rmeta.allow_duplicates == True
    assert rmeta.dependencies == ['b','a']

# Generated at 2022-06-13 08:56:20.513486
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rmd = RoleMetadata()
    rmd._allow_duplicates = True
    rmd._dependencies = ['a', 'b']
    rmd._galaxy_info = {'a': 'b'}
    rmd._argument_specs= {'c': ['d']}
    rmd_serialize = rmd.serialize()
    assert len(rmd_serialize.keys()) == 2
    assert rmd_serialize.get('allow_duplicates') is True
    assert rmd_serialize.get('dependencies') == ['a', 'b']
    assert rmd_serialize.get('galaxy_info') is None
    assert rmd_serialize.get('argument_specs') is None


# Generated at 2022-06-13 08:56:26.821227
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    # setup for the test:
    # create the calling object (play) with the appropriate fields and methods
    def get_name():
        return 'test-play'
    test_play = Play()
    test_play.get_name = get_name
    test_play._variable_manager = None

    # create the role to be called
    # role metadata should throw an error if this is not in dictionary form
    test_role_data_dict = {'allow_duplicates': True,
                           'dependencies': ['test-dependency', 'test-dependency2']}

# Generated at 2022-06-13 08:56:35.958335
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    a = RoleMetadata()
    a.deserialize(dict(allow_duplicates=False, dependencies=[dict(role="dep1", skip_tags=["a","b"]), dict(role="dep2",), dict(role="dep3")]))
    assert a._allow_duplicates == False
    assert len(a._dependencies) == 3
    assert a._dependencies[0].role == "dep1"
    assert a._dependencies[0].conditional is None
    assert a._dependencies[0].restrict_to_hosts is None
    assert a._dependencies[0].restrict_to_environments is None
    assert a._dependencies[0].tags == ["a","b"]
    assert a._dependencies[1].role == "dep2"

# Generated at 2022-06-13 08:56:46.127024
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    ds = {
        'allow_duplicates': False,
        'dependencies': [{'role': 'common', 'name': 'common'}]
    }

    try:
        r = RoleMetadata(owner=None).load(ds, owner=None)
    except AnsibleParserError as e:
        # expected to fail, as owner is required
        pass
    else:
        raise Exception("Expected ParserError to be raised")

    # real minimal test
    play = Play().load({}, variable_manager=None, loader=None)
    context = PlayContext()
    context._play = play
    play._context = context

# Generated at 2022-06-13 08:56:52.853104
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    test = RoleMetadata(owner=None)
    setattr(test, 'allow_duplicates', True)
    setattr(test, 'dependencies', [])
    assert test.serialize() == {'allow_duplicates': True, 'dependencies': []}


# Generated at 2022-06-13 08:57:08.499943
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import ansible.playbook.role.role
    import ansible.playbook.play
    import ansible.playbook.playbook

    import ansible.module_utils.ansible_release
    ansible.module_utils.ansible_release.__version__ = '2.9.0'
    import ansible.module_utils.ansible_galaxy
    ansible.module_utils.ansible_galaxy.API = None

    import ansible.vars.manager
    from ansible.template import Templar

    import ansible.parsing.dataloader

    import ansible.inventory.manager
    import ansible.inventory.host
    import ansible.inventory.group
    import ansible.inventory.inventory

    import ansible.utils.display


# Generated at 2022-06-13 08:57:17.214210
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    # given
    role_metadata = RoleMetadata(owner=None)
    role_metadata._allow_duplicates = True
    role_metadata._dependencies = [1, 2]

    # when
    result = role_metadata.serialize()

    # then
    print("result:", result)
    assert result == {'allow_duplicates': True, 'dependencies': [1, 2]}



# Generated at 2022-06-13 08:57:50.632610
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    rolemetadata = RoleMetadata(owner=None)
    rolemetadata.deserialize({ "dependencies": [], "allow_duplicates": False})
    print(rolemetadata.dependencies)
    assert rolemetadata.allow_duplicates == False
    #assert rolemetadata.dependencies == []

# Generated at 2022-06-13 08:57:53.786696
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    meta = RoleMetadata.load(dict(
        allow_duplicates=True,
        dependencies=['foo', 'bar'],
    ), None, None, None)
    assert meta.serialize() == dict(
        allow_duplicates=True,
        dependencies=['foo', 'bar'],
    )

# Generated at 2022-06-13 08:57:59.626254
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    m._allow_duplicates = True
    m._dependencies = [{'role': 'common'}]
    data = m.serialize()
    assert isinstance(data, dict)
    assert data == {
        'allow_duplicates': True,
        'dependencies': [{'role': 'common'}]
    }


# Generated at 2022-06-13 08:58:03.633583
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = {'allow_duplicates': True, 'dependencies': []}
    role_metadata = RoleMetadata(owner=None)
    role_metadata.deserialize(metadata)
    assert role_metadata.allow_duplicates is True
    assert role_metadata.dependencies == []


# Generated at 2022-06-13 08:58:05.072807
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Test constructor
    role = RoleMetadata()
    assert role.dependencies == []

# Generated at 2022-06-13 08:58:06.797121
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    ro = RoleMetadata()
    ser = ro.serialize()
    assert ser == dict(allow_duplicates=False, dependencies=[])

# Generated at 2022-06-13 08:58:14.039859
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    def test():
        rd = RoleDefinition.load(dict(role='test_role'), owner=None)
        rm = RoleMetadata(rd)
        serialized = rm.serialize()

        rm2 = RoleMetadata(rd)
        rm2.deserialize(serialized)
        serialized2 = rm2.serialize()
        assert serialized == serialized2
    test()

    def test2():
        rd = RoleDefinition.load(dict(role='test_role'), owner=None)
        rm = RoleMetadata(rd)
        rm._dependencies = [rd, rd]

        serialized = rm.serialize()
        rm2 = RoleMetadata(rd)
        rm

# Generated at 2022-06-13 08:58:24.966314
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager

    yaml_text = '''
    name: mysql
    description: MySQL database server as role
    galaxy_info:
      author: me
      company: company
      min_ansible_version: 2.8
    allow_duplicates: True
    dependencies:
    - foo
    - bar
    '''
    yaml_ds = {'name': 'mysql', 'description': 'MySQL database server as role', 'galaxy_info': {'author': 'me', 'company': 'company', 'min_ansible_version': '2.8'}, 'allow_duplicates': True, 'dependencies': ['foo', 'bar']}

    role_defs = RoleDefinition(yaml_text)
   

# Generated at 2022-06-13 08:58:30.337259
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.meta import RoleMetadata
    data = {
            'allow_duplicates': True,
            'dependencies': ['name', 'name2']
    }
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    assert role_metadata.serialize()['allow_duplicates'] == data['allow_duplicates']
    assert role_metadata.serialize()['dependencies'] == data['dependencies']

# Generated at 2022-06-13 08:58:45.707953
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import get_loader

    play = Play()
    play._variable_manager = play.get_variable_manager()
    play._loader = play.get_loader()
    play._loader.set_basedir('.')
    play._context = PlayContext(play=play._play, options=play._options, passwords=dict())
    play._connection = None
    play._task_vars = dict()
    play._included_file_vars = dict()

    playbook = Playbook()
    playbook._loader = play._loader
    playbook._variable_manager

# Generated at 2022-06-13 08:59:56.817569
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    import os
    import sys
    import copy
    import ansible.playbook.role.meta
    from ansible.utils.display import Display
    import ansible.constants as C

    display = Display()
    display.verbosity = 3

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase


# Generated at 2022-06-13 08:59:58.344399
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    d = RoleMetadata(owner = None)
    assert d._owner is None

# Generated at 2022-06-13 09:00:06.846474
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.definition import RoleDefinition

    class Play(Play):
        pass

    class PlayContext(PlayContext):
        pass

    class Task(Task):
        pass

    class Block(Block):
        pass

    class Handler(Handler):
        pass

    class RoleDefinition(RoleDefinition):
        pass

    class RoleRequirement(object):
        def __init__(self, role_args):
            pass

    class RoleMetadata(object):
        def __init__(self, role_args):
            pass


# Generated at 2022-06-13 09:00:14.153915
# Unit test for method load of class RoleMetadata

# Generated at 2022-06-13 09:00:21.999687
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    role_metadata = RoleMetadata()
    assert role_metadata is not None

    try:
        assert False == role_metadata.allow_duplicates
    except AssertionError as e:
        print("AssertionError: ", e)
        return 1

    try:
        assert [] == role_metadata.dependencies
    except AssertionError as e:
        print("AssertionError: ", e)
        return 1

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(test_RoleMetadata())

# Generated at 2022-06-13 09:00:27.396928
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():

    # Test case 1: Empty dictionary
    try:
        RoleMetadata.load({}, None)
    except AnsibleParserError as e:
        assert e.message.startswith(
            'the \'main.yml\' for role is not a dictionary')

    # Test case 2: RoleMetadata object loaded with empty dict
    role_metadata = RoleMetadata.load({}, None)
    assert list(role_metadata.__dict__.keys()) == ['_dependencies', '_galaxy_info', '_owner', '_argument_specs']

# Generated at 2022-06-13 09:00:32.926697
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    """
    This test case checks that serialize method of class RoleMetadata works as expected
    """
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.module_utils.six import PY2
    import sys
    import tempfile
    import os
    import json

    # Create temporary file as play book
    if PY2:
        play_book_fh, play_book_name = tempfile.mkstemp(prefix='ansible-test-playbook')
    else:
        play_book_fh, play_book_name = tempfile.mkstemp(prefix='ansible-test-playbook', text=True)
    play_book_fh = os.fdopen(play_book_fh, "w")
    play_book_fh

# Generated at 2022-06-13 09:00:37.241085
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    data = dict()
    data['allow_duplicates'] = True
    data['dependencies'] = ['a.b.c','d.e.f']
    metadata.deserialize(data)
    assert metadata._allow_duplicates == True
    assert metadata._dependencies == ['a.b.c','d.e.f']


# Generated at 2022-06-13 09:00:43.187610
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    data = {}
    variable_manager = MockVariableManager()
    loader = MockLoader()
    owner = Mock()
    owner.get_name = lambda: "foo"
    result = RoleMetadata.load(data, owner, variable_manager, loader)

    assert isinstance(result, RoleMetadata)
    assert result._variable_manager is variable_manager
    assert result._loader is loader
    assert result._owner is owner
    assert result._dependencies == []
    assert result._allow_duplicates is False


# Generated at 2022-06-13 09:00:48.901605
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.play_context import PlayContext

    data = {'dependencies': [{'role': 'common'}], 'allow_duplicates': False}
    role = RoleMetadata.load(data=data, owner=None)
    assert role._dependencies[0]._role == 'common'
    assert role._allow_duplicates == False
