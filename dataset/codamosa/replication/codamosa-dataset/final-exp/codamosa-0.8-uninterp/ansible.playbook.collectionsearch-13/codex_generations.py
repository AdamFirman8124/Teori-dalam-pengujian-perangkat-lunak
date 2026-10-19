

# Generated at 2022-06-22 11:29:49.828001
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    attr = []
    ds = []
    CollectionSearch._load_collections(attr, ds)

# Generated at 2022-06-22 11:29:52.158455
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.name is None
    assert collection_search.collections is not None

# Generated at 2022-06-22 11:29:53.816467
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:29:56.667904
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch()._collections, list)
    assert 'ansible.builtin' in CollectionSearch()._collections
    assert 'ansible.legacy' in CollectionSearch()._collections

# Generated at 2022-06-22 11:29:59.341126
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs1 = CollectionSearch()
    cs2 = CollectionSearch()
    assert cs1._collections == cs2._collections
    assert cs1._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:11.663156
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test passing one valid coll collection
    test_coll_search = CollectionSearch(collections=['awx.awx'])
    assert test_coll_search._collections == ['awx.awx']

    # test passing a None collection list
    test_coll_search = CollectionSearch(collections=None)
    assert test_coll_search._collections == ['ansible.builtin']

    # test passing a valid collection list
    test_coll_search = CollectionSearch(collections=['ansible.builtin', 'awx.awx'])
    assert test_coll_search._collections == ['ansible.builtin', 'awx.awx']

    # test passing coll collection list with an invalid coll collection name

# Generated at 2022-06-22 11:30:13.537492
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections

# Generated at 2022-06-22 11:30:16.195781
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    collection_search = CollectionSearch()
    collections = collection_search._load_collections('collections', ['Test'])
    assert collections == ['Test', 'ansible.builtin']

# Generated at 2022-06-22 11:30:17.532466
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:28.631940
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import collections


# Generated at 2022-06-22 11:30:41.576268
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    sub = CollectionSearch()
    sub._collections = ['ansible.builtin', 'ansible.terminal', 'ansible.legacy']
    assert sub._load_collections(None, None) == ['ansible.builtin', 'ansible.terminal', 'ansible.legacy']

    sub = CollectionSearch()
    sub._collections = ['ansible.builtin', 'ansible.legacy']
    assert sub._load_collections(None, None) == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:44.352585
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test._collections.default() == test._ensure_default_collection()
    assert test._collections.default() == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:50.018170
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Assert _collections is set properly
    assert CollectionSearch()._collections == _ensure_default_collection()
    default_collections = _ensure_default_collection()
    assert CollectionSearch(collections=default_collections)._collections == default_collections
    assert CollectionSearch(collections=None)._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:53.009216
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    #Create instance of Class CollectionSearch
    cs = CollectionSearch()
    cs._collections = 'galaxy.role.collections'
    assert cs._collections == 'galaxy.role.collections'

# Generated at 2022-06-22 11:30:56.461392
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert isinstance(search, CollectionSearch)
    assert search.collections is None
    assert search.get_validated_value('collections', search.collections, ['abc'], None) == ['abc']
    assert isinstance(search.get_validated_value('collections', search.collections, None, None), list)

# Generated at 2022-06-22 11:30:58.662548
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == ['ansible.builtin', 'ansible.legacy']
    assert cs.collections is None

# Generated at 2022-06-22 11:31:02.205201
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    ansible_collection = 'ansible.builtin'
    obj.collections = [ansible_collection]
    assert obj.collections == [ansible_collection]

# Generated at 2022-06-22 11:31:03.303322
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    result = CollectionSearch()
    assert result is not None

# Generated at 2022-06-22 11:31:05.638053
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Verify the constructor declaration of class CollectionSearch
    obj = CollectionSearch()
    assert obj
    assert isinstance(obj, CollectionSearch)

# Generated at 2022-06-22 11:31:13.207234
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.config.manager import ConfigManager
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.task.include import IncludeTask
    from ansible.playbook.task.action import ActionTask

    # test for default value of collections
    m = CollectionSearch()
    x = m._load_collections('collections', None)
    assert x == _ensure_default_collection()

    # test for collections with a non empty list of collections
    y = ['ansible_collections.foo.bar']
    z = m._load_collections('collections', y)
    assert z == _ensure_default_collection(collection_list=y)

    # test for collections with an empty list


