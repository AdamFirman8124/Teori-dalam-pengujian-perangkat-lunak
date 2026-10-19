

# Generated at 2022-06-13 05:59:51.567197
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    module_validate_certs = True
    module_check_mode = False
    module_result = {}
    module_rc = 0

    def execute_command(cmd):
        stdout = "keyid:\n"
        if cmd[-1] == "bad_key":
            stdout = "bad key"
        return stdout, ""

    rpm_key = RpmKey(None)
    rpm_key.rpm = "rpm"
    rpm_key.gpg = "gpg"
    rpm_key.module = None
    rpm_key.module.check_mode = module_check_mode
    rpm_key.module.run_command = execute_command
    rpm_key.module.validate_certs = module_validate_certs

# Generated at 2022-06-13 06:00:01.293391
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    module = None
    key = "test_gpg_key"
    rpm = "test_rpm"
    rpm_obj = RpmKey(module)
    rpm_obj.rpm = rpm
    rpm_obj.execute_command = mock_execute_command
    import_key_mock = MagicMock(name="execute_command")
    rpm_obj.execute_command = import_key_mock
    rpm_obj.import_key(key)
    import_key_mock.assert_called_with([rpm, "--import", key])


# Generated at 2022-06-13 06:00:07.364700
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    import sys
    sys.path.append(".")
    m = AnsibleModule({})
    instance = RpmKey(m)
    assert(instance.is_keyid("0xDEADBEEF") == True)
    assert(instance.is_keyid("DEADBEEF") == True)
    assert(instance.is_keyid("0xDEADBEE") == False)
    assert(instance.is_keyid("DEADBEE") == False)

# Generated at 2022-06-13 06:00:13.992818
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import sys

    # Initialize a module like ansible.module_utils.basic.AnsibleModule
    class MockAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.params = {}
            self.exit_json = sys.exit
            self.fail_json = sys.exit



# Generated at 2022-06-13 06:00:20.517125
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import mock

    module = mock.Mock()
    RpmKeyObject = RpmKey(module)
    RpmKeyObject.rpm = "rpm"

    with mock.patch('os.path.isfile') as mock_isfile:
        mock_isfile.return_value = True
        RpmKeyObject.import_key("/tmp/test.gpg")
        module.run_command.assert_called()


# Generated at 2022-06-13 06:00:29.760685
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    import tempfile

    # Create a tempfile
    tempfd, tempname = tempfile.mkstemp()

    # Create a fake keyid
    keyid = 'BD6E1A6F'

    # Create a fake rpm command
    rpm_cmd = 'echo gpg-pubkey-%s' % keyid

    # Create a fake gpg command
    gpg_cmd = "echo fpr:3E:16:08:D7:16:22:FA:7B:34:AC:C4:64:53:E8:06:66:FB:2E:DB:5F"

    # Create a fake RpmKey object
    rpmkey_obj = RpmKey(rpm_cmd, gpg_cmd, keyid)

    # Call the is_key_imported method

# Generated at 2022-06-13 06:00:39.911556
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module = 'ansible.builtin.rpm_key'
    # cmd = 'echo 1'
    # cmd = 'echo 1 && false'
    # cmd = 'echo 1 && false'
    cmd = 'echo 1; false'

    module = __import__(module, globals(), locals(), ['RpmKey'])
    rpm_key = module.RpmKey(None)
    # print(rpm_key.rpm)
    # print(rpm_key.gpg)
    # stdout, stderr = rpm_key.execute_command(['echo', '1'])
    stdout, stderr = rpm_key.execute_command(cmd.split())
    print(stdout)
    print(stderr)
    # print(rpm_key.is_key_imported('DEADB33F'))

   

# Generated at 2022-06-13 06:00:47.391988
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import tempfile
    import os
    keyfile = tempfile.mkstemp()
    os.write(keyfile[0], "test")
    module = MockAnsibleModule(check_mode=True)
    module.check_mode = False
    rpmkey = RpmKey(module)
    rpmkey.import_key(keyfile[1])
    os.unlink(keyfile[1])


