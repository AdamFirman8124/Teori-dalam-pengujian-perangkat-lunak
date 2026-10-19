

# Generated at 2022-06-13 05:59:50.892452
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import os
    import tempfile
    import unittest
    test_tmpfile_path = '{}/{}'.format(tempfile.gettempdir(), 'tempfile')

# Generated at 2022-06-13 06:00:04.251382
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    import sys
    sys.stderr.write("Test of RpmKey_execute_command()\n")
    sys.stderr.flush()

    # Initialize the fake module
    module = ""

    # Call execute_command of RpmKey with a simple command
    sys.stderr.write("RpmKey_execute_command with a simple command.\n")
    sys.stderr.flush()
    RpkKey = RpmKey(module)
    cmd = ['date']
    stdout, stderr = RpkKey.execute_command(cmd)
    assert stdout != ""

    # Call execute_command of RpmKey with a command that does not exist
    sys.stderr.write("RpmKey_execute_command with a command that does not exist.\n")
    sys.stderr

# Generated at 2022-06-13 06:00:09.294954
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():

    rpm_key = RpmKey(module)

    key = rpm_key.fetch_key('http://apt.sw.be/RPM-GPG-KEY.dag.txt')

    assert is_pubkey(key)

# Generated at 2022-06-13 06:00:17.600449
# Unit test for method is_keyid of class RpmKey

# Generated at 2022-06-13 06:00:25.372793
# Unit test for constructor of class RpmKey
def test_RpmKey():
    test_module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    assert test_module
    assert test_module.check_mode
    assert test_module.run_command
    assert test_module.run_command([])

# Unit tests for methods is_key_imported and is_keyid of class RpmKey

# Generated at 2022-06-13 06:00:35.732861
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # This code will be executed only in unit tests

    # Initialize the module object
    rpm_module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Create the class object
    rpm_module.RpmKey(rpm_module)

    # Get the getfingerprint method
    getfingerprint = rpm_module.RpmKey.getfingerprint

    # Build the test input

# Generated at 2022-06-13 06:00:48.096263
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # Here we create a FakeModule to test the class
    class FakeModule:
        def __init__(self):
            self.fail_json_called = False
            self.params = {
                "fingerprint": None,
                "key": "",
                "state": "present"
            }

        def fail_json(self, msg=""):
            self.fail_json_called = True

        def get_bin_path(self, cmd, required=False):
            if cmd == "rpm":
                return "/usr/bin/rpm"
            elif cmd == "gpg":
                return "/usr/bin/gpg"
            elif cmd == "gpg2":
                return None
            elif required:
                self.fail_json("Failed to find required executable: %s" % cmd)
            else:
                return

# Generated at 2022-06-13 06:00:56.771696
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    import tempfile
    import os.path
    import random
    import random
    import string

    # Generate a random eight characters string
    def generate_random_string():
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

    # Generate a valid gpg key with a given keyid
    def generate_key(keyid):
        # Check the format of the keyid
        if not re.match('(0x)?[0-9a-f]{8}', keyid, re.IGNORECASE):
            raise RuntimeError("Keyid '%s' is not a valid keyid" % keyid)

        keyid = keyid.strip().upper()

        # Starting point of the key

# Generated at 2022-06-13 06:01:05.219814
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    class MockModule(object):
        def __init__(self):
            self.fail_json = lambda a: self

    class MockOs(object):
        @staticmethod
        def fdopen(fd, mode):
            return TestRpmKey.fake_tmpfile
        @staticmethod
        def close(fd):
            pass

    class MockGpg(object):
        @staticmethod
        def get_bin_path(bin, required=False):
            return '/usr/bin/gpg'

    class MockFetchUrl(object):
        @staticmethod
        def fetch_url(module, url):
            return '', {"status": 200, "msg": "OK"}

    class MockTempfile(object):
        @staticmethod
        def mkstemp():
            return 12345, "/tmp/tmpfile"


# Generated at 2022-06-13 06:01:11.670277
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    assert RpmKey(None).is_keyid('deadbeef')
    assert RpmKey(None).is_keyid('0xdeadbeef')
    assert RpmKey(None).is_keyid('0x0xdeadbeef')
    assert RpmKey(None).is_keyid('deadbeefdeadbeef')
    assert not RpmKey(None).is_keyid('deadbeefdeadbee')
    assert not RpmKey(None).is_keyid('deadbeefdeadbeefdeadbeef')
    assert not RpmKey(None).is_keyid('deadbeefx')
    assert not RpmKey(None).is_keyid('deadbeef ')
    assert not RpmKey(None).is_keyid('deadbeef.asc')
    assert not RpmKey(None).is_

