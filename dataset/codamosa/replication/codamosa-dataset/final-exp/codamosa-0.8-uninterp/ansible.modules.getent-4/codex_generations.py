

# Generated at 2022-06-13 05:23:54.273503
# Unit test for function main
def test_main():
    # TEST 1
    # by default, fail_key is enabled
    # In this test, key: root is an existing key

    ans_getent_passwd = {'getent_passwd':
                             {'root':
                                  ['x', '0', '0', 'root', 'root', '/root', '/bin/bash']}
                         }
    ans_rc = 0
    ans_msg = ""

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    from ansible.module_utils.basic import Ans

# Generated at 2022-06-13 05:24:02.600332
# Unit test for function main
def test_main():
    from ansible.module_utils.common.json import json as json_module
    import ansible.module_utils.getent as getent_module
    from ansible.module_utils.basic import AnsibleModule

    def run_command_mock(self, cmd, daemonize=False, environ_update=None, **kwargs):
        return (0, 'test_value', '')

    getent_module.AnsibleModule.run_command = run_command_mock


# Generated at 2022-06-13 05:24:11.445242
# Unit test for function main
def test_main():
    """Tests for the module getent"""
    import inspect
    import json
    import sys
    import os

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, os.path.dirname(parentdir))
    sys.path.append(parentdir)
    import modules.getent


# Generated at 2022-06-13 05:24:12.870532
# Unit test for function main
def test_main():
    # Placeholder for tests in future
    assert True

# Generated at 2022-06-13 05:24:22.531345
# Unit test for function main
def test_main():
    import sys

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        )
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]

    if split is None and database in colon:
        split

# Generated at 2022-06-13 05:24:23.125917
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:24:33.540770
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

    database = 'group'
    key = 'root'
    split = ':'
    service = None
    fail_key = False

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]

# Generated at 2022-06-13 05:24:39.716842
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool'),
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


# Generated at 2022-06-13 05:24:41.331411
# Unit test for function main
def test_main():
    if os.path.exists('/etc/passwd'):
        assert main() is None

# Generated at 2022-06-13 05:24:42.529933
# Unit test for function main
def test_main():

    assert callable(main)

# Generated at 2022-06-13 05:25:02.230774
# Unit test for function main
def test_main():
    '''
    ansible all -i inventory -m getent -a 'database=passwd key=root'
    '''
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

    rc = 0
    out = 'root:x:0:0:root:/root:/bin/bash'
    err = ''
    module.run_command = MagicMock(return_value=(rc, out, err))
    main()

# Generated at 2022-06-13 05:25:09.025780
# Unit test for function main
def test_main():
    #Testing 1:
    #   getent passwd jdoe
    #   Expected result:
    #      jdoe:x:1000:1000:user jdoe:/home/jdoe:/bin/bash
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.params['database'] = 'passwd'
    module.params['key'] = 'jdoe'

    getent_bin = module.get_bin_path('getent', True)

# Generated at 2022-06-13 05:25:15.297547
# Unit test for function main
def test_main():
    inter_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True
    )
    inter_module.exit_json = lambda x: print(x)
    main()

# Generated at 2022-06-13 05:25:23.632570
# Unit test for function main
def test_main():
    module = mock.Mock()

    options = dict(
        database="test",
        key="test",
        service="test",
        split="test",
        fail_key=False
    )

    module.params = options

    getent_bin = module.get_bin_path('getent', True)
    cmd = [getent_bin, "test", "test"]

    # Database argument is none
    options["database"] = None
    module.params = options
    main()

    # Return code is non-zero
    module.run_command.return_value = (1, "", "")
    main()

    # Return code is non-zero

# Generated at 2022-06-13 05:25:34.240814
# Unit test for function main
def test_main():
    import sys
    import os
    from ansible.config.manager import ConfigManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    import pytest
    from units.mock.fs import mock_open_fixture


# Generated at 2022-06-13 05:25:46.210542
# Unit test for function main
def test_main():
    with mock.patch.object(basic.AnsibleModule, "_ansible_version", '2.9.15'):
        with mock.patch.object(basic._AnsibleModule, "run_command") as run_command:
            run_command.return_value = (0, 'root:x:0:0:root:/root:/bin/bash\nbin:x:1:1:bin:/bin:/sbin/nologin\ndaemon:x:2:2:daemon:/sbin:/sbin/nologin', '')

# Generated at 2022-06-13 05:26:00.143133
# Unit test for function main
def test_main():
    result_expected = {
        'ansible_facts': {
            'getent_passwd': {
                'root': ['x', '0', '0', 'root', '/root', '/bin/bash'],
                'bin': ['x', '1', '1', 'bin', '/bin', '/sbin/nologin'],
                'daemon': ['x', '2', '2', 'daemon', '/sbin', '/sbin/nologin']
            }
        }
    }

    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, msg):
            raise AssertionError(msg['msg'])


