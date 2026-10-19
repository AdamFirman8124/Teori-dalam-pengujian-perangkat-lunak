

# Generated at 2022-06-12 23:17:17.852237
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    # Mock up AnsibleModule.run_command
    # Set rc=0 and out to list of locales available on the system
    out = StringIO('''C
en_US.utf8
POSIX
''')

    def run_command(*args, **kwargs):
        return (0, out.read(), '')

    import ansible.module_utils.basic
    ansible.module_utils.basic.AnsibleModule.run_command = run_command

    # mock up the module
    am = AnsibleModule(argument_spec={})

    locale = get_best_parsable_locale(am)
    assert locale == 'C'
    locale = get_best_parsable_locale

# Generated at 2022-06-12 23:17:20.421537
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module= AnsibleModule(argument_spec={})

    locale = get_best_parsable_locale(module)
    assert locale == 'C'

# Generated at 2022-06-12 23:17:29.323521
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    fake_out = """
C
en_US.utf8
POSIX
fr_FR.utf8
C.utf8
en_US.utf8
POSIX
en_US.utf8
C.utf8
POSIX
"""
    from ansible.utils.path import unfrackpath, module_finder
    from ansible.utils.unicode import to_bytes
    from ansible.module_utils.basic import AnsibleModule as AM
    from ansible.module_utils.six import PY3

    am = AM()

    # Change to Fake module bin directory.
    orig_finder = module_finder()
    fake_bin = unfrackpath('/fake/bin/path')
    if PY3:
        fake_bin = to_bytes(fake_bin)
    module_finder.bin_dir = fake_bin

   

