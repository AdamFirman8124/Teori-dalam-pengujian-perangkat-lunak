

# Generated at 2022-06-13 06:56:53.948947
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(action=dict(shell='echo hi'))
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser.parse() == ('shell', {'_raw_params': 'echo hi'}, Sentinel)
    task_ds = dict(action='shell echo hi')
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser.parse() == ('shell', {'_raw_params': 'echo hi'}, Sentinel)
    task_ds = dict(local_action='shell echo hi')
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser.parse() == ('shell', {'_raw_params': 'echo hi'}, 'localhost')
    task_ds = dict(local_action='shell echo hi', delegate_to='otherhost')
    parser = Module

# Generated at 2022-06-13 06:57:04.899286
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:14.776806
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import VaultPassword
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.path import unfrackpath
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager  
    # create the global vault director
    vault_secret = VaultSecret(VaultPassword('test'))
    vault = VaultLib(vault_secret)
    loader = DataLoader()

# Generated at 2022-06-13 06:57:23.672868
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:29.528931
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  # Test when type of task_ds is not a dict
  with pytest.raises(AnsibleAssertionError):
    parser = ModuleArgsParser(task_ds = None)
    parser = ModuleArgsParser(task_ds = [])
    parser = ModuleArgsParser(task_ds = "")

  class TestTask(object):
    _valid_attrs = ['test_attr']
  class TestMod(object):
    class Attribute(object):
      def __init__(self, *args, **kwargs):
        pass
      _valid_attrs = ['test_attr']
      def load(self, *args, **kwargs):
        pass
      def assert_not_in_final(self, *args, **kwargs):
        pass

# Generated at 2022-06-13 06:57:41.614484
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.playbook.task_include
    import ansible.playbook.task_static
    task_ds = {'name': 'test', 'action': 'shell echo foo', 'connection': 'local', 'args': {'echo': 'xyz', 'creates': '/tmp/somefile'}}
    task = ansible.playbook.task_include.TaskInclude(load_from=task_ds, block=dict(), role=None, task_include=None)
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    parser_result_tuple = module_args_parser.parse(skip_action_validation=False)
    assert parser_result_tuple[0] == 'shell'

# Generated at 2022-06-13 06:57:55.324682
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.role import Role

    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play as Play_object

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    from ansible.playbook.included_file import IncludedFile


# Generated at 2022-06-13 06:58:03.037579
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Case: Delegate 'localhost' as delegate_to, but action is not present
    task_ds = {}
    collection_list = []

    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    result = module_args_parser.parse()

    assert len(result) == 3
    assert result[0] == 'ping'
    assert result[1] == {}
    assert result[2] == 'localhost'

    # Case 2: Delegate 'localhost' as delegate_to and action is present
    task_ds = {'action': {'module': 'copy', 'args': 'src=a dest=b'}}
    collection_list = []

    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    result = module_args_parser.parse()

    assert len(result)

