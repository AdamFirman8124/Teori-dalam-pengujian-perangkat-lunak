

# Generated at 2022-06-13 06:56:45.141549
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """Test the parse method of class ModuleArgsParser"""
    assert ModuleArgsParser()



# Generated at 2022-06-13 06:56:53.189093
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    import ansible.constants as C
    import ansible.utils.vars
    import os
    import pytest
    import yaml
    
    ansible_vars = ansible.utils.vars.VariableManager()
    templar = Templar(loader=None, variables=ansible_vars)
    action_loader = action_loader.ActionModuleLoader('./lib/ansible/modules/', './lib/ansible/modules/extras/')
    module_loader = module_loader.ModuleLoader('./lib/ansible/modules/')

# Generated at 2022-06-13 06:57:04.654399
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with pytest.raises(AnsibleParseError) as excinfo:
        ModuleArgsParser({'action': 'doesnotexist'}).parse()

    excinfo.match('couldn\'t resolve module/action')

    with pytest.raises(AnsibleParseError) as excinfo:
        ModuleArgsParser({'action': 'ping', 'doesnotexist': True}).parse()

    excinfo.match('conflicting action statements')

    action, argspec, delegate_to = ModuleArgsParser({'action': 'command'}).parse()
    assert action == 'command'
    assert argspec == {}
    assert delegate_to is None

    action, argspec, delegate_to = ModuleArgsParser({'action': 'ping'}).parse()
    assert action == 'ping'
    assert argspec == {}

# Generated at 2022-06-13 06:57:14.577838
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    runner = ActionModule().runner
    task_ds = runner.load_from_file('./test/integration/targets/module_arguments/module_args_parser/old-style_action-module_args.yml')
    obj = ModuleArgsParser(task_ds, collection_list=[])
    action, args, delegate_to = obj.parse()
    assert action == 'win_ping'
    assert delegate_to is None
    assert args == {'data': 'ping'}
    task_ds = runner.load_from_file('./test/integration/targets/module_arguments/module_args_parser/old-style_action-module_args-with_raw_args.yml')
    obj = ModuleArgsParser(task_ds, collection_list=[])
    action, args, delegate_to

# Generated at 2022-06-13 06:57:28.637830
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # create a module_args parse class
    m = ModuleArgsParser()

    ### first check - unify arguments

    # check working with complex args
    task_ds_list = [
        {'action': {'module': 'command', '_raw_params': 'ifconfig -a', '_uses_shell': True, 'chdir': '/tmp'}},
        {'action': 'command ifconfig -a', 'args': {'chdir': '/tmp'}},
        {'action': 'command ifconfig -a', 'chdir': '/tmp'},
        {'action': 'command', '_raw_params': 'ifconfig -a', '_uses_shell': True, 'chdir': '/tmp'}
    ]
    for task_ds in task_ds_list:
        m.resolved_action = None
        a,

# Generated at 2022-06-13 06:57:40.812579
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:41.630047
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

# Generated at 2022-06-13 06:57:46.094172
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # test with AnisbleVaultEncryptedUnicode object
    test_data = AnsibleVaultEncryptedUnicode('''
    - include_vars:
        file: "{{ secrets_file }}"
        name: secrets
      tags:
        - secrets
    ''')
    module_args_parser = ModuleArgsParser(test_data)
    module_args_parser.parse()

    # test with string
    test_data = '''
    - include_vars:
        file: "{{ secrets_file }}"
        name: secrets
      tags:
        - secrets
    '''

# Generated at 2022-06-13 06:57:50.473488
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mock_loader = MagicMock()
    mock_loader.module_loader = 'mock_module_loader'
    mock_loader.action_loader = 'mock_action_loader'

    # Ensure the correct task_ds is passed
    data = dict(action='test_action')
    result = ModuleArgsParser(data, mock_loader).parse()
    assert result[0] == 'test_action'


# Generated at 2022-06-13 06:57:58.543396
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    task_ds = {
        'action': 'action_example',
        'local_action': 'local_action_example',
        'args': 'args_example',
    }

    with pytest.raises(AnsibleError) as excinfo:
        x = ModuleArgsParser(task_ds)
        x.parse()

    # __str__ is the error message
    assert 'action and local_action are mutually exclusive' in str(excinfo.value)

    task_ds = {
        'action': 'action_example',
        'args': 'args_example',
    }

    with pytest.raises(AnsibleParserError) as excinfo:
        x = ModuleArgsParser(task_ds)
        x.parse()

   

