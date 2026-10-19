

# Generated at 2022-06-13 05:59:54.541973
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    from builtins import classmethod
    from ansible.module_utils.six import StringIO

    module_args = dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        fingerprint=dict(type='str'),
        validate_certs=dict(type='bool', default=True),
    )

    @classmethod
    def execute_command(cls, cmd):
        pass

    @classmethod
    def fail_json(cls, msg):
        raise Exception(msg)

    @classmethod
    def add_cleanup_file(cls, tmpname):
        pass

    # Mock class

# Generated at 2022-06-13 06:00:03.112183
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    class module_mock:
        def run_command(self, cmd, use_unsafe_shell=True):
            if cmd[0] == 'false':
                return 1, u'', u'stderr'
            else:
                return 0, u'stdout', u''
    assert RpmKey.execute_command(None, ['false']) == (u'', u'stderr')
    assert RpmKey.execute_command(None, ['true']) == (u'stdout', u'')

# Generated at 2022-06-13 06:00:10.159022
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    assert RpmKey.is_keyid("0xDEADB33F")
    assert RpmKey.is_keyid("deadb33f")
    assert RpmKey.is_keyid("deadb33f")
    assert not RpmKey.is_keyid("DEADB33F")
    assert not RpmKey.is_keyid("0x")
    assert not RpmKey.is_keyid("0xDeadBeef")
    assert not RpmKey.is_keyid("deadbeef")
    assert not RpmKey.is_keyid("deadbeef")
    assert not RpmKey.is_keyid("deadbeef")

# Generated at 2022-06-13 06:00:18.419462
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url

    m = AnsibleModule()
    rk = RpmKey(m)

    # Given a keyfile, returns its keyid, the keyid is the last 8 characters of the long form fingerprint
    keyid = rk.getkeyid('test/fixtures/files/RPM-GPG-KEY.dag.txt')
    assert keyid == "79E6B8D6"

    # When the file is a url, it's fetched and its keyid is returned
    keyid = rk.getkeyid('http://apt.sw.be/RPM-GPG-KEY.dag.txt')
    assert keyid == "79E6B8D6"

    # When the url is invalid,

# Generated at 2022-06-13 06:00:27.564658
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Unit tests are a mechanism to ensure that software functions as intended.
    # This is a unit test to ensure that the method getfingerprint of class RpmKey
    # works as intended.
    # In order to do so, we need to import the module, create a mock file and run
    # the method. The mock file contains a valid gpg key, if the method extracts
    # the correct key, the test will pass.
    #
    # Here is the fingerprint of the gpg key: EBC6 E12C 62B1 C734 026B  2122 A20E 5214 6B8D 79E6

    from ansible.module_utils import rpm_key
    myfile = create_mockfile_with_key()
    RpmKey = rpm_key.RpmKey({})

# Generated at 2022-06-13 06:00:33.650134
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    module = type("module", (), {})
    rpm_key = RpmKey(module)
    rpm_key.execute_command = MagicMock(return_value=("Importing keys: done\n", ""))
    rpm_key.import_key("foo.gpg")
    rpm_key.execute_command.assert_called_once_with(["rpm", "--import", "foo.gpg"], use_unsafe_shell=True)


# Generated at 2022-06-13 06:00:34.271118
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    pass

# Generated at 2022-06-13 06:00:41.883355
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    test_object = RpmKey(None)

    assert test_object.normalize_keyid('0xDEADBEEF') == 'DEADBEEF'
    assert test_object.normalize_keyid('0XDEADBEEF') == 'DEADBEEF'
    assert test_object.normalize_keyid('DEADBEEF') == 'DEADBEEF'
    assert test_object.normalize_keyid('DEADBEEF   ') == 'DEADBEEF'
    assert test_object.normalize_keyid('DEADBEEF\n') == 'DEADBEEF'


