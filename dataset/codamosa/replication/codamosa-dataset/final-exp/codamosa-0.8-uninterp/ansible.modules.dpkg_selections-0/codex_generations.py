

# Generated at 2022-06-13 05:13:02.641483
# Unit test for function main
def test_main():
    pass

# Unit tests for function main

# Generated at 2022-06-13 05:13:11.334834
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

# Generated at 2022-06-13 05:13:21.998167
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

# Generated at 2022-06-13 05:13:23.326128
# Unit test for function main
def test_main():
    # Put here mock code to make unit test
    pass

# Generated at 2022-06-13 05:13:28.909130
# Unit test for function main
def test_main():

    # Initialize args
    args = dict(name='ansible')

    # Initialize AnsibleModule with the above arguments
    module = AnsibleModule(argument_spec=args)

    # Return value of the function
    results = dict(changed=True, original_message='', message='Ansible Support', after=None, before=None)

    # AnsibleModule.exit_json function to exit from module
    module.exit_json(**results)



# Generated at 2022-06-13 05:13:36.033838
# Unit test for function main
def test_main():
    # Test case 1
    # Imagine that the only distro that I care about is ubuntu (unlikely, but right now a good test case)
    # Should return that the distro is ubuntu
    supported_platforms = ['debian']

    current_platform = 'debian'

    platfrom_exists_in_supported_distros = False

    for iterable_item in supported_platforms:
        if iterable_item == current_platform:
            platfrom_exists_in_supported_distros = True

    if platfrom_exists_in_supported_distros == True:
        print('Platform Exists in Supported distros')
    else:
        print('Platform does not exist in supported distros')

    # Test case 2
    # There is no distro called Ubuntu (example)
    # Should return that the distro is not ub

# Generated at 2022-06-13 05:13:44.145781
# Unit test for function main
def test_main():
    from ansible.modules.packaging.os import dpkg_selections

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = 'python'
    selection = 'hold'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:13:45.703497
# Unit test for function main
def test_main():
    assert True


# Generated at 2022-06-13 05:13:55.666442
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.check_mode = False
    if module.params['name'] == 'dpkg1' and module.params['selection'] == 'hold':
        module.run_command = lambda *args, **kwargs: ('', 'dpkg1 hold', '')
        module.run_command([], data="dpkg1 hold", check_rc=True)
        module.exit_json(changed=True, before="dpkg1 install", after="dpkg1 hold")

# Generated at 2022-06-13 05:13:57.139345
# Unit test for function main
def test_main():
    # Placeholder for unit test
    assert(True)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:14:11.441114
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

    name = 'python'
    selection = 'hold'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    assert changed == True
    assert current == 'install'
    assert selection == 'hold'

# Generated at 2022-06-13 05:14:13.206771
# Unit test for function main
def test_main():
    # Test if __main__'s dpkg variable is a string.
    main_dpkg_typecheck = isinstance(dpkg(), str)
    assert(main_dpkg_typecheck)

# Generated at 2022-06-13 05:14:19.242275
# Unit test for function main
def test_main():
    try:
        import mock
    except ImportError:
        import unittest.mock as mock

    module = mock.MagicMock()
    module.get_bin_path = mock.MagicMock(side_effect=['dpkg', 'dpkg'])
    module.params = {'name': 'python', 'selection': 'install'}
    module.run_command.return_value = (0, 'python install', '')
    module.check_mode = False

    try:
        main()
    except SystemExit as e:
        assert e.code == 0
    finally:
        assert module.run_command.call_count == 2
        assert module.run_command.call_args == mock.call(['dpkg', '--get-selections', 'python'], check_rc=True)
        assert module.run

