

# Generated at 2022-06-13 09:13:23.187397
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class SimpleTaggable(Taggable):
        _tags = ['foo', 'bar']

    t = SimpleTaggable()
    assert t.evaluate_tags(only_tags=['foo', 'bar', 'foobar'], skip_tags=[], all_vars=dict()) == True
    assert t.evaluate_tags(only_tags=['foo', 'bar'], skip_tags=[], all_vars=dict()) == True
    assert t.evaluate_tags(only_tags=['foo'], skip_tags=[], all_vars=dict()) == True
    assert t.evaluate_tags(only_tags=[], skip_tags=['foo', 'bar', 'foobar'], all_vars=dict()) == False

# Generated at 2022-06-13 09:13:29.725788
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self, tags = []):
            self._tags = tags
            self._loader = None
            self.tags = tags

    my_tags = TestTaggable(tags = ['tag1','tag2','always'])

    assert my_tags.evaluate_tags([], [], {}) == True
    assert my_tags.evaluate_tags(["tag1"], ["tag3"], {}) == True
    assert my_tags.evaluate_tags(["tag1","tag2"], ["tag3"], {}) == True
    assert my_tags.evaluate_tags(["tag5"], ["tag3"], {}) == False


# Generated at 2022-06-13 09:13:34.231860
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Test(Taggable):
        def __init__(self, tags):
            self.tags = tags

    taggable = Test(['tag1', 'tag2', 'tag3'])
    assert taggable.evaluate_tags([], [], {}) == True

    taggable = Test(['tag1', 'tag2', 'tag3'])
    assert taggable.evaluate_tags(['tag1'], [], {}) == True

    taggable = Test(['tag1', 'tag2', 'tag3'])
    assert taggable.evaluate_tags(['tag10'], [], {}) == False

    taggable = Test(['tag1', 'tag2', 'tag3'])
    assert taggable.evaluate_tags(['tag1', 'tag2'], [], {}) == True



# Generated at 2022-06-13 09:13:39.235466
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Dummy(Taggable):
        def __init__(self):
            self.tags = ['foo']
    def _test(only_tags, skip_tags, tags):
        d = Dummy()
        d.tags = tags
        assert d.evaluate_tags(only_tags, skip_tags, {}) == expected


# Generated at 2022-06-13 09:13:51.630583
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    fake_self = dict(
        tags=['a', 'b'],
        untagged=frozenset(['untagged'])
    )

    all_vars = dict()

    assert not Taggable.evaluate_tags(fake_self, ['a'], [], all_vars)
    assert Taggable.evaluate_tags(fake_self, ['a', 'b', 'c'], [], all_vars)
    assert not Taggable.evaluate_tags(fake_self, [], ['a', 'b', 'c'], all_vars)
    assert Taggable.evaluate_tags(fake_self, [], ['c', 'd'], all_vars)
    assert not Taggable.evaluate_tags(fake_self, ['a', 'b'], ['b'], all_vars)


# Generated at 2022-06-13 09:14:02.930560
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.play_context import PlayContext

    tc = Taggable()
    all_vars = dict()
    play_context = PlayContext()
    tc._loader = False
    # Test on tags value list
    tc.tags = ['tag1', 'tag2']
    assert tc.evaluate_tags(['tag1'], [], all_vars) == True, 'Tag list should be executed when only_tags'
    assert tc.evaluate_tags(['tag3'], [], all_vars) == False, 'Tag list should not be executed when no match between only_tags'

# Generated at 2022-06-13 09:14:14.854211
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    task_tags = ['test1', 'test2', 'test3']
    only_tags = ['test1', 'test2']
    skip_tags = ['test3', 'test4']

    t = Taggable()
    t.tags = task_tags

    should_run = t.evaluate_tags(only_tags, skip_tags, None)
    assert should_run == True

    should_run = t.evaluate_tags(None, skip_tags, None)
    assert should_run == True

    should_run = t.evaluate_tags(None, None, None)
    assert should_run == True

    only_tags = ['test1', 'test4']
    should_run = t.evaluate_tags(only_tags, None, None)
    assert should_run == True


