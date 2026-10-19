

# Generated at 2022-06-13 05:23:52.672375
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

    dbtree = 'getent_%s' % module.params['database']
    results = {dbtree: 'test'}

    module.exit_json(ansible_facts=results)


# Generated at 2022-06-13 05:23:55.225482
# Unit test for function main
def test_main():
    from ansible.module_utils.facts.system.getent import main
    args = {
        "database": "passwd",
        "key": None,
        "split": None
    }
    main(args)

# Generated at 2022-06-13 05:24:03.431146
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
    )

    # key provided, database known
    set_module_args(dict(
        database='passwd',
        key='root',
        service='',
        split='',
        fail_key=True
    ))
    out = main()
    assert out['ansible_facts']['getent_passwd']['root'] == ['x', '0', '0', 'root', '/root', '/bin/bash']

# Generated at 2022-06-13 05:24:11.852319
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common._json_compat import json
    from ansible.module_utils.basic import AnsibleModule
    import pytest
    import os
    import re

    testdata = dict()
    testdata['passwd'] = dict()
    testdata['passwd']['nobody'] = ['', '', '65534', '65534', 'Uid nobody not used', '/', '/usr/sbin/nologin']
    testdata['passwd']['root'] = ['x', '', '0', '0', 'System Administrator', '/var/root', '/bin/sh']

# Generated at 2022-06-13 05:24:20.353080
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

# Generated at 2022-06-13 05:24:27.000101
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

    getent_bin = module.get_bin_path('getent', True)

# Generated at 2022-06-13 05:24:28.009655
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:24:30.805933
# Unit test for function main
def test_main():
    import getent
    print(getent.main())

# Generated at 2022-06-13 05:24:42.316510
# Unit test for function main
def test_main():

    import os
    import sys
    import pytest
    from io import StringIO
    from unittest.mock import patch, call

    test_db_path = os.path.abspath(os.path.dirname(__file__))
    fixture_path = os.path.join(test_db_path, 'fixtures')

    module_name = 'ansible.modules.system.getent'
    getent_module = __import__(module_name)


# Generated at 2022-06-13 05:24:51.729205
# Unit test for function main
def test_main():
    from ansible.modules.system.getent import main
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native

    # We need to mock all the module input params.
    fake_params = {
        'database': 'fake_database',
        'key': 'fake_key',
        'fail_key': 'yes',
    }

    # We need to mock getent return code, stdout and stderr.
    # In this case we will simulate a successful run.
    fake_rc = 0
    fake_stdout = 'fake_stdout'
    fake_stderr = 'fake_stderr'

    # Instantiate our basic AnsibleModule, with the mocked parameters.
    AnsibleModule = basic.AnsibleModule

# Generated at 2022-06-13 05:25:05.715553
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:25:18.270336
# Unit test for function main
def test_main():
    import imp, os

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3

    this_module = imp.load_source(os.path.basename(__file__), __file__)
    this_module.ANSIBLE_MODULE_ARGS = {
        'database': 'passwd'
    }

    try:
        from test.support import EnvironmentVarGuard
    except ImportError:
        from test.test_support import EnvironmentVarGuard

    env_guard = EnvironmentVarGuard()

    fake_path = ['/bin', '/usr/bin']
    env_guard.set('PATH', os.pathsep.join(fake_path))


# Generated at 2022-06-13 05:25:29.008923
# Unit test for function main
def test_main():
    from ansible.module_utils.facts.system.getent import main

    class AnsibleModule:
        def __init__(self, argument_spec, supports_check_mode=False, bypass_checks=False, no_log=False, check_invalid_arguments=True, mutually_exclusive=None, required_together=None, required_one_of=None, add_file_common_args=False, supports_diff=False, supports_inline_artifacts=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.bypass_checks = bypass_checks
            self.no_log = no_log
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually_exclusive = mutually_exclusive or []
            self.required

# Generated at 2022-06-13 05:25:37.093095
# Unit test for function main
def test_main():
    def test_main_use_cases(mocker):
        # mock the run_command function
        mocker.patch(
            'ansible.module_utils.basic.AnsibleModule.run_command',
            return_value=(0, "dummy_success_data", None)
        )
        # mock public functions
        mocker.patch('ansible_collections.ansible.builtin.plugins.module_utils.basic.AnsibleModule.get_bin_path')

        # Test case 1: getent_passwd
        module_args = dict(
            database="passwd"
        )
        with mocker.patch('ansible.module_utils.basic.AnsibleModule.params', module_args):
            main()
        # Test case 2: getent_passwd with key root
        module_args = dict

# Generated at 2022-06-13 05:25:42.952946
# Unit test for function main
def test_main():
    import pytest

    from ansible.module_utils.basic import AnsibleModule

    with pytest.raises(SystemExit):
        main()

    module = AnsibleModule({
        "database": "passwd",
        "key": "root",
    })

    # This should not exit with SystemExit
    main(module)

# Generated at 2022-06-13 05:25:48.636812
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

    assert 'getent_' in main()['ansible_facts']

# Generated at 2022-06-13 05:25:52.365219
# Unit test for function main
def test_main():
    argument_spec = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    )
    data = dict(database='hosts', key='localhost')
    rc, out, err = module.run_command(cmd, data['key'])
    assert rc == 0, "test_main failed"