# Generated at 2022-06-13 06:00:56.539218
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile

    a = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 06:00:58.336070
# Unit test for constructor of class RpmKey
def test_RpmKey():
    """RpmKey unit tests"""
    import mock
    with mock.patch('ansible.module_utils.basic.AnsibleModule', autospec=True):
        main()

# Generated at 2022-06-13 06:01:19.143926
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    '''
    Test method drop_key of class RpmKey.
    '''
    # Setup test
    keyid = 'DEADB33F'
    rpm = '/usr/bin/rpm'
    rpm_key = RpmKey(keyid, rpm)

    # Execute tested method
    rpm_key.drop_key(keyid)

    # Assert results
    assert result == expected, 'Expected: %s, but was: %s' % (expected, result)


# Generated at 2022-06-13 06:01:25.443221
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    import ansible.module_utils.rpm_key

    m = ansible.module_utils.rpm_key
    strings = [
        ('0xDEADB33F', 'DEADB33F'),
        ('DEADB33F', 'DEADB33F'),
        ('deadb33f', 'DEADB33F'),
        ('0XDEADB33F', 'DEADB33F'),
    ]
    for test, expect in strings:
        r = m.RpmKey(None)
        assert r.normalize_keyid(test) == expect


# Generated at 2022-06-13 06:01:37.358376
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2, PY3
    import mock
    import os

    class MockAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.result = {'changed': False}
            super(MockAnsibleModule, self).__init__(*args, **kwargs)

        def exit_json(self, **kwargs):
            if 'changed' in kwargs:
                self.result['changed'] = kwargs['changed']
            self.result.update(kwargs)
            self.exit_args = kwargs


# Generated at 2022-06-13 06:01:47.568088
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Get key
    import requests
    key = requests.Response()
    key.status_code = 200

# Generated at 2022-06-13 06:01:58.476247
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Test module is working properly
    assert(is_pubkey('-----BEGIN PGP PUBLIC KEY BLOCK-----\n-----END PGP PUBLIC KEY BLOCK-----\n'))

    # Test module is working properly
    assert(not is_pubkey('-----BEGIN PGP PUBLIC KEY B'))

    # Test module is working properly
    mod = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Test module is working properly
    obj = RpmKey(mod)



# Generated at 2022-06-13 06:02:00.870054
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    RpmKey.getkeyid(None, "some_mock_file")

# Generated at 2022-06-13 06:02:13.220838
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    import unittest

    class TestRpmKey(unittest.TestCase):
        def test_is_key_imported(self):
            class FakeModule():
                def __init__(self):
                    self.run_command_run_command_call_count = 0
                    self.__run_command_call_args = []
                    self.check_mode = False

                def run_command(self, cmd):
                    self.run_command_run_command_call_count += 1
                    self.__run_command_call_args.append(cmd)

                    if self.run_command_run_command_call_count == 1:
                        return 0, '\nkey1\nkey2', ''


# Generated at 2022-06-13 06:02:21.004574
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    r = RpmKey(None)
    assert r.is_keyid('0x0D8469F1')
    assert r.is_keyid('0D8469F1')
    assert not r.is_keyid('0x')
    assert not r.is_keyid('0D8469F12')
    assert not r.is_keyid('foo')


# Generated at 2022-06-13 06:02:25.253299
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    key_valid = '0x12345678'
    assert RpmKey.is_keyid(self, key_valid)
    key_valid = '12345678'
    assert RpmKey.is_keyid(self, key_valid)
    key_invalid = '123456789'
    assert not RpmKey.is_keyid(self, key_invalid)

