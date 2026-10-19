

# Generated at 2022-06-22 11:29:50.897678
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert _ensure_default_collection(collection_list=cs._collections)

# Generated at 2022-06-22 11:29:52.937766
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_CollectionSearch = CollectionSearch()
    assert test_CollectionSearch._collections is None
    assert test_CollectionSearch.collections is None


# Generated at 2022-06-22 11:30:02.548531
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._load_collections(None, None) is None
    assert c._load_collections(None, []) is None
    assert c._load_collections(None, []) == c._load_collections(None, None)
    assert c._load_collections(None, None) == c._load_collections(None, [])
    assert c._load_collections(None, ['ansible.builtin']) is not None
    assert c._load_collections(None, ['ansible.builtin']) == c._load_collections(None, None)
    assert c._load_collections(None, None) == c._load_collections(None, ['ansible.builtin'])

# Generated at 2022-06-22 11:30:14.752723
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    c = CollectionSearch()

    # Run unit test for constructor of class CollectionSearch
    def test_constructor_CollectionSearch(c):
        assert isinstance(c, CollectionSearch)

    # Run unit test for constructor of class CollectionSearch
    test_constructor_CollectionSearch(c)

    # Set _collections
    collections = 'test'
    c._collections = collections

    # Run unit test to check setter of _collections
    def test_set_collections(c):
        assert c._collections == 'test'

    test_set_collections(c)

    # Run unit test to check getter of _collections
    def test_get_collections(c):
        assert c.collections == 'test'

    test_get_collections(c)

    # Run unit test for _load_collections method
   

# Generated at 2022-06-22 11:30:22.344963
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    # Test empty collections list
    assert cs._collections.post_validate([]) == ['ansible.builtin']

    # Add collection name to the collections list
    assert cs._collections.post_validate(['another-collection']) == ['another-collection', 'ansible.builtin']

    # Test templatable name
    assert cs._collections.post_validate(['{{foo}}']) == ['{{foo}}', 'ansible.builtin']

# Generated at 2022-06-22 11:30:27.089889
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    default_list_collections = _ensure_default_collection()
    assert isinstance(default_list_collections, list)
    assert default_list_collections == search._load_collections('collections', None)
    assert 'ansible.builtin' in search._load_collections('collections', ['ansible.builtin'])

# Generated at 2022-06-22 11:30:35.595716
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import ansible.playbook
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.template import is_template
    from ansible.utils.display import Display
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionResolver
    from ansible.utils.collection_loader._collection_finder import AnsibleRoleFinder
    from ansible.errors import AnsibleError

    current_dir = os.path.dirname(os.path.abspath(__file__))

    display = Display()
    AnsibleCollectionConfig.default_collection = 'ansible_namespace.my_collection'
    AnsibleCollectionConfig.configured = True

# Generated at 2022-06-22 11:30:36.850458
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs is not None