# Generated at 2022-06-13 09:14:24.264539
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self, tags=None, only_tags=None, skip_tags=None):
            self.tags = tags
            super(TestTaggable, self).__init__(tags)
            self.only_tags = only_tags
            self.skip_tags = skip_tags

        def get_tags(self):
            return self.evaluate_tags(self.only_tags, self.skip_tags, self.tags)

    t = TestTaggable()
    t.tags = ['tag1', 'tag2', 'tag3']
    t.only_tags = []
    t.skip_tags = []

    assert t.get_tags() == True

    t = TestTaggable()
    t.tags = []
    t.only_tags = []
   

# Generated at 2022-06-13 09:14:32.676919
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t._tags = ["test"]
    assert t.evaluate_tags(["test"], [], {})
    assert not t.evaluate_tags(["nomatch"], [], {})
    assert t.evaluate_tags(["all"], ["never"], {})
    assert not t.evaluate_tags(["all"], ["always"], {})
    assert not t.evaluate_tags(["all"], ["all"], {})
    assert t.evaluate_tags(["all"], ["never", "all"], {})
    assert t.evaluate_tags(["all"], ["never"], {})
    assert t.evaluate_tags(["all"], ["always"], {})
    assert t.evaluate_tags(["all"], ["never", "all"], {})
    assert t.evaluate_tags([], ["never"], {})
    assert t.evaluate_

# Generated at 2022-06-13 09:14:36.448008
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTester:
        def __init__(self, loader):
            self._loader = loader
        def _get_parent_attribute(self, name, default=None):
            return default

    loader = True
    taggable_tester = TaggableTester(loader)
    taggable_tester.tags = ['1','2','3']

    # A task that has 'always' tag, should always run
    taggable_tester.tags = ['always']
    assert taggable_tester.evaluate_tags(['all'], [], True) == True
    assert taggable_tester.evaluate_tags(['1'], [], True) == True

    # A task that has 'never' tag, should never run
    taggable_tester.tags = ['never']
    assert tagg

# Generated at 2022-06-13 09:14:53.824281
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    from ansible.playbook.role.include import Include
    from ansible.playbook.role.task_include import TaskInclude

    ansible_task = Task()

    ansible_block = Block()

    ansible_include = Include()

    ansible_task_include = TaskInclude()


# Generated at 2022-06-13 09:15:06.289576
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_case = {
        'only_tags': [],
        'skip_tags': [],
        'all_vars': {},
        'expected': True
    }

    taggable = Taggable()
    taggable._loader = None
    taggable.tags = []
    assert taggable.evaluate_tags(
        test_case['only_tags'], test_case['skip_tags'], test_case['all_vars']) == test_case['expected']


    test_case = {
        'only_tags': ['ansible', 'foo', 'bar'],
        'skip_tags': [],
        'all_vars': {},
        'expected': False
    }

    taggable = Taggable()
    taggable._loader = None
    taggable.tags

# Generated at 2022-06-13 09:15:18.141687
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Instantiate a mocked Taggable object
    taggable = Taggable()

    # Only run if tag 'test' is present
    assert taggable.evaluate_tags(['test'], [], dict()) == False

    # Only run if tag 'test' is present
    taggable.tags = ['test']
    assert taggable.evaluate_tags(['test'], [], dict()) == True

    # Do not run if tag 'test' is present
    assert taggable.evaluate_tags([], ['test'], dict()) == False

    # Do not run if tag 'test' is present
    taggable.tags = ['other']
    assert taggable.evaluate_tags([], ['test'], dict()) == True

    # Only run if tag 'test' is present
    taggable.tags = ['test']
   

# Generated at 2022-06-13 09:15:26.654451
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        pass

    tt = TestTaggable()

    # Should run: tagged: no, all: no
    tt.tags = ['test']
    only_tags = []
    skip_tags = []
    result = tt.evaluate_tags(only_tags, skip_tags, {})
    assert result == True

    # Should not run: tagged: no, all: yes
    tt.tags = ['test']
    only_tags = ['all']
    skip_tags = []
    result = tt.evaluate_tags(only_tags, skip_tags, {})
    assert result == False

    # Should run: tagged: yes, all: yes
    tt.tags = ['test']
    only_tags = ['all', 'test']
    skip_tags = []
   

