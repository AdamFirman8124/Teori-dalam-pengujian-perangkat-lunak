

# Generated at 2022-06-13 06:57:10.127149
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # help() doesn't work in unit tests so we'll have to use the code
    # which is the most common case
    ds = dict(
        action=dict(
            module='ec2',
            x=1,
        ),
    )

    args_parser = ModuleArgsParser(ds)
    action, args, delegate_to = args_parser.parse()
    assert action == 'ec2'
    assert args['x'] == 1
    assert delegate_to is None

    ds = dict(
        local_action=dict(
            module='ec2',
            x=1,
        ),
    )

    args_parser = ModuleArgsParser(ds)
    action, args, delegate_to = args_parser.parse()
    assert action == 'ec2'
    assert args['x'] == 1
    assert delegate_to

# Generated at 2022-06-13 06:57:20.224897
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds=dict())
    (action, args, delegate_to) = parser.parse(skip_action_validation=True)
    assert action is None
    assert args is None
    assert delegate_to is Sentinel

    parser = ModuleArgsParser(task_ds=dict(action=dict()))
    (action, args, delegate_to) = parser.parse(skip_action_validation=True)
    assert action is None
    assert args is None
    assert delegate_to is Sentinel

    parser = ModuleArgsParser(task_ds=dict(action=''))
    (action, args, delegate_to) = parser.parse(skip_action_validation=True)
    assert action is None
    assert args is None
    assert delegate_to is Sentinel


# Generated at 2022-06-13 06:57:30.805313
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = dict()
    args['delegate_to'] = None
    args['action'] = 'copy'
    args['task_ds'] = {u'delegate_to': None, u'action': u'copy'}
    args['_task_ds'] = {u'delegate_to': None, u'action': u'copy'}
    args['collection_list'] = None
    args['_collection_list'] = None
    args['_task_attrs'] = frozenset([u'local_action', u'static'])

    obj = ModuleArgsParser(**args)
    result = obj.parse(skip_action_validation=False)
    assert result == ('copy', {}, None)


# Generated at 2022-06-13 06:57:40.240791
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # prep function
    def parse_kv(arg_string):
        return dict()

    def _split_module_string(module_string):
        return {'action': 'test', 'args': ''}

    def _normalize_old_style_args(thing):
        if thing == {'module': 'ec', 'x': 1}:
            return {'action': 'ec', 'args': {'x': 1}}

    def _normalize_new_style_args(thing, action):
        if thing == {'module': 'ec', 'x': 1} and action == 'ec':
            return {'x': 1}

    def _normalize_parameters(thing, action=None, additional_args=None):
        return 'ec', {'x': 1}

    task_ds = {'x': 1}
    collection

# Generated at 2022-06-13 06:57:42.893214
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser({
        'action': 'copy src=a dest=b',
        'name': 'copy file to the node',
        'local_action': 'shell sleep 10',
    },[])

    assert module_args_parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, 'localhost')
# end of test_ModuleArgsParser_parse()


