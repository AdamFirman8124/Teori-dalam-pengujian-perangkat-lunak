

# Generated at 2022-06-13 09:13:22.295548
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """Unit test for method evaluate_tags of class Taggable.
        """
    # =========================================================
    # Test if a task has the expected behavior in case of
    #     - usage of tags
    #     - special usage of the tag 'always'
    # =========================================================
    # Create a task with a list of three tags.
    test1_task = Taggable()
    test1_task.tags = ['tag1', 'tag2', 'tag3']

    # Scenario 1: Only tasks with tag1 or tag2 should run
    # => Task should not run
    assert test1_task.evaluate_tags(only_tags = ['tag1', 'tag2'], skip_tags = [], all_vars = {}) == False
    # => Task should not run

# Generated at 2022-06-13 09:13:22.830402
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass



# Generated at 2022-06-13 09:13:24.818334
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class ExampleClass(Taggable):
        pass

    e = ExampleClass()
    assert e.evaluate_tags(['all'], [], {})

# Generated at 2022-06-13 09:13:35.953076
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableFakeClass(Taggable):
        def __init__(self):
            self._tags = []

    # Setup
    test_tags = ['faketag1', 'faketag2']
    test_obj = TaggableFakeClass()
    test_obj._tags = test_tags

    # Testing
    result = test_obj.evaluate_tags(only_tags=['faketag1'], skip_tags=[], all_vars=dict())
    assert result is True

    result = test_obj.evaluate_tags(only_tags=[], skip_tags=['faketag1'], all_vars=dict())
    assert result is False


# Generated at 2022-06-13 09:13:43.495611
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    # create play
    play = Play().load({
        'name'        : "Test Play",
        'hosts'       : 'localhost',
        'gather_facts': 'no',
        'tasks'       : [],
    }, loader=None, variable_manager=None)
    play.post_validate()

    # create block

# Generated at 2022-06-13 09:13:55.520194
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableSubclass(Taggable):
        pass

    try:
        taggable = TaggableSubclass()
        taggable.tags = []
        taggable.tags.append({'all': True})

        only_tags = ['foo', 'bar']
        skip_tags = []
        all_vars = dict()
        result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
        assert result == True

    except AssertionError:
        raise AssertionError("test_Taggable_evaluate_tags() FAILED")

test_Taggable_evaluate_tags()

# Generated at 2022-06-13 09:14:06.152356
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags
    assert FakeTaggable(None).evaluate_tags([], [], None)
    assert not FakeTaggable(None).evaluate_tags(['never'], [], None)
    assert FakeTaggable(['never']).evaluate_tags(['never'], [], None)
    assert not FakeTaggable(['always']).evaluate_tags(['never'], [], None)
    assert FakeTaggable(['foo']).evaluate_tags(['never'], [], None)
    assert not FakeTaggable(['bar']).evaluate_tags([], ['never'], None)

# Generated at 2022-06-13 09:14:16.547931
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.conditional import Operand
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    only_tags = set(['foo'])
    skip_tags = set(['bar'])
    all_vars = dict()
    all_vars['foo'] = 'bar'

    test_play = Play()
    test_play.hosts = 'non-localhost'
    test_play.role = Role()
    test_task = Task()
    test_task._parent = test_play.role
    test_task.tags = ['foo']
    test_task.evaluate_tags(only_tags, skip_tags, all_vars)

    # Test for when the only_tags option is present but the
   

# Generated at 2022-06-13 09:14:25.768233
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.role.task import Task as RoleTask
    from ansible.playbook.role.handler import Handler as RoleHandler
    from ansible.playbook.play_context import PlayContext

    taggable_classes=[Task,Handler,Block,RoleTask,RoleHandler]
    class_test_passed = {}

    for taggable_class in taggable_classes:
        class_test_passed[taggable_class] = 0
        taggable_class.tags = ['tagged']
        all_vars = {}
        only_tags=['tagged']
        skip_tags=[]
       

