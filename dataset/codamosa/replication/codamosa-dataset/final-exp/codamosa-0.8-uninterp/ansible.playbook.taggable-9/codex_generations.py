

# Generated at 2022-06-13 09:13:22.490618
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook
    p = ansible.playbook.Play()
    t = ansible.playbook.Task()
    assert t.evaluate_tags(['all'], [], {'foo': 'bar'}) == True
    assert t.evaluate_tags([], [], {'foo': 'bar'}) == True
    assert t.evaluate_tags([], ['all'], {'foo': 'bar'}) == False
    assert t.evaluate_tags(['foo'], [], {'foo': 'bar'}) == False
    assert t.evaluate_tags(['foo', 'bar'], [], {'foo': 'bar'}) == False
    t._tags = ['foo', 'bar']
    assert t.evaluate_tags(['foo', 'bar'], [], {'foo': 'bar'}) == True
    assert t

# Generated at 2022-06-13 09:13:30.193835
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class foo(Taggable):
        def __init__(self, tags=None, only_tags=None, skip_tags=None):
            self._tags = tags
            self._only_tags = only_tags
            self._skip_tags = skip_tags
    # test play settings
    pl = foo()
    pl._only_tags = []
    pl._skip_tags = []
    # test tasks settings
    t1 = foo(tags=['tag1'], only_tags=[], skip_tags=[])
    t2 = foo(tags=['tag2'], only_tags=[], skip_tags=[])
    t3 = foo(tags=['tag3'], only_tags=[], skip_tags=[])
    # test tasks values

# Generated at 2022-06-13 09:13:39.913364
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.parsing.vault import VaultLib
    from ansible.playbook.helpers import load_list_of_blocks

    from unittest import TestCase

    import os
    import tempfile
    import yaml

    test_data_dir = os.path.join(os.path.dirname(__file__), 'test_data')

    class MockLoader:

        def __init__(self, vault_pass=None):
            self.vault_pass = vault_pass
            self.vault = VaultLib(password=self.vault_pass)


    class TestTaggable(TestCase):

        def test_block_evaluate_tags(self):

            vault_secret = u'vault_secret'
            vault_password_file = tempfile.NamedTemporaryFile(mode='w')
           

# Generated at 2022-06-13 09:13:51.945596
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableTest(Taggable):
        pass
    # Dictionary with optional parameters for the test
    options = {'tags': ['test_tags'],
               'only_tags': ['always', 'test_tags'],
               'skip_tags': ['never', 'test_tags']}

    test_object = TaggableTest(**options)
    result = test_object.evaluate_tags(only_tags=['test_tags'], skip_tags=[], all_vars={})
    assert result is True
    result = test_object.evaluate_tags(only_tags=['test_tags'], skip_tags=['test_tags'], all_vars={})
    assert result is False
    result = test_object.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars={})


# Generated at 2022-06-13 09:13:57.966260
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableTestClass(Taggable):
        pass

    taggable = TaggableTestClass()

    task_tags = None
    only_tags = ['tag1']
    skip_tags = ['tag2']
    all_vars = {}
    result = taggable.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == True


# Generated at 2022-06-13 09:14:07.832248
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    t = Taggable()

    all_vars = dict()
    only_tags = set()
    skip_tags = set()

    # tag: untagged
    t.tags = None
    assert t.evaluate_tags(only_tags, skip_tags, all_vars)

    # tag: always
    t.tags = ['always']
    assert t.evaluate_tags(only_tags, skip_tags, all_vars)

    # tag: never
    t.tags = ['never']
    assert not t.evaluate_tags(only_tags, skip_tags, all_vars)

    # tag: never, always
    t.tags = ['never', 'always']
    assert not t.evaluate_tags(only_tags, skip_tags, all_vars)

    # tag: always, never
    t.tags

