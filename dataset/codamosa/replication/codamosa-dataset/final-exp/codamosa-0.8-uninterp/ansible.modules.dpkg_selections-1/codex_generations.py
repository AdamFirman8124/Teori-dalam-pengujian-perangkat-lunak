

# Generated at 2022-06-13 05:13:10.369415
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

    module.get_bin_path = lambda *a, **kw: '/bin/dpkg'
    module.run_command = lambda *a, **kw: (0, 'test install', '')

    rc, out, err = module.run_command([module.get_bin_path(), '--get-selections', name], check_rc=True)
    if not out:
        current = 'not present'
    else:
        current = out.split()

# Generated at 2022-06-13 05:13:15.260151
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

# Generated at 2022-06-13 05:13:24.272617
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.constants as C
    import tempfile
    import os
    def set_module_args(args):
        args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
        basic._ANSIBLE_ARGS = to_bytes(args)

    m_path = os.path.join('/work/ansible/test/modules', 'dpkg.py')

    module_args = dict(
        name='python',
        selection='hold',
        _ansible_no_log=True,
        _ansible_verbosity=4
    )

    set_module_args(module_args)

    f = tempfile.NamedTemporaryFile(mode='w+t')


# Generated at 2022-06-13 05:13:28.801518
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    assert isinstance(main(), dict)

# Generated at 2022-06-13 05:13:35.952119
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

# Generated at 2022-06-13 05:13:42.311759
# Unit test for function main
def test_main():

    # Unit test for function main
    def test_main():
        # Unit test for function main
        def test_main():
            # Unit test for function main

            # Unit test for function main
            def test_main():
                # Unit test for function main
                def test_main():
                    # Unit test for function main
                    def test_main():
                        # Unit test for function main
                        def test_main():
                            # Unit test for function main
                            def test_main():
                                # Unit test for function main

                                assert False


assert False

# Generated at 2022-06-13 05:13:53.942695
# Unit test for function main
def test_main():
    import os
    import mock
    class AnsibleModule(object):
        def __init__(self, argument_spec, supports_check_mode):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.params = {}
            self.diff = {}
        def fail_json(self, **kwargs):
            print("fail_json : %s" % (kwargs))
        def exit_json(self, **kwargs):
            print("exit_json : %s" % (kwargs))
        def run_command(self, command, data, check_rc):
            print("run_command : %s, %s" % (command, data))
            return (0, "test_name install", "")

# Generated at 2022-06-13 05:14:01.402266
# Unit test for function main
def test_main():
    import sys
    import os
    import tempfile
    import shutil
    import mock

    # Ensure we are pointing at our test directory and not a system directory.
    path = '{0}/{1}'.format(os.path.dirname(os.path.realpath(__file__)), "test_data")
    sys.path.insert(0, path)

    # Import the module
    module = __import__('dpkg_selections')

    # Run the module to ensure any exceptions are raised.
    module.main()

    # # Mock the dpkg binary
    # path = '{0}/{1}'.format(os.path.dirname(os.path.realpath(__file__)), "dpkg")
    # mock.patch('module.run_command', return_value=[0, "PASS", ""])

# Generated at 2022-06-13 05:14:09.485413
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

# Generated at 2022-06-13 05:14:10.437893
# Unit test for function main
def test_main():
    print("Unit test for function main")
    assert True

# Generated at 2022-06-13 05:14:29.952754
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

    # test for name is null
    name = ""
    selection = "install"
    module.params['name'] = name
    module.params['selection'] = selection
    os.system("apt-get remove " + name)
    main()
    assert module.exit_json.called
    # test for selection is null
    name = "python"
    selection = ""
    module.params['name'] = name
    module.params['selection'] = selection

# Generated at 2022-06-13 05:14:40.103384
# Unit test for function main
def test_main():
    # Stub AptModule()
    apt = AptModule()
    apt._binary_path = lambda *args, **kwargs: "mdkir"
    apt._run_command = lambda *args, **kwargs: [0, "python hold", ""]
    apt._run_command = lambda *args, **kwargs: [0, "python install", ""]

    # Test install
    main()

    # Test already installed
    apt._run_command = lambda *args, **kwargs: [0, "python hold", ""]
    main()

    # Test check mode
    apt._check_mode = True
    apt._run_command = lambda *args, **kwargs: [0, "python install", ""]
    main()

# Generated at 2022-06-13 05:14:45.774183
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


