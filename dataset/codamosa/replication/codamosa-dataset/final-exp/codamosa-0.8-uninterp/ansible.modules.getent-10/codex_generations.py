

# Generated at 2022-06-13 05:23:45.503240
# Unit test for function main
def test_main():
    # Make all asserts 'lazy' so we can see whether the code raises an exception or not, and get a full traceback
    # in the logs.
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 05:23:56.927955
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={
        'database': {'type': 'str', 'required': True},
        'key': {'type': 'str', 'no_log': False},
        'service': {'type': 'str'},
        'split': {'type': 'str'},
        'fail_key': {'type': 'bool', 'default': True},
    })
    module.run_command = Mock(return_value=(0, 'test:test:test:test:test::test:test', None))
    test_main()
    assert module.exit_json.called
    assert module.fail_json.called == 0
    assert module.run_command.called == 1

# Generated at 2022-06-13 05:24:08.519433
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required='true'),
            key=dict(type='str', required=False),
            service=dict(type='str', required=False),
            split=dict(type='str', required=False),
            fail_key=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )

    m_run_command = module.run_command
    m_run_command.return_value = (0, '', '')
    m_get_bin_path = module.get_bin_path

    ret_command = ['getent', 'hosts']
    ret_command_args = ['getent', 'hosts', 'localhost']

    # Testing getent_hosts

# Generated at 2022-06-13 05:24:20.432608
# Unit test for function main
def test_main():
    # Fake arguments for testing
    class Args(object):
        def __init__(self, database, key, split, service, fail_key):
            self.database = database
            self.key = key
            self.split = split
            self.service = service
            self.fail_key = fail_key

    # Fake module for testing
    class Module(object):
        def __init__(self, argument_spec, check_invalid_arguments, supports_check_mode, no_log, mutually_exclusive, required_together, required_one_of, required_by, add_file_common_args, supports_diff, supports_encrypted_keyed_values):
            self.argument_spec = argument_spec
            self.check_invalid_arguments = check_invalid_arguments

# Generated at 2022-06-13 05:24:27.052166
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    from ansible.module_utils.common.collections import ImmutableDict
    # AnsibleModule Mocking
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
    )

    # stub command execution
    def run_command_stub(command, check_rc=False):
        return [0, '', '']
    ansible.module_utils.basic.AnsibleModule.run_command = run_command_stub

    # Function call
    main()

# Generated at 2022-06-13 05:24:40.613283
# Unit test for function main
def test_main():
    import os
    import json
    import pytest

    from ansible.cli import CLI
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    def execute_module(module_name=None, module_args=None):
        cli = CLI(args=[])
        cli._load_plugins()
        cli._display.verbosity = 3
        cli.run()
        loader, inventory, variable_manager = cli._get_core_plugins()
        module_args = module_args or {}

        if module_name is None:
            module_args.update(
                dict(
                    _ansible_debug=True,
                    ansible_facts=dict(),
                    _ansible_module_name="getent",
                )
            )

        module

# Generated at 2022-06-13 05:24:50.433620
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    # Some tests need native strings
    module.run_command = lambda x, environ_update=None, check_rc=False, binary_data=False: (0, to_native(x), None)
    # Test missing key
    assert module.from_json(main()) == {
        'ansible_facts': {
            'getent_database': {
            }
        },
        'changed': False,
    }
    # Test key success
    module.params['key'] = 'test'
    assert module.from_json

# Generated at 2022-06-13 05:24:51.983237
# Unit test for function main
def test_main():
    module = AnsibleModule({})
    assert main() == True

# Generated at 2022-06-13 05:25:01.154556
# Unit test for function main
def test_main():
    import sys
    import os
    module_data = dict(
        path='/usr/bin:/usr/sbin:/bin:/sbin',
        database='passwd',
        split=':',
        key='root',
        state='present',
    )
    module_data['_ansible_sys_executable'] = sys.executable
    module_data['_ansible_shell_executable'] = '/bin/sh'
    module_data['_ansible_tmpdir'] = os.getcwd() + '/tmp'
    module_data['_ansible_shell_type'] = 'posix'
    module_data['_ansible_python_interpreter'] = sys.executable
    module_data['_ansible_remote_tmp'] = module_data['_ansible_tmpdir']

