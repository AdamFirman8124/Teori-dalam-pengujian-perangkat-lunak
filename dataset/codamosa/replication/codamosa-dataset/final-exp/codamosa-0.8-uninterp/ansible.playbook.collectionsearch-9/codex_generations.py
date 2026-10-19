

# Generated at 2022-06-22 11:29:49.095279
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections is not None

# Generated at 2022-06-22 11:29:50.505261
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert isinstance(collection_search, CollectionSearch)

# Generated at 2022-06-22 11:30:00.546239
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import os
    import collections
    from ansible.playbook.__init__ import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task_include import IncludeTask
    from ansible.template import Templar
    from ansible.utils.collection_loader import _get_collection_name, _get_collection_resolver_config
    from ansible.utils.collection_plugins import get_resolver_for_collections
    from ansible.utils.hashing import checksum_s

    env = Environment()
    collection_cache = collections.defaultdict(dict)
    # Set up a valid context for a Playbook

# Generated at 2022-06-22 11:30:09.449514
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # Test for invalid collection name
    col_search = CollectionSearch()
    try:
        col_search.post_validate({'collections': ['test_coll:test_module']}, False)
        assert False
    except AssertionError:
        assert True

    # Test for valid collection name
    col_search = CollectionSearch()
    try:
        col_search.post_validate({'collections': ['test_coll:test_module.test_task']}, False)
        assert True
    except AssertionError:
        assert False

# Generated at 2022-06-22 11:30:14.505772
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    # _collections is a static attribute, so it won't be populated by the constructor. In this case, _collections will be a FieldAttribute instance
    print("_collections is a static attribute, so it won't be populated by the constructor. In this case, _collections will be a FieldAttribute instance")
    print(obj._collections)
    print(type(obj._collections))

    # Test the getter of _collections
    # get_static_attr will only work for static attributes
    obj._get_static_attr = lambda name: name
    print("Test the getter of _collections")
    print(obj._get_static_attr("_collections"))

    # Test the setter of _collections
    # set_static_attr will only work for static attributes

# Generated at 2022-06-22 11:30:16.310740
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search.post_validate('collections', collection_search._collections, None, None)

# Generated at 2022-06-22 11:30:25.925977
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print('Constructor CollectionSearch test')

    from ansible.playbook.block import Base
    from ansible.playbook.role import Role
    import ansible.utils.collection_loader

    original_loader = ansible.utils.collection_loader.collection_loader
    ansible.utils.collection_loader.collection_loader = None

    # test that it works as the base class of a role
    role = Role()
    role.post_validate()
    assert role.collections == ['ansible.legacy']
    assert role_collections_post_validate_get_collection_list(role) == ['ansible.legacy']

    # test that it works as a mixin
    role = Role()
    role.post_validate()
    assert role.collections == ['ansible.legacy']
    assert role_collections

# Generated at 2022-06-22 11:30:26.901573
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch(), CollectionSearch)

# Generated at 2022-06-22 11:30:28.406676
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook import Task
    t = Task()
    assert t.collections is None

# Generated at 2022-06-22 11:30:28.939370
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection

# Generated at 2022-06-22 11:30:38.232975
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs.post_validate()
    assert cs.collections == ['ansible_collections.ansible.builtin']

# Generated at 2022-06-22 11:30:40.481432
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    print(search.collections)
    return True


if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:30:42.521297
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs_test = CollectionSearch()
    assert cs_test._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:44.472031
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs._load_collections('collections', [])
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:51.491633
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            collections=dict(default=_ensure_default_collection()),
        ),
        supports_check_mode=True
    )

    result = dict(
        ansible_facts=dict(
            collections=module.params['collections'],
        ),
        changed=False
    )

    module.exit_json(**result)

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:30:56.307291
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_ds = {'collections': ['ansible_collections.my.fake']}
    search = CollectionSearch()
    search._collections = test_ds['collections']

    attr = 'collections'
    ds = {}
    test = search._load_collections(attr, ds)
    assert test == test_ds['collections']