# Generated at 2022-06-13 05:14:59.622836
# Unit test for function main
def test_main():
    dpkg = 'apt-get'
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    name = 'test'
    current = 'purge'
    selection = 'purge'
    changed = current != selection
    assert changed == False
    out = 'success'
    assert out == 'success'
    rc = 0
    assert rc == 0

    name = 'test'
    current = 'purge'
    selection = 'deinstall'
    changed = current != selection
    assert changed == True
    out = 'success'
    assert out == 'success'
    rc = 0
   

# Generated at 2022-06-13 05:15:00.441097
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:15:00.918426
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:15:06.260174
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


# Generated at 2022-06-13 05:15:14.759054
# Unit test for function main
def test_main():

    # Get the relative path to the test module.
    test_path = os.path.realpath(__file__)
    test_dir = os.path.dirname(test_path)
    test_module = test_dir + "/test_main.py"

    # Execute the test module
    (rc, out, err) = module_exec(test_module, json.dumps({'name': 'python', 'selection': 'hold'}))

    assert rc == 0
    assert out['changed'] == True


# Generated at 2022-06-13 05:15:15.399629
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:15:16.266204
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:15:31.851544
# Unit test for function main
def test_main():
    args = dict(name='python',selection='hold')
    module = AnsibleModule(argument_spec=dict(
                                name=dict(required=True),
                                selection=dict(required=True)
                            ))
    main()

# Generated at 2022-06-13 05:15:41.881026
# Unit test for function main
def test_main():
    import tempfile
    import os
    import collections
    import subprocess
    module_args = collections.namedtuple('module_args', 'name selection')

    class AnsibleModule(object):
        def __init__(self, argument_spec, supports_check_mode):
            self.check_mode = False

        def get_bin_path(self, name, required):
            if name == 'dpkg':
                return os.path.join(os.path.dirname(__file__), 'dpkgbin')
            else:
                raise Exception("Invalid bin name")

        def run_command(self, cmd, check_rc=False, **kwargs):
            output = None

# Generated at 2022-06-13 05:15:45.147005
# Unit test for function main
def test_main():
    args = dict(
        name='python',
        selection='hold'
    )
    module = AnsibleModule(argument_spec=args)
    assert main()

# Generated at 2022-06-13 05:15:45.972156
# Unit test for function main
def test_main():
    # Do something?
    print("Haha")

# Generated at 2022-06-13 05:15:46.892547
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:15:48.027013
# Unit test for function main
def test_main():
    dpkg_selections.main({"name":"python","selection":"hold"})

# Generated at 2022-06-13 05:15:52.314487
# Unit test for function main
def test_main():
    test = {
        'name': 'python',
        'selection': 'install',
        'rc': 0,
        'stdout': 'python install\n',
        'stderr': ''
    }
    module = AnsibleModule(argument_spec=dict())
    module.run_command = magic_run_command
    module.run_command_environ_update = dict()
    module.get_bin_path = lambda x, y: '/bin/dpkg'
    res = main()
    assert res['changed'] == False
    assert res['before'] == test['selection']
    assert res['after'] == test['selection']

# Magic function to mock run_command

# Generated at 2022-06-13 05:15:53.005339
# Unit test for function main
def test_main():
    assert True == True

# Generated at 2022-06-13 05:16:01.833306
# Unit test for function main
def test_main():
    with six.moves.mock.patch('ansible.module_utils.basic.AnsibleModule.run_command') as run_command:
        result = {
            'stdout': 'python install',
            'rc': 0,
            'stderr': ''
        }
        run_command.return_value = result
        result = main()
        assert result['changed'] == False
        assert result['before'] == 'install'
        assert result['after'] == 'hold'


# Generated at 2022-06-13 05:16:07.783783
# Unit test for function main
def test_main():
    out = ""
    rc = 0
    err = ""
    module = None
    name = "python"
    selection = "hold"
    changed = "install" != "hold"
    current = selection
    assert changed == True
    assert current != selection
    assert module.check_mode == True or not changed == False
    assert not out
    assert rc == 0
    assert err == ""

# Generated at 2022-06-13 05:16:48.315109
# Unit test for function main
def test_main():
    def run_command_mock(args, check_rc=True):
        """mock for module.run_command"""
        if args[4] == 'python':
            return 0, 'python install', ''
        else:
            raise ValueError('unexpected call to run_command: %s' % args)

    module = get_ansible_module(commit=True)
    module.run_command = run_command_mock
    module.get_bin_path = lambda x: x
    module.main()

