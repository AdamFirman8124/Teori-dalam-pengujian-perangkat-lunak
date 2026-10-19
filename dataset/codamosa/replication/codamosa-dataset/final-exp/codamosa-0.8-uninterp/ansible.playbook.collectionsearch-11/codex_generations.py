

# Generated at 2022-06-22 11:29:48.369815
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections == None

# Generated at 2022-06-22 11:29:49.828317
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs = CollectionSearch(collections=['collection_1'])

# Generated at 2022-06-22 11:29:53.029462
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:29:54.587194
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    test_CollectionSearch.__name__ = 'test_CollectionSearch'
    assert instance.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:29:55.929195
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()

    assert collection_search is not None

# Generated at 2022-06-22 11:29:57.843075
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection(None)

# Generated at 2022-06-22 11:30:00.705383
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    T = type('Test', (CollectionSearch,), {})
    instance = T()
    # The default collection should be the primary one
    assert instance.collections == [AnsibleCollectionConfig.default_collection]

# Generated at 2022-06-22 11:30:02.761972
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
   c = CollectionSearch()
   assert c.collections is None

# Generated at 2022-06-22 11:30:07.989852
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    # For test, we do not declared a collections element in the incoming
    # task file. So, we are going to test the default value of collections.
    # Make sure that the default value is the default collection.
    assert collectionSearch.collections == ['ansible.posix']

# Generated at 2022-06-22 11:30:10.861333
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections.default.__name__ == '_ensure_default_collection'
    assert c._load_collections(None, None) == None

# Generated at 2022-06-22 11:30:24.562075
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from units.mock.loader import DictDataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DictDataLoader({
        # no files loaded here
    })

    collections = CollectionSearch()
    collections.post_validate(dict(), PlayContext())

    assert len(collections.collections) == 1
    assert collections.collections[0] == 'ansible.builtin'


# Generated at 2022-06-22 11:30:26.216013
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:27.532304
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert isinstance(search._collections, FieldAttribute)

# Generated at 2022-06-22 11:30:29.672083
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj.get_validated_value('collections', obj._collections, [], None) == ['ansible_collections.foo.bar']

# Generated at 2022-06-22 11:30:33.073759
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    '''
    Test whether CollectionSearch class is properly instantiated.
    '''

    cs = CollectionSearch()

# Generated at 2022-06-22 11:30:36.107874
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.default() == ['ansible.builtin']

# Generated at 2022-06-22 11:30:38.585078
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class T(CollectionSearch):
        def __init__(self):
            super(T, self).__init__()
    x = T()

# Generated at 2022-06-22 11:30:47.361259
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Ensure CollectionsSearch() returns the default collection.
    r = CollectionSearch()
    assert('ansible.legacy' in r.collections)

    # Ensure CollectionsSearch() returns the default collection, if
    # _ensure_default_collection() is given None.
    r = CollectionSearch()
    assert('ansible.legacy' in r.collections)

    # Ensure CollectionsSearch() returns additional collections,
    # _ensure_default_collection() is given additional collections.
    r = CollectionSearch()
    r.collections = ['foo.bar', 'fizz.buzz']
    assert('foo.bar' in r.collections)
    assert('fizz.buzz' in r.collections)

# Generated at 2022-06-22 11:30:48.450036
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search

# Generated at 2022-06-22 11:30:58.920046
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_bytes

    context = PlayContext()

    # Test _ensure_default_collection function
    tc1 = CollectionSearch()
    tc1.post_validate(context=context)
    assert tc1._collections == ['ansible.legacy']
    tc2 = CollectionSearch()
    tc2.post_validate(context=context)
    assert tc2._collections == ['ansible.legacy']
    tc3 = CollectionSearch()
    tc3.post_validate(context=context)
    tc3._collections = ['ns.repo', 'ns.repo2']
    tc3.post_validate(context=context)

# Generated at 2022-06-22 11:31:14.627927
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    thing = CollectionSearch()
    assert thing.collections == [AnsibleCollectionConfig.default_collection] or thing.collections is None

# Generated at 2022-06-22 11:31:17.110003
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collections = collection_search._load_collections(None, None)
    assert collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:23.394140
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Call constructor
    cs = CollectionSearch()

    # Method _ensure_default_colletion
    assert cs._ensure_default_collection(None) == ['ansible_collections.ansible.builtin']

    collections = ['ns.name', 'ansible_collections.ns.name']
    # Method _load_collections
    assert cs._load_collections(None, collections) == collections

