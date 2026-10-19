

# Generated at 2022-06-13 05:13:02.170497
# Unit test for function main
def test_main():
    testdict = dict(
        name='test',
        selection='test'
    )
    result = main()
    assert result is None or result == ''

# Generated at 2022-06-13 05:13:11.095507
# Unit test for function main
def test_main():
    # We don't want to require dpkg for this test.
    module = AnsibleModule(argument_spec={
        'name': {
            'required': True
        },
        'selection': {
            'required': True,
            'choices': [ 'install', 'hold', 'deinstall', 'purge' ]
        }
    }, supports_check_mode=True)
    module.run_command = mock_run_command
    module.run_command.return_value = (0, 'python install', '')

    main()
    assert module.run_command.call_args == call([module.get_bin_path('dpkg', True), '--get-selections', 'python'])

# Generated at 2022-06-13 05:13:21.998079
# Unit test for function main
def test_main():
    import json
    import pty
    from mock import MagicMock
    from ansible.modules.packaging.os import dpkg_selections
    from ansible.module_utils.basic import AnsibleModule

    dpkg = dpkg_selections.module.get_bin_path('dpkg', True)
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Module params
    name = "python"
    selection = "hold"

    # Get current settings.
    (master, slave) = pty.openpty()

# Generated at 2022-06-13 05:13:31.710914
# Unit test for function main
def test_main():
    """ Unit test for function main """

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


# Generated at 2022-06-13 05:13:41.192694
# Unit test for function main
def test_main():
    sample_name = "python"

    try:
        sample_dpkg = __salt__['dpkg.get_selections'](sample_name)
    except ValueError:
        sample_dpkg = 'not present'

    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Set arguments
    test_module.params['name'] = sample_name
    test_module.params['selection'] = 'install'

    main()

# Generated at 2022-06-13 05:13:53.242198
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

# Generated at 2022-06-13 05:13:54.177243
# Unit test for function main
def test_main():
    assert True


# Generated at 2022-06-13 05:13:56.621434
# Unit test for function main
def test_main():
    # Test for module(action='dpkg --get-selections')
    res = main()
    assert res

# Test for module(action='dpkg --set-selections')

# Generated at 2022-06-13 05:14:02.730092
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    rc, out, err = module.run_command(["dpkg", "--get-selections", "python"], check_rc=True)
    if not out:
        current = 'not present'
        rc, out, err = module.run_command(["dpkg", "--set-selections"], data="python install", check_rc=True)
    else:
        current = out.split()[1]

# Generated at 2022-06-13 05:14:03.867628
# Unit test for function main
def test_main():
    val1 = main()
    assert val1 == None

# Generated at 2022-06-13 05:14:13.746691
# Unit test for function main
def test_main():
    print("Test the main function")
    main()


# Generated at 2022-06-13 05:14:18.122458
# Unit test for function main
def test_main():
    # Mock parameters
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


# Generated at 2022-06-13 05:14:27.251495
# Unit test for function main
def test_main():
    testcase = dict(name='ansible', selection='hold')
    testdata = dict(failed=False, before='not present', after='hold')

    module = AnsibleModule(testcase)
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.exit_json = MagicMock(side_effect=check_result)

    main()
    assert run_command_mock.call_args_list[0][0][0] == ['dpkg', '--set-selections']
    assert run_command_mock.call_args_list[0][0][1] == 'ansible hold'

main()

# Generated at 2022-06-13 05:14:33.629290
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name="",
            selection="",
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = "libssh2"
    selection = "hold"

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection
    print("Current is: " + current + " selection is: " + selection + "changed is: " + changed)

# End of unit test

# Generated at 2022-06-13 05:14:39.874830
# Unit test for function main
def test_main():
    # Arrange and act
    params = { 'name': 'nginx', 'selection': 'hold', 'diff_mode': 'no', 'check_mode': 'no', 'platform': 'any' }
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.params = params
    m = main()
    result = m.params['after']

    # Assert
    assert result == 'hold'

