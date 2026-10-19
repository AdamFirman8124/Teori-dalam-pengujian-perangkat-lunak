

# Generated at 2022-06-13 05:23:55.177857
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    def run_command_mock(args, check_rc=True, **kw):
        return 0, '', ''

    orig_run_command = basic.AnsibleModule.run_command

    # Mock run_command
    basic.AnsibleModule.run_command = run_command_mock
    module = basic.AnsibleModule(argument_spec={'database': {'required': True, 'type': 'str'}, 'key': {'no_log': False, 'type': 'str'}, 'service': {'type': 'str'}, 'split': {'type': 'str'}, 'fail_key': {'default': True, 'type': 'bool'}}, supports_check_mode=True)
    basic.AnsibleModule.run_command = orig_run_command

# Generated at 2022-06-13 05:23:56.083331
# Unit test for function main
def test_main():
    print('Test', main())

# Generated at 2022-06-13 05:24:04.052969
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
        supports_check_mode=True,
    )
    # Test passing value for database:
    test_module.params = {'database': 'passwd'}
    result = main()
    # Test passing value for key:
    test_module.params = {'database': 'passwd', 'key': 'root'}
    result = main()
    # Test passing value for service:

# Generated at 2022-06-13 05:24:12.749708
# Unit test for function main
def test_main():
    from ansible.module_utils import module_args_parser

    test_args = dict(
        database='passwd',
        key='root',
        service='/bin/false',
        split=':',
        fail_key=True,
    )

    module_args = module_args_parser.get_module_args(test_args)

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

    assert main() == m.exit_json()

# Generated at 2022-06-13 05:24:21.588444
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

    database = 'passwd'
    key = 'root'
    split = ':'
    service = None
    fail_key = True

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]

# Generated at 2022-06-13 05:24:27.765536
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

   

# Generated at 2022-06-13 05:24:41.119509
# Unit test for function main
def test_main():
    # assert 0 == 0

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


# Generated at 2022-06-13 05:24:48.856578
# Unit test for function main
def test_main():
    import inspect
    import os

    mod = AnsibleModule({'database': 'passwd', 'key': 'root'},
                        check_invalid_arguments=False)
    path = [x for x in os.environ['PATH'].split(':') if os.path.exists(os.path.join(x, 'getent'))]
    assert mod.run_command([os.path.join(path[0], 'getent'), 'passwd', 'root'])

    assert mod.run_command([os.path.join(path[0], 'getent'), 'passwd'])

# Generated at 2022-06-13 05:24:59.408476
# Unit test for function main
def test_main():
    import os

    # We must override function main to add the fake_binary
    # which is not present in the unitary test
    def _main():
        module = AnsibleModule(
            argument_spec=dict(
                database=dict(type='str', required=True),
                key=dict(type='str', no_log=False),
                split=dict(type='str'),
            ),
            supports_check_mode=True,
        )

        database = module.params['database']
        key = module.params.get('key')
        split = module.params.get('split')

        # We need to add a fake getent binary to the PATH
        os.environ['PATH'] = os.path.abspath(os.path.dirname(__file__)) + ':' + os.environ['PATH']

        get

# Generated at 2022-06-13 05:25:06.012023
# Unit test for function main
def test_main():
    # ansible_facts cannot be mocked
    import ansible.module_utils.facts.system.getent
    import ansible.module_utils.facts.system.getent.facts as getentfacts
    try:
        reload(ansible.module_utils.facts.system.getent)
        reload(ansible.module_utils.facts.system.getent.facts)
    except:
        pass
    from ansible.module_utils.facts.system.getent import main
    from ansible.module_utils.facts.system.getent.facts import getent_facts

    def mock_ansible_module(**kwargs):
        class MockAnsibleModule(object):
            def __init__(self, **kwargs):
                self.params = kwargs['params']

# Generated at 2022-06-13 05:25:32.561836
# Unit test for function main
def test_main():
    # return un-mocked values
    def fake_run_command(cmd, tmp=None, check_rc=True, close_fds=True):
        return rc, out, err
    module = AnsibleModule(
        argument_spec=dict(
            database=dict(type='str', required=True),
            key=dict(type='str'),
            split=dict(type='str'),
        ),
    )
    # save the actual run_command for later
    real_run_command = module.run_command
    # replace with our own
    module.run_command = fake_run_command

    # run test cases
    # all return a failed result, exit_json and fail_json have been mocked out
    # we only care about the results, so test cases can be added without
    # worrying about ids or error messages

   

# Generated at 2022-06-13 05:25:38.973894
# Unit test for function main
def test_main():
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

    colon = ['passwd', 'shadow', 'group', 'gshadow']
    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    fail_key = module.params.get('fail_key')


# Generated at 2022-06-13 05:25:48.527630
# Unit test for function main
def test_main():
    test1 = dict(database='passwd', key='root')
    test2 = dict(database='group', split=':')
    test3 = dict(database='passwd', key='root', fail_key=False)
    test4 = dict(database='group', split=':', fail_key=False)
    test5 = dict(database='passwd', key='xxxx', fail_key=False)
    test6 = dict(database='group', split=':', fail_key=False)
    test7 = dict(database='passwd', key='xxxx', fail_key=True)
    test8 = dict(database='group', split=':', fail_key=True)


