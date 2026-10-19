

# Generated at 2022-06-13 05:49:01.397962
# Unit test for function main
def test_main():
    mkdir_p(dirname(dirname(dirname(dirname(dirname(__file__))))))
    with redirect_stdout(stderr) as self.output:
        main()
    return self.output

# Generated at 2022-06-13 05:49:08.929853
# Unit test for function main
def test_main():
    import json
    import sys
    import platform

    class Args(object):
        pass

    args = Args()
    args.data = 'pong'

    class MockedException(Exception):
        pass

    class MockModule(object):
        def __init__(self):
            self.params = {'data': args.data}
            self.check_mode = False
            self.fail_json = None

        def exit_json(self, **kwargs):
            self.fail_json = kwargs

        def fail_json(self, **kwargs):
            raise MockedException(kwargs)

    class MockSystem(object):
        def __init__(self):
            self.prefix = '/usr/local'
            self.sys_prefix = '/usr/local'
            self.real_prefix = None

   

# Generated at 2022-06-13 05:49:18.938232
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.abc import Event
    from ansible.compat.mock import patch

    mock_module = patch.object(ansible.module_utils.basic, "AnsibleModule")
    mock_exit_json = patch.object(AnsibleModule, "exit_json")
    mock_fail_json = patch.object(AnsibleModule, "fail_json")

    main()

    assert mock_module.called
    assert mock_fail_json.called == False

    # Test that module.exit_json was called with no arguments
    assert mock_exit_json.called
    assert mock_exit_json.call_args == ((), dict(ping='pong'))


# Generated at 2022-06-13 05:49:24.733279
# Unit test for function main
def test_main():
    args = dict(
        data="pong"
    )
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
    pass

# Generated at 2022-06-13 05:49:25.895841
# Unit test for function main
def test_main():
    assert ping() == {'ping': 'pong'}

# Generated at 2022-06-13 05:49:29.170913
# Unit test for function main
def test_main():
    is_error, has_changed, result = main()
    assert not is_error
    assert not has_changed
    assert 'pong' in result
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:49:33.687269
# Unit test for function main
def test_main():
    module_name = "ansible.builtin.ping"

    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

    if module.params['data'] == 'crash':
        assert False
    
    hubby = {
        'ping':module.params['data']
    }
    module.exit_json(**hubby)


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:49:39.521853
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    args = []
    m = AnsibleModule
    try:
        main()
    except SystemExit:
        pass
    if m.params == None:
        print("Params not set")
    else:
        print(m.params)
    if m.params['data'] == 'crash':
        raise Exception("boom")
    result = dict(
        ping=m.params['data'],
    )
    m.exit_json(**result)

print(test_main())

# Generated at 2022-06-13 05:49:44.479850
# Unit test for function main
def test_main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True,
        bypass_checks=True
    )
    try:
        main()
    except Exception as e:
        raise Exception(e)

# Generated at 2022-06-13 05:49:46.366665
# Unit test for function main
def test_main():
    params = {'data': 'pong'}
    result = main(params)
    assert result['ping'] == 'pong'

# Generated at 2022-06-13 05:50:01.573957
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')))
    # The AnsibleModule object is a mock object.  It has a set of built-in
    # methods that mimic methods of the real AnsibleModule object.  This will
    # cause the main() function to execute normally and we can then test the
    # exit_json and fail_json methods.
    module.exit_json = lambda x: x
    module.fail_json = lambda x: x

    import sys
    saved_stdout = sys.stdout
    try:
        from StringIO import StringIO
        sys.stdout = mystdout = StringIO()
        main()
        result = mystdout.getvalue()
    finally:
        sys.stdout = saved_stdout

# Generated at 2022-06-13 05:50:06.622412
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(ping=1)
    module.exit_json(**result)

# Generated at 2022-06-13 05:50:11.047600
# Unit test for function main
def test_main():
    with pytest.raises(Exception) as excinfo:
        main()
    assert 'boom' in str(excinfo)

# Generated at 2022-06-13 05:50:13.589846
# Unit test for function main
def test_main():
    data = {'data': 'test'}
    result = {'ping': 'test'}
    assert main(data) == result

