

# Generated at 2022-06-13 05:59:50.270196
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.six import PY3

    class MockAnsibleModule(object):

        def __init__(self, **kwargs):
            self.params = kwargs
            self.module_args = kwargs

        def get_bin_path(self, name, required=False, opt_dirs=[]):
            return get_bin_path(name, required, opt_dirs)

        def fail_json(self, *args, **kwargs):
            raise Exception(*args, **kwargs)


# Generated at 2022-06-13 06:00:03.005186
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
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

    assert rpm_key.normalize_keyid("0xdeadbeef") == "DEADBEEF"
    assert rpm_key.normalize_keyid("deadbeef") == "DEADBEEF"
    assert rpm_key.normalize_keyid("DEADBEEF") == "DEADBEEF"



# Generated at 2022-06-13 06:00:10.372423
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
    # rpm_key = RpmKey(module)
    stdout, stderr = RpmKey.execute_command(self, [self.rpm, '--import', keyfile])
    assert stdout is not None and stderr is None

# Generated at 2022-06-13 06:00:18.605831
# Unit test for method getfingerprint of class RpmKey

# Generated at 2022-06-13 06:00:27.692104
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import io
    import io
    import sys
    import tempfile
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    testmodule = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    key_file = "test_key.gpg"

# Generated at 2022-06-13 06:00:38.240704
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Create a mocked AnsibleModule to avoid having to deal with parameters
    mocked_module = MockedAnsibleModule()

    # Create a mocked url
    url = 'https://keybase.io/hector/key.asc'

    # Create a test RpmKey instance
    rpm_key = RpmKey(mocked_module)

    # Execute the fetch_key method
    keyfile = rpm_key.fetch_key(url)

    # Get the mocked body from the AnsibleModule
    body = mocked_module.mocked_url_responses[0]['body']

    # Assert that the body is a valid pubkey
    assert is_pubkey(body)

    # Assert that it is a valid path
    assert isinstance(keyfile, str)

    # Check that it returns a valid path
    assert os.path

# Generated at 2022-06-13 06:00:44.816450
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
    rp = RpmKey(module)

    assert rp.gpg != None
    assert rp.getkeyid("./test/RPM-GPG-KEY-dag.txt") == "0DFB3188"


# Generated at 2022-06-13 06:00:51.809782
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    rpm_key_obj = RpmKey(None)
    assert(rpm_key_obj.is_keyid("deadb33f"))
    assert(rpm_key_obj.is_keyid("0XDeadb33f"))
    assert(rpm_key_obj.is_keyid("0xDeadb33f"))
    assert(not rpm_key_obj.is_keyid("mykey"))


# Generated at 2022-06-13 06:00:57.052603
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    # Check that an existing key is detected
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
    )
    rpmkey = RpmKey(module)
    result = rpmkey.is_key_imported('437D05B5')
    assert result == True
    # Check that a non-existing key is not detected
    result = rpmkey.is_key_imported('AABBCCDD')
    assert result == False

# Generated at 2022-06-13 06:01:00.887668
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():

    keyfile = RpmKey.fetch_key(RpmKey, 'https://localhost:8000/RPM-GPG-KEY.dag.txt')
    assert os.path.exists(keyfile)


# Generated at 2022-06-13 06:01:23.320354
# Unit test for method drop_key of class RpmKey

# Generated at 2022-06-13 06:01:34.480286
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    rpmkey_instance = RpmKey(module)
    generated_keyid = rpmkey_instance.getkeyid('/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release')
    result = rpmkey_instance.is_key_imported(generated_keyid)
    assert result


# Generated at 2022-06-13 06:01:43.164129
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import io
    import unittest

    from ansible.module_utils.urls import fetch_url

    from ansible.module_utils._text import to_native

    with open('tests/fixtures/ansible_rpm_key/key.gpg', 'r') as f:
        pubkey = f.read()

    def mocked_fetch_url(module, url, *args, **kwargs):
        return [io.StringIO(pubkey), dict()]

    fetch_url_orig = fetch_url

    fetch_url = mocked_fetch_url

    class MockModule(object):
        # Fake class

        def __init__(self):
            pass

        def get_bin_path(self, binary):
            return binary

        def check_mode(self):
            return False


