

# Generated at 2022-06-13 05:49:06.560531
# Unit test for function main
def test_main():
    import sys
    import os
    import io
    from io import StringIO

    from collections import OrderedDict
    from ansible.module_utils.basic import AnsibleModule
    from contextlib import contextmanager

    @contextmanager
    def mock_stdin(input_string):
        original_input = sys.stdin
        sys.stdin = StringIO(input_string)
        yield
        sys.stdin = original_input

    @contextmanager
    def mock_stdout():
        original_stdout = sys.stdout
        stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = original_stdout

    @contextmanager
    def mock_stderr():
        original_stderr = sys.stderr
        stderr = StringIO()
       

# Generated at 2022-06-13 05:49:11.606287
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:49:20.885521
# Unit test for function main
def test_main():

    # Retreive dict of argument_spec //
    argument_spec = dict(
        data=dict(type='str', default='pong'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    # end retreive dict of argument_spec //

    # Retreive dict of function result //
    result = dict(
        ping=module.params['data'],
    )
    # end retreive dict of function result //

    # Assertion of arguments and the result of the function //
    assert module.params['data'] == 'pong'

    assert dict(
        ping=module.params['data'],
    ) == result
    # end assertion of arguments and the result of the function //

# Generated at 2022-06-13 05:49:32.095087
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic
    import basic_ping
    __tracebackhide__ = True
    m = AnsibleModule({},{})
    assert m.params == {}
    m = AnsibleModule(dict(data="crash"))
    m._ansible_builtin_ping = basic_ping.main
    with pytest.raises(Exception) as exc:
        m._ansible_builtin_ping()
    assert "boom" in str(exc.value)
    m = AnsibleModule(dict(data="pong"))
    m._ansible_builtin_ping = basic_ping.main

    m._ansible_builtin_ping()
    assert m.exit_json.called
    assert not m.fail_json

# Generated at 2022-06-13 05:49:39.666461
# Unit test for function main
def test_main():
    # Required for unit tests
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common

    # The following lines simulate the effects of AnsibleModule()
    module = common.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # The following lines simulate the effects of main()
    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:49:44.024232
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            data = dict(type='str', default='pong'),
        ),
        supports_check_mode = True
    )
    result = main()

    assert result['changed'] == False
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:49:45.620605
# Unit test for function main
def test_main():
    # Pong
    result = main()
    assert result['ping']=='pong'


# Generated at 2022-06-13 05:49:50.439771
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)



# Generated at 2022-06-13 05:49:59.966560
# Unit test for function main
def test_main():
    import copy
    fixture = dict(
        ANSIBLE_MODULE_ARGS = dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    fixture = copy.deepcopy(fixture)
    original = copy.deepcopy(fixture)

    # Test when check mode is true
    fixture['ANSIBLE_CHECK_MODE'] = True
    out = main()
    assert out == dict()
    assert fixture == original

    # Test when check mode is false
    fixture['ANSIBLE_CHECK_MODE'] = False
    out = main()
    assert out == dict(
        ping='pong',
    )
    assert fixture == original

# vim: set et ft=python ts=4 sw=4 :

# Generated at 2022-06-13 05:50:05.774510
# Unit test for function main
def test_main():
    '''
    Unit test for function main
    '''
    args = dict(data='pong')
    result = dict(
    ping='pong',
    )
    AnsibleModule = AnsibleModule('ping', argument_spec=dict(
        data=dict(type='str', default='pong'),
        ),
         supports_check_mode=True)
    module = AnsibleModule
    assert result == main(module)

# Generated at 2022-06-13 05:50:15.356504
# Unit test for function main
def test_main():
    test_ansible_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    test_ansible_module.params['data'] == 'pong'
    test_result = {'ping': 'pong'}
    assert test_ansible_module.exit_json(**test_result) == None, "Test if the function 'main' returns the correct result"


# Generated at 2022-06-13 05:50:17.538646
# Unit test for function main
def test_main():
    subprocess.check_output = MagicMock(return_value='pong')
    assert main() == 'pong'

# Generated at 2022-06-13 05:50:23.898430
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={
            "data": {"type": "str", "default": "pong"},
        },
        check_invalid_arguments=False,
        bypass_checks=True,
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )
    assert result == dict(ping='pong')

# Generated at 2022-06-13 05:50:35.852310
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import shutil

    rc, out, err = basic.run_command('python --version')

    if rc != 0:
        # Python isn't installed on the system or isn't configured properly.
        # Don't try to run any tests.
        return

    temp_dir = tempfile.mkdtemp(prefix='ansible_test_folders')


