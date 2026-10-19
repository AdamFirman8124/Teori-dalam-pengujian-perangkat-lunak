

# Generated at 2022-06-13 05:13:05.603905
# Unit test for function main
def test_main():
    # Test with a simple command and return code
    # command_outputs = []
    # command_outputs.append(CommandOutput("ls -l /proc/1/cwd", "", 0))
    #
    # module = AnsibleModule()
    # module.get_bin_path = Mock(return_value="ls")
    # module.run_command = MyRunCommand(command_outputs)
    #
    # main()

    pass

# Generated at 2022-06-13 05:13:06.891524
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        main()

# Generated at 2022-06-13 05:13:12.853162
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    name = "testName"
    selection = "testSelection"
    return_rc = 123
    return_out = "testOut"
    return_err = "testErr"
    rc, out, err = test_module.run_command(["echo", "test"], check_rc=True)
    test_selection = return_out.split()[1]
    changed = True
    test_module.exit_json(changed=changed, before='testBefore', after='testAfter')

# Generated at 2022-06-13 05:13:22.985277
# Unit test for function main
def test_main():
    import sys
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule, get_bin_path
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import binary_type, text_type
    from ansible.module_utils.six import iteritems, string_types
    from ansible.module_utils.six.moves import input

# Generated at 2022-06-13 05:13:32.187826
# Unit test for function main

# Generated at 2022-06-13 05:13:42.735988
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common.network import run_command

    dpkg = get_bin_path('dpkg', True)

    responses = {
        'dpkg --get-selections a': ('0', '', '', None),
    }

    def run_command(command, check_rc=None):
        response = responses.get(command)
        return response

    def get_bin_path(command, required):
        return dpkg

    basic.AnsibleModule = basic.AnsibleModule
    basic.AnsibleModule.get_bin_path = get_bin_path
    basic.AnsibleModule.run_command = run_command
    main()

# Generated at 2022-06-13 05:13:53.014838
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
    print(dpkg, name, selection)
    print(module.run_command([dpkg, '--get-selections', name], check_rc=True))
    print('Exit AnsibleModule function')
    return

# Generated at 2022-06-13 05:13:58.714325
# Unit test for function main
def test_main():
    from collections import namedtuple
    module = namedtuple('module', 'check_mode')
    module.check_mode = True
    module.get_bin_path = lambda x,y:'/usr/bin/dpkg'

    module.run_command = lambda x,**kwargs: (True, '', '')
    assert main() == { 'changed': True, 'after': 'not present', 'before': 'not present' }
    module.check_mode = False

    def run_command(x,check_rc=False,**kwargs):
        if x == ['/usr/bin/dpkg', '--get-selections', 'python']:
            return True, '', ''
        elif x == ['/usr/bin/dpkg', '--get-selections', 'python3-pip']:
            return True,

# Generated at 2022-06-13 05:14:07.356704
# Unit test for function main
def test_main():

    import sys
    import os
    import json

    my_dir = os.path.dirname(__file__)
    if my_dir:
        os.chdir(my_dir)

    test_cases = ['not present', 'install', 'deinstall', 'purge']
    for test in test_cases:
        os.environ['ANSIBLE_MODULE_ARGS'] = '{"name": "test", "selection": "%s", "check_mode": true}' % test

        module = __import__('main')
        sys.modules['main'] = module

        response = module.main()

        assert response['changed'] == False

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:14:13.892202
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import test_dpkg_selections
    module = test_dpkg_selections
    module.run_command = lambda *args, **kwargs: (0, "", "")
    module.check_mode = False
    module.get_bin_path = lambda *args, **kwargs: '/usr/bin/dpkg'
    setattr(module, '_ansible_module', AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    ))

    module.main()

# Generated at 2022-06-13 05:14:30.667058
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

# Generated at 2022-06-13 05:14:34.158505
# Unit test for function main
def test_main():
    with pytest.raises(OSError) as excinfo:
        main()
    assert 'No such file or directory' in str(excinfo.value)

