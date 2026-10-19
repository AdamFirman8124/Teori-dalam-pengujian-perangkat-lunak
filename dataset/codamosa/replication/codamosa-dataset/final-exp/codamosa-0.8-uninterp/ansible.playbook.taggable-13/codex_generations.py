

# Generated at 2022-06-13 09:13:24.412508
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass(Taggable):
        def __init__(self, _loader, tags):
            self._loader = _loader
            self.tags = tags

    # Test scenarios

# Generated at 2022-06-13 09:13:35.458311
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import sys
    import os

    test_class = Taggable()
    test_class.tags = ['test_tag']

    sys.path.append("..") 
    if not os.getcwd().endswith("test"):
        raise AnsibleError("Unexpected working directory. Should be in test dir")

    from ansible.playbook.task import Task
    test_obj = Task()
    test_obj.vars = {}
    test_obj.tags = []
    should_run = test_class.evaluate_tags(test_obj, [], [], test_obj.vars)
    assert should_run == True

    should_run = test_class.evaluate_tags(test_obj, ['test_tag'], [], test_obj.vars)
    assert should_run == True


# Generated at 2022-06-13 09:13:43.213527
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    taggable = Taggable()

    # Test with both tags and only_tags
    taggable._tags = ['all', 'target']
    only_tags = ['all']
    skip_tags = []
    assert taggable.evaluate_tags(only_tags, skip_tags, None)

    # Test with both tags and skip_tags
    taggable._tags = ['all', 'target']
    only_tags = []
    skip_tags = ['all']
    assert not taggable.evaluate_tags(only_tags, skip_tags, None)

    # Test with skip_tags and untagged
    taggable._tags = []
    only_tags = []
    skip_tags = ['all', 'untagged']
    assert not taggable.evaluate_tags(only_tags, skip_tags, None)

    #

# Generated at 2022-06-13 09:13:53.659618
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class text(Taggable):
        def __init__(self):
            self.tags = []
    class test(Taggable):
        def __init__(self):
            self.tags = None
    # test1
    only_tags = []
    skip_tags = []
    obj = text()
    res = obj.evaluate_tags(only_tags, skip_tags, {})
    assert(res == True)
    # test2
    only_tags = ['test_tag']
    skip_tags = []
    obj = text()
    obj.tags = ['test_tag']
    res = obj.evaluate_tags(only_tags, skip_tags, {})
    assert(res == True)
    # test3
    only_tags = ['test_tag']
    skip_tags = ['test_tag2']


