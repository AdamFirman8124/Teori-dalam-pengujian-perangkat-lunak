

# Generated at 2022-06-13 05:23:51.240096
# Unit test for function main
def test_main():
    # unit tests
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', required=False),
            service=dict(type='str', required=False),
            split=dict(type='str', required=False),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    main()

# Generated at 2022-06-13 05:23:58.730965
# Unit test for function main
def test_main():
    # Importing module requires the following block
    import sys
    sys.path.append('.')
    from ansible.module_utils.basic import AnsibleModule

    # Stub module_utils.basic.AnsibleModule.run_command
    class RunCommandMock():
        def __init__(self):
            self.rc = 0
            self.out = ''
            self.err = ''

    run_command_mock = RunCommandMock()
    run_command_mock.rc = 1
    run_command_mock.out = ''
    run_command_mock.err = 'Missing arguments, or database unknown.'
    AnsibleModule.run_command = run_command_mock

    # Stub module_utils.basic.AnsibleModule.get_bin_path

# Generated at 2022-06-13 05:24:05.558592
# Unit test for function main
def test_main():
    a = AnsibleModule({
        'database': 'passwd',
        'key': 'root',
    })

    class FakeRunCommand():
        def __init__(self):
            self.rc = 0
            self.stdout = 'root:x:0:0:root:/root:/bin/bash'
            self.stderr = ''

    # set up the real run_command
    a.run_command = FakeRunCommand

    # fake getent_passwd
    import sys
    sys.modules['ansible_facts'] = type('fake facts', (), {})
    returncode, stdout, stderr = main()
    assert(returncode['ansible_facts']['getent_passwd']['root'] == ['x', '0', '0', 'root', '/root', '/bin/bash'])

# Generated at 2022-06-13 05:24:14.179467
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path

    getent_bin = get_bin_path('getent')
    assert(getent_bin)

    if getent_bin is not None:
        # test the passwd db
        module = basic.AnsibleModule(
            argument_spec=dict(
                database='passwd',
                key='root',
            )
        )
        main()
        # test the passwd db missing key
        module = basic.AnsibleModule(
            argument_spec=dict(
                database='passwd',
                key='nope',
            ),
            supports_check_mode=True,
        )
        main()
        # test a non-supported db

# Generated at 2022-06-13 05:24:22.319733
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        "database": {"required": True},
        "key": {},
        "service": {},
        "split": {},
        "fail_key": {"type": "bool", "default": True}
    })
    module.get_bin_path = mock.MagicMock(return_value='/usr/bin/getent')
    module.run_command = mock.MagicMock(return_value=(0, 'foo', ''))
    main()
    # again but with non-zero return code
    module.run_command = mock.MagicMock(return_value=(1, '', ''))
    main()

# Generated at 2022-06-13 05:24:22.891364
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:33.400254
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action
    import os
    import pytest
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.collections import is_sequence
    #import sys
    #sys.path.insert(0, os.path.dirname(__file__) + '/internal')
    #from main import getent_main
    os.environ['GETENT_BIN'] = '/bin/getent'


# Generated at 2022-06-13 05:24:39.695837
# Unit test for function main
def test_main():
    import tempfile
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b"1\troot\t30000\t30000\t\n")
    tmp.write(b"2\tdaemon\t30000\t30000\t\n")

# Generated at 2022-06-13 05:24:49.572949
# Unit test for function main
def test_main():
    # Mock our module args, as we would do when testing with unit tests
    import sys, os
    from ansible.module_utils import basic
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    # mock the module path, so we can import the main module
    path_orig = sys.path
    sys.path = [os.path.dirname(os.path.realpath(__file__))]

    # mock the action plugin loader, so we can import the main module
    cli_args = ['-m', 'getent', '-a', 'database=passwd', 'key=root']
    mock_runner_args = {'check': False, 'diff': False, 'module_args': 'database=passwd key=root'}
    action

# Generated at 2022-06-13 05:24:59.783100
# Unit test for function main
def test_main():
  args = {
    'database': 'iptables',
    'key': '',
    'split': '',
    'fails_key': False
}
  msg = main(args)
  assert args['database'] in msg['ansible_facts']['getent_iptables']

  args = {
    'database': 'hosts',
    'key': 'localhost',
    'split': '\\t',
    'fails_key': False
}
  msg = main(args)
  assert args['database'] in msg['ansible_facts']['getent_hosts']
  assert '127.0.0.1' in msg['ansible_facts']['getent_hosts']['localhost']


# Generated at 2022-06-13 05:25:21.164398
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    p = basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    main(p)

# Generated at 2022-06-13 05:25:32.783340
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

   

# Generated at 2022-06-13 05:25:45.168917
# Unit test for function main

# Generated at 2022-06-13 05:25:45.817927
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:58.308316
# Unit test for function main
def test_main():
  module = AnsibleModule(
    argument_spec=dict(
      database=dict(type='str', required=True),
      key=dict(type='str', no_log=False),
      service=dict(type='str'),
      split=dict(type='str'),
      fail_key=dict(type='bool', default=True)
    )
  )

  module.check_mode = True  # suppress warnings and command output
  module.params['database'] = 'aliases'
  module.params['key'] = 'root'
  module.params['service'] = 'sshd'
  module.params['split'] = ':'
  module.params['fail_key'] = True

  main()

