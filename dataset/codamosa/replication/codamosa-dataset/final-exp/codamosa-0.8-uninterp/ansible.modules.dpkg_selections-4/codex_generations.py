

# Generated at 2022-06-13 05:13:01.184667
# Unit test for function main
def test_main():
    assert main() == True


# Generated at 2022-06-13 05:13:10.551752
# Unit test for function main
def test_main():
    import os
    import sys
    import signal
    import subprocess

    # Build dict of test cases.
    test_cases = []
    env = os.environ.copy()
    env['ANSIBLE_MODULE_ARGS'] = "{'name': 'python', 'selection': 'hold'}"
    env['ANSIBLE_CHECK_MODE'] = "True"
    test_cases.append((env, 1, 0, 'install'))

    # Iterate through test cases, and run function main with each.
    executor = os.path.join(os.path.dirname(__file__), 'executor.py')
    sys.path.insert(0, os.path.dirname(executor))

# Generated at 2022-06-13 05:13:15.481808
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 05:13:24.427676
# Unit test for function main
def test_main():
    test_args = [
        '-s', 'name=python',
        '-s', 'selection=hold'
    ]

    # Mock the return value of get_bin_path to always return dpkg.
    def mock_get_bin_path(path, required=False, opt_dirs=[]):
        return 'dpkg'
    mock_get_bin_path.old_get_bin_path = AnsibleModule.get_bin_path
    AnsibleModule.get_bin_path = mock_get_bin_path

    # Mock the function that runs the command so we can check its return.
    def mock_run_command(cmd, check_rc=True):
        mock_stdout = 'python hold'
        return (0, mock_stdout, '')

# Generated at 2022-06-13 05:13:33.247994
# Unit test for function main
def test_main():
    module_args = {
      "name": "python",
      "selection": "hold"
    }
    module = AnsibleModule(argument_spec={}, supports_check_mode=True, **module_args)

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
        module.exit_json(changed=changed, before=current, after=selection)

    module

# Generated at 2022-06-13 05:13:35.522164
# Unit test for function main
def test_main():
    assert main() == 'main'

# Generated at 2022-06-13 05:13:43.979067
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
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
        return (changed, current, selection)

# Generated at 2022-06-13 05:13:45.703801
# Unit test for function main
def test_main():
    ansible_module_main(['', ''], None)

# Generated at 2022-06-13 05:13:55.705649
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, 'python hold', '')):
        with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, '', '')):
            M = AnsibleModule(
                argument_spec=dict(
                    name=dict(required=True),
                    selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
                ),
                supports_check_mode=True,
            )
            main()
            assert M.exit_json.called
            assert M.exit_json.call_args == call(changed=False, before='hold', after='hold')

# Generated at 2022-06-13 05:14:02.603535
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
    #   

# Generated at 2022-06-13 05:14:31.017482
# Unit test for function main

# Generated at 2022-06-13 05:14:33.131739
# Unit test for function main
def test_main():
    response = main()
    Assert(response, "")


# Generated at 2022-06-13 05:14:40.375102
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    assert module.params['name'] is not None
    assert module.params['selection'] is not None
    assert AnsibleModule.run_command is not None
    assert AnsibleModule.get_bin_path is not None

# Generated at 2022-06-13 05:14:40.960703
# Unit test for function main
def test_main():
    assert main() == True

# Generated at 2022-06-13 05:14:45.501211
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'name': 'python',
        'selection': 'hold',
    }, check_mode=True)
    dpkg = module.get_bin_path('dpkg', True)
    module.run_command([dpkg, '--set-selections'], data="python hold", check_rc=True)
    main()
    # Test that check mode is on
    assert module.check_mode

# Generated at 2022-06-13 05:14:49.830187
# Unit test for function main
def test_main():
    assert main(['python', '--get-selections', 'python']) == 'install'
    assert main(['python-apt', '--get-selections', 'python-apt']) == 'hold'

