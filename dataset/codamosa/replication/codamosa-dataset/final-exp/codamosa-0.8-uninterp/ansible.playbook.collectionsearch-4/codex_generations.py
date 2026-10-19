

# Generated at 2022-06-22 11:29:48.326129
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert isinstance(cs._collections, FieldAttribute)

# Generated at 2022-06-22 11:29:52.632680
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.module_utils.six import iteritems

    assert(isinstance(CollectionSearch.__dict__, dict))
    for k, v in iteritems(CollectionSearch.__dict__):
        if not k.startswith("__"):
            assert("FieldAttribute" == v.__class__.__name__)


# Generated at 2022-06-22 11:29:53.586557
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    a._load_collections('collections', [])

# Generated at 2022-06-22 11:30:04.186225
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._validate_collections(None) == ['berkshelf.forge']
    assert c._validate_collections(['my.forge']) == ['my.forge', 'berkshelf.forge']
    assert c._validate_collections(['my.forge','ansible.builtin']) == ['my.forge','ansible.builtin']
    assert c._validate_collections(['my.forge','ansible.builtin','berkshelf.forge']) == ['my.forge','ansible.builtin','berkshelf.forge']
    assert c._validate_collections(['berkshelf.forge','ansible.builtin']) == ['berkshelf.forge','ansible.builtin']

# Generated at 2022-06-22 11:30:06.474727
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == ['ansible_collections.ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:09.073306
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collection_search = CollectionSearch()
    assert test_collection_search.collections == _ensure_default_collection()



# Generated at 2022-06-22 11:30:13.655302
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # No collections
    assert CollectionSearch._load_collections(None, None) == _ensure_default_collection()

    # Collections specified
    assert CollectionSearch._load_collections(None, ['collection1', 'collection2']) == ['collection1', 'collection2']

# Generated at 2022-06-22 11:30:15.476627
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = AnsibleCollectionConfig()
    obj._load_collections('collections', [])


# Generated at 2022-06-22 11:30:17.249173
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # Verify _load_collections method is initialised
    assert cs._load_collections

# Generated at 2022-06-22 11:30:23.252587
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()

    # Tests that the collection list is wrapped in an object
    assert isinstance(search.collections, object)

    # Tests that the collection list is always an array
    assert isinstance(search.collections, list)

    # Tests that the collection list is always a list
    assert isinstance(search.collections, list)

# Generated at 2022-06-22 11:30:34.039216
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    print(cs.collections)


if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:30:35.658397
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()

# Generated at 2022-06-22 11:30:37.410331
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    TestCollectionSearch = CollectionSearch()
    TestCollectionSearch._load_collections(
        attr='collections', ds=['test'])

# Generated at 2022-06-22 11:30:39.346905
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()
    assert isinstance(s._collections, FieldAttribute)


# Generated at 2022-06-22 11:30:44.723117
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None
    assert cs._collections.default == _ensure_default_collection
    assert cs._collections.isa == 'list'
    assert cs._collections.listof == string_types
    assert cs._collections.priority == 100
    assert cs._collections.static
    assert cs._collections.always_post_validate



# Generated at 2022-06-22 11:30:45.790102
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    if search:
        pass

# Generated at 2022-06-22 11:30:48.663813
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # pylint: disable=unused-variable
    assert _ensure_default_collection(list()) == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:51.128971
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == ['ansible_collections.azure.azcollection']


# Generated at 2022-06-22 11:31:02.007896
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class MyPlay(object):
        def __init__(self, collections=None):
            self.myplay_collections = collections
    class MyTask(CollectionSearch, object):
        def __init__(self, play):
            self.play = play

    p = MyPlay(collections=['col.A'])
    t = MyTask(p)

    assert t._collections == ['col.A']

    t = MyTask(p)
    p = MyPlay(collections=None)
    assert t._collections == ['ansible.builtin']

    t = MyTask(p)
    p = MyPlay(collections=['col.A'])
    assert t._collections == ['col.A']

    t = MyTask(p)
    p = MyPlay(collections=[])
    assert t._collections

# Generated at 2022-06-22 11:31:11.311521
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    attr = FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection,
                                  always_post_validate=True, static=True)
    ds = ['github.com/ansible/ansible_collections/ansible/builtin']
    default_collection = AnsibleCollectionConfig.default_collection
    if default_collection and default_collection not in ds:
        ds.insert(0, default_collection)
    if ds and 'ansible.builtin' not in ds and 'ansible.legacy' not in ds:
        ds.append('ansible.legacy')
    print(ds)
