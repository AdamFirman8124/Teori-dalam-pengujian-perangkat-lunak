

# Generated at 2022-06-22 11:29:53.047202
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role import Role
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    obj = CollectionSearch()

    collections = ['ansible.builtin']
    obj.set_loader(AnsibleCollectionLoader())
    obj._collections = collections
    obj._load_collections(attr=None, ds=collections)

    # If the obj._collections is None means it is empty
    assert obj._collections != None
    assert role_key in obj.get_loader().collections

# Generated at 2022-06-22 11:29:55.884586
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    try:
        test_class = CollectionSearch()
        assert test_class.get_value_list()
    except SystemExit:
        assert True
    else:
        assert False


# Generated at 2022-06-22 11:29:58.877552
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        pass
    test_collection_search = TestCollectionSearch()
    assert test_collection_search._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:01.775722
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert "ansible.builtin" in collection_search._collections
    assert "ansible.legacy" in collection_search._collections

# Generated at 2022-06-22 11:30:07.064793
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    connection_search_class = ISearch()

    assert connection_search_class._load_collections(attr='collections', ds=None) is None

    assert connection_search_class._load_collections(attr='collections', ds=['Collections1']) == ['Collections1']


# Generated at 2022-06-22 11:30:10.854669
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # c is an instance of CollectionSearch
    assert isinstance(c, CollectionSearch)
    # c._collections is an instance of FieldAttribute
    assert isinstance(c._collections, FieldAttribute)



# Generated at 2022-06-22 11:30:15.630218
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print ("Test: test_CollectionSearch")
    ds = {
            "collections": ["test_ansible_collections.test_test_test"],
        }
    dc = CollectionSearch()
    dc.post_validate(ds, False)
    print ("\nSUCCESS\n")

# Generated at 2022-06-22 11:30:22.649208
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # This tests:
    #   * that the constructor does not have a crash
    #   * that the class has the correct number of fields
    collection_search = CollectionSearch()
    assert hasattr(collection_search, 'collections'), "CollectionSearch does not have a 'collections' field"
    assert len(collection_search._get_attributes()) == 1, "CollectionSearch has more than 1 field but constructor does not set them"

# Generated at 2022-06-22 11:30:24.010479
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:25.312468
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test for default values
    cs = CollectionSearch()
    assert cs._collections is None

# Generated at 2022-06-22 11:30:39.296359
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # Ensure that collections is not empty
    assert c.collections is not None
    # Ensure that collections is a list
    assert isinstance(c.collections, list)
    # Ensure that collections is not empty
    assert len(c.collections) > 0
    # Ensure that default_collection is in collections
    assert c.default_collection in c.collections

# Generated at 2022-06-22 11:30:42.161821
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert not CollectionSearch.__bases__
    assert CollectionSearch._collections == _ensure_default_collection
    assert CollectionSearch._load_collections is not None

# Generated at 2022-06-22 11:30:44.512132
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == ['ansible.builtin']
    assert CollectionSearch(collections=['collection']).collections == ['collection', 'ansible.builtin']

# Generated at 2022-06-22 11:30:48.620521
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    def __init__(object):
        object._collections = FieldAttribute(isa='list', listof=string_types, priority=100,
                                             default=_ensure_default_collection, always_post_validate=True, static=True)
        object.ds = [ 'test_collection' ]
    __init__(CollectionSearch())

# Generated at 2022-06-22 11:30:56.757417
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class MockCollectionSearch(CollectionSearch):
        def __init__(self, data_source='data_source'):
            self.data_source = data_source
            super(MockCollectionSearch, self).__init__(loader=None)
    cs = MockCollectionSearch()
    assert cs.get_validated_value('collections', cs._collections, cs.data_source, None) == ['ansible.builtin', 'ansible.legacy']
    cs.data_source = None
    assert cs.get_validated_value('collections', cs._collections, cs.data_source, None) is None

# Generated at 2022-06-22 11:30:59.347143
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj.collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:31:02.260836
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search._collections = ['test', 'ansible.builtin']
    collection_search.post_validate()
    assert collection_search._collections == ['test', 'ansible.builtin']

# Generated at 2022-06-22 11:31:04.124048
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    _CollectionSearch = CollectionSearch();
    assert _CollectionSearch._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:05.817701
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs

# Generated at 2022-06-22 11:31:13.775232
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base
    from ansible.playbook.play_context import PlayContext

    t = CollectionSearch()
    b = Base()

    # _load_collections: Input: None
    # _load_collections: Input: Empty list
    # _load_collections: Input: PlayContext
    # _load_collections: Input: Valid list
    # _load_collections: Input: None, with _default_collection = True
    # _load_collections: Input: Templates in the list

    assert t._load_collections(None, None) == None
    assert t._load_collections(None, []) == None
    assert t._load_collections(None, PlayContext()) == None

# Generated at 2022-06-22 11:31:22.926237
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.__dict__['_collections'] is not None
    assert cs.__dict__['_collections'].default is not None
    assert cs._collections is not None
    assert cs._collections.default is not None


