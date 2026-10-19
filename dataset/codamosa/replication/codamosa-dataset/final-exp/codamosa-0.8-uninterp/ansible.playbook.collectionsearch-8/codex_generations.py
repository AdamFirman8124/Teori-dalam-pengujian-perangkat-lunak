

# Generated at 2022-06-22 11:29:56.753756
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collec = CollectionSearch()

    collec._collections.load(None)
    assert collec._collections.value == 'ansible.builtin:ansible.legacy'

    collec._collections.load(['mycol'])
    assert collec._collections.value == 'mycol:ansible.builtin:ansible.legacy'

    collec._collections.load(['mycol:othercol'])
    assert collec._collections.value == 'mycol:othercol:ansible.builtin:ansible.legacy'

    collec._collections.load(['mycol:othercol'])
    assert collec._collections.value == 'mycol:othercol:ansible.builtin:ansible.legacy'

# Generated at 2022-06-22 11:30:00.106373
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    my_collection_search = CollectionSearch()
    # Test the constructor.
    assert(my_collection_search.collections == ['ansible.builtin', 'ansible.legacy'])


# Test the _ensure_default_collection method.

# Generated at 2022-06-22 11:30:08.836784
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections is not None
    assert collection_search._collections == ['ansible_collections.ansible.builtin']
    assert collection_search._collections[0] == 'ansible_collections.ansible.builtin'

    # collection_path = None
    collection_search = CollectionSearch(['my.ns'])
    assert collection_search._collections is not None
    assert collection_search._collections == ['my.ns', 'ansible_collections.ansible.builtin']
    assert collection_search._collections[0] == 'my.ns'
    assert collection_search._collections[1] == 'ansible_collections.ansible.builtin'

    # collection_path = 'my.ns'

# Generated at 2022-06-22 11:30:09.994066
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default == _ensure_default_collection()

# Generated at 2022-06-22 11:30:12.464648
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch(collections=['test.collections','test.collections2','test.collections2'])
    if (len(cs.collections)==3):
        print("Test case CollectionSearch #1: [SUCCESS]")
    else:
        print("Test case CollectionSearch #1: [FAILURE]")

# Generated at 2022-06-22 11:30:16.657853
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test for constructor
    CS = CollectionSearch()
    if CS.get_validated_value('collections', CS._collections, [], None):
        assert 'CS' == 'CS'
    else:
        assert 'CS' != 'CS', \
        "The class constructor does not function properly"

# Generated at 2022-06-22 11:30:23.925802
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._load_collections("", ["ansible.builtin"]) == ["ansible.builtin"]
    assert c._load_collections("", "ansible.builtin") == ["ansible.builtin"]
    assert c._load_collections("", None) == ["ansible.builtin"]
    assert c._load_collections("", []) == ["ansible.builtin"]

# Generated at 2022-06-22 11:30:26.334740
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == 'ansible.builtin,ansible.legacy'


# Unit Test for method _load_collections of class CollectionSearch

# Generated at 2022-06-22 11:30:27.627494
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:30:31.140107
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # New an object
    collection_search = CollectionSearch()

    # Test the constructor of class CollectionSearch
    assert isinstance(collection_search, CollectionSearch)
    assert isinstance(CollectionSearch._collections, FieldAttribute)
    assert 'collections' in CollectionSearch.fields

# Generated at 2022-06-22 11:30:47.930771
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    def test_collections(self, attribute, new_value):
        # Method to set collections for testing
        self._collections = new_value

    def test_validate_collections(self, attr, ds):
        # Method to validate collections for testing
        # This duplicates static attr checking logic from post_validate()
        # because if the user attempts to template a collection name, it may
        # error before it ever gets to the post_validate() warning (e.g. trying
        # to import a role from the collection).
        env = Environment()

# Generated at 2022-06-22 11:30:51.519922
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    if collection_search.collections[0] == 'ansible.builtin':
        print('Test passed for constructor of class CollectionSearch')
    else:
        print('Test failed for constructor of class CollectionSearch')

# Generated at 2022-06-22 11:30:53.459107
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    ds = cs._load_collections(attr='collections', ds=None)
    assert ds is not None