if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:34.620545
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    test = CollectionSearch()

    # No collections passed in, ensure the builtin exists
    assert test._load_collections(None, []) == ['ansible.legacy']

    # Ensures specified collection is added to the head of the list, with the
    # default collection at the back.
    assert test._load_collections(None, ['namespace.test']) == ['namespace.test', 'ansible.builtin', 'ansible.legacy']

    # Ensures the specified collections are added to the head of the list,
    # with the default collection at the back.
    assert test._load_collections(None, ['namespace.test', 'namespace.test2']) == \
           ['namespace.test', 'namespace.test2', 'ansible.builtin', 'ansible.legacy']

    # Ensures the

# Generated at 2022-06-22 11:31:36.563879
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    cs = CollectionSearch()
    assert cs._collections.get(ds=None) == ['ansible.builtin.tasks']

# Generated at 2022-06-22 11:31:38.759413
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible.builtin', 'ansible.legacy', 'ansible_collections.namespace.collection']

# Generated at 2022-06-22 11:31:47.600211
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    candidate = CollectionSearch()
    assert candidate._collections.value == ['ansible.builtin.role']
    assert candidate.__dict__['_collections'].value == ['ansible.builtin.role']

    candidate = CollectionSearch(collections=['collection1', 'collection2'])
    assert candidate._collections.value == ['collection1', 'collection2', 'ansible.builtin.role', 'ansible.legacy']
    assert candidate.__dict__['_collections'].value == ['collection1', 'collection2', 'ansible.builtin.role', 'ansible.legacy']



# Generated at 2022-06-22 11:31:49.990109
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test the constructor of the class
    collections = CollectionSearch()
    assert collections._collections.default(_ensure_default_collection())

# Generated at 2022-06-22 11:31:53.899110
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    y = CollectionSearch({'collections': ['test','test1','test2']})
    assert y.collections == ['test','test1','test2']

# Generated at 2022-06-22 11:31:54.956925
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # just make sure we can instantiate the class
    CollectionSearch()

# Generated at 2022-06-22 11:31:59.545245
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = [u'ansible.builtin', u'ansible.legacy', u'collection_name']
    data = {'collections': ds}
    cs = CollectionSearch()
    cs.validate_attributes(data)
    assert cs.collections == ds

# Generated at 2022-06-22 11:32:08.653351
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    class LocalCollectionSearch(CollectionSearch):
        pass

    # When no collection list is provided, _ensure_default_collection() should
    # be called.
    cs = LocalCollectionSearch()
    assert cs._collections == _ensure_default_collection()

    # When providing collection_list as parameter, ensure_default_collection()
    # should be called.
    cs = LocalCollectionSearch(collections=['namespace.thatdoesnotexist'])
    assert cs._collections == _ensure_default_collection(collection_list=['namespace.thatdoesnotexist'])

    # If a list is provided, but no collections, then we should just return the
    # list.
    cs = LocalCollectionSearch(collections=[])
    assert cs._collections == _ensure_default_collection(collection_list=[])

# Generated at 2022-06-22 11:32:10.057772
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == _ensure_default_collection()



# Generated at 2022-06-22 11:32:36.694261
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == ['ansible_collections.nsone.n1tools']



# Generated at 2022-06-22 11:32:38.575603
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections, "No default collection found"