# Generated at 2022-06-13 06:01:32.406608
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO
    module = AnsibleModule({})
    obj = RpmKey(module)
    obj.rpm = "/usr/bin/rpm"
    obj.gpg = "/usr/bin/gpg"
    obj.module.run_command = lambda cmd, use_unsafe_shell=True: (
        0,
        StringIO('foo'),
        ''
    )
    assert obj.execute_command([obj.rpm, '--version']) == ('foo', '')

# Generated at 2022-06-13 06:01:38.070849
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Test for an invalid url
    fake_module = DummyModule('not a real url')
    with pytest.raises(AnsibleFailJson) as e:
        RpmKey(fake_module)
    assert 'msg' in e.value.args[0]
    assert 'failed to fetch key at not a real url' in e.value.args[0]['msg']


# Generated at 2022-06-13 06:01:47.790289
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Create a new tempfile
    tmpfd, tmpname = tempfile.mkstemp()
    os.close(tmpfd)

    # Create the gpg key file
    with open(tmpname, 'w') as f:
        f.write('-----BEGIN PGP PUBLIC KEY BLOCK-----\n')
        f.write('Version: GnuPG v1\n')
        f.write('\n')
        f.write('mQENBFQxzNgBCAC6kKjSKN0T+TcEUzpWExR8C+YuhVeoYf3vP4xI4ekyA4z1Fjb4\n')

# Generated at 2022-06-13 06:01:58.646996
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    rpm_key = RpmKey(None)
    rpm_key.gpg = '/bin/gpg'


# Generated at 2022-06-13 06:02:10.140354
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

    rpm_key = RpmKey(module)
    keyfile = "test/data/dag.pub"
    assert rpm_key.getfingerprint(keyfile) == "EB6E1C62B1C734026B21222A20E52146B8D79E6"

# Generated at 2022-06-13 06:02:16.327966
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    class_object = RpmKey(module)
    assert class_object.getkeyid("/Users/manusajith/ansible.pub") == "0BD3C0E3C78AD2B8"
    return "Pass"



# Generated at 2022-06-13 06:02:26.222619
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, "", "")
    module_mock.check_mode = False
    rpm_key = RpmKey(module_mock)
    rpm_key.rpm = "fake_rpm"
    rpm_key.drop_key("ABCD1234")
    module_mock.run_command.assert_called_once_with(["fake_rpm", "--erase", "--allmatches", "gpg-pubkey-1234"], True)


# Generated at 2022-06-13 06:02:34.072569
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

    # Set proper key to check
    subject = 'gpg-pubkey-deadb33f'

    # Check that proper command is called
    rpm_key.module.run_command = MagicMock(return_value=(0, subject, ''))

    # Call method to test
    ret = rpm_key.drop_key('DEADB33F')



# Generated at 2022-06-13 06:02:46.411540
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():

    # expected output
    import_key_out = 'gpg: key DEADB33F: "Zabbix Monitoring Tool <packager@zabbix.com>" imported\n'
    # expected error
    import_key_err = ''

    # mock the module
    mock_module = AnsibleModule(argument_spec=dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        validate_certs=dict(type='bool', default=True)
    ))

    # mock the object
    rpm_key_object = RpmKey(mock_module)

    # mock the RPM script
    rpm_script = 'script/rpm_key.py'

    # mock the key file
    key_file

# Generated at 2022-06-13 06:02:55.142802
# Unit test for constructor of class RpmKey
def test_RpmKey():
    test = RpmKey(AnsibleModule({
        'argument_spec': dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        'supports_check_mode': True,
    }))
    assert test.module is not None
    assert test.rpm is not None
    assert test.gpg is not None

# Generated at 2022-06-13 06:03:30.637535
# Unit test for method getfingerprint of class RpmKey

# Generated at 2022-06-13 06:03:36.559443
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    keyid = 'deadb33f'
    rpm_key = RpmKey(None)
    assert rpm_key.normalize_keyid(keyid) == keyid.upper()
    assert rpm_key.normalize_keyid('0x' + keyid) == keyid.upper()
    keyid = rpm_key.normalize_keyid('    0x    ' + keyid)
    assert keyid == keyid.upper()
    assert len(keyid) == 8


