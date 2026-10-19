

# Generated at 2022-06-13 09:13:20.785322
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):
        pass

    my_taggable = MyTaggable()
    my_taggable.tags = ['some_tag', 'other_tag']

    assert my_taggable.evaluate_tags(only_tags=set(), skip_tags=set()) == True
    assert my_taggable.evaluate_tags(only_tags=set(['other_tag']), skip_tags=set()) == True
    assert my_taggable.evaluate_tags(only_tags=set(['other_tag']), skip_tags=set(['some_tag'])) == True
    assert my_taggable.evaluate_tags(only_tags=set(['other_tag']), skip_tags=set(['some_tag'])) == True

# Generated at 2022-06-13 09:13:27.599470
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    class TestTaggable(Taggable):
        def __init__(self, tags=None):
            super(TestTaggable, self).__init__()
            self.tags = tags

    def make_tags(l):
        return TestTaggable(tags=l)

    def make_vars(v):
        return dict(include_tasks=make_tags(v))

    def make_setup_vars(v):
        return dict(include_tasks=make_tags(v), _task_fields=['tags'], _include_tasks_setup=True)

    #  _      _     _      _     _      _     _      _     _      _     _      _     _      _     _      _     _      _     _      _
    # | |    (_)   | |

# Generated at 2022-06-13 09:13:37.744910
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    class MockTaggable(Taggable):
        # Mocked tags
        tags = ['always', 'a']
    b = MockTaggable()
    # Only tags
    assert b.evaluate_tags(only_tags=set(['a']), skip_tags=None, all_vars={})
    assert b.evaluate_tags(only_tags=set(['always']), skip_tags=None, all_vars={})
    assert not b.evaluate_tags(only_tags=set(['foo']), skip_tags=None, all_vars={})
    assert b.evaluate_tags(only_tags=set(['all']), skip_tags=None, all_vars={})

# Generated at 2022-06-13 09:13:50.377998
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class A(Taggable):
        def __init__(self):
            self.tags = ['foo']
        def _loader(self): pass
    a = A()
    assert a.evaluate_tags(None, None, {}) == True
    assert a.evaluate_tags(set(['foo']), None, {}) == True
    assert a.evaluate_tags(set(['foo', 'bar']), None, {}) == True
    assert a.evaluate_tags(set(['bar']), None, {}) == False
    assert a.evaluate_tags(set(['foo']), set(['bar']), {}) == True
    assert a.evaluate_tags(set(['bar']), set(['foo']), {}) == False

