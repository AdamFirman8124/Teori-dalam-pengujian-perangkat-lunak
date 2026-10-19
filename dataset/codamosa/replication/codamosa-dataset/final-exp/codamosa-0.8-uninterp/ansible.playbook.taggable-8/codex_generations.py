

# Generated at 2022-06-13 09:13:20.944275
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test 1: no only_tags and skip_tag, should run
    class Test_Taggable1(Taggable):
        pass

    test = Test_Taggable1()
    should_run = test.evaluate_tags(False, False, dict())
    assert should_run == True
    # Test 2: only_tags contains 'always' and 'all', should run
    class Test_Taggable2(Taggable):
        tags = []
    test = Test_Taggable2()
    test.tags.append('always')
    should_run = test.evaluate_tags(['always','all'], False, dict())
    assert should_run == True
    # Test 3: only_tags contains 'all', but tags has 'never', should not run

# Generated at 2022-06-13 09:13:28.365273
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    task = Task()
    # with defaults
    assert task.evaluate_tags(None, None, {})

    # with only_tags
    assert not task.evaluate_tags(['foo'], None, {})
    task.tags = ['foo']
    assert task.evaluate_tags(['foo'], None, {})
    task.tags = ['foo', 'bar']
    assert task.evaluate_tags(['foo', 'bar'], None, {})
    task.tags = ['foo', 'bar']
    assert not task.evaluate_tags(['baz'], None, {})

test_Taggable_evaluate_tags()

# Generated at 2022-06-13 09:13:38.459869
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(object):
        def __init__(self):
            self._tags = []
    t = Taggable()
    mt = MyTaggable()
    mt.tags = None
    mt.evaluate_tags(['all'], [], {})
    mt.evaluate_tags(['tagged'], [], {})
    mt.evaluate_tags(['tagged'], ['tagged'], {})
    assert mt.evaluate_tags(['all'],['tagged'], {}) == True
    assert t.evaluate_tags([],['tagged'], {}) == True
    assert t.evaluate_tags(['all'],['never'], {}) == True
    assert t.evaluate_tags([],['never'], {}) == True

# Generated at 2022-06-13 09:13:51.145009
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class fake_task(Taggable):
        def __init__(self, tags, only_tags=None, skip_tags=None, all_vars=None):
            self.tags = tags
            self.evaluate_tags(only_tags, skip_tags, all_vars)

    assert fake_task(['a', 'b'],['a'], None, None).should_run == True
    assert fake_task(['a', 'b'],['a'], ['a'], None).should_run == False
    assert fake_task(['a', 'b'],['a'], ['b'], None).should_run == True
    assert fake_task(['a', 'b'],['a', 'c'], None, None).should_run == True

# Generated at 2022-06-13 09:14:02.403920
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    fake_ds = dict(
        always_run=True,
        always_run2=False,
        tags=["tag1", "tag2"],
        tags_var="tag3",
        tags_var2="tag4",
        skip_tags=["tag5"],
        skip_tags_var=["tag6"],
    )
    fake_task = Task.load(fake_ds, variable_manager=VariableManager(), loader=None)

    # Tasks with no tags
    assert fake_task.evaluate_tags(only_tags=["all"], skip_tags=[], all_vars={}) is True

# Generated at 2022-06-13 09:14:10.671049
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest

    class TestTaggable(Taggable):
        def __init__(self):
            self._tags = []

    # only_tags=[], skip_tags=[] and tags=[] is always true
    TestTaggable_instance_01 = TestTaggable()
    TestTaggable_instance_01._tags = []
    only_tags = []
    skip_tags = []
    all_vars = {}
    result = TestTaggable_instance_01.evaluate_tags(only_tags, skip_tags, all_vars)
    print("result: %s" % result)
    assert result == True

    # only_tags=['tag1'], skip_tags=[] and tags=['tag1'] is always true
    TestTaggable_instance_02 = TestTaggable()
    Test

# Generated at 2022-06-13 09:14:19.691191
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class Test(Taggable):

        def __init__(self, tags=None):
            self._tags = tags
            self.tags = self._load_tags(self._tags, self._tags)

        def __repr__(self):
            return '%s(%r)' % (self.__class__.__name__, self.tags)

    t1 = Test(None)
    t2 = Test(['tag1', 'tag2'])
    t3 = Test(['tag1', 'tag2', 'always'])

    # should run
    assert t1.evaluate_tags(['all'], None, dict())
    assert t1.evaluate_tags(None, None, dict())
    assert t1.evaluate_tags(None, ['all'], dict())

