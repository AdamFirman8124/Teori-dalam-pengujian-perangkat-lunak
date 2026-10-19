

# Generated at 2022-06-13 05:49:06.274501
# Unit test for function main
def test_main():
    args = dict(
        data="unit test"
    )

    result = dict(
        ping="unit test",
        changed=0,
        failed=0
    )

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.params = args
    _result = main()
    assert _result['ping'] == result['ping']
    assert _result['changed'] == result['changed']
    assert _result['failed'] == result['failed']

# Generated at 2022-06-13 05:49:09.126808
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.community.plugins.modules.ping.AnsibleModule'):
        ansible_collections.ansible.community.plugins.modules.ping.main()


# Generated at 2022-06-13 05:49:09.625074
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:49:13.642022
# Unit test for function main
def test_main():
    #Test output of main() with no params set
    result = main()
    assert result['ping'] == 'pong'
    #Test output of main() with params set
    result = main(data="boom")
    assert result['ping'] == 'boom'

# Generated at 2022-06-13 05:49:20.418184
# Unit test for function main
def test_main():
    # load the module
    m = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    m.exit_json = Mock()
    m.exit_json.return_value = None
    # call the function
    main()
    # test the results
    assert m.exit_json.called
    args, kwargs = m.exit_json.call_args
    assert not kwargs
    assert args[0]['ping'] == 'pong'

# Generated at 2022-06-13 05:49:31.702488
# Unit test for function main
def test_main():
    """
    Unit test for main
    """
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    # Test case where data == 'crash'
    module.params['data'] = 'crash'
    result = dict(
        ping=module.params['data'],
    )
    if result['ping'] == 'crash':
        raise Exception("boom")
    else:
        module.exit_json(**result)
    # Test case where data == 'pong'
    module.params['data'] = 'pong'
    result = dict(
        ping=module.params['data'],
    )

# Generated at 2022-06-13 05:49:32.493800
# Unit test for function main
def test_main():
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:49:39.735211
# Unit test for function main
def test_main():

    # Mock up an AnsibleModule object
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Mock up an object to use for the AnsibleModule's exit_json()
    result = {
        'ping': 'pong'
    }

    # Call the main function
    main()

    # Make sure we called exit_json() with the result dictionary we created
    module.exit_json.assert_called_with(**result)

# Generated at 2022-06-13 05:49:42.498785
# Unit test for function main
def test_main():
    test_args = {'data': 'crash'}
    with pytest.raises(Exception):
        assert main(test_args) == "boom"

# Generated at 2022-06-13 05:49:45.371874
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:49:55.445593
# Unit test for function main
def test_main():
    # Fixture for the call to the main function
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    # Call to the main function
    main()

    # Assertions
    assert True

# Generated at 2022-06-13 05:49:58.907887
# Unit test for function main
def test_main():
    def f():
        raise Exception("boom")
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.exit_json = f
    main()

# Generated at 2022-06-13 05:49:59.853897
# Unit test for function main
def test_main():
    resp = main()
    assert type(resp) == dict

# Generated at 2022-06-13 05:50:04.098319
# Unit test for function main
def test_main():
    args = dict(
        data='pong'
    )
    result = main()
    assert result == dict(
        ping='pong',
    )
    assert result == dict(
        ping='pong',
    )
    assert result == dict(
        ping='pong',
    )

# Generated at 2022-06-13 05:50:05.147010
# Unit test for function main
def test_main():
    assert True
#

# Generated at 2022-06-13 05:50:08.927726
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_ping
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert ansible.module_ping.main() == 0

# Generated at 2022-06-13 05:50:20.684236
# Unit test for function main
def test_main():

    # Unit tests are run in a separate virtual Python interpreter that
    # has ansible-base installed and can import all ansible_collections.ansible
    # and other modules that are needed by Ansible.

    # Import test module for the ping module
    import ansible_collections.ansible.builtin.tests.ping as ping

    # Set up the argument spec to mimic what the AnsibleModule() would have
    # received
    argument_spec = dict(
        data=dict(type='str', default='pong'),
    )

    # Test with no exception
    result = ping.main(argument_spec)
    assert result['ping'] == 'pong'
    assert result['changed'] == False
    assert result['invocation'] == {}
    assert result['ctime']

    # Test with exception

