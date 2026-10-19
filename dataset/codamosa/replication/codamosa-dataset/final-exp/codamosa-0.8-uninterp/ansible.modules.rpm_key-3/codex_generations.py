

# Generated at 2022-06-13 05:59:48.283855
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    import ansible
    assert is_pubkey(RpmKey(ansible.module_utils.basic.AnsibleModule(dict(key='http://apt.sw.be/RPM-GPG-KEY.dag.txt'))).fetch_key('http://apt.sw.be/RPM-GPG-KEY.dag.txt'))


# Generated at 2022-06-13 05:59:55.554278
# Unit test for constructor of class RpmKey
def test_RpmKey():
    a = AnsibleModule(
    argument_spec=dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        key=dict(type='str', required=True, no_log=False),
        fingerprint=dict(type='str'),
        validate_certs=dict(type='bool', default=True),
    ),
    supports_check_mode=True,
    )

    run = RpmKey(a)
    # Test with url as key
    a.params['key'] = 'https://www.apache.org/dist/ant/KEYS'
    run = RpmKey(a)
    # Test with a file path as key
    a.params['key'] = './KEYS'
    run = RpmKey(a)
    # Test with a keyid as key

# Generated at 2022-06-13 06:00:01.570427
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    # Create the object
    obj = RpmKey()
    # Method to be tested
    fingerprint = obj.getfingerprint(keyfile)
    # Unit test

# Generated at 2022-06-13 06:00:10.573058
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    # Creation of function variables
    # Declare module
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    RpmKey_self = RpmKey(module)
    RpmKey_self.module = module
    RpmKey_self.rpm = RpmKey_self.module.get_bin_path('rpm', True)
    state = module.params['state']
    key = module.params['key']
    fingerprint = module.params['fingerprint']

# Generated at 2022-06-13 06:00:18.793558
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
    assert(rpmkey.normalize_keyid('0xDEADB33F') == 'DEADB33F')
    assert(rpmkey.normalize_keyid('0XDEADB33F') == 'DEADB33F')
    assert(rpmkey.normalize_keyid('DEADB33F') == 'DEADB33F')


# Generated at 2022-06-13 06:00:27.816378
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
    test_obj = RpmKey(module)
    # Test with leading 0x
    expected_keyid = 'DEADBEEF'
    given_keyid = '0xDEADBEEF'
    assert test_obj.normalize_keyid(given_keyid) == expected_keyid
    given_keyid = '0XDEADBEEF'
    assert test_obj.normal

# Generated at 2022-06-13 06:00:38.383231
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    class RpmKey:
        def __init__(self, module):
            self.module = module
            self.module.params['state'] = 'absent'
            self.module.params['key'] = '0C7E4D68'
            self.rpm = '/bin/rpm'
    import unittest


# Generated at 2022-06-13 06:00:39.281989
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    pass


# Generated at 2022-06-13 06:00:52.085054
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    mock_module = Mock(name='mock_module')
    mock_module.run_command.side_effect = [(1, '', ''), (0, '', '')]

    rpm_key = RpmKey(mock_module)
    # Checking that the command has been called twice with the correct arguments, one for check_mode and one for the actual execution
    rpm_key.drop_key('deadbeef')


# Generated at 2022-06-13 06:00:58.013517
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    tmpfd, tmpfile = tempfile.mkstemp()
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True
    )
    print(tmpfile)
    cmd = "echo -e 'ok' > %s" % tmpfile
    p = subprocess.Popen(cmd, shell=True)
    p.communicate()
    assert p.returncode == 0
    rpmkey = RpmKey(module)
    assert rpmkey.drop_key("0xDEADBEEF") == 'ok'

# Generated at 2022-06-13 06:01:23.404254
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    # Init
    keys = ['deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef',
            'deadbeef'
            ]

# Generated at 2022-06-13 06:01:34.577646
# Unit test for method is_keyid of class RpmKey
def test_RpmKey_is_keyid():
    module = AnsibleModule(argument_spec=dict(),supports_check_mode=True)
    rpmkey = RpmKey(module)
    assert rpmkey.is_keyid('0x12345678')
    assert rpmkey.is_keyid('12345678')
    assert rpmkey.is_keyid('0X87654321')
    assert not rpmkey.is_keyid('0x1234567')
    assert not rpmkey.is_keyid('0x123456789')
    assert not rpmkey.is_keyid('1234567')
    assert not rpmkey.is_keyid('abcdefg')
    assert not rpmkey.is_keyid('ABCDEFG')
    assert not rpmkey.is_keyid('0xABCDEFG')