# Generated at 2022-06-13 06:01:50.122839
# Unit test for function main
def test_main():
    try:
        from ansible.modules.packaging import rpmkey
    except ImportError:
        from ansible.modules.packaging.redhat import rpmkey
    key = 'my-key'
    cmd = 'rpm -q  gpg-pubkey --qf "%{description}" | gpg --no-tty --batch --with-colons --fixed-list-mode -'
    result = {
        'changed': False,
        'failed': False,
        'msg': ''
    }
    module = MagicMock()
    module.run_command.return_value = (0, '', '')
    module.check_mode = True
    module.get_bin_path.return_value = 'sudo'
    module.params = {
        'state': 'present',
        'key': key
    }
    rpmkey

# Generated at 2022-06-13 06:01:58.835438
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
    rpmkey = RpmKey(module)
    assert rpmkey.import_key(rpmkey.fetch_key(
        'https://access.redhat.com/security/team/key'))


# Unit test to verify that exception is thrown if key file not found

# Generated at 2022-06-13 06:02:11.642626
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    # Dummy module
    class DummyModule():
        def __init__(self):
            self.gpg = '/usr/bin/gpg'

    # Dummy file
    from io import StringIO
    key = StringIO()
    key.write('-----BEGIN PGP PUBLIC KEY BLOCK-----\n')
    key.write('Version: GnuPG v1.4.11 (GNU/Linux)\n')
    key.write('\n')
    key.write('mQENBFH3oqkBCADrF6Q2h9cYf6Uvx6y8d51w+fy6jh5RWkZ+MbZzfKozX9YdCvQy\n')

# Generated at 2022-06-13 06:02:18.740746
# Unit test for function main
def test_main():
    import mock
    import json

    def execute_command(self, cmd):
        return '', ''

    def is_key_imported(self, keyid):
        return True

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    module.params['fingerprint'] = 'EBC6 E12C 62B1 C734 026B 2122 A20E 5214 6B8D 79E6'

# Generated at 2022-06-13 06:02:31.200185
# Unit test for method getkeyid of class RpmKey

# Generated at 2022-06-13 06:02:39.997953
# Unit test for function main
def test_main():
    # Test with normal input
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

# Generated at 2022-06-13 06:02:40.740406
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    assert True

# Generated at 2022-06-13 06:03:12.863385
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

# Generated at 2022-06-13 06:03:17.994367
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    keyid = "1c3f3196"
    theclass = RpmKey(None)
    assert keyid != theclass.normalize_keyid(keyid)
    keyid = "0x" + keyid
    assert keyid != theclass.normalize_keyid(keyid)
    keyid = "0X" + keyid[2:]
    assert keyid != theclass.normalize_keyid(keyid)

# Generated at 2022-06-13 06:03:25.128380
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    rpm_key_obj = RpmKey(module)
    cmd = rpm_key_obj.rpm + ' -q  gpg-pubkey'
    cmd += ' --qf "%{description}" | ' + rpm_key_obj.gpg + ' --no-tty --batch --with-colons --fixed-list-mode -'
    stdout, stderr = rpm_key_obj.execute_command(cmd)
    assert stderr == '', "stderr should be empty"
    assert stdout != '', "stderr should not be empty"

# Generated at 2022-06-13 06:03:29.912882
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    assert_equal(RpmKey.getkeyid(r'/tmp/tmpuAG1V2/RPM-GPG-KEY-dag'), 'EBC6E12C62B1C7C8062B2122A20E52146B8D79E6')