# Generated at 2022-06-22 11:32:49.455133
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # This is the test code for the constructor of class CollectionSearch,
    # the code is mainly for checking the the behavior of the constructor.
    # The __init__ method is simple, and not covered in this testing code.

    print("\nCollectSearch: Checking the _ensure_default_collection()...")
    print("\t- Check the behavior of _ensure_default_collection() when the collection_list == None")
    print("\t\tExpected: The returned value is equal to 'ansible.builtin'")
    default_collection = AnsibleCollectionConfig.default_collection
    AnsibleCollectionConfig.default_collection = 'ansible.builtin'
    collection_list = None
    collection = _ensure_default_collection(collection_list)

# Generated at 2022-06-22 11:32:51.306843
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:57.985410
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    obj.collections = None
    assert obj._load_collections('collections', None) == ['ansible.builtin']
    obj.collections = []
    assert obj._load_collections('collections', None) == ['ansible.builtin']
    obj.collections = ['namespace.collection']
    assert obj._load_collections('collections', None) == ['namespace.collection', 'ansible.builtin']

# Generated at 2022-06-22 11:33:01.043440
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    collection.get_validated_value('collections', ['my_collection'], 'my_collection', None)
    assert ['my_collection'] == collection._collections

# Generated at 2022-06-22 11:33:06.090255
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections is not None
    assert c._collections.default_for_attr(c, 'collections') == ['ansible_collections.ansible', 'ansible.builtin']
    assert c._collections.post_validate(c, 'collections', []) == ['ansible_collections.ansible', 'ansible.builtin']

# Generated at 2022-06-22 11:33:09.794876
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()
    # check we have collections field
    assert hasattr(s, '_collections')
    # check we have _load_collections method
    assert hasattr(s, '_load_collections')
    # check we have _ensure_default_collection method
    assert hasattr(s, '_ensure_default_collection')

# Generated at 2022-06-22 11:33:12.555455
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test with no collection
    cs = CollectionSearch()
    cs.populate({})
    assert cs.collections == _ensure_default_collection()

    # test with collections
    collections = ['my.collection', 'my.second.collection']
    cs = CollectionSearch()
    cs.populate({'collections': collections})
    assert cs.collections == collections

# Generated at 2022-06-22 11:33:21.145648
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    test_collections = [
        "namespace.collection",
        "namespace2.collection2",
        "ansible.builtin",
        "ansible.builtin",
        "ansible.builtin"
    ]

    filter_collections = cs.get_validated_value('collections', cs._collections, test_collections)
    assert len(filter_collections) == 3
    assert "ansible.builtin" in filter_collections
    assert "namespace.collection" in filter_collections
    assert "namespace2.collection2" in filter_collections

# Generated at 2022-06-22 11:34:22.380240
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    cs = CollectionSearch()
    # Test that the default collection is present in the default list
    default_collection = AnsibleCollectionConfig.default_collection
    assert default_collection in cs._collections
    # Test that an empty config string results in an empty list
    assert cs._load_collections('collections', '""') == []
    # Test that a list of collection configs works
    # Test that a single config string works
    # Test that a single invalid config string raises an exception
    with pytest.raises(AssertionError) as error_info:
        cs._load_collections('collections', '"invalid_collection_name"')
    assert str(error_info.value) == 'invalid_collection_name is not a collection'
    # Test that a template string is not allowed

# Generated at 2022-06-22 11:34:28.774305
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    collections._collections = None # Set the _collections attribute to None

    # Call _load_collections with mock data
    ds=["ansible.builtin","ansible.legacy","ansible_collection.test_namespace.test_collection"]
    collections._load_collections(collections._collections, ds)

    # Check to see if the values are same
    assert collections._collections == ["ansible_collection.test_namespace.test_collection","ansible.builtin","ansible.legacy"]

# Generated at 2022-06-22 11:34:32.419784
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    c = CollectionSearch()

    ds = {
        'collections': ['test']
    }
    for collection_name in c._load_collections('collections', ds):
        assert(collection_name == 'test')