# Generated at 2022-06-13 06:58:10.340138
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    unit test to validate ModuleArgsParser
    '''

    # 1. Install prereq roles
    runner = CliRunner()
    result = runner.invoke(cli.cli, [
        'galaxy', 'install', '-r', 'test/unit/galaxy_install_requirements.yml'
    ])
    assert result.exit_code == 0, result.output

    # 2. Load yaml files
    tasks_ds = load_yaml('test/unit/playbooks/playbook-test_module_args.yml')
    task_ds = tasks_ds['tasks'][0]
    # task_ds = tasks_ds['tasks'][1]
    # task_ds = tasks_ds['tasks'][2]
    # task_ds = tasks_ds['tasks'][3]


# Generated at 2022-06-13 06:58:16.903958
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def _test(arg_type, action, args, expected_action, expected_args, expected_error=None, expected_exception=None):
        if expected_error is None and expected_exception is None:
            # normal case
            task_ds = {
                action: arg_type,
            }
            if args is not None:
                task_ds[action] = dict(task_ds[action], **args)
            task_ds = {
                'action': task_ds,
            }
            module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)
            result_action, result_args, result_delegate_to = module_args_parser.parse()
            assert result_action == expected_action
            assert result_args == expected_args
            assert result_delegate_

# Generated at 2022-06-13 06:58:33.286488
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # WIP
    # Need to write this method to test that the ModuleArgsParser class successfully returns the action, args and
    # delegate_to when given a task in one of the supported forms.
    pass

# Generated at 2022-06-13 06:58:43.650200
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = {u'module': u'set_fact', u'ansible_ssh_user': u'root', u'ansible_ssh_host': u'{{inventory_hostname}}', u'delegate_to': u'{{_machine_ip}}', u'x': 1, u'y': 1, u'z': 1, u'_raw_params': u'ansible_ssh_user=root ansible_ssh_host={{inventory_hostname}} delegate_to={{_machine_ip}}'}

# Generated at 2022-06-13 06:58:58.240524
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_ds = {'action': 'copy', 'foo': 'bar', 'baz': 'qux', 'args': {'extra_args': '1234'}}
    parser = ModuleArgsParser(task_ds=module_ds)
    parser.parse()

    assert parser._split_module_string('copy src=a dest=b') == ('copy', 'src=a dest=b')

    assert parser._normalize_parameters('copy src=a dest=b') == ('copy', {'src': 'a', 'dest': 'b'})
    assert parser._normalize_parameters('copy src=a dest=b', additional_args={'_raw_params': 'foo'}) == ('copy', {'src': 'a', 'dest': 'b', '_raw_params': 'foo'})

    assert parser._normalize_new

# Generated at 2022-06-13 06:59:08.809532
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test_ModuleArgsParser.test_parse()

    # Test with a dictionary for the action
    test1 = {'action': {'module': 'ec2'}}
    task = ModuleArgsParser(task_ds=test1)
    action, args, delegate_to = task.parse()
    assert task.resolved_action == 'ansible.builtin.ec2'
    assert action == 'ec2'
    assert args == {}
    assert delegate_to is None

    # Test with a dictionary for the action and local_action
    test2 = {'action': {'module': 'ec2'}, 'local_action': {'module': 'ec2'}}
    task = ModuleArgsParser(task_ds=test2)
    action, args, delegate_to = task.parse()

# Generated at 2022-06-13 06:59:17.868726
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.utils.vars import combine_vars
    from ansible.vars.reserved import RESERVED_VARS
    from ansible.utils.display import Display
    display = Display()
    # In the following case, the args key is present and is a dict, which is "wrong" according to the method
    # so it should raise an exception
    display.display("Test case 1")
    test_case_1_item = dict()
    test_case_1_item['action'] = dict()
    test_case_1_item['action']['module'] = 'copy'
    test_case_1_item['action']['args'] = dict()
    test_case_1_item['action']['args']['src'] = 'a'

# Generated at 2022-06-13 06:59:23.251239
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    original_task_ds = {'local_action': 'shell echo hi', 'delegate_to': 'localhost'}
    expected_result = ('shell', {'_raw_params': 'echo hi'}, 'localhost')
    actual_result = ModuleArgsParser(original_task_ds).parse()
    assert expected_result == actual_result
# This is the end of class ModuleArgsParser

# Generated at 2022-06-13 06:59:32.190813
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    data = '{"_ansible_position": 1, "_ansible_no_log": false, "_raw_params": "dismounting...", "_ansible_verbosity": 0, "_ansible_diff": false, "_ansible_selective": false, "_ansible_syslog_facility": "LOG_USER", "_ansible_version": {"full": "2.8.2", "major": 2, "minor": 8, "revision": 2, "string": "2.8.2"}, "_ansible_module_name": "raw", "_ansible_debug": false, "changed": true, "_ansible_check_mode": false, "_ansible_debug_traceback": true, "_ansible_forks": 5, "_ansible_module_fingerprint": false}'
    test = ModuleArgsParser(json.loads(data))

# Generated at 2022-06-13 06:59:42.385671
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    ActionModule = namedtuple('ActionModule', ['name', 'action'])
    ActionLoader = namedtuple('ActionLoader', ['action_plugins', '_tasks_per_file'])
    loader = DataLoader()
    # 1 - test with no module_utils

# Generated at 2022-06-13 06:59:46.715602
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser()
    assert m.parse() == (None, None, None)
    # Test with args
    assert m.parse(skip_action_validation=True) == (None, None, None)


# Test stuff for 'now'


# Generated at 2022-06-13 06:59:54.972602
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.executor.task_result
    task_t = type('DummyTask', (object,), dict(action=None, args=None, delegate_to=None))
    task_ds_o = task_t()
    task_ds_o.action = None
    task_ds_o.args = None
    task_ds_o.delegate_to = None
    collection_list = ansible.plugins.loader.ActionModule.all
    parser = ModuleArgsParser(task_ds_o, collection_list)
    # Run the test
    action, args, delegate_to = parser.parse()

# Generated at 2022-06-13 07:00:03.254320
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse(): 
    module_args_parser = ModuleArgsParser(dict(with_items=[dict(shell='echo hi', args=dict(chdir='/tmp'))]))
    module_args_parser.parse()

# Generated at 2022-06-13 07:00:11.206414
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def test_ModuleArgsParser_parse_action_and_local_action_both_exist():
        ds = dict(action="shell wc", local_action="shell echo")
        mp = ModuleArgsParser(ds)
        pytest.raises(AnsibleParserError, mp.parse)

    def test_ModuleArgsParser_parse_action_and_local_action_both_exist_skip_action_validation():
        ds = dict(action="shell wc", local_action="shell echo")
        mp = ModuleArgsParser(ds)
        mp.parse(skip_action_validation=True)

    def test_ModuleArgsParser_parse_action_is_not_string():
        ds = dict(action=dict(module="shell", args="wc"))
        mp = ModuleArgsParser(ds)
        mp.parse

# Generated at 2022-06-13 07:00:16.695155
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    The task_ds is of the form:

    - local_action: shell echo hi

    - copy: src=a dest=b

    - action: copy src=a dest=b

    - copy:
        src: a
        dest: b

    - action:
        module: copy
        args:
          src: a
          dest: b

    Standard YAML form for command-type modules. In this case, the args specified
    will act as 'defaults' and will be overridden by any args specified
    in one of the other formats (complex args under the action, or
    parsed from the k=v string

    - command: 'pwd'
      args:
        chdir: '/tmp'

    Tests for parsing the different task formats for parameters and module
    '''

    # local_action: shell echo hi
   

