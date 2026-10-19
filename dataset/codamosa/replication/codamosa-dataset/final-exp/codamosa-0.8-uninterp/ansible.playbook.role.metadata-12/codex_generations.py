

# Generated at 2022-06-13 08:52:20.645399
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    metadata = RoleMetadata()
    deserialize_data = {'allow_duplicates': False, 'dependencies': []}
    metadata.deserialize(deserialize_data)

    assert metadata.allow_duplicates is False
    assert metadata.dependencies == []

# Generated at 2022-06-13 08:52:28.263828
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader

    ROLE_METADATA_YAML = """
        allow_duplicates: False
        dependencies:
          - role: galaxy.role
            version: 1.0
            collections:
              - geerlingguy.apache
          - role: logrotate
            meta:
              allow_duplicates: False
              dependencies:
                - role: geerlingguy.drupal
    """
    ROLE_METADATA_DS = AnsibleMapping(ROLE_METADATA_YAML)

    role_def = RoleDefinition.load

# Generated at 2022-06-13 08:52:38.079626
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    loader = DataLoader()

    play_source =  dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

    play = Play.load(play_source, variable_manager=None, loader=loader)

    play_context = Play

# Generated at 2022-06-13 08:52:39.233558
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    print(RoleMetadata())

# Generated at 2022-06-13 08:52:46.524917
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vault import VaultLib

    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_vars
    from ansible.vars import combine_vars

    # mock class import
    import ansible.playbook.role.definition
    import ansible.playbook.role.include
    import ansible.plugins.loader

    class PluginLoader:
        @staticmethod
        def _load_plugins(plugin_type):
            return None

    # class to mock the RoleDefinition class
    class RoleDefinition:
        def __init__(self, *args, **kwargs):
            import ansible.play

# Generated at 2022-06-13 08:52:53.607066
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    m = RoleMetadata()
    test_data = { 
        'allow_duplicates': False,
        'dependencies': [
            { 'role': 'test.role' },
            { 'src': 'test.role', 'version': '1.0' },
        ]
    }
    m.deserialize(test_data)
    assert m.allow_duplicates == False
    assert m.dependencies == [
            { 'role': 'test.role' },
            { 'src': 'test.role', 'version': '1.0' },
        ]

# Generated at 2022-06-13 08:53:00.843335
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    """
    deserialize() should return a dict with allow_duplicates and dependencies
    """
    role_metadata = RoleMetadata()
    role_metadata._ds = dict(
        allow_duplicates = True,
        dependencies = ['dependency1', 'dependency2', 'dependency3']
    )

    assert role_metadata.deserialize() == dict(
        allow_duplicates = True,
        dependencies = ['dependency1', 'dependency2', 'dependency3']
    )


# Generated at 2022-06-13 08:53:04.046992
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    data = {
        'allow_duplicates':True,
        'dependencies':['webserver']
    }
    metadata = RoleMetadata()
    metadata.deserialize(data=data)
    assert metadata.serialize() == data

# Generated at 2022-06-13 08:53:11.112194
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    r = RoleMetadata()
    serialized = r.serialize()
    assert serialized['allow_duplicates'] == False
    assert serialized['dependencies'] == []

    r = RoleMetadata(allow_duplicates=True)
    serialized = r.serialize()
    assert serialized['allow_duplicates'] == True
    assert serialized['dependencies'] == []

    r = RoleMetadata(dependencies=['foo.bar'])
    serialized = r.serialize()
    assert serialized['allow_duplicates'] == False
    assert serialized['dependencies'] == ['foo.bar']

# Generated at 2022-06-13 08:53:11.705387
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    pass

# Generated at 2022-06-13 08:53:24.708993
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    rm = RoleMetadata(owner=None)
    setattr(rm, 'allow_duplicates', True)
    dependencies = [{'role': 'collections.example.role', 'name': 'example'}]
    setattr(rm, 'dependencies', dependencies)
    assert rm.serialize() == {'allow_duplicates': True, 'dependencies': dependencies}

