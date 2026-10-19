

# Generated at 2022-06-13 09:13:23.025572
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    assert Taggable().evaluate_tags(only_tags=['foo'], skip_tags=['bar'], all_vars={}) == False

    assert Taggable(tags=['foo']).evaluate_tags(only_tags=['foo'], skip_tags=[''], all_vars={}) == True
    assert Taggable(tags=['foo']).evaluate_tags(only_tags=['foo'], skip_tags=[''], all_vars={}) == True
    assert Taggable(tags=['foo']).evaluate_tags(only_tags=[], skip_tags=['bar'], all_vars={}) == True
    assert Taggable(tags=['foo']).evaluate_tags(only_tags='foo', skip_tags='bar', all_vars={}) == True

# Generated at 2022-06-13 09:13:30.520538
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Default value of only_tags and skip_tags is empty, so return value should be True.
    only_tags = []
    skip_tags = []
    all_vars = None
    item = Taggable()
    assert True == item.evaluate_tags(only_tags, skip_tags, all_vars)

    # Testing case with value of list only_tags having one item and skip_tags having no items.
    # This should return True since tags of item is always empty.
    only_tags = ['tag1']
    skip_tags = []
    all_vars = None
    item = Taggable()
    assert True == item.evaluate_tags(only_tags, skip_tags, all_vars)

    # Testing case with value of list skip_tags having one item and skip_tags having no items.
    # This should

# Generated at 2022-06-13 09:13:39.938019
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    import ansible.constants as C
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    all_vars = HostVars({"id": 12345, "color": "blue", "flavor": "tea"})
    templar = Templar(loader=None, variables=all_vars)

    # test Block
    block = Block()
    block._role = lambda: None
    block._role.get_path = lambda: None
    block._role.get_name = lambda: 'myrole'

    block.role = 'myrole'
    block.hosts = ['host1', 'host2']

# Generated at 2022-06-13 09:13:51.987337
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestTaggable(Taggable):
        def __init__(self, tags=None, only_tags=None, skip_tags=None,
                     all_vars=None):

            # Skip the __init__ of base class Taggable
            # Taggable.__init__(self, **kwargs)
            pass

            self._tags = tags

            self.run_if_conditional = self.evaluate_tags(only_tags, skip_tags,
                                                         all_vars)

    # Test case 1: when all_vars is None
    test_task = TestTaggable(tags=['a', 'b'], only_tags=['a', 'b', 'c'],
                             skip_tags=[], all_vars=None)
    assert test_task.run_if_conditional is True



# Generated at 2022-06-13 09:14:03.322226
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyItem:
        def __init__(self, tags):
            self.tags = tags
        def __repr__(self):
            return 'DummyItem(%s)' % repr(self.tags)

    from ansible.parsing.yaml.objects import AnsibleUnicode

    import unittest

    class TestTaggable(unittest.TestCase):
        def test_empty(self):
            tags = []
            only = []
            skip = []
            item = DummyItem(tags)
            self.assertTrue(Taggable.evaluate_tags(item, only, skip))

        def test_run_if_not_tagged(self):
            tags = []
            only = ['tagged']
            skip = []
            item = DummyItem(tags)

# Generated at 2022-06-13 09:14:05.496276
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass

# Generated at 2022-06-13 09:14:15.752872
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest

    class TestTaggable(Taggable):
        pass

    class TestTaggable_evaluate_tags(unittest.TestCase):

        def setUp(self):
            self.t = TestTaggable()

        def test_evaluate_tags_all_tags(self):
            self.t.tags = ['tag1', 'tag2']
            ret = self.t.evaluate_tags(only_tags=['tag1', 'tag2'], skip_tags=[], all_vars={})
            self.assertEqual(ret, True)

        def test_evaluate_tags_always(self):
            self.t.tags = ['always']
            ret = self.t.evaluate_tags([], ['never'], {})
            self.assertEqual(ret, True)


# Generated at 2022-06-13 09:14:25.064608
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    import ansible.playbook.base

    class mock_Taggable(Taggable):
        ''' Class to mock Taggable so that its method evaluate_tags can be tested'''

        def __init__(self):
            self._tags = []
            self._loader = None

    # Try with '_tags' empty
    obj = mock_Taggable()
    res = obj.evaluate_tags([], [], {})
    assert res == True

    # Try with '_tags' not empty
    obj = mock_Taggable()
    obj._tags = ['testTag1', 'testTag2', 'testTag3']
    res = obj.evaluate_tags([], [], {})
    assert res == True

    # Try with 'only_tags' given and '_tags' empty
    obj