# Generated at 2022-06-13 07:00:27.324899
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader

    cli = CLI(args=['test'])
    loader = DataLoader()
    cli.options = cli.parse()
    cli.set_play_context(loader=loader, options=cli.options)
    cli._load_plugins()

    # setup
    lookup_plugin_mock = Mock()
    lookup_plugin_mock.run.return_value = 'a'
    task_vars = {'a': 'a', 'b': 'b', 'c': 'c'}
    task_ds = {'action': 'debug', 'args': {'msg': 'a'}}
    templar = Templar(loader=cli._loader)

    # Given a task in one of the supported forms, pars

# Generated at 2022-06-13 07:00:32.730445
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'copy src=a dest=b'}

    m = ModuleArgsParser(task_ds, collection_list=None)
    assert m.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)

# Generated at 2022-06-13 07:00:42.126624
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    inst = ModuleArgsParser(task_ds, collection_list)
    assert isinstance(inst, ModuleArgsParser)

    with pytest.raises(AnsibleParserError):
        inst.parse()

    task_ds = {'args': {}}
    collection_list = None
    inst = ModuleArgsParser(task_ds, collection_list)
    assert isinstance(inst, ModuleArgsParser)

    with pytest.raises(AnsibleParserError):
        inst.parse()

    task_ds = {'action': 'copy src=a dest=b'}
    collection_list = None
    inst = ModuleArgsParser(task_ds, collection_list)
    assert isinstance(inst, ModuleArgsParser)

# Generated at 2022-06-13 07:00:47.722485
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = []
    m = ModuleArgsParser(task_ds, collection_list)
    assert m.parse(True) == (None, None, None)
    m.parse()
    task_ds = {'copy': 'copy src=a dest=b'}
    m = ModuleArgsParser(task_ds, collection_list)
    assert m.parse(True) == ('copy', {'src': 'a', 'dest': 'b'}, None)
    m.parse()
    task_ds = {'local_action': 'copy src=a dest=b'}
    m = ModuleArgsParser(task_ds, collection_list)
    assert m.parse(True) == ('copy', {'src': 'a', 'dest': 'b'}, 'localhost')
    m.parse()
   

# Generated at 2022-06-13 07:00:56.709234
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_spec = dict(
        one=dict(type='str', required=True),
        two=dict(type='str', required=True),
        three=dict(type='str', required=False),
        four=dict(type='str'),
    )
    task_ds = dict(
        action='action_name',
        one='one',
        two='two',
        three='three',
    )
    module_arg_spec.update(task_ds)
    run_task = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = run_task.parse()
    assert action == 'action_name'
    assert args == module_arg_spec

