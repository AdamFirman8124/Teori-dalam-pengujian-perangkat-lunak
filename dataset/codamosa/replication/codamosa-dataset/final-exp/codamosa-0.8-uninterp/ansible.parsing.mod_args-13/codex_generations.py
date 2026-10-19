

# Generated at 2022-06-13 06:56:52.776182
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.six import iteritems

# Generated at 2022-06-13 06:57:03.672353
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.errors import AnsibleError
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    #from ansible.playbook.block import Block
    #from ansible.playbook.role import Role
    data = {}
    # test parameter 'task_ds' here
    # test for raising exception
    with pytest.raises(AnsibleAssertionError) as excinfo:
        parser = ModuleArgsParser(task_ds=data)
    assert type(excinfo.value) == AnsibleAssertionError
    # test parameter 'collection_list'
    data = {}
    data['action'] = dict()
    data['action']['module'] = 'shell'
    data['action']['args']

# Generated at 2022-06-13 06:57:13.822139
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Initialize test module object
    parser = ModuleArgsParser()
    test_dict = {u'action': u'debug', u'env': {u'DIB_INSTALLTYPE_puppet_modules': u'git', u'DIB_INSTALLTYPE_python2_m2crypto': u'git'}}
    assert parser.parse(test_dict) == ('debug', {'env': {u'DIB_INSTALLTYPE_puppet_modules': u'git', u'DIB_INSTALLTYPE_python2_m2crypto': u'git'}}, None)

# Generated at 2022-06-13 06:57:22.868222
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    options = PlaybookExecutor.load_extra_vars('www.example.com')
    play_context = PlayContext(options=options, variable_manager=variable_manager)

# Generated at 2022-06-13 06:57:29.546580
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task = dict(action = dict(module='something'))
    obj = ModuleArgsParser(task)
    result = obj.parse()
    assert result == ('something', {}, None)

    # fail
    task = dict(action = dict(module='something'))
    obj = ModuleArgsParser(task)
    try:
        result = obj.parse()
        assert False
    except AnsibleParserError:
        assert True


# Generated at 2022-06-13 06:57:31.961005
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    map = ModuleArgsParser(task_ds)
    map.parse()
    assert map.parse() == True


# Generated at 2022-06-13 06:57:33.487470
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()



# Generated at 2022-06-13 06:57:46.459326
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Unit test for method parse of class ModuleArgsParser
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests import unittest
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    class TestModuleArgsParserParse(unittest.TestCase):
        def parse(self):
            self.assertEqual(AnsibleBaseYAMLObject.parse(), AnsibleBaseYAMLObject)

    def setUp(self):
        self.module_args_parser_parse = AnsibleBaseYAMLObject.parse()

    def tearDown(self):
        del self.module_args_parser_parse


# Generated at 2022-06-13 06:57:53.752873
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    def test_ModuleArgsParser_parse(task_ds=None,
                                    collection_list=None,
                                    expected_action=None,
                                    expected_args=None,
                                    expected_delegate_to=None,
                                    expected_resolved_action=None):

        parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
        action, args, delegate_to = parser.parse()

        assert action == expected_action
        assert args == expected_args
        assert delegate_to == expected_delegate_to
        assert parser.resolved_action == expected_resolved_action

    # Test with empty task_ds

# Generated at 2022-06-13 06:57:58.050781
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
     "action": "shell",
     "args": "echo hi",
     "name": "shell"
    }
    collection_list = [
     "ansible.builtin"
    ]
    parser = ModuleArgsParser(task_ds, collection_list)
    assert parser.parse() == ('shell', {'_raw_params': 'echo hi'}, None)


# Generated at 2022-06-13 06:58:27.649359
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def compare_output(input_args, expected_output):
        module_args_parser = ModuleArgsParser(input_args)
        output = module_args_parser.parse()
        if output != expected_output:
            print("Test failed:")
            print("Input: %s" % repr(input_args))
            print("Expected output: %s" % repr(expected_output))
            print("Output: %s" % repr(output))

    # test for module name and arguments parsings
    compare_output(
        {'shell': 'echo xyzzy', 'args': {'executable': '/bin/zsh'}},
        ('shell', {'_raw_params': 'echo xyzzy', 'executable': '/bin/zsh'}, None)
    )