# Generated at 2022-06-13 09:14:17.592372
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    obj = Taggable()
    obj.tags = [0]
    # Test with only_tags
    only_tags = [0]
    skip_tags = []
    all_vars = {"test1":"test1"}
    # make the expectation
    expected = True
    actual = obj.evaluate_tags(only_tags, skip_tags, all_vars)
    assert actual == expected
    # Test with skip_tags
    only_tags = []
    skip_tags = [1]
    all_vars = {"test1":"test1"}
    # make the expectation
    expected = True
    actual = obj.evaluate_tags(only_tags, skip_tags, all_vars)
    assert actual == expected
    # Test with only_tags and skip_tags
    only_tags = [0]

# Generated at 2022-06-13 09:14:30.033084
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import unittest.mock as mock
    class TestTaggable(Taggable):
        pass

    tags = ['tag1', 'tag2', 'tag3']
    t = TestTaggable()
    with mock.patch.object(t, '_loader', return_value=None):
        t.tags = tags
        assert(t.evaluate_tags(set(), set(), {}) is True)

        assert(t.evaluate_tags(set(['tag1']), set(), {}) is True)
        assert(t.evaluate_tags(set(['tag1', 'tag2', 'tag3']), set(), {}) is True)
        assert(t.evaluate_tags(set(['tag2']), set(['tag3']), {}) is True)

# Generated at 2022-06-13 09:14:36.291369
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestClass(Taggable):
        pass

    # this test should pass
    tc = TestClass()
    tc.tags = ['always']
    result = tc.evaluate_tags(['always'], [], {})
    assert result == True

    # this test should fail
    tc = TestClass()
    tc.tags = ['never']
    result = tc.evaluate_tags(['always'], [], {})
    assert result == False

# Generated at 2022-06-13 09:14:45.152414
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    '''
    Test the method evaluate_tags of class Taggable.
    '''
    import ansible.playbook.task

    task = ansible.playbook.task.Task()

    task.only_tags = ['all', 'tagged', 'foo']
    task.skip_tags = ['bar', 'baz']

    # test for empty tags
    task.tags = []
    assert task.evaluate_tags(task.only_tags, task.skip_tags, dict()) == True

    # test with empty task.tags and task.only_tags and task.skip_tags
    task.only_tags = []
    task.skip_tags = []

    task.tags = []
    assert task.evaluate_tags(task.only_tags, task.skip_tags, dict()) == True

    task.tags = ['foo']
   

# Generated at 2022-06-13 09:15:10.017155
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    block = Block()
    task = Task()
    play_context = PlayContext()

    block.tags = ['all']
    task.tags = ['all']
    assert block.evaluate_tags(['all'], [], play_context)
    assert task.evaluate_tags(['all'], [], play_context)

    block.tags = ['all']
    task.tags = ['tagged']
    assert block.evaluate_tags(['tagged'], [], play_context)
    assert task.evaluate_tags(['tagged'], [], play_context)

    block.tags = []
    task.tags = []

# Generated at 2022-06-13 09:15:21.785188
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    tags = Taggable()
    tags.tags = ['tests', 'test']
    tags.tags = ['always', 'test']

    assert tags.evaluate_tags({}, ['always'], {}) is False
    assert tags.evaluate_tags(['always'], [], {}) is True
    assert tags.evaluate_tags(['always', 'test'], [], {}) is True
    assert tags.evaluate_tags(['always', 'test'], ['always'], {}) is False
    assert tags.evaluate_tags(['tagged', 'test'], [], {}) is True
    assert tags.evaluate_tags(['tagged', 'test'], ['tagged'], {}) is False
    assert tags.evaluate_tags(['tagged', 'test'], ['tagged', 'test'], {}) is False
    assert tags.evaluate_