# Generated at 2022-06-22 11:34:36.945704
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    assert x._collections.default == _ensure_default_collection
    assert x._collections.static == True
    assert x._collections.priority == 100
    assert isinstance(x._collections.listof, type(string_types))
    assert x._collections.default == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:34:46.402250
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test no default collection
    test_data = {'collections': None}
    obj = CollectionSearch()
    obj.load_data(data=test_data)
    assert obj._collections is not None
    assert obj._collections == ['ansible.builtin']

    # Test no default collection, fallback to legacy
    test_data = {'collections': None}
    obj = CollectionSearch()
    obj.fallback_to_legacy = True
    obj.load_data(data=test_data)
    assert obj._collections is not None
    assert obj._collections == ['ansible.legacy']

    # Test default collection added to collection list
    test_data = {'collections': ['test.collection']}
    obj = CollectionSearch()
    obj.load_data(data=test_data)
   

# Generated at 2022-06-22 11:34:50.046404
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch(collections=["ansible.builtin", "ansible.legacy", "collection.mycollection"])
    assert obj._collections == ['ansible.builtin', 'ansible.legacy', 'collection.mycollection']
    obj = CollectionSearch(collections=["collection.mycollection", "collection.yourcollection", "collection.theircollection"])
    assert obj._collections == ['collection.mycollection', 'collection.yourcollection', 'collection.theircollection', 'ansible.legacy']
    obj = CollectionSearch(collections=["ansible.builtin", "ansible.legacy"])
    assert obj._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:34:53.166354
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.collections == None
    assert collection_search._collections.static == True


# Generated at 2022-06-22 11:34:54.947347
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Verify constructor can be called with default argument
    result = CollectionSearch()

    # Verify constructor can be called with valid argument
    result = CollectionSearch(collections=['collection1', 'collection2'])

# Generated at 2022-06-22 11:35:07.069617
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    test1 = CollectionSearch()
    test2 = CollectionSearch()
    test3 = CollectionSearch()
    test4 = CollectionSearch()
    test5 = CollectionSearch()

    # set_from_playbook_file
    test1.set_from_playbook_file(collections=['ansible_collections.some_collection.some_collection_name'])
    test2.set_from_playbook_file(collections=[
        'ansible_collections.some_collection.some_collection_name', 'ansible.builtin'])
    test3.set_from_playbook_file(collections=[
        'ansible_collections.some_collection.some_collection_name', 'ansible.builtin', 'ansible.legacy'])

# Generated at 2022-06-22 11:35:09.037005
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = CollectionSearch()
    assert ds._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:36:59.677669
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    print(x._collections)

# Generated at 2022-06-22 11:37:01.413969
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection.__class__.__name__ == 'CollectionSearch'

# Generated at 2022-06-22 11:37:09.664037
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    if c.collections is None:
        raise AssertionError("The constructor of CollectionSearch fails to set `collections` to 'ansible.builtin,ansible.legacy' when `collections` is None")
    else:
        print("Passed: the constructor of CollectionSearch sets `collections` to 'ansible.builtin,ansible.legacy' when `collections` is None")
    if len(c.collections) != 2:
        raise AssertionError("The constructor of CollectionSearch fails to set `collections` to 'ansible.builtin,ansible.legacy' when `collections` is None")
    else:
        print("Passed: the constructor of CollectionSearch sets `collections` to 'ansible.builtin,ansible.legacy' when `collections` is None")

# Generated at 2022-06-22 11:37:10.219917
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    print(search)

# Generated at 2022-06-22 11:37:12.056447
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:37:13.964421
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == ['ansible.posix'] or CollectionSearch()._collections == ["ansible.windows"]

# Generated at 2022-06-22 11:37:15.646201
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    data ={
        "collections" : ["test"]
    }
    collection = CollectionSearch()
    collection.load_from_file(data)

    assert collection._collections == ["test"]

# Generated at 2022-06-22 11:37:16.635810
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col_search = CollectionSearch()

# Generated at 2022-06-22 11:37:17.656845
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

# Generated at 2022-06-22 11:37:20.869427
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections is None
    assert c.make_vars_private is None
    assert c.no_log is None
    assert c.run_once is None
    assert c.vars is None