# Generated at 2022-06-13 06:58:39.681812
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("test_ModuleArgsParser_parse()")

    print("1) Task with action: module: args")
    task_ds = {
        'action': "echo hi",
        'delegate_to': 'localhost',
    }
    parser = ModuleArgsParser(task_ds)
    (action, args, delegate_to) = parser.parse()
    assert action == 'echo'
    assert args == {'_raw_params': 'hi'}
    assert delegate_to == 'localhost'

    print("2) Task with action: module, args")
    task_ds = {
        'action': {
            'module': "echo hi",
            'k': 'v'
        },
        'delegate_to': 'localhost',
    }
    parser = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 06:58:47.613711
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.plugins import action_loader
    from ansible.plugins import module_loader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import merge_hash

    #print('SUT action_loader.__dict__=',action_loader.__dict__)
    #print('SUT module_loader.__dict__=',module_loader.__dict__)

    print('Test case 1: the task is {action: module_name, args: {arg1: value1}' )

# Generated at 2022-06-13 06:58:53.274068
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell echo hi', 'delegate_to': '', 'first_name': 'Bob', 'greeting': 'hello', 'group_names': ['wheel', 'dev'], 'hosts': ['localhost'], 'ignore_errors': False, 'name': 'Greet the Ansible'}
    collection_list = None
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    assert parser.parse() == ('shell', {}, None)

# Generated at 2022-06-13 06:59:04.421978
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import copy
    import pytest
    from ansible.module_utils.common.parameters import count_special_args

    # test_ds may be overridden by individual tests in this module
    test_ds = {'action': {'module': 'setup', 'x': 'hello', 'y': 'world'}, 'changed': True, 'failed': False}
    parser = ModuleArgsParser(test_ds)

    # test action
    assert parser.parse() == ('setup', {'x': 'hello', 'y': 'world'}, None)

    # test local_action
    # test_ds = {'local_action': {'module': 'setup', 'x': 'hello', 'y': 'world'}, 'changed': True, 'failed': False}
    # parser = ModuleArgsParser(test_ds)
    # assert parser.parse()

# Generated at 2022-06-13 06:59:11.166128
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    task_ds = {}
    skip_action_validation = False
    res_expected = None
    res_real = module_args_parser.parse(skip_action_validation)
    assert res_real == res_expected

    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    task_ds = None
    skip_action_validation = True
    res_expected = None
    res_real = module_args_parser.parse(skip_action_validation)
    assert res_real == res_expected

    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    task_ds = None
    skip_action_validation = False
    res_expected = None

# Generated at 2022-06-13 06:59:14.847625
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser({'action': 'name=ansible', 'delegate_to': 'localhost'}, [])
    assert module_args_parser.parse() == ('name', {'name': 'ansible'}, 'localhost')

# Generated at 2022-06-13 06:59:25.394122
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(action='shell echo hi')
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    action,args,delegate_to = module_args_parser.parse()
    assert action == "shell"
    assert args == dict(_raw_params="echo hi")
    assert delegate_to is None

    task_ds = dict(local_action='shell echo hi')
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    action,args,delegate_to = module_args_parser.parse()
    assert action == "shell"
    assert args == dict(_raw_params="echo hi")
    assert delegate_to == "localhost"

    task_ds = dict(shell='echo hi')

# Generated at 2022-06-13 06:59:29.682787
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(action=dict(module='copy', args='src=a dest=b'))
    assert ModuleArgsParser(task_ds).parse() == ('copy',
                                                 {'args': 'src=a dest=b'},
                                                 None)



# Generated at 2022-06-13 06:59:32.955470
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # ModuleArgsParser is a private class
    # This unit test is only for method parse of class ModuleArgsParser
    # No Public API exposed for class ModuleArgsParser
    # Unit test not relevant

    pass


# Generated at 2022-06-13 06:59:55.014509
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible import constants as C
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    # Ensure that the constructor succeeds
    assert ModuleArgsParser()

    # Task is a python dictionary. It needs to be encoded to yaml and then
    # decoded to load it as a valid AnsibleTask
    task_ds = yaml.safe_load("""
- name: test action run
  action: shell echo hi
""")
    task_ds = task_ds[0]
    # test parse 1
    parser = ModuleArgsParser(task_ds, ['/opt/ansible/collections/ansible_collections/somecoll'])

