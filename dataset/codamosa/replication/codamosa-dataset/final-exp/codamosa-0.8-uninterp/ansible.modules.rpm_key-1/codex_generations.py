

# Generated at 2022-06-13 05:59:52.140040
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    """
    Test method drop_key of class RpmKey
    """
    from mock import Mock, patch, call
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils import rpm_key

    # Construct a mock module object
    module = AnsibleModule(argument_spec={
        'state': {'type': 'str', 'default': 'present', 'choices': ['absent', 'present']},
        'key': {'type': 'str', 'required': True, 'no_log': False},
        'validate_certs': {'type': 'bool', 'default': True}
    },
    supports_check_mode=True)

    # Construct a

# Generated at 2022-06-13 05:59:57.569276
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    expected_res = False
    module = AnsibleModule(argument_spec={'key': '12345678', 'state': 'present'})
    rpm = RpmKey(module)
    assert rpm.is_keyid('12345678') == expected_res, " is_keyid failed"


# Generated at 2022-06-13 06:00:06.227764
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    # This is an extremely simple test that just checks a call to the method
    # without touching any state.
    module = Mock()
    module.check_mode = True
    module.run_command = Mock()
    module.run_command.return_value = 0, "", ""
    rpm_key = RpmKey(module)
    rpm_key.drop_key("keyid")
    args, kwargs = module.run_command.call_args_list[0]
    assert args[0] == ["rpm", "--erase", "--allmatches", "gpg-pubkey-eyid"]

# Generated at 2022-06-13 06:00:07.657564
# Unit test for constructor of class RpmKey
def test_RpmKey():
    assert RpmKey is not None

# Generated at 2022-06-13 06:00:16.299564
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import sys
    import os
    import tempfile

    reload(sys)
    sys.setdefaultencoding('utf8')

    module_args = dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        validate_certs=dict(type='bool', default=True)
    )

    tmp, key_path = tempfile.mkstemp()
    module_args["key"] = key_path
    tmpfile = os.fdopen(tmp, "w+b")
    tmpfile.write('-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v2\n\n')

# Generated at 2022-06-13 06:00:20.348079
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    module = AnsibleModule(argument_spec={},supports_check_mode=True)
    obj = RpmKey(module)

    url = "https://ntp.org/ntp.keys"
    keyfile = obj.fetch_key(url)

    f = open(keyfile,"r")
    key = f.read()
    f.close()

    assert is_pubkey(key)


# Generated at 2022-06-13 06:00:25.931924
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    keyfile = '/path/to/key.gpg'
    mock_object(RpmKey, 'execute_command', return_value=('', ''))
    RpmKey.getkeyid(keyfile)
    cmd = ['gpg', '--no-tty', '--batch', '--with-colons', '--fixed-list-mode', keyfile]
    RpmKey.execute_command.assert_called_with(cmd)

# Generated at 2022-06-13 06:00:36.131831
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    import re
    module = Mock()
    rpm_key = RpmKey(module)
    # case: keyid with 0x is a valid keyid
    keyid1 = "0xdeadbeef"
    assert rpm_key.is_keyid(keyid1)
    # case: keyid in uppercase is a valid keyid
    keyid2 = "DEADBEEF"
    assert rpm_key.is_keyid(keyid2)
    # case: keyid in lowercase is a valid keyid
    keyid3 = "deadbeef"
    assert rpm_key.is_keyid(keyid3)
    # case: keyid is 8 chars long
    keyid4 = "deadbeef"
    assert not rpm_key.is_keyid(keyid4)
    # case: keyid is

# Generated at 2022-06-13 06:00:44.416566
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # First test all the parameters passed to run_command are what we expect

    class mock_module:
        """mock the class used in RpmKey, to control the method run_command"""
        class TestMockArgs:
            """Mock the class needed to mock run_command of class mock_module"""
            def __init__(self):
                self.check_mode = True
                self.stdout_callback = 'default'
                self.run_command = []

            def run_command(self, args, use_unsafe_shell=True):
                self.run_command.append(args)
                return 0, 'test', ''

        def __init__(self):
            self.params = {'foo': 'bar'}
            self.run_command_args = []
            self.args = self.TestMockArgs()