# Generated at 2022-06-13 08:53:26.099376
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    roleMetadata = RoleMetadata()
    assert roleMetadata

# Generated at 2022-06-13 08:53:26.584016
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    pass

# Generated at 2022-06-13 08:53:30.735715
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {"allow_duplicates": False, "dependencies": []}
    r = RoleMetadata()
    r.deserialize(data)
    assert r.allow_duplicates == False
    assert r.dependencies == []


# Generated at 2022-06-13 08:53:33.583554
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = { 'dependencies' : ['a','b','c','d'] }
    r = RoleMetadata(owner = None)
    r.deserialize(data)
    assert r.dependencies == ['a', 'b', 'c', 'd']

# Generated at 2022-06-13 08:53:40.920324
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data1 = {
        'allow_duplicates': True,
        'dependencies': [
            'role1',
            {'role':'role2', 'tags':['tag1', 'tag2']},
            {'role': 'role3', 'name': 'name3', 'version': '0.11.0'}
        ]
    }
    roledf = RoleMetadata(owner=None).deserialize(data1)
    assert len(roledf['dependencies']) == 3
    assert roledf['allow_duplicates'] == True
    assert roledf['dependencies'][0]['role'] == 'role1'
    assert roledf['dependencies'][1]['role'] == 'role2'
    assert roledf['dependencies'][2]['role'] == 'role3'

# Generated at 2022-06-13 08:53:49.924849
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    import ansible.playbook.role.definition
    import ansible.playbook.role.include
    m = RoleMetadata()
    m.deserialize({ 'allow_duplicates': True,
                    'dependencies': [
                        ansible.playbook.role.definition.RoleDefinition(role_name='foo'),
                        ansible.playbook.role.include.RoleInclude(role_name='bar', role_path=None, task_includes=None, role_args=None, task_args=None, implicit=None, parent_role=None)
                    ]
                  })
    assert m._allow_duplicates == True
    assert len(m._dependencies) == 2
    assert isinstance(m._dependencies[0], ansible.playbook.role.definition.RoleDefinition)

# Generated at 2022-06-13 08:53:52.363418
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    # Constructor of class RoleMetadata
    role_metadata = RoleMetadata()
    assert role_metadata is not None

# Generated at 2022-06-13 08:53:58.607468
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata()
    m.allow_duplicates = True
    m.dependencies = [{'role': 'example.foo', 'name': 'foo'}, {'role': 'example.bar', 'name': 'bar'}]
    data = m.serialize()
    assert data['allow_duplicates'] == True
    assert data['dependencies'] == [{'role': 'example.foo', 'name': 'foo'}, {'role': 'example.bar', 'name': 'bar'}]

# Generated at 2022-06-13 08:54:07.259078
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.module_utils import basic
    from ansible.template import Templar

    loader, inventory, variable_manager = basic.load_freeparam_vars()
    variables = variable_manager.get_vars(loader=loader, play=None)
    templar = Templar(loader=loader, variables=variables)


# Generated at 2022-06-13 08:54:20.232861
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata.load({}, None) is not None

# Generated at 2022-06-13 08:54:25.921725
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role

    role_name = "ansible.mock.role"
    role_path = "/does/not/exist/ansible.mock.role"

    # class and function
    data = dict(
        galaxy_info=dict(
            author="MockAuthor1",
            company="MockCompany1",
        ),
        dependencies=[
            dict(role="MockRole1"),
            dict(role="MockRole2", foo="bar"),
        ]
    )
    role = Role.load(role_name, role_path)
    role.metadata = RoleMetadata.load(data, role)

    assert(role.metadata._dependencies[0].role == "MockRole1")
    assert(role.metadata._dependencies[1].role == "MockRole2")


# Generated at 2022-06-13 08:54:27.726839
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r = RoleMetadata()
    assert r.serialize() == {
        'allow_duplicates': False,
        'dependencies': []
    }

# Generated at 2022-06-13 08:54:32.439092
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
	test_data = dict(
		allow_duplicates=False,
		dependencies=['test']
	)
	role_meta = RoleMetadata()
	role_meta.deserialize(test_data)
	assert role_meta._dependencies == ['test']
	assert role_meta._allow_duplicates == False

