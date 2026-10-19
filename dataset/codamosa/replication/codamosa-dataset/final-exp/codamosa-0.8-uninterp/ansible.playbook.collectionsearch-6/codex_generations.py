

# Generated at 2022-06-22 11:29:53.509529
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    t = CollectionSearch()
    assert t._collections == ['ansible.builtin']
    assert not t._load_collections(None, None)
    assert t._load_collections(None, ['a']) == ['a', 'ansible.builtin']
    assert t._load_collections(None, ['a', 'ansible.builtin']) == ['a', 'ansible.builtin']
    assert t._load_collections(None, ['a', 'b', 'ansible.builtin']) == ['a', 'b', 'ansible.builtin']


# Generated at 2022-06-22 11:29:55.441930
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    print(cs.collections)

# Generated at 2022-06-22 11:30:04.042502
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col_search = CollectionSearch()
    assert col_search._collections._static is True
    assert col_search._collections.always_post_validate is True
    assert col_search._collections.priority == 100
    assert col_search._collections.default is _ensure_default_collection
    default_collection = AnsibleCollectionConfig.default_collection
    if default_collection is None:
        assert col_search._collections.default() == []
    else:
        assert col_search._collections.default() == [default_collection]
    assert col_search._collections.__class__.__name__ == 'FieldAttribute'
    assert col_search._collections.isa == 'list'
    assert col_search._collections.listof == string_types

# Generated at 2022-06-22 11:30:06.726936
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print('Start testing.')
    cur_cs = CollectionSearch()
    cur_cs._load_collections('collections', None)
    print('End testing.')

# Generated at 2022-06-22 11:30:11.914897
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # We are always a mixin with Base, so we can validate this untemplated
    # field early on to guarantee we are dealing with a list.
    ds = cs.get_validated_value('collections', cs._collections, [], None)
    assert ds == _ensure_default_collection(collection_list=[])

# Generated at 2022-06-22 11:30:17.343171
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    """ Unit test for constructor of class CollectionSearch """
    collection_search = CollectionSearch()

    # Assert that collections is a list
    assert isinstance(collection_search.collections, list)

    # Assert that collections has the correct value
    for item in ("ansible", "ansible.builtin", "ansible.legacy"):
        assert item in collection_search.collections

# Generated at 2022-06-22 11:30:28.401114
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.collections = 'ansible'
    assert cs._collections == ['ansible']
    cs.collections = 'ansible,test'
    assert cs._collections == ['ansible', 'test']
    cs.collections = None
    assert cs._collections == ['ansible_collections.test']
    cs.collections = 'not.a.collection'
    assert cs._collections == ['ansible_collections.not.a.collection']
    cs.collections = 'not.a.collection,another.collection'
    assert cs._collections == ['ansible_collections.not.a.collection', 'ansible_collections.another.collection']
    cs.collections = [1, 2, 3]
    assert cs._collections == [1, 2, 3]
    cs

# Generated at 2022-06-22 11:30:30.979880
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.include import TaskInclude
    role_definition = RoleDefinition()
    assert role_definition._collections == ['ansible.posix']

# Generated at 2022-06-22 11:30:34.631789
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = AnsibleCollectionConfig.default_collection
    obj = CollectionSearch()
    assert collections == obj._collections

# Generated at 2022-06-22 11:30:44.187420
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import unittest
    import ansible.playbook.role
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.role_include
    import ansible.playbook.task_include
    import ansible.playbook.block_include

    class TestCollectionSearch(unittest.TestCase):
        def test_collections(self):
            # Constructor from class CollectionSearch
            cs = CollectionSearch()
            # From attribute data 'collections'
            # Has its own getter '_load_collections'
            self.assertEqual(['ansible.builtin'], cs._collections)

    unittest.main()