# Generated at 2022-06-22 11:31:23.290301
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    #assert(c._collections.default == _ensure_default_collection())
    assert(c._collections.default == None)
    c._collections.default = ['collection1', 'collection2', 'collection3']
    ds = None
    c._load_collections(None, ds)

# Generated at 2022-06-22 11:31:24.382222
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()


# Generated at 2022-06-22 11:31:27.230335
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    tcs = CollectionSearch()
    print("Instance of CollectionSearch is: ")
    print(tcs)

if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:28.735986
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections == ['ansible.posix']

# Generated at 2022-06-22 11:31:35.109709
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class Base(object):
        def __init__(self, collections=None):
            self.collections = collections

    class TestObject(Base, CollectionSearch):
        pass

    obj = TestObject(None)
    assert obj.collections == _ensure_default_collection()
    assert type(obj.collections) == list
    assert obj._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:31:35.672862
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

# Generated at 2022-06-22 11:31:38.872385
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ansible_collections = ['ansible.builtin']
    assert ansible_collections == CollectionSearch()._load_collections(None, None)
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:39.912800
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    a._load_collections("", {})

# Generated at 2022-06-22 11:31:45.592102
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    d = dict(collections=['ansible_namespace.foo_collection'])
    obj = CollectionSearch(d)
    assert obj.collections == _ensure_default_collection([d['collections'][0]])
    d = dict(collections=['foo_namespace.foo_collection'])
    obj = CollectionSearch(d)
    assert obj.collections == _ensure_default_collection([d['collections'][0]])
    d = dict()
    obj = CollectionSearch(d)
    assert obj.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:54.707329
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._load_collections(None,["ansible"]) ==  ['ansible']
    assert collection_search._load_collections(None,["ansible"]) ==  ['ansible']
    assert collection_search._load_collections(None,["ansible.builtin"]) ==  ['ansible.builtin']
    assert collection_search._load_collections(None,["ansible.collection"]) ==  ['ansible.collection']
    assert collection_search._load_collections(None,["ansible.legacy"]) ==  ['ansible.legacy']
    assert collection_search._load_collections(None,["ansible.module_utils"]) ==  ['ansible.module_utils']

# Generated at 2022-06-22 11:32:16.106536
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import unittest
    from test.unit.playbook.test_loader import LoaderModuleMock

    co = LoaderModuleMock()
    co_instance = co.get_collection_loader()

    ansible_base = LoaderModuleMock()
    ansible_base_instance = ansible_base.get_ansible_base()
    t = CollectionSearch()
    assert t._collections is not None
    t._load_collections(None, None)



# Generated at 2022-06-22 11:32:17.154636
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs

# Generated at 2022-06-22 11:32:21.592770
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test a good value
    cs1 = CollectionSearch()
    cs2 = CollectionSearch()
    assert cs1._collections == cs2._collections

    # Test setting a bad value for _collections
    cs1 = CollectionSearch()
    cs1._collections = 6
    assert cs1._collections == 6

# Generated at 2022-06-22 11:32:28.609442
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test Case 1: 
    cs1 = CollectionSearch()
    assert _ensure_default_collection(collection_list=None) == cs1.collections
    
    # Test Case 2:
    collection_list = [
        "nsmbl.hoge",
        "nsmbl.fuga",
        "nsmbl.piyo"
    ]
    cs2 = CollectionSearch()
    cs2.collections = collection_list
    assert _ensure_default_collection(collection_list) == cs2.collections

# Generated at 2022-06-22 11:32:37.283870
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_loader(loader)
    variable_manager.extra_vars = {'ansible_collections': [ 'foo.collection' ] }

    obj = CollectionSearch()
    obj.variable_manager = variable_manager
    obj._collections = '{{ ansible_collections }}'
    ds = {}

    # no collection list is set, so default list should be used
    collection_list = obj._load_collections(None, ds)
    assert collection_list == ['ansible.builtin', 'ansible.legacy', 'foo.collection']

    # empty collection list is set, so no collection list should be used