# Generated at 2022-06-13 06:00:54.408267
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.utils.path import which
    with mock.patch('subprocess.Popen') as mock_subprocess_popen:
        mock_subprocess_popen.return_value.communicate.return_value = ('a', 'b')
        mock_subprocess_popen.return_value.wait.return_value = 0
        mock_subprocess_popen.return_value.returncode = 0
        module = mock.MagicMock()
        module.run_command = mock.Mock()
        module.run_command.return_value = (0, 'stdout', 'stderr')
        class TestRpmKey(RpmKey):
            def __init__(self, module):
                self.rpm = 'rpm'
                self.gpg = which('gpg')
        rpm_key = TestRpmKey

# Generated at 2022-06-13 06:01:16.609732
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    module = AnsibleModule(argument_spec={})
    rpmkey =  RpmKey(module)
    keyid = ' 0x1e115612341234123412341234123412341234123'
    assert rpmkey.normalize_keyid(keyid) == '1E115612341234123412341234123412341234123'
    assert rpmkey.normalize_keyid(keyid) != '0x1e115612341234123412341234123412341234123'
    keyid = ' 0X1E115612341234123412341234123412341234123'

# Generated at 2022-06-13 06:01:25.606590
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

    fakeRpmKey = RpmKey(module)
    fakeRpmKey.rpm = "/bin/rpm"
    fakeRpmKey.execute_command = MagicMock(return_value=(None, None))
    fakeRpmKey.drop_key("my key")

# Generated at 2022-06-13 06:01:29.947822
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    rpm_key_obj = RpmKey(None)
    stdout, stderr = rpm_key_obj.execute_command("ls")
    assert stdout.find("rpm_key") > -1


# Generated at 2022-06-13 06:01:40.056579
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    class MagicMockModule(object):
        def __init__(self):
            pass
        def run_command(self, cmd):
            return 0, 'The following keys are unknown:\nE5267286\nE5267287', 'WARNING: 1 keys are not installed'
    class MagicMockClass(RpmKey):
        def __init__(self, module):
            self.module = MagicMockModule()
            self.rpm = 'rpm'
    key = MagicMockClass(None)
    assert key.is_key_imported('E5267287') == False
    assert key.is_key_imported('E5267286') == True
    assert key.is_key_imported('E5267286', cmd = 'gpg') == True

# Generated at 2022-06-13 06:01:44.002914
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module = AnsibleModule(argument_spec={})
    rpm_key = RpmKey(module)
    stdout, stderr = rpm_key.execute_command(rpm_key.rpm)
    assert stdout.startswith('RPM version')
    assert not stderr

# Generated at 2022-06-13 06:01:50.494978
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    """Unit test for method execute_command of class RpmKey"""
    # Test with valid command
    key = 'deadbeef'
    module = mock.Mock()
    module.params = dict(key='deadbeef')
    rpm_key = RpmKey(module)
    rpm_key.rpm = 'rpm'
    rpm_key.execute_command([rpm_key.rpm, '-q', 'gpg-pubkey', '--qf', "%{description}", "gpg-pubkey-%s" % key[-8:].lower()])
    # Test with invalid command

# Generated at 2022-06-13 06:01:51.339482
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    assert False

# Generated at 2022-06-13 06:02:00.016148
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from unit.modules.helper_module_common_test import AnsibleExitJson, AnsibleFailJson

    rpms = os.path.join(os.path.dirname(__file__), 'fixtures', 'rpm_key')

    def execute_command(self, cmd):
        """Mocking method for RpmKey class"""
        if cmd[-1] == '-':
            return to_native(open(os.path.join(rpms, 'gpg_key_colon_output.txt')).read()), ''