# Generated at 2022-06-13 05:14:30.383245
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import json
    import os
    import sys
    import shutil
    import tempfile

    current_dir  = os.path.dirname(os.path.abspath(__file__))
    module_path = os.path.join(current_dir, '../../../../lib/ansible/modules/extras')
    module_kwargs = dict(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    mock_module = AnsibleModule(**module_kwargs)


# Generated at 2022-06-13 05:14:30.919606
# Unit test for function main
def test_main():
    assert 5 == 5

# Generated at 2022-06-13 05:14:42.331481
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = MagicMock(return_value=(0, 'python not present', ''))
    module.run_command.side_effect = [
        (0, 'python install', ''),
        (0, 'python install', ''),
        (0, 'python hold', ''),
        (0, 'python hold', ''),
        (0, '', ''),
        (0, '', ''),
    ]
    module.exit_json = MagicMock()

# Generated at 2022-06-13 05:14:42.957502
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:14:53.694417
# Unit test for function main
def test_main():
    # mock the module object
    module = Mock()
    # mock the module exit_json method
    module.exit_json = Mock()
    # mock the module run_command method
    module.run_command = Mock(return_value=(0, 'theFoo theBar', ''))
    # mock the module get_bin_path method
    module.get_bin_path = Mock(return_value='/bin/dpkg')
    # call main
    main()
    # if the test makes it here then it has passed
    assert True

# Generated at 2022-06-13 05:15:01.094753
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

    name = 'python'
    selection = 'hold'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:15:08.385665
# Unit test for function main
def test_main():
    args = {}
    args['name'] = 'python'
    args['selection'] = 'hold'

    dpkg = AnsibleModule(argument_spec={})
    setattr(dpkg, 'get_bin_path', lambda *args, **kwargs: '-/bin/dpkg')

    args['module'] = dpkg
    args['check_mode'] = False
    args['diff_mode'] = True

    # Get current settings.
    args['rc'], args['out'], args['err'] = 0, 'test install', ''
    if not args['out']:
        args['current'] = 'not present'
    else:
        args['current'] = args['out'].split()[1]

    args['changed'] = args['current'] != args['selection']

# Generated at 2022-06-13 05:15:28.624917
# Unit test for function main
def test_main():
    test = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    test.run_command = Mock(return_value=(0, '', ''))
    test.get_bin_path = Mock(return_value='/path/to/dpkg')

    test.params['name'] = 'python'
    test.params['selection'] = 'hold'

    main()

    assert test.run_command.call_count == 2
    assert test.run_command.call_args_list[0][0][0] == ['/path/to/dpkg', '--get-selections', 'python']

# Generated at 2022-06-13 05:15:37.795983
# Unit test for function main
def test_main():
    dpkg = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg.check_mode = False
    dpkg.params['name'] = 'exim4-base'
    dpkg.params['selection'] = 'hold'

    assert main() == dpkg.run_command_environ_update(['dpkg', '--set-selections'], data="exim4-base hold", check_rc=True)[1]

# Generated at 2022-06-13 05:15:48.182711
# Unit test for function main
def test_main():
    import sys
    import shlex, subprocess
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ))

    # Mock the module input parameters
    test_module.params = {
        'name': 'python',
        'selection': 'hold',
    }

    # Mock the module methods
    test_module.get_bin_path = lambda x=None, opt_dirs=None: '/usr/bin/dpkg'
    test_module.run_command = run_command_mock

    # Mock the AnsibleModule.exit_json()
    test_module.exit_json = exit_json_mock

# Generated at 2022-06-13 05:15:52.964369
# Unit test for function main
def test_main():
    # This example test is OK as it contains a 'skip_if' check
    # See: https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_documenting.html#unit-tests-and-integration-tests
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

# Generated at 2022-06-13 05:16:01.833161
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    name = module.params['name']
    selection = module.params['selection']

    module.params['name'] = 'python'
    module.params['selection'] = 'hold'
    assert main() == False

# Generated at 2022-06-13 05:16:09.719075
# Unit test for function main
def test_main():
    import unittest
    module = AnsibleModule({}, supports_check_mode=True)
    setattr(module, '_ansible_check_mode', True)

    class Args:
        name = 'python'
        selection = 'hold'

    setattr(module, 'params', Args)

    classtest = DpkgWrapper(module)
    x = classtest.main()
    assert type(x) == dict
    assert x['changed'] == True
    assert x['before'] == 'not present'
    assert x['after'] == 'hold'

# Generated at 2022-06-13 05:16:12.113792
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert main() == True

# Generated at 2022-06-13 05:16:12.674260
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:16:18.907401
# Unit test for function main
def test_main():

    names = []
    selections = []

    def run_command_mock(args, check_rc=False, data=None):
        if args[0] == '/usr/bin/dpkg' and args[1] == '--get-selections' and args[2] == 'python':
            return 0, 'python install', ''
        if args[0] == '/usr/bin/dpkg' and args[1] == '--get-selections' and args[2] == 'python3':
            return 0, 'python3 install', ''
        if args[0] == '/usr/bin/dpkg' and args[1] == '--set-selections' and data == 'python hold':
            names.append('python')
            selections.append('hold')
            return 0, '', ''

# Generated at 2022-06-13 05:16:20.322469
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleModuleSystemExit):
        main()

# Generated at 2022-06-13 05:16:54.651878
# Unit test for function main
def test_main():
    # import the module
    from ansible.modules.packaging.os.dpkg_selections import main



# Generated at 2022-06-13 05:17:02.561392
# Unit test for function main
def test_main():
    import os
    import ansible.module_utils.basic
    module = os.path.join(os.path.dirname(__file__), '../lib/ansible/modules/packaging/os/dpkg_selections.py')
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            selection=dict(type='str', required=True, choices=['install', 'hold', 'deinstall', 'purge'])
        )
    )

# Generated at 2022-06-13 05:17:07.653785
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    x = main()
    assert x != 5

# Generated at 2022-06-13 05:17:20.256198
# Unit test for function main
def test_main():
    argument_spec = {
        "selection": {
            "choices": [
                "install", 
                "hold", 
                "deinstall", 
                "purge"
            ], 
            "required": True
        }, 
        "name": {
            "required": True
        }
    }

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'

# Generated at 2022-06-13 05:17:27.592032
# Unit test for function main

# Generated at 2022-06-13 05:17:33.305335
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert main() == 0