# Generated at 2022-06-13 09:15:33.533534
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.task as task
    import ansible.playbook.block as block
    a = task.Task(dict(name="test", actions=[dict(module="test")], tags=["foo", "bar"]))
    b = task.Task(dict(name="test", actions=[dict(module="test")], tags=["foo", "baz"]))
    c = task.Task(dict(name="test", actions=[dict(module="test")], tags=["foobar", "baz"]))
    d = task.Task(dict(name="test", actions=[dict(module="test")]))
    e = task.Task(dict(name="test", actions=[dict(module="test")], tags=["never"]))

# Generated at 2022-06-13 09:15:42.877569
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableSub(Taggable):
        tags = ['foo', 'bar']

    only_tags = ['foo', 'bar']
    skip_tags = ['baz']
    all_vars = {}

    t = TaggableSub()
    result = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == True

    only_tags = ['foo', 'bar', 'baz']
    skip_tags = ['baz']
    all_vars = {}

    t = TaggableSub()
    result = t.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result == True

    only_tags = ['baz']
    skip_tags = ['baz']
    all_vars = {}

    t = TaggableSub()


# Generated at 2022-06-13 09:15:56.015603
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TaggableTest(Taggable):
        pass

    tag = TaggableTest()
    tag.tags = ['test-tag']

    # Taggable method evaluate_tags should return true when
    # only_tags is 'all', skip_tags is empty and tags is not empty
    print("1")
    only_tags = ['all']
    skip_tags = []
    assert tag.evaluate_tags(only_tags, skip_tags, dict() == True)

    # Taggable method evaluate_tags should return true when
    # only_tags is 'tagged', skip_tags is empty and tags is not
    # empty and contains 'test-tag'
    print("2")
    only_tags = ['tagged']
    skip_tags = []
    assert tag.evaluate_tags(only_tags, skip_tags, dict())

# Generated at 2022-06-13 09:16:06.187809
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    b = Block()
    b.vars = dict(foo='foo', bar='bar', baz='baz')
    all_vars = dict(foo='foo', bar='bar', baz='baz')

    b.tags = dict(baz="not baz")
    tags = b.evaluate_tags(None, None, all_vars)
    assert tags == True
    b.tags = dict(baz="baz")
    tags = b.evaluate_tags(None, None, all_vars)
    assert tags == True

    all_vars['hostvars'] = dict(foo='foo', bar='bar', baz='baz')
    b.tags = dict(tags="hostvars")

# Generated at 2022-06-13 09:16:15.386069
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # test for load_tags
    t = Taggable()
    assert t._load_tags(None, 'tag1') == ['tag1']
    assert t._load_tags(None, 'tag1,tag2') == ['tag1', 'tag2']

    # check the evaluate_tags method
    only_tags = set()
    skip_tags = set()
    all_vars = dict()
    assert t.evaluate_tags(only_tags, skip_tags, all_vars) == True

    t.tags = 'tag1'
    t.only_tags = set()
    t.skip_tags = set()
    assert t.evaluate_tags(only_tags, skip_tags, all_vars) == True

    t.tags = 'tag1'
    only_tags = set(['tag2'])
   

# Generated at 2022-06-13 09:16:25.530687
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakePlaybook:
        def __init__(self, loader, variables):
            self.vars = variables

    class FakeTask:
        def __init__(self):
            self.tags = list()
            self.when = list()
            self.loader = FakePlaybook(dict(), dict())

    # Test conditions for "only_tags" parameter
    t = FakeTask()
    t.tags = ['always']
    assert t.evaluate_tags(['always', 'foo'], list(), dict()) is True
    t.tags = ['foo']
    assert t.evaluate_tags(['always', 'foo'], list(), dict()) is True
    t.tags = ['foo', 'bar']
    assert t.evaluate_tags(['foo', 'bar'], list(), dict()) is True
    t.tags = ['foo', 'bar']