# Generated at 2022-06-13 09:14:33.467836
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestObj(Taggable):
        def __init__(self):
            self.tags = []

    test_obj = TestObj()

    test_obj.tags = ['tag_A']
    assert test_obj.evaluate_tags(['tag_A'], [], {})
    assert not test_obj.evaluate_tags([], ['tag_A'], {})
    assert not test_obj.evaluate_tags(['tag_B'], [], {})
    assert test_obj.evaluate_tags(['tag_B'], ['tag_A'], {})

    test_obj.tags = ['tag_A', 'tag_B']
    assert test_obj.evaluate_tags(['tag_A'], [], {})
    assert test_obj.evaluate_tags(['tag_B'], [], {})

# Generated at 2022-06-13 09:14:39.980210
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    play_context = PlayContext()
    play_context.tags = ['all']
    play = Play()
    play._play_context = play_context

    task = Task()
    task._parent = play

    # 1.
    # default, task should run
    task.tags = ['all']
    assert task.evaluate_tags() is True

    # 2.
    # only_tags = ['all'], task should run
    play_context.only_tags = ['all']
    task = Task()
    task._parent = play
    task.tags = ['all']
    assert task.evaluate_tags() is True

    # 3.
    # only_tags = ['

# Generated at 2022-06-13 09:14:56.236916
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' Unit tests for method evaluate_tags of class Taggable '''

    test_item = Taggable()
    test_item.tags = ['all', 'any', 'never']
    all_vars = dict()

    # Should run only when the tag 'all' is specified
    assert True == test_item.evaluate_tags(['all'], [], all_vars)

    # Should always run when the tag 'always' is specified
    test_item.tags = ['all', 'any', 'never', 'always']
    assert True == test_item.evaluate_tags(['all'], [], all_vars)

    # Skip when the tag 'never' is specified
    assert False == test_item.evaluate_tags(['all'], ['never'], all_vars)

    # Skip when the tag 'none' is specified

# Generated at 2022-06-13 09:15:08.557282
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):
        def __init__(self):
            self.tags = []
            self._loader = None
            self._pos = 0

    # test data
    only_tags = 'tag1,tag2'
    skip_tags = 'tag3'
    only_tags_list = ['tag1', 'tag2']
    skip_tags_list = ['tag3']
    all_vars = {}
    always_tags = ['always']
    never_tags = ['never']

    # Test 1: Test tagged item, with all and tagged
    my_taggable = MyTaggable()
    my_taggable.tags = ['tag1']
    my_taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert my_taggable.tags

# Generated at 2022-06-13 09:15:20.279678
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play import Play
    playbook = Play()
    playbook.hosts = "localhost"
    playbook.name = "Foo Play"
    playbook.tags = ['bar']

    task = Task()
    task.action = 'foo'
    task.args = {}
    task.tags = ['bar']

    # Test case where only_tags is an empty list
    result = task.evaluate_tags([], ['never'], None)
    assert result == True

    # Test case where only_tags is a list containing strings
    result = task.evaluate_tags(['foo', 'bar'], [], None)
    assert result == True
    result = task.evaluate_tags(['foo', 'bar', 'foobar'], [], None)
    assert result == False

# Generated at 2022-06-13 09:15:27.566545
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.parsing.dataloader
    from ansible.playbook.role import Role
    loader = ansible.parsing.dataloader.DataLoader()

    # Build the all_vars dictionary, which is the first argument of evaluate_tags
    # This dictionary is used to replace data in templates
    all_vars = {}

    # Build the Taggable class. This is the class that contains the method
    # evaluate_tags.
    role = Role()
    role._loader = loader

    # Test 1. Check if wrong input types are not accepted
    # Wrong type for element of list. Check if string_types is accepted
    # and if not, check if AnsibleError is raised

