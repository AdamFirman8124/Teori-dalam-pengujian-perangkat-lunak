

# Generated at 2022-06-12 23:17:16.265699
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import get_distribution

    class TestModule(object):
        def __init__(self, environ_update=None, params=None, **kwargs):
            self.params = params
            self.environ_update = environ_update
            self.kwargs = kwargs

        def get_bin_path(self, bin_path, required=False, opt_dirs=[]):
            bin_path = sys.executable
            return bin_path


# Generated at 2022-06-12 23:17:24.089867
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class MockedModule():
        def __init__(self, locale_found=True):
            self.locale_found = locale_found
            self.changed = False

        def get_bin_path(self, arg):
            if arg == 'locale':
                if self.locale_found:
                    return arg
                else:
                    return None

        def run_command(self, arg):
            if arg[0] == 'locale':
                return (0, 'en_US.utf8\nC\nC.utf8', None)
            else:
                return (0, None, None)

    #
    # Test the different conditions
    #
    # No preferences passed in
    m = MockedModule()

    result = get_best_parsable_locale(m)

# Generated at 2022-06-12 23:17:30.337849
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.fail_json = lambda: None
        def get_bin_path(self, name):
            if name == "locale":
                return "/usr/bin/locale"
            else:
                return None
        def run_command(self, command):
            if command[0] == "/usr/bin/locale" and command[1] == "-a":
                return (0, "C\nen_US.utf8\nC.utf8\nPOSIX\n", "")
            else:
                return (0, "", "")

    # Locale found
    assert get_best_parsable_locale(AnsibleModule()) == "C.utf8"
    # Locale not found
    assert get

# Generated at 2022-06-12 23:17:35.545331
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Import module
    import ansible.module_utils.basic

    # Create an AnsibleModule instance
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
        check_invalid_arguments=False
    )

    # Assert that value is 'C'
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:17:46.171684
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import tempfile

    locale_path = os.path.join(tempfile.gettempdir(), 'locale')
    os.environ['PATH'] = ':'.join([locale_path, os.environ['PATH']])

    from ansible.modules.system.locale import get_best_parsable_locale


# Generated at 2022-06-12 23:17:51.849658
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = MockAnsibleModule()
    expected_locale = "C"
    actual_locale = get_best_parsable_locale(module)
    assert expected_locale == actual_locale

    expected_locale = "C.utf8"
    rc, out, err = module.run_command([module.get_bin_path("locale"), "-a"])
    actual_locale = get_best_parsable_locale(module)
    assert expected_locale == actual_locale


# MockAnsibleModule Class

# Generated at 2022-06-12 23:18:03.030252
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import EnvironmentFallback, HAS_LOCALE
    from ansible.module_utils.six import StringIO

    module = AnsibleModule(
        argument_spec=dict()
    )

    # set up some fake test data
    module.run_command = lambda x, environment_fallback=EnvironmentFallback.NONE, check_rc=True: (0, 'C\nPOSIX\nen_US.UTF-8', '')
    module.get_bin_path = lambda x: 'locale'

    assert get_best_parsable_locale(module) == 'POSIX'


# Generated at 2022-06-12 23:18:13.269091
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule

    locale_path = None
    locale_utility = None
    locale_test_file = None
    locale_unit_test_path = os.path.split(os.path.realpath(__file__))[0]
    locale_test_path = os.path.join(locale_unit_test_path, 'locale_test_files')
    locale_test_utility = os.path.join(locale_test_path, 'locale')
    locale_test_content = os.path.join(locale_test_path, 'locale_content')

    locale_test_data = None
    locale_test_content_file = None
    locale_test_content_file_data = None
    locale_test

# Generated at 2022-06-12 23:18:20.937626
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import locale
    from tempfile import NamedTemporaryFile

    m = AnsibleModule(argument_spec={'prioritized_locales': dict(type='list')})
    # override arguments passed to ansible module since we don't want to actually run
    m.params = {}
    # test default of POSIX when nothing else is available
    # also needs to test when locale is not installed
    with NamedTemporaryFile() as locale_file:
        # inject a fake locale executable to m
        locale_file.write(b'#!/bin/sh\n')
        locale_file.flush()
        m.get_bin_path = lambda name, required=False, opt_dirs=[] : locale_file.name
        my_locale = get_best_parsable_loc

