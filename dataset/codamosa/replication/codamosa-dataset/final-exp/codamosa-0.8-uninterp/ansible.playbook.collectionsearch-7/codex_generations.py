

# Generated at 2022-06-22 11:29:50.629536
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    testCollectionSearch = CollectionSearch()
    assert testCollectionSearch._collections is None

# Generated at 2022-06-22 11:29:53.010867
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()
    assert cs._load_collections(None, None) == _ensure_default_collection()

# Generated at 2022-06-22 11:29:56.573737
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    with pytest.raises(AttributeError):
        CollectionSearch._collections = FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection,
                                  always_post_validate=True, static=True)

# Generated at 2022-06-22 11:29:59.973492
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test for invalid value
    expected_msg = "value of collections must be a list of strings"
    try:
        _ = CollectionSearch(collections='collections')
    except ValueError as e:
        assert str(e) == expected_msg

# Generated at 2022-06-22 11:30:03.092059
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search=CollectionSearch()
    collection_search._collections=['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:03.749906
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()

# Generated at 2022-06-22 11:30:15.628719
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test 1: Testing both default collections and default collections as a list of 1.
    test_object1 = CollectionSearch()
    assert test_object1._load_collections({'_collections': ["ansible_collections.sensu.sensu_go"]}) == ['ansible_collections.sensu.sensu_go', "ansible.builtin"]
    # Test 2: Testing that the default collection is not added when provided.
    test_object2 = CollectionSearch()
    assert test_object2._load_collections({'_collections': ["ansible_collections.sensu.sensu_go", "ansible.builtin"]}) == ['ansible_collections.sensu.sensu_go', "ansible.builtin"]
    # Test 3: Testing that the default collection is not added when

# Generated at 2022-06-22 11:30:18.772011
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    display.debug('{0}'.format(collection))
    assert collection

# Generated at 2022-06-22 11:30:22.844761
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print("TESTING: CollectionSearch")
    cs = CollectionSearch()
    assert cs
    assert cs._collections == ['ansible.builtin']
    assert cs._load_collections == ['ansible.builtin']

# Unit tests for _ensure_default_collection function

# Generated at 2022-06-22 11:30:24.350928
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collections = CollectionSearch()
    print(test_collections)

# Generated at 2022-06-22 11:30:33.789628
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test
    collection_search = CollectionSearch()
    assert collection_search._collections is _ensure_default_collection
    assert isinstance(collection_search._collections, FieldAttribute)
    assert collection_search._load_collections is not None

# Generated at 2022-06-22 11:30:36.931898
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    obj.collections = 'ansible.builtin'
    assert obj.collections == 'ansible.builtin'

# Generated at 2022-06-22 11:30:37.556546
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:30:38.285977
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:30:41.960498
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()

    # test to see if constructor returns Base for bases
    assert CollectionSearch.__bases__ == (test._store,)

    # Test to see if check_required is a static method
    assert hasattr(test, 'check_required')

# Generated at 2022-06-22 11:30:42.578994
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    t = CollectionSearch()

# Generated at 2022-06-22 11:30:43.849814
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    loader = CollectionSearch()
    assert loader._collections == ['ansible']

# Generated at 2022-06-22 11:30:54.894369
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.executor.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude

    task = TaskInclude()

# Generated at 2022-06-22 11:31:02.313694
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansiblelint.rules.AnsibleLintRule import AnsibleLintRule
    from ansiblelint.runner import Runner
    import ansiblelint.utils
    filepath = 'testResources/collectionSearch/test_collections_search.yml'
    rule = AnsibleLintRule()
    runner = Runner(rule, [filepath], [], [], [])
    collectionSearch = CollectionSearch()
    display.verbosity = 3
    collectionSearch._load_collections(None, runner)

# Generated at 2022-06-22 11:31:11.284504
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.attribute import FieldAttribute
    from ansible.module_utils.six import string_types
    # test _collections isa FieldAttribute, priority 100, default _ensure_default_collection, always_post_validate True, static True
    assert isinstance(CollectionSearch._collections, FieldAttribute)
    assert CollectionSearch._collections.isa == 'list'
    assert CollectionSearch._collections.priority == 100
    assert CollectionSearch._collections.default == _ensure_default_collection
    assert CollectionSearch._collections.always_post_validate == True
    assert CollectionSearch._collections.static == True
    assert isinstance(CollectionSearch._collections.listof, string_types)

# Generated at 2022-06-22 11:31:34.807927
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block_include import BlockInclude
    from collections import namedtuple

    class FakeRole(RoleInclude):
        pass

    class FakeIncludedTask(TaskInclude):
        pass

    class FakePlayContext(PlayContext):
        pass

    class FakeBlock(Block):
        pass

    class FakeBlockInclude(BlockInclude):
        pass

    Collection = namedtuple('Collection', ['name', 'collections', 'version'])

# Generated at 2022-06-22 11:31:36.056337
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:31:38.787090
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    attr = 'collections'
    ds = ['ansible.builtin','ansible.legacy', 'ansible.ubuntu']
    cs = CollectionSearch()
    assert cs._load_collections(attr, ds) == ds

# Generated at 2022-06-22 11:31:40.992484
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c1 = CollectionSearch()
    c1_collections = c1._collections
    # Test if _collections is populated with a list of collection names
    assert isinstance(c1_collections, type([]))

# Generated at 2022-06-22 11:31:42.795414
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert isinstance(getattr(obj, '_collections'), FieldAttribute)

# Generated at 2022-06-22 11:31:50.852913
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class CollectionSearchMock(CollectionSearch):
        def __init__(self, ds):
            super(CollectionSearchMock, self).__init__(ds)

        def get_validated_value(self, name, attribute, sourced_data, obj):
            return sourced_data

    test_ds = ['test_collection']
    cs = CollectionSearchMock(test_ds)
    assert cs._collections._value == test_ds
    assert len(cs._collections._value) == 1
    assert cs._collections._value[0] == 'test_collection'

# Generated at 2022-06-22 11:31:52.919721
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections['default'] == None

# Generated at 2022-06-22 11:32:01.550457
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test for constructor
    module = CollectionSearch()

    # Default value for 'collections'
    assert module.get_validated_value('collections', module._collections, None, {}) == "None"

    # Reseting the value for 'collections'
    module.collections = ['ansible.builtin', 'ansible.legacy']

    # Testing the updated value of 'collections' field
    assert module.get_validated_value('collections', module._collections, None, {}) == "['ansible.builtin', 'ansible.legacy']"

# Generated at 2022-06-22 11:32:08.177341
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    result = cs._load_collections("collections", "")
    assert result is None

    cs = CollectionSearch()
    result = cs._load_collections("collections", "some collections")
    assert result == ['ansible.builtin', 'some collections'] 

    cs = CollectionSearch()
    result = cs._load_collections("collections", ['some collections'])
    assert result == ['ansible.builtin', 'some collections']

# Generated at 2022-06-22 11:32:10.760295
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # pylint: disable=unnecessary-lambda
    isinstance(CollectionSearch, (type))
    assert callable(CollectionSearch)

# Generated at 2022-06-22 11:32:30.341914
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role import Role
    from ansible.plugins.loader.roles import Roles
    from ansible.playbook.task import Task
    from ansible.plugins.loader.tasks import Tasks
    from ansible.playbook.block import Block

    for B in (Role, Task, Block, Tasks, Roles):
        c = B()
        assert c._collections == c.collections
        assert c._collections == c._load_collections(None, None)



# Generated at 2022-06-22 11:32:32.602030
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cls = CollectionSearch()
    cls.__init__()
    assert isinstance(cls, CollectionSearch)

# Generated at 2022-06-22 11:32:33.841519
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch_obj = CollectionSearch()
    assert CollectionSearch_obj._collections() is not None

# Generated at 2022-06-22 11:32:39.856617
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search.post_validate({ 'collections': ['c1', 'c2', 'c3'] }, {})
    assert collection_search.post_validate({ 'collections': ['c1', 'c2', 'c3'] }, {})['collections'] == ['ansible.builtin', 'c1', 'c2', 'c3']

# Generated at 2022-06-22 11:32:44.957176
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cl = CollectionSearch()

    # we manually set the collections field
    cl._collections = ['col1','col2','col3']

    # The actual call to _load_collections
    cl._load_collections('collections', ['ans1','ans2','ans3'])
    assert cl._collections==['ans1','ans2','ans3']


# Generated at 2022-06-22 11:32:47.006656
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch(), CollectionSearch)

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:48.376028
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is None