# Generated at 2022-06-13 05:14:44.300884
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import sys

    class MyModule(object):
        pass

    module = MyModule()
    module.name = 'python'
    module.selection = 'hold'
    module.params = dict(name='python', selection='hold')
    module.run_command = lambda cmd, **kw: (0, module.selection, 'error')
    module.get_bin_path = lambda bin, required: sys.executable
    module.check_mode = False
    module.exit_json = lambda **kw: os._exit(0)


# Generated at 2022-06-13 05:14:45.071236
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:14:55.258965
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    module.run_command = Mock(return_value=(0, "", ""))
    module.check_mode = False
    module.params['name'] = 'python'
    module.params['selection'] = 'hold'

    dpkg_selections.main()


# Generated at 2022-06-13 05:15:06.561474
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

# Generated at 2022-06-13 05:15:07.815181
# Unit test for function main
def test_main():
    assert main([]) == ("", None)

# Generated at 2022-06-13 05:15:19.040605
# Unit test for function main
def test_main():
    # This test involves the shell command, dpkg
    # Python mock library is required for this test (pip install mock)
    import mock
    import os
    import sys

    # Mock out os.geteuid() to always return 0 (root)
    os.geteuid = mock.MagicMock(return_value=0)

    # Mock out the 'run_command' function so it always returns 0 (no failures)
    # See: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock.return_value
    # All functions mocked out in this way must be called with the absolute path of the function
    # to mock out. In other words, main().run_command is mocked out, not module_utils.basic.AnsibleModule.run_command
    # This is

# Generated at 2022-06-13 05:15:28.721677
# Unit test for function main
def test_main():
    def run_command(module_name, command, check_rc):
        # print("###### command is {}".format(command))
        if command == ['dpkg', '--get-selections', 'python']:
            return (0, "python       install\n", "")
        elif command == ['dpkg', '--get-selections', 'ruby']:
            return (0, "ruby         \n", "")
        elif command == ['dpkg', '--set-selections']:
            return (0, "", "")

    def get_bin_path(module_name, bin_name, required):
        return '/usr/bin/dpkg'
        
    def exit_json(module_name, changed, before, after):
        assert changed == True
        assert before == 'not present'

# Generated at 2022-06-13 05:15:34.802887
# Unit test for function main
def test_main():
    content = dict(
        name='testname',
        selection='testselection',
        changed=True
    )

    # test with the usually values
    check_main(content)
    # test with float param
    content['selection'] = 100.0
    check_main(content)
    # test with bool param
    content['selection'] = True
    check_main(content)


# Generated at 2022-06-13 05:15:51.794701
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import Mapping
    import json

    module_args = dict(
        name=dict(required=True, type='str'),
        selection=dict(required=True, type='str')
    )

    test_name = 'python'
    test_selection = 'hold'
    test_current = 'not present'
    changed = True

    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, name, req=False):
            if name == 'dpkg':
                return '/usr/bin/dpkg'
            else:
                return None


# Generated at 2022-06-13 05:15:52.438053
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:16:05.718764
# Unit test for function main
def test_main():
    import os
    import tempfile
    import json

    eval_result = None

    # Test simple case, no error check mode
    module_args = {
        "name": "python",
        "selection": "hold",
    }

    with tempfile.NamedTemporaryFile(suffix=".data") as tf:
        data_file = tf.name
        os.chmod(data_file, 0o600)
        tf.write(b'python hold')
        tf.seek(0)


# Generated at 2022-06-13 05:16:14.432040
# Unit test for function main
def test_main():
    import os
    import sys
    import platform
    import tempfile
    import shutil
    import subprocess

    temp_dir = tempfile.mkdtemp()

    if platform.system() == 'Darwin':
        # python2
        if sys.version_info[0] == 2:
            cmd = '/usr/bin/python -m ansible.module_utils.basic'
        # python3
        else:
            cmd = '/usr/bin/python3 -m ansible.module_utils.basic'
    else:
        cmd = 'python -m ansible.module_utils.basic'

    # test config file
    args = {
        'ANSIBLE_MODULE_ARGS': {
            'dpkg': 'dpkg',
            'name': 'python',
            'selection': 'hold'
        }
    }

# Generated at 2022-06-13 05:16:19.975052
# Unit test for function main
def test_main():

    name = 'python'
    selection = 'hold'
    module_args = {'name': name, 'selection': selection}

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


