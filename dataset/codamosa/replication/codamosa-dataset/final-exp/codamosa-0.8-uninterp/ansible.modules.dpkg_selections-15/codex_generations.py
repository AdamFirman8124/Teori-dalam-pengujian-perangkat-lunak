

# Generated at 2022-06-13 05:13:11.646655
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

# Generated at 2022-06-13 05:13:12.173700
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:13:22.658762
# Unit test for function main
def test_main():
    import sys
    import os.path
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule_load_params, AnsibleModule_dump_result
    from ansible.module_utils.six import StringIO

    sys.path.append(os.path.join(os.path.dirname(__file__), '../library'))
    import __main__

    module_name = 'test_module'
    name = 'testpkg'
    selection = 'hold'

    test_module_args = {
        'name':name,
        'selection':selection
    }


# Generated at 2022-06-13 05:13:31.897756
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

# Generated at 2022-06-13 05:13:34.078049
# Unit test for function main
def test_main():
    assert main() == {'changed': False, 'after': 'hold', 'before': 'hold'}

# Generated at 2022-06-13 05:13:37.672970
# Unit test for function main
def test_main():
    # Run function main
    results = main()

    # Assert that function main is supposed to return a JSON string in the format of a dictionary
    assert type(results) == dict

# Generated at 2022-06-13 05:13:41.610186
# Unit test for function main
def test_main():
    testcases = [
        {'name': 'ansible', 'selection': 'install', 'changed': False},
        {'name': 'ansible', 'selection': 'hold', 'changed': True},
    ]
    for testcase in testcases:
        name, selection, changed = list(testcase.values())
        assert main(name, selection) == changed

# Generated at 2022-06-13 05:13:53.563174
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

    def get_selections(name):
        rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
        if not out:
            current = 'not present'
        else:
            current = out.split()[1]
        return current

    module.params['name'] = "python"
    module.params['selection'] = "hold"


# Generated at 2022-06-13 05:14:01.111551
# Unit test for function main
def test_main():

    import os
    import tempfile

    def module_run_command(command, data='', check_rc=True, pass_fds=None):
        '''Fake implementation of run_command to allow testing.'''

        # Handle dpkg --get-selections.
        if command[0] == dpkg and command[1] == '--get-selections':
            if command[2] in selections:
                return (0, '%s %s' % (command[2], selections[command[2]]), '')
            else:
                return (0, '', '')

        # Handle dpkg --set-selections.
        if command[0] == dpkg and command[1] == '--set-selections':
            for line in data.strip().split('\n'):
                pkg, sel = line.strip().split

# Generated at 2022-06-13 05:14:09.301922
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

# Generated at 2022-06-13 05:14:18.778107
# Unit test for function main
def test_main():
    assert main() == 'K'


# Generated at 2022-06-13 05:14:29.951588
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    # Create a fake dpkg for testing.
    module.run_command = lambda args, **kwargs: ("test", "fake output", "fake error")
    module.exit_json = lambda **kwargs: None

    # Check mode will run the checks, but not the command.
    module.params = {
        'name': 'test',
        'selection': 'test',
    }
    module.check_mode = True
    main()
    assert module.called == 'check'

    # Regular run will run the checks and then the command.
    module.params = {
        'name': 'test',
        'selection': 'test',
    }
    module.check_mode = False
    main()
    assert module.called == 'run'


# Generated at 2022-06-13 05:14:35.553294
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.exit_json(changed=True)


# Generated at 2022-06-13 05:14:36.142564
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:14:45.468465
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

# Generated at 2022-06-13 05:14:48.398235
# Unit test for function main
def test_main():
    test_object = DpkgSelections()
    try:
        test_object.main()
    except Exception as e:
        assert False, str(e)

# Generated at 2022-06-13 05:15:01.646949
# Unit test for function main
def test_main():
    import platform
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

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

# Generated at 2022-06-13 05:15:05.129920
# Unit test for function main
def test_main():
    args = {'name':'python', 'selection':'hold'}
    main(args)

# Generated at 2022-06-13 05:15:06.776774
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'
    assert main()

# Generated at 2022-06-13 05:15:18.706002
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

