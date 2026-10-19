

# Generated at 2022-06-13 05:59:49.629249
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


# Retrieve rpm key from Gazzang repo

# Generated at 2022-06-13 06:00:01.839146
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # Create a mock module and mock return values
    #
    # Note that this mocks the action module, not the rpm key module
    #
    # 'ansible' is an import from the global namespace
    #
    # 'ActionModule' is a class from the ansible.module_utils package
    module = MagicMock(spec=ansible.module_utils.action.ActionModule)
    module.run_command = MagicMock(
        return_value=(0, 'stdout', 'stderr')
    )

    # Instantiate the class and check the results
    rpm_key = RpmKey(module)
    stdout, stderr = rpm_key.execute_command(['command', 'args'])

    assert stdout == 'stdout'
    assert stderr == 'stderr'



# Generated at 2022-06-13 06:00:10.745880
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    session = AnsibleModule(argument_spec={})
    test_obj = RpmKey(session)
    assert test_obj.normalize_keyid("0xDEADB33F") == "DEADB33F"
    assert test_obj.normalize_keyid("0XDEADB33F") == "DEADB33F"
    assert test_obj.normalize_keyid("0XDEADB33F ") == "DEADB33F"
    assert test_obj.normalize_keyid(" 0XDEADB33F  ") == "DEADB33F"
    assert test_obj.normalize_keyid(" DEADB33F") == "DEADB33F"
    assert test_obj.normalize_keyid("DEADB33F ") == "DEADB33F"

# Generated at 2022-06-13 06:00:23.121305
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():

    # Case1: Fingerprint of key is found in file.
    # Expected result: Fingerprint as string.
    keyfile = 'tests/unit/modules/ansible_collections/dell/community/plugins/modules/rpm_key.py'
    expected_fingerprint = 'A72B 6C2A 3E0B B1F4 519C E7F4 5EFF 86F6 8659 D9EC'
    rpm_key = RpmKey(None)
    assert rpm_key.getfingerprint(keyfile) == expected_fingerprint

    # Case2: Fingerprint of key is not found in file.
    # Expected result: Error message.
    keyfile = 'tests/unit/files/not_a_key'
    rpm_key = RpmKey(None)
    rpm_key.module.fail_json

# Generated at 2022-06-13 06:00:34.053040
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    import types
    import ansible.modules.packaging.os.yum_key
    import unittest

    # Replace the system time with a known value for testing.
    from ansible.module_utils.six import PY3
    if PY3:
        import unittest.mock as mock
    else:
        import mock

    rpm_key = ansible.modules.packaging.os.yum_key.RpmKey(mock.Mock())

    # Unit test for method is_keyid defined in module ansible.modules.packaging.os.yum_key
    # Check if a key is a valid keyid
    assert type(rpm_key.is_keyid('ABCD1234')) is bool

    # Check if a key is a valid keyid

# Generated at 2022-06-13 06:00:42.869644
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.gpg = 'gpg'
    rpm_key = RpmKey(module)
    assert rpm_key.getfingerprint('test/RPM-GPG-KEY-elrepo.org') == 'D30104A7421F1C806E55BF77BB9A04F9C725A508'

# Generated at 2022-06-13 06:00:53.985371
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    # create an instance of the class
    rpm_key = RpmKey(module)
    # get the keyid
    keyid = rpm_key.normalize_keyid('0xDEADBEEF')
    # call the method
    rpm_key.drop_key(keyid)
    # assert that rpm command has been run
    assert rpm_key.module.run_command.called
    # get the list of arguments passed to the mocked run_command
    rcase, args, kwargs = rpm_key.module.run_command.mock_calls[0]
    # the arguments should have the correct rpm, erase, --allmatches, and
    # gpg-pubkey-<last eight of the keyid> parameters

# Generated at 2022-06-13 06:00:59.429123
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    def mock_run_command(cmd):
        if cmd[0] == 'rpm' and cmd[3] == 'gpg-pubkey' and cmd[1] == '-q':
            return 0, '', ''
        elif cmd[0] == 'rpm' and cmd[2] == '--erase' and cmd[1] == '--allmatches':
            return 0, '', ''

    import mock
    module = mock.MagicMock()
    module.run_command = mock_run_command
    module.check_mode = False
    rpm_key = RpmKey(module)
    rpm_key.drop_key('00AABBCCDDEEFF11')


# Generated at 2022-06-13 06:01:06.584476
# Unit test for method getkeyid of class RpmKey

# Generated at 2022-06-13 06:01:10.544346
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    # Set up mock so that we can test the execute_command method
    module = mock.Mock()
    module.run_command = mock.Mock(return_value=(0, '', ''))
    module.check_mode = False
    self = RpmKey(module)
    # Run import_key method
    self.import_key('keyfile')
    # Assert that the execute_command method was called
    assert module.run_command.call_count > 0