# Generated at 2022-06-13 08:54:38.867787
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role.definition import RoleDefinition

    loader = DataLoader()

    # This is a subset of the data from meta/main.yml from the Ansible
    # role "Ansible-Examples"

# Generated at 2022-06-13 08:54:49.920718
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    # load_data() is not called, so _dependencies and _galaxy_info will be None
    m = RoleMetadata()
    m.load({}, RoleDefinition('foo'))
    assert m.dependencies is None
    assert m.galaxy_info is None

    # TODO: this is probably broken, as dependecies is a FieldAttribute and should be set
    # by _load_dependencies()
    m = RoleMetadata()
    m.load({'dependencies': ''}, RoleDefinition('foo'))
    assert m.dependencies is None
    assert m.galaxy_info is None

    m = RoleMetadata()

# Generated at 2022-06-13 08:54:50.762331
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    r = RoleMetadata()
    assert(r)

# Generated at 2022-06-13 08:54:55.422901
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'allow_duplicates': False, 'dependencies': []}
    rm = RoleMetadata()
    rm.deserialize(data)
    assert rm.allow_duplicates == False
    assert rm.dependencies == []


# Generated at 2022-06-13 08:55:01.983422
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    owner = object()
    m = RoleMetadata(owner)
    data = {'allow_duplicates': True, 'dependencies': [{'role': 'foobar', 'bar': 'baz'}]}

    m.deserialize(data)
    assert m._allow_duplicates is True
    assert m._dependencies[0]['role'] == 'foobar'
    assert m._dependencies[0]['bar'] == 'baz'

# Generated at 2022-06-13 08:55:04.765647
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    test_data = dict(
        allow_duplicates=True,
        dependencies=[]
    )
    RoleMetadata().load(test_data, None, None, None)

# Generated at 2022-06-13 08:55:18.701695
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.vars.manager import VariableManager

    try:
        with open('fixtures/metadata/meta_main.yml') as metadata_file:
            data = yaml.safe_load(metadata_file)

        variable_manager = VariableManager()
        role_metadata = RoleMetadata.load(
            data=data,
            owner=None,
            variable_manager=variable_manager,
            loader=None
        )

        assert len(role_metadata.dependencies) == 0
        assert role_metadata._galaxy_info == "galaxy_info"
        assert len(role_metadata.argument_specs) == 0

    except Exception as err:
        print(err)
        raise

# Generated at 2022-06-13 08:55:25.039026
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    m = RoleMetadata(owner=None)
    result = m.serialize()
    assert result == {'allow_duplicates': False, 'dependencies': []}
    m._allow_duplicates = True
    result = m.serialize()
    assert result == {'allow_duplicates': True, 'dependencies': []}


# Generated at 2022-06-13 08:55:32.080430
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    '''
    Unit test for method load() of class RoleMetadata
    '''

    import sys
    import unittest
    from . import TestCaseDiscovery
    from ansible.compat.tests import unittest
    from ansible.config.manager import ConfigManager
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:55:40.831923
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    m = RoleMetadata()
    assert m.allow_duplicates == False
    assert m.dependencies == []
    assert m._argument_specs == {}

    m = RoleMetadata(owner=None)
    assert m.allow_duplicates == False
    assert m.dependencies == []
    assert m._argument_specs == {}

    _data = {
        'allow_duplicates': True,
        'dependencies': [
            'role1',
            'role2'
        ]
    }

    m = RoleMetadata().load(_data, owner=None)
    assert m.allow_duplicates == True
    assert m.dependencies == ['role1', 'role2']
    assert m._argument_specs == {}


# Generated at 2022-06-13 08:55:43.100233
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    ds = {
        'allow_duplicates': True,
        'dependencies': ['foo', 'bar']
    }
    m = RoleMetadata.load(ds, None)
    assert m.serialize() == ds

