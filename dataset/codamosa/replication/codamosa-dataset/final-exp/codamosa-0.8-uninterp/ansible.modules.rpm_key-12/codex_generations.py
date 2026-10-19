

# Generated at 2022-06-13 05:59:54.276398
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    from mock import patch
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.urls import open_url

    x = RpmKey(AnsibleModule(argument_spec={ "state": {"choices": ['present', 'absent'], "type": 'str', "default": 'present' },
                                             "fingerprint": {"type": 'str'},
                                             "key": {"required": True, "type": 'str'},
                                             "validate_certs": {"type": 'bool', "default": True} }))
    x.module.run_command = lambda args, **kwargs: (0, "", "")

# Generated at 2022-06-13 06:00:02.841874
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    from ansible.module_utils.six import PY3
    from ansible.modules.system.rpm_key import RpmKey
    from ansible.module_utils.basic import AnsibleModule
    class MyClass:
      def __init__(self, keystr):
         self.keystr = keystr
         self.keystr = keystr
    x = MyClass("0x01234567")
    r = RpmKey(x)
    assert r.is_keyid("0x01234567") == True

# Generated at 2022-06-13 06:00:11.327795
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    ''' Test if method is_key_imported correctly identifies presense of keys in rpm db '''
    # test if is_key_imported returns false if no key is installed
    def exec_command_no_key(self, cmd):  # pragma: no cover
        ''' simulate the output of an rpm command when no key is installed on the system '''
        return 1, '', ''
    from mock import patch
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:00:15.102453
# Unit test for constructor of class RpmKey
def test_RpmKey():
    rpmkey = RpmKey(mo=None)
    assert rpmkey.rpm != None
    assert rpmkey.gpg != None


# Generated at 2022-06-13 06:00:16.260463
# Unit test for constructor of class RpmKey
def test_RpmKey():
    rk = RpmKey('')

# Generated at 2022-06-13 06:00:26.437598
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
    module.run_command = MagicMock(return_value=[0,'stdout', None])
    # Normal case: run a valid command, return a tuple with three elements and isinstance of [str, str, str]
    rpm_key = RpmKey(module)
    result = rpm_key.execute_command([rpm_key.rpm, '--import', '/tmp/gpg_key'])

# Generated at 2022-06-13 06:00:36.452603
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    from ansible.module_utils.common.collections import ImmutableDict
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
        bypass_checks=True
    )
    module.params = ImmutableDict(dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        validate_certs=dict(type='bool', default=True),
    ))
    rpmkey

# Generated at 2022-06-13 06:00:42.159445
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    key = "http://apt.sw.be/RPM-GPG-KEY.dag.txt"
    tmpfd, tmpname = tempfile.mkstemp()
    tmpfile = os.fdopen(tmpfd, "w+b")
    tmpfile.write(b'sam')
    tmpfile.close()
    instance = RpmKey(tmpname)
    assert instance.fetch_key() == 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'

# Generated at 2022-06-13 06:00:45.218916
# Unit test for constructor of class RpmKey
def test_RpmKey():
    with pytest.raises (Exception) as info:
        RpmKey(None)
    assert 'Need to have a module' in str(info.value)

# Generated at 2022-06-13 06:00:55.700157
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Create a temporary module that does nothing
    class MyModule():
        def __init__(self):
            pass
        def get_bin_path(self, name, required=False):
            return name
        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, "", ""
        def fail_json(self, msg):
            raise Exception("fail_json: "+msg)
        def cleanup(self, keyfile):
            pass
        def add_cleanup_file(self, keyfile):
            pass
    # Create a tmp file
    tmpfd, tmpname = tempfile.mkstemp()
    tmpfile = os.fdopen(tmpfd, "w+b")

# Generated at 2022-06-13 06:01:17.505369
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    rpmkey = RpmKey()
    key = os.path.join(os.path.dirname(__file__), 'fixtures', 'testkey.asc')
    expected_fingerprint = '9F4C8A0EDA1F01F180E788D5B5B5E25EDE6E687A'
    assertRpmKey.rpmkey.getfingerprint(key) == expected_fingerprint
 

