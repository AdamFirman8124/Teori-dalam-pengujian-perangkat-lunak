

# Generated at 2022-06-13 05:13:10.616274
# Unit test for function main
def test_main():
    m = {"run_command.rc": True, "module_utils.basic.AnsibleModule.run_command.return_value": (0, "dpkg\n", "")}
    m.update({"run_command.return_value.stderr": "", "run_command.return_value.rc": 0, "run_command.return_value.stdout": "dpkg\n"})
    with patch.dict(__salt__, m):
        assert main() == {"changed": True, "after": "install", "before": "install"}
    m = {"run_command.rc": True, "module_utils.basic.AnsibleModule.run_command.return_value": (0, "dpkg\n", "")}

# Generated at 2022-06-13 05:13:11.281377
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-13 05:13:12.289343
# Unit test for function main
def test_main():
    assert not main('example')

# Generated at 2022-06-13 05:13:22.762776
# Unit test for function main
def test_main():
    dpkg = '/usr/bin/dpkg'
    dpkg_args = ['--get-selections', 'python']
    python_selection = 'install'
    dpkg_set_selection = '--set-selections'
    dpkg_selection_config = 'python hold'
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert module.get_bin_path('dpkg', True) == dpkg
    assert module.run_command.call_args_list == [(([dpkg, '--get-selections', 'python'],), {'check_rc': True})]
   

# Generated at 2022-06-13 05:13:32.008265
# Unit test for function main
def test_main():
    import os
    data = 'python\tinstall\n'

    def __mock_run_command__(self, command, data=None, check_rc=False, close_fds=True, binary_data=True, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None, errors='surrogate_then_replace', create_empty_tempfile=True, stdin=None):
        if data == 'python install':
            return os.EX_OK, '', ''
        else:
            return os.EX_OK, 'python\tinstall', ''

    import ansible.module_utils.basic
    old_run_command = ansible.module_utils.basic.AnsibleModule.run_command


# Generated at 2022-06-13 05:13:42.575925
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.dpkg_selections import main
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import cStringIO
    import sys

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Simulate dpkg by printing passed in selections to stdout and returning 0
    def fake_dpkg(args, **kwargs):
        assert isinstance(args, (list, tuple))
        if args[0] == "--get-selections":
            print

# Generated at 2022-06-13 05:13:54.123197
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import random
    import string
    import subprocess
    import sys
    import stat
    import ansible.module_utils.basic as basic_module_utils
    import ansible.module_utils.basic_module as basic_module
    module_test_code = '''
import sys
import os
sys.path.insert(0, os.path.abspath('.'))
import dpkg_selections
dpkg_selections.main()
'''
    tmpdir = tempfile.mkdtemp()
    old_cwd = os.getcwd()
    os.chdir(tmpdir)
    with open('dpkg_selections.py', 'w') as f:
        f.write(module_test_code)

# Generated at 2022-06-13 05:13:58.623360
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = MagicMock(return_value=(0, 'python hold', ''))
    main()

# Generated at 2022-06-13 05:14:07.891922
# Unit test for function main
def test_main():
    # Mock module_utils
    module_utils_mock = mock.MagicMock()
    dpkg_selections.module_utils = module_utils_mock
    module_utils_mock.basic.AnsibleModule.return_value = ansible_module_mock

    # Mock module.run_command
    ansible_module_mock.run_command = mock.MagicMock()

    # Mock module.get_bin_path
    ansible_module_mock.get_bin_path = mock.MagicMock(return_value='/usr/bin/dpkg')

    # Provide a side effect for run_command in check mode
    ansible_module_mock.run_command.side_effect = [
        (0, 'python install', ''),  # dpkg --get-selections
    ]

    #

# Generated at 2022-06-13 05:14:08.313863
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:14:18.933181
# Unit test for function main
def test_main():
    # Fixture for function main
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    main()

