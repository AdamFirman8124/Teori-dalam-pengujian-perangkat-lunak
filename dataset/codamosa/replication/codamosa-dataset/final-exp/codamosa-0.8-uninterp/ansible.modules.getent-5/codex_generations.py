

# Generated at 2022-06-13 05:23:45.441301
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:23:55.404775
# Unit test for function main
def test_main():
    import sys
    import ansible
    
    test_args = "{'database': 'passwd', 'key': 'root', 'fail_key': True, " \
                "'check_mode': False, 'diff_mode': False}"
    test_args = test_args.replace("'", "\"")
    test_args = ansible.utils.unsafe_proxy.AnsibleUnsafeText(test_args)
    sys.argv = ["/usr/bin/ansible-playbook", "",
                "--extra-vars", test_args]
    
    try:
        main()
    except SystemExit as e:
        pass
    assert True

# Generated at 2022-06-13 05:24:03.557440
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    import os
    import pytest
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils import basic
    import os
    import pytest
    from ansible.module_utils.basic import AnsibleModule

    fixture = """

module.exit_json(ansible_facts=dict(getent_passwd=dict(root=['x', '0', '0', 'root', '/root', '/bin/bash'])))

"""


# Generated at 2022-06-13 05:24:11.994019
# Unit test for function main
def test_main():
    '''
    AnsibleModule for testing function main
    '''
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        )
    )

    # this is the return data for the getent test
    # might be better to test output of getent instead
    class Out:
        rc = 0

# Generated at 2022-06-13 05:24:20.390703
# Unit test for function main
def test_main():
    import tempfile
    fd, tmp_file = tempfile.mkstemp()

# Generated at 2022-06-13 05:24:27.026885
# Unit test for function main
def test_main():
    test_command1 = ['getent', 'foo']
    test_command2 = ['getent', 'foo', 'bar']
    test_command3 = ['getent', 'foo', 'bar', '-s', 'foobar']

    class MockModule:
        params = {
            'database': 'foo',
            'key': None,
            'service': None,
            'split': None,
            'fail_key': True
        }

    class MockModuleArgs:
        argument_spec = {}

    class MockRc:
        def __init__(self):
            self.cmd = None
            self.rc = None
            self.stdout = None
            self.stderr = None


# Generated at 2022-06-13 05:24:33.351182
# Unit test for function main
def test_main():
    # Create an arguments object.
    class Args(object):
        pass
    args = Args()
    # args.database = 'passwd'
    # args.key = 'root'
    # args.split = ':'

    assert main(args) == 0


# Generated at 2022-06-13 05:24:39.695315
# Unit test for function main
def test_main():
    # Import dependencies
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.basic import AnsibleModule

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, mock_open, MagicMock, Mock, call

    # Set up a mocker
    mocker = patch('ansible_collections.notstdlib.moveitallout.plugins.module_utils.getent.main.AnsibleModule')

    # Build our test subject
    mocker.start()
    osMock = MagicMock(autospec=True)
    osMock.path.isfile.return_value = False

# Generated at 2022-06-13 05:24:49.572629
# Unit test for function main
def test_main():
    import re
    import os
    import subprocess
    import sys
    import pwd

    from collections import namedtuple

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    pwd_db = {}
    gid_list = []
    uid_list = []

    # get list of users and groups
    for p in pwd.getpwall():
        if p.pw_uid not in uid_list:
            uid_list.append(p.pw_uid)
        if p.pw_gid not in gid_list:
            gid_list.append(p.pw_gid)

    # build a test pwd db

# Generated at 2022-06-13 05:24:59.785372
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

    dbtree = 'getent_%s' % module.params['database']
    results = {dbtree: {}}

    class MockPopen(object):
        def __init__(self):
            pass

        def communicate(self):
            return None, None

        def wait(self):
            if module.params['key']:
                return 1
            else:
                return 0


# Generated at 2022-06-13 05:25:23.526443
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    module = basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        )
    )

    module.get_bin_path = lambda arg, arg2: None


# Generated at 2022-06-13 05:25:34.168795
# Unit test for function main
def test_main():
    import json
    import ansible.module_utils.basic as ansible_basic
    from ansible.module_utils.common.file import is_executable
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:25:46.171510
# Unit test for function main
def test_main():
    import sys, os
    import json
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native

    test_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(test_dir + '/../')
    # Mock ansible module
    mock = AnsibleModule(argument_spec={})
    mod = __import__('getent')
    setattr(mod, 'AnsibleModule', AnsibleModule)
    setattr(mod, 'main', main)
    # Mock ansible module end


