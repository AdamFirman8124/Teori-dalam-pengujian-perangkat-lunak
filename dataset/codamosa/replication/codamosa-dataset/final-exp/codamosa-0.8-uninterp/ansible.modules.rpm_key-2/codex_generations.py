

# Generated at 2022-06-13 05:59:51.874165
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True
    )
    
    rpm_key = RpmKey(module)

    assert rpm_key.normalize_keyid(' 0xDEADBEEF ') == 'DEADBEEF'
    assert rpm_key.normalize_keyid(' 0XDEADBEEF ') == 'DEADBEEF'

# Generated at 2022-06-13 05:59:57.015571
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    expected = [
        ['rpm', '--erase', '--allmatches', 'gpg-pubkey-deadb33f'],
    ]

    result = RpmKey().drop_key("DEADB33F")

    assert expected == result


# Generated at 2022-06-13 06:00:07.854728
# Unit test for method getkeyid of class RpmKey

# Generated at 2022-06-13 06:00:16.435695
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    import json
    import os
    import os.path
    import tempfile

    # Prepare a module
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Create an instance of class RpmKey
    rpm_key = RpmKey(module)

    # Prepare parameters
    keyid = '65B5D4C1'

    # Get the full path to rpm binary
    rpm_path = rpm_key.rpm

    # Create a temp file
    tmpfd, tmpname = tempfile.mk

# Generated at 2022-06-13 06:00:26.638077
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Tests if the key is downloaded and the right pubkey contents are returned
    # This is not a valid pubkey, it's only used for this test
    url = "http://localhost/key.gpg"
    module = None
    key = RpmKey(module)


# Generated at 2022-06-13 06:00:36.328238
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
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
    cmd = rpm_key.rpm + ' -q  gpg-pubkey'
    stdout, stderr = rpm_key.execute_command(cmd)
    assert type(stdout) == str
    assert len(stdout) != 0
    assert type(stderr) == str

# Generated at 2022-06-13 06:00:44.538276
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # Case 1, the command with no error
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    rpm_key_instance = RpmKey(module)
    cmd = ["rpm","-q","gpg-pubkey"]
    result = rpm_key_instance.execute_command(cmd)
    assert result == None

    # Case 2, the command with error

# Generated at 2022-06-13 06:00:46.275748
# Unit test for constructor of class RpmKey
def test_RpmKey():
    assert RpmKey(2)

# Generated at 2022-06-13 06:00:54.844186
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import tempfile
    import os
    # Use a temporary file
    temp = tempfile.NamedTemporaryFile()
    # Write to it
    temp.write(b'whatever')
    # This is the key that would be returned
    key = temp.name
    # Close and delete
    temp.close()
    # Create an object of class RpmKey
    rpk = RpmKey(key)
    # Run the method
    result = rpk.fetch_key('http://someimaginaryhost')
    # Check that the file has been deleted
    assert not os.path.exists(result)


# Generated at 2022-06-13 06:00:59.570677
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import ansible.modules.packaging.os.rpm_key as rpm_key

    class FakeModule(object):
        def __init__(self):
            self.params = {'key': 'http://www.google.com'}

        def get_bin_path(self, name, required=False):
            return '%s' % (name)

        def add_cleanup_file(self, filename):
            return True

        def run_command(self, cmd):
            return 1, "stdout", "stderr"

    fake_module = FakeModule()
    rpm_key.RpmKey(fake_module)

# Generated at 2022-06-13 06:01:30.528498
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    """
    Unit test to make sure the output of fetch_key method is
    a valid public key.
    """
    rpm_key = RpmKey(None)

    key = rpm_key.fetch_key('https://raw.githubusercontent.com/ansible/ansible/devel/lib/ansible/module_utils/urls.py')
    assert is_pubkey(key)

# Generated at 2022-06-13 06:01:34.519608
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    test_object = RpmKey(AnsibleModule({}))

# Generated at 2022-06-13 06:01:45.925932
# Unit test for method getfingerprint of class RpmKey

