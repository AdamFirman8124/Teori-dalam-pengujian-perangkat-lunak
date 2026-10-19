

# Generated at 2022-06-13 09:13:20.973177
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import PlaybookBase
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    def reset_Taggable(self):
        self.tags = None
        self.untagged = frozenset(['untagged'])

    PlaybookBase.tags = None
    PlaybookBase.untagged = frozenset(['untagged'])
    PlaybookBase.reset_Taggable = reset_Taggable.__get__(PlaybookBase)
    PlayContext.reset_Taggable = reset_Taggable.__get__(PlayContext)
    Task.reset_Taggable = reset_Taggable.__get__(Task)

    # Test case 1 - Set some task tags and check execution
    PlaybookBase.reset_Taggable()

# Generated at 2022-06-13 09:13:29.280317
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Check if tag is not excluded
    a= Taggable()
    a.tags = ['some_tag']
    assert a.evaluate_tags(only_tags=None, skip_tags=None, all_vars={})
    # Check if tag is excluded from list
    assert not a.evaluate_tags(only_tags=['some_tag_2'], skip_tags=None, all_vars={})
    # Check if tag is excluded as "all"
    assert not a.evaluate_tags(only_tags=['all'], skip_tags=['some_tag'], all_vars={})
    # Check if tag is excluded as "all" but forced in
    assert a.evaluate_tags(only_tags=['all', 'some_tag'], skip_tags=['some_tag'], all_vars={})




# Generated at 2022-06-13 09:13:29.936077
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    pass

# Generated at 2022-06-13 09:13:35.203162
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    assert not t.evaluate_tags(['foo'], ['bar'], {})
    assert t.evaluate_tags(['foo', 'bar'], [], {})
    assert t.evaluate_tags([], ['bar'], {})
    assert not t.evaluate_tags(['bar'], ['foo'], {})


# Generated at 2022-06-13 09:13:43.049613
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    import sys
    import StringIO

    ############################################################################
    # Test Playbook
    ############################################################################

    # test playbook

# Generated at 2022-06-13 09:13:57.470318
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Create a taggable object
    class TaggableClass(Taggable):
        """ Class for unit testing purpose"""
        pass

    taggable_obj = TaggableClass()

    # Test with only_tags = ['tagged']
    taggable_obj.tags = []
    result = taggable_obj.evaluate_tags(['tagged'], [], {})
    assert result == False

    # Test with only_tags = ['tagged', 'web']
    taggable_obj.tags = ['web']
    result = taggable_obj.evaluate_tags(['tagged', 'web'], [], {})
    assert result == True

    # Test with only_tags = ['tagged', 'web', 'database']
    taggable_obj.tags = ['web']
    result = taggable_

# Generated at 2022-06-13 09:14:12.032463
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = {'tag1', 'tag2'}
    skip_tags = {'tag3', 'tag4'}
    all_vars = {}
    task = Taggable()
    #1. When task include tag1, tag2 and tag3
    task.tags = [ 'tag1', 'tag2', 'tag3' ]
    assert task.evaluate_tags(only_tags, skip_tags, all_vars) == False
    #2. When task includes tag1 and tag2
    task.tags = [ 'tag1', 'tag2' ]
    assert task.evaluate_tags(only_tags, skip_tags, all_vars) == True
    #3. When task includes tag3 and tag4
    task.tags = [ 'tag3', 'tag4' ]

# Generated at 2022-06-13 09:14:17.106859
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    t.tags = []
    only_tags = ['foo']
    skip_tags = []
    all_vars = {}
    should_run = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert should_run == False

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "-rx", __file__])