# Generated at 2022-06-13 06:00:51.426308
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():

    assert_equal(RpmKey.normalize_keyid(' 0x DEADB33F'), 'DEADB33F')
    assert_equal(RpmKey.normalize_keyid(' DEADB33F '), 'DEADB33F')
    assert_equal(RpmKey.normalize_keyid('DEADB33F'), 'DEADB33F')
    assert_equal(RpmKey.normalize_keyid('0X DEADB33F'), 'DEADB33F')
    assert_equal(RpmKey.normalize_keyid('0xDEADB33F'), 'DEADB33F')

# Generated at 2022-06-13 06:00:58.336078
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import unittest
    class TestRpmKey(unittest.TestCase):
        def setUp(self):
            self.fd, self.filename = tempfile.mkstemp(text=True)
            self.fname = os.fdopen(self.fd, "w+")

# Generated at 2022-06-13 06:01:22.660844
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import os
    import sys
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_text
    sys.path.append("/usr/lib/python2.7")
    # import unit test class, run test in terminal
    test_instance = RpmKey(AnsibleModule(dict(
        key='http://apt.sw.be/RPM-GPG-KEY.dag.txt',
        state='present' ,
        validate_certs=True
    )) )
    assert test_instance.fetch_key('http://apt.sw.be/RPM-GPG-KEY.dag.txt')
    # test_instance.fetch_key(to_text(rsp))


# Generated at 2022-06-13 06:01:33.188443
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
    key_obj=RpmKey(module)
    key_obj.module.check_mode=False
    key_obj.rpm='echo'
    key_obj.gpg='echo'
    key_obj.import_key("/tmp/abc")


# Generated at 2022-06-13 06:01:41.521220
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import os

    tmpfd, tmpname = tempfile.mkstemp()
    os.write(tmpfd, "test".encode("utf-8"))
    os.close(tmpfd)

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params = {'key': tmpname, 'state': 'present'}
    module.run_command = FakeRunCommand()
    RpmKey(module)
    assert os.path.exists(tmpname) is False
    os.remove(tmpname)



# Generated at 2022-06-13 06:01:45.846941
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    rpm_key = RpmKey(module)

    stdout, stderr = rpm_key.execute_command(['echo', 'foo'])

    assert stdout == 'foo\n'
    assert stderr == ''

# Generated at 2022-06-13 06:01:57.462024
# Unit test for constructor of class RpmKey
def test_RpmKey():
    """Class constructor testing"""
    import inspect
    import os
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    # Mock variables and functions
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    def mock_fail_json(self, msg):
        self.msg = msg


# Generated at 2022-06-13 06:02:10.618049
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Arrange
    class MockModule:
        def __init__(self, *args, **kwargs):
            self.url = 'https://secure.python.org/static/files/gpg-key-D88E42B4.txt'
            self.key = 'D88E42B4'
            self.fingerprint = '6AF9 7BA1 2D3E A5B5  40B0 C5E5 09FA EFBE D88E 42B4'
            self.debug = False

        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/gpg2'

        def add_cleanup_file(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 06:02:23.681565
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule, AnsibleModuleError

    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    keyfile = tempfile.NamedTemporaryFile(prefix='test_RpmKey_getkeyid')

# Generated at 2022-06-13 06:02:31.888586
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    class FakeModule(object):
        def __init__(self, params=None):
            if params is None:
                params = {
                    'state': 'present',
                    'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt',
                    'fingerprint': '',
                }

            self.params = params

            self.params = params

        def fail_json(self, msg=None):
            if msg:
                raise AssertionError(msg)

        def run_command(self, cmd, use_unsafe_shell=True):
            # We do not care if this command is indeed run.  What we
            # care about is if the command was run with the expected
            # arguments.

            if cmd != ['rpm', '--import', '/tmp/testfile']:
                raise Ass

# Generated at 2022-06-13 06:02:44.835587
# Unit test for constructor of class RpmKey
def test_RpmKey():
    mock_module = AnsibleModule(
      argument_spec=dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        fingerprint=dict(type='str'),
        validate_certs=dict(type='bool', default=True),
      ),
      supports_check_mode=True
    )

    # Tests is_keyid method
    rpm_key = RpmKey(mock_module)
    assert rpm_key.is_keyid('0xDEADB33F') == True
    assert rpm_key.is_keyid('DEADB33F') == True
    assert rpm_key.is_keyid('DEADB33F0') == False

    # Tests normalize_keyid