# Generated at 2022-06-22 11:30:58.724273
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    instance = CollectionSearch()

# Generated at 2022-06-22 11:31:00.411614
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections is not None

# Generated at 2022-06-22 11:31:04.640044
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():


    collection_search_cs = CollectionSearch()
    # use _load_collections() from CollectionSearch class and
    # pass the Anisble Collection name as'attr' arguement
    # which will be used to load collection
    collection_search_cs._load_collections('test',None)

# Generated at 2022-06-22 11:31:12.829129
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    data = [task_include_dict]
    task_include = TaskInclude()
    task = Task()
    block = Block()
    play = Play()
    role = RoleDefinition()
    role_req = RoleRequirement()
    # playbook_data = []
    playbook = Playbook()
    task.post_validate()
    block.post_validate()
    play.post_validate()

# Generated at 2022-06-22 11:31:27.327323
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:30.072933
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    #CollectionSearch._collections.default_value =  _ensure_default_collection([])
    print(CollectionSearch._collections)

test_CollectionSearch()

# Generated at 2022-06-22 11:31:32.268896
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    try:
        a = CollectionSearch('collections', _collections='test')
        assert True
    except:
        assert False

# Generated at 2022-06-22 11:31:34.412742
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert _ensure_default_collection() == ['ansible.builtin','ansible.legacy']

# Generated at 2022-06-22 11:31:35.734843
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert AnsibleCollectionConfig.default_collection == 'ansible.builtin'

# Generated at 2022-06-22 11:31:43.200440
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # CollectionSearch's constructor will be called by Base.__init__() which is called in Role.__init__()
    roles_paths = '/etc/ansible/roles'
    role = Role(name='test_role', collection_list=['test_collection'])
    if role.collections != ['test_collection']:
        print('PR:1345 - initial collections are not in the order of [\'test_collection\']')
        print(role.collections)
    if role.roles_paths != [roles_paths]:
        print('PR:1345 - roles_paths are not default to: [\'%s\']' % roles_paths)
        print(role.roles_paths)
    test_ds = {'roles_path': '/home/roles'}

# Generated at 2022-06-22 11:31:44.246146
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c is not None

# Generated at 2022-06-22 11:31:46.503405
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == [
        AnsibleCollectionConfig.default_collection,
        'ansible.legacy'
    ]

# Generated at 2022-06-22 11:31:50.984631
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    search = collection_search._collections
    assert search is not None
    assert len([e for e in search if e == "ansible.builtin"]) == 1
    assert len([e for e in search if e == "ansible.legacy"]) == 1

# Generated at 2022-06-22 11:32:02.346667
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    class TestCollectionSearch:
        def __init__(self):
            self.__dict__ = {'ansible_positional_args_supported': True}

    test_collections_search = CollectionSearch(ds={"collections": "default_collection"})
    test_collections_search.post_validate(TestCollectionSearch(), "collections")

    assert test_collections_search._collections == ['default_collection']

    class TestCollectionSearch:
        def __init__(self):
            self.__dict__ = {'ansible_positional_args_supported': True}

    test_collections_search = CollectionSearch(ds={"collections": []})

# Generated at 2022-06-22 11:32:17.835568
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj
    # Asserting that the constructor call did not fail
    assert obj._collections



# Generated at 2022-06-22 11:32:21.397836
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    print(obj._collections)
    print(obj._collections.default(None))
    print(obj._load_collections(None, None))

if __name__ == '__main__':
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:22.895079
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
        col = CollectionSearch()
        assert col.collections == []

# Generated at 2022-06-22 11:32:28.473467
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default() == _ensure_default_collection()

    assert cs._collections.default() == ['ansible_collections.nsxt.nsxt', 'ansible.builtin']
    assert cs._collections.default() == ['ansible_collections.nsxt.nsxt', 'ansible.legacy']

# Generated at 2022-06-22 11:32:29.778967
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections is _ensure_default_collection