# Generated at 2022-06-13 06:58:17.308915
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class AnsibleModule_args(object):
        def __init__(self, argument_spec, bypass_checks=False, no_log=True, check_invalid_arguments=True, mutually_exclusive=None,
                     supports_check_mode=False, required_together=None, required_one_of=None, add_file_common_args=False):
            self.argument_spec = argument_spec
            self.bypass_checks = bypass_checks
            self.no_log = no_log
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually_exclusive = mutually_exclusive or []
            self.supports_check_mode = supports_check_mode
            self.required_together = required_together or []
            self.required_one_of = required_one_of or []


# Generated at 2022-06-13 06:58:24.453553
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds_1 = eval("dict(action='copy', src=dict(), dest=dict())")
    module_args_parser_1 = ModuleArgsParser(task_ds=task_ds_1, collection_list=None)
    assert module_args_parser_1.parse() == ('copy', dict(), Sentinel)
    task_ds_2 = eval("dict(action='file', before=dict())")
    module_args_parser_2 = ModuleArgsParser(task_ds=task_ds_2, collection_list=None)
    assert module_args_parser_2.parse() == ('file', dict(), Sentinel)
    task_ds_3 = eval("dict(action='service', before=dict())")
    module_args_parser_3 = ModuleArgsParser(task_ds=task_ds_3, collection_list=None)


# Generated at 2022-06-13 06:58:31.444945
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action_loader.add_directory(
        path='tests/fixtures/modulerargsparse/action_plugins')
    module_loader.add_directory(
        path='tests/fixtures/modulerargsparse/modules')

    # Test all kinds of valid dict, string inputs
    for test in ModuleArgsParserTestCases:
        task = test['input']
        ans = test['output']
        parsed_action, parsed_args, parsed_delegate_to = ModuleArgsParser(task_ds=task).parse()
        assert parsed_action == ans['action'], "Error in case: " + test['name']
        assert parsed_args == ans['args'], "Error in case: " + test['name']
        assert parsed_delegate_to == ans['delegate_to'], "Error in case: " + test['name']

   