# Generated at 2022-06-13 09:15:37.814652
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeTask(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = None

    task = FakeTask()
    task.tags = ['tag1', 'tag2']

    # default tags are always run
    assert task.evaluate_tags(None, None, None)

    # if we only want tagged tasks and we have tags, run
    assert task.evaluate_tags(['tagged'], None, None)

    # if we only want a different tag, don't run
    assert not task.evaluate_tags(['foo'], None, None)

    # but if we only want a different tag, don't run
    assert task.evaluate_tags(['foo', 'bar'], None, None)

    # but if we only want a different tag and we have two tags, do run
    assert task

# Generated at 2022-06-13 09:15:53.376927
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = None

    class TestClass2(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = None
            self.task = None

    assert TestClass().evaluate_tags([], [], {}) # test default, no tag options, no tags
    assert TestClass().evaluate_tags([], ['notatag'], {}) # test default, skip tags does not match
    assert TestClass().evaluate_tags(['notatag'], [], {}) # test default, only tags does not match
    assert TestClass2().task # TestClass2, unlike TestClass, has a task variable

    test_obj = TestClass()

# Generated at 2022-06-13 09:16:03.572776
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook import Play

    play = Play()
    only_tags = ['a', 'b']
    skip_tags = ['c', 'd']
    all_vars = {}

    # 1.
    # tags: none
    # result: 1
    assert play.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars=all_vars) is True

    # 2.
    # tags: ['c']
    # result: 1
    play = Play(tags=['c'])
    assert play.evaluate_tags(only_tags=only_tags, skip_tags=skip_tags, all_vars=all_vars) is True

    # 3.
    # tags: ['a']
    # result: 0

# Generated at 2022-06-13 09:16:13.240682
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """
    Unit test for method evaluate_tags of class Taggable
    """

    obj = Taggable()
    obj.tags = ['test']
    only_tags = set(['all'])
    skip_tags = set()
    all_vars = []
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars) == True

    obj = Taggable()
    obj.tags = ['test']
    only_tags = set(['always'])
    skip_tags = set()
    all_vars = []
    assert obj.evaluate_tags(only_tags, skip_tags, all_vars) == True

    obj = Taggable()
    obj.tags = ['test']
    only_tags = set(['tagged'])
    skip_tags = set()
    all_

# Generated at 2022-06-13 09:16:24.341454
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # This test case is to check tag values are incorrect, so it should raise an exception.
    # case 1
    item1 = Taggable()
    item1.tags = 1 #here tags value should be a list, but we input it as a int
    all_vars1 = dict()
    try:
        result1 = item1.evaluate_tags(tags=["tag1"], skip_tags=["tag2"], all_vars=all_vars1)
    except AnsibleError:
        result1 = False
    assert result1 is False, "evaluate_tags method test case #1 failed"

    # This test case is to check tag values are correct, so it should be success.
    # case 2
    item2 = Taggable()
    item2.tags = ["tag1"]
    all_vars2 = dict()

# Generated at 2022-06-13 09:16:30.749305
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Dummy(Taggable):
        def __init__(self, tags, only_tags=[], skip_tags=[]):
            self.tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags

        def __call__(self):
            return self.evaluate_tags(self.only_tags, self.skip_tags, {})

    assert Dummy([], [], [])(), 'default tasks with both empty lists of tags should run'
    assert not Dummy([], ['all'], [])(), 'skip all tasks with empty list of tags'
    assert not Dummy([], ['tagged'], [])(), 'skip tagged tasks with empty list of tags'
    assert Dummy(['all'], ['all'], [])(), 'run all tasks with <all> in list of tags'
   

# Generated at 2022-06-13 09:16:58.549937
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Verify the run result of evaluate_tags when only_tags has 'test' and skip_tags has 'test'
    items = Taggable()
    setattr(items, 'tags', ['test'])
    result = items.evaluate_tags('test', 'test', {})
    assert result == False

    # Verify the run result of evaluate_tags when only_tags has 'test' and skip_tags has 'skip'
    items = Taggable()
    setattr(items, 'tags', ['skip'])
    result = items.evaluate_tags('test', 'skip', {})
    assert result == False

    # Verify the run result of evaluate_tags when only_tags has 'test' and skip_tags has 'skip' and tags has 'test' and 'skip'
    items = Taggable()

