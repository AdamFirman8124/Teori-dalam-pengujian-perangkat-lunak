

# Generated at 2022-06-22 11:29:49.031577
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c is not None
    # NOTE: This is tested through the 'collections' field test.

# Generated at 2022-06-22 11:29:50.316851
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:29:51.468206
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collections = CollectionSearch()
    assert isinstance(collections, CollectionSearch)

# Generated at 2022-06-22 11:29:53.631766
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs != None
    assert type(cs) == CollectionSearch
    assert cs.collections == _ensure_default_collection()

# Generated at 2022-06-22 11:29:58.559495
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    with open(r'unit/fixtures/multi_collection/tasks/main.yml') as file:
        res = file.read()
        # print(res)
        collection_search = CollectionSearch()
        collection_search.post_validate([], res)
        print(collection_search.__dict__)
    assert True

# Generated at 2022-06-22 11:30:03.635157
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collections = [ 'ansible.builtin' ]
    test_search_attr = 'collections'
    test_search_ds = test_collections
    obj = CollectionSearch()
    results = obj._load_collections(test_search_attr, test_search_ds)
    assert results == test_collections

# Generated at 2022-06-22 11:30:08.681899
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class MyCollectionSearch(CollectionSearch):
        pass

    objCS = MyCollectionSearch()
    objCS.collections = ['ansible.builtin', 'ansible.legacy']
    assert objCS.collections == ['ansible.builtin', 'ansible.legacy']
    assert objCS.check_conditional()
    objCS.set_loader(None)


test_CollectionSearch()

# Generated at 2022-06-22 11:30:10.185398
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj.collections == ['ansible']

# Generated at 2022-06-22 11:30:20.629443
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.collection_loader.collections_find import _AnsibleCollectionsFind
    from ansible.utils.collection_loader._collection_finder import _CollectionsFinder
    collection_search = CollectionSearch()
    assert isinstance(collection_search._collections, FieldAttribute)
    assert collection_search._collections.isa == 'list'
    assert isinstance(collection_search._collections.default(), list)
    assert isinstance(collection_search.set_loader(DataLoader()), DataLoader)
    assert isinstance(collection_search.set_finder(_CollectionsFinder(AnsibleCollectionLoader())), _CollectionsFinder)

# Generated at 2022-06-22 11:30:26.550461
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # a default instance of CollectionSearch class is created
    cs = CollectionSearch()
    assert isinstance(cs, CollectionSearch), "Default instance creation of CollectionSearch failed"

    # a new instance of CollectionSearch class is created with collections = ["ansible.builtin", "ansible.legacy"]
    cs = CollectionSearch(collections=["ansible.builtin", "ansible.legacy"])
    assert isinstance(cs, CollectionSearch), "New instance creation of CollectionSearch failed"


# Generated at 2022-06-22 11:30:45.306666
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.parsing.mod_args.argument_spec import ArgumentSpec
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.collection_loader._combine import _get_collection_name

    class MyClass(AnsibleBaseYAMLObject, CollectionSearch):
        def __init__(self, ds, parent=None):
            self._config = dict(
                spec=ArgumentSpec(),
                parent=parent,
                args=ds,
            )
            self._post_validate_if_needed()

    # create an instance of MyClass
    ds = dict(
        collections=['ansible.builtin', _get_collection_name('test1.test1')]
    )
    my_obj = MyClass(ds=ds)
   

# Generated at 2022-06-22 11:30:49.055993
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    part1 = "ansible.builtin"
    part2 = "ansible.legacy"
    print(cs._collections)
    assert part1 in cs._collections
    assert part2 in cs._collections

# Generated at 2022-06-22 11:30:59.564856
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.utils.yaml import AnsibleLoader
    import types
    import ansible.module_utils._text as text
    data = text.to_bytes("""
---
tasks:
  - name: test
    ping:
    register: result
    collections:
      - ansible.builtin
      - ansible.netcommon
""")
    yaml_obj = AnsibleLoader(data,
                             AnsibleConstructor(
                                 typ='safe',
                                 base_class=AnsibleBaseYAMLObject,
                             )
                             ).get_single_data()
    search = CollectionSearch()