# Generated at 2022-06-12 23:17:39.911832
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for function get_best_parsable_locale
        :return:
    '''

    def run_mock_command(cmd, **kwargs):
        ''' Used in tests to mock the AnsibleModule.run_command function
        '''
        class MockResults(object):
            ''' MockResults class used to mock the AnsibleModule.run_command function
            '''
            def __init__(self, rc, out, err):
                self.rc = rc
                self.stdout = out
                self.stderr = err

        if cmd[-1] == "locale":
            return MockResults(0, """utf-8
C.utf8
en_US.utf8
C
POSIX""", '')

    # Mock AnsibleModule instance

# Generated at 2022-06-12 23:17:49.046956
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.six import PY3
    from ansible.module_utils import basic
    import pytest

    # prepare fake shell environment
    environ = {'PATH': '/usr/bin'}
    # ensure locale is in PATH
    environ['PATH'] = ':'.join(('/usr/bin', environ['PATH']))

    # mock module
    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)

    # mock module.run_command
    def run_command(args, **kwargs):
        if args == ['locale', '-a']:
            return (0, 'C.utf8\nC\nen_GB.utf8\nen_US.utf8\nPOSIX\n', '')

    module.run_command = run_command


# Generated at 2022-06-12 23:17:58.277783
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def get_bin_path(args):
        if args == 'locale':
            return args

    # Test when 'locale' command is not present in the system
    module = type(
        "AnsibleModule",
        (object,),
        dict(
            get_bin_path=get_bin_path,
            run_command=lambda self, args: (1, '', 'not found'),
        )
    )()

    result = get_best_parsable_locale(module, raise_on_locale=True)
    assert result == 'C'

    # Test when 'locale' command is present but there are no locales in the system

# Generated at 2022-06-12 23:18:09.403972
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    if sys.version_info[0] > 2:
        unicode = str

    # We don't test the module import, shell and get_bin_path
    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, args):
            if args == [unicode('locale'), unicode('-a')]:
                return 0, unicode('C.utf8\nC\nen_US.utf8'), ''
            else:
                raise Exception('Invalid run_command args')

    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def run_command(self, args):
            if args == [unicode('locale'), unicode('-a')]:
                return

# Generated at 2022-06-12 23:18:18.321698
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play_context import PlayContext
    from ansible.utils import context_objects as co

    class FakeModule(AnsibleModule):
        '''
        Class for unit-testing get_best_parsable_locale()
        '''
        def __init__(self):
            self.argument_spec = dict()
            self.ansible_version = '2.0.0'
            self.params = {}
            self.check_mode = False
            self.no_log = False
            self.play_context = PlayContext()
            super(FakeModule, self).__init__(self.argument_spec, bypass_checks=True, no_log=self.no_log)


# Generated at 2022-06-12 23:18:23.256502
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.parameters import is_executable
    from ansible.module_utils.basic import AnsibleModule

    # nansible module is needed for to get_bin_path
    nansible_module = AnsibleModule(argument_spec=dict())
    nansible_module.get_bin_path = is_executable

    # test empty env
    def mock_run_command(cmd, cwd=None, use_unsafe_shell=False, environ_update=None, executable=None):
        return (0, "", "")

    # needed for get_bin_path
    nansible_module.run_command = mock_run_command
    # needed for debug print
    nansible_module.fail_json = lambda exc: exc

# Generated at 2022-06-12 23:18:24.630735
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:18:39.435102
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import glob
    import tempfile
    import shutil
    import re
    import locale
    from ansible.module_utils import basic
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestGetBestParsableLocale(unittest.TestCase):

        def setUp(self):
            self.module = basic.AnsibleModule(
                argument_spec=dict()
            )
            self.module_path = os.path.abspath(os.path.curdir)
            self.temp_path = tempfile.mkdtemp()
            os.chdir(self.temp_path)
            os.mkdir('test_bins')
            os.chdir('test_bins')
            self.module.add_module

# Generated at 2022-06-12 23:18:49.330148
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os

    test_preferences = ['C.iso-8859', 'C.iso8859', 'C.utf8', 'C', 'POSIX']
    test_locale_a = os.linesep.join([
        'C',
        'en_AU',
        'posix',
        'C.iso-8859',
        'C.iso8859',
        'C.utf8',
        'C.utf-8',
        'POSIX',
    ])

    test_locale_b = os.linesep.join([
        'C',
        'C.utf8',
        'C.utf-8',
        'POSIX',
    ])


# Generated at 2022-06-12 23:18:59.968972
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    class MockModule:
        class MockFailJson:
            def __init__(self, rc=0, cmd=None, msg=None, stdout=None, stderr=None, changed=False):
                self.rc = rc
                self.cmd = cmd
                self.msg = msg
                self.stdout = stdout
                self.stderr = stderr
                self.changed = changed
                self.failed = False
                self.warnings = []
            def __call__(self, *args, **kwargs):
                raise Exception(kwargs['msg'])

        class MockRunCommand:
            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

# Generated at 2022-06-12 23:19:04.491405
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    best_parsable_locale = ansible.module_utils.basic.get_best_parsable_locale(ansible.module_utils.basic.AnsibleModule(argument_spec={}))
    print(best_parsable_locale)

if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:19:13.752627
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    test_module = ansible.module_utils.basic.AnsibleModule({})
    test_preferences = ['ar_SA.utf8', 'C.utf8', 'POSIX', 'C']
    test_raised_locale = get_best_parsable_locale(test_module, test_preferences, raise_on_locale=True)
    assert test_raised_locale == 'C.utf8'
    test_default_locale = get_best_parsable_locale(test_module, test_preferences, raise_on_locale=False)
    assert test_default_locale == 'C'

# Generated at 2022-06-12 23:19:18.002113
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    test_available = [
        'C',
        'POSIX',
        'de_DE.utf8',
        'en_US.utf8',
        'fr_FR.utf8'
    ]

    result = get_best_parsable_locale(None, test_available)
    assert result == 'C'

    result = get_best_parsable_locale(None, test_available, raise_on_locale=True)
    assert result == 'C'

# Generated at 2022-06-12 23:19:23.079866
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Tests the get_best_parsable_locale function with various
    checks on the return value.
    """

    # Test the return value
    # A. When the return value is expected to be C.utf8
    preferences = ['C.utf8', 'en_US.utf8']
    class AnsibleModule:
        def get_bin_path(self, locale):
            return True
        def run_command(self, command):
            return (rc, out, err)
    rc = 0
    out = "C.utf8"
    err = None
    ansible_module = AnsibleModule()
    assert get_best_parsable_locale(ansible_module, preferences) == "C.utf8"

    # B. When the return value is expected to be C

# Generated at 2022-06-12 23:19:31.775307
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Test that we get the first choice of
    preferred locales
    """
    token = "test"
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    locale = {'get_bin_path': ['locale']}
    def run_command(cmd, **kwargs):
        return 0, token, ''
    locale['run_command'] = run_command

    assert(get_best_parsable_locale(locale, preferences) == token)



# Generated at 2022-06-12 23:19:41.637558
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class LocalModule(AnsibleModule):

        def get_bin_path(self, arg):
            if 'locale' in arg:
                return '/usr/bin/locale'
            return super(LocalModule, self).get_bin_path(arg)

        def run_command(self, args):
            class RunningResult(object):
                def __init__(self, rc, out, err):
                    self.rc = rc
                    self.out = out
                    self.err = err
            # /usr/bin/locale -a
            if args[0] == '/usr/bin/locale' and args[1] == '-a':
                return RunningResult(0, '''C
