

# Generated at 2022-06-22 11:29:47.552593
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:29:48.120816
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    pass

# Generated at 2022-06-22 11:29:50.622760
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    collection.collections = ['collections']
    assert collection.collections == ['collections', 'ansible.builtin']
    return

# Generated at 2022-06-22 11:29:53.336601
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.collections = ['ansible.builtin', 'ansible.legacy']
    assert cs.collections == ['ansible.builtin', 'ansible.legacy']


# Generated at 2022-06-22 11:29:56.159144
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search, CollectionSearch)
    assert hasattr(collection_search, '_collections')
    assert hasattr(collection_search, '_load_collections')

# Generated at 2022-06-22 11:29:59.926928
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.task_include.construct import TaskInclude

    t = TaskInclude()
    assert 'ansible.builtin' in t._collections

    u = TaskInclude(collections=['*'])
    assert 'ansible.builtin' in u._collections

# Generated at 2022-06-22 11:30:00.644314
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    pass

# Generated at 2022-06-22 11:30:02.205027
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c is not None

# Generated at 2022-06-22 11:30:04.410125
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default == AnsibleCollectionConfig.default_collection

# Generated at 2022-06-22 11:30:07.347219
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._fields['collections'].default is not None
    assert isinstance(cs, CollectionSearch)

# Generated at 2022-06-22 11:30:12.351291
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    task = CollectionSearch()
    assert task._collections._valid_data == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:13.937197
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert isinstance(collection, CollectionSearch)

# Generated at 2022-06-22 11:30:15.380600
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert not cs._load_collections

# Generated at 2022-06-22 11:30:19.042554
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

    cs = CollectionSearch(collections=["test"])
    assert cs.collections == _ensure_default_collection(collection_list=["test"])

# Generated at 2022-06-22 11:30:21.741033
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == [
        'ansible_collections.ansible.builtin',
        'ansible_collections.ansible.legacy'
    ]

# Generated at 2022-06-22 11:30:25.361661
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        pass

    class TestTask(TestCollectionSearch):
        pass

    t = TestTask()

    assert t.collections == ['ansible.builtin', 'ansible.legacy'], "Incorrect collections"

# Generated at 2022-06-22 11:30:31.038851
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj.collections == ['ansible.builtin', 'ansible.legacy']
    obj = CollectionSearch(collections=['ansible.legacy'])
    assert obj.collections == ['ansible.legacy']
    obj = CollectionSearch(collections=[])
    assert obj.collections == ['ansible.builtin', 'ansible.legacy']
    obj = CollectionSearch(collections=None)
    assert obj.collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:38.385955
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    type_ansible_base = type(CollectionSearch)
    assert (type_ansible_base.__name__ == 'CollectionSearch')
    assert (isinstance(type_ansible_base._collections, FieldAttribute))
    assert (type_ansible_base._collections.default() == ['ansible.builtin', 'ansible.legacy'])

# Generated at 2022-06-22 11:30:43.277830
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.play_context import PlayContext

    cs = CollectionSearch()
    pc = PlayContext()
    ds = [{'collections': ['ansible.builtin']}]

    cs.post_validate(ds, pc)
    assert ds == [{'collections': ['ansible.builtin']}]

# Generated at 2022-06-22 11:30:54.801075
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.errors import AnsibleParserError
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.module_utils.six import PY3
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    if PY3:
        # py3 doesn't have a callable()
        def callable(obj):
            return hasattr(obj, '__call__')

    # test constructor and default collections
    c = CollectionSearch()
    assert callable(c._load_collections)
    assert c._collections.default == [AnsibleCollectionConfig.default_collection]

    # test constructor with collections list
    c = CollectionSearch(collections=['Collection1', 'Collection2', 'Collection3'])

# Generated at 2022-06-22 11:31:11.473759
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class InitCollectionSearch(CollectionSearch):
        def __init__(self, collection_list=None):
            if collection_list:
                self.collections = collection_list
            else:
                self.collections = None
    # Test without collections
    collection_search = InitCollectionSearch(collection_list=None)
    assert collection_search.collections == ['ansible.builtin']
    # Test with collections
    collection_search = InitCollectionSearch(collection_list=['foo.bar'])
    assert collection_search.collections == ['foo.bar', 'ansible.builtin']
    # Test with default collection
    collection_search = InitCollectionSearch(collection_list=['ansible.builtin'])
    assert collection_search.collections == ['ansible.builtin']
    # Test with default collection and other collections
    collection