# Generated at 2022-06-13 05:26:07.184901
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.getent as getent
    module = AnsibleModule(argument_spec = dict(database = dict(required = True, type = 'str'),
                                                key = dict(type = 'str'),
                                                service = dict(type = 'str'),
                                                split = dict(type = 'str', default = ':'),
                                                fail_key = dict(type = 'bool', default = True)))
    getent_bin = getent.main(module)
    cmd = [getent_bin, module.params['database']]
    rc, out, err = module.run_command(cmd)
    msg = "Unexpected failure!"
    dbtree = 'getent_%s' % module.params['database']

# Generated at 2022-06-13 05:26:18.613140
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

    result = main(module)

# Generated at 2022-06-13 05:26:23.206943
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        'database': dict(type='str', required=True),
        'key': dict(type='str', no_log=False),
        'service': dict(type='str'),
        'split': dict(type='str'),
        'fail_key': dict(type='bool', default=True),
    })


# Generated at 2022-06-13 05:26:56.590193
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

   

# Generated at 2022-06-13 05:27:05.752445
# Unit test for function main
def test_main():
    import sys

    # we can not use exit_json or fail_json as they would prevent our assertions
    old_exit_json = sys.modules['ansible.module_utils.basic'].AnsibleModule.exit_json
    old_fail_json = sys.modules['ansible.module_utils.basic'].AnsibleModule.fail_json

    def exit_json(*args, **kwargs):
        old_exit_json(*args, **kwargs)
        assert False

    def fail_json(*args, **kwargs):
        old_fail_json(*args, **kwargs)
        assert False

    sys.modules['ansible.module_utils.basic'].AnsibleModule.fail_json = fail_json
    sys.modules['ansible.module_utils.basic'].AnsibleModule.exit_json = exit

# Generated at 2022-06-13 05:27:06.243774
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:27:17.649224
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import action
    from ansible.module_utils.common.text.converters import to_text

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', default=None),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
        mutually_exclusive=[
            ('key', 'service')
        ]
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')

# Generated at 2022-06-13 05:27:20.606957
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
    )

# Generated at 2022-06-13 05:27:21.431907
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:27:30.582036
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common import json

    mymodule = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    getent_bin = get_bin_path(mymodule, 'getent', True)
    cmd = [getent_bin, 'passwd', 'root']
    rc = 0

# Generated at 2022-06-13 05:27:31.863850
# Unit test for function main
def test_main():
   print("Dummy test_main")


# Generated at 2022-06-13 05:27:44.296921
# Unit test for function main
def test_main():
    key = 'testkey'
    database = 'testdb'
    split = ':'
    service = 'testservice'

    class Args:
        database = database
        key = key
        split = split
        service = service
        fail_key = True

    class Module:
        class Run:
            def __init__(self, cmd, check_mode=False, no_log=False):
                self.cmd = cmd
                self.check_mode = check_mode
                self.no_log = no_log
                self.rc = 0
                self.stdout = 'testout'
                self.stderr = ''

            def __call__(self, *args, **kwargs):
                return (self.rc, self.stdout, self.stderr)


# Generated at 2022-06-13 05:27:44.986808
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:28:48.706051
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import common_koji
    from ansible.module_utils._text import to_bytes
    import os
    import sys

    if sys.version_info[:2] == (2, 6):
        import unittest2 as unittest
    else:
        import unittest

    def set_module_args(args):
        args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
        basic._ANSIBLE_ARGS = to_bytes(args)

    def get_module_args():
        return json.loads(to_bytes(common_koji._ANSIBLE_ARGS))['ANSIBLE_MODULE_ARGS']

    def exit_json(*args, **kwargs):
        raise Exception(kwargs['msg'])

# Generated at 2022-06-13 05:28:57.006463
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

   

# Generated at 2022-06-13 05:29:02.183916
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    class AnsibleRunResults:
        def __init__(self, rc=0, stdout="", stderr=""):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr

    class AnsibleModuleMock:
        def __init__(self, test_module):
            self.params = test_module.params
            self.check_mode = test_module.check_mode
            self.supp

# Generated at 2022-06-13 05:29:08.381870
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
    rc, out, err = module.run_command('exit 0', use_unsafe_shell=False)
    assert rc == 0
    assert out == b''
    assert err == b''

# Generated at 2022-06-13 05:29:10.698414
# Unit test for function main
def test_main():
    cmd = module_args = dict(
        database='passwd',
        key='root',
    )

    rc, out, err = main()
    assert rc == 0
    assert out == results

# Generated at 2022-06-13 05:29:17.681776
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    from . import getent

    sys.path.append('/var/lib/awx')
    from awx.main.utils import memoize

    getent_run_command = memoize(getent.run_command_with_module)

    @pytest.fixture
    def getent_module_mock(monkeypatch):
        module = AnsibleModule(
            argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                service=dict(type='str'),
                split=dict(type='str'),
                fail_key=dict(type='bool', default=True),
            ),
            supports_check_mode=True
        )
        module_mock = MagicMock

