

# Generated at 2022-06-13 05:59:44.502047
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    try:
        result = RpmKey.execute_command("/bin/ls -al")
        assert result == True
    except Exception:
        assert False

# Test if is_pubkey returns True

# Generated at 2022-06-13 05:59:53.365190
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.urls import ConnectionError

    op = RpmKey(AnsibleModule(argument_spec={}) )
    op.module.run_command = mock.Mock(return_value=('', '', 0))
    # Test with a key provided on a file
    with open("test/testfiles/key.gpg", "r") as keyfile:
        op.getkeyid(keyfile.name)

# Generated at 2022-06-13 06:00:05.575543
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():

    class MockModule(object):
        def __init__(self):
            self.run_command_results = [
                [0, 'test_output', '']
            ]
            self.run_command_exceptions = [
                False
            ]
            self.run_command_calls = [
                0
            ]
            self.params = {}
            self.fail_json_msg = 'fail_json'
            self.fail_json_exceptions = [False]
            self.fail_json_calls = [0]

        def run_command(self, cmd, use_unsafe_shell=True):
            self.run_command_calls[0] += 1
            if self.run_command_exceptions[0]:
                raise Exception
            return self.run_command_results[0]


# Generated at 2022-06-13 06:00:13.724633
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
    rpm_key.drop_key("DEADBEEF")
    assert(not rpm_key.is_key_imported("DEADBEEF"))


# Generated at 2022-06-13 06:00:24.735414
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    module_args = dict(
        state='absent',
        key='DEADB33F'
    )

    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.params.update(module_args)

    # key deadb33f imported to rpm db
    rpm_key_instance = RpmKey(module)

    # drop key deadb33f
    rpm_key_instance.drop_key(module.params.get('key'))

    # no longer present in rpm db
   

# Generated at 2022-06-13 06:00:30.383222
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    module = AnsibleModule(argument_spec={'state':dict(type='str', default='present', choices=['absent', 'present']),
                                          'key':dict(type='str', required=True, no_log=False),
                                          'validate_certs':dict(type='bool', default=True),
                                             })
    rpm_key = RpmKey(module)
    result = rpm_key.is_key_imported("0xdeadbeef")
    assert result == False

# Generated at 2022-06-13 06:00:40.368471
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    class FakeModule:
        def fail_json(msg):
            assert False, msg

    rpmkey = RpmKey(FakeModule())
    normalized = rpmkey.normalize_keyid("0xDEADB33F")
    assert normalized == "DEADB33F", "Unexpected keyid '%s'" % normalized
    normalized = rpmkey.normalize_keyid("0xDEADB33F ")
    assert normalized == "DEADB33F", "Unexpected keyid '%s'" % normalized
    normalized = rpmkey.normalize_keyid(" 0xDEADB33F")
    assert normalized == "DEADB33F", "Unexpected keyid '%s'" % normalized
    normalized = rpmkey.normalize_keyid(" 0xDEADB33F ")

# Generated at 2022-06-13 06:00:49.889503
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Import keyset
    keyfile = './test/unit/module_utils/ansible_collections/ansible/builtin/rpm_key_test_key.gpg'
    assert is_pubkey(open(keyfile).read())

    # Get fingerprint of key, it's the same value for this key but has newlines
    assert RpmKey(None).getfingerprint(keyfile) == 'D17A 3E1C E4DC 7D66 5A4E  7A8A 6AA2 72DC 3FC3 4A69'



# Generated at 2022-06-13 06:00:57.477871
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    '''rpm_key: test_RpmKey_fetch_key'''
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # ---- Given ----
    # We have a valid pubkey url
    url = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'
    # ---- When ----
    # We call the fetch_key method
    rpm_key_class = RpmKey(module)
    keyfile = rpm_key_class.fetch_key

# Generated at 2022-06-13 06:01:00.001327
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    stdout, stderr = RpmKey.execute_command('gpg')
    assert is_pubkey(stdout)




# Generated at 2022-06-13 06:01:24.895422
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    fake_module = FakeModule()
    fake_module.run_command_value = 1
    fake_module.run_command_stdout = "gpg-pubkey-3e1ba8d2-37e3ff4b"
    fake_module.run_command_stderr = ""
    # Verify a gpg key is not imported
    keyid = '5A5F 37E2 9E8F 1A22 7108  5FFD B949 2A18 3E1B A8D2'
    keyid = keyid.replace(' ', '').upper()
    rpm_key = RpmKey(fake_module)
    assert not rpm_key.is_key_imported(keyid)
    fake_module.run_command_value = 0
    fake_module.run_command_stderr = ""
   