C.utf8
POSIX''', '')

# Generated at 2022-06-12 23:19:49.587479
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class AnsibleModule:

        def get_bin_path(self, prog):
            return '/usr/bin/locale'

        def run_command(self, cmd):

            # We do not have any flags as we only have one command, '-a', hence, not setting rc
            out = '''C
C.utf8
de_DE.utf8
en_US.utf8
POSIX
zh_CN.utf8'''
            return 0, out, ''


    module = AnsibleModule()
    preferences = ['en_US.utf8', 'POSIX']
    result = get_best_parsable_locale(module, preferences)
    assert result == 'en_US.utf8'

    preferences = ['zh_CN.utf8', 'en_US.utf8', 'POSIX']
    result = get_

# Generated at 2022-06-12 23:20:07.257461
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class TestModule(object):
        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
            out = ""

            if cmd[0] == "locale" and cmd[1] == "-a":
                for pref in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']:
                    out = out + pref + "\n"
            else:
                raise Exception("Unexpected input")

            return 0, out, ""

        def get_bin_path(self, path, required=False):
            return "/bin/locale"

    preferences = ["en_US.utf8", "C.utf8", "en_US.utf1", "POSIX", "C"]
    test_module = TestModule()


# Generated at 2022-06-12 23:20:13.764842
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common.process import get_bin_path_input
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.sys_info import systype

    if systype == 'Windows':
        locale_mock_path = 'C:\\Windows\\system32\\locale.exe'
    else:
        locale_mock_path = '/bin/locale'

    available = ['C', 'en_US.utf8']
    unavailable = ['en_US.US-ASCII']

# Generated at 2022-06-12 23:20:18.949475
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'C']) == 'C.utf8'
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'C'], raise_on_locale=False) == 'C'


# Generated at 2022-06-12 23:20:28.426843
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Testing get_best_parsable_locale function
        :returns: raised exceptions
    '''
    from ansible.module_utils.basic import AnsibleModule

    MODULE = AnsibleModule(argument_spec=dict())
    TEST_PREFERENCES = ['C.utf8', 'en_US.utf8', 'en_US.utf-8', 'C', 'POSIX']

    assert get_best_parsable_locale(MODULE, TEST_PREFERENCES) in TEST_PREFERENCES

# Unit Test for function get_best_parsable_locale with raise_on_locale=True

# Generated at 2022-06-12 23:20:37.522123
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import sys
    from ansible.module_utils.common.collections import ImmutableDict

    # Needed so that we get a valid module object
    from ansible.module_utils.basic import AnsibleModule

    # ------------------------------------------------------------------------------------------------------------------
    # Set up values to use for test
    # ------------------------------------------------------------------------------------------------------------------
    preferences = ['foo', 'bar']
    module_args = {}

    # ------------------------------------------------------------------------------------------------------------------
    # Test 1: With valid CLI
    # ------------------------------------------------------------------------------------------------------------------
    # Setup
    module = AnsibleModule(argument_spec=module_args)
    module.run_command = lambda args, check_rc=True: (0, '\n'.join(preferences), '')

    # Run
    best_locale = get_best_parsable_locale(module, preferences=preferences)

    # Verify

