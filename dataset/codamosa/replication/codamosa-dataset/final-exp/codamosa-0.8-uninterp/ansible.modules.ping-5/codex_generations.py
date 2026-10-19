

# Generated at 2022-06-13 05:49:00.154584
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-13 05:49:00.884236
# Unit test for function main
def test_main():
  assert main()

# Generated at 2022-06-13 05:49:08.565968
# Unit test for function main
def test_main():
    # Mocking modules
    import modules.ping as ping
    if False:
        from ansible.module_utils.basic import AnsibleModule
        AnsibleModule = AnsibleModule

        def _exit_json(ping, **kwargs):
            print('exit_json:')
            print(kwargs)

        def _fail_json(msg, **kwargs):
            print('fail_json: {0}'.format(msg))
            print(kwargs)

        setattr(AnsibleModule, 'exit_json', lambda x, y: _exit_json(**y))
        setattr(AnsibleModule, 'fail_json', lambda x, y: _fail_json(y))


# Generated at 2022-06-13 05:49:15.532083
# Unit test for function main
def test_main():
    global_data = [
        "pong"
        ]
    class AnsibleModule:
        global_data = None
        def __init__(self, global_data):
            self.global_data = global_data
    class Exception:
        def __init__(self, global_data):
            self.global_data = global_data
    class MockModule:
        params = global_data
    ansible_module = AnsibleModule(MockModule())
    main()
    assert global_data == ["pong"]

# Generated at 2022-06-13 05:49:18.319576
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    main()

# Generated at 2022-06-13 05:49:29.886748
# Unit test for function main
def test_main():
    # description field is not supported
    # args field is not supported
    # check_mode field is not supported
    # diff field is not supported
    # no_log field is not supported.
    # Will create a test module with 3 parameters and pass data=pong to it.
    testmod = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    # args changed to params
    testmod.params = {'data': 'pong'}
    # result changed to actual
    actual = test_main()
    # We expect the main function to return these values
    expected = dict(
        ping='pong',
    )
    assert actual == expected, "Error"



# Generated at 2022-06-13 05:49:33.253978
# Unit test for function main
def test_main():
  args = dict(
    data = "test"
  )
  check = dict(
    ping = "test"
  )
  with patch.object(AnsibleModule, 'exit_json') as mock_exit_json:
    main()
    mock_exit_json.asert_called_once_with(**check)


# Generated at 2022-06-13 05:49:36.644148
# Unit test for function main
def test_main():
    testobj = dict(
        data=dict(type='str', default='pong'),
    )
    assert main(testobj) == dict(
        ping=testobj['data']
    )

# Generated at 2022-06-13 05:49:40.665295
# Unit test for function main
def test_main():
    # Unit test to test function main.
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    if module.params['data'] == 'crash':
        raise Exception('boom')
    result = dict(ping=module.params['data'])
    module.exit_json(**result)

# Generated at 2022-06-13 05:49:45.415807
# Unit test for function main
def test_main():
    module = mock.MagicMock()
    module.exit_json = exit_json
    module.params = dict(data='pong')

    p = os.path
    try:
        main()
        assert mock_exit_json.called
    finally:
        os.path = p

# Generated at 2022-06-13 05:49:52.392748
# Unit test for function main
def test_main():
    result = main()
    assert result == {
      "changed": False,
      "ping": "pong"
    }


# Generated at 2022-06-13 05:49:58.243553
# Unit test for function main
def test_main():
    data = "{\"ping\": \"pong\"}"

    sys.path.append(os.path.dirname(__file__))
    import ping
    current_dir = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    module = imp.load_source('ping', 'ping')
    sys.modules['ansible.module_utils.basic'] = imp.load_source('ansible.module_utils.basic', '../module_utils/basic')
    sys.modules['ansible.module_utils.action'] = imp.load_source('ansible.module_utils.action', '../module_utils/action')
    sys.modules['ansible.module_utils.connection'] = imp.load_source('ansible.module_utils.connection', '../module_utils/connection')
   

