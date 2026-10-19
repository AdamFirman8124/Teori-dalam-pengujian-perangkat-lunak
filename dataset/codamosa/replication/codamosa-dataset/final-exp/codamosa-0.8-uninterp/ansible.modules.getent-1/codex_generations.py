

# Generated at 2022-06-13 05:23:55.064086
# Unit test for function main
def test_main():
  module = AnsibleModule(
      argument_spec={
          'database': {'required': True, 'type': 'str'},
          'key': {'no_log': False, 'type': 'str'},
          'service': {'type': 'str'},
          'split': {'type': 'str'},
          'fail_key': {'default': True, 'type': 'bool'},
      },
      supports_check_mode=True,
  )

  database = module.params['database']
  key = module.params.get('key')
  split = module.params.get('split')
  service = module.params.get('service')
  fail_key = module.params.get('fail_key')

  getent_bin = module.get_bin_path('getent', True)


# Generated at 2022-06-13 05:23:55.599370
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:23:56.509067
# Unit test for function main
def test_main():
    global KEY
    KEY = 'root'
    main()

# Generated at 2022-06-13 05:24:01.899765
# Unit test for function main
def test_main():
    from ansible.utils.contextmanager import RedirectStream
    from ansible.module_utils import basic
    import io

    import ansible.module_utils.facts as ansible_facts
    from ansible.module_utils.facts import get_distribution
    from ansible.module_utils.facts import get_distribution_version
    from ansible.module_utils.facts import get_distribution_release
    from ansible.module_utils.facts import get_system_vendor

    from ansible.module_utils.basic import AnsibleModule

    class AnsibleModuleMock(object):

        def __init__(self, facts, distro):
            self.facts = facts
            self.distro = distro
            self.params = {}
            self.fail_json = lambda x: exit(1)
            self.exit_json

# Generated at 2022-06-13 05:24:11.656764
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import facts
    from ansible.module_utils.facts import default_collectors

    m_ansible = basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    m_ansible.params = dict(
        database='passwd',
        key='root',
        split=':',
        fail_key=False,
    )

    from ansible.module_utils.basic import AnsibleModule_fail_json

# Generated at 2022-06-13 05:24:21.993252
# Unit test for function main
def test_main():
    # Invalid DB
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='bool'),
        ),
        supports_check_mode=True
    )

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]

    if split is True and database in colon:
        split = ':'


# Generated at 2022-06-13 05:24:32.842657
# Unit test for function main
def test_main():
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

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')

    results = {
        'getent_%s' % database:
        {'foo': ['bar']}
    }

    if key is not None:
        cmd = ['getent', database, key]

# Generated at 2022-06-13 05:24:37.962760
# Unit test for function main
def test_main():
	dict={}
	dict['database']='passwd'
	dict['key']='root'
	dict['service']=''
	dict['split']=None
	dict['fail_key']=True
	dict['check_mode']=True
	#dict['diff_mode']=True
	dict['facts']=True
	dict['platform']='posix'
	main(dict)


# Generated at 2022-06-13 05:24:48.319044
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            service=dict(type='str'),
            fail_key=dict(type='bool'),
        ),
        supports_check_mode=False,
    )

    database = module.params['database']
    key = module.params.get('key')
    service = module.params.get('service')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    module.exit_json(ansible_facts=get_getent_facts(module, database, split, service, key, fail_key))


# Generated at 2022-06-13 05:24:48.699671
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:08.998227
# Unit test for function main
def test_main():

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

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]
   

# Generated at 2022-06-13 05:25:19.966323
# Unit test for function main
def test_main():
    import ansible.module_utils.basic

    m = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
    )

    m.run_command = lambda x: (0, '', '')


# Generated at 2022-06-13 05:25:24.903871
# Unit test for function main
def test_main():
    return '{"changed": false, "invocation": {"module_args": {"database": "group", "key": "", "split": ":"}}, "success": true, "ansible_facts": {"getent_group": {"root": ["x", "0", ""]}}}'

# Generated at 2022-06-13 05:25:34.755904
# Unit test for function main
def test_main():
    testargs = "--database passwd".split()
    assert main(testargs) == 0
    testargs = "--database passwd --key root".split()
    assert main(testargs) == 0
    testargs = "--database group".split()
    assert main(testargs) == 0
    testargs = "--database group --key root".split()
    assert main(testargs) == 0
    testargs = "--database hosts".split()
    assert main(testargs) == 0
    testargs = "--database services".split()
    assert main(testargs) == 0
    testargs = "--database services --key http".split()
    assert main(testargs) == 0
    testargs = "--database shadow".split()
    assert main(testargs) == 0

# Generated at 2022-06-13 05:25:44.945606
# Unit test for function main
def test_main():
    getent_bin = '/bin/getent'
    rc = 1

    database = 'group'
    key = None
    split = ':'
    service = None
    fail_key = True

    class TestModule(object):
        def get_bin_path(self, bin, required, opts=None):
            return getent_bin

        def run_command(self, bin):
            return rc, '', ''

        def fail_json(self, **kwargs):
            return

        def exit_json(self, **kwargs):
            return

    test_module = TestModule()
    main()