# Generated at 2022-06-13 05:50:24.761330
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    module.exit_json = lambda **kwargs: kwargs
    module.fail_json = lambda **kwargs: kwargs
    module.params = dict(data='crash')
    try:
        main()
    except:
        pass
    assert module.exception

# Generated at 2022-06-13 05:50:35.972867
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import mock
    from io import StringIO
    from ansible.utils.display import Display
    from ansible.plugins.action.ping import main

    display = Display()
    display.verbosity = 3

    module_args = dict()
    test_cases = [
        # test_case[0] => module_args
        # test_case[1] => expected_returned_result
        # test_case[2] => expected_output_result
        # test_case[3] => expected_exception
        (dict(data='test'),
         dict(ping='test'),
         None,
         None),
        (dict(data='crash'),
         None,
         None,
         Exception('boom')),
    ]


# Generated at 2022-06-13 05:50:36.864088
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:50:45.464191
# Unit test for function main
def test_main():
	pass


# Generated at 2022-06-13 05:50:57.625931
# Unit test for function main
def test_main():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    import pytest

    return_args = dict(
        changed=False,
        failed=False,
        ping='pong',
    )

    os_path_exists_path = 'ansible.builtin.ping.os.path.exists'
    os_mkdir_path = 'ansible.builtin.ping.os.mkdir'

    # Test 1 - Normal successful run
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        with mock.patch(os_path_exists_path) as mock_exists:
            with mock.patch(os_mkdir_path) as mock_mkdir:
                mock_exists.return_

# Generated at 2022-06-13 05:51:06.211415
# Unit test for function main
def test_main():
    # Module argument specs
    argument_spec = dict(
        data=dict(type='str', default='pong'),
    )
    # Instantiate module
    module = AnsibleModule(argument_spec=argument_spec)
    # If data equals to 'crash', raise exception
    if module.params['data'] == 'crash':
        raise Exception("boom")
    # Set ping to value of data parameter
    result = dict(ping=module.params['data'])
    # Set _ansible_result_callback to True
    module.params['_ansible_result_callback'] = True
    # Create actual result
    actual_result = module.exit_json(**result)
    # Set expected_result

# Generated at 2022-06-13 05:51:07.698707
# Unit test for function main
def test_main():
    """
    Here is where you prepare the test fixture
    """
    main()


# Generated at 2022-06-13 05:51:10.635347
# Unit test for function main
def test_main():
    assert ansible_ping({'data':'pong'}) == {'ping': 'pong'}

# Generated at 2022-06-13 05:51:11.223077
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:51:15.369500
# Unit test for function main
def test_main():
    # Mock class
    class mock_AnsibleModule():
        def __init__(self):
            self.params = {'data': 'pong'}

        def exit_json(self, **result):
            module.exit_json(**result)

    module = mock_AnsibleModule()
    main()



# Generated at 2022-06-13 05:51:15.920697
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:51:20.309822
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert module.params['data'] == 'pong'

# Generated at 2022-06-13 05:51:22.806494
# Unit test for function main
def test_main():
    import pytest
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:51:39.159491
# Unit test for function main
def test_main():
    # This is just a dummy unit test
    main()

# Generated at 2022-06-13 05:51:46.745946
# Unit test for function main
def test_main():
    target = dict()

    # Check expected input and response
    result = dict(ansible_facts=dict(ping='pong'))
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    module.exit_json(**result)

    # Check for exception when data is crash
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='crash')), supports_check_mode=True)
    with pytest.raises(Exception):
        main()

# Generated at 2022-06-13 05:51:56.413021
# Unit test for function main
def test_main():
    from ansible.modules.network.nxos import ping
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    m = basic.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert ping.main() == m.exit_json(ping='pong')
    assert ping.main() == m.exit_json(
        ping='pong',
        ansible_facts={
            'discovered_interpreter_python': '/usr/bin/python'
        }
    )

