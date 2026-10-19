

# Generated at 2022-06-13 06:56:53.692621
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    def _run_module_raw_extraction_test(module, expected_action, expected_unparsed_params):
        task_ds = {}
        task_ds['action'] = module
        task = ModuleArgsParser(task_ds)
        action, _, _ = task.parse()
        assert action == expected_action
        assert task._task_ds['action']['_raw_params'] == expected_unparsed_params

    for module in RAW_PARAM_MODULES:
        _run_module_raw_extraction_test(module, module, "")

    _run_module_raw_extraction_test("copy src=a dest=b", "copy", "")

# Generated at 2022-06-13 06:57:04.708718
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Unit: ModuleArgsParser: test_parse

    # 1. test, when there is no args, should return action and args
    task_ds = {'action': 'echo hi'}
    collection_list = []
    normalizer = ModuleArgsParser(task_ds, collection_list)

    action, args, delegate_to = normalizer.parse()
    assert action == 'echo'
    assert args == {'_raw_params': 'hi'}
    assert delegate_to == Sentinel

    # 2. test, when there is args, should return action and args, and args is in the args
    task_ds = {'action': 'echo hi', 'args': 'a=2'}
    collection_list = []
    normalizer = ModuleArgsParser(task_ds, collection_list)


# Generated at 2022-06-13 06:57:12.317972
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:21.766149
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:29.704544
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    module_args_parser._task_ds = {'hosts': 'localhost', 'tasks': [{'action': 'shell pwd', 'register': 'shell_out'}, {'action': 'copy src=/etc/ansible/hosts dest=/tmp/hosts', 'register': 'copy_out'}]}
    task = module_args_parser.parse(skip_action_validation=False)
    assert True


# Generated at 2022-06-13 06:57:41.888293
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action_loader = DictDataLoader({
        'name': {'args': ['{{ bar }}']},
        'failed': {}
    })
    module_loader = DictDataLoader({})
    task_ds = dict(action=dict(module='name', bar=1))
    res = ModuleArgsParser(task_ds, action_loader, module_loader).parse()
    assert_equal(res, ('name', dict(bar=1), 'localhost'))

    task_ds = dict(action=dict(action='name', bar=1))
    res = ModuleArgsParser(task_ds, action_loader, module_loader).parse()
    assert_equal(res, ('name', dict(bar=1), 'localhost'))

    task_ds = dict(action=dict(action='name'), bar=1)
    res = ModuleArgsParser

