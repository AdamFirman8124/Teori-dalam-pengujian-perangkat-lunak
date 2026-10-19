

# Generated at 2022-06-13 05:59:52.271624
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    test_data = {
        'url': 'http://apt.sw.be/dag/RPM-GPG-KEY.dag.txt',
        'fpath': '/tmp/RPM-GPG-KEY.dag.txt',
        'key': 'RSA/SHA256, Thu Jan 01 00:00:00 1970, Key ID 79b322e91e1a7c42',
    }
    tmpfd, tmpname = tempfile.mkstemp()
    tmpfile = os.fdopen(tmpfd, "w+b")
    tmpfile.write(test_data['key'])
    tmpfile.close()
    module = {}
    Rpm = RpmKey(module)
    assert (Rpm.getkeyid(tmpname) == '79B322E91E1A7C42')

# Generated at 2022-06-13 06:00:04.638483
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import tempfile
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils import basic
    fp = tempfile.NamedTemporaryFile()

# Generated at 2022-06-13 06:00:13.527831
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    module = AnsibleModule(argument_spec={})
    rpmkey = RpmKey(module)
    keyid = "7d06e950f0e7fad6"
    # Test when keyid is inside key description
    assert rpmkey.is_key_imported(keyid)
    # Test when keyid is not inside key description
    keyid = "12345678"
    assert not rpmkey.is_key_imported(keyid)
    # Test when no keys are installed
    rpmkey.execute_command = mock.Mock(return_value=(1, "", ""))
    assert not rpmkey.is_key_imported(keyid)

# Generated at 2022-06-13 06:00:24.613339
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    from ansible.modules.packaging.os.rpm_key import RpmKey
    import unittest

    rpm = RpmKey(None)
    assert rpm.normalize_keyid(None) == ""
    assert rpm.normalize_keyid("0x12345678") == "12345678"
    assert rpm.normalize_keyid("0X12345678") == "12345678"
    assert rpm.normalize_keyid("12345678") == "12345678"
    assert rpm.normalize_keyid("0x1234567") == "01234567"
    assert rpm.normalize_keyid("0X1234567") == "01234567"
    assert rpm.normalize_keyid("01234567") == "01234567"

# Generated at 2022-06-13 06:00:29.389128
# Unit test for constructor of class RpmKey
def test_RpmKey():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        )
    )

    test = RpmKey(module)
    return test

# Generated at 2022-06-13 06:00:39.573267
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url

    from ansible_rpm_utils.rpm_key import RpmKey

    # Create a temporary rpm db for testing
    temp_dir = tempfile.mkdtemp()

    # Create a pubkey.gpg file with a dummy pubkey inside
    pubfile = open('pubfile.gpg', 'w')
    pubfile.write('-----BEGIN PGP PUBLIC KEY BLOCK-----\n')
    pubfile.write('MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqvghDhvJn7n5PQ9rY5hW\n')

# Generated at 2022-06-13 06:00:52.452675
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():

    import os
    import tempfile
    import ast
    import pytest
    import shutil
    from ansible.module_utils.basic import AnsibleModule

    class FakeAnsibleModule(AnsibleModule):

        def __init__(self, argument_spec, bypass_checks=False, no_log=False,
                     check_invalid_arguments=None, mutually_exclusive=None,
                     required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_check_mode=False,
                     required_if=None, required_by=None):
            self.argument_spec = argument_spec
            self.check_mode = False
            self.cleanup_files = []

        def fail_json(self, **kwargs):
            pass


# Generated at 2022-06-13 06:00:53.443453
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    assert RpmKey.getkeyid("/path/to/key.gpg") == "keyid"


# Generated at 2022-06-13 06:00:59.513103
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import sys
    path = os.path.dirname(os.path.realpath(__file__))
    keyfile = os.path.join(path, 'testkey')
    if len(sys.argv) > 1:
        if sys.argv[1] == '--keyfile':
            print(keyfile)
            sys.exit(0)
        if sys.argv[1] == '--keyid':
            print('0xDEADB33F')
            sys.exit(0)

    class AnsibleModuleFake:
        def __init__(self, argument_spec):
            pass

        def get_bin_path(self, path, required=False):
            return 'gpg'

        def add_cleanup_file(self, path):
            pass


