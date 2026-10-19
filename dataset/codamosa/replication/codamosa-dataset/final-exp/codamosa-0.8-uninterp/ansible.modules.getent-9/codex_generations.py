

# Generated at 2022-06-13 05:23:54.836259
# Unit test for function main
def test_main():

    # NOTE: This is a test that is used for unittest. This is not an example of how to use the module or is it idempotent. If a test is not idempotent you should use the check_mode=yes option.
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

# Generated at 2022-06-13 05:23:55.353630
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:23:57.288441
# Unit test for function main
def test_main():
    test_argv = ['getent', 'foo', 'service']
    with patch.object(sys, 'argv', test_argv):
        main()

# Generated at 2022-06-13 05:24:04.794650
# Unit test for function main
def test_main():
    class options(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)
    obj = AnsibleModule(argument_spec={})
    args = (
        options(
            database='passwd',
            key=None,
            split=':',
            fail_key=True,
        ),
    )
    rc = None
    out = 'root:x:0:0:root:/root:/bin/zsh\n'
    err = ''


# Generated at 2022-06-13 05:24:10.421832
# Unit test for function main
def test_main():
    import os
    import sys
    import unittest
    old_getent_path = os.environ.get('PATH')
    sc = os.path.dirname(os.path.realpath(__file__))
    os.environ['PATH'] = '%s:%s' % (sc, old_getent_path)

    class TestMain(unittest.TestCase):
        def test_1(self):
            sys.modules['__main__'].main()
    unittest.main()

# Generated at 2022-06-13 05:24:11.146635
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:15.381905
# Unit test for function main
def test_main():
    argv = [
        'database=passwd',
        'key=root',
        'src=/home/username/.ansible',
    ]
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    module.exit_json(ansible_facts={})

# Generated at 2022-06-13 05:24:21.433621
# Unit test for function main
def test_main():
    ansible_module = AnsibleModule({
        "database": "passwd",
        "key": "root",
        "split": ":"
    })
    # this is needed for the module fixture to work
    ansible_module.exit_json = exit_json
    ansible_module.fail_json = fail_json
    try:
        main()
    except Exception as e:
        print("An error occured: %s" % repr(e))


# Generated at 2022-06-13 05:24:32.498533
# Unit test for function main
def test_main():

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    import tempfile, shutil, os


# Generated at 2022-06-13 05:24:41.341449
# Unit test for function main
def test_main():
    import os
    import sys
    import pytest

    # we don't have getent on windows
    if sys.platform.startswith('win'):
        pytest.skip("getent is not available on windows")

    # if root, passwd is a safe test
    os.environ['GETENT_TEST_KEY'] = 'root'
    os.environ['GETENT_TEST_DATABASE'] = 'passwd'
    os.environ['GETENT_TEST_SPLIT'] = ':'

    # test run
    from ansible.modules.system.getent import main
    main()

# Generated at 2022-06-13 05:25:01.217487
# Unit test for function main
def test_main():
    """
    main function unit test function
    """

    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.system.getent import main

    module_args = dict(
        database='passwd'
    )

    obj = Facts(
        module_args=module_args,
        #module_path='/var/lib/jenkins/workspace/ansible/ansible/module_utils/facts/system/getent.py'
    )

    try:

        #import pdb;pdb.set_trace()

        main()

    except Exception as e:
        print(e)




# Generated at 2022-06-13 05:25:08.886984
# Unit test for function main
def test_main():
    import tempfile
    results={'getent_hosts': {}}
    results['getent_hosts']['localhost'] = ['127.0.0.1']
    results['getent_hosts']['localhost.localdomain'] = ['127.0.0.1']
    results['getent_hosts']['localhost4'] = ['127.0.0.1']
    results['getent_hosts']['localhost4.localdomain4'] = ['127.0.0.1']
    results['getent_hosts']['localhost6'] = ['::1']
    results['getent_hosts']['localhost6.localdomain6'] = ['::1']
    results['getent_hosts']['ip6-localhost'] = ['::1']

# Generated at 2022-06-13 05:25:19.889624
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    # Set up parameters
    argument_spec = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    )
    module = basic.AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    module.params['database'] = 'passwd'
    module.params['key'] = 'bcoca'

    getent_bin = module.get_bin_path('getent', True)
    cmd = [getent_bin, module.params['database'], module.params['key']]
    rc, out, err = module.run_command(cmd)


# Generated at 2022-06-13 05:25:31.710643
# Unit test for function main
def test_main():
    # This is how you would normally import
    from ansible.modules.system.getent import main as getent

    # set up needed objects
    class _module(object):
        def __init__(self):
            self.module = None
            self.params = None

    class _params(object):
        def __init__(self):
            self.database = None
            self.key = None

    class _config(object):
        def __init__(self):
            self.module_name = None

    # create needed objects
    module = _module()
    module.params = _params()
    module.params.database = "passwd"
    module.params.key = "root"
    module.config = _config()
    module.config.module_name = 'getent'