# Generated at 2022-06-13 09:14:29.161540
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        pass

    only_tags  = ['A']
    skip_tags  = ['B']
    all_vars   = {}
    # Default tag 'tags' of MyTaggable is empty, which will be evaluated to 'untagged'
    assert MyTaggable().evaluate_tags(only_tags, skip_tags, all_vars) == True

    class MyTaggable1(Taggable):
        _tags = ['always']

    all_vars   = {}
    # 'always' will make the task to be evaluated to True for certain, even though 'tags' is empty
    assert MyTaggable1().evaluate_tags(only_tags, skip_tags, all_vars) == True

    class MyTaggable2(Taggable):
        _tags = ['never']

# Generated at 2022-06-13 09:14:38.567292
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()
    # TODO: move this to test/utils/tag/tag_spec.json.
    #       Right now, it is difficult to implement the same
    #       test logic for test/units/parsing/parser_unittest.py.
    #
    # The following test logic is from test/units/parsing/parser_unittest.py
    #
    tag_entry = {
        'action': {
            'task': 'include_role',
            'args': {
                'name': 'common'
            },
            'tags': [
                'tagged'
            ]
        },
        'results': {
            'skipped': False,
        }
    }

# Generated at 2022-06-13 09:14:54.847520
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTaggable(Taggable):
        pass

    myMockTaggable = MockTaggable()
    myMockTaggable.tags = ["tag1", "tag2"]

    # We only want to run tasks tagged with 'tag1' or 'tag2', and skip those tagged with 'skip_tag1' or 'skip_tag2'
    only_tags = ['tag1','tag2']
    skip_tags = ['skip_tag1','skip_tag2']

    result = myMockTaggable.evaluate_tags(only_tags, skip_tags, None)

    # We expect the method to return True because the task is tagged with tag1 or tag2
    assert result == True


# Generated at 2022-06-13 09:15:07.225608
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Taggable_obj(Taggable):
        pass

    t = Taggable_obj(tags=['tagA', 'tagB'])
    res = t.evaluate_tags(only_tags=['tagA'], skip_tags=['tagB'], all_vars=dict())
    assert res == True

    t = Taggable_obj(tags=['tagA', 'tagB'])
    res = t.evaluate_tags(only_tags=['tagB'], skip_tags=['tagA'], all_vars=dict())
    assert res == False

    t = Taggable_obj(tags=['tagA', 'tagB'])
    res = t.evaluate_tags(only_tags=['tagA'], skip_tags=['tagC'], all_vars=dict())
    assert res

# Generated at 2022-06-13 09:15:18.974360
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import os
    from ansible.compat.six import StringIO
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    work_dir = os.path.dirname(os.path.realpath(__file__))
    play = Play.load(StringIO('''
- hosts: all
  gather_facts: False
  tasks:
    - shell: echo "Hello world"
      tags:
        - always
        - test
        - '{{ "test" }}'
      when: False
'''), loader=None, variable_manager=None)
    play_context = PlayContext(play=play)
    assert play_context.only_tags == set()
    assert play_context.skip_tags == set()
   

# Generated at 2022-06-13 09:15:29.440865
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Define a class that inherits from Taggable
    class MyClass(Taggable):
        def __init__(self):
            self.tags = ["tag1", "tag2"]

    # Define a MyClass object
    myObj = MyClass()
    all_vars = {}

    # Case one:
    '''
    Should return TRUE if:
    only_tags:
      - 'tagged'
    AND
    skip_tags:
      - 'never'
    '''
    only_tags = ['tagged']
    skip_tags = ['never']
    assert myObj.evaluate_tags(only_tags, skip_tags, all_vars)

    # Case two:

# Generated at 2022-06-13 09:15:39.239971
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # NOTE: this does an eval() on the list, so a real [], not a string list
    # Basic run
    item = Taggable()
    item.tags = ['foo']
    assert item.evaluate_tags(['foo'], [], {}), "tags should match"

    # tags should not match
    item = Taggable()
    item.tags = ['bar']
    assert not item.evaluate_tags(['foo'], [], {}), "tags should not match"

    # tags list should not match
    # NOTE: this does an eval() on the list, so a real [], not a string list
    item = Taggable()
    item.tags = ['foo', 'bar']
    assert not item.evaluate_tags(['bar', 'qux'], [], {}), "tags list should not match"

    # all should

