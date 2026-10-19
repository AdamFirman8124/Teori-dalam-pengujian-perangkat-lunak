

# Generated at 2022-06-22 11:29:47.926713
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    collection.collections = "ansible.builtin"
    assert collection.collections != None, "CollectionSearch._ensure_default_collection not working as expected"

# Generated at 2022-06-22 11:29:54.528066
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.taggable import Taggable

    class Task(CollectionSearch, RoleInclude, Taggable):
       def __init__(self, collection_list):
           self.collections = collection_list

    test_task = Task(['awx.main'])
    assert test_task.collections == ['awx.main']

    test_task = Task(['awx.main', 'ansible.builtin'])
    assert test_task.collections == ['awx.main', 'ansible.builtin']

    test_task = Task(['awx.main', 'ansible.builtin', 'ansible.legacy'])

# Generated at 2022-06-22 11:29:55.157191
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch, object)

# Generated at 2022-06-22 11:30:00.346375
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collection_search = CollectionSearch()
    test_collection_search._collections = []
    assert test_collection_search._collections == []
    assert test_collection_search._load_collections(attr='collections', ds=[]) == []
    assert test_collection_search._load_collections(attr='collections', ds=None) is None
    assert test_collection_search._load_collections(attr='collections', ds=['ansible.builtin']) == ['ansible.builtin']

    test_collection_search._collections = None
    assert test_collection_search._load_collections(attr='collections', ds=['ansible.builtin']) == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:03.911665
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert not hasattr(collection_search, 'collections')
    assert not hasattr(collection_search, '_collections')



# Generated at 2022-06-22 11:30:10.801180
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # test for class attributes
    assert isinstance(cs._collections, FieldAttribute)

    # test for class functions
    assert isinstance(cs._load_collections, type(lambda: None))

    # test for class functions _load_collections
    test_list = ['ansible.zadt']
    cs._collections = test_list
    assert cs._load_collections(cs._collections, None) == test_list

# Generated at 2022-06-22 11:30:15.581684
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = {'collections':['ansible_namespace.name']}
    cs = CollectionSearch()
    print(cs._collections)
    print(cs._load_collections(cs._collections, ds))

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:30:17.717395
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import doctest
    my_test = CollectionSearch()
    #my_test._load_collections("collections", None)
    doctest.testmod()

# Generated at 2022-06-22 11:30:20.416655
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    variable_manager = VariableManager()

    result = CollectionSearch()

# Generated at 2022-06-22 11:30:22.488695
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    attr = ""
    ds = ""
    collectionSearch._load_collections(attr, ds)

# Generated at 2022-06-22 11:30:33.889926
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible.builtin', 'ansible.legacy']



# Generated at 2022-06-22 11:30:35.225109
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    temp = CollectionSearch()


# Generated at 2022-06-22 11:30:38.134935
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._load_collections(None, None) == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:44.392337
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    try:
        # Attempt to instantiate class CollectionSearch with an explicitly set
        # field 'collections' in the dictionary of fields
        obj = CollectionSearch(collections=["collections_test"])
        # Test that the 'collections' field is set to
        # ["collection_test", "ansible.builtin"]
        assert obj.collections == ["collections_test", "ansible.builtin"]
    except:
        # Test fails if constructor fails
        assert False

# Generated at 2022-06-22 11:30:49.591808
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # pylint: disable=unused-argument
    display = Display()

    class TestCollectionSearch(CollectionSearch):

        def __init__(self, display=None):
            super(TestCollectionSearch, self).__init__(display)
    # Check constructor
    assert isinstance(TestCollectionSearch(display), TestCollectionSearch)



# Generated at 2022-06-22 11:30:51.432894
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections is None



# Generated at 2022-06-22 11:30:54.004084
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create an instance of class CollectionSearch
    collection_search = CollectionSearch()
    assert collection_search.collections == ["ansible.builtin", "ansible.legacy"]

