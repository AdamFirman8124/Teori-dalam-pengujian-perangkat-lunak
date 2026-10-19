

# Generated at 2022-06-13 06:56:47.809639
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Tested in connection with the ansible/playbook and ansible/modules
    # that are defined in this repository
    return None

# Generated at 2022-06-13 06:56:54.097808
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Setup test
    task_ds = {
        "action": "{ 'module': 'copy', 'src': 'a', 'dest': 'b' }"
    }
    expected_action = "copy"
    expected_args = {
        "src": "a",
        "dest": "b"
    }
    expected_delegate_to = None
    collection_list = None
    instance = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    # Invoke method
    action, args, delegate_to = instance.parse()

    # Verify results
    assert action == expected_action
    assert args == expected_args
    assert delegate_to == expected_delegate_to



# Generated at 2022-06-13 06:56:56.208284
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    assert module_args_parser.parse() == (None, None, None)


# Generated at 2022-06-13 06:57:04.258067
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test_path/tasks.yml contents:
    """
     - local_action: shell echo hi
    """
    parser = YamlParser('test_path/tasks.yml')
    data = parser.get_single_data()
    task_ds = data[0]
    parser_inst = ModuleArgsParser(task_ds)
    result = parser_inst.parse()
    # Assertion error if the result doesn't match the expected value
    assert result == ('shell', {'_raw_params': 'echo hi', '_uses_shell': False}, 'localhost')

# Generated at 2022-06-13 06:57:14.290038
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print('Testing ModuleArgsParser.parse()')


# Generated at 2022-06-13 06:57:19.140371
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    task_ds_no_module = { 'name': '', 'any_value': 'test' }
    parser = ModuleArgsParser(task_ds=task_ds_no_module, loader=loader)
    assert parser.parse() == (None, dict(), Sentinel)

    task_ds_no_action = { 'name': '', 'action': '', 'any_value': 'test' }
    parser = ModuleArgsParser(task_ds=task_ds_no_action, loader=loader)
    assert parser.parse() == (None, dict(), Sentinel)

    task_ds_no_localaction = { 'name': '', 'local_action': '', 'any_value': 'test' }

# Generated at 2022-06-13 06:57:30.953278
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'copy src=a dest=b'}
    collection_list= None
    module_args_parser = ModuleArgsParser(task_ds,collection_list)
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}
    assert delegate_to is None

    # test canonizalization of module
    # this is insane, but sometimes actions are specified in the form
    # of a dictionary, like { 'copy' : 'src=a dest=b' }
    # this is only legal when the key is the module name
    task_ds = {'copy': 'src=a dest=b'}
    collection_list = None

# Generated at 2022-06-13 06:57:44.110192
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    d = {'delegate_to': 'localhost'}
    assert ModuleArgsParser(d, collection_list=None).parse() == ('ping', {}, 'localhost')
    assert ModuleArgsParser({'ping': {'action': {'module': 'ping-2', 'arg1': '1'}}}, collection_list=None).parse() == ('ping-2', {'arg1': '1'}, Sentinel)
    assert ModuleArgsParser({'action': 'print-3 anstest "test"', 'local_action': 'print-4 {{ansible_hostname}}'}, collection_list=None).parse() == ('print-4', {'_variable_params': '{{ansible_hostname}}'}, 'localhost')

# Generated at 2022-06-13 06:57:57.319024
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    TASK_DS = {
        'with_dict': {'a': 1, 'b': 2},
        'with_items': ['c'],
        'assert': 'a == b',
        'local_action': {
            'shell': 'htop'
        },
        'wait_for': 'path=/',
        'yum': {
            'name': 'httpd',
            'state': 'present'
        },
        'notify': ['restart'],
        'loop_control': {
            'loop_var': 'item'
        },
        'fail': 'msg=failed'
    }