# Generated at 2022-06-13 08:55:48.833961
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    r1 = RoleMetadata()
    d1 = r1.serialize()
    assert isinstance(d1, dict)
    assert d1 == {'allow_duplicates': False, 'dependencies': []}
    r2 = RoleMetadata(allow_duplicates=True)
    d2 = r2.serialize()
    assert d2 == {'allow_duplicates': True, 'dependencies': []}


# Generated at 2022-06-13 08:55:59.515732
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    datastruct = {
        "_galaxy_info": "galaxy_info",
        "_allow_duplicates": True,
        "_dependencies": "dependencies",
        "argument_specs": "argument_specs"
    }
    datastruct_1 = {
        "_galaxy_info": "galaxy_info",
        "_allow_duplicates": True,
        "_dependencies": "dependencies",
        "_argument_specs": "argument_specs"
    }
    assert isinstance(RoleMetadata(None).load_data(datastruct, variable_manager=None, loader=None), RoleMetadata)
    assert isinstance(RoleMetadata(None).load_data(datastruct_1, variable_manager=None, loader=None), RoleMetadata)

# Generated at 2022-06-13 08:56:04.774883
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    rmd = RoleMetadata()
    rmd.load({"allow_duplicates": True,
              "dependencies": [{'role': 'foo', 'bar': 1}], }, None)
    assert rmd._allow_duplicates == True

# Generated at 2022-06-13 08:56:11.688704
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    owner_role = AnsibleRole('name', 'path', 'collection', None, None)
    role_metadata = RoleMetadata(owner_role)

    role_metadata.allow_duplicates = False
    role_metadata.dependencies = ['test']

    assert role_metadata.serialize() == dict(
        allow_duplicates=False,
        dependencies=['test']
    )

# Generated at 2022-06-13 08:56:15.820122
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    role_metadata = RoleMetadata()
    role_metadata.allow_duplicates = True
    role_metadata.dependencies = [1, 2, 3]

    expected_result = dict(
        allow_duplicates=True,
        dependencies=[1, 2, 3]
    )

    assert role_metadata.serialize() == expected_result

# Generated at 2022-06-13 08:56:32.604165
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 3
    role = Role()
    role._role_path = '/path/to/role'
    main_meta_path = os.path.join(role._role_path, 'meta', 'main.yml')
    data = {}
    variable_manager = None
    loader = None
    m = RoleMetadata.load(data, role, variable_manager, loader)

    with open(main_meta_path, "r") as role_meta_file:
        data = loader.load_from_file(role_meta_file)
    m = RoleMetadata.load(data, role, variable_manager, loader)
   

# Generated at 2022-06-13 08:56:40.878258
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    import ansible.utils.module_docs as module_docs

    class Options(object):
        module_name = 'AnsibleModule'
        module_path = module_docs._MODULE_PATH

    task = Task()
    task.action = 'setup'
    task.register = 'result'
    task._parent = PlayContext()
    task._role = None
    task._role_path = '/path/to/role'
    task._parent._role = None
    task._parent._role_path = '/path/to/role'
    task._parent._play = None
    task._parent._play

# Generated at 2022-06-13 08:56:50.030712
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role import Role
    from ansible.inventory.host import Host

    r = Role()
    r._role_path = "Modules/Deprecations"
    h = Host()
    h.name = 'localhost'
    r.get_vars.return_value = {}
    r.get_direct_vars.return_value = {}
    r._play = role_play(r, h)
    s_data = {'allow_duplicates': False, 'dependencies': ['geerlingguy.apache', {'role': 'geerlingguy.php'}]}
    m = RoleMetadata.load(data=s_data, owner=r)
    data = m.serialize()
    assert data == s_data



# Generated at 2022-06-13 08:57:06.722253
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # imports
    import os
    import tempfile
    import shutil
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.plugins.loader import role_loader

    # setup temp dir
    temp_dir = tempfile.mkdtemp()

    # create a role directory
    role_dir = os.path.join(temp_dir, 'myrole')
    os.mkdir(role_dir)

    # create a task


