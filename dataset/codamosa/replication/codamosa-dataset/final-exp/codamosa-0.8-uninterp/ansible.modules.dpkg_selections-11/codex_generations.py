

# Generated at 2022-06-13 05:13:10.060120
# Unit test for function main
def test_main():
    import shlex
    from ansible.module_utils.basic import AnsibleModule

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


# Generated at 2022-06-13 05:13:15.044360
# Unit test for function main
def test_main():
    class ModuleMock(object):
        def __init__(self):
            self.params = {}
            self.check_mode = None
            self.exit_args = {'failed': False}
            self.return_val = None
            self.run_command_output = None

        def get_bin_path(self, bin_name, required=False):
            return 'dpkg'

        def run_command(self, cmd, **kwargs):
            return (0, self.run_command_output, '')

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = True

    module = ModuleMock()

# Generated at 2022-06-13 05:13:24.137329
# Unit test for function main
def test_main():
    dpkg_test_package_name = 'python3'
    dpkg_test_package_selection = 'install'
    dpkg_test_package_selection_after = 'hold'

    # get test values
    dpkg_test_cmd_get_selection = "%s --get-selections %s" % (
        module.get_bin_path('dpkg', True), dpkg_test_package_name)
    rc, out, err = module.run_command(dpkg_test_cmd_get_selection, check=True)
    value_get_selection_before = out.split()[1]
    # set test values
    dpkg_test_cmd_set_selection = "%s --set-selections" % module.get_bin_path('dpkg', True)

# Generated at 2022-06-13 05:13:33.044026
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = 'test'
    selection = 'hold'

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

# Generated at 2022-06-13 05:13:43.406670
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = test_module.get_bin_path('dpkg', True)
    assert dpkg

    # Test weird name case
    name = 'test1'
    selection = 'purge'
    rc, out, err = test_module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:13:54.807726
# Unit test for function main
def test_main():
    # Mock module import.
    import mock
    import os.path
    import module
    import subprocess
    # Mock module exit_json.
    module.module.exit_json = lambda x: None
    # Mock module fail_json.
    module.module.fail_json = lambda x: None
    # Mock module get_bin_path.
    module.module.get_bin_path = lambda x: os.path.join('/usr/bin', x)
    # Mock module run_command
    def get_run_command(cmd):
        def run_command(x, **kwargs):
            if x[2] == 'dpkg':
                if x[3] == '--get-selections':
                    return (0, 'python\tinstall\n', '')

# Generated at 2022-06-13 05:13:55.343180
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:13:57.389979
# Unit test for function main
def test_main():
    synch_dict = dict(selection='hold', name='python')
    module = AnsibleModule(argument_spec=dict(synch_dict))
    main()

# Generated at 2022-06-13 05:14:03.141154
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.dict_transformations import to_list
    import sys
    import ast
    import shlex

    # install mock, required for mocking open()
    if sys.version_info > (2, 7):
        import unittest.mock as mock
    else:
        import mock

    # Read a string containing the output of dpkg command
    with open('tests/testdata/dpkg-get-selections.out') as fp:
        dpkg_get_selections_out = fp.read()

    test_result = {
        'changed': True,
        'before': 'hold',
        'after': 'install'
    }

    # Read test data from test_main_testdata.txt

# Generated at 2022-06-13 05:14:09.484235
# Unit test for function main
def test_main():
    # create the mock interface for dpkg module
    module = MockDpkgModule()

    # define the name and selection
    name = "python"
    selection = "hold"

    # define the args
    args = 'name=' + name + ',selection=' + selection

    # set the argv to utf-8 encoded version
    module.params = json.loads(base64.b64decode(args))

    # check first if we are not in check mode
    if not module.check_mode:
        isExited = False
    else:
        isExited = True

    # check if the module is exited
    assert isExited is True

# Generated at 2022-06-13 05:14:32.684185
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

    # select a hardcoded current value here
    # so that we can test the code paths
    def get_selections(name):
        current = 'not present'
        return (current, 0, '')

    module.get_bin_path = lambda a: 'dpkg'
    module.run_command = lambda a: get_selections(name)

    dpkg_selections = Dpkg_Selections(module)

# Generated at 2022-06-13 05:14:43.398826
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'
    dpkg_selections_result = main(name, selection)
    assert_equal(dpkg_selections_result['changed'], True)
    assert_equal(dpkg_selections_result['after'], selection)
    old_selection = dpkg_selections_result['before']
    new_selection = dpkg_selections_result['after']

    # Return to the original state.
    dpkg_selections_result = main(name, old_selection)
    assert_equal(dpkg_selections_result['changed'], True)
    assert_equal(dpkg_selections_result['after'], old_selection)
    # Test that the state has been restored.
    dpkg_selections_result = main(name, new_selection)
    assert_