# Generated at 2022-06-13 06:03:35.999561
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    keyid = "deadb33f"
    keyid1 = "0xDeadb33f"
    keyid2 = "0xDeadb33f" + " "
    assert RpmKey(None).normalize_keyid(keyid) == keyid.upper()
    assert RpmKey(None).normalize_keyid(keyid1) == keyid1.upper()[2:]
    assert RpmKey(None).normalize_keyid(keyid2) == keyid2.upper()[2:].strip()

# Generated at 2022-06-13 06:03:47.252886
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
    # Test existing key
    existing_key = '../../../../static/gpg-pubkey-deadb33f-56a3bd14.key'
    if not os.path.exists(existing_key):
        ansible_module.fail_json(msg='Test file not exist.')

# Generated at 2022-06-13 06:03:54.837188
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    import tempfile
    import os
    module = AnsibleModule(argument_spec=dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        fingerprint=dict(type='str'),
        validate_certs=dict(type='bool', default=True),
    ), supports_check_mode=True)

    # Dummy gpg public key
    # pub   rsa2048/EBC6E12C62B1C734026B2122A20E52146B8D79E6 2016-01-09 [SC] [expires: 2017-01-09]
    #       Key fingerprint = 9160 A8F2 4E1B 6DE2 CC07  9BA4 B6AA E94

# Generated at 2022-06-13 06:04:06.371728
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    with patch('ansible.module_utils.urls.fetch_url') as mock_fetch_url:
        keyfile = '/tmp/test_RpmKey_getfingerprint.key'
        keyid = 'C734A20E526B8D79E6'
        mock_fetch_url.return_value = (
            b"", {
                'status': 200,
                'msg': 'OK (unknown size)',
                'url': 'http://www.example.com',
            }
        )

# Generated at 2022-06-13 06:04:20.696853
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
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

    # keyid doesn't include 0x
    keyid = '0C902B1D'
    normalized_keyid = rpmkey.normalize_keyid(keyid)
    assert normalized_keyid == 'C902B1D'

    # keyid includes 0x
    keyid = '0x0C902B1D'
    normalized

# Generated at 2022-06-13 06:04:32.276482
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    # Test 1: The key is present
    with pytest.raises(Exception):
        # Instance created with an unknown keyid.
        rpm_key = RpmKey(AnsibleModule(argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key='deadb33f',
            validate_certs=dict(type='bool', default=True),
        ), supports_check_mode=True))
        assert rpm_key.is_key_imported('deadb33f')

        # Instance created with a known keyid.

# Generated at 2022-06-13 06:05:31.114317
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    testmodule = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=False,
    )
    rpmkey = RpmKey(testmodule)
    assert rpmkey.is_key_imported('DEADBEEF') == False


# Generated at 2022-06-13 06:05:38.944425
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import tempfile
    tmpfd, tmpname = tempfile.mkstemp()
    os.close(tmpfd)

# Generated at 2022-06-13 06:05:53.461532
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    from ansible.module_utils.basic import AnsibleModule

    class RpmModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, cmd, use_unsafe_shell=True):
            if cmd[0].endswith('q'):
                return (0, 'gpg-pubkey-2fa658e0-41bd7d7d')

# Generated at 2022-06-13 06:06:02.045176
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class ModuleStub:
        def __init__(self):
            self.check_mode = False
            self.fail_json = lambda self, msg: None
            self.cleanup = lambda self, msg: None

        def run_command(self, cmd, use_unsafe_shell=True):
            return_code = 0

# Generated at 2022-06-13 06:06:07.398259
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    module = AnsibleModule({}, check_mode=False)
    rpm_key_obj = RpmKey(module)
    assert os.path.exists(rpm_key_obj.fetch_key('https://pastebin.com/raw/hKKvJ9ud'))
    with pytest.raises(Exception):
        rpm_key_obj.fetch_key('https://error/url.foo')



# Generated at 2022-06-13 06:06:08.641546
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    assert RpmKey.import_key(self, keyfile) == "foo"