# Generated at 2022-06-13 05:26:00.084759
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import deepcopy

    def _fail_json(*args, **kwargs):
        raise Exception(kwargs['msg'])

    def _run_command(*args, **kwargs):
        return 0, 'a:b', ''

    p = {
        'database': 'passwd',
        'key': 'root',
        'fail_key': True,
    }


# Generated at 2022-06-13 05:26:07.163219
# Unit test for function main
def test_main():
    import subprocess
    import sys
    import os
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import StringIO

    assert os.path.isfile(main.__code__.co_filename)
    assert os.access(main.__code__.co_filename, os.X_OK)

    process = subprocess.Popen(['getent'], shell=False, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate()
    assert process.returncode == 1


# Generated at 2022-06-13 05:26:13.142951
# Unit test for function main
def test_main():
    msg = "Unexpected failure!"
    getent_bin = '/usr/bin/getent'
    database = "group"
    key = "test"
    xit = 3
    split = None
    cmd = [getent_bin, database, key]

    rc, out, err = module.run_command(cmd)
    assert rc == 3

# Generated at 2022-06-13 05:26:23.388085
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
   

# Generated at 2022-06-13 05:26:35.754026
# Unit test for function main
def test_main():
    test_input = {
                'database': 'group',
                'fail_key': True,
                'key': None,
                'split': None,
                'service': None
            }
    test_obj = AnsibleModule(argument_spec=test_input)

    test_obj.run_command = mock.Mock()
    test_obj.get_bin_path = mock.Mock(return_value='/usr/bin/getent')
    test_obj.exit_json = mock.Mock()
    test_obj.fail_json = mock.Mock()
    test_obj.run_command.return_value = 0, 'test_out', 'test_err'

    main()


# Generated at 2022-06-13 05:26:42.211957
# Unit test for function main
def test_main():
    # Skip this if we are not running on posix
    try:
        import os
        os_name = os.name
    except ImportError:
        os_name = None

    if os_name != 'posix':
        return

    # Need the main module to run this
    import main

    # Arguments (mock)
    module_args = {}

    # Errors (mock)
    errors = [None]

    # Generate tests
    for database in ['passwd', 'group', 'hosts']:
        module_args['database'] = database

        # Tests for arguments check

# Generated at 2022-06-13 05:26:42.996307
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:27:20.548545
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

   

# Generated at 2022-06-13 05:27:30.135414
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

    # second test
    module.params = dict(database='services')
    module.params['database'] = 'services'
    module.params['key'] = 'telnet'
    module.params['split'] = '\t'

# Generated at 2022-06-13 05:27:32.702859
# Unit test for function main
def test_main():
    import ansible.module_utils.facts.system.getent
    ff = ansible.module_utils.facts.system.getent.main()

    assert ff['ansible_facts']['getent_group']['root'] == ['x', '0']

# Generated at 2022-06-13 05:27:44.843758
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.dictstrify import DictStrify, DictStrifyUnicode
    from ansible.module_utils.six import b, PY3

    module_args = dict(
        database='passwd',
        split=':',
    )

    def mock_run_command(self, cmd, check_rc=True):
        return (0, "root:x:0:0:root:/root:/bin/bash", "")

    def mock_run_command_rc2(self, cmd, check_rc=True):
        return (2, "", "")

    def mock_run_command_rc3(self, cmd, check_rc=True):
        return (3, "", "")


# Generated at 2022-06-13 05:27:59.186499
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            split=dict(type='str'),
        ),
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
        split = ':'


# Generated at 2022-06-13 05:28:07.712619
# Unit test for function main
def test_main():
    '''
    If we were able to run getent, test it.
    '''
    module = AnsibleModule(
        argument_spec = dict(
            database = dict(type = 'str', required = True),
            key = dict(type = 'str', required = False),
            split = dict(type = 'str', required = False),
            fail_key = dict(type = 'bool', required = False),
        ),
        supports_check_mode = False,
    )
    try:
        output = main()
    except Exception:
        pass
    else:
        assert output['ansible_facts'] == "Test Message."


