

# Generated at 2022-06-13 05:13:10.420374
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    name = "python"
    selection = "hold"
    rc, out, err = module.run_command('echo "%s\t%s" | /usr/bin/dpkg --set-selections' % (name, selection), check_rc=True)
    rc, out, err = module.run_command("/usr/bin/dpkg --get-selections %s" % (name), check_rc=True)
    current = out.split()[1]
    assert (current == "hold")

# Generated at 2022-06-13 05:13:15.449832
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

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]


# Generated at 2022-06-13 05:13:20.613600
# Unit test for function main
def test_main():
    # Check Debian
    ansible_output = '{"changed": true, "before": "deinstall", "after": "install"}'

    # Check Ubuntu
    ansible_output = '{"changed": true, "before": "not present", "after": "hold"}'
    # assert ansible_output == main()

test_main()

# Generated at 2022-06-13 05:13:31.523326
# Unit test for function main
def test_main():
    import subprocess
    import os
    def mock_exit_json(*args, **kwargs):
        """function to stop program exiting"""
        return 0

    def mock_run_command(*args, **kwargs):
        """function to add the command run"""
        if args[0][0] == 'dpkg':
            if args[0][2] == 'python':
                return 0, 'python	install', 0
            else:
                return 0, '', 0
        else:
            return 0, '', 0

    def mock_get_bin_path(*args, **kwargs):
        """function to change the return value for path"""
        return "/usr/bin/dpkg"

    class AnsibleModule(object):
        """Ansible module for unit testing"""

# Generated at 2022-06-13 05:13:37.445340
# Unit test for function main
def test_main():
    """Unit test for main function"""

    # Unit test: module
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

    # Unit test: Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current

# Generated at 2022-06-13 05:13:38.097196
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:13:38.447105
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:13:42.292301
# Unit test for function main
def test_main():
    name = 'bash'
    selection = 'hold'
    rc, out, err = main()
    module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)
    assert out[0] == name
    assert out[1] == selection
    assert rc == 0

# Generated at 2022-06-13 05:13:51.917650
# Unit test for function main
def test_main():
    # Change working dir
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Create test object
    class Args():
        name = 'python-minimal'
        selection = 'hold'

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.params = Args

    # Run function main()
    main()

# Generated at 2022-06-13 05:13:54.932397
# Unit test for function main
def test_main():
    params = {
        'name': 'nginx',
        'selection': 'install',
    }
    data = {}
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    main(module=module, params=params, data=data)

# Generated at 2022-06-13 05:14:09.977500
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.community.general.tests.unit.compat import unittest

    class TestModule(unittest.TestCase):
        def setUp(self):
            self.spec = dict(name=dict(required=True),
                             selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True))
            self.module = AnsibleModule(argument_spec=self.spec, supports_check_mode=True)
            self.module.params = dict(name='test', selection='test')

        def test_should_exit_with_failure_on_bad_rc(self):
            self.module.run_command = lambda args, check_rc=True: (1, '', '')

# Generated at 2022-06-13 05:14:13.956989
# Unit test for function main
def test_main():
    old_run_command = AnsibleModule.run_command
    AnsibleModule.run_command = lambda self, args, check_rc=False, data=None, binary_data=False, path_prefix=None: (0, '', '')
    module = AnsibleModule(dict(name='python', selection='hold'))
    module.exit_json = lambda changed, before, after: True
    module.check_mode = lambda : False
    main()

# Generated at 2022-06-13 05:14:17.400573
# Unit test for function main
def test_main():
    test_args = [
        ('{"name": "python", "selection": "hold", "changed": false}', "python", "hold"),
        ('{"name": "python", "selection": "install", "changed": true}', "python", "install")
    ]
    for test_input, name, selection in test_args:
        print("testing with:")
        print("name " + name)
        print("selection " + selection)
        print("input: " + test_input)
        changed, out = main(name, selection)
        assert test_input == out
    print("assertion succeess!")

# Generated at 2022-06-13 05:14:24.498801
# Unit test for function main
def test_main():

    import ansible.module_utils.basic as basic
    import ansible.module_utils.action as action
    from ansible.module_utils.action import AnsibleModule

    # Execute function main() with no parameters
    # If a SystemExit exception is raised, this test passes

# Generated at 2022-06-13 05:14:32.883786
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

# Generated at 2022-06-13 05:14:43.564648
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

# Generated at 2022-06-13 05:14:56.517512
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
        module

# Generated at 2022-06-13 05:15:03.421067
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

