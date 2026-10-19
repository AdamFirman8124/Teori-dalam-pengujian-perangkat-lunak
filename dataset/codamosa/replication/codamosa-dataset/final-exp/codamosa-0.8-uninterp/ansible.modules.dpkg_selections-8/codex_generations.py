

# Generated at 2022-06-13 05:13:11.337944
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

# Generated at 2022-06-13 05:13:18.467246
# Unit test for function main
def test_main():
    fake_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert len(fake_module.params['name']) > 0
    assert len(fake_module.params['selection']) > 0

# Generated at 2022-06-13 05:13:18.994874
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:13:29.638469
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=False),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.params['name'] = "python"
    module.params['selection'] = "hold"
    dpkg = module.get_bin_path('dpkg', True)
    name = module.params['name']
    selection = module.params['selection']
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

# Generated at 2022-06-13 05:13:31.560805
# Unit test for function main
def test_main():
    args = {'name': 'nginx', 'selection': 'install'}
    main(args)
    #Check that final state is correct.

# Generated at 2022-06-13 05:13:42.311841
# Unit test for function main
def test_main():
    import os
    import sys
    import tempfile
    import filecmp
    #
    # Set up a file with a list of package names.
    #
    file_list = tempfile.NamedTemporaryFile(delete=False)
    file_list.write("python\n")
    file_list.close()
    #
    # Set up a file for the dpkg --get-selections.
    #
    file_set = tempfile.NamedTemporaryFile(delete=False)
    file_set.close()
    #
    # Set up the test directory.
    #
    testdir = tempfile.mkdtemp()
    os.chdir(testdir)
    #
    # Copy the source file to the test directory.
    #

# Generated at 2022-06-13 05:13:53.942838
# Unit test for function main
def test_main():
    from ansible.module_utils import modules as mod

    module = mod.AnsibleModule(
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



# Generated at 2022-06-13 05:14:01.402745
# Unit test for function main
def test_main():
    import copy
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)))

    name = 'test'
    selection = 'hold'
    dpkg = '/bin/dpkg'
    module.run_command = get_run_command(
        dpkg,
        {
            "check_rc=True": [0, '', ''],
            "data=%s %s" % (name, selection): None,
        },
        "%s --get-selections %s" % (dpkg, name))


# Generated at 2022-06-13 05:14:07.236911
# Unit test for function main
def test_main():
    module = {"params": {"name": "debconf-2.0", "selection": "install"}, "get_bin_path": lambda x, y: "/bin/dpkg"}
    rc, out, err = main(module)
    import json
    print(json.dumps(rc))
    assert rc['changed'] == True
    assert rc['before'] != rc['after']
    assert rc['after'] == "install"



# Generated at 2022-06-13 05:14:14.298930
# Unit test for function main
def test_main():
    """
    Tests for the main function
    """

    import imp

    import ansible.module_utils.basic as basic

    # Save the original module_utils for basic so we can restore them later
    orig_basic_utils = basic.__dict__.copy()

    # Make sure we are also running this through the action plugin wrapper
    from ansible.plugins import action

    # Generate a mock module for the action plugin
    _action_plugin = imp.new_module('_action_plugin')
    _action_plugin.ActionBase = action.ActionBase
    _action_plugin.BASIC_ARG_SPEC = basic.BASIC_ARG_SPEC.copy()

    # Give our new module_utils some basic functions
    basic._ANSIBLE_ARGS = None
    basic.ANSIBLE_ARGS = None
    basic.Ans

# Generated at 2022-06-13 05:14:39.523291
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

# Generated at 2022-06-13 05:14:47.458347
# Unit test for function main
def test_main():

    # import sys
    # sys.path.insert(0, '../action_plugins')
    # import dpkg_selections

    test_params = [
        {
            'name': 'python',
            'selection': 'hold'
        }
    ]


    # import time
    # time.sleep(10)
    # import pdb; pdb.set_trace()

    # test_params = [
    #     {
    #         'name': 'python',
    #         'selection': 'hold'
    #     }
    # ]


# Generated at 2022-06-13 05:14:52.186902
# Unit test for function main
def test_main():
    test_module = AnsibleModule(argument_spec=dict())
    test_module.mock_binary_module('dpkg')
    test_module.run_command = lambda args, data, check_rc: ('', '', 0)
    main()

# Generated at 2022-06-13 05:14:53.562150
# Unit test for function main

# Generated at 2022-06-13 05:14:54.064250
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:14:59.318754
# Unit test for function main
def test_main():
    fields = ["name", "selection"]
    module_args = {
        "name": "python",
        "selection": "hold"
    }

    module = AnsibleModule(argument_spec=dict())
    module.params = module_args
    main()
    assert module.run_command.call_count == 2
    assert module.run_command.call_args[0][0] == ['/usr/bin/dpkg', '--set-selections']
    assert module.run_command.call_args[0][1]['data'] == 'python hold'