# Generated at 2022-06-13 09:14:32.411254
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeTask(Taggable):
        def __init__(self, tags=[]):
            super(FakeTask, self).__init__()
            self.tags = tags

    # test for only_tags options
    t = FakeTask(['always'])
    assert t.evaluate_tags(['always'], [], {})
    assert t.evaluate_tags(['all'], [], {})
    assert t.evaluate_tags(['tagged'], [], {})

    t = FakeTask(['never'])
    assert t.evaluate_tags(['never'], [], {}) == False
    assert t.evaluate_tags(['all'], [], {}) == False
    assert t.evaluate_tags(['tagged'], [], {}) == False

    t = FakeTask(['always', 'never'])
   

# Generated at 2022-06-13 09:14:42.120701
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

    t = TestTaggable(['foo'])
    assert t.evaluate_tags(['foo'], [], {})
    assert not t.evaluate_tags(['bar'], [], {})

    t = TestTaggable(['foo'])
    assert t.evaluate_tags([], ['bar'], {})
    assert not t.evaluate_tags([], ['foo'], {})

    t = TestTaggable(['foo'])
    assert t.evaluate_tags(['foo'], ['bar'], {})
    assert not t.evaluate_tags(['foo'], ['foo'], {})

    t = TestTaggable(['foo'])

# Generated at 2022-06-13 09:14:51.758213
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # mock the class
    class testClass(object):
        tags=[]

    simpletest = testClass()
    simpletest.tags = ["tag1", "tag2"]
    print("Testing evaluate_tags(None, None) - No exclusion: '{0}'".format(simpletest.evaluate_tags(None, None, None)))
    assert simpletest.evaluate_tags(None, None, None) == True

    print("Testing evaluate_tags([\"-tag1\"], None) - Single exclusion: '{0}'".format(simpletest.evaluate_tags(["-tag1"], None, None)))
    assert simpletest.evaluate_tags(["-tag1"], None, None) == False

# Generated at 2022-06-13 09:15:16.134092
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    # No-op case
    assert t.evaluate_tags(None, None, None)

    # Both only_tags and skip_tags are specified
    try:
        t.evaluate_tags(set(['tag1']), set(['tag2']), None)
        assert False, "Should have raised exception"
    except AnsibleError as e:
        assert "only_tags and skip_tags are mutually exclusive" in str(e)

    # No filter case
    assert t.evaluate_tags(set(), set(), None)
    assert t.evaluate_tags(set(['tag1']), set(), None)

    # Run only specific tags
    assert not t.evaluate_tags(set(['tag1']), None, None)

# Generated at 2022-06-13 09:15:25.887412
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # test for default case
    p=Play()
    t=Task()
    t.tags=['always']
    assert(t.evaluate_tags([], [], {}) is True)
    assert(t.evaluate_tags(['all'], [], {}) is True)
    assert(t.evaluate_tags([], ['all'], {}) is True)
    assert(t.evaluate_tags(['all'], ['all'], {}) is True)
    assert(t.evaluate_tags(['all'], ['never'], {}) is True)
    assert(t.evaluate_tags(['all'], ['never', 'all'], {}) is False)

# Generated at 2022-06-13 09:15:36.547130
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    class FakeVarsModule:
        ''' This class is used by the pytest_ansible_playbook test to fake
        the _templar attribute from a Task object. '''

        def __init__(self):
            self.no_log = False
            self.basedir = "./"
            self.vars = {}

        # This method is called by Taggable.evaluate_tags to resolve tags.
        def template(self, var):
            return var

    # Create a dictionary with tags that will be used to create the Task and Block objects.

# Generated at 2022-06-13 09:15:51.971554
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Define test class that will inherit from Taggable
    class TaggableTest(Taggable):
        def __init__(self):
            self._tags = set()

    # Instantiate test class
    taggable = TaggableTest()

    # Create a set of only_tags
    only_tags = set()
    only_tags.add("something else")
    only_tags.add("test1")
    only_tags.add("test2")

    # Verify that a correctly tagged item will be run
    taggable.tags = "test1"
    assert taggable.evaluate_tags(only_tags, set(), {}) == True
    taggable.tags = "test2"
    assert taggable.evaluate_tags(only_tags, set(), {}) == True

    # Verify that an incorrectly tagged item will

