

# Generated at 2022-06-22 11:29:51.173491
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default(None) == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:29:54.089066
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    result = obj._load_collections("collections", ['ansible.builtin', 'ansible.builtin'])
    assert result == ["ansible.builtin"]

# Generated at 2022-06-22 11:30:03.650087
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.playbook.attribute import FieldAttribute
    from ast import literal_eval
    from ansible.module_utils.six import string_types
    from ansible.utils.display import Display
    display = Display()

    # Test default value of collections
    _ensure_default_collection()
    default_collection = AnsibleCollectionConfig.default_collection
    if default_collection:
        assert isinstance(default_collection, string_types)
    else:
        assert isinstance(default_collection, (None.__class__,))

    # Test FieldAttribute
    assert isinstance(CollectionSearch._collections, FieldAttribute)
    assert isinstance(CollectionSearch._collections.default, types.FunctionType)

# Generated at 2022-06-22 11:30:06.245363
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    assert isinstance(instance._collections, list)
    assert isinstance(instance._collections, string_types)

# Generated at 2022-06-22 11:30:14.038878
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    _collections = cs._load_collections('collections', None)
    assert _collections == None

    _collections = cs._load_collections('collections', ['collection_name'])
    assert _collections == ['collection_name', 'ansible.builtin']

    _collections = cs._load_collections('collections', ['collection_name', 'ansible.builtin'])
    assert _collections == ['collection_name', 'ansible.builtin']

# Generated at 2022-06-22 11:30:15.825228
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs
    assert cs._collections == cs._load_collections

# Generated at 2022-06-22 11:30:23.222669
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test constructor when collection_list is None
    collection_list = _ensure_default_collection()
    assert 'ansible.builtin' in collection_list
    assert 'ansible.legacy' in collection_list
    assert AnsibleCollectionConfig.default_collection in collection_list

    # Test constructor when collection_list is not None
    collection_list = None
    collection_list = _ensure_default_collection(collection_list)
    assert 'ansible.builtin' in collection_list
    assert 'ansible.legacy' in collection_list
    assert AnsibleCollectionConfig.default_collection in collection_list

# Generated at 2022-06-22 11:30:31.613477
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.module_utils._text import to_text
    from ansible.cli.adhoc import AdHocCLI

    cli = AdHocCLI()  # type: ignore
    loader, options, commands = cli._load_params()  # pylint: disable=protected-access
    options.collections = []
    options.b = 'local'
    options.k = None
    options.new_vault_password_file = '/home/user/.vault_password.new'

    if not commands:
        commands = ['/usr/bin/uptime']

    display.verbosity = options.verbosity
    display.deprecation_warnings = options.show_deprecation_warnings

    # Create data structure
    from ansible.parsing.yaml.loader import AnsibleLoader
    #

# Generated at 2022-06-22 11:30:44.434268
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    #Test when no collection is provided
    c1 = CollectionSearch()
    c1.__dict__ = dict(collections=None, _collection_name=None, _collection_name_for_tasks=None)
    assert c1._load_collections(None, None) is None

    #Test when collection is provided
    c1 = CollectionSearch()
    c1.__dict__ = dict(collections=[], _collection_name=None, _collection_name_for_tasks=None)
    assert c1._load_collections(None, None) is None

    #Test when collection is provided as a string
    c1 = CollectionSearch()
    c1.__dict__ = dict(collections='test', _collection_name=None, _collection_name_for_tasks=None)
    assert c1._load_collections

# Generated at 2022-06-22 11:30:53.198593
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    class Test(CollectionSearch):
        _collections = FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection,
                                  always_post_validate=True, static=True)

    t = Test()

    # Test no value
    ds = dict()
    t._load_collections(None, ds)

    # Test empty value
    ds = dict(collections=list())
    t._load_collections(None, ds)

    # Test value
    ds = dict(collections=['collection'])
    t._load_collections(None, ds)

# Generated at 2022-06-22 11:31:01.734086
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    expected_output = ['ansible.builtin','ansible.legacy','ansible']
    result = CollectionSearch._load_collections(CollectionSearch,expected_output)
    assert result == expected_output
    expected_output = []
    result = CollectionSearch._load_collections(CollectionSearch,expected_output)
    assert result == None

# Generated at 2022-06-22 11:31:04.170202
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    class TestCollectionSearch(CollectionSearch):
        pass

    m = TestCollectionSearch()

    assert m.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:31:06.039901
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
  assert hasattr(CollectionSearch, '_collections')
  assert hasattr(CollectionSearch, '_load_collections')

# Generated at 2022-06-22 11:31:11.394595
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    instance = CollectionSearch()

    # check collection attribute is initialized with default value
    assert instance._collections == [ 'ansible.legacy' ]

    # check _load_collections method returns a list of collections
    assert instance._load_collections(attr='collections', ds=[ 'ansible.builtin', 'ansible.network' ]) == \
           [ 'ansible.builtin', 'ansible.network', 'ansible.legacy' ]

