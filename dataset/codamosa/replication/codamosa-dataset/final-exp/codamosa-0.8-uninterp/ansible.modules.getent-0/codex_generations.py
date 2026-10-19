

# Generated at 2022-06-13 05:23:52.155808
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

   

# Generated at 2022-06-13 05:24:00.698179
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action
    from ansible.module_utils._text import to_text
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.shell import ShellModule
    from ansible.module_utils.six import StringIO
    import json

    # Using mock to change the behavior of run_command
    class ConnectorMock():
        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, cmd):
            if cmd[-1] in ['root', 'service', '-s', 'http']:
                return (0, 'output', '')
            if cmd[-1] == 'missing':
                return (2, '', '')

# Generated at 2022-06-13 05:24:10.111546
# Unit test for function main
def test_main():
    import sys
    import os
    import StringIO
    import subprocess

    print(sys.version)
    path = os.path.dirname(os.path.realpath(__file__)) + "/test/lib/ansible/module_utils"
    print(path)
    sys.path.insert(0, path)

    # Create application
    print("Creating application")
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

    print("Setting up test stages")
   

# Generated at 2022-06-13 05:24:17.985341
# Unit test for function main
def test_main():
    out = """
alias:dept_rnd:x:100:100::/home/dept_rnd:/bin/bash
alias:dept_eng:x:101:101::/home/dept_eng:/bin/bash
alias:dept_eng:x:102:102::/home/dept_eng:/bin/bash
alias:dept_eng:x:103:103::/home/dept_eng:/bin/bash
"""
    # Redirect stdout to a fake out
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    # Redirect stderr to a fake out
    old_stderr = sys.stderr
    sys.stderr = io.StringIO()

    # Redirect getent to use our fake
    old_getent = __

