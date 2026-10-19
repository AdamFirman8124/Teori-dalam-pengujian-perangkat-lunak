

# Generated at 2022-06-22 11:29:55.248213
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.get_validated_value("collections", cs._collections, ["collections/collection1", "collection2"], None) == \
           _ensure_default_collection(["collections/collection1", "collection2"])
    assert cs.get_validated_value("collections", cs._collections, None, None) == \
           _ensure_default_collection(None)


# Generated at 2022-06-22 11:29:57.306666
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestSearch(CollectionSearch):
        pass

    assert TestSearch()._collections == _ensure_default_collection()



# Generated at 2022-06-22 11:29:59.617956
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.get_value('collections') == _ensure_default_collection()

# Generated at 2022-06-22 11:30:06.004644
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import unittest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.resources import CollectionSearch

    class TestCollectionSearch(unittest.TestCase):
        def test_empty_constructor(self):
            """Ensure defaults are set when constructor is empty."""
            c = CollectionSearch()
            self.assertEqual(c._collections, ['ansible_collections.notstdlib.moveitallout'])

    # Run the unit tests
    unittest.main()


# Generated at 2022-06-22 11:30:11.280216
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_one = CollectionSearch()
    assert test_one._validated_data['collections'] == ['ansible.builtin', 'ansible.legacy']

    test_two = CollectionSearch(collections=None)
    assert test_two._validated_data['collections'] == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:15.681928
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    cs = CollectionSearch()

    cs.post_validate(u_ds=None, vars=None)

    #assert cs._collections == _ensure_default_collection()

    assert cs._load_collections(attr=None, ds=[]) == None

# Generated at 2022-06-22 11:30:18.830465
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    temp_collection_search = CollectionSearch()
    assert isinstance(temp_collection_search, CollectionSearch)

# Generated at 2022-06-22 11:30:25.063432
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # It doesn't use its own constructor, it is a mixin
    from ansible.playbook.base import Base
    test_object = CollectionSearch()
    assert test_object._collections == [ None ]
    assert hasattr(test_object, '_collections')
    test_obj = Base()
    test_obj.module_utils = globals().copy()
    test_obj._load_collections(None, None)


# Generated at 2022-06-22 11:30:27.408113
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    assert isinstance(instance._collections, FieldAttribute)
    assert instance._collections.default() == _ensure_default_collection()


# Generated at 2022-06-22 11:30:32.230661
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()
    assert cs.collections is None

    cs = CollectionSearch(collections=['foo'])
    assert cs.collections == ['foo', 'ansible.legacy']

    cs = CollectionSearch(collections=['foo', 'ansible.legacy'])
    assert cs.collections == ['foo', 'ansible.legacy']

# Generated at 2022-06-22 11:30:42.910002
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections == ['ansible_collections.foo.bar.baz']
    assert a._load_collections(None, ['ansible_collections.foo.bar.baz']) == ['ansible_collections.foo.bar.baz']

# Generated at 2022-06-22 11:30:47.410422
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    field = CollectionSearch()._collections
    default = _ensure_default_collection()
    assert field.default(None) == default
    assert CollectionSearch().collections == default
    assert CollectionSearch().collections is not None

# Generated at 2022-06-22 11:30:54.144167
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionsearch = CollectionSearch()
    assert collectionsearch._load_collections('collections', []) is None
    assert collectionsearch._load_collections('collections', ['ansible_collections.test']) == ['ansible_collections.test']
    assert collectionsearch._load_collections('collections', ['ansible_collections.test', 'ansible.builtin']) == ['ansible_collections.test', 'ansible.builtin']
    assert collectionsearch._collections == [_ensure_default_collection()]

# Generated at 2022-06-22 11:30:59.927907
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        pass

    # collections=None
    t0 = TestCollectionSearch(collection_list=None)
    assert t0.collections == ['ansible.builtin']

    # collections=[]
    t1 = TestCollectionSearch(collection_list=[])
    assert t1.collections == ['ansible.builtin']

    # collections=['foo']
    t2 = TestCollectionSearch(collection_list=['foo'])
    assert t2.collections == ['foo', 'ansible.builtin']

    # collections=['foo', 'bar']
    t3 = TestCollectionSearch(collection_list=['foo', 'bar'])
    assert t3.collections == ['foo', 'bar', 'ansible.builtin']

    # collections=['foo', 'ansible.builtin']
   

# Generated at 2022-06-22 11:31:10.503487
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.playbook.block import Play
    from ansible.executor.playbook.role import RoleDefinition
    from ansible.parsing.dataloader import DataLoader

    # Create and initialize instance of class
    # (CollectionSearch contains only static/read-only attributes and has no initializer)
    collection_search = CollectionSearch()

    # Test whether attribute 'collections' has been correctly set
    # Note that this is the only attribute of this class
    assert collection_search.collections == ['ansible_collections.ansible.builtin:', 'ansible_collections.ansible.legacy']

    # Use the instance of the class to test _load

# Generated at 2022-06-22 11:31:13.341343
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    print(cs.collections)
    print(cs._load_collections('collections', ['ansible.builtin']))