# Generated at 2022-06-13 06:02:12.544406
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    """
    Tests fetch_key method
    """
    def mock_run_command(cmd, **kwargs):
        """
        Mocks AnsibleModule's run_command method
        """
        mock_stdout = b'MOCKED_RUN_COMMAND_STDOUT'
        mock_stderr = b'MOCKED_RUN_COMMAND_STDERR'
        mock_rc = 0
        return (mock_rc, mock_stdout, mock_stderr)

    def mock_get_bin_path(binary, required=False):
        """
        Mocks AnsibleModule's get_bin_path method
        """
        mock_bin_path = 'MOCKED_BIN_PATH'
        if binary == 'gpg':
            return mock_bin_path

# Generated at 2022-06-13 06:02:26.079927
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Initialize a mock module
    mock_module = AnsibleModule(argument_spec)
    mock_module.get_bin_path.return_value = True

    # Create a class RpmKey object and initialize it with the mock module
    mock_rpm_key = RpmKey(mock_module)

    # The mocked module will return module.exit_json() when called
    # so here we initialize the correct output to be used
    output = {u'changed': False}

    # Call the fetch_key method with a valid url and with a return code of 200
    # We will mock fetch_url() of the module to return a valid output
    # so we can test if the file downloaded is a gpg public key

# Generated at 2022-06-13 06:02:51.266290
# Unit test for constructor of class RpmKey
def test_RpmKey():
    assert False

# Generated at 2022-06-13 06:03:02.403338
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    from mock import patch
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO
    import sys
    import tempfile
    import os.path
    import shutil

    class DummyModule:
        class DummyModuleFailJson:
            def __init__(self, module_class):
                self.module_class = module_class

            def __call__(self, *args, **kwargs):
                if 'msg' in kwargs:
                    sys.stderr.write(kwargs['msg'])
                self.module_class.fail_json(*args, **kwargs)
        class DummyModuleExitJson:
            def __init__(self, module_class):
                self.module_class = module_class


# Generated at 2022-06-13 06:03:08.494590
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Ensure the fingerprint for EBC6E12C62B1C734026B2122A20E52146B8D79E6 is correct
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rpmkey = RpmKey(module)
    filename = os.path.join(os.path.dirname(__file__), 'RPM-GPG-KEY-dag')
    fingerprint = rpmkey.getfingerprint(filename)
    assert fingerprint == 'EBC6E12C62B1C734026B2122A20E52146B8D79E6'

# Generated at 2022-06-13 06:03:10.285927
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    module = AnsibleModule({
        "argument_spec": {},
        "supports_check_mode": True,
    })
    fixture = RpmKey(module)
    fixture.import_key()
    pass

# Generated at 2022-06-13 06:03:15.447002
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # TODO: Test the constructor of class RpmKey
    # 1. Define all the mocks that are needed by the constructor
    # 2. Define all the constants that are used by the constructor
    # 3. Assert that the constructor of class RPMKey behaves as expected
    pass


# Generated at 2022-06-13 06:03:28.301488
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # Test for present state
    key = "12345'67890ABCDEF"
    params = {'key': key, 'state': 'present', 'fingerprint': "123456789 987654321 0987654321 0123456789"}
    setattr(params['key'], "startswith", lambda x: x == 'http://')
    setattr(params['key'], "endswith", lambda x: True)
    setattr(params['key'], "read", lambda: "")
    setattr(params['key'], "split", lambda x: ['pub:', '', '', '', key, '', '', '', '', '', '', '', '', '', '', '', ''])
    setattr(params['key'], "strip", lambda: "")

# Generated at 2022-06-13 06:03:37.326155
# Unit test for constructor of class RpmKey
def test_RpmKey():

    # Fetch parameters from user
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Create an object
    rpm_key = RpmKey(module)

    # Check if object is created
    if rpm_key:
        return True
    else:
        return False