# Generated at 2022-06-13 09:15:36.394171
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    import ansible.playbook.block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    loader = ansible.cli.CLI.load_file
    variable_manager = ansible.playbook.variable_manager.VariableManager()
    class MyBlock( ansible.playbook.block.Block ):
        pass
    block = MyBlock(loader=loader, play=None, parent_block=None, role=None, task_include=None, variable_manager=variable_manager)
    variable_manager.set_inventory(ansible.inventory.Inventory(loader=loader, variable_manager=variable_manager, host_list="/dev/null"))

# Generated at 2022-06-13 09:15:51.827509
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block 
    from ansible.playbook.play import Play
    from collections import namedtuple
    from ansible.module_utils.six import string_types

    def _check_evaluate_tags(obj, only_tags, skip_tags, vars, expected_result):
        if expected_result == 'error':
            try:
                obj.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars=vars)
                assert False
            except:
                pass
        else:
            actual_result = obj.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars=vars)
            assert actual

# Generated at 2022-06-13 09:15:56.732638
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self, tags, only_tags, skip_tags, all_vars):
            self.tags = tags
            self.evaluate_tags(only_tags, skip_tags, all_vars)

    # Check if the task runs when there are no tags set
    assert TestTaggable([], [], [], {}).evaluate_tags([], [], {})

    # Check if a task run when only_tags is empty
    assert TestTaggable(['a'], [], [], {}).evaluate_tags([], [], {})

    # Check if a task with different tags runs when only_tags is empty
    assert TestTaggable(['b'], [], [], {}).evaluate_tags([], [], {})

    # Check if a task with a common tag runs when

# Generated at 2022-06-13 09:16:06.744453
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    # Test a task
    task_tags = ['a', 'b']
    task = Task()
    task._attributes['tags'] = task_tags

    # only_tags = None, skip_tags = None
    assert task.evaluate_tags(None, None) == True

    # only_tags = None, skip_tags = []
    assert task.evaluate_tags(None, []) == True

    # only_tags = None, skip_tags = [t1, t2]
    only_tags = None
    skip_tags = [ 't1', 't2' ]

# Generated at 2022-06-13 09:16:14.947513
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    #TODO: test for all the possible combinations of the ifs in the function

    # test for when should_run = True
    host = Taggable()
    host.tags = ['always']
    only_tags = ['always']
    skip_tags = ['never']
    all_vars = {}
    assert host.evaluate_tags(only_tags, skip_tags, all_vars) == True

    # test for when should_run = False
    host.tags = ['never']
    only_tags = ['always']
    skip_tags = ['never']
    all_vars = {}
    assert host.evaluate_tags(only_tags, skip_tags, all_vars) == False

# Generated at 2022-06-13 09:16:25.297550
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeClass(Taggable):
        pass

    task = FakeClass()

    assert task.evaluate_tags(only_tags=set(['all']), skip_tags=set([]),
            all_vars={}) is True

    assert task.evaluate_tags(only_tags=set(['all']), skip_tags=set(['all']),
            all_vars={}) is False

    assert task.evaluate_tags(only_tags=set(['all']), skip_tags=set(['never']),
            all_vars={}) is True

    assert task.evaluate_tags(only_tags=set(['all']), skip_tags=set(['always']),
            all_vars={}) is True


# Generated at 2022-06-13 09:16:48.222483
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test when only_tags (include) is set
    test_play = Taggable()
    test_play.tags = ['include', 'include1', 'include2']
    assert test_play.evaluate_tags(['include', 'include2'], [], dict()) == True
    assert test_play.evaluate_tags(['include', 'include3'], [], dict()) == True
    assert test_play.evaluate_tags(['include1', 'include2'], [], dict()) == True
    assert test_play.evaluate_tags(['include1', 'include'], [], dict()) == True
    assert test_play.evaluate_tags(['include2', 'include'], [], dict()) == True
    assert test_play.evaluate_tags(['include3'], [], dict()) == False

    # Test when skip_tags is set