# Generated at 2022-06-13 06:58:05.651536
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    loader = DictDataLoader({
        'inventory1': """
            localhost ansible_connection=local
            localhost2 ansible_connection=local
            localhost3 ansible_connection=local
        """,
        'inventory2': """
            localhost ansible_connection=local
            localhost2 ansible_connection=local
        """,
    })
    inventory = InventoryManager(loader=loader, sources=['inventory1', 'inventory2'])


# Generated at 2022-06-13 06:58:25.965608
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
    collection_list = None
    m = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    result = m.parse(skip_action_validation=False)
    assert result == (None, dict(), Sentinel)

    task_ds = dict(
        action=dict(module='shell', args='echo hi'),
        local_action=dict(module='shell', args='echo hi'),
        delegate_to='xyz',
        args='echo hi'
    )
    collection_list = None
    m = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    result = m.parse(skip_action_validation=False)
    assert result == ('shell', dict(args='echo hi'), 'xyz')


# Generated at 2022-06-13 06:58:26.731006
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    p = ModuleArgsParser()
    


# Generated at 2022-06-13 06:58:32.921179
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'delegate_to': 'localhost', 'module': 'shell echo hi'}
    obj = ModuleArgsParser(task_ds)
    assert obj.resolved_action is None
    action, args, delegate_to = obj.parse()
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}
    assert delegate_to == 'localhost'
    assert obj.resolved_action is None
    task_ds = {'delegate_to': 'localhost', 'shell': 'echo hi'}
    obj = ModuleArgsParser(task_ds)
    assert obj.resolved_action is None
    action, args, delegate_to = obj.parse()
    assert action == 'shell'
    assert args == {'_raw_params': 'echo hi'}
    assert delegate_to

# Generated at 2022-06-13 06:58:37.892758
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test with no args
    with pytest.raises(AnsibleParserError) as error_message:
        parser = ModuleArgsParser()
        parser.parse()
    assert "unexpected parameter type in action: <class 'NoneType'>" in str(error_message.value)

    # Test with empty task_ds
    parser = ModuleArgsParser(task_ds=dict())
    (action, args, delegate_to) = parser.parse()
    assert action is None
    assert args is None
    assert delegate_to is Sentinel

    # Test with single module
    task_ds = dict()
    task_ds['action'] = 'ping'
    parser = ModuleArgsParser(task_ds=task_ds)
    (action, args, delegate_to) = parser.parse()
    assert action == 'ping'
    assert args == {}

# Generated at 2022-06-13 06:58:42.914443
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME: We may need to add more unit tests here.
    # Create mocks for methods:
    #     parse_kv(), _normalize_parameters(), _normalize_new_style_args(), _normalize_old_style_args()
    # and make sure they are called with predefined arguments.
    pass


# Utils
# =====


# Generated at 2022-06-13 06:58:48.549531
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)
    skip_action_validation = False
    obj.parse(skip_action_validation)



# Generated at 2022-06-13 06:58:53.385959
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell echo hi'}
    parser = ModuleArgsParser(task_ds)
    result = parser.parse()
    assert result == ('shell', {'_raw_params': 'echo hi'}, Sentinel)


# Generated at 2022-06-13 06:59:04.460744
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    tester = ModuleArgsParser({
        "action": "some_value",
        "local_action": "some_other_value",
        "random_key": True,
        "delegate_to": "some_other_host",
        "shell": "some_command arg1 arg2 arg3 arg4 arg5"
    })
    tester._split_module_string = mock.Mock(return_value=("some_value", "other key=value"))
    tester._normalize_parameters = mock.Mock(return_value=("some_value", { "key": "value" }))

    # Test for all variations of input
    assert tester.parse(skip_action_validation=True) == ("some_value", { "key": "value" }, "some_other_host")


# Generated at 2022-06-13 06:59:06.423233
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
    assert ModuleArgsParser.parse(task_ds) == ('shell', dict(), None)