# Generated at 2022-06-12 23:18:31.768230
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import sys
    import unittest
    from ansible.module_utils.common.process import get_bin_path

    from ansible.compat.tests.mock import patch, Mock

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.basic import AnsibleModule

    if get_bin_path('locale'):
        raise unittest.SkipTest("locale command found")

    # set up some test variables
    x_val = 10
    y_val = 15
    z_val = 20
    result_expected = {'failed': False, 'rc': 0, 'changed': False, 'changed_when_result': False,
                       'cmd': '', 'stdout': '', 'end': ''}

    # set up return values for our

# Generated at 2022-06-12 23:18:42.225148
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # pretend we have a module called 'module'
    import ansible.module_utils
    class FakeModule(object):
        def get_bin_path(self, arg):
            return arg


# Generated at 2022-06-12 23:18:52.418447
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:19:02.584131
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    get_best_parsable_locale()
    """

    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule

    # test C locale
    am = AnsibleModule(argument_spec={}, supports_check_mode=False)
    found = get_best_parsable_locale(am)
    assert found == 'C'

    # test with preference
    am = AnsibleModule(argument_spec={}, supports_check_mode=False)
    found = get_best_parsable_locale(am, preferences='ja_JP.utf8')
    assert found == 'C'

    # test to fail without locale command
    am = AnsibleModule(argument_spec={}, supports_check_mode=False)

# Generated at 2022-06-12 23:19:13.071158
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.six.moves import builtins
    import pytest

    if not hasattr(builtins, '__fake__'):
        pytest.skip("skipping as this is only to be run with __fake__ builtin support")

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common_koji

    def _load_koji_config():
        from ansible.module_utils import koji as local_koji

        return local_koji._load_koji_config()

    class AnsibleModuleFake(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, binary):
            if binary == 'locale':
                return get_bin_locale()
            return None


# Generated at 2022-06-12 23:19:24.231850
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import collections
    import sys
    import types

    mdict = {
        "get_bin_path": lambda *args: sys.executable,
        "run_command": lambda *args: (0, "C\nen_US.utf8\n", ""),
    }

    m = collections.namedtuple('AnsibleModule', mdict.keys())(**mdict)
    assert get_best_parsable_locale(m) == "C"

    # src: https://github.com/ansible/ansible/issues/50436
    # here test is failing when we have LANG=C.UTF-8
    del mdict["run_command"]
    mdict["run_command"] = lambda *args: (0, "C.UTF-8\nen_US.utf8\n", "")

# Generated at 2022-06-12 23:19:36.351923
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Mock up ansible module for testing
    class MockModule(object):
        @staticmethod
        def get_bin_path(tool):
            return tool

        @staticmethod
        def run_command(command):
            if command == ['locale', '-a']:
                return (0, 'C.utf8\nC\nen_US.utf8\nPOSIX\n', '')
            else:
                return (127, '', 'Command not found')
    module = AnsibleModule()
    module.AnsibleModule = MockModule

    # Test specific cases
    assert get_best_parsable_locale(module) == 'C.utf8'

# Generated at 2022-06-12 23:19:40.507957
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    module = mock.MagicMock()
    module.run_command.return_value = (0, '', '')
    module.get_bin_path.return_value = True
    assert get_best_parsable_locale(module) == 'C'


# Generated at 2022-06-12 23:19:48.835896
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        This function is not included in the main Ansible import,
        so this unit test module needs to be manually run at this time.
    '''

    # Mock AnsibleModule class
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, prog, required=False):
            if prog == 'locale':
                return '/usr/bin/locale'
            else:
                return None


# Generated at 2022-06-12 23:19:58.002018
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # the below tests won't work unless locale is present
    locale = module.get_bin_path('locale')
    if not locale:
        return

    # default test
    assert get_best_parsable_locale(module) == 'C'

    # test a known good preference
    assert get_best_parsable_locale(module, preferences=['C.utf8']) == 'C.utf8'

    # test a known bad preference
    assert get_best_parsable_locale(module, preferences=['notreallyalocale']) == 'C'

    # test a known good preference in a list with a bad

# Generated at 2022-06-12 23:20:08.626362
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common._text import to_bytes
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={})

    # locale not present in the system
    test_module.run_command = lambda x, **kwargs: (99, "", "locale: not found\n")
    assert(get_best_parsable_locale(test_module, preferences=['C.utf8', 'en_US.utf8'], raise_on_locale=True) is None)

    # locale not present in the system
    test_module.run_command = lambda x, **kwargs: (127, "", "")

# Generated at 2022-06-12 23:20:28.378239
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:20:37.449005
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Use a mock AnsibleModule to test
    from ansible.module_utils.basic import AnsibleModule

    mode = 'command'
    params = {'warnings': [], 'warnings_lines': []}
    tmp = AnsibleModule(argument_spec={}, supports_check_mode=False, **params)

    # Test when no locales are available
    tmp.run_command = lambda args: (0, '', '')
    assert tmp._get_best_parsable_locale() == 'C'

    # Test when some locales are available
    tmp.run_command = lambda args: (0, 'C\nC.UTF-8\nfr_FR\nfr_FR.UTF-8', '')
    assert tmp._get_best_parsable_locale() == 'C.UTF-8'

   

# Generated at 2022-06-12 23:20:45.314765
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic

    class AnsibleModule:
        @staticmethod
        def run_command(args):
            return 0, "C\nen_US.utf8\nfr_FR@euro\nPOSIX\n", ""

        @staticmethod
        def get_bin_path(bin):
            return bin

    result = get_best_parsable_locale(AnsibleModule, ['de_DE', 'fr_FR@euro'])
    assert result == 'fr_FR@euro'

# Generated at 2022-06-12 23:20:54.255283
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = object()
    # for testing, return a known locale
    module.run_command = lambda cmd: (0, 'C\nen_US.utf8', '')
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.UTF-8']) == 'en_US.utf8'
    module.run_command = lambda cmd: (0, 'C\nen_US.UTF-8', '')
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.UTF-8']) == 'en_US.UTF-8'
    module.run_command = lambda cmd: (0, 'C', '')

# Generated at 2022-06-12 23:21:05.856110
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:21:15.062233
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.utils.module_docs_fragments
    test_module = ansible.utils.module_docs_fragments.AnsibleModule(
        argument_spec=dict(),
    )
    test_module.get_bin_path = lambda x: '/bin/locale'

    class TestException(Exception):
        pass

    class MockPopen(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err


# Generated at 2022-06-12 23:21:20.740953
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class Module(object):
        def __init__(self):
            self.bin_path = {}
        def get_bin_path(self, exe):
            return self.bin_path.get(exe, None)
        def run_command(self, cmd):
            return 0, "", ""

    # Case 1: Success
    module = Module()
    res = get_best_parsable_locale(module)
    assert res == 'C'

    # Case 2: Success
    module = Module()
    module.bin_path = {'locale': '/bin/locale'}
    res = get_best_parsable_locale(module)
    assert res == 'C'

    # Case 3: Failure

# Generated at 2022-06-12 23:21:25.779390
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test the output of get_best_parsable_locale for the case where there is no
    output from the locale command, the command returns an error, and the case
    where a valid locale is returned.
    '''
    class MockModule:
        def __init__(self):
            self.fail_json_called = False
            self.fail_json_kwargs = {}
            self.run_command_return_value = 0
            self.run_command_kwargs = {}
            self.run_command_output = None
            self.run_command_error = None

        def fail_json(self, *args, **kwargs):
            self.fail_json_called = True
            self.fail_json_kwargs = kwargs


# Generated at 2022-06-12 23:21:30.314727
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Test with no 'locale' command.
    """
    class FakeModule:
        def __init__(self):
            self.fail_json = lambda **kwargs: print(kwargs)

    class FakeRunner:
        def __init__(self, rc=0, out='', err=''):
            self.rc = rc
            self.out = out
            self.err = err
        def run(self, cmdargs):
            return self.rc, self.out, self.err

    fake_module = FakeModule()
    fake_module.get_bin_path = lambda prog: None
    fake_module.run_command = FakeRunner()

    found = get_best_parsable_locale(fake_module)
    assert found == 'C'