# Generated at 2022-06-13 06:01:36.587262
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    import rpm
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.tests import get_fixture_path
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils.rpm_key import RpmKey

    # Setup
    rpm_key = RpmKey(module)
    if rpm_key.getkeyid(get_fixture_path('test_key.gpg')) is None:
        rpm_key.import_key(get_fixture_path('test_key.gpg'))
    keyid = rpm_key.getkeyid(get_fixture_path('test_key.gpg'))

    # Action
    rpm_key.drop_

# Generated at 2022-06-13 06:01:44.371877
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import os
    import ansible.module_utils
    from ansible.module_utils import basic
    from ansible.module_utils import url as url_utils
    # Test class and functions
    class Test_RpmKey:
        def __init__(self, name):
            self.name = name

    def run_command(self, arg, **kwargs):
        return 'RSA1 123456789', ''

    # Fake variables
    class Mock_AnsibleModule:
        def __init__(self, argument_spec, **kwargs):
            self.argument_spec = argument_spec
            self.params = {'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'}
            self.check_mode = False
            self.run_command = run_command


# Generated at 2022-06-13 06:01:56.411383
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
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
    # Test all conditional branches in execute_command
    # Test all conditional branches in the import_key
    rpm_key.import_key = Mock(return_value=True)
    rpm_key.module.check_mode = False
    rpm_key.execute_command = Mock(return_value=(0, "stdout", "stderr"))

    # call

# Generated at 2022-06-13 06:02:04.751242
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    module = AnsibleModule({"key": "http://apt.sw.be/RPM-GPG-KEY.dag.txt", "validate_certs": True})
    (key, keyid) = RpmKey(module).fetch_key("http://apt.sw.be/RPM-GPG-KEY.dag.txt")
    assert key
    assert keyid == "0x8D81338D52B9C7F4"

# Generated at 2022-06-13 06:02:15.573611
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    class FakeModule(object):
        def __init__(self, cmd_output):
            self.cmd_output = cmd_output
            self.fail_json = lambda **kwargs: None

        def run_command(self, cmd, use_unsafe_shell=True):
            return self.cmd_output

    # Fake successful command
    cmd_output = (0, 'stdout', '')
    fake_module = FakeModule(cmd_output)
    rpm_key = RpmKey(fake_module)
    assert rpm_key.execute_command(['grep', '-v', 'foo']) == ('stdout', '')

    # Fake failing command
    cmd_output = (1, '', 'stderr')
    fake_module = FakeModule(cmd_output)

# Generated at 2022-06-13 06:02:24.224341
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    rk = RpmKey(None)
    rk.rpm = "mock_rpm"
    rk.module = type('obj', (object,), {'check_mode': False, 'run_command': fake_run_command})

    rk.drop_key("12345678")
    assert rk.module.last_run_command == ["mock_rpm", "--erase", "--allmatches", "gpg-pubkey-12345678"]



# Generated at 2022-06-13 06:02:32.305019
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins

    setattr(builtins, "open", lambda x, y: StringIO("fake data"))
    import ansible.modules.packaging.os.rpm_key
    from ansible.modules.packaging.os.rpm_key import RpmKey
    class FakeModule():
        def __init__(self):
            self.params = {}
            self.check_mode = True
            self.run_command_expect_pass = True
            self.run_command_output = [0, "fake output", "fake error"]

        def fail_json(self, msg):
            assert False, msg

        def exit_json(self, changed):
            self.exit_json_called = True

# Generated at 2022-06-13 06:02:37.922326
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    rpm_key = RpmKey
    key_file = "test_data/test.key.txt"

    fp = rpm_key.getfingerprint(key_file)

    assert fp == "EBC6E12C62B1C734026B2122A20E52146B8D79E6"

# Generated at 2022-06-13 06:02:44.892385
# Unit test for function main
def test_main():
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

# Generated at 2022-06-13 06:03:18.069932
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    key = RpmKey(None)
    assert key.is_keyid('0xcafebabe')
    assert key.is_keyid('0xCafeBabe')
    assert key.is_keyid('cafebabe')
    assert key.is_keyid('cafeba')
    assert not key.is_keyid('be')
    assert not key.is_keyid('cafebabebeef')
    assert not key.is_keyid('cafebabexbeef')
    assert not key.is_keyid('deadbeef')
    assert not key.is_keyid('cafebabebeef')


# Generated at 2022-06-13 06:03:29.269052
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile

    tmpfd, tmpname = tempfile.mkstemp()
    tmpfile = os.fdopen(tmpfd, "w")
    expected_keyid = 'B36C6267E46CFB03'

