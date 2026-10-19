

# Generated at 2022-06-13 09:13:17.862834
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    tags = ['t1', 't2', 't3']

    # Test with no tags
    t = Taggable()
    t.tags = []

    only_tags = []
    skip_tags = []
    all_vars = {}
    should_run = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run == True

    only_tags = ['t1']
    skip_tags = []
    all_vars = {}
    should_run = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run == False

    only_tags = []
    skip_tags = ['t1']
    all_vars = {}

# Generated at 2022-06-13 09:13:25.433572
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # 1. test if the current item should not be executed depending on tag options
    # 1.1 test the case only_tags=all AND skip_tags=all
    only_tags, skip_tags = ['all'], ['all']
    all_vars = dict()
    class_Taggable = Taggable()
    class_Taggable.tags = []
    class_Taggable.untagged = ['untagged']
    assert class_Taggable.evaluate_tags(only_tags, skip_tags, all_vars) == False
    
    # 1.2 test the case only_tags=all AND skip_tags=all, tagged AND always
    only_tags, skip_tags = ['all'], ['all', 'tagged', 'always']
    all_vars = dict()
    class_Taggable = Taggable

# Generated at 2022-06-13 09:13:32.045622
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    import sys

    # Add the directory containing your module to the Python path (wants absolute paths)
    module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    if module_path not in sys.path:
        sys.path.insert(0, module_path)

    # create a mock class that we can use to test the method evaluate_tags
    class MockTaggable(Taggable):
        def __init__(self):
            self._tags = {}

    mock_vars = dict()

    # Hash of test cases

# Generated at 2022-06-13 09:13:40.867896
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task

    # setup
    play = ansible.playbook.play.Play()
    play.hosts = "host1"
    play.name = "play1"

    # test 1 tags not enabled
    taskIncl = TaskInclude()
    taskIncl.name = "task1"
    taskIncl.tags = "tag1"
    taskIncl.prereq = []
    taskIncl.postres = []
    taskIncl.deps = []
    taskIncl._parent = play
    assert taskIncl.evaluate_tags(only_tags=False, skip_tags=False, all_vars=dict())

    # test 2 include task
    taskIncl

# Generated at 2022-06-13 09:13:45.785437
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import json
    import tests.data.task_include as data_task_include

    # Load the task include data
    task_include_data = json.loads(data_task_include.task_data)

    tags = task_include_data["tasks"][0]["with_items"][0]["tags"]
    # with_items attribute is of type list
    assert isinstance(tags, list)
    # with_items attribute is of length 2
    assert len(tags) == 2
    # with item value is 'item1'
    assert tags[0] == 'item1'
    # with item value is 'item2'
    assert tags[1] == 'item2'

    # Load the task include data
    task_include_data = json.loads(data_task_include.task_data)

    # Get the task

# Generated at 2022-06-13 09:13:58.783629
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import itertools


# Generated at 2022-06-13 09:14:13.077264
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Test(Taggable):
        tags = ['test1', 'test2']

    t = Test()
    assert t.evaluate_tags(None, None, None)
    assert not t.evaluate_tags([], None, None)
    assert t.evaluate_tags(['test1','test2','all','always','tagged'], None, None)
    assert t.evaluate_tags(['all','always','tagged'], None, None)
    assert t.evaluate_tags(['test1','test2','tagged'], None, None)
    assert t.evaluate_tags(['tagged'], None, None)
    assert t.evaluate_tags(['all'], None, None)
    assert not t.evaluate_tags(['never'], None, None)

# Generated at 2022-06-13 09:14:24.407232
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Imports for this test
    import unittest
    import sys
    from ansible.playbook.task_include import TaskInclude

    from ansible.template import Templar

    # Create test class Taggable
    class TaggableTest(Taggable):
        def __init__(self, task=None, only_tags=None, skip_tags=None, loader=None, variable_manager=None, use_handlers=False):
            super(TaggableTest, self).__init__()
            self._task = task
            self._only_tags = only_tags
            self._skip_tags = skip_tags
            self._loader = loader
            self._variable_manager = variable_manager
            self._use_handlers = use_handlers

    # Create test class TaskInclude