# Generated at 2022-06-13 07:00:06.055106
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.cli.galaxy.parser import GalaxyParser
    from ansible.plugins.loader import action_loader
    from ansible.galaxy.collection import CollectionRequirement, Collection
    # test_ModuleArgsParser_parse() should be able to parse task, module, builtin_action
    with open('./tests/unit/cli/galaxy/test_fixtures/action_plugins.json') as action_plugins_f:
        action_plugins_yaml = yaml.safe_load(action_plugins_f)
    module_args_parser = ModuleArgsParser({'action': 'test_action_plugin'}, [])
    parsed_result = module_args_parser.parse(skip_action_validation=True)
    assert parsed

# Generated at 2022-06-13 07:00:20.221246
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'action': 'shell',
        'args': 'echo hi',
        'delegate_to': 'localhost'
    }
    parser = ModuleArgsParser(task_ds=task_ds)
    exp_action = 'shell'
    exp_args = {'_raw_params': 'echo hi', '_uses_shell': True}
    exp_delegate_to = 'localhost'
    act_action, act_args, act_delegate_to = parser.parse()

    assert (act_action, act_args, act_delegate_to) == (exp_action, exp_args, exp_delegate_to)

    # Test static parameter

# Generated at 2022-06-13 07:00:28.469078
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell echo hi', 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert (('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, 'localhost') == parser.parse())
    #
    task_ds = {'action': {'module': 'shell', 'args': 'echo hi'}, 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=task_ds)
    assert (('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, 'localhost') == parser.parse())
    #
    task_ds = {'local_action': {'module': 'shell', 'args': 'echo hi'}}
    parser = ModuleArgsParser

# Generated at 2022-06-13 07:00:35.819302
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action = 'myaction'
    args = 'myargs'
    delegate_to = 'foo'
    task_ds = {'action': action, 'args': args, 'delegate_to': delegate_to}
    obj = ModuleArgsParser(task_ds)
    # Call method
    r = obj.parse()

    assert r[0] == action
    assert r[1] == parse_kv(args)
    assert r[2] == delegate_to



# Generated at 2022-06-13 07:00:38.862925
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    result = parser.parse(skip_action_validation=True)
    # set()


# class ModuleArgsParser


# class TaskInclude

# Generated at 2022-06-13 07:00:45.916463
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.common.collections import is_sequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    # The following param is a list containing tuples of 3 elem:
    #       - the input data
    #       - the expected result for action
    #       - the expected result for args

# Generated at 2022-06-13 07:00:51.627833
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser(task_ds={'action': 'shell echo hi', 'delegate_to': 'localhost', 'should_be_removed': False})
    expected_result = ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, 'localhost')
    actual_result = module_args_parser.parse(skip_action_validation=True)
    assert actual_result == expected_result

# Generated at 2022-06-13 07:00:59.883806
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # There are no test cases in the code. The function code is not executable.

    # test case 1
    # self._task_ds = {'action': 'name=val'}
    # return (action, args, delegate_to)

    # test case 2
    # self._task_ds = {'action': {'module_name': {'param1': 'value1'}}}
    # return (action, args, delegate_to)

    # test case 3
    # self._task_ds = {'action': {'module_name': 'name=val'}}
    # return (action, args, delegate_to)
    pass

# class for dealing with roles

# Generated at 2022-06-13 07:01:09.975559
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # testcase 1
    # Initializing an empty dict and then calling the method parse
    test_task_ds = dict()
    maparser = ModuleArgsParser(test_task_ds)

    action, args, delegate_to = maparser.parse()
    assert action is None
    assert args == dict()
    assert delegate_to == dict()

    # testcase 2
    # Initializing a dict and then calling the method parse
    test_task_ds = dict()
    test_task_ds['action'] = 'copy'
    test_task_ds['args'] = dict()
    maparser = ModuleArgsParser(test_task_ds)
    action, args, delegate_to = maparser.parse()
    assert action == 'copy'
    assert args == dict()
    assert delegate_to == dict()

    # testcase 3
   

# Generated at 2022-06-13 07:01:23.066167
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import TaskInclude

    play_context_instance = PlayContext()
    TaskInclude.action_loader = DummyActionLoader()
    TaskInclude.module_loader = DummyModuleLoader()

    module_args_parser = ModuleArgsParser(task_ds={"name": "my task", "local_action": "copy src=a dest=b"}, collection_list=[])
    module_args_parser.parse()



# Generated at 2022-06-13 07:01:25.492957
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(task_ds=None)
    assert m.parse() == (None, dict(), Sentinel)

# Generated at 2022-06-13 07:01:34.904052
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # NOTE: Cannot directly use loader, as it will try and
    # parse the files being loaded.
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create the loader object
    loader = DataLoader()

    # Create the variable manager
    variable_manager = VariableManager()

    # Create the inventory
    inventory = InventoryManager(loader=loader, sources="")

    # Create the variable_manager object
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create the task queue manager

# Generated at 2022-06-13 07:01:43.067532
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action_loader.add_directory(DATA_DIR)
    module_loader.add_directory(DATA_DIR)
    module_loader.set_cwd(DATA_DIR)
    collection_loader.update_collections()


# Generated at 2022-06-13 07:01:54.057181
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'include_role': {'name': 'test_name'}, 'tasks': {'action': 'action'}, 'handlers': {'action': 'action'}, 'pre_tasks': {'action': 'action'}}
    # Exception raised:
    # AnsibleAssertionError: the type of 'task_ds' should be a dict, but is a <class 'dict'>
    module_args_parser = ModuleArgsParser(task_ds)
    module_args_parser.parse(skip_action_validation=False)