# Generated at 2022-06-22 11:31:13.873142
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    f = CollectionSearch()
    assert f.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:31:20.743834
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch._collections, FieldAttribute)
    assert CollectionSearch._collections.name == 'collections'
    assert CollectionSearch._collections.isa == 'list'
    assert CollectionSearch._collections.listof == string_types
    assert CollectionSearch._collections.priority == 100
    assert CollectionSearch._collections.default == _ensure_default_collection
    assert CollectionSearch._collections.always_post_validate is True
    assert CollectionSearch._collections.static is True

# Generated at 2022-06-22 11:31:26.814312
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # default case
    test = CollectionSearch()
    assert test._collections.default is not None
    assert 'ansible.builtin' in test._collections.default

    # test with a custom collection
    test = CollectionSearch(collections=['custom.collection'])
    assert 'custom.collection' in test._collections.default
    assert 'ansible.builtin' in test._collections.default

# Generated at 2022-06-22 11:31:28.298469
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert isinstance(search, CollectionSearch)

# Generated at 2022-06-22 11:31:35.757573
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch(loader=None, variable_manager=None)
    print(collection_search)
    print(type(collection_search))
    print(collection_search.__class__.__name__)
    print(collection_search.__class__.__module__)
    print(collection_search.__class__.__bases__)
    print(collection_search._validation_errors)
    print(collection_search._attributes)
    print(collection_search._attribute_values)


# Generated at 2022-06-22 11:31:37.315473
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:40.339496
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # create a new instance of class CollectionSearch
    cs = CollectionSearch()

    # assert attributes of class CollectionSearch
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:49.209443
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # case 1:
    collection_search=CollectionSearch(collections=None)
    assert collection_search.collections == ['ansible.builtin']
    # case 2:
    collection_search=CollectionSearch(collections=['ansible.builtin'])
    assert collection_search.collections == ['ansible.builtin']
    # case 3:
    collection_search=CollectionSearch(collections=['ansible.builtin','ansible.builtin.plugins'])
    assert collection_search.collections == ['ansible.builtin', 'ansible.builtin.plugins']
    # case 4:
    collection_search=CollectionSearch(collections=['ansible.builtin.plugins'])
    assert collection_search.collections == ['ansible.builtin.plugins']

# Generated at 2022-06-22 11:31:51.063823
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test._collections == None

# Generated at 2022-06-22 11:32:10.231221
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c_s = CollectionSearch()
    assert c_s._collections.default == _ensure_default_collection(), '_collections.default is not expected value!'
    assert c_s._collections.isa == 'list', '_collections.isa is not expected value!'
    assert c_s._collections.priority == 100, '_collections.priority is not expected value!'
    assert c_s._collections.static == True, '_collections.static is not expected value!'

# Generated at 2022-06-22 11:32:13.890440
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    assert x.collections == _ensure_default_collection()

if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:18.140969
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    ansible_collections = c._load_collections('collections', ['ansible_collections'])
    assert 'ansible_collections' in ansible_collections
    assert 'ansible.builtin' in ansible_collections

# Generated at 2022-06-22 11:32:21.289104
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base

    base = Base()
    assert base.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:23.570481
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert not cs._collections, 'collections should be initialized to an empty list'


# Generated at 2022-06-22 11:32:33.187233
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base
    from ansible.plugins.loader import module_loader, fragment_loader
    from ansible.errors import AnsibleParserError

    base = Base(Base.load("plays/empty_play.yml", {}))
    base.module_loader = module_loader
    base.fragment_loader = fragment_loader

    # For the default constructor with no parameter, we expect valid value for
    # collections with ansible.legacy and ansible.builtin.
    ds = base.get_validated_value('collections', FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection, always_post_validate=True, static=True), None, None)
    assert len(ds) == 2

# Generated at 2022-06-22 11:32:36.298306
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs == "{'collections': ['ansible.builtin','ansible.builtin.plugins','ansible.builtin.modules','ansible.builtin.lookup','ansible.builtin.filter','ansible.builtin.action','ansible.builtin.module_utils']}"

# Generated at 2022-06-22 11:32:39.906128
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
	test_obj = CollectionSearch()
	assert test_obj is not None
	print ('testCollectionSearch() - SUCCESS')

