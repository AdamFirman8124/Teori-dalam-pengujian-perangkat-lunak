

# Generated at 2022-06-22 11:29:51.041730
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # Test for collection list is empty
    assert cs._load_collections('collections', None) is None

# Generated at 2022-06-22 11:30:01.061021
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import os
    import json
    import sys
    import shutil

    # Create a temp directory
    tmp_path = os.path.realpath(os.path.expanduser('~/.ansible/tmp'))
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)

    # Create a temp config file
    config_file = os.path.join(tmp_path, 'ansible.cfg')
    config_data = {'defaults': {'collections_path': '~/.ansible/collections'}}
    with open(config_file, 'w') as f:
        json.dump(config_data, f)

    # Create a temp collection

# Generated at 2022-06-22 11:30:01.778039
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()

# Generated at 2022-06-22 11:30:02.827983
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None

# Generated at 2022-06-22 11:30:05.592571
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.play_context import PlayContext
    context_obj = PlayContext()
    assert context_obj.collections == None

# Generated at 2022-06-22 11:30:11.332376
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class CollectionSearchTest(CollectionSearch):
        pass

    cst = CollectionSearchTest()
    assert cst._load_collections(None, []) == []
    assert cst._load_collections(None, ['collection_name']) == ['collection_name']
    assert cst._load_collections(None, ['']) == ['']



# Generated at 2022-06-22 11:30:14.159149
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_list = ['test.collection_name']
    collection_search = CollectionSearch()
    collection_search._collections = collection_list
    assert collection_search._load_collections(None, []) == collection_list

# Generated at 2022-06-22 11:30:15.991896
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections is not None
    assert c.collections is not []

# Generated at 2022-06-22 11:30:20.260049
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    d = {'a': 'b'}
    instance = CollectionSearch(d)
    assert 'collections' in d
    assert instance._collections is not None

# Generated at 2022-06-22 11:30:29.815966
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # Test case 1: Assert _collections attribute is returned
    cs = CollectionSearch()
    cs._collections = ['foo', 'bar']
    assert cs._collections == ['foo', 'bar']

    # Test case 2: Assert _collections attribute is properly set
    attribute = FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection,
                                  always_post_validate=True, static=True)
    cs._collections = attribute
    assert cs._collections == attribute

    # Test case 3: Assert _load_collections method is working properly
    cs._collections = ['foo', 'ansible.builtin']
    attr = 'foo'
    ds = 'bar'

# Generated at 2022-06-22 11:30:37.110545
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    p = CollectionSearch()

# Generated at 2022-06-22 11:30:46.650600
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionsearch = CollectionSearch()
    assert collectionsearch._load_collections(None, None) == None
    #assert collectionsearch._load_collections(None, []) == []
    assert collectionsearch._load_collections(None, ['ansible.builtin']) == ['ansible.builtin']
    assert collectionsearch._load_collections(None, ['ansible.builtin', 'ansible.ansible_collections.foo.bar']) == ['ansible.builtin', 'ansible.ansible_collections.foo.bar']
    assert collectionsearch._load_collections(None, ['ansible.ansible_collections.foo.bar']) == ['ansible.ansible_collections.foo.bar']


# Generated at 2022-06-22 11:30:48.065085
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default() is not None

# Generated at 2022-06-22 11:30:50.017129
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = CollectionSearch()
    assert ds._collections == _ensure_default_collection([])

# Generated at 2022-06-22 11:30:50.469585
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # TODO: implement unit test
    assert True == True

# Generated at 2022-06-22 11:30:52.675507
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == [ 'ansible.builtin', 'ansible.legacy' ]

# Generated at 2022-06-22 11:30:58.419397
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections(None, None) == None
    assert 'ansible.builtin' in cs._load_collections(None, ['ansible.builtin'])
    assert 'ansible.builtin' in cs._load_collections(None, ['ansible.builtin', 'test.testc'])
    assert 'ansible.legacy' in cs._load_collections(None, ['ansible.builtin'])
    assert 'ansible.legacy' not in cs._load_collections(None, [])
    assert 'ansible.legacy' in cs._load_collections(None, ['test.testc'])