# Generated at 2022-06-13 06:03:38.114513
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class RpmKeyMock(RpmKey):
        def __init__(self):
            self.module = Mock()
            self.module.params = {}
            self.module.params['fingerprint'] = "EBC6 E12C 62B1 C734 026B  2122 A20E 5214 6B8D 79E6"
            self.module.params['key'] = 'foo'
            self.gpg = 'bin/gpg'
            self.rpm = 'bin/rpm'
            self.getkeyid = Mock(return_value='A20E52146B8D79E6')
            self.import_key = Mock()
            self.is_key_imported = Mock(return_value=False)

    class Mock:
        def __init__(self, *args, **kwargs):
            pass

# Generated at 2022-06-13 06:03:48.665021
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import os
    import sys
    import unittest

    class KeyRpmTest(unittest.TestCase):
        results = dict(
            changed=False,
            state="present",
            key="key.gpg",
        )
        results_check = dict(
            changed=True,
            state="present",
            key="key.gpg",
        )

        results_remove = dict(
            changed=True,
            state="absent",
            key="1234ABCD",
        )
        results_remove_check = dict(
            changed=False,
            state="absent",
            key="1234ABCD",
        )

# Generated at 2022-06-13 06:04:01.255455
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    # If a keyid has a leading 0x, it should be stripped out
    module = AnsibleModule(argument_spec={})
    rpm_key = RpmKey(module)
    keyid = rpm_key.normalize_keyid('0xDEADBEEF')
    assert keyid == 'DEADBEEF'

    # It should also work with 0X
    keyid = rpm_key.normalize_keyid('0XDEADBEEF')
    assert keyid == 'DEADBEEF'

    # Whitespace before and after should be stripped out
    keyid = rpm_key.normalize_keyid('   DEADBEEF   ')
    assert keyid == 'DEADBEEF'

    # And the result should be uppercase

# Generated at 2022-06-13 06:04:06.243979
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rpm_key_test = RpmKey(module)
    stdout, stderr = rpm_key_test.execute_command(['/bin/echo', 'foo'])
    assert stdout == 'foo\n'


# Generated at 2022-06-13 06:04:20.642190
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import unittest
    import tempfile

    class TestRpmKey(unittest.TestCase):

        KEY_URL = "https://s3.amazonaws.com/hectoracosta-static-assets/ansible-signing-key.pub"
        KEY_FILE = "ansible-signing-key.pub"

        def setUp(self):
            self.tmpfd, self.tmpname = tempfile.mkstemp()

        def tearDown(self):
            os.unlink(self.tmpname)

        def test_normalize_keyid(self):
            normalize_keyid = RpmKey.normalize_keyid
            self.assertEqual(normalize_keyid("DEADB33F"), "DEADB33F")

# Generated at 2022-06-13 06:04:32.277540
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    class RpmKey():
        def __init__(self, *args, **kwargs):
            pass
        def execute_command(self, cmd):
            return ["ABCD", ""]
        def module_fail_json(self, msg):
            raise Exception(msg)
        def module_add_cleanup_file(self, p):
            pass
    class module():
        def __init__(self, *args, **kwargs):
            pass
        def get_bin_path(self, name, required):
            return "/bin/%s" % name
        def fail_json(self, msg):
            raise Exception(msg)
        def run_command(self, cmd, use_unsafe_shell):
            return (0, "", "")
        def cleanup(self, p):
            pass
    import tempfile
   

# Generated at 2022-06-13 06:04:35.408363
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    keyfile = './test/test_key.gpg'
    rpmkey = RpmKey('present', keyfile, None)
    rpmkey.import_key(keyfile)

# Generated at 2022-06-13 06:04:39.948072
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import mock
    module = mock.Mock(check_mode=False)
    rpm_key = RpmKey(module)
    with mock.patch.object(rpm_key, 'execute_command') as execute_command:
        rpm_key.import_key('keyfile')
        execute_command.assert_called_with([rpm_key.rpm, '--import', 'keyfile'])



# Generated at 2022-06-13 06:05:40.270238
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # First test (with the right parameters)
    # In this test, the key is in the rpm db
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
    assert rpm_key is not None

    # Second test (with the wrong parameters)
    # In this test, the key isn't in the rpm db