# Generated at 2022-06-22 11:30:55.803744
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == ['ansible.builtin','ansible.legacy']
    assert len(c._collections) == len(c._load_collections('collections',None))

# Generated at 2022-06-22 11:30:57.233501
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test for default collection list
    search_collections = CollectionSearch()
    assert search_collections._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:59.124928
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    collection_search = CollectionSearch()

    #FIXME: Write a test for this

# Generated at 2022-06-22 11:31:02.261584
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.__dict__ = {'_collections': 'collections'}
    cs._collections = []
    cs._load_collections(None, None)

# Generated at 2022-06-22 11:31:03.131307
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()

# Generated at 2022-06-22 11:31:04.220965
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    assert collections

# Generated at 2022-06-22 11:31:06.583846
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()
    assert instance.collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:31:15.896227
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.task_include import TaskInclude
    x = TaskInclude()
    assert x._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:17.417038
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj is not None


# Generated at 2022-06-22 11:31:18.819492
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()

    assert hasattr(obj, '_collections')

# Generated at 2022-06-22 11:31:21.180372
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    validator = CollectionSearch()
    assert validator._load_collections(collections=['local']) == ['local']

# Generated at 2022-06-22 11:31:23.228785
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Simple test to check if the CollectionSearch object is created
    c = CollectionSearch()

# Generated at 2022-06-22 11:31:28.245022
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pdb; pdb.set_trace()
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin', 'ansible.legacy']
    assert cs._collections._default == ['ansible.builtin', 'ansible.legacy']

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:31:38.680770
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Create an instance of class CollectionSearch
    # Where collections is the attribute name
    # And _collections is the FieldAttribute
    collection_search = CollectionSearch()

    # collection_search._load_collections
    # Where the first parameter is collections
    # And the second parameter is None
    result = collection_search._load_collections(collection_search.collections, None)

    # assert result is not None
    assert result is not None
    # assert result is of type list
    assert isinstance(result, list)
    # assert result is not empty
    assert result != []

    # collection_search._load_collections
    # Where the first parameter is collections
    # And the second parameter is a list
    result = collection_search._load_collections(collection_search.collections, ['a', 'b', 'c'])

   

# Generated at 2022-06-22 11:31:50.434856
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible import context
    from ansible.vars.manager import VariableManager

    # Test with auto_vars_lazy and auto_vars_inheritance
    # In fact, they are the same, because they are called in the same place
    display.verbosity = 3
    context.CLIARGS = {'auto_vars_lazy': True, 'auto_vars_inheritance': True, 'verbosity': 3}

    test_collection_search = CollectionSearch()
    test_collection_search.vars = VariableManager()

    # Test with auto_vars_lazy
    display.verbosity = 3
    context.CLIARGS = {'auto_vars_lazy': True, 'verbosity': 3}
    test_collection_search = CollectionSearch()
    test_collection_search.vars

# Generated at 2022-06-22 11:31:53.899006
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Initialize an instance of CollectionSearch class
    collectionSearch = CollectionSearch()
    print(collectionSearch)

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:01.219674
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search._collections, FieldAttribute) is True
    assert isinstance(collection_search._collections.static, bool) is True
    assert isinstance(collection_search._collections.always_post_validate, bool) is True
    assert isinstance(collection_search._collections.priority, int) is True
    assert isinstance(collection_search._collections.default, type(_ensure_default_collection)) is True

# Generated at 2022-06-22 11:32:20.338212
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # Private variable gets exposed through the default function
    assert cs._collections == ['ansible.builtin']
    # CollectionSearch has a list of string types as a listof attribute
    assert cs.collections == ['ansible.builtin']
    cs.collections = ['ansible.builtin']
    assert cs.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:32:26.932708
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionsearch = CollectionSearch()
    assert collectionsearch._collections == ['ansible_collections.notstdlib.moveitallout.plugins.module_utils.netcommon', 'ansible_collections.notstdlib.moveitallout.plugins.action', 'ansible_collections.notstdlib.moveitallout.plugins.module_utils.network.common', 'ansible.netcommon', 'ansible.builtin']

# Generated at 2022-06-22 11:32:27.976360
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == None