# Generated at 2022-06-13 09:14:05.213433
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Unit test for method evaluate_tags of class Taggable
    '''

    # Create dummy class inheriting from Taggable
    class DummyTaggableClass(Taggable):
        pass

    task1 = DummyTaggableClass()
    task2 = DummyTaggableClass()
    task3 = DummyTaggableClass()
    task4 = DummyTaggableClass()

    # Test the behavior of method evaluate_tags when parameter only_tags is specified
    only_tags = {'tagged', 'all', 'always'}

    # Test task1 with tags = []
    task1.tags = []
    res = task1.evaluate_tags(only_tags, [], {})
    assert res == True

    # Test task2 with tags = {'tagged', 'all', 'always'}


# Generated at 2022-06-13 09:14:12.335835
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest
    from ansible.playbook.base import Base

    only_tags = frozenset(['tag1', 'tag2', 'tagged'])
    skip_tags = frozenset(['tag3', 'tag4', 'tagged'])

    class ClassTaggable(Taggable):
        def __init__(self, tags):
            self.tags = tags

    class TestTaggable(unittest.TestCase):
        def test_list_tags(self):
            ''' Check the case that the tags are a list of items '''
            class_taggable = ClassTaggable(tags=['tag1'])
            self.assertTrue(class_taggable.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars={}))


# Generated at 2022-06-13 09:14:25.278006
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class myclass(Taggable):
        def __init__(self):
            self._tags = ["tag1"]

    a=myclass()

    # Only run the task if its tagged
    assert a.evaluate_tags(["tag1","tag2"], [], {}) == True
    assert a.evaluate_tags(["tag2"], [], {}) == False

    # Skip the task if its tagged
    assert a.evaluate_tags([], ["tag1","tag2"], {}) == False
    assert a.evaluate_tags([], ["tag2"], {}) == True

    # Skip the task if its tagged and run the task if tagged
    assert a.evaluate_tags(["tag1", "tag2"], ["tag1", "tag2"], {}) == True


# Generated at 2022-06-13 09:14:27.906822
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    # assert obj.evaluate_tags('only_tags', 'skip_tags') == True

# Generated at 2022-06-13 09:14:35.676532
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.taggable import Taggable
    block = Block()
    block.tags = ["tag1", "tag2"]
    block.taggable = Taggable()
    assert(block.taggable.evaluate_tags(["tag1"], [], {}) == True)
    assert(block.taggable.evaluate_tags(["tag3"], [], {}) == False)
    assert(block.taggable.evaluate_tags([], ["tag1"], {}) == False)
    assert(block.taggable.evaluate_tags([], ["tag3"], {}) == True)
    assert(block.taggable.evaluate_tags([], [], {}) == True)

# Generated at 2022-06-13 09:14:41.382154
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    # Play with tags
    play1 = Play()
    play1.tags = ['test']

    # Task without tags
    task1 = Task()
    task1.tags = None

    # Task with tags
    task2 = Task()
    task2.tags = ['test']

    # Task with tags
    task3 = Task()
    task3.tags = ['tag1', 'tag2']

    task3.evaluate_tags(['test', 'tag1'], [], VariableManager())

    # Test
    assert(play1.evaluate_tags(['test'], [], VariableManager()) == True)

# Generated at 2022-06-13 09:14:57.059895
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.host import Host

    # test for: task include
    host = Host(name="fake_host")
    i_obj = TaskInclude()
    i_obj._role_name = 'fake_role'
    i_obj._task_name = 'fake_task'
    i_obj.tags = ['fake_tag']

    # even when tags are set, only_tags or skip_tags
    # should determine if we run or not
    assert i_obj.evaluate_tags(['always'], [], host.get_vars()) is True
    assert i_obj.evaluate_tags([], ['never'], host.get_vars()) is True

# Generated at 2022-06-13 09:15:09.073481
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Define a dict with variable names and their values.
    variables = dict(
        foo="Foo variable value",
        bar="Bar variable value",
    )

    # Create a Taggable instance.
    t = Taggable()

    # Initialize the Taggable fields.
    t._loader = None
    t.name = None
    t.tags = list()

    # Define the only_tags and skip_tags lists.
    # Both empty lists.
    only_tags = list()
    skip_tags = list()

    # Run the evaluated tags.
    should_run0 = t.evaluate_tags(only_tags, skip_tags, variables)

    # The "should_run" value must be "True".
    assert should_run0 == True

    # Define the only_tags and skip_tags lists.


# Generated at 2022-06-13 09:15:20.796594
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = set()
    skip_tags = set()
    host = Taggable()
    host.tags = ['A','B','C','D','never','always']

    assert host.evaluate_tags(only_tags, skip_tags, dict())
    only_tags.add('A')
    assert host.evaluate_tags(only_tags, skip_tags, dict())
    only_tags.add('B')
    assert host.evaluate_tags(only_tags, skip_tags, dict())
    only_tags.add('C')
    assert host.evaluate_tags(only_tags, skip_tags, dict())
    only_tags.add('D')
    assert host.evaluate_tags(only_tags, skip_tags, dict())
    only_tags.add('never')

# Generated at 2022-06-13 09:15:32.372665
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    task_without_tags = dict(action=dict(module='shell', args='echo bonjour'),
                             delegate_to='127.0.0.1',
                             name='A task',
                             notify=[],
                             run_once=False,
                             environment={},
                             register='shell_out',
                             tags=[])

    task_with_tags = task_without_tags.copy()
    task_with_tags['tags'] = ['a_tag']

    task_with_multiple_tags = task_without_tags.copy()
    task_with_multiple_tags['tags'] = ['a_tag', 'another_tag']

    task_with_always_tag = task_with_tags.copy()
    task_with_always_tag['tags'].append('always')

    task_with_never_

# Generated at 2022-06-13 09:15:41.879276
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        pass

    result = []

    def test_evaluate_tags(tags, only_tags, skip_tags, should_run):

        task = TestTaggable()
        task.tags = tags
        result.append(task.evaluate_tags(only_tags, skip_tags, {}) == should_run)

    # Functionality for short-circuit evaluation is tested.
    # Number of steps is minimized and selected at random, so some steps might be redundant.

    # Tagged task should run if no tags given
    test_evaluate_tags(tags=['tag1'], only_tags=None,    skip_tags=None,    should_run=True)

    # Tagged task should run if only_tags none

# Generated at 2022-06-13 09:15:55.640053
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    assert t.evaluate_tags(None, None, None) == True

    t.tags = ['some_tag']
    assert t.evaluate_tags(None, None, None) == True

    t.tags = ['some_tag']
    assert t.evaluate_tags(['all'], ['all'], None) == True
    assert t.evaluate_tags(['all'], ['some_tag'], None) == True
    assert t.evaluate_tags(['all'], ['all', 'some_tag'], None) == True
    assert t.evaluate_tags(['some_tag'], ['all', 'some_tag'], None) == True
    assert t.evaluate_tags(['some_tag'], ['all'], None) == True

    t.tags = ['some_tag_2']
   

# Generated at 2022-06-13 09:16:05.880586
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):
        def __init__(self, tags, only_tags, skip_tags):
            self._tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags

    ############################################################

    # all tags are empty lists
    tags = []
    only_tags = []
    skip_tags = []
    mock_taggable = MockTaggable(tags, only_tags, skip_tags)
    assert(mock_taggable.evaluate_tags(only_tags, skip_tags, {}))

    # only_tags has 'a'
    tags = []
    only_tags = ['a']
    skip_tags = []
    mock_taggable = MockTaggable(tags, only_tags, skip_tags)

# Generated at 2022-06-13 09:16:15.209224
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    import sys

    # test Task
    t = Task()
    t._load_name("test")
    t._load_tags("foo, bar, baz")

    only_tags = ["foo", "baz"]
    skip_tags = ["bar"]
    all_vars = {}
    should_run = t.evaluate_tags(only_tags, skip_tags, all_vars)
    if not should_run:
        print("Test failed. Expected should_run to be True.")
        sys.exit(1)

    # test TaskInclude
    ti = TaskInclude()
    ti._load_name("test")

# Generated at 2022-06-13 09:16:18.623563
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    from ansible.playbook.base import Base
    from ansible.playbook.handler import Handler

    host = Base()
    handler = Handler()

    vars = {'name': 'hello'}
    templar = Templar(loader=host._loader, variables=vars)

    class FakeTask(Taggable):
        def __init__(self):
            self._tags = ['tag1']

    class FakeHandler(Taggable):
        def __init__(self):
            self._tags = ['tag1']


# Generated at 2022-06-13 09:16:27.484234
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    playbook = {}
    t = Taggable(loader=None, play=playbook, parent_block=None)
    t._tags = ['first_tag', 'second_tag']
    should_run = t.evaluate_tags(['first_tag'],['second_tag'], {})
    assert should_run

    t._tags = []
    should_run = t.evaluate_tags([],['second_tag'], {})
    assert should_run

    t._tags = []
    should_run = t.evaluate_tags(['first_tag'],['second_tag'], {})
    assert not should_run

    t._tags = ['first_tag', 'second_tag']
    should_run = t.evaluate_tags(['first_tag'],['second_tag'], {})
    assert should_run

# Generated at 2022-06-13 09:16:41.662212
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass



# Generated at 2022-06-13 09:16:49.790045
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestClass:
        # fake class for test
        _loader = None
        tags = None

        def __init__(self, tags):
            self.tags = tags


# Generated at 2022-06-13 09:16:58.060940
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    play = Play()
    names_list = [
        'A',
        'B',
        'C',
        'never',
        '1234',
        'untagged',
    ]
    for name in names_list:
        play.add(Task(name=name, tags=['always'], action='noop'))
        play.add(Task(name=name, tags=['never'], action='noop'))
    play.add(Task(name='D', tags=['1234'], action='noop'))
    play.add(Task(name='E', tags=['never', '1234'], action='noop'))
    play.add(Task(name='F', action='noop'))

# Generated at 2022-06-13 09:17:09.322636
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # load test data
    data_base_dir = 'lib/ansible/playbook/test/data'
    data_dir = '%s/blocks/tagged' % data_base_dir
    data_vars = '%s/vars.yml' % data_dir
    data_play = '%s/play.yml' % data_dir
    data_play_untagged_task = '%s/play.yml' % data_base_dir

    # load data
    from ansible.parsing.yaml.loader import AnsibleLoader
    data_vars = AnsibleLoader(open(data_vars, 'r'), file_name=data_vars).get_single_data()

# Generated at 2022-06-13 09:17:21.488936
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    tags = ['tag1','tag2','tag3','tag4','tag5','tag6','tag7','tag8','tag9','tag10']

    p0 = Play()
    p1_1 = Task()
    p1_2 = Task()
    p1_3 = Task()
    p1_4 = Task()
    p1_5 = Task()
    p1_6 = Task()
    p1_7 = Task()
    p1_8 = Task()
    p1_9 = Task()
    p1_10 = Task()
    p1 = Play()
    p2_1 = Task()
    p2_2 = Task()

# Generated at 2022-06-13 09:17:30.956062
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Test evaluate_tags()
    '''

    class Taggable_test(Taggable):
        '''
        Derived class for testing Taggable class.
        '''

        # Fake _loader parameter.
        _loader = None

    # Prepare variables used in the tests
    taggable = Taggable_test()
    taggable.tags = ['tag1', 'tag2', 'tag3']
    tags = taggable.tags
    only_tags = None
    skip_tags = None
    all_vars = dict()

    # Test case 1.
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3']
    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)

