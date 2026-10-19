

# Generated at 2022-06-13 06:56:51.859684
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def _get_datas():
        _datas = {}
        _datas['default'] = {}
        _datas['default']['_task_ds'] = {"action": "copy", "args": {"src": "a", "dest": "b"}}
        _datas['action_only'] = {}
        _datas['action_only']['_task_ds'] = {"action": "copy", "src": "a", "dest": "b"}
        _datas['module_only'] = {}
        _datas['module_only']['_task_ds'] = {"module": "copy src=a dest=b"}
        _datas['delegate_to_module_only'] = {}

# Generated at 2022-06-13 06:56:56.758380
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    ds = {}
    skip_action_validation = False
    collection_list = None
    action = None
    args=None
    delegate_to=None
    #module_name = 'ping'
    #args = {'other_args':'other_args'}
    #action = 'shell'
    m = ModuleArgsParser(ds, collection_list)
    for i in range(0, 5):
        (action, args, delegate_to) = m.parse(skip_action_validation)
        #print(action, args, delegate_to)
    return


# Generated at 2022-06-13 06:57:01.727065
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test successful parsing of a dictionary as module args
    task_ds = dict(
        action=dict(
            test_key_1="value 1",
            test_key_2="value 2",
        )
    )
    module_args_parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = module_args_parser.parse()
    assert action is not None
    assert len(args) == 2
    assert args['test_key_1'] == "value 1"
    assert args['test_key_2'] == "value 2"
    assert delegate_to is None

    # Test successful parsing of a string as module args
    task_ds = dict(
        action="test_key_1='value 1' test_key_2='value 2'"
    )
    module_args_parser = ModuleArgsParser

# Generated at 2022-06-13 06:57:03.241096
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert False # TODO: implement your test here


# Generated at 2022-06-13 06:57:12.639808
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args = {'playbook_dir': '/var/lib/awx/projects/_1__hello-world'}
    task_ds = {'block': {'block': None, 'tasks': [{'name': 'say hello', 'command': '/usr/bin/date', 'when': 'False'}]}, 'hosts': 'all', 'name': u'Hello World'}
    obj = ModuleArgsParser(task_ds, module_args=module_args)
    try:
        real_result = obj.parse()
    except Exception as e:
        print('Raised exception when calling ModuleArgsParser.parse(): {}'.format(e))
test_ModuleArgsParser_parse()

# AnsibleTaskInclude


# Generated at 2022-06-13 06:57:17.908295
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.playbook.task
    from ansible.collections.ansible.shared.txt import Runner
    task_ds = dict()
    collection_list = list()
    parser = ModuleArgsParser(task_ds, collection_list)
    assert False == isinstance(parser, dict)
    assert True == isinstance(parser, ansible.playbook.task.ModuleArgsParser)
    assert None == parser.parse()

# ===========================================
# Subclass: Runner
# ===========================================

# Generated at 2022-06-13 06:57:26.077022
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class MockTask(object):
        """
        Mock class for AnsibleTask
        """
        def __init__(self, task_ds=None, collection_list=None):
            self._task_ds = task_ds
            self._collection_list = collection_list
            self.resolved_action = None

    collection_list = [MockCollection1()]

# Generated at 2022-06-13 06:57:36.394401
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # set task_ds and collection_list
    task_ds = {}
    collection_list = None
    action = 'shell'
    args = ''
    delegate_to = Sentinel
    with pytest.raises(AnsibleAssertionError, match='the type of \'task_ds\' should be a dict, but is a '):
        # Issue #35054: check exception when task_ds without dict type
        ModuleArgsParser(None, None).parse()

    # set task_ds and collection_list
    task_ds = {'action': 'shell', 'delegate_to': 'localhost'}
    collection_list = None
    action, args, delegate_to = ModuleArgsParser(task_ds, collection_list).parse()
    assert action == 'shell'
    assert args == 'echo hi'

# Generated at 2022-06-13 06:57:50.969767
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Setup:
    from ansible.parsing.yaml.dumper import AnsibleDumper