# Generated at 2022-06-13 06:57:43.771315
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for the function parse
    '''
    pass

# Generated at 2022-06-13 06:57:57.103561
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test imports
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.role_include import RoleInclude
    yaml_snippet = {u'name': u'foo', u'connection': u'local'}
    task_ds = {u'name': u'foo', u'connection': u'local'}
    loader = DictDataLoader({})

    # Test function
    def _process_action(self, task_ds):
        # The path to the module_utils directory to load utilities.
        self._module_utils_path = None

        # The path to the action plugins directory to load plugins from.
        self._action_plugins_path = None

        # Whether the action being loaded is local to this

# Generated at 2022-06-13 06:57:57.667831
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True



# Generated at 2022-06-13 06:58:03.937850
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_parser = ModuleArgsParser()
    assert args_parser.parse(skip_action_validation=False) == (None, {}, Sentinel)
    assert args_parser.resolved_action == None
    task_ds = {
        "delegate_to": "localhost",
        "local_action": "copy src= {{ a }} dest = {{ b }} ",
        "action": "shell echo hi"
    }
    args_parser = ModuleArgsParser(task_ds=task_ds)
    assert args_parser.parse(skip_action_validation=False) == ('copy', {'src': '{{ a }}', 'dest': '{{ b }}'}, 'localhost')
    assert args_parser.resolved_action == None

# Generated at 2022-06-13 06:58:14.120703
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell echo hi'}
    collection_list = '/etc/ansible/collections'
    module = ModuleArgsParser(task_ds, collection_list)
    module.parse()


# class AnsibleModule(object):

# Generated at 2022-06-13 06:58:19.770300
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    temp_task_ds = ActionModule.ActionModule._load_task_data(
        task_ds={'shell': 'pwd', 'args': {'chdir': '/tmp'}})
    task_ds = temp_task_ds.copy()
    temp_collection_list = []
    collection_list = temp_collection_list
    test_module_args_parser = ModuleArgsParser(task_ds=task_ds,
                                               collection_list=collection_list)
    ansible_module_args_parser_parse = test_module_args_parser.parse(
        skip_action_validation=False)
    assert ansible_module_args_parser_parse == ('shell', {'chdir': '/tmp',
                                                          '_raw_params':
                                                          'pwd'}, None)
# test class

# Generated at 2022-06-13 06:58:28.003782
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_bytes
    # The following should all be valid examples of 'module' args,
    # and should be normalized to the following:
    # {'module': 'testmodule', args: {'arg1': 'arg1-val', 'arg2': 'arg2-val'}}

# Generated at 2022-06-13 06:58:39.920879
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    # store the valid Task/Handler attrs for quick access
    valid_attrs = set(Task._valid_attrs.keys())
    valid_attrs.update(set(Handler._valid_attrs.keys()))
    # HACK: why are these not FieldAttributes on task with a post-validate to check usage?
    valid_attrs.update(['local_action', 'static'])
    valid_attrs = frozenset(valid_attrs)

    # valid attributes of task
    valid_attrs = frozenset(Task._valid_attrs)

    # load the test data
    data = load_fixture('validate_task_args/args_parser.yml')


# Generated at 2022-06-13 06:58:47.768662
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    argparse = ModuleArgsParser(task_ds, collection_list)
    result = argparse.parse()
    assert result == (None, {}, Sentinel)
    task_ds = {
        'action': 2
        }
    argparse = ModuleArgsParser(task_ds, collection_list)
    assert argparse.parse() == (None, {}, Sentinel)
    task_ds = {
        'action': ''
        }
    argparse = ModuleArgsParser(task_ds, collection_list)
    assert argparse.parse() == (None, {}, Sentinel)
    task_ds = {
        'action': '',
        'args': ''
        }
    argparse = ModuleArgsParser(task_ds, collection_list)

# Generated at 2022-06-13 06:58:48.226482
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass



# Generated at 2022-06-13 06:58:56.112240
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task

    # valid task has only one module specified
    t = Task()
    t.load(dict(action=dict(module='copy', src='a', dest='b')))
    parser = ModuleArgsParser(t._ds, collection_list=None)
    assert parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)

    # json for many modules is not allowed
    t.load(dict(action=dict(module=json.dumps({'module': 'copy', 'src': 'a', 'dest': 'b'}))))
    parser = ModuleArgsParser(t._ds, collection_list=None)
    with pytest.raises(AnsibleParserError) as e:
        parser.parse()

# Generated at 2022-06-13 06:59:01.544542
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import mock

    class Tester(object):
        def assertEqual(self, a, b):
            assert a == b
        def assertTrue(self, a):
            assert a == True

    b = mock.MagicMock()
    b.default_vars.return_value = {}
    b.hostvars.return_value = {}
    b.vars = {}
    b.get_name.return_value = 'test_host'
    c = dict(connection='local', become=False, become_user=None, become_method=None,
             check=False, diff=False, become_flags=None, scenario='default',
             become_flag_list=[])

    test = Tester()

    # Test module: action
    # Test new-style module invocation

# Generated at 2022-06-13 06:59:05.426555
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds={'action': 'shell', 'args': 'echo hi', '_ansible_verbosity': 0, '_ansible_no_log': False}
    ModuleArgsParser(task_ds).parse()


# Generated at 2022-06-13 06:59:11.598402
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.template import Templar

    task_ds = {} if task_ds is None else task_ds
    collection_list = {} if collection_list is None else collection_list
    action = None if action is None else action
    additional_args = None if additional_args is None else additional_args
    action = None if action is None else action
    args = dict() if args is None else args

    test_obj = ModuleArgsParser(task_ds, collection_list)
    assert(isinstance(test_obj, ModuleArgsParser))

    test_obj2 = ModuleArgsParser(None, None)
    assert(not isinstance(test_obj2, ModuleArgsParser))

    test_obj3 = ModuleArgsParser(None, None)
   

# Generated at 2022-06-13 06:59:27.046089
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test with a valid args for task
    valid_task_args = dict(
        name="Test",
        action="win_shell",
        args="dir /d"
    )
    parser = ModuleArgsParser(task_ds=valid_task_args)
    expected_action = "win_shell"
    expected_args = dict(
        _command="dir /d"
    )
    expected_delegate_to = None
    action, args, delegate_to = parser.parse()
    assert expected_action == action
    assert expected_args == args
    assert expected_delegate_to == delegate_to
    # Test with a valid args for handler
    valid_handler_args = dict(
        name="Test",
        action="win_service",
        args=dict(
            name="test"
        )
    )


# Generated at 2022-06-13 06:59:30.236255
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # create an instance of ModuleArgsParser with empty argument
    module_args_parser = ModuleArgsParser()
    # call parse with following arguments
    # skip_action_validation=False
    assert False


# Generated at 2022-06-13 06:59:40.943516
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with pytest.raises(AnsibleError, match=r"Invalid data passed to ModuleArgsParser: expected dict, got None"):
        ModuleArgsParser().parse()

    with pytest.raises(AnsibleAssertionError, match="the type of 'task_ds' should be a dict, but is a <class 'NoneType'>"):
        ModuleArgsParser(task_ds=None).parse()

    with pytest.raises(AnsibleParserError, match=r"unexpected parameter type in action: <class 'NoneType'>"):
        ModuleArgsParser(task_ds={'action': None}).parse()


# Generated at 2022-06-13 06:59:52.836802
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Initialize variables which are required for executing the testcase
    task_ds = { 'local_action': 'shell echo hi'}
    mock_module_parser = MagicMock()
    mock_module_parser.action = 'shell'
    mock_module_parser.resolved_action = None
    mock_module_parser._task_ds = {'local_action': 'shell echo hi'}

# Generated at 2022-06-13 06:59:53.430642
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass



# Generated at 2022-06-13 07:00:04.322915
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:00:18.786223
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    item1 = {
        'action': 'script',
        'delegate_to': 'localhost',
        'a': 'A',
        'b': 'B'
    }

    item2 = {
        'action': 'script',
        'delegate_to': 'localhost',
        '_raw_params': 'a=A b=B'
    }

    item3 = {
        'module': 'script',
        'a': 'A',
        'b': 'B'
    }

    item4 = {
        'script': {
            'a': 'A',
            'b': 'B'
        }
    }

    item5 = 'script a=A b=B'

    parser = ModuleArgsParser(task_ds=item1)

# Generated at 2022-06-13 07:00:27.932222
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:00:39.987207
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test for method parse of class ModuleArgsParser
    """
    task_ds = {}
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    ansible_module_utils = AnsibleModuleUtils(substitution=False,
                                              check_invalid_arguments=False,
                                              argument_spec={},
                                              supports_check_mode=False,
                                              no_log=True,
                                              min_ansible_version=None,
                                              min_ansible_collection_version=None)
    module_args_parser.ansible_module_utils = ansible_module_utils
    
    action, args, delegate_to = module_args_parser.parse()
    expected_action

# Generated at 2022-06-13 07:00:41.405215
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    # module_args_parser.parse()
    return True

# Generated at 2022-06-13 07:00:48.600986
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # initialize module_args_parser
    task_ds = {}
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds, collection_list)

    # call parse with skip_action_validation=False
    result = module_args_parser.parse(skip_action_validation=False)
    assert result is None



# Generated at 2022-06-13 07:00:58.002663
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # called by modules/system/setup.py and modules/system/stat.py
    #    def _get_cpuinfo(sysctl):
    obj = ModuleArgsParser()
    non_task_ds = [
        '_ansible_version',
        '_ansible_module_name',
        '_ansible_no_log',
        '_ansible_debug',
        '_ansible_check_mode',
        '_ansible_selinux_special_fs',
        '_ansible_ignore_errors',
        '_ansible_syslog_facility',
        '_ansible_keep_remote_files',
        '_ansible_verbosity',
        '_ansible_diff'
    ]

# Generated at 2022-06-13 07:01:04.145492
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_parser = ModuleArgsParser()

    # test_ModulArgsParser_parse: None arg
    result = module_arg_parser._normalize_parameters(None)
    assert result == (None, None)

    result = module_arg_parser._normalize_parameters(None, 'action_name')
    assert result == ('action_name', None)

    # test_ModulArgsParser_parse: string as arg
    result = module_arg_parser._normalize_parameters('ec2', 'action_name')
    assert result == ('action_name', {'module': 'ec2'})

    # test_ModulArgsParser_parse: dict as arg

# Generated at 2022-06-13 07:01:11.030472
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    obj = ModuleArgsParser()

    action_dict = {
        'action': 'test_action',
        'args': 'test_args',
        'delegate_to': 'test_delegate_to',
        'local_action': 'test_local_action'
    }

    obj._task_ds = action_dict
    actual = obj.parse()

    assert actual == ('test_action', 'test_args', 'test_delegate_to')



# Generated at 2022-06-13 07:01:18.451333
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    testcases = dict()
    testcases[1] = dict(
        task_ds=dict(
            name='test_ModuleArgsParser_parse_1',
            action=dict(
                module='copy',
                src='a',
                dest='b'
            )
        ),
        expected=dict(
            action='copy',
            args=dict(
                src='a',
                dest='b'
            ),
            delegate_to=None
        )
    )

# Generated at 2022-06-13 07:01:26.806130
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def make_task_ds(action, args=None, local_action=None, delegate_to=None):
        args = {} if args is None else args
        tds = {
            'action': action,
            'args': args,
            'delegate_to': delegate_to
        }
        if local_action is not None:
            tds['local_action'] = local_action
        return tds

    action = 'command'
    final_args = {
        '_raw_params': 'pwd',
        '_uses_shell': False
    }
    parser = ModuleArgsParser(make_task_ds(action, args=final_args))
    assert parser.parse() == ('command', final_args, None)
    # test with action
    action = 'command'
    args = 'pwd'
   

# Generated at 2022-06-13 07:01:32.501089
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task

    yaml_dict = Task.load(dict(action="copy", args=dict(src="a", dest="b", state="c")))
    m = ModuleArgsParser(dict(action=yaml_dict))
    module_name, args, delegate_to = m.parse()

    assert module_name == 'copy'
    assert args == dict(src="a", dest="b", state="c")
    assert delegate_to is None

    yaml_dict = Task.load(dict(local_action="shell 'echo {{ x }}'", args=dict(x=1, y=2)))
    m = ModuleArgsParser(dict(local_action=yaml_dict))
    module_name, args, delegate_to = m.parse()

    assert module_name == 'shell'
   

# Generated at 2022-06-13 07:01:35.686212
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'copy src=a dest=b'}
    collection_list = None
    assert ModuleArgsParser(task_ds, collection_list).parse() == ('copy', {'dest': 'b', 'src': 'a'}, Sentinel)

# Generated at 2022-06-13 07:01:37.026927
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # The method parse does not return a value.
    # There is no way to test this method
    return



# Generated at 2022-06-13 07:01:43.817013
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action = 'copy'
    args = dict()
    delegate_to = 'localhost'
    task_ds = {'local_action': 'copy src=a dest=b'}
    task_ds.update({'delegate_to': delegate_to})
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    assert (module_args_parser.parse() == (action, args, delegate_to))
    action = 'shell'
    args = dict(_raw_params='echo hi', _uses_shell=True)
    task_ds = dict(action='shell echo hi')
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    assert (module_args_parser.parse() == (action, args, None))
    action = 'shell'

# Generated at 2022-06-13 07:01:58.292033
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action_loader = ActionModuleLoader()
    collection_list = CollectionList()
    define_module_action_module(action_loader)

    task_ds = {'action': 'action_module'}
    m = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    (action, args, delegate_to) = m.parse()
    assert action == 'action_module'
    assert not args
    assert delegate_to is Sentinel

    task_ds = {'module': 'ping', 'action': 'action_module'}
    m = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    with pytest.raises(AnsibleParserError) as err:
        m.parse()
    assert "conflicting action statements" in str(err.value)



# Generated at 2022-06-13 07:02:05.611249
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:12.419609
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("\n===== test_ModuleArgsParser_parse ===============================")
    print("test with action: copy src=a dest=b")
    task_ds = {'action': 'copy src=a dest=b'}
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    print("action: {}, args: {}, delegate_to: {}".format(action, args, delegate_to))
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}
    assert delegate_to == None

    print("test with action: copy src='a' dest='b'")
    task_ds = {'action': 'copy src=\'a\' dest=\'b\''}
    parser = ModuleArgsParser(task_ds)
   

# Generated at 2022-06-13 07:02:19.242584
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test for method parse of class ModuleArgsParser
    """
    loader, inventory, variable_manager = ConfigLoader().setup_loader()
    task_ds = {}
    collection_list = None

    parser = ModuleArgsParser(task_ds, collection_list)
    parser.parse()

# Class ModuleCommon

# Generated at 2022-06-13 07:02:33.199196
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task_include import TaskInclude
    # instantiate
    mod_args = ModuleArgsParser()
    # test with 'action: something'
    input = {'action': 'something', 'delegate_to': 'xyz'}
    output = ('something', {}, 'xyz')
    expected = mod_args.parse(input)
    assert expected == output
    # test with 'local_action: something'
    module_include = TaskInclude()
    input = {'local_action': 'something'}
    output = ('something', {}, 'localhost')
    expected = mod_args.parse(input)
    assert expected == output
    # test with 'module: something'
    module_include = TaskInclude()
    input = {'module': 'something'}

# Generated at 2022-06-13 07:02:47.970620
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds=None, collection_list=None)
    with pytest.raises(AnsibleAssertionError) as excinfo:
        parser.parse()
    assert "the type of 'task_ds' should be a dict, but is a " in to_text(excinfo.value)

    task_ds = {"action": "shell echo hi"}
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = parser.parse()
    assert action == "shell"
    assert args == {"_raw_params": "echo hi"}
    assert delegate_to == Sentinel

    task_ds = {"action": "shell", "args": "echo hi"}
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)

# Generated at 2022-06-13 07:02:57.832533
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    # create an instance of the class we want to test
    module_args_parser = ModuleArgsParser(collection_list=None)
    # a sample action
    action = 'copy'
    # a sample dictionary
    args = {'src': 'a', 'dest': 'b' }
    # a sample host to delegate_to
    delegate_to = None
    # the expected outcome of the method under test
    expected_outcome = (action, args, delegate_to)
    # the actual outcome of the method under test
    actual_outcome = module_args_parser.parse(skip_action_validation=False)
    # assert that expected outcome matches actual outcome
    assert expected_outcome == actual_outcome


# Generated at 2022-06-13 07:03:09.530608
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.cli.arguments import options as cli_options
    class AnsibleOptions(object):
        def __init__(self):
            self.connection = 'local'
            self.module_path = None
            self.forks = 100
            self.become = False
            self.become_method = None
            self.become_user = None
            self.check = False
            self.diff = False
            self.syntax = None
            self.listhosts = None
            self.listtasks = None
            self.listtags = None
            self.step = None
            self.start_at_task = None
            self.verbosity = 0
            self.extra_vars = None
            self.private_key_file = None
            self.inventory = None

    # Initialize parser options
   

# Generated at 2022-06-13 07:03:18.781789
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({})
    module_name, args, delegate_to = parser.parse()
    assert module_name is None
    assert args == {}
    assert delegate_to is None

    parser = ModuleArgsParser({'action': 'shell echo hi'})
    module_name, args, delegate_to = parser.parse()
    assert module_name == 'shell'
    assert args == {'_raw_params': 'echo hi'}
    assert delegate_to is None

    parser = ModuleArgsParser({'local_action': 'shell echo hi'})
    module_name, args, delegate_to = parser.parse()
    assert module_name == 'shell'
    assert args == {'_raw_params': 'echo hi', '_uses_delegate': True}
    assert delegate_to == 'localhost'

    parser = Module

# Generated at 2022-06-13 07:03:21.102952
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # assert False, "Unimplemented test case for method: test_ModuleArgsParser_parse"
    pass
# --- end of test_ModuleArgsParser_parse ---



# Generated at 2022-06-13 07:03:56.407546
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import sys
    module_args = {'action': 'shell echo hi'}
    module_args_parser = ModuleArgsParser(module_args, ['core'])
    (action, args, delegate_to) = module_args_parser.parse()
    assert (action == 'shell' and args == {'_raw_params': 'echo hi', '_uses_shell': True} and delegate_to is None)
    module_args = {'local_action': 'shell echo hi'}
    module_args_parser = ModuleArgsParser(module_args, ['core'])
    (action, args, delegate_to) = module_args_parser.parse()
    assert (action == 'shell' and args == {'_raw_params': 'echo hi', '_uses_shell': True} and delegate_to == 'localhost')
    module_args

# Generated at 2022-06-13 07:03:57.810103
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    obj = ModuleArgsParser()
    # TODO
    obj.parse()


# Generated at 2022-06-13 07:04:08.167420
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # try without module_name
    print("Testing ModuleArgsParser.parse without module_name")
    task_ds = {
        'shell': 'echo hi'
    }
    p = ModuleArgsParser(task_ds)
    res = p.parse()
    assert res[0] == 'shell'
    assert res[1] == {}
    assert res[2] == Sentinel
    print("ModuleArgsParser.parse: passed")

    print("Testing ModuleArgsParser.parse with skip_action_validation")
    task_ds = {
        'suspend-vm': ''
    }
    p = ModuleArgsParser(task_ds)
    res = p.parse(True)
    assert res[0] == 'suspend-vm'
    assert res[1] == {}
    assert res[2] == Sentinel

# Generated at 2022-06-13 07:04:21.964375
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # set up PYTHONPATH to include the 'test' dir so our test files can be
    # found by the python import machinery
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'test'))
    import ansible.playbook.tests.test_module_args_parser

    test_cases = ansible.playbook.tests.test_module_args_parser.get_test_cases(
        os.path.join(os.path.dirname(__file__), 'test', 'module_args_input.txt'),
        os.path.join(os.path.dirname(__file__), 'test', 'module_args_output.txt'))

    # test all our test cases

# Generated at 2022-06-13 07:04:31.811954
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Setup arguments
    task_ds = {'args': {'some_arg': 'some test value'}, 'action': 'test module', 'delegate_to': 'some test value'}
    module_args_parser = ModuleArgsParser(task_ds)

    module_args_parser._task_ds = {'args': {'some_arg': 'some test value'}, 'action': 'test module', 'delegate_to': 'some test value'}
    module_args_parser._collection_list = None
    module_args_parser._task_attrs = frozenset(['args', 'action', 'delegate_to'])

    # Call function
    actual_return = module_args_parser.parse()

    # Assertions

# Generated at 2022-06-13 07:04:41.111636
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    parser = ModuleArgsParser()

    # test simple
    data = dict(ansible_version='2.10',
                connection='local',
                gather_facts='no',
                hosts='localhost',
                name='copy module test',
                tasks=dict(action=dict(module='copy', src='source file', dest='destination file')))
    result = parser.parse(data)
    assert result[0] == 'copy'

    # test with args

# Generated at 2022-06-13 07:04:52.009111
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    # store the valid Task/Handler attrs for quick access
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    task_attrs = frozenset(task_attrs)
    task_attrs = task_attrs.union({u'local_action', u'static'})
    skip_action_validation = False

# Generated at 2022-06-13 07:05:01.333862
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    import yaml
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader
    from collections import namedtuple

    #####################################################################################
    # test extracted from /ansible/test/units/test_module_args.py
    #####################################################################################
    # TODO
    # - 'static'
    # - 'arguments'
    # - 'with_'

    ArgsTestNT = namedtuple('ArgsTestNT', 'input_ds expected_action expected_args expected_delegate_to')

    # input_ds is the task dictionary
    # expected_action is what module the task maps to
    # expected_args is the arguments that the module takes
    # expected_delegate_to is the host that the module runs on


# Generated at 2022-06-13 07:05:07.081606
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'subaction': 'subaction', 'a': 'a'}}
    module_args_parser = ModuleArgsParser(
        task_ds=task_ds,
        collection_list=None
    )
    module_args_parser.parse()



# Generated at 2022-06-13 07:05:19.043674
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.utils.vars import combine_vars
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.helpers import load_list_

# Generated at 2022-06-13 07:05:35.915020
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_loader.add_directory(data_context().content.collection_dir.strpath)
    task_ds_1 = dict(
        action=dict(module='ec2', region='xyz'),
        delegate_to='xyz')
    args_1 = dict(
        action='ec2',
        args=dict(region='xyz'),
        delegate_to='xyz')
    task_ds_2 = dict(
        action=dict(module='ec2', region='xyz'),
        delegate_to='xyz')
    args_2 = dict(
        action='ec2',
        args=dict(region='xyz'),
        delegate_to='xyz')
    task_ds_3 = dict(
        action='ec2',
        delegate_to='xyz')

# Generated at 2022-06-13 07:05:50.041161
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(None)
    assert m.parse(None) == (None, [], [])
    assert m.parse([]) == (None, [], [])
    assert m.parse("") == (None, [], [])
    assert m.parse("test") == ("test", [], [])
    assert m.parse("test: 123") == ("test", [("123", [])], [])
    assert m.parse("test: 123,456") == ("test", [("123,456", [])], [])
    assert m.parse("test: 123, 456") == ("test", [("456", [("123", [])])], [])
    assert m.parse("test: 123,456,789") == ("test", [("789", [("123", [("456", [])])])], [])
   

# Generated at 2022-06-13 07:06:01.159450
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import tempfile
    import os


# Generated at 2022-06-13 07:06:09.318429
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    task = {
        'action': 'copy src=/tmp/1 dest=/tmp/3',
        'with_items': [
            'one',
            'two',
            'three'
        ]
    }
    assert parser.parse(task) == ('copy', {'dest': '/tmp/3', 'src': '/tmp/1', '_raw_params': ''}, None)

    task = {
        'action': {'module': 'copy src=/tmp/1 dest=/tmp/3'},
        'with_items': [
            'one',
            'two',
            'three'
        ]
    }
    assert parser.parse(task) == ('copy', {'dest': '/tmp/3', 'src': '/tmp/1', '_raw_params': ''}, None)

    task

# Generated at 2022-06-13 07:06:11.993537
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    args = parser.parse()
    assert_type(args, tuple)

# Generated at 2022-06-13 07:06:22.756088
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Parse method of ModuleArgsParser class
    task_ds = {}
    collection_list = None
    actual = ModuleArgsParser(task_ds, collection_list).parse()
    expected = (None, dict(), Sentinel)
    assert actual == expected

    task_ds = {'action': 'copy src=a dest=b'}
    actual = ModuleArgsParser(task_ds, collection_list).parse()
    expected = ('copy', {'dest': 'b', 'src': 'a'}, Sentinel)
    assert actual == expected

    task_ds = {'action': 'copy src=a dest=b'}
    actual = ModuleArgsParser(task_ds, collection_list).parse()
    expected = ('copy', {'dest': 'b', 'src': 'a'}, Sentinel)
    assert actual == expected


# Generated at 2022-06-13 07:06:32.199287
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Test ModuleArgsParser.parse
    """
    # Arrange
    ds = {'action': 'shell', 'args': {'chdir': '/tmp'}}
    # test for:
    #    - module: <module_name>
    #    - args: <args>
    module = 'shell'
    args = {'chdir': '/tmp'}
    delegate_to = None
    expected = (module, args, delegate_to)

    collection_list = None

    # Act
    parser = ModuleArgsParser(ds, collection_list)
    actual = parser.parse()

    # Assert
    assert actual == expected, "Parser did not return expected"