# Generated at 2022-06-13 05:26:06.235292
# Unit test for function main
def test_main():

    from ansible.module_utils import basic
    from ansible.module_utils.common.dict_transformations import _to_lines
    from ansible.module_utils._text import to_native

    p = basic._ANSIBLE_ARGS
    s = "python", "library/examples/getent.py", "_", json.dumps({
        "ANSIBLE_MODULE_ARGS": {
            "database": "passwd",
            "key": "root",
        },
    })


# Generated at 2022-06-13 05:26:06.959022
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:26:16.597244
# Unit test for function main
def test_main():

    def test_run_command(params, rc, out, err):
        assert params == ['/usr/bin/getent', 'passwd', 'root']
        assert rc == 0
        assert out == 'root:x:0:0:root:/root:/bin/bash\n'
        assert err is None

    # ToDo: mock module object

    global module
    module = AnsibleModule
    module.run_command = test_run_command
    module.exit_json = lambda **x: None
    module.fail_json = lambda **x: None

    main()

# Generated at 2022-06-13 05:26:19.833676
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-13 05:26:33.916933
# Unit test for function main
def test_main():

    # Test failure cases
    module = AnsibleModule(dict(
        database='fail',
        key='fail',
    ))

    rc, out, err = module.run_command([module.get_bin_path('getent', True), 'passwd', 'root'])

    assert rc == 0

    rc, out, err = module.run_command([module.get_bin_path('getent', True)])
    assert rc == 1

    rc, out, err = module.run_command([module.get_bin_path('getent', True), 'passwd', 'missing key'])
    assert rc == 2

    rc, out, err = module.run_command([module.get_bin_path('getent', True), 'hosts', 'missing key'])
    assert rc == 0

    # Test with multiple results
    rc

# Generated at 2022-06-13 05:27:05.475016
# Unit test for function main
def test_main():
    module = None
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']
    database = "passwd"
    key = "root"
    split = None
    service = None
    fail_key = True

    getent_bin = module.get_bin_path('getent', True)
    if key is not None:
        cmd = [getent_bin, database, key]

# Generated at 2022-06-13 05:27:11.067247
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Test for shadow
    module.params = {"database": "shadow",
                     "key": "root",
                     }

    results = main()
    assert 'shadow' in results['ansible_facts']['getent_shadow'].keys()

    # Test for shadow
    module.params = {"database": "shadow",
                     }

    results = main()
    assert 'shadow' in results['ansible_facts'].keys

# Generated at 2022-06-13 05:27:19.690982
# Unit test for function main
def test_main():
    args = {
        'database': 'group',
        'key': 'foo',
        'check_mode': True
    }
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic
    m = basic.AnsibleModule(argument_spec=args)
    m.exit_json = unittest.mock.Mock(return_value=42)
    main()
    m.exit_json.assert_called_once()

# Generated at 2022-06-13 05:27:25.804022
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    
    assert False, "Not Implemented"

# Generated at 2022-06-13 05:27:39.745739
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict

    module_args = dict(
        database='group',
    )

    argv = ['-vvvvv', '/path/to/ansible/module', '-m', 'getent', '-a', 'database=group', '-k', '1']
    conn = basic.AnsibleConnection('local', '', '', module_args, None, to_bytes(argv), None, ImmutableDict(), False, False)

    module_return_value = {'ansible_facts': {'getent_group': 'test'}}
    rc, json_out, err = conn.run()

    assert rc == 0

# Generated at 2022-06-13 05:27:48.015521
# Unit test for function main
def test_main():
   import sys
   from ansible.module_utils._text import to_bytes
   from ansible.module_utils.six import PY3
   from ansible.module_utils.six.moves import StringIO
   from ansible.module_utils import basic
   from ansible.module_utils.basic import AnsibleModule
   from ansible.module_utils.action.getent import main

   if PY3:
      module_name = 'ansible.module_utils.action.getent.main'
   else:
      module_name = 'ansible.module_utils.action.getent'

   # dummy AnsibleModule object
   set_module_args = dict(
      database='passwd',
      key='root',
   )
   module = AnsibleModule(argument_spec=set_module_args)

   # capture

# Generated at 2022-06-13 05:28:00.726990
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as m:
        with patch('ansible.module_utils.facts.getent.get_bin_path') as f:
            f.return_value = '/usr/bin/getent'

            with patch('os.path.exists') as p:
                p.return_value = True

                with patch('os.access') as a:
                    a.return_value = True

                    with patch('ansible.module_utils.basic.AnsibleModule._run_command') as r:
                        r.return_value = (0, '\n'.join(['root:x:0:0:root:/root:/bin/bash', 'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin']), None)


# Generated at 2022-06-13 05:28:07.006223
# Unit test for function main
def test_main():
    import subprocess

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    basic._ANSIBLE_ARGS = to_bytes('')
    setattr(subprocess, 'Popen', lambda *args, **kwargs: FakePopen(*args, **kwargs))

    args = dict(
        database='passwd',
        key='root',
        split=':',
    )
    m = AnsibleModule(**args)

    main()