# Generated at 2022-06-22 11:32:38.321082
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections is None # since no collections specified in constructor

# Generated at 2022-06-22 11:32:43.843342
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    # Pre-validate without passing collection list
    assert cs._collections.post_validate(cs, 'collections', None, None) == _ensure_default_collection()

    # Pre-validate while passing collection list
    assert cs._collections.post_validate(cs, 'collections', None, None) == _ensure_default_collection(['ansible.posix'])

# Generated at 2022-06-22 11:32:53.138104
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.errors import AnsibleError
    from ansible.utils.collection_loader._collection_finder import CollectionFinder

    obj = CollectionSearch()
    assert obj != None

    # Test that we can pass a single collection to obj._load_collections
    collections = ['my_collection']
    actual_result = obj._load_collections('collections', collections)
    expected_result = collections
    assert actual_result == expected_result, \
        "Actual result: %s, Expected result: %s" % (actual_result, expected_result)

    # Test that we can pass an empty list to obj._load_collections
    collections = []
    actual_result = obj._load_collections

# Generated at 2022-06-22 11:32:55.250644
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    d = {'collections': ['my.collection']}
    ans = CollectionSearch(ds=d)

# Generated at 2022-06-22 11:32:57.119868
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # TODO: create unit test for constructor of class CollectionSearch
    assert False # TODO: implement your test here

# Generated at 2022-06-22 11:33:25.708506
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:34.750561
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections['default'] == _ensure_default_collection()
    assert cs._collections['default'] == _ensure_default_collection(collection_list=None)
    assert cs._collections['default'] == _ensure_default_collection(collection_list=['a'])
    assert cs._collections['default'] == _ensure_default_collection(collection_list=['b', 'c'])
    assert cs._collections['default'] == _ensure_default_collection(collection_list=['c', 'b'])
    assert cs._collections['default'] == _ensure_default_collection(collection_list=['ansible.builtin'])
    assert cs._collections['default'] == _ensure_default_collection(collection_list=['ansible.legacy'])

# Generated at 2022-06-22 11:33:42.139321
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections('collections', 'ansible.builtin') == ['ansible.builtin']
    assert cs._load_collections('collections', ['ansible.builtin']) == ['ansible.builtin']
    assert isinstance(cs._load_collections('collections', None), list)
    assert cs._load_collections('collections', ['ansible.builtin', 'my.collection']) == ['ansible.builtin', 'my.collection']
    assert cs._load_collections('collections', ['my.collection', 'ansible.builtin']) == ['ansible.builtin', 'my.collection']
    assert cs._load_collections('collections', ['my.collection']) == ['ansible.legacy', 'my.collection']

# Generated at 2022-06-22 11:33:43.251258
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test



# Generated at 2022-06-22 11:33:44.790373
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    assert collectionSearch._load_collections is not None

# Generated at 2022-06-22 11:33:46.665718
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    result = CollectionSearch()
    assert result
    assert hasattr(result, '_collections')

# Generated at 2022-06-22 11:33:52.198482
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ansible_collections = ['ansible.builtin', 'ansible.legacy']
    collection_search = CollectionSearch()
    assert collection_search.get_validated_value('collections', _ensure_default_collection(), None, None) == ansible_collections
    assert collection_search._load_collections('collections', None) == ansible_collections

# Generated at 2022-06-22 11:33:53.260631
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

# Generated at 2022-06-22 11:33:55.085611
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    assert collections.collections == _ensure_default_collection(None)

# Generated at 2022-06-22 11:33:57.688545
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    my_col_search = CollectionSearch()
    assert my_col_search._collections is None

# Generated at 2022-06-22 11:34:56.395961
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print('hasattr(CollectionSearch,"_collections")=', hasattr(CollectionSearch,"_collections"))
    print('hasattr(CollectionSearch,"_load_collections")=', hasattr(CollectionSearch,"_load_collections"))

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:34:58.916000
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Check for Empty object
    test_object = CollectionSearch()
    assert test_object != ""
    assert test_object != None