# Generated at 2022-06-13 06:59:10.300625
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = ModuleArgsParser(task_ds={'action': 'copy'})
    assert args.parse()==(u'copy', {}, Sentinel)


# Generated at 2022-06-13 06:59:25.580593
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    # store the valid Task/Handler attrs for quick access
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    task_attrs = frozenset(task_attrs)

    task_ds = {
        'action': 'echo hi',
        'local_action': 'ec2',
        'module': 'copy',
        'args': '',
        'with_items' : '{{var}}',
        'with_dict' : {},
        'with_first_found' : '',
        'with_sequence' : '',
    }
    del task_ds['local_action']

# Generated at 2022-06-13 06:59:31.129567
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    load_data = load_fixture('test_ModuleArgsParser_parse.yml')
    # 1. Create object
    obj = ModuleArgsParser(task_ds=load_data['task_ds'], collection_list=load_data['collection_list'])
    # 2. Run method parse
    result = obj.parse(skip_action_validation=load_data['skip_action_validation'])
    # 3. Assertion
    assert [result[0], result[1]] == load_data['expected_result'][0:2]



# Generated at 2022-06-13 06:59:41.620477
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:59:47.682200
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser()
    task = {'action': {'module': 'shell echo hello'}}
    (action, args, delegate_to) = m.parse(task)
    expected_action = 'shell'
    expected_args = {'_raw_params': 'echo hello'}
    expected_delegate_to = None
    assert (action == expected_action) and (args == expected_args) and (delegate_to == expected_delegate_to)

    task = {'action': {'module': 'shell', 'args': 'echo hello'}}
    (action, args, delegate_to) = m.parse(task)
    expected_action = 'shell'
    expected_args = {'_raw_params': 'echo hello'}
    expected_delegate_to = None

# Generated at 2022-06-13 06:59:59.107304
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    METHOD_NAME = 'parse'
    module_name = ACTION_MODULE_PATH + '.ping'
    args = dict()
    delegate_to = 'localhost'

    # Non-empty task dict
    task_ds = dict()
    task_ds['action'] = module_name
    task_ds['register'] = 'ping_result'
    task_ds['notify'] = 'start_ping'
    task_ds['local_action'] = 'command pdsh -w all hostname'
    task_ds['raw'] = 'pwd'
    task_ds['no_log'] = True
    task_ds['delegate_to'] = 'ubuntu_18'


# Generated at 2022-06-13 07:00:04.846422
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = {'action': 'ping', 'args': {'_raw_params': ''}, 'delegate_to': 'somehost'}
    module_args_parser = ModuleArgsParser(ds)
    assert module_args_parser != None
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'ping'
    assert args == {}
    assert delegate_to == 'somehost'

# Generated at 2022-06-13 07:00:10.120976
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Instantiate an object with the information of a task_ds
    task_ds={'delegate_to': 'localhost', 'local_action': 'ec2', 'args': {'region': 'xyz'}}
    parser = ModuleArgsParser(task_ds=task_ds)
    # Test the method parse
    action, args, delegate_to = parser.parse()
    assert action == 'ec2'
    assert args == {'region': 'xyz'}
    assert delegate_to == 'localhost'
# endtest



# Generated at 2022-06-13 07:00:15.436413
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest

    from ansible.errors import AnsibleParserError
    from ansible.playbook.task import Task

    task_ds = {'action': 'ping'}
    collection_list = None
    test_obj = ModuleArgsParser(task_ds, collection_list)
    answer = {
        'action': 'ping',
        'args': {}
    }
    assert test_obj.parse() == answer
    test_obj = ModuleArgsParser(task_ds)
    assert test_obj.parse() == answer

    task_ds = {'ping': {'test':'OK', 'data':'data2'}}
    collection_list = None
    test_obj = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 07:00:16.181058
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True is True


