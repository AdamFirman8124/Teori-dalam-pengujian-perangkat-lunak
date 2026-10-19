

# Generated at 2022-06-22 11:29:48.751373
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert isinstance(CollectionSearch().collections, list)

# Generated at 2022-06-22 11:29:58.830162
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    data_structure = dict(
                          tasks = dict(
                              users = dict(
                                    name = "a user",
                                    state = "present"
                              ),
                              users2 = dict(
                                  name = "a user",
                                  state = "present"
                              )
                          ),
                          collections = [
                              "ansible.builtin",
                              "community.general"
                          ]
                        )

    cs = CollectionSearch()
    cs.init_data_struct(data_structure)
    assert cs.validate_data_struct()
    print (cs.tasks['users']['name'])
    print (cs.tasks['users2']['state'])
    print (cs.collections)

# Generated at 2022-06-22 11:30:00.597457
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == ["ansible_collections.my_namespace.my_collection"]

# Generated at 2022-06-22 11:30:05.756492
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert bool(obj)
    assert isinstance(obj, CollectionSearch)
    assert obj is not None
    assert obj._collections is not None
    assert obj._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:07.568092
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    inst = CollectionSearch()
    assert inst._collections is not None

# Generated at 2022-06-22 11:30:12.458575
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # setup
    class TestCollectionSearch(CollectionSearch):
        pass
    
    obj = TestCollectionSearch()
    
    # test
    assert obj.collections == ['ansible_collections.ansible.builtin', 'ansible_collections.ansible.builtin.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:30:15.629403
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    # The private and protected variables in the module are not accessible(in python3)
    # So commented out the validation part
    # assert collection_search.collections is None

# Generated at 2022-06-22 11:30:17.390444
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections._value == _ensure_default_collection([])

# Generated at 2022-06-22 11:30:28.440124
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import ansible.playbook.task_include
    import ansible.plugins.loader

    task_include_instance = ansible.playbook.task_include.TaskInclude.load(dict(name='test', collections=['test', 'ansible.builtin']))
    assert isinstance(task_include_instance, ansible.playbook.task_include.TaskInclude)
    assert task_include_instance.collections == ['test', 'ansible.builtin']

    task_include_instance = ansible.playbook.task_include.TaskInclude.load(dict(name='test', collections=['test', 'ansible.builtin.uri']))
    assert isinstance(task_include_instance, ansible.playbook.task_include.TaskInclude)

# Generated at 2022-06-22 11:30:29.289969
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    print(c)

# Generated at 2022-06-22 11:30:36.719676
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()

# Generated at 2022-06-22 11:30:38.336830
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None

# Generated at 2022-06-22 11:30:44.229478
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    # cs.validate_attributes()
    assert cs._collections == ['ansible_collections.test.test_ns.test_coll']
    assert cs._collections == ['ansible_collections.test.test_ns.test_coll']
    # cs.validate_attributes()
    assert cs._collections == ['ansible_collections.test.test_ns.test_coll']

# Generated at 2022-06-22 11:30:45.832097
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:30:47.033740
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert(cs)

# Generated at 2022-06-22 11:30:57.585333
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # Default value of collection is "ansible.builtin" when no value is passed
    assert c.collections == ['ansible.builtin', 'ansible.legacy']

    #Default value of collection is "ansible.builtin" when an empty list is passed
    c = CollectionSearch()
    c.collections = []
    assert c.collections == ['ansible.builtin', 'ansible.legacy']

    #Default value of collection is "ansible.builtin" when a None value is passed
    c = CollectionSearch()
    c.collections = None
    assert c.collections == ['ansible.builtin', 'ansible.legacy']

    #Default value of collection is "ansible.builtin" when a empty string value is passed
    c = CollectionSearch()
    c.collections

# Generated at 2022-06-22 11:31:05.547538
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class TestCollectionSearch(CollectionSearch):
        pass

    test_obj = TestCollectionSearch()
    assert test_obj._load_collections('collections', 'Ansible.Collection:1.0.0') == ['Ansible.Collection:1.0.0']
    assert test_obj._load_collections('collections', ['Ansible.Collection:1.0.0', 'Ansible.Collection:2.0.0']) == ['Ansible.Collection:2.0.0', 'Ansible.Collection:1.0.0', 'ansible.builtin']



# Generated at 2022-06-22 11:31:10.777704
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ################################################################################################################
    # CollectionSearch constructor
    ################################################################################################################
    """
    Unit test case for the constructor of Class CollectionSearch.

    """
    # Create an object of class CollectionSearch
    collection_search_obj = CollectionSearch()

    # Check if an object of class CollectionSearch is created
    assert isinstance(collection_search_obj, CollectionSearch) is True, "Object not created"


# Generated at 2022-06-22 11:31:12.355499
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == AnsibleCollectionConfig.default_collection

# Generated at 2022-06-22 11:31:14.487557
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class Test(CollectionSearch):
        pass
    obj = Test()
    assert obj._collections is None

# Generated at 2022-06-22 11:31:36.484057
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    cs_collections = cs.__dict__['_collections']
    assert isinstance(cs_collections, FieldAttribute)
    assert cs_collections.name == 'collections'
    assert cs_collections.isa == 'list'
    assert len(cs_collections.listof) == 1
    assert string_types in cs_collections.listof
    assert cs_collections.priority == 100
    assert cs_collections.static == True
    assert cs_collections._default == _ensure_default_collection
    assert cs_collections.always_post_validate == True

# Generated at 2022-06-22 11:31:36.856943
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()

# Generated at 2022-06-22 11:31:38.070028
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:31:40.654725
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    search._collections = _ensure_default_collection()
    assert search._collections == _ensure_default_collection()
    assert search._load_collections(search._collections, search._collections) == None

# Generated at 2022-06-22 11:31:41.259170
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()

# Generated at 2022-06-22 11:31:45.157120
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    value = 'examplename.namespace.collection'
    loader = DataLoader()
    variable_manager = VariableManager()

    collection_search = CollectionSearch()
    collection_search.post_validate('collections', value, loader)
    collection_search.post_validate('collections', value, loader)

    print('test_CollectionSearch passed')

test_CollectionSearch()

# Generated at 2022-06-22 11:31:50.723740
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    default_collection = AnsibleCollectionConfig.default_collection
    if default_collection is None:
        default_collection_list = []
    else:
        default_collection_list = [default_collection]

    collection_search = CollectionSearch()
    res = collection_search._load_collections(attr=None, ds=None)
    assert res == default_collection_list

# Generated at 2022-06-22 11:32:02.927393
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == _ensure_default_collection()
    obj._collections = ['foo']
    assert obj._collections == ['foo', 'ansible.builtin']
    obj._collections = None
    assert obj._collections is None
    obj._collections = ['bar']
    assert obj._collections == ['bar', 'ansible.builtin']
    obj._collections = ['ansible.builtin', 'foo', 'bar']
    assert obj._collections == ['ansible.builtin', 'foo', 'bar']
    obj._collections = ['foo', 'ansible.builtin', 'bar']
    assert obj._collections == ['foo', 'ansible.builtin', 'bar']
    obj._collections = ['bar', 'foo', 'ansible.builtin']
   

# Generated at 2022-06-22 11:32:09.856890
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert collection._collections.default == _ensure_default_collection()
    assert collection._collections.name == 'collections'
    assert collection._collections.static == True
    assert collection._collections.always_post_validate == True
    assert collection._collections.priority == 100
    assert collection._collections.listof == string_types
    assert collection._collections.isa == 'list'
    assert collection._collections.post_validate == None
    assert collection._collections.field_class == None
    assert collection._collections.validate == None
    assert collection._collections.default_is_template == False
    assert collection._collections.default_is_json == False
    assert collection._collections.default_is_yaml == False

test_CollectionSearch()

# Generated at 2022-06-22 11:32:11.724801
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:42.174952
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search._collections is not None
    assert search._collections == ['ansible.builtin', 'ansible.legacy']

# unit test for function _ensure_default_collection

# Generated at 2022-06-22 11:32:50.589805
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test for the private constructor.
    f = CollectionSearch()
    assert f._collections == _ensure_default_collection()

    f._collections = ["ansible.builtin","ansible,legacy"]
    assert f._collections == ["ansible.builtin","ansible,legacy"]
    # Test for populating of collections
    f._load_collections('test', None)
    assert f._collections == _ensure_default_collection()
    # Test for populating of collections
    f._collections = None
    f._load_collections('test', None)
    assert f._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:57.735771
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import pytest
    with pytest.raises(TypeError) as excinfo:
        cs = CollectionSearch(collections=_ensure_default_collection())
    assert 'missing 1 required positional argument' in str(excinfo.value)
    cs = CollectionSearch.load(dict(collections=_ensure_default_collection()))
    assert cs._validated_attributes['collections'] == cs.collections
    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:32:59.464178
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionsearch = CollectionSearch()
    if collectionsearch:
        assert True
    else:
        assert False

# Generated at 2022-06-22 11:33:01.352160
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections._static is True

# Generated at 2022-06-22 11:33:03.225943
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert isinstance(obj, CollectionSearch)
    assert obj._collections is not None

# Generated at 2022-06-22 11:33:05.262359
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c._collections.default(None) == ['ansible.builtin']

# Generated at 2022-06-22 11:33:06.616131
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections is not None



# Generated at 2022-06-22 11:33:11.353067
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    result = test._load_collections('test_attr', ['ansible.builtin'])
    print("testCollectionSearch Success" if result == ['ansible.builtin'] else "testCollectionSearch Failure")

# Invoke Unit test function
test_CollectionSearch()

# Generated at 2022-06-22 11:33:13.196880
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default == _ensure_default_collection()


# Generated at 2022-06-22 11:34:11.247942
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # Test case for constructor of class CollectionSearch
    # Arrange
    _collections = []
    # Act
    ansible_collections = CollectionSearch()
    # Assert
    assert ansible_collections



# Generated at 2022-06-22 11:34:13.011446
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search.collections is not None

# Generated at 2022-06-22 11:34:15.068810
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x=CollectionSearch()
    x._load_collections('collections', [])
    print(x._collections)

# Generated at 2022-06-22 11:34:17.467047
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_obj = CollectionSearch()
    assert isinstance(test_obj, CollectionSearch)
    assert test_obj.collections is None

# Generated at 2022-06-22 11:34:19.029057
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch._collections.default() == _ensure_default_collection()

# Generated at 2022-06-22 11:34:20.552343
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionsearch = CollectionSearch()
    assert collectionsearch._collections._value is not None

# Generated at 2022-06-22 11:34:23.081271
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    obj._load_collections("_load_collections", None)
    assert(obj._collections.default == ['ansible.builtin'])

# Generated at 2022-06-22 11:34:33.797169
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import os
    import tempfile
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    # Create temp directory to store some files
    temp_dir = tempfile.TemporaryDirectory()
    temp_file = temp_dir.name + '/' + 'test_file.yml'
    temp_host_file = temp_dir.name + '/' + 'host_file.yml'
    
    # Create a yaml file to store test data

# Generated at 2022-06-22 11:34:34.736421
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    a = CollectionSearch()
    assert a is not None

# Generated at 2022-06-22 11:34:36.723175
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.play_context import PlayContext

    c = CollectionSearch()

    assert c._collections._length_constraint == 2048

# Generated at 2022-06-22 11:36:31.593082
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == AnsibleCollectionConfig.default_collection

# Generated at 2022-06-22 11:36:34.282160
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # create a instance of CollectionSearch
    x = CollectionSearch()

    # check the default value of collections
    default_value = ['ansible.builtin']
    assert default_value == x._collections

# Generated at 2022-06-22 11:36:37.786683
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    # Test if we have the right collections
    assert c._collections == _ensure_default_collection()
    # Test if we have the right load_collections method
    assert str(c._load_collections) == str(_ensure_default_collection)

# Generated at 2022-06-22 11:36:41.564374
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # testing empty list
    test = CollectionSearch()
    assert test.collections is None
    # testing with a collection
    test = CollectionSearch(collections=["test_collection"])
    assert test.collections == ["test_collection"]



# Generated at 2022-06-22 11:36:43.223845
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    assert collections._collections is not None

# Generated at 2022-06-22 11:36:50.771806
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search_obj = CollectionSearch.__new__(CollectionSearch)
    # below statements create a attributes of CollectionSearch class
    collection_search_obj._collections = ['ansible_collections.test.test_collection_loader']
    collection_search_obj.collections = ['ansible_collections.test.test_collection_loader']
    # below statements call the __init__ method of CollectionSearch class
    collection_search_obj.__init__()
    assert collection_search_obj.collections == ['ansible_collections.test.test_collection_loader']


# Generated at 2022-06-22 11:36:53.974024
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    result = search._load_collections(None, ["ansible.builtin", "ansible.legacy"])

    assert result == ["ansible.builtin", "ansible.legacy"]

# Generated at 2022-06-22 11:37:02.455664
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.plugins.collection_loader import get_collection_loader

    collection_search = CollectionSearch()

    loader = get_collection_loader()
    loader.set_collection_playbook_paths(['/roles', '/roles/test-role'])

    expected_collections = [u'ansible.builtin,alpha.collection,beta.collection',
                            u'ansible.builtin,alpha.collection',
                            u'ansible.builtin']
    collections = []

    # testing case 1
    loader.set_collection_paths([u'/roles/test-role/collections/alpha.collection',
                                 u'/roles/test-role/collections/beta.collection'])
    collections = collection_search._load_collections('collections', collections)
    assert collections == expected_collections



# Generated at 2022-06-22 11:37:05.172080
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col_search = CollectionSearch()
    col_search.post_validate()
    assert col_search.collections == ['ansible_collections.notmintest.not_a_real_collection']

# Generated at 2022-06-22 11:37:16.345376
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    col = CollectionSearch()

    # For now only testing that none of this fails

    col.get_validated_value('collections', col._collections, None, None)

    col.get_validated_value('collections', col._collections, ['foo'], None)

    col.get_validated_value('collections', col._collections, ['ansible.builtin'], None)

    col.get_validated_value('collections', col._collections, ['ansible.legacy'], None)

    col.get_validated_value('collections', col._collections, ['foo', 'ansible.builtin', 'bar'], None)

    col.get_validated_value('collections', col._collections, ['foo', 'ansible.legacy', 'bar'], None)

    col.get