# Generated at 2022-06-13 05:14:29.804412
# Unit test for function main
def test_main():
    module = AnsibleModule(dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ), supports_check_mode=True)

    def run_command(args, data=None, check_rc=False):
        if data == "python2.7 install":
            return (0, "python not present", "")
        elif data == "python2.7 deinstall":
            return (0, "python2.7 install", "")
        else:
            raise Exception('Unexpected call to run_command')

    module.run_command = run_command
    module.get_bin_path = lambda exe, required=False, opt_dirs=None: exe
    main()

# Generated at 2022-06-13 05:14:31.295791
# Unit test for function main
def test_main():

    # Code is not expected to run in a test environment
    assert False, "No unit test for dpkg_selections module"

# Generated at 2022-06-13 05:14:42.719913
# Unit test for function main
def test_main():
    dpkg = 'dpkg'
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

    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]



# Generated at 2022-06-13 05:14:43.318110
# Unit test for function main
def test_main():
    assert main() == true

# Generated at 2022-06-13 05:14:58.139152
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import os

    dpkg = os.path.join(tempfile.gettempdir(), 'dpkg')
    with open(dpkg, 'w') as f:
        f.write('''
#!/bin/sh

case "$*" in
    --get-selections*)
	echo "$1 hold"
	;;
esac
''')
    os.chmod(dpkg, 0o777)

    old_path = os.environ['PATH']
    os.environ['PATH'] = '/usr/bin:' + tempfile.gettempdir()


# Generated at 2022-06-13 05:14:58.995761
# Unit test for function main
def test_main():
    # test
    main()

# Generated at 2022-06-13 05:15:00.697834
# Unit test for function main
def test_main():
    # test for generate random integer number
    #assert random_integer(1, 10) >= 1 and random_integer(1, 10) <= 10
    pass

# Generated at 2022-06-13 05:15:06.140830
# Unit test for function main
def test_main():
    testmodule = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = testmodule.get_bin_path('dpkg', True)

    dpkg = 'dpkg'
    name = 'python'
    selection = 'hold'

    # Get current settings.
    rc, out, err = testmodule.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:15:12.402570
# Unit test for function main
def test_main():
    args = dict(name='python', selection='hold')
    with pytest.raises(SystemExit):
        main()
    args = dict(name='python', selection='install')
    with pytest.raises(SystemExit):
        main()
    args = dict(name='python', selection='hold')
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-13 05:15:30.914049
# Unit test for function main
def test_main():
    mydata = dict(
        name='python',
        selection='hold',
        changed=False
    )
    myansible = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
        check_invalid_arguments=False,
        bypass_checks=True
    )
    myansible.params = mydata
    check_mode = myansible.check_mode
    changed = myansible.params['changed']
    rc = 0
    out = 'python hold'
    err = ''
    myansible.run_command = lambda args, check_rc=False: (rc, out, err)
    my

# Generated at 2022-06-13 05:15:39.779814
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        check_invalid_arguments=False,
        supports_check_mode=True
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


# Generated at 2022-06-13 05:15:47.117016
# Unit test for function main
def test_main():
    '''Test dpkg_selections module'''
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = MagicMock(return_value=(0, '0:i386 0:all', ''))
    dpkg_selections.main()
    assert module.exit_json.called

# Generated at 2022-06-13 05:15:53.678188
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import tempfile
    import contextlib

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
        loader=None,
        shared_loader_obj=None,
        from_ansible=True,
        no_log=False,
        use_ansible_caching=False,
    )

    dpkg = '/usr/bin/dpkg'
    module._debug = False
    module._socket_path = tempfile.mkdtemp()


# Generated at 2022-06-13 05:16:06.205726
# Unit test for function main
def test_main():
    import ansible.module_utils.action_plugins.system.dpkg_selections as dpkg_selections
    module = dpkg_selections.AnsibleModule(argument_spec=dict(name=dict(required=True),selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)),supports_check_mode=True,)
    module.check_mode = False
    module.params['name'] = 'python'
    module.params['selection'] = 'hold'
    module.run_command = MagicMock(return_value=(0, 'python install', ''))
    dpkg_selections.main()
    module.run_command.assert_called_with(['/usr/bin/dpkg', '--set-selections'], data="python hold", check_rc=True)

