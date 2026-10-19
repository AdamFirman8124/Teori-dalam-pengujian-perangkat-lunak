

# Generated at 2022-06-13 05:13:02.133793
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:13:11.033462
# Unit test for function main
def test_main():
    content = '''
from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''

# Generated at 2022-06-13 05:13:14.653378
# Unit test for function main
def test_main():
    # Call main with a name (with no action), return code should be 2
    args = dict(name='test', selection='hold')
    rc, out, err = main(args)
    assert rc == 2

# Generated at 2022-06-13 05:13:24.009484
# Unit test for function main
def test_main():
    try:
        import tempfile
        import os
    except ImportError:
        # python <= 2.5
        import shutil
        import sys
        import tempfile
        import os

    tmp_file = tempfile.mkstemp()[1]
    os.environ['DPKG_MAINTSCRIPT_NAME'] = tmp_file
    os.environ['DPKG_MAINTSCRIPT_PACKAGE'] = 'dpkg_selections'
    os.environ['DPKG_MAINTSCRIPT_PACKAGE'] = 'dpkg_selections'

    # Unit test for function main
    def test_main():
        main()
        fd = open(tmp_file, 'r')
        file_content = fd.read()
        fd.close()

# Generated at 2022-06-13 05:13:32.983388
# Unit test for function main
def test_main():
    # Import here try to be more friendly for testing
    import ansible.modules.system.dpkg_selections as dpkg_selections

    # test run on a debian wheezy
    # https://github.com/ansible/ansible/pull/17855/files#diff-2a3a8440f5e5ab6e3e063d57110902d6L227
    # https://github.com/ansible/ansible/pull/17855/files#diff-2a3a8440f5e5ab6e3e063d57110902d6L228
    args = dict(
        name='apache2',
        selection='hold',
    )

# Generated at 2022-06-13 05:13:43.350981
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

# Generated at 2022-06-13 05:13:54.807789
# Unit test for function main
def test_main():
    argv = ['--name', 'python', '--selection', 'hold']

    ansible_module_mock = AnsibleModuleMock(argument_spec={'name':dict(required=True), 'selection':dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)}, supports_check_mode=True)
    ansible_module_mock.get_bin_path = MagicMock(return_value='/usr/bin/dpkg')

    # get current settings.
    rc = 0
    out = "python\thold\t+\n"
    err = ''
    ansible_module_mock.run_command = MagicMock(return_value=(rc, out, err))

    main()

    # Assert that some other thing is called.
    ansible_module_m

# Generated at 2022-06-13 05:14:01.798312
# Unit test for function main
def test_main():
    inp_name = 'python'
    inp_selection = 'hold'
    inp_check_mode = False
    inp_changed = True
    inp_before = 'install'
    inp_after = 'hold'
    inp_run_command_rc = True

    old_rc = module.run_command
    old_mock_check_output = module.mock_check_output
    old_mock_check_mode = module.mock_check_mode
    module.run_command = lambda *_, **__: (True, '', '')
    module.mock_check_output = True
    module.mock_check_mode = True


# Generated at 2022-06-13 05:14:02.252978
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:14:03.451439
# Unit test for function main
def test_main():
    dpkg_selections_module_main("name=python selection=hold")

# Generated at 2022-06-13 05:14:18.873178
# Unit test for function main
def test_main():
    print("Unit test for function main")
    # Return value for a positive result for the action
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

   

# Generated at 2022-06-13 05:14:30.060250
# Unit test for function main
def test_main():
    # Setup mocks for our test.
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    # Mock some responses, and set the names up.
    module.run_command.return_value = 0, "python install\n", ""
    module.params = dict(
        name="python",
        selection="deinstall",
    )

    # Run the module.
    main()

    # Check to see if the methods we are expecting to call actually get called.
    assert module.run_command.call_count == 2



# Generated at 2022-06-13 05:14:38.503563
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
        check_invalid_arguments=False,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True, no_log=True)

    if not out:
        current = 'not present'
    else:
        current = out.split()[1]


# Generated at 2022-06-13 05:14:44.204918
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
    current = 'install'
    changed = True
    selection = 'hold'
    rc = module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)
    assert rc, 'Should return 0 if successful'
    assert name == module.params['name']
    assert selection == module.params['selection']

# Generated at 2022-06-13 05:14:47.853844
# Unit test for function main
def test_main():
    try:
        main()
        test_main.called = True
        raise Exception('main() did not exit on AnsibleModule fail.')
    except AnsibleModuleExit:
        pass

# Generated at 2022-06-13 05:15:01.408842
# Unit test for function main
def test_main():
    get_bin_path_mock = mock.Mock(return_value="dpkg")
    get_bin_path_orig = ansible_pkg.get_bin_path
    dpkg_mock = mock.Mock()
    dpkg_mock.configure_mock(**{
        "run_command.return_value": (0, 'python hold', ''),
    })
    run_command_orig = ansible_pkg.run_command
    ansible_pkg.get_bin_path = get_bin_path_mock
    ansible_pkg.run_command = dpkg_mock
    main({"name": "python", "selection": "hold"})
    ansible_pkg.get_bin_path = get_bin_path_orig
    ansible_pkg.run_command = run_command_

# Generated at 2022-06-13 05:15:05.254001
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

test_main()

# Generated at 2022-06-13 05:15:06.892015
# Unit test for function main
def test_main():
    """
    This function is used to unit test the main function.
    """

# Generated at 2022-06-13 05:15:18.734148
# Unit test for function main
def test_main():
    new_stdout = StringIO()
    new_stderr = StringIO()
    # the following 3 lines were copied from module "apt".  I think it sets
    # the standard output and error to some buffer so we can capture the output
    with contextlib.redirect_stdout(new_stdout):
        with contextlib.redirect_stderr(new_stderr):
            with patch.dict(os.environ, {'LANG': 'C', 'LC_ALL': 'C'}):
                # do the thing you want here.  For example:
                main()
                # print()
                # print("my stdout", new_stdout.getvalue())
                # print("my stderr", new_stderr.getvalue())
            out_string = new_stdout.getvalue()

# Generated at 2022-06-13 05:15:26.543298
# Unit test for function main
def test_main():
    # Test with all valid inputs
    module = AnsibleModule(
        argument_spec={
            'name': dict(required=True),
            'selection': dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        },
        supports_check_mode=True,
    )

    module.params = {'name': 'test_package',
                     'selection': 'hold'}
    out = module.run_command(["echo $PATH"], check_rc=True)
    assert not out[2]


# Test with all valid inputs

# Generated at 2022-06-13 05:15:48.106314
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = MagicMock(return_value=(0, "name\thold\n", ""))
    module.run_command.__name__ = 'run_command'
    dpkg = module.get_bin_path('dpkg', True)
    dpkg = "/bin/dpkg"
    module.get_bin_path = MagicMock(return_value=dpkg)
    module.get_bin_path.__name__ = "get_bin_path"
    module.exit_json = MagicMock()
   

# Generated at 2022-06-13 05:15:49.146294
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'
    assert main() == 0

# Generated at 2022-06-13 05:16:02.408376
# Unit test for function main
def test_main():
    """Unit test for function main"""
    module = AnsiblesModule(argument_spec=dict(name=dict(required=True), selection=dict(choices=[ 'install', 'hold', 'deinstall', 'purge' ], required=True)))

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    current = out.split()[1]
    changed = current != selection
    if module.check_mode or not changed:
        return changed, current, selection

# Generated at 2022-06-13 05:16:12.753760
# Unit test for function main
def test_main():
    import os
    import sys
    import imp
    import argparse
    import tempfile
    import shutil
    import contextlib
    import shlex
    import subprocess

    # install the dpkg_selections module
    module_path = tempfile.mktemp()
    open(module_path, 'w').write(
        open(os.path.join(os.path.dirname(__file__), 'main.py')).read())
    dpkg_selections = imp.load_source('dpkg_selections', module_path)

    with tempfile.TemporaryFile(mode='w') as stderr:
        with contextlib.redirect_stderr(stderr):
            dpkg_selections.main()
            stderr.seek(0)

# Generated at 2022-06-13 05:16:19.774784
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

# Generated at 2022-06-13 05:16:27.422034
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
    )

    name = "python"
    selection = "hold"
    module.params = {"name": name, "selection": selection}

    module.run_command = lambda x, check_rc=True: (0, "pkgname state\n%s %s" % (name, selection), "err")
    module.check_mode = False

    rc, out, err = module.run_command([x for x in module.params['name']], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]


# Generated at 2022-06-13 05:16:27.899085
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:16:37.708628
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

# Generated at 2022-06-13 05:16:48.514630
# Unit test for function main
def test_main():
    diff_mode = True
    # check_mode is not needed here
    check_mode = False
    platform = "ubuntu"

    # check_mode and supports_check_mode are not needed here
    class AnsibleModuleMock(object):
        def __init__(self, argument_spec, check_invalid_arguments, bypass_checks):
            self.params = None
            self.check_mode = check_mode
            self.diff = None

        def get_bin_path(self, arg, required):
            return "/usr/bin/%s" % arg

        def run_command(self, arg, check_rc=True):
            return (0, str(self.params[arg]), "")

    class TestModule(object):
        def __init__(self, module):
            self.module = module


# Generated at 2022-06-13 05:16:54.007262
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ), supports_check_mode=True)

    assert module.check_mode is True
    assert module.params['name'] is not None
    assert module.params['selection'] is not None

# Generated at 2022-06-13 05:17:25.153366
# Unit test for function main
def test_main():

    main()

# Generated at 2022-06-13 05:17:30.678374
# Unit test for function main
def test_main():
    param = {
        'name': 'python',
        'selection': 'hold'
    }

    module_mock = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
    )
    module_mock = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
    )

    dpkg = 'dpkg'

    name = param['name']
    selection = param['selection']

    # Get current settings.

# Generated at 2022-06-13 05:17:40.535554
# Unit test for function main
def test_main():
    # unit test for function main
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


# Generated at 2022-06-13 05:17:51.821467
# Unit test for function main
def test_main():

    # Unit test with check_mode enabled.
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


# Generated at 2022-06-13 05:17:52.551493
# Unit test for function main
def test_main():
    name = package.name
    selection = 'hold'

# Generated at 2022-06-13 05:18:00.549417
# Unit test for function main
def test_main():
    # Mock module.run_command for get_selections
    mock_get = mock.Mock()
    mock_get.return_value = 0, 'python hold', ''

    # Mock module.run_command for set_selections
    mock_set = mock.Mock()
    mock_set.return_value = 0, '', ''

    # Mock the module
    mock_module = mock.Mock()
    # Mock the module.check_mode
    mock_module.check_mode = False
    # Mock the module.exit_json
    mock_module.exit_json = mock.Mock()
    # Mock the module.get_bin_path
    mock_module.get_bin_path = lambda a, b: '/bin/dpkg'
    # Mock the module.run_command

# Generated at 2022-06-13 05:18:05.823288
# Unit test for function main
def test_main():
    import json
    import shlex
    import sys

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


# Generated at 2022-06-13 05:18:07.886965
# Unit test for function main
def test_main():
    from ansible.modules.packaging.os import dpkg_selections


# Generated at 2022-06-13 05:18:08.850160
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:18:17.357898
# Unit test for function main
def test_main():
    import os
    import tempfile

    test_data = ['python install', 'blah deinstall', 'binutils hold']
    test_file = open(tempfile.mkstemp()[1], 'w')
    test_file.write('\n'.join(test_data))
    test_file.flush()

    orig_env = dict(os.environ)
    os.environ['PATH'] = '/bin:/usr/bin'
    mymodule = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    os.environ.clear()
    os.environ.update(orig_env)


# Generated at 2022-06-13 05:19:14.088177
# Unit test for function main
def test_main():
    current = 'hold'
    selection = 'hold'
    cmd = ['/usr/bin/dpkg', '--get-selections', 'python']
    out = ''
    rc = 0
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    class args:
        check_mode = False
    rc = 0
    #Check function return changed=False and test_main.current
    if new_main(current, selection, cmd, out, rc, args, module) == (False, current):
        print('Function return (False, ' + current + ') as expected')

# Generated at 2022-06-13 05:19:22.822272
# Unit test for function main
def test_main():
    import sys
    import inspect
    from mock import MagicMock, patch

    def get_bin_path(name, required=True):
        if name == 'dpkg':
            return 'dpkg'

    module = MagicMock()
    module.exit_json = MagicMock()
    module.check_mode = False
    module.get_bin_path = MagicMock(side_effect=get_bin_path)
    module.run_command.return_value = (0, 'python install', '')

    sys.modules['ansible'] = MagicMock()
    sys.modules['ansible.module_utils.basic'] = MagicMock()
    sys.modules['ansible.module_utils.basic'].AnsibleModule = MagicMock(return_value=module)


# Generated at 2022-06-13 05:19:31.801816
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule:
        def __init__(self, module_args):
            self.module_args = module_args
            self.params = module_args
            pass

    class FakeModuleResult:
        def __init__(self, exit_args, check_rc=True):
            self.exit_args = exit_args
            self.check_rc = check_rc
            pass

        def exit_json(self, **kwargs):
            return self.exit_args

        def run_command(self, cmd, **kwargs):
            return self.exit_args
    ####################################################################################
    # test happy path
    ####################################################################################
    module_args = dict(
        name='python',
        selection='hold'
    )
    module_args

# Generated at 2022-06-13 05:19:44.474888
# Unit test for function main
def test_main():
    # Mock module
    module = Mock()
    module.params = {'name': 'python', 'selection': 'hold'}
    module.run_command = Mock()
    # module.run_command.return_value = (0, "python hold", "")
    module.run_command.return_value = (0, "python install", "")
    #module.run_command.return_value = (0, "python hold", "")
    module.exit_json = Mock()
    module.check_mode = True

    main()
    module.exit_json.assert_called_with(changed=False, before=u'install', after=u'hold')
    #main()
    #module.exit_json.assert_called_with(changed=True, before=u'hold', after=u'install')
    #main()

# Generated at 2022-06-13 05:19:55.230408
# Unit test for function main
def test_main():
    class AnsibleExitJson(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    class AnsibleFailJson(Exception):
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return repr(self.value)

    module_mock = None
    fake_rc = None
    fake_out = None
    fake_err = None
    fake_datas = None

    # Note: all following methods must be called from context managers, e.g.:
    # with AnsibleExitJson(42):
    #     do_stuff()

    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs

# Generated at 2022-06-13 05:19:56.450639
# Unit test for function main
def test_main():
    out = main()
    print(out)
    assert True

# Generated at 2022-06-13 05:20:06.994076
# Unit test for function main
def test_main():
    fields = {}
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.params = fields
    main()
    # Changed is True, as we assume the package is not already set to the same selection
    assert module.params['changed'] == True
    module.params['selection'] = 'hold'
    main()
    # Changed is False, as we assume the package is already set to the selection
    assert module.params['changed'] == False
    module.params['name'] = 'notexist'
    main()
    # Package does not exist previously and no change made,
    # so changed is False


# Generated at 2022-06-13 05:20:14.967394
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

# Generated at 2022-06-13 05:20:15.411721
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:20:17.600142
# Unit test for function main

# Generated at 2022-06-13 05:22:33.689030
# Unit test for function main
def test_main():
    assert main() == 0
# If a unit test throws an exception then the test fails
#     try:
#         assert main()
#     except Exception as e:
#         assert False

# Generated at 2022-06-13 05:22:44.172146
# Unit test for function main
def test_main():
    # Test module build
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    name = module.params['name']
    selection = module.params['selection']

    dpkg = module.get_bin_path('dpkg', True)

    # Test module run
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:22:45.582118
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """
    pass

# Generated at 2022-06-13 05:22:46.686812
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-13 05:22:47.306540
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:22:52.027372
# Unit test for function main
def test_main():
    current = 'hold'
    selection = 'deinstall'
    out = '%s %s' % (name, current)
    dpkg = 'dpkg'
    module = basic.AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:22:57.062311
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import subprocess

    def run(cmd):
        (rc, out, err) = module.run_command(cmd, check_rc=True)
        print(cmd, rc, out, err)

    def set_selections(selections):
        module.run_command([dpkg, '--set-selections'], data=selections, check_rc=True)

    def get_selections():
        rc, out, err = module.run_command([dpkg, '--get-selections'], check_rc=True)
        # Set up a dictionary with the package selections.
        selections = {}
        for line in out.splitlines():
            if not line:
                continue
            (package, selection) = line.split()
            selections[package] = selection
       