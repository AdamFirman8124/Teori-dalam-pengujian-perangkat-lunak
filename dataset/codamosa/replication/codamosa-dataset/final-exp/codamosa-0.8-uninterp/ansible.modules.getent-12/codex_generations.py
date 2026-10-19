

# Generated at 2022-06-13 05:23:54.157305
# Unit test for function main
def test_main():
    mod = AnsibleModule(argument_spec=dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
        )

    # set up
    mod.params['database'] = 'passwd'
    mod.params['key'] = 'root'
    mod.params['fail_key'] = True
    # execute
    main()

    # set up
    mod.params['database'] = 'passwd'
    mod.params['key'] = 'rOoOt'
    mod.params['fail_key'] = True
    # execute
    main()

# Generated at 2022-06-13 05:23:58.738246
# Unit test for function main
def test_main():
  echo_str = -1
  module = AnsibleModule(
    argument_spec=dict(
      echo_str=dict(type='str', required=True)
    )
  )
  args = dict(
    echo_str = module.params['echo_str']
  )
  echo_str = args['echo_str']
  module.exit_json(msg=echo_str)


# Generated at 2022-06-13 05:24:05.569637
# Unit test for function main
def test_main():
    import sys
    import os

    if 'getent' not in os.listdir('/bin') and 'getent' not in os.listdir('/usr/bin'):
        print("System test requires getent to be installed.")
        sys.exit(1)

    rc, out, err = module.run_command('getent --version')
    if rc != 0 or 'getent' in err:
        print("System test requires getent to be executable")
        sys.exit(1)
    main()

# Generated at 2022-06-13 05:24:14.208772
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

    class FakeDatabases():
        pass


    class FakePopen():
        def __init__(self, cmd):
            pass

        def communicate(self):
            return (None, None)

    class FakePopenFailure(FakePopen):
        def __init__(self, cmd):
            pass

        def communicate(self):
            raise Exception("OMG")


# Generated at 2022-06-13 05:24:18.078795
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

# Generated at 2022-06-13 05:24:29.934013
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


# Generated at 2022-06-13 05:24:34.325071
# Unit test for function main
def test_main():
    import copy
    test_data = copy.deepcopy(RETURN)
    test_data = eval(test_data['ansible_facts'])
    test_data = test_data['getent_passwd']
    test_data = {'getent_passwd': {'root': ['x', '0', '0', 'root', '/root', '/bin/bash']}}
    assert main() == test_data

# Generated at 2022-06-13 05:24:44.396567
# Unit test for function main
def test_main():
    from ansible.module_utils.partial_argument_spec import partial_argument_spec

    def test_getent(database, key, service, split, fail_key, rc, out):
        _module = AnsibleModule(partial_argument_spec(
            full_spec={'database': dict(type='str', required=True),
                       'key': dict(type='str', no_log=False),
                       'service': dict(type='str'),
                       'split': dict(type='str'),
                       'fail_key': dict(type='bool', default=True)},
            argument_spec={'database': database,
                           'key': key,
                           'service': service,
                           'split': split,
                           'fail_key': fail_key}
        ))
        # Mocked getent

# Generated at 2022-06-13 05:24:46.177988
# Unit test for function main
def test_main():
    cmd = ['getent', 'group', 'root']
    rc, out, err = main()
    assert rc == 0

# Generated at 2022-06-13 05:24:54.254473
# Unit test for function main
def test_main():
    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import ansible.module_utils.facts.system.getent as getent

    rc = 1
    out = b''
    err = b''

    getent.getent_bin = ''

    MOCK_MODULE = type('AnsibleModule', (object,), {'run_command': lambda self, cmd: (rc, out, err)})
    mock_module = MOCK_MODULE()
    mock_module.params = dict(database='passwd', key='root')
    getent.main()

    mock_module.params = dict(database='passwd', key='root', service='none')
    getent.main()


# Generated at 2022-06-13 05:25:33.472726
# Unit test for function main
def test_main():
    # dict with basic args
    args = dict(
        database='passwd',
        split=':'
    )

    # dict with args required by module
    opts = dict(
        ansible_facts={}
    )

    # dict with facts/info from module

# Generated at 2022-06-13 05:25:45.840707
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rc = 1
    out = ""
    err = ""
    module.run_command = MagicMock(return_value=(rc, out, err))
    m_exit_json = MagicMock()
    m_fail_json = MagicMock()
    with patch.multiple(basic.AnsibleModule, exit_json=m_exit_json, fail_json=m_fail_json):
        main()
        assert m_fail_json.called
    m_exit_json = MagicMock()
    m_fail_json = MagicMock()
    rc = 2
    with patch.multiple(basic.AnsibleModule, exit_json=m_exit_json, fail_json=m_fail_json):
        main()

