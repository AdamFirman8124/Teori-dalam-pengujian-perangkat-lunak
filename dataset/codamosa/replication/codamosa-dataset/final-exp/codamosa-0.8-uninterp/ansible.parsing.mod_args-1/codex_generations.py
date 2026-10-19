

# Generated at 2022-06-13 06:56:49.730168
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import json
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.parsing.yaml.loader import AnsibleLoader
    # load the module_args.yml for use in testing
    loader = AnsibleLoader(open('./test/units/parsing/yaml/module_args.yml'),
                           byteify=True)

    # use the module_args.yml file to test all of the parsers
    test_list = loader.get_single_data()

    # normalize the test_list so that the format from the YAML file is
    # changed to the format that the parser is expecting
    for data in test_list:
        # this is the "input" for the module_args parser
        input_data = data['input']
        # this is the expected

# Generated at 2022-06-13 06:56:53.081840
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

ModuleArgsParser._normalize_old_style_args.__test__ = False
ModuleArgsParser.__init__.__test__ = False
ModuleArgsParser._normalize_new_style_args.__test__ = False
ModuleArgsParser._normalize_parameters.__test__ = False
ModuleArgsParser._split_module_string.__test__ = False

# Generated at 2022-06-13 06:57:04.298334
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = mock.mock_open(read_data='{"foo": "bar"}')
    with mock.patch('ansible.playbook.task.open', m, create=True):
        args_parser = ModuleArgsParser()
        #
        # test with task_ds=None, collection_list=None
        #
        args_parser.parse()
        #
        # test with task_ds={}, collection_list=None
        #
        args_parser.parse()
        #
        # test with task_ds={'action': 'shell echo hi'}, collection_list=None
        #
        args_parser.parse()
        #
        # test with task_ds={'local_action': 'shell echo hi'}, collection_list=None
        #
        args_parser.parse()
        #
        # test with task_

# Generated at 2022-06-13 06:57:13.603818
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Set up test data
    test_data = dict()

    test_data['play'] = {
        'name': 'helloworld',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {
                'name': 'greeting',
                'debug': 'msg=hello world'
            }
        ]
    }

    td = test_data['play']

    # Run the task parsing process
    task_ds = td['tasks'][0]
    action, args, delegate_to = ModuleArgsParser(task_ds).parse()

    # Verify the results
    assert action == 'debug'
    assert args == {'msg': 'hello world'}
    assert delegate_to is None

# Generated at 2022-06-13 06:57:28.236369
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:33.260948
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:46.240316
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'action': {
            'module': 'copy',
            'src': 'a',
            'dest': 'b'
        },
        'delegate_to': 'seneca.example.org',
        'args': {
            'attributes': 'mode=0644'
        }
    }
    expected_action = 'copy'
    expected_delegate_to = 'seneca.example.org'
    expected_args = {
        'src': 'a',
        'dest': 'b',
        'attributes': 'mode=0644'
    }
    parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = parser.parse()
    assert action == expected_action
    assert args == expected_args
    assert delegate_to == expected_de

# Generated at 2022-06-13 06:57:53.635723
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:58:02.078855
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.errors import AnsibleParserError

    # In TestModuleArgsParser.setup_class() we registered a fake module
    # 'test-module' (see TestModuleArgsParser below)
    task = dict(action='test-module')
    parser = ModuleArgsParser(task_ds=task, collection_list=None)
    assert parser.parse() == ('test-module', {}, Sentinel)

    task = dict(action='test-module', args=dict(foo='bar'))
    parser = ModuleArgsParser(task_ds=task, collection_list=None)
    assert parser.parse() == ('test-module', {'foo': 'bar'}, Sentinel)

    task = dict(action='test-module', args=dict(foo='bar'), delegate_to='localhost')