# Generated at 2022-06-12 23:20:41.504850
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Not sure how to test this other than examining whether the function is raising exception or not
    # will add more tests once I have better ideas
    try:
        get_best_parsable_locale()
    except RuntimeWarning:
        # this is expected in Appveyor and TravisCI
        pass

# Generated at 2022-06-12 23:20:51.924101
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.network import register_transport, get_default_argspec
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.basic import AnsibleModule

    pspec = get_default_argspec(use_default_args=True)

    class TestModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.connection = 'network_cli'
            self.network_os = ''
            super(TestModule, self).__init__(*args, **kwargs)

    class TestConnection(Connection):
        def set_host_overrides(self, host):
            self.host = host
            self.connection = 'network_cli'
            self.network_os = ''


# Generated at 2022-06-12 23:20:58.833651
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import locale
    import unittest

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule, get_platform

    module = AnsibleModule(argument_spec=dict())

    # Test default preferences
    best = get_best_parsable_locale(module)
    assert(best == 'C' or best == 'POSIX')

    # Test on non-English locales
    locale.setlocale(locale.LC_ALL, to_bytes(''))
    best = get_best_parsable_locale(module, raise_on_locale=True)
    assert(best == 'C' or best == 'POSIX')

    # Test on macos with non-English locales
    if get_platform() == 'Darwin':
        locale.set

# Generated at 2022-06-12 23:21:10.173408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def get_bin_path(self, _):
            return locale_path

        def run_command(self, cmd):
            return rc, out, err

    module = FakeModule()

    # No locale tool
    locale_path = None
    assert get_best_parsable_locale(module) == 'C'

    # No output from locale
    locale_path = 'locale'
    rc = 0
    out = ''
    err = ''
    assert get_best_parsable_locale(module) == 'C'

    # Error from locale
    locale_path = 'locale'
    rc = 1
    out = ''
    err = 'error'

# Generated at 2022-06-12 23:21:11.872513
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    res = get_best_parsable_locale(module)
    assert res == 'C'

# Generated at 2022-06-12 23:21:20.234503
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:21:31.261251
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock import module as we don't have a real object/instance
    import sys
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    # Define the mocked function
    def mocked_get_bin_path(name, opt_dirs=[]):
        if name == "locale":
            return "locale"
        return None

    # Mock the module for this test
    module.get_bin_path = mocked_get_bin_path

    # Define the expected value for each test

# Generated at 2022-06-12 23:21:41.176443
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import tempfile

    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.bin_path_cache = {}

        def get_bin_path(self, name, required=True, opt_dirs=None):
            if name in self.bin_path_cache:
                return self.bin_path_cache[name]
            if required:
                raise Exception("get_bin_path called with required=true")
            # fake get_bin_path behavior for this unit test
            for bin_path in ["/bin", "/usr/bin", "/sbin", "/usr/sbin", "/usr/local/bin"]:
                if self.params.get(bin_path):
                    return self.bin_path_cache.setdefault(name, bin_path)
           

# Generated at 2022-06-12 23:21:52.504857
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    # Old style class for compat with Python 2.6-2.7
    class AnsibleModule:
        def __init__(self):
            self._bin_path = {}

        def get_bin_path(self, cmd):
            return self._bin_path.get(cmd, cmd)

        def run_command(self, cmd, check_rc=False, **kwargs):
            return 0, 'C\nen_US.utf8', ''

    class ModuleTest:
        def __init__(self, module):
            self.module = module
            self.results = {}
            self.fail_json = lambda **kwargs: sys.exit(1)

    # test with 'locale' command not found
    module = AnsibleModule()