# Generated at 2022-06-13 05:14:59.494617
# Unit test for function main
def test_main():
    import mock
    import os
    m = mock.mock_open(read_data='python hold')
    m.return_value.readline.return_value = 'python hold'
    m.return_value.readline.return_value = 'python hold\n'
    m.return_value.__iter__.return_value = ['python hold']
    m.return_value.__iter__.return_value = ['python hold\n']
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        mock_class = mock_module.return_value.__class__
        mock_class.fail_json = mock.MagicMock()
        mock_class.fail_json.side_effect = SystemExit
        mock_class.run_command = mock.MagicMock()


# Generated at 2022-06-13 05:15:07.878473
# Unit test for function main
def test_main():
    # be sure to update the module_utils/basic.py file to have the correct load_platform_subclass variable
    module_path="/usr/share/ansible/module_utils/basic.py"
    f = open(module_path, "r")
    contents = f.read()
    f.close()

    if "needs_platform_subclass = False" in contents:
        f = open(module_path, "w")
        contents = contents.replace("needs_platform_subclass = False", "needs_platform_subclass = True")
        f.write(contents)
        f.close()

    # import the module in here (tests.py is a separate file)
    from dpkg_selections import main

    # global variables that get changed by the module functions
    global dpkg
    global name
    global selection
   

# Generated at 2022-06-13 05:15:19.054579
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common.process import get_bin_path_input_data
    from ansible.module_utils.common.systemd import init

    ansible_module = basic.AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    ansible_module.get_bin_path = get_bin_path

    dpkg = '/usr/bin/dpkg'

# Generated at 2022-06-13 05:15:21.479566
# Unit test for function main
def test_main():
    # assert main('python', 'deinstall') == {'changed': True, 'before': 'hold', 'after': 'deinstall'}
    pass

# Generated at 2022-06-13 05:15:41.102539
# Unit test for function main
def test_main():
    # Test a basic call to the module to see if the package
    # gets set to a selection.

    # TODO there's no reliable way to test that the package
    # is set to hold. This doesn't really change the
    # functionality, but it would be nice to be able to test it.
    import mock
    import sys
    sys.modules['ansible.module_utils.basic'] = mock.MagicMock()

    from ansible.modules.packaging.os.dpkg_selections import main
    assert main() == {
        'changed': True,
        'before': 'install',
        'after': 'hold'
    }

# Generated at 2022-06-13 05:15:50.143523
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

# Generated at 2022-06-13 05:15:51.815238
# Unit test for function main
def test_main():
  print('Hola')
  assert 'hello' == 'hello'

# Generated at 2022-06-13 05:16:01.593618
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

# Generated at 2022-06-13 05:16:06.218596
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.packages import aptlib
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    from collections import namedtuple
    from ansible import context
    import json

    module = namedtuple('module', 'params')
    aptlib.do_update = lambda _: False
    context.CLIARGS = namedtuple('CLIARGS', 'connection check diff')
    context.CLIARGS.connection = 'local'
    context.CLIARGS.check = False
    context.CLIARGS.diff = False

# Generated at 2022-06-13 05:16:06.732017
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:16:07.855828
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:16:16.218739
# Unit test for function main
def test_main():
    m = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ))
    # Input parameters
    m.params = dict(
                    name='python',
                    selection='hold',
                    )
    selection_out = 'python install'
    selection_err = ''
    main()
    assert selection_out == m.run_command(m.get_bin_path('dpkg', True), '--get-selections', m.params['name'])[1]
    assert selection_err == m.run_command(m.get_bin_path('dpkg', True), '--get-selections', m.params['name'])[2]

# Generated at 2022-06-13 05:16:19.106515
# Unit test for function main
def test_main():
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    assert rc == out

# Generated at 2022-06-13 05:16:19.549109
# Unit test for function main
def test_main():
    assert False

# Generated at 2022-06-13 05:17:02.728100
# Unit test for function main
def test_main():
    dpkg_selections_obj = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg = dpkg_selections_obj.get_bin_path('dpkg', True)

    name = 'python'
    selection = 'install'

    # Get current settings.
    dpkg_selections_obj.run_command([dpkg, '--get-selections', name], check_rc=True)
    dpkg_selections_obj.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)

# Generated at 2022-06-13 05:17:11.318284
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