# Generated at 2022-06-13 05:50:38.682739
# Unit test for function main
def test_main():
   with pytest.raises(Exception) as excinfo:
     assert main() == "boom"
 


# Generated at 2022-06-13 05:50:46.722334
# Unit test for function main
def test_main():
    # Run test case for units tests.
    # Used to check the module is working correctly.
    module_args = {'data': 'pong'}
    result = dict(
        ping='pong'
    )
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.exit_json(**result)
    out = module.exit_json(**result)
    assert out["ping"] == result["ping"]

# Generated at 2022-06-13 05:50:50.765352
# Unit test for function main
def test_main():
    output = {'ping': 'pong'}
    module = AnsibleModule(argument_spec={
        'data': dict(type='str', default='pong')
    }, supports_check_mode=True)
    module.exit_json(**output)

# Generated at 2022-06-13 05:51:01.492806
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    def test_module(module):
        assert module.params['data'] == 'pong'
        assert module._check_mode == False

    # Test main() as if it were a method in a class
    def test_class():
        args = {'data': 'pong'}
        setattr(ansible_module, '_ansible_check_mode', False)
        main()
        test_module(ansible_module)

    # Test main() as if it were a method in a class in check mode
    def test_class_check():
        args = {'data': 'pong'}
        setattr(ansible_module, '_ansible_check_mode', True)
        main()
        test_module(ansible_module)

    # Set up

# Generated at 2022-06-13 05:51:07.629413
# Unit test for function main
def test_main():
    import ansible.module_utils.basic as basic
    testmodule = basic.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        )
    )
    result = dict(
        ping=testmodule.params['data'],
    )
    testmodule.exit_json(**result)

# Generated at 2022-06-13 05:51:12.917388
# Unit test for function main
def test_main():
    global raw_result, result, module
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=module.params['data'],
    )
    raw_result = result
    module.exit_json(**result)
    assert True

# Generated at 2022-06-13 05:51:29.014355
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.module_utils.six.moves import StringIO

    module = AnsibleModule(argument_spec=dict())
    stdout = StringIO()
    encoder = AnsibleJSONEncoder()
    module.exit_json(msg='Hello World', changed=True, data=['a', 'b', 'c'])
    result = stdout.getvalue()
    assert result == '{"changed": true, "data": ["a", "b", "c"], "msg": "Hello World", "failed": false}'

# end unit test

# Generated at 2022-06-13 05:51:38.280784
# Unit test for function main
def test_main():
    # Test with default value for data, no exception
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = {"ping": "pong"}
    assert main() == result

    # Test with an explicitly provided data value that doesn't cause an exception
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = {"ping": "test_data"}
    assert main() == result

    # Test with an explicitly provided data value that causes an exception

# Generated at 2022-06-13 05:51:43.954900
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        assert Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:51:54.758688
# Unit test for function main
def test_main():
    import json
    import os

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    library_dir = os.path.join(curr_dir, 'library')
    module_path = os.path.join(library_dir, 'ping')
    module_args = json.dumps({'data': "pong"})
    sys.path.insert(0, module_path)
    try:
        ping = AnsibleModule(argument_spec={
            'data': dict(type='str', default='pong'),
        })
        ping.exit_json(**ping_main(module_args, ping))
    finally:
        sys.path.pop(0)

# Generated at 2022-06-13 05:52:02.626175
# Unit test for function main
def test_main():
    test_args = {}
    test_args["data"] = "pong"
    with patch.object(AnsibleModule, 'exit_json') as mock_exit, patch.object(AnsibleModule, 'run_command') as mock_run:
        instance = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )
        instance.check_mode = False
        instance.params = test_args
        main()
        assert mock_exit.called


# Generated at 2022-06-13 05:52:12.059024
# Unit test for function main
def test_main():
    # Mock all the things!
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleExitJson, AnsibleFailJson, ModuleFailException
    # First we monkeypatch some stuff...
    original_AnsibleModule = AnsibleModule
    original_AnsibleExitJson = AnsibleExitJson
    original_AnsibleFailJson = AnsibleFailJson
    original_ModuleFailException = ModuleFailException
    def dummy_AnsibleModule(*args, **kwargs):
        class MockAnsibleModule():
            def __init__(self, *args, **kwargs):
                self.params = dict(
                    data='pong'
                )
            def fail_json(self, *args, **kwargs):
                raise ModuleFailException()

# Generated at 2022-06-13 05:52:17.880564
# Unit test for function main
def test_main():
    ansible_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    # Unit tests go here
    assert ansible_module.params['data'] == 'pong'
    assert ansible_module.check_mode == True