# Generated at 2022-06-13 06:03:47.662515
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    import tempfile
    def is_key_imported(module, keyid):
        cmd = module.get_bin_path('rpm') + ' -q  gpg-pubkey'
        rc, stdout, stderr = module.run_command(cmd)
        if rc != 0:  # No key is installed on system
            return False
        cmd += ' --qf "%{description}" | ' + module.get_bin_path('gpg') + ' --no-tty --batch --with-colons --fixed-list-mode -'
        stdout, stderr = module.execute_command(cmd)
        for line in stdout.splitlines():
            if keyid in line.split(':')[4]:
                return True
        return False

# Generated at 2022-06-13 06:03:55.088786
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    """
    Assert that the key is imported correctly when state='present'
    """
    import os
    import tempfile

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
            'state': dict(default='present', type='str', choices=['absent', 'present']),
            'key': dict(required=True, type='str'),
            'fingerprint': dict(type='str'),
            'validate_certs': dict(type='bool', default=True),
        },
        supports_check_mode=True,
    )

    tmpfd, tmpname = tempfile.mkstemp()
    with os.fdopen(tmpfd, 'w') as tmpfile:
        tmpfile.write('foobar')

# Generated at 2022-06-13 06:03:59.693957
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    m = AnsibleModule(
        argument_spec=dict(
            key=dict(type='str', required=True, no_log=False)
        ),
        supports_check_mode=True
    )
    RpmKey.fetch_key(m, "http://www.apache.org/dist/ant/KEYS")

# Generated at 2022-06-13 06:04:09.256911
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    key = '0xDEADBEEF'
    mock_module = MockModule(key=key)
    rpm_key = RpmKey(mock_module)
    file_name = 'test_RpmKey_getfingerprint'
    file_text = 'This is a test\n'
    file_path = os.path.join(tempfile.mkdtemp(), file_name)
    with open(file_path, 'w') as f:
        f.write(file_text)

    mock_module.add_cleanup_file(file_path)
    mock_module.run_command.return_value = 0, 'fpr:0xDEADBEEF', ''
    result = rpm_key.getfingerprint(file_path)
    assert result == '0xDEADBEEF'

# Generated at 2022-06-13 06:04:15.654733
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import mock
    m = mock.Mock()
    m.params.return_value = {'state': 'present', 'key': '0x11111111'}
    m.check_mode.return_value = True
    m.fail_json.return_value = True
    m.exit_json.return_value = True
    rpm = RpmKey(m)
    return rpm

# Generated at 2022-06-13 06:04:22.751844
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    import ansible.module_utils.action_plugins.rpm_key as rpm_key
    import ansible.module_utils.basic as basic
    import ansible.module_utils.urls as urls

    class MockAnsibleModule:
        def __init__(self, argument_spec, check_invalid_arguments=None, bypass_checks=False):
            self.argument_spec = argument_spec
            self.check_invalid_arguments = check_invalid_arguments
            self.bypass_checks = bypass_checks
            self.params = dict()

    class MockActionBase:
        def __init__(self, add_cleanup_file):
            self.add_cleanup_file = add_cleanup_file


# Generated at 2022-06-13 06:04:29.121222
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    rpm = RpmKey(None)
    tests = [
        ('key1.gpg', '6B8D79E6'),
        ('key2.gpg', 'DE0A091E'),
        ('key3.gpg', None),
    ]
    for keyfile, fingerprint in tests:
        keyid = rpm.getkeyid(keyfile)
        assert keyid == fingerprint


# Generated at 2022-06-13 06:04:37.559089
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
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

# Generated at 2022-06-13 06:05:38.435923
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    module = None
    rp = RpmKey(module)
    assert rp.normalize_keyid("DEADB33F") == "DEADB33F"
    assert rp.normalize_keyid(" 0xDEADB33F ") == "DEADB33F"
    assert rp.normalize_keyid(" 0XDEADB33F ") == "DEADB33F"
    assert rp.normalize_keyid("0xDEADB33F") == "DEADB33F"
    assert rp.normalize_keyid("0XDEADB33F") == "DEADB33F"


# Generated at 2022-06-13 06:05:44.889516
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
  r_test_RpmKey_import_key = RpmKey(
    False,
    ['rpm', '--import', '/path/to/key.gpg'],
    {},
    [],
    [],
    0,
    )
  return r_test_RpmKey_import_key

# Generated at 2022-06-13 06:05:46.217404
# Unit test for constructor of class RpmKey
def test_RpmKey():
    assert RpmKey() == "RpmKey()"

# Generated at 2022-06-13 06:05:58.079362
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile
    from ansible.module_utils.common._collections_compat import Mapping

    # Create a temp file.