# Generated at 2022-06-13 09:14:34.033761
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    mock_results = []

    test_obj = Taggable()
    test_obj.tags = ["second", "first"]

    test_obj.evaluate_tags(["first"], [], {})
    mock_results.append(test_obj.tags == ["second", "first"])

    test_obj.evaluate_tags(["first"], ["first"], {})
    mock_results.append(test_obj.tags == ["second", "first"])

    test_obj.evaluate_tags(["first"], ["second"], {})
    mock_results.append(test_obj.tags == ["second", "first"])

    test_obj.evaluate_tags([], ["first"], {})
    mock_results.append(test_obj.tags == ["second", "first"])

    test_obj.evaluate_tags([], ["second"], {})

# Generated at 2022-06-13 09:14:52.837231
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import json
    import mock

    class Playbook:
        pass

    class Task:
        pass

    playbook = Playbook()
    playbook.tags = ['test', 1, 2]
    playbook.all_vars = dict()
    playbook.all_vars['test'] = 'foo'

    task = Task()
    task._play = playbook
    task.tags = ['test']

    with mock.patch('ansible.template.Templar._get_type_validator', return_value=list):
        assert task.evaluate_tags(['foo'], ['foo'], dict()) is False
        assert task.evaluate_tags(['always'], ['always'], dict()) is True
        assert task.evaluate_tags(['always'], ['never'], dict()) is True

# Generated at 2022-06-13 09:15:05.302244
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert(Taggable.evaluate_tags(Taggable(tags=['tag1']), only_tags=['tag1'], skip_tags=['never'], all_vars={}))
    assert(not Taggable.evaluate_tags(Taggable(tags=['tag1']), only_tags=['tag2'], skip_tags=['never'], all_vars={}))
    assert(not Taggable.evaluate_tags(Taggable(tags=['tag1']), only_tags=['tag1'], skip_tags=['tag1'], all_vars={}))
    assert(Taggable.evaluate_tags(Taggable(tags=['tag1']), only_tags=['tag1'], skip_tags=['tag2'], all_vars={}))

# Generated at 2022-06-13 09:15:17.066006
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # testcase 1 : tests with only_tags as ['tag1','tag2'] and skip_tags as empty list
    all_vars = dict()
    only_tags = ['tag1','tag2']
    skip_tags = list()
    testcase_1_set = set(['tag1','tag2','tag3'])
    assert(Taggable().evaluate_tags(only_tags,skip_tags,all_vars) == True)
    # testcase 1.1 : tests with only_tags as ['tag1','tag2'] and skip_tags as empty list
    testcase_1_1_set = set(['tag1','tag2'])
    assert(Taggable().evaluate_tags(only_tags,skip_tags,all_vars) == True)
    # testcase 1.2 : tests with only_tags as

# Generated at 2022-06-13 09:15:26.208640
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.playbook.task import Task # noqa

    task1 = Task()
    task2 = Task()

    task1._ds = {'tags':['first']}
    task2._ds = {'tags':['second']}

    assert task1.evaluate_tags([], [], {}) == True
    assert task2.evaluate_tags([], [], {}) == True

    assert task1.evaluate_tags([], [], {'tags':['first']}) == True
    assert task2.evaluate_tags([], [], {'tags':['first']}) == True


# Generated at 2022-06-13 09:15:36.799188
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # For each test case we do the following
    # 1. Create an instance of class Taggable
    # 2. set attributes only_tags and skip_tags
    # 3. call method evaluate_tags
    # 4. compare the returned value with expected result

    # Test case 1:
    # Tagged, no skip or only tag
    # The task should be executed
    t = Taggable()
    t.tags = ['a', 'b']
    if t.evaluate_tags([], [], {}) != True:
        raise AssertionError()

    # Test case 2:
    # Tagged, skip a, but not b
    # The task should be executed
    t = Taggable()
    t.tags = ['a', 'b']
    if t.evaluate_tags([], ['a'], {}) != True:
        raise

