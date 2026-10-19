

# Generated at 2022-06-13 06:56:44.407491
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds=None, collection_list=None)
    assert parser.parse() == (None, (), None)

# Generated at 2022-06-13 06:56:52.632887
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.task import TaskInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.handler_task_include import HandlerTaskInclude

    # handler tests

    task_ds = {'name': 'foo', 'action': {'module': 'shell', 'args': 'ls'}}
    m = ModuleArgsParser(task_ds=task_ds)
    assert (m.parse() == ('shell', {'args': 'ls'}, None))

    task_ds = {'name': 'foo', 'action': 'shell ls'}
    m = ModuleArgsParser(task_ds=task_ds)

# Generated at 2022-06-13 06:57:03.596271
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    with pytest.raises(AnsibleAssertionError):
        parser.parse(task_ds='')

    task_ds = dict()
    assert parser.parse(task_ds=task_ds) == (None, dict(), Sentinel)

    task_ds = dict(foo='bar')
    assert parser.parse(task_ds=task_ds) == (None, dict(), Sentinel)

    task_ds = dict(module='bar')
    assert parser.parse(task_ds=task_ds) == ('bar', dict(), Sentinel)

    task_ds = dict(module='bar', foo='bar')
    assert parser.parse(task_ds=task_ds) == ('bar', dict(), Sentinel)

    task_ds = dict(module='bar foo')

# Generated at 2022-06-13 06:57:13.734981
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.compat.tests import unittest
    from ansible.module_utils._text import to_bytes

    class TestModuleArgsParser(unittest.TestCase):

        def setUp(self):
            self.parser = ModuleArgsParser()

        def tearDown(self):
            pass

        def test_parse_raw(self):
            action, args, delegate_to = self.parser.parse({'shell': 'cat /tmp/test.txt'})
            self.assertEqual(action, 'shell')
            self.assertEqual(args, {u'_raw_params': u'cat /tmp/test.txt'})
            self.assertEqual(delegate_to, Sentinel)

        def test_parse_raw_with_pipe(self):
            action, args, delegate_to = self.parser.parse

# Generated at 2022-06-13 06:57:22.245664
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds=dict(
        local_action='echo hi',
        args=dict(
            a=1
        )
    ), collection_list=None)
    (action, args, delegate_to) = parser.parse()
    assert action == 'shell'
    assert delegate_to == 'localhost'
    assert args == dict(
        a=1,
        _raw_params='echo hi'
    )

# Generated at 2022-06-13 06:57:29.784442
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        "name": "show version",
        "show version": "show version",
        "ignore_errors": True
    }

    collection_list = []

    task_ds_parser = ModuleArgsParser(task_ds, collection_list)
    action, args, delegate_to = task_ds_parser.parse()

    assert action == 'show version'
    assert args == {'ignore_errors': True}
    assert delegate_to == None


# Generated at 2022-06-13 06:57:30.679505
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# Generated at 2022-06-13 06:57:40.190141
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test1 = dict(action='')
    test2 = dict(action='shell echo hi')
    test3 = dict(action={'module': 'ec2', 'x': 1 })
    test4 = dict(action={'shell': 'echo hi' })
    test5 = dict(local_action='')
    test6 = dict(local_action='shell echo hi')
    test7 = dict(local_action={'module': 'ec2', 'x': 1 })
    test8 = dict(local_action={'shell': 'echo hi' })
    test9 = dict(module='')
    test10 = dict(module='shell echo hi')
    test11 = dict(module={'module': 'ec2', 'x': 1 })
    test12 = dict(module={'shell': 'echo hi' })
    test13 = dict

# Generated at 2022-06-13 06:57:54.016648
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    oModuleArgsParser = ModuleArgsParser()
    oPlaybook = Playbook()
    oPlayContext = PlayContext(extra_vars={})
    oPlayContext.network_os = 'ios'
    oPlayContext.connection = 'network_cli'
    oPlayContext.become = True
    oPlayContext.become_method = 'enable'
    oPlayContext.become_user = 'cisco'
    oPlayContext.check_mode = False
    oPlayContext.remote_addr = "192.168.1.1"
    oPlayContext.port = 22
    oPlayContext.remote_user = 'cisco'
    oPlayContext.private_key_file = '/path/to/ssh/key'
    oPlayContext.password = 'cisco'
    oPlayContext.timeout = 10
    oPlayContext