# Generated at 2022-06-22 11:31:15.602477
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    print(cs._load_collections('collections', 'ansible_collections.canux.example_collection'))


if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:27.031574
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()

    expected_result = ['ansible.builtin']
    result = c._load_collections('', ['ansible.builtin'])
    assert result == expected_result

    expected_result = ['foo.bar', 'ansible.builtin']
    result = c._load_collections('', ['foo.bar', 'ansible.builtin'])
    assert result == expected_result

    expected_result = ['ansible.builtin', 'foo.bar']
    result = c._load_collections('', ['ansible.builtin', 'foo.bar'])
    assert result == expected_result

    expected_result = ['ansible.builtin', 'foo.bar']
    result = c._load_collections('', ['foo.bar'])
    assert result == expected_result


# Generated at 2022-06-22 11:31:28.947210
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()



# Generated at 2022-06-22 11:31:32.703993
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    result = CollectionSearch('collections', [], [])
    ds = {}
    result._load_collections('collections', ds)
    assert result.collections == None


# Generated at 2022-06-22 11:31:36.267983
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default == _ensure_default_collection()
    assert collection_search._collections.always_post_validate == True
    assert collection_search._collections.static == True

# Generated at 2022-06-22 11:31:38.479012
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
  cs = CollectionSearch()
  cs._collections = ['col1', 'col2']
  cs._load_collections(None, ['col1', 'col2'])

# Generated at 2022-06-22 11:31:47.370257
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None
    assert cs.collections == 'ansible.builtin'

# Generated at 2022-06-22 11:31:48.868276
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    assert x._collections.default() == [',core']

# Generated at 2022-06-22 11:31:59.164559
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class Foo(object):
        def __init__(self):
            self._collections = None
            self.post_validate_calls = []

        def get_validated_value(self, attr, validator, ds, fail_required):
            return ds

    # get_value will call post_validate to validate the result
    foo_obj = Foo()
    collection_search = CollectionSearch()
    collection_search._load_collections('collections', foo_obj, ['test'])
    assert foo_obj.post_validate_calls == [{'collections': ['ansible.builtin', 'test']}]

# Generated at 2022-06-22 11:32:01.219418
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search_object = CollectionSearch()
    assert collection_search_object.collections == "ansible.builtin"

# Generated at 2022-06-22 11:32:03.128362
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == _ensure_default_collection()


# Generated at 2022-06-22 11:32:05.675539
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin','ansible.legacy']

# Generated at 2022-06-22 11:32:08.588886
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default() == _ensure_default_collection()
    assert cs._collections.priority == 100


# Generated at 2022-06-22 11:32:11.099853
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test to make sure that the collections list is empty when this class is first constructed
    cs = CollectionSearch()
    assert not cs.collections


# Generated at 2022-06-22 11:32:13.121729
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:16.110905
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        pass
    
    t = TestCollectionSearch()
    t.post_validate()
    assert isinstance(t.collections, list)

# Generated at 2022-06-22 11:32:30.430913
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    assert CollectionSearch()._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:32:32.144298
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default == _ensure_default_collection(None)



# Generated at 2022-06-22 11:32:33.041964
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
	collectionSearch = CollectionSearch()

# Generated at 2022-06-22 11:32:35.039407
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Arrange
    collection_search = CollectionSearch()

    # Assert
    assert collection_search is not None
    assert collection_search._collections is not None


# Generated at 2022-06-22 11:32:46.576940
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base
    from collections import namedtuple
    from ansible.playbook.vars.manager import VarManager
    from ansible.playbook.vars.singlevar import Singlevar

    def _get_var_manager(var_manager):
        Var = namedtuple('Var', ('name', 'value'))
        var = Var('collections', {'name': 'test', 'version': '1.0.0'})
        return var_manager.add_new_variable(var, Singlevar())

    var_manager = VarManager()
    var_manager = _get_var_manager(var_manager)

    base = Base(dict(collections=['test']), var_manager)
    assert base.collections == ['test']

# Generated at 2022-06-22 11:32:54.471585
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    play = Play()
    block = Block()
    role = Role()
    task = Task()
    play.load(dict(name='foo',), play._ds)
    block.load(dict(), block._ds)
    role.load(dict(name='bar',), role._ds)
    task.load(dict(name='baz',), task._ds)
    play.post_validate()
    block.post_validate()
    role.post_validate()
    task.post_validate()
    play.block = block
    block.block = block