# Generated at 2022-06-13 09:15:52.258137
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTaggable(Taggable):
        pass

    t = MockTaggable()

    # default tags value is []
    assert t.evaluate_tags(only_tags=None, skip_tags=None, all_vars={}) == True
    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True

    # all_vars does not affect tags evaluation
    assert t.evaluate_tags(only_tags=None, skip_tags=None, all_vars={ 'tags': ['something'] }) == True
    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars={ 'tags': ['something'] }) == True

    # skip_tags takes precedence over only_tags

# Generated at 2022-06-13 09:15:56.061120
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.task_include import TaskInclude
    def test(only_tags, skip_tags, tags, expected_outcome):
        task = TaskInclude()
        task.tags = tags
        assert task.evaluate_tags(only_tags, skip_tags, []) == expected_outcome
    test([], [], None, True)
    test(None, [], ['foo'], True)
    test([], None, ['foo'], True)
    test([], None, None, True)
    test(None, [], None, True)
    test(['foo'], ['foo'], ['foo'], True)
    test(['foo'], ['foo'], None, True)
    test(['foo'], ['bar'], ['foo'], False)

# Generated at 2022-06-13 09:16:06.224422
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    Options = namedtuple("Options", ['listtags', 'listtasks', 'listhosts', 'syntax',
                                     'connection','module_path', 'forks', 'remote_user',
                                     'private_key_file', 'ssh_common_args', 'ssh_extra_args',
                                     'sftp_extra_args', 'scp_extra_args', 'become', 'become_method',
                                     'become_user', 'verbosity','check', 'diff','tags','skip_tags','host_pattern','extra_vars'])

    class Play:
        def __init__(self, options):
            self.options = options

# Generated at 2022-06-13 09:16:10.583475
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Object
    TaggableObject = Taggable()
    # Values
    only_tags = ['tag1']
    skip_tags = ['tag2']
    all_vars = {}
    # Test
    assert TaggableObject.evaluate_tags(only_tags, skip_tags, all_vars) == True

# Generated at 2022-06-13 09:16:17.802139
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible import constants
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader

    class FakeDataLoader(DataLoader):
        def get_basedir(self, hostname):
            return '/fake/dir'

    class FakeRunnerOptions(object):
        def __init__(self):
            self.connection = 'ssh'
            self.module_path = None
            self.forks = constants.DEFAULT_FORKS
            self.become = False
            self.become_method = 'sudo'
            self.become_user = 'root'
            self.verbosity = False
            self.check = False

    class FakePlay(Taggable):
        def __init__(self):
            self.only_tags = None
            self.skip_tags = None
            self

# Generated at 2022-06-13 09:16:43.738088
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # default run
    test_tag_obj = MockTaggable(['test_tag'])
    result = test_tag_obj.evaluate_tags([], [], {})
    assert result

    # run with 'always'
    test_tag_obj = MockTaggable(['test_tag', 'always'])
    result = test_tag_obj.evaluate_tags([], [], {})
    assert result

    test_tag_obj = MockTaggable(['always'])
    result = test_tag_obj.evaluate_tags([], [], {})
    assert result

    # dont run with 'never'

# Generated at 2022-06-13 09:16:58.362866
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyTaggable(Taggable):
        def __init__(self):
            self._loader = None

    dt = DummyTaggable()
    only_tags = frozenset(['tag1', 'tag2'])
    skip_tags = frozenset(['tag3', 'tag4'])
    all_vars = {}

    # always
    dt.tags = ['always']
    assert(dt.evaluate_tags(only_tags, skip_tags, all_vars))
    dt.tags = ['tag1', 'always']
    assert(dt.evaluate_tags(only_tags, skip_tags, all_vars))
    dt.tags = ['tag3', 'always']
    assert(dt.evaluate_tags(only_tags, skip_tags, all_vars))

    #

