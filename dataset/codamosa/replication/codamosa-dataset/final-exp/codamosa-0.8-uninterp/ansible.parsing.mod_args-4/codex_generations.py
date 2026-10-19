

# Generated at 2022-06-13 06:56:42.311051
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(action='copy')

    parser = ModuleArgsParser(task_ds=task_ds)
    parser.parse()

# Generated at 2022-06-13 06:56:44.177381
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# Generated at 2022-06-13 06:56:52.391000
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:56:58.425117
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar
    action_loader.add_directory(os.path.join(TEST_DIR, 'action_plugins'))
    module_loader.add_directory(os.path.join(TEST_DIR, 'modules'))
    # the key test cases are in the tests/test_validate_modules.py
    # and tests/test_validate_playbook.py.  This was put together
    # as we found cases which were not tested.
    arg_parser = ModuleArgsParser(collection_list=[b_collection])
    result = arg_parser.parse(skip_action_validation=False)
    #assert isinstance(result, tuple)
    #assert len(result) == 3
   

# Generated at 2022-06-13 06:57:09.444946
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test 6: test with "action: { module: 'copy', src: 'a', dest: 'b' }"
    module_args_parser = ModuleArgsParser(task_ds={'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}})
    assert module_args_parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)
    # test 11: test with 'action: { module: "copy", args: "src=a dest=b" }'
    module_args_parser = ModuleArgsParser(task_ds={'action': {'module': 'copy', 'args': 'src=a dest=b'}})
    assert module_args_parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)