# Generated at 2022-06-13 06:01:39.254574
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    rpm_key = RpmKey(module)
    args = [rpm_key.rpm, '--import', 'keyfile']
    rpm_key.execute_command = MagicMock(return_value=(0, '', ''))
    rpm_key.import_key('keyfile')
    rpm_key.execute_command.assert_called_with(args)

# Generated at 2022-06-13 06:01:48.262680
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils.common.process import get_bin_path
    test_module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 06:01:51.062166
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    test = RpmKey()
    assertEqual(test.getfingerprint(), True)

# Generated at 2022-06-13 06:01:59.940127
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    class mock_AnsibleModule():
        def __init__(self, **kwargs):
            self.check_mode = False
            self.params = kwargs

    class mock_AnsibleRunner():
        def __init__(self, **kwargs):
            self.module = mock_AnsibleModule(**kwargs)

        def get_bin_path(self, name, **kwargs):
            return name

        def run_command(self, cmd, **kwargs):
            return 0, "", ""

    runner = mock_AnsibleRunner(state='present', key='testkey')
    rpm_key = RpmKey(runner)

    def execute_command_mock(cmd):
        if cmd:
            return 0, "", ""
        else:
            raise Exception('command missing')


# Generated at 2022-06-13 06:02:06.679243
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    import pytest
    mod = pytest.Mock()
    keyid = 'DEADB33F'
    rpm = 'rpm'
    cmd = rpm + ' --erase --allmatches gpg-pubkey-' + keyid[-8:].lower()
    RpmKey(mod).drop_key(keyid)
    mod.run_command.assert_called_with(cmd, use_unsafe_shell=True)

# Generated at 2022-06-13 06:02:14.120554
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    class MockRpmKey(RpmKey):
        def __init__(self, module):
            pass
    class MockModule(object):
        def getkeyid(self, keyfile):
            return 'DEADB33F'

    class MockModule2(object):
        def getkeyid(self, keyfile):
            return 'DEADB33F00'

    # Validate correct keyid
    rpm_key = MockRpmKey(MockModule)
    assert rpm_key.normalize_keyid('DEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xDEADB33F') == 'DEADB33F'
    assert rpm_key.normalize_keyid('0xDEADB33F\n') == 'DEADB33F'

   

# Generated at 2022-06-13 06:02:23.097063
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    mock_module = MagicMock()
    mock_module.run_command.side_effect = [(0, 'stdout', '')]
    mock_module.fail_json.side_effect = Exception('fail_json')

    rpm_key = RpmKey(mock_module)
    rpm_key.import_key('keyfile')

    mock_module.run_command.assert_called_with(['rpm', '--import', 'keyfile'])



# Generated at 2022-06-13 06:02:29.806645
# Unit test for method fetch_key of class RpmKey
def test_RpmKey_fetch_key():
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    key = "https://example.com/key1"
    set_module_args(dict(
    state='present',
    key=key
    ))
    # Download a key from url, returns a valid path to a gpg key
    rsp, info = fetch_url(module, key)
    if info['status'] != 200:
            module.fail_json(msg="failed to fetch key at %s , error was: %s" % (key, info['msg']))

    key = rsp.read()


# Generated at 2022-06-13 06:03:07.802507
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    from mock import patch
    import tempfile

    # Mock the module
    mock_module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['absent', 'present']),
            key=dict(type='str', required=True, no_log=False),
            fingerprint=dict(type='str'),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    # Fixtures
    empty_stdout = ""

# Generated at 2022-06-13 06:03:13.380574
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    """ Method getkeyid of class RpmKey should return the expected keyid """
    cls = RpmKey("")
    keyfile = 'files/test_gpg.pub'
    result = cls.getkeyid(keyfile)
    assert result == '64A7D1C4'

# Generated at 2022-06-13 06:03:19.491957
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    module = AnsibleModule(argument_spec={})
    rpm_key = RpmKey(module)
    import os
    keyfile = os.path.join(os.path.dirname(__file__), 'test/test_key.txt')
    assert rpm_key.getfingerprint(to_bytes(keyfile)) == "EBC6212C62B1C734026B21222A20E52146B8D79E6"