# Generated at 2022-06-13 05:50:03.609567
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

# Generated at 2022-06-13 05:50:09.222086
# Unit test for function main
def test_main():
    args = ['--data=boh']
    with patch.object(AnsibleModule, 'exit_json') as mock_exit_json:
        main()
        mock_exit_json.assert_called_once_with(**{'ping': 'boh'})
    with patch.object(AnsibleModule, 'fail_json') as mock_exit_json:
        args = ['--data=crash']
        main()
        mock_exit_json.assert_called_once_with(msg='boom')

# Generated at 2022-06-13 05:50:10.781529
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:50:14.604459
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == dict(ping='pong')

# Generated at 2022-06-13 05:50:19.969365
# Unit test for function main
def test_main():
    args = dict(
        data = 'pong',
    )

    # set up needed objects
    module = AnsibleModule(argument_spec=args)
    module.params['data'] = 'pong'

    # check if exit_json is called
    main()

    # check if there are exit_json and fail_json calls
    assert True

# Generated at 2022-06-13 05:50:27.481417
# Unit test for function main
def test_main():

    test_arguments = dict(
        data='pong',
    )
    expected_results = dict(
        ping='pong',
    )
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule

    def AnsibleModule_run_result():
        class AnsibleExitJson(Exception):
            def __init__(self, **kwargs):
                self.kwargs = kwargs
                Exception.__init__(self)

        def exit_json(*args, **kwargs):
            if 'changed' not in kwargs:
                kwargs['changed'] = False
            raise AnsibleExitJson(**kwargs)

        class AnsibleFailJson(Exception):
            def __init__(self, **kwargs):
                self.kwargs = kwargs

# Generated at 2022-06-13 05:50:34.498923
# Unit test for function main
def test_main():
    mock_module = Mock()
    # Shouldn't reach here
    mock_module.params = {'data': 'pong'}
    main()

    # Shouldn't reach here
    mock_module.params = {'data': 'crash'}
    try:
        main()
    except:
        print('Test case passed')

mock_module = Mock()
mock_module.params={"data":"pong"}
main()

# Generated at 2022-06-13 05:50:41.430336
# Unit test for function main
def test_main():
    args = dict(data='crash')
    result = dict(failed=True, msg='boom', rc=1, stderr='boom', stdout='')
    with pytest.raises(SystemExit):
        with patch('ansible.module_utils.basic.AnsibleModule',
                   return_value=AnsibleModule):
            main()

# Generated at 2022-06-13 05:50:55.620574
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

# Generated at 2022-06-13 05:50:57.343347
# Unit test for function main
def test_main():
    args = dict(data='pong')
    result = dict(ping='pong')
    assert main(args) == result

# Generated at 2022-06-13 05:51:04.799758
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

# Generated at 2022-06-13 05:51:08.048395
# Unit test for function main
def test_main():
    """
    Test for the main function.
    """
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == module.exit_json()
    assert main() == AnsibleModule.exit_json()

# Generated at 2022-06-13 05:51:12.781765
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

    assert(result == dict(ping=module.params.get('data')))

# Generated at 2022-06-13 05:51:19.374182
# Unit test for function main
def test_main():
    args = {"data":"crash"}

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    m = AnsibleModule(**args)
    with pytest.raises(Exception) as excinfo:
        main()
    assert 'boom' in str(excinfo.value)


# Generated at 2022-06-13 05:51:21.515634
# Unit test for function main
def test_main():
    assert callable(main)


# Generated at 2022-06-13 05:51:26.383211
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

# Generated at 2022-06-13 05:51:30.151115
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main(test_module) == None

# Generated at 2022-06-13 05:51:33.989747
# Unit test for function main
def test_main():
    module_args={'data': 'pong'}
    module = AnsibleModule(argument_spec={})
    result = main(module, module_args)
    assert result['changed'] == True
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:51:53.112434
# Unit test for function main
def test_main():
    result = dict()
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