# end class ModuleArgsParser

# The following methods are currently at the playbook level, but should be moved to the task level:
# _validate_tags_skip_tags
# _get_task_vars
# _get_task_type
# _load_tags_skip_tags


# Generated at 2022-06-13 07:01:56.068484
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Tests for method parse of class ModuleArgsParser
    # FIXME: Unittest skipped
    pass

# Generated at 2022-06-13 07:02:04.408555
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:05.311904
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass # place holder for test

# Generated at 2022-06-13 07:02:07.113881
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME: write integration test here; this is just a unit test stub
    raise NotImplementedError


# Generated at 2022-06-13 07:02:10.318909
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_parser = ModuleArgsParser()

    task_ds = {'delegate_to': 'localhost',
     'local_action': 'debug: var=test'}
    skip_action_validation = False
    action, args, delegate_to = module_arg_parser.parse(task_ds, skip_action_validation)


# Generated at 2022-06-13 07:02:24.649889
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    loader_mock = mock.MagicMock()
    # prepare the input data
    task_ds = {}
    collection_list = []
    mg = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    # expected
    expected_action = None
    expected_args = dict()
    expected_delegate_to = None

    # act
    (actual_action, actual_args, actual_delegate_to) = mg.parse()

    # assert
    assert actual_action == expected_action
    assert actual_args == expected_args
    assert actual_delegate_to == expected_delegate_to

# Generated at 2022-06-13 07:02:26.132038
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # TODO: write unit test
    assert True
    return True


# Generated at 2022-06-13 07:02:34.561642
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mock_task_dict = {
        'name': 'test_task',
        'action': 'command',
        'args': {
            'echo': True,
            'creates': '/tmp/test.txt',
            'removes': ['/tmp/*test*', '/tmp/*test*'],
            'executable': '/bin/bash',
            "warn": True
        },
        'other_param': {
            'shell': '/bin/bash',
            'creates': '/tmp/test.txt',
            'removes': ['/tmp/*test*', '/tmp/*test*'],
            'executable': '/bin/bash',
            "warn": True
        }
    }

    mock_action = 'command'

# Generated at 2022-06-13 07:02:40.175040
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:43.787927
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    dso = AnsibleDummyClass()
    task_ds = {'x':1}
    obj = ModuleArgsParser(dso, task_ds)
    assert obj.parse() == (None, {}, None)