# Generated at 2022-06-22 11:30:45.571127
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test the normal constructor
    cs = CollectionSearch()
    assert cs._collections == ['ansible.builtin', 'ansible.legacy']

    # Test the constructor with a specific collection
    cs = CollectionSearch(collections=['test.collection'])
    assert cs._collections == ['test.collection', 'ansible.builtin', 'ansible.legacy']

    # Test the constructor with a specific collection
    cs = CollectionSearch(collections=['test.collection', 'test.two'])
    assert cs._collections == ['test.collection', 'test.two', 'ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:56.355883
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    """ Unit test for constructor of class CollectionSearch """
    from ansible_collections.ansible.builtin import builtin
    from ansible_collections.ansible.builtin.plugins.module_utils.sensu_go import collection_search
    import pprint

    # pylint: disable=unused-argument
    def _make_collection(self, collection_name, collection_paths=None, only_collections=False):
        """ replace the original function to avoid filesystem interaction """
        del self, collection_name, only_collections
        return builtin

    collection_search.CollectionSearch.make_collection = _make_collection

    cs = collection_search.CollectionSearch()
    pprint.pprint(cs.collections)
    assert cs.get_validated_value('collections', cs._collections, None, None)

# Generated at 2022-06-22 11:31:01.460519
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    display.display("CollectionSearch loaded")

# Generated at 2022-06-22 11:31:05.421170
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    d = {'collections': ['my.ns.collection']}
    c._load_collections('collections', d)
    assert c.collections == ['my.ns.collection', 'ansible.legacy']


# Generated at 2022-06-22 11:31:06.367495
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs is not None

# Generated at 2022-06-22 11:31:10.316192
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    __collections = _ensure_default_collection()
    collection_search = CollectionSearch(collections = __collections)
    if collection_search._collections == __collections:
        print("Successfully created instance of Collection Search")
    else:
        print("Instance of Collection Search not created")

test_CollectionSearch()

# Generated at 2022-06-22 11:31:12.198031
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection

# Generated at 2022-06-22 11:31:17.419757
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Check that collections can be set
    c = CollectionSearch()
    c.collections = ['test_collection']
    assert c.collections == ['test_collection']

    # Check that collections can be set in the constructor
    c = CollectionSearch(collections=['test_collection'])
    assert c.collections == ['test_collection']


# Generated at 2022-06-22 11:31:22.844837
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Setup
    from ansible.playbook.base import Base

    class TestCollectionSearch(Base, CollectionSearch):
        pass

    test_collection_search = TestCollectionSearch()

    # Exercise
    test_collection_search.validate()

    # Verify
    assert test_collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:24.381634
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    with pytest.raises(ValueError):
        CollectionSearch('collections', [])

# Generated at 2022-06-22 11:31:28.014132
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == cs._collections
    assert cs.collections is not None
    # TODO: Add assert for _load_collections
    print("Test CollectionSearch: OK")


# Generated at 2022-06-22 11:31:30.366139
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default() == _ensure_default_collection(collection_list=None)

# Generated at 2022-06-22 11:31:37.584523
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert not CollectionSearch().collections

# Generated at 2022-06-22 11:31:39.803199
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:31:41.340728
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.construct()['collections'] is not None

# Generated at 2022-06-22 11:31:46.743397
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    myCollectionSearch = CollectionSearch()
    assert(myCollectionSearch._load_collections(None, []) == None)
    assert(myCollectionSearch._load_collections(None, []) == None)
    assert(myCollectionSearch._load_collections(None, None) == None)
    assert(myCollectionSearch._load_collections(None, ['some', 'collection']) == ['some', 'collection'])

# Generated at 2022-06-22 11:31:53.831317
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    temp = CollectionSearch()
    assert temp._load_collections(attr=None, ds=["ansible_test.test.test_collections"]) == \
           ["ansible_test.test.test_collections", "ansible.builtin", "ansible.legacy"]
    assert temp._load_collections(attr=None, ds=None) == \
           ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:31:58.854135
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class test_cs(CollectionSearch):
        # static attribute will be assigned to the class only once
        static_attr = 10

    # Construct an instance of test_cs
    test = test_cs()

    # Check if the static attribute is initialized with the correct value
    assert test.static_attr == 10

# Generated at 2022-06-22 11:32:00.942485
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections._value is None
    assert cs.collections is None

# Generated at 2022-06-22 11:32:02.590317
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections is None
    assert CollectionSearch().collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:04.393262
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search._load_collections('collections', ['ns'])

# Generated at 2022-06-22 11:32:06.470772
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:21.505163
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert len(search.collections) >= 1
    assert search.collections[0] == 'ansible.builtin'

# Generated at 2022-06-22 11:32:23.152141
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections is not None

# Generated at 2022-06-22 11:32:24.815050
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    result = collectionSearch._collections
    assert result == _ensure_default_collection()

# Generated at 2022-06-22 11:32:34.149492
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class C(object):
        pass

    class Inventory(object):
        pass

    i = Inventory()
    i.__class__ = C
    i.play = dict()
    c = CollectionSearch()

    assert c.collections == _ensure_default_collection()
    assert c._load_collections('collections', i) == _ensure_default_collection()

    # Test with no default collection
    AnsibleCollectionConfig.default_collection = None

    assert c.collections == []
    assert c._load_collections('collections', i) == None

    AnsibleCollectionConfig.default_collection = 'test.test'

    c.collections = 'test.test'
    ds = dict()
    ds['play'] = dict()
    ds['play']['collections'] = 'test.test'


# Generated at 2022-06-22 11:32:36.426753
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == _ensure_default_collection(collection_list=None)

# Generated at 2022-06-22 11:32:39.236987
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # c._load_collections(None, 'ansible.builtin')
    assert c._load_collections(None, "ansible.builtin")

# Generated at 2022-06-22 11:32:42.621135
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_class = CollectionSearch()
    list = test_class._load_collections('_collections', [])
    assert list[0] == 'ansible.builtin'
    assert len(list) == 1

# Generated at 2022-06-22 11:32:48.718888
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role.definition import RoleDefinition

    test_collection_search = CollectionSearch()
    test_role = RoleDefinition()
    test_collections = _ensure_default_collection()

    # Test that _ensure_default_collection adds the correct value to test_collection_search._collections
    assert test_collection_search._collections == None
    assert test_collections == test_collection_search._collections

# Generated at 2022-06-22 11:32:51.975633
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # test if CollectionSearch() can create an instance of class CollectionSearch
    collectionsearch = CollectionSearch(collections=['some_collection', 'another_collection'])
    assert len(collectionsearch.collections), 2

# Generated at 2022-06-22 11:32:57.173335
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost, '])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-22 11:33:24.716259
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj is not None


# Generated at 2022-06-22 11:33:31.794276
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Testing _collections instantiation
    search = CollectionSearch()

    assert search._collections.default == _ensure_default_collection
    assert search._collections.priority == 100
    assert search._collections.needs_post_validate()
    assert search._collections.desc == 'One or more collections to use'
    assert search._collections.aliases == ['collection', 'collections']
    assert search._collections.always_post_validate

    assert search._collections.type == 'list'
    assert search._collections.static
    assert search._collections._listof == string_types

    # Test _collections instantiation with specific collection list
    def my_collection_list(x=None):
        return [x]
    search._collections.default = my_collection_list
    assert search._collections.default

# Generated at 2022-06-22 11:33:36.288810
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    print(obj.__dict__)
    obj.post_validate(None, 'build_collection')
    print(obj.__dict__)
    obj.post_validate(None, 'collections')
    print(obj.__dict__)

# Generated at 2022-06-22 11:33:44.010388
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    collection_list = ['linux.istsre', 'apache.a2site']
    ans = test._ensure_default_collection(collection_list)
    print(ans)

    _test = CollectionSearch()
    _test._collections = collection_list
    print(_test._collections)

    test_object = _test._load_collections('_collections', collection_list)
    print('All collections names: ', test_object)
    print(type(test_object))

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:33:47.130263
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    list_collection = ['collection1', 'collection2']
    collection = CollectionSearch(_collections=list_collection)
    assert collection._collections == list_collection
    assert collection.collections == list_collection

# Generated at 2022-06-22 11:33:54.743299
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    if 'ansible.builtin' != obj._collections[0]:
        raise AssertionError('ansible.builtin not default collection for CollectionSearch')

    obj = CollectionSearch(collections='nti310.nti310infra')
    if 'nti310.nti310infra' != obj._collections[0]:
        raise AssertionError('nti310.nti310infra not collection for CollectionSearch')

if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:33:57.637372
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_instance = CollectionSearch()
    # This test is for verifying attribute '_collections'
    assert test_instance._collections is not None

# Generated at 2022-06-22 11:34:07.403155
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    display = Display()
    # display = Display(verbosity=display.VERBOSITY_DEBUG)
    display.columns = 80
    collection_search = CollectionSearch()
    try:
        display.verbosity = -1
        collection_search._load_collections(None, None)
        # assert False
    except SystemExit:
        pass

    display.verbosity = 3
    display.banner("test_CollectionSearch case 1, attr: None, ds: None")
    result = collection_search._load_collections(None, None)
    assert result

    display.banner("test_CollectionSearch case 2, attr: None, ds: 'test'")
    result = collection_search._load_collections(None, 'test')
    assert result

# Generated at 2022-06-22 11:34:09.605269
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c=CollectionSearch()
    assert c._collections is _ensure_default_collection



# Generated at 2022-06-22 11:34:21.006404
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Testcase1 (default collection)
    cs = CollectionSearch()
    assert cs._collections['static'] == True
    assert cs._collections['priority'] == 100
    assert cs._collections['isa'] == 'list'
    assert cs._collections['listof'] == string_types
    assert cs._collections['always_post_validate'] == True
    assert cs._collections['default'] == _ensure_default_collection
    assert cs._collections['name'] == 'collections'
    assert cs._collections['value'] == _ensure_default_collection
    assert cs.collections == _ensure_default_collection

    # Testcase2 (custom collection)
    cs = CollectionSearch()

# Generated at 2022-06-22 11:35:16.272894
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Testing the constructor of CollectionSearch
    search = CollectionSearch()
    assert search._collections._value == _ensure_default_collection()

# Generated at 2022-06-22 11:35:25.528638
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.task.memorized import MemorizedTask
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import TaskTerms
    from ansible.playbook.play import Play

    assert issubclass(RoleDefinition, CollectionSearch)
    assert issubclass(RoleInclude, CollectionSearch)
    assert issubclass(MemorizedTask, CollectionSearch)
    assert issubclass(Task, CollectionSearch)
    assert issubclass(Block, CollectionSearch)
    assert issub

# Generated at 2022-06-22 11:35:26.608080
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert isinstance(cs, CollectionSearch)

# Generated at 2022-06-22 11:35:38.429891
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class MyObj(CollectionSearch):
        pass

    obj = MyObj()

    # first test that _collections in the object is a list of strings
    assert isinstance(obj._collections, list)
    for item in obj._collections:
        assert isinstance(item, string_types)

    # second test that collections in the object is a list of strings
    assert isinstance(obj.collections, list)
    for item in obj.collections:
        assert isinstance(item, string_types)

    # third test that collections is not empty
    assert obj.collections
    
    # fourth test that 'ansible.builtin' or 'ansible.legacy' is in collections
    assert 'ansible.builtin' in obj.collections or 'ansible.legacy' in obj.collections

# Generated at 2022-06-22 11:35:42.050524
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test: Constructor of class CollectionSearch
    test = CollectionSearch()
    assert test != None


# Generated at 2022-06-22 11:35:43.763834
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.static == True

# Generated at 2022-06-22 11:35:48.543496
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Initialize CollectionSearch
    test_cols = CollectionSearch()

    # Verify the collections list
    result = test_cols._collections
    assert result == _ensure_default_collection()

    # Verify the load_collections method
    result = test_cols._load_collections('collections', test_cols._collections)
    assert result == _ensure_default_collection()

# Generated at 2022-06-22 11:35:50.198006
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    assert collectionSearch._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:35:54.109989
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Given
    collection_search = CollectionSearch()

    # When
    result = collection_search.collections

    # Then
    assert result == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:35:55.492797
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections._get_default() == _ensure_default_collection()

# Generated at 2022-06-22 11:37:50.325740
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:37:53.223325
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin', 'ansible.ansible_collections.ns.foo', 'ansible.legacy']

# Generated at 2022-06-22 11:37:58.433071
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from collections import namedtuple
    from ansible.playbook.base import Base
    item = namedtuple('item', ['collections'])
    c = CollectionSearch()
    ds = item(collections=[])
    assert _ensure_default_collection(ds.collections) == c._collections

# Generated at 2022-06-22 11:38:09.709700
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_list = CollectionSearch()
    collection_list._load_collections('collections', None)
    assert collection_list._collections

    display.deprecations = {
        'deprecated_message': None,
        'version': None,
        'removed_in': None,
        'collection': None
    }
    assert display.deprecations['deprecated_message']

    display.deprecations = {
        'deprecated_message': "",
        'version': "",
        'removed_in': "",
        'collection': ""
    }
    assert display.deprecations['deprecated_message']

    display.deprecations = {
        'deprecated_message': "",
        'version': "",
        'removed_in': "",
        'collection': ""
    }

# Generated at 2022-06-22 11:38:10.787344
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search =  CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:38:16.374509
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create a test CollectionSearch object
    my_collection_search = CollectionSearch()

    # Create a test data sources
    my_ds = [
        'ansible_collections.ns1.namespace1.collection1',
    ]

    # Update the data sources
    my_collection_search._load_collections(None, my_ds)

    # Check to see if the list actually got loaded
    assert(my_ds == my_collection_search._collections)

    # Check to see if the default collection got loaded
    assert(my_ds[0] == my_collection_search._collections[1])

# Generated at 2022-06-22 11:38:17.587145
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch._load_collections(None, None)
    assert collections is not None

# Generated at 2022-06-22 11:38:19.408614
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert test_obj.collections is None

# Unit test to test static method _load_collections

# Generated at 2022-06-22 11:38:21.271427
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_object = CollectionSearch()
    assert test_object._collections is not None

# Generated at 2022-06-22 11:38:30.686208
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert _ensure_default_collection() == None
    assert _ensure_default_collection(collection_list=['one']) == ['one']
    assert _ensure_default_collection(collection_list=['ansible.builtin']) == ['ansible.builtin']
    assert _ensure_default_collection(collection_list=['ansible.builtin', 'two']) == ['ansible.builtin', 'two']
    assert _ensure_default_collection(collection_list=['one', 'two', 'ansible.builtin']) == ['one', 'two', 'ansible.builtin']

if __name__ == '__main__':
    test_CollectionSearch()