# Generated at 2022-06-13 06:58:38.526302
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit tests for parse method of the ModuleArgsParser
    """
    #test
    args = dict(
        collection_list = [],
        task_ds = {
            'ec2': {
                'region': 'xyz'
            }
        }
    )
    module_args_parser = ModuleArgsParser(**args)
    expected = ( 'ec2', { 'region': 'xyz' }, None )
    actual = module_args_parser.parse()
    assert (expected == actual)


# Generated at 2022-06-13 06:58:42.114312
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task # local import

    task = Task()
    module = ModuleArgsParser(task_ds=task)
    try:
        module.parse()
    except AnsibleParserError as e:
        assert True
        print(e.message)



# Generated at 2022-06-13 06:58:50.022295
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_parser = ModuleArgsParser(task_ds={'action': 'shell echo hi'})
    assert module_parser.parse() == ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, None)

    module_parser = ModuleArgsParser(task_ds={'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}})
    assert module_parser.parse() == ('copy', {'dest': 'b', 'src': 'a'}, None)

    with pytest.raises(AnsibleParserError):
        module_parser = ModuleArgsParser(task_ds={'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}, 'local_action': 'echo hi'})
        module_parser.parse()


# Generated at 2022-06-13 06:58:56.750541
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    
    ds = dict(action=dict(module='shell', args='echo hi'))
    ds['action'].update(local_action=dict(module='shell', args='echo hi'))
    
    mp = ModuleArgsParser(task_ds=ds)
    result = mp.parse()
    assert len(result) == 3
    assert result[0] == 'shell'
    assert result[1] == dict(args='echo hi')
    assert result[2] == 'localhost'
    
    ds = dict(action=dict(shell=dict(args='echo hi')))
    ds['action'].update(local_action=dict(shell=dict(args='echo hi')))
    
    mp = ModuleArgsParser(task_ds=ds)
    result = mp.parse()

# Generated at 2022-06-13 06:59:07.296127
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = dict(
        name="sample plugin",
        action=dict(
            module="command",
            args=dict(
                chdir="/tmp",
                warn=False,
                stdout=True,
                pwd="{{lookup('env','PWD')}}"
            )
        )
    )
    arguments_spec = dict()
    delegate_to = None
    collection_list = list()
    # Use the class to parse the module args
    parser = ModuleArgsParser(task_ds=ds, collection_list=collection_list)
    action, args, delegate_to = parser.parse()
    assert action == 'command' and args == {'chdir': '/tmp', 'warn': False, 'stdout': True, 'pwd': "{{lookup('env','PWD')}}"} and delegate_to is None

# Generated at 2022-06-13 06:59:14.921707
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class_name = 'ModuleArgsParser'
    task_ds1 = dict(
        action = dict(
            module = 'shell echo hi'
        )
    )
    collection_list1 = None
    module_args_parser1 = ModuleArgsParser(task_ds=task_ds1, collection_list=collection_list1)
    # does not raise an error
    module_args_parser1.parse(skip_action_validation=True)


# Generated at 2022-06-13 06:59:23.251257
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    runner = TaskExecutor(module_loader=module_loader, variable_manager=variable_manager, all_vars=dict())
    test_task = dict(
        action=dict(
            module='setup',
            args=dict(
                gather_facts="no"
            )
        ),
        with_items=[
            1, 2, 3, 4, 5
        ],
        changed_when=False,
        register=dict(
            result='{{ out }}'
        )
    )
    parser = ModuleArgsParser(task_ds=test_task, collection_list=None)
    parser.parse()

# Generated at 2022-06-13 06:59:42.097446
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    # The code below is generated by a tool, please do not edit by hand.
    #
    with pytest.raises(AnsibleParserError, match=r"^conflicting action statements: command, shell$"):
        ModuleArgsParser({
            u'action': u'echo hi',
            u'local_action': u'shell echo hello world'
        }).parse()
    with pytest.raises(AnsibleParserError, match=r"^conflicting action statements: shell, command$"):
        ModuleArgsParser({
            u'local_action': u'shell echo hello world',
            u'action': u'echo hi'
        }).parse()

# Generated at 2022-06-13 06:59:53.665611
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test multiple conditions of parse, and make use of function "random.choice" to have a random choice of input or output
    #
    # test with module name included in action property
    action = random.choice(BUILTIN_TASKS)
    test_task_ds1 = {'action': '%s: "%s"' % (action, 'arg1')}
    parser1 = ModuleArgsParser(test_task_ds1)
    parser1.parse()
    # name of action property is randomly chosen from BUILTIN_TASKS

    #
    # test with module name included in local_action property
    local_action = random.choice(BUILTIN_TASKS)
    test_task_ds2 = {'local_action': '%s: "%s"' % (local_action, 'arg1')}
   

# Generated at 2022-06-13 07:00:01.099299
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    ModuleArgsParserInst = ModuleArgsParser(task_ds, collection_list)
    assert isinstance(ModuleArgsParserInst,ModuleArgsParser)

    # Call parse without the mandatory argument
    with pytest.raises(TypeError) as excinfo:
        result = ModuleArgsParserInst.parse()
    assert "parse() missing 1 required positional argument: 'skip_action_validation'" == str(excinfo.value)
# Unit test class for ModuleArgsParser

# Generated at 2022-06-13 07:00:09.736307
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence, MutableSet
    from ansible.module_utils.common.text.converters import to_bytes
    task_ds = {'test': 'value'}
    parser = ModuleArgsParser(task_ds)
    assert parser._split_module_string('module arg1 arg2 arg=2') == ('module', 'arg1 arg2 arg=2')
    assert parser._split_module_string('module') == ('module', '')
    assert parser._split_module_string('module arg1 arg=2') == ('module', 'arg1 arg=2')
    assert parser._split_module_string('module="arg1 arg2 arg=2"') == ('module', 'arg1 arg2 arg=2')
    assert parser._split

# Generated at 2022-06-13 07:00:14.675872
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task_include import TaskInclude

    args = dict(
        name='test1',
        args=dict(
            a=1
        ),
        local_action=dict(
            module='copy',
            dest='/tmp/a',
            src='/tmp/b'
        ),
        delegate_to='127.0.0.1'
    )
    task = TaskInclude(add_role_vars=False, role_name="test1", task_ds=args)
    parser = ModuleArgsParser(task.args)

    assert parser.parse() == ('copy', {'src': '/tmp/b', 'dest': '/tmp/a'}, '127.0.0.1')


# Generated at 2022-06-13 07:00:23.062000
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    loader = DictDataLoader({})
    collection_loader = MockCollectionLoader()
    collection_list = AnsibleCollectionLoader(loader=collection_loader)
    task_ds = {'ignore_errors': True, 'action': {'module': 'a_module', 'key1': 'val1', 'key2': 'val2'}}

    parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    assert parser.parse() == ('a_module', {'key1': 'val1', 'key2': 'val2'}, Sentinel)

    task_ds = {'action': 'a_module'}
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    assert parser.parse() == ('a_module', {}, Sentinel)


# Generated at 2022-06-13 07:00:34.007306
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test_module_args_parser.py

    # Unit tests for ModuleArgsParser

    # Basic unit tests for the ModuleArgsParser class

    import pytest

    # TODO: More coverage, especially for the bad inputs

    @pytest.fixture
    def loader():
        from ansible.plugins.loader import action_loader
        from ansible.plugins.loader import module_loader
        def loader_fn(name):
            ctx = action_loader.find_plugin_with_context(name)
            if not ctx.resolved:
                ctx = module_loader.find_plugin_with_context(name)
            return ctx

        return loader_fn

    # No args, so just the module itself

# Generated at 2022-06-13 07:00:40.358296
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Test the ModuleArgsParser parser method
    '''
    args = dict(module='shell', _raw_params='echo "hi"')
    task = dict(action=args)
    parser = ModuleArgsParser(task)
    action, args, delegate_to = parser.parse()
    assert action == 'shell'
    assert args == dict(_raw_params='echo "hi"')
    assert delegate_to is None

    task = dict(action='shell echo hi')
    parser = ModuleArgsParser(task)
    action, args, delegate_to = parser.parse()
    assert action == 'shell'
    assert args == dict(_raw_params='echo hi')
    assert delegate_to is None

    action = dict(module='shell', _raw_params='echo "hi"')
    task = dict(action=action)


# Generated at 2022-06-13 07:00:44.637837
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action = dict(
            module='copy',
            src='s',
            dest='d',
            args='arg1=1 arg2=2',
        ),
    )
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert dict(src='s', dest='d') == args, "ModuleArgsParser parse(): args"
    assert 'copy' == action, "ModuleArgsParser parse(): action"
    assert 'localhost' == delegate_to, "ModuleArgsParser parse(): delegate_to"


# Generated at 2022-06-13 07:00:49.292353
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(action='{{ a }}',
                   delegate_to='{{ b }}',
                   args=dict(c='{{ c }}'))
    collection_list = None
    expected_action = '{{ a }}'
    expected_args = dict(c='{{ c }}')
    expected_delegate_to = '{{ b }}'

    mod_args_parser = ModuleArgsParser(task_ds, collection_list)
    actual_action, actual_args, actual_delegate_to = mod_args_parser.parse()

    assert expected_action == actual_action
    assert expected_args == actual_args
    assert expected_delegate_to == actual_delegate_to


# Generated at 2022-06-13 07:00:59.511012
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    data = dict(action='shell',
                delegate_to='some')
    res = ModuleArgsParser(task_ds=data).parse()
    # Check the result is what we expected
    assert res == ('shell', {}, 'some'), \
        "expected \"('shell', {}, 'some')\", got %s" % repr(res)


# Generated at 2022-06-13 07:01:09.714458
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  class FakePlaybookContext(object):
    def __init__(self):
      self.CLIARGS = dict()
      self.basedir = os.path.join(os.path.dirname(__file__), 'test_data', 'playbook')
      self.loader = DataLoader()
  pc = FakePlaybookContext()
  loader = pc.loader
  myfile = open(os.path.join(pc.basedir, 'test_playbook.yaml'))
  task_ds = yaml.load(myfile)['tasks'][0]
  task_ds = {k: (v if isinstance(v, string_types) else dict(v)) for k, v in iteritems(task_ds)}
  p = ModuleArgsParser(task_ds, collection_list=None)
  result = p.parse

# Generated at 2022-06-13 07:01:17.489889
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    # Test the task type 'legacy'
    # test with the form  `action: 'module_name action_args'`
    task_ds = {"action": "shell echo hi"}
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    result = module_args_parser.parse()

# Generated at 2022-06-13 07:01:26.104213
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # build our dependencies
    module_loader._load_plugins()
    action_loader._load_plugins()

    mock_task_ds_1 = {
        "module": "command",
        "args": {"echo": "hi"},
        "name": "shell echo hi"
    }
    mock_task_ds_2 = {
        "module": "shell",
        "args": {"echo": "hi"},
        "name": "shell echo hi"
    }
    mock_task_ds_3 = {
        "module": "command",
        "args": {"echo": "hi"},
        "name": "shell"
    }
    mock_task_ds_4 = {
        "delegate_to": "localhost",
        "module": "shell"
    }

# Generated at 2022-06-13 07:01:31.882675
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    t1 = dict(action='file src=/tmp/a dest=/tmp/b force=no')
    t2 = dict(action=dict(module='file src=/tmp/a dest=/tmp/b force=no'))
    t3 = dict(action=dict(module='file src=/tmp/a dest=/tmp/b', force='no'))
    t4 = dict(action=dict(module='file', src='/tmp/a', dest='/tmp/b', force='no'))
    t5 = dict(file=dict(src='/tmp/a', dest='/tmp/b', force='no'))
    t6 = dict(action='shell echo hi')
    t7 = dict(action='ping')
    t8 = dict(local_action='ping')

# Generated at 2022-06-13 07:01:39.688354
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Data setup
    task_ds = {u'action': {u'module': u'foo', u'key': u'value'}}

    # Test call
    test_obj = ModuleArgsParser(task_ds)
    actual = test_obj.parse()
    assert actual == (u'module', {u'key': u'value'})

    # Data setup
    task_ds = {u'action': {u'module': u'foo', u'_raw_params': u'value'}}

    # Test call
    test_obj = ModuleArgsParser(task_ds)
    actual = test_obj.parse()
    assert actual == (u'module', {u'_raw_params': u'value'})

    # Data setup
    task_ds = {u'action': u'module'}

   

# Generated at 2022-06-13 07:01:45.741642
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    loader = DictDataLoader({})
    collection_loader = PluginLoader(
        '',
        'CollectionModuleLoader',
        C.DEFAULT_COLLECTIONS_PATHS,
        'module_utils'
    )

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='')
    variable_manager.set_inventory(inventory)



# Generated at 2022-06-13 07:01:54.795721
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_parser = ModuleArgsParser()
    skip_action_validation_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fixtures',
        'skip_action_validation_task.yml'
    )
    with open(skip_action_validation_path) as skip_action_validation_file:
        skip_action_validation_task = yaml.safe_load(skip_action_validation_file)
    action1, args1, _ = module_parser.parse(skip_action_validation_task)
    assert action1 == 'test_action'
    assert args1['test_arg'] == 'test_value'
    # testing the use of None as a parameter to ModuleArgsParser.parse()

# Generated at 2022-06-13 07:01:58.949763
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}

    collection_list = []

    obj = ModuleArgsParser(task_ds, collection_list)
    obj.parse()


# class used to hold lists of most recently and most frequently used actions,
# used to provide better TAB completion suggestions

# Generated at 2022-06-13 07:02:05.978400
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    This function automagically gets called when `python -m unittest discover` is run
    on this directory.

    See: https://docs.python.org/3/library/unittest.html#unittest-discover-api
    '''

    class _ModuleArgsParser(ModuleArgsParser):
        pass

    RESOLVED_MODULE_NAME = 'resolved_module_name'

    class MockActionResolver(object):
        def find_plugin_with_context(self, action, collection_list=None):
            resolved = MockResolvedModule(action, collection_list)
            return ActionContext(action, resolved)

    class MockResolvedModule(object):
        def __init__(self, action, collection_list):
            self.action = action
            self.collection_list = collection_list
           

# Generated at 2022-06-13 07:02:16.315296
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:27.074297
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.six import string_types
    from ansible.errors import AnsibleParserError
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_text
    from ansible.module_utils.hashing import ensure_hashable
    # ansible.playbook.task.Task._load_args has been refactored, but tests below still work.
    # If this line is changed however, the test will fail. It is a good check to make sure
    # that the tests are still valid.
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.plugins import action_loader
    from ansible.plugins.loader import module_loader


# Generated at 2022-06-13 07:02:35.114125
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
   #TODO: Update
   parser = ModuleArgsParser(task_ds={'action': 'ec2', 'bob': 'fob', 'delegate_to': 'localhost', 'region': 'xyz'})
   result = parser.parse()
   assert result == ('ec2', {'region': 'xyz'}, 'localhost')

   parser = ModuleArgsParser(task_ds={'local_action': 'copy src=a dest=b'})
   result = parser.parse()
   assert result == ('copy', {'src': 'a', 'dest': 'b'}, 'localhost')

   parser = ModuleArgsParser(task_ds={'local_action': {'module': 'copy', 'src': 'a', 'dest': 'b'}})
   result = parser.parse()

# Generated at 2022-06-13 07:02:40.658219
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task.include import IncludeTask
    from ansible.playbook.task.include import IncludeRole

# Generated at 2022-06-13 07:02:47.925560
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test for method parse of class ModuleArgsParser
    """


    # create the dummy objects for testing
    test_task_ds = {}
    test_collection_list = {}

    # create object and call method parse
    test_module_args_parser = ModuleArgsParser(task_ds=test_task_ds, collection_list=test_collection_list)
    test_module_args_parser.parse()