# Generated at 2022-06-13 09:15:56.845719
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    import pytest

    class MyPlaybookObject(Base):
        def __init__(self, variable_manager=None, loader=None):
            super(MyPlaybookObject, self).__init__()
            self.variable_manager = variable_manager
            self.loader = loader

    playbook = Playbook()
    my_playbook_object = MyPlaybookObject(variable_manager=playbook.variable_manager, loader=playbook.loader)

    # test with a task

# Generated at 2022-06-13 09:16:06.844713
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    import ansible.constants as C

    # create simple playbook
    playbook_name = 'test'
    playbook = Playbook.load(dict(
        name = playbook_name,
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(
                action = dict(
                    module = 'setup',
                )
            )
        ],
    ), loader=None, variable_manager=None)

    # create play

# Generated at 2022-06-13 09:16:14.379613
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = ['all']
    skip_tags = ['never']
    all_vars = {}

    task = Taggable()
    task.evaluate_tags(only_tags, skip_tags, all_vars)
    assert(task.tags == ['untagged'])

    task.tags = 'always'
    task.evaluate_tags(only_tags, skip_tags, all_vars)
    assert(task.tags == ['always'])

    task.tags = ['always']
    task.evaluate_tags(only_tags, skip_tags, all_vars)
    assert(task.tags == ['always'])

# Generated at 2022-06-13 09:16:20.295401
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Setup
    t = Taggable()
    t.tags = ['foo', 'bar']
    only_tags = ['baz']
    skip_tags = ['bar', 'qux']
    all_vars = dict()
    expected_value = False

    # Test
    result = t.evaluate_tags(only_tags, skip_tags, all_vars)

    # Verify
    assert result == expected_value

# Generated at 2022-06-13 09:16:28.621961
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeLoader():
        pass
    loader = FakeLoader()
    fake_vars = dict()
    fake_block = Taggable()
    fake_block._loader = loader

    # insetance of type FakeBlock
    if not isinstance(fake_block, Taggable):
        raise AssertionError('fake_block is not an instance of FakeBlock')

    # default should_run is True
    should_run = fake_block.evaluate_tags(only_tags=None, skip_tags=None, all_vars=fake_vars)
    if not should_run:
        raise AssertionError('default should_run is False')

    # evaluate_tags with tags = ['all'] should_run = True
    fake_block.tags = ['all']

# Generated at 2022-06-13 09:16:41.972048
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTest(Taggable):
        pass
    t = TaggableTest()
    t.tags = ['t1','t2','t3','t4']
    glob_vars = { 't1':'t1.1', 't2':'t2.1' }

    # "all" in only_tags and "never" not in tags
    assert t.evaluate_tags(['all'], [], glob_vars) == True
    # "always" in tags
    assert t.evaluate_tags(['always'], [], glob_vars) == True
    # tags.isdisjoint(only_tags) == False
    assert t.evaluate_tags(['t1','t2'], [], glob_vars) == True
    # "tagged" in only_tags and tags != self.unt

# Generated at 2022-06-13 09:17:06.892404
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.block import Block

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])

# Generated at 2022-06-13 09:17:19.943514
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import argparse
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    options = argparse.Namespace(inventory=['./tests/inventory'],check=False,listtags=False,listtasks=False,listhosts=False,syntax=False,module_path=None,private_key_file=None,forks=5,timeout=10,remote_user=None,ask_pass=False,extra_vars=[],tags=['all'],skip_tags=[])

    loader = DataLoader()