# Generated at 2022-06-13 09:17:09.409737
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    only_tags = frozenset()
    skip_tags = frozenset()
    all_vars = dict()
    parent_block = Block()

    ###########
    # 1. normal tags
    ###########

    # 1.1
    tags_list = [ "tag_1", "tag_2" ]
    task = Task()
    task.tags = tags_list
    result = task.evaluate_tags( only_tags, skip_tags, all_vars )
    assert result == True
    result = task._load_tags( "tags", task.tags )
    assert result == tags_list

    # 1.2
    clear_tags_list()
    task.load_tags

# Generated at 2022-06-13 09:17:21.474529
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test 1: tagged task
    t = Taggable()
    t.tags = ['test_tag']
    only_tags = ['test_tag']
    skip_tags = []
    assert t.evaluate_tags(only_tags, skip_tags, {})

    # Test 2: tagged task and --skip-tag provided
    t = Taggable()
    t.tags = ['test_tag']
    only_tags = []
    skip_tags = ['test_tag']
    assert not t.evaluate_tags(only_tags, skip_tags, {})

    # Test 3: untagged task and --only-tag provided
    t = Taggable()
    only_tags = ['test_tag']
    skip_tags = []
    assert not t.evaluate_tags(only_tags, skip_tags, {})

    # Test

# Generated at 2022-06-13 09:17:30.927526
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableClass(Taggable):
        pass

    obj = TaggableClass()
    obj.tags = list()

    assert(obj.evaluate_tags(['a', 'b'], ['c', 'd'], dict()) == True)
    assert(obj.evaluate_tags(['a', 'b'], ['c', 'd', 'always'], dict()) == True)
    assert(obj.evaluate_tags(['a', 'b'], ['c', 'd', 'never'], dict()) == True)
    assert(obj.evaluate_tags(['a', 'always'], ['c', 'd', 'always'], dict()) == True)
    assert(obj.evaluate_tags(['never'], ['never'], dict()) == False)

# Generated at 2022-06-13 09:17:40.381594
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        def __init__(self, tags, only_tags, skip_tags, all_vars):
            self._tags = tags
            self._only_tags = only_tags
            self._skip_tags = skip_tags
            self._all_vars = all_vars

        def evaluate_tags(self):
            # Mocking _loader
            self._loader = ''
            return super(MyTaggable, self).evaluate_tags(self._only_tags, self._skip_tags, self._all_vars)

    # Test for items without tags
    assert MyTaggable(None, set(['test']), set(), {}).evaluate_tags() == False
    assert MyTaggable(None, None, None, {}).evaluate_tags() == True

# Generated at 2022-06-13 09:17:51.530325
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    results = dict(skipped=False, failed=False, unreachable=False)
    play_context = PlayContext()
    task = TaskInclude(play=None, task_blocks=[])
    block = Block(parent_block=None, role=RoleDefinition(), task_include=task)
    role_requirement = RoleRequirement(role_name_to_run='test')
    task._parent = block
    task._role = role_requirement
    task._play_context = play_context

# Generated at 2022-06-13 09:18:06.227955
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    import sys
    import yaml
    sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
    from ansible.playbook.task import Task
    from ansible.plugins.loader import play_contexts
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy

    task_data1 = {"tags": ["tag1", "tag2"]}
    task1 = Task.load(task_data1, play=None, variable_manager=None, loader=None)
    task_data2 = {"tags": ["tag1"]}
    task2 = Task.load(task_data2, play=None, variable_manager=None, loader=None)
    task_data3 = {}
    task3 = Task