# Generated at 2022-06-13 09:16:40.108719
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class AnsibleModule(Taggable):
        def __init__(self, *args, **kwargs):
            super(AnsibleModule, self).__init__()
            for k,v in kwargs.items():
                setattr(self, k, v)
    # all and (any or tagged)
    module = AnsibleModule(tags=['always', 'yes'], _loader=None)
    assert module.evaluate_tags(only_tags=['all', 'yes'], skip_tags=[], all_vars=dict()) == True
    assert module.evaluate_tags(only_tags=['all', 'no'], skip_tags=[], all_vars=dict()) == False

# Generated at 2022-06-13 09:16:46.062667
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    a = Taggable()
    tags = ['test']
    a.tags = tags
    should_run = a.evaluate_tags(None, None, None)
    assert should_run is True
    should_run = a.evaluate_tags(['test'], None, None)
    assert should_run is True
    should_run = a.evaluate_tags(['test'], ['test'], None)
    assert should_run is False

if __name__ == "__main__":
    test_Taggable_evaluate_tags()

# Generated at 2022-06-13 09:17:22.557776
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestClass:
        def __init__(self):
            self._tags = []
            self._loader = None

        def set_tags(self, tags):
            self._tags = tags

        tags = property(lambda s: s._tags,
                        set_tags)

    # Test 1: always should be run
    tc1 = TestClass()
    tc1.tags = ['always']
    assert tc1.evaluate_tags(['never'], [], {})
    assert tc1.evaluate_tags(['never'], [], {'tags': 'never'})

    # Test 2: run when one of the tags of object is in the only_tags list
    tc2 = TestClass()
    tc2.tags = ['always', 'test2']
    assert tc2.evaluate_tags(['test2'], [], {})

   

# Generated at 2022-06-13 09:17:31.558938
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Setup fakes and mocks
    fake_self = None
    fake_self.tags = ['foo', 'bar']
    fake_only_tags = ['foo']
    fake_skip_tags = ['bar']

    fake_all_vars = {'foo': '1', 'bar': '2', 'baz': '3'}
    fake_Templar = None
    fake_Templar.template = lambda x: x

    # Setup mocks for test
    fake_self._loader = None
    fake_self._loader.load_from_file = lambda x: x
    fake_self._loader.get_basedir = lambda x: x
    
    fake_self.tags = ['foo', 'bar']
    fake_only_tags = ['foo']
    fake_skip_tags = ['bar']

    # Mocks

# Generated at 2022-06-13 09:17:40.546096
# Unit test for method evaluate_tags of class Taggable

# Generated at 2022-06-13 09:17:51.636971
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    import pytest

    class TaggableImplementation(Taggable):

        def __init__(self, tags=None):
            self._tags = tags

    # Tags are in only_tags, there should be no skip
    class TaggableImplementation1(TaggableImplementation):
        pass

    assert TaggableImplementation1().evaluate_tags(only_tags=['foo', 'bar'], skip_tags=[], all_vars={})

    # Tags are not in only_tags, there should be a skip
    class TaggableImplementation2(TaggableImplementation):
        pass

    assert not TaggableImplementation2().evaluate_tags(only_tags=['foobar'], skip_tags=[], all_vars={})

    # Tags are in skip_tags, there should be no skip

# Generated at 2022-06-13 09:18:06.298035
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    """
    This method is a unit test for method evaluate_tags of class Taggable
    """
    class Task(Taggable):
        _tags = ['tag1', 'tag2', 'tag3']

    task = Task()
    all_vars = {}

    # Test 1
    # Test inclusion of tags
    only_tags = ['tag1']
    skip_tags = []
    assert task.evaluate_tags(only_tags, skip_tags, all_vars)
    # Test 2
    # Test exclusion of tags
    only_tags = []
    skip_tags = ['tag1']
    assert not task.evaluate_tags(only_tags, skip_tags, all_vars)
    # Test 3
    # Test with tags being specified in both only_tags and skip_tags
    only_tags = ['tag2']