# Generated at 2022-06-13 09:15:47.605660
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        pass

    my_instance = MyTaggable()

    # 1 - Tasks that are always or never are always executed
    my_instance.tags = ['always']
    assert my_instance.evaluate_tags(only_tags=[], skip_tags=['all']) is True
    assert my_instance.evaluate_tags(only_tags=[], skip_tags=['never']) is False

    my_instance.tags = ['never']
    assert my_instance.evaluate_tags(only_tags=[], skip_tags=['all']) is False
    assert my_instance.evaluate_tags(only_tags=[], skip_tags=['never']) is True

    # 2 - Tasks without tags are skipped if skip_tag 'tagged' is set

# Generated at 2022-06-13 09:15:58.192115
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    only_tags = ['web', 'deploy']
    skip_tags = ['frontend', 'meta']
    all_vars = {}

    fake_loader = {'templar': Templar(loader=fake_loader, variables=all_vars)}

    obj=Taggable()
    obj.tags = ['deploy', 'web']
    obj._loader = fake_loader
    assert(obj.evaluate_tags(only_tags, skip_tags, all_vars) == True)

    obj.tags = ['frontend', 'web']
    obj._loader = fake_loader
    assert(obj.evaluate_tags(only_tags, skip_tags, all_vars) == False)

    # should run when only_tags includes 'all'
    obj.tags = ['frontend', 'web']
    obj._loader = fake_loader

# Generated at 2022-06-13 09:16:07.737738
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.role
    role = ansible.playbook.role.Role()
    role.tags = ['one','two','always','untagged']
    role.tags_metadata = {}

    # No only_tags, no skip_tags, return should be True
    retval = role.evaluate_tags(None, None, None)
    assert retval == True

    # Only skip_tag 'two', return should be True
    retval = role.evaluate_tags(None, [u'two'], None)
    assert retval == True

    # Only skip_tag 'always', return should be True
    retval = role.evaluate_tags(None, [u'always'], None)
    assert retval == False

    # Only skip_tag 'iptables', return should be True

# Generated at 2022-06-13 09:16:16.089610
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.module_utils.six import iteritems

    # Assume that this dict is the same as AnsibleVars
    vars = {"k1": "v1", "k2": "v2", "k3": "v3"}

    def mock_template(self, data):
        return data

    t = Taggable()
    t.tags = None
    t._loader = "MOCK"
    t.evaluate_tags = Taggable.evaluate_tags
    t.evaluate_tags = Templar.template = mock_template

    # Define test cases, each tuple is made of
    #     (only_tags, skip_tags, ansible_vars, expected value from function)

# Generated at 2022-06-13 09:16:25.981797
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:16:44.018201
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.handler_include import HandlerInclude


# Generated at 2022-06-13 09:16:58.549557
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Test the evaluation of task should_run in case of no tags and
    # no only_tags and no skip_tags.
    # Expected result should be True
    task_name = "shell command"
    tags = ()
    only_tags = ()
    skip_tags = ()
    all_vars = {}

    task = Taggable()
    task.name = task_name
    task.tags = tags

    if not task.evaluate_tags(only_tags, skip_tags, all_vars):
        # This is not the expected result. Raise an exception
        raise Exception("Task {} should be run, but the evaluation result is False".format(task_name))

    # Test the evaluation of task should_run in case of no tags,
    # but one value in only_tags and no skip_tags.
    # Expected result should

# Generated at 2022-06-13 09:17:09.409331
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableImpl(Taggable):
        def __init__(self, tags):
            self._tags = tags

    class _loader:
        def __init__(self, template_vars):
            self.template_vars = template_vars

        def get_basedir(self, task_ds):
            return None

        def template(self, template_str):
            for key in self.template_vars.keys():
                if key in template_str:
                    template_str = template_str.replace(key, self.template_vars[key])
            return template_str

    def test_evaluate_tags(tags, only_tags, skip_tags, template_vars, expect_should_run):
        taggable = TaggableImpl(tags)