# Generated at 2022-06-13 06:57:18.147787
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    unit test for method parse of class ModuleArgsParser
    '''
    import os
    import sys
    module_location = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(module_location)
    module_location_parent = os.path.dirname(module_location)
    sys.path.append(module_location_parent)
    from ansibleparser.parser.task_parser import TaskParser
    from ansible.plugins import module_loader
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host

    loader = DataLoader()
    results_

# Generated at 2022-06-13 06:57:21.965871
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Test for the method ModuleArgsParser.parse
    """

    # test call of method parse
    # test return value of method parse is valid
    # test exception raised by method parse
    pass


# Generated at 2022-06-13 06:57:30.990382
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds=tasks[0], collection_list=[])
    assert parser.parse() == ('ping', {}, 'localhost')

    parser = ModuleArgsParser(task_ds=tasks[1], collection_list=[])
    assert parser.parse() == ('ping', {}, None)

    parser = ModuleArgsParser(task_ds=tasks[2], collection_list=[])
    assert parser.parse() == ('ping', {"data": "icmp_seq=0 ttl=128 time=0.817 ms", "ping_args": "-c4 -W1"}, "localhost")


# Generated at 2022-06-13 06:57:43.101623
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:51.553780
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    
    # Create a new instance of ModuleArgsParser
    module_args_parser = ModuleArgsParser()

    # The following test cases verify that the method parse works properly
    # when passed different values for the argument skip_action_validation

    # Test Case 1: skip_action_validation = False
    action, args, delegate_to = module_args_parser.parse(skip_action_validation = False)
    assert action == None
    assert args == {}
    assert delegate_to is None

    # Test Case 2: skip_action_validation = True
    action, args, delegate_to = module_args_parser.parse(skip_action_validation = True)
    assert action == None
    assert args == {}
    assert delegate_to is None

# Generated at 2022-06-13 06:58:13.690788
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == (None, {}, None)

    task_ds = { 'action': 'hello' }
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == ('hello', {}, None)

    task_ds = { 'action': { 'shell': 'echo hello'} }
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == ('echo hello', {}, None)

    task_ds = { 'action': { 'shell': 'echo hello'}, 'delegate_to': 'me'}
    parser = ModuleArgsParser(task_ds)
    assert parser.parse() == ('echo hello', {}, 'me')


# Generated at 2022-06-13 06:58:18.729341
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_ds = dict(
        _variable_params='_raw_params',
        _task_fields=dict(
            action=dict(
                module=dict(
                    _raw_params='module value',
                    _uses_shell=True
                ),
                args=dict(
                    _raw_params='args value'
                )
            ),
            delegate_to='localhost'
        ),
        _task_ds=dict(
            args=dict(
                _raw_params='args value'
            ),
            action='module: _raw_params=module value'
        ),
        _task_attrs=frozenset(['local_action', 'module', 'delegate_to', 'action', 'args']),
        _task_ds_name='task name',
        _collection_list=dict()
    )

   

# Generated at 2022-06-13 06:58:26.466465
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    moduleargs = dict(
            action="ping",
            module="ping",
            args=dict(data="pong"),
            delegate_to="shuimutong.com",
            local_action="local"
        )
    parser = ModuleArgsParser(task_ds=moduleargs)
    action, args, delegate_to = parser.parse()
    print(action, args, delegate_to)

    moduleargs = dict(
            action="ping",
            module="ping",
            args=dict(data="pong")
        )
    parser = ModuleArgsParse

# Generated at 2022-06-13 06:58:32.739225
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  parser = ModuleArgsParser()
  #with pytest.raises(AnsibleAssertionError):
  #  parser.parse(1)
  assert parser.parse(task_ds={}) == ("", {}, None)
  assert parser.parse(task_ds={"action": "ping"}) == ("ping", {}, None)
  # Test 'action: ping'
  assert parser.parse(task_ds={"action": "ping"}, skip_action_validation=True) == ("ping", {}, None)
  # Test 'action: "echo 'hi'"'
  assert parser.parse(task_ds={"action": '"echo \'hi\'"'}) == ("", {"_variable_params": '"echo \'hi\'"'}, None)
  # Test 'action: "echo ''hi''"'

# Generated at 2022-06-13 06:58:36.521885
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({'action': 'copy src=a dest=b'})
    assert parser.parse() == ('copy', {'dest': 'b', 'src': 'a'}, None)



# Generated at 2022-06-13 06:58:41.858476
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(_raw_params='')
    collection_list = list()
    obj = ModuleArgsParser(task_ds, collection_list)
    skip_action_validation = False
    action, args, delegate_to = obj.parse(skip_action_validation)
    assert action == None
    assert not args
    assert delegate_to == Sentinel


# Generated at 2022-06-13 06:58:46.029638
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = dict(
        action = 'copy',
        delegate_to = 'localhost',
        args = {'src': '/source/path', 'dest': '/dest/path'}
    )
    obj = ModuleArgsParser(task_ds=args)
    result = obj.parse()
    assert result == ('copy', {'dest': '/dest/path', 'src': '/source/path'}, 'localhost')


# Generated at 2022-06-13 06:59:00.296946
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:59:08.266421
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import os
    import yaml

    source_path = os.path.join(os.path.dirname(__file__), 'test_data', 'module_args_parser_parse.yaml')
    with open(source_path) as f:
        test_data = yaml.load(f, Loader=yaml.FullLoader)
        for data in test_data:
            print(data)
            parser = ModuleArgsParser(data['input'])
            assert parser.parse() == (data['expected']['action'],
                                      data['expected']['args'],
                                      data['expected'].get('delegate_to', None))

# Generated at 2022-06-13 06:59:17.630762
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import unittest

# Generated at 2022-06-13 06:59:30.305923
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Init objects used in this test
    p = None #type: ModuleArgsParser
    action = ''
    args = ''
    delegate_to = ''

    # Init expected values
    expected_action = ''
    expected_args = ''
    expected_delegate_to = ''

    # Run test
    p = ModuleArgsParser(task_ds={'delegate_to': 'localhost',
                                  'action': 'echo hi'})
    (action, args, delegate_to) = p.parse()

    # Check expected vs actual results
    print('Test passed')
    assert action == expected_action
    assert args == expected_args
    assert delegate_to == expected_delegate_to

test_ModuleArgsParser_parse()

# Generated at 2022-06-13 06:59:40.981128
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_text

    ######################################
    # test for method parse for class ModuleArgsParser
    ######################################

    # test_without_action
    task = {'other': 'a'}
    parser = ModuleArgsParser(task, None)
    assert parser.parse() == (None, None, None)

    # test_normal_action
    task = {'action': 'localhost'}
    parser = ModuleArgsParser(task, None)
    assert parser.parse() == ('localhost', {}, 'localhost')

    # test_local_action_override_action
    task = {'action': 'localhost', 'local_action': 'localhost'}
    parser = ModuleArgsParser(task, None)
    assert parser.parse() == ('localhost', {}, 'localhost')

    # test_

# Generated at 2022-06-13 06:59:45.856101
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with pytest.raises(AnsibleError) as excinfo:
        ModuleArgsParser._normalize_new_style_args('test','shell')
        assert "unexpected parameter type in action: %s" % 'test' in str(excinfo.value)


# Generated at 2022-06-13 06:59:56.440929
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    # 1. test with 'action'
    task_ds = dict(action={'module': 'copy', 'file': 'src', 'dest': 'dst'})
    host = Host(name='t')
    hosts = [host]
    play_context = dict(remote_addr="100.100.100.100")
    task = Task.load(task_ds, loader=loader, variable_manager=variable_manager, play_context=play_context)


# Generated at 2022-06-13 07:00:07.120381
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_action = 'copy'
    test_args = {'src': 'a', 'dest': 'b'}
    test_ds = {'action': test_action, 'args': test_args}
    test = ModuleArgsParser(test_ds).parse()
    assert test[0] == test_action
    assert test[1] == test_args


TASK_ATTRIBUTES = frozenset(['name', 'tags', 'when', 'async_val', 'poll', 'register', 'ignore_errors', 'delegate_to'])

# FIXME: Deprecate this in favour of action_loader.is_valid_action

# Generated at 2022-06-13 07:00:20.621966
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    # Build a dict containing a task
    # action: 'shell echo hi'
    # local_action: 'copy src=a dest=b'
    # module: 'copy', src: 'a', dest: 'b'
    task_ds = {}
    task_ds[u'action'] = u'shell echo hi'
    task_ds[u'local_action'] = u'copy src=a dest=b'
    task_ds[u'module'] = {'module': u'copy', u'src': 'a', u'dest': 'b'}
    module_args_parser = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 07:00:28.566639
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test with None as arg
    expect = (None, dict(), Sentinel)
    actual = ModuleArgsParser(None).parse()
    assert actual == expect, "Unexpected module args parse result from None: expected: {0}, actual: {1}".format(expect, actual)

    # Test with wacky input
    expect = (None, dict(), Sentinel)
    actual = ModuleArgsParser(thing=dict()).parse()
    assert actual == expect, "Unexpected module args parse result from None: expected: {0}, actual: {1}".format(expect, actual)

    # Test with shell module 'single-line' args
    expect = (
        'shell', dict(_raw_params='echo "hello world"'), Sentinel
    )
    actual = ModuleArgsParser({'action': 'shell echo "hello world"'}).parse()
    assert actual

# Generated at 2022-06-13 07:00:40.333413
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import tempfile
    import shutil
    test_dir = tempfile.mkdtemp()
    (flexmock(os.path)
        .should_receive('expanduser')
        .and_return(test_dir))
    config = mock_config()

    collection_dir = os.path.join(test_dir, 'empty_collection')
    os.makedirs(collection_dir)
    (flexmock(CollectionLoader)
        .should_receive('list_directory')
        .with_args(collection_dir)
        .and_return([]))
    collection_list = CollectionList([collection_dir])

    # task_ds = {}
    task_ds = {}
    assert ModuleArgsParser(task_ds, collection_list).parse() == (None, {}, None)
    # task_ds =

# Generated at 2022-06-13 07:00:46.756597
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    Task = MagicMock()
    Task.task = Task
    Action = MagicMock()
    Action.action = Action
    Handler = MagicMock()
    Handler.handler = Handler
    loader = MagicMock()
    task_ds = {}
    delegate_to = 'localhost'
    
    # Thing is None
    args = {}
    non_task_ds = {}
    action = 'action'
    thing = None
    args['additional_args'] = ''
    args['args'] = ''
    args['thing'] = thing
    args['action'] = action
    args['delegate_to'] = delegate_to
    args['non_task_ds'] =  non_task_ds
    args['modules'] = Action
    

# Generated at 2022-06-13 07:00:57.163848
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mock_action_loader_find_plugin_with_context = MagicMock()
    mock_module_loader_find_plugin_with_context = MagicMock()
    with patch.multiple(action_loader, find_plugin_with_context=mock_action_loader_find_plugin_with_context,
                                                             resolved_fqcn='mock_resolved_fqcn'):
        with patch.multiple(module_loader, find_plugin_with_context=mock_module_loader_find_plugin_with_context):
            # Testing 'action: command'
            mock_action_loader_find_plugin_with_context.return_value.resolved = True
            mock_action_loader_find_plugin_with_context.return_value.redirect_list = []
            mock_module_loader_find_plugin

# Generated at 2022-06-13 07:01:11.889168
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def test_action(data_in, data_out):
        parser = ModuleArgsParser(data_in)
        args, kwargs = parser.parse()
        assert data_out == (args, kwargs)


# Generated at 2022-06-13 07:01:19.019010
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  import pytest
  import sys
  import json


  with pytest.raises(AnsibleParserError) as excinfo:
    ModuleArgsParser(task_ds=None, collection_list=None).parse(skip_action_validation=False)
  assert 'the type of \'task_ds\' should be a dict, but is a <class \'NoneType\'>' in str(excinfo.value)

  # Invalid isinstance of 'thing'
  with pytest.raises(AnsibleParserError) as excinfo:
    ModuleArgsParser(task_ds={}, collection_list=None).parse(skip_action_validation=False)
  assert 'unexpected parameter type in action: <class \'dict\'>' in str(excinfo.value)

  # Invalid 'action'

# Generated at 2022-06-13 07:01:25.800430
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'action': 'ping',
        'name': 'test',
        'register': 'test_result'
    }
    collection_list = None
    
    my_parser = ModuleArgsParser(task_ds, collection_list)
    result = my_parser.parse()
    assert result == ('ping', {}, None), "Expected: ('ping', {}, None), but got: %s" % result
    print("\n>>>> test_ModuleArgsParser_parse() >>>> SUCCESS!")

if __name__ == "__main__":
    test_ModuleArgsParser_parse()

# Generated at 2022-06-13 07:01:31.608496
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    assert ModuleArgsParser({'action': 'shell echo hi'}).parse() == ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, None)
    assert ModuleArgsParser({'action': {'module': 'shell echo hi'}}).parse() == ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, None)
    assert ModuleArgsParser({'action': {'module': 'shell echo hi', 'foo': 'bar'}}).parse() == ('shell', {'foo': 'bar', '_raw_params': 'echo hi', '_uses_shell': True}, None)
    assert ModuleArgsParser({'local_action': 'shell echo hi'}).parse() == ('shell', {'_raw_params': 'echo hi', '_uses_shell': True}, 'localhost')


# Generated at 2022-06-13 07:01:37.184194
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    _task_ds = {
        'local_action': {'module': 'copy', 'src': 'a', 'dest': 'b'},
        'delegate_to': 'localhost'
    }
    parser = ModuleArgsParser(_task_ds=_task_ds)
    action, args, delegate_to = parser.parse()
    assert action == 'copy'
    assert isinstance(args, dict)
    assert 'src' in args
    assert 'dest' in args
    assert delegate_to == 'localhost'
# class for ActionBase

# Generated at 2022-06-13 07:01:39.979232
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  obj_task = dict(
    name='test',
    action='test',
    delegate_to=None
  )

  obj = ModuleArgsParser(obj_task)
  res = obj.parse()
  assert res == ('test', dict(), None)


# Class VarsModule

# Generated at 2022-06-13 07:01:45.987856
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  """
  Test for method parse()
  """
  # 0. Setup
  from ansible.playbook.play_context import PlayContext
  from ansible.playbook.task_include import TaskInclude
  from ansible.parsing.yaml.loader import AnsibleLoader
  play_ds = dict(
      hosts='all',
      gather_facts='no',
      roles=['role1', 'role2'],
  )
  play_ds = AnsibleLoader(play_ds).get_single_data()
  play_context = PlayContext(play_ds)
  play_context._task_include = TaskInclude.load(play_ds)
  play_context._task_include.set_play_context(play_context)


# Generated at 2022-06-13 07:01:54.461383
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    t = Template()
    task_ds = {'delegate_to': 'localhost',
               'action': 'copy',
               'args': 'src=/tmp/foo dest=/tmp/bar mode=0777'}
    c = ModuleArgsParser(task_ds=task_ds)
    (action, args, delegate_to) = c.parse()
    assert action == 'copy', "action must be 'copy'"
    assert delegate_to == 'localhost', "delegate_to must be 'localhost'"
    assert args.get('_raw_params') == 'src=/tmp/foo dest=/tmp/bar mode=0777', \
        "raw_params must be 'src=/tmp/foo dest=/tmp/bar mode=0777'"


# Generated at 2022-06-13 07:02:03.551551
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # module args dict
    args_dict = {}
    # module args string
    args_string = ''
    parser = ModuleArgsParser()
    # Test parse() method when action is defined
    args_dict['action'] = 'action'
    result = parser.parse(args_dict, skip_action_validation=False)
    assert result == {'action': 'action', 'args': {}, 'delegate_to': None}, "Unexpected parse result."
    # Test parse() method when local_action is defined
    args_dict['local_action'] = 'local_action'
    result = parser.parse(args_dict, skip_action_validation=False)
    assert result == {'action': 'local_action', 'args': {}, 'delegate_to': 'localhost'}, "Unexpected parse result."
    # Test parse()

# Generated at 2022-06-13 07:02:08.021051
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # The test cases are taken from ansible/test/units/playbook/test_parser.py
    # Test case 1:

    # task_ds is a dict contains the following keys
    task_ds = dict()
    # View into task_ds as a dict: {'action': {'module': 'copy', 'args': {'dest': 'a'}}
    task_ds['action'] = dict()
    task_ds['action']['module'] = 'copy'
    task_ds['action']['args'] = dict()
    task_ds['action']['args']['dest'] = 'a'
    # action: copy src=a dest=b
    # left-hand side is the key, right-hand side is the value
    # module is the key
    # copy is the value

    # collection_list is a

# Generated at 2022-06-13 07:02:27.738131
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:35.527969
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest

# Generated at 2022-06-13 07:02:41.053032
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:02:42.551990
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass  # TODO: implement test


# Generated at 2022-06-13 07:02:44.253498
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser()
    assert m.parse() == (None, None, None)

# Generated at 2022-06-13 07:02:46.710407
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # TODO: Add more tests
    pass


# Generated at 2022-06-13 07:02:57.196724
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:03:08.950794
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.utils.shlex
    from ansible.errors import AnsibleAssertionError, AnsibleParserError
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.utils.shlex import shlex_split
    from ansible.vars.unsafe_proxy import AnsibleVarsUnsafeText
    from ansible.utils.unicode import to_bytes
    # using _valid_attrs instead of the actual class ValidAttribute above because the attributes are used to
    #   determine the keys inside the action and are not action specific, I've used the Task class and the Handler class
    #   to get the keys that should be used to check if the keys are part of the

# Generated at 2022-06-13 07:03:18.489191
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.plugins.loader import collection_loader
    from ansible.plugins import module_loader
    from ansible.plugins.action.copy import ActionModule as CopyActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    manager = VariableManager()
    collection_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/collections/ansible_collections/test_collection/test_namespace'))
    module_loader._add_directory(os.path.join(os.path.dirname(__file__), '../../lib/ansible/modules/extras'))

# Generated at 2022-06-13 07:03:27.209971
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action_loader = ActionModuleLoader()
    module_loader = ModuleLoader()
    # test_data is a dictionary than contains test data used in the tests
    test_data = {}
    test_data['action_loader'] = action_loader
    test_data['module_loader'] = module_loader
    # test_cases is a list of lists than contains the test data itself
    # Each test consists of:
    #  - the input data
    #  - the expected output
    #  - the expected exception
    test_cases = [
        [
            {'action': 'test', 'args': {'a': 1}},
            ('test', {'a': 1}, None)
        ]
    ]


# Generated at 2022-06-13 07:03:34.298042
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass
#
#

# Generated at 2022-06-13 07:03:36.893744
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # No test, as the functionality is tested in test_normalize_task_and_variable_names
    assert True


# Generated at 2022-06-13 07:03:43.677557
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test that validates the above code is working correctly.
    my_task = {'action': 'shell echo hi', 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=my_task)
    action, args, delegate_to = parser.parse()
    assert action == 'shell'
    assert args == {'A': 'echo hi'}
    assert delegate_to == 'localhost'
    my_task = {'action': {'shell': 'ls'}, 'delegate_to': 'localhost'}
    parser = ModuleArgsParser(task_ds=my_task)
    action, args, delegate_to = parser.parse()

    assert action == 'shell'
    assert args == {'A': 'ls'}
    assert delegate_to == 'localhost'


# test that we handle complex args correctly

# Generated at 2022-06-13 07:03:49.759115
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for module_common.ModuleArgsParser.parse
    '''

    # test cases