# Generated at 2022-06-13 09:17:01.890456
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:17:14.087826
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.role.definition import RoleDefinition

    fake_loader = "fake_loader"
    fake_variable_manager = "fake_variable_manager"

    role = RoleDefinition()

    role._loader = fake_loader
    role.name = "fake_role"
    role.only_tags = ["fake_only_tags"]
    role.skip_tags = ["fake_skip_tags"]

    role.tags = ["fake_tags"]
    role.tags = [ "fake_tags"]

    result = role.evaluate_tags(role.only_tags, role.skip_tags, "fake_variable_manager")
    assert result == False



# Generated at 2022-06-13 09:17:23.202193
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        tags = ['test1']
    t = TestTaggable()

    assert t.evaluate_tags(['test1'], [], dict())
    assert not t.evaluate_tags([], ['test1'], dict())
    assert t.evaluate_tags([], [], dict())

    t.tags = ['test2', 'test1']
    assert t.evaluate_tags(['test1'], [], dict())
    assert not t.evaluate_tags([], ['test1'], dict())

    t.tags = ['test1', 'test2', 'test3']
    assert t.evaluate_tags(['test1', 'test2'], [], dict())
    assert not t.evaluate_tags(['test2', 'test3'], [], dict())
    assert not t.evaluate_

# Generated at 2022-06-13 09:17:31.870165
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    class FakeLoader(object):
        def find_plugin(self, name, mod_type):
            return None
        def get_basedir(self):
            return None

    class FakeVarManager(object):
        def __init__(self):
            self.vars = {}
        def get_vars(self):
            return self.vars

    class TestEvaluateTags(unittest.TestCase):

        def setUp(self):
            self.task = Task()
            self.task._loader = FakeLoader()
            self.task._variable_manager = FakeVarManager()

            self.play = Play()
            self.play._loader = FakeLoader()

# Generated at 2022-06-13 09:17:36.731085
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Sample(Taggable):
        pass

    obj = Sample()
    obj.tags = ['a', 'b']

    # Test 1:
    # all_vars = None
    # only_tags = 'c'
    # skip_tags = None
    all_vars = None
    only_tags = 'c'
    skip_tags = None
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars) is False

    # Test 2:
    # all_vars = None
    # only_tags = 'c'
    # skip_tags = 'b'
    all_vars = None
    only_tags = 'c'
    skip_tags = 'b'
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars) is True

    # Test

# Generated at 2022-06-13 09:17:48.840674
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    o = Taggable()
    o.tags = ["myHost"]

    # no tags enabled
    assert o.evaluate_tags(None, None, {})
    assert o.evaluate_tags([], [], {})
    assert o.evaluate_tags([], ['all'], {})

    # only tags
    assert o.evaluate_tags(["myHost","otherHost"], [], {})
    assert not o.evaluate_tags(["otherHost"], [], {})

    # skip tags
    assert not o.evaluate_tags(["all"], ['myHost'], {})
    assert not o.evaluate_tags(["all"], ['myHost','otherHost'], {})
    assert o.evaluate_tags(["all"], ['otherHost'], {})

    # both enabled

# Generated at 2022-06-13 09:17:56.045655
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    task = Task()
    task.tags = ['tag1']
    assert task.evaluate_tags(['tag1'], [], {})

    task = Task()
    task.tags = ['tag1']
    assert not task.evaluate_tags(['tag2'], [], {})

    task = Task()
    task.tags = ['tag1', 'tag2']
    assert task.evaluate_tags(['tag1', 'tag2'], [], {})

    task = Task()
    task.tags = ['tag1', 'tag2']
    assert not task.evaluate_tags(['tag1'], [], {})

    task = Task()
    task.tags = ['tag1']

# Generated at 2022-06-13 09:18:10.509553
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Assemble the test data
    _templar = "Templar"
    _loader = "Loader"
    _variables = "Variables"
    _task = Taggable()
    _task._loader = _loader
    _task.tags = [1,2]

    # Run the code to be tested
    result = _task.evaluate_tags("only_tags", "skip_tags", _variables)

    # Verify results
    assert result == True
    assert _task.tags == [1,2]
    assert _task.evaluate_tags("only_tags", None, _variables) == True
    assert _task.evaluate_tags("only_tags", "all", _variables) == False
    assert _task.evaluate_tags("only_tags", "tagged", _variables) == True