# Generated at 2022-06-13 06:01:22.151008
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    # For testing, we need an object of class AnsibleModule. This will parse the commandline arguments,
    # set up logging, etc.
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    # For testing, we need to turn off authentification, so that fetch_url can be mocked.
    # For some reason, the argument `follow_redirects` does not work, so we have to set it afterwards.
    module._authenticate = lambda: None
    module

# Generated at 2022-06-13 06:01:28.870415
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    test_module = AnsibleModule(argument_spec={})
    # Tested method
    test_RpmKey = RpmKey(test_module)
    # The actual key used in the test
    key_RpmKey = "http://apt.sw.be/RPM-GPG-KEY.dag.txt"
    # The expected resulting gpg key file path
    expected_result_RpmKey = "/tmp/ansible_RpmKey_payload.uZ7Lzg"
    
    # We remove the file if it already exists, to ensure our test is independent and consistent
    if os.path.isfile(expected_result_RpmKey):
        os.remove(expected_result_RpmKey)
    
    # We call fetch_key with our test parameters

# Generated at 2022-06-13 06:01:39.254911
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    assert RpmKey.is_keyid("0xAAA")
    assert RpmKey.is_keyid("AAA")
    assert not RpmKey.is_keyid("0xAA")
    assert not RpmKey.is_keyid("AA")
    assert not RpmKey.is_keyid("A")
    assert not RpmKey.is_keyid("AAAB")
    assert not RpmKey.is_keyid("AAA A")
    assert not RpmKey.is_keyid("")
    assert not RpmKey.is_keyid("0x")
    assert not RpmKey.is_keyid("0x0")
    assert not RpmKey.is_keyid("10xA")
    assert not RpmKey.is_keyid("10x0")
    assert not RpmKey.is_

# Generated at 2022-06-13 06:01:48.262391
# Unit test for constructor of class RpmKey
def test_RpmKey():
    class FakeModule(object):
        def __init__(self, argument_spec, supports_check_mode):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.params = {}
            self.fail_json = lambda msg=None, **kwargs: None
            self.run_command = lambda cmd: None
            self.exit_json = lambda changed=None: None

        def get_bin_path(self, name, required=False):
            if required:
                return name
            else:
                return None

        def add_cleanup_file(self, path):
            pass

        def cleanup(self, path):
            pass

    attrs = {'params':
                {'state': 'present',
                 'key': 'key'}}

    key = R

# Generated at 2022-06-13 06:01:49.706205
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    pass

# Generated at 2022-06-13 06:01:51.846362
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    RpmKey.execute_command(None, ['./test_rpm_key_module.py'])


# Generated at 2022-06-13 06:01:56.620842
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    class RpmKey:
        def execute_command(self, abc):
            assert abc == ['/usr/bin/rpm', '--import', '/tmp/test.gpg'], "Test failed!"

    command = RpmKey()
    command.execute_command = execute_command
    command.import_key('/tmp/test.gpg')

# Generated at 2022-06-13 06:02:01.304939
# Unit test for method fetch_key of class RpmKey

# Generated at 2022-06-13 06:02:04.803146
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import tests.lib.rpm_key
    import test.lib.urls
    test_instance = tests.lib.rpm_key.RpmKey(test.lib.urls.fetch_url)
    assert test_instance

# Generated at 2022-06-13 06:02:30.177109
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import os
    import unittest
    import tempfile
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:02:44.090054
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Basic case
    _fingerprint = 'EBC6 E12C 62B1 C734 026B  2122 A20E 5214 6B8D 79E6'
    _keyfile = fetch_file('RPM-GPG-KEY-dag', content_type='text/plain')

    r = RpmKey(AnsibleModule(argument_spec={}))
    assert r.getfingerprint(_keyfile) == _fingerprint.replace(' ', '').upper()

    # Test case where key is not public, but a secret key
    _keyfile = fetch_file('RPM-GPG-KEY-dag-priv', content_type='text/plain')
    exc = None

    try:
        r.getfingerprint(_keyfile)
    except Exception as err:
        exc = err


