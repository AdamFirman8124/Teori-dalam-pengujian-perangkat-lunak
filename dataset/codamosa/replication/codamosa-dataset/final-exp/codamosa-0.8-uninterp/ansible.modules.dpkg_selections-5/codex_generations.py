

# Generated at 2022-06-13 05:13:10.970300
# Unit test for function main
def test_main():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common._collections_compat import Mapping
    def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        return (0, "python install")

    module = AnsibleModule(argument_spec={
        'name': {'required': True, 'type': str},
        'selection': {'required': True, 'choices': ['install', 'hold', 'deinstall', 'purge']}},
        supports_check_mode=True)

    module.run_command = run_command
    module.get_bin_path = get_bin_path

    result = main()

    assert result['changed'] == False

# Generated at 2022-06-13 05:13:17.397003
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


# Generated at 2022-06-13 05:13:24.750912
# Unit test for function main
def test_main():

    import shlex
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    name = 'python'
    selection = 'hold'
    out = '%s hold' % name
    err = ''
    rc = 0

    check_rc = True

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)


# Generated at 2022-06-13 05:13:33.384929
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
    
    name = 'mypackage'
    selection = 'hold'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:13:42.205835
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    # dpkg = module.get_bin_path('dpkg', True)
    # module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)
    # module.exit_json(changed=changed, before=current, after=selection)
    main()

# Generated at 2022-06-13 05:13:53.869081
# Unit test for function main
def test_main():
    field_changed = False
    field_check_mode = True
    field_name = 'python'
    field_selection = 'hold'

    # Mock module.run_command
    class run_command:
        def __init__(self, *args, **kwargs):
            pass
        def __call__(self, *args, **kwargs):
            pass
    module.run_command = run_command

    # Mock module.exit_json
    def exit_json(*args, **kwargs):
        global field_changed, field_check_mode, field_name, field_selection
        return dict(changed=field_changed, check_mode=field_check_mode, name=field_name, selection=field_selection)

    module.exit_json = exit_json

    # Calling main
    main()
    assert module.run

# Generated at 2022-06-13 05:14:01.352046
# Unit test for function main
def test_main():
    import os
    import stat
    import shutil
    import tempfile
    import subprocess
    import json
    import pytest
    import ansible.module_utils.basic
    import ansible.module_utils.common.removed
    import ansible.module_utils.common.collections_compat
    import ansible.module_utils.action
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.network
    import ansible.module_utils.urls
    import ansible.module_utils.text
    import ansible.module_utils.six.moves.urllib.error

# Generated at 2022-06-13 05:14:02.030473
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:14:09.740548
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
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


# Generated at 2022-06-13 05:14:10.761276
# Unit test for function main
def test_main():
    dpkg_selections = main()

    assert dpkg_selections is not None

# Generated at 2022-06-13 05:14:31.113888
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
    changed = True

    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    if module.check_mode or not changed:
        module.exit_json

# Generated at 2022-06-13 05:14:32.862216
# Unit test for function main

# Generated at 2022-06-13 05:14:33.729245
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:14:42.238521
# Unit test for function main
def test_main():

    from ansible.modules.packaging.os.dpkg_selections import main

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.get_bin_path = lambda x, y: x
    module.run_command = lambda x, **args: (0, x[1], '')

    assert main() == dict(changed=False, before='', after=''), 'Invalid value'

# Generated at 2022-06-13 05:14:43.227335
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-13 05:14:58.139112
# Unit test for function main
def test_main():
    # Mock module arguments
    args = dict(
        name="python3",
        selection="install",
    )

    # Mock the module runner
    from ansible.module_utils.basic import AnsibleModule
    module_instance = AnsibleModule(
        argument_spec=args,
        supports_check_mode=True,
    )

    # Mock the run_command method
    import sys
    from ansible.module_utils.common.shell import Shell

    def mocked_run_command(command, check_rc=False, quiet=False, data="", binary_data=False):
        if command == ['dpkg', '--get-selections', 'python3']:
            return 0, "python3 install", ""
        elif command == ['dpkg', '--get-selections', 'python']:
            return 0, "", ""

# Generated at 2022-06-13 05:15:04.740613
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
    current = 'not present'
    changed = current != selection
    if module.check_mode or not changed:
        module.exit_json(changed=changed, before=current, after=selection)
    module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)
    module.exit_json(changed=changed, before=current, after=selection)

# Generated at 2022-06-13 05:15:06.890252
# Unit test for function main
def test_main():
    print("Test main function")
    main()
    assert 1==0, "function main failed"

# Generated at 2022-06-13 05:15:07.633757
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:15:18.985326
# Unit test for function main
def test_main():
    # Test raise error
    with pytest.raises(AnsibleModule):
        main()

    # Test check mode
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.check_mode = True
    dpkg = module.get_bin_path('dpkg', True)
    rc, out, err = module.run_command([dpkg, '--get-selections', 'ansible'])
    assert out.split()[1] == 'install'