# Generated at 2022-06-13 09:14:36.565008
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Helper function to test the evaluate_tags() method of the Taggable class.
    '''
    import unittest

    class TestTaggable(Taggable):
        def __init__(self, tags=None):
            self.tags = tags
            self._loader = None

    class TestTaggableClass(unittest.TestCase):
        # Test the evaluate_tags() method
        def test_evaluate_tags(self):

            # Set the tags and tags options
            tags = ["python", "secure"]
            only_tags = {"python"}
            skip_tags = {"secure"}
            all_vars = {}

            # Call the method
            taggable = TestTaggable(tags=tags)

# Generated at 2022-06-13 09:14:45.320477
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    import pytest

    # when an item has no tags
    only_tags = frozenset(['tag_one', 'tag_two'])
    item = Task()
    item._load_name('Some task with no tags')
    assert item.evaluate_tags(only_tags, None, {}) == True

    # when an item has tags and `only_tags` is empty
    skip_tags = frozenset(['skip_this'])
    item = Task()
    item._load_name('Some task with tags')
    item

# Generated at 2022-06-13 09:15:04.867247
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Taggable class is not being tested here but
    # this test is present to mock out Taggable class
    class Taggable(object):
        def __init__(self, tags, playbook_tags=None):
            self.tags = tags

    # In order to test evaluate_tags, a mock of AnsibleLoader has to be created
    # and passed to Taggable instance
    class AnsibleLoader(object):
        def __init__(self, file_name):
            self.file_name = file_name

    # Empty dictionary is passed to Taggable class but it is not required to
    # be passed as the dict is not used in evaluate_tags()
    vars = {}


# Generated at 2022-06-13 09:15:16.189923
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        pass
    only_tags = set(['mytag'])
    skip_tags = set([])

    # check item with no tags
    t = MyTaggable()
    t.tags = []
    assert t.evaluate_tags(only_tags, skip_tags, {}) is False

    # check item with mytag
    t = MyTaggable()
    t.tags = ['mytag']
    assert t.evaluate_tags(only_tags, skip_tags, {}) is True

    # check item with always
    t = MyTaggable()
    t.tags = ['mytag', 'always']
    assert t.evaluate_tags(only_tags, skip_tags, {}) is True

    # check item with never
    t = MyTaggable()

# Generated at 2022-06-13 09:15:25.933941
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable.evaluate_tags(Taggable(), [], [], {}) == True
    assert Taggable.evaluate_tags(Taggable(), ['always'], [], {}) == True
    assert Taggable.evaluate_tags(Taggable(), [], ['all'], {}) == False
    assert Taggable.evaluate_tags(Taggable(), ['all'], ['all'], {}) == False
    assert Taggable.evaluate_tags(Taggable(), ['all'], ['never'], {}) == True
    assert Taggable.evaluate_tags(Taggable(), ['all'], ['always'], {}) == True
    assert Taggable.evaluate_tags(Taggable(), ['never'], [], {}) == False

# Generated at 2022-06-13 09:15:34.494356
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Sample(Taggable):
        name = "Sample"

    sample = Sample()
    sample.tags = ['foo', 'bar', 'never']

    # Case 1: No tags, no skip
    assert(sample.evaluate_tags(None, [], {}))

    # Case 2: no tags, skip
    assert(not sample.evaluate_tags(None, ["skip"], {}))

    # Case 3: tags, no skip
    assert(sample.evaluate_tags(["foo"], [], {}))

    # Case 4: tags, skip
    assert(not sample.evaluate_tags(["foo"], ['skip', "bar"], {}))


# Generated at 2022-06-13 09:15:43.802885
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    import os

    class FakeClass:
        tags = []

    class TestEvaluteTags(unittest.TestCase):
        ''' Test the module_utils.Taggable evaluate_tags method '''
        def setUp(self):
            self.fake = FakeClass()

        def test_passing_test(self):
            ''' Test a simple passing test '''
            self.fake.tags = ['test']
            result = Taggable.evaluate_tags(self.fake, ['test'], None, {})
            self.assertTrue(result)

        def test_failing_test(self):
            ''' Test a simple failing test '''
            self.fake.tags = ['test']
            result = Taggable.evaluate_tags(self.fake, ['notest'], None, {})


# Generated at 2022-06-13 09:15:55.146603
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass:
        tags = []

    t_test_obj = TestClass()

    t_test_obj.tags = ['test_tag1']
    only_tags = {'all', 'test_tag1'}
    skip_tags = {'test_tag2'}
    result = t_test_obj.evaluate_tags(only_tags, skip_tags, all_vars=None)
    assert result is True

    t_test_obj.tags = ['test_tag2']
    only_tags = {'all', 'test_tag1'}
    skip_tags = {'test_tag2'}
    result = t_test_obj.evaluate_tags(only_tags, skip_tags, all_vars=None)
    assert result is False


# Generated at 2022-06-13 09:16:05.426922
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader

    PlayContext._options = dict(tags=['tagA', 'tagB'], skip_tags=['tagC'], host_vars=dict({'test': 'var'}))
    PlayContext._users = dict(remote_user='user', become_user='become_user')
    PlayContext._privilege_escalation = dict(become='yes', become_method='sudo', become_user='root')
    PlayContext._connection = dict(connection='ssh', network_os='network os')
    mytags = dict(tags=['tagA', 'tagB'], skip_tags=['tagC'])

# Generated at 2022-06-13 09:16:14.875173
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test normal execution
    only_tags = None
    skip_tags = None
    all_vars = None
    # Set global tags
    global_only_tags = ['tag1', 'tag2']
    global_skip_tags = ['tag3', 'tag4']
    # Create object of class Taggable
    class TaggableTest(Taggable):
        pass
    # Execute evaluate_tags method
    taggable_test = TaggableTest()
    # Set tags of taggable_test
    taggable_test.tags = ['global_tag1', 'global_tag2']
    result = taggable_test.evaluate_tags(only_tags, skip_tags, all_vars)
    # Verify the result
    assert result

# Generated at 2022-06-13 09:16:21.719295
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    class Test(Taggable):
        pass


# Generated at 2022-06-13 09:16:29.381779
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Test(Taggable):
        tags = ['role1', 'role2', 'role3']

    test = Test()
    assert test.evaluate_tags([], ['role2'], {}) is True, \
        'evaluate_tags with tags {} should return True'.format(test.tags)
    test.tags = ['role2']
    assert test.evaluate_tags([], ['role2'], {}) is False, \
        'evaluate_tags with tags {} should return False'.format(test.tags)
    assert test.evaluate_tags([], [], {}) is True, \
        'evaluate_tags with tags {} should return True'.format(test.tags)
    assert test.evaluate_tags(['role1'], [], {}) is False, \
        'evaluate_tags with tags {} should return False'.format(test.tags)


# Generated at 2022-06-13 09:16:50.685669
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableTest(Taggable):
        pass

    class BlockTest(Taggable):
        pass

    t = TaggableTest()

    t.always_run = False

# Generated at 2022-06-13 09:16:56.135377
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    taggable = Taggable()

    taggable.tags = ['a','b']
    only_tags = []
    skip_tags = []
    all_vars = []
    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars)

    taggable.tags = ['all']
    only_tags = ['all']
    skip_tags = []
    all_vars = []
    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars)

    taggable.tags = ['a','b']
    only_tags = ['a']
    skip_tags = []
    all_vars = []
    assert taggable.evaluate_tags(only_tags, skip_tags, all_vars)


# Generated at 2022-06-13 09:17:07.481674
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import unittest
    import sys
    from ansible.playbook.block import Block

    class FakeLoader:
        def __init__(self):
            self.paths = []
        def get_basedir(self, path):
            return '.'
        def path_dwim(self, path):
            return path

    class MyBlock(Block, Taggable):
        _parent = None
        _default_vars = {}
        name = 'MyBlock'

    class TestTaggable(unittest.TestCase):

        def setUp(self):
            self.block = MyBlock(loader=FakeLoader(), play=None)

        def test_evaluate_tags_no_tags(self):
            only_tags=[]
            skip_tags=[]
            all_vars = {}

# Generated at 2022-06-13 09:17:20.222850
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.constants import DEFAULT_VAULT_PASSWORD_FILE
    from ansible.template import Templar
    from ansible.vars.clean import clean_facts
    from ansible.vars.unsafe_proxy import wrap_var

    tmp = wrap_var(clean_facts({'gid': 0, 'group': 'root', 'home': '/root', 'name': 'root', 'shell': '/bin/bash', 'uid': 0, 'user': 'root'}))
    templar = Templar(loader=None, variables=tmp)

    vault_password = 'secret'

# Generated at 2022-06-13 09:17:30.255966
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()

    only_tags = set([
        'tag1',
        'tag2',
        'tag3',
        'tagged',
        'all',
        'always'
    ])
    skip_tags = set([
        'tag4',
        'tag5',
        'tag6',
        'tagged',
        'all',
        'always'
    ])
    deps = []

    class Test1(Taggable):
        tags = ['tag1', 'tag7', 'tag8', 'always']
        depends_on = deps

    class Test2(Taggable):
        tags = ['tag2', 'tag9', 'tag10', 'never']
        depends_on = deps


# Generated at 2022-06-13 09:17:40.067764
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Test case for all possible options (only_tags, skip_tags, tags)
    For the list of tags, we use the given set by the ansible-playbook --list-tasks
    '''