# Generated at 2022-06-13 06:02:53.771176
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

    r = RpmKey( module )
    key = 'DAD95197'
    keyfile = '/path/to/key.gpg'
    r.getfingerprint( keyfile )

# Generated at 2022-06-13 06:02:59.954116
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import ansible.module_utils.basic as basic
    basic.AnsibleModule = object
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def __init__(self):
            args = dict(
                state=dict(type='str', default='present', choices=['absent', 'present']),
                key=dict(type='str', required=True, no_log=False),
                fingerprint=dict(type='str'),
                validate_certs=dict(type='bool', default=True),
            )
            self.params = dict(
                state='present',
                key='key',
                fingerprint='fingerprint',
                validate_certs=True,
            )
            self.check_mode = False
            self.run_command = run_command


# Generated at 2022-06-13 06:03:04.581779
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    # Should fail with mocked fail_json
    key = RpmKey()
    key.module.run_command = Mock(return_value=(1, 'stdout', 'stderr'))
    key.module.fail_json = Mock()
    key.execute_command(['rpm', '-q'])
    key.module.fail_json.assert_called

# Generated at 2022-06-13 06:03:14.619687
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    testrpmkey = RpmKey(None)
    assert testrpmkey.is_keyid('DEADB33F')
    assert not testrpmkey.is_keyid('DEADB33F1')
    assert testrpmkey.is_keyid('0xDEADB33F')
    assert testrpmkey.is_keyid('0xDEADB33F1')
    assert not testrpmkey.is_keyid('http://test.com/test.txt')
    assert not testrpmkey.is_keyid('/test')

# Generated at 2022-06-13 06:03:22.754849
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    mock = {
        'rpm': 'rpm',
        'run_command': Mock(return_value=(0,'Success','')),
        'check_mode': True
    }
    o = RpmKey(mock)
    o.drop_key('abcdef12')
    mock['run_command'].assert_called_with(
        ['rpm', '--erase', '--allmatches', 'gpg-pubkey-12345678']
    )


# Generated at 2022-06-13 06:03:31.712119
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Create a mock module with mock responses
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=('', ''))
    module.add_cleanup_file = MagicMock()

    # Test with a correct url
    rpmkey = RpmKey(module)
    keyfile = rpmkey.fetch_key('http://sample.com')
    assert os.path.isfile(keyfile)

    # Test with a malformed url
    with pytest.raises(SystemExit):
        rpmkey.fetch_key('http://sample.com/malformed_key')



# Generated at 2022-06-13 06:03:44.728702
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils._text import to_native
    import re
    import os
    import tempfile
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    rkey = RpmKey(module)
    rkey.gpg = 'gpg2'
    rkey.module = module
    rkey.module

# Generated at 2022-06-13 06:03:49.660046
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    keyid = '0xDEADB33F'
    rpm = RpmKey(keyid)
    # when key is imported and is_key_imported method is called
    # should return True
    result = rpm.is_key_imported(keyid)
    assert result == True



# Generated at 2022-06-13 06:04:34.164750
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from mock import MagicMock
    mod_obj = MagicMock()
    mod_obj.params = {
        'state': 'present',
        'key': 'DEADBEEF',
        'fingerprint': None,
        'validate_certs': True,
    }
    mod_obj.check_mode = False
    mod_obj.get_bin_path = MagicMock(return_value='/usr/bin/rpm')
    RpmKey(mod_obj)

    mod_obj = MagicMock()
    mod_obj.params = {
        'state': 'absent',
        'key': 'DEADBEEF',
        'fingerprint': None,
        'validate_certs': True,
    }
    mod_obj.check_mode = False
    mod_obj.get_bin_