# Generated at 2022-06-13 06:58:01.069409
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
   
    task_ds = {
      'tags': 'always',
      'tree': '~/ansible/test',
      'delegate_to': 'localhost',
      'name': 'tree',
      'action': 'find excludes="*" patterns="*" use_regex=False'
    }
    module_parser = ModuleArgsParser(task_ds)
    result = module_parser.parse()
    if result[0] == 'find' and result[1]['excludes'] == "*" and result[1]['patterns'] == "*" and result[1]['use_regex'] == False and result[2] == "localhost": 
        print("Test case 1: PASS")
    else:
        print("Test case  1: FAIL")
        

# Generated at 2022-06-13 06:58:24.317849
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert ModuleArgsParser({'module':'copy','src':'a','dest':'b'}).parse() == ('copy',{'src':'a','dest':'b'},None)
    assert ModuleArgsParser({'action':'copy','src':'a','dest':'b'}).parse() == ('copy',{'src':'a','dest':'b'},None)
    assert ModuleArgsParser({'local_action':'copy','src':'a','dest':'b'}).parse() == ('copy',{'src':'a','dest':'b'},'localhost')

# class TaskExecutor(object):
#     '''
#     This is the main worker class for executing handlers and tasks.
#     '''
#
#     # ************************************************************
#     # Below are the subroutines used by the main

# Generated at 2022-06-13 06:58:31.334461
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser({'shell': 'ansible-playbook'})

    (action, args, delegate_to) = module_args_parser.parse()
    assert action == 'shell'
    assert args == dict(_raw_params='ansible-playbook')
    assert delegate_to is None

    module_args_parser = ModuleArgsParser({'action': {'module': 'shell', 'args': 'ansible-playbook'}})

    (action, args, delegate_to) = module_args_parser.parse()
    assert action == 'shell'
    assert args == dict(_raw_params='ansible-playbook')
    assert delegate_to is None

    module_args_parser = ModuleArgsParser({'module': 'shell', 'args': 'ansible-playbook'})


# Generated at 2022-06-13 06:58:32.870438
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    a = ModuleArgsParser()
    print(len(a.parse()))

# Generated at 2022-06-13 06:58:43.393568
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_dict = dict(
        action='shell',
        local_action=dict(
            module='command',
            args='echo "hello"'
        )
    )
    parser = ModuleArgsParser(task_ds=args_dict)
    assert parser.parse() == ('shell', {'_raw_params': u'"hello"'}, 'localhost')

    args_dict = dict(
        local_action='command hello'
    )
    parser = ModuleArgsParser(task_ds=args_dict)
    assert parser.parse() == ('command', {'_raw_params': u'hello'}, 'localhost')

    args_dict = dict(
        action=dict(
            module='shell',
            args=dict(
                chdir='/tmp'
            )
        )
    )

# Generated at 2022-06-13 06:58:57.109530
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #Case 1: task_ds is empty
    task_ds={}
    action=None
    args=None
    delegate_to=None
    ModuleArgsParser_obj=ModuleArgsParser(task_ds)
    assert ModuleArgsParser_obj.parse() == (action, args, delegate_to)
    #Case 2: task_ds is not empty
    task_ds={"action":{"module":"copy","args":{"src":"a","dest":"b"}}}
    action="copy"
    args={"src":"a","dest":"b"}
    delegate_to=None
    ModuleArgsParser_obj=ModuleArgsParser(task_ds)
    assert ModuleArgsParser_obj.parse() == (action, args, delegate_to)


# Generated at 2022-06-13 06:59:07.953304
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    play_context = PlayContext()
    # Test with required arg and non-required arg
    task2 = {'copy': {'src': "file", 'dest': "dest"}}
    task = ModuleArgsParser(task2).parse()
    assert isinstance(task, tuple)
    action, args, delegate_to = task
    assert action == 'copy'
    assert delegate_to == 'localhost'
    assert args['src'] == 'file'
    assert args['dest'] == 'dest'

    task2 = {'action': {'module': "copy src=file dest=dest"}}
    task = ModuleArgsParser(task2).parse()
    assert isinstance(task, tuple)
    action, args, delegate_to = task
    assert action == 'copy'
    assert delegate_to == 'localhost'
    assert args['src']