# Generated at 2022-06-13 06:01:36.833130
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    from ansible.module_utils.six import b
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.common.command_cache import CommandCache
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    keyid = b('0xDEADBEEF')
    rpm = RpmKey(module)
    # There are no keys installed

# Generated at 2022-06-13 06:01:42.709052
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    """Test RpmKey.is_key_imported()"""
    os.system("echo 'gpg-pubkey-deadb33f-58d43573' | sudo tee key_gpg_pubkey_deadb33f-58d43573")
    rpk = RpmKey(module)
    assert rpk.is_key_imported("DEADB33F")

# Generated at 2022-06-13 06:01:45.119401
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    keyid = '0x89df2c3bfd3fbe9c'
    assert RpmKey.is_keyid(RpmKey, keyid) == True


# Generated at 2022-06-13 06:01:56.704834
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile
    import os

# Generated at 2022-06-13 06:02:07.187880
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import unittest

    class RpmKeyUnittest(unittest.TestCase):
        def test_method_import_key_with_keyfile_only(self):
            # Arrange
            self.module = Mock()
            self.rpm = 'rpm'
            keyfile = 'keyfile'
            rpm_key = RpmKey(self.module)

            # Act
            rpm_key.import_key(keyfile)

            # Assert
            self.module.run_command.assert_called_with([self.rpm, '--import', keyfile])

    unittest.main()

# Generated at 2022-06-13 06:02:17.248055
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # Patch module.run_command with a mock function
    class module:
        @staticmethod
        def run_command(cmd, **kwargs):
            return 0, '', ''
    RpmKey.module = module
    RpmKey.gpg = '/usr/bin/gpg'
    RpmKey.rpm = '/bin/rpm'
    result = RpmKey.execute_command(['/usr/bin/gpg', '--no-tty', '--batch', '--with-colons',
                                     '--fixed-list-mode', '-', '/path/to/key'],
                                    )
    assert(result == ('', ''))

# Generated at 2022-06-13 06:02:30.026221
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    # Create a temporary file
    import tempfile
    _, tmp_file_path = tempfile.mkstemp()

    # Write contents to temporary file

# Generated at 2022-06-13 06:02:44.091121
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import unittest as ut
    from ansible.module_utils.basic import AnsibleModule
    from test_rpm_key import RpmKey

    class MockModule():
        def __init__(self):
            self.params = { "key" : "foo" }
            self.check_mode = True

        def fail_json(self,msg):
            raise ut.AssertionError(msg)

        def run_command(self,cmd,use_unsafe_shell=True):
            self.last_command_ran = cmd
            return 0, "", ""

        def cleanup(self,keyfile):
            pass

        def get_bin_path(self,bin,required=True):
            return "/usr/bin/{0}".format(bin)


# Generated at 2022-06-13 06:02:48.473980
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    assert RpmKey.is_key_imported('41E7C906') == True
    assert RpmKey.is_key_imported('FAKEKEYID') == False


# Generated at 2022-06-13 06:02:59.591944
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    class Module:
        check_mode = False
        _at_exit = []

        def cleanup(self, *args):
            for arg in args:
                if arg not in self._at_exit:
                    self._at_exit.append(arg)

        def fail_json(self, *args, **kwargs):
            raise Exception('FATAL: %s' % args)

        def run_command(self, args, use_unsafe_shell=False):
            # NOTE: This does not work properly for rpm --import, as it runs gnupg with the system's available tty
            # We need to mock this out, but this is not trivial
            raise Exception('Not a valid test use case')

    class RpmKey:
        def __init__(self, module):
            self.module = module
            self.rpm = None



# Generated at 2022-06-13 06:03:25.835377
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Test if fetch_key returns a file path with a pubkey
    key = "http://apt.sw.be/RPM-GPG-KEY.dag.txt"
    rpmkey = RpmKey(module)
    keyfile = rpmkey.fetch_key(key)
    assert is_pubkey(keyfile)



# Generated at 2022-06-13 06:03:36.445525
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():

    # Set up mock classes
    class ModuleMock(object):
        def __init__(self):
            self.params = {}
            self.check_mode = False
        def fail_json(self, *args, **kwargs):
            raise Exception()
        def run_command(self, cmd, use_unsafe_shell=True):
            if cmd == ['rpm', '-q', 'gpg-pubkey']:
                return 0, 'gpg-pubkey-deadb33f', ''
            elif cmd == ['rpm', '--erase', '--allmatches', 'gpg-pubkey-deadb33f']:
                return 0, '', ''