# Generated at 2022-06-22 11:32:50.917047
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections == _ensure_default_collection()
    assert c.collections == ["ansible_collections.ansible"]

# Generated at 2022-06-22 11:32:53.162850
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._load_collections(None, None) is None

# Generated at 2022-06-22 11:32:57.788556
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._validate_collections(c._collections, ['ansible.legacy', 'ansible_collections.bar.foo']) == ['ansible_collections.bar.foo', 'ansible.legacy'], "Error"
    return c



# Generated at 2022-06-22 11:33:30.604831
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from collections import OrderedDict
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition


    play_context = PlayContext()
    task = Task()
    block = Block()
    role_definition = RoleDefinition()

    assert issubclass(CollectionSearch, OrderedDict)

    assert isinstance(play_context, PlayContext)
    assert isinstance(task, Task)
    assert isinstance(block, Block)
    assert isinstance(role_definition, RoleDefinition)

# Generated at 2022-06-22 11:33:41.992560
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    obj = CollectionSearch()
    ret = {}
    ret['collections'] = ["ansible_namespace.collection_name"]
    obj._validate_collections(ret)
    assert obj.collections is not None
    assert obj.collections == ["ansible.builtin", "ansible.legacy", "ansible_namespace.collection_name"]

    ret['collections'] = [""]
    obj._validate_collections(ret)
    assert obj.collections is not None
    assert obj.collections == ["ansible.builtin"]

    ret['collections'] = ["ansible.builtin"]
    obj._validate_collections(ret)
    assert obj.collections is not None
    assert obj.collections == ["ansible.builtin"]