# Generated at 2022-06-22 11:31:29.261782
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    _ensure_default_collection(collection_list=None)
    _ensure_default_collection(collection_list=['ansible.builtin'])
    _ensure_default_collection(collection_list=['ansible.builtin', 'ansible.builtin'])
    _ensure_default_collection(collection_list=['ansible.builtin', 'ansible.legacy'])

# Generated at 2022-06-22 11:31:31.514973
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch.collections == _ensure_default_collection(["ansible.builtin"])

# Generated at 2022-06-22 11:31:35.971389
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._load_collections('collections', []) is None
    assert collection_search._load_collections('collections', None) is None
    assert collection_search._load_collections('collections', ['foo_collection']) == ['foo_collection']

# Generated at 2022-06-22 11:31:39.411448
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a=CollectionSearch()
    a.collections=['col1', 'col2']
    print(a.collections)
    print(a._load_collections(attr='collections', ds=[1,2,3]))

if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:41.256962
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:44.679092
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections is not None
    assert 'ansible.builtin' in collection_search._collections or 'ansible.legacy' in collection_search._collections

# Generated at 2022-06-22 11:31:45.836962
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert isinstance(cs, CollectionSearch)


# Generated at 2022-06-22 11:32:13.890523
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections ==  ['ansible_distrobuilder.distrobuilder.distrobuilder']

# Generated at 2022-06-22 11:32:22.325908
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Don't call constructor
    error_message = "unbound method __init__() must be called with CollectionSearch instance as first argument"
    try:
        CollectionSearch.__init__()
    except TypeError as error:
        assert str(error) == error_message
    # Don't pass argument
    error_message = "__init__() takes exactly 2 arguments (1 given)"
    try:
        cs = CollectionSearch()
    except TypeError as error:
        assert str(error) == error_message
    # Create object of class CollectionSearch
    cs = CollectionSearch()
    assert isinstance(cs, CollectionSearch)

# Generated at 2022-06-22 11:32:32.276957
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.module_utils.six import PY3
    if PY3:
        unicode = str

    env = Environment()
    templar = Templar(loader=None)
    templar.environment = env

    class Data:
        pass

    ds = Data()
    ds.ansible_positional_args_count = 1
    ds.args = [unicode('Please work')]
    ds.vars = {}
    ds.host_vars = {}
    ds.group_vars = {}
    ds.set_vars = {}
    ds.task_vars = {}
    ds.meta_vars = {}

   

# Generated at 2022-06-22 11:32:36.128820
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()

    collection_search = CollectionSearch(collections=['my.collection1', 'my.collection2'])
    assert collection_search._collections == _ensure_default_collection(['my.collection1', 'my.collection2'])



# Generated at 2022-06-22 11:32:37.480673
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:32:38.482000
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search.__init__
    assert collection_search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:39.959241
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert not obj._collections

# Generated at 2022-06-22 11:32:50.446166
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # Test no collection_list is passed to class constructor
    # Default collection must be present in the list
    collection_search = CollectionSearch()
    assert(collection_search._collections[0] == 'ansible_collections.ansible')

    # Test collection_list is passed to class constructor
    collection_list = ['collection_name1','collection_name2']
    collection_search = CollectionSearch(collections=collection_list)

    # Default collection must be present in the list
    assert(collection_search._collections[0] == 'ansible_collections.ansible')
    # The list used for class constructor must be present in the list
    assert(collection_search._collections[1] == collection_list[0])
    assert(collection_search._collections[2] == collection_list[1])


# Generated at 2022-06-22 11:33:01.373985
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    ans = _ensure_default_collection(collection_list=None)
    assert obj._collections._get_default_value() == ans
    # _ensure_default_collection() is called every time when the object is created.
    # Therefore, the _collections field is changed every time.
    # Also, the assigned value is empty list, so the field is '', not None.
    assert obj._collections == ''
    # When there is no value, default value is used.
    assert obj.get_validated_value('collections', obj._collections, None, None) == ans
    # When there is no value, None is returned.
    assert obj._load_collections(None, None) == None
    # When there is a value, the value is returned.

# Generated at 2022-06-22 11:33:02.952219
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()

    assert obj._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:58.372966
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections(None, ['ansible.builtin']) == ['ansible.builtin']
    assert cs._load_collections(None, []) == None
    assert cs._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:34:01.051576
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch({})
    assert a._collections.default == _ensure_default_collection
    assert a._collections.priority == 100
    assert a._collections.always_post_validate == True

