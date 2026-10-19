

# Generated at 2022-06-13 05:49:01.797630
# Unit test for function main
def test_main():
    argument_spec = {'data': {'type': 'str', 'default': 'pong'}}
    assert main(dict()) == dict(ping='pong')
    assert main(dict(data='crash')) == dict(ping='pong')
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:49:02.277973
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:49:06.698901
# Unit test for function main
def test_main():
    # Function data declaration
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Data declaration
    data = 'pong'

    result = dict(
        ping=module.params['data'],
    )

    print(result)
    # Verify the results
    assert(result == result)

# Generated at 2022-06-13 05:49:10.175376
# Unit test for function main
def test_main():
    ping = unittest.mock.MagicMock(data='ping')
    ansible_module = unittest.mock.MagicMock(spec_set=AnsibleModule)
    ansible_module.exit_json.return_value = ping
    class_args = [dict(data='ping')]
    assert main(class_args, ansible_module) == ping
    ansible_module.exit_json.assert_called_with(ping='ping')

# Generated at 2022-06-13 05:49:10.820868
# Unit test for function main
def test_main():
  assert main() is None

# Generated at 2022-06-13 05:49:20.341759
# Unit test for function main
def test_main():
    module_mock = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module_mock.params = { 'data': 'pong' }

    # Test function error
    try:
        result = main()
        assert False, "Expected exception"
    except SystemExit as e:
        assert isinstance(e.code, int), "Expected int"
        assert e.code == 0, "Expected 0"

    # Test function error
    try:
        module_mock.params = { 'data': 'crash' }
        result = main()
        assert False, "Expected exception"
    except Exception as e:
        assert False, 'ValueError not raised'

    # Normal case


# Generated at 2022-06-13 05:49:31.593757
# Unit test for function main
def test_main():
    class AnsibleModuleException(Exception):
        def __init__(self, results):
            self.results = results

    def ansible_module_exit_json(results=None, **kwargs):
        if results:
            raise AnsibleModuleException(results)
        return dict(data=kwargs)

    def ansible_module_fail_json(msg=None, **kwargs):
        raise AnsibleModuleException(msg)

    module = {}
    module['params'] = {'data': 'pong'}
    module['check_mode'] = False
    module['exit_json'] = ansible_module_exit_json

    try:
        main()
    except AnsibleModuleException as e:
        if e.results != dict(ping='pong'):
            raise AssertionError()
        return True
    raise Ass

# Generated at 2022-06-13 05:49:34.255857
# Unit test for function main
def test_main():
    """ Ping module unit test stubs """
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    result = dict(
        ping=module.params['data'],
    )

# Generated at 2022-06-13 05:49:40.565187
# Unit test for function main
def test_main():
    core_ansible = dict(
        changed=False,
        ping='pong',
    )

    def new_module(additions=None):
        if additions is None:
            additions = dict()

        return AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )

    # Test main without exception
    m = new_module()
    main()
    assert m.params == dict(data='pong')
    assert m.exit_json.call_count == 1
    args, kwargs = m.exit_json.call_args
    assert args == tuple()
    assert kwargs == core_ansible

    # Test main with exception
    m = new_module()
    m.params['data']

# Generated at 2022-06-13 05:49:41.178834
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:49:45.709467
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:49:50.511972
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


# Generated at 2022-06-13 05:49:56.287130
# Unit test for function main
def test_main():
    """
    Test function main of the ping module
    """
    module_helper = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    data = module_helper.params['data']

    # When data is equal pong, function main should return pong
    if data == 'pong':
        assert main() == dict(ping='pong')

    # When data is equal crash, function main should raise an exception
    if data == 'crash':
        with pytest.raises(Exception) as err:
            main()
        assert str(err.value) == 'boom'



# Generated at 2022-06-13 05:50:01.221231
# Unit test for function main
def test_main():
    response = {'failed': False, 'changed': False, 'ping': 'pong'}
    assert main({'data': 'pong'}) == response
    response = {'failed': True, 'changed': False}
    assert main({'data': 'crash'}) == response

# Generated at 2022-06-13 05:50:08.813683
# Unit test for function main
def test_main():
    import os
    os.environ = {"ANSIBLE_MODULE_ARGS": '{"data": "pong"}'}
    try:
      from ansible.modules.system.ping import *
      from ansible.module_utils.basic import AnsibleModule

      C = AnsibleModule
      C.check_mode = lambda self: True
      C.params = {}
      C.args = {}
      C.jsonify = lambda self, s: s
      C.fail_json = lambda self, a, b: None
      C.exit_json = lambda self, a: None
      main()
    except Exception as e:
      raise e