# Generated at 2022-06-22 11:31:10.267064
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    import copy
    import os
    import sys
    import unittest
    import ansible.module_utils.paramiko
    from ansible.module_utils.common._collections_compat import CollectionLoader

    class MyClass(CollectionSearch):
        pass

    class TestPlay(unittest.TestCase):
        def test_collection_search(self):

            # Get the path to the test data
            test_data_path = os.path.join(os.path.dirname(__file__), 'collection_search_data')

            # Create a collection loader for this test
            loader = CollectionLoader(None, '/', [], [])

            # Add the path to the collection loader
            loader._module_utils_paths = [test_data_path]

            # Add the collection loader to Ansible

# Generated at 2022-06-22 11:31:11.540325
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()

# Generated at 2022-06-22 11:31:14.306043
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_CollectionSearch = CollectionSearch()
    assert isinstance(test_CollectionSearch._load_collections("", {}), list)

# Generated at 2022-06-22 11:31:20.041089
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # create CollectionSearch instance
    collection_search = CollectionSearch()
    # validate collections
    collection_search.collections = [
        "my.namespace", "my.namespace.role"]
    # get collections
    collections = collection_search._collections
    # check collections
    assert collections == [
        "my.namespace", "my.namespace.role"]

# Generated at 2022-06-22 11:31:21.525025
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    x = CollectionSearch()
    print(x._load_collections('attr', 'ds'))

# Generated at 2022-06-22 11:31:24.438377
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections is None
    assert collection_search._collections == _ensure_default_collection()


# Generated at 2022-06-22 11:31:34.908963
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    result = search.get_validated_value('collections', '_collections', [], None)
    assert result == ['ansible.builtin', 'ansible.legacy'], \
        'The constructor of class CollectionSearch is not correct!'
    assert search._load_collections('_collections',
                                    ['ansible.builtin', 'ansible.legacy']) == ['ansible.builtin',
                                                                              'ansible.legacy'], \
        'The _load_collections function of class CollectionSearch is not correct!'
    # Unit test for the case that collection_list is None

# Generated at 2022-06-22 11:31:51.667001
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    col_search = CollectionSearch()
    assert col_search._collections == ['ansible.builtin', 'ansible.legacy']
    assert col_search._load_collections(None, None) is None

# Generated at 2022-06-22 11:31:53.723308
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections is not None


# Generated at 2022-06-22 11:31:55.742265
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections == _ensure_default_collection()
    assert collection_search._collections == _ensure_default_collection([])



# Generated at 2022-06-22 11:31:57.371890
# Unit test for constructor of class CollectionSearch

# Generated at 2022-06-22 11:31:59.663599
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:03.460005
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_collection = []
    assert test_collection == _ensure_default_collection(test_collection)

    test_collection = None
    assert test_collection == _ensure_default_collection(test_collection)

    test_collection = ['ansible.collections.test']
    assert _ensure_default_collection(test_collection) == ['ansible.collections.test', 'ansible.legacy']

# Generated at 2022-06-22 11:32:05.763268
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections.default == _ensure_default_collection()

# Generated at 2022-06-22 11:32:12.655448
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    if c._load_collections(None, None) is None:
        assert True, 'Default collection is successfully loaded'
    else:
        assert False, 'Default collection is not loaded'

    if c._load_collections(None, ['fake_collection']) is None:
        assert True, 'Default collection is successfully loaded with additional collection'
    else:
        assert False, 'Default collection is not loaded with additional collection'

    if c._load_collections(None, ['ansible.builtin']) == ['ansible.builtin']:
        assert True, 'Default collection is successfully overwritten'
    else:
        assert False, 'Default collection is not overwritten'


# Generated at 2022-06-22 11:32:18.312283
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    #print(c._collections)
    #print(type(c._collections))
    #print(c._collections)
    #print(type(c._load_collections(None, None)))
    #print(c._load_collections(None, None))
    pass

if __name__ == "__main__":
    test_CollectionSearch()

# Generated at 2022-06-22 11:32:24.857876
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # overrides is None by default
    c = CollectionSearch(collections=['test1.test1', 'test2.test2'])
    assert c._collections.default == ['test1.test1', 'test2.test2']
    assert c.collections == ['test1.test1', 'test2.test2']
    c = CollectionSearch(collections=None)
    assert c._collections.default == 'ansible.builtin'

# Generated at 2022-06-22 11:32:54.030903
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections == _ensure_default_collection()
    #assert obj._collections == ['ansible.builtin', 'ansible.legacy']

# Generated at 2022-06-22 11:32:56.439744
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test = CollectionSearch()
    assert test._collections == _ensure_default_collection(), "_collections should be %s" % (test._collections)