# Generated at 2022-06-13 07:02:55.254936
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test basic usage of the parser
    from ansible.playbook.play_context import PlayContext
    play_context = PlayContext()
    task_ds = {}
    collection_list = None
    args_parser = ModuleArgsParser(task_ds, collection_list)
    action, args, delegate_to = args_parser.parse()
    assert action == None
    assert args == {}
    assert delegate_to == None

    # Test basic usage of the parser
    task_ds = {
        'action': 'remote_tmp'
    }
    collection_list = None
    args_parser = ModuleArgsParser(task_ds, collection_list)
    action, args, delegate_to = args_parser.parse()
    assert action == 'remote_tmp'
    assert args == {'_raw_params': ''}
    assert delegate_

# Generated at 2022-06-13 07:03:02.236908
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'command': 'echo hi', 'chdir': '/tmp'}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    assert ['echo hi', {'chdir': '/tmp'}, None] == parser.parse()
    # Unit test for method parse of class ModuleArgsParser
    task_ds = {'action': 'copy src=a dest=b'}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    assert ['copy', {'src': 'a', 'dest': 'b'}, None] == parser.parse()
    # Unit test for method parse of class ModuleArgsParser
    item = 'action'
    collection_list = None

# Generated at 2022-06-13 07:03:04.250048
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # No need to test, as it is a wrapper function
    pass

# Generated at 2022-06-13 07:03:06.936753
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():  # TODO
    '''
    Unit test for method parse of class ModuleArgsParser
    
    
    '''
    pass



# ===========================================
# Subclass: MetaTask


# Generated at 2022-06-13 07:03:11.546679
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(loader)
    action, args, delegate_to = parser.parse(skip_action_validation=True)
    assert action == 'wait_for'
    assert args['connect_timeout'] == 10
    assert delegate_to == 'localhost'

# Generated at 2022-06-13 07:03:26.858882
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_parser = ModuleArgsParser(task_ds=dict())
    assert args_parser.parse() == (None, {}, Sentinel)

    task_ds = {'module': 'shell'}
    args_parser = ModuleArgsParser(task_ds=task_ds)
    assert args_parser.parse() == ('shell', {}, None)

    task_ds = {'module': 'shell', 'args': 'pwd'}
    args_parser = ModuleArgsParser(task_ds=task_ds)
    assert args_parser.parse() == ('shell', {'_raw_params': 'pwd'}, None)

    task_ds = {'module': 'shell', 'args': {'chdir': '/tmp'}}
    args_parser = ModuleArgsParser(task_ds=task_ds)
    assert args_parser.parse()

# Generated at 2022-06-13 07:03:39.628639
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args = '''{'delegate_to': None, 'register': 'logger_result', 'action': 'command', 'local_action': 'command', 'args': {'_raw_params': '{{ abc }}', '_uses_shell': True, 'chdir': None}, 'ignore_errors': False, 'warn': True}'''
    task = dict(action='action', delegate_to='localhost', args=dict(chdir='/tmp', args='xyz=1'))
    delegate_to = 'localhost'
    args = dict(chdir='/tmp', args='xyz=1')
    module_args_parser = ModuleArgsParser(task)
    assert module_args_parser.parse() == (action, args, delegate_to)


# Generated at 2022-06-13 07:03:46.297826
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Positive test, is an AnsibleTask object
    # No parameters
    with pytest.raises(AnsibleParserError):
        ModuleArgsParser().parse()
    # task_ds is not an AnsibleTask
    with pytest.raises(AnsibleAssertionError):
        ModuleArgsParser('task_ds').parse()
    # task_ds is a valid AnsibleTask
    task_ds = {'action': 'copy', 'src': 'a', 'dest': 'b'}
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    assert module_args_parser.parse() == ('copy', {'dest': 'b', 'src': 'a'}, None)
    # task_ds is a valid AnsibleTask dictionary

# Generated at 2022-06-13 07:03:50.413199
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    task = Task()
    map = ModuleArgsParser(task._attributes, collection_list=Config().get_collections_paths()).parse()
    assert map == (None, {}, None)