# Generated at 2022-06-13 05:14:51.636679
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.params['name'] = 'python'
    module.params['selection'] = 'hold'
    assert main() == None

# Generated at 2022-06-13 05:14:57.275254
# Unit test for function main
def test_main():
    
    print('Testing module: %s' % __file__)
    
    # From here we'll use internal ansible modules
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    
    
    # Import module
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
    
    
    # Mock data functions

# Generated at 2022-06-13 05:15:04.051997
# Unit test for function main
def test_main():
    import json
    
    # Mock test
    def fake_run_command(module, command, check_rc=False):
        return (0, 'python install', ''), None
        
    with patch.object(AnsibleModule, 'run_command', fake_run_command):
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


# Generated at 2022-06-13 05:15:16.411862
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

    print(changed)
    print(current)

# Generated at 2022-06-13 05:15:17.183254
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:15:27.840774
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

    assert(changed)
    assert(current == 'hold')
   

# Generated at 2022-06-13 05:15:38.874588
# Unit test for function main
def test_main():
    test = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    test.get_bin_path = lambda _, required: "/usr/bin/dpkg"

    test.run_command = lambda args, check_rc=False: (
        1 if args[3] == 'hold' and args[2] == '--set-selections' else 0,
        "%s install" % args[3] if args[2] == '--get-selections' else '', '', []
    )

    m = main()
    print(m)

# Generated at 2022-06-13 05:15:48.576522
# Unit test for function main
def test_main():
    import mock
    mock_module = mock.Mock()
    mock_module.fail_json = mock.Mock(side_effect=Exception('FAIL'))
    mock_module.check_mode = False
    mock_module.params = {
        'name': 'python',
        'selection': 'hold'
    }
    mock_module.run_command = mock.Mock()
    mock_module.get_bin_path = mock.Mock()
    mock_module.run_command.return_value = (0, '', '')
    mock_module.get_bin_path.return_value = 'dpkg'
    main()
    mock_module.exit_json.assert_called_with(changed=False, before='hold', after='hold')

# Generated at 2022-06-13 05:16:16.467915
# Unit test for function main
def test_main():
    print("test_main")

    assert main() == True

# Generated at 2022-06-13 05:16:25.768856
# Unit test for function main
def test_main():
    import sys

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    import ansible.module_utils as module_utils

    class TestDpkgSelections(unittest.TestCase):

        def setUp(self):
            sys.modules['__main__'] = module_utils.basic
            self.module = __import__('__main__')


    def run_module():
        module_args = dict(
            name='python',
            selection='hold'
        )

        if 'check_mode' in module_args:
            module_args['check_mode'] = True
        else:
            module_args['check_mode'] = False

        # Fail the module if dpkg command can't be found
        module_args['ansible_check_mode'] = False



# Generated at 2022-06-13 05:16:36.592763
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


# Generated at 2022-06-13 05:16:40.190718
# Unit test for function main
def test_main():
    # Test with no changes
    module = ansible_mock.MockModule({
        'name': 'python',
        'selection': 'hold'
    })
    rc = dpkg_selections.main()
    assert rc['changed'] == False
    assert 'before' in rc
    assert 'after' in rc

    # Test with changes
    module = ansible_mock.MockModule({
        'name': 'python',
        'selection': 'install'
    })
    rc = dpkg_selections.main()
    assert rc['changed'] == True
    assert 'before' in rc
    assert 'after' in rc

# Generated at 2022-06-13 05:16:41.598431
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:16:50.166577
# Unit test for function main
def test_main():
    # Test that checks the --set-selections command to set the package selection state.
    # This test is based on the example provided.
    print('Testing dpkg_selections.main().')
    # Setup arguments to match the example.
    args = {
        'name': 'python',
        'selection': 'hold'
    }
    # Add the arguments to a module object.
    mod = AnsibleModule(argument_spec={
        "name": dict(required=True),
        "selection": dict(required=True, choices=['install', 'hold', 'deinstall', 'purge'])
    }, supports_check_mode=True)
    mod.params = args
    # Create a mock for the main() function returning True.
    main = MagicMock(return_value=True)
    # Assign the mock.
    dpkg

