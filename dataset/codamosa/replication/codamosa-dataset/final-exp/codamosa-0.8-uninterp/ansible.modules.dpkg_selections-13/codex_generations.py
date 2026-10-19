

# Generated at 2022-06-13 05:13:03.278967
# Unit test for function main
def test_main():
    print("Testing function main()")
    assert True

# Generated at 2022-06-13 05:13:11.488417
# Unit test for function main
def test_main():
    # Consider refactoring to reduce duplication here
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModuleExitJson
    from ansible.module_utils.basic import AnsibleModuleFailJson
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert module.params['name'] == 'python'
    assert module.params['selection'] == 'hold'

# Generated at 2022-06-13 05:13:15.493775
# Unit test for function main
def test_main():
    module_args = dict(
        name="dpkg-selections"
    )

    with pytest.raises(SystemExit) as exit_exception:
        main()

    assert exit_exception.type == SystemExit
    assert exit_exception.value.code == 2

# Generated at 2022-06-13 05:13:22.260032
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.params = {'name': 'python'}

    current = 'hold'
    selection = 'install'
    changed = current != selection
    module.exit_json(changed=changed, before=current, after=selection)

# Generated at 2022-06-13 05:13:23.673500
# Unit test for function main
def test_main():
    rc, out, err = main() 
    assert rc == 0

# Generated at 2022-06-13 05:13:32.470883
# Unit test for function main
def test_main():
    # Test module with all supported arguments
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Test module without required arguments
    with pytest.raises(AnsibleFailJson) as exc:
        module = AnsibleModule(
            argument_spec=dict(
                selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
            ),
            supports_check_mode=True,
        )
    assert 'name' in exc.value.args[0]['msg']

# Generated at 2022-06-13 05:13:42.948339
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.get_bin_path = lambda x, y: "/usr/bin/dpkg"

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:13:44.866444
# Unit test for function main
def test_main():
     test_result = main()
     assert(test_result == 'This test should fail.')

# Generated at 2022-06-13 05:13:52.005758
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
	assert main() == module.exit_json(changed=False, before='install', after='deinstall')

# Generated at 2022-06-13 05:13:55.506922
# Unit test for function main
def test_main():
    rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)
    assert out == "libc6 install"
    assert rc == 0
    assert err == ""

    assert type(out) == str

    assert "unittest" in out


test_main()

# Generated at 2022-06-13 05:14:14.603820
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert main()

# Generated at 2022-06-13 05:14:20.362713
# Unit test for function main
def test_main():
    # Using mock.patch inbuilt Python library
    # In your tests you will need to mock all dependencies

    import sys
    import ansible.utils
    import ansible.errors
    import ansible.module_utils.helpers

    # Mock the arguments that the module would normally receive
    module_args = dict(
        name="python",
        selection="hold"
    )

    # Example of mocking a function in a class
    monkeypatch.setattr(ansible.module_utils.helpers, "get_bin_path", lambda self, name, required=False: "path")

# Generated at 2022-06-13 05:14:24.578032
# Unit test for function main
def test_main():
    module = AnsibleModule({'name':'python', 'selection':'hold'}, check_mode=True)
    assert main() == {'changed': True, 'before': 'not present', 'after': 'hold'}

# Generated at 2022-06-13 05:14:25.109003
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:14:32.175193
# Unit test for function main
def test_main():
    dpkg_selections_module = AnsibleModule({
        'name': 'python',
        'selection': 'hold',
        'check_mode': False,
        'debug': False,
        'supports_check_mode': True,
    })
    dpkg_selections_module.run_command = lambda command, check_rc=True, data=None: (0, "python install", "")
    dpkg_selections_module.get_bin_path = lambda arg1, arg2: 'dpkg'
    dpkg_selections = __import__('dpkg_selections')
    dpkg_selections.main()

# Generated at 2022-06-13 05:14:43.360455
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