# Generated at 2022-06-13 07:02:58.073031
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:03:09.565142
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.mod_args import ModuleArgsParser
    class_ = ModuleArgsParser

    action = 'ping'
    args = 'hello'
    delegate_to = 'localhost'

    task_ds = {
        'action': args,
        'delegate_to': delegate_to
    }

    x = class_(task_ds=task_ds)

    assert isinstance(x.parse(), tuple)
    assert set(['action', 'args', 'delegate_to']) == set(x.parse())
    assert x.parse()[0:2] == (action, args)
    assert delegate_to == x.parse()[2]


if __name__ == '__main__':
    # Unit test
    configure_logging(logging.DEBUG)
    unittest.main()

# Generated at 2022-06-13 07:03:18.810498
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    variable_manager = VariableManager()
    variable_manager._extra_vars = {}

    variable_manager.set_inventory(Inventory(loader=None, variable_manager=variable_manager, host_list=['test_host_0']))
    variable_manager.add_group('group_1')
    variable_manager.add_host(Host(name='test_host_0'))
    variable_manager.get_group('group_1').add_host(variable_manager.get_host('test_host_0'))

   

# Generated at 2022-06-13 07:03:22.288244
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'action': 'copy src=test dest=test2',
        'delegate_to': 'localhost',
        'args': {
            'test': 'a'
        }
    }

    expected = ('copy', {
        'src': 'test',
        'dest': 'test2',
        'test': 'a'
    }, 'localhost')
    actual = ModuleArgsParser(task_ds).parse()
    assert actual == expected