# Generated at 2022-06-13 06:02:56.757698
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    import ansible.modules.packaging.os.rpm_key
    import ansible.module_utils.basic

    class FakeModule(ansible.module_utils.basic.AnsibleModule):
        def __init__(self):
            self.argument_spec = ansible.modules.packaging.os.rpm_key.RpmKey._ARGS
            self.params = {}
            self.check_mode = False
            self.run_command = RpmKey_execute_command_hijack

    def RpmKey_execute_command_hijack(self, cmd):
        return '', ''

    module = FakeModule()
    r = ansible.modules.packaging.os.rpm_key.RpmKey(module)
    r.execute_command('fake cmd')

# Generated at 2022-06-13 06:03:31.742452
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
    rpmkey_obj = RpmKey(module)
    assert rpmkey_obj.is_keyid('0xEA3E3B6B') == True
    assert rpmkey_obj.is_keyid('EA3E3B6B') == True
    assert rpmkey_obj.is_keyid('0XEA3E3B6B') == True
    assert rpmkey_obj.is_key

# Generated at 2022-06-13 06:03:33.306566
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    #  TODO: Implement me!
    return False

# Generated at 2022-06-13 06:03:34.847688
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    assert RpmKey.execute_command(RpmKey, ['hostname']) == ('hostname')


# Generated at 2022-06-13 06:03:38.306936
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    a = RpmKey("")
    assert a.normalize_keyid("   0xDEADB33F0D    ") == "DEADB33F0D"


# Generated at 2022-06-13 06:03:39.713014
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    """Unit test for method fetch_key of class RpmKey."""
    pass

# Generated at 2022-06-13 06:03:44.967330
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # This file was obtained from https://debian.org/CD/torrent-cd/
    # and contains a 2048 bit key.
    keyfile = "/tmp/test_RpmKey_getfingerprint.asc"


# Generated at 2022-06-13 06:03:53.888761
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():

    import os
    import shutil

    tmpdir = os.path.realpath(os.path.dirname(__file__) + '/../../' + 'test-keyring')
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)

    os.makedirs(tmpdir)
    os.environ['HOME'] = tmpdir
    os.environ['RPM_HOME'] = tmpdir
    os.environ['RPM_GPG_DIR'] = tmpdir
    os.environ['GNUPGHOME'] = tmpdir

    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:04:04.762324
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    if __name__ == '__main__':
        class AnsibleModule:
            #Data to be used by AnsibleModule methods

            def __init__(self, argument_spec=None, supports_check_mode=False):
                self.argument_spec = argument_spec
                self.supports_check_mode = supports_check_mode

            def run_command(self, cmd, use_unsafe_shell=True):
                return 0, '68B0 1662 F7AD B31A  908A  93A1 2536 F9E0 D3A5 6A2C', ''

            def exit_json(self, changed=True):
                raise Exception("exit_json")


# Generated at 2022-06-13 06:04:11.553014
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    # Create mock of module
    module = AnsibleModule(
        argument_spec={}
    )
    module.check_for_missing_params.return_value = False
    module.command_basename.return_value = '/usr/bin/rpm'

    # Create instance of class RpmKey
    rpmkey = RpmKey(module)

    # open a file, used to mock the function open
    keyfile = open(tkinter.__file__, 'r')

    # mock the attribute rpmkey.gpg
    rpmkey.gpg = 'gpg2'

    # mock the response of the function os.path.isfile

# Generated at 2022-06-13 06:04:23.307219
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import os

    with open(os.path.join(os.path.dirname(__file__), 'files', 'test_key.txt'), 'r') as f:
        test_key = f.read()

    rk = RpmKey(None)
    keyfile = rk.fetch_key('https://fedoraproject.org/static/0608B895.txt')
    assert rk.getfingerprint(keyfile) == '6706 B086 169D 8672 A7F6  EE05 8BA2 F1E2 0608 B895'

    keyfile = rk.fetch_key('file://' + keyfile)