# Generated at 2022-06-13 06:58:02.942480
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_text
    from ansible.utils.vars import combine_vars
    from ansible.config.manager import ensure_type
    from ansible.template import Templar

    # These are needed for the sys.modules hack
    from ansible.context import AnsibleContext
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars import copy_vars

    # This hack ensures load_listener is registered (look at issue #34827 and PR #8802).
    # That can be removed as soon as we fix issue #34982
    from ansible.plugins import CALLBACK_LOAD

# Generated at 2022-06-13 06:58:18.131603
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds={"module": {'src':'/path/to/file1', 'dest':'path/to/file2'}}
    obj = ModuleArgsParser(task_ds=task_ds)
    assert obj.parse() == ('copy', {'src':'/path/to/file1', 'dest':'path/to/file2'}, None)
    assert obj.resolved_action == 'copy'
    
    
task_ds={"module": {'src':'/path/to/file1', 'dest':'path/to/file2'}}
obj = ModuleArgsParser(task_ds=task_ds)
assert obj.parse() == ('copy', {'src': '/path/to/file1', 'dest': 'path/to/file2'}, None)
assert obj.resolved_action == 'copy'



# Generated at 2022-06-13 06:58:26.047108
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {"action": "copy src=a dest=b"}
    collection_list = [{'name': 'foo', 'version': '1.0.0', 'namespace': 'bar'}]
    obj = ModuleArgsParser(task_ds, collection_list)
    # module_args = obj.parse()
    # assert module_args[0] == {'src': 'a', 'dest': 'b'}
    #
    # task_ds = {"args": {"src": "a", "dest": "b"}}
    # collection_list = [{'name': 'foo', 'version': '1.0.0', 'namespace': 'bar'}]
    # obj = ModuleArgsParser(task_ds, collection_list)
    module_args = obj.parse()

# Generated at 2022-06-13 06:58:32.437582
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    canary = {}
    instance = ModuleArgsParser(task_ds=canary)
    instance._task_ds = {}
    # Test for non existing action
    try:
        instance.parse()
    except AnsibleParserError as e:
        assert "no module/action detected" in to_native(e)
    # Test for existing action, without args (Supported case)
    instance._task_ds = {"action": "ping"}
    action, args, delegate_to = instance.parse()
    assert action == 'ping'
    assert args == {}
    assert delegate_to is None
    # Test for existing action, with args (Supported case)
    instance._task_ds = {"action": "shell", "args": {"_variable_params": "echo hello world"}}
    action, args, delegate_to = instance.parse()
    assert action

# Generated at 2022-06-13 06:58:43.082859
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    t = dict()
    t['action'] = 'shell echo hi'
    t['args'] = dict()
    t['args']['chdir'] = '/tmp'
    t['local_action'] = 'command pwd'
    t['local_action']['args'] = dict()
    t['local_action']['args']['chdir'] = '/tmp'
    t['module'] = 'shell'
    t['module']['args'] = dict()
    t['module']['args']['chdir'] = '/tmp'
    t['arg'] = 'val'

    p = ModuleArgsParser(task_ds=t)
    p.parse()

    t['local_action'] = dict()
    t['local_action']['module'] = 'command'

# Generated at 2022-06-13 06:58:58.024535
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Create a target object to be tested.
    test_target = ModuleArgsParser()

    # Test with an invaild type.
    # TODO: We need an API to create a new AnsibleAssertionError object.
    # assert_raises(AnsibleAssertionError, test_target.parse, None)

    # Test with an invaild action.
    # TODO: We need an API to create a new AnsibleParserError object.
    # assert_raises(AnsibleParserError, test_target.parse, {})

    # Test with an invaild action.
    # TODO: We need an API to create a new AnsibleParserError object.
    # assert_raises(AnsibleParserError, test_target.parse, {'action':'fake_action'})

    # Test with a normal task

# Generated at 2022-06-13 06:59:02.808921
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    module_parser = ModuleArgsParser(Task())
    task = dict()
    action = "shell"
    args = dict(
        chdir="/tmp")
    task['command'] = "pwd"
    task['args'] = args
    result = module_parser.parse()
    assert result == (action, args, None)