# Generated at 2022-06-13 07:03:54.130454
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action = 'setup'
    delegate_to = 'localhost'

    expected = (action, dict(), delegate_to)

    actual = ModuleArgsParser({'local_action': action}).parse()

    assert actual == expected


# Generated at 2022-06-13 07:04:04.835196
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # Case-1: task in the form of action: { module: 'copy', src: 'a', dest: 'b' }
    task_ds = {
        'action': {
            'module': 'copy',
            'src': 'a',
            'dest': 'b'
        }
    }
    parser = ModuleArgsParser(task_ds=task_ds)
    (action, args, delegate_to) = parser.parse()
    assert action == 'copy'
    assert args == {'dest': 'b', 'src': 'a'}
    assert delegate_to == Sentinel

    # Case-2: task in the form of action: copy src=a dest=b
    task_ds = {
        'action': 'copy src=a dest=b'
    }

# Generated at 2022-06-13 07:04:12.236099
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'ignore_errors': True, 'args': {u'chdir': u'/tmp'}, 'when': u'False', u'command': u'pwd'}
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    assert module_args_parser.parse() == ('command', {u'chdir': u'/tmp', u'when': u'False'}, None)

    task_ds = {'action': "copy src=a dest=b"}
    module_args_parser = ModuleArgsParser(task_ds=task_ds)
    assert module_args_parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)

    task_ds = {'module': 'copy src=a dest=b'}
    module_args_parser = Module