# Generated at 2022-06-13 09:14:01.739042
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    This method is not called by the regular execution workflow,
    but is used by the unit tests.
    '''

    # Create an instance of Taggable
    class TaggableItem(Taggable):
        def __init__(self):
            self.tags = None

    item = TaggableItem()

    # test #1: no tags
    only_tags = set()
    skip_tags = set()
    item.tags = None
    assert item.evaluate_tags(only_tags, skip_tags) == True

    # test #2: tagged and only_tags
    only_tags = set(['tagged'])
    skip_tags = set()
    item.tags = ['tagged']
    assert item.evaluate_tags(only_tags, skip_tags) == True

    # test #3: tagged and

# Generated at 2022-06-13 09:14:10.249984
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

    taggable = DummyTaggable(tags=['server1'])
    only_tags = set(['server1'])
    skip_tags = set(['server2'])
    all_vars = {}
    assert taggable.evaluate_tags(only_tags=only_tags,
                                  skip_tags=skip_tags,
                                  all_vars=all_vars)
    only_tags = set(['server1', 'server2'])
    assert taggable.evaluate_tags(only_tags=only_tags,
                                  skip_tags=skip_tags,
                                  all_vars=all_vars)
    only_tags = set(['server2'])

# Generated at 2022-06-13 09:14:19.408784
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    t=Taggable()
    t.tags=['always']
    assert t.evaluate_tags(['tagged'], ['tagged'], None) == True

    t=Taggable()
    t.tags=['never']
    assert t.evaluate_tags(['tagged'], ['tagged'], None) == False

    t=Taggable()
    t.tags=['untagged']
    assert t.evaluate_tags(['tagged'], ['tagged'], None) == True

    t=Taggable()
    t.tags=[]
    assert t.evaluate_tags(['tagged'], ['tagged'], None) == True

    t=Taggable()
    t.tags=['test1']
    assert t.evaluate_tags(['test2'], ['test2'], None) == False

# Generated at 2022-06-13 09:14:31.931422
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.role import Role
    from ansible.playbook.taggable import RoleDefinition
    from ansible.vars.manager import VariableManager

    role = Role()
    role._role_name = 'untagged'

    role_def = RoleDefinition()
    role_def._role_name = 'untagged'

    variable_manager = VariableManager()
    variable_manager.root_vars = template.Vars(loader=None)
    variable_manager.extra_vars = { 'foo': 'bar' }

    assert role.evaluate_tags([], [], variable_manager)
    assert role.evaluate_tags(['untagged'], [], variable_manager)
    assert role.evaluate_tags([], ['untagged'], variable_manager)


# Generated at 2022-06-13 09:14:34.031943
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass

try:
    from ansible.tests import helpers as testutils
    testutils.run_unit(__name__, needs_daemon=False)
except ImportError:
    pass

# Generated at 2022-06-13 09:14:39.144227
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    t = Taggable()

    # Check if function will run if skip_tags is empty
    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) is True

    # Check if function will not run on skip_tags
    assert t.evaluate_tags(only_tags=[], skip_tags=['noway'], all_vars={}) is False

    # Check if function will not run on skip_tags
    assert t.evaluate_tags(only_tags=[], skip_tags=['all'], all_vars={}) is False

# Generated at 2022-06-13 09:14:55.022082
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    tags = ['a', 'b', 'c', 'always']
    only_tags = ['a', 'b', 'never', 'tagged']
    skip_tags = ['c', 'always', 'tagged']
    only_tagsTrue = ['all']
    skip_tagsTrue = ['never']
    obj = Taggable()
    all_vars = {}
    obj.tags = tags

    obj.evaluate_tags(only_tags, skip_tags, all_vars)
    obj.evaluate_tags(only_tagsTrue, skip_tags, all_vars)
    obj.evaluate_tags(only_tags, skip_tagsTrue, all_vars)
    obj.evaluate_tags(only_tagsTrue, skip_tagsTrue, all_vars)

    # Should raise AssertionError since the input for tags is incorrect
   

# Generated at 2022-06-13 09:15:07.379743
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # This should NOT raise an error, but should return True
    t = Taggable()
    t.tags = ['not_all', 'not_tagged', 'never']
    assert t.evaluate_tags(['all', 'never'], ['never'], {}) == True

    # This should NOT raise an error, but should return False
    t = Taggable()
    t.tags = ['not_all', 'not_tagged', 'never']
    assert t.evaluate_tags(['all', 'never'], ['never'], {}) == True

    # This should NOT raise an error, but should return False
    t = Taggable()
    t.tags = ['not_all', 'not_tagged', 'never']
    assert t.evaluate_tags(['all', 'never'], ['always'], {}) == False

   

# Generated at 2022-06-13 09:15:19.132792
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # case 1: pass the test
    tag_obj = Taggable()
    tag_obj.tags = [ 'debug','a','b','c' ]
    print("case 1: pass the test")
    print("tags = %s" % (tag_obj.tags))
    only_tags = ['aa','bb','cc']
    skip_tags = ['aa','cc','f']
    all_vars = { 'a': {'val':{'b':'aa'}} }
    print("only_tags = %s; skip_tags = %s" % (only_tags, skip_tags))
    print("ans = %s" % (tag_obj.evaluate_tags(only_tags, skip_tags, all_vars)))

    # case 2: fail the test
    tag_obj = Taggable()
    tag_obj

# Generated at 2022-06-13 09:15:29.490461
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    only_tags = ['a', 'b', 'c', 'd']
    skip_tags = ["f", "never"]

    # Test for the case when there are only tags given
    task_only = Task()
    task_only.tags = only_tags
    play_context_only = PlayContext()
    task_only._play_context = play_context_only
    assert task_only.evaluate_tags(only_tags, None, {})

    task_only = Task()
    task_only.tags = ["never"]
    play_context_only = PlayContext()
    task_only._play_context = play_context_only
    assert not task_only.evaluate_tags(only_tags, None, {})



# Generated at 2022-06-13 09:15:39.279978
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
  '''
  This is a unit test for Taggable class's method evaluate_tags
  '''
  mock_only_tags = ['test_tag','test_tag2','always']
  mock_skip_tags = ['skip_tag','skip_tag2']
  mock_all_vars = {'playbook_dir': '', 'play_hosts': [], 'inventory_hostname': '', 'ansible_ssh_pass': False, 'inventory_hostname_short': '', 'ansible_ssh_password': False, 'groups': {'all': ['localhost'], 'ungrouped': ['localhost']}, 'ansible_check_mode': False, 'inventory_file': '', 'ansible_playbook_python': '/usr/bin/python'}
  mock_tags = ['test_tag','test_tag2']
  mock

# Generated at 2022-06-13 09:15:47.629978
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeClass(Taggable):
        pass

    import sys
    import pytest
    from ansible.plugins.loader import become_loader, connection_loader, action_loader, cache_loader, callback_loader, credentials_loader, lookup_loader, vars_loader, filter_loader, test_loader, terminal_loader, strategy_loader

    loader_list = [become_loader, connection_loader, action_loader, cache_loader, callback_loader, credentials_loader, lookup_loader, vars_loader, filter_loader, test_loader, terminal_loader, strategy_loader]

    class FakeLoader(object):
        def __init__(self):
            self.all_vars = dict()


# Generated at 2022-06-13 09:15:58.192520
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockUnicode(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other

    class MockUnicodeList(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other

    class MockModule(object):
        __module__ = None
        _result = Taggable()

        @property
        def result(self):
            return self._result

        @result.setter
        def result(self, value):
            self._result = value

        def set_play_context(self, play_context):
            self.play_context = play_context


# Generated at 2022-06-13 09:16:07.738230
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    item = Taggable()
    item.tags = ['test']
    assert item.evaluate_tags(set(['']), set(['']), dict())
    assert item.evaluate_tags(set(['test']), set(['']), dict())
    assert item.evaluate_tags(set(['test']), set(['test']), dict()) == False
    assert item.evaluate_tags(set(['test']), set(['notest']), dict())
    assert item.evaluate_tags(set(['notest']), set(['notest']), dict()) == False
    assert item.evaluate_tags(set(['tagged']), set(['untagged']), dict())
    assert item.evaluate_tags(set(['untagged']), set(['untagged']), dict()) == False

# Generated at 2022-06-13 09:16:16.027762
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = [
        'tag1',
        'tagged'
    ]
    assert(t.evaluate_tags(['tag1'], [], {}))
    assert(t.evaluate_tags(['tagged'], [], {}))
    assert(not t.evaluate_tags([], ['tag1'], {}))
    assert(not t.evaluate_tags([], ['tagged'], {}))
    assert(not t.evaluate_tags(['tag2'], [], {}))
    assert(not t.evaluate_tags(['tag2'], ['tag1'], {}))
    assert(not t.evaluate_tags(['tag2'], ['tagged'], {}))
    assert(t.evaluate_tags([], [], {}))

# Generated at 2022-06-13 09:16:17.283280
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert True  # TODO

# Generated at 2022-06-13 09:16:43.659662
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import json

    class MyTaggable(Taggable):
        pass

    my_taggable = MyTaggable()

    # default value test
    assert my_taggable.evaluate_tags([], [], dict())

    # only_tags == [all] test
    assert my_taggable.evaluate_tags(['all'], [], dict())

    # only_tags == [all] and skip_tags == [never] test
    assert not my_taggable.evaluate_tags(['all'], ['never'], dict())

    # only_tags == [all] and skip_tags == [] test
    assert my_taggable.evaluate_tags(['all'], [], dict())

    # only_tags == [all] and skip_tags == ['all'] test
    assert not my_taggable.evaluate_

# Generated at 2022-06-13 09:16:55.200315
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakePlaybook:
        class FakeVars:
            pass

        class FakeTask:
            class FakeLoader:
                pass

    fake_playbook = FakePlaybook()
    fake_task = FakePlaybook.FakeTask()
    fake_task._loader = FakePlaybook.FakeTask.FakeLoader()
    fake_task.tags = ["foo", "bar", "baz"]
    fake_task.evaluate_tags(only_tags=["foo"], skip_tags=[], all_vars=FakePlaybook.FakeVars())


if __name__ == '__main__':
    test_Taggable_evaluate_tags()

# Generated at 2022-06-13 09:16:57.037822
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # TODO: expand unit test for Taggable.evaluate_tags
    pass

# Generated at 2022-06-13 09:17:08.785872
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # given
    class MockTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

        def __getattribute__(self, name):
            if name == 'tags':
                return object.__getattribute__(self, name)
            else:
                return None

    # when
    taggable = MockTaggable([])
    assert taggable.evaluate_tags(['untagged'], ['never', 'never-run'], {'tags': []}) == True

    taggable = MockTaggable(['untagged'])
    assert taggable.evaluate_tags(['untagged'], ['never', 'never-run'], {'tags': []}) == True

    taggable = MockTaggable([])

# Generated at 2022-06-13 09:17:20.678375
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockRunner:
        def __init__(self):
            self.tags = ['all']

    class MockHost:
        def __init__(self):
            self.name = "test_host"
            self.runner = MockRunner()
            self.task_vars = dict() # tests don't care about vars
            self.included_file = None
            self.blocks = []
            self.rescue = []
            self.always = []
            self.conditional = []
            self.roles = []

    class MockTask(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = ['untagged']

    host = MockHost()
    task = MockTask()
    only_tags = frozenset()
    skip_tags = frozenset()
    all_

# Generated at 2022-06-13 09:17:30.650105
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from collections import namedtuple
    from ansible.vars import VariableManager

    host_vars = dict()
    variable_manager = VariableManager()
    variable_manager.set_inventory(host_vars)

    block = Block()
    block._loader = variable_manager

    class Host:
        def get_vars(self):
            return dict()

    host = Host()
    block.tags = dict()
    block.tags = list()

    # default, tasks to run
    assert block.evaluate_tags(['role'], None, host.get_vars())

    # Check for tags that we need to skip
    block.tags = ['all', 'never']
    assert not block.evaluate_tags(['role'], ['all'], host.get_vars())


# Generated at 2022-06-13 09:17:40.224718
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyTask(Taggable):
        def __init__(self, name, tags):
            self.name = name
            self.tags = tags

    # Should run
    t1 = DummyTask("Should run 1", ['a', 'b'])
    assert t1.evaluate_tags(['a', 'b', 'c'], [], {}) is True

    # Should NOT run
    t2 = DummyTask("Should NOT run 1", ['c', 'd'])
    assert t2.evaluate_tags(['a', 'b'], [], {}) is False

    # Should run
    t3 = DummyTask("Should run 2", ['c', 'd'])
    assert t3.evaluate_tags(['a', 'b'], ['c'], {}) is True

    # Should NOT run

# Generated at 2022-06-13 09:17:44.625663
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task
    from units.mock.loader import DictDataLoader
    from units.compat.unittest import TestCase

    class VariableManager(object):
        def get_vars(self, play=None, host=None, task=None):
            return dict(foo="bar")

    class TaskModule(Task):
        _task_type = "Test"

        def __init__(self):
            super(TaskModule, self).__init__(
                is_meta_task=False,
                load_path=None,
                loader=DictDataLoader(),
                variable_manager=VariableManager(),
            )

    t = TaskModule()

    # basic test case
    t.tags = ["foo", "bar"]

# Generated at 2022-06-13 09:17:49.347907
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    obj.tags = ['all', 'test']
    tags = obj.tags
    only_tags = ['test']
    skip_tags = []
    all_vars = []
    test = obj.evaluate_tags(only_tags, skip_tags, all_vars)
    assert test == True


# Generated at 2022-06-13 09:17:56.347144
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    taggable = Taggable()
    taggable.tags = ['a', 'b', 'never', 'c']
    assert taggable.evaluate_tags(only_tags=['c'], skip_tags=[], all_vars=dict()) == True

    taggable.tags = ['never', 'c']
    assert taggable.evaluate_tags(only_tags=['a'], skip_tags=[], all_vars=dict()) == False

    taggable.tags = ['never', 'c']
    assert taggable.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars=dict()) == True

    taggable.tags = ['never', 'c']

# Generated at 2022-06-13 09:18:27.856968
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:18:35.242327
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    myplay = Play().load({'name': 'test_play',
                          'hosts': 'dummy',
                          'tasks': [{'action': {'module': 'test', 'tags': [ 'tagged' ]}},
                                    {'action': {'module': 'test', 'tags': [ 'always' ]}},
                                    {'action': {'module': 'test', 'tags': [ 'never' ]}},
                                    {'action': {'module': 'test', 'tags': [ 'undefined' ]}}
                                   ]})
    assert len(myplay.tasks) == 4
    myplay.post_validate(templar=None)



# Generated at 2022-06-13 09:18:46.578080
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play
    import ansible.playbook.play as play
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    dataloader = DataLoader()
    variable_manager = VariableManager()
    loader = dataloader
    play_context = PlayContext()
    block = Block()
    play_source = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [dict(action=dict(module='setup', args=''))]
    )

# Generated at 2022-06-13 09:18:57.570309
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    taggable_object = Taggable()
    host = '127.0.0.1'

    vm = VariableManager()
    play = Play().load({}, variable_manager=vm, loader=None)

    playcontext = play.set_context()

    task = Task()
    task._role = None
    task._play = play
    task._loader = None

    # check the evaluate_tags method result
    # case 1: only_tags set, tags set, skip_tags not set
    assert taggable_object.evaluate_tags(only_tags=['first', 'second'], skip_tags=None, all_vars=None) == False

    # case 2:

# Generated at 2022-06-13 09:19:04.355026
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Case 1:
    # Construct a Taggable and call evaluate_tags
    # Expect to have a return value
    task = Taggable()
    task._loader = None
    result = task.evaluate_tags(['tag1', 'tag2'], ['tag3'], {})

    # Case 2:
    # Uncomment line below and expect to get an error
    #task = Taggable()
    #result = task.evaluate_tags(['tag1', 'tag2'], ['tag3'], {})

    assert result == True  # Case 1
    assert result != None  # Case 2

# Generated at 2022-06-13 09:19:15.075456
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    
    class Task(Taggable):
        pass

    testtags = ['tag_one', 'tag_two']

    t1 = Task()
    assert t1.evaluate_tags(only_tags=set(testtags), skip_tags=set(['tag_three']), all_vars={}) is False

    t2 = Task()
    t2.tags = ['tag_one']
    assert t2.evaluate_tags(only_tags=set(testtags), skip_tags=set(['tag_three']), all_vars={}) is True

    t3 = Task()
    t3.tags = ['tag_three']
    assert t3.evaluate_tags(only_tags=set(testtags), skip_tags=set(['tag_three']), all_vars={}) is False

    t4 = Task()
   

# Generated at 2022-06-13 09:19:27.924831
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class fake_Taggable(Taggable):
        def __init__(self):
            self.tags = []

    # Create fake_Taggable object
    t = fake_Taggable()

    # Create fake_vars for the templar
    all_vars = dict()

    # By default the tags attribute should be an empty list
    assert len(t.tags) == 0

    # should_run should be true if only_tags and skip_tags are empty
    should_run = t.evaluate_tags(only_tags=[], skip_tags=[], all_vars=all_vars)
    assert should_run is True

    # should_run should be true if only_tags and skip_tags are None

# Generated at 2022-06-13 09:19:39.864514
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    task = Task()

    # Start testing with only_tags
    assert task.evaluate_tags(['all'], ['all'], {}) == True
    assert task.evaluate_tags(['all'], [], {}) == True
    assert task.evaluate_tags(['all'], ['never'], {}) == True
    assert task.evaluate_tags(['all'], ['test'], {}) == True
    assert task.evaluate_tags(['all'], ['tagged'], {}) == True

    play = Play()

# Generated at 2022-06-13 09:19:47.474716
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import sys

    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    # Setup and run

# Generated at 2022-06-13 09:19:56.728771
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class test_Taggable(Taggable):
        def __init__(self):
            self.tags = None

    tt = test_Taggable()
    print("Test case1: only_tags=[], skip_tags=[], tags=[], should_run=True")
    assert tt.evaluate_tags([], [], [])

    print("Test case2: only_tags=[], skip_tags=[], tags=[1,2], should_run=True")
    assert tt.evaluate_tags([], [], ['1', '2'])

    print("Test case3: only_tags=[], skip_tags=[], tags=[never], should_run=False")
    assert not tt.evaluate_tags([], [], ['never'])


# Generated at 2022-06-13 09:21:03.017864
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    task = Task()
    play = Play()
    play.hosts = ['test_host']
    play.tasks = [task]
    task.tags = ['tagged']

    # Test whether task should run
    assert task.evaluate_tags(set(['tagged']), set(['never']), dict()) == True
    assert task.evaluate_tags(set(['tagged']), set(['never']), dict()) == True
    assert task.evaluate_tags(set(['tagged']), set(['never']), dict()) == True
    assert task.evaluate_tags(set(['always']), set(['never']), dict()) == True

# Generated at 2022-06-13 09:21:08.385370
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # unit test to ensure excluded tags work as expected
    # mock a Taggable object with tags and tags_skip attributes
    tags = ['tag1','tag2']
    tags_skip = ['tag2']
    obj = {}
    result = Taggable.evaluate_tags(obj, tags, tags_skip, None)
    # test assertion
    assert result == True


# Generated at 2022-06-13 09:21:15.815371
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):
        def __init__(self):
            self._tags = []

    mock_taggable = MockTaggable()
    mock_taggable._tags = ["no-linux"]
    assert mock_taggable.evaluate_tags(["all", "never"], ["linux"], {}) == False
    assert mock_taggable.evaluate_tags(["all", "never"], ["no-linux"], {}) == True
    assert mock_taggable.evaluate_tags(["all", "never"], [], {}) == False

    mock_taggable._tags = ["linux"]
    assert mock_taggable.evaluate_tags(["all", "never"], ["linux"], {}) == False
    assert mock_taggable.evaluate_tags(["all", "never"], ["no-linux"], {})

# Generated at 2022-06-13 09:21:27.458063
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    v = {'foo': 'bar'}
    assert t.evaluate_tags(None, None, None)
    assert not t.evaluate_tags(None, None, v)
    assert t.evaluate_tags('all', None, v)
    assert t.evaluate_tags('tagged', None, v)
    assert t.evaluate_tags('tagged,bar', None, v)
    assert t.evaluate_tags('tagged,baz', None, v)
    assert not t.evaluate_tags('tagged,nope', None, v)
    assert not t.evaluate_tags('bar', None, v)
    assert not t.evaluate_tags('bar', 'baz', v)
    assert t.evaluate_tags('bar', 'nope', v)

# Generated at 2022-06-13 09:21:41.453769
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyUnit(Taggable):
        _name = FieldAttribute(isa='string', default=None)

        def __init__(self, name, tags=[]):
            self._name = name
            self._tags = tags

        def __repr__(self):
            return "{0}".format(self._name)

    def evaluate_tags_test(module, obj, only_tags, skip_tags, all_vars, expected_result, message):
        unit = MyUnit(module.params['name'], module.params['tags'])
        result = unit.evaluate_tags(only_tags, skip_tags, all_vars)
        if result != expected_result:
            module.fail_json(msg=message)


# Generated at 2022-06-13 09:21:49.353103
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass(Taggable):
        def __init__(self):
            self._tags = []
            self.tags = None

    class TestVars:
        def __init__(self):
            self.tags = None

    only_tags = ['tag1', 'tag2', 'tag3']
    skip_tags = ['skip1', 'skip2']

    obj = TestClass()

    obj.tags = ['tag1']
    if not obj.evaluate_tags(only_tags, skip_tags, TestVars()):
        raise Exception("Unable to evaluate tags")

    obj.tags = ['always']
    if not obj.evaluate_tags(only_tags, skip_tags, TestVars()):
        raise Exception("Unable to evaluate tags")

    obj.tags = ['tagged']

# Generated at 2022-06-13 09:21:55.575084
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()

    # Test method Taggable.evaluate_tags without any tags
    assert obj.evaluate_tags(None, None, None) is True

    # Test method Taggable.evaluate_tags with only_tags parameter:
    # 1. Test with the 'always' tag
    assert obj.evaluate_tags(['always'], None, None) is True
    # 2. Test with the 'all' tag
    assert obj.evaluate_tags(['all'], None, None) is True
    # 3. Test with the 'tagged' tag
    assert obj.evaluate_tags(['tagged'], None, None) is False

    # Test method Taggable.evaluate_tags with skip_tags parameter:
    # 1. Test with the 'always' tag
    assert obj.evaluate_tags(None, ['always'], None)

# Generated at 2022-06-13 09:22:05.184740
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """
    Tests when evaluate_tags should run(True) or not(False)
    """

# Generated at 2022-06-13 09:22:15.876515
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    playbook = ansible.playbook.Playbook.load("", "",'',loader=ansible.loader.DataLoader(), variable_manager = ansible.vars.VariableManager())
    task = ansible.playbook.Task()
    task._loader = ansible.loader.DataLoader()
    task._role = ansible.playbook.Role()
    task.name = 'test'
    task._role._role_path = '/'
    task._role.name = 'test_role'
    task._play = ansible.playbook.Play()
    task.tags = []
    only_tags = ['all']
    skip_tags = []
    all_vars = ansible.vars.VariableManager()


# Generated at 2022-06-13 09:22:27.325928
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()

    vars = dict()

    t.tags = None
    only_tags = {'all', 'never'}
    skip_tags = set()
    assert not t.evaluate_tags(only_tags, skip_tags, vars)

    t.tags = None
    only_tags = set()
    skip_tags = {'all', 'never'}
    assert t.evaluate_tags(only_tags, skip_tags, vars)

    t.tags = None
    only_tags = {'all', 'never'}
    skip_tags = {'all', 'never'}
    assert not t.evaluate_tags(only_tags, skip_tags, vars)

    t.tags = None
    only_tags = {'all'}
    skip_tags = {'never'}