# Generated at 2022-06-22 11:32:59.416897
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # instantiate CollectionSearch class
    obj = CollectionSearch()

    # assert instance variables
    assert obj._collections == _ensure_default_collection(collection_list=None)



# Generated at 2022-06-22 11:33:00.962605
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    # TODO: add unit test
    pass

# Generated at 2022-06-22 11:33:02.911262
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    ds = dict()
    cs = CollectionSearch()
    cs._load_collections('collections', ds)

# Generated at 2022-06-22 11:33:05.308633
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collectionSearch = CollectionSearch()
    assert collectionSearch._collections.default() == _ensure_default_collection()


# Generated at 2022-06-22 11:33:06.833610
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search.collections == None

# Generated at 2022-06-22 11:33:07.835040
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search != None

# Generated at 2022-06-22 11:33:19.537763
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    print("Unit test for constructor of class CollectionSearch")
    display = Display()
    collection_search = CollectionSearch()
    display.display("collection_search= %s" % collection_search)
    display.debug("type(collection_search)= %s" % type(collection_search))
    display.debug("dir(collection_search)= %s" % dir(collection_search))
    display.debug("vars(collection_search)= %s" % vars(collection_search))
    display.debug("collection_search._collections= %s" % collection_search._collections)
    display.debug("collection_search._collections.priority= %s" % collection_search._collections.priority)

# Generated at 2022-06-22 11:33:24.215039
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_class_instance = CollectionSearch()
    test_class_instance.collections('ansible.builtin')
    assert test_class_instance.collections == 'ansible.builtin'
    assert test_class_instance._collections == 'ansible.builtin'

# Generated at 2022-06-22 11:33:53.312465
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    print(cs.collections)
    
    
if __name__ == "__main__":
    cs = CollectionSearch()
    print(cs.collections)

# Generated at 2022-06-22 11:33:54.687245
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
  collectionSearch = CollectionSearch()
  assert(collectionSearch.collections is not None)

# Generated at 2022-06-22 11:33:56.394644
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    search = CollectionSearch()
    assert search.collections == _ensure_default_collection(None)

# Generated at 2022-06-22 11:34:03.588834
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections == _ensure_default_collection()
    assert CollectionSearch()._collections == _ensure_default_collection(collection_list=None)
    assert CollectionSearch()._collections == _ensure_default_collection(collection_list=['col1', 'col2'])
    assert CollectionSearch()._collections == ['col1', 'col2', 'ansible.builtin']

# Generated at 2022-06-22 11:34:04.613874
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    l = CollectionSearch()
    assert l

# Generated at 2022-06-22 11:34:08.339193
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    collection_search.collections = ['random_collection']
    print(collection_search.collections)

# Entrypoint to test CollectionSearch class

# Generated at 2022-06-22 11:34:19.984828
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    variable_manager =  None
    loader = None
    templar = None
    shared_loader_obj = None
    collection_loader = None
    options = None
    variable_manager = None
    loader = None
    passwords = None
    display = None

    all_vars = dict(
        ansible_collection_name="my.collection",
        ansible_collections=["my.collection"],
    )

    cs = CollectionSearch()
    cs.vars = all_vars
    cs.display = display
    cs.variable_manager = variable_manager
    cs.loader = loader
    cs.shared_loader_obj = shared_loader_obj
    cs.collection_loader = collection_loader
    cs.options = options
    cs.variable_manager = variable_manager
    cs.loader = loader

# Generated at 2022-06-22 11:34:22.597117
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    test_CollectionSearch_class = CollectionSearch()
    assert test_CollectionSearch_class is not None

# Generated at 2022-06-22 11:34:25.339833
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections.field_name == 'collections'
    assert collection_search._collections.static



# Generated at 2022-06-22 11:34:27.722755
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection = CollectionSearch()
    assert [''] == collection._collections.default('')

# Generated at 2022-06-22 11:35:22.843466
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    v = CollectionSearch()
    assert isinstance(v.__dict__, type({}.__class__))
    assert isinstance(v._collections, list)

# Generated at 2022-06-22 11:35:28.205418
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    config = CollectionSearch()
    assert config._collections.field_name == 'collections'
    assert config._collections.default is _ensure_default_collection
    assert config._collections.always_post_validate is True
    assert config._collections.static is True
    assert config._collections.instance_type is list
    assert config._collections.listof is string_types