# Generated at 2022-06-13 07:04:25.815603
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    task_ds = {
        "action": {
            "module": "copy",
            "src": "a",
            "dest": "b"
        }
    }
    parm = ModuleArgsParser(task_ds)
    result = parm.parse()
    assert result[0] == "copy"
    assert result[1] == {"src": "a", "dest": "b"}
    assert result[2] == None
    task_ds = {
        "delegate_to": "localhost",
        "local_action": {
            "module": "copy",
            "src": "a",
            "dest": "b"
        }
    }
    parm = ModuleArgsParser(task_ds)
    result = parm.parse

# Generated at 2022-06-13 07:04:30.564374
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # There are no unit tests for this class, because this class is a private class for use in Task and Handler.
    # Therefore, it is not tested at all within Ansible, unless it is also used in a task or handler.
    # There is a test for this class as part of the test for the Handler class in unit.playbook.test_handler.py,
    # and there are several tests for this class as part of the test for the Task class in unit.playbook.test_task.py.
    pass


# Now that ModuleArgsParser has been defined, we can import those classes that need it.

from ansible.playbook.attribute import FieldAttribute
from ansible.playbook.base import Base, base_vars
from ansible.playbook.role.definition import RoleDefinition
from ansible.playbook.role.metadata import RoleMetadata