# Generated at 2022-06-13 05:52:04.248481
# Unit test for function main
def test_main():
    data = dict(
        data='pong',
    )

    module_args = dict(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    result = dict(
        ping=data['data'],
    )

    module = AnsibleModule(**module_args)

    assert module.exit_json(**result) == None


# Generated at 2022-06-13 05:52:13.516428
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.builtin.plugins.modules.ping.AnsibleModule') as mock_module:
        with patch('ansible_collections.ansible.builtin.plugins.modules.ping.AnsibleModule.exit_json') as mock_exit_json:
            mock_module().params = {'data': 'pong'}
            main()
            mock_exit_json.assert_called_once_with(ping='pong')
        with pytest.raises(Exception):
            mock_module().params = {'data': 'crash'}
            main()


# Test for documentation example 3

# Generated at 2022-06-13 05:52:18.638725
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == dict(
        ping=module.params['data'],
    )

# Generated at 2022-06-13 05:52:21.117461
# Unit test for function main
def test_main():
    args = dict(
        data='pong',
    )
    with pytest.raises(AnsibleExitJson):
        main(tempfile.TemporaryFile(), args)

# Generated at 2022-06-13 05:52:27.875271
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

# Generated at 2022-06-13 05:52:32.601053
# Unit test for function main
def test_main():
  module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

  #Test that this function returns the proper value for data
  assert main(module) == 'pong'

# Generated at 2022-06-13 05:52:33.223785
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:53:08.327079
# Unit test for function main
def test_main():
    args = dict(
        data="pong"
    )

    set_module_args(args)
    result = main()
    assert result['changed'] == False

# Generated at 2022-06-13 05:53:14.272611
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result_args = dict(
        ping='pong'
    )
    #resp = main()
    #assert resp == result_args

# Generated at 2022-06-13 05:53:14.772202
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:53:15.529568
# Unit test for function main
def test_main():
    add = main()
    assert add == None

# Generated at 2022-06-13 05:53:16.582202
# Unit test for function main
def test_main():
    test_program = Main()
    test_program.ping("hello")

# Generated at 2022-06-13 05:53:18.100505
# Unit test for function main
def test_main():
    try:
        assert main() == "pong"
    except Exception as e:
        assert "boom" in e.message

# Generated at 2022-06-13 05:53:18.632561
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:53:21.750158
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

# Generated at 2022-06-13 05:53:22.728796
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:53:26.720185
# Unit test for function main
def test_main():
    module = AnsibleModule(
            argument_spec=dict(
                data=dict(type='str', default='pong'),
            ),
            supports_check_mode=True
        )

    import pytest
    pytest.main(args=['-q', __file__])

# Generated at 2022-06-13 05:54:38.898871
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        raise

    result = dict(
        ping=module.params['data'],
    )

    module.exit_json(**result)


# Generated at 2022-06-13 05:54:39.804996
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:54:48.129625
# Unit test for function main
def test_main():
    action = 'ping'
    params = {'data': 'pong'}
    ansible_facts = {'ansible_check_mode': 'True', 'ansible_diff_mode': 'False'}
    module = AnsibleModule(action=action, params=params, supports_check_mode=True)

    result = dict(
        ping=params['data'],
    )

    module.exit_json(**result)

# Generated at 2022-06-13 05:54:57.665777
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    import pytest

    test_cases = [
        # test arguments
        {
           "data": "crash"
        }
    ]

    @pytest.mark.parametrize("data", test_cases)
    def test_main_param(mocker, data):
        m = mocker.patch('ansible.module_utils.basic.AnsibleModule')
        mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS',
                     new_callable=lambda: [
                         'ansible-inventory',
                         '--version', str(ansible_version),
                     ])
        args = data

# Generated at 2022-06-13 05:55:00.278752
# Unit test for function main
def test_main():
    pytest;
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    if module.params['data'] == 'crash':
        raise Exception("boom")

# Generated at 2022-06-13 05:55:02.397307
# Unit test for function main
def test_main():
    module = AnsibleModule(dict(data='pong'))
    assert main() == dict(data='pong')