# Generated at 2022-06-13 07:04:01.952230
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # create mock objects
    # FIXME: create more mock object if needed
    mock_loader = Mock()

    # create the object under test
    module_args_parser = ModuleArgsParser(collection_list=mock_loader)

    # set return values of mock objects
    # FIXME: set return values of more mock object if needed
    mock_loader.find_plugin_with_context.side_effect = [("", ""), ("", ""), ("", "")]

    # do the test
    # FIXME: create more testcases if needed
    task_ds = {}
    assert_equal(module_args_parser.parse(task_ds), (None, {}, None))

    task_ds = {"action": "shell", "x": "y"}

# Generated at 2022-06-13 07:04:02.523045
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# Generated at 2022-06-13 07:04:08.624866
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    task_ds =  {'args': {}, 'delegate_to': 'localhost', 'local_action': 'copy src=a dest=b'}
    module_args_parser._task_ds = task_ds
    result = module_args_parser.parse()
    assert result == ('copy', {'src': 'a', 'dest': 'b'}, 'localhost')



# Generated at 2022-06-13 07:04:22.874018
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test for method parse
    :return:
    """

    yaml_file = "../docs/yaml_spec/task_spec.yaml"
    task_spec = get_yaml_object(yaml_file, TaskSpec)
    param_spec_generated = task_spec.get_param_spec()

    for task_def in task_spec.task_defs:
        task_dict = task_def.task_dict
        module_args_parser = ModuleArgsParser(task_dict)

        (action, args, delegate_to) = module_args_parser.parse()
        action = to_text(action)
        if action in param_spec_generated:
            param_spec = param_spec_generated[action]


# Generated at 2022-06-13 07:04:32.128998
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = {'action': 'copy module=copy src=a dest=b'}
    loader = DictDataLoader({})
    variable_manager = VariableManager(loader=loader)
    mp = ModuleArgsParser(task_ds=ds)
    action, args, delegate_to = mp.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b', 'module': 'copy'}
    assert delegate_to == Sentinel

    ds = {'action': 'copy arg1=a arg2=b'}
    mp = ModuleArgsParser(task_ds=ds)
    action, args, delegate_to = mp.parse()
    assert action == 'copy'
    assert args == {'arg1': 'a', 'arg2': 'b'}
    assert delegate_to == Sentinel

# Generated at 2022-06-13 07:04:41.313118
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  MOCK_ANSIBLE_MODULES_PATH = 'tests/modules'
  MOCK_COLLECTIONS_PATH = 'tests/collections'

  #given
  task_ds = { 'action': 'copy_test src=a dest=b some_param=c', 'args': {'_raw_params':'', 'some_other_param':'d'} }
  expected_return = ('copy_test', {'src': 'a', 'dest': 'b', 'some_param': 'c', 'some_other_param': 'd'}, Sentinel)
  collection_list = None

  #when
  module_args_parser = ModuleArgsParser(task_ds, collection_list)
  actual_return = module_args_parser.parse()

  #then
  assert actual_return == expected_return


# Generated at 2022-06-13 07:04:59.803135
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # legacy=True
    task_ds_1 = {}
    task_ds_2 = {
        'action': {
            'use_shell': True,
            'args': 'echo hello'
        },
        'delegate_to': 'bob'
    }
    task_ds_3 = {
        'action': {
            'module': 'copy',
            'args': 'foo=bar bar=foo'
        }
    }
    task_ds_4 = {
        'action': {
            'module': 'copy',
            'args': 'foo=bar bar=foo',
            '_ansible_check_mode': True
        }
    }

# Generated at 2022-06-13 07:05:14.475685
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=InventoryManager(loader=loader))
    play_context = PlayContext()

    parser = ModuleArgsParser(task_ds=None, collection_list=None)
    res = parser.parse(skip_action_validation=False)
    assert ('action' not in res)
    assert ('args' not in res)
    print(res)
    assert ('delegate_to' not in res)

    task_ds = {}
    parser = ModuleArgsParser(task_ds, collection_list=None)
    res

# Generated at 2022-06-13 07:05:25.691834
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = """
    - name: Test task
      action:
        module: copy
        args:
          src: a
          dest: b
          other:
            with: 'foo'
            _raw_params: 'sudo rm -rf {{ hostvars[inventory_hostname].ansible_env.HOME }}'
              """
    task_ds = {
        'name': 'Test task',
        'action': {
            'module': 'copy',
            'args': {
                'src': 'a',
                'dest': 'b',
                'other': {
                    'with': 'foo',
                    '_raw_params': 'sudo rm -rf {{ hostvars[inventory_hostname].ansible_env.HOME }}',
                }
            }
        }
    }

# Generated at 2022-06-13 07:05:30.322293
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with pytest.raises(AnsibleError) as excinfo:
        task_ds = {}
        #call method
        ModuleArgsParser(task_ds = task_ds).parse()
    assert 'no module/action detected in task.' in to_native(excinfo.value)


# Generated at 2022-06-13 07:05:32.788608
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Note: cannot be unit tested easily currently, 
    #       functionality is too intertwined with its usage from the Playbook class.
    pass


# Generated at 2022-06-13 07:05:47.531490
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}

    # Testing module and action specified (new style)
    task_ds = dict(
        name='testing parse',
        shell=dict(
            _raw_params='echo "{{ test }}"',
            creates='/tmp/{{ test }}',
            chdir='/tmp'
        )
    )
    task = ModuleArgsParser(task_ds, collection_list=None).parse()
    assert dict(action='shell', args={'_raw_params': 'echo "{{ test }}"', 'creates': '/tmp/{{ test }}', 'chdir': '/tmp'}, delegate_to=None) == task

    # Testing module specified, no action specified (new style)

# Generated at 2022-06-13 07:05:54.178248
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = dict(ping=dict(data='hello'))
    loader = DictDataLoader({})
    for collection_list in (None, ['col1'], ['col2']):
        for skip_action_validation in [True, False]:
            module_args_parser = ModuleArgsParser(ds, collection_list=collection_list)
            action, args, delegate_to = module_args_parser.parse(skip_action_validation=skip_action_validation)
            assert action == 'ping'
            assert args == dict(data='hello')
            assert delegate_to is Sentinel
    del loader
    del module_args_parser


# NOTE: see the private test_module_args method below for a more thorough test

# Generated at 2022-06-13 07:05:56.420072
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test ModuleArgsParser parse method
    module = ModuleArgsParser()
    res = module.parse()
    assert(res[0] == '')

# Generated at 2022-06-13 07:06:03.028879
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # set up vars
    task_ds = {'action': '', 'local_action': None, 'delegate_to': '', 'args': {}}
    collection_list = None

    instance = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    # call method under test
    (action, args, delegate_to) = instance.parse(skip_action_validation=False)

    # assert methods called correctly
    assert action is None
    assert args == {}
    assert delegate_to is Sentinel


# Generated at 2022-06-13 07:06:07.938988
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    # Testing with:
    # {'action': 'x', 'delegate_to': 'localhost'}
    # Expected result:
    # ('x', {}, 'localhost')
    task_ds = {'action': 'x', 'delegate_to': 'localhost'}
    result = module_args_parser.parse(task_ds=task_ds)
    assert result == ('x', {}, 'localhost')


# Generated at 2022-06-13 07:06:25.051526
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import Sequence
    import pytest

    # Need to provide read access to valid_attrs in tests
    for cls in [Task, Handler]:
        cls._valid_attrs = cls.validate_attributes
        cls.validate_attributes = lambda x: x

    test_module_name = 'test_module'

    # Test a task from different Ansible forms
    # action: <module>
    task_ds = {}
    task_ds['action'] = test_module_

# Generated at 2022-06-13 07:06:34.003457
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test ModuleArgsParser.parse
    # Check handling of module name in action.
    raw_task = { 'action': { 'module': 'copy',
                             'dest': 'test',
                             'src': 'blah' } }
    task = ModuleArgsParser(raw_task).parse()
    assert task.action == 'copy'
    assert task.args == { 'dest': 'test',
                          'src': 'blah' }
    assert task.delegate_to is None
    assert task.unamed_module_vars == ''
    
    # Check handling of module name in module.
    raw_task = { 'copy': { 'dest': 'test',
                           'src': 'blah' } }
    task = ModuleArgsParser(raw_task).parse()
    assert task.action == 'copy'
   