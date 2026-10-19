

# Generated at 2022-06-13 05:23:51.506921
# Unit test for function main
def test_main():
    # import python libraries
    import os
    import sys
    # append module
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    # import module
    from module_utils.basic import AnsibleModule
    from module_utils._text import to_native
    # set module args
    set_module_args(
        dict(
            database='passwd',
            key='root',
            service=None,
            split=None,
            fail_key=True,
        )
    )
    # execute main function
    main()


# Generated at 2022-06-13 05:24:00.502922
# Unit test for function main
def test_main():
    # Setup test data and mock module
    module_args = {'database': 'passwd', 'service': None, 'fail_key': True, 'key': 'root', 'split': None}
    mocked_module = MagicMock()
    mocked_module.params = module_args

# Generated at 2022-06-13 05:24:07.831283
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
    module.exit_json(msg='Not implemented')


# Make sure test_main() is ran when importing module
from ansible.module_utils.basic import *
main()

# Generated at 2022-06-13 05:24:08.498895
# Unit test for function main
def test_main():
    assert main


# Generated at 2022-06-13 05:24:09.001535
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:20.886685
# Unit test for function main
def test_main():
    test_module = AnsibleModule({
        'database': 'passwd',
        'key': 'root',
        'split': ':',
    })
    # No error when called with all good params
    res = main()
    assert not res['failed']
    # No error when missing key is not requested to be fatal
    test_module = AnsibleModule({
        'database': 'passwd',
        'key': 'roota',
        'split': ':',
        'fail_key': False,
    })
    res = main()
    assert not res['failed']
    # No error when missing key is requested to be fatal but there is a value

# Generated at 2022-06-13 05:24:26.794218
# Unit test for function main
def test_main():
    args = dict(
      database="passwd",
      key="root",
    )
    rc, out, err = main(args)
    assert rc == dict(
      ansible_facts=dict(
	getent_passwd=dict(
	  root=[0, 0, 0, 0]
	),
      )), "Did not return valid facts!"

# Generated at 2022-06-13 05:24:35.501158
# Unit test for function main
def test_main():
    import pytest

    getent_bin = '/usr/bin/getent'
    database = 'passwd'
    key = 'root'
    split = ':'
    service = None
    fail_key = True

    # Exists
    def run_command(cmd):
        return 0, ['root:x:0:0:root:/root:/bin/bash'], ''

    # Not exists
    def run_command_not_exists(cmd):
        return 2, [''], ''

    # No split
    def run_command_no_split(cmd):
        return 0, ['root x 0 0 root /root /bin/bash'], ''

    # Enum no support
    def run_command_enum_no_support(cmd):
        return 3, [''], ''


# Generated at 2022-06-13 05:24:45.582946
# Unit test for function main
def test_main():
    import os
    import sys
    import tempfile

    try:
        from ansible.module_utils.basic import AnsibleModule

        HAS_IMPORTS = True
    except ImportError:
        HAS_IMPORTS = False

    fields = {
        'database': 'passwd',
        'key': 'root',
        'split': ':',
        'fail_key': True,
    }

    if not HAS_IMPORTS:
        pytest.skip('ansible required for testing', allow_module_level=True)

    dummy_data = ['root:x:0:0:root:/root:/bin/bash']

    with tempfile.NamedTemporaryFile() as unixpasswd, tempfile.NamedTemporaryFile() as unixpasswd_shadow:
        passwd_path = unixpasswd.name

# Generated at 2022-06-13 05:24:53.910221
# Unit test for function main
def test_main():
    """
    Test for function main
    """
    dummy_dict = dict()
    dummy_dict['_ansible_verbosity'] = 3
    dummy_dict['_ansible_check_mode'] = False
    dummy_dict['_ansible_no_log'] = False
    dummy_dict['database'] = 'passwd'
    dummy_dict['key'] = 'root'
    dummy_dict['_ansible_debug'] = False
    dummy_dict['_ansible_diff'] = False
    dummy_dict['ansible_version'] = dict()
    dummy_dict['ansible_version']['full'] = '2.9.0'
    dummy_dict['ansible_version']['major'] = 2
    dummy_dict['ansible_version']['minor'] = 9

# Generated at 2022-06-13 05:25:14.561225
# Unit test for function main
def test_main():
    args = dict(
        database='group',
        key='root',
    )
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            service=dict(type='str'),
            split=dict(type='str'),
        ),
        supports_check_mode=False,
    )
    results = main(module, args)
    module.exit_json(**results)

# Generated at 2022-06-13 05:25:23.274805
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

    module.params = dict(
        database='hosts',
        key='10.0.0.1',
        split="\t",
    )

    import sys
    import contextlib

    stdout = sys.stdout
    stdin = sys.stdin
    stderr = sys.stderr

    class SplitStdout(object):
        def __init__(self):
            self.buf = ""