# Generated at 2022-06-13 05:51:54.571066
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        print(e)
        assert False
    assert True

# Generated at 2022-06-13 05:51:56.306418
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        print("Error: main() is failed")
 

# Generated at 2022-06-13 05:51:58.729970
# Unit test for function main
def test_main():
    testmod = AnsibleModule({}, {}, {})
    assert main() == {'changed': False, 'ping': 'pong'}


# Generated at 2022-06-13 05:52:07.596348
# Unit test for function main
def test_main():
    test_args = {'data': 'foobar'}
    test_exit_json = {'ping': 'foobar'}
    test_fail_json = {}

    def test_exit_json(*args):
        assert args[0] == test_exit_json

    def test_fail_json(*args):
        assert args[0] == test_fail_json

    # Patch the exit json functions
    builtins.exit_json = test_exit_json
    builtins.fail_json = test_fail_json

    # Run the unit test
    main(test_args)

# Generated at 2022-06-13 05:52:09.838130
# Unit test for function main
def test_main():
    args = dict(
        data='Test data'
    )
    r = main(args)
    assert r ==  {'ping': 'Test data'}


# Generated at 2022-06-13 05:52:15.314418
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule({'data': 'pong'})
    mod.exit_json = lambda x: x
    try:
        mod.main()
    except SystemExit as e:
        if e.args[0] == 0:
            exit(0)
        else:
            exit(1)


# Generated at 2022-06-13 05:52:20.215029
# Unit test for function main
def test_main():
    # Import delete_all
    from ansible.modules.cloud.amazon.ping import main

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

# Generated at 2022-06-13 05:52:27.287950
# Unit test for function main
def test_main():
    # AnsibleModule mock object
    module = AnsibleModule(
        argument_spec={
            'data': dict(type='str', default='pong'),
        },
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)



# Generated at 2022-06-13 05:52:34.499663
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec = dict(
            data = dict(type = 'str', default = 'pong'),
        ),
        supports_check_mode = True,
    )

    if module.params['data'] == 'crash':
        raise Exception("boom")

    result = dict(
        ping = module.params['data'],
    )

    module.exit_json(**result)


# Generated at 2022-06-13 05:53:17.116911
# Unit test for function main
def test_main():

    # Mock module_utils.basic.AnsibleModule, for the module to call before exiting
    class AnsibleModuleMock:
        def __init__(self, argspec, **kwargs):
            pass
        def exit_json(self, **kwargs):
            pass

    # Mock module_utils.basic.AnsibleModule, to receive the return values of main
    class AnsibleModuleMockReturn:
        def __init__(self, argspec, **kwargs):
            pass
        def exit_json(self, **kwargs):
            pass

    # Patch AnsibleModule (object returned by module_utils.basic.AnsibleModule)
    # to make the module exit with given return value
    # and exit_json method to check the value passed to exit_json

# Generated at 2022-06-13 05:53:22.466581
# Unit test for function main
def test_main():
    # Check dictionary is returned
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert isinstance(main(module), dict)
    
    # Check dictionary structure is correct
    assert main(module).has_key('ping')
    assert isinstance(main(module)['ping'], str)

# Generated at 2022-06-13 05:53:28.018903
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

    assert result == {'ping': 'pong'}

# Generated at 2022-06-13 05:53:29.750063
# Unit test for function main
def test_main():
    '''
    Unit test for function main
    '''
    main()

# Generated at 2022-06-13 05:53:34.556428
# Unit test for function main
def test_main():

    # create the AnsibleModule object
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # call main and see if it crashes
    main()

# Generated at 2022-06-13 05:53:35.200124
# Unit test for function main
def test_main():
    # Implement test function for function main
    pass

# Generated at 2022-06-13 05:53:39.169619
# Unit test for function main
def test_main():
    mock_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    mock_module.params = dict(data='pong')
    main()
    assert mock_module.exit_json.called, 'function should have called exit_json()'
    assert mock_module.exit_json.call_count == 1, 'function should\'ve called exit_json() once'