# Generated at 2022-06-22 11:30:56.455732
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    _collections_instance = CollectionSearch()
    assert _collections_instance

    assert _collections_instance._collections is None

# Generated at 2022-06-22 11:31:01.899505
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    tester = CollectionSearch()
    assert tester._collections == ['ansible.builtin', 'ansible.legacy']
    tester._collections = ['test.test']
    assert tester._collections  == ['test.test']
    assert tester._load_collections(tester._collections ,tester._collections) == ['test.test']

# Generated at 2022-06-22 11:31:11.808621
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import os
    import tempfile

    COLLECTION_PATH = tempfile.mkdtemp()

    # you can use ansible-galaxy collection init as a template for collections
    # subdirectories.
    # ansible-galaxy collection init will create a collection directory structure with
    # the following contents:
    #
    # <namespace>-<collection>/
    #   docs/
    #   galaxy.yml
    #   license
    #   plugin_type/
    #     plugin_type/
    #       action/
    #       callback/
    #       connection/
    #       filter/
    #       inventory/
    #       lookup/
    #       module_utils/
    #       modules/
    #       test/
    #       vars/
    #       module_utils/
    #       roles/

# Generated at 2022-06-22 11:31:24.219614
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search.__dict__ = dict()
    collection_search.__dict__['_collections'] = []

    _load_collections = collection_search._load_collections(None, None)
    print( _load_collections )


if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:26.654895
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:31:27.280879
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:31:32.799842
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections is not None, '_collections was not set'
    assert obj.collections is not None, 'collections was not set'
    assert isinstance(obj._collections, object), '_collections is not an object'
    assert isinstance(obj.collections, list), 'collections is not a list'

# test _ensure_default_collection() function

# Generated at 2022-06-22 11:31:34.974085
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_name = 'ansible.builtin'
    collections = CollectionSearch()
    collections.collections = collection_name

# Generated at 2022-06-22 11:31:37.245319
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    collection_search1 = CollectionSearch()
    assert collection_search1 is not None
    assert collection_search1._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:31:39.912853
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # pylint: disable=protected-access
    # pylint: disable=no-member
    collection_search = CollectionSearch()
    assert collection_search._collections == collection_search._load_collections(None, [])

# Generated at 2022-06-22 11:31:45.836727
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Initialize a DataLoader object for loading playbooks
    # and templates from file system, and a variable manager
    loader = DataLoader()
    variable_manager = VariableManager()

    # Create a CollectionSearch object
    cs = CollectionSearch()

    # Initialize it with a dictionary
    ds = {'collections': ['acme.somelib', 'acme.anotherlib']}
    cs.post_validate(ds, False)
    cs.preprocess_data(ds)
    cs._load_collections('collections', ds)

    assert ds['collections'] == ['acme.somelib', 'acme.anotherlib']

# Generated at 2022-06-22 11:31:48.916941
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    #The configuration variables are explained in `docs/dev_guide/collections.rst`
    coll1 = CollectionSearch()
    coll2 = CollectionSearch()

    assert(coll1.collections == coll2.collections)

# Generated at 2022-06-22 11:31:53.083360
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    myTest = CollectionSearch()
    myTest._collections.post_validate()
    # the constructor should set collections to ansible.builtin
    assert myTest.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:32:08.261923
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections._static

# Generated at 2022-06-22 11:32:09.156178
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    pass

# Generated at 2022-06-22 11:32:15.482382
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert len(search._collections) == 1
    # Test for _load_collections
    assert search._load_collections(search._collections, ['all']) is None
    assert search._load_collections(search._collections, []) is None
    assert search._load_collections(search._collections, None) is None

# Generated at 2022-06-22 11:32:26.048817
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    def _ensure_default_collection(collection_list=None):
        default_collection = AnsibleCollectionConfig.default_collection

        # Will be None when used as the default
        if collection_list is None:
            collection_list = []

        # FIXME: exclude role tasks?
        if default_collection and default_collection not in collection_list:
            collection_list.insert(0, default_collection)

        # if there's something in the list, ensure that builtin or legacy is always there too
        if collection_list and 'ansible.builtin' not in collection_list and 'ansible.legacy' not in collection_list:
            collection_list.append('ansible.legacy')

        return collection_list

    a = CollectionSearch()