# Generated at 2022-06-12 23:21:54.283597
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, preferences=['POSIX', 'C']) == 'C'

# Generated at 2022-06-12 23:22:05.259091
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # For testing we'll use a dict to emulate a module
    class TestModule:
        def get_bin_path(self, tool):
            if tool == 'locale':
                return '/usr/bin/locale'
            return None

        def run_command(self, cmd):
            if cmd == ['/usr/bin/locale', '-a']:
                # Return a list of all locales in the system
                return 0, 'C\nC.UTF-8\nen_US.UTF-8\nPOSIX\n', None
            return None

    test_module = TestModule()
    # No locale preferences specified. This should return the first
    # preferred locale, in order of preference.
    assert get_best_parsable_locale(test_module) == 'C.utf8'

    # Specific locale preference specified.

# Generated at 2022-06-12 23:22:09.916809
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    an_module = AnsibleModule(argument_spec=dict())

    # Check if script works when there is no locale binary
    an_module.get_bin_path = lambda x: None
    assert(get_best_parsable_locale(an_module) == 'C')

    # Check if script returns C when there is no output from locale command
    an_module.get_bin_path = lambda x: 'locale'
    an_module.run_command = lambda x: (0, '', '')
    assert(get_best_parsable_locale(an_module) == 'C')

    # Check if script returns C when there is no preferred locale

# Generated at 2022-06-12 23:22:17.762116
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils.six import PY3

    def run_command(args):
        cmd = ' '.join(args)
        if cmd == 'locale -a':
            # return all variants of C.utf and en_US.utf in utf-8
            # and just 'C' and 'POSIX' in ascii
            if PY3:
                s_out = 'C.utf8\nen_US.utf8\nC\nPOSIX\n'.encode('utf-8')
            else:
                s_out = 'C.utf8\nen_US.utf8\nC\nPOSIX\n'
            return 0, s_out,

# Generated at 2022-06-12 23:22:22.456436
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    import os
    import tempfile

    from ansible.module_utils.basic import AnsibleModule, get_platform

    TEST_DATA = '''
---
'''
    TEST_DATA_SEARCH_LOCALE = '''
    locale -a
'''
    TEST_DATA_SEARCH_LOCALE_NO_OUTPUT = '''
    locale -a
    No output
'''
    TEST_DATA_SEARCH_LOCALE_NO_POSIX = '''
    locale -a
    de_DE.utf8
    de_DE
'''

# Generated at 2022-06-12 23:22:33.178629
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils

    # success with list
    mod = ansible.module_utils.basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    assert mod.get_best_parsable_locale(preferences=["en_US.utf-8", "C"]) == "en_US.utf-8"
    assert mod.get_best_parsable_locale(preferences=["fr_FR.utf-8", "en_US.utf-8", "C"]) == "en_US.utf-8"
    assert mod.get_best_parsable_locale(preferences=["fr_FR.utf-8", "C"]) == "C"

    # success with single

# Generated at 2022-06-12 23:22:48.062339
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.common.removed import removed_module
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
    )

    available_locales = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    module.run_command = lambda x: (0, '\n'.join(available_locales), '')

    assert get_best_parsable_locale(module, preferences=None) == 'C.utf8'
    assert get_best_parsable_locale(module, preferences=['POSIX', 'C.UTF-8']) == 'POSIX'

# Generated at 2022-06-12 23:22:58.018909
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' Test get_best_parsable_locale against list of test cases '''

# Generated at 2022-06-12 23:23:04.624655
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Fail with no locale tool
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.sys_info import get_platform
    from ansible.module_utils.common.sys_info import get_distribution

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.check_mode = False
            self.exit_json = None
            self.fail_json = None
            self.run_command = MockAnsibleModule.mock_run_command


# Generated at 2022-06-12 23:23:13.879769
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']


# Generated at 2022-06-12 23:23:15.237442
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert(get_best_parsable_locale(None) == 'C')

# Generated at 2022-06-12 23:23:16.474113
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) is not None