# Generated at 2022-06-13 05:17:00.231814
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common.shell import run_command
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    dpkg = get_bin_path('dpkg', True)

    class FakeModule(object):
        def __init__(self):
            self.params = dict(
                name='python',
                selection='hold',
            )
            self.check_mode = False
            self.supports_check_mode = True

        def get_bin_path(self, _, want_raise=True):
            return dpkg


# Generated at 2022-06-13 05:17:00.940889
# Unit test for function main
def test_main():
    assert main() == "foo"

# Generated at 2022-06-13 05:17:06.213844
# Unit test for function main
def test_main():
    # Mock of AnsibleModule
    class AnsibleModuleMock:
        def __init__(self, argument_spec, supports_check_mode=False, check_invalid_arguments=True, mutually_exclusive=None, required_together=None, required_one_of=None,
                     add_file_common_args=True, supports_crud_flags=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually_exclusive = mutually_exclusive or []
            self.required_together = required_together or []
            self.required_one_of = required_one_of or []
            self.add_file_common_args = add_file_common_args
           

# Generated at 2022-06-13 05:17:11.910128
# Unit test for function main
def test_main():
    with patch.object(ModuleUtil, 'run_command', return_value=(0, 'python install', '')) as mock_run_command:
        with patch.object(Module, 'run_command', return_value=(0, '', '')) as mock_run_command:
            import dpkg_selections
            dpkg_selections.main()
    mock_run_command.assert_has_calls([call([dpkg, '--get-selections', 'python'], check_rc=True), call([dpkg, '--set-selections'], data="python hold", check_rc=True)], any_order=True)

# Generated at 2022-06-13 05:17:48.626549
# Unit test for function main
def test_main():
    args = {
      'name': 'python',
      'selection': 'hold',
      'check_mode': True,
    }
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.run_command = mock.Mock()
    module.exit_json = mock.Mock()
    module.get_bin_path = mock.Mock(return_value=get_bin_path('dpkg'))


# Generated at 2022-06-13 05:17:55.544435
# Unit test for function main

# Generated at 2022-06-13 05:17:56.574024
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:18:04.778190
# Unit test for function main
def test_main():
    import pytest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import mock
    from ansible_collections.notstdlib.moveitallout.plugins.modules import dpkg_selections

    module = mock.MagicMock()

    module.params = {
        'name': 'python',
        'selection': 'hold'
    }

    dpkg = mock.MagicMock()
    module.get_bin_path.return_value = dpkg

    module.run_command.return_value = (0, "python hold\n", "")

    return_code = dpkg_selections.main()
    assert return_code == (True, "not present", "hold")

    module.run_command.return_value = (0, "python install\n", "")

   

# Generated at 2022-06-13 05:18:12.486869
# Unit test for function main
def test_main():
    target = AnsibleModule({'name': 'tar', 'selection': 'hold'})
    goal = {
        'changed': True,
        'after': 'hold',
        'before': 'install'
    }

    with mock.patch.object(target, 'run_command') as run_command:
        run_command.return_value = [0, 'tar install', '']
        run_command.return_value = [0, '', '']
        result = main()
        assert result == goal

# Generated at 2022-06-13 05:18:18.935509
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

# Generated at 2022-06-13 05:18:27.615088
# Unit test for function main
def test_main():

    class AnsibleModuleMock():

        params = {
            'name': 'testpython',
            'selection': 'hold'
        }

        class run_command():
            def __init__(self, cmd, data=None, check_rc=True):
                if 'purge' in cmd:
                    rc = 0
                    err = ''
                else:
                    rc = 1
                    err = 'error'
                self.rc = rc
                self.err = err
                self.data = data
                self.check_rc = check_rc

        def get_bin_path(self, bin, required):
            return '/usr/bin/dpkg'

        def exit_json(self, changed=False, before='', after=''):
            self.out = changed
            self.before = before
            self.after = after


# Generated at 2022-06-13 05:18:33.722128
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert dpkg == "/usr/bin/dpkg"
    assert name == "test_package"
    assert selection == "hold"

# Generated at 2022-06-13 05:18:42.823859
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'],required=True),
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
    assert changed == True
    print ("Test is successfull")

# Generated at 2022-06-13 05:18:54.571814
# Unit test for function main
def test_main():
    import pytest
    import os
    import tempfile
    from ansible.executor.process.execute import run_command

    # Set up a temporary directory and change to it to isolate us from
    # any side effects of the test.
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)

    # Create a fake dpkg database in the temporary directory.
    run_command(["dpkg", "--get-selections"], check_rc=True)
    os.rename("/var/lib/dpkg/status", "status")

    with pytest.raises(Exception):
        # Test no name.
        args = {}
        main(args)

    with pytest.raises(Exception):
        # Test no selection.
        args = { "name": "test" }
        main(args)