# Generated at 2022-06-13 06:06:20.634928
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    class TestModule(object):
        def __init__(self, fail_json_arguments):
            self.fail_json_arguments = fail_json_arguments
        def fail_json(self, **kwargs):
            self.assert_args = kwargs
            raise Exception(kwargs['msg'])
        def run_command(self, cmd, use_unsafe_shell=False):
            if self.fail_json_arguments:
                return (1, '', 'an error occurred')
            else:
                return (0, 'completed successfully', '')

    module = TestModule(True)
    rpm_key = RpmKey(module)

# Generated at 2022-06-13 06:06:25.982583
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    rpm_key = RpmKey(None)
    assert rpm_key.normalize_keyid('adeadb33f') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xadeadb33f') == 'DEADB33F'
    assert rpm_key.normalize_keyid(' 0xadeadb33f') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xadeadb33f ') == 'DEADB33F'


# Generated at 2022-06-13 06:06:30.624232
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import os
    import tempfile
    from ansible.module_utils.six import PY2

    from .rpm_key import RpmKey

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.urls import fetch_url
    class DummyModule(object):
        def __init__(self):
            self.params = {
                'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt',
                'state': 'present'
            }

        def fail_json(self, msg):
            raise Exception(msg)

        def get_bin_path(self, name, required=True):
            return name


# Generated at 2022-06-13 06:06:35.422245
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    """Method getkeyid of class RpmKey"""
    class FakeModule:
        pass
    key_obj = RpmKey(FakeModule)
    assert key_obj.getkeyid("/test/test-file.gpg") == "0xDEADB33F"


# Generated at 2022-06-13 06:08:53.618284
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    global self
    self.module.check_mode = False
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

# Generated at 2022-06-13 06:09:05.145712
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    class Module:
        def __init__(self):
            self.fail_json = lambda **kwargs: sys.exit(1)
            self.run_command = lambda command, shell=True: (0, '', '')

    class MockFile(object):
        def __init__(self):
            self.readlines = lambda: ['gpg-pubkey-deadb33f-57c3dbd3', 'gpg-pubkey-deadb33f-57c3dbd4']

    class MockFile2(object):
        def __init__(self):
            self.readlines = lambda: []

    assert RpmKey(Module()).is_key_imported('deadb33f')
    assert not RpmKey(Module()).is_key_imported('deadb33g')

# Generated at 2022-06-13 06:09:11.151978
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    def execute_command(self, cmd):
        # Reproduce the output of the gpg command
        expected_fingerprint = 'CFAF00D2F64E0537'
        if cmd == [self.gpg, '--no-tty', '--batch', '--with-colons', '--fixed-list-mode', '--with-fingerprint', 'test_keyfile']:
            return expected_fingerprint, ''
        else:
            return '', ''

    def isfile(self, keyfile):
        if keyfile == 'test_keyfile':
            return True
        return False

    rpm_key = RpmKey(object())
    rpm_key.getfingerprint = RpmKey.getfingerprint.__func__

# Generated at 2022-06-13 06:09:17.879881
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    from ansible.module_utils.basic import AnsibleModule
    from mock import MagicMock
    m = AnsibleModule(argument_spec={})
    m.run_command = MagicMock(return_value=(0, '', ''))
    m.check_mode = False
    m.fail_json = MagicMock()
    k = RpmKey(m)
    k.drop_key('0xABCEE5214')
    m.run_command.assert_called_once_with([k.rpm, '--erase', '--allmatches', 'gpg-pubkey-abcEE5214'])



# Generated at 2022-06-13 06:09:23.648034
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import mock
    module = mock.Mock()
    module.params = {'state': 'present', 'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'}
    module.check_mode = False
    module.cleanup = mock.Mock()
    module.fail_json = mock.Mock()
    module.get_bin_path = mock.Mock(return_value=True)
    module.run_command = mock.Mock()

    os.path.exists = mock.Mock(return_value=True)

    def test_fetch_url_func(*args, **kwargs):
        return ('PGP PUBLIC KEY BLOCK', 'http://apt.sw.be/RPM-GPG-KEY.dag.txt')