# Generated at 2022-06-13 05:53:42.064763
# Unit test for function main
def test_main():
    obj = {
        'data': 'pong',
    }
    try:
        main()
    except Exception as e:
        assert False, "Exception calling module main {}".format(e)

# Generated at 2022-06-13 05:53:49.289039
# Unit test for function main
def test_main():
    argv = ['ansible', 'ping']
    argv.append('--connection-local')
    argv.append('--data=crash')
    with open('/dev/null', 'w') as f:
        origstdout = sys.stdout
        sys.stdout = f
        try:
            main()
        except Exception as e:
            print("Exception:", e)
            pass
        sys.stdout = origstdout

# Generated at 2022-06-13 05:53:49.872102
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:55:13.867603
# Unit test for function main
def test_main():
    # first with pong
    assert main() == dict(ping='pong')
    # now with crash
    assert main(data='crash') == dict(ping='crash')
    # now with crash and check_mode
    assert main(data='crash', check_mode=True) == dict(ping='crash', check_mode=True, diff_mode=False)
    # now with pong, check_mode and diff_mode
    assert main(data='pong', check_mode=True, diff_mode=True) == dict(ping='pong', check_mode=True, diff_mode=True)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:55:16.931403
# Unit test for function main
def test_main():
    args = {'data': 'pong'}
    res = main(args)
    assert res == {'ping': 'pong'}


# Generated at 2022-06-13 05:55:24.287987
# Unit test for function main
def test_main():
    args = []
    kwargs = dict(
        data='pong',
    )

    ansible_module_for_test = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    result = dict(
        ping=kwargs['data'],
    )

    ansible_module_for_test.exit_json(ansible_facts=result)

# Generated at 2022-06-13 05:55:27.097301
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:55:32.477577
# Unit test for function main
def test_main():
    argument_spec = dict(
        data=dict(type='str', default='pong'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:55:40.096891
# Unit test for function main
def test_main():
    # get valid parameters
    test_params = {'data': 'pong'}
    # create a valid Ansible module
    module = AnsibleModule(argument_spec=dict(
        data=dict(type='str', default='pong'),
    ), supports_check_mode=True)
    # set module parameters
    module.params = test_params
    # run function under test
    main()
    # check output result
    assert module.exit_json == {'ping': 'pong'}

# Generated at 2022-06-13 05:55:46.085777
# Unit test for function main
def test_main():
    args = dict( data="test" )

    rpc_exec = dict(
        methods=dict(
            run_command=dict(
                args=dict(
                    command=["ls"],
                    in_data="",
                    binary=False,
                    socket_path="/var/tmp/openssh-ansible-test.sock",
                    run_as=None,
                    metadata={},
                    input_data=None
                ),
                success=True
            )
        )
    )

    from openssh_runner import OpensshRunner
    t = OpensshRunner(**rpc_exec)
    t.run_command(**args)

# Generated at 2022-06-13 05:55:52.159459
# Unit test for function main
def test_main():
    AnsibleModule.exit_json = lambda self, **kwargs: kwargs
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == dict(
        ping=module.params['data'],
    )

# Generated at 2022-06-13 05:55:57.406613
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert main() == 0

# vim: ai et ts=4 sts=4 sw=4 ft=python

# Generated at 2022-06-13 05:56:08.891537
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    # Dummy module for unit testing
    class DummyModule(object):
        def __init__(self):
            self.params = dict()
            self.check_mode = False
            self.exit_json = ansible.module_utils.basic._ANSIBLE_ARGS['exit_json']
            self.fail_json = ansible.module_utils.basic._ANSIBLE_ARGS['fail_json']
    # Dummy test case for unit testing
    class DummyTestCase(object):
        def __init__(self, test_name):
            self.test_name = test_name
            self.assert_called_with = dict()
    ansible.module_utils.basic._ANSIBLE_ARGS = dict()
    ansible.module_utils.basic._ANSIBLE_ARGS