# Generated at 2022-06-22 11:30:55.344612
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # collection_list = ['ansible.base', 'ansible.builtin', 'ansible.legacy']
    collection_list = ['ansible.base']
    assert cs._load_collections(None, collection_list) == ['ansible.base', 'ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:56.605579
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch() is not None

# Generated at 2022-06-22 11:31:03.818619
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    print("x is " + str(x))
    print("type(x) is " + str(type(x)))
    assert str(x) == "&lt;ansible.plugins.loader.collection_search.CollectionSearch object at 0x7f06f0b32150&gt;"
    assert str(type(x)) == "&lt;class 'ansible.plugins.loader.collection_search.CollectionSearch'&gt;"
test_CollectionSearch()



# Generated at 2022-06-22 11:31:06.503329
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    assert collections.collections == 'ansible.builtin,ansible.legacy,ansible.builtin'

# Generated at 2022-06-22 11:31:10.739289
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    """Test class CollectionSearch."""
    # Get default CollectionSearch object without parameters
    collection_search = CollectionSearch()
    # Check if collections_list is always sanitized
    assert collection_search.collections is not None
    # Check if collections_list always contains the default collection
    assert 'ansible.netcommon' in collection_search.collections

# Generated at 2022-06-22 11:31:20.066849
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude

    class TestCollectionSearch:

        def __init__(self, *args, **kwargs):
            self.ds = {}
            self.ds.update(kwargs.get('loader', {}).get('_ds', {}))
            self.ds.update(kwargs.get('_ds', {}))
            self.loader = kwargs.get('loader', None)
            self.playbook = kwargs.get('playbook', None)
            self.collections = kwargs.get('collections', None)

# Generated at 2022-06-22 11:31:21.553797
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.value == ['ansible.builtin']

# Generated at 2022-06-22 11:31:22.651233
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:25.550017
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    """
        Unit test for constructor of class CollectionSearch
    """
    # test if CollectionSearch is created with empty collection list
    cs = CollectionSearch()
    assert cs.collections._values == []

# Generated at 2022-06-22 11:31:27.078916
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.collections is None

# Generated at 2022-06-22 11:31:35.195689
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections is not None

# Generated at 2022-06-22 11:31:36.436964
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:37.983551
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    SearchObject = CollectionSearch()
    # test default value
    assert SearchObject.collections == ['ansible.legacy']

# Generated at 2022-06-22 11:31:42.203917
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # this needs to be populated before we can resolve tasks/roles/etc
    _collections = FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection,
                                  always_post_validate=True, static=True)
    collectionSearch = CollectionSearch()
    print (_ensure_default_collection())
    collectionSearch._load_collections('collections',_ensure_default_collection())

# Generated at 2022-06-22 11:31:45.247531
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a_obj = CollectionSearch()
    assert a_obj.__class__.__name__ == "CollectionSearch"
    assert a_obj._collections == _ensure_default_collection()


# Generated at 2022-06-22 11:31:54.900185
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    from ansible.playbook.base import Base
    collections = CollectionSearch()
    test_instance = Base()
    test_instance._parent_datastore = None
    test_instance._attributes['collections'] = collections
    test_instance.validate()
    assert (test_instance._attributes['collections'].get_value() ==
            ['ansible.builtin', 'ansible.legacy', 'ansible_collections.community.general'])
    test_instance._attributes['collections'].set_value(['ansible_collections.community.general','ansible.builtin'])
    test_instance.validate()

# Generated at 2022-06-22 11:32:03.031130
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    collections= [ 'ansible.builtin', 'collection_name' ]
    assert cs._load_collections(None, collections) == collections
    collections= None
    assert cs._load_collections(None, collections) == collections
    collections= []
    assert cs._load_collections(None, collections) == ['ansible.builtin']
    assert cs._load_collections(None, collections) == ['ansible.builtin']

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:05.265600
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    res = CollectionSearch()
    assert res._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:07.406651
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs._load_collections('collections', ['foo', 'bar'])

# Generated at 2022-06-22 11:32:08.850123
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:23.619614
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections is None

# Generated at 2022-06-22 11:32:26.962599
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == ['ansible_collections.foo.bar']

    cs = CollectionSearch(collections=['ansible.builtin'])
    assert cs._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:32:28.121387
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    assert x is not None

# Generated at 2022-06-22 11:32:30.678457
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert 'ansible.builtin' in CollectionSearch().collections
    assert 'ansible.builtin' in CollectionSearch(collections=['ansible.builtin']).collections
# test_CollectionSearch

# Generated at 2022-06-22 11:32:33.285092
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # pylint: disable=protected-access
    cs = CollectionSearch()
    assert cs._collections._default == _ensure_default_collection