# Generated at 2022-06-13 05:17:42.009507
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = Mock(return_value=(0, '', ''))
    module.get_bin_path = Mock(return_value='/usr/bin/dpkg')
    setattr(module, '_diff', False)
    setattr(module, '_changed', False)
    setattr(module, '_ansible_check_mode', False)
    dpkg_selections.main()

# Generated at 2022-06-13 05:17:53.205487
# Unit test for function main
def test_main():
    DpkgSelections = __import__('main')
    attr = {'run_command.return_value': (0, 'python install', '')}
    attr1 = {'run_command.return_value': (0, '', 'Error!')}
    module = AnsibleModule(argument_spec={'name': {'required': True}, 'selection': {'required': True}})
    module.get_bin_path = lambda x: "/opt/bin/"+x
    module.check_mode = False
    module.exit_json = lambda x: x if 'changed' in x else None
    module.run_command = lambda x, check_rc=None: (0, 'python install', '')
    assert DpkgSelections.main() == {'changed': True, 'before': 'install', 'after': 'install'}


# Generated at 2022-06-13 05:18:00.982426
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.system.package.dpkg import main as dpkg_main
    from ansible.module_utils._text import to_bytes
    import os
    # First parameter is the name of the module, the rest of the items are the arguments
    # os.environ is required for the AnsibleModule to access the environment
    # to_bytes is required for the test function to convert the string to bytes
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg_main(module, module.params)

# Generated at 2022-06-13 05:18:13.491517
# Unit test for function main
def test_main():
    # mock input
    class MockModule():
        def __init__(self):
            self.params = {
                'name': 'python',
                'selection': 'hold'
            }
            self.check_mode = True
        def get_bin_path(self, path, required):
            return path
    class MockCommand():
        def __init__(self):
            self.rc = 0
            self.out = "python        hold"
            self.err = ""
        def run_command(self, cmd, check_rc=True):
            return self.rc, self.out, self.err
    mock_module = MockModule()
    mock_command = MockCommand()
    # set mock run_command
    mock_module.run_command = mock_command.run_command
    # call function
    main()
    #

# Generated at 2022-06-13 05:19:06.965395
# Unit test for function main
def test_main():
    import re
    import platform

    import mock

    if platform.system() == 'Darwin':
        return

    def run_command(command, check_rc=True):
        return (0, 'dpkg --get-selections out', 'err')

    # Import our module
    dpkg_selections = __import__('dpkg_selections')

    # Mock module_utils/basic.py
    dpkg_selections.__import__('ansible.module_utils.basic')
    ansible_basic = dpkg_selections.sys.modules['ansible.module_utils.basic']
    ansible_basic.run_command = run_command


# Generated at 2022-06-13 05:19:16.957765
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

# Generated at 2022-06-13 05:19:20.125836
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ))
    assert main() == module.exit_json()

# Generated at 2022-06-13 05:19:30.264469
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

# Generated at 2022-06-13 05:19:43.133467
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

# Generated at 2022-06-13 05:19:44.834519
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name="python",
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True),
            check_mode=True
        )
    )
    main()

# Generated at 2022-06-13 05:19:49.802714
# Unit test for function main
def test_main():
    name = "apache2"
    selection = "hold"
    module = AnsibleModule(argument_spec={'name': {'required': True, 'type': 'str'}, 'selection': {'required': True, 'choices': ['install', 'hold', 'deinstall', 'purge']}})
    main()

# Generated at 2022-06-13 05:19:51.710482
# Unit test for function main
def test_main():
    dpkg_selections = module.get_bin_path('dpkg_selections', True)
    assert dpkg_selections

# Generated at 2022-06-13 05:19:52.211035
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:20:03.018824
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
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


# Generated at 2022-06-13 05:22:31.617953
# Unit test for function main
def test_main():
    #mocks
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


# Generated at 2022-06-13 05:22:42.611279
# Unit test for function main
def test_main():
    m = AnsibleModule(argument_spec={'name': {'required': True, 'type': 'str'}, 'selection': {'choices': ['install', 'hold', 'deinstall', 'purge'], 'required': True, 'type': 'str'}, 'check_mode': {'support': 'full'}, 'diff_mode': {'support': 'full'}, 'platform': {'support': 'full', 'platforms': ['debian']}}, supports_check_mode=True)

    m.run_command = run_command

    # Test no change
    m.params['name'] = 'python'
    m.params['selection'] = 'hold'
    m.exit_json = exit_json
    main()
    assert m.exited == 0

    # Test change
    m.params['name'] = 'python'
   

# Generated at 2022-06-13 05:22:49.621676
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
    )
    module.run_command = MagicMock(return_value=(0, 'cat', ''))
    module.run_command.assert_called_with(['dpkg', '--set-selections'], data="cat install", check_rc=True)

# Generated at 2022-06-13 05:22:58.022431
# Unit test for function main
def test_main():
    # Create a mock module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Set dpkg path and current selection to "deinstall"
    dpkg = '/usr/bin/dpkg'
    name = 'python'
    current = 'deinstall'
    changed = True


    # Test dpkg --get-selections python
    module.run_command = MagicMock()
    module.run_command.return_value = (0, "%s\t%s" % (name, current), '')
    list(main())