# Generated at 2022-06-13 09:17:21.487916
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    obj.tags = ['foo', 'bar']

    # test all
    obj.all_tags = None
    assert obj.evaluate_tags(['all'], None, None)
    assert not obj.evaluate_tags(None, ['all'], None)

    # test 'tagged'
    obj.tags = ['foo', 'bar', 'baz']
    assert obj.evaluate_tags(['tagged'], None, None)
    assert not obj.evaluate_tags(None, ['tagged'], None)
    obj.tags = None
    assert not obj.evaluate_tags(['tagged'], None, None)
    assert obj.evaluate_tags(None, ['tagged'], None)

    # test tags in tags
    assert obj.evaluate_tags(['foo'], None, None)
   

# Generated at 2022-06-13 09:17:30.956842
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    fake_ds = {}
    fake_all_vars = {}
    temp_object = Taggable()
    temp_object.tags = []
    assert temp_object.evaluate_tags(only_tags = None, skip_tags = None, all_vars = fake_all_vars)

    # test without any only_tags and skip_tags
    temp_object.tags = []
    assert temp_object.evaluate_tags(only_tags = [], skip_tags = [], all_vars = fake_all_vars)

    temp_object.tags = ["always"]
    assert temp_object.evaluate_tags(only_tags = [], skip_tags = [], all_vars = fake_all_vars)

    temp_object.tags = ["never"]

# Generated at 2022-06-13 09:17:39.682509
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass:
        tags = []

    testClass = TestClass()
    only_tags = set()
    skip_tags = set()
    assert testClass.evaluate_tags(only_tags, skip_tags, {}) == True

    testClass.tags = ["tag1"]
    only_tags.add("tag1")
    assert testClass.evaluate_tags(only_tags, skip_tags, {}) == True
    only_tags.add("tag2")
    assert testClass.evaluate_tags(only_tags, skip_tags, {}) == False
    only_tags.add("all")
    assert testClass.evaluate_tags(only_tags, skip_tags, {}) == True

    only_tags.clear()
    skip_tags.add("tag1")

# Generated at 2022-06-13 09:17:51.167163
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Set up test objects
    task = Taggable()
    task.tags = ['test_tag']
    host = Taggable()
    host.tags = ['test_tag']
    tag = Taggable()
    tag.tags = ['test_tag']
    play = Taggable()
    play.tags = ['test_tag']
    playbook = Taggable()
    playbook.tags = ['test_tag']

    # Test with only_tags
    only_tags = ['abc','def','ghi']
    assert(not task._should_run(only_tags, [], {}))
    only_tags = ['abc','test_tag','ghi']
    assert(task._should_run(only_tags, [], {}))
    only_tags = ['tagged']

# Generated at 2022-06-13 09:18:05.804346
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import mock
    from ansible.playbook.block import Block

    block = Block()

    # Evaluate an always tagged block when only_tags=['all']
    block.tags = ['always']
    assert block.evaluate_tags(only_tags=['all'], skip_tags=None,
                               all_vars={})

    # Evaluate an always tagged block when only_tags=['tagged']
    block.tags = ['always']
    assert block.evaluate_tags(only_tags=['tagged'], skip_tags=None, all_vars={})

    # Skip an always tagged block when skip_tags=['all']
    block.tags = ['always']
    assert not block.evaluate_tags(only_tags=None, skip_tags=['all'],
                                   all_vars={})

    # Skip an

# Generated at 2022-06-13 09:18:13.873815
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    t = Task()
    t.tags = ['always']
    assert t.evaluate_tags({'all': True}, {}, {}) == True

    t = Task()
    t.tags = ['never']
    assert t.evaluate_tags({'all': True}, {}, {}) == False

    t = Task()
    t.tags = ['never']
    assert t.evaluate_tags({'all': True}, {'always': True}, {}) == True

    t = Task()
    t.tags = ['always']
    assert t.evaluate_tags({'all': True}, {'always': True}, {}) == False

    t = Task()
    t.tags = ['untagged']
    assert t.evaluate_tags