# Generated at 2022-06-13 05:14:58.139171
# Unit test for function main
def test_main():
    # Importing globally
    global main
    # Importing for test
    import sys
    from unittest.mock import Mock, patch
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    from . import dpkg_selections
    from .dpkg_selections import main

    # Unit test cases
    class TestCase(object):
        def __init__(self, name, inp_args, exp_args, exp_rc):
            self.name = name
            self.inp_args = inp_args
            self.exp_args = exp_args
            self.exp_rc = exp_rc

    FAIL = (1 << 8)
    SUCCESS = 0

# Generated at 2022-06-13 05:15:01.610058
# Unit test for function main
def test_main():
    dpkg_selections = {
      "args": {
        "name": "unzip",
        "selection": "install"
      },
      "changed": True,
      "invocation": {
        "module_args": {
          "name": "unzip",
          "selection": "install"
        }
      }
    }

    main()

# Generated at 2022-06-13 05:15:15.257940
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
    dpkg = "dpkg"
    name = module.params['name']
    selection = module.params['selection']

    # Get current settings.
    rc, out, err = module.run_command([dpkg, '--get-selections'], check_rc=True)
    current = "install"
    changed = current != selection


# Generated at 2022-06-13 05:15:16.090159
# Unit test for function main
def test_main():
    assert main() == True

# Generated at 2022-06-13 05:15:48.449437
# Unit test for function main
def test_main():
    import io

    import ansible.module_utils.basic
    import ansible.module_utils.action

    class ActionModule(ansible.module_utils.action.ActionBase):
        def run(self, tmp=None, task_vars=None):
            return action_main(self, tmp, task_vars)

    def action_main(self, tmp, task_vars):
        module = AnsibleModule(
            argument_spec=dict(
                name=dict(required=True),
                selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
            ),
            supports_check_mode=True,
        )

        dpkg = module.get_bin_path('dpkg', True)

        name = module.params['name']

# Generated at 2022-06-13 05:15:54.475314
# Unit test for function main
def test_main():
    from ansible_collections.community.generic.plugins.modules.packaging.os.dpkg_selections import main
    # If no parameters where present
    args = dict(name='abc', selection='hold')
    result = main(args)
    assert result == {'changed': True, 'name': 'Abc'}

# Generated at 2022-06-13 05:16:05.717939
# Unit test for function main
def test_main():
    import os
    import subprocess
    os.environ['PATH'] = '/usr/bin:/bin'
    subprocess.check_call(["dpkg","--get-selections"])
    with open("/tmp/dpkg_selections_test.py", "w") as out_file:
        with open("/home/travis/build/ansible/ansible/lib/ansible/modules/packaging/os/dpkg_selections.py", "r") as in_file:
            for line in in_file:
                out_file.write(line)
    subprocess.check_call(["python", "/tmp/dpkg_selections_test.py"])

# Generated at 2022-06-13 05:16:14.395730
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)),
        supports_check_mode=True)

    rc = 0
    out = 'python	install'
    err = ''
    module.run_command = Mock(return_value=(rc, out, err))
    d = dict(
        changed=False,
        before='install',
        after='hold',
        module='dpkg_selections'
    )
    module.exit_json = Mock(return_value=d)
    module.check_mode = True
    module.params = dict(
        name='python',
        selection='hold'
    )

# Generated at 2022-06-13 05:16:14.861323
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:16:16.343705
# Unit test for function main
def test_main():
    test_args = ["", "--get-selections", "test"]
    module.run_command(test_args, check_rc=True)

# Generated at 2022-06-13 05:16:25.696339
# Unit test for function main
def test_main():
    name = "python"
    selection = "install"
    args = dict(
        name=name,
        selection=selection
    )
    testmodule = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ), supports_check_mode=True)
    res = testmodule.run_command(['dpkg', '--get-selections', name])
    res = dict(
        rc = res[0],
        out = res[1],
        err = res[2]
    )
    res['out'] = res['out'].split()[1]
    current = res['out']
    changed = current != selection