# Generated at 2022-06-13 05:15:04.814427
# Unit test for function main
def test_main():
    print("Test run")
    main()

# Generated at 2022-06-13 05:15:17.191297
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO # pylint: disable=import-error
    from ansible.module_utils.six import PY3 # pylint: disable=import-error

    class RunCommandMock:
        def __init__(self):
            self.rc = 0
            self.out = ''
            self.err = ''

        def set(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def __call__(self, cmd, **kwargs):
            return self.rc, StringIO(self.out), StringIO(self.err)



# Generated at 2022-06-13 05:15:39.265657
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

# Generated at 2022-06-13 05:15:39.865109
# Unit test for function main
def test_main():
    main()
    pass

# Generated at 2022-06-13 05:15:49.518860
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:15:58.734170
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        )
    )

    module.params = {
        'name' : 'python3-lxml',
        'selection' : 'install'
    }

    module.run_command = Mock(return_value=(0, 'python3-lxml\thold', ''))
    assert main()['changed'] == True


# Generated at 2022-06-13 05:16:07.786908
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

    name = 'test_package'
    selection = 'deinstall'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:16:09.675318
# Unit test for function main
def test_main():
  res_1 = main()
  assert res_1['changed'] == True
  assert res_1['after'] == 'hold'


# Generated at 2022-06-13 05:16:17.427266
# Unit test for function main
def test_main():
    args = dict(
        name="python", 
        selection="hold"
        )
    
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    rc, out, err = module.run_command(["echo", "0"], check_rc=True)
    class Args:
        def __init__(self, **entries):
            self.__dict__.update(entries)
    module.exit_json = lambda a: a
    rc = main()
    assert rc['changed'] == True
    assert rc['before'] == 'hold'

# Generated at 2022-06-13 05:16:26.195338
# Unit test for function main
def test_main():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.connection import Connection
    import os
    import tempfile

    execute_path = get_bin_path('dpkg', True)

    tmpdir = tempfile.mkdtemp()
    test_file = '%s/test_selections' % tmpdir
    fake = '%s/fake_path' % tmpdir
    os.mknod(fake, 0o600)


# Generated at 2022-06-13 05:16:36.692301
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

    name = "python"
    selection = "hold"

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:16:38.614431
# Unit test for function main
def test_main():
    (rc, out, err) = main()
    msg = "ERROR: Failed to execute command "
    assert err == msg

# Generated at 2022-06-13 05:17:15.613573
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'

    assert test_main(name=name, selection=selection)

# Generated at 2022-06-13 05:17:22.027286
# Unit test for function main
def test_main():
    """Generic unit test for function main."""
    module = AnsibleModule(
        argument_spec={
            'name': dict(required=True),
            'selection': dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        },
        supports_check_mode=True,
    )
    module.run_command = MagicMock(return_value=0)
    module.check_mode = False

    dpkg_selections = main()
    assert dpkg_selections is not None

# Generated at 2022-06-13 05:17:28.833195
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils._text import to_text

    # Setup arguments to module.
    dpkg = get_bin_path('dpkg', True)
    args = dict(
        name='python',
        selection='hold',
        dpkg=dpkg,
    )
    args_backup = args.copy()

    # Execute.
    result = basic.AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    ).execute_module(**args)

    # Verify result

# Generated at 2022-06-13 05:17:36.566580
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.params = {
        'name': 'test',
        'selection': 'install'
    }

    out = main()
    assert out['changed'] == False
    assert out['before'] == 'install'
    assert out['after'] == 'install'

# Generated at 2022-06-13 05:17:43.592664
# Unit test for function main
def test_main():

    test_main.ansible_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    test_main.ansible_module.get_bin_path = Mock(return_value='/usr/bin/dpkg')

    test_main.ansible_module.run_command = Mock(side_effect=[
        (0, "python hold", ""),
        (0, "", ""),
        (0, "python none", ""),
        (0, "", ""),
    ])

    dpkg_selections.main()
    test_main.ansible_module.exit_json.assert_called

# Generated at 2022-06-13 05:17:53.971828
# Unit test for function main
def test_main():
    # Setup
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
    # Test 1: Check results

# Generated at 2022-06-13 05:17:54.461568
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:18:01.657070
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic
    import pdb
    pdb.set_trace()
    mock_module = type('ansible.module_utils.basic.AnsibleModule', (), {'check_mode':False, 'params':{'name': 'python', 'selection': 'hold'}})()
    mock_module.run_command = lambda *args, **kwargs: (0, 'python hold', '')
    mock_module.get_bin_path = lambda *args, **kwargs: '/usr/bin/dpkg'
    mock_module.run_command = lambda *args, **kwargs: (0, 'python hold', '')
    main()