# Generated at 2022-06-13 06:03:48.073389
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    """Test for method fetch_key of class RpmKey"""
    # Set up mock stuff that's needed to get past AnsibleModule
    class FakeAnsibleModule():
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = lambda x: test_RpmKey_fetch_key_fail_json(x)
            self.check_mode = False
            self.exit_json = lambda x: test_RpmKey_fetch_key_exit_json(x)
            self.add_cleanup_file = lambda x: test_RpmKey_fetch_key_add_cleanup_file(x)
            self.get_bin_path = lambda x: test_RpmKey_fetch_key_get_bin_path(x)


# Generated at 2022-06-13 06:03:55.082353
# Unit test for constructor of class RpmKey
def test_RpmKey():
    input_values = {
        'state': 'absent',
        'key': '0x52674C94',
        'fingerprint': 'deadbeefcafe',
        'validate_certs': True
    }
    module = AnsibleModule(argument_spec=input_values)
    rpm_key = RpmKey(module)
    assert rpm_key



# Generated at 2022-06-13 06:04:06.532193
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule:
        def __init__(self):
            self._cleanup_files = []
            self._url_connection_cache = dict()

        def fail_json(self, msg):
            raise Exception(msg)

        def add_cleanup_file(self, filename):
            self._cleanup_files.append(filename)

        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, "", ""

        def cleanup(self, filename):
            if filename in self._cleanup_files:
                os.unlink(filename)
                self._cleanup_files.remove(filename)


# Generated at 2022-06-13 06:05:11.824173
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    """
    If there are no keys installed in the system
    :return:
    """
    from unittest.mock import Mock
    module = Mock()
    rpmkey = RpmKey(module)
    module.run_command.return_value = (1, 'stdout1', 'stderr1')
    assert False == rpmkey.is_key_imported("keyid")

    """
    If the key is installed in the system
    :return:
    """
    keyid = "54C527DD"
    rpmkey = RpmKey(module)
    module.run_command.return_value = (0, 'stdout2', 'stderr2')

# Generated at 2022-06-13 06:05:18.661466
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    test_module = AnsibleModule(argument_spec={'state': {'type': 'str', 'default': 'present', 'choices': ['absent', 'present']}, 'key': {'type': 'str', 'required': True, 'no_log': False}, 'fingerprint': {'type': 'str'}, 'validate_certs': {'type': 'bool', 'default': True}})
    RpmKey(test_module)


# Generated at 2022-06-13 06:05:30.335932
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    '''
    Due to the fact that the tested method uses os.system to execute a command,
    it was necessary to mock its behavior
    '''
    import mock
    @mock.patch('ansible.module_utils.basic.AnsibleModule.run_command')
    def test(mock_run_command):
        mock_run_command.return_value = (0, "stdout1","stderr1")
        RpmKey.rpm = "rpm"
        RpmKey.gpg = "gpg"
        RpmKey.execute_command(["command"])
        mock_run_command.assert_called_with(["command"], True)

        mock_run_command.return_value = (1, "stdout2","stderr2")

# Generated at 2022-06-13 06:05:38.483379
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():

    def mock_execute_command(cmd):
        return 0, "", ""

    # Set values for mock_is_key_imported and mock_execute_command
    mock_is_key_imported_value = True
    mock_execute_command_value = 0, "", ""

    # Create a mock for class ansible.module_utils.basic.AnsibleModule
    mock_module = ansible_mock.create_autospec(AnsibleModule)
    # Create a mock for class rpm_key.RpmKey
    mock_rpmkey = ansible_mock.create_autospec(RpmKey)
    # Replace method is_key_imported of class rpm_key.RpmKey
    # with mock_is_key_imported
    rpm_key.RpmKey.is_key_imported = mock

# Generated at 2022-06-13 06:05:44.425917
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    sut = RpmKey()

    sut.drop_key('0xDEADBEEF')

    sut.execute_command.assert_called_with(sut.rpm + ' --erase --allmatches gpg-pubkey-deadbeef -')