# Generated at 2022-06-22 11:33:43.451825
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search, CollectionSearch)

# Generated at 2022-06-22 11:33:48.526410
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    if _ensure_default_collection(collection_list=None):
        assert True
    else:
        assert False
    if _ensure_default_collection(['sweet']):
        assert True
    else:
        assert False
    if _ensure_default_collection(['sweet', 'ansible.builtin']):
        assert True
    else:
        assert False
    return True

# Generated at 2022-06-22 11:33:51.150037
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    a = cs._load_collections(None, None)
    print(a)


test_CollectionSearch()

# Generated at 2022-06-22 11:33:53.209810
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.__init__()
    cs._load_collections()
    cs._collections()

# Generated at 2022-06-22 11:34:02.579015
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    def display_warning(msg):
        display_warning.last_msg = msg
        # print(msg)

    import ansible.playbook
    ansible_playbook_instance = ansible.playbook.Playbook()
    collection_search = CollectionSearch()

    assert collection_search._collections.default == ['ansible_collections.my_namespace.my_collection.tasks']

    assert collection_search.collections == ['ansible_collections.my_namespace.my_collection.tasks']

    collection_search.collections = None
    assert collection_search.collections == None

    display_warning.last_msg = None
    collection_search.post_validate(ansible_playbook_instance)
    assert display_warning.last_msg == None

    display_warning.last_msg = None
    collection

# Generated at 2022-06-22 11:34:04.695538
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.block import Block

    block = Block()
    assert block.collections is None

# Generated at 2022-06-22 11:34:17.204214
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import unittest
    from ansible.playbook.playbook_attribute import PlaybookAttribute
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude

    class TestAnsibleCollectionSearch(unittest.TestCase):
        def test_collections(self):
            # default value for collections
            cs = CollectionSearch(PlaybookAttribute(), PlayContext())
            self.assertIsNotNone(cs.collections)

            # load_collections, which is called during post_validate, is
            # tested in another test case

            with self.assertRaises(AttributeError):
                # Should not be able to set collections because it is static
                cs.collections = [u'ansible.builtin']

    tc = TestAnsibleCollectionSearch()
    tc.test

# Generated at 2022-06-22 11:34:19.184779
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == 'ansible.builtin'

# Generated at 2022-06-22 11:35:12.609476
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()

# Generated at 2022-06-22 11:35:19.438994
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ''' test_collection_search.py::test_CollectionSearch '''
    from ansible.playbook.task_include import TaskInclude, _TaskIncludeConstructor
    from ansible.playbook.role import Role, _RoleRequirementConstructor
    import ansible.playbook.role_include
    import ansible.playbook.block
    import ansible.playbook.play
    import ansible.playbook.playbook

    # pylint: disable=protected-access

    # Ensure priority is set to 100
    assert CollectionSearch()._collections.priority == 100
    assert len(CollectionSearch()._collections.aliases) == 0

    # Ensure default value is set to '_ensure_default_collection'
    assert CollectionSearch()._collections.default == _ensure_default_collection

    # Ensure 'listof' is

# Generated at 2022-06-22 11:35:25.183505
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert 'ansible.builtin' in a._load_collections('collections', ['ansible.builtin'])
    assert 'ansible.builtin' in a._load_collections('collections', None)
    assert 'ansible.builtin' in a._load_collections('collections', [])
    assert 'ansible.builtin' in a._load_collections('collections', ['mike.mike'])