# Generated at 2022-06-13 09:18:20.755178
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # test that 'always' always runs
    item = Taggable()
    item.tags = ['always']
    result = item.evaluate_tags(only_tags=[], skip_tags=[], all_vars={})
    assert result is True, result

    # test that 'never' never runs
    item = Taggable()
    item.tags = ['never']
    result = item.evaluate_tags(only_tags=[], skip_tags=[], all_vars={})
    assert result is False, result

    # test that no tags sets untagged
    item = Taggable()
    item.tags = None
    result = item.evaluate_tags(only_tags=[], skip_tags=[], all_vars={})
    assert result is True, result

    # test that simple match works for only_tags
    item = Taggable

# Generated at 2022-06-13 09:18:51.065363
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    assert Taggable.evaluate_tags(None, set(), None) == True, "Test case 1 failed"



# Generated at 2022-06-13 09:19:00.986380
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base

    class SubClass(Base, Taggable):
        pass

    only_tags = ['tag1', 'tag2']
    skip_tags = ['tag3', 'tag4']
    all_vars = dict()

    # Use case when tags is undefined
    # expect that method return true
    c = SubClass()
    result = c.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result, "evaluate_tags method return wrong value"

    # Use case when tags is defined, but method is not templar
    # expect that method return true
    c = SubClass()
    c.tags = ['tag1']
    result = c.evaluate_tags(only_tags, skip_tags, all_vars)

# Generated at 2022-06-13 09:19:08.351916
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    my_taggable = Taggable()

    my_taggable.tags = ['always']
    assert my_taggable.evaluate_tags(['always'], [], {})

    my_taggable.tags = ['always']
    assert my_taggable.evaluate_tags([], ['never'], {})

    my_taggable.tags = ['always']
    assert my_taggable.evaluate_tags([], ['always'], {})

    my_taggable.tags = ['never']
    assert not my_taggable.evaluate_tags(['always'], [], {})

    my_taggable.tags = ['always']
    assert not my_taggable.evaluate_tags(['never'], [], {})

    my_taggable.tags = ['never']
    assert not my

# Generated at 2022-06-13 09:19:17.859000
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()
    pc.tags = [ 'all' ]
    pc.only_tags = [ 'all' ]

    class DummyTaggable(Taggable):

        def __init__(self, tags):
            self.tags = tags

    assert DummyTaggable(tags=['foo']).evaluate_tags(pc.only_tags, pc.skip_tags, dict()) == True
    assert DummyTaggable(tags=['bar']).evaluate_tags(pc.only_tags, pc.skip_tags, dict()) == True
    assert DummyTaggable(tags=['all']).evaluate_tags(pc.only_tags, pc.skip_tags, dict()) == True
    assert DummyTaggable(tags=['never']).evaluate_tags

# Generated at 2022-06-13 09:19:27.340718
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class Test(Taggable):
        pass

    test = Test()
    test.tags = ['tag1', 'tag2']

    # test "only_tags"
    assert test.evaluate_tags(['tag1'], [], {}) is True
    assert test.evaluate_tags(['tag3'], [], {}) is False
    assert test.evaluate_tags(['tag4'], [], {}) is False
    assert test.evaluate_tags(['all'], [], {}) is True
    assert test.evaluate_tags(['tagged'], [], {}) is True
    assert test.evaluate_tags(['tagged'], [], {'tags': ['tag1', 'tag2']}) is False

# Generated at 2022-06-13 09:19:39.340700
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # This function has the following return values:
    # -1: exception
    #  0: not run
    #  1: run

    # This emulates the behaviour of the following Ansible command:
    # $ ansible-playbook --list-tasks example.yml -e "flag=true"

    class Example(Taggable):
        tags = FieldAttribute(isa='list', default=list, listof=string_types, extend=True)