# Generated at 2022-06-13 07:00:26.894695
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Just testing several different use cases of the parser
    loader = DataLoader()
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args="ls -al")),
            dict(action=dict(module='copy', src='/path/to/src', dest='/path/to/dest')),
            dict(copy=dict(src='/path/to/src', dest='/path/to/dest')),
            dict(copy="src=/path/to/src dest=/path/to/dest")
        ]
    )

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    tqm = None

# Generated at 2022-06-13 07:00:44.846743
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.plugins import module_loader

    loader = DataLoader()

# Generated at 2022-06-13 07:00:54.956127
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    # test dict
    task_ds = {'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}}
    # create instance of ModuleArgsParser
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    # store the valid Task/Handler attrs for quick access
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    # HACK: why are these not FieldAttributes on task with a post-validate to check usage?
    task_attrs.update(['local_action', 'static'])

# Generated at 2022-06-13 07:00:58.966872
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds={"action": "shell echo hi"}, collection_list=[])
    print("parser.parse()="+str(parser.parse()))
    print("parser.resolved_action="+str(parser.resolved_action))
# test_ModuleArgsParser_parse()

# Generated at 2022-06-13 07:00:59.846333
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# Generated at 2022-06-13 07:01:09.971345
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({
        'action': 'copy src=a dest=b',
    }, collection_list=None)
    assert parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)

    parser = ModuleArgsParser({
        'module': 'copy src=a dest=b',
    }, collection_list=None)
    assert parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)

    parser = ModuleArgsParser({
        'action': 'copy',
        'args': 'var1=value1 var2=value2',
    }, collection_list=None)
    assert parser.parse() == ('copy', {'var1': 'value1', 'var2': 'value2'}, None)


# Generated at 2022-06-13 07:01:17.182114
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
   task_ds = {
       'action': {
           'module': 'ec2',
           'x': 1
       },
       'local_action': 'echo hi',
       'a': {
           'module': 'ec2',
           'x': 1
       },
       'b': 'echo hi'
   }

   collection_list = [
   'ansible.builtin',
   'ansible_collections.amazon.aws',
   'ansible_collections.ansible.builtin']

   module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
   assert module_args_parser.parse() == ('ec2', {'x': 1}, None)


# Generated at 2022-06-13 07:01:25.946748
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print('\n<=== Test ModuleArgsParser_parse ===>')
    task_ds = dict()
    task_ds['delegate_to'] = 'localhost'
    task_ds['action_test'] = dict(raw_params='echo hi')
    task_ds['action_test_cmd_test'] = dict(a=4, b=5)
    task_ds['action_test_cmd'] = 'echo hi'
    task_ds['action_test_dict'] = dict(a=4, b=5)
    task_ds['action_test_dict_cmd'] = dict(raw_params='echo hi')
    task_ds['action_test_raw_params'] = dict(raw_params='echo hi')
    task_ds['action_test_raw_params_cmd'] = 'echo hi'

# Generated at 2022-06-13 07:01:31.760765
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:01:39.596360
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser()
    # test case 1
    # returns a tuple:
    #   action: str
    #   args: dict
    #   delegate_to: str
    task_ds = {'action': {'module': 'test_module'}}
    assert m.parse(task_ds) == ('test_module', {}, None), "returned: %s" % m.parse(task_ds)
    # test case 2
    # returns a tuple:
    #   action: str
    #   args: dict
    #   delegate_to: str
    task_ds = {'action': {'module': 'test_module', 'args': 'test_arg'}}

# Generated at 2022-06-13 07:01:45.665058
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mock_task_ds = dict()
    mock_collection_list = list()
    module_args_parser = ModuleArgsParser(task_ds=mock_task_ds, collection_list=mock_collection_list)
    # Invalid argument for method parse (case101)
    # Invalid 'skip_action_validation'
    args = {}
    if PY3:
        args['skip_action_validation'] = 'hello'
    else:
        args['skip_action_validation'] = b'hello'
    kwargs = {}
    with pytest.raises(AnsibleAssertionError) as excinfo:
        module_args_parser.parse(**args)