# Generated at 2022-06-13 05:17:23.446781
# Unit test for function main
def test_main():
    args = dict(
        name=dict(required=True, type='str'),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True, type='str')
    )
    check_mode=True,
    supports_check_mode=True
    module = AnsibleModule(argument_spec=args, supports_check_mode=True)
    module.check_mode = True
    dpkg = '/usr/bin/dpkg'
    module.get_bin_path = lambda *args, **kwargs: dpkg
    module.run_command = lambda *args, **kwargs: (0, 'python install', '')

    # Test case 1 - current is 'install'
    name = 'python'
    selection = 'hold'
    current = 'install'

# Generated at 2022-06-13 05:17:23.934742
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:17:33.902013
# Unit test for function main
def test_main():
    test_url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks/2'
    test_data = {'title':'Read a book', 'description':'The Raven', 'done':False}
    test_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    response = requests.put(test_url, data=json.dumps(test_data), headers=test_headers)
    assert response.status_code == 200
    assert response.json['task']['title'] == 'Read a book'
    assert response.json['task']['description'] == 'The Raven'
    assert not response.json['task']['done']


# Generated at 2022-06-13 05:17:42.289970
# Unit test for function main
def test_main():
    target = DpkgSelectionModule()
    target.warn = MagicMock()
    target.fail_json = MagicMock()
    target.exit_json = MagicMock()
    target.run_command = MagicMock()
    target.get_bin_path = MagicMock()

    target.run_command.return_value = (0, 'python install', '')
    target.get_bin_path.return_value = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dpkg')

    target.main()
    assert target.exit_json.called
    assert not target.fail_json.called
    assert not target.warn.called

    target.params = dict(
        name='python',
        selection='hold',
    )
    target.main()


# Generated at 2022-06-13 05:17:53.205007
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True),
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

# Generated at 2022-06-13 05:18:00.980535
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import filecmp
    import ansible.module_utils.basic

    test_directory = tempfile.mkdtemp(prefix='ansible_test_dpkg_selections_')
    this_directory = os.path.dirname(os.path.realpath(__file__))

    test_var = {
        'name': 'python',
        'selection': 'hold'
    }

    test_rc = 0
    test_stdout = b'python hold\n'
    test_stderr = b''

    class TestModule(object):
        def __init__(self, ansible_args):
            self.ansible_args = ansible_args

        def get_bin_path(self, arg, required=False):
            return test_directory


# Generated at 2022-06-13 05:18:07.806799
# Unit test for function main
def test_main():

    class MockedModule(object):
        pass

    module = MockedModule()
    module.params = {'name': 'apache2', 'selection': 'hold'}
    module.get_bin_path = lambda x, default: default and '/bin/dpkg'

    class MockedReturnCode(object):
        pass

    rc = MockedReturnCode()
    rc.rc = 0

    class MockedRunCommand(object):
        def __call__(self, *args, **kwargs):
            if args[0] == ['/bin/dpkg', '--get-selections', 'apache2']:
                return rc, "apache2 hold\n", ''
            else:
                assert args[0] == ['/bin/dpkg', '--set-selections']

# Generated at 2022-06-13 05:18:16.959254
# Unit test for function main
def test_main():

    # Remove if already present.
    patched_modules = patch.dict(ansible.module_utils.basic.MODULES, dpkg={})
    patched_run_command = patch.object(ansible.module_utils.basic.AnsibleModule, 'run_command')
    patched_check_mode = patch.object(ansible.module_utils.basic.AnsibleModule, 'check_mode')
    patched_exit_json = patch.object(ansible.module_utils.basic.AnsibleModule, 'exit_json')
    try:
        from ansible.modules.system import dpkg_selections
    except ImportError:
        dpkg_selections = sys.modules[__package__ + '.dpkg_selections']

    # Construct required objects

# Generated at 2022-06-13 05:19:09.996379
# Unit test for function main
def test_main():
    import pytest

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path

    # Get binaries
    dpkg = get_bin_path('dpkg', True)

    def run_command_func(module, cmd, check_rc=True, data=None):
        if cmd == [dpkg, '--get-selections', 'python']:
            import os
            if os.path.exists('/usr/bin/python'):
                out = "python install\n"
            else:
                out = ""
            return 0, out, ""
        elif cmd == [dpkg, '--set-selections']:
            print(data)
            return 0, "", ""
        else:
            return 1