# Generated at 2022-06-13 06:58:09.318303
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Test case : Test the try except block of parse() method of ModuleArgsParser
    """
    # Execution 1, Arguments: _task_ds = None
    module_arg_parser = ModuleArgsParser(task_ds=None)
    try:
        module_arg_parser._task_ds = module_arg_parser._task_ds
    except Exception:
        module_arg_parser.parse(skip_action_validation=False)
    # Execution 2: Task is not a 'dict' type
    try:
        module_arg_parser = ModuleArgsParser(task_ds=121)
    except Exception:
        module_arg_parser.parse(skip_action_validation=False)
    task_ds = {'action': {'module': 'copy', 'src':'a', 'dest':'b'}}
    # Execution

# Generated at 2022-06-13 06:58:33.199110
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    with pytest.raises(AnsibleAssertionError):
        parser.parse(task_ds="something")
    with pytest.raises(AnsibleError):
        parser.parse(task_ds={"action": 'copy src=a dest=b'})
    with pytest.raises(AnsibleError):
        parser.parse(task_ds={"action": 'copy src=a dest=b', "args": {1: 2}})
    with pytest.raises(AnsibleError):
        parser.parse(task_ds={"action": {'module': 'xyz'}, "args": {1: 2}})
    with pytest.raises(AnsibleParserError):
        parser.parse(task_ds={"action": 'unknown'})

# Generated at 2022-06-13 06:58:42.999123
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test = {'action': {'module': 'command', 'args': 'echo hi', 'warn': False}}
    parser = ModuleArgsParser(task_ds=test, collection_list=None)
    action, args, delegate_to = parser.parse()
    assert (action, args, delegate_to) == ('command', {'_raw_params': 'echo hi', 'warn': False}, None)
    test = {'action': {'module': 'command', 'args': 'echo hi', 'warn': False}}
    parser.task_ds = test
    action, args, delegate_to = parser.parse()
    assert (action, args, delegate_to) == ('command', {'_raw_params': 'echo hi', 'warn': False}, None)



# Generated at 2022-06-13 06:58:51.030281
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class MockTask():
        task_ds = {'action': 'copy src=a dest=b',
                   'args': {'other_var': 'foo'},
                   'delegate_to': 'localhost'}
    
    mock_task = MockTask()
    parser = ModuleArgsParser(task_ds=mock_task.task_ds)
    parser.parse()


# Generated at 2022-06-13 06:59:02.808644
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    # Test with non-dicts
    #

    # test_massive_args
    task_ds = 123
    parser = ModuleArgsParser(task_ds=task_ds)
    with pytest.raises(AnsibleAssertionError):
        parser.parse()

    # test_non_dict
    task_ds = 'string'
    parser = ModuleArgsParser(task_ds=task_ds)
    with pytest.raises(AnsibleAssertionError):
        parser.parse()

    # test_list
    task_ds = [1, 2, 3]
    parser = ModuleArgsParser(task_ds=task_ds)
    with pytest.raises(AnsibleAssertionError):
        parser.parse()

    # test_tuple

# Generated at 2022-06-13 06:59:10.463085
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = dict(
        action = dict(
            x = dict(
                sub_x = 'a'
            ),
            module = 'copy src=b dest=c',
            action = 'shell echo hi',
            local_action = dict(
                module = 'copy src=c dest=d'
            )
        ),
        args = dict(
            chdir = '/tmp'
        ),
        delegate_to = 'test'
    )
    parser = ModuleArgsParser(task_ds=args)
    assert(parser.parse() == ('shell', dict(_raw_params='echo hi', _uses_shell=True), 'test'))

# Generated at 2022-06-13 06:59:18.377728
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # Create the object that is normally instantiated by the parser.
    module_parser = ModuleArgsParser()

    # Test for the correct operation of ModuleArgsParser.parse()
    # Create a task dictionary with a bad module/action and verify that parse() throws an AnsibleParserError exception.
    task_ds = dict(name='test_bad_module', action='bad_module')
    assertRaisesRegex(AnsibleParserError, "couldn't resolve module/action 'bad_module'", module_parser.parse, task_ds=task_ds)

    # Create a task dictionary with a local_action and verify that parse() throws an AnsibleParserError exception.
    task_ds = dict(name='test_local_action', local_action='command echo hi')

# Generated at 2022-06-13 06:59:21.385454
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    result = module_args_parser.parse()
    assert result == None , 'parser did not raise AnsibleParserError exception'


# Generated at 2022-06-13 06:59:31.186210
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    loader = AnsibleCollectionLoader()
    collection = loader.collections[0]
    action_loader.add_directory(collection._action_dir)
    module_loader.add_directory(collection._module_utils_dir)

    task_data = dict()
    task_data = {"action": "shell", "args": "pwd"}
    args_parser = ModuleArgsParser(task_data, collection_list=[collection])
    assert args_parser.parse() == ('shell', {"args": "pwd"}, None)

    task_data = {"action": "pwd"}
    args_parser = ModuleArgsParser(task_data, collection_list=[collection])
   

# Generated at 2022-06-13 06:59:36.239538
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'name': 'test'}
    parser = ModuleArgsParser(task_ds=task_ds)
    parser.parse()
    # Check for exceptions raised
    with pytest.raises(AnsibleParserError, match=r"couldn't resolve module/action ''\."):
        parser.parse()


# Generated at 2022-06-13 06:59:44.674212
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Testing parameter skip_action_validation
    action = 'shell'
    args = {'_raw_params': 'echo hi'}
    delegate_to = None
    thing = 'echo hi'
    additional_args = {}
    skip_action_validation = False


    # Testing parameter delegate_to
    delegate_to = 'localhost'


    # Testing parameter thing
    thing = {'module': 'shell', '_raw_params': 'echo hi'}


    # Testing parameter action
    action = 'shell'
    args = {'_raw_params': 'echo hi', 'chdir': '/tmp'}
    thing = 'shell echo hi'


    # Testing parameter args
    args = {'_raw_params': 'echo hi', 'chdir': '/tmp'}


    # Testing parameter action

# Generated at 2022-06-13 06:59:52.307151
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser({}, {})
    args = module_args_parser.parse()
    eq_(args, ('', {}, Sentinel))


# Generated at 2022-06-13 07:00:02.924688
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_parser = ModuleArgsParser()

    # Test __init__
    assert test_parser._task_ds == {}
    assert test_parser._collection_list is None

        # Test _split_module_string
    assert test_parser._split_module_string('shell echo hi') == ('shell', 'echo hi')
    assert test_parser._split_module_string('shell "echo hi"') == ('shell', '"echo hi"')

    # Test _split_module_string with an error
    try:
        test_parser._split_module_string(None)
        assert False
    except:
        assert True

    # Test _normalize_parameters
    assert test_parser._normalize_parameters(thing='echo hi', action='shell') == ('shell', {'_raw_params': 'echo hi'})

    assert test

# Generated at 2022-06-13 07:00:10.992928
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.errors import AnsibleParserError, AnsibleError
    from ansible.playbook.task_include import TaskInclude

    class AnsibleOptions:
        def __init__(self, verbosity=0, modules='', action_plugins='', callback_whitelist='', forks=5, check=False,
                     diff=False, step=False, syntax=False, start_at_task=None, inventory=None, force_handlers=False,
                     flush_cache=False, listhosts=False, listtasks=False, listtags=False, module_path='',
                     extra_vars=None, private_key_file=None, connection_type='', vault_password_files="", verbosity_level=0):
            self.verbosity = verbosity
            self.modules = modules
            self.action_plugins = action

# Generated at 2022-06-13 07:00:14.276849
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'module': 'test', 'arg1': 'arg2'}, 'delegate_to': 'test_delegate_to'}
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = obj.parse()
    assert action == 'test'
    assert delegate_to == 'test_delegate_to'


# Generated at 2022-06-13 07:00:19.066750
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    datadict = {'tasks':[{'debug': {'msg': '{{msg}}'}}]}
    parser = ModuleArgsParser(task_ds=datadict, collection_list=[])
    action, args, delegate_to = parser.parse()
    assert action == 'debug' and delegate_to == None and args['msg'] == '{{msg}}'

    datadict = {'tasks':[{'apt': {'cache_valid_time': 0}}]}
    parser = ModuleArgsParser(task_ds=datadict, collection_list=[])
    action, args, delegate_to = parser.parse()
    assert action == 'apt' and delegate_to == None and args['cache_valid_time'] == 0

    datadict = {'tasks':[{'command': 'echo hi'}]}

# Generated at 2022-06-13 07:00:24.363123
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'test': 'test'}
    collection_list = "test"
    arg_parser = ModuleArgsParser(task_ds, collection_list)
    arg_parser.parse()


# pylint: disable=too-many-instance-attributes,too-many-public-methods,protected-access

# Generated at 2022-06-13 07:00:34.761984
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(task_ds={'action': 'xyz', ' delegate_to': 'localhost', 'a':1, 'b':2, 'shell': 'echo hi', 'args': {'x': 1, 'y': 2}})
    assert m.parse() == ('shell', {'x': 1, 'y': 2}, 'localhost')

    m = ModuleArgsParser(task_ds={'action': {'module': 'xyz', 'a': 1, 'b': 2}})
    assert m.parse() == ('xyz', {'a': 1, 'b': 2, '_raw_params': ''}, None)

    m = ModuleArgsParser(task_ds={'action': 'xyz a="b" c=1'})

# Generated at 2022-06-13 07:00:40.721940
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:00:43.092921
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    obj = ModuleArgsParser()
    assert obj is not None
##############################################################################################



# Generated at 2022-06-13 07:00:43.538287
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

# Generated at 2022-06-13 07:00:49.930071
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # NOTE: Can't test a method with a keyword arg, it fails.
    print("TODO:  Implement test")

# Generated at 2022-06-13 07:00:54.726854
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    inst = ModuleArgsParser({'action': {'module': 'wget', 'url': 'https://www.saltstack.com/'}})
    assert inst.parse() == ('wget', {'url': 'https://www.saltstack.com/', '_raw_params': 'url=https://www.saltstack.com/'}, None)



# Generated at 2022-06-13 07:01:02.587966
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mod_args_parser = ModuleArgsParser(task_ds={'action': 'shell echo hello'})
    mod_args_parser.parse()

    mod_args_parser = ModuleArgsParser(task_ds={'action': 'echo hello'})
    try:
        mod_args_parser.parse()
    except Exception as e:
        assert isinstance(e, AnsibleParserError)

    mod_args_parser = ModuleArgsParser(task_ds={'kvm': {'name': 'hello'}})
    try:
        mod_args_parser.parse()
    except Exception as e:
        assert isinstance(e, AnsibleParserError)

    mod_args_parser = ModuleArgsParser(task_ds={'kvm': {'name': 'hello'}})

# Generated at 2022-06-13 07:01:03.601745
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    raise NotImplementedError


# Generated at 2022-06-13 07:01:13.907595
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # HACK: why are these not FieldAttributes on task with a post-validate to check usage?
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    task_attrs.update(['local_action', 'static'])
    task_attrs = frozenset(task_attrs)

    task_ds = {'action': {'module': 'copy', 'src': None, 'dest': 'q', 'args': None}, 'delegate_to': 'localhost', 'with_items': [1, 2, 3]}

    a = ModuleArgsParser(task_ds)


# Generated at 2022-06-13 07:01:20.329518
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes

    try:
        # python 2
        unicode
    except NameError:
        # python 3
        unicode = str

    # Test when 'delegate_to' is not present in the _task_ds
    # test with multiple kv pairs in the action
    task_ds = dict()
    task_ds['action'] = 'shell echo hi'
    parser = ModuleArgsParser(task_ds=task_ds)
    actual_action, actual_args, actual_delegate_to = parser.parse()
    expected_action = 'shell'
    expected_args = dict()

# Generated at 2022-06-13 07:01:27.900419
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    thing = {'module': 'copy', 'arg1': '1', 'arg2': '2'}
    ds = { 'action': thing}
    parser = ModuleArgsParser(task_ds=ds)
    (action, args, delegate_to) = parser.parse()
    expected_action = 'copy'
    expected_args = {'arg1': '1', 'arg2': '2'}
    assert action == expected_action
    assert args == expected_args
    assert delegate_to is None

    ds = { 'action': 'copy arg1=1 arg2=2'}
    parser = ModuleArgsParser(task_ds=ds)
    (action, args, delegate_to) = parser.parse()
    expected_action = 'copy'

# Generated at 2022-06-13 07:01:36.708825
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    l_task_ds = {
        'tasks': [
            {
                'action': 'copy src=a dest=b',
                'delegate_to': 'localhost',
                'args': {'x': 2, 'y': 3}
            }
        ]
    }

    l_module = ModuleArgsParser(l_task_ds)
    l_action, l_args, l_delegate_to = l_module.parse()
    assert l_action == 'copy'
    assert l_args == {'src': 'a', 'dest': 'b', 'x': 2, 'y': 3}, \
        'action args error ' + str(l_args) + " except {'src': 'a', 'dest': 'b', 'x': 2, 'y': 3}"

# Generated at 2022-06-13 07:01:43.470751
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml.common import AnsibleParserError
    task_ds = {}
    collection_list = []
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    assert obj.parse() == (None, {}, Sentinel)
    task_ds = 0
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

# Generated at 2022-06-13 07:01:54.185078
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    parser = ModuleArgsParser()
    task_ds = {'action': 'copy src=a dest=b'}
    thing = {'module': 'shell echo hi'}
    action = 'shell'

    # running the whole script with no params, it will run action.yml
    parser.parse()

    # running the whole script with --help, it will run action.yml (only for ansiballz)
    parser.parse()

    # test with different 'thing' inputs
    task_ds = {'action': thing}
    action, args, delegate_to = parser.parse(skip_action_validation=True)
    assert action == action
    assert args == {'_raw_params': 'echo hi'}

# Generated at 2022-06-13 07:02:07.885170
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({"action":"ping", "args":{"_raw_params":"-c 4", "data":"pong"}})
    assert parser.parse() == ('ping', {'_raw_params': '-c 4', 'data': 'pong'}, None)



# Generated at 2022-06-13 07:02:12.359069
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.errors import AnsibleError

    # simple task
    module_data = {'action' : 'shell echo hi'}
    module_data = ModuleArgsParser(module_data).parse()
    assert module_data == ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, None)
    module_data = {'action': {'module': 'shell echo hi'}}
    module_data = ModuleArgsParser(module_data).parse()
    assert module_data == ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, None)

    # complex task args

# Generated at 2022-06-13 07:02:23.856828
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    fixture_data = {
        'action': {
            'module': 'shell echo hi',
            'delegate_to': 'localhost',
            'args': 'region=xyz',
            'foo': 'unexpected key',
            'async': 5,
            'poll': 5,
        },
        'expected': ('shell', {'_raw_params': 'echo hi', 'region': 'xyz'}, 'localhost'),
    }

    for fixture_label, args, expected in iteritems(fixture_data):
        assert ModuleArgsParser(args).parse() == expected

# Generated at 2022-06-13 07:02:25.157141
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME: add unit tests
    pass

# Generated at 2022-06-13 07:02:33.914557
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser_instance = ModuleArgsParser(task_ds={'action': 'copy', 'args': {'src': 'a', 'dest': 'b'}})
    # When nothing is passed as additional_args, the args should contain
    # only the dictionary(args: {src: a, dest: b}) as the args.
    action, args, delegate_to = module_args_parser_instance._normalize_parameters(thing={'src': 'a', 'dest': 'b'})
    assert action is None
    assert args == {'src': 'a', 'dest': 'b'}
    # When args are passed as additional_args, args dictionary should
    # contain additional_args and the passed args.

# Generated at 2022-06-13 07:02:34.774888
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True

# Generated at 2022-06-13 07:02:43.423857
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds={'name': 'test_name', 'register': 'test_register', 'delegate_to': 'test_delegate_to', 'local_action': {}, 'action': {}}
    collection_list=['test_collection_list']
    expected = (None, {}, 'test_delegate_to')
    result = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list).parse()
    assert expected == result


# Generated at 2022-06-13 07:02:54.805490
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
    collection_list = list()
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    obj._normalize_parameters = Mock()
    obj._normalize_new_style_args = Mock()
    obj._normalize_old_style_args = Mock()
    obj.resolved_action = 'test resolved_action'
    action = 'test action'
    obj._task_ds = dict(action=action)
    res = obj.parse()
    assert res[0] == action
    assert res[1] == obj.resolved_action

    obj._task_ds = dict(action='test action', delegate_to='test delegate_to')
    res = obj.parse()
    assert res[0] == action
    assert res[1] == obj

# Generated at 2022-06-13 07:03:01.947221
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  '''
  Unit test for:
    parse method of class ModuleArgsParser
  '''
  # Expected output of parse method
  expected = ('ec2', {'action':'run_instance', 'region':'us-east-1', 'name':'test'}, None)
  # Test parse method with action as dict
  # task_ds must have only 'module' or 'action' key
  task_ds = {'action': {'module': 'ec2', 'action': 'run_instance', 'region': 'us-east-1', 'name': 'test'}}
  module_args_parser = ModuleArgsParser(task_ds)
  result = module_args_parser.parse()
  assert result == expected
  # Test parse method with action as string
  # task_ds must have only 'module' or 'action' key


# Generated at 2022-06-13 07:03:10.625029
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = dict(action='shell')
    a = ModuleArgsParser(args)
    try:
        a.parse()
    except AnsibleParserError:
        assert True
    args['action'] = dict(module='shell')
    a = ModuleArgsParser(args)
    try:
        a.parse()
    except AnsibleParserError:
        assert True


    args = dict(action=dict(module='shell', args='echo hi'))
    a = ModuleArgsParser(args)
    (action, args, delegate_to) = a.parse()
    assert action == 'shell'
    assert isinstance(args, dict)
    assert args['args'] == 'echo hi'
    assert delegate_to == Sentinel

    args = dict(action=dict(module='shell', args=dict(echo='hi')))
    a = Module

# Generated at 2022-06-13 07:03:21.519369
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell', 'args': {'chdir': '/tmp'}, 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=task_ds, collection_list=[])
    expected = ('shell', {'_raw_params': '', 'chdir': '/tmp'}, 'localhost')
    assert parser.parse() == expected


#
# CODE UNDER TEST
#

BUILTIN_TASKS = frozenset(('meta', 'debug', 'include', 'import_playbook', 'include_tasks', 'import_tasks', 'pause', 'wait_for', 'async_status', 'async_wait'))

RAW_PARAM_MODULES = frozenset(('command', 'shell', 'win_shell', 'raw'))

# made available

# Generated at 2022-06-13 07:03:23.104676
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pytest.skip("TODO")

# Generated at 2022-06-13 07:03:38.161581
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    arp = AnsibleRoleParser()
    arp.fqcn_map = dict()
    arp.index_lookup = dict()
    arp.index_lookup['task'] = 1
    arp.index_lookup['name'] = 1
    arp.index_lookup['action'] = 1
    arp.index_lookup['module'] = 1
    arp.index_lookup['local_action'] = 1
    arp.index_lookup['args'] = 1
    arp.index_lookup['delegate_to'] = 1
    arp.index_lookup['templar'] = 1
    arp.index_lookup['playbook_dir'] = 1
    arp.index_lookup['static'] = 1
    ar

# Generated at 2022-06-13 07:03:42.461406
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args = 'src=/etc/hosts dest=/tmp/hosts'
    module = 'copy'
    task_ds = { module: module_args }

    parser = ModuleArgsParser(task_ds, None)

    action, args, delegate_to = parser.parse()

    assert action == module
    assert args == { 'src': '/etc/hosts', 'dest': '/tmp/hosts'}
    assert delegate_to == Sentinel

# unit test for method _split_module_string of class ModuleArgsParser

# Generated at 2022-06-13 07:03:50.746966
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds=None, collection_list=None)
    module_string = "shell echo hi"
    tokens = parser._split_module_string(module_string=module_string)
    assert tokens == ("shell", "echo hi")
    module_string = "shell"
    tokens = parser._split_module_string(module_string=module_string)
    assert tokens == ("shell", "")
    thing = dict(module='copy src=test dest=test1')
    action = "copy"
    additional_args = dict()
    results = parser._normalize_parameters(thing=thing, action=action, additional_args=additional_args)
    assert results == ("copy", dict(src="test", dest="test1"))
    thing = dict(module='copy src=a dest=b')
   

# Generated at 2022-06-13 07:03:55.226553
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    sample_task_ds = {
        'action': u'copy',
        'args': {
            'src': u'/abc',
            'dest': u'/xyz'
        },
        'async': 10,
        'delegate_to': u'localhost',
        'poll': 10,
        'register': u'res'
    }
    sample_task_ds_with_module = {
        'module': u'copy',
        'delegate_to': u'localhost',
        'args': {
            'src': u'/abc',
            'dest': u'/xyz'
        },
        'async': 10,
        'poll': 10,
        'register': u'res'
    }

# Generated at 2022-06-13 07:04:06.222248
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_spec = dict()
    module_arg_spec['args'] = dict()
    module_arg_spec['args']['host'] = dict()
    module_arg_spec['args']['host']['required'] = True
    module_arg_spec['args']['host']['type'] = 'str'
    module_arg_spec['args']['host']['default'] = None
    module_arg_spec['args']['host']['choices'] = list()
    module_arg_spec['args']['host']['aliases'] = list()
    module_arg_spec['args']['host']['version_added'] = None
    module_arg_spec['args']['host']['no_log'] = False

# Generated at 2022-06-13 07:04:12.769450
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_module_ansible_facts_init = ModuleArgsParser()

    test_module_ansible_facts_init._task_ds = dict()
    test_module_ansible_facts_init._task_ds['action'] = {'ansible_facts': {'gather_subset': ['all'], 'gather_timeout': '10'}}
    result_should_be = ('ansible_facts', {'gather_subset': ['all'], 'gather_timeout': '10'}, None)
    assert test_module_ansible_facts_init.parse() == result_should_be

    # It seems there is no way to get action=None with action in a dict,
    # so we skipping this test case

    test_module_ansible_facts_init._task_ds = dict()
    test_module_ans

# Generated at 2022-06-13 07:04:20.143684
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    actual = ModuleArgsParser()
    task_ds = {'action': 'shell', 'delegate_to': 'localhost', 'args': {'chdir': '/tmp'}}
    actual_1 = actual.parse(task_ds)
    assert_equal(actual_1, ('shell', {'_raw_params': '', '_uses_shell': True, 'chdir': '/tmp'}, 'localhost'))

# Generated at 2022-06-13 07:04:28.773049
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    x = {}
    x.update({"a":"b"})
    assert(x=={"a":"b"})

    #test 0
    x = {}
    x.update({"a":"b"})
    assert(x=={"a":"b"})


    #test 1
    y = {}
    x = {}
    x == y
    x.update({"a":None})
    y.update({"a":None})
    assert(x==y)

    #test 2
    x = {}
    try:
        x.update({"a":"b", "c":{"d":"e"}})
        assert(False)
    except:
        assert(True)
        pass

    #test 3

# Generated at 2022-06-13 07:04:46.015485
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_task_ds = {'action': 'copy src=a dest=b', 'args': {'b': 2}}
    parser = ModuleArgsParser(task_ds=test_task_ds)
    result = parser._normalize_old_style_args(test_task_ds['action'])
    print (result)
    # Expected result: ('copy', {'src': 'a', 'dest': 'b'})
    result = parser._normalize_new_style_args(test_task_ds['action'], 'copy')
    print (result)
    # Expected result: {'src': 'a', 'dest': 'b'}
    result = parser._normalize_parameters(test_task_ds['action'], 'copy', test_task_ds['args'])
    print (result)
    # Expected

# Generated at 2022-06-13 07:04:49.858261
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for `ModuleArgsParser.parse`
    '''
    task_ds = {'action': {'module': 'copy src=a dest=b'}}
    map_obj = ModuleArgsParser(task_ds)
    out = map_obj.parse()
    assert (out[0], out[1], out[2]) == ('copy', {'src': 'a', 'dest': 'b'}, Sentinel)


# Generated at 2022-06-13 07:05:00.434418
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_str = '''
    - name: Standard form
      copy: src=a dest=b
    '''
    test_dict = yaml.load(test_str)
    assert ModuleArgsParser(task_ds=test_dict[0]).parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)

    test_str = '''
    - name: Complex args, copy module
      copy:
        src: a
        dest: b
    '''
    test_dict = yaml.load(test_str)
    assert ModuleArgsParser(task_ds=test_dict[0]).parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)


# Generated at 2022-06-13 07:05:14.222529
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:05:25.262974
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    # Case 1 or 2:
    # Cases where action is specified in task
    # Case 1:
    #    - run_once:
    #    - action: ping
    # Case 2:
    #    - action: ping
    task_result = Task.load(dict(action='ping'), variable_manager=variable_manager, loader=DataLoader())
    assert task_result.action == 'ping'
    assert task_

# Generated at 2022-06-13 07:05:35.391244
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:05:49.545398
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    yaml_text = """
    - name: Create a snapshot of the host's filesystems
      action: command
      args:
        _raw_params: "{{ _filesystems_snapshot_cmd }}"
        creates: "{{ _filesystems_snapshot_file }}"

    - name: Create a snapshot of the host's mysql databases
      action: command
      args:
        _raw_params: "{{ _mysql_snapshot_cmd }}"
        creates: "{{ _mysql_snapshot_file }}"
    """
    task_ds_list = yaml.safe_load(yaml_text)
    for task_ds in task_ds_list:
        p = ModuleArgsParser(task_ds)
        # args_data = p.parse()
        p.parse()

# Generated at 2022-06-13 07:05:55.188083
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'echo hi', 'module': 'copy', 'delegate_to': 'abc'}
    class_obj = ModuleArgsParser(task_ds)
    expected_result = ('copy', {'_raw_params': 'echo hi'}, 'abc')
    assert class_obj.parse() == expected_result


# Generated at 2022-06-13 07:05:56.099064
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # TODO: Implement unit test
    pass

# Generated at 2022-06-13 07:06:07.425377
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:06:27.075367
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'debug': {
            'msg': 'Hi, there!'
        }
    }
    collection_list = [
        {
            '_load_name': 'debug',
            'action_plugin': 'debug',
            'action_loader': 'debug',
            'class_name': 'Debugg'
        }
    ]
    map_obj = ModuleArgsParser(task_ds, collection_list)
    action_name, args, delegate_to = map_obj.parse()
    assert (action_name == 'debug')
    assert (args == {'msg': 'Hi, there!'})
    assert (delegate_to == None)