# Generated at 2022-06-13 06:03:30.728031
# Unit test for constructor of class RpmKey
def test_RpmKey():
    import os
    import shutil
    from ansible.module_utils.basic import AnsibleModule
    from tempfile import mktemp
    from ansible.module_utils.urls import fetch_url

    def check_file(path):
        try:
            with open(path, 'r') as fd:
                return True
        except IOError:
            return False

    def create_keyfile(path, key):
        with open(path, 'w') as keyfile:
            keyfile.write(key)

    def fetch_url_side_effect(module, url):
        return (key, {'status': 200})

    def remove_keyfile(keyfile):
        if os.path.isfile(keyfile):
            os.remove(keyfile)


# Generated at 2022-06-13 06:03:38.882723
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

    # Mock the urlopen function
    # source: https://stackoverflow.com/questions/19079082/how-to-mock-openurlrequest-in-python3-3-3
    import urllib
    old_urlopen = urllib.request.urlopen
    mock_content = b"MOCKED CONTENT"

# Generated at 2022-06-13 06:03:49.171885
# Unit test for method getkeyid of class RpmKey
def test_RpmKey_getkeyid():
    from unittest.mock import Mock, patch
    from tempfile_mock import mkstemp_mock


# Generated at 2022-06-13 06:04:01.535838
# Unit test for constructor of class RpmKey
def test_RpmKey():
    class FakeModule:
        def __init__(self,params):
            self.params = params

        def get_bin_path(self, name, required=False):
            return name

        def fail_json(self, msg):
            pass

        def run_command(self, cmd, use_unsafe_shell=True):
            return 0, '', ''

        def exit_json(self, changed=True):
            pass

    class FakeCommand:
        def __init__(self, rc, stdout, stderr):
            self.rc = rc
            self.stdout = stdout
            self.stderr = stderr

    import_command = FakeCommand(0, '', '')
    erase_command = FakeCommand(0, '', '')


# Generated at 2022-06-13 06:04:08.390869
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    from mock import patch
    import rpm_key
    obj = rpm_key.RpmKey(None)
    cmd = ['gpg', '--no-tty', '--batch', '--with-colons', '--fixed-list-mode', '-']
    with patch("rpm_key.RpmKey.module.run_command") as mock_run_command:
        mock_run_command.return_value = (0, '', '')
        stdout, stderr = obj.execute_command(cmd)
        assert stdout == ''
        assert stderr == ''

# Generated at 2022-06-13 06:04:20.309155
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():
    import sys
    sys.path.insert(0, '/tmp/ansible_rpm_key_payload/library')
    import ansible.utils
    import ansiballz
    mock_ansible_module = ansiballz.AnsiballzMethod(
        'ansible.module_utils.basic',
        'AnsibleModule',
        _ansiballz_parameters={},
        _uses_shell=False,
        _uses_binary_modules=False,
    )
    mock_ansible_module.params = {
  "validate_certs": True,
  "state": "present",
  "fingerprint": "",
  "key": "/tmp/ansible_rpm_key_payload/library/rpm_key/test.gpg"
}
    mock_ansible_module.check_

# Generated at 2022-06-13 06:04:32.225561
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native
    from ansible.module_utils.urls import fetch_url
    import os.path

    # Setup mock AnsibleModule, fetch_url functions
    m = basic.AnsibleModule(argument_spec={})
    m.exit_json = lambda: exit(0)
    m.fail_json = lambda msg: exit(1)
    m.cleanup = lambda: exit(0)
    m.run_command = lambda command, use_unsafe_shell: (0, '', '')
    m.get_bin_path = lambda cmd, required=False, opt_dirs=[] : cmd
    m.add_cleanup_file = lambda: exit(0)

# Generated at 2022-06-13 06:05:42.435064
# Unit test for method is_key_imported of class RpmKey
def test_RpmKey_is_key_imported():
    class MockModule(object):
        class MockFail_json(object):
            def __init__(self, msg):
                self.msg = msg

            def __call__(self, *args, **kwargs):
                print(self.msg)

        class MockRun_command(object):
            def __init__(self, rc, stdout, stderr):
                self.rc, self.stdout, self.stderr = rc, stdout, stderr

            def __call__(self, *args):
                return self.rc, self.stdout, self.stderr

        def __init__(self, dict_arg):
            self.params = dict_arg
            self.fail_json = self.MockFail_json('')