# Generated at 2022-06-22 11:31:25.390274
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    obj = CollectionSearch()

    assert obj.collections == ['ansible.builtin']
    assert obj._collections.value == ['ansible.builtin']

# Generated at 2022-06-22 11:31:26.920644
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    print(search._collections)

# Generated at 2022-06-22 11:31:29.668627
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    c._collections = "test.test"
    c._load_collections("test1.test1", "test2.test2")

# Generated at 2022-06-22 11:31:34.896907
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default == _ensure_default_collection
    assert collection_search._collections.always_post_validate == True
    assert collection_search._collections.static == True
    assert collection_search._collections.priority == 100
    assert collection_search._collections.listof == string_types
    assert collection_search._collections.isa == 'list'

# Generated at 2022-06-22 11:31:36.482742
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert _ensure_default_collection(['test_collection']) == ['test_collection', 'ansible.builtin']

# Generated at 2022-06-22 11:31:38.131639
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:31:44.759733
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create instance of class CollectionSearch
    search_collections = CollectionSearch()
    assert(isinstance(search_collections, CollectionSearch))

    # Test default value
    assert(search_collections._collections.default == ['ansible.builtin'])
    assert(search_collections._collections.value == ['ansible.builtin'])

    # Test default _load_collections()
    assert(search_collections._load_collections('collections', None) is None)

    # Test _load_collections()
    assert(search_collections._load_collections('collections', []) == _ensure_default_collection())
    assert(search_collections._load_collections('collections', ['foo','bar']) == _ensure_default_collection(['foo','bar']))

    #Test templatable

# Generated at 2022-06-22 11:31:46.603557
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert isinstance(cs._load_collections(None, None), list)

# Generated at 2022-06-22 11:31:50.302338
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    obj.collections = [
        'ansible_collections.test.test_collection_search',
        'ansible.builtin'
    ]
    obj.post_validate()

    print(obj.collections)

# Generated at 2022-06-22 11:32:12.312559
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert(test_obj.collections == ['ansible.builtin'])
    assert(test_obj.get_validated_value('collections', test_obj._collections, ['ansible.builtin'], None) == ['ansible.builtin'])
    assert(test_obj.get_validated_value('collections', test_obj._collections, ['ansible.builtin', 'ansible.legacy'], None) == ['ansible.builtin', 'ansible.legacy'])
    assert(test_obj.get_validated_value('collections', test_obj._collections, ['namespace.test'], None) == ['ansible.builtin', 'namespace.test'])

# Generated at 2022-06-22 11:32:15.768262
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        pass
    collectionsearch = TestCollectionSearch()
    assert collectionsearch._collections is not None
    assert collectionsearch._collections.default is _ensure_default_collection

# Generated at 2022-06-22 11:32:17.708316
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch(ds=None)

    assert cs._collections == 'ansible.builtin'

# Generated at 2022-06-22 11:32:20.487220
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    collect_list = []
    assert obj._load_collections(None, collect_list) == ['ansible.builtin']

# Generated at 2022-06-22 11:32:28.706985
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._load_collections('collections', None) is None
    assert collection_search._load_collections('collections', []) is None
    assert collection_search._load_collections('collections', ['ansible.legacy']) == ['ansible.legacy']
    assert collection_search._load_collections('collections', ['sample_collection']) == ['sample_collection', 'ansible.legacy']
    assert collection_search._load_collections('collections', ['sample_collection', 'ansible.legacy']) == ['sample_collection', 'ansible.legacy']

# Generated at 2022-06-22 11:32:30.439734
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    m = CollectionSearch()
    assert m._collections[0] == AnsibleCollectionConfig.default_collection

# Generated at 2022-06-22 11:32:35.441111
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()

    assert obj._collections.default == _ensure_default_collection
    assert obj._collections._is_static == True
    assert obj._collections.priority == 100
    assert obj._collections.always_post_validate == True
    assert obj._collections.isa == 'list'
    assert obj._collections.listof == string_types



# Generated at 2022-06-22 11:32:39.905612
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    first = CollectionSearch()
    print(first.collections)
    s = CollectionSearch(collections=["c1", "c2"])
    print(s.collections)
    s.collections = ["c3"]
    print(s.collections)


# Generated at 2022-06-22 11:32:41.862314
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    assert type(collections._collections) is FieldAttribute

# Generated at 2022-06-22 11:32:43.843210
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search_instance = CollectionSearch()
    assert collection_search_instance._collections is not None

# Generated at 2022-06-22 11:33:13.113182
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    dummy_data = {"collections": ["ansible_collections.my_namespace.my_collection"]}
    collection_search.load_data(dummy_data, validate=True)
    assert collection_search.get_collections() == ["ansible_collections.my_namespace.my_collection"]

# Generated at 2022-06-22 11:33:15.588616
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_obj = _ensure_default_collection()
    assert collection_obj == ['ansible.legacy', 'ansible_collections.ansible']

# Generated at 2022-06-22 11:33:17.300035
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections(None, None) == ['ansible.builtin']