# Generated at 2022-06-13 09:17:30.157980
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t._tags = ['tagged']
    assert t.evaluate_tags(only_tags=['tagged'], skip_tags=['all'], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['tagged'], skip_tags=['never'], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['tagged'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['all'], skip_tags=['never'], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['all'], skip_tags=['all'], all_vars={}) == False

# Generated at 2022-06-13 09:17:40.067544
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.playbook.helpers import load_list_of_tasks
    from ansible.playbook.task_include import TaskInclude

    task = TaskInclude()
    task._loader = get_all_plugin_loaders()[0]
    task.tags = None
    task.vars = dict()
    
    only_tags = None
    skip_tags = None
    vars = dict()
    should_run = task.evaluate_tags(only_tags, skip_tags, vars)
    assert should_run
    
    only_tags = ['all']
    skip_tags = None
    vars = dict()
    should_run = task.evaluate_tags(only_tags, skip_tags, vars)
    assert should

# Generated at 2022-06-13 09:17:51.342528
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    print("\nTest method evaluate_tags of class Taggable")
    print("=============================================\n")

    import ansible.playbook
    # How to simulate the loader object?
    loader = ansible.playbook.play_context.Loader()
    # How to simulate the variable object?
    all_variables = {'var_name': 'var_value'}

    # How to simulate an untagged object (noplaybook)?
    tags = []
    # Playbook
    playbook = ansible.playbook.Playbook()
    playbook.set_loader(loader)
    playbook.set_variable_manager(ansible.playbook.VariableManager(loader=loader, inventory=None))
    # How to simulate ansible.playbook.attribute.FieldAttribute() (noplaybook)?
    tags = ansible.playbook.attribute

# Generated at 2022-06-13 09:18:05.966238
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeTaggable(Taggable):
        pass

    # For both of these cases, nothing is skipped by tags
    assert FakeTaggable().evaluate_tags([], [], {}) == True
    assert FakeTaggable().evaluate_tags(['untagged'], [], {}) == True

    # Now we'll tag something with 'tag'
    assert FakeTaggable(tags=['tag']).evaluate_tags(['tag'], [], {}) == True
    assert FakeTaggable(tags=['tag']).evaluate_tags([], ['tag'], {}) == False

    # With 'never' we'll ignore all tags
    assert FakeTaggable(tags=['tag']).evaluate_tags(['tag'], ['never'], {}) == False

# Generated at 2022-06-13 09:18:17.222544
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    t = Task()
    t.tags = ['a', 'b']
    t.evaluate_tags(['a'], ['b'], {'a': 'a'})
    assert t.evaluate_tags(['a'], ['b'], {'a': 'a'}) is True
    assert t.evaluate_tags(['a'], ['c'], {'a': 'a'}) is True
    assert t.evaluate_tags(['d'], ['c'], {'a': 'a'}) is False
    assert t.evaluate_tags(['d'], ['b'], {'a': 'a'}) is False
    assert t.evaluate_tags(['d'], ['a'], {'a': 'a'}) is False

# Generated at 2022-06-13 09:18:23.352151
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):
        pass

    taggable = MockTaggable()
    taggable.tags = ['foo','bar','baz','never']
    assert taggable.evaluate_tags(['all'],['never'],{}) is True, 'foo'
    assert taggable.evaluate_tags(['foo'],['never'],{}) is True, 'bar'
    assert taggable.evaluate_tags(['bar'],['never'],{}) is True, 'baz'
    assert taggable.evaluate_tags(['baz'],['never'],{}) is True, 'never'
    assert taggable.evaluate_tags(['foo','baz'],['never'],{}) is True, 'foo and baz'

# Generated at 2022-06-13 09:18:32.568479
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.plugins import task_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    task = Task()
    task._attributes = dict()
    task.action = 'test'
    task.only_tags = None
    task.tags = ['test']
    task.task_loader = task_loader
    test_name = "test_evaluate_tags"

    # Test evaluation of tags when there is no 'only_tags' or 'skip_tags'
    if not task.evaluate_tags(only_tags=task.only_tags, skip_tags=task.skip_tags):
        raise AssertionError(test_name + "(1) failed")

    # Test evaluation of tags when 'only_tags' is not a