# Generated at 2022-06-13 06:05:56.276951
# Unit test for method import_key of class RpmKey
def test_RpmKey_import_key():
    import io
    import sys

    from ansible.module_utils._text import to_bytes

    # Create a temporary file to use as the gpg key
    tmpfd, tmpname = tempfile.mkstemp()
    tmpfile = os.fdopen(tmpfd, 'w+b')

# Generated at 2022-06-13 06:06:04.300648
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    """Verify the getfingerprint method of the class RpmKey works as expected"""
    import os
    import tempfile
    import ansible.module_utils.basic
    import ansible.module_utils.urls
    import ansible.module_utils._text
    import ansible.module_utils.action_common_attributes


# Generated at 2022-06-13 06:06:15.615370
# Unit test for method execute_command of class RpmKey
def test_RpmKey_execute_command():
    module = DummyAnsibleModule(check_mode=False)

    # We will write a script to stdin, because we can't
    # test if sys.stdin is a tty from Python.
    # The script will, then, detect if it is being executed
    # with a TTY or not.
    # If it is not being executed with a tty, it will
    # write "no tty" to stdout and return 0.
    # Otherwise, it will write "has tty" and return 1.
    script = textwrap.dedent("""
#!/bin/sh
if tty -s ; then
   echo "has tty"
   exit 1
else
   echo "no tty"
   exit 0
fi
""")

    # The objective of the test is to verify if
    # RpmKey.execute_

# Generated at 2022-06-13 06:06:20.511629
# Unit test for constructor of class RpmKey
def test_RpmKey():
    # Set module_args for unit test
    module_args = dict(
        key="/path/to/RPM-GPG-KEY.dag.txt",
        state="present"
    )
    # Set module for unit test
    module = AnsibleModule(argument_spec=module_args)
    # Test constructor
    RpmKey(module)

# Generated at 2022-06-13 06:06:27.531409
# Unit test for method drop_key of class RpmKey
def test_RpmKey_drop_key():

    class MockModule(object):
        def __init__(self, params=None):
            self.params = params
            self.result = {"changed": False}

        def fail_json(self, msg, **kwargs):
            self.result['failed'] = True
            if 'msg' not in self.result:
                self.result['msg'] = msg
            else:
                self.result['msg'] += "\n%s" % msg

        def run_command(self, cmd, use_unsafe_shell=True):
            self.cmd = cmd
            return 0, "", ""

    module_inst = MockModule({'state': 'present',
                              'key': 'DEADBEEF',
                              })
    rpm_key = RpmKey(module_inst)

# Generated at 2022-06-13 06:06:41.074082
# Unit test for method getkeyid of class RpmKey

# Generated at 2022-06-13 06:06:46.002822
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
        rpm_key = RpmKey(None)
        ret = rpm_key.getfingerprint_from_file('tests/files/pubring.gpg')
        assert ret == 'EBC6E12C62B1C7B1EB96F1F9B7B98B0580C0ECC3'


# Generated at 2022-06-13 06:06:53.090295
# Unit test for constructor of class RpmKey
def test_RpmKey():
    from ansible.module_utils import basic
    from ansible.module_utils.urls import fetch_url
    from ansible.module_utils import common
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils import action_common_attributes
    from ansible.module_utils import action_plugins
    from ansible.module_utils._text import to_native
    import os.path
    import tempfile
    import re

    # Testing key fetching function.
    # First we try with an invalid url
    url = 'http://nourlhere.com'

# Generated at 2022-06-13 06:07:03.645205
# Unit test for method getfingerprint of class RpmKey
def test_RpmKey_getfingerprint():
    class Attribute():
        def __init__(self):
            self.rc = 0
            self.stdout = ''
            self.stderr = ''

    class Module():
        def __init__(self):
            self.run_command = Attribute()

        def fail_json(self, msg):
            raise Exception(msg)

    class RpmKey():
        def __init__(self):
            self.module = Module()
            self.gpg = ''

    getfingerprint = RpmKey()
    keyfile = '/doc/test/test_RpmKey_getfingerprint.gpg'
    with open(keyfile) as f:
        key = f.read()
    getfingerprint.module.run_command.stdout = key