# Generated at 2022-06-13 05:52:19.393399
# Unit test for function main
def test_main():
    res = main()


# Generated at 2022-06-13 05:52:23.605949
# Unit test for function main
def test_main():
    print("In test_main")
    data="pong"
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default=data),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == data
    result = dict(
        ping=module.params['data'],
    )
    assert result['ping'] == data
    print("End test_main")

test_main()

# Generated at 2022-06-13 05:52:32.204637
# Unit test for function main
def test_main():
    from ansible import context
    context._init_global_context(None)
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:52:51.705827
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == dict(ping='pong')

# Generated at 2022-06-13 05:52:56.121037
# Unit test for function main
def test_main():
    # Test when the target is active
    ping_data = {"ansible_facts":{"ping": "pong"}}
    result = AnsibleModule({"data":"pong"}, check_mode=False).exit_json(**ping_data)
    assert result[0] is True
    assert result[1] == ping_data["ansible_facts"]

    # Test when the target is active but we want a crash
    ping_data = {"ansible_facts":{"ping": "crash"}}
    result = AnsibleModule({"data":"crash"}, check_mode=False).exit_json(**ping_data)
    assert result[0] is False
    assert result[1] == ping_data["ansible_facts"]

# Generated at 2022-06-13 05:52:59.609318
# Unit test for function main
def test_main():
   pong = main()
   assert pong == 'pong'

   # Tests for crashing module functionality.
   # Tests for check_mode functionality.
   # Tests for unsupported platform functionality.
   # Test for .FutureWarning

# Generated at 2022-06-13 05:53:05.192927
# Unit test for function main
def test_main():
    argv = ['ansible-test', 'ping']
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(ping=module.params['data'])
    module.exit_json(**result)

# Generated at 2022-06-13 05:53:11.614854
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:53:12.544938
# Unit test for function main
def test_main():
    # Unit test for function main
    main()

# Generated at 2022-06-13 05:53:18.412914
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # First test
    test_module.params = { 'data' : 'pong' }
    test_main()
    assert test_module.exit_json == dict(
        ping=test_module.params['data'],
    )

    # Second test
    test_module.params = { 'data' : 'crash' }
    test_main()

# Generated at 2022-06-13 05:53:24.951816
# Unit test for function main
def test_main():
    content = dict(
        ANSIBLE_MODULE_ARGS = dict(
            data = 'pong'
        )
    )

    ansible_module_instance = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    result = dict(
        ping=ansible_module_instance.params['data'],
    )

    assert main(ansible_module_instance, content) == result

# Generated at 2022-06-13 05:53:32.962641
# Unit test for function main
def test_main():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.network import NetworkModule
    from ansible.module_utils.ping import Ping

    argument_spec = dict(
        data=dict(type='str', default='pong'),
    )

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    Ping().main()


# Generated at 2022-06-13 05:53:38.312551
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    #module.exit_json(**result)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:54:17.275110
# Unit test for function main
def test_main():
    mock_runner = MagicMock(return_value=(0, '', '', ''))
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        with patch('ansible.module_utils.network.common.runner.CommandRunner', new=mock_runner) as runner:
            with patch('ansible.module_utils.network.common.runner.CommandRunner.get_command_args') as mock_get_command_args:
                mock_get_command_args.return_value = ''
                main()
    assert mock_module.mock_calls == [call(argument_spec={'data': {'required': False, 'type': 'str', 'default': 'pong'}},
                                            supports_check_mode=True)]

# Generated at 2022-06-13 05:54:25.271316
# Unit test for function main
def test_main():
    import os
    import json

    from ansible.module_utils.basic import AnsibleModule

    # TODO: Move this fixture out to a shared location
    data_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'ping_data.json'
    )

    with open(data_file, 'r') as data_fp:
        data = json.load(data_fp)

    for scenario in data:
        args = scenario.get('args')
        result = scenario.get('result')

        module = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )

        # We need to inject the module params into the function directly
        #

# Generated at 2022-06-13 05:54:30.037148
# Unit test for function main
def test_main():
    ping_data = {'ping': 'pong'}
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if ping_data['ping'] == 'pong':
        test_module.exit_json(**ping_data)