# Generated at 2022-06-13 05:16:27.565859
# Unit test for function main

# Generated at 2022-06-13 05:16:28.602244
# Unit test for function main
def test_main():
    print("TESTING dpkg_selections")
    assert True

# Generated at 2022-06-13 05:16:34.117468
# Unit test for function main
def test_main():
    '''
    Unit test for main()
    '''
    test_args = {}
    test_args = {
        'selection': 'install',
        'name': 'python',
        'check_mode': 'no'
    }
    # This will return False as no python package is installed
    test_result = main(test_args)
    # Actual result
    ac = False
    assert test_result == ac

# Generated at 2022-06-13 05:16:44.888665
# Unit test for function main
def test_main():
    dpkg = '/bin/dpkg'
    class OpenshiftModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.params['_ansible_check_mode'] = True
            self.params['_ansible_verbosity'] = 0
            self.params['_ansible_diff'] = False
            self.params['_ansible_debug'] = False
            self.checks_loaded = False
            self.no_log = False
            self.exit_json = lambda **kwargs: sys.exit()
            self.fail_json = lambda **kwargs: sys.exit(2)
            self.run_command = self.run_command_mock
            self.get_bin_path = lambda *args, **kwargs: dpkg
            self

# Generated at 2022-06-13 05:16:51.263281
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )
    name = 'python'
    selection = 'hold'
    out = 'python         deinstall\n'
    module.run_command = MagicMock(return_value=(0, out, ''))
    main()
    module.run_command.assert_any_call(['dpkg', '--get-selections', name], check_rc=True)
    module.run_command.assert_any_call(['dpkg', '--set-selections'], data="python hold", check_rc=True)

# Generated at 2022-06-13 05:17:28.590661
# Unit test for function main
def test_main():
    from ansible_collections.ansible.community.plugins.module_utils.modules import dpkg_selections as module

    def run_command_mock(cmd, data=None):
        if cmd == ['dpkg', '--get-selections', 'python']:
            return 0, 'python install', ''
        if cmd == ['dpkg', '--set-selections']:
            return 0, '', ''
        raise AssertionError('Unexpected run_command call: %s' % cmd)

    def exit_json_mock(changed, before, after):
        assert changed
        assert before == 'install'
        assert after == 'hold'

    def fail_json_mock(*args, **kwargs):
        raise AssertionError('fail_json should not be called')


# Generated at 2022-06-13 05:17:29.817776
# Unit test for function main
def test_main():
    # Test sanity.
    assert True

# Generated at 2022-06-13 05:17:40.063009
# Unit test for function main
def test_main():
    from ansible.module_utils.six.moves import StringIO

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    name = 'name'
    module.params['name'] = name

    selection = 'selection'
    module.params['selection'] = selection

    dpkg = module.get_bin_path('dpkg', True)

    rc = 0
    err = 'errmsg'
    out = StringIO("%s %s" % (name, selection))
    module.run_command.return_value = rc, out.read(), err

    main()

    module.run_command

# Generated at 2022-06-13 05:17:51.311166
# Unit test for function main
def test_main():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.ansible_release import __version__ as ansible_version

    ansible_2_9 = ansible_version >= '2.9.0'

    # Import module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

    # Ansible 2.9.0+ modules should check change and fail

# Generated at 2022-06-13 05:17:59.584869
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={
            'name': {'required': True},
            'selection': {'choices': ['install', 'hold', 'deinstall', 'purge'], 'required': True},
        },
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


# Generated at 2022-06-13 05:18:00.125828
# Unit test for function main

# Generated at 2022-06-13 05:18:05.587940
# Unit test for function main
def test_main():

    import tempfile
    import os

    dpkg = os.path.join(tempfile.gettempdir(), 'dpkg_selections.py')

# Generated at 2022-06-13 05:18:15.675680
# Unit test for function main
def test_main():

    for _ in range(5):
        module = AnsibleModule(argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True)

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
        assert changed

# Generated at 2022-06-13 05:18:18.641874
# Unit test for function main
def test_main():
    assert main(["python", "/usr/share/lizardfs/tests/dpkg_selections/test.py"],
        [], ["name: test-package\n"]) == 0