# Generated at 2022-06-13 07:04:40.447254
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """ Unit test for ModuleArgsParser.parse """
    import os
    import sys
    import tempfile
    from ansible.parsing.dataloader import DataLoader

    test_cases = []

    # test_case_0
    test_case_0_task_ds = {"action": {"module": "copy", "args": {"content": "test content", "dest": "foo.txt"}}}
    test_case_0_skip_action_validation = False
    test_case_0_exp_action = "copy"
    test_case_0_exp_args = {"content": "test content", "dest": "foo.txt"}
    test_case_0_exp_delegate_to = None
    test_case_0_exp_resolved_action = "ansible.builtin.copy"
    test_cases

# Generated at 2022-06-13 07:05:01.221625
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    #  get the task_ds from playbook.yml file
    from ansible.playbook.play import Play
    from ansible.config.manager import ConfigManager

    # get a ConfigManager object
    config_manager = ConfigManager(None, None, None)
    # set the config_manager options
    config_manager.options['transport'] = 'local'
    config_manager.options['defaults_loader'] = False
    config_manager.options['verbosity'] = 0
    config_manager.options['listhosts'] = False
    config_manager.options['listtags'] = False
    config_manager.options['listtasks'] = False
    config_manager.options['list_hooks'] = False
    config_manager.options['module_path'] = None
    config_manager.options['inventory'] = None

    # get