# Generated at 2022-06-13 05:25:59.845958
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, load_platform_subclass
    import sys
    import json

    if not 'ANSIBLE_UNIT_TEST' in os.environ:
        raise Exception("ANSIBLE_UNIT_TEST Environment variable not set")

    test_args = {
        'database': 'group',
        'key': 'vcsa',
    }

    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    is_old_facts = module._module._name == 'facts'

# Generated at 2022-06-13 05:26:07.044853
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
   

# Generated at 2022-06-13 05:26:19.661839
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, get_exception
    from ansible.module_utils.action import AnsibleAction
    from ansible.module_utils.action._facts import Facts
    import sys
    import platform
    import os

    if platform.system() == 'Darwin':
        pass
    else:

        def fake_run_command(module, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
            return (0, "1:1:1::/home/test:/bin/sh", "")

        def fake_get_bin_path(name, required=False, opt_dirs=None):
            return '/bin/getent'


# Generated at 2022-06-13 05:26:21.959468
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-13 05:26:34.927182
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

   

# Generated at 2022-06-13 05:26:35.440674
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:26:42.039088
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec = dict(
        database = dict(type='str', required=True),
        key = dict(type='str', no_log=False),
        service = dict(type='str'),
        split = dict(type='str'),
        fail_key = dict(type='bool', default=True),
        ))

    need_key = dict(
        changed=False,
        ansible_facts=dict(
            getent_passwd=dict(
                root=[
                    'x',
                    '0',
                    '0',
                    'root',
                    '/root',
                    '/bin/bash'])
            )
        )


# Generated at 2022-06-13 05:26:54.735379
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    getent_bin = module.get_bin_path('getent', True)

    database = "test"
    msg = "Unexpected failure!"
    dbtree = 'getent_%s' % database
    results = {dbtree: {}}

    # test rc = 0
    out = "test123:test123:test123:test123:test123:test123:test123\n"

# Generated at 2022-06-13 05:27:30.134920
# Unit test for function main
def test_main():

    db = 'passwd'
    key = 'root'
    service = 'service'
    split = 'split'

    fail_key = False

    cp = MagicMock()
    cp.run_command.return_value = 1, 'out', 'err'
    cp.get_bin_path.return_value = '/getent'

    m = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            service=dict(type='str'),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=False,
    )


# Generated at 2022-06-13 05:27:30.940054
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:27:31.744638
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:27:34.047559
# Unit test for function main
def test_main():
    # Tested in test/sanity/code-smell/getent-facts.yml
    pass

# Generated at 2022-06-13 05:27:34.902432
# Unit test for function main
def test_main():

    main()

# Generated at 2022-06-13 05:27:45.873374
# Unit test for function main
def test_main():
    from ansible.modules.extras.cloud.digital_ocean.getent import main

    try:
        getent_bin = module.get_bin_path('getent', True)
    except:
        print("Unable to locate getent binary")
        return False

    m = {
        "params": {"database": "passwd", "key": "root"},
        "run_command": lambda x, y: (0, "root:x:0:0:root:/root:/bin/bash", None),
    }

    result = main()
    assert result["ansible_facts"]["getent_passwd"] == {"root": ["x", "0", "0", "root", "/root", "/bin/bash"]}
    assert result["changed"] is False

# Generated at 2022-06-13 05:27:48.360375
# Unit test for function main
def test_main():
    getent_bin = module.get_bin_path('getent', True)
    pass

# Generated at 2022-06-13 05:28:00.830101
# Unit test for function main
def test_main():

    test_unit = [{'database': 'passwd', 'key': 'root', 'split': ':', 'fail_key': 'yes'},
                 {'database': 'group', 'split': ':', 'fail_key': 'yes'},
                 {'database': 'hosts', 'split': None, 'fail_key': 'yes'},
                 {'database': 'services', 'key': 'http', 'split': ':', 'fail_key': 'no'},
                 {'database': 'shadow', 'key': 'www-data', 'split': ':', 'fail_key': 'yes'}]

    for unit_test in test_unit:
        result = main(unit_test)['ansible_facts']['getent_' + unit_test['database']]

# Generated at 2022-06-13 05:28:06.106158
# Unit test for function main
def test_main():
    test_params = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    )

    module = AnsibleModule(test_params, supports_check_mode=True)


# Generated at 2022-06-13 05:28:16.198934
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible.module_utils.getent import main

    # define arguments to pass to main function (what if this was passed as input?)
    argument_spec = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        fail_key=dict(type='bool', default=True),
    )

    # create an instantiation of the module
    module = AnsibleModule(argument_spec)
    # assign the following variables
    module.params = dict(
        database = 'passwd',
        key = 'root',
        fail_key = True,
    )