# Generated at 2022-06-13 09:18:44.502103
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''Test for Taggable class'''
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 09:19:24.650705
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        task1 = {'tags': ['foo', 'bar']}
        task2 = {'tags': ['foo', 'baz']}
        task3 = {'tags': ['bar']}
        task4 = {'tags': ['foo', 'tagged']}
        task5 = {'tags': ['foo', 'always']}
        task6 = {'tags': ['bar', 'never']}
        task7 = {'tags': ['foo']}


# Generated at 2022-06-13 09:19:28.653551
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyClass(Taggable):
        tags = []
    c = MyClass()
    assert c.evaluate_tags(['tag1', 'tag2'], [], {}) == True

if __name__ == '__main__':
    test_Taggable_evaluate_tags()

# Generated at 2022-06-13 09:19:40.531588
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.task import Task
    test_task = Task()

    test_task.tags = []
    assert test_task.evaluate_tags(None, None, []) == True
    assert test_task.evaluate_tags([], None, []) == True
    assert test_task.evaluate_tags(None, [], []) == True
    assert test_task.evaluate_tags([], [], []) == True

    test_task.tags = ['untagged']
    assert test_task.evaluate_tags(None, None, []) == True
    assert test_task.evaluate_tags([], None, []) == True
    assert test_task.evaluate_tags(None, [], []) == True
    assert test_task.evaluate_tags([], [], []) == True


# Generated at 2022-06-13 09:19:47.882180
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Tests with tag 'never'
    # Tests with always=True, all=False and 'never' in skip_tags
    # If a task contains the tag 'never', that task should not be executed
    # except if always is in the only_tags
    taggable = Taggable()
    taggable.tags = ['never']

    only_tags = []
    skip_tags = ['never']
    all_vars = dict()
    res = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert(res is False)

    only_tags = ['always']
    skip_tags = []
    all_vars = dict()
    res = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert(res is True)

    only_

# Generated at 2022-06-13 09:19:56.906111
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_host_variable('host1','host1_var','host1')
    variable_manager.set_host_variable('host1','host1_list',['host1_list_1','host1_list_2'])
    variable_manager.set_host_variable('host1','host1_dict',{'host1_dict_1':'host1_dict_1','host1_dict_2':'host1_dict_2'})
    variable_manager.set_host_variable('host1','host1_var2','host1_2')

# Generated at 2022-06-13 09:20:06.345535
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
  
    class foo(Taggable):
        pass

    assert foo().evaluate_tags(None, None, None) == True
    assert foo().evaluate_tags([], [], None) == True
    assert foo().evaluate_tags(['a'], [], None) == False
    assert foo().evaluate_tags(['a'], [], None) == False
    assert foo().evaluate_tags(['a'], ['a'], None) == False
    assert foo().evaluate_tags([], ['a'], None) == True
    assert foo().evaluate_tags(['b'], ['a'], None) == True
    assert foo().evaluate_tags([], ['all'], None) == False
    assert foo().evaluate_tags([], ['all', 'a'], None) == False

# Generated at 2022-06-13 09:20:12.022535
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import collections

    class DeepChainMap(collections.ChainMap):
        ''' Recursive version of collections.ChainMap '''
        def __getitem__(self, key):
            try:
                return super(DeepChainMap, self).__getitem__(key)
            except KeyError:
                try:
                    return self.__getitem__(list(self.keys())[0])[key]
                except (KeyError, IndexError):
                    raise KeyError(key)

    class TaggableImpl(Taggable):
        _tags = FieldAttribute(isa='list', default=['all', 'tagged'], listof=string_types)

        def __init__(self, only_tags=[], skip_tags=[], all_vars={}):
            self.all_vars = all_vars
            self.only

# Generated at 2022-06-13 09:20:22.738654
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Tests for evaluate_tags method from Taggable class

    # Case : only_tags, skip_tags and self.tags are None
    # Expected : should_run = True
    taggable = Taggable()
    only_tags = None
    skip_tags = None
    assert taggable.evaluate_tags(only_tags, skip_tags, None)

    # Case : only_tags = set(['all']) and skip_tags = set(['never'])
    # and self.tags = None or empty set
    # Expected : should_run = True
    taggable = Taggable()
    only_tags = set(['all'])
    skip_tags = set(['never'])
    taggable.tags = None

# Generated at 2022-06-13 09:20:35.713584
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    class MyTask(Base):
        _task_fields = dict(
            tags = dict(aliases=['tags'], default=[], type='list', listof=string_types),
            always_run = dict(default=False, type='bool'),
        )
        __slots__ = MyTask._task_fields.keys()

    task = MyTask()
    task.tags = ['tag1', 'tag2', 'tag3']

    # Check for default behavior
    assert task.evaluate_tags(None, None, None)

    # Check for all tags
    assert task.evaluate_tags(['all'], None, None)
   

# Generated at 2022-06-13 09:20:49.742888
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTaggable(Taggable):

        def __init__(self, name, tags):
            self.name = name
            self.tags = tags

    all_vars = {}
    tagged_task = MockTaggable('tagged_task', ['tagged', 'a_tag'])
    untagged_task = MockTaggable('untagged_task', [])
    never_task = MockTaggable('never_task', ['never'])
    always_task = MockTaggable('always_task', ['always'])

    for t in (tagged_task, untagged_task, never_task, always_task):
        assert t.evaluate_tags(None, None, all_vars)

    for t in (tagged_task, untagged_task, never_task, always_task):
        assert t

# Generated at 2022-06-13 09:21:56.432505
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host

    context = PlayContext()
    templar = Templar(loader=None)
    host = Host(name='hostname')
    group = Group(name='groupname')
    host.groups.append(group)
    group.hosts.append(host)
    context._hostvars = templar.set_available_variables({'hostvars': dict()})
    context._hostvars['hostname'] = dict()
    task = Task()
    task.tags = ['tag1']

# Generated at 2022-06-13 09:22:05.664229
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    from io import StringIO
    from collections import namedtuple
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources='')

    # Create a host to work with
    test_host = Host(name="fake_host")
    test_host.vars = dict()
    fake_inventory.add_host(test_host)

    # Create a group to work with
    test_group = Group(name='fake_group')
   

# Generated at 2022-06-13 09:22:16.157732
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    import mock # TODO: use staticmock
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.unittest import TestLoader, TextTestRunner

    def MockConstructor(data=None, block=None, role=None, task_include=None, use_handlers=None,
            defaults=None, vars=None, post_validate_converge=None):
        task = TaskInclude()
        task._attributes.update(data)
        return task

    class TestTaggable(unittest.TestCase):
        def setUp(self):
            self.task = TaskInclude()
            self.task._validate_tags = mock.mock_open()


# Generated at 2022-06-13 09:22:27.579174
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):
        pass

    # Empty tags
    t = MockTaggable()
    t.tags = []
    assert t.evaluate_tags(None, None, None) == True

    # Untagged item
    t = MockTaggable()
    t.tags = t.untagged
    assert t.evaluate_tags(None, None, None) == True

    # Tagged item
    t = MockTaggable()
    t.tags = ['flavor:chocolate']
    assert t.evaluate_tags(None, None, None) == True

    # Item with only_tags
    t = MockTaggable()
    t.tags = ['flavor:chocolate']
    assert t.evaluate_tags(['flavor:vanilla'], None, None) == False
    assert t.evaluate_

# Generated at 2022-06-13 09:22:36.272571
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = ['sometag']

    # Test only_tags
    only_tags = ['sometag']
    skip_tags = []
    all_vars = {}

    assert t.evaluate_tags(only_tags, skip_tags, all_vars)

    only_tags = ['sometag', 'tagged']
    assert t.evaluate_tags(only_tags, skip_tags, all_vars)

    only_tags = ['othertag']
    assert not t.evaluate_tags(only_tags, skip_tags, all_vars)

    only_tags = ['othertag', 'tagged']
    assert not t.evaluate_tags(only_tags, skip_tags, all_vars)

    only_tags = ['othertag', 'all']

# Generated at 2022-06-13 09:22:42.020549
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Initialize class Taggable
    class TaggableImplementation(Taggable):
        def __init__(self):
            self.tags = []
            self._loader = None

    # Run test from issue #9372
    t = TaggableImplementation()
    t.tags = ['a', 'b', 'c']
    assert t.evaluate_tags(only_tags=['a'], skip_tags=[], all_vars={})
    assert not t.evaluate_tags(only_tags=['d'], skip_tags=[], all_vars={})
    assert t.evaluate_tags(only_tags=['a', 'd'], skip_tags=[], all_vars={})

# Generated at 2022-06-13 09:22:51.414690
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTestable(Taggable):
        def __init__(self, tags, loader=None):
            self.tags = tags
            self._loader = loader
    # basic test to make sure tags are handled correctly
    mytask = TaggableTestable(['tag1', 'tag2'])
    assert mytask.evaluate_tags(['tag1'], [], {}) == True
    assert mytask.evaluate_tags(['tag2'], [], {}) == True
    assert mytask.evaluate_tags(['tag3'], [], {}) == False
    assert mytask.evaluate_tags([], ['tag2'], {}) == False
    assert mytask.evaluate_tags([], ['tag3'], {}) == True

# Generated at 2022-06-13 09:22:59.346802
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert True == Taggable().evaluate_tags(only_tags=[], skip_tags=[])
    assert True == Taggable().evaluate_tags(only_tags=['a'], skip_tags=[])
    assert True == Taggable().evaluate_tags(only_tags=[], skip_tags=['a'])
    assert False == Taggable().evaluate_tags(only_tags=['a'], skip_tags=['a'])
    assert True == Taggable().evaluate_tags(only_tags=[], skip_tags=['b'])
    assert False == Taggable().evaluate_tags(only_tags=['a'], skip_tags=['b'])
    # 'always' in tags means Taggable().evaluate_tags(only_tags=['all']) should return True

# Generated at 2022-06-13 09:23:09.788447
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    import os

    loader = dict(
        path=os.getcwd()
    )

    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    play_context.remote_user = "root"