# Generated at 2022-06-13 07:03:37.381155
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    # Init a task data structure
    task_ds = {
            'shell':'echo hi',
            'args': { 'chdir': '/tmp' }
    }

    # Init a ModuleArgsParser class
    mapa = ModuleArgsParser(task_ds)

    # Call method parse()
    action, args, delegate_to = mapa.parse()

    # Test if the method parse() is executed successfully
    assert action == "shell", "The action is wrong. The correct answer should be shell."
    assert args == {'_raw_params': 'echo hi', 'chdir': '/tmp'}, "The args is wrong."
    assert delegate_to is None, "The delegate_to should be None."

    # Init a task data structure

# Generated at 2022-06-13 07:03:48.178987
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def new_style_parser(ds):
        '''
            Returns a valid (action, args, delegate_to) tuple
        '''
        parser = ModuleArgsParser(ds)
        return parser.parse()

    def old_style_parser(ds):
        '''
            Returns a valid (action, args, delegate_to) tuple
        '''
        parser = ModuleArgsParser(ds)
        return parser.parse()

    # valid new invocation
    assert new_style_parser({'module': 'shell', '_raw_params': 'echo hi', '_uses_shell': True}) == \
               ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, Sentinel())

    # valid old invocation

# Generated at 2022-06-13 07:03:59.315500
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("----------- test_ModuleArgsParser_parse --------------")

    def dict_equal(d1, d2):
        if d1 == d2:
            return True
        elif len(d1) != len(d2):
            return False
        else:
            for k, v in iteritems(d1):
                if k not in d2:
                    return False
                elif d2[k] != v:
                    return False
            for k, v in iteritems(d2):
                if k not in d1:
                    return False
                elif d1[k] != v:
                    return False
            return True

    def assert_parse_result(task_ds, expected_action, expected_args, expected_delegate_to):
        ap = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 07:04:09.257285
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'action': 'command',
        'args': {
            'executable': 'bash'
        }
    }
    # validate the content of the dictionary
    assert 'action' in task_ds
    assert 'args' in task_ds
    assert 'executable' in task_ds['args']
    assert task_ds['action'] == 'command'
    assert task_ds['args']['executable'] == 'bash'
    # validate the type of the dictionary key and value
    assert isinstance(dict(task_ds), dict)
    assert isinstance(task_ds['action'], str)
    assert isinstance(task_ds['args'], dict)
    assert isinstance(task_ds['args']['executable'], str)

    action = task_ds['action']