# Generated at 2022-06-13 05:25:07.150146
# Unit test for function main
def test_main():

    # basic passwd test
    getent_passwd_raw = "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\n"

    # basic group test

# Generated at 2022-06-13 05:25:32.952155
# Unit test for function main
def test_main():
    import json
    import os
    import subprocess
    import sys
    import tempfile
    from ansible.module_utils import basic

    PRINT_JSON_FORMAT = '%s'

    def _exec(cmd):
        # We need to create a new stdin for the subprocess so that it does not get
        # redirected to the pipe that we read from here.
        (fd_null, fname_null) = tempfile.mkstemp()
        (fd_pipe_out, fname_pipe_out) = tempfile.mkstemp(prefix='ansible-test-module')


# Generated at 2022-06-13 05:25:33.478143
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:39.537739
# Unit test for function main
def test_main():
    global module, getent_bin
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

    database = 'passwd'
    key = 'root'
    split = ':'

    getent_bin = module.get_bin_path('getent', True)
    assert getent_bin == '/usr/bin/getent'

    if key is not None:
        cmd = [getent_bin, database, key]

# Generated at 2022-06-13 05:25:48.891016
# Unit test for function main
def test_main():
    import os
    import tempfile
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(required=True),
            key=dict(type='str', default=''),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    # Create the temp database file
    fd, temp_path = tempfile.mkstemp()
    f = os.fdopen(fd, "w")
    colon = ['passwd', 'shadow', 'group', 'gshadow']

    #

# Generated at 2022-06-13 05:25:51.757455
# Unit test for function main
def test_main():
    argv = ["--database", "passwd",
            "--key", "root"]
    module = AnsibleModule( argument_spec=dict(),
                            supports_check_mode=True)
    module.getent_bin = 'getent'
    rc, out, err = module.run_command([])

    if rc == "0":
        pass

# Generated at 2022-06-13 05:25:52.161360
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:56.797516
# Unit test for function main
def test_main():
    """
    Test with parameters:
        database: 'passwd'
        key: 'root'
    """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    import os
    import pytest

    module_args = dict(
        database='passwd',
        key='root'
    )
    args = ['ansible', '-m', __file__, '-a', module_args]

# Generated at 2022-06-13 05:26:05.993207
# Unit test for function main
def test_main():
    import tempfile
    import shutil

    with tempfile.NamedTemporaryFile(delete=False) as f:
        tmp_file = f.name

        shutil.copy2(tmp_file, tmp_file + '.bak')


# Generated at 2022-06-13 05:26:19.043409
# Unit test for function main
def test_main():

    fake_check_mode = False
    fake_split = ':'
    fake_cmd = ['abc', 'abc', 'abc']
    fake_rc = 0
    fake_out = 'abc:123'
    fake_err = ''

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

    module.get_bin_path = MagicMock(return_value='abc')

# Generated at 2022-06-13 05:26:25.603488
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'database': 'passwd',
        'key': 'root'
    })
    rc = 0
    out = 'root:x:0:0:root:/root:/bin/bash'
    err = ''
    module.run_command = lambda x: (rc, out, err)
    main()
    assert module.exit_json.called
    assert module.exit_json.call_args[0][0]['ansible_facts']['getent_passwd'] == {'root': ['x', '0', '0', 'root', '/root', '/bin/bash']}


# Generated at 2022-06-13 05:27:00.289586
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils.action import ActionBase
    from ansible.module_utils.facts import ModuleFacts

    mf = ModuleFacts('getent', module_utils=basic)
    mf._action = ActionBase(mf)

    data = {
        'database': 'passwd',
        'key': 'root',
    }
    mf.normalize_module_parameters(data)
    # test_main() is called at the end of this file
    sys.exit(mf.run(data))