# Generated at 2022-06-13 06:57:51.975729
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Test case 1: If the type of task_ds is not dict, it should raise
        AnsibleAssertionError.
    Test case 2: If the type of thing is dict, it should return the action
        and args.
    Test case 3: If the type of thing is string, it should return the action
        and args.
    Test case 4: If args and action are not in FREEFORM_ACTIONS, it should
        raise AnsibleError.
    '''

    # Test case 1

# Generated at 2022-06-13 06:57:59.702359
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    # Test for when args has dict form
    #
    task_ds = {'action': {'module': 'copy', 'src': 'a', 'dest': 'b'}}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    expected = ('copy', {'src': 'a', 'dest': 'b'}, None)
    actual = parser.parse()
    assert expected == actual
    #
    # Test for when args has string form
    #
    task_ds = {'action': 'copy src=a dest=b'}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    expected = ('copy', {'src': 'a', 'dest': 'b'}, None)
    actual = parser.parse()
    assert expected

# Generated at 2022-06-13 06:58:02.592405
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    ok_(module_args_parser)
    print(module_args_parser.parse())

import ansible.module_utils.basic

# Generated at 2022-06-13 06:58:09.829550
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # The is a unit test for ModuleArgsParser.parse()
    # that tests whether it can properly parse the following YAML structure
    #  as a dict.

    from ansible.parsing.mod_args import ModuleArgsParser
    from collections import namedtuple

# Generated at 2022-06-13 06:58:16.121451
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:58:29.998213
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    thing = dict(src='a', dest='b')
    action = None
    additional_args = dict()
    args = dict()
    parser = ModuleArgsParser()
    ret = parser._normalize_parameters(thing=thing, action=action, additional_args=additional_args)
    assert(ret == ('unknown', dict(src='a', dest='b')))

    thing = 'copy src=a dest=b'
    action = None
    additional_args = dict()
    args = dict()
    parser = ModuleArgsParser()
    ret = parser._normalize_parameters(thing=thing, action=action, additional_args=additional_args)
    assert(ret == ('copy', dict(src='a', dest='b')))


# Generated at 2022-06-13 06:58:40.738321
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # args[0] is action, args[1] is args, args[2] is delegate_to
    # testcase 1 -- without delegate_to
    mp = ModuleArgsParser({'action': 'echo hi', 'args': {'_raw_params': '{{ vars }}'}})
    assert (mp.parse() == ('echo', {'_raw_params': '{{ vars }}'}, Sentinel))
    # testcase 2 -- with delegate_to
    mp = ModuleArgsParser({'local_action': 'echo hi'})
    assert (mp.parse() == ('echo', {}, 'localhost'))
    # testcase 3
    mp = ModuleArgsParser({'action': 'copy src=a dest=b'})
    assert (mp.parse() == ('copy', {'src': 'a', 'dest': 'b'}, Sentinel))


# Generated at 2022-06-13 06:58:48.245853
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    task_ds = {'action': {'delegate_to': 'localhost', 'module': 'shell', 'args': {'_raw_params': 'echo hi'}}}
    collection_list = [AnsibleCollectionConfig('/Users/alikins/git/ansible/test/units/modules/test_collections/ansible_collections/testns/testcoll/',
                                               '/Users/alikins/git/ansible/test/units/modules/test_collections/ansible_collections/testns/testcoll/plugins/modules')]

# Generated at 2022-06-13 06:58:50.729102
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    # Nothing to test as python lists are mutable.
    return

# Generated at 2022-06-13 06:58:53.716456
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    result = module_args_parser.parse()
    assert result == (None, {}, Sentinel)

# Generated at 2022-06-13 06:58:56.724426
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'test_action': {'test_module_args': 'test_value'}}
    module_args_parser = ModuleArgsParser(collection_list=[], task_ds=task_ds)
    assert (module_args_parser.parse() == ('test_action', {'test_module_args': 'test_value'}, None))


# Generated at 2022-06-13 06:59:02.125504
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from collections import MutableMapping
    from six import itervalues
    import pytest
    from ansible.module_utils.six.moves.urllib.parse import quote
    from ansible.errors import AnsibleParserError, AnsibleAssertionError, AnsibleError
    from ansible.module_utils._text import to_text, to_bytes

    # initialize
    task_ds = dict()
    collection_list = list()
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    # At

# Generated at 2022-06-13 06:59:03.406600
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  ok_(True)

# Generated at 2022-06-13 06:59:15.565047
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("############# test_ModuleArgsParser_parse ##############")

    m = ModuleArgsParser()
    # failed: action: { module: 'copy', src: 'a', dest: 'b' }
    # failed: 'shell echo hi'
    # failed: { 'shell' : 'echo hi' }
    # success: {'module': 'ec2', 'x': 1 }
    # failed: { region: xyz }

    d = {'module': 'ec2', 'x': 1}
    action, args, delegate_to = m.parse()
    print("action: %s" % action)
    print("args: %s" % args)
    print("delegate_to: %s" % delegate_to)
    print("_task_ds: %s" % m._task_ds)
# Unit test

# Generated at 2022-06-13 06:59:26.115851
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test module with local action

    task_ds = dict(
        delegate_to = 'local',
        action = 'shell echo "Hello World"'
    )
    ds = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = ds.parse()
    assert action == 'shell'
    assert args == {
        'ARGS': 'echo "Hello World"'
    }
    assert delegate_to == 'local'
    # Test module with delegate_to
    task_ds = dict(
        delegate_to = u'local',
        copy = u'src=/tmp/source dest=/tmp/dest'
    )
    ds = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = ds.parse

# Generated at 2022-06-13 06:59:41.446788
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    @mock.patch.object(ModuleArgsParser, "_split_module_string", return_value=("copy", "src=a dest=b"))
    @mock.patch.object(ModuleArgsParser, "_normalize_parameters", return_value=("copy", {"src": "a", "dest": "b"}))
    def test_ModuleArgsParser_parse_1(Mock1, Mock2):
        m = ModuleArgsParser({"action": "copy: src=a dest=b"})
        assert m.parse() == ("copy", {"src": "a", "dest": "b"}, Sentinel)
        assert m.resolved_action is None


# Generated at 2022-06-13 06:59:45.428562
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    task_ds = {
        'module': 'ping',
        'delegate_to': 'localhost'
    }
    collection_list = []
    module_args_parser = ModuleArgsParser(task_ds, collection_list)

    result = module_args_parser.parse()

    assert result.get("action") == "ping"
    assert result.get("args") is None
    assert result.get("delegate_to") == "localhost"


# Generated at 2022-06-13 06:59:46.530924
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with pytest.raises(AnsibleParserError):
        ModuleArgsParser(task_ds={})


# Generated at 2022-06-13 06:59:57.952138
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    class UnitTestModuleArgsParser(ModuleArgsParser):
        pass

    # testing following block of code
    #
    # if action is not None:
    #     raise AnsibleParserError("action and local_action are mutually exclusive", obj=self._task_ds)
    in_dict = dict()
    in_dict['action'] = 'action'
    in_dict['local_action'] = 'local_action'

    t = UnitTestModuleArgsParser(task_ds=in_dict)
    try:
        t.parse()
        assert False
    except AnsibleParserError as e:
        err_msg = "action and local_action are mutually exclusive"
        if err_msg not in str(e):
            assert False
        else:
            assert True

    # testing following block of code
    #
    # if context is not None

# Generated at 2022-06-13 07:00:01.648763
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()
#    collection_list = None
    obj = ModuleArgsParser(task_ds=task_ds)
    obj.parse()
    print('test_ModuleArgsParser_parse')
    return


# Generated at 2022-06-13 07:00:02.223606
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# Generated at 2022-06-13 07:00:10.511107
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.task_ds import TaskData
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    task_ds = TaskData()
    task_ds.update({'action': 'shell echo hi',
     'args': 'chdir=/tmp'})
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert type(delegate_to)==Sentinel
    assert action=='shell'
    assert args['_raw_params']=='echo hi'
    assert type(args)==dict
    assert args['chdir']=='/tmp'
    task_ds = TaskData()

# Generated at 2022-06-13 07:00:16.135737
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_task_ds = {'delegate_to': 'localhost', 'action': {'module': 'shell', 'args': 'echo hi'}, 'args': {'chdir': '/tmp'}, 'local_action': {'module': 'shell', 'args': 'echo hi'}}
    a = ModuleArgsParser(task_ds=test_task_ds)
    action, args, delegate_to = a.parse()
    assert (action == 'shell')
    assert (args == {'args': 'echo hi', 'chdir': '/tmp'})
    assert (delegate_to == 'localhost')

# Generated at 2022-06-13 07:00:25.203996
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    actual = ModuleArgsParser(task_ds=ANSIBLE_TASK_DS, collection_list=ANSIBLE_COLLECTION_LIST).parse()
    expected = {
        'action': 'setup',
        'args': {
            'filter': 'ansible_virtualization_role',
            'fact_path': '<path to modules directory>/ansible/module_utils/facts.d',
            'gather_subset': None,
            'gather_timeout': 10
        },
        'delegate_to': None
    }
    assert actual == expected

### class ActionModule

# Generated at 2022-06-13 07:00:35.463822
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
 
    # Test with correct arguments
    args_parser = ModuleArgsParser({'action': 'command', 'args': {'_raw_params': 'echo hi'}}, collection_list=None)  
    assert (args_parser.parse(skip_action_validation=False) == ('command', {'_raw_params': 'echo hi'}, None)) 
 
    # Test with wrong arguments
    #args_parser = ModuleArgsParser({'action': 'command', 'args': 'echo hi'}, collection_list=None)
    #assert not (args_parser.parse(skip_action_validation=True) == ('command', {'_raw_params': 'echo hi'}, None)) 
 
    # Test with wrong arguments
    #args_parser = ModuleArgsParser({'action': 'command', 'args': 'echo hi'},

# Generated at 2022-06-13 07:00:42.356836
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # action, args, delegate_to = ModuleArgsParser(task_ds).parse()
    action, args, delegate_to = ModuleArgsParser().parse()
    print(args)
    print(action)
    print(delegate_to)

if __name__ == '__main__':
    test_ModuleArgsParser_parse()

# Generated at 2022-06-13 07:00:48.008698
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    p = ModuleArgsParser()
    task_ds = {
        'action': 'copy src=a dest=b',
        'delegate_to': 'localhost'
    }
    result = p.parse(task_ds=task_ds)
    print(result)

    task_ds = {
        'action': {
            'module': 'copy src=a dest=b'
        },
        'delegate_to': 'localhost'
    }
    result = p.parse(task_ds=task_ds)
    print(result)

    task_ds = {
        'action': {
            'module': 'copy',
            'src': 'a',
            'dest': 'b'
        },
        'delegate_to': 'localhost'
    }

# Generated at 2022-06-13 07:00:57.803894
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''

    # Instance the class
    module_args_parser = ModuleArgsParser()

    # Create arg1
    arg1 = 'shell echo hi'

    # Create arg2
    arg2 = 'copy src=a dest=b'

    # Create arg3
    arg3 = 'start with_items={{ servers }}'

    # Create arg4
    arg4 = """action:
  module: command
  args:
    _raw_params: 'echo hi'
    chdir: '/tmp'
  delegate_to: localhost"""

    # Create arg5
    arg5 = """action:
  module: copy
  args:
    src: a
    dest: b
  delegate_to: localhost"""

    # Create arg6

# Generated at 2022-06-13 07:01:04.048785
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # Unit test for method parse of class ModuleArgsParser
    class MyModuleArgsParser(ModuleArgsParser):
        def __init__(self, task_ds=None, collection_list=None):
            super(MyModuleArgsParser, self).__init__(task_ds=task_ds, collection_list=collection_list)
            self.__getattr__ = self.__getattribute__
            self._task_ds = task_ds
            self._collection_list = collection_list
            # delayed local imports to prevent circular import
            from ansible.playbook.task import Task
            from ansible.playbook.handler import Handler
            # store the valid Task/Handler attrs for quick access
            self._task_attrs = set(Task._valid_attrs.keys())

# Generated at 2022-06-13 07:01:14.331393
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    my_object = ModuleArgsParser()

# class RawCondition:

#     def __init__(self, condition):
#         self.condition = condition

#     def run(self, variables=None, allvars=None, omit=None, **kwargs):
#         ## FIXME: need to correctly handle loop and fail
#         if watch:
#             # FIXME: this will depend on a new callback plugin type, or
#             #        some other work we haven't done yet
#             pass

#         if kwargs.get('fail'):
#             # FIXME: need to implement try/except around the run of the task
#             #        to check for failed/unreachable status and then exit if
#             #        fail: true is set on the blocked task (or if fail is present,
#             #        even if it

# Generated at 2022-06-13 07:01:21.004905
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # set up test data
    task_ds = {'action': 'shell echo hi'}
    # execute the code to be tested
    parser = ModuleArgsParser(task_ds, ['my_collections'])
    parser.parse()
    # verify the outcome
    assert parser.resolved_action is None
    assert parser._task_ds['action'] == 'shell echo hi'


# Generated at 2022-06-13 07:01:33.965110
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Input data
    task_ds = {}
    collection_list = None

    # Expected output
    expected_output = {'returned_values': {'action': None, 'args': {}, 'delegate_to': None}}

    # Create object under test
    module_args_parser_obj = ModuleArgsParser(
        task_ds=task_ds,
        collection_list=collection_list
        )

    # Call method being tested
    method_output = module_args_parser_obj.parse(skip_action_validation=False)

    # Compare method output with expected output
    assert (method_output == expected_output['returned_values'])


# Generated at 2022-06-13 07:01:42.454826
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Setup
    task_ds = {'action': 'ping', 'delegate_to': None, 'args': {'_raw_params': 'foo', '_uses_shell': True}}
    collection_list = None

    # Invocation
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    # Verification
    assert 'ping' == module_args_parser.action
    assert {
        '_raw_params': 'foo',
        '_uses_shell': True,
    } == module_args_parser.args
    assert None == module_args_parser.delegate_to
    assert 'ping' == module_args_parser.resolved_action

# Generated at 2022-06-13 07:01:47.059451
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  # This testcase is created by iwaseyusuke
  # Currently, this testcase covers below statements.
  # 100% Statement coverage
  assert True


# class ModuleStore

# Generated at 2022-06-13 07:01:55.330910
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        "action": {
            "module": "command",
            "free-form": "shell echo hi"
        },
        "delegate_to": "localhost",
        "name": "test-module-args-parser-parse",
        "notify": ["HandlerName"],
        "register": "var_name"
    }
    collection_list = ansible_collections
    def_args = {
        "_ansible_parsed": True,
        "_ansible_check_mode": False,
        "_ansible_no_log": False,
        "_raw_params": "shell echo hi"
    }
    # Test with ordinary input
    mod_args_parser = ModuleArgsParser(task_ds, collection_list)

# Generated at 2022-06-13 07:02:07.296200
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''test_ModuleArgsParser_parse
    Tests normalize_parameters method of ModuleArgsParser class.
    '''
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    def parse(task_ds, collection_list=None):
        '''
        Parses the YAML input task to a canonical form.
        '''
        # test_normalize_parameters
        task_ds = dict(task_ds) if task_ds else dict()

        if not isinstance(task_ds, dict):
            raise AssertionError
        parser = ModuleArgsParser(task_ds, collection_list)
        return parser.parse()

    # test_normalize_parameters