# Generated at 2022-06-13 07:04:22.475606
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_string = "shell"
    test_string2 = "shell echo hi"
    test_dict = {'module': 'copy', 'src': 'a', 'dest': 'b'}
    test_dict2 = {'module': 'command', 'chdir': '/tmp'}
    test_dict3 = {'module': 'command', 'args': {'chdir': '/tmp'}}

    print()
    print("Testing ModuleArgsParser.parse()...")
    for test_case in [test_string, test_string2, test_dict, test_dict2, test_dict3]:
        result = ModuleArgsParser(test_case).parse()
        print(result)

test_ModuleArgsParser_parse()


# Generated at 2022-06-13 07:04:23.891711
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
	pass


# Generated at 2022-06-13 07:04:32.579557
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:38.714238
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = {'module': 'shell < /dev/null', 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=args)
    actual_result = parser.parse()

    expected_result = ('shell', {}, 'localhost')
    assert expected_result == actual_result, "Actual resulting tuple of `parser.parse()` is `%r` but we expected `%r`" % (
        actual_result, expected_result
    )

# Generated at 2022-06-13 07:04:45.546216
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    load_module = lambda: None

    def validate_common_attributes(module_name):
        module_name = to_bytes(module_name, errors='surrogate_or_strict')
        mod = load_module()
        mod.check_mode = False
        mod._name = module_name
        mod.no_log = True
        mod.no_log_values = list()
        mod.params = dict()
        mod.changed = False
        mod.warnings = list()
        mod.deprecations = list()