# Generated at 2022-06-13 09:18:21.759517
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableClass(Taggable):
        tags = []

    t = TaggableClass()

    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['never'], skip_tags=[], all_vars={}) == False

    t.tags = ['always']
    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars={}) == True

# Generated at 2022-06-13 09:18:59.058290
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.utils.vars import combine_vars
    from ansible.vars import VariableManager

    class TaggableTest:
        def __init__(self, tags = None):
            self.tags = tags
            self.only_tags = None
            self.skip_tags = None
            self.role = None
            self._loader = None

        def evaluate_tags(self, only_tags, skip_tags, all_vars):
            self.only_tags = only_tags
            self.skip_tags = skip_tags
            return Taggable.evaluate_tags(self, only_tags, skip_tags, all_vars)

        def evaluate_only_tags(self, all_vars):
            return self.evaluate_tags(self.only_tags, None, all_vars)


# Generated at 2022-06-13 09:19:06.776274
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    testobj = Taggable()
    testobj.tags = ['test', 'anothertest']

    # Simple test
    assert testobj.evaluate_tags(['test'], ['never'], []) == True
    assert testobj.evaluate_tags(['test'], ['test', 'never'], []) == False

    # Tags is not a list
    try:
        testobj.evaluate_tags(1, 1, [])
    except AnsibleError as e:
        pass
    else:
        assert False, "Should raise an AnsibleError Exception, but no Exception was raised"

    # Attempt to modify the original list
    attempt = ['test']
    testobj.evaluate_tags(attempt, ['never'], [])
    assert attempt == ['test'], "Should not have modified the original list"

# Generated at 2022-06-13 09:19:17.024463
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task

    class test_Taggable(Taggable):
        def __init__(self):
            self.tags=None

    obj=test_Taggable()
    obj.tags=[]

    # test when tags is []
    print('Test only_tags=all, skip_tags=[]')
    assert obj.evaluate_tags(['all'], [], {})
    print('Test only_tags=untagged, skip_tags=[]')
    assert obj.evaluate_tags(['untagged'], [], {})
    print('Test only_tags=[], skip_tags=[]')
    assert obj.evaluate_tags([], [], {})
    print('Test only_tags=[], skip_tags=tagged')
    assert obj.evaluate_tags([], ['tagged'], {})

# Generated at 2022-06-13 09:19:23.445357
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeModule(object):
        pass

    fake_module = FakeModule()
    fake_module.tags = None
    fake_module.only_tags = None
    fake_module.skip_tags = None
    fake_module.all_vars = {}


    # Test with no tags
    assert Taggable().evaluate_tags(None, None, {}) == True
    assert Taggable().evaluate_tags(None, [], {}) == True
    assert Taggable().evaluate_tags([], None, {}) == True
    assert Taggable().evaluate_tags([], [], {}) == True

    # Test with a list of tags
    assert Taggable().evaluate_tags(None, ['foo'], {}) == True
    assert Taggable().evaluate_tags(None, ['tagged'], {}) == True

# Generated at 2022-06-13 09:19:30.081622
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    only_tags = ['first', 'second']
    skip_tags = ['skip']

    obj = DummyTaggable()

    # Check : should run as tagged
    obj.tags = ['first']
    should_run = obj.evaluate_tags(only_tags, skip_tags, None)
    assert should_run

    # Check : should run as tagged
    obj.tags = ['second']
    should_run = obj.evaluate_tags(only_tags, skip_tags, None)
    assert should_run

    # Check : should run as no skip-tags
    obj.tags = ['first']
    should_run = obj.evaluate_tags(only_tags, [], None)
    assert should_run

    # Check : should not run as tagged as skip-tag
    obj.tags = ['skip']
    should_run = obj

# Generated at 2022-06-13 09:19:41.163066
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    test_task = Task()
    test_task._role_name = 'test_task'
    test_task.task_include = 'templates/test_task_tags.yml'

    test_block = Block()
    test_block._role_name = 'test_block'
    test_block.block_include = 'templates/test_block_tags.yml'


    # Test condition when only_tags is None
    test_task.only_tags = None
    assert test_task.evaluate_tags(test_task.only_tags, test_task.skip_tags, test_task._variable_manager.get_vars(loader=test_task._loader, play=test_task._play))

    # Test condition