# Generated at 2022-06-22 11:35:25.667286
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search=Collec

# Generated at 2022-06-22 11:35:30.295237
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    test_collections = ['ansible.builtin','ansible.legacy','user_collection','other_collection','third_collection','fourth_collection']
    collection_search.collections = test_collections
    assert collection_search.collections == test_collections

# Generated at 2022-06-22 11:35:41.732955
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Load the class here for this test since Ansible needs to be imported in the module that loads this class
    from ansible.errors import AnsibleError
    from ansible.playbook.base import Base
    from ansible.plugins.loader import collection_loader

    # Load the class
    obj = CollectionSearch()

    # Check if the obj is an instance of CollectionSearch
    assert isinstance(obj, CollectionSearch)
    # Check if the obj is an instance of Base
    assert isinstance(obj, Base)

    # Check if the '_collections' attribute of the obj is set
    # Which calls '_ensure_default_collection'
    assert obj._collections == _ensure_default_collection()

    # Check if the '_load_collections' function fails when no collection is specified
    ds = "not_valid"
    assert obj

# Generated at 2022-06-22 11:35:47.187921
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()

    # testing default constructor
    assert search.collections == _ensure_default_collection()

    # testing explicit constructor
    test_collections = ["1.0.0", "2.0.0"]
    search = CollectionSearch(collections=test_collections)
    assert search.collections == test_collections
    assert "ansible.builtin" in search.collections

# Generated at 2022-06-22 11:35:48.385785
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a=CollectionSearch()
    # test constructor of class CollectionSearch
    assert a is not None

# Generated at 2022-06-22 11:35:49.710247
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:35:53.909660
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert isinstance(a._load_collections, FieldAttribute)
    assert isinstance(a._collections, FieldAttribute)
    assert a.collections is None
    assert a.collections is None


# Generated at 2022-06-22 11:37:54.930683
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    ds = dict(
        collections=['my_collection'],
    )
    _collections = CollectionSearch()
    _collections._collections = ['my_collection']
    _collections._loader = loader
    _collections._load_collections('collections', ds)
    assert _collections._collections == ['my_collection']

# Generated at 2022-06-22 11:37:59.286347
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test the constructor of class CollectionSearch
    # Test the constructor with different input parameters to test the
    # functionality of class CollectionSearch's constructor.
    c1 = CollectionSearch()
    c2 = CollectionSearch(collections=["ansible_collections.test_namespace.test_collection"])
    c3 = CollectionSearch(collections="ansible_collections.test_namespace.test_collection")

# Generated at 2022-06-22 11:38:04.253824
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default == _ensure_default_collection
    assert collection_search._collections.static
    assert collection_search._collections.always_post_validate
    assert collection_search._collections.priority == 100
    assert collection_search._collections.isa == 'list'
    assert collection_search._collections.listof == string_types

# Generated at 2022-06-22 11:38:12.201984
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import json

    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible_collections.ansible.builtin', 'ansible.builtin', 'ansible.legacy']

    # Test if _load_collections() method works correctly
    # Test case_1: input is not empty
    test_collections = ["test-collections"]
    assert collection_search._load_collections(None, test_collections) == ['test-collections', 'ansible_collections.ansible.builtin', 'ansible.builtin', 'ansible.legacy']

    # Test case_2: input is empty
    test_collections = []
    assert collection_search._load_collections(None, test_collections) == None

    # Test if _load_collections() method works correctly when input is from

# Generated at 2022-06-22 11:38:13.341775
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    print(collections.collections)

# Generated at 2022-06-22 11:38:14.812602
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()
    assert cs._collections == [None]


# Generated at 2022-06-22 11:38:17.570490
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections(None, None) is None

# Generated at 2022-06-22 11:38:19.407713
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:38:21.753787
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default == ["ansible_collections.my_ns.my_coll"]

# Generated at 2022-06-22 11:38:32.852530
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import include
    from ansible.playbook.block import role
    from ansible.playbook.block import task
    from ansible.playbook.role import RoleInclude

    b = Block()
    assert b._collections is None

    b = Block(collections=['foo.bar', 'baz.qux'])
    assert b._collections == ['foo.bar', 'baz.qux']

    b = Block(collections=[])
    assert b._collections == []

    class Foo(Block):
        _collections = []
        _bar = FieldAttribute(isa='str')

    foo = Foo()
    assert foo._col