# Generated at 2022-06-22 11:34:07.564809
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collections = CollectionSearch()
    assert test_collections.collections == _ensure_default_collection()

    test_collections_with_default = CollectionSearch(collections=None)
    assert test_collections_with_default.collections == _ensure_default_collection()

    test_collections_with_input = CollectionSearch(collections=['a.b'])
    assert test_collections_with_input.collections == _ensure_default_collection(['a.b'])

# Generated at 2022-06-22 11:34:12.105244
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    collection_search = CollectionSearch()
    assert collection_search._collections.default == [collection_search.default_collection]
    assert collection_search._collections.name == "collections"
    assert collection_search._collections.priority == 100



# Generated at 2022-06-22 11:34:16.462299
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test._collections.default == _ensure_default_collection()
    assert test._collections.static == True
    assert test._collections.always_post_validate == True
    assert test._load_collections([], []) == None

# Generated at 2022-06-22 11:34:25.435957
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import RoleInclude
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.role_dependency import RoleDependency

    class TestCollectionSearch(CollectionSearch):
        # This is a valid use case that can be use by plugins, which then can
        # call post_validate()
        _collections = FieldAttribute(isa='list', listof=string_types, priority=100, always_post_validate=True,
                                      static=True)

# Generated at 2022-06-22 11:34:29.806377
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch(collections=[])
    assert search._collections.value == _ensure_default_collection([])
    assert search._collections.value == ['ansible.builtin', 'ansible.legacy']



# Generated at 2022-06-22 11:34:36.634842
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default == _ensure_default_collection
    cl = test_CollectionSearch()
    assert cl._load_collections("collections", ["collections"]) == ["collections"]
    default_collection = AnsibleCollectionConfig.default_collection
    if default_collection is None:
        assert cl._load_collections("collections", []) is None
        assert _ensure_default_collection() is None
    else:
        assert cl._load_collections("collections", []) == [default_collection, "ansible.legacy"]

# Generated at 2022-06-22 11:34:40.639215
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections() == _ensure_default_collection(None)
    test_default_collection = "random_default_collection"
    assert cs.collections([test_default_collection])[0] == test_default_collection
    assert cs.collections([test_default_collection])[1] == "ansible.builtin"

# Generated at 2022-06-22 11:34:42.614190
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs_object = CollectionSearch()
    assert cs_object._collections == _ensure_default_collection

# Generated at 2022-06-22 11:35:34.802267
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs is not None
    assert cs.collections is not None

# Generated at 2022-06-22 11:35:36.906785
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    display.deprecated(msg='TESTING OBJECT: %s' % (str(cs)))

# Generated at 2022-06-22 11:35:40.065925
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    print(test_obj.collections)


test_obj = CollectionSearch()
test_obj.collections = ['test', 'test2']
print(test_obj.collections)

# Generated at 2022-06-22 11:35:47.069283
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch.get_validated_value = lambda self, attr, GV, ds, ty: ds
    cs = CollectionSearch()
    assert cs._load_collections(None, []) is None
    assert cs._load_collections(None, ["foo"]) == ["foo"]
    assert cs._load_collections(None, ["foo", "bar"]) == ["foo", "bar"]

# Generated at 2022-06-22 11:35:54.072025
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test _load_collections by passing in a string
    # This should fail because _load_collections expects a list
    s = CollectionSearch()
    ds = "string"
    assert s._load_collections('collections', ds) is None
    ds = []
    assert s._load_collections('collections', ds) is None
    ds = ['ansible.builtin']
    assert s._load_collections('collections', ds) == ['ansible.builtin', 'ansible.legacy']
    ds = ['ansible.builtin', 'ansible.legacy']
    assert s._load_collections('collections', ds) == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:35:56.616804
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert test_obj._collections == [AnsibleCollectionConfig.default_collection, 'ansible.legacy'], "Not equal.."

# Generated at 2022-06-22 11:36:00.963617
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.collections = ['ansible.builtin']
    cs._load_collections("x", "y")
    assert(type(cs.collections) == list)
    assert(cs.collections == ['ansible.builtin'])

# Generated at 2022-06-22 11:36:10.353580
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # Test default collection search
    cs = CollectionSearch()
    assert cs

    # Test for sibling default collection search
    cs_1 = CollectionSearch()
    cs_1.collections = 'all'
    assert cs_1.collections == ['ansible.builtin','ansible.legacy','all']

    # Test for arg collection search
    cs_2 = CollectionSearch()
    cs_2.collections = ['col1', 'col2']
    assert cs_2.collections == ['col1', 'col2', 'ansible.builtin', 'ansible.legacy']

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:36:11.728313
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # TODO: test the attribute collections
    pass