# Generated at 2022-06-22 11:32:35.243945
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

    # Test for _load_collections method
    collection_search._load_collections('collections', 'ansible_collections.community.general')

# Generated at 2022-06-22 11:32:38.627727
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create an instance of the CollectionSearch class
    obj = CollectionSearch()

    # Make sure the value of the object instance is as expected
    assert obj.collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:41.724846
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    try:
        var = CollectionSearch()
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError', 'test failed: collectionSearch constructor failed'

# Generated at 2022-06-22 11:32:47.006966
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import unittest
    from ansible.module_utils._text import to_bytes

    class TestCollectionSearch(unittest.TestCase):

        def test_CollectionSearch(self):
            x = CollectionSearch()
            self.assertEqual(to_bytes(x._collections), b'ansible_collections.ansible.builtin')
    unittest.main(exit=False)

# Generated at 2022-06-22 11:32:47.863313
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:33:16.048840
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert(search._collections.default_value == _ensure_default_collection(None))

# Generated at 2022-06-22 11:33:18.260434
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    z = CollectionSearch()
    assert z.get_validated_value('collections', z._collections, "", "") is None

# Generated at 2022-06-22 11:33:22.018958
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print("\n        Running unit test for constructor of class CollectionSearch")
    m = CollectionSearch()
    print("        Testing collections attribute for class CollectionSearch")
    assert m.collections is None
    print("        Testing _collections attribute for class CollectionSearch")
    assert m._collections is None
    print("        Testing _load_collections method for class CollectionSearch")
    assert m._load_collections("collections", ["legacy", "builtin"]) is not None
    print("        SUCCESS: CollectionSearch class constructed and methods tested\n")

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:33:24.657645
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create instance
    instance = CollectionSearch()

    # Should return a list of collections
    assert instance._load_collections(None, None) == _ensure_default_collection()

# Generated at 2022-06-22 11:33:29.822480
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # c.collections is a field attribute
    # test that it is initialized to a list
    assert isinstance(c.collections, list)
    # test that the default value contains the default collection
    assert AnsibleCollectionConfig.default_collection in c.collections
    # test that builtin is the last element in the default list
    assert "ansible.builtin" == c.collections[-1]

# Generated at 2022-06-22 11:33:31.661777
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = CollectionSearch()
    print(ds._collections)

# Generated at 2022-06-22 11:33:33.025308
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test is not None

# Generated at 2022-06-22 11:33:34.886009
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    assert isinstance(instance, CollectionSearch)

# Generated at 2022-06-22 11:33:42.284568
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # Test default value
    collections = CollectionSearch()._load_collections("collections", [])
    assert collections == ['ansible.builtin', 'ansible.legacy']

    # Test when collection_list is None
    collections = CollectionSearch()._load_collections("collections", None)
    assert collections == ['ansible.builtin', 'ansible.legacy']

    # Test when AnsibleCollectionConfig.default_collection is set
    AnsibleCollectionConfig.default_collection = "my.namespace"
    collections = CollectionSearch()._load_collections("collections", [])
    assert collections == ['my.namespace', 'ansible.builtin', 'ansible.legacy']
    collections = CollectionSearch()._load_collections("collections", ['my.namespace'])

# Generated at 2022-06-22 11:33:44.267014
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._ensure_default_collection() == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:34:40.783020
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class Test(CollectionSearch):
        pass

    t = Test(collections=None)
    assert t.collections is not None

# Generated at 2022-06-22 11:34:43.020429
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    assert collectionSearch._load_collections("collections", ["test-collection"]) == ["test-collection"]

# Generated at 2022-06-22 11:34:44.677269
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert isinstance(cs, CollectionSearch)

# Generated at 2022-06-22 11:34:46.240724
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default is _ensure_default_collection
    assert CollectionSearch._collections.static is True

# Generated at 2022-06-22 11:34:56.220365
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

    # Check type of private member variable
    assert isinstance(collection_search._collections, FieldAttribute)
    assert isinstance(collection_search._collections.isa, str)
    assert collection_search._collections.isa == 'list'
    assert isinstance(collection_search._collections.listof, type)
    assert collection_search._collections.listof == string_types
    assert isinstance(collection_search._collections.priority, int)
    assert collection_search._collections.priority == 100
    assert isinstance(collection_search._collections.default, Callable)
    assert collection_search._collections.default == _ensure_default_collection
    assert collection_search._collections.static is True