# Generated at 2022-06-13 07:05:09.280919
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    t = ModuleArgsParser()
    assert t.parse() == (None, None, None) == (None, None, 'localhost') == (None, {}, None) == (None, {}, 'localhost')
    assert t.parse(skip_action_validation=True) == (None, None, None) == (None, None, 'localhost') == (None, {}, None) == (None, {}, 'localhost')


# Test ModuleArgsParser._split_module_string()

# Generated at 2022-06-13 07:05:10.132013
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# Generated at 2022-06-13 07:05:20.374868
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.splitter import parse_kv
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import MutableMapping
    loader = DictDataLoader({})
    collection_finder = MockCollectionFinder()
    results = collection_finder.resolve_spec_sources('mock_collection1', 'mock_type')
    utils.plugins.loader.add(results['mock_type'], results['paths'])

# Generated at 2022-06-13 07:05:32.009950
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({"an_action": "shell", "another_action": "shell"})
    assert parser.parse() == ('an_action', {}, Sentinel)

    parser = ModuleArgsParser({"action": "shell", "another_action": "shell"})
    assert parser.parse() == ('an_action', {}, Sentinel)

    parser = ModuleArgsParser({"module": "shell", "another_action": "shell"})
    assert parser.parse() == ('shell', {}, Sentinel)

    parser = ModuleArgsParser({"action": "shell", "another_action": "shell"},
                              collection_list=set(['aws']))
    assert parser.parse() == ('an_action', {}, Sentinel)