# Generated at 2022-06-13 05:16:09.835533
# Unit test for function main
def test_main():
  name = "vim"
  selection = "install"
  assert main(name,selection) == 0
  assert main(name+"1",selection) == 1
  name = "python"
  selection = "hold"
  assert main(name,selection) == 0
  assert main(name+"1",selection) == 1

# Generated at 2022-06-13 05:16:10.472164
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:16:10.992372
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:16:18.078315
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
            argument_spec=dict(
                name=dict(required=True),
                selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
                ),
            supports_check_mode=True,
            )

    def run_command_fn(args, check_rc=False):
        # Return the expected state for dpkg --get-selections
        if args[0] == 'dpkg' and args[1] == '--get-selections':
            return(0, '%s\tinstall\n' % test_module.params['name'], '')
        # Return the expected return code for dpkg --set-selections

# Generated at 2022-06-13 05:16:22.016115
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

# Generated at 2022-06-13 05:16:56.126700
# Unit test for function main
def test_main():
    assert main()[1]
    print ("test_main: " + "ok")

test_main()

# Generated at 2022-06-13 05:16:57.868804
# Unit test for function main
def test_main():
    assert callable(main)


# Generated at 2022-06-13 05:17:04.240891
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

# Generated at 2022-06-13 05:17:11.943662
# Unit test for function main
def test_main():
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as am:
        am.return_value = mock.Mock()
        am.return_value.params = dict(name='apt', selection='install')
        am.return_value.check_mode = False
        am.return_value.run_command = mock.Mock()
        am.return_value.run_command.return_value = (0,'','apt               install\n')
        am.return_value.get_bin_path = mock.Mock()
        am.return_value.get_bin_path.return_value = 'dpkg'
        am.return_value.exit_json = mock.Mock()
        main()

# Generated at 2022-06-13 05:17:17.995371
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert test_module.params['name'] == 'python'
    assert test_module.params['selection'] == 'hold'

# Generated at 2022-06-13 05:17:18.554434
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:17:26.593020
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

# Generated at 2022-06-13 05:17:27.065330
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:17:38.868863
# Unit test for function main
def test_main():
    import os
    import tempfile

    # Create a test environment.
    test_dir = tempfile.mkdtemp()
    os.environ['HOME'] = test_dir
    os.environ['PATH'] = '/usr/bin:' + os.environ['PATH']

    # Create a mock config.
    test_config = """APT::Get::Assume-Yes "true";
DPkg::Options { "--force-confdef"; "--force-confold"; }"""
    with open(os.path.join(test_dir, 'apt.conf'), 'w') as fp:
        fp.write(test_config)

    # Create a mock dpkg-status.

# Generated at 2022-06-13 05:17:41.059509
# Unit test for function main
def test_main():
    rc, out, err = module.run_command([dpkg, '--get-selections', python], check_rc=True)

# Generated at 2022-06-13 05:18:34.339191
# Unit test for function main
def test_main():
    # Argument spec for module
    argument_spec = dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    )
    m = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    # Mock methods that are called on our module
    check_mode_result = {"changed": False}

    # Mock modules that are called on our module
    import sys, os
    sys.modules["ansible"] = __import__("mock")
    sys.modules["ansible.module_utils.basic"] = __import__("mock")
    sys.modules["ansible.module_utils.common.process"] = __import__("mock")

# Generated at 2022-06-13 05:18:36.073653
# Unit test for function main
def test_main():
    print("Test function main")
    print("placeholder")

# Generated at 2022-06-13 05:18:43.710975
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg = module.get_bin_path('dpkg', False)
    # Testing with a non-existent dpkg binary
    assert dpkg is None

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    dpkg = module.get_bin_path('dpkg', True)
    # Testing with