# Generated at 2022-06-13 07:02:15.119699
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    hostvars = HostVars({}, variable_manager)
    variable_manager._fact_cache[inventory.get_host('localhost').name] = hostvars

# Generated at 2022-06-13 07:02:23.009497
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    with mock.patch.object(AnsibleParserError, 'message'):
        with mock.patch.object(AnsibleParserError, 'obj'):
            with mock.patch.object(AnsibleParserError, 'wrap_info'):
                module_arg_parser = ModuleArgsParser({ 'action': 'shell echo hi' })
                module_arg_parser.parse()


# Generated at 2022-06-13 07:02:32.906257
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest


# Generated at 2022-06-13 07:02:47.695668
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': {'args': '{{ hostname }}'}}

    obj = ModuleArgsParser(task_ds=task_ds, collection_list=[])
    action, args, delegate_to = obj.parse()

    assert action is None
    # TODO: args is currently None, but should be {'_variable_params': '{{ hostname }}'}

    task_ds = {'action': 'shell echo hi'}
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=[])
    action, args, delegate_to = obj.parse()

    assert action == 'shell'

    task_ds = {'action': {'module': 'shell echo hi'}}
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=[])

# Generated at 2022-06-13 07:02:57.937975
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    assert module_args_parser.parse() == (None, None, 'localhost')
    
    