# Generated at 2022-06-13 05:29:30.939173
# Unit test for function main
def test_main():

    # Test for missing required=True parameter
    # Was causing an error to be returned, not in documentation
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str'),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    assert module.fail_json.called is True
    assert 'missing required arguments' in str(module.fail_json.call_args)

    # Test default fail_key, fail_key=True

# Generated at 2022-06-13 05:29:34.486242
# Unit test for function main
def test_main():
    test_cases = [
        (
            dict(
                database='passwd',
                key='root',
            ),
            dict(
                changed=False,
                ansible_facts={'getent_passwd': {'root': ['x', 0, 0, 'root', '/root', '/bin/bash']}}
            ),
        ),
    ]

    for args, expected_results in test_cases:
        m = AnsibleModule(argument_spec=args)
        main()
        assert m.exit_json.call_args == call(**expected_results)

# Generated at 2022-06-13 05:29:48.138066
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:29:52.573624
# Unit test for function main
def test_main():
    import shlex
    import os
    import tempfile
    from ansible.module_utils import basic

    # Fake system collection
    # Change this when you write your own test

# Generated at 2022-06-13 05:32:00.036516
# Unit test for function main
def test_main():
    import sys

    # Mock arguments
    sys.argv = [
        '',
        'database=passwd', 'key=root',
    ]

    # Mock AnsibleModule
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}
            self.check_mode = False
            self.exit_json = lambda data: sys.exit(0)
            self.fail_json = lambda data: sys.exit(1)

        def run_command(self, cmd):
            # Simulate a failed getent
            return 4, '', 'Unexpected failure!'

    am = MockAnsibleModule()
    assert main() == am.fail_json(msg='Unexpected failure!')

    # Simulate a successful getent

# Generated at 2022-06-13 05:32:00.586392
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:32:07.479359
# Unit test for function main
def test_main():
    mock_module = MockModule()

    # setup
    mock_module.params = dict(
        database='passwd',
        key='ansible',
        split=':')

    mock_bin = MagicMock()
    mock_bin.return_value = 'test_bin'

    mock_run = MagicMock()
    mock_run.return_value = (0, 'ansible:x:2463:300::/home/ansible:/bin/bash\n', 'err')

    mock_module.get_bin_path = mock_bin
    mock_module.run_command = mock_run

    # execute
    main()

    # assert
    mock_bin.assert_called_once_with('getent', True)

# Generated at 2022-06-13 05:32:19.771673
# Unit test for function main
def test_main():
    from ansible.utils.pycompat import NestedDict

    cmd_out = '''
hosts:1:2:3:4:5:6:7
hosts:a:b:c:d:e:f:g
passwd:a:b:c:d:e:f
passwd:1:2:3:4:5:6
shadow:a:b:c:d:e:f
shadow:1:2:3:4:5:6
group:a:b:c:d
group:1:2:3:4
    '''

    cmd_rc = 0


# Generated at 2022-06-13 05:32:20.425087
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:32:31.045626
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
    cmd = ['/usr/bin/getent', 'group', 'root']
    rc, out, err = module.run_command(cmd)
    if rc == 0:
        print("Output: %s" % out)
    else:
        print("Failed: %s" % err)

# Generated at 2022-06-13 05:32:37.315701
# Unit test for function main
def test_main():
    os.environ['LC_ALL'] = 'C'
    os.environ['LANG'] = 'C'
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
    m_run_command = mock.Mock(return_value=(0, '/bin/getent\n/usr/bin/getent', ''))
    m_module = mock.Mock()
    m_module.run_command = m_run_command
    m_module.get_bin_path

# Generated at 2022-06-13 05:32:41.402085
# Unit test for function main
def test_main():
    "Unit test for function main"
    # Create an instance of our class and run the main() function
    import doctest
    doctest.testmod(sys.modules[__name__])

    main()

# Generated at 2022-06-13 05:32:42.056164
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:32:48.628226
# Unit test for function main
def test_main():
    class AnsibleModuleMock(object):
        def run_command(self, cmd):
            return 0, 'foo:bar:baz'

        def get_bin_path(self, cmd, required=False):
            return '/usr/bin/getent'

    class ModuleExitJsonMock(object):
        def __init__(self):
            self.results = None

        def __call__(self, results):
            self.results = results

    class ModuleFailJsonMock(object):
        def __init__(self):
            self.msg = None

        def __call__(self, msg):
            self.msg = msg

    # Initialising a module mock
    module = AnsibleModuleMock()
    module.exit_json = ModuleExitJsonMock()
    module.fail_json = ModuleFailJson