# Generated at 2022-06-13 05:25:33.977190
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest

    # set the environment so we can find getent binary
    os.environ['PATH'] = os.pathsep.join([os.path.dirname(__file__), '../../../../bin:/usr/bin', os.environ['PATH']])
    print("PATH: %s" % os.environ['PATH'])

    my_argv = [pytest.__file__, __file__]

    #
    # create a mock module and add necessary arguments
    #
    class MyModule(object):
        def __init__(self):
            self.params = {
                'database': 'passwd',
                'key': 'root',
                'fail_key': True,
                'split': None,
                'service': None,
            }

    # mock

# Generated at 2022-06-13 05:25:38.641356
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
    test_module.exit_json = exit_json
    test_module.fail_json = fail_json
    test_module.params = {
        'database': 'aliases',
        'key': 'foo',
    }
    main()

# Generated at 2022-06-13 05:25:42.438081
# Unit test for function main
def test_main():
    import sys
    import tempfile
    import subprocess

    print("Running getent unit tests:")
    for database in ["group", "hosts", "passwd", "protocols", "services"]:
        test_file = tempfile.mkstemp()[1]
        test_cmd = [sys.executable, __file__, "--database=%s" % database]
        print(test_cmd)
        subprocess.run(test_cmd, stdout=open(test_file, 'w'))
        with open(test_file, 'r') as fp:
            print(fp.read())
        print("")

# Generated at 2022-06-13 05:25:51.579686
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
   

# Generated at 2022-06-13 05:26:03.389457
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

   

# Generated at 2022-06-13 05:26:17.839688
# Unit test for function main

# Generated at 2022-06-13 05:26:26.765547
# Unit test for function main
def test_main():
    import shlex
    import subprocess
    import json
    import sys
    import os
    import getent
    import re
    import platform

    # existance of getent command
    cmd_args = shlex.split("getent --help")
    cmd = subprocess.Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = cmd.communicate()
    assert cmd.returncode == 0

    # calling main function
    db = "passwd"
    key = "root"
    split = ":"
    json_str = ""
    t_platform = platform.system()
    if t_platform == 'Darwin' or t_platform == 'FreeBSD':
        # has to remove the colon in the dict
        json

# Generated at 2022-06-13 05:26:33.329952
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
        supports_check_mode=True,
    )

    global getent_bin
    def getent_bin(*args, **kwargs):
        if args[0] == 'getent':
            return 'getent'
        else:
            return '/bin/false'

    module.get_bin_path = getent_bin
    module.run_command = magic_run_command

    from ansible.modules.system import getent
    getent.main()

# Generated at 2022-06-13 05:27:05.570023
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
    passed = {}
    passed['getent_passwd'] = {
        'root': ['x', '0', '0', 'root', '/root', '/bin/bash'],
        'daemon': ['x', '1', '1', 'daemon', '/usr/sbin', '/bin/sh'],
    }

    failed = {}

# Generated at 2022-06-13 05:27:15.104873
# Unit test for function main
def test_main():
    args = dict(
        database='passwd',
        key='root',
    )
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.params = args
    rc, out, err = main()
    assert rc == 0
    assert out['ansible_facts']['getent_passwd']['root'] == 'x:0:0:root:/root:/bin/bash'

# Generated at 2022-06-13 05:27:15.764238
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:27:27.079538
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.basic import AnsibleModule

    main = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Mock the main function
    main.run_command = lambda cmd: (0, "test_out", "test_err")

    # Mock the AnsibleModule.exit_json

# Generated at 2022-06-13 05:27:41.088095
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

  cmd = ['getent','passwd','root']
  module.run_command(cmd)
  x = module.exit_json.return_value
  x = x.replace('u\'','\'')
  x = x.replace('\'','\"')
  x = x.replace('False','false')
  x = x.replace('True','true')

# Generated at 2022-06-13 05:27:46.131154
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
        supports_check_mode=True,
    )

    module.params['database'] = 'group'

    rc, out, err = main(module)
    print(out)

# Generated at 2022-06-13 05:27:47.766065
# Unit test for function main
def test_main():

    pass

# Generated at 2022-06-13 05:28:00.568747
# Unit test for function main
def test_main():
    os.environ['PATH'] = os.pathsep.join(['.', os.environ['PATH']])
    os.environ['ANSIBLE_GETENT_BIN'] = './test-data/getent'

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')

    getent_bin

# Generated at 2022-06-13 05:28:02.231172
# Unit test for function main
def test_main():
    import os
    os.system("touch /tmp/test_main")


# Generated at 2022-06-13 05:28:03.668470
# Unit test for function main
def test_main():
    import doctest
    print(doctest.testmod())

# Generated at 2022-06-13 05:29:12.834231
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
    assert main() == '{"changed": false, "failed": false}'