# Generated at 2022-06-13 06:59:07.632629
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''test action_plugin_loader'''
    parser = ModuleArgsParser(task_ds={'module': 'test'})
    action, args, delegate_to = parser.parse()
    assert action == 'test'
    assert args == {}
    assert delegate_to is None

    parser = ModuleArgsParser(task_ds={'action': 'test'})
    action, args, delegate_to = parser.parse()
    assert action == 'test'
    assert args == {}
    assert delegate_to is None

    parser = ModuleArgsParser(task_ds={'test': 'test'})
    action, args, delegate_to = parser.parse()
    assert action == 'test'
    assert args == {}
    assert delegate_to is None


# Generated at 2022-06-13 06:59:17.417490
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Filenames will be created in the following format:
    # test_ModuleArgsParser_parse_file_<counter>.yml

    # Counts the number of created files
    counter = 0

    # Sample data

# Generated at 2022-06-13 06:59:21.566079
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_parser = ModuleArgsParser(task_ds=None, collection_list=None)
    args_parser._split_module_string(module_string='shell echo "hello world"')
    action, args, delegate_to=args_parser.parse()


# Generated at 2022-06-13 06:59:22.366768
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True



# Generated at 2022-06-13 06:59:31.296073
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    data = dict(
        module='test',
        state='present',
        token='test_token',
    )
    parser = ModuleArgsParser(data)
    action, args, delegate_to = parser.parse()
    assert action == 'test'
    assert args == data
    print('ModuleArgsParser::parse() ok')


# Generated at 2022-06-13 06:59:41.762466
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

# Generated at 2022-06-13 06:59:53.378957
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.loader import AnsibleLoader
    yaml_data = """
- ec2:
    instance_type: t2.micro
    count_tag:
      key: 'auto-scaling-group'
      value: 'demo-app'
"""
    loader = AnsibleLoader(yaml_data, file_name='non_file')
    tasks_list = loader.get_single_data()
    task_ds = tasks_list[0]

    task_ds = dict((to_bytes(k, errors='surrogate_or_strict'), v) for k, v in task_ds.items())
    parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = parser.parse

# Generated at 2022-06-13 07:00:04.231480
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    # Test Method: parse
    #
    # test cases:
    # 1. test_input type = dictionary, test_args = None
    # 2. test_input type = dictionary, test_args = dictionary
    # 3. test_input type = string, test_args = None
    # 4. test_input type = string, test_args = dictionary
    #
    task_ds = {
        'action': {
            'module': 'shell',
            'args': '"echo hi"'
        }
    }

# Generated at 2022-06-13 07:00:11.641170
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:00:22.377127
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    for data in [
        {'shell': 'echo hi'},
        {'shell': {'_raw_params': 'echo hi'}},
        {'module': 'shell', 'args': 'echo hi'},
        {'module': 'shell', '_raw_params': 'echo hi'},
        {'shell': {'_raw_params': 'echo hi'}},
        'shell echo hi',
        'shell: echo hi',
        'shell: {{ ansible_os_family }}',
        'echo "{{ ansible_all_ipv4_addresses }}"',
        'shell: echo hi',
        {'module': 'shell', 'args': 'echo hi'},
        {'module': 'shell', '_raw_params': 'echo hi'},
    ]:
        expected = 'shell'
        actual

# Generated at 2022-06-13 07:00:33.884030
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def test(task_ds, action, args, delegate_to):
        my_parser = ModuleArgsParser(task_ds)
        result_action, result_args, result_delegate_to = my_parser.parse()
        assert result_action == action
        assert result_args == args
        assert result_delegate_to == delegate_to

    test(task_ds=dict(action=dict(module='copy', src='a', dest='b')),
         action='copy', args=dict(src='a', dest='b'), delegate_to=None)

    test(task_ds=dict(action='copy src=a dest=b'),
         action='copy', args=dict(src='a', dest='b'), delegate_to=None)


# Generated at 2022-06-13 07:00:40.290056
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
    collection_list = []
    obj = ModuleArgsParser(task_ds,collection_list)
    action = None
    args = dict()
    delegate_to = None
    result = obj.parse()
    assert action == result[0]
    assert args == result[1]
    assert delegate_to == result[2]

    action = "test"
    args = dict()
    delegate_to = "localhost"
    task_ds = dict({'local_action': "test", "delegate_to": "localhost"})
    result = ModuleArgsParser(task_ds,collection_list).parse()
    assert action == result[0]
    assert args == result[1]
    assert delegate_to == result[2]

# end class ModuleArgsParser

# end class ModuleArgsParser

# Generated at 2022-06-13 07:00:46.732208
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mp = ModuleArgsParser({'delegate_to': 'localhost', 'echo': 'hi', 'module': 'shell'})
    (action, args, delegate_to) = mp.parse(skip_action_validation=True)
    assert action == 'shell'
    assert args == {'_raw_params': 'hi'}
    assert delegate_to == 'localhost'

    mp = ModuleArgsParser({'shell': 'echo hi', 'module': 'shell'})
    (action, args, delegate_to) = mp.parse(skip_action_validation=True)
    assert action == 'shell'
    assert args == {'_raw_params': 'hi'}
    assert delegate_to is None

    mp = ModuleArgsParser({'module': 'shell echo hi'})
    (action, args, delegate_to) = mp.parse

# Generated at 2022-06-13 07:00:57.164359
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(a=1, b=2)
    map = ModuleArgsParser(task_ds=task_ds)

    # try to invoke parse with invalid task_ds
    map._task_ds = None
    with pytest.raises(AnsibleAssertionError) as e:
        map.parse()
    assert str(e.value) == "the type of 'task_ds' should be a dict, but is a <class 'NoneType'>"

    # add action to test what happens when we have action and delegate_to
    task_ds['action'] = 'shell echo'
    task_ds['delegate_to'] = 'localhost'
    map._task_ds = task_ds
    with pytest.raises(AnsibleParserError) as e:
        map.parse()

# Generated at 2022-06-13 07:01:14.753902
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}, 'delegate_to': 'localhost', 'args': {'test': 'test'}}
    args = ModuleArgsParser(task_ds).parse()
    assert args[0] == 'copy'
    assert args[1] == {'src': 'a', 'dest': 'b', 'test': 'test'}
    assert args[2] == 'localhost'

    task_ds = {'action': 'copy: src=a dest=b', 'delegate_to': 'localhost', 'args': {'test': 'test'}}
    args = ModuleArgsParser(task_ds).parse()
    assert args[0] == 'copy'

# Generated at 2022-06-13 07:01:25.238588
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'dest': '/tmp/foo', 'src': 'somewhere'}}
    parser = ModuleArgsParser(task_ds)
    ansible_module = import_module('ansible.modules.files.synchronize')
    assert ansible_module.AnsibleModule is not None
    assert (__file__, 'copy', {'dest': '/tmp/foo', 'src': 'somewhere'}, None) == parser.parse()
    parser = ModuleArgsParser({'action': 'copy src=/tmp/foo dest=/tmp/bar'})
    assert (__file__, 'copy', {'dest': '/tmp/bar', 'src': '/tmp/foo'}, None) == parser.parse()

# Generated at 2022-06-13 07:01:34.667205
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    paths = []
    paths.append("../../lib/ansible/playbook/tests/module_args_parser.yml")
    test_dataset = YamlIncludeConstructor.construct_yaml_objects(paths)
    # test_dataset is a list of dictionaries
    # each dictionary is a test case
    # where 'in' is input and 'out' is expected output
    for test_data in test_dataset:
        # input (copy_action and copy_action_args)
        args = {}
        for k, v in iteritems(test_data['in']['copy_action']):
            args[k] = v
        for k, v in iteritems(test_data['in']['copy_action_args']):
            args[k] = v
        # expected output
       

# Generated at 2022-06-13 07:01:43.022007
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_name = 'copy'

# Generated at 2022-06-13 07:01:54.064823
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()

    # Test normal scenario to test module parse
    module_args_parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = module_args_parser.parse()
    assert action is None
    assert args == dict()
    assert delegate_to == sentinel.Sentinel

    # Test normal scenario to test module parse
    task_ds = 'test'
    module_args_parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'test'
    assert args == dict()
    assert delegate_to == sentinel.Sentinel

    # Test normal scenario to test module parse
    task_ds = 'test'
    module_args_parser = ModuleArgsParser(task_ds)
    action, args, delegate_

# Generated at 2022-06-13 07:02:03.256269
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest
    import ansible.playbook.task as task
    import ansible.playbook.task_include as task_include
    import ansible.playbook.play_context as play_context
    import ansible.playbook.play as play
    import ansible.playbook.playbook as playbook
    import ansible.playbook.role as role
    import ansible.playbook.block as block
    import ansible.playbook.role_include as role_include
    import ansible.playbook.handler_task_include as handler_task_include
    import ansible.vars.hostvars as hostvars
    import ansible.vars.manager as manager
    from ansible.parsing.vault import VaultLib

    def _prep_file(base_filename):
        file_path = os.path.join

# Generated at 2022-06-13 07:02:09.522934
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # setup
    task_ds = {}
    collection_list = [
        Mock(),
        Mock(resolved=False),
        Mock(resolved=True, fqcn='/tmp/foo', redirect_list=[])
    ]
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    # test with empty dictionary passed in
    action, args, delegate_to = parser.parse(skip_action_validation=True)
    assert action == None
    assert not args
    assert delegate_to is Sentinel

# Generated at 2022-06-13 07:02:16.375970
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import lookup_loader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=[])
    variable_manager.set_inventory(inventory)

    target_host = inventory.get_host('all')
    play_context = PlayContext()
    play_context.remote_addr = target_host.name

    play_

# Generated at 2022-06-13 07:02:27.098662
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Without arguments
    result = ModuleArgsParser().parse()
    assert result[0] == None
    assert result[1] == {}
    assert result[2] == Sentinel

    # With arguments
    result = ModuleArgsParser({'action':{'module':'test', 'val':'test'}}).parse()
    assert result[0] == 'test'
    assert result[1] == {'val': 'test'}
    assert result[2] == Sentinel

    # With arguments
    task_ds = {'action':{'module':'test'}, 'delegate_to':'delegate_to', 'other_stuff':'other_stuff'}
    result = ModuleArgsParser(task_ds).parse()
    assert result[0] == 'test'
    assert result[1] == {}

# Generated at 2022-06-13 07:02:35.142611
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''

# Generated at 2022-06-13 07:02:44.350559
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:55.805534
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds1 = {'module': 'ec2', 'x': 1 }
    collection_list1 = None
    args_parser1 = ModuleArgsParser(task_ds1, collection_list1)
    result1 = args_parser1.parse()
    assert result1 == ('ec2', {'x': 1})

    task_ds2 = {'action': 'echo hi'}
    collection_list2 = None
    args_parser2 = ModuleArgsParser(task_ds2, collection_list2)
    result2 = args_parser2.parse()
    assert result2 == ('echo', {'_raw_params': 'hi'})

    task_ds3 = {'local_action': 'echo hi'}
    collection_list3 = None

# Generated at 2022-06-13 07:03:01.057222
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    current_dir = os.getcwd()
    root_dir = os.path.dirname(current_dir)
    collection_dir = os.path.join(root_dir, 'test/integration/targets/collections/ansible_collections/test/test_collection')
    collection_list = [collection_dir]

    #self.assertEqual(expected, ModuleArgsParser(task_ds=None, collection_list=None).parse(skip_action_validation=False))
    #assert False # TODO: implement your test here


# Generated at 2022-06-13 07:03:02.341041
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME:
    pass


# Generated at 2022-06-13 07:03:12.170845
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print('TESTING ModuleArgsParser parse')
    _task_ds = {}
    _collection_list = None

    _task_ds = {'action': 'shell echo hi'}
    _collection_list = None
    parser = ModuleArgsParser(_task_ds, _collection_list)
    assert parser.parse() == ('shell', {'_raw_params': None, 'echo': 'hi'}, None)

    _task_ds = {'action': {'module': 'shell echo hi'}}
    _collection_list = None
    parser = ModuleArgsParser(_task_ds, _collection_list)
    assert parser.parse() == ('shell', {'_raw_params': None, 'echo': 'hi'}, None)

    _task_ds = {'action': {'module': 'shell '}}

# Generated at 2022-06-13 07:03:12.820285
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True == True

# Generated at 2022-06-13 07:03:20.549760
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # tested method with new action
    from ansible.plugins.action import ActionBase
    class DummyAction(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            pass
        def run(self, tmp=None, task_vars=None):
            pass
        def _execute_module(self, module_name=None, module_args=None, task_vars=None, tmp=None):
            pass
    class DummyActionBase(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            pass
        def run(self, tmp=None, task_vars=None):
            pass

# Generated at 2022-06-13 07:03:35.884400
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # this is a basic example that should work fine
    task_ds = dict(
        ping='pong'
    )
    # args should contain ping=pong
    parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = parser.parse()
    assert 'pong' == args['ping']

    # more complex arguments
    task_ds = dict(
        shell='echo hi',
        chdir='/tmp'
    )
    # args should contain { '_raw_params': 'echo hi', 'chdir': '/tmp' }
    parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = parser.parse()
    assert 'echo hi' == args['_raw_params']
    assert '/tmp' == args['chdir']

    # test

# Generated at 2022-06-13 07:03:39.215323
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  module_args_parser_inst = ModuleArgsParser()
  assert module_args_parser_inst.parse() == (None, dict(), None)


# Test that the type of 'args' defined in the class ModuleArgsParser is a dict

# Generated at 2022-06-13 07:03:44.771889
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    example_input = {
        'meta': 'noop',
        'module': 'noop',
        'name': 'this is a test',
        'args': {
            'msg': 'this is a message'
        },
        'delegate_to': '{{ inventory_hostname }}',
        'register': 'output'
    }

    expected_result = ('noop', {'msg': 'this is a message'}, {{ inventory_hostname }})

    parser = ModuleArgsParser(task_ds=example_input)
    result = parser.parse()

    assert result == expected_result, \
        "Expected {0} but got {1}".format(expected_result, result)

# Generated at 2022-06-13 07:04:01.952813
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    t = dict(action='A',
             delegate_to='B',
             args=dict(C='D', E='F'))
    t_expected = dict(action='A',
                      delegate_to='B',
                      args=dict(C='D', E='F'))
    assert ModuleArgsParser(t).parse() == t_expected
    t = dict(local_action='A',
             delegate_to='B',
             args=dict(C='D', E='F'))
    t_expected = dict(action='A',
                      delegate_to='B',
                      args=dict(C='D', E='F'))
    assert ModuleArgsParser(t).parse() == t_expected

# Generated at 2022-06-13 07:04:10.902784
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action = 'shell'
    args = {
        '_raw_params': 'echo \"{{ item }}\"',
        '_uses_shell': 'True',
        'chdir': '/tmp'
    }
    delegate_to = 'localhost'

# Generated at 2022-06-13 07:04:24.519337
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(None, None)
    assert m._normalize_parameters(None) == (None, {})
    assert m._normalize_parameters('bad_params') == (None, {})
    assert m._normalize_parameters({'x': 'y'}) == (None, {})
    assert len(m._normalize_parameters('echo hi')[1]) == 0
    assert len(m._normalize_parameters('shell echo hi')[1]) == 0
    assert m._normalize_parameters('shell echo hi')[0] == 'shell'
    assert m._normalize_parameters('echo hi', action='shell')[0] == 'shell'
    assert len(m._normalize_parameters('shell echo hi', action='shell')[1]) > 0
    assert m._normalize_

# Generated at 2022-06-13 07:04:30.052423
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Tests for method parse of class ModuleArgsParser
    # Setup test data
    task_ds = {'action': 'cmd /c dir'}
    collection_list = None

    p = ModuleArgsParser(task_ds, collection_list)
    # Exercise the code
    action, args, delegate_to = p.parse()
    # Verify the results
    assert p.resolved_action is None, "The method parse of class ModuleArgsParser has failed!"



# Generated at 2022-06-13 07:04:40.265422
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:46.583101
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    Task = namedtuple('Task', ['action', 'args', 'delegate_to'])

    collection_list = ['ansible_collections.1_namespace.2_collection']

# Generated at 2022-06-13 07:04:57.491608
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Without argument
    parser = ModuleArgsParser()
    try:
        action, args, delegate_to = parser.parse()
        assert False
    except AnsibleParserError:
        assert True
    # Parse the first case
    task_ds = dict(action="copy src=a dest=b", delegate_to=None)
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert action == 'copy'
    assert args == dict(src='a', dest='b')
    assert delegate_to is None
    # Parse the second case
    task_ds = dict(local_action="copy src=a dest=b", delegate_to=None)
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert action

# Generated at 2022-06-13 07:05:10.707359
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # import statements for module
    import os
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    import json

    # initialize needed objects

# Generated at 2022-06-13 07:05:12.143450
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass
# Class Action:

# Generated at 2022-06-13 07:05:23.765932
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:05:33.211071
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    # fill in
    test_data = {}
    test_data[''] = {}

    mp = ModuleArgsParser()

    for test_input, expected_result in test_data.items():
        actual_result = mp.parse(test_input)

        assert actual_result == expected_result

# Generated at 2022-06-13 07:05:47.845005
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    ansible_dict = { "action": {'module': 'baz', 'x':1 } }
    assert parser.parse(ansible_dict) == ('baz', {'x': '1'}, None)

    ansible_dict = { "action": 'service name={{ some_var }} state=started' }
    assert parser.parse(ansible_dict) == ('service', {'name': '{{ some_var }}', 'state': 'started'}, None)

    ansible_dict = { "action": 'service name={{ some_var }} state=started', 'args': { 'shell': True } }

# Generated at 2022-06-13 07:05:54.814800
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Testing with skip_action_validation = False

    # With action:
    task_ds = {'action': 'shell echo hi'}
    mlp = ModuleArgsParser(task_ds)
    action, args, delegate_to = mlp.parse(skip_action_validation=False)
    assert action == 'shell'
    assert args == {'cmd': 'echo hi'}
    assert delegate_to == Sentinel

    task_ds = {'action': 'copy src=a dest=b'}
    mlp = ModuleArgsParser(task_ds)
    action, args, delegate_to = mlp.parse(skip_action_validation=False)
    assert action == 'copy'
    assert args == {'dest': 'b', 'src': 'a'}
    assert delegate_to == Sentinel


# Generated at 2022-06-13 07:06:03.142673
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action='command', 
        delegate_to='localhost', 
        args=dict(_raw_params='echo hello')
    )

    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == ('command', {'_raw_params': 'echo hello'}, 'localhost')

    task_ds = dict(
        action='command', 
        delegate_to='localhost', 
        args='echo hello', 
    )

    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == ('command', {'_raw_params': 'echo hello'}, 'localhost')

    task_ds = dict(
        action='command', 
        delegate_to='localhost', 
    )

    parser = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 07:06:11.263327
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:06:11.800488
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert False

# Generated at 2022-06-13 07:06:19.023992
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(None)
    assert m.parse() == (None, {}, 'Sentinel')
    m = ModuleArgsParser({'action': 'shell echo hi'})
    assert m.parse() == ('shell', {'_raw_params': 'echo hi'}, 'Sentinel')
    m = ModuleArgsParser({'action': 'shell', 'args': {'_raw_params': 'echo hi'}}) # args is for old style playbook
    assert m.parse() == ('shell', {'_raw_params': 'echo hi'}, 'Sentinel')
    m = ModuleArgsParser({'action': 'shell', 'args': {'_raw_params': 'echo hi'}, 'delegate_to': 'me'})
    assert m.parse() == ('shell', {'_raw_params': 'echo hi'}, 'me')

# Generated at 2022-06-13 07:06:21.443778
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME: This test cannot be run as part of the unit test suite because it depends on
    #        playbook_dir and playbook_paths config options.
    # test_ModuleArgsParser_parse()
    pass


# Generated at 2022-06-13 07:06:23.005205
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds={'name': 'hello world'})
    print(parser.parse())



# Generated at 2022-06-13 07:06:33.158516
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(action = dict(module = "copy src=xyz dest=abc"))
    t = ModuleArgsParser(task_ds=task_ds)
    actual = t.parse()
    assert actual[0] == 'copy'
    assert actual[1] == {'src': 'xyz', 'dest': 'abc'}
    assert actual[2] is None

    task_ds = dict(action = "copy src=xyz dest=abc")
    t = ModuleArgsParser(task_ds=task_ds)
    actual = t.parse()
    assert actual[0] == 'copy'
    assert actual[1] == {'src': 'xyz', 'dest': 'abc'}
    assert actual[2] is None