# Generated at 2022-06-13 06:02:33.242349
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import os
    import types

    linux_distribution = lambda: [None, None, 'CentOS']
    os.path.isfile = types.MethodType(lambda self, filename: True, os)
    os.path.isdir = types.MethodType(lambda self, filename: True, os)
    os.access = types.MethodType(
        lambda self, filename, mode: True, os)
    os.geteuid = types.MethodType(lambda self: True, os)
    os.path.exists = types.MethodType(lambda self, filename: True, os)
    os.environ = {
        'PATH': '/sbin:/usr/sbin:/usr/local/sbin:/bin:/usr/bin:/usr/local/bin'
    }

# Generated at 2022-06-13 06:03:07.644470
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    module = AnsibleModule(
            argument_spec=dict(
                state=dict(type='str', default='present', choices=['absent', 'present']),
                key=dict(type='str', required=True, no_log=False),
                fingerprint=dict(type='str'),
                validate_certs=dict(type='bool', default=True),
            ),
        )

    rpmKey = RpmKey(module)
    assert rpmKey.is_key_imported("0xEBC6E12C62B1C734026B2122A20E52146B8D79E6") == False
    assert rpmKey.is_key_imported("EBC6E12C62B1C734026B2122A20E52146B8D79E6") == False
    assert rpmKey.is_

# Generated at 2022-06-13 06:03:15.530931
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # Testing constructor
    module = AnsibleModule(argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True)
    r = RpmKey(module)
    assert r.module == module

# Generated at 2022-06-13 06:03:28.301231
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    """Unit tests for class RpmKey, method is_key_imported"""

    class MockModule():
        def __init__(self, x):
            self.x = x
        def run_command(self, cmd, use_unsafe_shell=True):
            if cmd[-2:] == ' -q':
                return 0, self.x, None
            else:
                return 0, self.x, None
        def fail_json(self, msg):
            print(msg)
            pass

    class MockModule_key_imported():
        def __init__(self, x):
            self.x = x

# Generated at 2022-06-13 06:03:38.957949
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    tempfile_mock = flexmock(tempfile)
    tempfile_mock.should_receive('tempfile').and_return(('test_fd', 'test_path'))
    ansible_module_mock = flexmock(AnsibleModule)
    ansible_module_mock.should_receive('get_bin_path').with_args('gpg').and_return("/bin/gpg")
    ansible_module_mock.should_receive('run_command')
    flexmock(os)
    os.should_receive('fdopen').with_args('test_fd').and_return("test_fd_obj")
    ansible_module_mock.should_receive('cleanup')
    rpm_key = RpmKey(ansible_module_mock)
    rpm_

# Generated at 2022-06-13 06:03:49.236016
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import pytest

    @pytest.fixture
    def m(mocker):
        class M(object):
            def __init__(self):
                self.params = {
                    'fingerprint': None
                }
                self.exit_json = True
        return M()

    def getfingerprint(m, keyfile):
        return RpmKey.getfingerprint(m, keyfile)


# Generated at 2022-06-13 06:04:01.085221
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    from ansible.module_utils.six import PY2
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    rp = RpmKey(module)
    if PY2:
        assert isinstance(rp.is_keyid("0x12345678"), bool)
    else:
        assert isinstance(rp.is_keyid("0x12345678"), bool)

# Generated at 2022-06-13 06:04:08.391216
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    rpm_key = RpmKey(module)
    rpm_key.module.check_mode = True
    rpm_key.drop_key("0xDEADBEEF")

# Generated at 2022-06-13 06:04:21.092395
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import os
    import tempfile
    from ansible.module_utils.urls import fetch_url

    class RpmKey:
        pass

    # Test missing key
    rp = RpmKey()
    rp.module = AnsibleModule(argument_spec=dict(key=dict(type='str', required=True, no_log=False)), supports_check_mode=True)
    rp.module.params = dict()
    rp.module.params['key'] = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'
    try:
        RpmKey.fetch_key(rp, 'http://apt.sw.be/RPM-GPG-KEY.dag.txt')
        assert 0
    except SystemExit as e:
        assert e.code == 1

   