# Generated at 2022-06-13 09:18:17.374072
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
        # Test when tags is a list
        only_tags = ['tag1', 'tag2']; skip_tags = ['tag3', 'tag4']
        t = Taggable()
        t._tags = ['tag1', 'tag2', 'tag3']
        assert t.evaluate_tags(only_tags, skip_tags, {}) == True
        t._tags = ['tag3', 'tag4', 'tag5']
        assert t.evaluate_tags(only_tags, skip_tags, {}) == False
        t._tags = ['tag5', 'tag6']
        assert t.evaluate_tags(only_tags, skip_tags, {}) == False
        # Test when tags is a string
        only_tags = ['tag1', 'tag2']; skip_tags = ['tag3', 'tag4']
        t = Taggable

# Generated at 2022-06-13 09:18:29.293083
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Definition of a task without tags
    class Task(Taggable):
        pass
    t = Task()

    # Definition of two sets of tags
    only_tags1 = ['tag1', 'tag2', 'tag3']
    skip_tags1 = ['skipped_tag1', 'skipped_tag2', 'skipped_tag3']

    only_tags2 = ['all', 'tag4', 'tag5']
    skip_tags2 = ['skipped_tag4', 'skipped_tag5', 'skipped_tag6']

    # Initialization of the set of variables
    all_vars = dict()

    # Test1: check if the task will be executed when only_tags is set and task has no tags
    # Expected result: False

# Generated at 2022-06-13 09:19:04.682441
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockAnsibleModule(Taggable):
        def __init__(self):
            self.tags = list()

    import pytest

    def test_evaluate_tags_no_tags():
        a = MockAnsibleModule()
        assert a.evaluate_tags(set(), set(), dict()) == True

    class TestEvaluateTags():
        def test_evaluate_tags_only_tags(self):
            a = MockAnsibleModule()
            a.tags.append("test")
            assert a.evaluate_tags(set(["test"]), set(), dict()) == True

        def test_evaluate_tags_only_tags_multi(self):
            a = MockAnsibleModule()
            a.tags.append("test")
            a.tags.append("test2")

# Generated at 2022-06-13 09:19:15.318172
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # First, we imitate a Taggable (in our case a Block) object and initialize it
    # After that, we run the tests on it
    class Block(Taggable):
        name="myblock"

        def __init__(self):
            super(Block, self).__init__()

    block = Block()
    # Normal test
    # True means the item should run
    block.tags = ["t1"]
    only_tags = set()
    skip_tags = set()
    all_vars = {}
    should_run = block.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run is True
    # False means the item shouldn't run
    block.tags = ["t1"]
    only_tags = set()
    skip_tags = set(["t1"])


# Generated at 2022-06-13 09:19:25.072229
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:19:36.892587
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:19:45.708936
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    
    # The attributes of class Taggable
    only_tags = ['Always','Never','Ubuntu','RedHat','Centos','Fedora','Debian','Ubuntu','Windows','Vmware','Cisco','Juniper','Arista','Alcatel','Hpe','Hp','Huawei','Lenovo','MySQL','MSSQL','Oracle','Postgresql','others']
    skip_tags = ['Never']
    all_vars = ['Always','Never']
    
    # The attributes of class Taggable, but with wrong values
    only_tags_failed = ['Always', 'OK', 'Ubuntu', 'Windows']
    skip_tags_failed = ['Never', 'Vmware']
    
    # The output of the test, the test will run with the list of tags assigned to the device, the output should be true if the device is running with the

# Generated at 2022-06-13 09:19:55.697408
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t._tags = [] # empty tags
    t.always_run = False
    assert t.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars=[]) == True
    t._tags = ['always']
    t.always_run = False
    assert t.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars=[]) == True
    t._tags = ['always']
    t.always_run = False
    assert t.evaluate_tags(only_tags=['always'], skip_tags=['always'], all_vars=[]) == False
    t._tags = ['always', 'error']
    t.always_run = False