# Generated at 2022-06-13 09:17:09.409145
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    class TestTaggable(Taggable):
        def __init__(self):
            super(TestTaggable, self).__init__()
            self._tags = ['test_tag1']

    test_taggable = TestTaggable()
    assert test_taggable.evaluate_tags(['test_tag1'], None, None)
    assert test_taggable.evaluate_tags(['test_tag1'], ['test_tag1'], None)
    assert not test_taggable.evaluate_tags(None, ['test_tag1'], None)
    assert test_taggable.evaluate_tags(None, None, None)
    assert test_taggable.evaluate_tags(None, ['test_tag2'], None)

# Generated at 2022-06-13 09:17:21.477592
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    fake_only_tags = ['tag1','tag2','tag3','tag4','tag5']
    fake_skip_tags = ['tag1','tag2','tag3']
    fake_tags = ['tag1','tag5']
    class FakeClass(Taggable):
        def __init__(self):
            self.tags = fake_tags;
    f = FakeClass()
    # only_tags is empty, skip_tags is empty
    res = f.evaluate_tags([], [], {})
    assert res == True

    # only_tags is empty, skip_tags is not empty
    res = f.evaluate_tags([], fake_skip_tags, {})
    assert res == True

    # only_tags is not empty, skip_tags is empty

# Generated at 2022-06-13 09:17:30.925886
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class MyTaggable(Taggable, Base):
        _valid_attrs = frozenset(['tags'])

    # Test simple tag
    taggable = MyTaggable()
    taggable.tags = ['tag-1']
    print(taggable.tags)
    assert taggable._load_tags(None, taggable.tags) == ['tag-1']
    assert taggable.evaluate_tags(['tag-1'], [], VariableManager())
    assert not taggable.evaluate_tags([], ['tag-1'], VariableManager())

    # Test sequence tag
    taggable = MyTaggable()

# Generated at 2022-06-13 09:17:35.240426
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Note: As the Taggable class is not instantiated, this unit test can only check the
    #       return value of the evaluate_tags method.
    #       Therefore the method is tested with different variations of input parameters
    #       where the expected return value can be defined.

    # As only one return value can be defined, this case is tested as one item list
    # with tags only and always.
    assert Taggable.evaluate_tags(['only_tags'], ['skip_tags'], {'only_tags': ['tag1', 'tag2', 'always'],
                                                                  'skip_tags': ['skip1', 'skip2']}) is True

# Generated at 2022-06-13 09:17:39.121085
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task

    task = Task()
    task.tags = ['tag_a', 'tag_b']
    task.evaluate_tags(['tag_a'],['tag_c'], dict())
    assert True

# Generated at 2022-06-13 09:17:50.778679
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task_include import TaskInclude
    try:
        class MyTask(Taggable, TaskInclude):
            pass
    except Exception as e:
        assert False, 'Could not create class'

    test_subject = MyTask()

    try:
        test_subject.tags = ['test_tag', 'tag2']
    except Exception as e:
        assert False, 'Could not set tags'

    assert(test_subject.evaluate_tags(['tag1', 'tag2'], [], {}) == True)

    assert(test_subject.evaluate_tags(['tag3'], [], {}) == False)

    assert(test_subject.evaluate_tags([], ['tag1'], {}) == False)


# Generated at 2022-06-13 09:18:05.346183
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']


# Generated at 2022-06-13 09:18:16.860862
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.template import Templar

    # test class without tags
    class MyPlayTest(Play):
        pass
    my_play = MyPlayTest.load({'hosts': 'all'})
    # test with empty tags option
    assert my_play.evaluate_tags([], [], {}) is True
    # test with only_tags option without any tag
    assert my_play.evaluate_tags(['all'], [], {}) is True
    assert my_play.evaluate_tags(['tagged'], [], {}) is True
    assert my_play.evaluate_tags(['notags'], [], {}) is False
    # test with skip tags options

# Generated at 2022-06-13 09:18:23.218249
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyTaggable(Taggable):
        def __init__(self):
            self._tags = set()
    # Check that evaluate_tags returns True if we want to execute all tasks
    dummy_taggable = DummyTaggable()
    assert dummy_taggable.evaluate_tags(only_tags=None, skip_tags=None, all_vars=None) == True

    # Check that evaluate_tags returns True if we have only_tags == all
    dummy_taggable = DummyTaggable()
    dummy_taggable.tags = set(['some-tag'])
    assert dummy_taggable.evaluate_tags(only_tags={'all'}, skip_tags=None, all_vars=None) == True

    # Check that evaluate_tags returns False if we have only_tags == all but