# Generated at 2022-06-13 06:05:53.353510
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    """Test normalize_keyid function from RpmKey class"""
    from ansible.modules.system.rpm_key import RpmKey
    from ansible.module_utils.six import BytesIO
    test_module = MockModule(argument_spec={})
    rpm_key = RpmKey(test_module)
    # Testing with all variations of a keyid
    keyid = "0xDEADB33F"
    assert(rpm_key.normalize_keyid(keyid) == "DEADB33F")
    keyid = "0XDEADB33F"
    assert(rpm_key.normalize_keyid(keyid) == "DEADB33F")
    keyid = "DEADB33F"

# Generated at 2022-06-13 06:06:00.382540
# Unit test for constructor of class RpmKey
def test_RpmKey():
    class FakeModule():
        class FakeArgs():
            state = 'present'
            key = 'oXMYKEY'
            validate_certs = True
        params = FakeArgs()

        def fail_json(self, msg):
            pass

        def fall_json(self, changed):
            pass

        def run_command(self, cmd, use_unsafe_shell=True):
            pass

        def cleanup(self, tmpfile):
            pass

        def add_cleanup_file(self, tmpname):
            pass

        def get_bin_path(self, bin, required=True):
            return "/usr/bin/rpm"

    key = RpmKey(FakeModule())

# Generated at 2022-06-13 06:06:06.467547
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    rpm_key = RpmKey(None)

    assert rpm_key.normalize_keyid(' 1234ABCD ') == '1234ABCD'
    assert rpm_key.normalize_keyid('0x1234ABCD') == '1234ABCD'
    assert rpm_key.normalize_keyid('0X1234ABCD') == '1234ABCD'
    assert rpm_key.normalize_keyid('0x 1234ABCD') == '1234ABCD'


# Generated at 2022-06-13 06:06:18.221053
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # Build the default options
    import errno
    import os
    import tempfile
    module_args = dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        fingerprint=dict(type='str'),
        validate_certs=dict(type='bool', default=True),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    try:
        os.mkdir('unit_test')
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
    tmpdir = 'unit_test/'
    tmpfd, tmpname = tempfile.mk

# Generated at 2022-06-13 06:06:26.389359
# Unit test for method getkeyid of class RpmKey

# Generated at 2022-06-13 06:08:55.173601
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    path_to_module = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rhn_reg.py')
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.exit_json = Mock()
    RpmKey(module)

# Generated at 2022-06-13 06:09:03.263927
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    # Given:
    import mock
    from ansible.module_utils.ansible_rpm_key import RpmKey
    module = mock.Mock()
    module.check_mode = False
    rp = RpmKey(module)

    # When:
    rp.import_key('keyfile_path')

    # Then
    module.execute_command.assert_called_once_with(['rpm', '--import', 'keyfile_path'])



# Generated at 2022-06-13 06:09:09.971560
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    class RpmKey_MockModule(object):
        def __init__(self):
            self._bin_path = {}

        def get_bin_path(self, bin, required=False):
            if bin in self._bin_path:
                return self._bin_path[bin]
            return None

    class RpmKey_MockRsp(object):
        def __init__(self):
            self._read = None

        def read(self):
            return self._read

    script_path = os.path.dirname(os.path.realpath(__file__))
    key_path = 'file://{0}/key.gpg'.format(script_path)
    urllib2.urlopen = Mock(return_value=RpmKey_MockRsp())

    # 1. Check if file is present

# Generated at 2022-06-13 06:09:16.677505
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
    rp = RpmKey(module)
    assert rp.drop_key("0x12345678") == None


# Generated at 2022-06-13 06:09:26.731176
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    rpm_key = RpmKey(AnsibleModule(argument_spec=dict()))
    command = rpm_key.execute_command
    def test_failure(cmd, error_msg):
        try:
            command(cmd)
            assert False, "Should have raised AssertionError"
        except AssertionError:
            assert str(error_msg) in str(sys.exc_info()[1])
    def test_success(cmd, stdout, stderr):
        temp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        temp_stdout, temp_stderr = temp.communicate()
        assert temp.returncode == 0
        assert stdout == temp_stdout
        assert stderr == temp_stderr
   