# Generated at 2022-06-13 05:55:02.931416
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:55:08.240179
# Unit test for function main
def test_main():
    import os
    import sys

    def assertEqual(a, b):
        assert a == b

    fake_args = {'ANSIBLE_MODULE_ARGS': {'data': 'pong'}}
    fake_args = dict()
    saved_sys_argv = sys.argv
    sys.argv = [os.path.basename(__file__)]
    try:
        main()
    finally:
        sys.argv = saved_sys_argv

# Generated at 2022-06-13 05:55:15.146585
# Unit test for function main
def test_main():
    import mock
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as am:
        module = am.return_value
        module.params = {'data': 'pong'}
        module.exit_json = lambda **kw: None
        main()
        assert module.exit_json.called
        assert module.exit_json.call_count == 1
        args, kwargs = module.exit_json.call_args
        assert args == tuple()
        assert kwargs == {'ping': 'pong'}
        assert module.supports_check_mode.called
        assert module.supports_check_mode.call_count == 1
        args, kwargs = module.supports_check_mode.call_args
        assert args == tuple()
        assert kwargs == {}




# Generated at 2022-06-13 05:55:19.845155
# Unit test for function main
def test_main():
    module = AnsibleModule(
            argument_spec=dict(
                    data=dict(type='str', default='pong'),
                ),
            supports_check_mode=True
        )
    assert module.params['data'] == 'pong'


# Generated at 2022-06-13 05:57:57.992677
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    import pytest
    import sys

    pm = AnsibleModule(
        argument_spec=dict(
            # data=dict(type='str', default='pong')
        ),
        supports_check_mode=True,
    )

    with pytest.raises(Exception) as excinfo:
        if pm.params['data'] == 'crash':
            raise Exception("boom")
        excinfo.match("boom")


    result = dict(
        ping=pm.params['data'],
    )

    pm.exit_json(result)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:58:03.346959
# Unit test for function main
def test_main():
    # Make the arguments that would be sent to the AnsibleModule
    arguments = dict(
        data='pong',
    )
    # Make an instance of the AnsibleModule mock class
    module = AnsibleModule(**arguments)
    # Create a mock for the Result class
    result = AnsibleModuleResult(dict(
        ping='pong',
    ))
    # Assign our mock result instance to a variable
    module.exit_json = result
    # Call the main function, which we've mocked out already
    main()

# Generated at 2022-06-13 05:58:05.929735
# Unit test for function main
def test_main():
    result = dict(
        ping='pong',
    )
    assert(main() == result)


# Generated at 2022-06-13 05:58:08.667206
# Unit test for function main
def test_main():
    mock = {
        'params': {'data': 'pong'}
    }
    main(mock)



# Generated at 2022-06-13 05:58:09.868396
# Unit test for function main
def test_main():
    assert(main() == 0)

# Generated at 2022-06-13 05:58:13.500056
# Unit test for function main
def test_main():

    # Test with no data = pong
    result = main()
    assert result == "pong"

    # Test with data = crash
    result = main()
    assert result == "crash"

# Generated at 2022-06-13 05:58:21.672308
# Unit test for function main
def test_main():
    # Copy of module_utils/connection.py
    class AnsibleModuleMock(object):
        class ArgumentSpec:
            pass

    class Exception(object):
        def __init__(self, message):
            self.message = message
            self.args = (None, message)

    def main():
        class ModuleExitJson(object):
            def __init__(self, **result):
                self.result = result
                self.exit_kwargs = result

            def exit_json(self, **kwargs):
                self.exit_kwargs = kwargs

        data = 'pong'
        module = AnsibleModuleMock()
        module.params = {}
        module.params['data'] = data
        module.exit_json = ModuleExitJson
        # Test raise Exception

# Generated at 2022-06-13 05:58:25.281400
# Unit test for function main
def test_main():
    ping_data = "pong"
    module_args = {}
    module_args.update({"data" : ping_data})
    module_args.update({"ansible_check_mode":True})
    result = main()
    assert result['success']
    assert result['ping'] == "pong"

# Generated at 2022-06-13 05:58:26.646641
# Unit test for function main
def test_main():
    assert (main() == 100)

# Generated at 2022-06-13 05:58:30.169324
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main() == module.exit_json(ping='pong')