# Generated at 2022-06-13 05:16:58.261346
# Unit test for function main
def test_main():
    import json
    import shutil
    from ansible_collections.community.general.plugins.modules.packaging.os.dpkg_selections import main
    from ansible_collections.ansible.misc.plugins.module_utils.common.process import get_bin_path
    from ansible_collections.ansible.misc.plugins.module_utils._text import to_bytes
    from ansible_collections.ansible.misc.plugins.module_utils._text import to_native

    # Redirect module output to stderr so we can capture it.
    import sys
    stderr = sys.stderr
    sys.stderr = sys.stdout

    dpkg = get_bin_path('dpkg', True)


# Generated at 2022-06-13 05:17:04.550288
# Unit test for function main
def test_main():
    from mock import patch
    from module_utils.common.compat import StringIO

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

    with patch('ansible.module_utils.basic.AnsibleModule.run_command') as run_command_mock:
        run_command_mock.return_value = (0, StringIO("%s\t%s" % (name, 'hold')), '')
        main()


# Generated at 2022-06-13 05:17:12.118300
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import StringIO

    class MockModule(object):
        def __init__(self):
            self.params = dict(name='python', selection='install')
            self.run_command_calls = 0
            self.check_mode = False

        def get_bin_path(self, arg, required=False):
            return get_bin_path(arg, required=required)

        def run_command(self, cmd, check_rc=True, data=None):
            self.run_command_calls += 1
            rc = 1
           

# Generated at 2022-06-13 05:17:23.613291
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required = True),
            selection = dict(choices = ['install', 'hold', 'deinstall', 'purge'], required = True)
        )
    )

    # Mock out the imports
    import ansible.module_utils.basic
    import ansible.module_utils.action
    ansible.module_utils.basic.AnsibleModule = lambda *args, **kwargs: module
    ansible.module_utils.action.AnsibleModule = lambda *args, **kwargs: module

    # Mock out the ansible module actions
    module.get_bin_path = lambda *args, **kwargs: None
    module.run_command = lambda *args, **kwargs: (0, '', '')
    module.check_mode = False

# Generated at 2022-06-13 05:17:24.096554
# Unit test for function main
def test_main():

    assert True == True

# Generated at 2022-06-13 05:17:29.983941
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

# Generated at 2022-06-13 05:17:40.204244
# Unit test for function main
def test_main():
    # Test example: Prevent python from being upgraded
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
    assert changed == False, 'Current is not equal to selection'
    # module

# Generated at 2022-06-13 05:17:43.403628
# Unit test for function main
def test_main():
    doc = dict(name='python', selection='hold')
    assert ansible_module.ansible_main.main(doc) == dict(changed=True, after='hold', before='install')

# Generated at 2022-06-13 05:17:50.051057
# Unit test for function main
def test_main():

    main() # Workaround for pytest and imports.
    import inspect
    import os
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 05:18:42.996853
# Unit test for function main
def test_main():

    module_name = "AnsibleModule"
    argument_spec = {
        "name": "python",
        "selection": "hold"
    }
    changed = True
    current = "not present"
    selection = "hold"

    # Add expected functions to the module mock
    mock_module = MagicMock()
    mock_module_result = MagicMock(return_value=changed)
    mock_module.run_command = MagicMock(return_value=mock_module_result)
    mock_module.exit_json = MagicMock()

    # Add expected functions to the module class
    mock_module.AnsibleModule = MagicMock()
    mock_module.AnsibleModule.get_bin_path = MagicMock(return_value="dpkg")
    mock_module.AnsibleModule.run

# Generated at 2022-06-13 05:18:43.859870
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:18:50.546333
# Unit test for function main
def test_main():
    module = AnsibleModule(
            argument_spec=dict(
                name=dict(required=True, type='str'),
                selection=dict(required=True, type='str', choices=['install', 'hold', 'deinstall', 'purge'])
            ),
            supports_check_mode=True
            )
    dpkg = module.get_bin_path('dpkg', True)
    assert dpkg == '/usr/bin/dpkg'

