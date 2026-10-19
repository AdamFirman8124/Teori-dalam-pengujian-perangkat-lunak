

# Generated at 2022-06-13 06:56:53.287936
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse
    '''
    task_ds = {'shell': 'echo hi'}
    module_args_parser = ModuleArgsParser(task_ds)
    actual_result = module_args_parser.parse()
    assert actual_result == (u'shell', {'_raw_params': u'echo hi'}, None)

    task_ds = {'action': 'echo hi', 'delegate_to': 'localhost'}
    module_args_parser = ModuleArgsParser(task_ds)
    actual_result = module_args_parser.parse()
    assert actual_result == (u'echo', {'_raw_params': u'hi'}, u'localhost')

    task_ds = {'local_action': 'echo hi'}

# Generated at 2022-06-13 06:56:58.585797
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # This test case call the parse method and validate the response got in return
    #
    # Args:
    #    None
    #
    # Returns:
    #     None
    #
    # Raises:
    #     None
    module_args = dict(action=dict(module='copy', src='a', dest='b'))
    obj = ModuleArgsParser(task_ds=module_args)
    assert ('copy', dict(_raw_params='src=a dest=b'), None) == obj.parse()
    module_args = dict(action='copy src=a dest=b')
    obj = ModuleArgsParser(task_ds=module_args)
    assert ('copy', dict(_raw_params='src=a dest=b'), None) == obj.parse()
    module_args = dict(action='shell echo hi')


# Generated at 2022-06-13 06:56:59.639676
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    raise NotImplementedError("Test is not implemented")

# Generated at 2022-06-13 06:57:10.258312
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds=dict(action='echo', args=dict(var1='abc', var2='xyz'))
    collection_list=ansible.plugins.loader.collection_loader.all(class_only=True)
    obj=ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    action, args, delegate_to = obj.parse()

# Generated at 2022-06-13 06:57:20.302587
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook import Playbook
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    # These tests cover the original 3 supported forms
    # - action: copy src=a dest=b
    # - action: shell echo hi
    # - action: { module: copy, src: a, dest: b }

    # Missing module/action line is an error
    task = dict()
    try:
        parser = ModuleArgsParser(task)
        parser.parse()
        assert False
    except AnsibleParserError:
        assert True

    #

# Generated at 2022-06-13 06:57:31.681085
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Unit: ModuleArgsParser: parse
    parser = ModuleArgsParser()
    # AssertionError: the type of 'task_ds' should be a dict, but is a <class 'str'>
    # TypeError: 'NoneType' object is not subscriptable
    # AttributeError: 'NoneType' object has no attribute 'get'
    # TypeError: 'NoneType' object is not iterable
    # AttributeError: 'NoneType' object has no attribute 'copy'
    # TypeError: 'NoneType' object is not subscriptable
    # Exception: expected string or buffer
    # Exception: expected string or buffer
    # TypeError: argument of type 'NoneType' is not iterable
    # AttributeError: 'NoneType' object has no attribute 'get'
    # TypeError: 'NoneType' object is not subscriptable
    # Exception

# Generated at 2022-06-13 06:57:40.216958
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar

    loader = DictDataLoader({})
    play_context = PlayContext()

    parser = ModuleArgsParser()
    parser.parse(action='copy src=a dest=b', skip_action_validation=True)
    assert parser.resolved_action == 'copy'
    assert parser.parse(action='copy src=a dest=b', skip_action_validation=True) == ('copy', {'src': 'a', 'dest': 'b'}, Sentinel)

# Generated at 2022-06-13 06:57:54.063268
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # store the valid Task/Handler attrs for quick access
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    task_attrs.update(['local_action', 'static'])
    task_attrs = frozenset(task_attrs)

    # test invalid task ds
    # extra_args is not str or dict, raise exception
    invalid_task_ds = ['action', 'echo hi']
    invalid_parser = ModuleArgsParser(invalid_task_ds)
    with pytest.raises(AnsibleAssertionError):
        invalid_parser.parse()

    # test parser
    # task d

# Generated at 2022-06-13 06:58:02.977552
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_parser = ModuleArgsParser(None, None)
    _t = {
        'action': {'module': 'copy', 'src': 'a', 'dest': 'b'},
        'want': {'action': 'copy', 'args': {'src': 'a', 'dest': 'b'}}
    }
    _got = TaskDict(args_parser.parse(thing=_t['action'], action=None, additional_args=None))
    try:
        assert _t['want']['action'] == _got.action
        for key, value in _t['want']['args'].items():
            assert value == _got.args[key]
    except AssertionError:
        print_fail('test_ModuleArgsParser_parse', _t, _got)
        

# Generated at 2022-06-13 06:58:05.991581
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser(task_ds={'action': 'copy'})
    result = module_args_parser.parse()
    assert result == ('copy', {}, None)
    assert module_args_parser.resolved_action is None



# Generated at 2022-06-13 06:58:20.940888
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert False # TODO: implement your test here


# Generated at 2022-06-13 06:58:24.064038
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'command ls'}
    collection_list = list()
    parser = ModuleArgsParser(task_ds, collection_list)
    assert parser.parse() == ('command', {}, None)
# vim: set et ts=4 sw=4:

# Generated at 2022-06-13 06:58:31.162748
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common._collections_compat import Mapping
    import ansible.module_utils.common.unsafe_proxy as a_0_ansible_module_utils_common_unsafe_proxy
    import ansible.module_utils.six as a_0_ansible_module_utils_six
    import ansible.module_utils.six.moves._thread as a_0_ansible_module_utils_six_moves__thread
    import ansible.module_utils.six.moves.builtins as a_0_ansible_module_utils_six_moves_builtins
    import ansible.module_utils.six.moves.queue as a_0_ansible_module_utils_six_moves_queue
    import ansible.module_utils.six.moves.socketserver

# Generated at 2022-06-13 06:58:41.640592
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test case data
    task_ds = dict(action='shell',
                   echo='hi',
                   module='test module name',
                   x=3)

    # Perform the test
    obj = ModuleArgsParser(task_ds=task_ds)
    retval = obj.parse()
    assert retval[0] == 'test module name'
    assert retval[1]['x'] == 3
    assert retval[1]['_raw_params'] == 'echo=hi'
    assert retval[2] is None

    # Another test case
    task_ds = dict(action='shell',
                   echo='hi',
                   module='test module name')
    obj = ModuleArgsParser(task_ds=task_ds)
    retval = obj.parse()
    assert retval[0] == 'test module name'

# Generated at 2022-06-13 06:58:46.120270
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser(task_ds={
        'ignore_errors': True,
        'local_action': 'shell echo hi',
        'delegate_to': 'localhost'
    })
    action, args, delegate_to = module_args_parser.parse()

    assert action == "shell"
    assert args == {"_raw_params": "echo hi"}
    assert delegate_to == "localhost"


# Generated at 2022-06-13 06:59:00.361158
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class Fake_Context(object):
        def __init__(self):
            self.resolved = True

    class Fake_Loader(object):
        def find_plugin_with_context(self, item, collection_list=None):
            if not collection_list:
                raise AnsibleError("'collection_list' is required to load a module")
            return Fake_Context()

    tmp_module_loader = module_loader
    tmp_action_loader = action_loader
    module_loader = Fake_Loader()
    action_loader = Fake_Loader()


# Generated at 2022-06-13 06:59:09.527024
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    d = {u'handler': {u'name': u'start nginx'}, u'notify': [{u'name': u'start nginx'}, {u'name': u'stop nginx'}], u'name': u'start nginx'}
    t = {u'handler': {u'name': u'start nginx'}, u'notify': [{u'name': u'start nginx'}, {u'name': u'stop nginx'}], u'name': u'start nginx'}
    parser = ModuleArgsParser(d,None)
    parsed = parser.parse()   # u'handler': {u'name': u'start nginx'}, u'notify': [{u'name': u'start nginx'}, {u'name': u'stop nginx

# Generated at 2022-06-13 06:59:10.310323
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass



# Generated at 2022-06-13 06:59:15.796912
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(
        task_ds={
            'action': None,
            'local_action': None,
            'module': None,
            'delegate_to': None,
            'args': None,
        }
    )
    action, args, delegate_to = parser.parse()
    assert(not action)
    assert(not args)
    assert(not delegate_to)



# Generated at 2022-06-13 06:59:26.309019
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.module_utils.six as six
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils import basic

    class MockLoader():
        def find_plugin_with_context(self, name, collection_list=None):
            assert isinstance(name, str)
            context = AnsiblePluginLoadContext(name, aliases=[], collection_list=collection_list)
            context.resolved = True
            context.resolved_fqcn = 'ansible.plugins.shell.ActionModule'
            return context


# Generated at 2022-06-13 06:59:42.197095
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:59:53.703180
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''

    # The following is the task dictionary that would be used
    # by the ModuleArgsParser to pass to the parse method
    task_ds = {'shell': 'echo hii'}
    module_args_parser_obj = ModuleArgsParser(task_ds)
    module_args_parser_obj.parse()
    assert module_args_parser_obj.resolved_action == 'ansible.builtin.shell' 

    # The following is the task dictionary that would be used
    # by the ModuleArgsParser to pass to the parse method
    task_ds = {'action': 'echo hii'}
    module_args_parser_obj = ModuleArgsParser(task_ds)
    module_args_parser_obj.parse()
    assert module_args_parser

# Generated at 2022-06-13 07:00:00.644203
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_data = {}
    module_arg_data['action'] = 'test_module'
    module_arg_data['args'] = 'test_module_args'
    module_args_parser_obj = ModuleArgsParser(module_arg_data)
    expected_result = ('test_module', {'_raw_params': 'test_module_args'}, None)
    result = module_args_parser_obj.parse()
    assert result == expected_result

# Generated at 2022-06-13 07:00:09.442121
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Testing all paths through the function
    test1_task = {'action': 'copy src=a dest=b'}
    test1_parser = ModuleArgsParser(task_ds=test1_task)
    assert test1_parser.parse() == ('copy', {'dest': 'b', 'src': 'a'}, None)

    test2_task = {'local_action': 'copy src=a dest=b'}
    test2_parser = ModuleArgsParser(task_ds=test2_task)
    assert test2_parser.parse() == ('copy', {'dest': 'b', 'src': 'a'}, 'localhost')

    test3_task = {'module': 'copy src=a dest=b'}
    test3_parser = ModuleArgsParser(task_ds=test3_task)
    assert test3

# Generated at 2022-06-13 07:00:21.446831
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    loader.add_directory(VARIABLE_MANAGER, DATA_PATH)
    parser = ModuleArgsParser(DATA_PATH + '/ansible-command/task/tasks/test.yml', collection_list=['testns.z'])
    action, args, delegate_to = parser.parse()
    assert args == {'output': 'test', '_raw_params': 'python --version'}
    assert action == 'command'
    assert delegate_to is None

if __name__ == '__main__':
    from ansible import constants as C
    from ansible.context import CLIContext
    #from ansible.plugins.loader import action_loader
    from ansible.utils.vars import VariableManager
    C.DEFAULT_DEBUG=True

# Generated at 2022-06-13 07:00:28.774539
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'shell': 'foo', 'args': 'bar', 'delegate_to': 'localhost'}
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)
    ret = obj.parse()
    assert ret == ('shell', {'_raw_params': 'foo', '_variable_params': 'bar'}, 'localhost')

    task_ds = {'plays': ['foo'], 'delegate_to': 'localhost'}
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)
    try:
        raise Exception
    except Exception as e:
        with pytest.raises(AnsibleParserError) as excinfo:
            obj.parse()
        assert "no module/action detected in task." in str(excinfo.value)

   

# Generated at 2022-06-13 07:00:32.959503
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)
    obj.parse()

# Generated at 2022-06-13 07:00:40.632354
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    #
    #

    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    pass


# Generated at 2022-06-13 07:00:50.408318
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = dict()
    ds['action'] = 'copy src=a dest=b'
    ds['local_action'] = 'shell echo hi'
    ds['some_module'] = dict()
    ds['some_module']['xyz'] = 1
    ds['some_module']['xyz2'] = 2
    ds['delegate_to'] = 'some_machine'

# Generated at 2022-06-13 07:00:59.882301
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  # Test parsing of the action statement using predefined value for action, args and delegate_to
  task_ds = {'action': 'copy src=a dest=b'}
  expected_result = ('copy', {'src': 'a', 'dest': 'b'}, None)
  map = ModuleArgsParser(task_ds)
  assert map.parse() == expected_result

  # Test parsing of the local_action statement using predefined value for action, args and delegate_to
  task_ds = {'local_action': 'copy src=a dest=b'}
  expected_result = ('copy', {'src': 'a', 'dest': 'b'}, 'localhost')
  map = ModuleArgsParser(task_ds)
  assert map.parse() == expected_result

  # Test parsing of the module statement using predefined value for action, args

# Generated at 2022-06-13 07:01:14.398612
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:01:24.473923
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # This is a symlink => realpath
    test_task_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_action_plugin_module_args_parser.yml')

    with open(test_task_path, 'r') as fd:
        test_tasks = yaml.load(fd)

    task = test_tasks['tasks'][0]
    action = 'include_role'
    args = dict()
    args['name'] = 'foo'

    module_arg_parser = ModuleArgsParser(task, collection_list=[])
    module_name, module_args, delegate_to = module_arg_parser.parse()

    assert module_name == action
    assert module_args == args

# Generated at 2022-06-13 07:01:26.374491
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME: Test not written yet
    # FIXME: Test not written yet
    pass

# Generated at 2022-06-13 07:01:40.193764
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_parser = ModuleArgsParser()

    task_ds = {
        'action': {
            'module': 'copy',
            'src': 'a',
            'dest': 'b'
        },
        'with_tags': 'test',
        'args': 'test'
    }

    assert module_parser._normalize_old_style_args(task_ds['action']) == (None, {'module': 'copy', 'src': 'a', 'dest': 'b'})
    assert module_parser.parse() == (None, {'module': 'copy', 'src': 'a', 'dest': 'b'}, None)

    task_ds = {
        'action': "copy src=a dest=b",
        'delegate_to': 'localhost',
        'with_items': 'test'
    }

   

# Generated at 2022-06-13 07:01:46.136417
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import re


# Generated at 2022-06-13 07:01:50.818573
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = { 'test': { 'test1': 'test1', 'test2': 'test2' } }
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    module_args_parser.parse()
    assert True


# Generated at 2022-06-13 07:01:59.116289
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args = dict(
        action='shell echo hi',
        module='shell echo hi',
        args={'module': 'shell echo hi'},
        delegate_to=None
    )

    task_ds = dict(
        action='copy',
        args='copy'
    )

    parser = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = parser.parse()

    assert action == 'copy'
    assert args == dict()
    assert delegate_to == None

# Generated at 2022-06-13 07:02:06.052049
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:12.645198
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # Instantiating a ModuleArgsParser with bad task_ds should result in a AnsibleAssertionError
    for task_ds in [ None, True, 123, 1.2, [], () ]:
        try:
            module_args_parser = ModuleArgsParser(task_ds=task_ds)
            assert False
        except AnsibleAssertionError:
            pass

    # Instantiating a ModuleArgsParser with a valid task_ds should yield a ModuleArgsParser instance
    for task_ds in [ {}, {'action': ''} ]:
        module_args_parser = ModuleArgsParser(task_ds=task_ds)
        assert isinstance(module_args_parser, ModuleArgsParser)

    # Parsing ModuleArgsParser._task_ds containing action statement with invalid thing should result in a AnsibleParserError

# Generated at 2022-06-13 07:02:25.343491
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """ Unit test for method `parse` of class `ModuleArgsParser` """

    # test 'echo hi', 'shell'
    thing = 'echo hi'
    action = 'shell'
    mod_args_parser = ModuleArgsParser(task_ds=task_ds)
    actual_result = mod_args_parser._normalize_new_style_args(thing, action)
    expected_result = {'_raw_params': 'echo hi', '_uses_shell': True}
    assert actual_result == expected_result, \
        "actual_result=%s expected_result=%s"%(actual_result, expected_result)

    # test {'region': 'xyz'}, 'ec2'
    thing = {'region': 'xyz'}
    action = 'ec2'
    mod_args_parser = ModuleArgs

# Generated at 2022-06-13 07:02:36.246429
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(task_ds=None, collection_list=None)
    # test_parse_1
    task_1 = {}
    action_1 = None
    args_1 = {}
    delegate_to_1 = None
    assert (m.parse(skip_action_validation=False) == (action_1, args_1, delegate_to_1))
    # test_parse_2
    task_2 = {'action': {'module': 'shell', 'args': '/usr/bin/false'}}
    action_2 = 'shell'
    args_2 = {'args': '/usr/bin/false'}
    delegate_to_2 = None
    assert (m.parse(skip_action_validation=False) == (action_2, args_2, delegate_to_2))
    # test

# Generated at 2022-06-13 07:02:37.753673
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert False # TODO: implement your test here


# Generated at 2022-06-13 07:02:48.774950
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    module_data = dict(
        ping=None,
        copy=dict(
            src="foo/bar",
            content="HELLO!",
            dest="foo/bar.1"
        ),
        shell="echo '{{foo.bar}}'"
    )
    module_data_desc = {}
    for k, v in iteritems(module_data):
        if isinstance(v, dict):
            v = dict((k1, AnsibleUnicode(v1)) for k1, v1 in iteritems(v))
        elif isinstance(v, string_types):
            v = AnsibleUnicode(v)
        module_data_desc[k] = v
    data = dict(action=module_data_desc)
   

# Generated at 2022-06-13 07:02:49.471947
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass



# Generated at 2022-06-13 07:02:59.101145
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test 1
    task_ds = {'action': 'shell echo hi'}
    parser = ModuleArgsParser(task_ds=task_ds)
    actual = parser.parse()
    expected = ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, None)
    assert expected == actual

    # test 2
    task_ds = {'action': ('shell echo hi', 'shell echo hello')}
    parser = ModuleArgsParser(task_ds=task_ds)
    actual = parser.parse()
    expected = ('shell', {'_raw_params': ('echo hi', 'echo hello'), '_uses_shell': True}, None)
    assert expected == actual

    # test 3
    task_ds = {'action': {'module': 'shell echo hi'}}

# Generated at 2022-06-13 07:03:09.661515
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task

    class TaskSub(Task):
        pass

    ############################################################################
    # tests for ModuleArgsParser._split_module_string
    ############################################################################

    # Case 1: Special case: If the module_string is '', returns the module_string
    assert ModuleArgsParser(TaskSub())._split_module_string('') == ('','')

    # Case 2: Otherwise, it splits the module_string as per 'split_args'
    assert ModuleArgsParser(TaskSub())._split_module_string('module_name arg1=val1 arg2=val2') == ('module_name', 'arg1=val1 arg2=val2')


    ############################################################################
    # tests for ModuleArgsParser._normalize_parameters
    ############################################################################

   

# Generated at 2022-06-13 07:03:18.840404
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_parser = ModuleArgsParser(task_ds={})
    action, args, delegate_to = args_parser.parse(skip_action_validation=False)
    assert action == None
    assert args == {}
    assert delegate_to == {}

    args_parser = ModuleArgsParser(task_ds={'action': {'module': 'ec2'}})
    action, args, delegate_to = args_parser.parse(skip_action_validation=False)
    assert action == 'ec2'
    assert args == {}
    assert delegate_to == {}

    args_parser = ModuleArgsParser(task_ds={'action': {'module': 'ec2', 'x': 1}})
    action, args, delegate_to = args_parser.parse(skip_action_validation=False)
    assert action == 'ec2'

# Generated at 2022-06-13 07:03:23.904005
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_task_ds = {
        'action': 'myaction',
        'with_items': 'arg1',
        'with_file': 'file.txt',
        'with_fileglob': 'file*.txt',
        'with_items': ['arg1', 'arg2'],
        'with_subelements': ['arg1', 'arg2'],
        'args': {'arg1': 'val1', 'arg2': 'val2'},
        'register': 'result'
    }

    my_module_args_parser = ModuleArgsParser(test_task_ds)
    action, args, delegate_to = my_module_args_parser.parse()

    assert 'arg1' in args
    assert 'arg2' in args


# Generated at 2022-06-13 07:03:38.543957
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test for method parse of class ModuleArgsParser
    """

    # test 1: no module name
    test_dict = {'delegate_to': 'test_host'}
    test_args = ModuleArgsParser(test_dict).parse()
    assert test_args == (None, {}, 'test_host'), test_args

    # test 2: action form
    test_dict = {'action': 'shell echo hi', 'delegate_to': 'test_host'}
    test_args = ModuleArgsParser(test_dict).parse()
    assert test_args == ('shell', {'_raw_params': 'echo hi'}, 'test_host'), test_args

    # test 3: dict form

# Generated at 2022-06-13 07:03:44.240475
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        "action": {
            "module": "shell",
            "args": {
                "chdir": "/tmp",
                "creates": "foo",
                "executable": None,
                "removes": "bar"
            }
        },
        "register": "shell_out"
    }

    parser = ModuleArgsParser(task_ds)
    result = parser.parse()
    assert result[0] == 'shell'
    assert result[1] == {'chdir': '/tmp', 'creates': 'foo', 'executable': None, 'removes': 'bar'}
    assert result[2] is None

# Test case for module_require_argspec function

# Generated at 2022-06-13 07:04:02.258085
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def my_check_name(name):
        import re
        name_re = re.compile("^[_a-zA-Z][_a-zA-Z0-9]*$")
        if not name_re.match(name):
            raise NameError("Invalid name: '%s'" % name)
        return True

    def my_is_template(data):
        import re
        if not isinstance(data, string_types):
            return False
        if data.find("{{") != -1 or data.find("{%") != -1:
            return True
        else:
            return False

    class my_Context(object):
        def __init__(self, resolved, resolved_fqcn, redirect_list):
            self.resolved = resolved
            self.resolved_fqcn = resolved

# Generated at 2022-06-13 07:04:05.969255
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  '''
  Test for method parse of class ModuleArgsParser
  '''
  test_obj = {}
  step = ModuleArgsParser(task_ds = test_obj)
  step.parse()
  return

# Generated at 2022-06-13 07:04:10.372845
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell echo hi', 'args': None, 'delegate_to': 'localhost'}
    collection_list = None
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    expected = ('shell', {'_uses_shell': True, '_raw_params': 'echo hi'}, 'localhost')
    actual = obj.parse()
    assert expected == actual


# Generated at 2022-06-13 07:04:23.970567
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    loader = DictDataLoader({})
    task_ds = { "action": "shell", "args": {"_raw_params": "true"} }
    collection_list = ["/home/peng/.ansible/collections/ansible_collections/test/t_action"]
    
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    
    assert module_args_parser is not None
    assert module_args_parser._task_ds == task_ds
    assert module_args_parser._collection_list == collection_list

# Generated at 2022-06-13 07:04:28.269777
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    src_dict = {"action": "command", "args": "echo Hi there", "delegate_to": "localhost"}
    parser = ModuleArgsParser(task_ds=src_dict)
    assert parser.parse() == ('command', {'_raw_params': 'echo Hi there'}, 'localhost')

# Generated at 2022-06-13 07:04:34.621406
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Bunch of tests that all do the same thing,
    # just in different syntax
    tests = []
    tests.append(
        dict(
            module_name='command',
            action={'module': 'command', 'args': 'foo=1'},
            delegate_to='bar',
            args={'foo': '1'},
            task_args={}
        )
    )
    tests.append(
        dict(
            module_name='command',
            action={'module': 'command', 'args': {'foo': 1}},
            delegate_to='bar',
            args={'foo': 1},
            task_args={}
        )
    )

# Generated at 2022-06-13 07:04:38.803708
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser(task_ds=None, collection_list=None)
    with pytest.raises(AnsibleAssertionError):
        module_args_parser.parse()
        pytest.fail("AnsibleAssertionError not raised")


# Generated at 2022-06-13 07:04:45.602957
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ts = Task()
    ts._task.name = "check_me"
    ts._parent = Play().load({'hosts': 'localhost'}, variable_manager=VariableManager())

    map = ModuleArgsParser(task_ds={'module': 'shell', 'args': 'echo hello'})
    m1 = map.parse()
    assert m1 == ['shell', {'args': 'echo hello'}, Sentinel]

    map = ModuleArgsParser(task_ds={'action': 'shell echo hello'})
    m2 = map.parse()
    assert m2 == ['shell', {'args': 'echo hello'}, Sentinel]


# Generated at 2022-06-13 07:04:46.598283
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert False  # TODO: implement your test here


# Generated at 2022-06-13 07:04:51.085645
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest
    from ansible.executor.module_loader import module_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.basic import AnsibleModule
    import ansible.constants as C
    from ansible.errors import AnsibleParserError
    from ansible.errors import AnsibleError
    import ansible.utils.encrypt


# Generated at 2022-06-13 07:05:03.367835
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds=dict()
    collection_list=None
    obj= ModuleArgsParser(task_ds,collection_list)
    with pytest.raises(AnsibleParserError):
        obj.parse()

# Generated at 2022-06-13 07:05:11.719678
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    thing = dict()
    test_inst = ModuleArgsParser(thing)
    assert test_inst.parse() == (None, dict(), Sentinel)

    thing = dict(
        action=dict(module="foo", bar="baz"),
        delegate_to="localhost",
        module="foo",
        bar="baz",
        with_foo=["abc", "def"])
    test_inst = ModuleArgsParser(thing)
    assert test_inst.parse() == ('foo', dict(bar="baz"), 'localhost')


# Generated at 2022-06-13 07:05:23.439249
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # store the valid Task/Handler attrs for quick access
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    task_attrs.update(['local_action', 'static'])
    task_attrs = frozenset(task_attrs)

    # HACK: why are these not FieldAttributes on task with a post-validate to check usage?
    
    # final args are the ones we'll eventually return, so first update
    # them with any additional args specified, which have lower priority
    # than those which may be parsed/normalized next
    
    
    # Test cases
    
    #case1
    task_

# Generated at 2022-06-13 07:05:31.892410
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert isinstance(ModuleArgsParser(None).parse(), tuple), "Method parse should return a tuple"

    # test is OK
    assert ModuleArgsParser({
        'module': 'copy',
        'args': {
            'src': '/path/to/src'
        }
    }).parse() == ('copy', {'src': '/path/to/src'}, Sentinel)

    # test is OK
    assert ModuleArgsParser({
        'action': 'copy src=/path/to/src'
    }).parse() == ('copy', {'src': '/path/to/src'}, Sentinel)

    # test is OK
    assert ModuleArgsParser({
        'local_action': 'copy src=/path/to/src'
    }).parse() == ('copy', {'src': '/path/to/src'}, 'localhost')

    #

# Generated at 2022-06-13 07:05:38.294133
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.template import Templar
    from ansible.plugins.action.command import ActionModule as command_ActionModule
    from ansible.plugins.action.shell import ActionModule as shell_ActionModule
    from ansible.plugins.action.raw import ActionModule as raw_ActionModule
    from ansible.plugins.action.debug import ActionModule as debug_ActionModule
    import os
    import sys
    import pytest

    if sys.version_info[0] == 2:
        assert_regex = assertRegexpMatches
    else:
        assert_regex = assertRegex

    # additional args as kwargs
    additional_args_kwargs = dict(run_once=True)

# Generated at 2022-06-13 07:05:41.887235
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'module': 'a'}
    m = ModuleArgsParser(task_ds)
    res = m.parse()
    print(res)


# Generated at 2022-06-13 07:05:54.138737
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # test the parse on a string action and module
    # also test that with_* parameters are ignored
    raw = '''
    - name: test action with with_* gets parsed as module
      action: echo "testing 123"
      with_items:
        - item1
        - item2
      with_dict:
        key1: item1
        key2: item2
    '''
    module_args_parser = ModuleArgsParser(yaml.safe_load(raw))
    (action, args, delegate_to) = module_args_parser.parse()
    assert action == 'echo'
    assert args['_raw_params'] == '"testing 123"'
    assert delegate_to is Sentinel

    # test parsing an action and module, with complex args

# Generated at 2022-06-13 07:05:56.979891
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)
    ret = obj.parse()
    assert ret == (None, dict(), Sentinel)


# Generated at 2022-06-13 07:06:05.927977
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:06:13.877885
# Unit test for method parse of class ModuleArgsParser