# Generated at 2022-06-13 05:25:53.765892
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(database=dict(type='str', required=True),
                                              key=dict(type='str'),
                                              split=dict(type='str'),
                                              fail_key=dict(type='bool', default=True),
                                              ),
                           supports_check_mode=True)
    module.params = {'database': 'passwd',
                     'key': 'root',
                     'split': ':'}
    try:
        rc, out, err = main()
    except Exception as e:
        module.fail_json(msg=to_native(e), exception=traceback.format_exc())

    module.exit_json(ansible_facts=out)

# Generated at 2022-06-13 05:25:54.558356
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 05:26:04.206789
# Unit test for function main
def test_main():
    """
    Test module main function
    """

    import os
    import tempfile
    import shutil
    import filecmp

    test_dir = tempfile.mkdtemp()
    test_files = {
        'testfile1': 'This is a test file1',
        'testfile2': 'This is a test file2',
    }
    for name, content in test_files.items():
        test_file = open(os.path.join(test_dir, name), 'w')
        test_file.write(content)
        test_file.close()

    module = import_module('ansible.modules.files.getent')
    main(module, test_dir)

    shutil.rmtree(test_dir)

# Generated at 2022-06-13 05:26:04.963792
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:26:16.991488
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=
        dict(
            database=dict(type='str', required=True),
            key=dict(type='str', no_log=False),
            split=dict(type='str'),
            fail_key=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    class dummy():
        def __init__(self, cmd_run, rc, out, err):
            self.cmd_run = cmd_run
            self.rc = rc
            self.out = out
            self.err = err
            self.stdout = out
            self.stderr = err

    if module.params['database'] == 'passwd':
        rc = 0

# Generated at 2022-06-13 05:26:26.706222
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

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')

    getent_bin = module.get_bin_path('getent', True)

    if key is not None:
        cmd = [getent_bin, database, key]
    else:
        cmd = [getent_bin, database]

    if split is None:
        split = ':'


# Generated at 2022-06-13 05:26:29.936226
# Unit test for function main
def test_main():
    import ansible.module_utils.common.removed as removed_module
    assert removed_module.__dict__['main'] == main
    return

# Generated at 2022-06-13 05:27:00.781157
# Unit test for function main
def test_main():

    class AnsibleModuleMock(object):
        def __init__(self, **kwargs):
            self.run_command_results = []
            self.run_command_results.append(kwargs['run_command_results'])
            self.run_command_calls = []
            self.params = kwargs['params']

        def run_command(self, *args, **kwargs):
            self.run_command_calls.append((args, kwargs))
            return self.run_command_results.pop(0)

        def get_bin_path(self, binary, required):
            return '/bin/getent'

    class Obj(object):
        def __init__(self, **kwargs):
            for field in kwargs:
                setattr(self, field, kwargs[field])



# Generated at 2022-06-13 05:27:06.950251
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
    assert getent_bin == '/usr/bin/getent'



# Generated at 2022-06-13 05:27:17.828703
# Unit test for function main
def test_main():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(AnsibleModule):
        def __init__(self):
            super(TestModule, self).__init__({
                'argument_spec': dict(
                    database=dict(type='str', required=True),
                    key=dict(type='str', no_log=False),
                    service=dict(type='str'),
                    split=dict(type='str'),
                    fail_key=dict(type='bool', default=True),
                ),
                'supports_check_mode': True,
            })


# Generated at 2022-06-13 05:27:28.128710
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    import ansible.module_utils.action
    import ansible.module_utils.facts
    import ansible.module_utils.satellite_facts

    try:
        from __main__ import display
    except ImportError:
        display = None

    module = basic.AnsibleModule(
        argument_spec = dict(
            database = dict(type='str', required=True),
            key = dict(type='str', no_log=False),
            split = dict(type='str'),
            fail_key = dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Mock display
    module._display = display

# Generated at 2022-06-13 05:27:40.068354
# Unit test for function main
def test_main():
    import _mock as mock
    import _mock_module
    import _mock_runner

    _mock_module.ansible_module_instance = mock.MagicMock()
    _mock_module.ansible_module_instance.params = {
        'database': 'passwd',
        'key': 'root',
    }

    _mock_runner.ansible_module_instance = _mock_module.ansible_module_instance

    getent_facts = main()
    assert getent_facts['ansible_facts']['getent_passwd']['root'] == ['x', '0', '0', 'root', '/root', '/bin/bash']

# Generated at 2022-06-13 05:27:41.641948
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-13 05:27:52.941981
# Unit test for function main
def test_main():
    import os
    import re
    import time
    import json

    # unit test for default configuration, with key  and no split
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
    fail_key = module

# Generated at 2022-06-13 05:28:03.926233
# Unit test for function main
def test_main():
    # AnsibleModule.run_command does not exist in python unit test,
    # but AnsibleModule.run_command does not actually call the function we want to test
    # so, we need to mock it
    def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        rc =0
        stdout = "stdout"
        stderr = "stderr"
        return (rc,stdout,stderr)
    def get_bin_path(self, cmd, required=False):
        return "cmd_path"


# Generated at 2022-06-13 05:28:11.222732
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

    getent_bin = module.get_bin_path('getent')


# Generated at 2022-06-13 05:28:21.210373
# Unit test for function main
def test_main():
    import os
    import sys
    import testlib
    import pytest
    from ansible.module_utils import basic

    module_path = os.path.realpath(os.path.dirname(__file__))

    fake_paths = {}
    fake_paths.update(os.environ)
    fake_paths['PATH'] += ":%s" % os.path.join(module_path, "./bin")

    testlib.FakeEnv(fake_paths).set()

    def exit_json(*args, **kwargs):
        sys.exit(0)

    def fail_json(*args, **kwargs):
        sys.exit(1)

    def run_command(*args, **kwargs):
        return 0, args[0], ""


# Generated at 2022-06-13 05:29:37.697795
# Unit test for function main
def test_main():
    import os
    import sys
    import pytest

    # Prevent loading of kwarg_spec which tries a relative import
    from ansible.module_utils.getent import AnsibleModule
    from ansible.module_utils.facts import ModuleArgsParser

    sys.modules['ansible.module_utils.action'] = None


    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
    m_args = dict(
        database='passwd',
        args=dict(
            database='passwd',
            key='coca',
            split=':',
            service=None,
            fail_key=True,
        ),
    )

    def run_module(*args, **kwargs):
        m = AnsibleModule(**kwargs)
        return m.run(*args)

# Generated at 2022-06-13 05:29:47.601620
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import cStringIO

    # This backports basic._ANSIBLE_ARGS to Ansible 2.8
    # See https://github.com/ansible/ansible/pull/43180/files#r240296665
    try:
        import __main__
        __main__.frozen = "not"
    except (NameError, AttributeError):
        __file__ = __file__

    # Instantiate module
    try:
        unicode('foo')
    except NameError:
        bytes_type = bytes
    else:
        bytes_type = str

    args = basic._ANSIBLE_ARGS


# Generated at 2022-06-13 05:29:52.496038
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

    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            super(AttrDict, self).__init__(*args, **kwargs)
            self.__dict__ = self

    module.params = AttrDict(database='passwd', key='root', split=':')

    main()

# Generated at 2022-06-13 05:29:54.349592
# Unit test for function main
def test_main():
    main()


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 tw=79:

# Generated at 2022-06-13 05:30:08.059759
# Unit test for function main
def test_main():
    getent_bin = os.path.expanduser("~/bin/getent")
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

    database = module.params['database']
    key = module.params.get('key')
    split = module.params.get('split')
    service = module.params.get('service')
    fail_key = module.params.get('fail_key')


# Generated at 2022-06-13 05:30:20.474760
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

   

# Generated at 2022-06-13 05:30:30.930834
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
    getent_bin = module.get_bin_path('getent', True)
    cmd = [getent_bin, 'passwd']
    rc, out, err = module.run_command(cmd)
    result = main()
    assert result != 0
    rc, out, err = module.run_command(cmd)
    result = main()
    assert result != 0
    rc, out, err = module.run_command(cmd)
    result = main()

# Generated at 2022-06-13 05:30:35.136001
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    assert to_bytes(main()) == b'{"ansible_facts": {"getent_passwd": {"root": ["x", "0", "0", "root", "/root", "/bin/bash"]}}}'

# Generated at 2022-06-13 05:30:44.658075
# Unit test for function main
def test_main():
    args = dict(
        database='passwd',
        key=None,
        fail_key=True,
    )
    module = AnsibleModule(argument_spec=args)

    def side_effect(*args, **kwargs):
        out = "root:x:0:0:root:/root:/bin/bash\nbin:x:1:1:bin:/bin:\n"
        return (0, out, '')

    def side_effect_fail(*args, **kwargs):
        out = ""
        return (1, out, '')

    module.run_command = side_effect
    main()

    module.run_command = side_effect_fail
    main()

# Generated at 2022-06-13 05:30:57.375600
# Unit test for function main
def test_main():
    post_process_json = '''
{"msg": "One or more supplied key could not be found in the database.", "ansible_facts": {"getent_passwd": {}}, "invocation": {"module_args": {"split": null, "fail_key": true, "database": "passwd", "key": "root"}}}
    '''

    process_error_json = '''
{"msg": "Unexpected failure!", "ansible_facts": {"getent_passwd": {}}, "invocation": {"module_args": {"split": null, "fail_key": true, "database": "passwd", "key": "root"}}}
    '''

    pre_process_json = '''
{"ansible_facts": {"getent_passwd": {}}, "changed": false}
    '''
    assert main() == post_process_