# Generated at 2022-06-13 09:18:14.246946
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TestTaggable(Taggable):
        pass

    t = TestTaggable()

    assert (t.evaluate_tags(
        only_tags=('specific_tag',),
        skip_tags=None,
        all_vars={'tags': ['specific_tag']}
    ) is True)

    assert (t.evaluate_tags(
        only_tags=('specific_tag',),
        skip_tags=None,
        all_vars={'tags': ['different_tag']}
    ) is False)

    assert (t.evaluate_tags(
        only_tags=('specific_tag',),
        skip_tags=('specific_tag',),
        all_vars={'tags': ['specific_tag']}
    ) is False)


# Generated at 2022-06-13 09:18:25.647952
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Import modules that are needed for testing
    # Mocking objects
    class TestRole(Taggable):
        _tags = ['a', 'b']

    def test_evaluate_tags():
        a = TestRole()
        # Test when only_tags and skip_tags are empty
        a.evaluate_tags(only_tags = [], skip_tags = [])
        # Test when only_tags is not empty and skip_tags is empty
        a.evaluate_tags(only_tags = ['a'], skip_tags = [])
        # Test when only_tags is empty and skip_tags is not empty
        a.evaluate_tags(only_tags = [], skip_tags = ['a'])
        # Test when only_tags and skip_tags are not empty

# Generated at 2022-06-13 09:18:34.197911
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    # Case 1:
    #   Tags: ['always']
    #   Only_tags: ['always']
    #   Skip_tags: []
    #   Should_run: True
    only_tags = ['always']
    skip_tags = []
    mock_tags = ['always']

    test_item = Taggable()
    test_item.tags = mock_tags

    assert test_item.evaluate_tags(only_tags, skip_tags, {}) == True

    # Case 2:
    #   Tags: ['always']
    #   Only_tags: []
    #   Skip_tags: ['always']
    #   Should_run: False
    only_tags = []
    skip_tags = ['always']
    mock_tags = ['always']

    test_item = Taggable()

# Generated at 2022-06-13 09:18:40.610896
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    import ansible.playbook.block
    block = ansible.playbook.block.Block()
    only_tags = []
    skip_tags = []
    all_vars = dict()
    block._dump_attrs()
    result = block.evaluate_tags(only_tags, skip_tags, all_vars)
    assert result is True

# Generated at 2022-06-13 09:18:49.663002
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # Wrong tags type
    tags = Taggable()
    tags.tags = 123
    
    assert tags.evaluate_tags([], [], {}) == False

    # Wrong only_tags type
    tags.tags = ['tag1']
    only_tags = 123

    assert tags.evaluate_tags(only_tags, [], {}) == False

    # Wrong skip_tags type
    skip_tags = 123

    assert tags.evaluate_tags(only_tags, skip_tags, {}) == False

    # Wrong all_vars type
    skip_tags = []
    all_vars = 123

    assert tags.evaluate_tags(only_tags, skip_tags, all_vars) == False

    # Normal situation
    skip_tags = []
    all_vars = {}


# Generated at 2022-06-13 09:19:52.016057
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    # From http://stackoverflow.com/questions/283437/unit-testing-a-python-class
    class TestTaggable(Taggable):
        """Taggable class for test purposes."""
        _tags = FieldAttribute(isa='list', default=list, listof=(string_types, int), extend=True)
        def __init__(self, tags):
            self.tags = tags

    tt = TestTaggable(["test", "untagged"])
    assert tt.evaluate_tags(["test"], None, None)  # implicit True
    assert tt.evaluate_tags(["test"], [], None)  # implicit True
    assert not tt.evaluate_tags(["stest"], [], None)
    assert tt.evaluate_tags(["stest"], ["stest"], None)
   

# Generated at 2022-06-13 09:19:58.800250
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.plays import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import IncludeTask

    only_tags = ['tag1','tag2','tag3','tag4','tag5','tag6']
    skip_tags = []
    all_vars = {}

    # test play