# Generated at 2022-06-13 09:19:52.513829
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Test valid_dataset with only_tags & skip_tags as None
    valid_dataset = [
        {'only_tags': None, 'skip_tags': None, 'tags': ['all'], 'result': True},
        {'only_tags': None, 'skip_tags': None, 'tags': ['bar'], 'result': True},
        {'only_tags': None, 'skip_tags': None, 'tags': ['notag'], 'result': True},
        {'only_tags': None, 'skip_tags': None, 'tags': [], 'result': True},
        {'only_tags': None, 'skip_tags': None, 'tags': None, 'result': True},
    ]

    for data in valid_dataset:
        tags = data['tags']

# Generated at 2022-06-13 09:20:02.961824
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import sys
    import os
    path_to_add = os.path.join(os.path.dirname(__file__), '..', '..', 'lib')
    sys.path.append(path_to_add)
    from ansible.playbook import Play, PlayBook

    #with no tags given
    play1 = Play().load({
        "name": "test-play",
        "hosts": "localhost",
        "tasks": [
            {
                "name": "test task",
                "action": {
                    "module": "shell",
                    "args": "/bin/false"
                    }
                }
        ]})
    only_tags = ['test-tag']
    skip_tags = []

    print(play1.evaluate_tags(only_tags, skip_tags, {}))
    assert play

# Generated at 2022-06-13 09:20:16.569080
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader

    # First create an empty object of class Taggable
    class Test(Taggable):
        pass

    tags_obj = Test()

    # Now tag the object with tags
    tags_obj._tags = ['demo', 'demo1']

    # Test to check if the task is to be run based on the tags
    # Check that the task is run for given tag
    only_tags = ['demo']
    skip_tags = []
    all_vars = {}
    assert tags_obj.evaluate_tags(only_tags, skip_tags, all_vars)

    # Test to check if the task is to be run based on the tags
    # Check that the task is to be skipped for the

# Generated at 2022-06-13 09:20:28.401355
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''Unit test for method evaluate_tags of class Taggable'''

    tag_list = ['tag1', 'tag2', 'tag3']
    skip_tags = ['tag1', 'tag4']
    only_tags = ['tag1', 'tag4']

    # Check for method signature change
    try:
        taggable = Taggable()
        taggable.tags = tag_list
        taggable.evaluate_tags(only_tags, skip_tags, {})
    except TypeError:
        raise Exception("Function signature of Taggable.evaluate_tags has changed")

    # Simulate actual execution based on tag options
    taggable = Taggable()
    taggable.tags = tag_list
    should_run = taggable.evaluate_tags(only_tags, skip_tags, {})

    #

# Generated at 2022-06-13 09:21:37.766733
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self):
            pass
        
    t = TestTaggable()
    t.tags = []
    assert t.evaluate_tags(['tag'], [], None) == True
    assert t.evaluate_tags(['tag', 'other_tag'], [], None) == True
    assert t.evaluate_tags(['tag'], ['other_tag'], None) == True
    assert t.evaluate_tags(['other_tag'], ['tag'], None) == False
    
    t.tags = ['tag']
    assert t.evaluate_tags(['tag'], [], None) == True
    assert t.evaluate_tags(['tag', 'other_tag'], [], None) == True

# Generated at 2022-06-13 09:21:44.091235
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class A(Taggable):
        pass

    class B(A):
        pass

    t = A()
    t.tags = ['tag1', 'tag2', 'tag3']
    only_tags = set(['tag1'])
    skip_tags = set(['tag2'])
    all_vars = dict()
    result = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == True

    t.tags = ['tag2']
    result = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == False

    t.tags = []
    skip_tags = set(['tag2'])
    result = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == False

   

# Generated at 2022-06-13 09:21:57.589471
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    #import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.block
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_hash
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader

    class TestTask(Taggable):
        tags = ['tagged']

    class TestPlay(Taggable):
        tags = ['tagged']

    class TestBlock(Taggable):
        tags = ['tagged']

    class TestPlaybook(Taggable):
        tags = ['tagged']

# Generated at 2022-06-13 09:22:01.959028
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    shouldn't test this method with the class Taggable itself
    because the class Taggable has to be imported from
    ansible.playbook.task_include
    ansible.playbook.task
    ansible.playbook.role.include
    ansible.playbook.role
    ansible.inventory
    ansible.runner.action_plugins
    so to make the test easy, a mock class Taggable is used
    '''
    class Taggable(object):
        def __init__(self, tags):
            self.tags = tags

        def evaluate_tags(self, only_tags, skip_tags, all_vars):
            if self.tags:
                templar = Templar(loader=None, variables=all_vars)
                tags = templar.template(self.tags)
                self