# Generated at 2022-06-22 11:32:38.205891
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections._valid_templates is False
    assert isinstance(cs._collections, FieldAttribute)
    assert cs._collections.default == _ensure_default_collection()
    assert cs._collections.always_post_validate == True
    assert cs._collections.static == True
    assert cs._collections.listof == string_types
    assert cs._collections.isa == 'list'
    assert cs._collections.priority == 100
    assert cs._collections.name == 'collections'
    assert cs._collections.private == False
    assert cs._collections.apply_defaults == False
    assert cs._collections.required == False
    assert cs._collections.default != cs._collections
    assert cs._collections.name == 'collections'
    assert cs

# Generated at 2022-06-22 11:32:39.588908
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert _ensure_default_collection() == obj._collections.default

# Generated at 2022-06-22 11:32:41.046300
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None

# Generated at 2022-06-22 11:32:51.128844
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    searchObj = CollectionSearch()
    actualResult = searchObj._load_collections('collections',['ansible.builtin'])
    expectedResult = ['ansible.builtin']
    assert actualResult == expectedResult

    actualResult = searchObj._load_collections('collections',['ansible.builtin','ansible.posix'])
    expectedResult = ['ansible.builtin','ansible.posix']
    assert actualResult == expectedResult

    actualResult = searchObj._load_collections('collections',['ansible.posix'])
    expectedResult = ['ansible.posix']
    assert actualResult == expectedResult

    actualResult = searchObj._load_collections('collections',None)
    expectedResult = ['ansible.builtin']
    assert actualResult == expectedResult

# Generated at 2022-06-22 11:32:55.822038
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    test_obj = CollectionSearch()
    assert test_obj._collections == _ensure_default_collection()
    assert test_obj._collections == ["test_module.test_module"]
    assert test_obj.collections == ["test_module.test_module"]

# Generated at 2022-06-22 11:33:23.127633
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
  test_object = CollectionSearch()
  assert test_object._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:25.979875
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()
    assert c._collections == ['ansible.builtin','ansible.legacy']

# Generated at 2022-06-22 11:33:34.088161
# Unit test for constructor of class CollectionSearch

# Generated at 2022-06-22 11:33:35.604252
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:33:37.015192
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:33:39.018261
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search._load_collections(None, ['collection1'])
    assert collection_search._collections == collection_search._load_collections(None, ['collection1'])

# Generated at 2022-06-22 11:33:42.556618
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Without default collection
    assert len(CollectionSearch._collections.value) == 1

    # With default collection
    assert len(CollectionSearch._collections.value) == 2

    # Without default collection and with collections
    collections = ['test']
    assert len(CollectionSearch._collections.value) == 2


# Generated at 2022-06-22 11:33:43.252729
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()

# Generated at 2022-06-22 11:33:44.796643
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch().collections == ['ansible.builtin']

# Generated at 2022-06-22 11:33:46.297993
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:34:46.892955
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    #_collections = FieldAttribute(isa='list', listof=string_types, priority=100, default=_ensure_default_collection,
    #                              always_post_validate=True, static=True)
    assert cs._collections.isa == 'list'
    assert cs._collections.listof == string_types
    assert cs._collections.priority == 100
    assert cs._collections.default == _ensure_default_collection
    assert cs._collections.always_post_validate == True
    assert cs._collections.static == True

# Generated at 2022-06-22 11:34:54.658071
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task_include import TaskInclude

    assert CollectionSearch._collections.default == _ensure_default_collection

    c = CollectionSearch()
    assert c.get_validated_value('collections', c._collections, '', None) == _ensure_default_collection()

    assert c.get_validated_value('collections', c._collections, ['ns.collection', 'next'], None) == ['ns.collection', 'next']

    assert c.get_validated_value('collections', c._collections, None, None) == _ensure_default_collection()

    assert RoleInclude._collections.default == CollectionSearch._collections.default