# Generated at 2022-06-13 06:01:57.540137
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import __builtin__
    setattr(__builtin__, 'open', mock_open())
    class MockModule(object):
        def __init__(self):
            self.params={}
            self.params['key']='file.gpg'
            self.check_mode=False
            self.run_command=Mock(return_value=(0,'',''))
            self.add_cleanup_file=Mock(return_value=None)
    class MockAnsibleModule(object):
        def __init__(self):
            self.module=MockModule()
        def fail_json(self,msg):
            raise Exception(msg)
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile()
    open(tmpfile.name,'w').write('key')

# Generated at 2022-06-13 06:02:10.723298
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class AnsibleModule(object):
        @staticmethod
        def fail_json(msg):
            raise AssertionError(msg)
        @staticmethod
        def get_bin_path(name, required=False):
            assert name == 'gpg'
            return '/usr/bin/gpg'
        @staticmethod
        def run_command(*args, **kwargs):
            assert args == (('/usr/bin/gpg', '--no-tty', '--batch', '--with-colons',
                             '--fixed-list-mode', '--with-fingerprint', '/path/to/file'),)

# Generated at 2022-06-13 06:02:12.742496
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # TODO: Tests need to be written
    return

# Generated at 2022-06-13 06:02:15.517144
# Unit test for function main
def test_main():
    b = dict(state='present', key='/path/to/key.gpg')
    assert main(b)

# Generated at 2022-06-13 06:02:17.025961
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    assert True


# Generated at 2022-06-13 06:02:29.991883
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rpm_key = RpmKey(module)

    assert ("-----BEGIN PGP PUBLIC KEY BLOCK-----" in rpm_key.fetch_key("http://apt.sw.be/RPM-GPG-KEY.dag.txt"))
    assert ("-----BEGIN PGP PUBLIC KEY BLOCK-----" in rpm_key.fetch_key("https://apt.sw.be/RPM-GPG-KEY.dag.txt"))
    assert ("-----BEGIN PGP PUBLIC KEY BLOCK-----" in rpm_key.fetch_key("https://wombat.gazzang.com/RPM-GPG-KEY-gazzang-pubkey.asc"))

# Generated at 2022-06-13 06:02:42.981701
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    import unittest
    import os
    import tempfile
    import shutil
    class MockModule(object):
        class RunCommand(object):
            def __call__(self, cmd, use_unsafe_shell):
                return 1, 'line1\nline2\n', 'error'
        def __init__(self):
            self.run_command = self.RunCommand()
            self.exit_json = lambda x: None
            self.fail_json = lambda x: None
    class TestRpmKey(unittest.TestCase):
        def test_execute_command(self):
            module = MockModule()
            rpmkey = RpmKey(module)
            test_cmd = 'test_cmd'

# Generated at 2022-06-13 06:03:18.963585
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    from ansible.module_utils.six.moves import StringIO

    # Import module for the sake of unittesting the class
    import rpm_key

    # Creation of a temporary file
    fh = tempfile.NamedTemporaryFile()
    fh.write(b"""{'changed': False, 'warnings': []}""")
    fh.flush()

    # Creation of a mock module to be able to use it as an input for
    # the class that is being unittested

# Generated at 2022-06-13 06:03:30.121313
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    from ansible.module_utils import rpm_key
    from ansible.module_utils.urls import fetch_url

    class FakeModule(object):

        def __init__(self):
            self.params = {'state': 'present', 'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt', 'fingerprint': None}
            self.result = {'changed': False}
            self.fail_json = None

        def get_bin_path(self, name):
            return 'path/to/%s' % name

        def get_bin_path(self, name, required):
            return 'path/to/%s' % name

        def run_command(self, cmd, use_unsafe_shell=False):
            return 0, "", ""