# Generated at 2022-06-13 09:17:51.342501
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Test conditions when no tags, only_tags and skip_tags are all empty
    def run_test_with(data):
        result = data['object'].evaluate_tags(data['only_tags'], data['skip_tags'], data['all_vars'])
        assert(result == data['expected_result'])

    test_data = [
        {
            'object': Taggable(),
            'only_tags': [],
            'skip_tags': [],
            'all_vars': {},
            'expected_result': True
        },
        {
            'object': Taggable(),
            'only_tags': None,
            'skip_tags': None,
            'all_vars': {},
            'expected_result': True
        }
    ]

# Generated at 2022-06-13 09:18:05.966869
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    from ansible.utils.unicode import to_unicode
    from ansible.utils.vars import combine_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    paths = os.path.dirname(__file__)
    inventory = InventoryManager(loader=loader, sources='/etc/ansible/hosts')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    class FakeClass(Taggable):

        _tags = FieldAttribute(isa='list')

        def __init__(self, tags, _hosts=None, _loader=None, _variable_manager=None):
            self.tags = tags
            self._host

# Generated at 2022-06-13 09:18:12.404925
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']
    all_vars = {'tags': ['tag1', 'tag2']}

    t = Taggable()
    assert(t.evaluate_tags(only_tags, skip_tags, all_vars))