# Generated at 2022-06-13 07:04:48.199011
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    c = ModuleArgsParser({'module': 'setup'})
    result = c.parse()
    assert result == ('setup', {}, None)


# Generated at 2022-06-13 07:04:59.175397
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext

    mock_task_ds = dict(
        name='test_task_name',
        action=dict(
            module='echo',
            args=dict(
                _raw_params='"{{ test_task_name }}"',
                _uses_shell=True,
            )
        ),
        delegate_to='localhost',
        become=False,
        become_user='root',
        async_val=0,
        poll=0,
        when=''
    )

    ModuleArgsParser(task_ds=mock_task_ds).parse()


# Generated at 2022-06-13 07:05:12.888559
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """Test :meth:`ansible.module_utils.common._ModuleArgsParser.parse`
    of :class:`ansible.module_utils.common._ModuleArgsParser`.
    """
    action = 'test'
    task_ds = {'test': 'test'}
    args = {}
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == (action, args, None)

# class ModuleArgsParser ends


# Generated at 2022-06-13 07:05:25.599298
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    source = {
        'action':'copy some more',
        'delegate_to':'localhost',
        'args': {'_ansible_foo':'bar'}
    }
    expected = ['copy', 'some more', 'localhost']
    module_args_parser = ModuleArgsParser(source)
    result = module_args_parser.parse()
    assert expected == result

    source = {
        'action':'copy: src=a dest=b',
        'delegate_to':'localhost',
        'args': {'_ansible_foo':'bar'}
    }
    expected = ['copy', {'_ansible_foo': 'bar', 'dest': 'b', 'src': 'a'}, 'localhost']
    module_args_parser = ModuleArgsParser(source)
    result = module_args_parser