# Generated at 2022-06-13 05:50:15.038553
# Unit test for function main
def test_main():
    try:
        res = main()
    except Exception as e:
        pass



# Generated at 2022-06-13 05:50:23.704005
# Unit test for function main
def test_main():
    import mock
    import types

    import ansible.module_utils.basic as basic

    # Set up for our test
    module_args = dict(
        data=dict(type='str', default='pong'),
        supports_check_mode=True,
    )
    module = basic.AnsibleModule(argument_spec=module_args)
    module.params = dict(
        data = 'pong',
    )

    # Sanity check the result
    result = dict(
        ping='pong',
    )
    assert result == main()

    # Test exception handling
    Exception("boom")

    # Test that check_mode doesn't cause an exception
    module.params = dict(
        data = 'crash',
    )

# Generated at 2022-06-13 05:50:27.246219
# Unit test for function main
def test_main():
  # argument_spec, return_type, exit_json, parameters, module_name, sent_parameters, fail_json, exit_args
  # Expected output: {'msg': 'module crashed'}
  global module
  module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='crash'),
        ),
        supports_check_mode=True
    )
  
  if module.params['data'] == 'crash':
    raise Exception("boom")

  result = dict(
        ping=module.params['data'],
    )

  module.exit_json(**result)


# Generated at 2022-06-13 05:50:27.854993
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:50:32.454310
# Unit test for function main
def test_main():
    class Class:
        def __init__(self, value):
            self.value = value
        def __eq__(self, other):
            return other == self.value
    module = Class('{"data": "pong", "changed": false}')
    assert main(module) == True

# Generated at 2022-06-13 05:50:33.143108
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:50:59.245667
# Unit test for function main
def test_main():
    # Test simple case
    # Test: init module
    module_args = {
        "data": "pong"
    }
    module = AnsibleModule(argument_spec=module_args)
    module.exit_json = mock_return_value(
        {
            "ping": "pong"
        }
    )
    # call
    main()
    # test assert
    module.exit_json.assert_called_with(
        {
            "ping": "pong"
        }
    )

    # Test simple case
    # Test: init module
    module_args = {
        "data": "crash"
    }
    module = AnsibleModule(argument_spec=module_args)

# Generated at 2022-06-13 05:51:07.467689
# Unit test for function main
def test_main():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    builtins.__ansible_module__ = mock.Mock(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    builtins.module.params = {'data': 'pong'}
    assert main() == {'ping': 'pong'}

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    builtins.__ansible_module__ = mock.Mock(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )

# Generated at 2022-06-13 05:51:09.371985
# Unit test for function main
def test_main():
    result = main()
    assert result == dict(ping='pong')

# Generated at 2022-06-13 05:51:14.627159
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

# Generated at 2022-06-13 05:51:23.637588
# Unit test for function main
def test_main():
    args = dict(
        data=dict(type='str', default='pong'),
    )

    result = dict(
        ansible_facts=dict(
            ansible_system='Linux',
            ansible_system_vendor='Debian',
            ansible_system_version='10',
            ansible_pkg_mgr='apt',
            ansible_kernel='4.19.0-6-amd64',
            ansible_python=dict(
                executable='/usr/bin/python',
                version='3.7.3',
                version_info=dict(
                    major=3,
                    minor=7,
                    micro=3,
                    releaselevel='final',
                    serial=0
                )
            )
        )
    )


# Generated at 2022-06-13 05:51:24.122978
# Unit test for function main
def test_main():
    assert 0 == main()

# Generated at 2022-06-13 05:51:28.834809
# Unit test for function main
def test_main():
    data = dict(
        data=dict(type='str', default='pong'),
    )
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    assert main() is None

# Generated at 2022-06-13 05:51:31.731607
# Unit test for function main
def test_main():
    data = dict(
        data='pong'
    )
    AnsibleModule(data).fail_json.assert_called_once()

# Generated at 2022-06-13 05:51:38.603313
# Unit test for function main
def test_main():
    (ansible_module, ansible_return) = (0, 0)
    try:
        main()
    except SystemExit as e:
        if e.code != 0:
            ansible_module = 1
    except Exception as e:
        ansible_return = 1
    finally:
        os.close(os.open("/tmp/result", os.O_CREAT, 0o777))
        os.chmod("/tmp/result", 0o777)
        with open("/tmp/result", "w") as result:
            result.write("{0} {1}".format(ansible_module, ansible_return))
            result.close()

# Generated at 2022-06-13 05:51:42.901216
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    result = dict(
        ping=test_module.params['data'],
    )
    assert result

# Generated at 2022-06-13 05:52:23.061273
# Unit test for function main
def test_main():
    # Test correct arguments
    with pytest.raises(AnsibleExitJson) as result:
        main()
    assert result.value.args[0] == {"changed": False, "ping": "pong"}

    # Test positional argument
    with patch('ansible_collections.ansible.builtin.plugins.modules.ping.AnsibleModule') as patch_module:
        sample_args = dict(data='pong')
        patch_module.return_value.params = {}
        patch_module.return_value.params['data'] = sample_args['data']
        with pytest.raises(AnsibleExitJson) as result:
            main()
        assert result.value.args[0] == {"changed": False, "ping": "pong"}

# Generated at 2022-06-13 05:52:30.352401
# Unit test for function main
def test_main():
    input_data = {'data': 'pong', '_ansible_modlib': True}
    module = AnsibleModule(argument_spec={'data': {'type': 'str', 'default': 'pong'}})
    module.exit_json = lambda obj, **kwargs: None
    main(module)
    assert module.params == input_data

# Generated at 2022-06-13 05:52:35.825433
# Unit test for function main
def test_main():
    # Test with no argument given to parameter data
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True,
    )
    result = dict(
        ping='pong',
    )
    assert module.exit_json(**result) == 0, "Failed to return pong"