# Generated at 2022-06-22 11:31:09.371535
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base
    from ansible.playbook.role import Role
    from ansible.playbook.tasks import Task
    from ansible.template import Templar

    assert not hasattr(Base, '_collections')
    assert not hasattr(Task, '_collections')
    assert not hasattr(Role, '_collections')

    class CollectionSearchBase(Base, CollectionSearch):
        # Base will populate _collections, so we need to explicitly
        # list it so Base's constructor doesn't try to create it.
        _fields = ['collections']

    try:
        CollectionSearchBase(1, 2)
    except TypeError:
        pass
    else:
        raise Exception("Should not be able to instantiate a Base class")


# Generated at 2022-06-22 11:31:09.793936
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:31:11.773351
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    collection_search = CollectionSearch()
    collection_search.post_validate(ds=None, var_name='collections', always_post_validate=True)

# Generated at 2022-06-22 11:31:20.692637
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections is not None
    assert CollectionSearch._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:31:26.759493
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._ensure_default_collection(None) == ['ansible.builtin']

    collection_list = ['ansible_test']
    assert CollectionSearch._ensure_default_collection(collection_list) == ['ansible_test', 'ansible.builtin']


if __name__ == "__main__":
    import pytest
    pytest.main(["-s", __file__])

# Generated at 2022-06-22 11:31:28.246954
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search is not None

# Generated at 2022-06-22 11:31:30.124474
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    pass

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:33.080374
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._ensure_default_collection(['a']) == ['a', 'ansible.legacy']
    assert CollectionSearch._ensure_default_collection() == ['ansible.legacy']

# Generated at 2022-06-22 11:31:35.241055
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default == _ensure_default_collection()

# Generated at 2022-06-22 11:31:36.103194
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    try:
        test_collection_search = CollectionSearch()
    finally:
        assert test_collection_search



# Generated at 2022-06-22 11:31:42.189108
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search
    assert collection_search._collections == None

    # Need to specify the type of 'ds', otherwise we will get
    #   TypeError: 'unexpected keyword argument'
    ds = {}
    collections = collection_search._load_collections(None, ds)
    assert collections == None

    # Add a value to 'collections'
    ds = {'collections':['']}
    collections = collection_search._load_collections(None, ds)
    assert collections == ['']

# Generated at 2022-06-22 11:31:47.206153
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    display.display("test_CollectionSearch: type of collection_search: %s" % (type(collection_search)))
    display.display("test_CollectionSearch: repr of collection_search: %s" % (collection_search))
    display.display("test_CollectionSearch: _collections of collection_search: %s" % (collection_search._collections))

# Generated at 2022-06-22 11:31:49.071409
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()