# Generated at 2022-06-13 07:02:04.184701
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    def build(module_name, module_options, delegate_to=None, args=None, tags=None, when=None, ignored=None):
        task = {
            'action': {
                'module': module_name,
                module_name: module_options,
            },
            'tags': tags,
            'when': when,
        }
        if delegate_to:
            task['delegate_to'] = delegate_to
        if args:
            task['args'] = args
        if ignored:
            for key in ignored:
                task[key] = ignored[key]
        return task

    def build_module_arg(module_name, module_options, args=None):
        return build(module_name, module_options, args=args)


# Generated at 2022-06-13 07:02:08.134615
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    yaml_data = {
        "action": "setup",
        "local_action": "shell",
        "delegate_to": "localhost",
        "args": None
    }
    parser = ModuleArgsParser(task_ds=yaml_data)
    assert parser.parse() == ('setup', {}, 'localhost')


# Generated at 2022-06-13 07:02:14.094367
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # no builtin tasks
    module_parser = ModuleArgsParser(task_ds={"module": "test_module", "a": "b"})
    assert module_parser.parse() == ("test_module", {"a": "b"}, None)

    # builtin task with action, args and delegate_to validators
    with pytest.raises(AnsibleParserError) as e:
        ModuleArgsParser(task_ds={"action": "test_module", "delegate_to": "localhost", "args": "a=b"})
    assert e.value.message == "conflicting action statements: test_module, delegate_to"

    # builtin task with action and args validators

# Generated at 2022-06-13 07:02:25.742174
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    task_ds = {}
    skip_action_validation = False

    # When action: fails to be found and one non-task action is found
    module_args_parser._task_ds = { 'bad_action': 'bad', 'a': 2 }
    with pytest.raises(AnsibleParserError) as excinfo:
        module_args_parser.parse(skip_action_validation)
    assert "conflicting action statements:" in str(excinfo.value)
    assert "couldn't resolve module/action" in str(excinfo.value)

    # When action: fails to be found and no non-task actions are found
    module_args_parser._task_ds = {}
    with pytest.raises(AnsibleParserError) as excinfo:
        module

# Generated at 2022-06-13 07:02:34.389584
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  # logging.basicConfig(filename='/tmp/ansible_moduleargs_unittest.log',
  #                     level=logging.DEBUG,
  #                     format='%(asctime)s %(levelname)s %(name)s %(message)s')
  module_args_parser = ModuleArgsParser()
  task_data = {
    "name": "copy sshkeys", 
    "free_form": "host_key_checking=False", 
    "dest": "{{ ansible_env.HOME }}/.ssh/authorized_keys", 
    "src": "{{ conf.ssh_private_key_path }}"
  }
  (action, args, delegate_to) = module_args_parser._normalize_parameters(task_data)
  assert action == 'copy'

# Generated at 2022-06-13 07:02:49.033188
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.yaml.error import AnsibleParserError
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    #from ansible.playbook.task.block import Block
    #from ansible.playbook.task.include import Include
    loader = AnsibleLoader(None)
    test_module_arguments_parser = ModuleArgsParser(task_ds={'a':1},collection_list=[])
    assert test_module_arguments_parser is not None


# Generated at 2022-06-13 07:02:58.874944
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'module': {'name': 'test_name', 'arg2': 'test_arg2'}, 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    assert parser.parse() == ('test_name', {'arg2': 'test_arg2'}, 'localhost')

    task_ds = {'key3': {'arg2': {'module': 'test_arg2', 'arg1': 'test_arg1'}}, 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)

# Generated at 2022-06-13 07:03:09.628757
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    mock_ds = {u'module': u'copy', u'args': u'src={{ source_dir}}/test dest={{ dest_dir }}/test', u'backup': 'yes', u'owner': u'root', u'group': u'root', u'mode': u'u=rw'}
    mock_task = u'copy'
    mock_result = (u'copy', {'dest': u'{{ dest_dir }}/test', 'src': u'{{ source_dir}}/test', 'backup': 'yes', 'owner': u'root', 'group': u'root', 'mode': u'u=rw'}, None)