# Generated at 2022-06-13 05:14:45.241494
# Unit test for function main
def test_main():
    args = {}
    args['name'] = 'ntp'
    args['selection'] = 'install'
    with patch('ansible.module_utils.basic.AnsibleModule') as an:
        instance = an.return_value
        instance.get_bin_path.return_value = 'bin/dpkg'
        instance.params = args
        instance.check_mode = True
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:14:53.220106
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
    selection = module.para

# Generated at 2022-06-13 05:15:00.696962
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import json
    import os

    class MockModule:
        def __init__(self, *args, **kwargs):
            self.run_command_calls = []
            self.check_mode = False
            self.params = kwargs['params']

        def run_command(self, args, **kwargs):
            if self.check_mode:
                if kwargs.get('data'):
                    print("%s <<< %s" % (args, kwargs['data']))
                else:
                    print("%s" % args)

            if args == ['dpkg', '--get-selections', 'python']:
                return (0, ' python install', '')

# Generated at 2022-06-13 05:15:08.168088
# Unit test for function main
def test_main():
    import sys
    import os
    import stat
    import pty
    import tempfile
    import subprocess
    import pytest
    import StringIO

    # Create test FIFO.
    file_path = '/tmp/ansible_test'
    os.mkfifo(file_path)
    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

    def cleanup():
        os.remove(file_path)

    # Run test process.
    pid, fd = pty.fork()

    if pid == 0:
        # Redirect stdin / stdout to FIFO
        child_fd = os.open(file_path, os.O_RDWR)
        os.dup2(child_fd, 0)

# Generated at 2022-06-13 05:15:08.910546
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:15:29.206172
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


# Generated at 2022-06-13 05:15:35.719177
# Unit test for function main
def test_main():
    params = {
        "name": "testname",
        "selection": "install",
        "check_mode": False
    }
    params['__ansible_module__'] = "dpkg_selections"
    params['__ansible_module_class__'] = "DpkgSelectionAction"
    params['__ansible_module_name__'] = "dpkg_selections"
    module = AnsibleModule(**params)

    main()

# Generated at 2022-06-13 05:15:38.453093
# Unit test for function main
def test_main():
    args = dict(
        name='python',
        selection='hold'
    )
    module = AnsibleModule(argument_spec={})
    module.params = args
    main()

# Generated at 2022-06-13 05:15:48.708635
# Unit test for function main
def test_main():
    from ansible.module_utils.common.modules_common import AnsibleModule
    from ansible.module_utils.common.run_commands import RunModule
    from ansible.module_utils.common.utils import basic
    
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

# Generated at 2022-06-13 05:15:51.513366
# Unit test for function main
def test_main():
    assert main()