# Generated at 2022-06-13 06:04:24.984391
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # given
    class Module(object):

        def __init__(self):
            self.fail_json_called = False

        def fail_json(self, **kwargs):
            self.fail_json_called = True

        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, '', ''

    module = Module()

    rpm_key = RpmKey(module)

    # when
    rpm_key.execute_command(['echo', 'test_RpmKey_execute_command'])

    # then
    assert not module.fail_json_called



# Generated at 2022-06-13 06:04:34.541951
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    r=RpmKey(module)
    keyid = '1 2 3'
    stdout, stderr,rc = r.drop_key(keyid)
    assert(rc==0)
    assert(stdout.split('\n')[0] == 'Preparing packages for installation...')

# Generated at 2022-06-13 06:05:36.502843
# Unit test for constructor of class RpmKey
def test_RpmKey():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    RpmKey(module)

# Generated at 2022-06-13 06:05:44.052672
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    from ansible.module_utils import basic
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils import six
    import os

    RPM_GPG_KEY_DAG = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'

# Generated at 2022-06-13 06:05:57.288405
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import shutil
    import tempfile
    import ansible.module_utils.action
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    tmpfile = tempfile.mkdtemp()


# Generated at 2022-06-13 06:06:08.776014
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    rpm_key = RpmKey(module)
    example_keys = [
        'e3a3f3cd',
        'DEADB33F',
        '0xDEADB33F',
        '0xDEADB33F'
    ]
    for key in example_keys:
        assert rpm_key.is_keyid(key) == True


# Generated at 2022-06-13 06:06:14.868623
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    rm = RpmKey()
    # test case missing parameters
    file = '/path/to/file'
    with pytest.raises(TypeError):
        keyid = rm.getkeyid()
    # test case with parameters
    keyid = rm.getkeyid(file)
    assert keyid is not None



# Generated at 2022-06-13 06:06:22.108941
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    rpm_key = RpmKey(AnsibleModule(argument_spec={}))
    assert rpm_key.normalize_keyid('0XDEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xDEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('DEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid(' DEADB33F  ') == 'DEADB33F'

# Generated at 2022-06-13 06:06:31.176009
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    from ansible.modules.packaging.os.rpm_key import RpmKey
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    test_key = RpmKey(module)
    assert test_key.is_keyid('12345678') == True
    assert test_key.is_keyid('0x12345678') == True
    assert test_key.is_keyid('123456789') == False

# Generated at 2022-06-13 06:06:43.905960
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import tempfile
    import pytest
    import ansible.module_utils.basic
    import ansible.module_utils.urls
    import ansible.module_utils.action
    import ansible.module_utils.six
    import ansible.module_utils._text
    import ansible.module_utils.rpm_key
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils.rpm_key import RpmKey
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_native
    temp_fd, temp_path = tempfile.mkstemp()
    temp_file = os.fdopen(temp_fd, "w+b")

# Generated at 2022-06-13 06:06:51.760260
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    import json
    m_module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    # Mock the rpm and gpg specific commands.
    m_module.get_bin_path = lambda *args, **kwargs: '/bin/rpm'
    m_module.get_bin_path.__name__ = 'get_bin_path'

# Generated at 2022-06-13 06:06:57.216255
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import sys
    import tempfile

    tmpdir = tempfile.mkdtemp()
    my_key = os.path.join(tmpdir, 'my_key')

# Generated at 2022-06-13 06:09:26.705117
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    class Module(object):
        # Return a dict with the argument names required to create an instance of the action plugin
        def argument_spec(self):
            return {}

        # Called after the action plugin has created the instance.
        def __set_module__(self, module):
            pass

        # Check if we can safely return the value for this option in JSON.
        # We can't be sure of the type of the value so we can't do a safe check for simple types.
        # So we just allow for bool and string.
        # This method is defined in the module_utils.basic
        def boolean(self, value):
            return value

        # Check if we can safely return the value for this option in JSON.