# Generated at 2022-06-13 09:20:13.493674
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class TaggableClass():
        def __init__(self):
            self._tags = None
            self._tags = []

    taggable_class = TaggableClass()
    only_tags = ['mytag']
    skip_tags = []
    all_vars = {}

    taggable_class._tags.append('mytag')
    result = Taggable.evaluate_tags(taggable_class, only_tags, skip_tags, all_vars)
    assert result == True

    del taggable_class._tags[:]
    result = Taggable.evaluate_tags(taggable_class, only_tags, skip_tags, all_vars)
    assert result == False

    taggable_class._tags.append('never')

# Generated at 2022-06-13 09:20:24.704559
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    from ansible.playbook.base import Base
    from ansible.playbook.task import Task

    class MyPlay(Base):
        pass

    class MyTask(Taggable, Task):
        pass

    t = MyTask()

    assert t.evaluate_tags(only_tags=[], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=['all'], skip_tags=[], all_vars={}) == True
    assert t.evaluate_tags(only_tags=[], skip_tags=['all'], all_vars={}) == False
    assert t.evaluate_tags(only_tags=['all'], skip_tags=['all', 'always'], all_vars={}) == False

# Generated at 2022-06-13 09:20:36.631930
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class NoDict:
        def __init__(self, d):
            self.d = d
        def __getitem__(self, k):
            return self.d[k]

    # Format: (only_tags, skip_tags, all_vars, result)

# Generated at 2022-06-13 09:20:45.744338
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    module = Taggable()
    task = dict(tags=['always'])
    result = module.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars=task)
    assert result == True

    task = dict(tags=['never'])
    result = module.evaluate_tags(only_tags=['always'], skip_tags=[], all_vars=task)
    assert result == False

    task = dict(tags=['never'])
    result = module.evaluate_tags(only_tags=[], skip_tags=['always'], all_vars=task)
    assert result == True


# Generated at 2022-06-13 09:20:54.845463
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class FakeVarManager:
        def __init__(self, variable_manager):
            self.variable_manager = variable_manager

    class FakeLoader:
        pass

    class FakeAction(Taggable):
        def __init__(self, tags, module_name):
            self._ds = None
            self._loader = FakeLoader()
            self._variable_manager = FakeVarManager(variable_manager)
            self._shared_loader_obj = None
            self.tags = tags
            self.module_name = module_name

    class FakeOptions:
        def __init__(self, tags, skip_tags):
            self.tags = tags
            self.skip_tags = skip_tags

    class FakePlay:
        def __init__(self, options):
            self.options = options


# Generated at 2022-06-13 09:21:05.016533
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    ''' Test function for Taggable._load_tags method
    :return: no return
    '''
    taggable_obj = Taggable()

    taggable_obj.tags = []
    result = taggable_obj.evaluate_tags(None, None, None)
    assert result == True, "taggable_obj.evaluate_tags failed to return True with only None as arguments"

    taggable_obj.tags = None
    result = taggable_obj.evaluate_tags(None, None, None)
    assert result == True, "taggable_obj.evaluate_tags failed to return True with only None as arguments"

    taggable_obj.tags = 'foo'
    result = taggable_obj.evaluate_tags(None, None, None)

# Generated at 2022-06-13 09:21:13.737445
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MockTask(object):
        def __init__(self, tags):
            self.tags = tags

    skip_tags = ['skip_me']
    run_tags = ['run_me']
    only_tags = ['only_me']
    always_tags = ['always_me', 'always']
    never_tags = ['never_me', 'never']
    tagged_tags = ['tagged_me', 'tagged']
    all_tags = ['all_me', 'all']

    task = MockTask(['run_me'])
    assert task.evaluate_tags(skip_tags=None, only_tags=None, all_vars=dict())

    task = MockTask(run_tags)
    assert task.evaluate_tags(skip_tags=skip_tags, only_tags=None, all_vars=dict())