# Generated at 2022-06-13 07:03:18.850709
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action = dict(
            module = 'fetch',
            src = '/home/a/a.txt',
            dest = '/home/b/b.txt',
            flat = 'yes'
        )
    )
    obj = ModuleArgsParser(task_ds)
    ret = obj.parse()
    assert ret == ('fetch', dict(dest='/home/b/b.txt', src='/home/a/a.txt', flat='yes'), None)
    task_ds = dict(
        local_action = dict(
            module = 'copy',
            src = '/home/a/a.txt',
            dest = '/home/b/b.txt',
            flat = 'yes'
        )
    )
    obj = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 07:03:23.382142
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/modules/network/cloudengine'))
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/modules/network/fortios'))
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/modules/network/junos'))
    module_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/modules/network/riverbed'))

# Generated at 2022-06-13 07:03:49.237370
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    parser = ModuleArgsParser({'shell': 'echo $ANSIBLE_VAR'}, None)
    argument, action_args, delegate_to = parser.parse()

    assert argument == 'shell'
    assert action_args == {'_raw_params': 'echo $ANSIBLE_VAR'}
    assert delegate_to == Sentinel

    parser = ModuleArgsParser({'shell': {'echo': {'$ANSIBLE_VAR': 'Foo'}}}, None)
    argument, action_args, delegate_to = parser.parse()

    assert argument == 'shell'
    assert action_args == {'$ANSIBLE_VAR': 'Foo'}
    assert delegate_to == Sentinel

    parser = ModuleArgsParser({'local_action': 'shell echo $ANSIBLE_VAR'}, None)
    argument, action_args, delegate_

# Generated at 2022-06-13 07:04:00.734200
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with pytest.raises(AnsibleParserError, match='unexpected parameter type in action'):
        # test bad type of thing
        ModuleArgsParser(task_ds=['bad']).parse()
    with pytest.raises(AnsibleError, match='invalid parameter specified for action'):
        # test invalid types of args
        task_ds = {'action': "dummy", 'args': {'_ansible_internal_param': 'internal_value', 'extra_param': 'extra_value'}}
        ModuleArgsParser(task_ds=task_ds).parse()
    with pytest.raises(AnsibleParserError, match='Complex args must be a dictionary or variable string'):
        # test bad value in additional_args
        task_ds = {'action': "dummy"}

# Generated at 2022-06-13 07:04:06.514208
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # additional_args = args = {}
    # action = item = action = item = action = item = action = item = action = item = ''
    task_ds_1 = {'action' : 'shell', 'args' : {'chdir' : '/tmp'}, 'delegate_to' : 'localhost'}
    module_args_parser = ModuleArgsParser(task_ds_1)
    module_args_parser.parse()

# Generated at 2022-06-13 07:04:12.940970
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task


# Generated at 2022-06-13 07:04:26.339905
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:33.649381
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds_0 = dict(action='echo hi', _ansible_verbose_always=True)
    parser_0 = ModuleArgsParser(task_ds=task_ds_0)
    assert parser_0.parse() == ('echo', dict(_raw_params='hi'), None)
    task_ds_0 = dict(args=dict(chdir='/tmp'), _ansible_verbose_always=True)
    parser_0 = ModuleArgsParser(task_ds=task_ds_0)
    assert parser_0.parse() == (None, dict(), None)
    task_ds_0 = dict(_ansible_verbose_always=True)
    parser_0 = ModuleArgsParser(task_ds=task_ds_0)
    with pytest.raises(AnsibleParserError):
        parser_0.parse()