# Generated at 2022-06-13 07:03:03.765920
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_text

    _loader = DictDataLoader({})
    collection_loader = CollectionLoader()
    collection_list = collection_loader.list_collections({})

    # constructor test cases
    module_args_parser = ModuleArgsParser()
    assert module_args_parser.__class__ == ModuleArgsParser

    # parse test cases
    module_args_parser = ModuleArgsParser(task_ds={}, collection_list=None)
    assert module_args_parser.parse(skip_action_validation=False) == (None, None, None)

    # parse test cases
    module_args_parser = ModuleArgsParser(task_ds={'action': 'command'}, collection_list=None)

# Generated at 2022-06-13 07:03:11.219857
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action_plugin_manager = ActionModule._shared_loader_obj
    module_plugin_manager = ModuleLoader._shared_loader_obj

    # Setup test data
    obj = ModuleArgsParser()

    def test_copy_var_to_files(variable_name, variable_value):
        task_ds = dict(
            action='copy content="{{' + variable_name + '}}" dest=/tmp/' + variable_name + '.txt mode=0644',
            args=dict(
                content=variable_value,
                dest='/tmp/' + variable_name + '.txt',
                mode='0644',
            ),
            delegate_to='localhost',
        )
        
        # Do the actual test
        (action, args, delegate_to) = obj.parse(task_ds)

        # Verify the results