# Generated at 2022-06-13 05:25:58.812200
# Unit test for function main
def test_main():
    import sys
    from io import StringIO

    arguments = dict(
        database='passwd',
        key='root',
    )

    # Set stdin and stdout as StringIO objects to simulate user input
    # and captured output from running a module.
    captured_stdout = StringIO()
    sys.stdout = captured_stdout

    captured_stdin = StringIO()
    sys.stdin = captured_stdin

    # Create a module object and execute main()

# Generated at 2022-06-13 05:26:07.490384
# Unit test for function main
def test_main():
    # Success case
    import os
    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.params['database'] = 'passwd'
            self.params['key'] = 'root'
            if os.path.exists('/usr/bin/getent'):
                self.params['_ansible_verbosity'] = 0
                self.get_bin_path = lambda x, y: '/usr/bin/getent'
        def fail_json(self, **kwargs):
            raise AssertionError('fail_json(%s)' % kwargs)
        def exit_json(self, **kwargs):
            return kwargs
        def run_command(self, cmd):
            rc = 0

# Generated at 2022-06-13 05:26:20.022942
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
    )

    test_module.run_command = mock.Mock()
    test_module.run_command.return_value = (0, 'key1:value1\nkey2:value2\n', '')
    test_module.params = {'database': 'passwd', 'key': None, 'split': ':'}

    result = main(test_module)
    assert result['ansible_facts']['getent_passwd']['key1']

# Generated at 2022-06-13 05:26:21.182096
# Unit test for function main
def test_main():
    # Name function as we are testing it
    main()



# Generated at 2022-06-13 05:26:34.149234
# Unit test for function main
def test_main():
    # Stub for function main
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


# Generated at 2022-06-13 05:27:05.524506
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 05:27:16.969069
# Unit test for function main
def test_main():
    import json

    return_dict = {
        'changed': True,
        'msg': 'some_fake_message',
        'ansible_facts': None,
    }

    ### Positive tests ###
    test_cases = [
        ('', '', '', '', '', '', ''),
        ('', '', '', '', '', '', ''),
        ('', '', '', '', '', '', ''),
    ]


# Generated at 2022-06-13 05:27:18.471160
# Unit test for function main
def test_main():
    '''
    getent.main unit test stub
    '''
    pass

# Generated at 2022-06-13 05:27:28.659819
# Unit test for function main
def test_main():
    test = False
    import sys
    import os
    import datetime
    import subprocess

    # GET THE PATH TO THE TEST FOLDER
    test_path = os.path.dirname(os.path.realpath(__file__))
    test_path += "/test_assets/"

    test_modules = {}
    test_modules["basic"] = {}
    test_modules["basic"]["getent_passwd"] = [
        ["root", "x", "0", "0", "root", "/root", "/bin/bash"],
        ["daemon", "x", "1", "1", "daemon", "/usr/sbin", "/bin/sh"],
        ["bin", "x", "2", "2", "bin", "/bin", "/bin/sh"],
    ]


# Generated at 2022-06-13 05:27:35.362505
# Unit test for function main
def test_main():

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

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]
   

# Generated at 2022-06-13 05:27:36.159504
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:27:46.980108
# Unit test for function main
def test_main():
    global module
    import tempfile
    tmp_f = tempfile.NamedTemporaryFile()
    tmp_f.write(b'root:x:0:0:root:/root:/bin/bash')
    tmp_f.seek(0)
    try:
        module = AnsibleModule(argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                split=dict(type='str'),
                fail_key=dict(type='bool', default=True)
            ))
        module.run_command = lambda args: (0, tmp_f.read(), '')
        module.get_bin_path = lambda args: '/usr/bin/getent'
        main()
    finally:
        tmp_f.close()

# Generated at 2022-06-13 05:27:52.203889
# Unit test for function main
def test_main():
    test_dict = {
        'database': 'passwd',
        'key': 'root'
    }
    rc, out, err = main(test_dict)

    assert rc == 0
    assert out == 'root:x:0:0:root:/root:/bin/bash\n'

# Generated at 2022-06-13 05:28:03.126603
# Unit test for function main
def test_main():
    import sys
    import os

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../lib/'))

    class MockModule(object):
        pass

    m = MockModule()
    m.params = {
        'database': 'passwd',
        'key': 'root',
        'service': None,
        'split': ':',
        'fail_key': True,
    }

    def mock_fail_json(*args, **kwargs):
        raise Exception("fail_json called")

    def mock_get_bin_path(*args, **kwargs):
        return "/usr/bin/getent"

    def mock_run_command(*args, **kwargs):
        return 0, "root:x:0:0:root:/root:/bin/bash",