# Generated at 2022-06-22 11:35:03.970720
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class CollectionSearchUser(CollectionSearch):
        def __init__(self):
            pass

    test_obj = CollectionSearchUser()
    assert test_obj._collections.default_arg == _ensure_default_collection
    assert test_obj._collections.default_ret == _ensure_default_collection(collection_list=None)

    # Note: This does not actually load the collections
    assert test_obj._load_collections('collections', []) is None



# Generated at 2022-06-22 11:35:11.583407
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # fail because of empty list
    try:
        x = CollectionSearch()
    except ValueError as e:
        assert "List may not be empty" in str(e)

    # fail because of invalid list values
    try:
        x = CollectionSearch(["invalid", "list", "values"])
    except ValueError as e:
        assert "Invalid value for type list" in str(e)

    # success because of valid list values
    x = CollectionSearch(["valid", "list", "values"])
    assert "valid" in x._collections

# Generated at 2022-06-22 11:35:17.228957
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    assert isinstance(instance.__dict__['_collections'], FieldAttribute)
    assert instance.__dict__['_collections'].default(_ensure_default_collection) == _ensure_default_collection()
    assert instance._collections == _ensure_default_collection()
    assert instance._load_collections('_collections', []) == _ensure_default_collection()

# Generated at 2022-06-22 11:35:22.554854
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default == cs._ensure_default_collection()
    assert cs._collections.priority == 100
    assert cs._collections.listof == string_types
    assert cs._collections.always_post_validate == True
    assert cs._collections.static == True

# Generated at 2022-06-22 11:35:29.027941
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # we need a valid context to create a CollectionSearch instance
    from ansible.context import CLIContext

    c = CLIContext()
    cs = CollectionSearch()
    assert cs._collections == ["ansible_collections.community.general"]
    assert cs._load_collections("_collections", []) == None
    assert cs._load_collections("_collections", [""]) == [""]
    assert cs._load_collections("_collections", ["", ""]) == ["", ""]

# Generated at 2022-06-22 11:37:24.789313
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default() is not None

# Generated at 2022-06-22 11:37:30.271153
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert test_obj._load_collections(attr='collections', ds=None) is None
    assert test_obj._load_collections(attr='collections', ds=[]) is None
    assert test_obj._load_collections(attr='collections', ds=['ansible.builtin']) is None
    assert test_obj._load_collections(attr='collections', ds=['ansible.legacy']) is None

# Generated at 2022-06-22 11:37:30.859089
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

# Generated at 2022-06-22 11:37:31.872072
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections

# Generated at 2022-06-22 11:37:42.867480
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class MyTest(CollectionSearch):
        def __init__(self, a=None, b=None, c=None, collections=None):
            self.a = a
            self.b = b
            self.c = c

            # Should call the constructor
            super(MyTest, self).__init__(collections=collections)

    test_obj = MyTest(a='test', b='test', c='test', collections=['col1', 'col2'])
    assert test_obj.a == 'test'
    assert test_obj.b == 'test'
    assert test_obj.c == 'test'

    assert test_obj.collections == ['col1', 'col2', 'ansible.builtin']

# Test for the post validation function for templates for the collections

# Generated at 2022-06-22 11:37:44.575171
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    obj = CollectionSearch()

    assert obj._collections == None

# Generated at 2022-06-22 11:37:46.165513
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_object = CollectionSearch()
    assert test_object._collections.default == _ensure_default_collection()

# Generated at 2022-06-22 11:37:51.210584
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = dict()
    ds['collections'] = ['testing.ansible_collections.a.b.c']
    obj = CollectionSearch()
    ob = obj._load_collections(None,ds)
    for i in ob:
        assert i in ds['collections']

# Generated at 2022-06-22 11:37:54.555590
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest

    collection_search = CollectionSearch()
    assert collection_search.collections == ['ansible.legacy']
    assert collection_search.get_validated_value('collections', 'ansible.legacy') == ['ansible.legacy']

# Generated at 2022-06-22 11:37:55.979193
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections is not None  # pylint: disable=protected-access