# Generated at 2022-06-13 05:54:35.553814
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# FIXME - this is a horrible hack to be able to call this as a seperate
# program rather than a module.  It allows us to test this code through the
# normal interface.
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:54:47.590633
# Unit test for function main
def test_main():
    # Create the basic ansible module mock
    class AnsibleModule(object):
        def __init__(self, argument_spec, supports_check_mode):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.check_mode = False
            self.params = {'data': 'pong'}
            self.exit_json = lambda **kwargs: print(kwargs['ping'])

    # Create the main function mock
    def main():
        module = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )

        if module.params['data'] == 'crash':
            raise Exception("boom")


# Generated at 2022-06-13 05:54:54.163805
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:54:55.184915
# Unit test for function main
def test_main():
    # nothing yet
    print('Test function main')
    main()

# Generated at 2022-06-13 05:54:55.961764
# Unit test for function main
def test_main():
  assert type(main()) == type(None)

# Generated at 2022-06-13 05:54:57.018532
# Unit test for function main
def test_main():
    result = dict(
        ping='pong',
    )
    assert result == main()

# Generated at 2022-06-13 05:54:57.498681
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:56:15.064870
# Unit test for function main
def test_main():
    # Mock module input
    mock_module_args = dict(
        data=dict(type='str', default='pong'),
    )

    # Mock module class
    module_obj = type('AnsibleModule', (), {})()
    module_obj.exit_json = type('exit_json', (), {})()

    exit_json_obj = type('exit_json', (), {})()
    exit_json_obj.result = dict(
        ping="pong"
    )

    # Mock module functions
    module_obj.params = mock_module_args
    module_obj.check_mode = False

    module_obj.exit_json = type('exit_json', (), {})()
    module_obj.exit_json.result = exit_json_obj

    main()

# Generated at 2022-06-13 05:56:24.321712
# Unit test for function main
def test_main():
    # Test module arguments and return values
    # The arguments used below are based on a subset of the actual arguments that the module will receive.
    # This subset is defined by the arg_spec dictionary in the module source code.
    # The return values of the module are based on the return values of the module function, main.
    # These return values are defined by the return statement(s) in the module function.
    # The arguments that the module will receive from the playbook are defined by the keys of the argument_spec dictionary.
    # The module arguments that are defined by argument_spec will also be validated by the AnsibleModule class.
    # For example, the module function cannot return successfully if a required argument has not been set.
    module_args = dict(
        data=dict(type='str', default='pong'),
    )

    # The result_message argument is set to ensure

# Generated at 2022-06-13 05:56:32.025458
# Unit test for function main
def test_main():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.argspec import ArgSpec
    import json
    import os
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils import basic

    class TestException(Exception):
        pass

    def test_main():
        module_args = {'data': 'ping'}
        module_results = {'ping': 'ping'}
        data_key = 'ping'
        empty_args = {}
        args_key = 'data'

        class FakeModule(object):
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs
                self.params = kwargs['argument_spec']
                self.load_result = None



# Generated at 2022-06-13 05:56:33.810006
# Unit test for function main
def test_main():
    # Test 1: ping: crash, sanity check
    assert main() == Exception("boom")
    # Test 2: ping: crash, sanity check
    assert main() == Exception("boom")

# Generated at 2022-06-13 05:56:37.014109
# Unit test for function main
def test_main():
    # test main
    assert main() is None


# Generated at 2022-06-13 05:56:37.651240
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:56:46.541485
# Unit test for function main
def test_main():
    import json
    import pytest
    case = pytest.param({'data': 'ping', 'check_mode': True}, {'ping': 'ping'}, id='check_mode')
    case1 = pytest.param({'data': 'crash'}, pytest.raises(Exception), id='exception')
    for c in (case, case1):
        m = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=c.param['check_mode'] if 'check_mode' in c.param else False)
        m.params = c.param
        with c.mark:
            main()

# Generated at 2022-06-13 05:56:48.690996
# Unit test for function main
def test_main():
    i = {'data': 'crash'}
    try:
        main()
    except Exception as e:
        assert str(e) == 'boom'


# Generated at 2022-06-13 05:56:49.883894
# Unit test for function main
def test_main():
  for i in range (0,10):
    yield run_main_test, i


# Generated at 2022-06-13 05:56:55.919260
# Unit test for function main
def test_main():
    import sys
    from cStringIO import StringIO

    # Set default values for parameters.
    # Use deep copy, to make sure we don't mess up the default values for other tests.
    from copy import deepcopy
    p = deepcopy(DEFAULT_PARAMS)
    p['data'] = 'pong'

    # Capture stdout so we can check if we get the expected result.
    stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    main()

    # Check if we got the expected result.
    sys.stdout = stdout
    assert mystdout.getvalue() == '{"changed": false, "ping": "pong"}'