# Generated at 2022-06-13 05:52:38.409578
# Unit test for function main
def test_main():
    pong = dict(ping='pong')
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert main(module) == pong

# Generated at 2022-06-13 05:52:43.592803
# Unit test for function main
def test_main():
    # Test case 1
    # Test of case where data parameter is set
    # to 'pong'
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

    assert result['ping'] == 'pong'

# Test case 2
# Test of case where data parameter is set to
# 'crash'


# Generated at 2022-06-13 05:52:46.767835
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
    except Exception as e:
        assert(module.params['data'] == 'crash')
        assert(e.__str__() == "boom")

# Generated at 2022-06-13 05:52:49.120289
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        assert main() == {'ping': 'pong'}


# Generated at 2022-06-13 05:52:54.515149
# Unit test for function main
def test_main():
    action = "ansible.builtin.ping"
    datadir = os.path.join(os.path.dirname(__file__), '..', '..', 'unit', 'library', 'data', action)
    for skip_file in ('module_args.json', 'required_if.json'):
        skip_file = os.path.join(datadir, skip_file)
        if os.path.exists(skip_file):
            os.remove(skip_file)
    test = AnsibleModule(action=action,
                         datadir=datadir,
                         restricted=True)
    test.execute_module()

# Generated at 2022-06-13 05:52:55.132672
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:52:56.374738
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:53:30.680674
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        #supports_check_mode=False
    )



# Generated at 2022-06-13 05:53:33.213803
# Unit test for function main
def test_main():
    args = dict(
        data='pong'
    )
    check_args(main, args)


# Generated at 2022-06-13 05:53:33.885424
# Unit test for function main
def test_main():
    assert main() is not None

# Generated at 2022-06-13 05:53:34.274216
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:53:38.357888
# Unit test for function main
def test_main():
    unit_test = ModuleTest()
    # good data
    module = unit_test.get_module_mock()
    data = dict(
        ping="pong"
    )
    unit_test.run_function(main, module)
    unit_test.exit_json.assert_called_once_with(**data)
    # bad data
    module = unit_test.get_module_mock()
    unit_test.run_function_raises_exception(main, module, data=dict(data="crash"))

# Generated at 2022-06-13 05:53:43.151533
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

# Generated at 2022-06-13 05:53:49.695961
# Unit test for function main
def test_main():
    for test_case in test_cases:
        m = AnsibleModule(test_case[0])
        result = m.main()
        assert result == test_case[1]