# Generated at 2022-06-22 11:32:56.034110
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:01.280568
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections
    assert search._collections.default == _ensure_default_collection
    assert search._collections.field_name == 'collections'
    assert search._collections.required == False
    assert search._collections.always_post_validate == True
    assert search._collections.static == True
    assert search._collections.attributes == {}


# Generated at 2022-06-22 11:33:03.485761
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    d = CollectionSearch()
    assert d._collections == 'ansible.builtin'
    assert isinstance(d._collections, string_types)

# Generated at 2022-06-22 11:33:08.115094
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test_data
    collection_search = CollectionSearch(None, None, None)
    data = {'collections': ['ansible.builtin', 'ansible.legacy']}

    # Exercise
    result = collection_search._load_collections(None, data)

    # Verify
    # It should be generate a Collection object
    assert isinstance(result, list)

# Generated at 2022-06-22 11:33:36.971676
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == ['ansible_galaxy.collections.ns5', 'ansible.builtin']  #FIXME!

# Generated at 2022-06-22 11:33:47.666444
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    with engine.play_context.set_remote_address('192.168.0.1'):
        with engine.play_context.set_port(22):
            host = 'example.org'
            r = Connection(host, engine.accelerate, engine.timeout, engine.user, engine.shell,
                           'smart', None, engine.passwords, engine.persistent_connect_timeout, engine.become,
                           engine.become_method, engine.become_user, verbosity=3, other_user=None,
                           private_key_file=None, connection_user=None, control_path=None)
            r.connection = self.connection_loader.get('ssh')
            
            p = self.loader.load_from_file('Playbook name')

# Generated at 2022-06-22 11:33:50.015166
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a=CollectionSearch()
    assert a._collections.default() == _ensure_default_collection()
    # assert a._collections.default().__str__() == ['ansible.posix']

# Generated at 2022-06-22 11:33:54.838279
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    test = CollectionSearch()

    # test attribute default value
    assert test._collections == _ensure_default_collection()
    assert test._collections.name == 'collections'
    assert test._collections.isa == 'list'
    assert test._collections.listof == string_types



# Generated at 2022-06-22 11:33:56.086359
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:04.776606
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import mock
    from ansible.module_utils.six import PY3

    # FIXME: Use a mock file to prevent the path from actually opening a file
    with mock.patch('ansible.playbook.role.RoleRequirementSpec._get_collection_config()', return_value=None):
        collection = CollectionSearch()

    if not PY3:
        expected = u'ansible.legacy'
    else:
        expected = 'ansible.legacy'

    assert collection.collections == [expected]

# Generated at 2022-06-22 11:34:07.570398
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections is not None, "Did not set collections correctly"

# Generated at 2022-06-22 11:34:09.211441
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:11.248142
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

    assert collection_search._collections is not None



# Generated at 2022-06-22 11:34:14.292219
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_instance = CollectionSearch()
    print("Collections")
    print(test_instance.collections)

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:35:09.660313
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    parser = CollectionSearch()
    parser.collections = ['collections']
    assert parser.collections == ['collections']

# Generated at 2022-06-22 11:35:18.282753
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test empty
    search_result = CollectionSearch()
    assert search_result._collections == _ensure_default_collection()

    # Test with one collection name
    test_name = "TEST_COLLECTION"
    search_result = CollectionSearch(collections=[test_name])
    assert search_result._collections == [test_name]

    # Test with multiple collection names
    test_names = ["TEST_COLLECTION_1", "TEST_COLLECTION_2"]
    search_result = CollectionSearch(collections=test_names)
    assert search_result._collections == test_names

    # Test with template collection name.
    # FIXME: this test should fail, but it passes because the environment is not set up.
    test_name = "${TEST_COLLECTION_TEMPLATE}"


# Generated at 2022-06-22 11:35:23.158627
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert test_obj._collections.default()[0] is 'ansible.builtin'
    test_obj._load_collections('collections', None)
    test_obj._load_collections('collections', ['test1'])

# Generated at 2022-06-22 11:35:25.321515
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    cs = CollectionSearch()
    print(cs._collections)
    print(cs._load_collections("collections", ["ansible.builtin"]))

# Generated at 2022-06-22 11:35:27.069678
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default == []
    assert CollectionSearch._collections.type == string_types

# Generated at 2022-06-22 11:35:30.147880
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c is not None
    assert c.__class__.__name__ == 'CollectionSearch'


# Generated at 2022-06-22 11:35:31.575310
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    assert instance.collections == ["ansible.legacy"]

# Generated at 2022-06-22 11:35:35.167984
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.task_include import TaskInclude

    a = TaskInclude()
    assert a._collections == _ensure_default_collection([])