# Generated at 2022-06-13 05:50:14.315741
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    data = module.params['data']
    assert data == 'pong'

# Generated at 2022-06-13 05:50:22.475065
# Unit test for function main
def test_main():
    test_func = main
    # The parameter data is set to 'pong' by default. This will be used for testing.
    # The 'data' parameter is the only parameter that the user can change in the Ansible module.
    # Note that the set_module_args call is similar to the call from Ansible.
    test_func.set_module_args(dict(data="pong"))
    result = test_func()
    print(result)
    assert(result['text'] == 'pong')
    
    test_func.set_module_args(dict(data="crash"))
    with pytest.raises(Exception) as e:
        test_func()

# Generated at 2022-06-13 05:50:24.319706
# Unit test for function main
def test_main():
  module_class = AnsibleModule
  AnsibleModule = None
  res = main()
  AnsibleModule = module_class
  return res

# Generated at 2022-06-13 05:50:35.892682
# Unit test for function main
def test_main():
    from ansible.modules.network.nios.nios_dhcp_shared_range import main
    from ansible.module_utils.network.nios.nios import get_config

    module = AnsibleModule(
        argument_spec=dict(
            provider=dict(required=True),
            state=dict(default='present', choices=['present', 'absent']),
            dhcp_shared_range=dict(required=True, type='list'),
        )
    )

    # Set up mock
    m1 = mocker.patch('ansible.module_utils.network.nios.nios.WapiModule.__init__', return_value=None)
    m2 = mocker.patch('ansible.module_utils.network.nios.nios.WapiModule.connect')

# Generated at 2022-06-13 05:50:47.799573
# Unit test for function main
def test_main():
    from ansible.modules.network.ping import main
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible.module_utils import six

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    import json

    def patched_get_bin_path(name, opts=None, require_executable=True):
        return "/bin/%s" % name


# Generated at 2022-06-13 05:51:01.493115
# Unit test for function main
def test_main():
    # Mock the module arguments
    module_args = dict()
    module_args.update(dict(
        data=['pong'],
        ansible_check_mode=['yes'],
    ))

    # Instantiate the module object
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Run the main function
    main()

# Generated at 2022-06-13 05:51:07.041797
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert main() == {
        'ping': 'pong'
    }

# Generated at 2022-06-13 05:51:11.950651
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        import ansible
        ansible.builtin.ping.main()
        assert mock_module.return_value.supports_check_mode.called
        assert mock_module.return_value.argument_spec.called
        assert mock_module.return_value.params.called
        assert mock_module.return_value.exit_json.called

# Generated at 2022-06-13 05:51:13.305462
# Unit test for function main
def test_main():
    import json
    print(json.loads(main()))
    return

# Generated at 2022-06-13 05:51:23.551701
# Unit test for function main
def test_main():

    # example of skipping test on a particular platform, only works with nosetests (not pytest)
    #@unittest.skipIf("Darwin" in platform.system(),"Skipping due to OS")
    def test_ping_return(self):

        from ansible.module_utils.basic import AnsibleModule

        # Store the original module args so that we can restore them in teardown
        orig_module_args = self.mock_module_args

        # Example of mocking module args
        self.mock_module_args = dict((k, v) for k, v in orig_module_args.items())
        self.mock_module_args.update(dict(
            data='pong',
        ))
        set_module_args(self.mock_module_args)

# Generated at 2022-06-13 05:51:35.117346
# Unit test for function main
def test_main():
    import pytest

    from ansible_collections.ansible.builtin.plugins.modules.ping import main

    # Example: values returned when module executed normally
    result = dict(
        ping='pong',
    )
    result.update(dict(
        changed=False,
        invocation=dict(
            module_args=dict(
                data='pong',
            ),
        ),
    ))

    # Example: values returned when module raises an exception
    raised_exception = dict(
        msg="boom",
    )
    raised_exception.update(dict(
        exception=dict(
            msg="boom",
            type="Exception",
        ),
        rc=1,
    ))

    # Example: values returned when module executed normally
    module = dict(
        data='pong',
    )

   

# Generated at 2022-06-13 05:51:35.730880
# Unit test for function main
def test_main():
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:51:36.329047
# Unit test for function main
def test_main():
    print(main())
    assert main() is None

# Generated at 2022-06-13 05:51:38.388576
# Unit test for function main
def test_main():
    return_obj = main()
    assert return_obj['ping'] == 'pong'