# Generated at 2022-06-13 09:20:05.481517
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = ['tag1', 'tag2']

    # Default values for only_tags and skip_tags
    assert(t.evaluate_tags([], [], {}) == True)
    # only_tags has 'all' so it should always return True
    assert(t.evaluate_tags(['all'], [], {}) == True)
    # only_tags has 'always' in it; so it should return True
    assert(t.evaluate_tags(['always'], [], {}) == True)
    # only_tags has 'never' in it; but it is not in tags. So it returns False
    assert(t.evaluate_tags(['never'], [], {}) == False)
    # only_tags has 'never' and 'tag2' in it; but 'never' is not in tags

# Generated at 2022-06-13 09:20:13.529448
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # [unit-test]
    # import library
    import sys
    sys.path.append("../../lib/")
    import ansible.module_utils.basic
    import ansible.playbook.task
    import ansible.playbook.role
    import ansible.playbook.play
    import ansible.playbook.handler

    all_vars = {
        'foo': {
            'bar': 'baz'
        }
    }

    # test for ansible.playbook.task.Task
    task = ansible.playbook.task.Task()
    # no tags
    ret = task.evaluate_tags(
        only_tags = None,
        skip_tags = None,
        all_vars  = all_vars,
    )
    assert(ret == True)

    ret = task.evaluate

# Generated at 2022-06-13 09:20:24.704644
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Mock(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # Only tags
    assert Mock(['foo', 'bar']).evaluate_tags(['foo'], [], {}) == True
    assert Mock(['foo', 'bar']).evaluate_tags(['bar'], [], {}) == True
    assert Mock(['foo', 'bar']).evaluate_tags(['baz'], [], {}) == False

    # Skip tags
    assert Mock(['foo', 'bar']).evaluate_tags([], ['foo'], {}) == False
    assert Mock(['foo', 'bar']).evaluate_tags([], ['bar'], {}) == False
    assert Mock(['foo', 'bar']).evaluate_tags([], ['baz'], {}) == True

    # Skip and only tag


# Generated at 2022-06-13 09:20:36.630221
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """
    unit test: evaluate_tags
    """
    class Test(Taggable):
        _loader = None

    only_tags = ['all']
    skip_tags = None
    all_vars = {}

    # test case 1
    result = Taggable.evaluate_tags(Taggable(), only_tags, skip_tags, all_vars)
    assert result == True

    # test case 2
    only_tags = ['all']
    tags = ['never']
    result = Taggable.evaluate_tags(Taggable(), only_tags, skip_tags, all_vars)
    assert result == False

    # test case 3
    only_tags = ['shell']
    tags = ['shell']

# Generated at 2022-06-13 09:21:42.815323
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create the objects we'll use
    variable_manager = VariableManager()
    loader = DataLoader()

    # Create an instance of our class to test
    t = Taggable()

    # Create a task
    t.vars = dict()
    t.tags = ['untagged']
    t.action = dict()
    t.action['__ansible_module__'] = 'test'
    t.action['args'] = {}
    t.action['args']['test'] = 'success'
    t.loop = []

# Generated at 2022-06-13 09:21:56.433104
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager

    mytask = Task()
    mytask._variable_manager = VariableManager()

    assert mytask._evaluate_tags(['all'], ['never']) is True
    assert mytask._evaluate_tags(['always'], ['never']) is True
    assert mytask._evaluate_tags(['never'], ['never']) is False
    assert mytask._evaluate_tags(['never'], ['always']) is False
    assert mytask._evaluate_tags(['all'], ['always']) is False
    assert mytask._evaluate_tags(['never'], []) is False
    assert mytask._evaluate_tags(['never'], ['all']) is False

# Generated at 2022-06-13 09:22:05.664412
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest

    class TestTaggable(Taggable):
        def __init__(self, tags=None):
            self.tags = tags

    class TestTaggable_evaluate_tags(unittest.TestCase):
        def setUp(self):
            self.taggable = TestTaggable

        def test_only_tags(self):
            self.assertFalse(self.taggable(tags=['fake1', 'fake2']).evaluate_tags(only_tags=['real1', 'real2'], skip_tags=None, all_vars=dict()))
            self.assertTrue(self.taggable(tags=['real1', 'real2']).evaluate_tags(only_tags=['real1', 'real2'], skip_tags=None, all_vars=dict()))
           

# Generated at 2022-06-13 09:22:18.816125
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.parsing.yaml.objects import AnsibleMapping

    class Taggable2(Taggable):

        def __init__(self):
            self.tags = ['tag1', 'tag2', 'tag3']

        def _get_ds(self):
            return { 'tags': self.tags }

        def _set_ds(self, ds):
            self.tags = ds['tags']

        ds = property(_get_ds, _set_ds)

    class Fake_Loader():
        pass

    class Fake_DS():
        def get_ds(self, play):
            return AnsibleMapping(play)

    class Fake_Play():
        loader = Fake_Loader()
        ds = Fake_DS()

    fake_play = Fake_Play()
    fake_play.tags = []

# Generated at 2022-06-13 09:22:32.600209
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Create a Taggable object for testing purpose
    class Foo(Taggable):
        pass

    # Create a Taggable object for testing purpose
    class Bar(Foo):
        pass

    t = Bar()

    assert t.evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=[], all_vars={})

    assert not t.evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=['tag3', 'tag1'], all_vars={})

    assert t.evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=['never'], all_vars={})

    # Case where we're not skipping anything