# Generated at 2022-06-13 09:18:47.419018
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping

    class MyTaggable(Taggable):

        def __init__(self, ds):
            self._ds = ds

    # data structure for tagable item
    class MyDS(object):
        pass

    # helper to instantiate tagable items with provided data structure
    def create_taggable(ds):
        my_taggable = MyTaggable(ds)
        return my_taggable

    # list of test unit: (taggable_ds, only_tags, skip_tags, all_vars, expected)
    # where taggable_ds is the data structure representing the taggable item

# Generated at 2022-06-13 09:18:57.751210
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class test_subject(Taggable):
        def __init__(self, tags):
            self.tags = tags

    # empty tags
    t = test_subject([])
    assert t.evaluate_tags([], [], [])
    assert t.evaluate_tags(['all'], [], [])
    assert t.evaluate_tags([], ['all'], [])
    assert t.evaluate_tags(['all'], ['all'], [])
    assert not t.evaluate_tags(['all'], ['all', 'always'], [])
    assert not t.evaluate_tags([], ['all', 'never'], [])
    assert not t.evaluate_tags(['untagged'], ['all'], [])
    assert not t.evaluate_tags(['tagged'], ['all'], [])

# Generated at 2022-06-13 09:19:01.333218
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest
    assert(False), "fix test_Taggable_evaluate_tags"
    return None

# I made this function up to ensure tests are always run using "unit"
# and not "component" so we can avoid potential side-effects and
# dependencies.

# Generated at 2022-06-13 09:19:08.538181
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class DummyParent(Taggable):
        pass

    # Tags passed as list to constructor
    parent = DummyParent(dict(tags=['active','inactive']))
    assert parent.tags == ['active','inactive']
    assert parent.evaluate_tags(only_tags=['active'], skip_tags=[]) == True
    assert parent.evaluate_tags(only_tags=['tagged'], skip_tags=[]) == True
    assert parent.evaluate_tags(only_tags=['active'], skip_tags=['active']) == False
    assert parent.evaluate_tags(only_tags=['active'], skip_tags=['inactive']) == True
    assert parent.evaluate_tags(only_tags=['inactive'], skip_tags=['active']) == True

    # Test some edge cases
    assert parent.evaluate

# Generated at 2022-06-13 09:19:17.847432
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableMock(Taggable):
        pass
    # only_tags, skip_tags, tags, expected

# Generated at 2022-06-13 09:19:24.025490
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    import pytest

    test_task = Task()

    test_task._play_context = {}

    test_task.action = 'debug'
    test_task.tags = ['always']

    assert test_task.evaluate_tags(only_tags = [], skip_tags = []) == True
    assert test_task.evaluate_tags(only_tags = ['always'], skip_tags = []) == True
    assert test_task.evaluate_tags(only_tags = ['whatever'], skip_tags = []) == True
    assert test_task.evaluate_tags(only_tags = [], skip_tags = ['always']) == False
    assert test_task.evaluate_tags(only_tags = ['always'], skip_tags = ['always']) == False

    test_task.tags

# Generated at 2022-06-13 09:19:36.438037
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    vars_manager = VariableManager()
    vars_manager.extra_vars = {'foo': 'bar'}

    t = Task()
    t._vars_manager = vars_manager

    assert t.evaluate_tags(['foo', 'bar'], [], {})
    assert t.evaluate_tags(['foo', 'bar'], ['baz'], {})
    assert t.evaluate_tags(['foo', 'bar'], ['foo'], {})

# Generated at 2022-06-13 09:19:44.877549
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    fakeplaybook = get_fakeplaybook(dict(
        hosts='all',
        remote_user='root',
        gather_facts='no',
        tasks=[dict(action=dict(module='shell', args='/bin/true', tags=['always']))],
        any_errors_fatal=False,
        tags=['x'],
        ignore_errors=False,
    ))
    failed = False
    try:
        fakeplaybook.evaluate_tags(only_tags=['y'], skip_tags=[])
    except AnsibleError as e:
        failed = e.message == 'A task includes tags which is not defined in tags play option'
    assert failed, 'should have failed'