# Generated at 2022-06-13 06:01:09.548111
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import mock
    import StringIO
    test_key_url = "http://vault.centos.org/RPM-GPG-KEY-CentOS-SIG-SCLo"
    test_key_id = "24180A0DB56B746AB39F70D7E9E2C300C6EB1EAE"


# Generated at 2022-06-13 06:01:29.619104
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    key = RpmKey(custom_ansible_module)
    assert key.getfingerprint('/tmp/test_RpmKey_getfingerprint.gpg') == '7E3675B0BFE7C8494F0C6E46B6BFEAC2DD3F869C'


# Generated at 2022-06-13 06:01:39.821143
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    module = AnsibleModule(argument_spec=dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        fingerprint=dict(type='str'),
        validate_certs=dict(type='bool', default=True),
    ), supports_check_mode=True)
    module.get_bin_path = MagicMock(return_value='test')
    k = RpmKey(module)
    k.execute_command = MagicMock(return_value=('fpr:::::::::A2958F927C9E7A4E4D4F2030D4C4FC22C4B6E5E6:', ''))

# Generated at 2022-06-13 06:01:47.043214
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    # Unit test for method is_key_imported of class RpmKey
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    rpmkey = RpmKey(module)
    assert rpmkey.is_key_imported('1') == False

# Generated at 2022-06-13 06:01:54.751606
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # Test for constructor
    test_RpmKey_key_not_found = {
        'state' : 'present',
        'key' : 'test',
        'fingerprint': '',
        'validate_certs': True
    }
    with pytest.raises(AnsibleExitJson) as excinfo:
        RpmKey(test_RpmKey_key_not_found)
    assert excinfo.value.args[0]['changed'] == False

# Generated at 2022-06-13 06:01:56.439998
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    pass

# Generated at 2022-06-13 06:02:09.824029
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    fake_module = MagicMock()
    fake_module.get_bin_path.return_value = '/path/to/rpm'
    fake_module.run_command.return_value = (0, '', '')
    fake_module.cleanup = MagicMock()
    fake_module.cleanup.return_value = None

    # Download a key from a url and return the valid path
    fake_module.params = {
        'state': 'present',
        'key': 'https://packages.chef.io/files/stable/chef/12.21.26/el/7/chef-12.21.26-1.el7.x86_64.rpm',
    }
    rpm_key = RpmKey(fake_module)

# Generated at 2022-06-13 06:02:13.624960
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    from mock import patch, MagicMock
    from ansible.module_utils.urls import fetch_url
    module = MagicMock()
    with patch('ansible.module_utils.urls.fetch_url', return_value=fetch_url):
        rpm_key = RpmKey(module)

    assert rpm_key.fetch_key('https://some.url.com')

# Generated at 2022-06-13 06:02:20.679387
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class FakeModule():
        def __init__(self, params):
            self.params = params
            self.fail_json = lambda msg, **kwargs: raise_exception()

    class FakeFile():
        def __init__(self, content):
            self.content = content

        def read(self):
            return self.content

    class FakeResult():
        def __init__(self, stdout):
            self.stdout = stdout

        def strip(self):
            return self.stdout

    class FakeWords():
        def __init__(self, words):
            self.words = words

        def __getitem__(self, index):
            return self.words[index]


# Generated at 2022-06-13 06:02:29.118587
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.builtin.plugins.modules.rpm_key import RpmKey
    import tempfile
    
    # Create a key file
    tmpfd, tmpname = tempfile.mkstemp()
    os.close(tmpfd)
    os.remove(tmpname)

# Generated at 2022-06-13 06:02:42.183213
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    mock_module = MagicMock()
    mock_module.run_command = MagicMock()
    mock_module.run_command.return_value = 0, 'gpg-pubkey-deadb33f-5214085d\n', ''
    test_class = RpmKey(mock_module)
    keyid = 'DEADB33F'
    test_class.is_key_imported(keyid)
    assert mock_module.run_command.call_count == 2
    assert mock_module.run_command.call_args_list[1][0][0][0].endswith('rpm')
    assert mock_module.run_command.call_args_list[1][0][0][1] == '-q'