# Generated at 2022-06-13 05:15:40.312781
# Unit test for function main
def test_main():
    import sys
    import os
    import shlex
    from ansible.module_utils.basic import AnsibleModule

    try:
        from ansible.modules.system import dpkg_selections
    except ImportError:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from ansible.modules.system import dpkg_selections

    fake_module_class = AnsibleModule({
        'check_mode': False,
        'diff_mode': False,
        'name': 'python',
        'selection': 'hold'
    }, check_invalid_arguments=False)
    path = os.path.dirname(os.path.abspath(dpkg_selections.__file__))
    sys.path.insert(0, path)
    dpkg_

# Generated at 2022-06-13 05:15:49.869142
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

# Generated at 2022-06-13 05:16:00.642972
# Unit test for function main
def test_main():
    import os
    import datetime
    import getpass
    import time
    import json
    import platform
    import subprocess

    import ansible.constants as C
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import is_sequence

    from ansible.module_utils._text import to_bytes, to_text

    from ansible.module_utils.basic import AnsibleModule

    argument_spec = dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    )

    module_name = 'dpkg_selections'
    module = AnsibleModule(
        argument_spec,
        supports_check_mode=True,
    )

    name = module.params

# Generated at 2022-06-13 05:16:08.529128
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

# Generated at 2022-06-13 05:16:16.719123
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
    )

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)
    module.exit_json

# Generated at 2022-06-13 05:16:25.947773
# Unit test for function main
def test_main():
    # Mock an ansible module
    import mock
    import platform
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = mock.Mock(return_value=(0, 'python hold', ''))
    if platform.system() == 'Linux':
        module.get_bin_path = mock.Mock(return_value='/usr/bin/dpkg')

# Generated at 2022-06-13 05:16:31.344257
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

# Generated at 2022-06-13 05:16:41.596046
# Unit test for function main
def test_main():
    test_arguments = dict(
        name='python',
        selection='hold'
    )
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = test_module.params['name']
    selection = test_module.params['selection']

    # Get current settings.
    rc, out, err = test_module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current

# Generated at 2022-06-13 05:16:50.179084
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


# Generated at 2022-06-13 05:17:00.264056
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

# Generated at 2022-06-13 05:17:33.204752
# Unit test for function main
def test_main():
    assert True


# Generated at 2022-06-13 05:17:41.954465
# Unit test for function main
def test_main():
    class Object(object):
        pass

    # Check parameters
    arguments = Object()
    arguments.name = 'test-package'
    arguments.selection = 'hold'

    m = Object()
    m.params = arguments
    m.check_mode = True

    from ansible.module_utils.basic import AnsibleModule
    executable = AnsibleModule(argument_spec=dict())
    executable.get_bin_path = lambda name, required=False: '/bin/' + name  # noqa
    m.get_bin_path = executable.get_bin_path

# Generated at 2022-06-13 05:17:47.632856
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    rc, out, err = main()
    module.exit_json(rc=rc, output=out, error=err)

# Generated at 2022-06-13 05:17:54.868229
# Unit test for function main
def test_main():
    # prepare the test environment
    import ansible.module_utils.basic
    import ansible.module_utils.ansible_release
    import sys
    import os
    import tempfile
    from subprocess import call
    from subprocess import check_output
    from subprocess import CalledProcessError
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.action_common import AnsibleModuleAction

    # variables used for the tests
    debug = "AnsibleModule.debug()"
    check_mode = True    

# Generated at 2022-06-13 05:17:59.629053
# Unit test for function main
def test_main():
    import os
    import tempfile
    os.environ['LC_ALL'] = "C"
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
    out = "python package_type selection_type\n"
    with tempfile.TemporaryFile(mode='w+') as f:
        f.write(out)
        f.seek(0)

# Generated at 2022-06-13 05:18:06.828420
# Unit test for function main
def test_main():
    name = "python"
    selection = "hold"

    example_args = dict(
        name=name,
        selection=selection
    )

    # Mock out the basic module
    mock_module = MagicMock()
    mock_module.params = example_args
    mock_module.run_command.return_value = (0, name + "\t" + selection, None)
    mock_module.get_bin_path.return_value = "/usr/bin/dpkg"

    # Turn off exit_json and exit_failure
    mock_module.exit_json = MagicMock()
    mock_module.exit_failure = MagicMock()

    # Run the code
    main()

    # Check to make sure everything that was supposed to happen, happened
    mock_module.get_bin_path.assert_called_once

# Generated at 2022-06-13 05:18:10.360971
# Unit test for function main
def test_main():
    args = dict(
        name="python",
        selection="hold"
    )
    result = main( args, {} )
    assert type(result) is dict
    assert result['changed'] is bool