# Generated at 2022-06-13 06:04:42.025539
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

    class args:
        keystr = None

    assert rpm_key.is_keyid(args) == False
    args.keystr = '0xC9943CF5'
    assert rpm_key.is_keyid(args) == True
    args.keystr = 'C9943CF5'

# Generated at 2022-06-13 06:04:42.985110
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():

    assert 1 == 1

# Generated at 2022-06-13 06:04:47.842437
# Unit test for constructor of class RpmKey
def test_RpmKey():
    module_args = dict(
        state='present',
        key='/path/to/key.gpg',
        fingerprint='',
        validate_certs=True,
    )
    test_object = RpmKey(AnsibleModule(**module_args))

    assert test_object.rpm is not None
    assert test_object.gpg is not None

# Generated at 2022-06-13 06:04:58.433471
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

    keyfile = "../tests/unit/modules/ansible_collections/ansible/builtin/rpm_key/public.key"
    rpmkey = RpmKey(module)
    assert rpmkey.getfingerprint(keyfile) == "EBC6E12C62B1C734026B2122A20E52146B8D79E6"



# Generated at 2022-06-13 06:05:06.261173
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module_args = dict(
        state='present',
        key='http://apt.sw.be/RPM-GPG-KEY.dag.txt',
        fingerprint=None,
    )

    module = AnsibleModule(
        argument_spec=module_args,
    )

    rpm_key = RpmKey(module)

    cmd = rpm_key.rpm + ' -q  gpg-pubkey --qf "%{description}" | ' + rpm_key.gpg + ' --no-tty --batch --with-colons --fixed-list-mode -'
    rc, stdout, stderr = rpm_key.module.run_command(cmd)
    expected = stderr

    stdout, stderr = rpm_key.execute_command(cmd)
    assert stderr == expected


# Generated at 2022-06-13 06:05:08.936239
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    assert RpmKey.fetch_key("http://apt.sw.be/RPM-GPG-KEY.dag.txt") != None

# Generated at 2022-06-13 06:05:15.434782
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    rpmkey = RpmKey(AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    ))


# Generated at 2022-06-13 06:05:26.534916
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import tempfile
    import os

    class TestModule():
        def __init__(self):
            self.params = {'key': "http://somedomain/somepath"}
            self.called_method = None

        def fail_json(self, msg):
            raise Exception(msg)

        def add_cleanup_file(self, path):
            os.unlink(path)

        def run_command(self, cmd, use_unsafe_shell=True):
            self.called_method = cmd
            return 0, "TEST_KEY", ""

    class TestFetchUrl():
        def __init__(self):
            self.content = "TEST_KEY"

        def read(self):
            return self.content

        def info(self):
            return {}


# Generated at 2022-06-13 06:05:36.319763
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    """
    Check function RpmKey.execute_command.
    """
    # Create a mock RpmKey object
    class MockModule(object):

        def __init__(self):
            self.params = dict([
                ('state', 'present'),
                ('key', '/path/to/key.gpg'),
                ('fingerprint', 'DEADBEEF'),
            ])

        def fail_json(self, msg):
            raise AssertionError(msg)

        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, '', ''

    rpm_key = RpmKey(MockModule())
    # Check command
    # AssertionError should be raised

# Generated at 2022-06-13 06:06:51.481823
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    class RpmModuleDummy:

        def __init__(self):
            self.fail = False

        def run_command(self, cmd):
            if self.fail:
                return 1, 'foo', 'bar'
            else:
                return 0, 'foo', 'bar'

        def fail_json(self, msg):
            print(msg)

    rpm_module = RpmModuleDummy()
    rpm_key = RpmKey(rpm_module)

    # case 0: is_key_imported return true if key is found in rpm database
    assert rpm_key.is_key_imported('ea5d5e0c') is True

    # case 1: is_key_imported return false if key is not found in rpm database
    rpm_module.fail = True
    assert rpm_key.is_key_im