# Generated at 2022-06-13 06:03:15.755257
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
    rpmkey = RpmKey(module)
    # The string 0xcec0ffff is a valid keyid
    assert rpmkey.is_keyid('0xcec0ffff')
    # The string 0xcec0ffff0 is not a valid keyid
    assert not rpmkey.is_keyid('0xcec0ffff0')
    # The string '0xcec0ffff' is

# Generated at 2022-06-13 06:03:28.467338
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # Create an instance of RpmKey
    rpm_key = RpmKey()

    # Create mocks for the required objects of the RpmKey.execute_command method
    module_mock = MagicMock()
    module_mock.fail_json.side_effect = Exception('Test')

    # Try to execute the RpmKey.execute_command method without arguments
    # An exception should be raised with the message:
    # "missing 1 required positional argument: 'cmd'"
    with pytest.raises(TypeError) as exception_info:
        rpm_key.execute_command()
    message = exception_info.value.args[0]
    assert message == "execute_command() missing 1 required positional argument: 'cmd'"

    # Try to execute the RpmKey.execute_command method with a non-tuple as argument
    # An exception

# Generated at 2022-06-13 06:03:39.151133
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import base64
    from io import StringIO
    from ansible.module_utils.urls import ConnectionError, SSLValidationError
    from ansible.module_utils.six.moves.urllib.error import HTTPError, URLError
    import ssl
    from os import remove
    from os.path import isfile
    from tempfile import mkstemp
    from ansible.module_utils.basic import AnsibleModule, AnsibleModuleExit

# Generated at 2022-06-13 06:03:49.328087
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile

    class MockModule(object):
        pass

    mock_module = MockModule()

    # Store original execute command method
    original_execute_command = RpmKey.execute_command

    # Write a mocked rpm key to file
    tmpfd, tmpname = tempfile.mkstemp()
    tmpfile = os.fdopen(tmpfd, "w+b")

# Generated at 2022-06-13 06:03:59.325308
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
    rpmKey = RpmKey(module)
    assert rpmKey.drop_key('4E6CCE6057EDBE1FF7BD854E931D0B26C63163BE') == None


# Generated at 2022-06-13 06:04:09.001529
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

    assert rpm_key.is_keyid("0xDEADBEEF") is True
    assert rpm_key.is_keyid("0XDEADBEEF") is True
    assert rpm_key.is_keyid("DEADBEEF") is True
    assert rpm_key.is_keyid("DEAD") is False
    assert rpm

# Generated at 2022-06-13 06:04:10.827203
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    key = RpmKey(None)
    assert True

# Generated at 2022-06-13 06:04:21.349134
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import sys
    import os
    import ansible.module_utils.ansible_release
    import ansible.module_utils.six.moves.urllib

    # construct a path to the test module
    abs_path = os.path.join(os.path.dirname(__file__), "../ansible_collections/ansible/builtin/rpm_key.py")
    sys.path.insert(0, os.path.abspath(abs_path))

    # mock up a module for testing
    class MockModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = lambda *args : None

        def get_bin_path(self, name, required=False):
            if name == "rpm":
                return "rpm"

# Generated at 2022-06-13 06:04:32.172303
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    m = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    r = RpmKey(m)
    assert r.getfingerprint("tests/data/RPM-GPG-KEY-fedora-23-primary-x86_64") == "3BDB3BDF7D8F6BC4B6B4D18AE5352B109AB3C4E6"


# Generated at 2022-06-13 06:04:39.061650
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
        ),
        supports_check_mode=True,
    )
    rpmKey = RpmKey(module)
    assert rpmKey.is_keyid("0xDEADB33F")
    assert rpmKey.is_keyid("DEADB33F")
    assert rpmKey.is_keyid("0xDEADB33")
    assert rpmKey.is_keyid("DEADB33")
    assert rpmKey.is_keyid("DEADB3") is False
    assert rpmKey.is_keyid("DEADB") is False
    assert rpmKey.is_