if __name__ == '__main__':
    test_Taggable_evaluate_tags()

# Generated at 2022-06-13 09:18:24.250677
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    taggableObj = Taggable()
    test1_only_tags = ['test1']
    test1_skip_tags = []
    test1_tags = ['test1']
    test1_all_vars = dict()
    # check for only_tags and skip_tags
    assert taggableObj.evaluate_tags(test1_only_tags, test1_skip_tags, test1_all_vars)
    # check for skip_tags
    test1_only_tags = []
    assert taggableObj.evaluate_tags(test1_only_tags, test1_skip_tags, test1_all_vars)
    # check for only_tags
    test1_skip_tags = ['test2']

# Generated at 2022-06-13 09:19:00.690256
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Note: _evaluate_tags expects an object with _loader and tags attributes
    class MockTaggable(Taggable):
        def __init__(self, loader, tags):
            self._loader = loader
            self.tags = tags
 
    # Test data
    taggable_a = MockTaggable(None, ['foo'])
    taggable_b = MockTaggable(None, ['bar'])
    taggable_c = MockTaggable(None, ['foo', 'bar'])
    taggable_d = MockTaggable(None, ['foo', 'always'])
    taggable_e = MockTaggable(None, ['foo', 'never'])
    taggable_f = MockTaggable(None, [])


# Generated at 2022-06-13 09:19:08.162176
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role.include import IncludeRole
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.add_group('all')
    variable_manager.add_host(Host(name='localhost'))
    variable_manager.add_host(Host(name='host1'))
    variable_manager.add_host(Host(name='host2'))
    variable_manager.add_host(Host(name='host3'))
    variable_manager.add_host(Host(name='host4'))

# Generated at 2022-06-13 09:19:17.724698
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:19:23.315467
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    class Taggable_evaluate_tags(unittest.TestCase):
        def setUp(self):
            self.taggable = Taggable()
            self.taggable.tags = ['a', 'b' , 'c']
            self.only_tags = set(['a', 'd'])
            self.skip_tags = set(['c'])
            self.all_vars = { }

        def test_should_run_true(self):
            self.assertTrue(self.taggable.evaluate_tags(self.only_tags, self.skip_tags, self.all_vars))

    unittest.main()

# Generated at 2022-06-13 09:19:24.225674
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass
    #TODO