# Generated at 2022-06-13 05:28:10.840889
# Unit test for function main
def test_main():
    """Ansible getent module test suite
    """
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    class AnsibleModuleMock(object):
        def __init__(self):
            self.resource_path = ["/usr/bin/getent"]

        def get_bin_path(self, arg, required):
            return self.resource_path

    module.get_bin_path = AnsibleModuleMock.get_bin_path
    database = "passwd"
    key = "Alan"
   

# Generated at 2022-06-13 05:29:33.521503
# Unit test for function main
def test_main():
    import tempfile
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_file.write("""
    usr1:x:1000:a,b,,
    usr2:x:1001:c,d,,
    usr3:x:1002:e,f
    """)
    tmp_file.close()

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
            path=dict(type='str'),
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 05:29:44.933009
# Unit test for function main
def test_main():
    import sys
    import json
    import pytest
    from .mock_module_helper import mock_module, MockModule
    from .mock_run_command import mock_run_command, MockCommand

    cmd_out = '''root:x:0:0:root:/root:/bin/bash'''
    cmd_rc = 0
    cmd_err = ''
    mock_run_command.return_value = (cmd_rc, cmd_out, cmd_err)

    def exit_json(*args, **kwargs):
        assert args[0]['ansible_facts']['getent_passwd']['root'][0] == 'x'
        assert args[0]['ansible_facts']['getent_passwd']['root'][1] == '0'

# Generated at 2022-06-13 05:29:55.697693
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(argument_spec={
        'database' : {'required': True},
        'key' : {'required': False},
        'service' : {'required': False},
        'split' : {'required' : False},
        'fail_key' : {'required' : True},
    },
    supports_check_mode=True
    )

    setattr(module, 'run_command', test_run_command)

    module.params = {'database': 'passwd', 'key' : '', 'service': '', 'split':':', 'fail_key':True}
    main()

# Generated at 2022-06-13 05:30:09.075311
# Unit test for function main
def test_main():
    # patch the module
    module = AnsibleModule(
        argument_spec=dict(
            key=dict(type='str'),
            database=dict(type='str', required=True),
            split=dict(type='str'),
            fail_key=dict(type='bool'),
        ),
        supports_check_mode=True,
    )
    setattr(module, 'run_command', run_command_mock)

    # testing with key and no split
    module.params['key'] = 'baz'
    module.params['database'] = 'foo'
    main()
    assert module.exit_json.call_count == 1
    assert 'baz' in module.exit_json.call_args[0][0]['ansible_facts']['getent_foo']
    assert module.exit_json.call

# Generated at 2022-06-13 05:30:13.567225
# Unit test for function main
def test_main():
    import os

    os.environ['GETENT'] = '/bin/false'
    if main():
        os.exit(1)

    os.environ['GETENT'] = '/bin/true'
    if main():
        os.exit(1)

# Generated at 2022-06-13 05:30:23.595464
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    import os
    main_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'modules', 'system', 'getent.py')
    module = basic.AnsibleModule(
        argspec=basic.AnsibleModule(argument_spec=dict()).argument_spec,
        supports_check_mode=True
    )
    module.exit_json = lambda args: args
    module.run_command = lambda cmd, fail_on_error: (0, 'localhost\t127.0.0.1\tlocalhost\n', '')
    module.fail_json = lambda args: exit(1)
    module.get_bin_path = lambda cmd, required: True

# Generated at 2022-06-13 05:30:24.292342
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:30:36.470152
# Unit test for function main
def test_main():

    # Mock module and its methods to prevent calls to external code
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

        def get_bin_path(self, name, required):
            return name

        def get_bin_path(self, name, required):
            return name

        def run_command(self, cmd):
            return 0, "", ""
        def fail_json(self, msg, **kwargs):
            assert False, msg
            exit(1)

        def exit_json(self, **kwargs):
            exit(0)

    # Assert if function tries to exit
    def mock_exit(x):
        if x != 0:
            raise Exception("Unexpected non-zero exit!")
    exit = mock_exit

    # Ass

# Generated at 2022-06-13 05:30:46.504653
# Unit test for function main
def test_main():

    import sys
    import os
    import stat

    # Mock the module arguments and return values
    class Options(object):
        def __init__(self):
            self.database = 'hosts'
            self.key = None
            self.split = None
            self.fail_key = True

    def AnsibleModuleStub(*args, **kwargs):
        module = AnsibleModuleStub.AnsibleModuleStubClass(*args, **kwargs)
        module.params = Options()
        module.fail_json = AnsibleModuleStub.fail_json
        module.exit_json = AnsibleModuleStub.exit_json
        return module


# Generated at 2022-06-13 05:30:56.730973
# Unit test for function main
def test_main():

    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils.common.run_command import Command

    module = basic.AnsibleModule(supports_check_mode=True, argument_spec={})
    module.get_bin_path = lambda *args, **kwargs: return_code, stdout, stderr
    module.run_command = Command()
    module.exit_json = lambda *args, **kwargs: exit('exit_json', *args, **kwargs)
    module.fail_json = lambda *args, **kwargs: exit('fail_json', *args, **kwargs)

    mock_func = Mocker()
    mock_func.mock()

    # No args, fail
    main()