# Generated at 2022-06-22 11:32:27.127822
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
  assert CollectionSearch.collections.default() == []

# Generated at 2022-06-22 11:32:28.255043
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    res = CollectionSearch()
    assert res != None

# Generated at 2022-06-22 11:32:29.123639
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search=CollectionSearch()

# Generated at 2022-06-22 11:32:37.652816
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ac = AnsibleCollectionConfig()
    ac.default_collection = 'ansible.builtin'

    x = CollectionSearch()
    assert x.collections == ['ansible.builtin']
    assert x.task_vars == {}

    x.initialize_collections()
    assert x.collections == ['ansible.builtin']
    assert x.task_vars == {}

    ac.default_collection = 'ansible.builtin'
    x = CollectionSearch(collections=['ansible.builtin'])
    assert x.collections == ['ansible.builtin']
    assert x.task_vars == {}

    ac.default_collection = 'ansible.builtin'
    x = CollectionSearch(collections=['ansible.builtin', 'ansible.baoyu'])
    assert x.collections

# Generated at 2022-06-22 11:32:44.384450
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    # Check the _load_collections function
    # Test 1: raise error when ds is not a list
    ds = 'test'
    try:
        cs._load_collections(None, ds)
        assert False
    except:
        assert True

    # Test 2: Test with a list
    ds = ['test1', 'test2']
    assert cs._load_collections(None, ds) == ds

# Generated at 2022-06-22 11:32:45.409849
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()


# Generated at 2022-06-22 11:33:01.082249
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col = CollectionSearch()
    assert col.collections == 'ansible.legacy'

# Generated at 2022-06-22 11:33:01.971551
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections

# Generated at 2022-06-22 11:33:03.941666
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    print("Unit test for constructor of class CollectionSearch")
    assert collection_search != None

# Generated at 2022-06-22 11:33:06.708956
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert test_obj is not None
    assert test_obj.collection_list == ['ansible_collections.my_namespace.my_collection']

# Generated at 2022-06-22 11:33:12.969880
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import copy
    import os
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    from collections import namedtuple
    display = Display()
    vars_dict = {'test': 'default'}
    play_context = PlayContext()
    play_context.become = None
    play_context.become_user = None
    play_context.become_method = None
    play_context.become_ask_pass = False
    play_context.become_flags = []
    play_context.verbosity = 0
    play_context.connection = 'local'
    play_context.network_os = None
    play_context.remote_addr = None
    play_context.port = None
    play_context.remote_user = None
    play_context

# Generated at 2022-06-22 11:33:17.344001
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    # assert(a._collections == 'ansible.builtin')
    assert (len(a._collections) == 1)
    assert (a._collections[0] == 'ansible.builtin')
    print("test_CollectionSearch succeeded")


# Generated at 2022-06-22 11:33:20.372449
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    x = CollectionSearch()

    assert x._collections.default == _ensure_default_collection
    assert x._collections.name == 'collections'



# Generated at 2022-06-22 11:33:25.720205
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.collections = ['ansible.builtin', 'ansible.poshlib']
    assert cs.collections == ['ansible.builtin', 'ansible.poshlib']
    cs.collections = []
    assert cs.collections == ['ansible.builtin']



# Generated at 2022-06-22 11:33:29.364059
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_CollectionSearch = CollectionSearch()
    test_CollectionSearch._collections = _ensure_default_collection()
    test_CollectionSearch._load_collections('test', None)
    assert(test_CollectionSearch._collections == ['ansible.builtin', 'ansible.legacy'])

# Generated at 2022-06-22 11:33:30.848389
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    my_coll_search = CollectionSearch()
    assert isinstance(my_coll_search,CollectionSearch)