# Generated at 2022-06-13 08:57:11.182397
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data= dict(
        allow_duplicates=False,
        dependencies=['ansible.posix']
    )
    rolemeta = RoleMetadata(owner=None)
    rolemeta.deserialize(data)
    assert rolemeta.allow_duplicates == False
    assert rolemeta.dependencies == ['ansible.posix']

# Generated at 2022-06-13 08:57:22.253800
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.plays import Plays
    from ansible.playbook.taggable import Taggable
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role.include import RoleInclude

    obj = RoleMetadata()
    print(obj)
    data = {
      "allow_duplicates": "str",
      "dependencies": [
        {
          "name": "str",
          "collections": [
            "str"
          ]
        }
      ]
    }

    play = Play().load(data, variable_manager=None, loader=None)
    print(play)


# Generated at 2022-06-13 08:57:32.946906
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.include import RoleInclude
    d = {}
    d["dependencies"] = [{}]
    d["allow_duplicates"] = True
    role = Role()
    role._role_path = "/home/ansible/test/roles/role1"
    role._role_collection = None
    role._play = None
    role._parent_role = None
    role._dep_failed = False
    role._dep_chain = []
    role._collections = []
    role.vars = {}
    ans = RoleMetadata.load(d, role)

    assert(isinstance(ans, RoleMetadata))

# Generated at 2022-06-13 08:57:38.667811
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata(owner=None)
    data = {"allow_duplicates": True, "dependencies": []}
    role_metadata.deserialize(data)

    assert role_metadata.allow_duplicates == True
    assert role_metadata.dependencies == []

# Generated at 2022-06-13 08:57:46.981035
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    var_mng = object()
    data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    rmeta = RoleMetadata(owner=object())
    rmeta.deserialize(data)
    assert rmeta.allow_duplicates == False
    assert rmeta.dependencies == []
    assert rmeta.dependencies == data.get('dependencies', [])

# Generated at 2022-06-13 08:57:54.476914
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition

    role_path = os.path.join("test", "testrole")
    role = Role().load("testrole", load_role_path=role_path)
    assert len(role.get_dependencies()) == 0

    role_path = os.path.join("test", "testrole_with_dependencies")
    role = Role().load("testrole", load_role_path=role_path)
    assert len(role.get_dependencies()) == 4
    assert role.get_dependencies()[0].get_name() == "my_first_role"
    assert role.get_dependencies()[1].get_name() == "my_second_role"

# Generated at 2022-06-13 08:58:09.772386
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    serialized_data = dict(
        allow_duplicates=False,
        dependencies=[]
    )
    metadata = RoleMetadata()
    assert metadata.serialize() == serialized_data



# Generated at 2022-06-13 08:58:13.806334
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import RoleInclude
    import ansible.constants as C

    play = Play.load(dict(
        name = "Ansible Play",
        hosts = 'all',
        roles = 'apache',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='setup', args=dict()))
        ]
    ), loader=None)

    task = Task.load(dict(action=dict(module='setup', args=dict())), play=play, task_include=None)
    role_include = RoleInclude.load(dict(role='apache', tasks=[task]), play=play)
    play.roles = [role_include]

    role_

# Generated at 2022-06-13 08:58:24.710374
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    from ansible.playbook.role.definition import RoleDefinition

    roleDefinition = RoleDefinition(
        "role_def",
        {
            'name': "role_def",
            'dependencies': [
                "role1",
                "role2"
            ]
        },
        "/my/roles"
    )

    roleMetadata = RoleMetadata(roleDefinition)
    roleMetadata.deserialize(
        {
            'allow_duplicates': False,
            'dependencies': [
                "role1",
                "role2"
            ]
        }
    )

    assert isinstance(roleMetadata, RoleMetadata)
    assert roleMetadata.serialize() == \
        {'allow_duplicates': False, 'dependencies': ['role1', 'role2']}

# Generated at 2022-06-13 08:58:26.311865
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    # test load function
    pass


# Generated at 2022-06-13 08:58:42.399895
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    #from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role.metadata import RoleMetadata
    from ansible.playbook.role.requirement import RoleRequirement
    test_role_name = 'test'
    test_role_path = 'test_RoleMetadata'
    #mock_role_definition = RoleDefinition.load(dict(role=test_role_name,name=test_role_name,collections=[],path=test_role_path))
    mock_play_context = PlayContext()