# Generated at 2022-06-13 05:19:48.230464
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:19:58.502503
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = test_module.get_bin_path('dpkg', True)

    name = test_module.params['name']
    selection = test_module.params['selection']

    # Get current settings.
    rc, out, err = test_module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:20:08.638043
# Unit test for function main
def test_main():
    argv = ['dpkg_selections']
    # Unsupported args
    # ---------------
    # name
    if 0:
        argv.extend(["-n", "apt"])
    # selection
    if 0:
        argv.extend(["-s", "install"])

    # supported args
    # ---------------
    if 0:
        argv.extend(["-c", "True"])
    if 0:
        argv.extend(["-C", "True"])
    if 0:
        argv.extend(["-D", "True"])
    if 0:
        argv.extend(["-l", "True"])
    if 0:
        argv.extend(["-L", "True"])
    if 0:
        argv.extend

# Generated at 2022-06-13 05:20:16.258363
# Unit test for function main
def test_main():
    test_main.__doc__ = """Check function main when no packages are installed"""
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    def run_command(args, check_rc):
        return 0, "set name install"

    module.run_command = run_command
    module.params['name'] = 'name'
    module.params['selection'] = 'install'
    main()
    assert module.exit_json.call_args[0][0] == {'changed': True, 'after': 'install', 'before': 'not present'}


# Generated at 2022-06-13 05:20:20.804319
# Unit test for function main
def test_main():
    rc, out, err = module.exit_json(changed=1, before="purge", after="deinstall")
    assert rc, out == 0
    assert err ==0
    assert changed == 1 
    #assert out == {"changed": 1, "before": "purge", "after": "deinstall"}

# Generated at 2022-06-13 05:20:29.455094
# Unit test for function main
def test_main():

    # Import Ansible module
    import ansible.modules.packaging.os.dpkg_selections as dpkg_selections

    # Set Ansible arguments
    args = dict(
        name='python',
        selection='hold',
    ) 

    # AnsibleModule()
    dpkg_selections.AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ),
    supports_check_mode=True,
    )

    # AnsibleModule().get_bin_path()
    dpkg_selections.AnsibleModule.get_bin_path(ansible.modules.packaging.os.dpkg_selections, 'dpkg', True)

    # AnsibleModule

# Generated at 2022-06-13 05:20:35.375442
# Unit test for function main
def test_main():
    payload = {
        "name": "python",
        "selection": "hold",
        "check_mode": False
    }
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    is_error, has_changed, result = main()
    module.exit_json(changed=has_changed, meta=result)



# Generated at 2022-06-13 05:20:43.770737
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_AnsibleModule, \
         patch('ansible.module_utils.basic.run_command') as mock_run_command, \
         patch('ansible.module_utils.basic.get_bin_path') as mock_get_bin_path:
        mock_AnsibleModule.return_value.check_mode = True
        mock_AnsibleModule.return_value.params = {
            'name': 'python',
            'selection': 'hold'
        }
        mock_AnsibleModule.return_value.run_command.return_value = (0, 'python hold', '')

        dpkg_selections.main()
        assert mock_AnsibleModule.return_value.exit_json.called
        assert mock_Ans

# Generated at 2022-06-13 05:20:49.133244
# Unit test for function main
def test_main():

    # Fail on missing or invalid arguments
    with pytest.raises(SystemExit):
        main()

    # Fail on missing or invalid arguments
    with pytest.raises(SystemExit):
        main(dict(name='apache2', selection='test'))

    # Fail on missing or invalid arguments
    with pytest.raises(SystemExit):
        main(dict(name='apache2', selection=' install'))

    # Fail on missing or invalid arguments
    with pytest.raises(SystemExit):
        main(dict(name='apache2', selection='install '))

    # Fail on missing or invalid arguments
    with pytest.raises(SystemExit):
        main(dict(name='apache2', selection='install'))

    # Fail on missing or invalid arguments

# Generated at 2022-06-13 05:20:53.073154
# Unit test for function main
def test_main():
    # Test no change
    module = AnsibleModule(
            argument_spec=dict(
                name='test-package',
                selection='hold'
            ),
            supports_check_mode=False
    )
    main()

    # Test change
    module = AnsibleModule(
            argument_spec=dict(
                name='test-package',
                selection='install'
            ),
            supports_check_mode=False
    )
    main()

    module = AnsibleModule(
            argument_spec=dict(
                name='test-package',
                selection='hold'
            ),
            supports_check_mode=False
    )
    main()