# Generated at 2022-06-13 09:22:13.598126
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Given: a task with 'when' tag, 'always' tag, and 'never' tag
    class test_task(Taggable):
        def __init__(self):
            self.tags = ['always', 'never', 'when']

    t = test_task()
    
    # when: only_tags is a list ['never']
    only_tags = ['never']
    # and: skip_tags is a list ['always']
    skip_tags = ['always']

    # then: the value should_run should be true
    assert t.evaluate_tags(only_tags, skip_tags, None)


# Generated at 2022-06-13 09:22:19.178340
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    # create instance of Taggable
    obj = Taggable()
    # set tags attribute
    obj.tags = [u'foo', u'bar']
    # set only_tags attribute
    only_tags = [u'foo', u'baz']
    # set skip_tags attribute
    skip_tags = [u'bar', u'baz']
    # create dummy vars
    all_vars = {u'foo': u'baz'}
    # create mock of PlayContext so evaluate_tags method can process
    mock_play_context = type('obj', (object,), {'tags': [only_tags, skip_tags]})()


# Generated at 2022-06-13 09:22:30.207671
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeTaggable(Taggable):
        def __init__(self, tags = []):
            self.tags = tags
    # Check the default value of should_run (True)
    assert True == FakeTaggable([]).evaluate_tags([], [], {}), "Class Taggable: method evaluate_tags: default value is not True"
    # Check if should_run is False when tag 'never' is present in only_tags
    assert False == FakeTaggable(['never']).evaluate_tags(['never'], [], {}), "Class Taggable: method evaluate_tags: should_run is not False when tag 'never' is present in only_tags"
    # Check if should_run is False when tag 'never' is present in skip_tags

# Generated at 2022-06-13 09:22:39.571453
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    class TestMetaClass(type):
        def __new__(cls, name, bases, attrs):
            def run_test(self, only_tags, skip_tags, tags, all_vars, expected):
                self.assertEqual(
                    self.testobject.evaluate_tags(only_tags, skip_tags, all_vars),
                    expected,
                    "expected %s with tags %s, only_tags %s and skip_tags %s" %
                    (expected, tags, only_tags, skip_tags)
                )
            for key, value in attrs.items():
                if key.startswith("test_"):
                    setattr(cls, key, run_test)
                    # Delete the test from attrs
                    del attrs[key]

# Generated at 2022-06-13 09:22:50.230921
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Testcase for method evaluate_tags of class Taggable
    '''
    # Extract current object
    test = Taggable()

    # Taggable only_tags and skip_tags
    # Testcase 1: both are None and tags are None
    test.tags = None
    assert test.evaluate_tags(only_tags=None, skip_tags=None, all_vars=None) == True

    # Testcase 2: both are None and tags are 'Testing'
    test.tags = 'Testing'
    assert test.evaluate_tags(only_tags=None, skip_tags=None, all_vars=None) == True

    # Testcase 3: only_tags are None and skip_tags are 'Testing'
    test.tags = 'Testing'

# Generated at 2022-06-13 09:22:55.761145
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class test_class(Taggable):
        tags = ['foo']
        only_tags = ['all', 'foo']
        skip_tags = ['all', 'bar']
        all_vars = {}
        _loader = ''

    test_obj = test_class()
    assert test_obj.evaluate_tags(test_obj.only_tags, test_obj.skip_tags, test_obj.all_vars) == True

if __name__ == '__main__':
    test_Taggable_evaluate_tags()