# Generated at 2022-06-13 09:19:30.333875
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    tags = ['tag1', 'tag2', 'tag3', 'always']
    only_tags = ['tag1', 'tag2', 'tag3', 'always']
    skip_tags = []
    all_vars = {}
    tagg = Taggable()
    tagg.tags = tags
    res = tagg.evaluate_tags(only_tags, skip_tags, all_vars)
    assert res == True, "Test failed"

    only_tags = ['tag1', 'tag2', 'tag3']
    res = tagg.evaluate_tags(only_tags, skip_tags, all_vars)
    assert res == True, "Test failed"

    # Test default value
    tagg.tags = None
    res = tagg.evaluate_tags(only_tags, skip_tags, all_vars)
   

# Generated at 2022-06-13 09:19:41.380959
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    only_tags = ['tag1','tag2']
    skip_tags = ['skip1','skip2']

    test_obj=Taggable()
    test_obj.tags=['tag1','tag2']

    assert(test_obj.evaluate_tags(only_tags=only_tags,skip_tags=skip_tags,all_vars={}) is True)

    test_obj.tags=['tag1','tag2','skip1']
    assert(test_obj.evaluate_tags(only_tags=only_tags,skip_tags=skip_tags,all_vars={}) is False)

    del test_obj
    test_obj=Taggable()
    test_obj.tags=['tag1','tag2','skip1']

# Generated at 2022-06-13 09:19:52.725800
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass(Taggable):
        _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)

    t = TestClass()
    assert t.evaluate_tags(only_tags=['a', 'b'], skip_tags=['c', 'd'], all_vars=dict(orig_t=t)) == True

    t = TestClass()
    t._tags = []
    assert t.evaluate_tags(only_tags=['a', 'b'], skip_tags=['c', 'd'], all_vars=dict(orig_t=t)) == False

    t = TestClass()
    t._tags = ['a', 'b', 'c']

# Generated at 2022-06-13 09:20:03.201377
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    # with no tags set
    assert t.evaluate_tags(only_tags = [], skip_tags = [])
    assert t.evaluate_tags(only_tags = ['all'], skip_tags = [])
    assert t.evaluate_tags(only_tags = ['all'], skip_tags = ['always'])
    assert not t.evaluate_tags(only_tags = ['all'], skip_tags = ['never'])
    assert not t.evaluate_tags(only_tags = ['untagged'], skip_tags = [])
    assert not t.evaluate_tags(only_tags = ['tagged'], skip_tags = [])
    assert t.evaluate_tags(only_tags = ['tagged'], skip_tags = ['untagged'])
    # with a single tag of 'test' set


# Generated at 2022-06-13 09:20:16.651254
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task
    task = ansible.playbook.task.Task()
    task.tags = ['foo', 'bar']

    assert task.evaluate_tags([], [], {})
    assert task.evaluate_tags(['foo', 'bar'], [], {})
    assert task.evaluate_tags([], ['foo', 'bar'], {})
    assert task.evaluate_tags(['foo'], ['bar'], {})
    assert task.evaluate_tags(['bar'], ['foo'], {})
    assert task.evaluate_tags(['always'], ['never'], {})
    assert not task.evaluate_tags([], ['foo', 'bar', 'baz'], {})
    assert task.evaluate_tags(['tagged'], [], {})

# Generated at 2022-06-13 09:21:17.283585
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    from units.mock.loader import DictDataLoader

    # safe_eval is not used here, because it does not return bools
    class Options:
        start_at_task = None
        step = None
        diff = False
        syntax = False
        connection = 'local'
        module_path = None
        forks = 5
        remote_user = 'root'
        remote_pass = None
        remote_port = None
        private_key_file = None
        sudo_user = 'root'
        sudo = False
        sudo_pass = None
        became = False
        become_method = None
        become_user = None
        become_pass = None
        tags = None
        skip_tags = None
        check = False
        extra_vars = []
        verbosity = 0

   