# Generated at 2022-06-13 08:58:48.427482
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    # input args
    data = {'dependencies': [('sample', 'sample', 'sample', 'sample')], 'allow_duplicates': 'True'}
    # expected result
    expected = [('sample', 'sample', 'sample', 'sample')]
    # the class to be tested
    role_metadata = RoleMetadata()
    role_metadata.deserialize(data)
    # assert
    assert role_metadata._dependencies == expected
    assert role_metadata._allow_duplicates == True

# Generated at 2022-06-13 08:58:49.470216
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    assert RoleMetadata() is not None

# Generated at 2022-06-13 08:58:52.232386
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    res = RoleMetadata(owner=None).serialize()
    assert res == dict(allow_duplicates=False, dependencies=[])


# Generated at 2022-06-13 08:59:01.944717
# Unit test for constructor of class RoleMetadata
def test_RoleMetadata():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    play = Play().load({
        'name' : "Ansible Play",
        'hosts' : 'all',
        'gather_facts' : 'no',
        'tasks' : [
            dict(action=dict(module='debug', args=dict(msg='Hello World!')))
        ]
    }, variable_manager=None, loader=None)

    play_context = PlayContext()

    role_meta = RoleMetadata(owner=play)
    role_meta.load_data({'dependencies': [{'src': 'geerlingguy.certbot', 'version': '1.0.0'}]}, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:59:03.914383
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():
    obj = RoleMetadata()
    obj._variable_manager = None
    assert obj.serialize() == {'allow_duplicates': False, 'dependencies': []}


# Generated at 2022-06-13 08:59:37.913718
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.plugins.loader import fragment_loader
    from ansible.utils.display import Display

    class Options(object):
        pass

    display = Display()
    options = Options()
    options.verbosity = 0
    options.connection = 'smart'
    options.module_path = ''
    options.forks = 5
    options.become = False
    options.become_method = 'sudo'
    options.become_user = None
    options.check = False
    options.diff = False
    options.listhosts = None
    options.listtasks = None
    options.listtags = None
    options.syntax = None

# Generated at 2022-06-13 08:59:43.218509
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    meta = RoleMetadata()

    meta.deserialize({'allow_duplicates': True, 'dependencies': [{'role': 'common'}]})
    assert meta.allow_duplicates is True
    assert meta.dependencies[0].get_name() == 'common'
    assert meta.dependencies[0].get_role_path() is None

# Generated at 2022-06-13 08:59:53.397906
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():

    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition

    role_data = {'dependencies': ['role1', 'role2'], 'allow_duplicates': True}
    role_metadata = RoleMetadata.load(role_data, None)

    assert role_metadata.allow_duplicates
    assert isinstance(role_metadata.dependencies, list)
    assert len(role_metadata.dependencies) == 2
    assert isinstance(role_metadata.dependencies[0], RoleDefinition)
    assert isinstance(role_metadata.dependencies[0].role, RoleInclude)
    assert role_metadata.dependencies[0].role.name == 'role1'

# Generated at 2022-06-13 08:59:58.832330
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    data = {'allow_duplicates': False,
            'dependencies': []}
    result = RoleMetadata().deserialize(data)
    assert result == None

    data = {'allow_duplicates': True,
            'dependencies': [{'role': 'role1'}, {'role': 'role2'}]}
    result = RoleMetadata().deserialize(data)
    assert result == None

# Generated at 2022-06-13 09:00:07.212955
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    meta_yml = '''
        allow_duplicates: false
        dependencies:
            - role: a_role_name,v1.0.0
              something: something_value
              somevar: "{{ somevar }}"
            - role: b_role_name,v2.0.0
              somevar: "{{ somevar }}"
    '''
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # AnsibleDumper(None, default_style='"', default_flow_style=False)
    dumper = AnsibleDumper(None, default_flow_style=False, width=1000)

# Generated at 2022-06-13 09:00:10.030138
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_meta = RoleMetadata()
    role_meta.deserialize({'allow_duplicates': False, 'dependencies': []})
    assert role_meta.allow_duplicates == False
    assert role_meta.dependencies == []

# Generated at 2022-06-13 09:00:18.669601
# Unit test for method serialize of class RoleMetadata
def test_RoleMetadata_serialize():

    # Valid data
    role_metadata = RoleMetadata().load({
        'allow_duplicates': True
    }, owner='owner')
    assert role_metadata.serialize() == dict(
        allow_duplicates=True,
        dependencies=[]
    )

    # Invalid data
    try:
        RoleMetadata().load({
            'allow_duplicates': 'invalid'
        }, owner='owner')
    except AnsibleParserError as e:
        assert "allow_duplicates: invalid" in to_native(e)
    else:
        assert False, "Expected AnsibleParserError"


# Generated at 2022-06-13 09:00:27.228828
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    data = dict(
        allow_duplicates=False,
        dependencies=[
            dict(
                role='b',
                x=1,
                y=2
            ),
            dict(
                role='c',
                z=3
            )
        ],
        galaxy_info=dict(
            author='d'
        )
    )

    variable_manager = VariableManager()

# Generated at 2022-06-13 09:00:36.880506
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    # Test data
    test_data = {'galaxy_info': {'author': 'TEST', 'description': 'TEST'},
                 'dependencies': ['role1', 'role2']}

    # Create a Playbook and add a Role
    p = Playbook()
    role = Role()
    role._role_path = 'role_path'
    role._play = p
    p._loader = DataLoader()
    p._tqm = None
    p._variable_manager = None
    p._basedir = 'basedir'
    p._play_context = PlayContext()

# Generated at 2022-06-13 09:00:45.668934
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude

    # Normal role definition
    role_def = RoleMetadata.load(data={'dependencies': ['foo']}, owner=RoleDefinition.load(name='bar'))
    assert role_def.dependencies[0].get_name() == 'foo'
    assert len(role_def.dependencies) == 1

    # Normal role include
    role_inc = RoleMetadata.load(data={'dependencies': ['foo']}, owner=RoleInclude())
    assert role_inc.dependencies[0].get_name() == 'foo'
    assert len(role_inc.dependencies) == 1

    # Empty role definition

# Generated at 2022-06-13 09:01:45.218697
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    r1 = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=[
            dict(
                src='https://github.com/joesmith/role',
                name='myrole',
                scm='git',
                version='master'
            )
        ]
    )
    r1.deserialize(data)
    assert r1.allow_duplicates
    assert r1.dependencies

    r2 = RoleMetadata()
    data = dict(
        allow_duplicates=True,
        dependencies=[
            dict(
                src='https://github.com/joesmith/role',
                scm='git',
                version='master'
            )
        ]
    )
    r2.deserialize(data)
    assert r2.allow_dupl

# Generated at 2022-06-13 09:01:56.594877
# Unit test for method load of class RoleMetadata
def test_RoleMetadata_load():
    from ansible.playbook.role import Role
    from ansible.parsing.yaml.objects import AnsibleUnicode

    role = Role()
    role._role_path = '../test_role'
    role.name = 'test_role'

    #pylint: disable=too-many-nested-blocks,too-many-branches,too-many-statements
    def fake_loader(file_name):

        ds = dict()


# Generated at 2022-06-13 09:02:03.457950
# Unit test for method deserialize of class RoleMetadata
def test_RoleMetadata_deserialize():
    role_metadata = RoleMetadata(owner=None)
    data = {'allow_duplicates': True}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates is True
    data = {'allow_duplicates': False}
    role_metadata.deserialize(data)
    assert role_metadata.allow_duplicates is False
    data = {'dependencies': [{'name': 'geerlingguy.java', 'role': {'name': 'geerlingguy.java'}}]}
    role_metadata.deserialize(data)
    assert role_metadata.dependencies == data.get('dependencies', [])
    data = {'dependencies': [{'name': 'nginx', 'role': {'name': 'nginx'}}]}
    role_metadata