# Generated at 2022-06-22 11:36:15.343510
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = {'collections': ['test'], 'name': 'test'}
    cs = CollectionSearch()
    cs._collections._load_from_datastructure(test, cs)
    assert cs._collections.value == ['test', 'ansible.builtin', 'ansible.legacy']



# Generated at 2022-06-22 11:37:23.934297
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # test with default collection
    class CollectionSearchTest1(CollectionSearch):
        pass
    t1 = CollectionSearchTest1()
    assert t1.collections == ['ansible.builtin']

    # test with one additional collection
    class CollectionSearchTest2(CollectionSearch):
        def __init__(self, collections=None):
            self._collections = collections
    t2 = CollectionSearchTest2(collections=['my_collection'])
    assert t2.collections == ['my_collection', 'ansible.builtin']

    # test with two additional collections
    class CollectionSearchTest3(CollectionSearch):
        def __init__(self, collections=None):
            self._collections = collections
    t3 = CollectionSearchTest3(collections=['my_collection1', 'my_collection2'])
    assert t3.col

# Generated at 2022-06-22 11:37:32.554003
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # c._collections should be empty list because we have not set this attribute
    assert c._collections == []
    # Constructor call should not set _collections
    assert c._collections == []
    # _load_collections will call the _ensure_default_collection method which will
    # make the first element in the collection list to be default_collection which is
    # 'ansible.builtin'
    c._load_collections(None, None)
    assert c._collections == ['ansible.builtin']
    # test_ensure_default_collection method will do the same thing as it called by
    # _load_collections method.
    c._collections = _ensure_default_collection()
    assert c._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:37:43.403036
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    search = CollectionSearch()

    if not isinstance(search, CollectionSearch):
        raise AssertionError("Test 1: Constructor for CollectionSearch failed")

    if search._collections is None:
        raise AssertionError("Test 2: Constructor for CollectionSearch failed")

    # Check values for default collection
    default_collection = AnsibleCollectionConfig.default_collection
    if default_collection is None:
        if len(search._collections) != 0:
            raise AssertionError("Test 3: Constructor for CollectionSearch failed")
    else:
        if len(search._collections) != 1:
            raise AssertionError("Test 3: Constructor for CollectionSearch failed")

        if search._collections[0] != default_collection:
            raise AssertionError("Test 3: Constructor for CollectionSearch failed")

    # Check values

# Generated at 2022-06-22 11:37:54.724688
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    from collections import namedtuple
    from ansible.module_utils.six import iteritems

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.attribute import FieldAttribute

    def _verify_collection_search():
        for attr in ('collections',):
            assert isinstance(getattr(CollectionSearch, attr, None), FieldAttribute)

    def _gen_ds(collections=None):
        return namedtuple('DataSet', ('ds',))(ds=collections)

    # test simple cases, just as standalone functions
    assert _ensure_default_collection(collection_list=None) == []
    assert _ensure_default_collection(collection_list=[]) == []

# Generated at 2022-06-22 11:37:58.375518
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    """This function performs unit test for constructor of class CollectionSearch."""
    obj = CollectionSearch()
    obj._collections = ["ansible.builtin"]
    obj._load_collections = lambda a, b: None
    assert obj._collections == ["ansible.builtin"]
    assert obj._load_collections(None, None) is None

# Generated at 2022-06-22 11:38:02.359309
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections_data = ["ansible_namespace.my_collection"]
    obj = CollectionSearch()
    obj._collections = collections_data
    assert obj._collections == collections_data
    obj._load_collections('collections', obj._collections)
    assert obj._collections == collections_data

# Generated at 2022-06-22 11:38:07.847657
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs_obj = CollectionSearch()
    path = ''
    with open('/home/travis/build/ansible/ansible/test/unit/mockplugins/test_mock_artifact.py', 'r') as f:
        path = f.read()
    cs_obj._collections = path
    collection_list = cs_obj._load_collections(cs_obj._collections, cs_obj)
    assert collection_list == 'mock_plugins.test_mock_artifact'

# Generated at 2022-06-22 11:38:09.566317
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs=CollectionSearch()
    print(cs._load_collections())

# Generated at 2022-06-22 11:38:12.833936
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class A(CollectionSearch):
        pass
    a = A()
    if a._load_collections('collections', {}) is None or a._load_collections('collections', {'collections': ['ansible.builtin']}) is None:
        raise Exception("Fail")

# Generated at 2022-06-22 11:38:21.898769
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

    #Define variables and instantiate object