# Generated at 2022-06-22 11:35:44.184369
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # The constructor of class Base class requires a data set
    data_set = dict()

    # Create an object of class CollectionSearch
    collection_search = CollectionSearch(data_set)

    # Test that the default collection list is ['ansible.builtin', 'ansible.legacy']
    assert collection_search._collections.default == _ensure_default_collection()

    # Test that the listof type of class CollectionSearch is string_types
    assert collection_search._collections.listof == string_types
    assert collection_search._collections.listof[0] == 'ansible.builtin'

    # Test that the value of the dataset is string_types
    assert collection_search.data_set == string_types

# Generated at 2022-06-22 11:35:45.450380
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:36:52.041280
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collection_search_obj = CollectionSearch()
    display.display("Testing CollectionSearch class constructor")
    assert test_collection_search_obj.__dict__['_collections'].default is _ensure_default_collection
    assert test_collection_search_obj.__dict__['_collections'].always_post_validate == True
    assert test_collection_search_obj.__dict__['_collections'].static == True

# Generated at 2022-06-22 11:37:00.895985
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert(AnsibleCollectionConfig.default_collection == 'ansible.builtin')
    assert(CollectionSearch()._collections == ['ansible.builtin', 'ansible.legacy'])
    assert(CollectionSearch().collections is None)

    # when a value is set
    c = CollectionSearch()
    c.collections = ['ns', 'ns2']
    assert(c.collections == ['ns', 'ansible.builtin', 'ansible.legacy'])
    # when a value is set by setting attr
    c = CollectionSearch()
    c.attributes['collections'] = ['ns', 'ns2']
    assert(c.collections == ['ns', 'ansible.builtin', 'ansible.legacy'])
    # when a value is set by setting attr
    c = CollectionSearch()
   

# Generated at 2022-06-22 11:37:05.355386
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    search.collections = ['col1', 'col2']
    assert search.collections == ['col1', 'col2']
    assert search._collections == ['col1', 'col2']
    search.collections = None
    assert search.collections == None


# Generated at 2022-06-22 11:37:16.442265
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import IncludeRole
    role_incl = IncludeRole()
    role_incl._collections = ['Foo.bar']
    assert role_incl._collections == ['Foo.bar']

    # Make sure we have the default collection for testing
    assert _ensure_default_collection() == ['ansible.builtin', 'ansible.legacy']

    # Test dynamic roles
    from ansible.playbook_tests.unit.task_include.role_include_task import dynamic_roles_test
    role = dynamic_roles_test[0]
    assert role._collections == ['Foo.bar', 'ansible.builtin', 'ansible.legacy']

    # Test static roles

# Generated at 2022-06-22 11:37:28.371555
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base
    from ansible.template import template as ansible_template
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    ansible_template.template = lambda x: 'template'
    b = Base.load(dict(collections=['collection']), wrap_as=Block)
    assert b._collections == ['collection']
    c = Base.load(dict(collections=['collection']), wrap_as=Conditional)
    assert c._collections == ['collection']
    t = Base.load(dict(collections=['collection']), wrap_as=Task)
    assert t._collections == ['collection']

# Generated at 2022-06-22 11:37:29.440820
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs is not None

# Generated at 2022-06-22 11:37:40.631090
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import ansible
    collection_path = ansible.constants.DEFAULT_COLLECTIONS_PATHS[0]
    collection_candidates = ['ansible_namespace.collection_name1', 'ansible_namespace.collection_name2']

    collection_search = CollectionSearch()

    # Make sure _load_collections() returns collection list with default collection at the head
    collection_list = collection_search._load_collections(None, collection_candidates)
    assert collection_list[0].startswith(collection_path)
    assert collection_list[1] in collection_candidates

    # Make sure _load_collections() throws an error if "collections" is empty
    collection_list = collection_search._load_collections(None, [])
    assert not collection_list

# Generated at 2022-06-22 11:37:46.209201
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    if ('ansible.builtin' in obj._collections) and ('ansible.legacy' in obj._collections) and ('ansible.builtin' in obj._collections):
        print("Ok")

if __name__ == '__main__':
    obj = CollectionSearch()
    obj._collections = obj._ensure_default_collection()

# Generated at 2022-06-22 11:37:51.937605
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    assert collectionSearch
    assert _ensure_default_collection() == ['Accelerate']
    assert _ensure_default_collection(['Accelerate']) == ['Accelerate']
    assert _ensure_default_collection(['Accelerate', 'Accelerate2']) == ['Accelerate', 'Accelerate2']
    assert _ensure_default_collection(['Accelerate2']) == ['Accelerate2']
    assert _ensure_default_collection(['Accelerate2', 'Accelerate']) == ['Accelerate2', 'Accelerate']
    assert _ensure_default_collection(['Accelerate', 'Accelerate2']) == ['Accelerate', 'Accelerate2']

# Generated at 2022-06-22 11:37:53.901544
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    del CollectionSearch._collections
    CollectionSearch()