test_cases = [
  (
    dict(
      data=dict(type='str', default='pong'),
    ),
    dict(
        ping='pong',
    )
  )
]

# Generated at 2022-06-13 05:53:54.426449
# Unit test for function main
def test_main():
    import sys
    sys.path.append('/usr/lib/python2.6/site-packages')
    import json
    with open('/tmp/ansible_ping_payload.json', 'r') as payload:
        # load the ipaddr data
        payload = json.load(payload)

    p = main()
    p = json.loads(i)
    assert p['ping'] == 'pong'

# Generated at 2022-06-13 05:53:56.906114
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    ping_result=dict(ping="pong")
    assert main(module.params) == ping_result

# Generated at 2022-06-13 05:54:04.160134
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    def raise_exception(x,*args,**kwargs):
        raise Exception(x)
    module = AnsibleModule
    module.fail_json = raise_exception
    module.exit_json = raise_exception
    # module.fail_json = lambda x,**kwargs: raise_exception(x,kwargs)
    args = dict(
        data='pong'
    )
    main(module=module,args=args)
    args['data'] = 'crash'
    with raises(Exception):
        main(module=module,args=args)

# Generated at 2022-06-13 05:55:24.287823
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    main()

# Generated at 2022-06-13 05:55:26.065564
# Unit test for function main
def test_main():
    assert main() == 'data'

# Generated at 2022-06-13 05:55:30.712319
# Unit test for function main
def test_main():
    result = dict(changed=True, ping='pong')

    m = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
    )

    m.exit_json = MagicMock(return_value=result)
    assert main() == result

# Generated at 2022-06-13 05:55:36.476616
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    assert(module.params["data"] == 'pong')


# Generated at 2022-06-13 05:55:44.065701
# Unit test for function main
def test_main():
    data_mocked = {
        'data': 'pong'
    }
    expected_result = {
    'failed': False,
    'changed': False,
    'ping': 'pong'
    }
    module = AnsibleModule(
        argument_spec=dict(
            data=dict(type='str', default='pong'),
        ),
        supports_check_mode=True
    )
    module.params = data_mocked
    result = main()
    assert expected_result == result

# Generated at 2022-06-13 05:55:45.884409
# Unit test for function main
def test_main():
    # No Test yet
    pass

# Generated at 2022-06-13 05:55:46.627108
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:55:58.094859
# Unit test for function main
def test_main():

    def mock_module(params):
        class AnsibleModule:
            def __init__(self, status):
                self.params = params
            def fail_json(self, **kwargs):
                return AnsibleModule(**kwargs)
            def exit_json(self, **kwargs):
                return AnsibleModule(**kwargs)
        return AnsibleModule(params)

    def mock_exit_json(params, **kwargs):
        return params

    def mock_fail_json(params, **kwargs):
        return params

    with patch.object(main, 'AnsibleModule', mock_module):
        with patch.object(main, 'exit_json', mock_exit_json):
            with patch.object(main, 'fail_json', mock_fail_json):

                main()
                main()

    main()

# Generated at 2022-06-13 05:56:09.549574
# Unit test for function main
def test_main():

    # Unit tests for main()
    #
    # Test module without arguments
    # Example:
    #       ping:
    #         ping: pong
    #
    def test_without_args(mocker):
        mocker.patch.object(AnsibleModule, 'exit_json')
        ping = {"ping": "pong"}
        ansible_args = {}
        module = AnsibleModule(argument_spec={})
        main()
        AnsibleModule.exit_json.assert_called_once_with(**ping)

    # Test module with arguments
    # Example:
    #       ping:
    #         ping: hello
    #
    def test_with_args(mocker):
        mocker.patch.object(AnsibleModule, 'exit_json')
        ping = {"ping": "hello"}
        ans

# Generated at 2022-06-13 05:56:13.351510
# Unit test for function main
def test_main():
    # test main() to get 'pong'
    my_argv = ['-a', 'ping']
    with pytest.raises(SystemExit):
        main()

    # test main() to get 'crash'
    my_argv = ['-a', 'ping', '-m', 'crash']
    with pytest.raises(Exception):
        main()