# Generated at 2022-06-12 23:21:40.611418
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    assert get_best_parsable_locale(AnsibleModule(
    )) == 'C'
    assert get_best_parsable_locale(AnsibleModule(
    ), preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(AnsibleModule(
    ), preferences=['C.utf8', 'POSIX', 'C', 'en_US.utf8']) == 'C'
    assert get_best_parsable_locale(AnsibleModule(
    ), preferences=['POSIX', 'C', 'en_US.utf8']) == 'C'

# Generated at 2022-06-12 23:22:10.320624
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    # setup the module
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # test for a good result
    assert get_best_parsable_locale(module) in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # test for an error result
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    try:
        get_best_parsable_locale(module, preferences=['abcdef','locale','fail'])
    except RuntimeWarning:
        pass
    else:
        raise Exception('should have failed')

# Generated at 2022-06-12 23:22:18.009840
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Run simple unit test for best parsable locale function
    '''
    # Setup required test vars
    module = AnsibleModule(argument_spec={})
    preferences = [
        'p1',
        'p2',
        'p3'
    ]

    # Test against locals we expect to be available
    # This uses a local os.environ, which we need to prep
    import os
    os.environ['LC_ALL'] = 'C.UTF-8'
    output = get_best_parsable_locale(module, preferences=preferences)
    assert output == 'C'

    os.environ['LC_ALL'] = 'POSIX'
    output = get_best_parsable_locale(module, preferences=preferences)
    assert output == 'POSIX'

    os

# Generated at 2022-06-12 23:22:26.511897
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # pylint: disable=import-error,unused-import
    from ansible.module_utils.basic import AnsibleModule

    # Test with available locales
    mock_module = AnsibleModule(argument_spec={})
    assert mock_module.get_best_parsable_locale({'changed': False, 'rc': 0, 'out': 'C'}) == 'C'

    assert mock_module.get_best_parsable_locale({'changed': False, 'rc': 0, 'out': 'C\nen_US\nen_US.UTF-8'}) == 'C'


# Generated at 2022-06-12 23:22:28.813252
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    found = get_best_parsable_locale()
    assert found == 'C', "Unexpected locale returned: " + found

# Generated at 2022-06-12 23:22:36.593845
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import os
    import tempfile
    import shutil
    import subprocess
    import platform

    class FakeModule(object):
        def get_bin_path(self, binary):
            return binary

        def run_command(self, list, check_rc=True):
            if list[0] == 'locale':
                tempdir = tempfile.mkdtemp()
                cmd = ['locale', ]
                # Always run in tempdir in order to not get an error message
                # from the command `locale -a`
                os.chdir(tempdir)
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                (out, err) = proc.communicate()
                rc = proc.returncode
                shutil.r

# Generated at 2022-06-12 23:22:46.111468
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import copy
    import pytest
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:22:54.508361
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    m = ansible.module_utils.basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True)

    # On systems without the locale command, this should raise RuntimeWarning
    try:
        get_best_parsable_locale(m)
        raise AssertionError('Expected RuntimeWarning')
    except RuntimeWarning:
        pass

    # On systems with the locale command, this should not raise a Warning
    m.get_bin_path = lambda x: x
    assert get_best_parsable_locale(m) == 'C'

# Generated at 2022-06-12 23:23:01.694374
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import tempfile
    from ansible.module_utils.basic import AnsibleModule

    # This test basically mocks module.run_command and mimics some of the possible
    # outputs from 'locale -a' so we can test the logic.

    module = AnsibleModule(
        argument_spec=dict()
    )

    parent_dir = os.path.join(os.path.dirname(__file__), "..")
    parent_path = os.path.normpath(parent_dir)
    os.environ["PATH"] = "{0}:{1}".format(parent_path, os.environ.get("PATH"))
    os.environ["ANSIBLE_LIBRARY"] = parent_path
    module.run_command = mock_run_command

    module.params['locales'] = []
   

# Generated at 2022-06-12 23:23:08.048102
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule, get_exception
    try:
        get_best_parsable_locale(AnsibleModule(
            argument_spec={'test': {'required': False}}))
    except Exception as e:
        fd = open('.stdout', 'r')
        output = fd.read()
        fd.close()
        assert 'Locale not found' in output
        assert 'using C locale' in output
        assert 'No output from locale' not in output
        assert 'POSIX' not in output
        assert 'C' not in output

# Generated at 2022-06-12 23:23:17.807473
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale = ['C', 'C.utf8', 'en_US.utf8']
    found = get_best_parsable_locale(locale)
    assert found == 'C', "get_best_parsable_locale: expected 'C', got %s" % (found)


locale = ['C', 'C.utf8', 'en_US.utf8', 'en_US.utf8']
found = get_best_parsable_locale(locale)
assert found == 'C', "get_best_parsable_locale: expected 'C', got %s" % (found)

locale = ['en_US.utf8', 'C.utf8', 'en_US.utf8']
found = get_best_parsable_locale(locale)

# Generated at 2022-06-12 23:24:21.887067
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    import ansible.module_utils.basic
    import ansible.module_utils.common
    from ansible.module_utils.common import run_command

    module = AnsibleModule(
        argument_spec = dict(),
    )

    module.get_bin_path = get_bin_path
    module.run_command = run_command

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=None) == 'C'
    assert get_best_parsable_locale(module, preferences=['C']) == 'C'

# Generated at 2022-06-12 23:24:28.564874
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    if sys.version_info < (2, 7):
        module = imp.load_source('test_module', os.path.join(os.path.dirname(__file__), '../..', 'module_utils', 'basic.py'))
    else:
        raise Exception("Importing AnsibleModules2.5 doesn't work on Python2")

    assert get_best_parsable_locale(module) == 'C'

    # Test the case where preferences is empty
    assert get_best_parsable_locale(module, []) == 'C'

# Generated at 2022-06-12 23:24:33.724521
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils._text import to_bytes
    import sys

    test_mock_locale = """
Warning: LC_MESSAGES: cannot change locale (zh_CN.UTF-8): No such file or directory
Warning: LC_ALL: cannot change locale (zh_CN.UTF-8): No such file or directory
Warning: LANG: cannot change locale (zh_CN.UTF-8): No such file or directory
C
C.UTF-8
en_US.utf8
en_US.UTF-8
zh_CN.gb18030
zh_CN.GB18030
zh_CN.GBK
zh_CN.GB2312
zh_CN
POSIX
"""


# Generated at 2022-06-12 23:24:44.247500
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Set locale available list
    locale_available = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Set expected results
    expected_results = {
        'C': 'C',
        'POSIX': 'C',
        'en_US.utf8': 'en_US.utf8',
        'default': 'C',
    }

    # Test with all preferences
    for pref in locale_available:
        assert get_best_parsable_locale(locale_available, [pref, 'POSIX', 'C']) == expected_results[pref]

    # Test with default value
    assert get_best_parsable_locale(locale_available, ['fr_FR']) == expected_results['default']

# Generated at 2022-06-12 23:24:49.574663
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    assert 'C' == get_best_parsable_locale(module, preferences)

    preferences.reverse()
    for pref in preferences:
        assert pref == get_best_parsable_locale(module, preferences)

    preferences = ['C.utf8', 'en_US.utf8']
    assert 'C.utf8' == get_best_parsable_locale(module, preferences)
    preferences.insert(0, 'POSIX')
    assert 'C.utf8' == get_best_parsable_locale(module, preferences)


# Generated at 2022-06-12 23:24:59.752585
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils.basic
    import ansible.module_utils.six
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.six.moves import StringIO


# Generated at 2022-06-12 23:25:02.113737
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    c = 1
    assert c == 1

# Generated at 2022-06-12 23:25:12.311987
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule, get_bin_path
    import os
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('\n'.join(['en_US', 'C', 'en_GB']))
    os.environ['LC_ALL'] = 'en_US'

    bin_path = get_bin_path('env')
    assert bin_path

    module = AnsibleModule(argument_spec=dict(
        locale_env=dict(type='path'),
        check_locale=dict(type='bool', default=False),
    ))

    module.params['locale_env'] = f.name
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:25:24.127270
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.plugins.loader import find_plugin

    fixture_path = 'modules/system/locale_info.yaml'
    module_name = 'locale_info'
    locale_info = find_plugin(module_name, 'modules')
    mocked_module = locale_info.load_module(module_name)
    mocked_module.params = dict(
        state='list',
    )

    mocked_module.run_command = fake_run_command(code=0, out='''
C
C.UTF-8
en_US.utf8
''')

    prefs = ['C', 'en_US.utf8']
    locale = get_best_parsable_locale(mocked_module, prefs)
    assert locale == 'en_US.utf8'


# Generated at 2022-06-12 23:25:34.889554
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit tests for function get_best_parsable_locale
    '''
    from ansible.module_utils.basic import AnsibleModule

    test_input = {
        'preferences': ['C.utf8', 'en_US.utf8', 'C', 'POSIX'],
        'out': 'C\nen_US.utf8\nen_US.utf8\nen_US.utf8\nen_US.utf8',
        'rc': 0,
        'err': ''
    }
    expected_output = 'en_US.utf8'

    mock_module = AnsibleModule(argument_spec={})
    mock_module.run_command.return_value = (test_input['rc'], test_input['out'], test_input['err'])

    assert expected_output == get

# Generated at 2022-06-12 23:26:40.005780
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import is_platform_windows

    module = AnsibleModule(
        argument_spec=dict(
        ),
    )

    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    # Cannot test this on Windows
    if not is_platform_windows():
        module = AnsibleModule(
            argument_spec=dict(
            ),
            supports_check_mode=False
        )

        locale = get_best_parsable_locale(module)
        assert locale == 'C.utf8' or locale == 'en_US.utf8' or locale == 'C' or locale == 'POSIX'

if __name__ == '__main__':
    test_get_best_

# Generated at 2022-06-12 23:26:46.028714
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    from ansible.modules.system import locale

    with tempfile.NamedTemporaryFile('w') as locale_file:
        locale_file.write('en_US.utf8\nen_US.UTF-8\nC\nPOSIX\n')
        locale_file.flush()
        preferences = ['en_US.ISO8859-1', 'en_US.utf8', 'C', 'POSIX']
        assert get_best_parsable_locale(locale, preferences, raise_on_locale=True) == 'posix'

# Generated at 2022-06-12 23:26:48.539026
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:26:57.077711
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from re import sub
    DEFAULT_RETURN_LOCALE = 'C'

    class TestModule(AnsibleModule):
        def __init__(self):
            super(TestModule, self).__init__(argument_spec={})

        def get_bin_path(self, arg):
            return sub(r"^(\S+\s+)|(\S+$)", "", arg)

        def run_command(self, cmd):
            # True: good command
            # False: something bad happened
            # None: command not supported
            locale_i18n_locales = ["de_DE.UTF-8", "en_US.UTF-8", "es_CL.UTF-8"]

# Generated at 2022-06-12 23:27:06.194222
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import os
    import shutil
    import tempfile
    import ansible.module_utils.basic
    import ansible.module_utils.pycompat24

    old_sys_path = sys.path
    old_bindir = tempfile.mkdtemp(prefix='ansible_test_get_best_parsable_locale')

    # Create a fake locale executable
    fake_locale = tempfile.mkdtemp(prefix='ansible_test_get_best_parsable_locale')

    fake_locale_fn = os.path.join(fake_locale, 'locale')
    with open(fake_locale_fn, 'w') as fd:
        fd.write('#!/bin/sh\n')