# Generated at 2022-06-13 06:03:38.569559
# Unit test for constructor of class RpmKey
def test_RpmKey():
    class Module():
        def __init__(self, debug=False, check_invalid_arguments=True, no_log=False, argspec=None):
            self.debug = debug
            self.check_invalid_arguments = check_invalid_arguments
            self.no_log = no_log
            self.argspec = argspec
            self.params = {}
        def get_bin_path(self, arg, required=False):
            return "/usr/bin/rpm"
        def fail_json(self):
            print("fail")
        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, "", ""
        def exit_json(self, changed=False):
            print("exit")

# Generated at 2022-06-13 06:03:48.977957
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    test_module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    test_module.get_bin_path = mock.Mock()
    test_module.get_bin_path.side_effect = [True, True]
    test_module.run_command = mock.Mock()
    test_module.fail_json = mock.Mock()
    test_module.cleanup = mock.Mock()


# Generated at 2022-06-13 06:03:57.749153
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

    rpm = RpmKey(module)
    assert rpm.import_key('/path/to/file')



# Generated at 2022-06-13 06:04:06.539461
# Unit test for method is_keyid of class RpmKey

# Generated at 2022-06-13 06:04:19.064728
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class module_object(object):
        def __init__(self):
            self.fail_json_called = False

        def run_command(self, command):
            stdout = ""
            stderr = ""

# Generated at 2022-06-13 06:04:23.065223
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    test_mod = AnsibleModule(argument_spec=dict(key=dict(type='str', required=True), state=dict(type='str')))
    test_key = RpmKey(test_mod)
    assert is_pubkey(test_key.fetch_key('https://apt.sw.be/RPM-GPG-KEY.dag.txt'))
    test_mod.fail_json = lambda **kwargs: True
    test_key.fetch_key('https://apt.sw.be/RPM-GPG-KEY.dag.txt')

# Generated at 2022-06-13 06:04:27.419064
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    obj = RpmKey(module)
    assert obj.getfingerprint('test_data/test_key.gpg') == b'EBC6E12C62B1C734026B2122A20E52146B8D79E6'


# Generated at 2022-06-13 06:04:36.761757
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    def side_effect_run_command(*args, **kwargs):
        if args[0] == ['/usr/bin/gpg', '--no-tty', '--batch', '--with-colons', '--fixed-list-mode', '/tmp/tmp0zr8o7w']:
            return (0, '', '')
        elif args[0] == ['/bin/rpm', '--import', '/tmp/tmp0zr8o7w']:
            return (0, '', '')
        else:
            return (1, '', 'Unexpected gpg output')

    def side_effect_cleanup(file):
        pass


# Generated at 2022-06-13 06:05:41.900722
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    # test when key is not installed
    from ansible_collections.community.general.tests.unit.compat import mock
    from ansible_collections.community.general.plugins.modules import rpm_key
    import ansible.module_utils
    import ansible.module_utils.urls
    import ansible.module_utils._text
    import os.path

    mock_module = mock.Mock()
    mock_module.run_command = mock.Mock(return_value=(0, 'something', ''))
    mock_module.fail_json = mock.Mock()
    mock_module.check_mode = False
    mock_module.add_cleanup_file = mock.Mock()
    mock_module.get_bin_path = mock.Mock(return_value='/bin/rpm')

    m = rpm

# Generated at 2022-06-13 06:05:53.747613
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    a = RpmKey()
    assert a.normalize_keyid('0x12345678') == '12345678'
    assert a.normalize_keyid('0XAABBCCDD') == 'AABBCCDD'
    assert a.normalize_keyid('  0x1122334455667788  ') == '1122334455667788'
    assert a.normalize_keyid('deadbeef') == 'DEADBEEF'
    assert a.normalize_keyid('0x12345678') == '12345678'
    assert a.normalize_keyid('0x12345678') == '12345678'