# Generated at 2022-06-22 11:34:00.284887
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collection = CollectionSearch()
    assert type(test_collection) is CollectionSearch
    assert type(test_collection._collections.default) is type(_ensure_default_collection)

# Generated at 2022-06-22 11:34:09.970400
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        def __init__(self, ds):
            super(TestCollectionSearch, self).__init__(ds)

    test = TestCollectionSearch({})
    assert test.collections == ['ansible.legacy']
    test = TestCollectionSearch({'collections': ['geerlingguy.hugo']})
    assert test.collections == ['geerlingguy.hugo', 'ansible.legacy']
    test = TestCollectionSearch({'collections': ['geerlingguy.hugo', 'geerlingguy.docker']})
    assert test.collections == ['geerlingguy.hugo', 'geerlingguy.docker', 'ansible.legacy']

# Generated at 2022-06-22 11:34:17.044484
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == ['ansible.legacy']
    assert c._collections.name == "collections"
    assert c._collections.isa == ['list']
    assert c._collections.listof == string_types
    assert c._collections.priority == 100
    assert c._collections.default() == ['ansible.legacy']
    assert c._collections.always_post_validate is True
    assert c._collections.static is True

# Generated at 2022-06-22 11:34:19.029839
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections(1, 1) == ['ansible.builtin']

# Generated at 2022-06-22 11:34:25.294607
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import ansible.playbook.task_include as ti
    from ansible.playbook.task import Task
    from ansible.playbook.role.task import Task as RoleTask
    obj = CollectionSearch()
    assert isinstance(obj, ti.RoleInclude)
    assert isinstance(obj, ti.TaskInclude)
    assert isinstance(obj, ti.BlockInclude)
    assert isinstance(obj, Task)
    assert isinstance(obj, RoleTask)

# Generated at 2022-06-22 11:34:27.725585
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch
    assert c._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:34.055319
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search._collections, FieldAttribute)
    assert collection_search._collections.isa == 'list'
    assert collection_search._collections.listof == string_types
    assert collection_search._collections.priority == 100
    assert collection_search._collections.default == _ensure_default_collection
    assert collection_search._collections.always_post_validate is True
    assert collection_search._collections.static is True

# Generated at 2022-06-22 11:34:35.693791
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:34:40.710254
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch._collections, FieldAttribute)
    assert CollectionSearch._collections.isa == 'list'
    assert isinstance(CollectionSearch._collections.listof, type)
    assert isinstance(CollectionSearch._collections.default, types.FunctionType)
    assert CollectionSearch._collections.always_post_validate is True
    assert CollectionSearch._collections.priority == 100
    assert CollectionSearch._collections.static is True

# Generated at 2022-06-22 11:34:47.404809
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        def __init__(self, *a, **kw):
            self.ds = {}
            self.ds['collections'] = ['ansible.builtin', 'my.repo']
            self._load_collections('collections', self.ds)
            assert type(self.collections) == type(self._collections.default)
            assert self.collections == ['ansible.builtin', 'my.repo']

    TestCollectionSearch()

# Generated at 2022-06-22 11:35:43.553593
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:35:48.954831
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search=CollectionSearch()
    # Test the _load_collections method
    attr=None
    ds=None
    result=search._load_collections(attr, ds)
    # Test the _ensure_default_collection function
    collection_list=['ansible_test']
    result=_ensure_default_collection(collection_list)
    collection_list=None
    result=_ensure_default_collection(collection_list)

# Generated at 2022-06-22 11:35:50.198128
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:36:01.902321
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import sys
    import ansible
    from ansible.module_utils.six import PY3
    from ansible.parsing import loader_module

    sys.path.insert(0, './test/units/library')
    if PY3:
        import collections_search_unit as test_module
    else:
        import collections_search_unit_py2 as test_module
    del sys.path[0]

    parsed = loader_module._load_module_source('collections_search_unit', './test/units/library/collections_search_unit.py')
    module_args = dict(
        collections=['my.collection'],
    )