# Generated at 2022-06-13 09:21:28.507346
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class mock_task(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = []
            self.run = []

    # check always if no skip tags are passed
    task = mock_task()
    task.tags = ['always']
    assert task.evaluate_tags('', '', {})
    task.tags = ['never']
    assert not task.evaluate_tags('', '', {})

    # check all if no skip tags are passed
    task = mock_task()
    task.tags = ['all']
    assert task.evaluate_tags('', '', {})
    task.tags = ['never']
    assert not task.evaluate_tags('', '', {})

    # skip all tag if all is passed as skip tag
    task = mock_task()

# Generated at 2022-06-13 09:21:40.267257
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTask(Taggable):

        _valid_keys = frozenset(['tags', 'tasks', 'name', 'priority'])

        def __init__(self, tags, **kwargs):
            super(MockTask, self).__init__(**kwargs)
            self.tags = tags
            self.tasks = [MockTask('x', tags='x'), MockTask('y', tags='y'), MockTask('z', tags='z')]

    class MockPlaybook(Taggable):

        _valid_keys = frozenset(['tasks', 'name', 'priority'])

        def __init__(self, tags, **kwargs):
            super(MockPlaybook, self).__init__(**kwargs)
            self.tags = tags

# Generated at 2022-06-13 09:21:49.172128
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task
    import collections
    import copy

    # Intantiate a mocked task
    task = ansible.playbook.task.Task()
    task.tags = []

    # Define the different tags combinations
    tags = [
        [], # tags is empty
        ['always'],
        ['never'],
        [1],
        ['tag1', 'tag2'],
    ]

    # Define inputs
    only_tags = [
        set([]),
        set(['all']),
        set([]),
        set(['always']),
        set([]),
        set(['tag1']),
        set(['tag1', 'tag2', 'tag3'])
    ]

# Generated at 2022-06-13 09:22:00.808474
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        def __init__(self):
            # Set tags and only_tags,skip_tags attributes
            self.tags = ['tag1','tag2']
            self.only_tags = ['tag1','tagged']
            self.skip_tags = ['tag2']
            # Set all_vars to empty dict
            self.all_vars = dict()

    # Evaluate if the taggable item should run
    # Result should be True
    obj = MyTaggable()
    assert obj.evaluate_tags(obj.only_tags,obj.skip_tags,obj.all_vars) == True


# Generated at 2022-06-13 09:22:16.043030
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=None)
    variable_manager.set_inventory(inventory)

    item = Task()

    item.tags = ['always', 'test']
    only_tags = ['all', 'test']
    skip_tags = []

    assert item.evaluate_tags(only_tags, skip_tags, variable_manager.get_vars()) is True

    only_tags = []
    skip_tags = ['all', 'test']


# Generated at 2022-06-13 09:22:27.493007
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """
    Unit test for method evaluate_tags of class Taggable
    """
    # Taggable is an abstract class, so create a concrete class that inherits
    # from it for testing
    class TestObject(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # only_tags and skip_tags are both None
    testobj = TestObject(tags=["tag1", "tag2"])
    only_tags = None
    skip_tags = None
    res = testobj.evaluate_tags(only_tags, skip_tags, {})
    assert res == True

    # only_tags is None, skip_tags is not None
    testobj = TestObject(tags=["tag1", "always", "never"])
    only_tags = None

# Generated at 2022-06-13 09:22:36.200998
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    from ansible.playbook.task import Task

    fname = os.path.basename(__file__)
    t = Task()

    # only_tags
    # 'all' and 'never' are special tags
    # if 'never' is present, then we need to return False
    # if 'all' is present, and 'never' is not present, then return True
    # Tagged means the task has tags
    # Untagged means the task has no tags
    # if 'tagged' is present, then return True if task has tags, else return False
    # if 'untagged' is present, then return True if task has no tags, else return False
    t.tags = ['foo', 'bar']
    assert t.evaluate_tags(['foo', 'untagged'], [], {},) == True
    assert t

# Generated at 2022-06-13 09:22:41.804838
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible import constants as C

    C.TAGS_RUN_ONLY_IF_INCLUDED = 'include_tags'
    C.TAGS_SKIP_IF_ANY_INCLUDED = 'skip_tags'

    from units.mock.loader import DictDataLoader


# Generated at 2022-06-13 09:22:46.707714
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from collections import namedtuple

    task = namedtuple('task', ['tags'])

    # Base cases
    assert Taggable.evaluate_tags(task, only_tags='always', skip_tags=[], all_vars={}) == True
    assert Taggable.evaluate_tags(task, only_tags=[], skip_tags='never', all_vars={}) == True
    assert Taggable.evaluate_tags(task, only_tags=[], skip_tags=['never'], all_vars={}) == True
    assert Taggable.evaluate_tags(task, only_tags=[], skip_tags=[], all_vars={}) == True

    # Only
    assert Taggable.evaluate_tags(task, only_tags='always', skip_tags=[], all_vars={}) == True
    assert Taggable.evaluate