# Generated at 2022-06-13 07:05:38.336821
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """Test parsing Task._attributes"""

    def test_cases(cases):
        for case in cases:
            task_ds = case['task_ds']
            expected = case['expected']

            print("case: %s" % task_ds)
            parser = ModuleArgsParser(task_ds)
            (action, args, delegate_to) = parser.parse()
            result = dict(action=action, args=args)
            if delegate_to is not Sentinel:
                result['delegate_to'] = delegate_to
            print("result: %s" % result)
            assert result == expected


# Generated at 2022-06-13 07:05:51.096093
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test_thing_1 is a valid task defined in YAML format
    test_thing_1 = {'name': 'get subnet',
                    'connection': 'local',
                    'delegate_to': 'localhost',
                    'local_action': 'ec2_vpc_subnet_facts',
                    'region': 'eu-west-1'}
    # test_thing_2 is a valid task defined in key/value format
    test_thing_2 = {'name': 'get subnet',
                    'connection': 'local',
                    'delegate_to': 'localhost',
                    'local_action': 'ec2_vpc_subnet_facts region=eu-west-1'}
    # test_thing_3 is a valid task defined in key/value format with a dictionary as argument

# Generated at 2022-06-13 07:05:57.444433
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    task_ds = {}

    # positional args
    task_ds = {'action': 'echo hi'}
    m = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = m.parse()
    assert action == 'echo'
    assert args == {}
    assert args.get('_raw_params') == 'hi'
    assert delegate_to is None

    task_ds = {'action': 'copy src=a dest=b'}
    m = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = m.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}
    assert delegate

# Generated at 2022-06-13 07:06:06.151505
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()

    # Execute test code
    task = dict(
        name = 'test_task',
        action = 'copy content=source dest=destination'
    )

    (action, args, delegate_to) = module_args_parser.parse(task)
    assert args == dict(content="source", dest="destination")

    # Execute test code
    task = dict(
        name = 'test_task',
        action = dict(
                module = 'copy',
                src = 'source',
                dest = 'destination'
            )
    )

    (action, args, delegate_to) = module_args_parser.parse(task)
    assert args == dict(src="source", dest="destination")

    # Execute test code

# Generated at 2022-06-13 07:06:10.102008
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    d = dict(
        action=dict(
            module='copy',
            args=dict(
                src='a',
                dest='b',
            )
        ),
        delegate_to='xyz',
    )
    task_ds = d
    collection_list = None
    task_parser = ModuleArgsParser(task_ds, collection_list)
    task_parser.parse()