# Generated at 2022-06-13 05:28:17.706605
# Unit test for function main
def test_main():
    class Args:
        database = 'passwd'
        key = 'root'
        split = None
        fail_key = 'yes'

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    module._ANSIBLE_ARGS = ['getent', 'passwd', 'root']
    module.params = Args

    class module:
        def __init__(self):
            self.check_mode = False
            self.exit_json = print
            self.fail_

# Generated at 2022-06-13 05:28:18.359740
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:29:37.602761
# Unit test for function main
def test_main():
    import sys
    import os
    import json
    import getent

    curdir = os.getcwd()
    # put ../ansible on the module path
    ansible_dir = os.path.join(curdir, '..')
    sys.path.insert(0, ansible_dir)

    # copy the module code to a tmp directory
    test_dir = os.path.join(curdir, 'tmp')
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
    getent_module_path = os.path.join(test_dir, 'getent.py')
    source_module_path = os.path.join(curdir, 'getent.py')

# Generated at 2022-06-13 05:29:51.059251
# Unit test for function main
def test_main():
    arguments = dict(
        database='passwd',
        key='root'
    )

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Mock the module
    module.run_command = lambda cmd, check_rc=False, environ_update=None: (0, 'root:x:0:0:root:/root:/bin/bash', None)

    module.main()

    # Test if the arguments get passed to the the run command
    assert module.run_command

# Generated at 2022-06-13 05:29:57.750414
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    class MockPopen:
        def __init__(self, command, rc, out, err):
            self.command = command
            self.rc = rc
            self.out = out
            self.err = err

        def communicate(self):
            return (self.out, self.err)

        def wait(self):
            return self.rc

        def poll(self):
            return self.rc


# Generated at 2022-06-13 05:30:09.763262
# Unit test for function main
def test_main():
    import os
    import tempfile
    from mock import patch, MagicMock
    from ansible.module_utils.basic import AnsibleModule

    module = MagicMock()
    module_data = AnsibleModule.load_fixture('/tmp/fixture.py', os.path.abspath(os.path.dirname(__file__)), module)
    module.params = module_data['params']

    module.run_command = MagicMock(return_value=(0, '''abc:x:1000:1000:abc:/home/abc:/bin/bash
def:x:1001:1001:def:/home/def:/bin/bash''', ''))

    getent_bin = module.get_bin_path('getent', True)


# Generated at 2022-06-13 05:30:20.284062
# Unit test for function main
def test_main():
    module = AnsibleModule({
      "database": "group",
      "key": 'root',
      "split": ":",
      "fail_key": True,
    })

    module.run_command = MagicMock(return_value=(0, "root:x:0::0\nadm:x:4:root,someone\n", ""))

    main()

    assert module.exit_json.called
    assert module.exit_json.call_args[0][0]['ansible_facts']['getent_group'] == {'root': ['x', '0', '', '0'], 'adm': ['x', '4', 'root,someone']}


# Generated at 2022-06-13 05:30:21.247562
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:30:31.129810
# Unit test for function main
def test_main():
    import os
    import tempfile

    from ansible.module_utils.basic import AnsibleModule, env_fallback, load_platform_subclass

    # test case 1
    test_dict_1 = dict(
        database='passwd',
        key='root',
        split='x',
        service='x',
        msg='Unexpected failure!',
        stderr='',
        rc=0,
    )

    # test case 2
    test_dict_2 = dict(
        database='passwd',
        key='rootxx',
        split='x',
        service='x',
        msg='One or more supplied key could not be found in the database.',
        stderr='',
        rc=2,
    )

    # test case 3

# Generated at 2022-06-13 05:30:35.876031
# Unit test for function main
def test_main():
    getent_bin = main.module.get_bin_path('getent', True)
    assert getent_bin is not None

# Unit tests for function getent

# Generated at 2022-06-13 05:30:36.618175
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:30:42.219985
# Unit test for function main
def test_main():
    # Make sure basic import works
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({
        'state': 'present',
        'name': 'world',
    })

    # Make sure getent exist
    from ansible.module_utils.basic import get_exim_version
    get_exim_version('/usr/bin/')

# Generated at 2022-06-13 05:33:18.141984
# Unit test for function main
def test_main():
    assert True == False

# Generated at 2022-06-13 05:33:24.428280
# Unit test for function main
def test_main():
    '''
    Unit test for function main
    '''
    import platform
    import tempfile
    import os
    import sys
    import ansible.module_utils.basic

    if sys.version_info[0] < 3:
        ansible.module_utils.basic.ANSIBLE_PYTHON_MAJOR = 2

    if platform.system() != 'Linux':
        return

    # Create a temporary file
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_filename = tmp_file.name
    tmp_file.write('hello test file\n')
    tmp_file.close()

    # Create a temporary file to store results
    tmp_results = tempfile.NamedTemporaryFile(delete=False)
    tmp_results_name = tmp_results.name
    tmp_