# Generated at 2022-06-13 07:01:01.741907
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action = dict(
            module = 'cowsay',
            args = dict(
                text = 'moo'
            )
        )
    )
    collection_list = None
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    action, args, delegate_to = parser.parse()

    assert action == 'cowsay'
    assert args == dict(text = 'moo')
    assert delegate_to is None



# Generated at 2022-06-13 07:01:12.003043
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    # These are some of the unit test inputs and their outputs

# Generated at 2022-06-13 07:01:19.098547
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # TODO
    raise NotImplementedError()


# The following classes subclass Base, which is a superclass
# of ModuleArgsParser


# Generated at 2022-06-13 07:01:20.238343
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

### utility methods



# Generated at 2022-06-13 07:01:29.203847
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = None
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)

    # test with normal args
    assert obj.parse() == (None, {}, Sentinel)

    # test with args: 'shell' and action
    task_ds = {}
    task_ds['action'] = 'shell'
    obj = ModuleArgsParser(task_ds, collection_list)
    assert obj.parse() == ('shell', {}, Sentinel)

    # test with args: 'b' and action
    task_ds = {}
    task_ds['action'] = 'copy src=a dest=b'
    obj = ModuleArgsParser(task_ds, collection_list)
    assert obj.parse() == ('copy', {'dest': 'b', 'src': 'a'}, Sentinel)

    # test with args

# Generated at 2022-06-13 07:01:37.607956
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds={})
    action, args, delegate_to = parser.parse(skip_action_validation=False)
    assert action is None
    assert args is None
    assert delegate_to is None
    #
    parser = ModuleArgsParser(task_ds={'args': {'arg1': 'foo'}})
    action, args, delegate_to = parser.parse(skip_action_validation=False)
    assert action is None
    assert args == {'arg1': 'foo'}
    assert delegate_to is None
    #
    parser = ModuleArgsParser(task_ds={'action': 'shell echo 1'})
    action, args, delegate_to = parser.parse(skip_action_validation=False)
    assert action == 'shell'