# Generated at 2022-06-13 05:24:29.884294
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """

    #  - name: Get root user info
    #  getent:
    #    database: passwd
    #    key: root
    #  - debug:
    #      var: ansible_facts.getent_passwd

    #  - name: Get all groups
    #  getent:
    #    database: group
    #    split: ':'
    #  - debug:
    #      var: ansible_facts.getent_group

    #  - name: Get all hosts, split by tab
    #  getent:
    #    database: hosts
    #  - debug:
    #      var: ansible_facts.getent_hosts

    #  - name: Get http service info, no error if missing
    #  getent:
    #

# Generated at 2022-06-13 05:24:37.038894
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', required=True),
        ),
        supports_check_mode=True,
    )
    module.run_command = mock.MagicMock(return_value=(0, "root:x:0", ""))
    module.get_bin_path = mock.MagicMock(return_value='/usr/bin/getent')
    main()
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', required=True),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 05:24:47.465149
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

   

# Generated at 2022-06-13 05:24:55.022453
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
    getent_bin = module.get_bin_path('getent', True)
    module.params['database'] = 'passwd'
    module.params['key'] = 'root'
    main()
    module.params['database'] = 'group'
    main()
    module.params['database'] = 'hosts'
    main()
    module.params['key'] = 'http'

# Generated at 2022-06-13 05:25:02.482994
# Unit test for function main
def test_main():
    # pylint: disable=import-error
    from ansible.module_utils.facts import ModuleArgsParser

    getent_bin = AnsibleModule(argument_spec={}).get_bin_path('getent', True)

    cmd = [getent_bin, 'group']

    rc, out, err = AnsibleModule(argument_spec={}).run_command(cmd)

    assert rc == 0

    cmd = [getent_bin, 'group', 'root']

    rc, out, err = AnsibleModule(argument_spec={}).run_command(cmd)

    assert rc == 0

    cmd = [getent_bin, 'group', 'foo']

    rc, out, err = AnsibleModule(argument_spec={}).run_command(cmd)

    assert rc == 2


# Generated at 2022-06-13 05:25:09.077149
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

   

# Generated at 2022-06-13 05:25:28.111121
# Unit test for function main
def test_main():
    global module
    import sys, os
    sys.path.append('../')
    sys.path.append('./')
    os.environ['ANSIBLE_MODULE_ARGS'] = '{"database": "passwd", "key": "root"}'
    main()



# Generated at 2022-06-13 05:25:28.811702
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:25:37.008012
# Unit test for function main
def test_main():
    import os
    from ansible.module_utils.six.moves import StringIO

    from ansible.module_utils.six import PY3

    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        os.remove(path)
    except OSError:
        pass

    # Create a file that does not exist to try and trigger the error as much as possible
    fd, path = tempfile.mkstemp()
    os.close(fd)

    # Make sure we have a /bin/sh

# Generated at 2022-06-13 05:25:47.608382
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

    rc = 1
    out = "Missing arguments, or database unknown."
    err = ""
    getent_bin = module.get_bin_path('getent', True)
    assert rc == 1, "Current test should pass"

    rc = 2
    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')

# Generated at 2022-06-13 05:25:50.390388
# Unit test for function main
def test_main():
    # TODO: Make sure ansible_getent is returning expected output
    pass

# Generated at 2022-06-13 05:26:02.126509
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2

    getent_bin = os.path.realpath('./getent_bin.py')
    del sys.modules['getent']

    if PY2:
        getent_dict = '{}'
    else:
        getent_dict = 'dict()'


# Generated at 2022-06-13 05:26:15.968759
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

    params = module.params
    setattr(params, 'database', '/etc/group')
    setattr(params, 'key', None)
    setattr(params, 'split', ':')
    setattr(params, 'fail_key', True)
    results = main()
    assert 'ansible_facts' in results
    assert isinstance(results['ansible_facts']['getent_group'], dict)

# Generated at 2022-06-13 05:26:20.005309
# Unit test for function main
def test_main():
    getent_bin = module.get_bin_path('getent', True)
    if not getent_bin:
        return None
    main()

# Generated at 2022-06-13 05:26:33.915511
# Unit test for function main
def test_main():
    import platform
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

    if platform.system() == 'Linux':
        cmd = ['getent', 'hosts', 'localhost']
        expected_code = 0
        expected_results = {'getent_hosts': {'localhost': [['127.0.0.1']]}}
    else:
        cmd = ['getent', 'group', 'wheel']
        expected_code = 0

# Generated at 2022-06-13 05:26:38.294050
# Unit test for function main
def test_main():
    argv = [
        '-k',
    ]

    # Init
    from ansible.modules.legacy.system import getent as x
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode = True
    )
    module.params = {}

    # Call function
    results = x.main()

    # Check results
    print(results)
    assert(results['failed'] == False)

# Generated at 2022-06-13 05:27:10.733478
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

   

# Generated at 2022-06-13 05:27:22.192442
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    # These are needed to bootstrap the module
    basic.get_distribution = lambda: 'redhat'
    basic._ANSIBLE_ARGS = None

    # And now the actual unit test
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

    getent_

# Generated at 2022-06-13 05:27:31.094063
# Unit test for function main
def test_main():
    import sys
    sys.path.append(os.path.dirname( __file__) + "/..")
    import library.getent as getent
    
    command = {"params": {"database": "passwd", "key": None, "split": None, "service": None, "fail_key": True},
               "supports_check_mode": True,
               "exit_json": {"exit_json_calls": 0}
               }

    def exit_json(**kwargs):
        command["exit_json"]["exit_json_calls"] += 1

    command["exit_json"] = exit_json

    # test getent with no split or key
    getent.main()

    assert(command["exit_json"]["exit_json_calls"] == 1)

    # test getent with split
    get

# Generated at 2022-06-13 05:27:32.376410
# Unit test for function main
def test_main():
    # FIXME: test output, input, etc
    pass

# Generated at 2022-06-13 05:27:41.575490
# Unit test for function main
def test_main():
    module = AnsibleModule({'database': 'services', 'key': 'ssh', 'split': ':', 'check_mode': True, 'service': '22/tcp'})
    main()
    assert module.exit_json['ansible_facts']['getent_services']['ssh'] == ['22/tcp', 'ssh', '', '1', '2', '3', '4', '5', '6']
    assert module.exit_json['changed'] == False
    assert module.exit_json['msg'] == ""


# Generated at 2022-06-13 05:27:52.942859
# Unit test for function main

# Generated at 2022-06-13 05:27:59.269470
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

    rc, out, err = module.run_command('sleep 1')

    assert rc == 0


# Generated at 2022-06-13 05:28:07.517467
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
    results = {'getent_passwd': {'root': ['x', '0', '0', 'root', '/root', '/bin/bash']}}
    module.exit_json(ansible_facts=results)

# Generated at 2022-06-13 05:28:18.059327
# Unit test for function main
def test_main():
    arguments = dict(
        database=dict(type='str', required=True),
        key=dict(type='str', no_log=False),
        service=dict(type='str'),
        split=dict(type='str'),
        fail_key=dict(type='bool', default=True),
    )

    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=True,
    )
    rc = 0
    out = "out"
    err = "err"
    colon = ['passwd', 'shadow', 'group', 'gshadow']

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')

# Generated at 2022-06-13 05:28:25.531965
# Unit test for function main
def test_main():
    import tempfile
    import os
    tmp_dir = tempfile.mkdtemp()
    tmp_file_path = os.path.join(tmp_dir, 'test_file')
    open(tmp_file_path, 'w').close()

    os.environ['SHELL'] = '/bin/bash'
    os.environ['OLDPWD'] = '/tmp'
    os.environ['HOME'] = '/tmp'
    os.environ['USER'] = 'tester'


# Generated at 2022-06-13 05:29:44.806915
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
    module.run_command = mock.Mock( return_value=(0, "testok", "") )
    main()
    module.fail_json.assert_not_called()

    module.run_command = mock.Mock( return_value=(1, "testok", "") )
    main()
    module.fail_json.assert_called_with(msg='Missing arguments, or database unknown.')

# Generated at 2022-06-13 05:29:51.443992
# Unit test for function main
def test_main():
    mock = MagicMock(return_value=dict(
        rc=0,
        stdout='''root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
''',
        stderr='',
    ))

# Generated at 2022-06-13 05:29:58.803186
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
    import sys
    import traceback
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native


    def main():
        database = module.params['database']
        key = module.params.get('key')
        split = module.params.get('split')
        service = module.params.get('service')
        fail_key = module.params.get

# Generated at 2022-06-13 05:30:10.284996
# Unit test for function main
def test_main():
    getent_bin = '/bin/getent'
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


# Generated at 2022-06-13 05:30:21.103424
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    # test_getent()
    setattr(basic.AnsibleModule, 'run_command', run_command)
    rc, out, err = module.run_command([to_bytes('/sbin/getent')])
    assert rc == 0


# Generated at 2022-06-13 05:30:31.129920
# Unit test for function main
def test_main():

    import tempfile

    # case 1:
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b"foobar:*:100:100::/home/foobar:/bin/bash\n")
        tf.flush()

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

        def mock_run_command(cmd, check_rc=False):
            return (0, tf.read(), "")

        module.run_command = mock_run_command

# Generated at 2022-06-13 05:30:44.131239
# Unit test for function main
def test_main():

    # Mock module input
    module_args = {
        'database': 'passwd',
        'key': 'root',
        'service': None,
    }

    # Set up module
    from ansible_collections.os.os_getent.tests.unit.compat.mock import patch
    from ansible.module_utils import basic
    m = basic.AnsibleModule(argument_spec=module_args)

    # Mock commands
    m.run_command = MagicMock(return_value=(0, 'foo', ''))

    # Run the module
    main()

    # Assert results
    expected_result = {'ansible_facts': {'getent_passwd': {'root': ['x', '0', '0', 'root', '/root', '/bin/bash']}}}
    assert m.exit_

# Generated at 2022-06-13 05:30:57.227699
# Unit test for function main
def test_main():
    # Getent module test
    import platform
    import struct
    import sys
    if sys.version_info[0] > 2:
        long = int
    module = AnsibleModule({"database": "passwd","key": "root"})
    if platform.system() == 'Darwin':
        module.run_command = lambda cmd: (0, 'root:*:0:0:System Administrator:/var/root:/bin/sh\n', None)
    elif platform.system() == 'Linux':
        module.run_command = lambda cmd: (0, 'root:x:0:0:root:/root:/bin/bash\n', None)

# Generated at 2022-06-13 05:31:05.435494
# Unit test for function main
def test_main():
    test_1 = {}
    test_1['database'] = 'passwd'
    test_1['key'] = 'root'
    test_1['service'] = None
    test_1['split'] = None
    test_1['fail_key'] = True

    test_2 = {}
    test_2['database'] = 'group'
    test_2['key'] = None
    test_2['service'] = None
    test_2['split'] = ':'
    test_2['fail_key'] = True

    test_3 = {}
    test_3['database'] = 'hosts'
    test_3['key'] = None
    test_3['service'] = None
    test_3['split'] = None
    test_3['fail_key'] = True

    test_4 = {}
    test_4

# Generated at 2022-06-13 05:31:09.178041
# Unit test for function main
def test_main():
    urlfetch_mock = MagicMock(return_value=None)
    with patch('urllib2.urlopen', urlfetch_mock):
        main()