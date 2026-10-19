

# Generated at 2022-06-13 05:13:11.280826
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:13:13.277447
# Unit test for function main
def test_main():
    dpkg_selections = {'selection': 'hold'}
    assert main() == dpkg_selections

# Generated at 2022-06-13 05:13:19.981020
# Unit test for function main
def test_main():
    # Load module and run function main with correct params
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=False,
    )

    module.params = {'name':'python3', 'selection':'install'}
    main()

# Generated at 2022-06-13 05:13:22.919972
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:13:32.153252
# Unit test for function main
def test_main():
    # Arrange
    module = AnsibleModule(argument_spec={"name": {"required": True}, "selection": {"choices": ["install", "hold", "deinstall", "purge"], "required": True}}, supports_check_mode=True)
    module.params = {"name": "python", "selection": "hold"}
    check_rc = True
    dpkg = "/usr/bin/dpkg"

    # Act
    dpkg_selections.main()

    # Assert
    dpkg_selections.AnsibleModule.get_bin_path.assert_called_once_with("dpkg", True)
    assert dpkg_selections.AnsibleModule.get_bin_path.call_count == 1

# Generated at 2022-06-13 05:13:42.704503
# Unit test for function main
def test_main():
    # Create a mocker object to mock the function
    mocker = Mocker()

    # Create a mock module, pass it the mocker object
    mock_module = MockerTestCase(mocker)

    # Create a mock module object
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    name = 'package'
    selection = 'hold'

    dpkg = '/usr/bin/dpkg'
    current = 'install'

    # Mock the required get_bin_path() function
    mock_module.get_bin_path('dpkg', True)

    # Mock the required run_command()

# Generated at 2022-06-13 05:13:48.371726
# Unit test for function main
def test_main():
    test_cases = [
        (
            "comment",
            {
                'name': 'python',
                'selection': 'hold'
            }
        )
    ]
    for test_case in test_cases:
        print(test_case)
        main(test_case)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:13:53.562635
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    assert isinstance(main(), dict)


# Generated at 2022-06-13 05:14:01.113296
# Unit test for function main
def test_main():
    # Tests if the module is idempotent if the package is already on hold
    out = "'dpkg-query', '--get-selections', 'python'\n'python', 'hold'"
    err = "python "
    rc = 0
    results = dict(
        changed=False,
        before='hold',
        after='hold'
    )
    test_main_func(out, err, rc, results)

    # Tests if the module is idempotent if the package is not present
    out = "'dpkg-query', '--get-selections', 'python'"
    err = "python "
    rc = 0
    module.run_command.return_value = (out, err, rc)
    results = dict(
        changed=False,
        before='not present',
        after='hold'
    )


# Generated at 2022-06-13 05:14:01.601638
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-13 05:14:12.023310
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'
    out="python  hold"
    selection = 'hold'
    assert out == "%s %s" % (name, selection)

# Generated at 2022-06-13 05:14:12.783683
# Unit test for function main
def test_main():
    #TODO: Implement unit tests
    pass

# Generated at 2022-06-13 05:14:17.150721
# Unit test for function main
def test_main():
    import StringIO
    import os

    # Mock return value of run_command
    def mock_run_command(a, b, c):
        if c['data'] == 'test_package hold\n':
            return 0, 'test_package deinstall', ''
        elif c['data'] == 'test_package install\n':
            return 0, 'test_package hold', ''
        elif c['data'] == 'test_package_2 deinstall\n':
            return 0, 'test_package_2 deinstall', ''

    # Set environment variables
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"name": "test_package", "selection": "hold"}'
    os.environ['ANSIBLE_CHECK_ARGS'] = '"check_mode": true, "diff_mode": false'

    #

# Generated at 2022-06-13 05:14:25.802644
# Unit test for function main
def test_main():
    # Test if name and selection were set and the module exits successfully
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.params['name'] = "test"
    module.params['selection'] = "test"

    assert module.params['name'] == "test"
    assert module.params['selection'] == "test"
    main()

# Generated at 2022-06-13 05:14:33.047474
# Unit test for function main
def test_main():
    import os
    import random
    import string
    import tempfile
    import shutil
    import ansible_module_dpkg_selections
    import ansible.module_utils.basic
    import ansible.module_utils.action_plugins.system.dpkg_selections

    # Build file path
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)))
    ansible_module_dpkg_selections.main()

    # Remove directory
    shutil.rmtree(temp_dir)



# Generated at 2022-06-13 05:14:43.687567
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:14:45.611915
# Unit test for function main
def test_main():
    assert main() == 'Hello, world'

# Generated at 2022-06-13 05:14:59.489079
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:15:02.693817
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert main.__name__ == 'main'