# Generated at 2022-06-13 06:03:46.577214
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    r = RpmKey(module)
    keyid = 'DEADB33F'
    assert keyid == r.normalize_keyid('0xDEADB33F')
    assert keyid == r.normalize_keyid('0XDEADB33F')
    assert keyid == r.normalize_keyid('DEADB33F')
    assert keyid == r.normalize_keyid('DEADB33F\n')
    assert keyid == r.normalize_keyid(' 0XDEADB33F')
    assert keyid == r.normalize_keyid('0xDEADB33F   ')

# Generated at 2022-06-13 06:03:54.515683
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():

    # Create a mock instance of module to get access to module.params
    module = AnsibleModule(argument_spec={})
    rpmkey = RpmKey(module)

    key_url = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'

    # Create a mock instance of fetch_url to get access to its return values
    fetch_url_mock = Mock(return_value=(b'MOCK', {'status': 200}))

    # Overwrite fetch_url to use our mock
    rpmkey.fetch_url = fetch_url_mock

    # Call the method under test
    keyfile = rpmkey.fetch_key(key_url)
    
    # Verify the method was called once
    assert fetch_url_mock.call_count == 1

    # Verify the method was called

# Generated at 2022-06-13 06:03:55.275605
# Unit test for constructor of class RpmKey
def test_RpmKey():
    assert 1 == 1

# Generated at 2022-06-13 06:04:06.646791
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    keyfile = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 06:04:09.728618
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    assert(RpmKey.getkeyid() == "0x00000000")

# Generated at 2022-06-13 06:04:15.590370
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    key_fingerprint = 'EBC6 E12C 62B1 C734 026B  2122 A20E 5214 6B8D 79E6'
    keyfile = '/home/hector/tmp/RPM-GPG-KEY.dag.txt'
    print(RpmKey.getfingerprint(keyfile))

# Generated at 2022-06-13 06:04:16.829959
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    pass


# Generated at 2022-06-13 06:04:21.384984
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import tempfile

    object = RpmKey(None)

    tmpfd, tmpname = tempfile.mkstemp()
    keyfile = tmpname
    object.execute_command([object.rpm, '--import', keyfile])

    os.remove(keyfile)


# Generated at 2022-06-13 06:05:04.841388
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    """
    Test method getfingerprint of class RpmKey:
    """
    rpm_key_test = RpmKey("test")
    rpm_key_test.gpg = "/usr/bin/gpg"

# Generated at 2022-06-13 06:05:05.940821
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    pass


# Generated at 2022-06-13 06:05:14.303386
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
    rpm = module.get_bin_path('rpm', True)
    rpm_key = RpmKey(module)
    rpm_key.is_key_imported = lambda x: False
    rpm_key.import_key('test')
    module.run_command.assert_called_with((rpm, '--import', 'test'), use_unsafe_shell=True)


# Generated at 2022-06-13 06:05:15.749603
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    assert False



# Generated at 2022-06-13 06:05:23.945125
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    rpm_key = RpmKey(None)

    # Test 1
    assert rpm_key.normalize_keyid('deadbeef') == 'DEADBEEF'

    # Test 2
    assert rpm_key.normalize_keyid('0xdeadbeef') == 'DEADBEEF'

    # Test 3
    assert rpm_key.normalize_keyid('0xDEadbeef') == 'DEADBEEF'

    # Test 4
    assert rpm_key.normalize_keyid('DEADBEEF') == 'DEADBEEF'


# Generated at 2022-06-13 06:05:34.679846
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import io
    import sys
    import unittest

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_listlike

    from ansible_collections.os_migrate.os_migrate.plugins.modules import rpm_key

    mock_RpmKey = rpm_key.RpmKey
    mock_RpmKey.rpm = 'mock_rpm'
    mock_RpmKey.gpg = 'mock_gpg'
    mock_RpmKey.execute_command = 'mock_execute_command'
    mock_RpmKey.is_keyid = 'mock_is_keyid'
    mock_RpmKey.normalize_keyid = 'mock_normalize_keyid'
    mock_RpmKey.getkeyid

# Generated at 2022-06-13 06:05:37.052818
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    rpm_key = RpmKey(None)
    assert rpm_key.drop_key("0") == None


# Generated at 2022-06-13 06:05:44.418794
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}

        @staticmethod
        def run_command(cmd, *args, **kwargs):
            raise NotImplementedError()

        def fail_json(self, msg):
            raise Exception(msg)

    module = MockModule()

    class MockRpmKey(RpmKey):
        def __init__(self):
            super(MockRpmKey, self).__init__(module)

        @staticmethod
        def execute_command(cmd):
            # This function is used to test a command that returns RC=1
            class Result(object):
                def __init__(self, stdout, stderr):
                    self.stdout = stdout.encode()
                    self.stderr = st

