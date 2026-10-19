

# Generated at 2022-06-13 05:23:52.207027
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
        ),
    )

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')

    msg = "Unexpected failure!"
    dbtree = 'getent_%s' % database
    results = {dbtree: {}}

    if key is not None:
        msg = "This key is not in the database"
        results[dbtree][key] = None
        module.exit_json(ansible_facts=results, msg=msg)



# Generated at 2022-06-13 05:24:00.734955
# Unit test for function main
def test_main():
    import unittest
    import test.support
    import tempfile
    import os
    import sys

    class TestMain(unittest.TestCase):
        def setUp(self):
            self.tempdir = tempfile.mkdtemp()
            self.tempname = 'ansible_test'
            self.test_dir = os.path.join(self.tempdir, self.tempname)
            os.mkdir(self.test_dir)
            os.chdir(self.test_dir)

            sys.modules['ansible.module_utils.basic'] = __import__('ansible.module_utils.basic')
            sys.modules['ansible.module_utils.basic'].get_platform = lambda: 'linux'
            sys.modules['ansible.module_utils.basic'].AnsibleModule = __import

# Generated at 2022-06-13 05:24:10.146614
# Unit test for function main
def test_main():
    import json
    import sys

    from ansible.module_utils import basic
    from ansible.module_utils.common.dicts import merge_hash

    if not basic.HAS_GETENT:
        sys.stderr.write("SKIP: getent/module_utils/basic required for this test.\n")
        sys.exit(0)

    test_dict = {
        'database': 'passwd',
        'key': 'root',
    }


# Generated at 2022-06-13 05:24:12.633021
# Unit test for function main
def test_main():
    from ansible.module_utils.common.process import get_bin_path

    getent_bin = get_bin_path('getent', True)

    assert getent_bin != None


# Generated at 2022-06-13 05:24:20.783558
# Unit test for function main
def test_main():
    args = dict(
        database='services',
        key='http',
        fail_key=False
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
    module.params = args
    getent_bin = module.get_bin_path('getent', True)
    cmd = [getent_bin, 'services', 'http']
    (rc, out, err) = module.run_command(cmd)
    assert rc == 0

# Generated at 2022-06-13 05:24:27.279278
# Unit test for function main
def test_main():
    failed = False
    test_data = { 'database': 'hosts', 'custom_args': None }
    test_module = AnsibleModule(argument_spec=dict(
        custom_args=dict(type='str'),
        database=dict(type='str')), check_invalid_arguments=False)
    test_module.params = test_data
    getent_bin = test_module.get_bin_path('getent', True)

    try:
        rc, out, err = test_module.run_command('/usr/bin/echo %s' % getent_bin)
    except Exception as e:
        print("failed to execute command: %s\n" % e)
        failed = True


# Generated at 2022-06-13 05:24:40.469249
# Unit test for function main
def test_main():
    # Given a module and database and key, return a dict
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

    assert main() == {'getent_{}'.format(database): key}

    # Test "ansible_facts": {
    #   "getent_group": {
    #     "kvm

# Generated at 2022-06-13 05:24:41.374226
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-13 05:24:42.198500
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-13 05:24:51.619009
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

    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = 'passwd'
    key = 'systemd-bus-proxy'
    split = ':'
    service = None
    fail_key = True
    getent_bin = '/bin/getent'

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]


# Generated at 2022-06-13 05:25:10.738407
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    import mock
    import inspect
    module_path = os.path.join('/tmp', 'ansible_getent_payload.py')
    if os.path.exists(module_path):
        os.remove(module_path)

# Generated at 2022-06-13 05:25:15.208638
# Unit test for function main
def test_main():

    # Dummy class for AnsibleModule to work.
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda: None
    module.fail_json = lambda: None
    module.run_command = lambda x: (0, '', '')

    main()

# Generated at 2022-06-13 05:25:21.460960
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={
        'database': {'type': 'str', 'required': True},
        'key': {'type': 'str', 'no_log': False},
        'split': {'type': 'str'},
        'service': {'type': 'str'},
        'fail_key': {'type': 'bool', 'default': True}
    })
    module.exit_json = lambda x: None
    main()