# Generated at 2022-06-13 05:27:05.513121
# Unit test for function main
def test_main():
    from ansible import context
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.local import LocalAnsibleModule, NeedsRepo
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.json_utils import AnsibleJSONEncoder
    from ansible.module_utils.basic import AnsibleModule

    vars = {}
    results = {}
    execute_command = module.run_command

    class LocalAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(LocalAnsibleModule, self).__init__(*args, **kwargs)
            self.fail_json = self.exit_json
            self.exit_json = self.exit_json_local

# Generated at 2022-06-13 05:27:16.970767
# Unit test for function main
def test_main():

    class Args(object):
        def __init__(self, **kwargs):
            for k in kwargs.keys():
                self.__setattr__(k, kwargs[k])

    def get_bin_path_mock(name, required):
        return name

    def run_command_mock(args):
        if 'shadow' in args:
            return 0, "root::16606:0:99999:7:::", ""
        return 0, "root:x:0:root", ""


# Generated at 2022-06-13 05:27:25.448513
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            service=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
    )
    class TestException(Exception):
        pass

    # Basically the same test as above but with a key we know will not
    # return a result so we test the failure case
    try:
        main()
    except TestException:
        pass

# Generated at 2022-06-13 05:27:26.313955
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:27:27.571760
# Unit test for function main
def test_main():

    # This will be replaced with a proper test
    assert None

# Generated at 2022-06-13 05:27:28.686318
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:27:35.403953
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    class Args:
        pass

    m = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    args = Args()
    args.database = 'passwd'
    args.key = 'root'
    args.split = ':'
    args.service = None
    args.fail_key = True
    m.params = vars(args)

    main()

    args.database = 'group'

# Generated at 2022-06-13 05:27:40.662458
# Unit test for function main
def test_main():
    # Declare var with params
    database = "passwd"
    key = "root"
    split = ":"
    # Declare var to store results
    results = {'module_result': {'out': 'out'}, 'module_args': {'key': 'root'}}
    # Call main function
    main()
    # Check if module.exit_json called
    assert main.call_count == 1
    # Get last call
    call = main.call_args
    # Check module.exit_json results
    assert call == call(results)
    # Get global var
    global main_results
    # Check global var
    assert main_results == dict(ansible_facts=results)
    # Declare var with params
    database = "passwd"
    key = "root"
    split = ":"
    #

# Generated at 2022-06-13 05:27:47.782814
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
  module.run_command = MagicMock(return_value=(0, "test1\ntest2\ntest3", ""))
  main()

  module.run_command.assert_called_with([module.get_bin_path('getent', True), 'test'])
  assert module.exit_json.called

# Generated at 2022-06-13 05:28:48.578329
# Unit test for function main
def test_main():
    args = dict(
        database="passwd",
        key="root",
        split=":",
        fail_key=True,
    )

    rc = main(args)
    assert rc == {
        "ansible_facts": {
            "getent_passwd": {"root": ["x", "0", "0", "root", "/root", "/bin/sh"]}
        }
    }