# Generated at 2022-06-13 05:18:55.296250
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
    selection = 'not present'

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection


# Generated at 2022-06-13 05:18:57.456300
# Unit test for function main
def test_main():
    out = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    assert out == 0

# Generated at 2022-06-13 05:19:04.517865
# Unit test for function main
def test_main():
    import json
    test_dict = {'params': {'name': 'abc', 'selection': 'hold'}, 'check_mode': False}
    test_module = AnsibleModule(argument_spec=dict())
    test_module.params = test_dict['params']
    test_module.check_mode = test_dict['check_mode']

    test_module.run_command = MagicMock(return_value=(0, '', ''))
    test_module.exit_json = MagicMock()
    main()
    assert test_module.exit_json.called


# Generated at 2022-06-13 05:19:10.498152
# Unit test for function main
def test_main():
    facts = {}
    module = AnsibleModule(argument_spec=dict(name=dict(required=True),
                                              selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], 
                                                  required=True)
                                              ), supports_check_mode=True)
    dpkg = module.get_bin_path('dpkg', True)
    name = module.params['name']
    selection = module.params['selection']
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
    changed = current != selection


# Generated at 2022-06-13 05:19:19.941091
# Unit test for function main
def test_main():
    # run module without --check and without --diff to check for idempotence
    from ansible.module_utils import dpkg_selections
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

# Generated at 2022-06-13 05:19:25.634023
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

# Generated at 2022-06-13 05:19:27.995829
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    klass = DpkgSelections(module)
    klass.main()

# Generated at 2022-06-13 05:21:47.402586
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

# Generated at 2022-06-13 05:21:51.189764
# Unit test for function main
def test_main():
    global rc, out, err
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]
    changed = current != selection
    module.run_command([dpkg, '--set-selections'], data="%s %s" % (name, selection), check_rc=True)

# Generated at 2022-06-13 05:22:00.660144
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True
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


# Generated at 2022-06-13 05:22:12.936072
# Unit test for function main
def test_main():
    print("Running unit test")
    
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

# Generated at 2022-06-13 05:22:15.721949
# Unit test for function main
def test_main():
    assert main("python", "hold") == "python	hold"
    #assert main("python", "not present") == "python	not present"
    #assert main("python", "hold1") == "python	hold"
    #assert main("pytho", "hold") == "pytho	hold"

# Generated at 2022-06-13 05:22:16.536181
# Unit test for function main
def test_main():
    assert True


# Generated at 2022-06-13 05:22:18.698500
# Unit test for function main
def test_main():
    name = 'python'
    out = [name, 'install', '\n']
    selection = 'hold'

    # Call main function with parameter and check result
    result = main(name, selection, out)
    assert result == True

# Generated at 2022-06-13 05:22:31.616631
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path

    dpkg = get_bin_path('dpkg', True)

    assert dpkg

    # Test passing the test
    name = 'python'
    selection = 'hold'

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.params['name'] = name
    module.params['selection'] = selection

    main()

    # Test failing the test
    name = 'python'
    selection = 'uninstall'


# Generated at 2022-06-13 05:22:42.619755
# Unit test for function main
def test_main():
    import tempfile
    import os
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.dpkg_selections import main

    with tempfile.NamedTemporaryFile() as tmp:
        with open(tmp.name, 'w') as f:
            f.write('''Package: python
Status: install ok installed
Provides: baz
Depends: quux
Priority: extra
Section: python
Installed-Size: 23
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: foreign
Source: python-defaults
Version: 2.7.5-5ubuntu3
'''.strip())

# Generated at 2022-06-13 05:22:52.126156
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        platform='ubuntu',
        version='0.0.1',
    )
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value='/usr/bin/dpkg')
    module.get_bin_path.return_value = '/usr/bin/dpkg'
    module.check_mode = True
    result = main()
    assert result['changed'] == True
    assert result['before'] == 'install'
    assert result['after'] == 'hold'
    assert module.deprecations