# Generated at 2022-06-22 11:33:23.525383
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections == _ensure_default_collection()
    b = CollectionSearch(collections=['ns1.ns2.collection1', 'ns3.ns4.collection2'])
    assert b._collections == _ensure_default_collection(['ns1.ns2.collection1', 'ns3.ns4.collection2'])

# Generated at 2022-06-22 11:33:25.335583
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:26.155680
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    print(collectionSearch)

# Generated at 2022-06-22 11:33:27.591733
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections_search = CollectionSearch()
    assert collections_search.collections == None

# Generated at 2022-06-22 11:33:30.344179
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    # The following should not be in a constructor.
    # a._collections = _ensure_default_collection()
    a._load_collections("collections",'ansible.builtin')

# Generated at 2022-06-22 11:33:34.935273
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test the attribute collections
    a = CollectionSearch()
    assert isinstance(a._collections, list)
    assert len(a._collections) == 1
    assert a._collections[0] == 'ansible.builtin'


# Generated at 2022-06-22 11:33:36.289236
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x=CollectionSearch()
    assert x._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:30.292589
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test default values
    cs = CollectionSearch()
    assert cs._collections is None
    assert cs._collections is _ensure_default_collection()

# Generated at 2022-06-22 11:34:33.166393
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # print("here")
    cs = CollectionSearch()
    # print("cs._collections", cs._collections)
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:34.825868
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:40.303015
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    from ansible.playbook.role_include import RoleInclude
    from ansible.utils.collection_loader import AnsibleCollectionRef

    AnsibleCollectionRef.clear_cache()
    role_include = RoleInclude()
    role_include._load_collections(None, ["test.test"])

    print(role_include._collections)
    assert role_include._collections == ["test.test"]

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:34:50.329673
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = 'ansible.builtin'
    CollectionSearch(ds)
    # Make sure library collection is not specified
    # and default should be used
    assert CollectionSearch._collections.name == 'collections'
    assert CollectionSearch._collections.priority == 100
    assert CollectionSearch._collections.default == _ensure_default_collection
    assert CollectionSearch._collections.static is True
    assert CollectionSearch._collections.always_post_validate is True
    assert CollectionSearch._collections.isa == 'list'
    assert CollectionSearch._collections.listof == string_types
    assert CollectionSearch._collections.attribute == 'collections'
    assert CollectionSearch._collections.allow_duplicates is False
    assert CollectionSearch._collections.required is False
    assert CollectionSearch._collections.private is False
    assert CollectionSearch

# Generated at 2022-06-22 11:34:58.815687
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test if the constructor of CollectionSearch is executed successfully
    # If a CollectionSearch object is created successfully, the test passed.
    required_fields = ['collections']
    for required_field in required_fields:
        if not hasattr(CollectionSearch, required_field):
            raise AssertionError("%s is not part of fields of the CollectionSearch class" % required_field)
    try:
        collection_search_obj = CollectionSearch()
        assert isinstance(collection_search_obj, CollectionSearch)
    except Exception as e:
        raise Exception(e)



# Generated at 2022-06-22 11:35:01.244882
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection._load_collections("collections", ["test.collection"]) == ["test.collection", "ansible.builtin"]

# Generated at 2022-06-22 11:35:05.653911
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search._collections, FieldAttribute)
    assert collection_search._collections._default == _ensure_default_collection
    assert callable(collection_search._collections._default)

# Generated at 2022-06-22 11:35:09.438427
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Initialise object of class CollectionSearch
    obj = CollectionSearch()
    expected = ['ansible_builtin', 'community.aws', 'community.general']
    # Check if the object of class CollectionSearch is initialised
    assert obj._collections == expected

# Generated at 2022-06-22 11:35:11.211142
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col = CollectionSearch()
    assert col._load_collections() == _ensure_default_collection()

# Generated at 2022-06-22 11:37:04.153357
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    list = CollectionSearch()
    assert list._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:37:06.025178
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:37:08.072801
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    aCollectionSearch = CollectionSearch()

    assert aCollectionSearch._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:37:11.347767
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collSearch = CollectionSearch()
    list = collSearch._load_collections("collections", None)
    assert list is not None
    assert len(list) == 2

# Generated at 2022-06-22 11:37:12.822982
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert _ensure_default_collection() == obj._collections

# Generated at 2022-06-22 11:37:13.757236
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search_test = CollectionSearch()
    assert isinstance(collection_search_test, CollectionSearch)

# Generated at 2022-06-22 11:37:15.911730
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    element = CollectionSearch()
    element._collections = ["collection1", "collection2"]
    assert element._collections == ["collection1", "collection2"]

# Generated at 2022-06-22 11:37:16.856052
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch
    CollectionSearch()

# Generated at 2022-06-22 11:37:19.185377
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert "ansible.builtin" in cs._collections
    assert "ansible.legacy" in cs._collections

# Generated at 2022-06-22 11:37:22.896354
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    print(type(cs))
    print(type(cs._collections))


if __name__ == '__main__':
    test_CollectionSearch()