# Generated at 2022-06-22 11:32:09.897815
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # Test with no collection_list
    assert _ensure_default_collection() == ['ansible_collections.ansible.builtin', 'ansible.legacy']

    # Test with collection_list
    assert _ensure_default_collection(['awx.awx']) == ['awx.awx', 'ansible_collections.ansible.builtin', 'ansible.legacy']

    # Test with empty collection_list
    assert _ensure_default_collection([]) == ['ansible_collections.ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:21.765439
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test - no params
    search = CollectionSearch()
    assert search._load_collections('collections', []) == None
    assert search._load_collections('collections', ['ansible.builtin']) == None
    assert search._load_collections('collections', ['ansible.legacy']) == None
    assert search._load_collections('collections', ['ansible.builtin', 'ansible.legacy']) == None
    assert search._load_collections('collections', ['test.testcollection']) == None
    assert search._load_collections('collections', ['test.testcollection', 'ansible.builtin']) == None
    assert search._load_collections('collections', ['test.testcollection', 'ansible.legacy']) == None

# Generated at 2022-06-22 11:32:27.575915
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    play_context._collections = _ensure_default_collection(['new_col.c1.c2.c3'])
    assert play_context._collections == ['new_col.c1.c2.c3','ansible.builtin','ansible.legacy'], 'Failed to add ansible.legacy and ansible.builtin'

# Generated at 2022-06-22 11:32:28.979120
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col = CollectionSearch()
    assert col._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:30.849750
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearchInstance = CollectionSearch()
    assert collectionSearchInstance._load_collections(attr="a", ds="b") is None

# Generated at 2022-06-22 11:32:33.764956
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()

    # Check that the class was initialized properly
    assert(str(type(s._collections)) == "<class 'ansible.playbook.attribute.FieldAttribute'>")

# Generated at 2022-06-22 11:32:34.550074
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a is not None

# Generated at 2022-06-22 11:32:37.391367
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:47.820583
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test collection list is empty
    attr_class = CollectionSearch()
    assert attr_class.collections == []

    # Test collection list has one item
    attr_class = CollectionSearch(collections=['ansible.builtin'])
    assert attr_class.collections == ['ansible.builtin']

    # Test collection list has multiple items
    attr_class = CollectionSearch(collections=['ansible.builtin', 'test.test_collection'])
    assert attr_class.collections == ['test.test_collection', 'ansible.builtin']

    # Test collection list with template item
    attr_class = CollectionSearch(collections=['{{ ansible_collection }}'])
    assert attr_class.collections == ['{{ ansible_collection }}']

# Generated at 2022-06-22 11:32:51.847149
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    for at in _ensure_default_collection():
        if at in AnsibleCollectionConfig.default_collection:
            assert at in AnsibleCollectionConfig.default_collection[at]
        else:
            assert at in AnsibleCollectionConfig.default_collection



# Generated at 2022-06-22 11:33:22.853637
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test default value
    coll_search = CollectionSearch()
    assert coll_search._collections == _ensure_default_collection()

    # Test with value
    coll_search = CollectionSearch(collections=['foobar'])
    assert coll_search._collections == ['foobar']

# Generated at 2022-06-22 11:33:28.046027
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()
    assert not s._load_collections(None, 'ansible.builtin')
    assert not s._load_collections(None, 'ansible.builtin')
    assert not s._load_collections(None, ['ansible.builtin'])
    assert not s._load_collections(None, ['ansible.builtin', 'cisco.ucs'])

# Generated at 2022-06-22 11:33:29.030491
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert hasattr(CollectionSearch, '_collections')

# Generated at 2022-06-22 11:33:35.158819
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test input_data
    input_data = {
        'collections': ['test.test1', 'test.test2'],
    }

    # Expected results
    exp_collections = ['ansible.builtin', 'ansible.legacy', 'test.test1', 'test.test2']

    # Instance of class CollectionSearch
    search_obj = CollectionSearch()

    # Validating input data
    val_data = search_obj.validate(input_data)

    # Check for expected output
    assert exp_collections == val_data.get('collections')

# Generated at 2022-06-22 11:33:36.141434
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearchObj = CollectionSearch()

# Generated at 2022-06-22 11:33:46.011201
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert 'ansible.builtin' == CollectionSearch._ensure_default_collection(collection_list = ['ansible.builtin', 'ansible.builtin.unix'])
    assert 'ansible.legacy' == CollectionSearch._ensure_default_collection(collection_list = ['ansible.legacy'])
    assert 'ansible.builtin' == CollectionSearch._ensure_default_collection(collection_list = [])
    assert ['my.collection', 'ansible.builtin'] == CollectionSearch._ensure_default_collection(collection_list = ['my.collection'])
    assert ['my.collection', 'ansible.legacy'] == CollectionSearch._ensure_default_collection(collection_list = ['my.collection'])


# Generated at 2022-06-22 11:33:47.796906
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:33:50.679165
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.collections = ['collection']
    assert cs._load_collections(cs.collections, cs.collections) == cs.collections

# Generated at 2022-06-22 11:33:59.297815
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # empty collection search
    cs = CollectionSearch()
    assert cs.collections is None

    # collection search with a list of collection names
    cs = CollectionSearch(collections=['ansible.builtin', 'ansible.netcommon'])
    assert cs.collections[0] == 'ansible.builtin'
    assert cs.collections[1] == 'ansible.netcommon'

    # collection search with a list of collection names
    cs = CollectionSearch(collections=['ansible.builtin', 'ansible.netcommon'])
    assert cs.collections[0] == 'ansible.builtin'
    assert cs.collections[1] == 'ansible.netcommon'

# Generated at 2022-06-22 11:34:02.657210
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.args['default']() == ['ansible_collections.ansible.builtin']

# Generated at 2022-06-22 11:35:03.741994
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.base import Base
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import collection_loader, module_loader

    # Default initialization without collection list
    # When no collection list is provided, it should use default collection
    # See https://github.com/ansible/ansible/issues/59927
    test_obj = RoleInclude()
    assert(len(test_obj._collections) == 1)
    assert(test_obj._collections[0] == AnsibleCollectionConfig.default_collection)

    test_obj = TaskInclude()
    assert(len(test_obj._collections) == 1)

# Generated at 2022-06-22 11:35:07.583715
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

    print (type(collection_search._load_collections("CollectionSearch", {})))
    print (type(collection_search.collections))


if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:35:08.212617
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:35:09.707388
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:35:12.678717
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()
    assert c._collections == ['ansible_galaxy.builtin', 'ansible_galaxy.legacy']
    assert c.__class__.__name__ == 'CollectionSearch'



# Generated at 2022-06-22 11:35:14.795026
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections._default == _ensure_default_collection

# Generated at 2022-06-22 11:35:16.332546
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    res = CollectionSearch()
    assert res is not None

# Generated at 2022-06-22 11:35:19.963998
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestClass(object):
        pass
    for args in [(), (1,), ['asd'],['ansible.builtin']]:
        obj = CollectionSearch(TestClass(), args)
        assert obj._collections == _ensure_default_collection(args)
        assert obj._collections == _ensure_default_collection(args)

# Generated at 2022-06-22 11:35:23.743517
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs
    assert len(cs._collections) > 0
    assert 'ansible.builtin' in cs._collections
    assert 'ansible.builtin' not in _ensure_default_collection()

# Generated at 2022-06-22 11:35:26.409575
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # testing constructor
    t = CollectionSearch()
    assert t._collections == _ensure_default_collection()
    assert t._load_collections(None, ['ansible.posix']) == ['ansible.posix']

# Generated at 2022-06-22 11:37:27.772024
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    mock_collections = ['col1', 'col2', 'col3']
    collection_search_object = CollectionSearch(collections=mock_collections)
    assert collection_search_object._collections == mock_collections
    assert collection_search_object._collections_computed is False
    assert collection_search_object._collections_finalized is False
    assert collection_search_object._collections_resolved is False
    assert collection_search_object._collections_value == mock_collections
    assert collection_search_object.collections == mock_collections

# Generated at 2022-06-22 11:37:35.002189
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    def check_attribute_values(obj):
        # Assert the default values of static attributes
        assert obj._collections.default == _ensure_default_collection
        assert obj._collections.static is True
        assert obj._collections.priority == 100
        assert obj._collections.field_name == 'collections'
        assert obj._collections.always_post_validate is True

    obj = CollectionSearch()
    check_attribute_values(obj)

# Generated at 2022-06-22 11:37:42.138757
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    c._collections = 'collection'
    assert c._load_collections(None, c._collections) == ['collection','ansible.builtin']
    c._collections = ['collection1','collection2','collection3']
    assert c._load_collections(None, c._collections) == ['collection1','collection2','collection3','ansible.builtin']
    c._collections = None
    assert c._load_collections(None, c._collections) == ['ansible.builtin']

# Generated at 2022-06-22 11:37:51.485028
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # test default collections
    assert cs._load_collections('collections', []) == _ensure_default_collection([])
    assert cs._load_collections('collections', None) == _ensure_default_collection([])
    # test collections with a passed in value
    assert cs._load_collections('collections', ['foo.bar']) == _ensure_default_collection(['foo.bar'])
    assert cs._load_collections('collections', ['ansible.builtin']) == ['ansible.builtin']

# Generated at 2022-06-22 11:37:55.393515
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    """CollectionSearch: tests the constructor of class CollectionSearch"""
    search = CollectionSearch()
    assert search is not None
    assert isinstance(search, CollectionSearch)
    assert search._collections is not None
    assert _ensure_default_collection(collection_list=None) == search._collections


# Generated at 2022-06-22 11:37:56.809949
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # pylint: disable=unused-variable
    cs = CollectionSearch()

# Generated at 2022-06-22 11:37:58.945339
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections.default == _ensure_default_collection

# Generated at 2022-06-22 11:37:59.928238
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections()

# Generated at 2022-06-22 11:38:01.230536
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:38:03.295030
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search_collection = CollectionSearch()
    assert search_collection._collections == _ensure_default_collection(search_collection._collections)