# Generated at 2022-06-22 11:32:33.559830
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == _ensure_default_collection()
    cs.collections = ['ansible.builtin']
    assert cs.collections == _ensure_default_collection(['ansible.builtin'])
    cs.collections = ['collections.c']
    assert cs.collections == ['collections.c']
    cs.collections = None
    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:35.211706
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection.collections is not None
    assert collection._collections is not None

# Generated at 2022-06-22 11:32:46.627302
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from collections import namedtuple

    assert CollectionSearch.get_fields()['collections']

    displayed_warning = []
    def mock_warning(msg):
        displayed_warning.append(msg)

    display.warning = mock_warning

    class Test(CollectionSearch):
        collections = None

    env = Environment()

    data = namedtuple('Data', ['collections'])(collections=['a.b', 'c.d', '{{ foo }}'])
    test = Test(collections=data.collections)

    collections = test._load_collections('collections', data)
    assert collections == ['a.b', 'c.d', '{{ foo }}']

# Generated at 2022-06-22 11:32:47.948664
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    tcs = CollectionSearch()

test_CollectionSearch()

# Generated at 2022-06-22 11:32:54.745992
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # datastructure for validating result of load_collections function
    class Ds:
        def __init__(self, value):
            self.collections = value

    test_ds_with_collections = Ds(["ansible_namespace.ansible_collection", "ansible_namespace.another_collection"])
    collection_search_object = CollectionSearch()
    # GIVEN a collection search object and a datastructure which has a collections field
    # WHEN the load_collections function is called
    # THEN assert that the collections in the datastructure are returned
    assert collection_search_object._load_collections('collections', test_ds_with_collections) == ["ansible_namespace.ansible_collection", "ansible_namespace.another_collection"]

# Generated at 2022-06-22 11:32:56.711814
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:32:58.905035
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections.default() == c._ensure_default_collection(collection_list=None)

# Generated at 2022-06-22 11:33:28.658916
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None
    assert cs._collections['static'] == True


# Generated at 2022-06-22 11:33:34.227846
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    #  case1
    ds = ["pulp.pulp"]

    cs = CollectionSearch()
    assert cs._load_collections('collections', ds)

    # case2
    ds = ["pulp.pulp", "geerlingguy.mysql"]

    cs = CollectionSearch()
    assert cs._load_collections('collections', ds)

    # case3
    ds = []

    cs = CollectionSearch()
    assert cs._load_collections('collections', ds) is None

# Generated at 2022-06-22 11:33:35.249644
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:36.575489
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()

    assert a._collections == 'ansible.builtin'


# Generated at 2022-06-22 11:33:39.327344
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    default_collection = AnsibleCollectionConfig.default_collection
    assert obj._collections.default == [default_collection] if default_collection else []


# Generated at 2022-06-22 11:33:45.842525
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_list = ['ansible.builtin']
    _ensure_default_collection(collection_list=collection_list)
    assert collection_list == ['ansible.builtin']

    collection_list = ['ansible.builtin', 'test_collection']
    _ensure_default_collection(collection_list=collection_list)
    assert collection_list == ['ansible.builtin', 'test_collection']

    collection_list = ['test_collection']
    _ensure_default_collection(collection_list=collection_list)
    assert collection_list == ['test_collection', 'ansible.builtin']

    assert _ensure_default_collection() == ['ansible.builtin']

# Generated at 2022-06-22 11:33:49.552996
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin']
    cs.collections = ['ansible.builtin', 'my_collection']
    assert cs.collections == ['ansible.builtin', 'my_collection']


# Generated at 2022-06-22 11:33:58.853325
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections('collections', None) == _ensure_default_collection()
    assert cs._load_collections('collections', []) == _ensure_default_collection([])
    assert cs._load_collections('collections', ['foo.bar']) == _ensure_default_collection(['foo.bar'])
    assert cs._load_collections('collections', ['my.collection']) == _ensure_default_collection(['my.collection'])
    assert cs._load_collections('collections', ['my.collection', 'foo.bar']) == _ensure_default_collection(['my.collection', 'foo.bar'])