# Generated at 2022-06-13 05:29:19.227405
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os

    def execute_module(module, fail_key):
        print("TESTING: %s %s" % (module.params['database'], module.params['key']))
        results = {}
        results['ansible_facts'] = {}
        if fail_key:
            results['ansible_facts']['getent_%s' % module.params['database']] = {}
        else:
            results['ansible_facts']['getent_%s' % module.params['database']][module.params['key']] = None

        module.exit_json(**results)

    module = AnsibleModule({
        "key": "foo",
        "database": "passwd",
        "fail_key": True
    })


# Generated at 2022-06-13 05:29:23.005996
# Unit test for function main
def test_main():
    module_args = dict(
        database='passwd',
        key='root',
    )
    result = main(module_args)
    assert result['failed'] is False

# Generated at 2022-06-13 05:29:34.991561
# Unit test for function main
def test_main():
    # Mock module and function arguments
    class Args:
        database = "passwd"
        key = "root"
        service = None
        split = None
        fail_key = True
    args = Args()

    # create an instance of the AnsibleModule class (helper class to create ansible modules)
    module = AnsibleModule(argument_spec={})
    module.params = {'database': args.database, 'key': args.key, 'service': args.service, 'split': args.split, 'fail_key': args.fail_key}

    # Mock the run_command function
    mock_run_command_result = 0, ["root:x:0:0:root:/root:/bin/bash"], ""
    def mock_run_command(cmd):
        return mock_run_command_result

    module.run_

# Generated at 2022-06-13 05:29:45.251149
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

   

# Generated at 2022-06-13 05:29:55.866453
# Unit test for function main
def test_main():
    # Test for all the cases for main()
    # test case to test all the conditions for fail if
    def test_main_fail(arg1, arg2, arg3, arg4, arg5):
        with pytest.raises(SystemExit):
            main(arg1, arg2, arg3, arg4, arg5)

    # test case to test all the conditions for exit json
    def test_main_exit_json(arg1, arg2, arg3, arg4, arg5):
        with pytest.raises(SystemExit):
            main(arg1, arg2, arg3, arg4, arg5)

    import os
    import stat
    import tempfile
    import shutil
    import subprocess
    import pytest

    # os.chmod(getent_bin, stat.S_IRWXU)


# Generated at 2022-06-13 05:30:08.355705
# Unit test for function main
def test_main():
    # mock module class
    class Module:
        def __init__(self):
            self.params = dict(
                database='passwd',
                split=None,
            )
            self.run_command = lambda x: (0, "root:x:0:0:root:/root:/bin/bash\nuser1:x:500:500:user1:/home/user1:/bin/bash", '')

        def fail_json(self, **kwargs):
            raise Exception('fail_json')

        class ParseError(Exception):
            pass

    # exercise code
    try:
        main()
    except Exception as e:
        # there are no failures expected
        assert False, "Unexpected exception: %s" % e.args[0]

# Generated at 2022-06-13 05:30:20.786473
# Unit test for function main
def test_main():
    import os
    import unittest
    from subprocess import call
    from mock import patch, Mock

    RUNNER_PATH = os.path.join(os.path.dirname(__file__), 'runner.py')

    def _run_module(additional_args={}):
        with patch.object(os.path, 'expanduser', return_value=os.path.expanduser.__wrapped__('~')):
            with patch('sys.argv', ['runner.py', '0', '0']):
                with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
                    with patch('ansible.module_utils._text.to_native') as mock_native:
                        mock = Mock()
                        mock.module = mock_module
                        mock.module.params = additional_args

# Generated at 2022-06-13 05:30:31.088727
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

   

# Generated at 2022-06-13 05:30:44.129549
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={'database': {'type': 'str', 'required': True},
                       'key': {'type': 'str', 'no_log': False},
                       'split': {'type': 'str'},
                       'fail_key': {'type': 'bool', 'default': True}}
    )

    getent_bin = module.get_bin_path('getent', True)
    database = 'passwd'
    key = 'root'

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]

    rc, out, err = module.run_command(cmd)
    assert rc == 0
    assert 'root:x:0:0:root:/root:/bin/bash' in out

# Generated at 2022-06-13 05:33:24.833996
# Unit test for function main
def test_main():
    import json
    import getent
    import tempfile
    import shutil

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    def fake_run_command(module, cmd):
        # return values for getent based on our fake data
        rc = 0
        err = ''
        out = ''

        if 'services' in cmd:
            if 'http' in cmd:
                out = 'http\t80/tcp\nhttp\t443/tcp\n'
            elif 'https' in cmd:
                rc = 2
        elif 'passwd' in cmd:
            if 'root' in cmd:
                out = 'root:x:0:0:root:/root:/bin/bash\n'

        return (rc, out, err)