# Generated at 2022-06-13 06:05:59.158012
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    """normalize_keyid tests"""
    m = AnsibleModule(argument_spec={})
    rpm_key = RpmKey(m)

    assert rpm_key.normalize_keyid('0XDEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xDEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid(' 0xDEADB33F ') == 'DEADB33F'

# Generated at 2022-06-13 06:06:09.317255
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    class FakeModule(object):
        def exit_json(*_):
            pass

    class FakeLogging(object):
        def warning(self, msg):
            print(msg)

    module = FakeModule()
    rpm_key = RpmKey(module)
    assert rpm_key.normalize_keyid('  DEADB33F ') == 'DEADB33F'
    assert rpm_key.normalize_keyid('DEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xDEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0XDEADB33F') == 'DEADB33F'



# Generated at 2022-06-13 06:06:21.369224
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    '''Unit test for method fetch_key of class RpmKey'''
    url = 'https://example.com/fred.txt'
    key = 'wibble'
    module = AnsibleModule(argument_spec={
        'state': dict(type='str', default='present', choices=['absent', 'present']),
        'key': dict(type='str', required=True, no_log=False),
        'fingerprint': dict(type='str'),
        'validate_certs': dict(type='bool', default=True),
    })

    class MockFetchUrl(object):
        '''Mock class to replace fetch_url'''
        class MockResponse(object):
            '''Mock class for fetch_url response'''
            def __init__(self, content):
                self.content = content

# Generated at 2022-06-13 06:06:30.813015
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    from ansible.module_utils._text import to_bytes
    from ansible.modules.system.rpm_key import RpmKey

    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.system.rpm_key import main as rpm_key_main

    # Creating a test instance of the RpmKey class
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    rpmkey = RpmKey(module)

    # Mock class attributes
    rpmkey.rpm = '/usr/bin/rpm'
    rpmkey.gpg = '/usr/bin/gpg'

    # Testing the is_key_imported method
    # Case where there no keys in the rpmdb

# Generated at 2022-06-13 06:06:40.777993
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    """Test is_key_imported"""
    keyid = 'D45B7A20'
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    key = RpmKey(module)
    key.is_key_imported(keyid)

# Generated at 2022-06-13 06:06:44.824071
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    rpmkey = RpmKey("")
    assert rpmkey.is_keyid("DEADB33F")
    assert rpmkey.is_keyid("0xDEADB33F")
    assert not rpmkey.is_keyid("my-key-id")

# Generated at 2022-06-13 06:06:52.521840
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.rpm_key import RpmKey

    # Test for specific keyid
    rpmkey_obj = RpmKey(None)

    with open('test/gpg_keys/RPM-GPG-KEY-dag', 'rb') as f:
        key = f.read()
    tmpfd, tmpname = tempfile.mkstemp()
    with os.fdopen(tmpfd, "w+b") as tmpfile:
        tmpfile.write(key)

    fingerprint = rpmkey_obj.getfingerprint(tmpname)
    assert fingerprint == 'EBC6E12C62B1C734026B2122A20E52146B8D79E6'
    os.remove(tmpname)

# Generated at 2022-06-13 06:07:03.423129
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import os.path
    from ansible.module_utils.basic import AnsibleModule
    class MockModule(object):
        def __init__(self):
            self.run_command_result = ('', '', 0)
        def run_command(self, cmd, use_unsafe_shell=True):
            return self.run_command_result
    class MockAnsibleModule(object):
        def __init__(self):
            self.module = MockModule()
        def fail_json(self, msg):
            raise AssertionError(msg)
        def get_bin_path(self, binary, required=True):
            if binary == 'rpm': return '/bin/rpm'
            if binary == 'gpg': return '/bin/gpg2'
            if binary == 'gpg2': return '/bin/gpg2'

# Generated at 2022-06-13 06:09:27.901971
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    keyid = None

    # GPG Key (without comment)
    key = "-----BEGIN PGP PUBLIC KEY BLOCK-----\n"
    key += "Version: GnuPG v2.0.14 (GNU/Linux)\n"
    key += "\n"
    key += "mQENBFeXjT8BCADD8sxt2QoI+Yzjq3SxS+jKbb0mfCLz9Xqhg4a4m0Kj6Rmz6M1U\n"
    key += "OJlL9XA/SI5N5O5+BdYJwN/Q2MZKjDLbF1pM5HX9B7LMK5C5f5+YkY1iAQ2xS+SZ\n"
   