# Generated at 2022-06-13 05:29:36.020671
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import binary_type

    # Fail, wrong databse
    1
    commands = {
        'getent': '',
    }
    mp = basic._ANSIBLE_ARGS = {
        'module_name': 'getent',
        'module_args': dict(
            database='doesntexist',
            key='root',
        ),
        'check_mode': False,
        'region': 'us-east-1',
    }
    setattr(basic, 'HAS_PYWINRM', False)
    mm = basic.AnsibleModule(argument_spec={})

# Generated at 2022-06-13 05:29:37.111619
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-13 05:29:44.368350
# Unit test for function main
def test_main():
    from ansible.modules.remote_management.os.getent import main
    import sys
    try:
        # database, key, fail_key
        main(['-i', 'ansible_getent_facts'], {'database': 'passwd', 'key': 'root'})
    except SystemExit as e:
        print(e)
        assert e.code == 0
    sys.exit(1)

# Generated at 2022-06-13 05:29:55.376125
# Unit test for function main
def test_main():
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import Mock
    from ansible.compat.tests.mock import call

    module = Mock()
    mock_params = {
        'database': 'passwd',
        'key': 'root',
        'service': None,
        'split': ':',
    }
    module.params = mock_params
    module.get_bin_path.return_value = 'getent'

    module.run_command.return_value = (0, 'root:*:-2:-2:root:/root:/bin/sh\n', '')

    # 2 responses, 1st is run_command, 2nd is handle_bin_path
    module.side_effect = [None, None]


# Generated at 2022-06-13 05:30:08.741148
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(database=dict(required=True),
                                              key=dict(type='str'),
                                              service=dict(type='str'),
                                              split=dict(type='str'),
                                              fail_key=dict(type='bool')))
    # test ok
    rc = 0
    out = 'passwd:x:0:0:root:/root:/bin/bash\npasswd:x:0:0:root:/root:/bin/bash\npasswd:x:0:0:root:/root:/bin/bash\n'
    err = ''
    module.run_command = Mock(return_value=(rc, out, err))
    main()
    assert module.exit_json.called

    # test error
    rc = 2

# Generated at 2022-06-13 05:30:16.824557
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(database=dict(type='str', required=True), key=dict(type='str')))

    # Mock module's run_command
    m_rc = MagicMock(return_value=(0, 'a: b\nc: d', 0))
    m_rc.run_command = m_rc
    module.run_command = m_rc

    main()

    assert module.exit_json.called

# Generated at 2022-06-13 05:30:17.452195
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:30:20.344380
# Unit test for function main
def test_main():
   '''
   This function tests main function in the module
   '''
   from ansible.modules.system.getent import main
   # Calling the main function
   main()

# Generated at 2022-06-13 05:30:28.476712
# Unit test for function main
def test_main():
    module = get_module_mock()
    result = eval(run_ansible_module(module))
    a_fact = result.pop('ansible_facts', None)
    assert result == dict(
        failed=False,
        changed=False,
        rc=0,
    )
    assert a_fact is not None
    assert 'getent_passwd' in a_fact
    assert a_fact['getent_passwd'] == dict(
        root=['x', '0', '0', 'root', '/root', '/bin/bash'],
    )

# Generated at 2022-06-13 05:30:38.207193
# Unit test for function main
def test_main():
    mock = MagicMock(return_value=0)
    with patch.dict(getent.__salt__, {'cmd.run': mock}):
        assert getent.main('passwd', 'root') == {'ansible_facts': {'getent_passwd': {'root': ['x', 0, 0, 'root', '/root', '/bin/bash']}}}
        mock.assert_called_once_with(['getent', 'passwd', 'root'], python_shell=False)

        assert getent.main('group', split=':', key='root') == {'ansible_facts': {'getent_group': {'root': ['x', 0, 'root']}}}
        mock.assert_called_once_with(['getent', 'group', 'root'], python_shell=False)


# Generated at 2022-06-13 05:33:19.408186
# Unit test for function main
def test_main():
    import json
    import os
    import sys
    import tempfile
    from ansible.module_utils import basic

    input_data = basic._ANSIBLE_ARGS

    # the test module so we can get the params
    test_module = os.path.join(os.path.dirname(__file__), '../library/getent.py')

    # generate a temp file to store the result
    tmp_fd, result_path = tempfile.mkstemp()

    # create a file with the input data
    f = open(input_data, 'w')
    json.dump(dict(
        ANSIBLE_MODULE_ARGS=dict(
            key='root',
            database='passwd',
        ),
    ), f)
    f.close()

    # create a file with the expected outcome
    expected_result