# Generated at 2022-06-22 11:34:03.964738
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default == ['ansible.builtin']
    assert cs._collections.static is True
    assert cs._collections.listof == string_types
    assert cs._collections.isa == 'list'
    assert cs._collections.always_post_validate is True
    assert cs._collections.priority == 100
    assert cs._collections.default == ['ansible.builtin']

# Generated at 2022-06-22 11:34:05.203195
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection._collections is None


# Generated at 2022-06-22 11:35:01.461797
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    co = CollectionSearch()
    assert co._collections.default == None # default value


# Generated at 2022-06-22 11:35:02.093994
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    CollectionSearch()

# Generated at 2022-06-22 11:35:07.951897
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections == ['ansible.posix']
    assert c._collections == ['ansible.posix']
    # default value is not returned by get_validated_value, so we have to test
    # constructor value
    # assert c.get_validated_value('collections') == ['ansible.posix']

# Generated at 2022-06-22 11:35:12.816963
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test for constructor with empty params
    c = CollectionSearch()
    assert c._collections is not None
    # Test for constructor with collections param
    collections = ['ansible_my_collection']
    c = CollectionSearch(collection_list=collections)
    assert c._collections == collections
    # Test for constructor with template param
    template_name = '{{ foo }}'
    c = CollectionSearch(collection_list=[template_name])
    assert c._collections == [template_name]

# Generated at 2022-06-22 11:35:23.366658
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.tasks import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.conditional import Conditional

    cs = CollectionSearch()
    assert cs._collections.post_validate(None, None) is None
    assert cs._collections.post_validate(None, {'collections': []}) is None
    assert cs._collections.post_validate(None, {'collections': ['foo']}) == ['foo', 'ansible.legacy']

    cs = CollectionSearch(collections=['foo'])
    assert cs._collections.post_validate(None, None) == ['foo']



# Generated at 2022-06-22 11:35:25.939486
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class Module(CollectionSearch):
        pass

    assert Module().collections == ['ansible.builtin']


if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:35:27.365417
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert test_obj is not None

# Generated at 2022-06-22 11:35:28.353665
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collection_search = CollectionSearch()

# Generated at 2022-06-22 11:35:31.234663
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    class TestClass(CollectionSearch):
        pass

    test_object = TestClass()

    assert test_object.collections == _ensure_default_collection()


# Generated at 2022-06-22 11:35:34.723850
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection._collections is not None
    assert collection._collections is not []
    assert 'ansible.builtin' in collection._collections


# Generated at 2022-06-22 11:37:35.001978
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    collections = CollectionSearch()

    with pytest.raises(AttributeError):
        collections.collections

    with pytest.raises(SystemExit):
        collections.collections = 'not a list'

# Generated at 2022-06-22 11:37:41.821401
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestClass:
        def __init__(self, collection_list=None):
            self.collections = _ensure_default_collection(collection_list)

        def __getitem__(self, attr):
            return self.__dict__[attr]

    test_obj = TestClass(['ansible.builtin', 'ansible_collections.community.general'])
    assert test_obj.collections == ['ansible_collections.community.general', 'ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:37:43.074859
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()
    print(s._collections)

# Generated at 2022-06-22 11:37:44.587221
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import collections
    cs = CollectionSearch()
    assert isinstance(cs._collections, collections.deque)

# Generated at 2022-06-22 11:37:46.207028
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default is _ensure_default_collection

# Generated at 2022-06-22 11:37:48.010535
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == _ensure_default_collection()


# Generated at 2022-06-22 11:37:50.224558
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == None

# Generated at 2022-06-22 11:37:54.512919
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test Case 1: CollectionSearch should be initialized with no args.
    test_search = CollectionSearch()
    # Test Case 2: _collections attribute is expected to be a dict and there
    # should be a default value as defined in the _ensure_default_collection method
    assert isinstance(test_search._collections, list)

# Generated at 2022-06-22 11:37:57.328360
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectsearch = CollectionSearch()
    assert collectsearch._valid_attrs['collections'] == True
    assert collectsearch._collections == 'ansible.builtin'

# Generated at 2022-06-22 11:37:59.774449
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    for attr in ['_collections']:
        assert hasattr(cs, attr)
    assert cs._collections._get_value() == _ensure_default_collection()