# Generated at 2022-06-13 09:19:55.438127
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestObj(Taggable):
        def __init__(self, tags):
            self.tags = tags

    t1 = TestObj(['a', 'b', 'c'])
    assert t1.evaluate_tags(None, None, {})
    assert t1.evaluate_tags(None, ['a'], {})
    assert t1.evaluate_tags(['a'], None, {})
    assert not t1.evaluate_tags(['a'], ['a'], {})

    assert not t1.evaluate_tags(['a'], ['b', 'c'], {})
    assert not t1.evaluate_tags(['a'], ['b'], {})
    assert t1.evaluate_tags(['a'], ['d'], {})

# Generated at 2022-06-13 09:20:05.361082
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext

    class MyTaggable(Taggable):
        def __init__(self, tags=None, all_vars=None):
            self.tags = tags
            self.all_vars = all_vars

    # define all_vars
    all_vars = dict(
        a=dict(
            b=dict(
                c=1
            )
        )
    )

    # test when only_tags is defined
    task = MyTaggable(tags=["a", "b"], all_vars=all_vars)
    assert task.evaluate_tags(only_tags = ["b"], skip_tags=None, all_vars=all_vars)

# Generated at 2022-06-13 09:20:29.713734
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable().evaluate_tags(set(['tag1']), set(['tag2']), {}) == True


# Generated at 2022-06-13 09:20:39.376821
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    from ansible.playbook.task import Task
    from ansible.playbook.conditional import Conditional

    class FakeVs(object):
        def __init__(self, v):
            self.all_vars = dict(my_tag=v, skip_tags=[], untagged=AnsibleUnicode('untagged'))

    # Check that tasks with no tags are run by default.
    vs1 = FakeVs(['other_tag'])
    t1 = Task()
    t1.tags = []
    assert t1.evaluate_tags([], [], vs1.all_vars)
    vs2 = FakeVs(['other_tag'])
    t2 = Conditional()
    t2.tags = []
    assert t2

# Generated at 2022-06-13 09:20:52.390510
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable().evaluate_tags(['all'], [], {}) is True
    assert Taggable().evaluate_tags([], ['all'], {}) is True
    assert Taggable().evaluate_tags(['all'], ['all'], {}) is False
    assert Taggable().evaluate_tags(['foo'], [], {}) is False
    assert Taggable().evaluate_tags([], ['foo'], {}) is True
    assert Taggable().evaluate_tags(['foo'], ['foo'], {}) is False
    assert Taggable().evaluate_tags(['foo'], ['bar'], {}) is False
    assert Taggable().evaluate_tags(['all'], [], {'tags': ['foo']}) is False

# Generated at 2022-06-13 09:21:03.092158
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    base = Base()
    assert (base.evaluate_tags(None, None, None) == True)
    assert (base.evaluate_tags(["a", "b"], None, None) == False)
    assert (base.evaluate_tags(["a", "b", "all"], ["c", "d"], None) == True)
    assert (base.evaluate_tags(["a", "b", "all"], ["a", "d"], None) == False)
    assert (base.evaluate_tags(["a", "b", "all"], ["c"], None) == True)
    assert (base.evaluate_tags(None, ["c", "d"], None) == True)
    assert (base.evaluate_tags(None, ["all"], None) == False)

# Generated at 2022-06-13 09:21:12.715468
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import pytest

    t = Taggable()
    result = t.evaluate_tags({'always', 'never'}, {}, {})
    assert result is True
    result = t.evaluate_tags({}, {'always', 'never'}, {})
    assert result is False
    result = t.evaluate_tags({'always'}, {}, {})
    assert result is True
    result = t.evaluate_tags({'always'}, {'always'}, {})
    assert result is False
    result = t.evaluate_tags({'never'}, {'never'}, {})
    assert result is False
    result = t.evaluate_tags({}, {'never'}, {})
    assert result is True
    result = t.evaluate_tags({'never'}, {}, {})
    assert result is True
    result = t.evaluate