# Generated at 2022-06-13 05:18:11.069245
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:18:12.396424
# Unit test for function main
def test_main():
    """
    Description: Unit test for function main.
    """
    main()

# Generated at 2022-06-13 05:18:13.021617
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:19:06.574382
# Unit test for function main
def test_main():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.common.file import ensure_tree
    from ansible.module_utils.common import tmp_path
    from ansible.module_utils.common.process import get_bin_path
    # Remove the system dpkg since we run ad-hoc.
    path = get_bin_path('dpkg', False)
    if path:
        os.remove(path)
    # Update the default symlink to our fake dpkg.  To test this we need to fully
    # resolve the path before we remove it.
    path = get_bin_path('dpkg', True)
    base = os.path.dirname(path)
    os.remove(path)
    os.symlink('/usr/bin/dpkg.py', path)
   

# Generated at 2022-06-13 05:19:15.982774
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    assert(changed == True)


# Generated at 2022-06-13 05:19:23.562433
# Unit test for function main
def test_main():
    """
    Test for function main
    """
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


# Generated at 2022-06-13 05:19:24.089398
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:19:32.349156
# Unit test for function main
def test_main():
    # Mock module to return a specific exit code
    class MockModule:
        def __init__(self, **kwargs):
            self.params = kwargs
            self.exit_json = lambda **kw: exit(kw["changed"])

        def get_bin_path(self, *a, **kw):
            return "/usr/bin/dpkg"

        def run_command(self, *a, **kw):
            kw["check_rc"] = True
            return (0, 'python\tinstall', '')

    # Get a mocked module
    module = MockModule(
        name='python',
        selection='hold'
    )

    # Call main with mocked params and exit code
    main()
    assert module.params["name"] == 'python'
    assert module.params["selection"] == 'hold'

# Generated at 2022-06-13 05:19:44.842452
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

# Generated at 2022-06-13 05:19:54.001185
# Unit test for function main
def test_main():
    args = dict(
        name='test_package',
        selection='purge',
    )
    fixture = dict(
        pkg_mock=dict(
            params=args,
            changed=False,
            before='hold',
            after='purge',
        ),
    )

    try:
        pkg = __import__('apt', globals(), locals(), ['pkg'])
        pkg.pkg = fixture['pkg_mock']
    except:
        pass

    pkg = __import__('ansible.modules.packaging.os.dpkg_selections', globals(), locals(), ['pkg'])
    pkg.main()

# Generated at 2022-06-13 05:19:54.551036
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:19:55.076614
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:19:55.595860
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-13 05:22:18.498795
# Unit test for function main
def test_main():
    dpkg = '/usr/bin/dpkg'

    # Test with name and selection.
    args = dict(
        name='python',
        selection='hold',
    )
    rc = main()
    assert rc['changed'] == True
    assert rc['before'] == 'install'
    assert rc['after'] == 'hold'

    # Test with name and selection.
    args = dict(
        name='python',
        selection='hold',
    )
    rc = main()
    assert rc['changed'] == False
    assert rc['before'] == 'hold'
    assert rc['after'] == 'hold'

    # Test with name and selection.
    args = dict(
        name='python',
        selection='hold',
        check_mode=True,
    )
    rc = main()
    assert rc['changed'] == True

# Generated at 2022-06-13 05:22:31.445651
# Unit test for function main
def test_main():

    # Create a mock module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
    )

    # set the return values
    module.run_command.return_value = (0,'python hold','')
    module.run_command.return_value = (0,'','','','','','','','','','','')

# Generated at 2022-06-13 05:22:37.347162
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

# Generated at 2022-06-13 05:22:44.788378
# Unit test for function main
def test_main():
  import mock
  mock_module = mock.MagicMock()
  mock_module.params = {'name': 'python', 'selection': 'hold'}
  mock_module.check_mode = False
  mock_module.run_command.return_value = (
      0,
      'python install\n',
      ''
  )
  main()
  mock_module.run_command.assert_called_with([
      '/usr/bin/dpkg', '--set-selections'
    ],
    data="python hold",
    check_rc=True
  )
  mock_module.exit_json.assert_called_with(
      changed=True,
      before='install',
      after='hold'
  )


# Generated at 2022-06-13 05:22:53.131251
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