# Generated at 2022-06-22 11:35:05.840547
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    # This is the correct execution of the constructor of class CollectionSearch
    try:
        # This is the correct execution of the constructor of class CollectionSearch
        obj = CollectionSearch()
    except AssertionError as e:
        print("Incorrect values for constructor of class CollectionSearch , exception is:: ")
        print(e)

    # This is the incorrect execution of the constructor of class CollectionSearch.This is because the default value of
    # _collections must be a list of strings.
    try:
        obj = CollectionSearch(collections=123)
    except AssertionError as e:
        print("Incorrect values for constructor of class CollectionSearch , exception is:: ")
        print(e)

if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:35:09.662216
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert isinstance(search, CollectionSearch)
    assert isinstance(search._collections, FieldAttribute)
    assert isinstance(search._collections.listof, string_types)
    assert search._collections.static == True

# Generated at 2022-06-22 11:35:18.305233
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c1 = CollectionSearch()
    c1.collections = ['ansible.builtin', 'test_collection']
    assert c1.collections == ['ansible.builtin', 'test_collection']
    assert c1._load_collections(attr="collections", ds=["ansible.builtin", "test_collection"]) == ['ansible.builtin', 'test_collection']

    # this will add "ansible.builtin" as the default collection
    c2 = CollectionSearch()
    c2.collections = []
    assert c2.collections == ['ansible.builtin']
    assert c2._load_collections(attr="collections", ds=[]) == ['ansible.builtin']

    # this will also add "ansible.builtin" as the default collection
    c3 = CollectionSearch()
   

# Generated at 2022-06-22 11:35:22.020829
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import collections

    collectionSearch = CollectionSearch()

    assert(collectionSearch is not None)
    assert(isinstance(collectionSearch, collections.Callable))



# Generated at 2022-06-22 11:35:23.043965
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search

# Generated at 2022-06-22 11:35:26.369403
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Given that I have a CollectionSearch class defined
    # When I create an instance of CollectionSearch
    collection_search = CollectionSearch()
    # Then I should have a valid instance of CollectionSearch
    assert collection_search is not None


# Generated at 2022-06-22 11:35:27.817701
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == ['ansible.builtin']

# Generated at 2022-06-22 11:35:39.634211
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.role_include import IncludeRole
    import collections
    import pytest

    class MyCollectionSearch(CollectionSearch): 
        pass


# Generated at 2022-06-22 11:37:33.931948
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = ['ansible.builtin', 'ansible.posix_lsb']
    cs = CollectionSearch(collections)
    assert cs._collections == collections

# Generated at 2022-06-22 11:37:44.320644
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

# Generated at 2022-06-22 11:37:50.405897
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    #
    # Test default constructor
    #
    collection_search = CollectionSearch()
    assert not collection_search._collections.value

    #
    # Test the constructor with a valid string
    #
    collection_search = CollectionSearch(collections='ansible.builtin')
    assert collection_search._collections.value == ['ansible.builtin', 'ansible.legacy']

    #
    # Test the constructor with a valid list of strings
    #
    collection_search = CollectionSearch(collections=['test.test1', 'test.test2'])
    assert collection_search._collections.value == ['test.test1', 'test.test2', 'ansible.legacy']

    #
    # Test the constructor with a valid list of strings, including legacy
    #

# Generated at 2022-06-22 11:37:51.956668
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection

# Generated at 2022-06-22 11:37:55.437889
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == 'ansible.builtin, ansible.legacy'

# Generated at 2022-06-22 11:37:56.858872
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:37:58.668357
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    game = CollectionSearch()
    assert game._collections == ['ansible.builtin']

# Generated at 2022-06-22 11:38:05.044659
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections.default_value is not None
    assert obj._collections.init_value is None
    assert obj._collections.value is None
    assert obj._collections.name == 'collections'
    assert obj._collections.parent == obj
    assert obj._collections.search_path is None
    assert obj._collections.required is False
    assert obj._collections.isa is not None
    assert obj._collections.fallback is None
    assert obj._collections.elements

# Generated at 2022-06-22 11:38:06.259810
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    coll_search = CollectionSearch()
    assert isinstance(coll_search, CollectionSearch)

# Generated at 2022-06-22 11:38:08.947998
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Check that object is created correctly
    obj = CollectionSearch()
    assert isinstance(obj, CollectionSearch)