# Generated at 2022-06-13 05:19:15.747993
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True, type='str')
        ),
        supports_check_mode=True,
        #ansible_facts={'platform': 'debian'}
    )
    module.exit_json = exit_json
    main()

# Generated at 2022-06-13 05:19:23.442357
# Unit test for function main
def test_main():
    import sys
    import json
    import os
    import subprocess
    data = json.loads(sys.stdin.read())
    name = data['name']
    selection = data['selection']
    current = 'hold'
    test_string = "\n".join([
        "%s deinstall" % name,
        "%s install" % name,
        "%s hold" % name,
        "%s install" % name,
        "%s purge" % name,
        "%s install" % name
    ])
    p = subprocess.Popen(['dpkg', '--set-selections'], stdin=subprocess.PIPE)
    p.stdin.write(test_string.encode('utf8'))
    p.stdin.close()

# Generated at 2022-06-13 05:19:24.289784
# Unit test for function main
def test_main():
    assert main() == True


# Generated at 2022-06-13 05:19:24.800541
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:19:32.643208
# Unit test for function main
def test_main():
    
    testargs = [ 'ansible',
                 '-m',
                 'dpkg_selections',
                 '-a',
                 'name=brian',
                 '-a',
                 'selection=install'
               ]

    import mock
    import sys
    import os
    import sys
    import mock
    with mock.patch('os.path.exists') as mock_path_exists:
        mock_path_exists.return_value = True

        with mock.patch.dict('sys.modules', {'ansible': mock.Mock()}):
            from ansible.module_utils.basic import AnsibleModule
            from ansible.module_utils import action_common_attributes
            from ansible.module_utils.action_common_attributes import ActionCommonAttributes

# Generated at 2022-06-13 05:19:41.570455
# Unit test for function main
def test_main():
    # Test if the module should return a changed
    # status with when changing the selection state
    # of a package that is not set rather than
    # installed
    assert main({
        'name': 'hello',
        'selection': 'install'
    }) == {
        'changed': True
    }

    # Test that the module should not return a changed
    # status if it is already set
    assert main({
        'name': 'hello',
        'selection': 'install'
    }) == {
        'changed': False
    }

# Generated at 2022-06-13 05:19:42.892836
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:19:46.956719
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    name = 'httpd'
    selection = 'install'

    def run_command_side_effect(cmd, data=None, check_rc=False, close_fds=True, executable=None, data_stderr=False):
        # Get current settings.
        if cmd == ['/usr/bin/dpkg', '--get-selections', name]:
            if data == None:
                return (0, '%s install' % name, '')

# Generated at 2022-06-13 05:19:57.729072
# Unit test for function main
def test_main():
    # We will be using dpkg_selections as the module
    dpkg_selections = 'dpkg_selections'

    # We will be using /tmp/ansible_dpkg_selections_payload as our POST payload file
    test_payload = '/tmp/ansible_dpkg_selections_payload'

    # Create the POST payload file
    open(test_payload, 'wb').write(b"\n")

    # The arguments for ansible.module_utils.basic.AnsibleModule
    module_args = dict(
        name=dict(required=True),
        selection=dict(required=True),
    )

    # The return values for ansible.module_utils.basic.AnsibleModule

# Generated at 2022-06-13 05:22:18.738797
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:22:20.177269
# Unit test for function main
def test_main():
    module = AnsibleModu

# Generated at 2022-06-13 05:22:21.237882
# Unit test for function main
def test_main():
    real_main()

# Generated at 2022-06-13 05:22:33.608489
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

# Generated at 2022-06-13 05:22:35.859326
# Unit test for function main
def test_main():
    print("No unit tests to run")

# Generated at 2022-06-13 05:22:36.837630
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:22:38.962688
# Unit test for function main
def test_main():
    test_1()
    test_2()
    test_3()
    test_4()

# Generated at 2022-06-13 05:22:50.802876
# Unit test for function main
def test_main():
    # Test with no change
    module = AnsibleModule(argument_spec={'name': {'required': True}, 'selection': {'choices': ['install', 'hold', 'deinstall', 'purge'], 'required': True}}, supports_check_mode=True)
    dpkg = module.get_bin_path('dpkg', True)
    name = module.params['name']
    selection = module.params['selection']
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
    changed = current != selection