# Generated at 2022-06-22 11:31:14.679794
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch() is not None, "Unable to create CollectionSearch"

# Generated at 2022-06-22 11:31:24.492264
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # check that collections if not set
    assert c._collections is None

    # check that collections gets set
    ds = ['test']
    assert c._load_collections(None, ds) == ['test']

    # check that collections gets set with default collection if nothing is passed in
    ds = None
    assert c._load_collections(None, ds) is not None

    # check that with default, builtin is present
    assert 'ansible.builtin' in c._collections or 'ansible.legacy' in c._collections

    # check that with default, test is present
    assert 'test' in c._collections

# Generated at 2022-06-22 11:31:26.364253
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:36.430461
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    coll = CollectionSearch()

    # Test default value
    coll.post_validate()
    assert coll.collections == _ensure_default_collection()

    # Test assignment of non-list types
    for value in (None, 'string', 12):
        coll.collections = value
        try:
            coll.post_validate()
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid collection "%s" did not raise a ValueError' % value)

    # Test assignment and validation of list of non-string types
    for value in ([None, 'string', 12], [None, 12]):
        coll.collections = value
        try:
            coll.post_validate()
        except ValueError:
            pass

# Generated at 2022-06-22 11:31:54.445779
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None
    assert cs._collections == list
    assert cs._load_collections('test', ['collections']) == 'collections'


if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:56.045134
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    print(c._collections)

# Generated at 2022-06-22 11:31:59.655024
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    assert cs._collections == [
        'ansible.builtin',
        'ansible_collections.my_namespace.my_collection',
        'ansible.legacy'
    ]

# Generated at 2022-06-22 11:32:02.977614
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    init_val = CollectionSearch()
    assert init_val._collections == _ensure_default_collection
    assert init_val.__class__.__name__ == 'CollectionSearch'


# Generated at 2022-06-22 11:32:04.346368
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:08.469240
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    attr = "collections"
    ds = test_obj._load_collections(attr, ds = None)
    expected = ["ansible_collections.ansible.builtin"]
    assert ds == expected


# Generated at 2022-06-22 11:32:10.370482
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:15.881349
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.post_validate([])
    assert cs._collections is None
    cs.post_validate(None)
    assert cs._collections is None
    cs.post_validate(['test'])
    assert cs._collections == ['test']

# Generated at 2022-06-22 11:32:18.249304
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections is not None
    assert CollectionSearch()._load_collections is not None
    assert CollectionSearch().collections is not None

# Generated at 2022-06-22 11:32:23.073975
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test with no arguments
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

    # Test with argument
    collection_list = ['collection1']
    cs = CollectionSearch(collection_list=collection_list)
    assert cs._collections == _ensure_default_collection(collection_list=collection_list)

# Generated at 2022-06-22 11:32:50.214015
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert isinstance(cs, CollectionSearch)

# Generated at 2022-06-22 11:32:51.559368
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    coll = CollectionSearch()
    assert coll._collections._default == _ensure_default_collection

# Generated at 2022-06-22 11:32:53.814774
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = CollectionSearch()
    assert ds._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:56.603739
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test constructor
    collectionSearch = CollectionSearch()

    print("test_CollectionSearch finished!")

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:59.935762
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # this is used by the test system to create a fake class
    from ansible.playbook import Base

    base = Base()
    assert base.collections == ['ansible.builtin', 'ansible.legacy']



# Generated at 2022-06-22 11:33:00.765592
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()

# Generated at 2022-06-22 11:33:02.710152
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search._load_collections(None,None)

# Generated at 2022-06-22 11:33:04.375916
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    print("collections = ", obj.collections)

# Generated at 2022-06-22 11:33:15.634673
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c1 = CollectionSearch()
    c2 = CollectionSearch(collections=['collection1', 'collection2'])

    assert 'ansible.legacy' in c1.get_validated_value('collections', c1.collections)
    assert 'ansible.legacy' in c2.get_validated_value('collections', c2.collections)
    assert 'ansible.builtin' not in c1.get_validated_value('collections', c1.collections)
    assert 'ansible.builtin' not in c2.get_validated_value('collections', c2.collections)
    assert 'collection1' in c2.get_validated_value('collections', c2.collections)

# Generated at 2022-06-22 11:33:17.360554
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    if cs is None:
        raise ValueError("CollectionSearch is not created for unit_test")

# Generated at 2022-06-22 11:34:12.999759
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default() == ["ansible-collections.cisco.asa"]

# Generated at 2022-06-22 11:34:15.017079
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    print(collection_search._collections)


# Generated at 2022-06-22 11:34:16.569242
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert 'ansible.builtin' in search._collections

# Generated at 2022-06-22 11:34:21.501721
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    my_collection_search = CollectionSearch()
    print(my_collection_search._collections)
    my_collection_search.collections = ['some_collection']
    print(my_collection_search.collections)
    my_collection_search.collections = []
    print(my_collection_search.collections)

# Generated at 2022-06-22 11:34:22.353454
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()

# Generated at 2022-06-22 11:34:24.741884
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_object = CollectionSearch()
    assert test_object._collections.default == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:34:28.434395
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test the default constructor
    CollectionSearch()
    # Test the constructor with a list of collections
    CollectionSearch(collections=['test.test'])