# Generated at 2022-06-13 05:25:54.501181
# Unit test for function main
def test_main():

    main()

main()

# Generated at 2022-06-13 05:25:55.257645
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:26:03.665977
# Unit test for function main
def test_main():
    # import units for testing
    import ansible.module_utils.basic

    # initialize module
    module = ansible.module_utils.basic.AnsibleModule(
            argument_spec=dict(
                    database=dict(type='str', required=True),
                    key=dict(type='str', no_log=False),
                    service=dict(type='str'),
                    split=dict(type='str'),
                    fail_key=dict(type='bool', default=True),
            ),
            supports_check_mode=True,
    )

    # overwrite module.run_command with mock function
    global run_command
    run_command = lambda cmd: (0, 'root:x:0:0:root:/root:/bin/bash', '')

    # call main
    main()

# Generated at 2022-06-13 05:26:37.623045
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """

    # Arrange
    # Use a private copy of the module under test
    from ansible.utils.module_docs_fragments.platform.posix import getent as module

    # Mock the module
    m = mock.MagicMock()
    m.params = {
        'database': 'passwd',
        'key': 'admin',
        'service': '',
        'split': '',
        'fail_key': '',
    }
    m.get_bin_path.return_value = 'getent'

    # Act
    rc, out, err = module.main()

    # Assert
    assert rc == 0
    assert err == ''
    assert out != ''

# Generated at 2022-06-13 05:26:51.901066
# Unit test for function main
def test_main():
    import tempfile
    import os
    f = tempfile.NamedTemporaryFile('w')
    f.write('root:x:0:0:root:/root:/bin/bash\n')
    f.write('www-data:x:33:33:www-data:/var/www:/bin/sh\n')
    os.fsync(f.fileno())
    f.seek(0)
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import ansiblemodule_getent

# Generated at 2022-06-13 05:27:02.367460
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class AnsibleModuleExit(Exception):
        pass

    class _AnsibleModule:
        def __init__(self, *args, **kwargs):
            for arg in args:
                if not hasattr(self, arg):
                    setattr(self, arg, kwargs.get(arg, None))

        def exit_json(self, *args, **kwargs):
            raise AnsibleModuleExit()

        def fail_json(self, *args, **kwargs):
            self.exit_json(*args, success=False, **kwargs)

    class AnsibleExitJson:
        def __init__(self, args):
            self.args = args
            self._success = False
            self

# Generated at 2022-06-13 05:27:12.808246
# Unit test for function main
def test_main():
    import os

    class AnsibleArgs(object):
        def __init__(self):
            self.params = {
                'database': 'passwd',
                'key': 'root',
                'split': None,
                'service': None,
                'fail_key': True,
            }

        def get_bin_path(self, path, required, opt_dirs=[]):
            return "getent"

        def run_command(self, args):
            # getent passwd root
            return 0, '''root:x:0:0:root:/root:/bin/bash''', ''

    module = AnsibleArgs()
    results = main()

# Generated at 2022-06-13 05:27:24.421026
# Unit test for function main
def test_main():
    args = dict(
        database = 'hosts',
        key = 'localhost',
        split = '\t',
        fail_key = 'yes'
    )

    results = dict(
        ansible_facts = dict(
            getent_hosts = {
                'localhost': ['127.0.1.1', 'localhost']
            }
        )
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

    module.run_command = mock.M

# Generated at 2022-06-13 05:27:32.859018
# Unit test for function main
def test_main():
    import os
    import sys
    import unittest
    import tempfile
    import shutil
    # Save a copy of sys.stdout
    old_stdout = sys.stdout

    # Temporarily replace sys.stdout
    sys.stdout = open(os.devnull, 'w')
    output = tempfile.mkstemp()
    try:
        main()
    finally:
        # Restore sys.stdout
        sys.stdout.close()
        sys.stdout = old_stdout

        # Delete temporary file
        os.unlink(output[1])
        shutil.rmtree(output[1])



# Generated at 2022-06-13 05:27:44.927142
# Unit test for function main
def test_main():
    def handler(module, result, exc=False):
        if exc:
            assert isinstance(result, Exception)
        else:
            assert 'ansible_facts' in result
            assert 'getent_hosts' in result['ansible_facts']
            assert 'ansible_getent_hosts' in result['ansible_facts']
            assert result['ansible_facts']['getent_hosts']['127.0.0.1'] == result['ansible_facts']['ansible_getent_hosts']['127.0.0.1']
            assert result['ansible_facts']['getent_hosts']['127.0.0.1'] == ['localhost']


# Generated at 2022-06-13 05:27:59.239572
# Unit test for function main
def test_main():
    import tempfile
    import platform
    import os

    test_shelve = tempfile.NamedTemporaryFile(delete=False)
    test_shelve.close()

    test_hosts = tempfile.NamedTemporaryFile(delete=False)
    test_hosts.close()

    test_passwd = tempfile.NamedTemporaryFile(delete=False)
    test_passwd.close()

    # test hosts file
    with open(test_hosts.name, "w") as f:
        f.write("127.0.0.1 localhost\n")
        f.write("127.0.1.1 vagrant\n")

    # test passwd file

# Generated at 2022-06-13 05:28:09.203346
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

   

# Generated at 2022-06-13 05:28:19.457272
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
    class AnsibleModule_fail_json(object):
        def __init__(self, msg):
            self.msg = msg

    class AnsibleModule_exit_json(object):
        def __init__(self, facts):
            self.facts = facts

    m_fail_json = AnsibleModule_fail_json
    m_exit_json = AnsibleModule_exit_json

    assert main() == m_fail_

# Generated at 2022-06-13 05:29:30.035608
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:29:38.168496
# Unit test for function main
def test_main():
    import sys
    sys.path.insert(0, '')
    import getent
    import ansible.module_utils.basic
    import ansible.module_utils.action
    import ansible.module_utils.facts
    import ansible.module_utils.common._collections_compat
    import ansible.module_utils.common.dict_transformations
    import ansible.module_utils.common.removed
    import ansible.module_utils.common.text_utils

    global module

# Generated at 2022-06-13 05:29:47.958954
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={
            'database': dict(type='str', required=True),
            'key': dict(type='str', no_log=False),
            'split': dict(type='str'),
            'fail_key': dict(type='bool', default=True),
        },
        supports_check_mode=True,
    )

    rc = 0
    out = 'brian:,20000:20000:,/home/brian,,,'
    err = ''
    try:
        module.run_command(cmd)
    except Exception as e:
        msg = to_native(e)
        exception = traceback.format_exc()

    msg = 'Unexpected failure!'
    dbtree = 'getent_' + 'passwd'
    results = {}
    results[dbtree]

# Generated at 2022-06-13 05:29:56.093693
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
        supports_check_mode=True,
    )
    module.run_command = lambda *args, **kwargs: ('', '', 0)
    module.run_command.return_value = ('', '', 0)
    result = main()
    assert result['ansible_facts']['getent_test']['testkey'] == ['testvalue']
    assert result['changed'] == False

# Generated at 2022-06-13 05:30:09.084181
# Unit test for function main
def test_main():
    import ansible.module_utils.action.getent as getent

    function_results = {
        'getent_passwd': {
            'root': ['x', '0', '0', 'root', '/root', '/bin/bash'],
        },
        'getent_group': {
            'root': ['x', '0'],
        },
        'getent_hosts': {
            '127.0.0.1': ['localhost'],
        },
        'getent_shadow': {
            'root': ['x', '', '0', '0', '0', '7', '', '', '', ''],
        },
    }


# Generated at 2022-06-13 05:30:21.066740
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

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    if key is not None:
        cmd = ['getent', database, key]

# Generated at 2022-06-13 05:30:31.089026
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.system.getent import main
    import pytest

    # Test that function fails as arguments are missing
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        def my_get_bin_path(arg):
            return '/bin/getent'
        setattr(basic, 'get_bin_path', my_get_bin_path)
        setattr(get_bin_path, 'get_bin_path', my_get_bin_path)
        main()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    # Test that function fails as database is

# Generated at 2022-06-13 05:30:44.129297
# Unit test for function main
def test_main():
    # call main() with a set of valid arguments to test for success
    result = main({
        "database": "passwd",
        "key": "root",
        "service": None,
        "split": None,
        "fail_key": "True"
    })
    # remove "skip_conditions" from results
    if "skip_conditions" in result:
        del result["skip_conditions"]
    # remove sensitive information before comparing to the baseline
    if "ansible_facts" in result:
        del result["ansible_facts"]
    # now compare the results
    assert result == {
        "changed": False,
        "ansible_facts": {"getent_passwd": {"root": ["root", "x", "0", "0", "root", "/root", "/bin/bash"]}}
    }
   

# Generated at 2022-06-13 05:30:54.543019
# Unit test for function main
def test_main():
    test_args = {
        "database": "hosts",
        "key": "127.0.0.1",
        "split": "     ",
    }

    expected = {"getent_hosts": {"127.0.0.1": ["localhost"]}}

    module = AnsibleModule(argument_spec=dict(
        database=dict(required=True, type='str'),
        key=dict(type='str'),
        split=dict(type='str')
    ))

    module.params = test_args

    results = main()
    assert(results["ansible_facts"]["getent_hosts"] == expected["getent_hosts"])

# Generated at 2022-06-13 05:31:04.813557
# Unit test for function main
def test_main():
    # First test should return a getent_passwd dictionary with 'root' key and a list of the root user's fields
    class AnsibleModule:
        def __init__(self, **kwargs):
            self.run_command = lambda x: (0, 'root:x:0:0:root:/root:/bin/bash', None)
            self.fail_json = lambda msg: msg

    class AnsibleModule_params:
        class AnsibleModule_get_bin_path:
            def __init__(self, x, y):
                self.x = x

        def __init__(self, **kwargs):
            self.database = 'passwd'
            self.key = 'root'
            self.split = ':'