# Generated at 2022-06-13 09:21:25.323215
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class TestedTaggable(Taggable):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    # Case 1: tags is None.
    # If tags is None, tags is set to empty list. Then for case 1, 2, 3, 4, 5, 7, 8, 9, 10 and 12, should_run is True.
    # For case 6, 11, 13 and 14, should_run is False.
    t = TestedTaggable()
    assert t.evaluate_tags(None, ['tagged'], None)
    assert t.evaluate_tags(None, ['always'], None)
    assert t.evaluate_tags(None, ['never'], None)
    assert t.evaluate_tags(None, [], None)

# Generated at 2022-06-13 09:22:28.682954
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class MyTaggable(Taggable):
        pass

    # Initialize ansible options
    ans_opts = '{"skip_tags":"never"}'
    ans_opts_list = ['skip_tags=never']

    # Initialize class variable 'superclass_caller'
    superclass_caller = 'ansible.playbook.task'

    # Create my test instance
    my_taggable = MyTaggable()

    # Create a mock for ansible.playbook.task.Task
    t_task = 'ansible.playbook.task.Task'
    m_task = mock.patch(t_task)
    mock_task = m_task.start()
    mock_task.get_vars.return_value = { "all_vars": "mocked_all_vars" }
    mock

# Generated at 2022-06-13 09:22:37.122495
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():
    class Mock:
        # pylint: disable=too-few-public-methods
        def __init__(self, tags=None):
            self.tags = tags

    class TestClass(Taggable):
        def __init__(self):
            self.tags = None

    t = TestClass()

    #TestCase-1
    mock = Mock(tags = None)
    assert t.evaluate_tags([], [], mock) == True

    #TestCase-2
    mock = Mock(tags = None)
    assert t.evaluate_tags(['foo'], [], mock) == False

    #TestCase-3
    mock = Mock(tags = ['foo'])
    assert t.evaluate_tags(['foo'], [], mock) == True

    #TestCase-4

# Generated at 2022-06-13 09:22:47.989795
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C

    class MockTask(Task, Taggable):
        pass

    mock_data_structure = dict(name='test-task', tags=['some-tag', 'another-tag'])
    mock_task = MockTask.load(mock_data_structure, None, None, play_context=PlayContext())
    assert mock_task.evaluate_tags(C.TAGS_ALL, C.TAGS_SKIP_TAGS, dict()) is True

# Generated at 2022-06-13 09:22:56.248870
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class FakeTaggable(Taggable):
        def __init__(self, tags=None):
            self.tags = tags

    # check if all tags are executed
    assert(FakeTaggable().evaluate_tags(only_tags=None, skip_tags=None, all_vars={}) == True)

    # verify that the all: tag works correctly
    assert(FakeTaggable(tags=['all']).evaluate_tags(only_tags=['all'], skip_tags=None, all_vars={}) == True)

    # check if only tags are executed correctly
    assert(FakeTaggable(tags=['all']).evaluate_tags(only_tags=['all', 'tag1'], skip_tags=None, all_vars={}) == True)

    # check if skip tags are executed correctly

# Generated at 2022-06-13 09:23:04.434914
# Unit test for method evaluate_tags of class Taggable
def test_Taggable_evaluate_tags():

    class MyTaggable(Taggable):
        pass

    myTaggable_1 = MyTaggable()
    myTaggable_1.tags = ['tag1', 'tag2']
    myTaggable_2 = MyTaggable()
    myTaggable_2.tags = ['tag1', 'tag2', 'tag3']

    # Case: no tags should be run
    only_tags = set(['tag3'])
    skip_tags = set(['tag3'])
    assert myTaggable_1.evaluate_tags(only_tags, skip_tags, {}) == False
    assert myTaggable_2.evaluate_tags(only_tags, skip_tags, {}) == False

    # Case: some tags should be run
    only_tags = set(['tag1', 'tag3'])