# Generated at 2022-06-22 11:36:03.985002
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is None

# Generated at 2022-06-22 11:36:13.892683
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import sys
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role_dependency import RoleDependency
    from ansible.playbook.attribute import FieldAttribute

    assert hasattr(CollectionSearch, "_collections")
    assert CollectionSearch._collections.field_name == "collections"
    assert CollectionSearch._collections.isa == "list"
    assert CollectionSearch._collections.default == _ensure_default_collection
    assert CollectionSearch._collections.always_post_validate
    assert CollectionSearch._collections.static
    assert CollectionSearch._collections.priority == 100
    assert CollectionSearch._collections.listof == string_types

# Generated at 2022-06-22 11:36:16.199755
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    plugin = CollectionSearch()
    assert plugin._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:36:24.206114
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import RoleInclude
    role_include = RoleInclude()
    assert isinstance(role_include, RoleInclude)
    assert isinstance(role_include, CollectionSearch)
    assert role_include._collections._default == _ensure_default_collection
    assert role_include._collections.always_post_validate == True
    assert role_include._collections.static == True
    assert role_include._collections.priority == 100
    assert role_include._collections.listof == string_types
    assert role_include._collections.isa == 'list'

# Generated at 2022-06-22 11:36:28.506231
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    data = test_obj._collections.post_validate(None, None)
    # Check if default collection is set in return data.
    assert('ansible.builtin' in data or 'ansible.legacy' in data)

# Generated at 2022-06-22 11:36:30.088997
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    c.load_data()

# Generated at 2022-06-22 11:38:33.277477
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # CollectionSearch is abstract and won't be instantiated directly.
    # But since it's a mixin base class, and abstract base classes can't have
    # a __init__ method, we just instantiate a concrete class to test CollectionSearch.
    import ansible.playbook.task

    class MyTask(ansible.playbook.task.Task, CollectionSearch):
        pass

    attr = 'collections'

    # empty ds
    ds = {}
    result = MyTask._load_collections(MyTask(), attr, ds)
    assert result is None

    # ds with string values
    ds = {'collections': 'ansible.base'}
    result = MyTask._load_collections(MyTask(), attr, ds)
    assert result is not None
    assert result == ['ansible.base']

# Generated at 2022-06-22 11:38:33.981784
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionsearch = CollectionSearch()
    assert collectionsearch is not None

# Generated at 2022-06-22 11:38:34.920082
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert _ensure_default_collection()

# Generated at 2022-06-22 11:38:37.394079
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create Instance of CollectionSearch without any Attributes
    collectionSearch = CollectionSearch()

    # Test the Attributes
    assert collectionSearch._collections is None

# Generated at 2022-06-22 11:38:40.098633
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection=CollectionSearch()
    ansible_config=AnsibleCollectionConfig()
    ansible_config.set_default_collection('test_collection')
    collection._ensure_default_collection(['test_collection'])

# Generated at 2022-06-22 11:38:43.076305
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    ansible_collections = ['ansible.builtin']
    collections.collections = ['ansible.builtin']
    assert collections.collections == ansible_collections
    assert collections._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:38:48.690530
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_class = CollectionSearch()
    assert 'ansible.legacy' in test_class._load_collections(None,None)
    assert 'ansible.legacy' in test_class._load_collections(None,[])
    assert 'ansible.legacy' in test_class._load_collections(None,["foo"])

    # test with a local collection
    assert 'ansible_collections.community.general' in test_class._load_collections(None,["ansible_collections.community.general"])

    # test with a local collection that does not exist
    assert 'ansible_collections.community.general.foobar' in test_class._load_collections(None,["ansible_collections.community.general.foobar"])

    # test with a local collection that has a trailing dot

# Generated at 2022-06-22 11:38:50.215024
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    obj._load_collections(None, None)

# Generated at 2022-06-22 11:38:51.486640
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search, CollectionSearch)

# Generated at 2022-06-22 11:38:52.883669
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    
    assert c._collections is None