# Generated at 2022-06-13 06:59:17.579289
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("Testing ModuleArgsParser")

    def __test_thing(test_thing, test_action, test_args, test_delegate_to):
        parser = ModuleArgsParser(test_thing, collection_list=None)
        (action, args, delegate_to) = parser.parse()
        print("[{0}] action={1}, args={2}, delegate_to={3}".format(test_thing, action, args, delegate_to))
        assert action == test_action
        assert args == test_args
        assert delegate_to == test_delegate_to

    # test_thing_action_args_delegate_to
    thing_dict = {'action': 'shell echo hi'}
    action = 'shell'
    args = {'echo hi': True}
    delegate_to = None

# Generated at 2022-06-13 06:59:27.875836
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def test_ModuleArgsParser_parse_assertion_error(task_ds, msg, collection_list=None):
        with pytest.raises(AssertionError, message=msg):
            ModuleArgsParser(task_ds=task_ds, collection_list=collection_list).parse()

    task_ds = 'shell echo hi'
    msg = "the type of 'task_ds' should be a dict, but is a %s" % type(task_ds)
    test_ModuleArgsParser_parse_assertion_error(task_ds=task_ds, msg=msg)

    task_ds = {'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}}
    msg = 'Complex args must be a dictionary or variable string ("{{var}}").'
    test_ModuleArgsParser_parse_

# Generated at 2022-06-13 06:59:34.588608
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # Non-registered module name with complex args
    module_argparse = ModuleArgsParser(task_ds={'non-registered-module': {'arg1': True, 'arg2': 'hi'}})
    assert module_argparse.parse() == ('non-registered-module', {'arg1': True, 'arg2': 'hi'}, None)

    # Non-registered module with raw params
    module_argparse = ModuleArgsParser(task_ds={'non-registered-module': 'arg1=True arg2=hi'})
    assert module_argparse.parse() == ('non-registered-module', {'arg1': True, 'arg2': 'hi'}, None)

    # Non-registered module with raw params and complex args

# Generated at 2022-06-13 06:59:43.522848
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class Mock_all():
        def __init__(self):
            self.options = namedtuple('options', ['connection', 'module_path', 'forks', 'become',
                                                  'become_method', 'become_user', 'check', 'diff'])
            self.options.connection = 'smart'
            self.options.module_path = None
            self.options.forks = 5
            self.options.become = None
            self.options.become_method = None
            self.options.become_user = None
            self.options.check = False
            self.options.diff = False

        @property
        def basedir(self):
            return './test/unit/ansible'


# Generated at 2022-06-13 07:00:01.099920
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    connection = 'local'
    play_context = PlayContext()

# Generated at 2022-06-13 07:00:09.736569
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("TaskEntry.test_ModuleArgsParser_parse")
    test_task_ds1 = {
        'name': 'test_task_ds1',
        'action': 'copy src={{ var_src }} dest={{ var_dest }}'
    }
    test_task_ds2 = {
        'name': 'test_task_ds2',
        'action': {
            'module': 'copy src={{ var_src }} dest={{ var_dest }}'
        }
    }
    test_task_ds3 = {
        'name': 'test_task_ds3',
        'copy': {
            'src': '{{ var_src }}',
            'dest': '{{ var_dest }}'
        }
    }

# Generated at 2022-06-13 07:00:12.653818
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mod_args_parser = ModuleArgsParser(task_ds={"action": "copy src=a dest=b"})
    assert "copy" == mod_args_parser.parse()[0]
    assert "a" == mod_args_parser.parse()[1]['src']
    assert "b" == mod_args_parser.parse()[1]['dest']

# Generated at 2022-06-13 07:00:15.920478
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # create an instance of the class under test
    module_args_parser = ModuleArgsParser()

    # test with a string argument
    args = module_args_parser.parse(None)
    assert isinstance(args, tuple)
    assert len(args) == 3

    # test with a dict argument
    args = module_args_parser.parse({})
    assert isinstance(args, tuple)
    assert len(args) == 3



# Generated at 2022-06-13 07:00:26.642314
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    # case 1
    try:
        ModuleArgsParser(task_ds=None).parse()
    except SystemExit:
        pass
    # case 2
    try:
        ModuleArgsParser(task_ds='task_ds').parse()
    except AnsibleAssertionError:
        pass
    # case 3
    try:
        ModuleArgsParser(task_ds={'a': 'b'}).parse()
    except AnsibleParserError:
        pass
    # case 4
    try:
        ModuleArgsParser(task_ds={'action': 'task_ds'}).parse()
    except SystemExit:
        pass
    # case 5

# Generated at 2022-06-13 07:00:37.735336
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {"handler": {"name": "show running"} }

# Generated at 2022-06-13 07:00:45.499214
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    fake_collection_set = FakeCollectionSet()
    fake_collection_set.add_plugin({'plugins': []}, 'fake_collection1')
    fake_collection_set.add_plugin({'plugins': []}, 'fake_collection2')
    fake_collection_set.add_plugin({'plugins': []}, 'fake_collection3')
    #assert False

    parser = ModuleArgsParser(collection_list=fake_collection_set)
    (action, args, delegate_to) = parser.parse(dict())
    assert action is None
    assert len(args) == 0
    assert delegate_to is None

    (action, args, delegate_to) = parser.parse(dict(action=dict()))
    assert action is None
    assert len(args) == 0
    assert delegate_to is None


# Generated at 2022-06-13 07:00:49.664131
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = {}
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    assert module_args_parser.parse(True) == (None, dict(), Sentinel)

# class ActionModule(object):

# Generated at 2022-06-13 07:00:59.126437
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    unit test for method parse of class ModuleArgsParser
    '''

    task_ds = {'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}}
    parser = ModuleArgsParser(task_ds)
    action = 'copy'
    args = {'dest': 'b', 'src': 'a'}
    delegate_to = None
    assert parser.parse() == (action, args, delegate_to)

    task_ds = {'action': 'copy: src=a dest=b'}
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == (action, args, delegate_to)

    task_ds = {'action': 'copy src=a dest=b'}
    parser = ModuleArgsParser(task_ds)
    assert parser.parse()

# Generated at 2022-06-13 07:01:08.921957
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pars = ModuleArgsParser()
    assert pars.parse({ 'action' : 'shell echo hi' }) == ('shell', {'_raw_params': 'echo hi'})

    assert pars.parse({ 'local_action' : 'shell echo hi' }) == ('shell', {'_raw_params': 'echo hi'})

    assert pars.parse({ 'shell' : 'echo hi' }) == ('shell', {'_raw_params': 'echo hi'})
    assert pars.parse({ 'command' : 'echo hi' }) == ('shell', {'_raw_params': 'echo hi'})
    assert pars.parse({ 'script' : 'echo hi' }) == ('shell', {'_raw_params': 'echo hi'})


# Generated at 2022-06-13 07:01:29.203974
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import tempfile
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    task_ds = {'action': {'x': 2, 'y': 3}, 'delegate_to': 'me', 'with_items': ['foo', 'bar', 'baz'], 'with_first_found': 'test', '_variable_params': '{{test}}'}
    parser = TaskParser()
    result = parser.parse(task_ds=task_ds, play_context=None, variable_manager=VariableManager(loader=DataLoader()), loader=DataLoader())
    assert result.action == 'meta'
    assert result.module_name == 'meta'

# Generated at 2022-06-13 07:01:33.758700
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    data = load_fixture('ModuleArgsParser_parse.yml')
    c = ModuleArgsParser(data)
    res = c.parse()
    print(res)
    assert isinstance(res, tuple)
    assert res[0] == 'yum'
    assert res[1]['name'] == 'kernel-foo'
    assert res[2] is None



# Generated at 2022-06-13 07:01:41.122242
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'tags': ['test'], 'connection': 'local', '_ansible_no_log': False, 'any_errors_fatal': True,
               'become': False, 'become_user': None, 'become_method': None, 'module': 'debug',
               'args': {'msg': '{{ inventory_hostname }}\n'}}
    action = 'debug'
    args = {'msg': '{{ inventory_hostname }}\n'}
    delegate_to = None
    obj = ModuleArgsParser()
    (a, b, c) = obj.parse(task_ds)
    assert a == action
    assert b == args
    assert c == delegate_to


# AnsibleModule is part of the public ansible API and should not be removed or modified,
# if you need to change internal

# Generated at 2022-06-13 07:01:46.838201
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #Just a basic test that the class parses a simple Playbook action
    module_args = ModuleArgsParser.parse(dict(action = dict(module = 'setup')), skip_action_validation=False)
    assert module_args == ('setup',{},None)


# Generated at 2022-06-13 07:01:55.238329
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    optional_args = {'delegate_to': 'www.example.com'}
    assert len(ModuleArgsParser(optional_args).parse()[2]) == len('www.example.com') # assert optional_args['delegate_to'] is 'www.example.com'
    optional_args = ({'module': 'copy', 'src': 'a', 'dest': 'b'}, 'www.example.com')
    assert ModuleArgsParser(optional_args[0])[optional_args[1]] == 'www.example.com' # assert optional_args[1] (== 'www.example.com') is in optional_args[0]
    optional_args = {'action': 'copy src=a dest=b'}

# Generated at 2022-06-13 07:02:04.127099
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'debug': {
            'msg': 'This is a message',
            'verbosity': 3
        }
    }
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    assert module_args_parser.parse()[0] == 'debug'
    assert module_args_parser.parse()[1] == { 'msg': 'This is a message',
                                              'verbosity': 3}
    assert module_args_parser.parse()[2] is None

# Generated at 2022-06-13 07:02:11.682120
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module = AnsibleModule(
        argument_spec = dict(
            data = dict(type='dict', required=True),
            collection_list = dict(type='list', required=True),
            ),
        supports_check_mode=True
    )
    data = module.params['data']
    collection_list = module.params['collection_list']
    try:
        parser = ModuleArgsParser(task_ds=data, collection_list=collection_list)
        (action, args, delegate_to) = parser.parse()
    except Exception as e:
        module.fail_json(msg=to_native(e), exception=traceback.format_exc())
    result = dict(
      action = action,
      args = args,
      delegate_to = delegate_to,
    )

# Generated at 2022-06-13 07:02:27.183007
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # regular case without any extra args
    parsed = ModuleArgsParser(
        task_ds={'action': 'shell sleep 1'},
        collection_list=['collections/ansible_collections/test/test_namespace/plugins/actions']
    ).parse()
    assert parsed[0] == 'shell'
    assert parsed[1] == {'_raw_params': 'sleep 1'}
    assert parsed[2] is None

    # regular case, with extra args
    parsed = ModuleArgsParser(
        task_ds={'action': 'shell sleep 1', 'async': '5'},
        collection_list=['collections/ansible_collections/test/test_namespace/plugins/actions']
    ).parse()
    assert parsed[0] == 'shell'

# Generated at 2022-06-13 07:02:31.201091
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = {'action': "tasks", 'tasks':'helloworld'}
    collection_list = ["tasks"]
    retval = ModuleArgsParser(ds, collection_list).parse()
    assert retval == ('tasks', {'tasks': 'helloworld'}, None)



# Generated at 2022-06-13 07:02:45.333753
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds={'a': 1, 'args': {'xyz': 'abc'}}, collection_list=[])
    parser._normalize_new_style_args = MagicMock(return_value={'abc': 'abc'})
    parser._normalize_parameters = MagicMock(return_value=('ab', {'xyz': 'abc'}))
    parser.resolved_action = 'false'
    (action, args, delegate_to) = parser.parse()

    assert action == 'ab'
    assert args == {'xyz': 'abc'}
    assert delegate_to == Sentinel
    # Test that _normalize_parameters() is called with right arguments
    args, _ = parser._normalize_parameters.call_args
    assert _ == {'xyz': 'abc'}

# Generated at 2022-06-13 07:03:32.118394
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    pap = ModuleArgsParser(task_ds, collection_list)
    result = pap.parse()
    assert result == (None, {}, None)

# Generated at 2022-06-13 07:03:41.302746
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.dataloader import DataLoader

    class MockVarsModule:
        def __init__(self):
            pass

        def add_directory(self, *args, **kwargs):
            pass

    class MockLoader:
        def __init__(self):
            self.vars = MockVarsModule()

    class MockTemplar:
        def __init__(self):
            pass

        def is_template(self, template):
            return True

        def is_immortal_variable(self, variable):
            return False

    loader = MockLoader()
    templar = MockTemplar()
    task_hash = {
        'name': 'test',
        'include_tasks': dict(files='test.yml', name='test')
    }
    namespace = 'test'

# Generated at 2022-06-13 07:03:49.186599
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # In this test, we want to test the parsing of a 'command' module invocation.
    # The setUp method at the end of the class will help us to initialize the parser.
    task_ds = dict(
        args = dict(
            chdir='/tmp'
        ),
        command='pwd',
    )
    action, args, delegate_to = map(lambda x: ModuleArgsParser(task_ds).parse()[x], range(3))
    assert action == command
    assert args == dict(_raw_params='pwd', chdir='/tmp')
    assert delegate_to is Sentinel

    # In this test, we want to test the parsing of a 'shell' module invocation
    # with both old-style and new-style arguments.
    # The setUp method at the end of the class will help us to initialize the parser.
   

# Generated at 2022-06-13 07:04:00.689648
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test valid task definition
    task_ds = dict(
        action=dict(module='copy', src='a', dest='b'))
    result = ModuleArgsParser(task_ds).parse()
    assert_equal(result, ('copy', dict(src='a', dest='b'), None))

    # test extra parameters
    task_ds = dict(
        action='copy src=a dest=b')
    with pytest.raises(AnsibleParserError):
        ModuleArgsParser(task_ds).parse()

    # test valid task definition with raw_params but without $var
    task_ds = dict(
        action='copy src=a dest=b date={{ansible_date_time.iso8601}}')
    result = ModuleArgsParser(task_ds).parse()

# Generated at 2022-06-13 07:04:10.080734
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mock_task_ds = dict()
    mock_collection_list = list()
    module_args_parser = ModuleArgsParser(mock_task_ds, mock_collection_list)
    with pytest.raises(AnsibleAssertionError) as pytest_wrapped_e:
        module_args_parser.parse()
    assert pytest_wrapped_e.type == AnsibleAssertionError

    mock_task_ds = dict()
    mock_collection_list = list()
    module_args_parser = ModuleArgsParser(mock_task_ds, mock_collection_list)
    result = module_args_parser.parse()
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert result[0] is None
    assert result[1] == {}

# Generated at 2022-06-13 07:04:19.479786
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'module': 'command', '_raw_param': 'ls', '_variable_params': 'command'}}
    collection_list = [
        {'name': 'core', 'version': 1.0},
        {'name': 'core', 'version': 2.0}]
    f = ModuleArgsParser(task_ds, collection_list)
    (action, args, delegate_to) = f.parse()

# ########################################
# class ActionModule
# ########################################

# Generated at 2022-06-13 07:04:28.548068
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:34.706416
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds={'remote_user': None, 'become': None, 'become_user': None, 'become_method': None, 'connection': 'smart', 'become_flags': None, 'check_mode': False, 'module_defaults': {}, 'module_path': '', 'no_log': False, 'action': 'cpanm', '_ansible_check_mode': False, '_ansible_verbosity': 0, '_ansible_version': '2.10.1', '_ansible_syslog_facility': 'LOG_USER', '_ansible_notify': set(), '_ansible_no_log': False},
                             collection_list=None)

# Generated at 2022-06-13 07:04:43.096032
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # empty case
    obj = ModuleArgsParser(task_ds=dict())
    assert (obj.parse() == (None, dict(), Sentinel))
    # action + additional args
    obj = ModuleArgsParser(task_ds=dict(action='foo', args='xyz=1'))
    assert (obj.parse() == ('foo', dict(xyz='1'), Sentinel))
    # local_action + additional args
    obj = ModuleArgsParser(task_ds=dict(local_action='foo', args='xyz=1'))
    assert (obj.parse() == ('foo', dict(xyz='1'), 'localhost'))
    # action + module
    obj = ModuleArgsParser(task_ds=dict(action='foo', module='bar'))
    with pytest.raises(AnsibleParserError):
        obj.parse()


# Generated at 2022-06-13 07:04:53.207628
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert False, "Test not implemented"

# class ShellModuleTestCase(unittest.TestCase):
#     '''
#     This test case tests the functionality of ShellModule, which is
#     a basic action module that is used sometimes when there is no
#     better module such as raw, script, etc.
# 
#     We test that ShellModule is available and will parse the args.
#     '''
# 
#     def test_parsing(self):
#         '''
#         test parsing the args.
#         '''
#         # This is the standard YAML form for command-type modules. We grab
#         # the args and pass them in as additional arguments, which can/will
#         # be overwritten via dict updates from the other arg sources below
#         additional_args = dict(warn=True)
#

# Generated at 2022-06-13 07:05:16.437068
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Set up for test
    task_ds = {"action": "copy src=a dest=b"}
    parser = ModuleArgsParser(task_ds)
    # Actual test
    parser.parse()

# Generated at 2022-06-13 07:05:27.793302
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser({})
    import pytest
    from ansible.module_utils.six.moves import builtins
    with pytest.raises(AnsibleAssertionError) as excinfo:
        module_args_parser.parse()
    excinfo.match("'task_ds' should be a dict, but is a .*")
    module_args_parser = ModuleArgsParser('action: ping')
    with pytest.raises(AnsibleParserError) as excinfo:
        module_args_parser.parse()
    excinfo.match("unexpected parameter type in action: <type 'str'>")

    module_args_parser = ModuleArgsParser({'action': 'ping'})
    (action, args, delegate_to) = module_args_parser.parse()

# Generated at 2022-06-13 07:05:29.597644
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    assert parser.parse() ==  ('', {}, None)


# Generated at 2022-06-13 07:05:33.308278
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """test_ModuleArgsParser"""

    result = ModuleArgsParser(task_ds=None, collection_list=None)

    assert result.parse(skip_action_validation=False) == (None, {}, Sentinel)


# Generated at 2022-06-13 07:05:47.975705
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    base_task = dict(action='setup')
    test_task = base_task.copy()
    action, args, delegate_to = ModuleArgsParser(test_task).parse()
    assert action == 'setup'
    assert args == {}
    assert delegate_to == Sentinel

    base_task = dict(setup=dict())
    test_task = base_task.copy()
    action, args, delegate_to = ModuleArgsParser(test_task).parse()
    assert action == 'setup'
    assert args == {}
    assert delegate_to == Sentinel

    base_task = dict(setup="")
    test_task = base_task.copy()
    action, args, delegate_to = ModuleArgsParser(test_task).parse()
    assert action == 'setup'
    assert args == {}
    assert delegate_to == Sentinel

    base

# Generated at 2022-06-13 07:05:54.903992
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:06:03.262767
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(
        {'action': 'copy src=/tmp/foo dest=/tmp/bar'},
        collection_list=COLLECTION_LIST
    )
    # Generate test cases for all modules
    for module_name in module_loader.all(collection_list=COLLECTION_LIST):
        try:
            res = parser.parse(skip_action_validation=True)
        except AnsibleParserError:
            pass
        else:
            assert res[0] == module_name, module_name
            assert res[1] == {'src': '/tmp/foo', 'dest': '/tmp/bar'}, module_name
            # we don't have a good way of testing this
            # assert res[2] == None, module_name
            # assert parser.resolved_action is not None, module_name


# Generated at 2022-06-13 07:06:06.348778
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    ModuleArgsParser:parse test stub.
    '''
    # FIXME: construct object for test
    # module = ModuleArgsParser(task_ds=None, collection_list=None)
    # FIXME: method test call
    # assert(False)



# Generated at 2022-06-13 07:06:14.390013
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.handler import Handler
    m = ModuleArgsParser(task_ds={'action': {'shell': 'echo hi'}}, collection_list={'ansible.builtin': ['answers']})
    assert m._task_attrs == frozenset(set(Handler._valid_attrs))
    assert m._task_ds == {'action': {'shell': 'echo hi'}}
    assert m._collection_list == {'ansible.builtin': ['answers']}
    assert m.resolved_action is None
    assert m.parse() == ('shell', {'_uses_shell': True, '_raw_params': 'echo hi'}, Sentinel)

# Generated at 2022-06-13 07:06:21.830854
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    task_ds = {}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    task_ds = {}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    task_ds = {}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)