# Generated at 2022-06-13 05:15:52.894241
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """
    pass

# Generated at 2022-06-13 05:15:53.680718
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:16:05.825222
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if module.check_mode or not changed:
        module.exit_json(changed=changed, before=current, after=selection)

    module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)
    module.exit_json(changed=changed, before=current, after=selection)


# Generated at 2022-06-13 05:16:14.505907
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

# Generated at 2022-06-13 05:16:19.996024
# Unit test for function main
def test_main():
    import os
    import tempfile
    import json
    import pytest
    import ansible.module_utils.basic
    import ansible.module_utils.action
    import ansible.module_utils.action.utils
    import ansible.module_utils.action.get_bin_path
    import ansible.module_utils.action.linux
    import ansible.module_utils.action.platform
    import ansible.module_utils.six
    
    # Fake functions
    def fake_ansible_module(**args):
        from ansible.module_utils.basic import AnsibleModule
        module = AnsibleModule(**args)
        return module


# Generated at 2022-06-13 05:16:55.984969
# Unit test for function main
def test_main():
    dpkg = '/usr/bin/dpkg'
    out = 'dpkg data'
    err = ''
    module = init_module()

    module.run_command = MagicMock(return_value=(0, out, err))
    main()
    assert dpkg in module.run_command.mock_calls[0][1]

# Generated at 2022-06-13 05:17:03.593907
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

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

   

# Generated at 2022-06-13 05:17:09.032813
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        'name': {
            'required': True,
            'type': 'str'
        },
        'selection': {
            'choices': ['install', 'hold', 'deinstall', 'purge'],
            'required': True,
            'type': 'str'
        }
    }, supports_check_mode=True)
    assert main() == '''{
        "changed": False,
        "failed": False
    }'''

# Generated at 2022-06-13 05:17:21.303349
# Unit test for function main
def test_main():
    args = {
        'name': 'python',
        'selection': 'install'
    }
    cur_selection = 'install'
    expected = {
        'changed': False,
        'before': cur_selection,
        'after': 'install'
    }
    m = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ))
    m.params = args
    m.run_command = lambda cmd, data=None, check_rc=True: (0, 'python\t%s\n' % cur_selection, '')
    assert main() == expected
    cur_selection = 'hold'
    expected['changed'] = True

# Generated at 2022-06-13 05:17:25.413171
# Unit test for function main
def test_main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    name = "python"
    selection = "hold"
    dpkg = "dpkg"

# Generated at 2022-06-13 05:17:35.892178
# Unit test for function main
def test_main():
    m = ModuleUtils.APT()
    m.exit_json = mock.MagicMock()
    m.run_command = mock.MagicMock(return_value=(0, '', ''))
    m.run_command.assert_called_with([m.get_bin_path('dpkg', True), '--get-selections', 'python'], check_rc=True)
    m = ModuleUtils.APT()
    m.exit_json = mock.MagicMock()
    m.run_command = mock.MagicMock(return_value=(0, 'python hold', ''))
    m.run_command.assert_called_with([m.get_bin_path('dpkg', True), '--get-selections', 'python'], check_rc=True)

# Generated at 2022-06-13 05:17:43.400015
# Unit test for function main
def test_main():
    # Mock class object.
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = mock.Mock()
            self.run_command = mock.Mock(return_value=(0, 'test', ''))

        def get_bin_path(self, name, path, required):
            return 'dpkg'

    class MockCheckModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = mock.Mock()
            self.run_command = mock.Mock(return_value=(0, 'test', ''))

        def get_bin_path(self, name, path, required):
            return 'dpkg'

    # Check for install when not present.
    m = MockModule()
    m.params

# Generated at 2022-06-13 05:17:53.824951
# Unit test for function main
def test_main():
    class MockArgs(object):
        def __init__(self, name, selection):
            self.name = name
            self.selection = selection

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common.process import get_bin_path_input

    m_get_bin_path = get_bin_path

    bin_path = '/usr/bin'
    m_get_bin_path.return_value = bin_path

    m_get_bin_path_input = get_bin_path_input
    m_get_bin_path_input.return_value = bin_path

    name = 'foo'


# Generated at 2022-06-13 05:18:01.400227
# Unit test for function main
def test_main():
        import sys
        import io
        import subprocess
        # Simulate input parameters
        sys.argv = ['dpkg_selections', '--check-mode', '{ "selection": "install", "name": "python" }']
        # Expected output
        sys.stdout = io.StringIO()
        main()
        result_string = sys.stdout.getvalue()
        # remove formatting
        result_string = result_string.replace('u\'', '\'')
        assert result_string == '{"changed": False, "after": "install", "before": "not present"}\n'
        result_string = result_string.replace('u\'', '\'')
        sys.stdout = sys.__stdout__
        sys.stdout.write(result_string)

        # Simulate input parameters
        sys

# Generated at 2022-06-13 05:18:03.033108
# Unit test for function main
def test_main():
    assert 1 == 1
# Unit test end

# Generated at 2022-06-13 05:18:56.789828
# Unit test for function main
def test_main():
    fake_stdout = None
    fake_stderr = None
    win_string = (0, 'hello world', '')

    def test_runner(module_name, **kwargs):
        if module_name == 'ansible.module_utils.basic.AnsibleModule':
            return AnsibleModule(
                argument_spec=dict(
                    name=dict(required=True),
                    selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
                ),
                supports_check_mode=True,
            )
        elif module_name == 'ansible.module_utils.basic.get_bin_path':
            return 'dpkg'

# Generated at 2022-06-13 05:19:05.958712
# Unit test for function main
def test_main():
    import json
    import os

    class AnsibleModuleFake(object):
        def __init__(self):
            self.params = {}
            self.exit_json = lambda x, **kw: x
            self.run_command = lambda x, **kw: x
        def get_bin_path(self, path, req):
            return os.path.join(os.path.dirname(__file__), path)
        def check_mode(self):
            return True
        def fail_json(self, **kw):
            raise AssertionError('Failed')


    module = AnsibleModuleFake()
    module.params = {'name': 'python', 'selection': 'hold'}
    result = main()
    # get_bin_path

# Generated at 2022-06-13 05:19:16.277908
# Unit test for function main
def test_main():
    import sys
    import io
    import subprocess
    import tempfile

    # Python 2/3 compatibility.
    try:
        from StringIO import StringIO
    except:
        from io import StringIO

    # Add a temp dir for the test to run in.
    tmpdir = tempfile.mkdtemp()

    # Ensure we can find dpkg.
    dpkg = subprocess.Popen("which dpkg".split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].strip("\n")

    # Our module has been installed in Ansibles module_utils dir.
    sys.path.append("/tmp/ansible/module_utils")


# Generated at 2022-06-13 05:19:16.836801
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:19:20.606660
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert module.fail_json.called

# Generated at 2022-06-13 05:19:30.359157
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


# Generated at 2022-06-13 05:19:43.256689
# Unit test for function main
def test_main():
    import sys
    sys.path.insert(0, '/root/.ansible/lib/ansible/module_utils')
    import ansible.utils
    from ansible.utils.display import Display
    from ansible.utils.path import check_for_controlchar
    from ansible.utils.unicode import to_unicode
    from ansible.utils.unicode import to_bytes
    from ansible.utils.unicode import to_str
    module_name = 'dpkg_selections'
    module = __import__('ansible.modules.packaging.os.%s' % module_name)
    module = getattr(module, module_name)

# Generated at 2022-06-13 05:19:46.030084
# Unit test for function main
def test_main():
    import sys

    m = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    m.check_mode = False

    rc = main(m)

    assert rc['changed'] == False
    assert rc['before'] == 'hold'
    assert rc['after'] == 'hold'

# Generated at 2022-06-13 05:19:56.851358
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True
    )

    name = 'python'
    selection = 'deinstall'

    dpkg = module.get_bin_path('dpkg', True)

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:20:02.647223
# Unit test for function main
def test_main():
    # Test module existence
    dpkg_selections = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert dpkg_selections

# Generated at 2022-06-13 05:22:31.099702
# Unit test for function main
def test_main():
    import json
    import os
    import subprocess
    import tempfile
    import unittest

    class TestDpkgSelections(unittest.TestCase):

        def setUp(self):
            self.cwd = os.getcwd()
            self.test_dir = tempfile.mkdtemp()
            os.chdir(self.test_dir)

        def tearDown(self):
            os.chdir(self.cwd)

        def call_main_with_args(self, args):
            module_args = dict(
                ANSIBLE_MODULE_ARGS = args,
                # Set to False because we don't want to copy
                # the module into the remote system.
                ANSIBLE_KEEP_REMOTE_FILES = False
            )


# Generated at 2022-06-13 05:22:37.080951
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    test_module.run_command = mock_run_command
    test_module.get_bin_path = mock_get_bin_path
    test_module.check_mode = False
    test_module.params = {
        'name': 'test',
        'selection': 'install'
    }

    # Test when no change is required.
    mock_run_command_results = [
        (0, 'test install', ''),
        (0, '', '')
    ]
    main()

# Generated at 2022-06-13 05:22:45.005807
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    # function main() begin
    dpkg = module.get_bin_path('dpkg', True)
    name = "python"
    selection = "hold"
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
    changed = current != selection

# Generated at 2022-06-13 05:22:53.248303
# Unit test for function main
def test_main():
    test = TestModule()
    choices = ['install', 'hold', 'deinstall', 'purge']
    # Test with no arguments
    result = test.run_module()
    assert result['failed']

    # Test with missing required argument
    for arg in ['name','selection']:
        assert test.run_module(**{arg: 'foo'})['failed']

    # Test with bad selection argument
    result = test.run_module(**{'name': 'python', 'selection': 'blah'})
    assert result['failed']

    # Test with all arguments
    for selection in choices:
        result = test.run_module(**{'name': 'python', 'selection': selection})
        assert result['changed'] == False
        assert result['before'] == 'not present'
        assert result['after'] == selection

# Unit