# Generated at 2022-06-13 06:05:31.931680
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    class MockModule:
        def __init__(self):
            self.params = {
                'state': 'present',
                'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt',
                'fingerprint': '',
                'validate_certs': True,
            }

            self.path_exists_map = {
                '/usr/bin/rpm': True,
                '/usr/bin/gpg': True,
                '/usr/bin/gpg2': False,
            }

        def get_bin_path(self, arg, required=False):
            return self.path_exists_map[arg]

    class MockFetchUrl:
        def __init__(self):
            self.read_content = ''

# Generated at 2022-06-13 06:05:41.936707
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    print("Running test_RpmKey_getfingerprint")
    import tempfile
    keyfile = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 06:05:42.843324
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    pass

# Generated at 2022-06-13 06:05:49.153637
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    rpm = RpmKey(module)
    # create a class
    rpm = RpmKey(module)

    def execute_command(self, cmd):
        if cmd[0] == '':
            self.module.fail_json(msg="Unexpected fail.")
    rpm.execute_command = execute_command.__get__(rpm)


# Generated at 2022-06-13 06:05:59.009335
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Create a new module
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    # Create a new object from the class RpmKey
    rpmkey = RpmKey(module)
    # Get the temporary file path of a gpg key
    tmpname = rpmkey.fetch_key('https://bintray.com/user/rpm/rpm/gpg')
    # Open file for reading
    tmpfile = open(tmpname, 'r+')
   

# Generated at 2022-06-13 06:06:09.941653
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import tempfile
    import os.path
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    rpm = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Create test files
    tmpfd, tmp_gpg_file = tempfile.mkstemp()
    rpm.add_cleanup_file(tmp_gpg_file)
    tmpfile = os.fdopen(tmpfd, "w+b")

# Generated at 2022-06-13 06:06:21.984465
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import os
    import tempfile
    
    class MockModule(object):
        @staticmethod
        def fail_json(msg):
            raise RuntimeError(msg)
        @staticmethod
        def add_cleanup_file(tmpname):
            return tmpname

    class MockFetchUrl(object):
        def __init__(self, module, url):
            pass


# Generated at 2022-06-13 06:06:30.906876
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    rpmkey = RpmKey()
    # Test a missing file
    ret = rpmkey.getfingerprint('/tmp/doesnotexist')
    assert ret is None

    # Test a valid key
    ret = rpmkey.getfingerprint('/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7')
    assert ret == 'EBC6E12C62B1C734'

    # Test a valid key without spaces
    ret = rpmkey.getfingerprint('/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7', False)
    assert ret == 'EBC6E12C62B1C734A026B2122A20E52146B8D79E6'


# Generated at 2022-06-13 06:06:43.230347
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
    gpg = module.get_bin_path('gpg', required=True)
    rpm = module.get_bin_path('rpm', required=True)
    key = RpmKey(module)
    key.gpg = gpg
    key.rpm = rpm
    keyfile = module.get_bin_path('pgpUtilTest.key', required=False)

# Generated at 2022-06-13 06:06:46.446882
# Unit test for function main
def test_main():
    assert is_pubkey("-----BEGIN PGP PUBLIC KEY BLOCK----- BEGIN PGP SIGNATURE ----")
    assert is_pubkey("-----BEGIN PGP PUBLIC KEY BLOCK----- ÁÑÇ ----")
    assert not is_pubkey("x-----BEGIN PGP PUBLIC KEY BLOCK----- BEGIN PGP SIGNATURE ----")

# Generated at 2022-06-13 06:09:16.109431
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

# Generated at 2022-06-13 06:09:26.715201
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    class Args:
        def __init__(self):
            self.key = 'tests/RPM-GPG-KEY-dag'
            self.fingerprint = None
            self.validate_certs = True
            self.state = 'present'

    args = Args()

    class Module:
        def __init__(self):
            self.params = args
            self.check_mode = False
            self.fail_json = None

        def get_bin_path(self, app, required=False):
            if app == 'rpm':
                return '/usr/bin/rpm'
            if app == 'gpg2':
                return '/usr/bin/gpg2'
            raise Exception('app not found in test')