# Generated at 2022-06-13 05:15:40.384046
# Unit test for function main
def test_main():

    #
    # Mock modules
    #
    import mock

    def fix_main(mock_module):
        #
        # Mock classes
        #
        class MockAnsibleModule(object):
            def __init__(self, argument_spec, check_invalid_arguments,
                         bypass_checks, no_log, check_mode, diff):
                self.argument_spec = argument_spec
                self.check_invalid_arguments = check_invalid_arguments
                self.bypass_checks = bypass_checks
                self.no_log = no_log
                self.check_mode = check_mode
                self.diff = diff

            def fail_json(self, **args):
                self.exit_json(**args)

            def exit_json(self, **args):
                self.result = args


# Generated at 2022-06-13 05:15:49.916929
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
    import random
    import string
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    selection = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    changed = selection != 'hold'


# Generated at 2022-06-13 05:15:50.619475
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:15:51.296642
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:15:51.934735
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:15:57.112293
# Unit test for function main
def test_main():
    unit_tests = [
        [{'name': 'vim', 'selection': 'hold'}, {}],
        [{'name': 'vim', 'selection': 'install'}, {}],
    ]
    for test_args, test_kwargs in unit_tests:
        print(test_args, test_kwargs)
        main(test_args, test_kwargs)

# Generated at 2022-06-13 05:16:07.269770
# Unit test for function main

# Generated at 2022-06-13 05:16:07.785968
# Unit test for function main
def test_main():
    assert main == True

# Generated at 2022-06-13 05:16:16.152770
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

    name = 'vim'
    current = 'hold'
    selection='purge'

    out = "vim hold"
    err = ""
    rc = 0

    module.run_command = mock.Mock(return_value=(rc, out, err))
    module.check_mode = True
    module.params = dict(name=name, selection=selection)
    # Module should not return changed in this case
    main()
    assert module.exited is False


# Generated at 2022-06-13 05:16:25.622657
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

# Generated at 2022-06-13 05:17:00.072280
# Unit test for function main
def test_main():
    # Dummy class to allow the args to be passed to the main class
    class DummyArgs(object):
        pass

    setattr(DummyArgs, 'name', 'python')
    setattr(DummyArgs, 'selection', 'hold')

# Generated at 2022-06-13 05:17:05.692746
# Unit test for function main
def test_main():
    print ("Checking function main")
    #Check_mode False
    original_run_command = AnsibleModule.run_command
    def run_command(self, args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None):
        if args[0] == 'dpkg':
            print(args, data)
            return (0, 'python install', '')
        return original_run_command(self, args, check_rc, close_fds, executable, data, binary_data, path_prefix, cwd, use_unsafe_shell, prompt_regex)
    AnsibleModule.run_command = run_command

# Generated at 2022-06-13 05:17:06.169126
# Unit test for function main
def test_main():
    result = main()

# Generated at 2022-06-13 05:17:07.397878
# Unit test for function main
def test_main():
     with pytest.raises(AnsibleExitJson):
         main()

# Generated at 2022-06-13 05:17:13.463872
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
    )
    rc = main()
    assert rc == True

# Generated at 2022-06-13 05:17:21.066200
# Unit test for function main
def test_main():
    # Test with a package not currently installed
    name = 'test_name'
    selection = 'install'
    mock_module = {}
    mock_module['name'] = name
    mock_module['selection'] = selection

    current = 'not installed'
    changed = True

    # Test function with the above params
    ret_values = main(mock_module)
    assert ret_values['changed'] == changed
    assert ret_values['before'] == current
    assert ret_values['after'] == selection

# Generated at 2022-06-13 05:17:28.179619
# Unit test for function main
def test_main():
    import mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    class MyMockFile(StringIO):
        def read(self, *args, **kwargs):
            return StringIO.read(self)
        def seek(self, *args, **kwargs):
            StringIO.seek(self, *args, **kwargs)
            return self

    test_file = MyMockFile()
    test_file.write('name selection\n')
    test_file.seek(0)

# Generated at 2022-06-13 05:17:39.305014
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

# Generated at 2022-06-13 05:17:39.920424
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:17:44.707274
# Unit test for function main
def test_main():
    my_class = ('/usr/bin/dpkg')
    selection = ('install')
    selection = ('deinstall')
    selection = ('purge')
    selection = ('hold')
    assert main == my_class
    assert main == selection
    assert main == selection
    assert main == selection
    assert main == selection

# Generated at 2022-06-13 05:18:38.910879
# Unit test for function main
def test_main():
    import tempfile
    # Test module without argument
    data_str = '''{
        "name": "test",
        "selection": "test",
        "_ansible_tmpdir": "tmpdir"
    }'''

    data = json.loads(data_str)

    res = main(data, False)
    assert res['failed'] == False
    assert res['changed'] == False
    assert res['before'] == 'not present'
    assert res['after'] == 'test'

    res = main(data, True)
    assert res['failed'] == False
    assert res['changed'] == True
    assert res['before'] == 'not present'
    assert res['after'] == 'test'

    # Test module with argument