# Generated at 2022-06-13 06:05:54.740152
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    test_gpg = "/usr/bin/gpg"
    test_rpm = "/bin/rpm"
    test_pgp_key_id = "DEADBEEF"
    test_module = AnsibleModule(
        argument_spec = dict(
            state = dict(type = "str", default = "present", choices = ["absent", "present"]),
            key = dict(type = "str", required = True, no_log = False),
            fingerprint = dict(type = "str"),
            validate_certs = dict(type= "bool", default = True),
        ),
        supports_check_mode = True,
    )

    # create class object
    test_instance = RpmKey(test_module)

    # set class variables
    test_instance.gpg = test_gpg
    test_instance.rpm

# Generated at 2022-06-13 06:06:03.198241
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    """
    This test verifies if the propser url will be provided
    """
    
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    import os
    import tempfile
    import json
    
    with open('test/unit/modules/ansible_collections/testns/plugins/modules/rpm_key_unittest.json') as json_file:
        data = json.load(json_file)
    
    def run_command_safe(self, cmd, data=None):
        return 'key'
    
    def run_command(self, cmd, data=None, use_unsafe_shell=True):
        return 0, 'gpg_output', 'error_output'
    

# Generated at 2022-06-13 06:06:10.346490
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    expected_id = "8E54A5B5"
    received_id =  RpmKey.normalize_keyid(self, keyid="0x8e54a5b5")
    received_id =  RpmKey.normalize_keyid(self, keyid="0x8E54A5B5")
    received_id =  RpmKey.normalize_keyid(self, keyid="0x8E54A5b5")
    received_id =  RpmKey.normalize_keyid(self, keyid="8E54A5B5")
    received_id =  RpmKey.normalize_keyid(self, keyid="8e54a5b5")

# Generated at 2022-06-13 06:06:22.347510
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # initialize variables
    tempfile.tempdir = '/root/tmp'
    gpg = '/bin/gpg'
    gpg2 = '/bin/gpg2'
    rpm = '/bin/rpm'


    # initialize module
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.get_bin_path = types.MethodType(get_bin_path, module, AnsibleModule)


# Generated at 2022-06-13 06:06:27.691854
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    # Setup
    obj = RpmKey(None)
    keyfile = "./testdata/ubuntu-archive-keyring.gpg"
    expected = "EFE21092"
    # Exercise
    actual = obj.getkeyid(keyfile)
    # Verify
    assert actual == expected, "Expected {0}, Actual {1}".format(expected, actual)


# Generated at 2022-06-13 06:06:34.693408
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    assert RpmKey(module)

# Generated at 2022-06-13 06:06:44.829341
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import os
    import tempfile

    with open(os.path.join(os.path.dirname(__file__), 'test', 'pubkey.test'), 'r') as test_file:
        pubkey = test_file.read()

    tmpfd, tmpname = tempfile.mkstemp()
    with os.fdopen(tmpfd, "w+b") as tmpfile:
        tmpfile.write(pubkey.encode())

    keyid = RpmKey.getkeyid(tmpname)
    assertEqual(keyid, 'EBC6E12C62B1C734026B2122A20E52146B8D79E6')

# Generated at 2022-06-13 06:06:52.522111
# Unit test for constructor of class RpmKey
def test_RpmKey():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
        ),
        supports_check_mode=True,
    )

    # key is file
    try:
        RpmKey(module)
    except:
        assert False

    # key is a keyid
    module.params['key'] = 'deadb33f'
    try:
        RpmKey(module)
    except:
        assert False

    # key is a url
    module.params['key'] = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'

# Generated at 2022-06-13 06:07:03.422822
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    try:
        module = AnsibleModule(
            argument_spec=dict(
                state=dict(type='str', default='present', choices=['absent', 'present']),
                key=dict(type='str', required=True, no_log=False),
                fingerprint=dict(type='str'),
                validate_certs=dict(type='bool', default=True),
            )
        )
        test_RpmKey = RpmKey(module)
        test_RpmKey.fetch_key(url='http://apt.sw.be/RPM-GPG-KEY.dag.txt')
    except:
        print("Failed to export key from %s" % 'http://apt.sw.be/RPM-GPG-KEY.dag.txt')


# Generated at 2022-06-13 06:09:26.240074
# Unit test for constructor of class RpmKey
def test_RpmKey():
    class TestModule:
        def __init__(self):
            self.params = {
                'state': 'present',
                'key': '/path/to/RPM-GPG-KEY.dag.txt',
                'fingerprint': 'EBC6 E12C 62B1 C734 026B  2122 A20E 5214 6B8D 79E6',
            }
            self.check_mode = True

        def cleanup(self):
            pass

        def exit_json(self):
            pass

        def fail_json(self):
            pass

        def get_bin_path(self, cmd, required=False):
            return cmd

        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, 'stdout', 'stderr'