# Generated at 2022-06-12 23:23:21.773316
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    import ansible.module_utils.basic
    locale = get_bin_path('locale')
    if locale is None:
        # skip test for platforms that don't have the locale command
        return True
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module) in ('C', 'POSIX')

# Generated at 2022-06-12 23:23:29.517126
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:23:36.799444
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    tests = (
        ({'preferences': ['C.utf8', 'en_US.utf8', 'C', 'POSIX']},
         'C'),
        ({'preferences': ['C.utf8']},
         'C.utf8'),
        ({'preferences': ['C']},
         'C'),
    )

    for test, expected in tests:
        module = AnsibleModule(argument_spec=test)
        module.params = test
        result = get_best_parsable_locale(module)
        assert result == expected

# Generated at 2022-06-12 23:23:38.845825
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    assert get_best_parsable_locale(ansible.module_utils.basic.AnsibleModule(
    ), raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:23:58.454769
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    def get_args(preferences=None):
        class AnsibleModule:
            def __init__(self):
                self.runner = None
            def get_bin_path(self, locale):
                if locale == 'locale':
                    return '/usr/bin/locale'
                else:
                    return None
            def run_command(self, cmd):
                if cmd == ['/usr/bin/locale', '-a']:
                    out = 'C\nPOSIX\nen_US.utf8\nC.UTF-8\n'
                    return (0, out, '')
                else:
                    return (1, '', '')
        class PlayContext:
            def __init__(self):
                self.fail_on_locale_err = True

# Generated at 2022-06-12 23:24:04.950742
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for function get_best_parsable_locale
    '''
    import ansible.module_utils.basic as module_args

    # test if default works
    assert get_best_parsable_locale(module_args) == 'C'
    # test with different preference
    assert get_best_parsable_locale(module_args, ['POSIX']) == 'POSIX'
    # empty list
    assert get_best_parsable_locale(module_args, []) == 'C'
    # invalid preference
    assert get_best_parsable_locale(module_args, ['invalid']) == 'C'

# Generated at 2022-06-12 23:24:11.999157
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    for locale_name in ['C', 'C.utf8', 'POSIX']:
        class MockModule(object):
            def get_bin_path(self, _):
                return 'locale'

            def run_command(self, cmd):
                if cmd == ['locale', '-a']:
                    return (0, '\n'.join(['C', 'en_US.utf8', 'POSIX']), None)
                else:
                    return (0, None, None)

        assert locale_name == get_best_parsable_locale(MockModule())

    # Test where locale is missing
    class MockModule(object):
        def get_bin_path(self, _):
            # Not using required=True as that forces fail_json
            raise RuntimeWarning("Could not find 'locale' tool")

   

# Generated at 2022-06-12 23:24:21.436597
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # There is no test for the return code not being 0 or for case
    # when the output is empty, so we can assume testing functions
    # are checking that

    # Mock the module to return a specific locale
    def get_bin_path(bin_name):
        return 'locale'

    # Mock the run_command function based on what we want to return
    # We assume the get_bin_path function is correctly tested

# Generated at 2022-06-12 23:24:30.101348
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import unittest
    import ansible.module_utils.basic
    import sys

    class TestModule(ansible.module_utils.basic.AnsibleModule):
        def get_bin_path(self, executable, required=True, opt_dirs=[]):
            return "locale"
        def run_command(self, args, check_rc=True, close_fds=True, executable=None,
                        data=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=True, prompt_regex=None, environ_update=None,
                        umask=None, encoding=None, errors=None):
            rc = 0
            out = ''
            err = ''
            return (rc, out, err)


# Generated at 2022-06-12 23:24:41.081365
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Create a fake module for testing
    module = MockModule()

    # Create a list of locales that are available on system

# Generated at 2022-06-12 23:24:46.074805
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert 'C' == get_best_parsable_locale({})
    # assert 'C' == get_best_parsable_locale(null, [], false)
    # assert 'C' == get_best_parsable_locale(null, [], true)
    assert 'C' == get_best_parsable_locale({}, [], True)
    assert 'C' == get_best_parsable_locale({}, None, True)



# Generated at 2022-06-12 23:24:58.033557
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' Test that we get the right locale, and return 'C' when we fail.
        Also test the raise_on_locale option
    '''
    from ansible.module_utils.basic import AnsibleModule

    # define a test case for the unit test
    class AnsibleModuleMock(AnsibleModule):
        def run_command(self, cmd):
            return 0, 'C.utf8\nen_US.utf8\nC', ''

        def get_bin_path(self, bin_name):
            if bin_name == "locale":
                return bin_name

    # Test that we pick up the first locale in the list
    module = AnsibleModuleMock(
        argument_spec=dict()
    )
    assert get_best_parsable_locale(module) == 'C.utf8'

# Generated at 2022-06-12 23:25:09.106874
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    assert type(get_best_parsable_locale(module)) == str
    assert get_best_parsable_locale(module) != ''
    assert type(get_best_parsable_locale(module, preferences=['POSIX', 'C'])) == str
    assert get_best_parsable_locale(module, preferences=['POSIX', 'C']) != ''
    assert get_best_parsable_locale(module, preferences=['POSIX']) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) != ''