# Generated at 2022-06-13 05:18:52.696852
# Unit test for function main
def test_main():

    # Mock module and arguments
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Mock name
    module.params['name'] = 'example'
    module.params['selection'] = 'hold'

    # Mock dpkg command
    dpkg_mock = Mock(return_value=(0, "example install", ''))
    with patch.dict(dpkg_selections.__salt__, {'cmd.run_all': dpkg_mock}):
        result = main()
        assert result['changed'] == True
        assert result['before'] == 'install'

# Generated at 2022-06-13 05:19:02.391755
# Unit test for function main
def test_main():
    # Test 1:
    # Test if the module works when things are correct
    data = dict(
        name="package",
        selection="hold"
    )
    module_mock = MagicMock()
    module_mock.params = data
    module_mock.check_mode = False
    module_mock.exit_json = exit_json
    module_mock.get_bin_path = get_bin_path
    module_mock.run_command = run_command

# Generated at 2022-06-13 05:19:12.605797
# Unit test for function main
def test_main():
    import os
    os.environ['LANG'] = 'C'
    os.environ['LC_MESSAGES'] = 'C'
    os.environ['LC_ALL'] = 'C'
    # Main
    name = "testpackage"
    dpkg = "/usr/bin/dpkg"
    selection = "hold"

    # Create two mock methods to simulate the interaction of this module with dpkg:
    # run_command(self, cmd, check_rc=False, close_fds=True, data=None, binary_data=False, cwd=None, use_unsafe_shell=False)
    # call(self, module_name, *args, **kwargs)

# Generated at 2022-06-13 05:19:13.402961
# Unit test for function main
def test_main():
    pass # no tests implemented

# Generated at 2022-06-13 05:19:22.225071
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

    output = '{} {}'.format(name, selection)

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)

    print(out)

    if not out:
        current_output = 'not present'
        current_name = ''
        current_selection = ''
   

# Generated at 2022-06-13 05:19:31.361863
# Unit test for function main
def test_main():

    # Configure the parameters that would be returned by a module
    module_args = dict(
        name='python',
        selection='hold'
    )

    # AnsibleModule args
    argument_spec = dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    )

    # Instantiate our module object
    module = AnsibleModule(argument_spec=module_args)

    # Configure the params that would be returned by ansible module
    module.params = module_args

    # Set the dpkg bin path
    dpkg = '/usr/bin/dpkg'

    # Mock the module.run_command()

# Generated at 2022-06-13 05:19:43.991985
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

# Generated at 2022-06-13 05:19:48.985189
# Unit test for function main
def test_main():
    global module, dpkg, name, selection, changed, current, out, err
    dpkg = "dpkg"
    out = ""
    err = ""
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    name = "testpackage"
    selection = "install"
    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
    changed = current != selection
   

# Generated at 2022-06-13 05:19:50.846391
# Unit test for function main
def test_main():
    m = __import__('__main__')
    m.main(['name', 'selection'])

# Generated at 2022-06-13 05:22:07.634415
# Unit test for function main
def test_main():
    args = dict(
        name="python",
        selection="hold"
    )
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    main(module, args)

# Generated at 2022-06-13 05:22:18.526046
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    from ansible.module_utils._text import to_bytes

    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = 'name'
    selection = 'selection'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out

# Generated at 2022-06-13 05:22:31.445572
# Unit test for function main
def test_main():
    check_set_selections_mock = MagicMock()
    check_get_selections_mock = MagicMock()
    check_get_selections_mock.return_value = ['', 'python\tinstall\n']
    dpkg_selections = DpkgSelections()
    dpkg_selections.check_set_selections = check_set_selections_mock
    dpkg_selections.check_get_selections = check_get_selections_mock
    name = 'python'
    selection = 'hold'
    dpkg_selections.main(name, selection, check_mode=True)
    check_get_selections_mock.assert_called_once_with(name)
    assert check_set_selections_mock.called is False

# Generated at 2022-06-13 05:22:34.819669
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.check_mode = False
    dpkg = module.get_bin_path('dpkg', True)
    module.get_bin_path = MagicMock(return_value=dpkg)
    main()

# Generated at 2022-06-13 05:22:37.611734
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True),
        )
    )
    # Should do nothing here.
    assert module.fail_json.called == 0

# Generated at 2022-06-13 05:22:41.797037
# Unit test for function main
def test_main():
    module = AnsibleModule({})
    setattr(module, 'run_command', mock_run_command)

    dpkg = module.get_bin_path('dpkg', True)

    module = AnsibleModule({'name': 'python', 'selection': 'hold'})
    main()


# Generated at 2022-06-13 05:22:52.037224
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg = module.get_bin_path('dpkg', True)
    # define argument values which will be passed to AnsibleModule.run_command()
    name = module.params['name']
    selection = module.params['selection']
    rc = 0
    out = "python install"
    err = ""
    # run AnsibleModule.run_command()
    module.run_command()
    assert rc == 0
    assert out == "python install"