# Generated at 2022-06-13 07:03:19.600396
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    def mock_import(module):
        return None

    from ansible.module_utils import basic
    basic.import_module = mock_import

    # Test cases for the parse method

# Generated at 2022-06-13 07:03:34.803778
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # tests shorthand module syntax
    ds = dict(action="debug msg=test")
    ap = ModuleArgsParser(ds)
    (action, args, delegate_to) = ap.parse()
    assert action == 'debug'
    assert args == dict(msg='test')

    # tests shorthan module syntax with complex args
    ds = dict(action="debug", args=dict(msg='test'))
    ap = ModuleArgsParser(ds)
    (action, args, delegate_to) = ap.parse()
    assert action == 'debug'
    assert args == dict(msg='test')

    # tests shorthand module syntax with variable complex args
    ds = dict(action="debug", args='{"msg": "{{ test }}"}')
    ap = ModuleArgsParser(ds)
    (action, args, delegate_to) = ap.parse

# Generated at 2022-06-13 07:03:43.727959
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds=[{'module': u'ec2', 'args': 'region=us-west-1', 'delegate_to': 'localhost'}]
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser.parse() == ('ec2', {u'region': u'us-west-1'}, 'localhost')



# Generated at 2022-06-13 07:03:49.759250
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    kwargs = {}
    self = ModuleArgsParser(**kwargs)
    task_ds = {
              "action": {
                "module": "ec2",
                "x": 1
              },
              "delegate_to": "xyz",
              "args": {
                "chdir": "/tmp"
              }
            }
    self._task_ds = task_ds
    self._collection_list = None
    # store the valid Task/Handler attrs for quick access
    self._task_attrs = set(Task._valid_attrs.keys())
    self._task_attrs.update(set(Handler._valid_attrs.keys()))
    # HACK: why are these not FieldAttributes on task with a post-validate to check usage?