# Generated at 2022-06-13 05:15:15.345972
# Unit test for function main
def test_main():
    import json
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = "telnet"
    selection = "install"

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:15:26.588372
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-13 05:15:38.545777
# Unit test for function main
def test_main():
    request = {
            "name": "python",
            "selection": "hold"
    }

    module = AnsibleModule(argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = request['name']
    selection = request['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]


# Generated at 2022-06-13 05:15:48.789530
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:16:00.564736
# Unit test for function main
def test_main():
    test_values = [
        dict(
            name='python',
            selection='hold',
            rc=0,
            out='python	install',
            err='',
            check_rc=True,
            check=True,
            changed=True,
            before='install',
            after='hold'
        ),
        dict(
            name='python',
            selection='hold',
            rc=0,
            out='python	hold',
            err='',
            check_rc=True,
            check=True,
            changed=False,
            before='hold',
            after='hold'
        )
    ]

# Generated at 2022-06-13 05:16:08.502894
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:16:10.869053
# Unit test for function main
def test_main():
    assert main() is True

# Run tests
if __name__ == '__main__':
    import pytest
    pytest.main(['-v', __file__])

# Generated at 2022-06-13 05:16:12.631484
# Unit test for function main
def test_main():
    m = {}
    if m != main():
        assert True
    else:
        assert False

# Generated at 2022-06-13 05:16:17.175331
# Unit test for function main
def test_main():
    m = Mock()
    m.get_bin_path = Mock(return_value=True)
    m.check_mode = True
    m.params = {'name': 'python', 'selection': 'hold'}
    m.run_command = Mock(side_effect=[[0, 'python hold\n', ''], [0, '', '']])
    main()
    (m.run_command.assert_called_with(['dpkg', '--set-selections'], 'python hold', True))

# Generated at 2022-06-13 05:16:18.968558
# Unit test for function main
def test_main():
    with pytest.raises(SigTermError):
        main()

# Generated at 2022-06-13 05:16:19.630551
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:16:49.805842
# Unit test for function main
def test_main():
    result = main()
    assert result == 0

# Generated at 2022-06-13 05:16:59.848962
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    #if module.check_mode or not changed:

# Generated at 2022-06-13 05:17:00.294156
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:17:01.264896
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import subprocess


# Generated at 2022-06-13 05:17:06.416202
# Unit test for function main
def test_main():
    print("This is a test of function main")
    # Replace the following code with test code that runs the unit test.
    # Note: The following code will cause this test to fail (by calling exit_json with changed=False), which is what we want.
    # Comment out the following code to cause this test to pass (by calling exit_json with changed=True), which is not what we want.
    # If you comment out the following block of code, the test will pass and the other tests will be skipped.
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.exit_json(changed=False)

# Generated at 2022-06-13 05:17:08.185153
# Unit test for function main
def test_main():
    assert main() == {}

# Generated at 2022-06-13 05:17:08.902021
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:17:21.193276
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        test_result = not changed

# Generated at 2022-06-13 05:17:28.288669
# Unit test for function main
def test_main():
    import mock
    import nbxmpp
    import sys

    class MockSocket():
        def __init__(self):
            self.sock = mock.Mock()
            self.sock.recv.return_value = "foo@bar.com"
            self.sock.getpeername.return_value = ("foo@bar.com/abc", "abcdef")
            
    module = mock.Mock()
    module.params = {'username':'foobar', 'password':'password', 'server':'example.com', 'server_port':'5222', 'to':'user@example.com', 'message':'text', 'timeout':90, 'debug':False}
    nbxmpp.socket.socket = MockSocket

# Generated at 2022-06-13 05:17:39.305682
# Unit test for function main
def test_main():
    # Base AnsibleModule object
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Mock module parameters
    module.params['name'] = 'python'
    module.params['selection'] = 'hold'

    # Mock dpkg --get-selections returns
    current = 'install'
    out = '{0} {1}'.format(name, current)

    # Mock run_command results, return True on check_rc
    module.run_command = MagicMock(return_value=(0, out, ''))
    module.run_command.check_rc = True

    # Mock Ans

# Generated at 2022-06-13 05:18:22.462081
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    (_, changed, _) = main(dpkg, name, selection, module)

    assert changed == True

# Generated at 2022-06-13 05:18:34.243123
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.external import hashlib
    from ansible.module_utils.basic import AnsibleModule
    import ansible.modules.system.dpkg_selections as sut

    print('Begin Test')
    m = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    m.params = {
        'name': 'python',
        'selection': 'hold'
    }
    m.check_mode = False
    sut.main()

    print(m.params)

    print('End Test')

# Generated at 2022-06-13 05:18:35.624829
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:18:36.279743
# Unit test for function main

# Generated at 2022-06-13 05:18:40.854421
# Unit test for function main
def test_main():
    out = StringIO()
    m = AnsibleModule(check_mode=True, diff=True, platform="UNKNOWN")
    m.exit_json = lambda **kw: m.exit_json_for_debug(**kw, stderr=out.getvalue(), stdout=out.getvalue())
    try:
        main()
    except SystemExit as e:
        pass
    assert out.getvalue() == ''

# Generated at 2022-06-13 05:18:41.816272
# Unit test for function main
def test_main():
    assert main() == True

# Generated at 2022-06-13 05:18:53.853014
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg = module.get_bin_path('dpkg', True)

    module.params['name'] = 'python'
    module.params['selection'] = 'hold'
    rc, out, err = module.run_command([dpkg, '--get-selections', 'python'], check_rc=True)
    old_selections = out
    assert old_selections
    main()

# need to mock the module.exit_json and module.run_command methods for unit tests
# this should be done automatically by AnsibleModule on import

# Generated at 2022-06-13 05:18:56.720013
# Unit test for function main

# Generated at 2022-06-13 05:19:05.888775
# Unit test for function main
def test_main():
    # Tests
    tests = [
        # test 1
        dict(
            name='python',
            selection='hold',
        ),
        # test 2
        dict(
            name='python',
            selection='deinstall',
        ),
    ]

    # Results
    results = []

    # Execute
    for test in tests:
        name = test.pop('name')
        selection = test.pop('selection')
        module = AnsibleModule(
            argument_spec=dict(
                name=dict(required=True),
                selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
            ),
            supports_check_mode=True,
        )
        module.params['name'] = name
        module.params['selection'] = selection

        dpkg = module.get

# Generated at 2022-06-13 05:19:16.194836
# Unit test for function main

# Generated at 2022-06-13 05:21:27.251940
# Unit test for function main
def test_main():
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as mockAnsibleModule:
        with mock.patch('ansible.module_utils.basic.run_command') as mockRunCommand:
            with mock.patch('ansible.module_utils.basic.get_bin_path') as mockGetBinPath:
                with mock.patch('ansible.module_utils.basic.ModuleFailException') as mockFailException:
                    mockAnsibleModule.return_value = mockAnsibleModule
                    mockAnsibleModule.check_mode = False
                    mockAnsibleModule.exit_json = mock.MagicMock()
                    mockAnsibleModule.params = {
                        'name': 'python',
                        'selection': 'hold',
                    }

# Generated at 2022-06-13 05:21:33.877816
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.community.plugins.modules.dpkg_selections.AnsibleModule') as mock_AnsibleModule:
        with patch('ansible_collections.ansible.community.plugins.modules.dpkg_selections.run_command'):
            with patch('ansible_collections.ansible.community.plugins.modules.dpkg_selections.get_bin_path'):
                main()
                mock_AnsibleModule.run_command.assert_called()

# Generated at 2022-06-13 05:21:36.916675
# Unit test for function main
def test_main():
    args = dict(
        name="python",
        selection="hold"
    )
    rc = main(args, set_defaults=True)
    assert rc['changed'] == True

# Generated at 2022-06-13 05:21:45.551233
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.actions import ModuleRunner

    requirements = {'bin': {'dpkg' : '/bin/true'}, }

    module = basic.AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', False)

    name = module.params['name']
    selection = module.params['selection']

    runner = ModuleRunner(module)
    result = runner.run(name, dpkg, requirements, selection)

    if result:
        assert result.get('changed') is not None

# Generated at 2022-06-13 05:21:49.446147
# Unit test for function main
def test_main():
    module = AnsibleModule(
    argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ),
    supports_check_mode=True,
    )
    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit

# Generated at 2022-06-13 05:21:59.237818
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    import tempfile
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.module_utils.basic import AnsibleModule

    def __exit__(m):
        pass

    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required = True),
            selection = dict(choices = ['install', 'hold', 'deinstall', 'purge'], required = True)
        )
    )
    # Test no change
    dpkg_out="trim:amd64 ntp 1:4.2.8p4+dfsg-3+b1 [amd64, i386]\n"
    dpkg_err=""

# Generated at 2022-06-13 05:22:00.065029
# Unit test for function main
def test_main():
    assert main() == True

# Generated at 2022-06-13 05:22:05.990143
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 05:22:06.680083
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:22:13.615785
# Unit test for function main
def test_main():
    name = 'vim'
    selection = 'install'
    current = selection
    changed = current != selection
    dpkg = '/usr/bin/dpkg'

    dpkg = '/usr/bin/dpkg'
    rc = 0
    out = 'vim hold'
    err = ''

    ret = dict(
        changed=changed,
        before=current,
        after=selection,
        rc=rc,
        stdout=out,
        stderr=err
    )