# Generated at 2022-06-13 05:51:40.810414
# Unit test for function main
def test_main():
    ret = main()
    assert ret['ping'] == 'pong'

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-13 05:52:08.387425
# Unit test for function main
def test_main():
    from ansible_skip_for_jython import JythonVersion, skip_for_jython_unless_java_version, skip_for_jython, AnsibleModule
    import ansible.module_utils.basic as module_utils; module_utils.Basic._ANSIBLE_ARGS=['-m', 'ping', '-a', 'data=crash']
    assert module_utils.HAS_PYWIN32_MODULES is None, "Jython should not have found pywin32"
    assert module_utils.HAS_PYCRYPTO_MODULES is None, "Jython should not have found pycrypto"
    module_utils.Basic._ANSIBLE_ARGS=['-m', 'ping', '-a', 'data=crash']

# Generated at 2022-06-13 05:52:12.385509
# Unit test for function main
def test_main():
    args = [(None, "print('crash')", {'changed': False, 'failed': True, 'invocation': {'module_args': 'ping: None'}, 'module_stderr': '', 'module_stdout': 'Exception: boom', 'msg': 'MODULE FAILURE'})]
    for a in args:
        args = "{'data':a[1]}"
        k = main(args)
        assert k == a[2]

# Generated at 2022-06-13 05:52:13.746084
# Unit test for function main
def test_main():
    print(ping.main())
    print('\n')

# Generated at 2022-06-13 05:52:19.402129
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:52:22.978890
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    try:
        main()
    except Exception as exception:
        if module.params['data'] == 'crash':
            module.exit_json(**result)
        else:
            raise exception

# Generated at 2022-06-13 05:52:34.559341
# Unit test for function main
def test_main():
    import json

    data = dict(
        ANSIBLE_MODULE_ARGS=dict(
            data='pong',
        ),
    )
    print('Data::', data)
    data = json.dumps(data)
    # ansible-playbook --syntax-check test_ping.yml -e '{"ANSIBLE_MODULE_ARGS": {"data": "pong"}}'
    rc, out, err = module.run_command('{0} {1}'.format(sys.executable, __file__), data=data)
    print('OUTPUT::', out)
    print('ERROR::', err)
    print('RC::', rc)

# Generated at 2022-06-13 05:52:38.249648
# Unit test for function main
def test_main():
    test_data = {'data': 'ping'}
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if test_data['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=test_data['data'],
    )

    module.exit_json(**result)

test_main()

# Generated at 2022-06-13 05:52:45.179923
# Unit test for function main
def test_main():
    p1 = dict(data="pong")
    p2 = dict(data="crash")
    p3 = dict(data="farce")
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    module.params = p1
    main()
    assert module.exit_json.call_args[1]['ping'] == 'pong'
    module.params = p2
    main()
    assert module.fail_json.call_args[1]['msg'] == 'boom'
    assert module.fail_json.call_sargs[1]['exception'] == Exception
    module.params['data'] = p3
    main()
    assert module.exit_json.call_args[1]['ping'] == 'farce'

# Generated at 2022-06-13 05:52:53.665696
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # From Ansible 2.9 onwards,
    # AnsibleModuleStub.exit_json is a function returning a function.
    # It makes a function which takes the args and kwargs
    # and calls the actual exit_json method with them.
    module_exit_json = test_module.exit_json
    # Create a function to mock the original exit function
    # which exits the control flow of the program by throwing an error
    def mock_exit_json(outputs):
        raise Exception('exit_json called')
    # Replace the exit_json method with our mock exit json method
    test_module.exit_json = mock_exit_

# Generated at 2022-06-13 05:52:54.276447
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:53:30.629267
# Unit test for function main
def test_main():
    import ansible.module_utils.basic as basic
    am = basic.AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    am.exit_json(**main())

# Generated at 2022-06-13 05:53:35.224854
# Unit test for function main
def test_main():
    M = AnsibleModule(
        argument_spec = dict(
            data = dict(type = 'str', default = 'pong'),
        ),
        supports_check_mode = True
    )
    # No exception raised
    assert M.params['data'] == 'pong'

# Generated at 2022-06-13 05:53:39.737963
# Unit test for function main
def test_main():
    # Function definition for test case for main function
    def test_ansible_module_main(mocker):
        request_mock = mocker.patch("module_utils.basic.AnsibleModule")
        request_instance = request_mock.return_value
        request_instance.params = {'data': 'pong'}
        request_instance.exit_json.return_value = None
        main()
        assert request_instance.exit_json.called

    test_ansible_module_main(mocker=mocker)

# Generated at 2022-06-13 05:53:44.729608
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