# Generated at 2022-06-13 09:21:24.248954
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest

    class MyTaggable(Taggable):
        def __init__(self, tags=None):
            self._tags = tags or []

    # If a task has no tags, it should always run
    task = MyTaggable()
    assert task.evaluate_tags(only_tags=None, skip_tags=None, all_vars={}) is True

    # If only_tags is None, the task should always run
    task = MyTaggable(tags=['foo'])
    assert task.evaluate_tags(only_tags=None, skip_tags=None, all_vars={}) is True

    # If both only_tags and skip_tags are empty sets, the task should always run
    task = MyTaggable(tags=['foo'])

# Generated at 2022-06-13 09:21:38.726839
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    test_class = Taggable()
    test_class.tags = [u'stuff']

    assert test_class.evaluate_tags([u'always', u'stuff'], [], {})
    assert test_class.evaluate_tags([u'always', u'stuff'], [], {})
    assert test_class.evaluate_tags([u'always', u'stuff'], [u'tag'], {})

    assert test_class.evaluate_tags([], [u'tag', u'nonexist'], {})
    assert test_class.evaluate_tags([], [u'tag', u'stuff'], {})

    assert not test_class.evaluate_tags([u'other', u'tag'], [], {})

# Generated at 2022-06-13 09:21:44.511077
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook import Play
    from ansible.playbook.play import Play as Play_obj

    play_obj = Play({'id': 'play_id', 'playbook': 'playbook'})
    play = Play_obj.load(play_obj, loader=None, variable_manager=None)

    task = play.task_blocks[0].block[0]

    # Test 1
    tags = ['tag1', 'tag2', 'tag3']
    task.tags = tags
    task.evaluate_tags(only_tags=['tag2'], skip_tags=[], all_vars={})
    assert task.tags == ['tag1', 'tag2', 'tag3']

    # Test 2
    tags = 'tag1, tag2 , tag3'
    task.tags = tags

# Generated at 2022-06-13 09:21:51.779442
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # we want to test the entire method, and all its possible branches
    # see if the returned boolean is always the right one
    # this is, of course, very hard
    # we can only test the returned boolean with what we know
    # and assume that the methods isdisjoint, set, list and str will work as intended
    # the only things we can test ourselves, is the evaluation of the boolean
    pass

# Generated at 2022-06-13 09:22:01.944020
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    test_only_tags = ['tagged']
    test_skip_tags = ['never']
    test_all_vars = dict(vars_1='vars_1_value', vars_2='vars_2_value', vars_3='vars_3_value')
    test_template_string = "{{ vars_1 }}"
    test_template_result = 'vars_1_value'

    test_Taggable = Taggable()

    templar = Templar(loader=None, variables=test_all_vars)
    test_Taggable.tags = templar.template(test_template_string)


# Generated at 2022-06-13 09:22:53.186832
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableClass:
        def __init__(self):
            self.tags = []

    test_object = TaggableClass()

    # case 1: no tags and no skip_tags. The method should return True
    assert test_object.evaluate_tags([], [], None)

    # case 2: no tags and only_tags contains a tag. The method should return False
    assert not test_object.evaluate_tags(['mytag'], [], None)

    # case 3: no tags and only_tags contains 'all'. The method should return True
    assert test_object.evaluate_tags(['all'], [], None)

    # case 4: no tags and only_tags contains 'all' and 'tagged'. The method should return False

# Generated at 2022-06-13 09:23:01.160327
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MockTaggable(Taggable):

        def __init__(self, tags):
            self.tags = tags

        def _get_fields(self):
            return ['tags']
    mock_taggable = MockTaggable(tags=['tag1', 'tag2'])

    # Should return true for an empty only_tags and skip_tags tag list
    assert mock_taggable.evaluate_tags([], [], {})

    # Should return true for an empty only_tags list and only_tags={'tag1', 'tag2'}
    assert mock_taggable.evaluate_tags([], ['tag1', 'tag2'], {})

    # Should return true for an empty only_tags list and skip_tags={'tag1'}

# Generated at 2022-06-13 09:23:11.285584
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # class to test
    class Taggable(Taggable):
        def __init__(self, tags=None, only_tags=None, skip_tags=None, all_vars=None, _loader=None):
            self.tags = tags
            self.only_tags = only_tags
            self.skip_tags = skip_tags
            self.all_vars = all_vars
            self._loader = _loader
            super(Taggable, self).__init__()
    # test cases