# Generated at 2022-06-13 07:03:52.798935
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''
    ModuleArgsParser.parse()



# Generated at 2022-06-13 07:04:03.221130
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser( {} )
    task_ds = {
        'action': 'shell',
        'delegate_to': 'test-delegate_to',
    }
    actual = parser.parse( skip_action_validation=True )
    expected = ( 'shell', {}, 'test-delegate_to' )
    assert actual == expected

    task_ds = {
        'action': 'copy src=a dest=b',
        'delegate_to': 'test-delegate_to',
    }
    actual = parser.parse( skip_action_validation=True )
    expected = ( 'copy', { 'dest': 'b', 'src': 'a' }, 'test-delegate_to' )
    assert actual == expected


# Generated at 2022-06-13 07:04:08.625078
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'copy src=a dest=b'}

    m = ModuleArgsParser()
    # Uncomment for code coverage
    # m.resolved_action = None
    # m._task_ds = task_ds
    # m._collection_list = None
    ret = m.parse()
    assert ret == ('copy', {'dest': 'b', 'src': 'a'}, None)

# Generated at 2022-06-13 07:04:22.017222
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import json


# Generated at 2022-06-13 07:04:30.272272
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    action = "copy"
    dict_args = dict()
    dict_args["src"] = "/etc/ansible/source"
    dict_args["dest"] = "/etc/ansible/destination"
    dict_args["content"] = "hello world"
    dict_args["original_basename"] = "ansible.cfg"
    thing = "src={{ src }} dest={{ dest }} content={{ content }}"
    testModuleArgsParser = ModuleArgsParser(thing, action)
    assert testModuleArgsParser.parse() == (action, dict_args, None)

# ---------------------------------------------------------------------------------------------------------

# Generated at 2022-06-13 07:04:30.938826
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

# Generated at 2022-06-13 07:04:36.566259
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'module': 'copy',
        'args': {
            'src': 'a',
            'dest': 'b'
        }
    }
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)



# Generated at 2022-06-13 07:04:44.109386
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({})
    assert parser.parse() == (None, dict(), None)

    parser = ModuleArgsParser({'action': ''})
    assert parser.parse() == (None, dict(), None)

    parser = ModuleArgsParser({'action': 'ping'})
    assert parser.parse() == ('ping', dict(), None)

    parser = ModuleArgsParser({'action': 'ping',
                               'args': '-a num_pings=3'})
    assert parser.parse() == ('ping', {'a': 'num_pings=3', '_raw_params': ''}, None)

    parser = ModuleArgsParser({'action': 'ping',
                               'args': '-a num_pings=3',
                               'delegate_to': 'localhost'})

# Generated at 2022-06-13 07:05:11.386133
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    tmp_task_ds = {'check_mode': False, 'vars': {}, 'when': True, 'name': '''/usr/bin/whoami''', '_ansible_no_log': False, '_ansible_verbosity': 1, 'register': 'foo', 'local_action': 'command {{userbin_whoami}}', '_ansible_module_name': 'command'}
    tmp_collection_list = []
    obj = ModuleArgsParser(tmp_task_ds, tmp_collection_list)
    (action, args, delegate_to) = obj.parse()
    assert action == 'command'
    assert args == {'_raw_params': '{{userbin_whoami}}'}
    assert delegate_to == 'localhost'