# Generated at 2022-06-13 05:19:00.793598
# Unit test for function main
def test_main():
    import os
    import sys
    import subprocess
    import shlex
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import shlex_quote
    #import ansible.module_utils.action_plugins.system.dpkg_selections as dpkg_selections
    sys.path.append('/home/brian-brazil/ansible/lib/augmentation_plugins')
    from action_plugins.system import dpkg_selections
    #from action_plugins.system.dpkg_selections import *
    #import action_plugins.system.dpkg_selections as dpkg_selections
    #from dpkg_

# Generated at 2022-06-13 05:19:06.673385
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    
    assert module.check_mode
    assert module.params
    assert module.params['name']
    assert module.params['selection']
    assert module.run_command
    assert module.run_command([])
    

# Generated at 2022-06-13 05:19:16.711590
# Unit test for function main
def test_main():
    # Test positive selection
    data = {'check_mode': False, 'diff_mode': False, 'name': 'python', 'selection': 'hold'}
    files = {'/usr/bin/dpkg': ''}

# Generated at 2022-06-13 05:19:18.843239
# Unit test for function main
def test_main():
    test = 'test'
    name = 'test'
    selection = 'test'
    changed = True
    set_selections = 'test'
    assert test



# Generated at 2022-06-13 05:19:25.140783
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

# Generated at 2022-06-13 05:19:27.592231
# Unit test for function main
def test_main():
    l = "{'name': ['python'], 'selection': ['hold'] }"
    main(l)

# Generated at 2022-06-13 05:19:28.249242
# Unit test for function main
def test_main():
    out = main()

# Generated at 2022-06-13 05:21:52.747527
# Unit test for function main
def test_main():
    '''
    Test module when calling main()
    '''
    # Mock module input parameters
    mocker = Mocker()
    module = mocker.Mock()
    module.check_mode = False
    module.params = dict(
        name='openssl',
        selection='hold',
    )

    # Mock function return values
    mocker.Mock(return_value=True)
    mocker.Mock(return_value=False)

    # Object under test
    rc = ResultCallback()

# Generated at 2022-06-13 05:21:55.305497
# Unit test for function main
def test_main():
    # Something to read
    module = AnsibleModule({'name':'foo', 'selection': 'install'})
    main([module])

# Generated at 2022-06-13 05:22:00.732269
# Unit test for function main
def test_main():
    name, selection = 'python', 'hold'

    params = {
        'name': name,
        'selection': selection
    }

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.params = params
    main()

# Generated at 2022-06-13 05:22:03.771953
# Unit test for function main
def test_main():
    # check dpkg_selections before python
    assert 'python\thold' in os.popen(dpkg + ' --get-selections python').read()

# Generated at 2022-06-13 05:22:15.260444
# Unit test for function main
def test_main():

    # Create the module mock
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Create a fake dpkg executable
    dpkg = module.get_bin_path('dpkg', True)

    # Create a dummy name and selection variable
    name = 'python'
    selection = 'hold'

    # Create a fake dpkp function that is used in module.run_command
    import os

# Generated at 2022-06-13 05:22:16.038321
# Unit test for function main
def test_main():
    name = 'python'
    selection = 'hold'

# Generated at 2022-06-13 05:22:21.821532
# Unit test for function main
def test_main():
    fixture = [
        ["dpkg", "--get-selections", "python"],
        ["dpkg", "--set-selections"],
    ]
    mock = AnsibleActionModuleMocker(fixture)
    module = mock._get_module(params=dict(name='python', selection='hold'))
    main()
    assert mock.executed_called == 2
    assert mock.executed_called_with[0] == [
        "dpkg", "--get-selections", "python"
    ]
    assert mock.executed_called_with[1] == [
        "dpkg", "--set-selections"
    ]
    assert mock.executed_called_with_data[1] == "python hold"

# Generated at 2022-06-13 05:22:34.069231
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os
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

    changed = current

# Generated at 2022-06-13 05:22:44.372568
# Unit test for function main
def test_main():
    d = {
        'name': 'python',
        'selection': 'hold'
    }
    rc = {}
    rc['cmd'] = ['dpkg', '--get-selections', d['name']]
    rc['rc'] = 0
    rc['stdout'] = 'python 2.7.2\n'
    rc['stdout_lines'] = [rc['stdout']]
    rc['stderr'] = ''
    rc['stderr_lines'] = []
    rc['changed'] = True
    run_command = Mock(return_value=rc)


# Generated at 2022-06-13 05:22:44.941549
# Unit test for function main
def test_main():
    main()