# Generated at 2022-06-13 09:17:39.682845
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    fake_loader = None
    fake_vars = dict(always=['always'], never=['never'], foo=['foo'], bar=['bar'], baz=['baz'])

# Generated at 2022-06-13 09:17:51.029044
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    task = Task()

    # default is true
    assert True == task.evaluate_tags(only_tags=[], skip_tags=[], all_vars={})

    # with 'always', should run
    assert True == task.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars={})

    # with 'never', should not run
    assert False == task.evaluate_tags(only_tags=['never'], skip_tags=[], all_vars={})

    # with 'never' in skip_tags and 'never' in tags, should not run
    assert False == task.evaluate_tags(only_tags=[], skip_tags=['never'], all_vars={})
    task._tags = ['never']
    assert False == task.evaluate_tags

# Generated at 2022-06-13 09:18:05.611485
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = ['a', 'b']
    assert t.evaluate_tags(only_tags=['a', 'c'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['c', 'd'], skip_tags=[], all_vars={}) == False
    assert t.evaluate_tags(only_tags=['a', 'not_b'], skip_tags=[], all_vars={}) == False
    assert t.evaluate_tags(only_tags=['a', 'b'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['not_a', 'not_b'], skip_tags=[], all_vars={}) == False

# Generated at 2022-06-13 09:18:17.030145
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    tag = Task()
    role = Role()

    tag.tags = 'tag1,tag2,tag3'
    tag.evaluate_tags([], ['tag3'], {})
    assert(tag.tags == ['tag1', 'tag2', 'tag3'])

    tag.evaluate_tags([], ['tag2'], {})
    assert(tag.tags == ['tag1', 'tag2', 'tag3'])

    tag.tags = 'tag1,tag2'
    tag.evaluate_tags(['tag1', 'tag2'], ['tag3'], {})
    assert(tag.tags == ['tag1', 'tag2'])


# Generated at 2022-06-13 09:18:50.873181
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
            tags = ['a']
    objTaggable = TestTaggable()

    # tags is a list; should return negative
    only_tags = ['b']
    skip_tags = []
    all_vars = {}
    assert objTaggable.evaluate_tags(only_tags, skip_tags, all_vars) == False

    # tags is a list; should return positive
    only_tags = ['a']
    skip_tags = []
    all_vars = {}
    assert objTaggable.evaluate_tags(only_tags, skip_tags, all_vars) == True

    # tags is a list; should return positive
    only_tags = ['all']
    skip_tags = []
    all_vars = {}
    assert objTaggable.evaluate_

# Generated at 2022-06-13 09:19:00.772496
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    import pytest

    # Test with list of tags
    b = Block()
    t = Task()
    t.set_loader(b._loader)
    b.set_loader(b._loader)
    b._parent = t
    b.tags = ['tag1', 'tag2', 'tag3', 'tag4']
    # Case 1: no only_tags, no skip_tags; should run
    should_run = b.evaluate_tags(None, None, None)
    assert should_run == True
    # Case 2: only_tags = ['tag1']; should run
    should_run = b.evaluate_tags(['tag1'], None, None)
    assert should_run == True
    # Case 3: only_

# Generated at 2022-06-13 09:19:10.936190
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Tests the the method Taggable.evaluate_tags.
    It creates several objects of class Taggable and test that
    '''
    t = Taggable()
    assert t.evaluate_tags([], [], {}) == True

    t = Taggable()
    t._tags = ['never']
    assert t.evaluate_tags([], [], {}) == False

    t = Taggable()
    t._tags = ['always']
    assert t.evaluate_tags([], [], {}) == True

    t = Taggable()
    t._tags = ['always']
    assert t.evaluate_tags(['never'], [], {}) == False

    # The following is to test the case when the tag name is a template
    # The tag name must be in double quotes because the tag names are separated with comma
   

# Generated at 2022-06-13 09:19:25.000867
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Test belongs to class Taggable
    class TestItem:
        def __init__(self, tags):
            self.tags = tags

    # Data sets

# Generated at 2022-06-13 09:19:33.664110
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    obj.tags = ['tag1', 'tag2']
    assert obj.evaluate_tags(['tag1', 'tag2'], [], {}) == True
    assert obj.evaluate_tags(['tag1', 'tag2'], ['tag1'], {}) == True
    assert obj.evaluate_tags(['tag1', 'tag2'], ['tag2'], {}) == True
    assert obj.evaluate_tags(['tag1', 'tag2'], ['tag1', 'tag2'], {}) == False


# Generated at 2022-06-13 09:19:43.626270
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableDummy(Taggable):
        def __init__(self, tags=None):
            super(TaggableDummy, self).__init__()
            self.tags = tags


# Generated at 2022-06-13 09:19:54.392434
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Foo(Taggable):
        pass
    foo = Foo()

    only_tags = ['tag1']
    skip_tags = []
    all_vars = {}
    foo.tags = []
    assert foo.evaluate_tags(only_tags, skip_tags, all_vars)
    foo.tags = ['tag1']
    assert foo.evaluate_tags(only_tags, skip_tags, all_vars)
    foo.tags = ['tag2']
    assert not foo.evaluate_tags(only_tags, skip_tags, all_vars)
    foo.tags = ['tag2', 'tag1']
    assert foo.evaluate_tags(only_tags, skip_tags, all_vars)

    only_tags = ['tag1', 'tag2']
    foo.tags = ['tag1']

# Generated at 2022-06-13 09:20:04.809650
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeTaggable(Taggable):
        def __init__(self, tags=None):
            self._tags = tags
            self._loader = 'fake_loader'

    # test basic usage
    t = FakeTaggable(tags=['test'])
    assert t.evaluate_tags(only_tags=['test'], skip_tags=None, all_vars=dict())
    assert t.evaluate_tags(only_tags=None, skip_tags=['no_test'], all_vars=dict())
    assert not t.evaluate_tags(only_tags=['test'], skip_tags=['test'], all_vars=dict())
    assert not t.evaluate_tags(only_tags=['no_test'], skip_tags=None, all_vars=dict())

    # test only_tags '

# Generated at 2022-06-13 09:20:10.432018
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        def __init__(self):
            self._loader = None
            self._tags = {'a', 'b'}

    m = MyTaggable()
    all_vars = dict()
    assert m.evaluate_tags(['a', 'b'], ['c'], all_vars)
    assert m.evaluate_tags(['a', 'b'], ['c'], all_vars)
    assert not m.evaluate_tags(['c'], ['d'], all_vars)
    assert not m.evaluate_tags(['e'], ['f'], all_vars)

# Generated at 2022-06-13 09:20:20.148439
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeVarsClass(object):
        pass

    class FakeTaskClass(object):
        pass

    fake_vars = FakeVarsClass()
    fake_task = FakeTaskClass()

    taggable = Taggable()

    fake_task.tags = []
    only_tags = ['tag1', 'tag2', 'tag3']
    skip_tags = ['tag4', 'tag5']
    assert taggable.evaluate_tags(only_tags, skip_tags, fake_vars) == False

    fake_task.tags = ['tag1', 'tag2']
    only_tags = ['tag1', 'tag2', 'tag3']
    skip_tags = ['tag4', 'tag5']
    assert taggable.evaluate_tags(only_tags, skip_tags, fake_vars) == True

   

# Generated at 2022-06-13 09:21:26.140141
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    
    class TestTaggable(Taggable):
        pass
    test_Taggable = TestTaggable()
    test_Taggable._loader = None
    test_Taggable.tags = []
    
    assert not test_Taggable.evaluate_tags(only_tags = [], skip_tags = [], all_vars = {})
    assert test_Taggable.evaluate_tags(only_tags = ['tagged'], skip_tags = [], all_vars = {})
    assert not test_Taggable.evaluate_tags(only_tags = ['tagged'], skip_tags = ['tagged'], all_vars = {})
    
    test_Taggable.tags = ['ansible']

# Generated at 2022-06-13 09:21:40.329255
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    item = Taggable()
    all_vars = {'foo': 'bar'}

    item.tags = ['tag1', 'tag2']
    only_tags = ['tag3', 'tag4']
    skip_tags = ['tag1', 'tag2']
    should_run = item.evaluate_tags(only_tags, skip_tags, all_vars)
    assert not should_run

    item.tags = ['tag1', 'tag2']
    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag1', 'tag2']
    should_run = item.evaluate_tags(only_tags, skip_tags, all_vars)
    assert not should_run

    item.tags = ['tag1', 'tag2']
    only_tags = ['tag3', 'tag4']


# Generated at 2022-06-13 09:21:51.493624
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    task = Task()
    task.tags = ['always']

    # task with tag 'always' should run whenever we tell it to, regardless
    # of skip_tags and only_tags
    only_tags = ['foo', 'bar']
    skip_tags = ['foo', 'bar', 'baz']
    all_vars = dict()

    assert task.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars=all_vars) == True
    task.tags = ['never']
    assert task.evaluate_tags(only_tags=['always'], skip_tags=['never']) == True
    assert task.evaluate_tags(only_tags=['blah'], skip_tags=['blah']) == True
    task.tags

# Generated at 2022-06-13 09:22:01.751388
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Test skip_tags is not set
    t = Taggable()
    t.tags = 'tag1, tag2'
    assert t.evaluate_tags(only_tags = [], skip_tags = [], all_vars = {}) == True

    # Test only_tags is not set
    t = Taggable()
    t.tags = 'tag1, tag2'
    assert t.evaluate_tags(only_tags = [], skip_tags = ['all'], all_vars = {}) == False

    # Test only_tags and skip_tags are set
    t = Taggable()
    t.tags = 'tag1, tag2'
    assert t.evaluate_tags(only_tags = [], skip_tags = ['tag1', 'all'], all_vars = {}) == False

    # Test only_

# Generated at 2022-06-13 09:22:16.839070
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    a = Taggable()
    a.tags = ['a','b','c']

    only_tags = []
    skip_tags = []
    all_vars = {}

    # should_run with only_tags = [] and skip_tags = []
    assert a.evaluate_tags(only_tags, skip_tags, all_vars)

    # should_run with only_tags = [] and skip_tags = ['b']
    skip_tags = ['b']
    assert a.evaluate_tags(only_tags, skip_tags, all_vars)

    # should_run with only_tags = ['a'] and skip_tags = []
    only_tags = ['a']
    skip_tags = []
    assert a.evaluate_tags(only_tags, skip_tags, all_vars)

    # should_run with only

# Generated at 2022-06-13 09:22:28.183018
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.vars.manager import VariableManager

    p = Base()
    m = VariableManager()
    p.vars = m.get_vars(loader=None, play=p)

    t = Taggable()
    t.name = 'foobar'
    t.tags = ['tag1', 'tag2']

    # just tags
    assert t.evaluate_tags(['tag1'], [], p.vars)
    assert not t.evaluate_tags(['tag3'], [], p.vars)
    # skip_tags + tags
    assert not t.evaluate_tags([], ['tag2'], p.vars)
    # only_tags + skip_tags + tags

# Generated at 2022-06-13 09:22:36.755276
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
  
    temporary_ansible_module = __import__('ansible.playbook.task')
    class task_test(temporary_ansible_module.playbook.task.Task):
        def __init__(self, my_tags=None, *args, **kwargs):
            super(temporary_ansible_module.playbook.task.Task, self).__init__(*args, **kwargs)
            self._tags = my_tags
            if self._tags is None:
                self._tags = []

    # This name is used to create a new task.
    # This test was created because the name was not defined and we had to mock it
    # later.
    fake_name = "my_fake_name"
    fake_only_tags = ["A", "B"]
    fake_skip_tags = []

    # Test

# Generated at 2022-06-13 09:22:42.255137
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    # Create a Taggable instance
    t = Task()
    # Create an empty dict for all variables
    all_vars = dict()
    # Test with default values
    assert t._load_tags('tags', list()) == list()
    assert t._load_tags('tags', 'foo,bar') == ['foo', 'bar']
    assert t.evaluate_tags(list(),list(),all_vars) == True
    # Test with values provided by user
    t.tags = ['foo']
    assert t.evaluate_tags(list(),list(),all_vars) == True
    t.tags = ['foo','bar']

# Generated at 2022-06-13 09:22:51.619796
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest2 as unittest
    class TestTaggable(Taggable):
        def __init__(self):
            self._tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)
        @property
        def tags(self):
            return self._tags
        @tags.setter
        def tags(self, value):
            self._tags = value
        def _load_tags(self, attr, ds):
            return self._tags

    class Test_Taggable(unittest.TestCase):
        def test_normal(self):
            only_tags = ['test']
            t = TestTaggable()
            t.tags = ['test']
            ret = t.evaluate_tags(only_tags, [], {})
            assert ret == True

# Generated at 2022-06-13 09:22:59.594480
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    :type self: Taggable
    '''

    t = Taggable()

    t._tags = ['tag1', 'tag2']
    assert t.evaluate_tags(['tag1'], [], {})
    assert not t.evaluate_tags(['tag3'], [], {})

    t._tags = []
    assert t.evaluate_tags([], ['tag1'], {})
    assert t.evaluate_tags([], ['never'], {})
    assert not t.evaluate_tags([], ['untagged'], {})
    assert t.evaluate_tags(['untagged'], [], {})
    assert t.evaluate_tags(['untagged'], ['never'], {})
    assert t.evaluate_tags(['untagged'], ['tag1'], {})
    assert not t.evaluate