if __name__ == '__main__':
	test_CollectionSearch()

# Generated at 2022-06-22 11:32:50.397531
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.role.requirement import RoleRequirement
    import os
    import sys

    # copy of collections in ansible.cfg

# Generated at 2022-06-22 11:32:51.349647
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

# Generated at 2022-06-22 11:33:23.300709
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.name == 'collections'
    assert CollectionSearch._collections.default == 'ansible.builtin'
    assert CollectionSearch._collections.priority == 100
    assert CollectionSearch._collections.always_post_validate is True
    assert CollectionSearch._collections.static is True

# Generated at 2022-06-22 11:33:31.002180
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

    # Check default always_post_validate
    assert collection_search._collections.always_post_validate == True

    # Check default listof
    assert collection_search._collections.listof == string_types

    # Check default priority
    assert collection_search._collections.priority == 100

    # Check default isa
    assert collection_search._collections.isa == 'list'

    # Check default static
    assert collection_search._collections.static == True

    # Check default static
    assert collection_search._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:33:32.700071
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    _test_class = CollectionSearch()
    assert _test_class._collections is not None

# Generated at 2022-06-22 11:33:34.942196
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    x._load_collections("test_attr", {})

# Generated at 2022-06-22 11:33:36.476874
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None
    assert cs.playbook is None
    assert cs.collections is None

# Generated at 2022-06-22 11:33:37.872935
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections is not None

# Generated at 2022-06-22 11:33:39.131601
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection(collection_list=[])

# Generated at 2022-06-22 11:33:46.805241
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import os
    import tempfile
    from ansible.errors import AnsibleError
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import collection_loader
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.path import unfrackpath

    test_collections = """
    collections:
    - ansible_namespace.collection_name
    """

    # create a temp directory
    tmp_directory = tempfile.mkdtemp()
    # create a temp ansible.cfg file
    with open(os.path.join(tmp_directory, 'ansible.cfg'), 'w') as f:
        f.write("""[defaults]
library = %s/library
""")

    # create a temp directory to serve as the library
   

# Generated at 2022-06-22 11:33:54.476232
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import sys
    import tempfile
    import pytest
    import os

    # prepare a simple test collection
    file_desc, target_file_path = tempfile.mkstemp()
    os.close(file_desc)

    target_collection_dir = os.path.dirname(target_file_path)
    target_collection_name = os.path.basename(target_collection_dir)

    # reset environment
    sys.path.pop()
    os.environ.pop('ANSIBLE_COLLECTIONS_PATHS')
    os.environ.pop('ANSIBLE_COLLECTIONS_PATH')


# Generated at 2022-06-22 11:33:58.372193
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # verify that the constructor populates the attribute _collections
    TestCollectionSearch = type('TestCollectionSearch', (CollectionSearch,), {})
    val = TestCollectionSearch()
    assert val._collections == _ensure_default_collection()



# Generated at 2022-06-22 11:34:55.397131
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class test_inst:
        pass
    t = test_inst()
    setattr(t, '_collections', [])
    ret = t._load_collections(None, [])
    assert ret == ['ansible.legacy']

# Generated at 2022-06-22 11:34:58.767269
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    a.post_validate(None, 'collections')
    assert isinstance(a.collections, list)
    assert a.collections[0] == 'ansible.builtin'

# Generated at 2022-06-22 11:35:04.703299
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # no field Attribute, then use default value
    assert isinstance(CollectionSearch()._collections, list)
    assert not CollectionSearch()._collections
    # pass in field Attribute and use value in field Attribute 
    assert CollectionSearch(collections=["test1", "test2"])._collections == ["test1", "test2"]

# Generated at 2022-06-22 11:35:08.880678
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create a Class by calling CollectionSearch constructor and test for name and value of attributes
    collection_search = CollectionSearch()
    assert (collection_search._collections.name == 'collections')
    assert (collection_search._collections.default == _ensure_default_collection())



# Generated at 2022-06-22 11:35:16.691064
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestClass:
        _collections = None
        def _load_collections(self, attr, ds):
            return self._collections
    try:
        a = CollectionSearch()
        b = TestClass()
        assert a.post_validate(b, None, {}, 'collections', None) == ['ansible.builtin', 'ansible_collections.myorg.mycollection']
        assert a.post_validate(b, None, {}, 'collections', ['ansible_collections.myorg.mycollection']) == ['ansible_collections.myorg.mycollection']
    except:
        print("test case failed")