# Generated at 2022-06-13 09:22:40.845176
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class a_Taggable(Taggable):
        def __init__(self, tags, all_vars):
            self.tags = tags
            self.all_vars = all_vars

    from ansible.parsing.dataloader import DataLoader

    fake_loader = DataLoader()

    task = a_Taggable(tags=['a', 'b', 'c'], all_vars={})
    result = task.evaluate_tags(['a', 'e', 'c'], [], fake_loader)
    assert result == True

    task = a_Taggable(tags=[], all_vars={})
    result = task.evaluate_tags(['a', 'e', 'c'], [], fake_loader)
    assert result == True


# Generated at 2022-06-13 09:22:46.039685
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeClass:
        def __init__(self, tags=None, _loader=None):
            self.tags = tags
            self._loader = _loader

        def evaluate_tags(self, only_tags, skip_tags, all_vars):
            return Taggable.evaluate_tags(self, only_tags, skip_tags, all_vars)

    # set up test data
    fake_tags = 'tag_1, tag_2'
    tags = [x.strip() for x in fake_tags.split(',')]
    task = FakeClass(tags=tags, _loader=None)

    # set up test execution context
    # the context is represented by just two strings, the two
    # values of cli options '--tags' and '--skip-tags'
    # in the following tests, the context is defined by

# Generated at 2022-06-13 09:22:54.708165
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeData:
        pass

    data = FakeData()

    data.tags = ['one','two', 'three']
    data.all_vars = dict(var1=1, var2=2, var3=3)
    data.all_vars['tags'] = ['one','two', 'three']

    assert data.evaluate_tags(['one'], [], data.all_vars)
    assert data.evaluate_tags(['one', 'two'], [], data.all_vars)

    assert data.evaluate_tags([], ['one'], data.all_vars)
    assert data.evaluate_tags([], ['one', 'two'], data.all_vars)

    assert data.evaluate_tags(['one'], ['two'], data.all_vars)
    assert data.evaluate_tags

# Generated at 2022-06-13 09:23:02.776128
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self):
            pass

    test_Taggable_object = TestTaggable()
    test_Taggable_object.tags = ['tag_one', 'tag_two']

    only_tags = ['tag_one']
    skip_tags = ['tag_two']
    all_vars = dict()

    assert(test_Taggable_object.evaluate_tags(only_tags, skip_tags, all_vars) == True)

    only_tags = ['tag_one', 'tag_three']
    skip_tags = ['tag_two', 'tag_four']

    assert(test_Taggable_object.evaluate_tags(only_tags, skip_tags, all_vars) == True)

    only_tags = ['tag_four']