# Generated at 2022-06-22 11:35:03.228368
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is None
    assert cs._load_collections(None, "ansible_collections.nsb.role.some_role") == "ansible_collections.nsb.role.some_role"
    assert cs._load_collections(None, "") is None

# Generated at 2022-06-22 11:35:14.207255
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    collection_search = CollectionSearch()
    collection_search.post_validate({}, [])

    collection_search2 = CollectionSearch()
    collection_search2._collections = None
    collection_search2.post_validate({}, [])
    collection_search2.collections = ['ansible.builtin', 'ansible.foo']
    collection_search2.post_validate({}, [])

    collection_search3 = CollectionSearch()
    collections_list = ['ansible.builtin', 'ansible.foo', 'ansible.bar']
    collection_search3._collections = collections_list
    assert ['ansible.builtin', 'ansible.foo', 'ansible.bar'] == collection_search3.post_validate({}, collections_list)

    collection_search4 = CollectionSearch()
   

# Generated at 2022-06-22 11:35:16.395850
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    """
    Constructor for class CollectionSearch with argument ds
    """

    collection_search = CollectionSearch(ds)

# Generated at 2022-06-22 11:35:18.046063
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = _ensure_default_collection()
    assert collection[0] == 'ansible.builtin'

# Generated at 2022-06-22 11:35:24.223678
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert _ensure_default_collection() == ['ansible.legacy']
    assert _ensure_default_collection(['some.namespace']) == ['some.namespace', 'ansible.legacy']
    assert _ensure_default_collection(['some.namespace', 'ansible.builtin']) == ['some.namespace', 'ansible.builtin']

# Generated at 2022-06-22 11:35:28.689121
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search_obj = CollectionSearch()
    print(collection_search_obj)
    # class has no attribute '_collections'
    # print(collection_search_obj._collections)
    # class has no attribute '_load_collections'
    # print(collection_search_obj._load_collections)



# Generated at 2022-06-22 11:35:29.321014
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

# Generated at 2022-06-22 11:35:30.626463
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col = CollectionSearch()
    assert col is not None

# Generated at 2022-06-22 11:37:28.296884
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create an instance of CollectionSearch
    i1 = CollectionSearch()
    assert i1._collections is not None
    assert isinstance(i1._collections, FieldAttribute)

# Generated at 2022-06-22 11:37:29.772892
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == []

# Generated at 2022-06-22 11:37:31.537409
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    pb = CollectionSearch()
    assert pb._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:37:33.623712
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections is not None

# Generated at 2022-06-22 11:37:37.355571
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert AnsibleCollectionConfig.default_collection is None
    assert CollectionSearch().collections == ['ansible.legacy']
    assert CollectionSearch().collections is not None

# Unit test with default collection

# Generated at 2022-06-22 11:37:40.776021
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ''' Unit test for constructor of class CollectionSearch '''
    obj1 = CollectionSearch()
    # Test that the instance is created properly
    assert 'AnsibleCollectionConfig' in str(type(obj1._collections))


# Generated at 2022-06-22 11:37:53.133890
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_CollectionSearch = CollectionSearch()
    test_CollectionSearch._collections = ['ansible.kubernetes_collection']
    test_CollectionSearch._load_collections(test_CollectionSearch._collections, None)
    assert test_CollectionSearch._collections == ['ansible.kubernetes_collection']
    test_CollectionSearch._collections = []
    test_CollectionSearch._load_collections(test_CollectionSearch._collections, None)
    assert test_CollectionSearch._collections == ['ansible.builtin', 'ansible.legacy']
    test_CollectionSearch._collections = ['ansible.builtin', 'ansible.legacy']
    test_CollectionSearch._load_collections(test_CollectionSearch._collections, None)

# Generated at 2022-06-22 11:37:59.091585
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # c.collections is not initialized, it's None
    assert c.collections is None
    # test the static method _ensure_default_collection
    assert c._ensure_default_collection() == ['ansible.builtin', 'ansible.legacy']

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:38:00.329755
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert isinstance(obj, CollectionSearch)

# Generated at 2022-06-22 11:38:00.954813
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()