# Generated at 2022-06-13 05:25:37.203450
# Unit test for function main
def test_main():
    def getent(module, cmd):
        return 0, ':'.join(cmd), ''
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(required=True, type='str'),
            key=dict(type='str'),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(default=True, type='bool'),
        ),
        supports_check_mode=True,
    )
    module.get_bin_path = lambda *x: '/bin/getent'
    module.run_command = getent
    main()

# Generated at 2022-06-13 05:25:47.604518
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_iterable
    from units.modules.utils import set_module_args, exit_json, fail_json, AnsibleExitJson
    import pytest
    import os

    def test_rc(rc, stdout, stderr):
        assert rc == 0
        assert stdout == ""
        assert stderr == ""

    def test_rc_fail(rc, stdout, stderr):
        assert rc == 1
        assert stdout == ""
        assert stderr == ""

    def test_run_command(stdout):
        module.run_command.side_effect = [ (0, stdout, "") ]


# Generated at 2022-06-13 05:26:01.319869
# Unit test for function main

# Generated at 2022-06-13 05:26:07.589714
# Unit test for function main
def test_main():
    args = dict(
        database='passwd',
        key='root'
    )
    out = dict(
        ansible_facts={
            'getent_passwd': {
                'root': ['x', '0', '0', 'root', '/root', '/bin/bash']
            }
        }
    )
    module = AnsibleModule(argument_spec=args)
    main()

# Generated at 2022-06-13 05:26:09.855766
# Unit test for function main

# Generated at 2022-06-13 05:26:21.473988
# Unit test for function main
def test_main():
    # Test with valid arguments
    module = AnsibleModule(argument_spec=dict(database=dict(type='str', required=True),
                                              key=dict(type='str', no_log=False),
                                              service=dict(type='str'),
                                              split=dict(type='str'),
                                              fail_key=dict(type='bool', default=True),),
                           supports_check_mode=True, )
    module.params = {
        'database': 'passwd',
        'key': 'root'
    }

    setattr(module, 'get_bin_path', lambda x, y: '/usr/bin/getent')
    m_run_command = MagicMock(return_value=(0, 'root:x:0:0:root:/root:/bin/bash', ''))
    set

# Generated at 2022-06-13 05:26:54.093145
# Unit test for function main
def test_main():
    # Replaces module_utils/facts.py with a mock
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

    def mock_get_bin_path(args, required=False):
        return 'getent'

    m.get_bin_path = mock_get_bin_path

    def mock_run_command(args):
        return (0, "root:x:0:0::/root:/bin/bash", "")

    m.run_command = mock_run

# Generated at 2022-06-13 05:27:03.870217
# Unit test for function main
def test_main():
    '''
    unit test function main
    '''

    # Mock the run_command function
    def mock_run_command(cmd):
        '''
        Mock the run_command function
        '''

        # getent passwd

# Generated at 2022-06-13 05:27:14.149680
# Unit test for function main
def test_main():
    import sys
    import json
    import tempfile

    # Create a temp file with a single line
    (fd, fn) = tempfile.mkstemp()
    with open(fn, "w") as f:
        f.write("Dummy entry\n")

    # Override module_utils/basic.py AnsibleModule to control args
    class FakeAnsibleModule():
        def __init__(self, **kwargs):
            self.params = kwargs

        # Fake run_command, just return fake status and output
        def run_command(self, cmd, check_rc=True):
            if self.params['key'] == 'bash' and self.params['database'] == 'passwd':
                return (2, "", "")
            else:
                return (0, fn, "")


# Generated at 2022-06-13 05:27:17.059850
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as exc:
        main()
    assert not exc.value.args[0]['changed']

# Generated at 2022-06-13 05:27:27.578324
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
    module.run_command = Mock(return_value=(0, b"root:x:0:0:root:/root:/bin/bash", ""))
    main()
    assert module.exit_json.called

# Generated at 2022-06-13 05:27:41.574139
# Unit test for function main
def test_main():
  import sys
  import os
  import shutil
  import tempfile
  import ansible.module_utils.basic
  from ansible.compat.tests import unittest
  from ansible.compat.tests.mock import MagicMock, patch, mock_open

  # Mock ansible.module_utils.basic.AnsibleModule
  def patched_AnsibleModule(argument_spec, supports_check_mode=False):
    return MagicMock(spec=ansible.module_utils.basic.AnsibleModule, name="MockedAnsibleModule")

  # Mock ansible.module_utils.basic.AnsibleModule.run_command

# Generated at 2022-06-13 05:27:48.392811
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    import json

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

    # Mock the run_command for testing
    mock = basic.AnsibleModule.run_command = lambda self, cmd: (0, "root:x:0:0:root:/root:/bin/bash\n", "")
    main

# Generated at 2022-06-13 05:27:59.025603
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os
    main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_dir = os.path.join(main_dir, 'unit/modules/action/getent_test/')
    os.chdir(test_dir)
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


# Generated at 2022-06-13 05:28:00.845303
# Unit test for function main
def test_main():
    # TODO: Add unit tests
    pass