# Generated at 2022-06-13 05:28:18.217540
# Unit test for function main
def test_main():

    # Dummy module
    test_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            split=dict(type='str'),
            service=dict(type='str'),
            fail_key=dict(type='bool'),
        ),
        supports_check_mode=True,
    )

    # Because we're not actually trying to run this command
    test_module.run_command = lambda x: (0, 'root:x:0:0:root:/root:/bin/bash\n_sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/usr/bin/false\nubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash\n', '')

    #

# Generated at 2022-06-13 05:28:25.621449
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
        ))

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')

    getent_bin = module.get_bin_path('getent', True)


# Generated at 2022-06-13 05:28:27.805454
# Unit test for function main
def test_main():
    # Test for module docstring
    assert __doc__

    # Test for example docstring
    assert EXAMPLES

    # Test for return docstring
    assert RETURN

# Generated at 2022-06-13 05:28:35.831049
# Unit test for function main
def test_main():
    file_args = {
        'database': 'passwd',
        'key': 'root',
        'split': ':',
    }
    file_args_key = {
        'status': 0,
        'stdout': [
            '0:root:x:0:0:root:/root:/bin/bash'
        ],
        'stderr': []
    }


# Generated at 2022-06-13 05:29:49.565938
# Unit test for function main

# Generated at 2022-06-13 05:29:54.446798
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path

    if not get_bin_path('getent'):
        raise SkipTest("getent not installed")

    module = basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
    )


# Generated at 2022-06-13 05:30:08.053934
# Unit test for function main
def test_main():
    result = main()
    assert result is not None
    assert result['ansible_facts'] is not None
    assert result['ansible_facts'][0] is not None
    assert result['ansible_facts'][0][0]['getent_passwd'] is not None
    assert result['ansible_facts'][0][0]['getent_shadow'] is not None
    assert result['ansible_facts'][0][0]['getent_group'] is not None
    assert result['ansible_facts'][0][0]['getent_gshadow'] is not None
    assert result['ansible_facts'][0][0]['getent_hosts'] is not None
    assert result['ansible_facts'][0][0]['getent_network'] is not None

# Generated at 2022-06-13 05:30:08.632697
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:30:21.025114
# Unit test for function main
def test_main():

    # Mock Module
    class AnsibleModuleMock:
        def __init__(self):
            self.params = {}

        def assert_has_fail_json(self):
            assert False

        def assert_has_exit_json(self, exit_args):
            assert isinstance(exit_args['ansible_facts']['getent_passwd'], list)
            assert len(exit_args['ansible_facts']['getent_passwd']) == 2
            assert exit_args['ansible_facts']['getent_passwd'][0] == 'root:x:0:0:root:/root:/bin/bash'
            assert exit_args['ansible_facts']['getent_passwd'][1] == 'bin:x:1:1:bin:/bin:/sbin/nologin'

# Generated at 2022-06-13 05:30:29.801648
# Unit test for function main
def test_main():
    argument_spec = {}
    argument_spec["database"] = {"type":"str","required":True}
    argument_spec["key"] = {"type":"str", "no_log":"False"}
    argument_spec["service"] = {"type":"str"}
    argument_spec["split"] = {"type":"str"}
    argument_spec["fail_key"] = {"type":"bool", "default":"True"}

    module = AnsibleModule(argument_spec=argument_spec)
    res = main()
    assert res["ansible_facts"]["getent_passwd"]["root"] == ["x", "0", "0", "root", "/root", "/bin/bash"]

# Generated at 2022-06-13 05:30:39.010350
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path

    # create a mock module, so we can set and control the params
    module = basic.AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # mock the return of get_bin_path

# Generated at 2022-06-13 05:30:54.216311
# Unit test for function main
def test_main():
    from ansible.module_utils import temporary_path, basic
    from ansible.module_utils.basic import AnsibleModule

    my_args = dict(
        database = 'group',
        key = 'root',
        split = ':',
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
    module.run_command = Mock(return_value=(0, 'root:x:0:0:root:/root:/bin/bash', ''))

    main()


# Generated at 2022-06-13 05:30:58.438128
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
    ))
    main()
    

# Generated at 2022-06-13 05:31:05.937462
# Unit test for function main
def test_main():
    import sys
    import shlex
    from ansible.module_utils import basic
    from ansible.module_utils.six.moves import StringIO, shlex_quote

    if sys.version_info >= (3,):
        from io import StringIO
        from shlex import quote as shlex_quote

    if sys.version_info >= (3, 6):
        pytest.importorskip("pytest_cov")
        pytest.importorskip("coverage")