# class RoleParser

# Generated at 2022-06-13 07:05:20.990127
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common.text.converters import to_text
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager

    fixture_default_args = dict(
        action='ping',
        args=dict(),
        delegate_to=None
    )
    fixture_complex_args = dict(
        action='setup',
        args=dict(filter='ansible_eth[0-9]'),
        delegate_to=None
    )
    fixture_delegate_to = dict(
        action='ping',
        args=dict(),
        delegate_to='127.0.0.1'
    )

    # test minimal task
    task_ds = dict(action='ping')

# Generated at 2022-06-13 07:05:32.190718
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action=dict(module='shell', echo='sup'),
        args=dict(chdir='/tmp'),
    )
    mp = ModuleArgsParser(task_ds)
    result = mp.parse()
    assert result == ('shell', dict(_raw_params='echo=sup' ,chdir='/tmp'), None), "ModuleArgsParser.parse() returns wrong setup"

    task_ds = dict(action="shell echo=sup")
    mp = ModuleArgsParser(task_ds)
    result = mp.parse()
    assert result == ('shell', dict(_raw_params='echo=sup'), None), "ModuleArgsParser.parse() returns wrong setup"

    task_ds = dict(action="shell echo=sup", delegate_to="localhost")
    mp = ModuleArgsParser(task_ds)

# Generated at 2022-06-13 07:05:43.594046
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    unit test for method parse of class ModuleArgsParser
    '''
    print('\n\n test_ModuleArgsParser_parse()')
    md_args_parser = ModuleArgsParser()
    action, args, delegate_to = md_args_parser.parse(task_ds={})
    pprint(action)
    pprint(args)
    pprint(delegate_to)
    '''
    expected results:
    Traceback (most recent call last):
    AnsibleError: no module/action detected in task.
    '''
    print('\n\n')

# Generated at 2022-06-13 07:05:52.702204
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        "action": {
            "module": "slack",
            "channel": "random",
            "token": "/root/slack.token",
            "msg": "Hello World!"
        }
    }
    parser = ModuleArgsParser(task_ds=task_ds)
    expected = {
        "_raw_params": "",
        "channel": "random",
        "msg": "Hello World!",
        "token": "/root/slack.token",
        "with_items": [],
        "with_random": None
    }
    returned = parser.parse()[1]
    assert returned == expected


# Generated at 2022-06-13 07:05:55.863407
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    print("In test_ModuleArgsParser_parse")
    md = ModuleArgsParser()
    assert(md.parse() is not None)


# Generated at 2022-06-13 07:06:07.183456
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict()

    parser = ModuleArgsParser()
    action, args, delegate_to = parser.parse(task_ds)

    result = action
    assert result == 'shell'

    result = args
    assert result is None

    result = delegate_to
    assert result is None

    task_ds = {u'action': u'shell echo hi'}

    parser = ModuleArgsParser()
    action, args, delegate_to = parser.parse(task_ds)

    result = action
    assert result == 'shell'

    result = args
    assert result is None

    result = delegate_to
    assert result is None

    task_ds = {u'action': {'module': u'shell echo hi'}}

    parser = ModuleArgsParser()
    action, args, delegate_to = parser.parse(task_ds)

# Generated at 2022-06-13 07:06:11.859039
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'name': '', 'with_items': [''], 'with_nested': [{'name': '', 'with_items': ['']}], 'tags': ['test'], 'when': ''}
    collection_list = ['collection1', 'collection2']

    parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    assert parser.parse() == (None, None, None)

# Generated at 2022-06-13 07:06:13.224405
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    this_parser = ModuleArgsParser()
    this_parser.parse()



# Generated at 2022-06-13 07:06:20.466066
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {u'action': u'{{t}}', u'args': u'{{t}}', u'delegate_to': u'localhost'}
    obj = ModuleArgsParser(task_ds)
    result = obj.parse()
    assert result == (u'{{t}}', {u'_variable_params': u'{{t}}'}, u'localhost')

    task_ds = {u'local_action': {u'p': u'{{t}}', u'q': u'{{t}}'}}
    obj = ModuleArgsParser(task_ds)
    result = obj.parse()
    assert result == (u'p', {u'p': {u'p': u'{{t}}', u'q': u'{{t}}'}, u'q': u'{{t}}'}, u'localhost')

    task