# Generated at 2022-06-13 09:19:50.602278
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:19:58.213690
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """
    Test the Taggable class's evaluate_tags method against
    all the combination of tags.
    """
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    tags = ['geo', 'prod']

    skip_tags = ['notgeo']
    only_tags = []
    e = Taggable()
    e.tags = tags
    assert e.evaluate_tags(only_tags, skip_tags, dict()), \
        "evaluate_tags failed with only_tags = {0} and skip_tags = {1} and tags = {2}".format(only_tags, skip_tags, tags)

    skip_tags = ['notgeo']
    only_tags = ['geo', 'prod']
   

# Generated at 2022-06-13 09:20:12.866231
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext

    fake_play_context = PlayContext()
    _loader = 'fake loader'
    _all_vars = {'fake_var1': 'fake_value1', 'fake_var2': 'fake_value2'}
    _tags = {'fake_tag1', 'fake_tag2'}

    class FakeTaggable(Taggable):
        def __init__(self):
            super(FakeTaggable, self).__init__()
            self._loader = _loader
            self.tags = frozenset(_tags)

    fake_taggable = FakeTaggable()

    # default tags (should run)
    assert fake_taggable.evaluate_tags(set(), set(), _all_vars)

    # empty tags (should run)
   

# Generated at 2022-06-13 09:20:23.904976
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    play_context.only_tags = set()
    play_context.skip_tags = set()

    # Check that the action should run when:
    # - there are no tags
    # - there are only tags and the action is tagged
    # - there are skip tags and the action is not tagged
    # - there are only tags, but the action is not tagged
    # - there are skip tags and the action is tagged
    # - there are only tags and skip tags, but the action is tagged

    # - there are no tags
    action = Taggable()
    action.tags = []
    assert action.evaluate_tags(play_context.only_tags, play_context.skip_tags, dict())

    # - there are only tags and the action

# Generated at 2022-06-13 09:21:31.234071
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    tasks = []
    task1 = Task()
    task1.tags = ['task1','task2','task3']
    task2 = Task()
    task2.tags = ['task2','task3','task4']
    task3 = Task()
    task3.tags = ['task5','task6']


    # Testing tasks with only_tags option
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)


    # only_tags = ['task3'], it will run task1 and task2
    # only_tags = ['task3','task4'], it will run task2
    # only_tags = ['task3','task4','task5'], it will not run any of three tasks

# Generated at 2022-06-13 09:21:42.398008
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    item = Taggable()
    # Test empty tags
    result = item.evaluate_tags([], [], {})
    assert result
    # Test only_tags
    result = item.evaluate_tags(['tagged'], [], {})
    assert not result
    result = item.evaluate_tags(['all'], [], {})
    assert result
    # Test skip_tags
    result = item.evaluate_tags([], ['tagged'], {})
    assert not result
    result = item.evaluate_tags([], ['all'], {})
    assert not result

if __name__ == "__main__":
    import nose
    nose.runmodule()

# Generated at 2022-06-13 09:21:56.066637
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    import ansible.constants as C
    import ansible.template as template

    def func(obj):
        if isinstance(obj, string_types):
            # assume it's a tag
            return frozenset([obj])
        else:
            return obj

    C.DEFAULT_ROLES_PATH = './test/roles'
    t = Task()

    # test only_tags for task
    t.tags = ['always']
    assert t.evaluate_tags(func('always'), [], {}) is True
    assert t.evaluate_tags(func('all'), [], {}) is True
    assert t.evaluate_tags(func(['all', 'test']), [], {}) is True