# Generated at 2022-06-13 06:05:49.701205
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import unittest

    class RpmKeyModule(unittest.TestCase):
        def setUp(self):
            self.module = AnsibleModule(
                argument_spec=dict(
                    state=dict(type='str', default='present', choices=['absent', 'present']),
                    key=dict(type='str', required=True, no_log=False),
                    fingerprint=dict(type='str'),
                    validate_certs=dict(type='bool', default=True),
                ),
                supports_check_mode=True,
            )

    RpmKeyModule()

# Generated at 2022-06-13 06:05:59.174294
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native
    from ansible.module_utils.rpm_key import RpmKey
    import os.path

    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 06:06:10.027436
# Unit test for method fetch_key of class RpmKey

# Generated at 2022-06-13 06:06:22.035438
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    class AnsibleModule(object):
        def __init__(self, arg):
            self.params = arg

    def test_exc(t, *args, **kwargs):
        t.fail("didn't expect to get called")

    class FakeAnsibleModule(object):
        def __init__(self, arg):
            self.arg = arg
            self.params = {}

        def fail_json(self, msg):
            raise AssertionError("msg: %s, arg: %s" % (msg, self.arg))

        def get_bin_path(self, cmd):
            return cmd

        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == "rpm --version":
                return 0, "4.11.1", ""

# Generated at 2022-06-13 06:06:30.651736
# Unit test for constructor of class RpmKey
def test_RpmKey():
    class FakeModule:
        def __init__(self):
            self.module = self
            self.params = {
                "key": "http://apt.sw.be/RPM-GPG-KEY.dag.txt",
                "state": "present"
            }

        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, "", ""

        def get_bin_path(self, cmd, required=False):
            return cmd

        def cleanup(self, keyfile_path):
            return

        def fail_json(self, msg):
            return

        def exit_json(self, changed):
            return

    rm = RpmKey(FakeModule())
    assert rm is not None

# Generated at 2022-06-13 06:06:43.230123
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils.six import StringIO
    try:
        from ansible.module_utils.six.moves import builtins, cPickle
    except ImportError:
        import __builtin__ as builtins
        import cPickle

    class AnsibleModuleMock():

        def __init__(self, spec):
            self.ansible_facts = {}
            self.params = {}
            self.check_mode = False
            self.debug_mode = None
            self.tmpdir = tempfile.mkdtemp()
            self.cleanup_file = []
            self.cleanup_dir = []
            self.exit_args = {}
            self.exit_json_args = None
            self.exit_json = None
            self.fail_json_args = None
            self.fail_json = None


# Generated at 2022-06-13 06:06:51.578037
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    class FakeModule(object):
        def fail_json(self, msg):
            raise AssertionError(msg)

        def run_command(self, cmd, **kwargs):
            return 42, 'stdout', 'stderr'

    def check(expected_msg, cmd):
        try:
            RpmKey(FakeModule()).execute_command(cmd)
        except AssertionError as exc:
            assert to_native(exc) == expected_msg
        else:
            assert False

    check('stderr', 'foo')
    check(
        "Unexpected gpg output",
        'foo --no-tty --batch --with-colons --fixed-list-mode bar'
    )

# Generated at 2022-06-13 06:07:02.258340
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    test_keyfile = '/tmp/rpm_key_test_RpmKey_getfingerprint'

# Generated at 2022-06-13 06:07:13.171712
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils._text import to_native
    from rpm_key_1_3 import RpmKey

    key = fetch_url(None, 'http://apt.sw.be/RPM-GPG-KEY.dag.txt')[0].read()
    tmpfd, tmpname = tempfile.mkstemp()
    os.write(tmpfd, key)
    os.close(tmpfd)

    # pylint: disable=protected-access
    fingerprint = RpmKey(AnsibleModule({}, {})).getfingerprint(tmpname)

# Generated at 2022-06-13 06:07:20.091551
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

    rpmkey = RpmKey(module)

    # Test 1
    test1_cmd = rpmkey.rpm + ' -q  gpg-pubkey'
    test1_stdout = 'this should crash'
    test1_stderr = 'there are no keys on this system'
    with pytest.raises(AnsibleError):
        rpmkey.execute_command(test1_cmd)