# Generated at 2022-06-13 06:05:56.150681
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    class RpmKey:
        def __init__(self, module):
            self.module = module
        def execute_command(self, cmd):
            return None, None
    rpm_key = RpmKey(module)
    rpm_key.import_key("./not_existing_file.txt")

# Generated at 2022-06-13 06:06:07.571985
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
    if not module.get_bin_path('rpm', True):
        # skip rpm tests
        return

    rpmkey = RpmKey(module)
    assert rpmkey.is_keyid('11112222') == True
    assert rpmkey.is_keyid('0x11112222') == True
    assert rpmkey.is_keyid('0x111') == False
    assert rpmkey.is_

# Generated at 2022-06-13 06:07:19.927982
# Unit test for constructor of class RpmKey
def test_RpmKey():

    import os
    import tempfile

    from ansible.module_utils.basic import AnsibleModule


    # TESTS:
    #
    # test_RpmKey_present_gpg_file
    # test_RpmKey_absent_gpg_file
    # test_RpmKey_present_gpg_file_exists
    # test_RpmKey_absent_gpg_file_not_exists
    # test_RpmKey_present_gpg_file_fingerprint_invalid
    # test_RpmKey_present_gpg_file_fingerprint_valid
    # test_RpmKey_present_gpg_file_invalid
    # test_RpmKey_absent_gpg_file_invalid
    # test_RpmKey_present_gpg_url
   

# Generated at 2022-06-13 06:07:32.082597
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    import os.path
    import subprocess

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

    if not os.path.exists(rpm_key.rpm):
        raise Exception("Unable to locate rpm")

    if not os.path.exists(rpm_key.gpg):
        raise Exception("Unable to locate gpg")

    # Test nonzero exit code

# Generated at 2022-06-13 06:07:39.385359
# Unit test for constructor of class RpmKey
def test_RpmKey():
    module = ansible.module_utils.ansible_module_create()
    module.params['key'] = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'
    r = RpmKey(module)
    assert r.keyfile
    assert r.should_cleanup_keyfile
    assert r.keyid
    assert r.normalize_keyid(' 0x00DEADBEEF ') == '00DEADBEEF'

# Generated at 2022-06-13 06:07:48.843231
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    module = AnsibleModule(argument_spec={})
    key_object = RpmKey(module)
    assert key_object.normalize_keyid('0xDEADB33F') == 'DEADB33F'
    assert key_object.normalize_keyid('0XDEADB33F') == 'DEADB33F'
    assert key_object.normalize_keyid('DEADB33F') == 'DEADB33F'
    assert key_object.normalize_keyid('deadb33f') == 'DEADB33F'
    assert key_object.normalize_keyid(' deadb33f') == 'DEADB33F'
    assert key_object.normalize_keyid('deadb33f ') == 'DEADB33F'


# Generated at 2022-06-13 06:07:52.822275
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    manual = RpmKey({
        'argument_spec': {},
        'check_mode': False,
    })
    assert manual.is_keyid("0xC7B131B6") is True
    assert manual.is_keyid("0xC7B131B") is False
    assert manual.is_keyid("C7B131B6") is True

# Generated at 2022-06-13 06:07:57.508198
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    Actual_keyid = 'DEADB33F'
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    obj = RpmKey(module)
    obj.drop_key(Actual_keyid)

# Generated at 2022-06-13 06:08:01.700354
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    # keyid is not imported
    module_mock = Mock(run_command=Mock(side_effect=subprocess.CalledProcessError(1, '', 'No package gpg-pubkey* available.')))
    mod = RpmKey(module_mock)
    assert(not mod.is_key_imported(None))

    # keyid is imported
    module_mock.run_command.side_effect = None
    module_mock.run_command.return_value = (0, '', 'gpg-pubkey-deadb33f-56e81517')
    mod = RpmKey(module_mock)
    assert(mod.is_key_imported(None))


# Generated at 2022-06-13 06:08:10.915403
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Setup
    import os.path
    import tempfile
    import hashlib
    import time
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    tmpfd, tmpname = tempfile.mkstemp()
    module.add_cleanup_file(tmpname)
    tmpfile = os.fdopen(tmpfd, "w+b")

# Generated at 2022-06-13 06:08:22.243845
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils import basic
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils._text import to_native
    import tempfile

    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.check_mode = False
            self.cleanup = []
            self.exit_args = {}
            self.fail_args = {}
            self._debug = []

        def get_bin_path(self, binary, required=False, opt_dirs=[]):
            return 'rpm'


# Generated at 2022-06-13 06:08:35.166744
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Test for fetching a key from a uri
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    rpm_key_object = RpmKey(module)
    tmp_file = rpm_key_object.fetch_key('https://github.com/hectcastro.keys')
    assert os.path.isfile(tmp_file)

    # Test for fetching a key from a uri, with a bad path