# Generated at 2022-06-13 09:22:05.448807
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Foo(Taggable):
        def __init__(self):
            super(Foo, self).__init__()
            self._parent = None

    tags_1 = ['tag1','tag2','tag3','tag4','tag5']
    tags_2 = ['tag6','tag7','tag8','tag9','tag10']
    tags_3 = ['tag1','tag10','tag2','tag3','tag4','tag5','tag6','tag7','tag8','tag9']
    tags_4 = ['tag1','tag2','tag3','tag4','tag5',"'tag6'",'tag7','tag8','tag9','tag10']

# Generated at 2022-06-13 09:22:16.033515
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Test setup
    class TestObj(Taggable):
        def __init__(self):
            self._loader = None
            self.tags = None

    # Test  skip_tags with "all" and "never"
    skip_tags = ['all', 'never']
    only_tags = None
    test_obj = TestObj()
    test_obj.tags = ['never']

    assert not test_obj.evaluate_tags(only_tags, skip_tags, {})

    test_obj.tags = ['always']
    assert test_obj.evaluate_tags(only_tags, skip_tags, {})

    # Test only_tags with "all" and "never"
    skip_tags = None
    only_tags = ['all', 'never']
    test_obj = TestObj()

# Generated at 2022-06-13 09:22:27.450122
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.role.requiremenst import RoleRequirement
    # Runtime data to be used in the tests

# Generated at 2022-06-13 09:22:36.165529
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Create mock loader
    class MockLoader(object):
        pass
    loader = MockLoader()

    # Create Taggable instance
    class MockTaggable(Taggable):
        def __init__(self):
            self._loader = loader

    taggable = MockTaggable()
    taggable.tags = ['foo', 'bar']

    # Test tags execution with only_tags
    assert taggable.evaluate_tags(only_tags=['foo'], skip_tags=[], all_vars={}) is True
    assert taggable.evaluate_tags(only_tags=['foo'], skip_tags=[], all_vars={'foo': 'foo'}) is True
    assert taggable.evaluate_tags(only_tags=['bar'], skip_tags=[], all_vars={}) is True

# Generated at 2022-06-13 09:22:41.975158
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    taggable_obj = Taggable()
    taggable_obj.tags = [ 'tag1', 'tag2' ]

    all_vars = dict()
    res = taggable_obj.evaluate_tags(['tag1', 'tag3'], ['tag3'], all_vars)
    assert res == True

    res = taggable_obj.evaluate_tags(['tag3'], ['tag3'], all_vars)
    assert res == False

    taggable_obj.tags = [ 'tag1', 'tag2', 'untagged' ]
    res = taggable_obj.evaluate_tags(['tag3'], ['tag3'], all_vars)
    assert res == False

    res = taggable_obj.evaluate_tags(['tag3'], [], all_vars)

# Generated at 2022-06-13 09:22:51.373389
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestTaggable(Taggable):
        def __init__(self):
            self._tags = []

    class TestTaggableEvaluateTags(unittest.TestCase):

        def test_evaluate_tags_default(self):
            test_tag = TestTaggable()
            test_tag.tags = []
            self.assertTrue(test_tag.evaluate_tags(set(), set(), {}))

        def test_evaluate_tags_skip_with_no_tags(self):
            test_tag = TestTaggable()
            test_tag.tags = []
            self.assertFalse(test_tag.evaluate_tags(set(), set(["test_with_no_tags"]), {}))

       

# Generated at 2022-06-13 09:22:58.398453
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    obj.tags = ["tag1"]
    ret = obj.evaluate_tags(only_tags=[],skip_tags=[],all_vars={})
    assert ret == True
    ret = obj.evaluate_tags(only_tags=[],skip_tags=["tag1"],all_vars={})
    assert ret == False
    ret = obj.evaluate_tags(only_tags=["tag1"],skip_tags=[],all_vars={})
    assert ret == True
    ret = obj.evaluate_tags(only_tags=["tag1"],skip_tags=["tag1"],all_vars={})
    assert ret == False

    obj.tags = []
    ret = obj.evaluate_tags(only_tags=["tag1"],skip_tags=[],all_vars={})
    assert ret == False