# Generated at 2022-06-13 05:28:48.959313
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:28:57.300861
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text import to_native

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught
        by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught
        by the test case"""
        pass

    module_args = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    )

# Generated at 2022-06-13 05:29:00.580355
# Unit test for function main
def test_main():
    test_cases = [
        {
            "cmd": [
                'getent',
                'passwd',
                'root',
            ],
            "expected_results": {
                "getent_passwd": {
                    "root": ["x","0","0","root","/root","/bin/bash"],
                },
            },
        }
    ]

    for test_case in test_cases:
        rc, out, err = module.run_command(test_case['cmd'])
        assert rc == 0
        assert out == test_case['expected_results']

# Generated at 2022-06-13 05:29:01.926396
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:29:10.128365
# Unit test for function main
def test_main():
    # pylint: disable=global-variable-not-assigned
    # pylint: disable=undefined-variable

    global module
    global getent_bin
    global database
    global key
    global split
    global service

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

    database = 'passwd'
    key = 'root'
    split = ':'
    service = None



# Generated at 2022-06-13 05:29:17.251243
# Unit test for function main
def test_main():
    import platform
    import unittest

    class TestGetentModule(unittest.TestCase):

        def setUp(self):
            self.module = AnsibleModule(
                argument_spec=dict(
                    state=dict(default='present', choices=['present', 'absent']),
                    name=dict(required=True),
                    force=dict(default=False, type='bool'),
                    prefix=dict(default='/etc/sudoers.d', type='path'),
                    backup=dict(default='yes', type='bool'),
                    mode=dict(default='0440'),
                    seuser=dict(default=None),
                    serole=dict(default=None),
                    setype=dict(default=None),
                    selevel=dict(default=None),
                ),
                supports_check_mode=True
            )



# Generated at 2022-06-13 05:29:18.089418
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:29:18.705350
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 05:29:29.628478
# Unit test for function main
def test_main():
    module_args = dict(
        database='passwd',
        key='root',
        split=':',
    )
    result = dict(
        ansible_facts=dict(
            getent_passwd=dict(
                root=['x', '0', '0', 'root', '/root', '/bin/bash']
            )
        )
    )
    module = AnsibleModule(module_args)
    module.exit_json = lambda x: x
    module.run_command = lambda cmd: (0, 'root:x:0:0:root:/root:/bin/bash\n', '')

    assert result == main()

# Generated at 2022-06-13 05:31:19.181812
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool'),
        ),
        # supports_check_mode=True,
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd

# Generated at 2022-06-13 05:31:30.748527
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

   

# Generated at 2022-06-13 05:31:31.266594
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:31:32.662785
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:31:40.885995
# Unit test for function main
def test_main():
    def test_module(module):
        mod = AnsibleModule(
            argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                service=dict(type='str'),
                split=dict(type='str'),
                fail_key=dict(type='bool', default=True),
            ),
            supports_check_mode=True,
        )
        return mod

    class TestModule(object):
        @classmethod
        def fail_json(cls, msg=""):
            raise Exception(msg)

        @classmethod
        def exit_json(cls, ansible_facts=None, msg="", **kwargs):
            return ansible_facts, msg


# Generated at 2022-06-13 05:31:46.299768
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        )
    )

    main(module)

# Generated at 2022-06-13 05:31:47.105770
# Unit test for function main

# Generated at 2022-06-13 05:31:56.259007
# Unit test for function main
def test_main():
    getent_bin = '/usr/bin/getent'

    # Unit test for main()
    class TestGetent(object):
        def __init__(self):
            self.fail_json = lambda msg, **kwargs: fail(msg)
            self.exit_json = lambda msg, **kwargs: succeed(msg)
            self.run_command = lambda args, **kwargs: succeed('')
            self.registered_arguments = {'split': None, 'key': 'root', 'database': 'passwd'}

        def get_bin_path(self, name, alt_paths=None):
            return getent_bin

    test_module = TestGetent()
    main()

# Generated at 2022-06-13 05:31:58.654940
# Unit test for function main
def test_main():
    args = dict(
        database='passwd',
        key='root',
    )
    run_ansible_module(module_args=args, check_mode=False)


# Generated at 2022-06-13 05:32:06.315119
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({
        'database': 'passwd',
        'key': 'root',
    })

    old_run_command = module.run_command

    def run_command(cmd, *args, **kwargs):
        cmd = [str(c) for c in cmd]
        if cmd == ['/usr/bin/getent', 'passwd', 'root']:
            return (0, to_bytes('root:x:0:0:root:/root:/bin/bash'), None)
        else:
            return old_run_command(cmd, *args, **kwargs)

    setattr(module, 'run_command', run_command)
    main() # Will fail unless test passes