# Generated at 2022-06-13 06:06:06.418964
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    key_path = 'test_key.txt'
    assert is_pubkey(open(key_path).read())
    keyid = RpmKey.getkeyid(key_path)
    assert RpmKey.is_keyid(keyid)
    key_rpm = RpmKey(None) # initialize with a None module so we can test
    key_rpm.import_key(key_path)
    assert key_rpm.is_key_imported(keyid)
    key_rpm.drop_key(keyid)


# Generated at 2022-06-13 06:06:18.172452
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    class MockModule(object):
        def fail_json(self, msg):
            pass
        def cleanup(self, path):
            pass
        def add_cleanup_file(self, path):
            pass
    class MockFetchUrl(object):
        def __init__(self, is_pubkey=True, status=200):
            self.is_pubkey = is_pubkey
            self.status = status
        def read(self):
            return 'fake pubkey' if self.is_pubkey else 'fake not pubkey'
    mock_module = MockModule()
    mock_module.fetch_url = lambda module, url: (MockFetchUrl(), {'status': 200})
    RpmKey(mock_module)

# Generated at 2022-06-13 06:06:26.352546
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils.ansible_modlib.ansible_module_mock import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    # Arguments provided in constructor
    state = module.params['state']
    key = module.params['key']
    fingerprint = module.params['fingerprint']
    rpKey = RpmKey(module)
    assert rpKey.module== module
    assert rpKey.fingerprint

# Generated at 2022-06-13 06:06:30.893580
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    class Module:

        def fail_json(self, msg):
            pass

    rpm = RpmKey(Module())
    assert rpm.normalize_keyid('EBC6E12C62B1C734026B2122A20E52146B8D79E6') == 'EBC6E12C62B1C734026B2122A20E52146B8D79E6'
    assert rpm.normalize_keyid('  \n  EBC6E12C62B1C734026B2122A20E52146B8D79E6') == 'EBC6E12C62B1C734026B2122A20E52146B8D79E6'

# Generated at 2022-06-13 06:06:41.301191
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    import re
    a = RpmKey(None)
    assert a.normalize_keyid(" DEADB33F ") == "DEADB33F"
    assert a.normalize_keyid("0xDEADB33F") == "DEADB33F"
    assert a.normalize_keyid("0XDEADB33F") == "DEADB33F"
    assert a.normalize_keyid("0x deadb33f ") == "DEADB33F"
    assert a.normalize_keyid("0x deadb33f \n") == "DEADB33F"


# Generated at 2022-06-13 06:06:46.325701
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    class dummy:
        def __init__(self, file):
            self.file = file
            self.gpg = 'gpg'

        def get_bin_path(self, path, required=False):
            if path == 'gpg' or path == 'gpg2':
                return self.gpg

    def e_c(cmd):
        if self.module.gpg == 'gpg':
            keyid = 'FF8104C87E86F7F193382DD6BB7CE2EE62E621F0'
        if self.module.gpg == 'gpg2':
            keyid = '62E621F0FF8104C87E86F7F193382DD6BB7CE2EE'
        return keyid.encode('utf-8'), b''


# Generated at 2022-06-13 06:09:08.970423
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import unittest
    from ansible.module_utils import basic
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils._text import to_native
    import os
    import tempfile
    import re
    import warnings

    class MockModule():
        def __init__(self):
            self.params = None
            self.check_mode = False
            self.run_command_results = []
            self.run_command_calls = []
            self.add_cleanup_file_files = []

        def get_bin_path(self, arg, required=True):
            if arg == 'gpg':
                return '/usr/bin/gpg'
            elif arg == 'gpg2':
                return '/usr/bin/gpg2'

# Generated at 2022-06-13 06:09:15.716411
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    # Create a mock module
    module = mock.Mock()

    # Create an instance of the RpmKey class
    rpmkey = RpmKey(module)

    # Create a temp file
    tmpfd, tmpname = tempfile.mkstemp()
    os.close(tmpfd)

    # Write 'test' to temp file
    with open(tmpname, 'w') as f:
        f.write('test')

    # Assert against getkeyid()
    assert rpmkey.getkeyid(tmpname) == ''

# Generated at 2022-06-13 06:09:23.478100
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    keyid = "aA1bB2cC3dD4eE5fF6aA1bB2cC3dD4eE5fF6"
    command = ['rpm', '--erase', '--allmatches', "gpg-pubkey-%s" % keyid[-8:].lower()]
    rpm_key = RpmKey(keyid, "gpg2", "rpm", module)
    assert rpm_key.drop_key(keyid) == command