# Generated at 2022-06-13 05:18:27.586785
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

# Generated at 2022-06-13 05:19:19.827576
# Unit test for function main
def test_main():
    # Mock AnsibleModule's exit_json
    with patch.object(AnsibleModule, 'exit_json') as mock_exit_json:
        # Call main() with empty args
        main()
        # assert AnsibleModule.exit_json was called
        AnsibleModule.exit_json.assert_called_with(changed=False, after='x', before='x', name='x', selection='x')


# Generated at 2022-06-13 05:19:23.249228
# Unit test for function main
def test_main():
  #pylint: disable=undefined-variable
  module = AnsibleModule(
    argument_spec={'name': {'required': True}, 'selection': { 'choices': [ 'install', 'hold', 'deinstall', 'purge' ], 'required': True}},
    supports_check_mode=True
  )
  assert main() == None


# Generated at 2022-06-13 05:19:31.887737
# Unit test for function main
def test_main():
    content = '''
        # This is a big long comment
        test line: data:
        '''

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

# Generated at 2022-06-13 05:19:44.546709
# Unit test for function main
def test_main():
    test = AnsibleModule(argument_spec=dict(
        name=dict(required=True),
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    ),
    supports_check_mode=True,)
    test.get_bin_path = lambda module, required, opt_dirs=None: "Test"
    test.check_mode = False
    test.params = dict(
        name='Test',
        selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
    )
    test.run_command = lambda args, check_rc=False, close_fds=True, executable=None, data=None: (1, "", "")

# Generated at 2022-06-13 05:19:55.307299
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

# Generated at 2022-06-13 05:19:56.535615
# Unit test for function main
def test_main():
  main_test = main()
  assert main_test != 0

# Generated at 2022-06-13 05:20:07.246937
# Unit test for function main
def test_main():

    # Import modules used by this function
    import tempfile
    import os

    # Create an empty AnsibleModule with defaults for testing
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # Make a temporary file to use as the dpkg binary
    tempdir = tempfile.mkdtemp()
    dpkg = open(os.path.join(tempdir, 'dpkg'), 'w')

    # Expect a call to dpkg --get-selections to fail the first time
    # then the second time to return ok
    dpkg.write('#!/bin/sh\n')
    dpkg.write('OUTPUT="$(echo \'$@\' | grep \'--get-selections\')"\n')
    dpkg.write('if [ -n "$OUTPUT" ]; then\n')
   

# Generated at 2022-06-13 05:20:09.798334
# Unit test for function main
def test_main():
  ALL_PARAMS = {
    'name': 'python',
    'selection': 'hold'
  }
  from ansible.module_utils.basic import AnsibleModule
  module = AnsibleModule(argument_spec=ALL_PARAMS)
  main()

# Generated at 2022-06-13 05:20:13.736270
# Unit test for function main
def test_main():
    test = AnsibleModule('action', 'test', 'test.yml')
    test.run_command(['dpkg', '--set-selections'], data="test hold", check_rc=True)
    assert test.run_command(['dpkg', '--get-selections', 'test']) == 'test hold'

# Generated at 2022-06-13 05:20:19.193598
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


# Generated at 2022-06-13 05:22:33.997333
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    module = basic._AnsibleModule()
    module.params = {'name':'python','selection':'hold','_ansible_check_mode':True}
    result = main()
    print(result)

test_main()

# Generated at 2022-06-13 05:22:39.030035
# Unit test for function main
def test_main():
    def run_command(self, command, data=None, check_rc=False, close_fds=False, executable=None, use_unsafe_shell=False, env=None, cwd=None, stdin=None, stdout=None, stderr=None):
        if command[0] == 'dpkg' and command[1] == '--get-selections':
            return (0, 'python	install', "")
        if command[0] == 'dpkg' and command[1] == '--set-selections':
            return (0, "", "")
    setattr(AnsibleModule, "run_command", run_command)

    class ModuleTest():
        def __init__(self):
            self.params = {}
            self.changed = False
            self.exit_json = exit_json
           

# Generated at 2022-06-13 05:22:44.767002
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            selection=dict(choices=['install', 'hold', 'deinstall', 'purge'], required=True)
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:22:53.107179
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