# Generated at 2022-06-22 11:34:29.853635
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == []

# Generated at 2022-06-22 11:34:34.556802
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections._static == True
    assert search._collections._always_post_validate == True
    assert search._collections._priority == 100
    assert search._collections._default == search._ensure_default_collection


if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:34:36.900633
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection._collections.default == 'ansible.builtin'
    assert collection._collections.default == 'ansible.builtin'

# Generated at 2022-06-22 11:36:32.686455
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None
    assert cs.collections is not None
    # this is a list
    assert isinstance(cs._collections, list)
    # this is a list
    assert isinstance(cs.collections, list)
    # the two are not the same
    assert cs._collections is not cs.collections
    # the two are equal
    assert cs._collections == cs.collections

# Generated at 2022-06-22 11:36:37.683685
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test 1:
    #    collections = None
    #    Should be the same as:
    #    collections = [default_collection]

    cs = CollectionSearch()
    collections = None
    cs.collections = collections
    assert cs._collections == _ensure_default_collection(collections)

    # Test 2:
    #    collections = ['local', 'ansible.builtin']
    #    Should be the same as:
    #    collections = [default_collection, 'local', 'ansible.builtin']
    cs = CollectionSearch()
    collections = ['local', 'ansible.builtin']
    cs.collections = collections
    assert cs._collections == _ensure_default_collection(collections)

    # Test 3:
    #    collections = ['local', 'ansible.builtin', default_collection]

# Generated at 2022-06-22 11:36:42.272088
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj1 = CollectionSearch()
    assert obj1.collections == ['ansible.builtin']

    obj1.collections = ['test']
    assert obj1.collections == ['test', 'ansible.builtin']

    obj1.collections = []
    assert obj1.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:36:43.908241
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:36:45.300207
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._load_collections(None, ['collections'])

# Generated at 2022-06-22 11:36:50.485415
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections is not None
    assert len(cs.collections) >= 1

# # Need to make sure the attribute search works, because this was breaking
# class TestBase:
#     def test_attribute_search(self):
#         collectionsearch = CollectionSearch()
#         base = Base()
#         assert base.collections is not None

# Generated at 2022-06-22 11:36:51.608861
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    C = CollectionSearch()
    assert C._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:36:53.120665
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == None

# Generated at 2022-06-22 11:37:01.781525
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test constructor
    import ansible
    from ansible.playbook.attribute import FieldAttribute
    from types import MethodType

    # create an instance of class CollectionSearch
    cs = CollectionSearch()

    # test if the functions of the instance are correct
    assert isinstance(cs._collections, FieldAttribute)
    assert type(cs._load_collections) is MethodType
    assert ansible.playbook.play.Play.__bases__[0] is CollectionSearch
    assert ansible.playbook.role.Role.__bases__[0] is CollectionSearch
    assert ansible.playbook.task.Task.__bases__[0] is CollectionSearch
    assert ansible.playbook.handler.Handler.__bases__[0] is CollectionSearch

# Generated at 2022-06-22 11:37:05.356440
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()
    assert collection_search._load_collections(None, ['test']) == ['test', 'ansible.builtin']

# Generated at 2022-06-22 11:39:00.682970
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == ['ansible.builtin']

# Generated at 2022-06-22 11:39:02.589168
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()



# Generated at 2022-06-22 11:39:04.123899
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search_instance = CollectionSearch()
    assert collection_search_instance._collections is not None

# Generated at 2022-06-22 11:39:05.501766
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
        print("Testing Class Validation")
        assert len(CollectionSearch()._collections) == 1

# Generated at 2022-06-22 11:39:15.610425
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()

    assert c.__dict__['_collections'].default(c) is None

    assert c.__dict__['_collections'].post_validate(c, None, None) is None
    assert c.__dict__['_collections'].post_validate(c, [], None) == ['ansible.builtin']
    assert c.__dict__['_collections'].post_validate(c, [''], None) == ['ansible.builtin']
    assert c.__dict__['_collections'].post_validate(c, ['ansible.builtin'], None) == ['ansible.builtin']

# Generated at 2022-06-22 11:39:24.218264
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    def _test(attr, ds, result):
        collection_search = CollectionSearch()
        try:
            collection_search._load_collections(attr, ds)
        except Exception as e:
            return str(e) == result
    assert _test("collections", None, None)
    assert _test("collections", [], None)
    assert _test("collections", ["ansible_collections.username.role"],
                 "ansible.collection.collection_loader.CollectionLoaderException: Failed to import collection "
                 "'ansible_collections.username.role': No module named ansible_collections.username.role")

# Generated at 2022-06-22 11:39:29.984467
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_data = '{"collections": ["ansible.builtin"]}'
    data_dict = {}
    data_dict = AnsibleCollectionConfig.load(data_dict, test_data)

    obj = CollectionSearch()
    obj.post_validate(data_dict, 'collections')
    assert obj.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:39:31.384254
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test.collections
    assert test._collections

# Generated at 2022-06-22 11:39:34.666362
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections is not None

# Generated at 2022-06-22 11:39:35.320831
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()