# Generated at 2022-06-13 05:16:27.841729
# Unit test for function main
def test_main():
    out = setup_module(module_args={'name': 'python', 'selection': 'hold'})
    assert out['changed'] == False
    assert out['before'] == 'hold'
    assert out['after'] == 'hold'

# Generated at 2022-06-13 05:16:37.092083
# Unit test for function main
def test_main():
    args = dict(name='python', selection='hold')
    result = dict(changed=False, before='install', after='hold')
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    fake_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    set_module_args(args)

# Generated at 2022-06-13 05:16:48.071137
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    class Response:
        pass
    response = Response()
    response.returncode = 0
    response.stdout = b"python install"
    response.stderr = b""
    module.run_command = lambda args, **kwargs: response

    dpkg = module.get_bin_path('dpkg', True)

    name = "python"
    current = "install"
    selection = "hold"

    changed = current != selection

    # Check mode

# Generated at 2022-06-13 05:17:22.128958
# Unit test for function main
def test_main():
    test_main.__name__ = 'test_dpkg_selections'
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 05:17:28.904734
# Unit test for function main
def test_main():
    mod = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    dpkg = mod.get_bin_path('dpkg', True)

    name = mod.params['name']
    selection = mod.params['selection']

    # Get current settings.
    rc, out, err = mod.run_command([dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()[1]

    changed = current != selection

    if mod.check_mode or not changed:
        mod.exit

# Generated at 2022-06-13 05:17:39.458546
# Unit test for function main
def test_main():
    import tempfile
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:17:50.393742
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

# Generated at 2022-06-13 05:17:57.947021
# Unit test for function main
def test_main():
    # mock data from a trapd command
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


# Generated at 2022-06-13 05:17:58.468787
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:18:05.923540
# Unit test for function main
def test_main():
    def make_module(param_dict):
        params = dict(
            # Module parameters
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True),
        )
        params.update(param_dict)
        return AnsibleModule(
            argument_spec=params,
            supports_check_mode=True,
        )

    # Unit: if changed is false, do not run dpkg module
    def test_no_change():
        module = make_module(dict(
            # Module parameters
            name='python',
            selection='hold',
        ))
        rc, out, err = module.run_command([dpkg, '--get-selections', name], check_rc=True)

# Generated at 2022-06-13 05:18:07.262353
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:18:07.841569
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:18:16.988606
# Unit test for function main
def test_main():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import dpkg_selections
    from pkg_resources import parse_version
    from ansible.module_utils.six import PY3
    from ansible.module_utils import action_common_attributes
    from ansible.module_utils.six.moves import configparser
    import os
    import sys

    dpkg_path = '/usr/bin/dpkg'
    temp_dir = tempfile.mkdtemp()
    with open('/usr/bin/dpkg', 'r') as dpkg_file:
        with open(os.path.join(temp_dir,'dpkg'), 'w+') as mock_dpkg:
            mock_dpkg.write(dpkg_file.read())

# Generated at 2022-06-13 05:19:06.167040
# Unit test for function main
def test_main():
    dpkg_selections_test_input = {
        'name': 'python',
        'selection': 'hold'
    }
    module = AnsibleModule(argument_spec=dpkg_selections_test_input, check_invalid_arguments=False, supports_check_mode=True)
    main()

# Generated at 2022-06-13 05:19:16.546577
# Unit test for function main
def test_main():
    # Mock module arguments
    module_args = dict(
        name='python',
        selection='hold'
    )
    # Create and initialize the module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.params = module_args
    # Create and initialize the module
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:19:23.865045
# Unit test for function main
def test_main():
    import logging, tempfile
    from ansible.module_utils import basic, dpkg_selections
    from ansible.module_utils._text import to_bytes

    logging.basicConfig()

    obj = basic.AnsibleModule(
        argument_spec={
            'name': {'required': True},
            'selection': {'choices': ['install', 'hold', 'deinstall', 'purge'], 'required': True}
        },
        supports_check_mode=True,
    )

    name = 'test'
    selection = 'install'

    # Get current settings.
    rc, out, err = obj.run_command([dpkg_selections.dpkg, '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current

# Generated at 2022-06-13 05:19:32.243364
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader
    import sys
    import unittest


    if not os.path.exists("/usr/bin/dpkg"):
        raise unittest.SkipTest("dpkg not installed")

    mock = MagicMock(return_value=(0, "", ""))
    mock2 = MagicMock(return_value=(0, "python install", ""))
    mock3 = MagicMock(return_value=(0, "", ""))
    mock4 = MagicMock(return_value=(0, "", ""))
    mock5 = MagicMock(return_value=(0, "python purge", ""))

# Generated at 2022-06-13 05:19:43.611725
# Unit test for function main
def test_main():
    name_input = 'test_name'
    selection_input = 'test_selection'
    module_result = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    main_result = main(module_result, name_input, selection_input)
    if(main_result[0] != True or main_result[1] != True):
        raise Exception("main() raised exception, main_result = " + str(main_result))

    print('test_main() passed')

# Generated at 2022-06-13 05:19:47.919540
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

# Generated at 2022-06-13 05:19:56.576120
# Unit test for function main
def test_main():
    # Function main is the only function that matters for the unit test
    # Only the first invocation of main will cause the unit test to actually run
    # All subsequent invocations simply return the current value of the global
    # variable changed. This is useful because some of the subsequent calls
    # to main are caused by AnsibleModule.exit_json and AnsibleModule.fail_json
    global changed
    # Mark the beginning of the main function
    main()
    # Mark the invocation of AnsibleModule.exit_json
    main()
    # Mark the beginning of the main function
    main()
    # Mark the invocation of AnsibleModule.fail_json
    main()
    # Mark the invocation of AnsibleModule.exit_json
    main()

# Generated at 2022-06-13 05:20:01.093592
# Unit test for function main
def test_main():
    import os
    os.environ['LC_ALL'] = 'C'
    import sys
    sys.path.append('/var/tmp')
    sys.stdout = open('/tmp/test.out','w')
    # Execute main function
    main()

# Generated at 2022-06-13 05:20:10.040816
# Unit test for function main
def test_main():
    dpkg = '/usr/bin/dpkg'
    name = 'dpkg_selections'
    selection = 'hold'
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    module.run_command = MagicMock()
    module.run_command.return_value = 0, '{0} {1}'.format(name, 'install'), ''
    module.exit_json = MagicMock()
    module.check_mode = False
    main()

# Generated at 2022-06-13 05:20:17.622579
# Unit test for function main
def test_main():
    module = get_test_module()
    command_test_data = {
        'dpkg --get-selections python': dict(
            rc=0,
            stdout='python                        install',
            stderr='',
        ),
        'dpkg --set-selections': dict(
            rc=0,
            stdout='',
            stderr='',
        ),
    }
    module.run_command = get_run_command(command_test_data)

    # All good if current selection is different
    main()

    # All good if current selection is different
    module.params['selection'] = 'hold'
    main()

    # Nothing changed if the current selection is the same
    module.params['selection'] = 'install'
    main()

# Unit test helper functions

# Generated at 2022-06-13 05:22:43.129073
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

# Generated at 2022-06-13 05:22:52.353835
# Unit test for function main
def test_main():
    # Pull the required modules into this namespace.
    from ansible.module_utils.basic import AnsibleModule

    # Set up the module input parameters and compare output.
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    def run_command(args, check_rc=True):
        if args == ['dpkg', '--set-selections']:
            return [0, '', '']
        elif args == ['dpkg', '--get-selections', 'python']:
            return [0, "python hold\n", '']
        else:
            print('unexpected args')
           

# Generated at 2022-06-13 05:22:53.960249
# Unit test for function main
def test_main():
    out = main()
    assert out['changed'] is True
    assert out['before'] is not None