# Generated at 2022-06-13 07:04:41.829159
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Generate a fake task to pass to ModuleArgsParser
    task_ds = {"action": "mymod arg1=foo arg2=bar arg3='random arg' arg4='{args}'"}

    # Call the method parse() on the fake task
    module_args_parser = ModuleArgsParser(task_ds)
    module_args_parser.parse()

    for item, value in iteritems(module_args_parser._task_ds):
        if item == 'action':
            assert value == "mymod arg1=foo arg2=bar arg3='random arg' arg4='{args}'"
        else:
            raise AnsibleParserError("'%s' is not an attribute of the class 'Module"
                                     "ArgsParser'." % item)

# Generated at 2022-06-13 07:04:47.616036
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:52.761573
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    (action, args, delegate_to) = module_args_parser.parse()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

# Generated at 2022-06-13 07:05:01.769734
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    cases = [
        (
            {'action': 'copy src=a dest=b'},
            ('copy', {'src': 'a', 'dest': 'b'}, None)
        ),
        (
            {'action': 'copy', 'args': {'src': 'a', 'dest': 'b'}},
            ('copy', {'src': 'a', 'dest': 'b'}, None)
        ),
        (
            {'action': 'copy', 'args': 'src=a dest=b'},
            ('copy', {'src': 'a', 'dest': 'b'}, None)
        )
    ]
    for msg, expected in cases:
        result = parser.parse(msg)
        assert_equal(result, expected)


# Generated at 2022-06-13 07:05:38.976190
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': '', 'local_action': '', 'delegate_to': ''}
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    print(module_args_parser.parse())


# Generated at 2022-06-13 07:05:51.262257
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    data = dict(
        action=dict(
            module=None,
            args=None,
        ),
        delegate_to=None,
    )
    parser = ModuleArgsParser(data)
    assert parser.parse() == (None, {}, None)

    data = dict(
        action=dict(
            module='os_server:',
            args=None,
        ),
        delegate_to=None,
    )
    parser = ModuleArgsParser(data)
    assert parser.parse() == ('os_server', {}, None)

    data = dict(
        action=dict(
            module='os_server:',
            args='',
        ),
        delegate_to=None,
    )
    parser = ModuleArgsParser(data)

# Generated at 2022-06-13 07:05:52.511616
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    # TODO write unit test for parse


# Generated at 2022-06-13 07:06:03.787371
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action=dict(
            module="setup",
            args=dict(
                filter="ansible_*_ipv4"
            )
        ),
        delegate_to="192.168.1.1",
        tags=[
            "something_else"
        ]
    )
    parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = parser.parse()
    assert action == "setup" and args == dict(
        filter="ansible_*_ipv4"
    ) and delegate_to == "192.168.1.1"


# Generated at 2022-06-13 07:06:11.860537
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mocked_context = MagicMock()
    mocked_context.resolved = True
    mocked_context.redirect_list = []
    mocked_context.resolved_fqcn = None


# Generated at 2022-06-13 07:06:15.150137
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(x=dict(arg1=1, arg2=2))
    collection_list = []
    module_args_parser = ModuleArgsParser(task_ds, collection_list)

    assert module_args_parser.parse() == ("x", dict(arg1=1, arg2=2), None)

# Generated at 2022-06-13 07:06:17.493408
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Arrange
    from ansible.task_vars import TaskVars
    module_parser = ModuleArgsParser(task_ds={})

    # Act & Assert
    assert module_parser.parse() is not None


# Generated at 2022-06-13 07:06:24.478556
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'module': 'ping', '_raw_params': 'data=another string', 'use_shell': True, '_uses_shell': True}}
    collection_list=None
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    result = obj.parse(skip_action_validation=False)
    assert result == ('ping', {'data': 'another string', 'use_shell': True, '_uses_shell': True}, None)

    task_ds = {'action': {'module': 'ping', '_raw_params': 'data=another string', 'use_shell': True, '_uses_shell': True}}
    collection_list=None
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)