# Generated at 2022-06-13 05:25:32.826016
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
   

# Generated at 2022-06-13 05:25:45.237130
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

   

# Generated at 2022-06-13 05:25:51.490037
# Unit test for function main
def test_main():
    module_args = dict(
        database='passwd',
        split=':'
    )
    res = main(module_args)
    assert res['ansible_facts'][0]['passwd'] == {"daemon": ["x", 2, 1, 1], "bin": ["x", 2, 1, 1]}

# Generated at 2022-06-13 05:26:03.323464
# Unit test for function main
def test_main():
    from ansible.module_utils.facts import FactsBase
    from ansible.module_utils.facts import ansible_facts
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import merge_hash

    MergeHash = merge_hash
    AnsibleFacts = ansible_facts
    ansible_facts = AnsibleFacts() # Reset the facts
    facts_dict = dict()

    facts = FactsBase()
    facts_dict = facts.populate()
    ansible_facts = AnsibleFacts(facts_dict)
    ansible_facts.preprocess_parallel()
    assert ansible_facts.getdict() is not None

    params = {}
    params["database"] = "passwd"
    params["key"] = None
    params["split"] = None

# Generated at 2022-06-13 05:26:17.784419
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.action.getent

    args = {
        'fail_key': False,
        'key': None,
        'database': 'group'
    }

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

    with pytest.raises(SystemExit):
        main()


# Generated at 2022-06-13 05:26:26.765162
# Unit test for function main
def test_main():
    # Function name is required for unit test function naming.
    def test_main_inner():
        module = AnsibleModule(
            argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                split=dict(type='str'),
                fail_key=dict(type='bool', default=True),
            ),
            supports_check_mode=True,
        )
        class MockPopen(object):
            def __init__(self, stdout):
                self.returncode = 0
                self.stdout = stdout
        class MockModuleRun(object):
            def __init__(self, stdout):
                self.p = MockPopen(stdout)

# Generated at 2022-06-13 05:26:34.264843
# Unit test for function main
def test_main():
    with patch.object(AnsibleModule, 'params', {'database': 'passwd', 'fail_key': False, 'key': '', 'split': None}):
        with patch.object(AnsibleModule, 'get_bin_path', return_value=None):
            with patch('ansible.module_utils.basic.run_command', return_value=(0, 'root:x:0:0:root:/root:/bin/bash')):
                assert main()

# Generated at 2022-06-13 05:27:08.105500
# Unit test for function main
def test_main():
    args = {
        "database": "passwd",
    }

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

    m_run_command = mock.Mock(return_value=(0, 'root:x:0:0:root:/root:/bin/bash', ''))
    m_get_bin_path = mock.Mock(return_value='/usr/bin/getent')


# Generated at 2022-06-13 05:27:18.969964
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

   

# Generated at 2022-06-13 05:27:29.122681
# Unit test for function main
def test_main():
    os.environ['PATH'] = "/usr/bin:/usr/sbin:/bin:/sbin"
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Mocking
    module.run_command = Mock()
    module.exit_json = Mock()
    module.fail_json = Mock()

    # Expected results
    # http://docs.ansible.com/ansible/latest/getent_module.html#examples
    # Database passwd
    # The list elements depend on the database queried, see

# Generated at 2022-06-13 05:27:29.933886
# Unit test for function main
def test_main():
  assert True

# Generated at 2022-06-13 05:27:43.022058
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.urls import open_url
    from ansible.module_utils.connection import ConnectionError
    import ansible.module_utils.connection
    from ansible.module_utils.urls import open_url
    class AnsibleFailJson(Exception):
      pass
    class AnsibleExitJson(Exception):
      pass
    module = ansible.module_utils.basic.AnsibleModule
    module.run_command = lambda self,cmd: (0,"","")
    module.get_bin_path = lambda self,binary,optional: "/usr/bin/%s" % binary

# Generated at 2022-06-13 05:27:49.083904
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
   