# Generated at 2022-06-13 07:01:44.143018
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({})
    assert parser.parse() == (None, {}, None)
    parser = ModuleArgsParser({'action': 'copy', 'args': 'src=a dest=b'})
    assert parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)
    parser = ModuleArgsParser({'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}, 'args': 'chdir=tmp'})
    assert parser.parse() == ('copy', {'src': 'a', 'dest': 'b', 'chdir': 'tmp'}, None)
    parser = ModuleArgsParser({'action': 'copy', 'local_action': 'shell echo hi'})

# Generated at 2022-06-13 07:01:54.209062
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import sys
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import StringIO

    class AnsibleExitException(Exception):
        pass

    class AnsibleModule(object):
        def __init__(self, argument_spec, bypass_checks=False, no_log=False, check_invalid_arguments=True, mutually_exclusive=None, required_together=None, required_one_of=None,
                     add_file_common_args=False):
            self.argument_spec = argument_spec
            self.bypass_checks = bypass_checks
            self.no_log = no_log
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually_

# Generated at 2022-06-13 07:02:01.605789
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = dict()
    ds['another'] = 'value'
    ds['action'] = 'echo hi'
    ds['id_'] = '1234567'
    ds['args'] = dict()
    ds['args']['echo'] = 'hi'
    ds['args']['_raw_params'] = 'echo hi'

    obj = ModuleArgsParser(task_ds=ds)
    assert obj is not None
    action, args, delegate_to = obj.parse()
    assert action == 'echo'
    assert args == dict()
    assert delegate_to == None


# Generated at 2022-06-13 07:02:06.717807
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for module_args.ModuleArgsParser.parse
    There is test case in module_args_spec.py
    '''
    # case 1, action is a dict, (action, args, delegate_to) = ('ec2', { 'x': 1}, None)
    task_ds = dict()
    task_ds['action'] = dict(module='ec2', x=1)
    mparser = ModuleArgsParser(task_ds)
    assert(mparser.parse() == ('ec2', { 'x': 1}, None))

    # case 2, action is a string, (action, args, delegate_to) = ('ec2', { 'x': 1}, None)
    task_ds = dict()
    task_ds['action'] = 'ec2 x=1'

# Generated at 2022-06-13 07:02:14.438603
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    target = dict()
    # correct args
    target['action'] = dict()
    target['action']['module'] = dict()
    target['action']['module']['args'] = dict()
    target['action']['module']['args']['_raw_params'] = ''

    # correct args
    target['action']['module']['args']['_raw_params'] = 'ansible_test'
    target['action']['module']['args']['testdict'] = {'test1': 'test1', 'test2': 'test2'}
    target['action']['module']['args']['testdict']['test3'] = dict()
    target['action']['module']['args']['testdict']['test3']['test4']

# Generated at 2022-06-13 07:02:29.791443
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test with and without a collection_list param
    parser = ModuleArgsParser(task_ds={'shell': 'echo hi'})
    assert parser.parse() == (u'shell', {u'_raw_params': u'echo hi'}, None)
    assert parser.parse(skip_action_validation=True) == (u'shell', {u'_raw_params': u'echo hi'}, None)

    parser = ModuleArgsParser(task_ds={'copy': 'src=a dest=b'})
    assert parser.parse() == (u'copy', {u'src': u'a', u'dest': u'b'}, None)
    assert parser.parse(skip_action_validation=True) == (u'copy', {u'src': u'a', u'dest': u'b'}, None)

   

# Generated at 2022-06-13 07:02:42.210394
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Initialize test environment
    role_path = '%s/roles/common/tasks/main.yml' % ANSIBLET_DIR
    task_ds = {u'module': u'copy src=./dest=../'}
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    expected_result = ('copy', {'src': './', 'dest': '../'}, None)

    # Run the test
    actual_result = module_args_parser.parse()
    #print (actual_result)
    assert actual_result==expected_result

# Generated at 2022-06-13 07:02:46.954891
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds={'delegate_to': 'localhost', 'local_action': 'shell echo hi'}
    # action, args, delegate_to = ModuleArgsParser(task_ds).parse()
    ModuleArgsParser(task_ds).parse()


# Generated at 2022-06-13 07:02:57.474161
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def _supply_module_args(module_string):
        '''
        helper method to call parse to get module args
        '''

        # instantiate and call parse
        module_args_parser = ModuleArgsParser(task_ds={'action': module_string})
        (action, args) = module_args_parser.parse()
        return (action, args)

    # test with no args
    (action, args) = _supply_module_args('copy')
    assert action == 'copy'
    assert args == {}

    # test with args
    (action, args) = _supply_module_args('copy src=hi dest=there')
    assert action == 'copy'
    assert args == {'src': 'hi', 'dest': 'there'}


# ==============================================================
# Module Parser - object for

# Generated at 2022-06-13 07:03:00.938574
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    pap = ModuleArgsParser(task_ds, collection_list)

    expected_action = None
    expected_args = None
    expected_delegate_to = None

    action, args, delegate_to = pap.parse()

    assert action == expected_action
    assert args == expected_args
    assert delegate_to == expected_delegate_to


# Generated at 2022-06-13 07:03:10.120615
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import copy

    # test_ModuleArgsParser_parse_action_and_delegate_to_specified()
    ds = {'action': 'command', 'delegate_to': 'localhost'}
    mp = ModuleArgsParser(ds)
    action, args, delegate_to = mp.parse()
    assert action == 'command'
    assert args == {}
    assert delegate_to == 'localhost'

    # test_ModuleArgsParser_parse_action_and_local_action_specified()
    ds = {'action': 'command', 'local_action': 'shell'}
    mp = ModuleArgsParser(ds)
    action, args, delegate_to = mp.parse()
    assert action == 'shell'
    assert args == {}
    assert delegate_to == 'localhost'

    # test_ModuleArgsParser_parse_action_specified

# Generated at 2022-06-13 07:03:13.935088
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {"action":"shell","args":{"chdir":"/home","creates":"file1"}}
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == ('shell', {'creates': 'file1', 'chdir': '/home'}, None)

# Generated at 2022-06-13 07:03:19.627108
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.playbook.task
    import ansible.playbook.handler
    input_data1 = {'module': 'copy', 'src': 'a', 'dest': 'b'}
    input_data2 = {'local_action': "copy src=a dest=b"}
    input_data3 = {'action': "copy src=a dest=b"}

# Generated at 2022-06-13 07:03:34.876002
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.errors import AnsibleError
    from ansible.errors import AnsibleParserError
    from ansible.module_utils.six import string_types
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.vars.clean import strip_internal_keys
    templar = Templar(loader=None, variables=combine_vars(loader=None, variable_manager=None, all_vars=None))
    simple_task_ds = {u'static': u'yes', u'when': u'inventory_hostname == myhost', u'action': {u'module': u'copy', u'args': u'src=a dest=b'}}


# Generated at 2022-06-13 07:03:45.391541
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # kwargs is a dictionary, should not raise an error
    kwargs = {}
    assert_no_error('ModuleArgsParser(**kwargs).parse')

    # kwargs is a dictionary, should raise error if "task_ds" is an empty dictionary
    kwargs = {'task_ds': {}}
    assert_raises_AnsibleError('ModuleArgsParser(**kwargs).parse')

    # kwargs is a dictionary, should raise error if "task_ds" is anything but a dictionary
    kwargs = {'task_ds': 'string'}
    assert_raises_AnsibleError('ModuleArgsParser(**kwargs).parse')

    # kwargs is a dictionary, In all three of the tests below should return action, arguments, and delegate_to values

# Generated at 2022-06-13 07:03:56.895616
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    _task_ds = Task._valid_attrs
    task_ds = dict()
    for k, v in iteritems(_task_ds):
        task_ds[k] = v
    task_ds['action'] = {'module': 'echo hi', 'other_param': 'other_value'}
    task_ds['local_action'] = {'module': 'echo hi', 'other_param': 'other_value'}
    task_ds[k] = v
    module_args_parser = ModuleArgsParser(task_ds)
    module_args_parser.parse()
    module_args_parser.parse(skip_action_validation=True)
    # ansible.utils.unsafe_proxy.AnsibleUnsafe

# Generated at 2022-06-13 07:04:25.446933
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    def t(action, module_args, expected):
        result = ModuleArgsParser(task_ds=dict(action=action), collection_list=[]).parse()
        assert result == expected

    # Test case:
    # echo hi
    t("shell echo hi", "shell echo hi", ('shell', {u'_raw_params': u'echo hi', u'_uses_shell': True}, None))

    # Test case:
    # tag: Name
    t("ec2 tag: Name", "ec2 tag=\"'Name'\"", ('tag', {u'tag': u"'Name'"}, None))

    # Test case:
    # { module: ec2, x: y }
    t("ec2 x=y", "{ module: ec2, x: y }", ('ec2', {u'x': u'y'}, None))



# Generated at 2022-06-13 07:04:33.245675
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.collection import CollectionLoader

    # test for when action is specified
    task_ds = {
        'action': {
            'module': 'command',
            'chdir': '/tmp'
        }
    }
    expected = ('command', {'chdir': '/tmp'}, None)
    module_args_parser = ModuleArgsParser(task_ds, collection_list=CollectionLoader())
    result = module_args_parser.parse()
    assert result == expected, "expected {}, got {}".format(expected, result)

    # test for when local action is specified
    task_ds = {
        'local_action': {
            'module': 'command',
            'chdir': '/tmp'
        }
    }

# Generated at 2022-06-13 07:04:42.124164
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    testParser = ModuleArgsParser(task_ds={'action': {'module': 'test', 'arg1': '1', 'arg2': '2'}, 'delegate_to': 'localhost'}, collection_list=[])
    assert testParser.parse() == ('test', {'delegate_to': 'localhost', 'arg1': '1', 'arg2': '2'}, 'localhost')
    assert testParser.resolved_action is None
    testParser = ModuleArgsParser(task_ds={'action': 'test arg1=1 arg2=2', 'delegate_to': 'localhost'}, collection_list=[])

# Generated at 2022-06-13 07:04:52.290741
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        "name": "name",
        "action": {
            "module": "shell",
            "args": "pwd"
        }
    }
    collection_list = []
    test_map = [
        (
            None, None, None
        )
    ]
    test_ = {}
    test_["task_ds"] = task_ds
    test_["collection_list"] = collection_list
    test_["result (action, args, delegate_to)"] = test_map
    yield test_

    task_ds = {
        "name": "name",
        "action": {
            "shell": "pwd"
        }
    }
    collection_list = []

# Generated at 2022-06-13 07:05:01.473550
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.module_utils.common.collections import is_sequence

    module_args = ''  # noqa: F841
    skip_action_validation = ''  # noqa: F841

    # verifies that the object we get back is a dictionary
    # and is of the proper form
    def _verify_action(action, args, delegate_to):
        if action in ('include', 'include_role', 'include_tasks') and not is_sequence(args):
            raise AssertionError("action '%s' was expected to have been normalized to a dictionary, but was not" % action)
        if isinstance(args, string_types):
            raise

# Generated at 2022-06-13 07:05:14.657241
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert ModuleArgsParser(dict(action=dict(module='foo', bar='one'))).parse() == ('foo', {'bar': 'one'})
    assert ModuleArgsParser(dict(local_action=dict(module='foo', bar='one'))).parse() == ('foo', {'bar': 'one'})
    assert ModuleArgsParser(dict(foo=dict(bar='one'))).parse() == ('foo', {'bar': 'one'})
    assert ModuleArgsParser(dict(foo='bar')).parse() == ('foo', {'bar': True})
    assert ModuleArgsParser(dict(foo='bar=one')).parse() == ('foo', {'bar': 'one'})
    assert ModuleArgsParser(dict(action='foo')).parse() == ('foo', {})

# Generated at 2022-06-13 07:05:25.957184
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:05:35.451152
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mod = AnsibleModule(argument_spec=dict(
        action=dict(type='str', required=True, aliases=['action_plugin']),
        delegate_to=dict(type='str'),
        args=dict(type='dict')
    ))

    # orig_action = {'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}, 'delegate_to': 'localhost'}
    orig_action = 'copy src=a dest=b'
    res = ModuleArgsParser(orig_action).parse()
    assert res == ('copy', {'src': 'a', 'dest': 'b'}, None)

    orig_action = {'module': 'copy', 'src': 'a', 'dest': 'b'}
    res = ModuleArgsParser(orig_action).parse()

# Generated at 2022-06-13 07:05:48.294450
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test for method parse of class ModuleArgsParser
    """

    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    import pytest
    from ansible.playbook.play_context import PlayContext

    def setUpModule():
        pass

    def tearDownModule():
        pass

    setUpModule()

    def setUp():
        """ setup test fixtures. """
        pass


    def tearDown():
        """ cleanup test fixtures. """
        pass


# Generated at 2022-06-13 07:06:00.276399
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    module_args_parser = ModuleArgsParser()
    task_ds = {'action': 'shell', 'args': 'echo hi'}
    skip_action_validation = False
    result = module_args_parser.parse(task_ds, skip_action_validation)
    expected_result =  ( 'shell', {'_raw_params': 'echo hi'}, None )
    assert result == expected_result

    # Test when args is a dict
    task_ds = {'action': 'shell', 'args': {'x': 1, 'y': 2}}
    result = module_args_parser.parse(task_ds, skip_action_validation)
    expected_result =  ( 'shell', {'x': 1, 'y': 2}, None )
    assert result == expected_result

    # Test when args contain variable
   

# Generated at 2022-06-13 07:06:15.151225
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    _task_ds = { 'delegate_to': 'localhost', 'action': 'shell echo hi', 'args': {'chdir': '/tmp'} }
    _action = 'shell'
    _args = {'_raw_params': 'echo hi', 'chdir': '/tmp'}
    _delegate_to = 'localhost'
    task_parser = ModuleArgsParser(task_ds=_task_ds)
    (action, args, delegate_to) = task_parser.parse()
    assert(action == _action)
    assert(args == _args)
    assert(delegate_to == _delegate_to)


# Generated at 2022-06-13 07:06:22.981882
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    my_args = {
        'shell': 'echo hi',
        'args': {
            'chdir': '/tmp',
            'creates': '/tmp/foo'
        }
    }
    my_dict = {
        'action': 'shell',
        'delegate_to': 'localhost'
    }
    my_dict.update(my_args)
    my_obj = ModuleArgsParser(my_dict)
    print(my_obj.parse())
    assert my_obj.parse() == ('shell', my_args, 'localhost')



# Generated at 2022-06-13 07:06:33.158398
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Create a ModuleArgsParser object
    module_arg_parser = ModuleArgsParser()

    # valid module args
    task_data = {
        'module': 'shell echo hello'
    }
    action, args, delegate_to = module_arg_parser.parse(task_data)
    assert action == 'shell' and args == {'_raw_params': 'echo hello'}
    action, args, delegate_to = module_arg_parser.parse(task_data, skip_action_validation=True)
    assert action == 'shell' and args == {'_raw_params': 'echo hello'}

    task_data = {
        'module': 'shell',
        '_raw_params': 'echo hello'
    }
    action, args, delegate_to = module_arg_parser.parse(task_data)
   