# Generated at 2022-06-13 05:18:02.137751
# Unit test for function main
def test_main():
    assert(True)

# Generated at 2022-06-13 05:18:08.155571
# Unit test for function main
def test_main():
    testdata = {
        'name': 'python',
        'selection': 'hold'
    }
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ))
    module.params.update(testdata)
    main()

# Generated at 2022-06-13 05:19:02.683686
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg = module.get_bin_path('dpkg', True)
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)

# Generated at 2022-06-13 05:19:09.605087
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

    # Get current settings.
    rc, out, err = module.run_command(['dpkg', '--get-selections', 'python'], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
        if not current == 'install':
            current = 'not present'


# Generated at 2022-06-13 05:19:18.952709
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught
        by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught
        by the test case"""
        pass

    def exit_json(*args, **kwargs):  # pylint: disable=unused-argument
        """function to patch over exit_json; package return data into an
        exception"""
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)


# Generated at 2022-06-13 05:19:20.179743
# Unit test for function main
def test_main():
    # Test the basic case
    dpkg_selections.main()
    assert True

# Generated at 2022-06-13 05:19:30.329003
# Unit test for function main
def test_main():
    # Mock module.
    module = type('', (), {'get_bin_path': lambda *args, **kwargs: '/bin/dpkg'})
    module.get_bin_path = lambda *args, **kwargs: '/bin/dpkg'

# Generated at 2022-06-13 05:19:43.195821
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.actions import AnsibleAction

    module = basic.AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
        bypass_checks=True,
    )

    dpkg = get_bin_path('dpkg', True)
    check_mode = module.check_mode

    name = 'python'
   

# Generated at 2022-06-13 05:19:47.337639
# Unit test for function main
def test_main():
    f = open('test_dpkg_selections_out.txt', 'r')
    out = f.read()
    f.close()

    f = open('test_dpkg_selections_err.txt', 'r')
    err = f.read()
    f.close()

    f = open('test_dpkg_selections_data.txt', 'r')
    data = f.read()
    f.close()

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = module.get_bin_path('dpkg', True)

    name = module.params

# Generated at 2022-06-13 05:19:47.942436
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:19:58.283194
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

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:20:08.423729
# Unit test for function main
def test_main():
    from patch import *
    from patch import *
    from patch import *
    from patch import *
    from patch import *
    from patch import *
    from patch import *
    from patch import *

    import os
    import tempfile

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
    rc, out, err = module.run_command

# Generated at 2022-06-13 05:22:32.651220
# Unit test for function main
def test_main():
    module_name = 'dpkg_selections'
    module = AnsibleModule(
        argument_spec={'name': {'required': True, 'type': 'str'}, 'selection': {'required': True, 'choices': ['install', 'hold', 'deinstall', 'purge'], 'type': 'str'}},
        supports_check_mode=True
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

# Generated at 2022-06-13 05:22:33.219355
# Unit test for function main
def test_main():
    assert main() == 1

# Generated at 2022-06-13 05:22:37.845743
# Unit test for function main
def test_main():
    ret = main(['python' ,'install'])
    assert(ret == {'changed': False, 'before': 'install'})
    print("Unit test for dpkg_selections module: PASS")

# Generated at 2022-06-13 05:22:45.280489
# Unit test for function main
def test_main():

    AnsibleModule.run = MagicMock(name="run")
    AnsibleModule.run_command = MagicMock(name="run_command")
    AnsibleModule.get_bin_path = MagicMock(name="get_bin_path")

    dpkg = "/usr/bin/dpkg"
    name = "foo"
    selection = "install"
    current = "not present"

    # Get current settings.
    rc = 0
    out = ""
    err = ""

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True),
        ),
        supports_check_mode=True,
    )
    module.get_bin_path.return_value

# Generated at 2022-06-13 05:22:53.382224
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        with patch('ansible.module_utils.basic.get_bin_path') as mock_bin:
            mock_bin.return_value = 'dpkg'

            mock_module.params = {
                'name': 'python',
                'selection': 'purge',
            }
            mock_module.check_mode = False
            mock_module.get_bin_path.side_effect = ['dpkg', 'dpkg']
            mock_module.run_command.side_effect = [[0, 'python hold', ''],
                                                   [0, '', '']]
            main()
            mock_module.exit_json.assert_called_with(changed=True, before='hold', after='purge')