# Generated at 2022-06-22 11:35:25.851056
# Unit test for constructor of class CollectionSearch

# Generated at 2022-06-22 11:35:32.531688
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs._collections = ['testing.ansible.modules']
    assert cs._collections == ['testing.ansible.modules']

    cs._collections = []
    cs._collections = ['testing.ansible.modules', 'community.general']
    assert cs._collections == ['testing.ansible.modules', 'community.general']

    assert cs._load_collections('collections', ['testing.ansible.modules', 'community.general']) == \
           ['testing.ansible.modules', 'community.general']

# Generated at 2022-06-22 11:35:36.862956
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ansible_vars = {}
    collection_search = CollectionSearch(play=None, play_context=None, new_play=None, loader=None, variable_manager=None,
                                         all_vars=ansible_vars)
    assert collection_search.collections == ['ansible.builtin', 'ansible.legacy']
    collection_search.collections = ['ansible.builtin', 'ansible.legacy', 'ansible_collections.notstdlib.moveit']
    assert collection_search.collections == collection_search.collections

# Generated at 2022-06-22 11:35:39.970475
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_CollectionSearch = CollectionSearch()
    print("\n" + "test_CollectionSearch: " + str(test_CollectionSearch._collections))

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:35:47.704431
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_list = [u'ansible_collections.nagypeter.collection_test', u'ansible_collections.testnamespace.testcollection']
    expected_list = [u'ansible_collections.testnamespace.testcollection', u'ansible_collections.nagypeter.collection_test', u'ansible.builtin', u'ansible.legacy']
    assert expected_list == _ensure_default_collection(collection_list)

# Generated at 2022-06-22 11:37:45.548813
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    if collection_search._collections != _ensure_default_collection():
        raise ClassConstructorException('CollectionSearch not properly initialized')

# Class for testing the CollectionSearch constructor

# Generated at 2022-06-22 11:37:46.046813
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:37:48.909853
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    _instace = CollectionSearch()
    _instace.collections = ['collection.path']
    assert _instace.collections == ['collection.path']

# Generated at 2022-06-22 11:37:57.245129
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    # Test the constructor (__init__)
    assert isinstance(cs, CollectionSearch)
    assert isinstance(cs._collections, FieldAttribute)
    assert cs._collections._key == 'collections'
    assert isinstance(cs._collections._isa, list)
    assert isinstance(cs._collections._listof, string_types)
    assert cs._collections._priority == 100
    assert cs._collections._default() == ['ansible.builtin', 'ansible.legacy']
    assert cs._collections._always_post_validate == True
    assert cs._collections._static == True

# Generated at 2022-06-22 11:37:59.370821
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._load_collections(None, None) is None

# Generated at 2022-06-22 11:37:59.811052
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    model = CollectionSearch()

# Generated at 2022-06-22 11:38:02.627239
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Sample data
    data = {'collections': ['f5.icontrol']}
    my_class = CollectionSearch(data)
    assert my_class._collections == ['f5.icontrol']

# Generated at 2022-06-22 11:38:12.797252
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Fixture:
    from ansible.playbook.base import Base
    from ansible.plugins.loader import fragment_loader

    class PlaybookInclude(Base, CollectionSearch):
        _collection_search_paths = FieldAttribute(isa='list', listof=string_types, include=['collections'])

    c = PlaybookInclude()

    # Test the constructor
    assert c.collections == ['ansible.legacy']

    # Test the constructor with a different default collection
    # Fixture:
    default_collection = 'foo.bar'
    AnsibleCollectionConfig.default_collection = default_collection

    class PlaybookInclude(Base, CollectionSearch):
        _collection_search_paths = FieldAttribute(isa='list', listof=string_types, include=['collections'])

    c = PlaybookInclude()

# Generated at 2022-06-22 11:38:14.124006
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections(None,None) is not None

# Generated at 2022-06-22 11:38:20.515411
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()

    # Test that the default collection is always used.
    assert search._collections == _ensure_default_collection()

    # Test presence of default collection if user defined a collection list
    assert search._collections == _ensure_default_collection(['Foo'])

    # Test empty collection list.
    assert search._collections == _ensure_default_collection([])