# Generated at 2022-06-12 23:25:14.903773
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    assert get_best_parsable_locale(preferences=['C']) == 'C'
    assert get_best_parsable_locale(preferences=['fr_FR']) == 'C'
    assert get_best_parsable_locale(preferences=['fr_FR', 'C']) == 'C'
    assert get_best_parsable_locale(preferences=['fr_FR', 'C', 'POSIX']) == 'POSIX'

# Generated at 2022-06-12 23:25:26.589102
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    assert get_best_parsable_locale(AnsibleModule({})) == 'C'

    assert get_best_parsable_locale(
        AnsibleModule({}),
        preferences=['an_invalid_locale'],
        raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:25:37.260311
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils._text import to_bytes

    from ansible.module_utils.connection import Connection
    from ansible.module_utils.common.sys_info import get_platform_subclass
    from ansible.module_utils.facts import ModuleFacts

    # mock the module to fake imlementation of the module
    def my_get_bin_path(name):
        if name == "locale":
            return "/usr/bin/locale"

# Generated at 2022-06-12 23:25:40.996480
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # this is an oddity of how unittest works
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    test_locales = ['en_US.utf8', 'en_US', 'C.utf8']
    assert get_best_parsable_locale(module, test_locales) == 'en_US.utf8'

# Generated at 2022-06-12 23:25:45.706921
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test function get_best_parsable_locale
    '''
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec=dict(
            preferences=dict(type='list', default=None),
            raise_on_locale=dict(type='bool', default=False),
        )
    )

    test_module.exit_json(**get_best_parsable_locale(test_module))


if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:25:55.681958
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # stub module
    class Module:
        @staticmethod
        def get_bin_path(name):
            return "locale"

        @staticmethod
        def run_command(cmd):
            stdout = "C\nC.UTF-8\nen_US.utf8"
            return (0, stdout, "")
    m = Module()

    locale = get_best_parsable_locale(m, ['en_US.utf8', 'en_US.UTF-8', 'en_US.utf-8'])
    assert locale == 'en_US.utf8'

    m.run_command = lambda cmd: (1, "", "")
    locale = get_best_parsable_locale(m, raise_on_locale=True)

# Generated at 2022-06-12 23:26:02.857087
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.utils.module_docs_fragments

    # The module context is required for the AnsibleModule mocking
    m = ansible.utils.module_docs_fragments.AnsibleModule(
        argument_spec=dict()
    )

    # Mock the module.get_bin_path function
    def mock_get_bin_path(path):
        return path
    m.get_bin_path = mock_get_bin_path

    # Mock the module.run_command function
    def mock_run_command(command):
        # Mocked response for the locale -a command
        if command == ['locale', '-a']:
            return 0, "output", "error"
        return 0, "", ""
    m.run_command = mock_run_command

    # Get the default C locale

# Generated at 2022-06-12 23:26:07.808294
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())
    locale = get_best_parsable_locale(module, raise_on_locale=True)
    assert locale in ['en_US.utf8', 'C.utf8', 'C', 'POSIX'], "Locale: %s was not in the list" % locale

# Generated at 2022-06-12 23:26:13.967892
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """ Test the get_best_parsable_locale function """
    import os

    class FakeModule:
        def __init__(self, **kwargs):
            self.params = kwargs

        def exit_json(self, **kwargs):
            self.exit_args = kwargs

        def fail_json(self, **kwargs):
            self.fail_args = kwargs

        def get_bin_path(self, _):
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'test', 'templates'))

        def run_command(self, args):
            if args[0] == 'locale':
                return (0, 'C\nen_US.utf8', '')

# Generated at 2022-06-12 23:26:22.804557
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Import module and setup mock support
    import sys
    import tempfile
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # Stub which locations locale is in
    locale_paths = [
        # Full path to mock locale binary
        os.path.join(tempfile.mkdtemp(), 'locale'),
        '/bin/locale',     # Linux
        '/usr/bin/locale', # *BSD
        '/usr/bin/env locale' # Fedora
    ]

    # Stub get_bin_path behavior
    def fake_get_bin_path(module, exe):
        if exe == 'locale':
            return locale_paths.pop(0)
        else:
            return None

    # Stub run_command behavior

# Generated at 2022-06-12 23:26:34.394902
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic

    class Args(object):
        def __init__(self):
            pass

    class FakeModule(object):
        def __init__(self):
            self.params = Args()
            self.params.binary = None
            self.params.warn = False
            self.params.get_bin_path = self.get_bin_path
            self.params.run_command = self.run_command

        def get_bin_path(self, name):
            #  This is a test and always return true
            return name

        def run_command(self, cmd):
            if cmd[1] == '-a':
                return 0, 'C\nen_US.utf8\nC\nen_US.utf8\nC\nen_US.utf8', ''

# Generated at 2022-06-12 23:26:48.170703
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import shutil
    import sys
    import tempfile
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils.six.moves import reload_module
    from ansible.compat.tests.mock import patch
    from ansible.module_utils.common.locale import (
        get_best_parsable_locale,
    )
    from ansible.tests.unit.compat.mock import MagicMock
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_text

    locale = shlex_quote('echo utf8')
    available = '''C
en_US.utf8
POSIX
'''

# Generated at 2022-06-12 23:26:52.664163
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    if sys.version_info < (2, 7):
        raise SkipTest("Test requires Python 2.7 or greater")

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
        },
        supports_check_mode=True
    )

    locale = get_best_parsable_locale(module)
    assert locale == 'C'

# Generated at 2022-06-12 23:26:55.532608
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os

    assert get_best_parsable_locale(os) == 'C'

    assert get_best_parsable_locale(os, preferences=None, raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:27:04.439180
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # Test that if the 'locale' command is not available, we return C.
    module.get_bin_path = lambda x: None
    assert 'C' == get_best_parsable_locale(module)

    # Test that if there is no output to the 'locale' command, we return C.
    module.get_bin_path = lambda x: x
    def test_run_command(cmd):
        if cmd[0] == 'locale' and len(cmd) == 2 and cmd[1] == '-a':
            return (0, '', '')
        else:
            raise Exception
    module.run_command = test_run_command
    assert 'C' == get_best_parsable_loc

# Generated at 2022-06-12 23:27:12.563271
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def check_response(cmd, expected):
        module = AnsibleModule(
            argument_spec={},
        )
        module.run_command = lambda args: (0, "", "", cmd)
        actual = get_best_parsable_locale(module, raise_on_locale=False)
        assert actual == expected

    check_response(
        cmd='''
"C"
"C.UTF-8"
"de_DE.utf8"
de_DE.utf-8
"de_DE@euro"
"de_DE"
"de"
"en_GB.utf8"
''',
        expected='C',
    )