# Generated at 2022-06-13 05:28:01.082546
# Unit test for function main
def test_main():
    import sys

    test_args = ['-database', 'passwd', '-key', 'root', '-service', 'some service']
    if sys.version_info[0] < 3:
        from io import BytesIO as StringIO
    else:
        from io import StringIO


# Generated at 2022-06-13 05:28:09.780167
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            service=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    test_module.params = dict(
        database='passwd',
        key='root',
    )

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:28:14.213800
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'database': 'hosts',
        'key': 'localhost',
    })

    results = {'getent_hosts': {}}
    results['getent_hosts']['localhost'] = ['127.0.0.1', 'localhost']

    assert main()['ansible_facts'] == results

# Generated at 2022-06-13 05:28:15.142908
# Unit test for function main
def test_main():

    # Update existing data
    pass

# Generated at 2022-06-13 05:29:35.895568
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

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]


# Generated at 2022-06-13 05:29:36.991617
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:29:50.440633
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.local import LocalAnsibleModule
    from ansible.module_utils.six import PY2

    # test module params

# Generated at 2022-06-13 05:29:56.122254
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

    module.get_bin_path = lambda *args, **kwargs: None
    module.run_command = lambda *args, **kwargs: (0, None, None)
    main()

# Generated at 2022-06-13 05:30:09.081809
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """
    import ansible.module_getent
    import ansible.module_utils.basic
    import os
    import unittest

    class TestGetent(unittest.TestCase):
        """
        Unit test class to test the getent module
        """

        def setUp(self):
            """
            Setup the Getent module
            """

            self.module = ansible.module_getent

            self.mock_module = mock.Mock()
            self.mock_module.params = {'database':'passwd', 'split':':', 'key':'root'}
            self.mock_module.run_command.return_value = (0,'root:x:0:0:root:root:root:root','')

            self.mock_module

# Generated at 2022-06-13 05:30:15.059693
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    basic.AnsibleModule = my_AnsibleModule
    my_AnsibleModule.params = {
        'database': 'passwd',
        'key': 'root',
        'fail_key': False
    }

    main()

# Mock for function basic.AnsibleModule

# Generated at 2022-06-13 05:30:24.551823
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

   

# Generated at 2022-06-13 05:30:36.675934
# Unit test for function main
def test_main():
    getent_bin = 'getent'
    fail_key = True
    colon = ['passwd', 'shadow', 'group', 'gshadow']
    
    database = 'passwd'
    key = 'root'
    split = None
    service = None

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]

    if service is not None:
        cmd.extend(['-s', service])

    if split is None and database in colon:
        split = ':'
        
    rc, out, err = module.run_command(cmd)

    msg = "Unexpected failure!"
    dbtree = 'getent_%s' % database
    results = {dbtree: {}}


# Generated at 2022-06-13 05:30:46.614607
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    from . import getent_stubs

    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    fixture_data = {}

    def load_fixture(name):
        path = os.path.join(fixture_path, name)

        if path in fixture_data:
            return fixture_data[path]

        with open(path) as f:
            data = f.read()

        try:
            data = json.loads(data)
        except Exception:
            pass

        fixture_data[path] = data
        return data

    @pytest.fixture
    def ansible_module():
        """Simulate ansible Module"""
        return getent_stubs.AnsibleModuleStub()


# Generated at 2022-06-13 05:30:50.575560
# Unit test for function main
def test_main():
    class Options:
        pass

    module = Options()
    module.params = dict(database='passwd')

    module.exit_json = lambda x: None
    module.fail_json = lambda x: None

    main()

# Generated at 2022-06-13 05:33:30.593268
# Unit test for function main
def test_main():

    import pytest, os

    test_data = [
        {'database':'passwd', 'key':'root', 'rc':0},
        {'database':'group', 'rc':0},
        {'database':'hosts', 'rc':0},
        {'database':'services', 'rc':0},
        {'database':'shadow', 'rc':0},
        ]

    for td in test_data:
        module = AnsibleModule(
            argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                split=dict(type='str'),
            ),
            supports_check_mode=True,
        )
        module.params = td
        main()
        assert module.rc == td['rc']