# Generated at 2022-06-13 05:28:07.399695
# Unit test for function main
def test_main():
    test_module = AnsibleModule({
        'database': 'passwd',
        'key': 'root',
        'fail_key': 'yes',
    })
    test_module.run_command = run_command
    test_module.run_command.side_effect = [
        (0, 'root:x:0:0:root:/root:/bin/bash', ''),
    ]
    test_main = test_function(main)
    test_main(test_module)
    assert test_module.exit_json.called


# Generated at 2022-06-13 05:29:21.060123
# Unit test for function main
def test_main():
    import sys
    import inspect
    import os
    import subprocess

    # get a reference to the main function
    main_fct = inspect.getmembers(sys.modules[__name__], inspect.isfunction)[0][1]

    # get a reference to the main function
    current_test = inspect.stack()[0][3]

    # find the directory of the current test
    test_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    # build the test command -> 'ansible -m test.py test_main'
    test_cmd = 'ansible -m %s %s' % (os.path.join(test_dir, __file__), current_test)

    # get the expected output
    expected_output = subprocess.check_output

# Generated at 2022-06-13 05:29:33.985165
# Unit test for function main
def test_main():
    from ansible.modules.system.getent import main
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Mock the external module
    # Specs are written so these should never be called
    module.run_command = basic.AnsibleModule.run_command

    # Set up the test
    database = "test_database"
    key = "test_key"
    split = None


# Generated at 2022-06-13 05:29:35.542280
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:29:47.164571
# Unit test for function main
def test_main():
    # Fix pytest testing when not a package
    module = AnsibleModule({'database': 'passwd'}, supports_check_mode=True)

    class AnsibleModuleFake:
        def __init__(self, argument_spec, **kwargs):
            return AnsibleModule(argument_spec=argument_spec, **kwargs)

        def exit_json(self, **kwargs):
            return
    setattr(AnsibleModuleFake, 'run_command', main.__globals__['run_command'])
    setattr(AnsibleModuleFake, 'get_bin_path', main.__globals__['get_bin_path'])

# Generated at 2022-06-13 05:29:53.683420
# Unit test for function main
def test_main():
    argument_spec = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    )
    module = AnsibleModule(
        argument_spec
    )
    main()
    #getent_main(self, module)

# Generated at 2022-06-13 05:29:54.163785
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:29:54.619944
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:29:59.138851
# Unit test for function main
def test_main():
    module_args = {
        "database": "passwd",
        "fail_key": False,
        "key": "root",
        "service": "",
        "split": None
    }

    result = module.main(module_args)

# Generated at 2022-06-13 05:30:10.435739
# Unit test for function main
def test_main():
    import sys

    # This is hacky, but it will do for now
    sys.modules['ansible'] = type('FakeAnsible', (), {})

    def get_bin_path_mock(p, required=False):
        if p == 'getent':
            return '/usr/bin/getent'
        else:
            return None

    def run_command_mock(cmd):
        if cmd[1] == 'passwd':
            return (0, 'root:x:0:0:root:/root:/bin/bash', '')
        elif cmd[1] == 'group' and cmd[2] == 'root':
            return (0, 'root:x:0:', '')

# Generated at 2022-06-13 05:30:21.677397
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

   

# Generated at 2022-06-13 05:32:48.545373
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action

    m = action.ActionModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    m._announce_deprecations()
    m._set_locale()
    m._load_params()
    m.params['database'] = 'group'
    m.params['key'] = 'root'
    m._execute_module()

# Generated at 2022-06-13 05:32:57.619716
# Unit test for function main
def test_main():
    mock_module = MagicMock()
    mock_module.params = {'database': 'passwd'}

    mock_module.get_bin_path.return_value = 'getent'
    mock_module.run_command.return_value = 0, 'root:x:0:0:root:/root:/bin/bash', None

    getent_facts = main(mock_module)

    assert getent_facts['ansible_facts']['getent_passwd']['root'] == ['x', '0', '0', 'root', '/root', '/bin/bash']



# Generated at 2022-06-13 05:33:03.579131
# Unit test for function main
def test_main():
    # Test no database provided
    module = AnsibleModule(
        argument_spec={'database': {'required': True, 'type': 'str'}}
    )
    module.run_command = mock.Mock(return_value=(3, 'Module output', 'Module error'))
    try:
        main()
    except SystemExit as e:
        assert e.code == 0
    else:
        pytest.fail('An exception should be raised')
    assert module.fail_json.call_count == 1
    assert module.fail_json.call_args[0][0]['msg'] == 'Enumeration not supported on this database.'
    assert module.fail_json.call_args[0][0]['rc'] == 3

    # Test database provided but missing arguments

# Generated at 2022-06-13 05:33:15.403774
# Unit test for function main
def test_main():
    """
    Unit test for function main
    :return:
    """
    import json
    import sys
    import getent
    class TestModule(object):
        def __init__(self, params):
            self.params = params
        def exit_json(self, **kwargs):
            print (json.dumps(kwargs, indent=4))
        def fail_json(self, **kwargs):
            print (kwargs)
            exit(1)
        def get_bin_path(self, binary, required=False, opt_dirs=[]):
            return '/bin/getent'


# Generated at 2022-06-13 05:33:23.007980
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

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

    getent_bin = module.get_bin_path