# Generated at 2022-06-13 06:07:02.161722
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    import subprocess

    class MockModule:
        def __init__(self):
            self.run_command = Mock(return_value=(0, "", ""))

    # Test case: no issues
    command = ["ls"]
    mock_module = MockModule()
    rpm_key = RpmKey(mock_module)
    rpm_key.execute_command(command)

    assert mock_module.run_command.called

    # Test case: run_command return non-zero exit code
    command = ["ls"]
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(1, "", ""))

    rpm_key = RpmKey(mock_module)
    with pytest.raises(AnsibleExitJson) as exec_info:
        rpm_key.execute_

# Generated at 2022-06-13 06:07:09.850253
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

    rpm_key = RpmKey(module)
    assert rpm_key.is_key_imported('0x2122A20E52146B8D') == False
    assert rpm_key.is_key_imported('0x2122A20E52146B8D') == False
    assert rpm_key.is_key_imported('2122A20E52146B8D') == False

# Generated at 2022-06-13 06:07:18.270757
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.module_utils.six.moves import StringIO
    import sys
    import pytest
    from mock import MagicMock

    module_args = dict(
        state='present',
        key='test_key_file',
        fingerprint='test_fingerprint',
        validate_certs=True # Surpress error message if module is executed outside a group_vars
    )

    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )


# Generated at 2022-06-13 06:07:31.145300
# Unit test for method normalize_keyid of class RpmKey
def test_RpmKey_normalize_keyid():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_native

    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda **args: None
    module.fail_json = lambda **args: None
    module.params = {
        'state': 'present',
        'key': 'http://apt.sw.be/RPM-GPG-KEY.dag.txt',
        'validate_certs': True,
    }
    url = 'http://apt.sw.be/RPM-GPG-KEY.dag.txt'
    rpm_key = RpmKey(module)


# Generated at 2022-06-13 06:07:41.215457
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():

    import unittest
    import ansible
    from ansible.module_utils.actions import AnsibleModule
    from ansible.module_utils.actions import _ANSIBLE_ARGS
    from ansible.module_utils.six.moves import StringIO

    module = AnsibleModule(argument_spec=dict())
    module.from_json = lambda data: unittest.TestCase().assertIn('stdout', data)

    # keyid is in the stdout of rpm -q
    module.run_command = lambda cmd, use_unsafe_shell=True: [0, 'stdout', 'stderr']
    ret = RpmKey(module).is_key_imported('deadb33f')
    assert ret == True

    # keyid is not in the stdout of rpm -q

# Generated at 2022-06-13 06:07:43.605100
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    module = AnsibleModule(argument_spec=dict())
    rpm_key = RpmKey(module)
    assert rpm_key.is_key_imported('aabbccdd')

# Generated at 2022-06-13 06:07:51.037279
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    import os
    import tempfile
    import StringIO
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.rpm import RpmKey

    def is_pubkey(string):
        """Verifies if string is a pubkey"""
        pgp_regex = ".*?(-----BEGIN PGP PUBLIC KEY BLOCK-----.*?-----END PGP PUBLIC KEY BLOCK-----).*"
        return bool(re.match(pgp_regex, string, re.DOTALL))

    # Create a GPG key to be used as a test case
    test_key = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 06:07:57.613839
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    rpm_key = RpmKey(module)
    cmd = '/bin/rpm'
    test_stdout = 'keyid'
    test_stderr = 'error: '
    test_rc = 1
    output = rpm_key.execute_command(cmd)
    assert output[0] is test_stdout
    assert output[1] is test_stderr

# Generated at 2022-06-13 06:08:09.235997
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class ModuleMock(object):
        name = 'ansible.builtin.rpm_key'
        check_mode = False
        no_log = False
        clean_traceback = False

        def run_command(self, cmd, use_unsafe_shell=False):
            return 0, 'fpr:::::::::EBC6E12C62B1C734' + cmd[4], ''

        def fail_json(self, msg):
            exit(1)

        def get_bin_path(self, *args, **kwargs):
            return 'gpg'

        def add_cleanup_file(self, tmpfile):
            pass

    class AnsibleModuleMock(object):
        def __init__(self, module):
            self.module = module