# Generated at 2022-06-13 05:53:45.876374
# Unit test for function main
def test_main():
    # Do nothing.
    pass

# Generated at 2022-06-13 05:53:52.481743
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True,
        skip_cases=['crash']
    )

    try:
        result = module.execute_main()
    except Exception as e:
        print(e)
        raise

    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:53:55.914211
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    data = 'pong'
    expected_result = dict(
        ping=data,
    )
    result = module.exit_json(**expected_result)
    assert data in result['ping']

# Generated at 2022-06-13 05:53:57.109531
# Unit test for function main
def test_main():
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:54:05.758210
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common as ansible_module_utils

    def execute_module(**kwargs):
        # function is called when running the module for testing
        # and it returns the module as an object with all the parameters
        module=AnsibleModule(**kwargs)
        main()
        return module

    # function calls the main function
    with pytest.raises(Exception) as exception:
        execute_module(data='crash')
    assert exception.value.args[0] == "boom"
    # test with other parameters
    result = execute_module(data='ping')
    assert result.params['data'] == 'ping'
    # or:
    assert result.params['data'] == result.result['ping']


# Generated at 2022-06-13 05:54:11.777945
# Unit test for function main
def test_main():
    '''
    Test that data = "crash" causes an error and that data != "crash" passes
    Result is True if the function exits with a status of 0
    '''
    # Crash
    test = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    test_result = not test.exit_json(changed=False, meta=dict(ping='crash'))
    assert test_result == True

    # Pong
    test = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

# Generated at 2022-06-13 05:55:38.477293
# Unit test for function main
def test_main():
    moduleArgs = {'data': 'crash'}
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    module.params = moduleArgs
    assert not main()

# Generated at 2022-06-13 05:55:43.249289
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

# Generated at 2022-06-13 05:55:45.632906
# Unit test for function main
def test_main():
    # Nothing to test, because the usage of the module is really trivial.
    pass

# Generated at 2022-06-13 05:55:50.014769
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == None


# Generated at 2022-06-13 05:56:00.288020
# Unit test for function main
def test_main():
    cmdline = [
        'ansible', '-m', 'ping', 'hostname'
    ]
    args = AnsibleModule(argument_spec={}).parse(cmdline[3:])
    assert args["ANSIBLE_MODULE_PATH"] == "ping"
    assert args["ANSIBLE_MODULE_NAME"] == "ping"
    assert args["ANSIBLE_CONFIG"] == "/etc/ansible/ansible.cfg"
    assert args["ANSIBLE_LIBRARY"] == "/usr/share/ansible"
    assert args["ANSIBLE_MODULE_ARGS"] == "data=pong"
    assert args["ANSIBLE_STDOUT_CALLBACK"] == "default"
    assert args["ANSIBLE_MODULE_UTILS"] == "/usr/share/ansible/module_utils"

# Generated at 2022-06-13 05:56:10.702292
# Unit test for function main
def test_main():
    import sys
    import os
    orig_sys_argv = sys.argv
    orig_wd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'library', 'plugins'))
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'library'))
    import json
    import pytest
    # Create a fake test_module
    module_args = {'data': 'pong'}
    check_mode = False
    test_module = AnsibleModule(argument_spec=dict(),
                                supports_check_mode=check_mode,
                                )
    test

# Generated at 2022-06-13 05:56:15.172361
# Unit test for function main
def test_main():
  # Test with data set to 'crash'
  data = {'data': 'crash'}
  with pytest.raises(Exception):
    main()
  # Test with data set to a non-default value
  data = {'data': 'foo'}
  result = main()
  assert result == {'changed': False, 'ping': 'foo'}
  # Test with data set to default value
  data = {}
  result = main()

# Generated at 2022-06-13 05:56:24.345789
# Unit test for function main
def test_main():
    import json

    # Mock out AnsibleModule
    original_module = AnsibleModule
    class AnsibleModuleMock:
        def __init__(self, argument_spec, supports_check_mode):
            self.params = dict()
            self.exit_json = dict()
        def exit_json(self, **kwargs):
            self.exit_json = kwargs
    AnsibleModule = AnsibleModuleMock

    # Generate test data to make sure that the logic is correct

# Generated at 2022-06-13 05:56:27.313440
# Unit test for function main
def test_main():
    m = AnsibleModule(dict(data=dict(default='pong', type='str')))
    r = main()
    assert r['ping'] == 'pong'

# Generated at 2022-06-13 05:56:29.625520
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    mock_module = AnsibleModule
    mock_module.params = {
        'data': 'pong'
    }
    ping.main()