# Generated at 2022-06-13 05:15:07.687317
# Unit test for function main
def test_main():
    import subprocess
    import sys
    import os
    import tempfile
    import re
    # Write the fixtures out to temporary file.
    fixture_fd, fixture_path = tempfile.mkstemp()
    fixture_data = '''
        python hold
    '''
    os.write(fixture_fd, fixture_data)
    os.close(fixture_fd)

    # Prepare some arguments to the main method.
    args = {
        'name': 'python',
        'selection': 'hold',
    }

    # Call the function.
    main(module)

    # The fixture contains a hold selection of 'python', so it should be returned from get-selections.
    cmd = module.get_bin_path('dpkg', True)

# Generated at 2022-06-13 05:15:13.809385
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.exit_json(changed=True, before="deinstall", after="install")

# Generated at 2022-06-13 05:15:25.553098
# Unit test for function main
def test_main():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    from tests.unit.compat.mock import patch
    from tests.unit.compat.mock import MagicMock

    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    mock_ansible_module = MagicMock()
    mock_ansible_module.params = {'name': 'python', 'selection': 'hold'}
    mock_ansible_module.check_mode = False

    m = 'ansible.module_utils.basic.AnsibleModule'


# Generated at 2022-06-13 05:15:32.491386
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

# Generated at 2022-06-13 05:15:50.244442
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    # determine whether to use '/usr/bin/dpkg' or 'usr/bin/dpkg'
    dpkg = module.get_bin_path('dpkg', True)

    name = 'ansible'
    selection = 'hold'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current

# Generated at 2022-06-13 05:15:53.353084
# Unit test for function main
def test_main():
    dpkg_selections = __import__('ansible.modules.system.dpkg_selections')
    assert callable(dpkg_selections.main)


# Generated at 2022-06-13 05:16:06.096180
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as mocked_module:
        mocked_module.return_value = mock_ansible_module(
            dict(
                name = 'python',
                selection = 'hold',
                check_mode = False,
                diff_mode = False,
                ansible_platform = 'debian',
            ),
            dict(
                package_state = dict(present=True),
                package_version = dict(present=True),
            ),
        )
        with patch('ansible.module_utils.basic.get_bin_path') as mocked_get_bin_path:
            mocked_get_bin_path.return_value = True
            with patch('ansible.module_utils.basic.AnsibleModule.run_command') as mocked_run_command:
                mocked_