# Generated at 2022-06-22 11:35:32.167211
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._load_collections('collections', ['ansible.posix']) == ['ansible.posix']
    assert collection_search._load_collections('collections', None) == ['ansible.builtin']

# Generated at 2022-06-22 11:35:34.149069
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._load_collections()


# Generated at 2022-06-22 11:35:35.325698
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs is not None

# Generated at 2022-06-22 11:35:36.705770
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search

# Generated at 2022-06-22 11:35:39.046209
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():

    class Test(CollectionSearch):
        pass

    test = Test({})
    assert test._collections == _ensure_default_collection()

# Generated at 2022-06-22 11:35:42.533198
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    c = CollectionSearch()
    assert c is not None
    # at this point, the collections list is empty, because it is not formed
    # until the collection_loader module is loaded and plugins are discovered.
    assert len(c._data['collections']) == 0



# Generated at 2022-06-22 11:35:48.306950
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import pytest
    collection_list = ["ansible.builtin", "ansible.mola"]
    my_collection_search = CollectionSearch()
    my_collection_search.collections = collection_list
    assert my_collection_search.collections == collection_list

# Generated at 2022-06-22 11:35:49.508943
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()

    print("collections:", obj.collections)

# Generated at 2022-06-22 11:37:45.989438
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    assert cs._collections == []
    assert cs._collections is cs.collections


# Generated at 2022-06-22 11:37:55.593829
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert obj._collections.name == 'collections'
    assert obj._collections.isa == 'list'
    assert obj._collections.listof == string_types
    assert obj._collections.priority == 100
    assert obj._collections.default == _ensure_default_collection
    assert obj._collections.always_post_validate
    assert obj._collections.static
    assert obj._collections.default_inherit == True
    assert obj._collections.required == False
    assert obj._collections.private == False
    assert obj._collections.private_exclude == False
    assert obj._collections.deprecated == None

# Generated at 2022-06-22 11:37:58.183963
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch(collections = ['col1', 'col2'])
    assert cs.collections == ['col1', 'col2']

# Generated at 2022-06-22 11:37:59.555982
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cS = CollectionSearch()
    cS.post_validate({}, True)

# Generated at 2022-06-22 11:38:02.233329
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    cs = CollectionSearch()
    if not cs is None:
        print('PASS')
    else:
        print('FAIL')


# Generated at 2022-06-22 11:38:10.524785
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    class Task(CollectionSearch):
        def __init__(self, collection_list=None):
            self.collections = collection_list

    # TODO: FIXME: This doesn't work
    #assert CollectionSearch._collections.default() == ['ansible_collections.overrides']
    #assert type(CollectionSearch._collections.default()) == list
    #assert CollectionSearch._collections.default() == ['ansible_collections.overrides']
    assert Task._collections.default() == ['ansible_collections.overrides']
    assert type(Task._collections.default()) == list

    # No value for collections:
    task = Task()
    assert task._load_collections(None, None) == ['ansible_collections.overrides']

    # User provided a collection list:
    coll_list

# Generated at 2022-06-22 11:38:12.292782
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    s = CollectionSearch()
    assert s._collections.default() == _ensure_default_collection(), "_collections.default() is not working"

# Generated at 2022-06-22 11:38:14.105573
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    assert CollectionSearch()._collections.default == ['ansible.builtin']
    assert CollectionSearch(collections=['foo.bar'])._collections.value == ['foo.bar','ansible.builtin']

# Generated at 2022-06-22 11:38:17.449958
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    collection_search = CollectionSearch()
    assert collection_search._collections is not None

# Generated at 2022-06-22 11:38:28.698510
# Unit test for constructor of class CollectionSearch
def test_CollectionSearch():
    obj = CollectionSearch()
    assert ['ansible.builtin', 'ansible.legacy'] == obj._load_collections(None, None)
    assert ['ansible.builtin', 'ansible.legacy'] == obj._load_collections(None, [])
    assert ['ansible.builtin', 'ansible.legacy'] == obj._load_collections(None, 'test')
    assert ['test'] == obj._load_collections(None, ['test'])
    assert ['test'] == obj._load_collections(None, ['test', 'test2'])
    assert ['test', 'ansible.builtin', 'ansible.legacy'] == obj._load_collections(None, ['test', 'ansible.builtin', 'ansible.legacy'])
    assert ['test', 'ansible.builtin']