# Generated at 2022-06-13 07:05:35.422239
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task = dict()

    task['action'] = {
      "arg1": "value1",
      "arg2": "value2",
    }

    module_name, args, delegate_to = ModuleArgsParser(task).parse()

    assert module_name == None
    assert args == None
    assert delegate_to == None


    task['action'] = 'shell echo'

    module_name, args, delegate_to = ModuleArgsParser(task).parse()

    assert module_name == None
    assert args == None
    assert delegate_to == None


    task['action'] = {
      "module": 'shell echo1',
      "arg1": "value1",
      "arg2": "value2",
    }

    module_name, args, delegate_to = ModuleArgsParser(task).parse()

    assert module_

# Generated at 2022-06-13 07:05:43.665788
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
    m = ModuleArgsParser(task_ds=task_ds)
    return_value = m.parse()
    assert type(return_value) is tuple
    assert len(return_value) == 3
    v1, v2, v3 = return_value
    assert type(v1) is NoneType
    assert type(v2) is dict
    assert type(v3) is type(Sentinel())

# Generated at 2022-06-13 07:05:52.721055
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:06:02.163970
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Setup a task object
    task_dict = { 'action': 'a',
                  'args': 'b',
                  'delegate_to': 'c',
                  'action_tmp': 'd',
                  'with_items': [1,2,3],
                  'with_dict': {'a': 1},
                  'local_action': 'e',
                  'unknown_attr': 'f' }
    parser = ModuleArgsParser(task_ds=task_dict)

    # Check the result of the parse() method
    action, args, delegate_to = parser.parse()
    assert action == 'a'
    assert args == 'b'
    assert delegate_to == 'c'

# Generated at 2022-06-13 07:06:14.399184
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class module_loader_mock:
        def find_plugin_with_context(self, item, collection_list):
            class _resolved_mock:
                resolved = True
                resolved_fqcn = True
                redirect_list = True
            return _resolved_mock()

    class AnsibleParserError_mock:
        def __init__(self, message, obj):
            self.message = message
            self.obj = obj

    class Templar_mock:
        def is_template(self, raw_params):
            if raw_params == 'echo hi':
                return False
            return True

    class AnsibleError_mock:
        def __init__(self, message):
            self.message = message


# Generated at 2022-06-13 07:06:19.689311
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_name = 'read_vault'
    _task_ds = {module_name: {'path': '~/secrets.yaml', 'password_file': '~/.vault_pass.txt', 'dest': 'secrets_var'}}
    _task_ds_multiple_modules = {'copy': {'src': 'file', 'dest': 'destfile'}, 'read_vault': {'path': '~/secrets.yaml', 'password_file': '~/.vault_pass.txt', 'dest': 'secrets_var'}}
    _task_ds_invalid_for_read_vault = {'read_vault': 'some_param'}

# Generated at 2022-06-13 07:06:26.184988
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    task1 = { 'action': 'shell $SHELL_OPTIONS', 'args': 'foo=bar baz=qux'}
    task2 = { 'action': 'set_fact', 'value': 'ansible_distribution'}
    task3 = { 'action': 'copy', 'dest': 'value'}
    task4 = { 'action': 'shell echo hi', 'args': {'_raw_params': 'echo hi'}}
    task5 = { 'action': 'shell echo hi', 'args': {'_raw_params': 'echo hi', 'foo': 'bar'}}

# Generated at 2022-06-13 07:06:36.265933
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.common._collections_compat import MutableMapping

    ds = dict()
    ds['action'] = dict()
    ds['local_action'] = dict()
    ds['module'] = dict()
    ds['action']['foo'] = dict()
    ds['action']['foo']['_ansible_no_log'] = False
    ds['action']['foo']['_ansible_verbosity'] = 1
    ds['action']['foo']['_ansible_debug'] = False