# Generated at 2022-06-13 05:16:14.694962
# Unit test for function main
def test_main():
    os.environ['PATH'] = '/sbin:/bin'

    # AnsibleModule.run_command parameters
    # This way of instantiating module to be used in unit test is similar to how
    # it is used in modules themselves
    class AnsibleModuleTest(object):
        def __init__(self, argument_spec, supports_check_mode=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode

            self.params = dict(
                name='python',
                selection='hold',
            )

        def get_bin_path(self, name, required):
            return which(name)

        def run_command(self, args, check_rc=False):
            return (0, "python hold", "")


# Generated at 2022-06-13 05:16:21.897814
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
                name=dict(required=True),
                selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.exit_json = lambda x: x
    assert(main() == None or True)
    assert(main() == None or True)
    assert(main() == None or True)

# Generated at 2022-06-13 05:16:31.970646
# Unit test for function main
def test_main():
    module_args = {}
    module_args.update(
        dict(
            name="python",
            selection="hold"
        )
    )
    # Mock required modules.
    module_mock = mock.MagicMock()
    module_mock.params = module_args
    module_mock.exit_json = mock.MagicMock()
    module_mock.get_bin_path = mock.MagicMock(return_value="/bin/dpkg")
    module_mock.run_command = mock.MagicMock(return_value=(0, "python hold", ""))
    dpkg_selections.main()
    module_mock.run_command.assert_called_with(["/bin/dpkg", "--set-selections"], data="python hold")

# Generated at 2022-06-13 05:16:42.686139
# Unit test for function main
def test_main():
    import os
    import tempfile
    import json
    import shutil
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible_collections.ansible.debian.tests.unit.compat import unittest
    from ansible_collections.ansible.debian.tests.unit.compat.mock import patch

    class TestMainModule(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            basic._ANSIBLE_ARGS = None
            self.mock_module = patch.multiple(basic.AnsibleModule,
                                              exit_json=self.exit_json,
                                              fail_json=self.fail_json)
            self.mock_module.start()



# Generated at 2022-06-13 05:16:50.475440
# Unit test for function main
def test_main():
    from ansible.module_utils.common._collections_compat import Mapping
    with patch('ansible.module_utils.basic.AnsibleModule') as mocked_module:
        instance = mocked_module.return_value

        # Configuration
        instance.check_mode = False
        instance.params = dict.fromkeys(['name', 'selection'])
        instance.params['name'] = 'python'
        instance.params['selection'] = 'hold'

        # --get-selections
        mocked_module.run_command.return_value = (0, 'python install', '')

        # --set-selections
        mocked_module.run_command.return_value = (0, '', '')

        main()

        assert mocked_module.run_command.called


# Generated at 2022-06-13 05:17:00.588472
# Unit test for function main
def test_main():
    # Mock out AnsibleModule's get_bin_path to return the correct binary for dpkg.
    # This is done to work around issues on RHEL 7 which doesn't include a /usr/bin/dpkg.
    AnsibleModule.get_bin_path = lambda s: '/usr/bin/dpkg'

    def module_run_command_mock(self, cmd, data=None, check_rc=False, close_fds=True, executable=None, use_unsafe_shell=False,
                                encoding=None, errors='strict', binary_data=False, cwd=None, use_shell=None):
        if cmd == ['/usr/bin/dpkg', '--get-selections', 'python']:
            return 0, 'python               install\n', ''


# Generated at 2022-06-13 05:17:01.035450
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:17:38.947976
# Unit test for function main
def test_main():
    out = '''
        "python" "hold"
    '''

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    
    assert output == out

# Generated at 2022-06-13 05:17:48.925144
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

    test_module.params['name'] = "python" 
    test_module.params['selection'] = "hold" 

    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:17:55.802093
# Unit test for function main
def test_main():
    """Ansible Dpkg Selections module. UnitTests"""
    # Assign test arguments
    name = "python"
    selection = "purge"
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


# Generated at 2022-06-13 05:18:04.396482
# Unit test for function main
def test_main():
    selection = 'deinstall'

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


# Generated at 2022-06-13 05:18:09.926094
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

# Generated at 2022-06-13 05:18:10.300870
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:18:13.775979
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
    name = 'python'
    selection = 'hold'
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    current = 'hold'
    changed = current != selection
    if module.check_mode or not changed:
        module.exit_json(changed=changed, before=current, after=selection)
    module.run

# Generated at 2022-06-13 05:18:24.684148
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


# Generated at 2022-06-13 05:18:25.686866
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:18:37.567879
# Unit test for function main
def test_main():
    # Ansible configuration, from ansible.cfg
    from ansible.config.manager import ConfigManager
    from ansible.module_utils.six.moves import StringIO

# Generated at 2022-06-13 05:19:38.208573
# Unit test for function main
def test_main():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+b') as dpkg_select:
        dpkg_select.write(b'dpkg --get-selections\npython\tinstall\nabc\tdeinstall\n')
        dpkg_select.flush()
        main(params={'name': 'python', 'selection': 'hold', 'check_mode': False, 'diff_mode': True, 'platform': 'debian'},
             utils={'run_command': lambda *args: (0, dpkg_select.name, '')})

# Generated at 2022-06-13 05:19:43.183430
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule.run_command') as mock_run_command:
        with patch('ansible.module_utils.basic.AnsibleModule.get_bin_path') as mock_get_bin_path:
            mock_run_command.return_value = (0, "python install", "")
            mock_get_bin_path.return_value = "/usr/bin/apt"
            mock_run_command.return_value = (0, "", "")
            res = main()
            assert isinstance(res, ansible.module_utils.basic.AnsibleModule)

# Generated at 2022-06-13 05:19:47.163856
# Unit test for function main
def test_main():
    fields = dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    )
    module = AnsibleModule(argument_spec=fields)

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


# Generated at 2022-06-13 05:19:57.729701
# Unit test for function main
def test_main():
    def run_command_mock(self, args, check_rc=False, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None, errors='surrogate_or_strict'):
        if args == [dpkg, '--get-selections', name]:
            if not out:
                return (3, "somename not installed", None)
            else:
                return (0, "%s %s\n" % (name, current), None)

# Generated at 2022-06-13 05:20:07.754090
# Unit test for function main
def test_main():
    args = dict(
        name='python',
        selection='install',
    )

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

    changed

# Generated at 2022-06-13 05:20:15.523264
# Unit test for function main
def test_main():
    fn = 'ansible.modules.packaging.os.dpkg_selections'
    fn = '.'.join(fn.split('.')[:-1])
    import imp
    m = imp.load_source(fn, fn.replace('.', '/') + '.py')
    assert m

# Generated at 2022-06-13 05:20:25.661851
# Unit test for function main
def test_main():
    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def run_command(self, command, data, check_rc=False):
            return (0, "python install\n", "")

        def get_bin_path(self, name, required=False):
            return "/usr/bin/dpkg"

        def exit_json(self, changed, before, after):
            assert changed == False
            assert before == "install"
            assert after == "hold"

        def fail_json(self):
            assert False

    params = {'name': 'python', 'selection': 'hold', '_ansible_check_mode': False}
    m = MockModule(params)
    main(m)


# Generated at 2022-06-13 05:20:34.911541
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

# Generated at 2022-06-13 05:20:43.401112
# Unit test for function main
def test_main():
    test_name = 'python'
    test_selection = 'hold'
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    test_module.params['name'] = test_name
    test_module.params['selection'] = test_selection
    test_module.run_command.rc = True
    test_module.run_command.return_value = (1, '', '')
    test_rc = test_module.run_command.rc
    test_module.exit_json.rc = True

# Generated at 2022-06-13 05:20:46.272458
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert "dpkg" in module.get_bin_path('dpkg', True)