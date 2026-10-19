

# Generated at 2022-06-12 23:17:17.528331
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system import setup

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Mock AnsibleModule
    class FakeAnsibleModule():
        def __init__(self, *args, **kwargs):
            self.module = self
            self.params = {}
            self.check_mode = False
            self.user_args = None
            self.global_args = None
            self.exit_args = None
            self.fail_json_args = None
            self.changed = False
            self.failures = []
            self.warnings = []
            self.no_log_args = None
            self.log_invocation = False
            self.verbosity = 0

        def fail_json(self, *args, **kwargs):
            raise

# Generated at 2022-06-12 23:17:25.147226
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == "C"
    assert get_best_parsable_locale(None, preferences=["en_US.utf8", "C.utf8", "C", "POSIX"]) == "C"
    assert get_best_parsable_locale(None, preferences=["en_US.utf8", "C.utf8", "C", "POSIX"], raise_on_locale=False) == "C"
    assert get_best_parsable_locale(None, preferences=["en_US.utf8", "C.utf8", "C", "POSIX"], raise_on_locale=True) == "C"
    assert get_best_parsable_locale(None, preferences=["en_US.utf8"]) == "C"


# Generated at 2022-06-12 23:17:31.410441
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    # Test that no exception is raised when run with default parameters
    get_best_parsable_locale(module)

    # Test that the default locale is returned when no preferences are specified
    default_locale = get_best_parsable_locale(module, preferences=None)
    assert default_locale == 'C'

    # Test that locale is returned when locale is present in preferences
    locale = get_best_parsable_locale(module, preferences=['C', 'C.UTF-8'])
    assert locale == 'C'

    # Test that exception is raised when run  with raise_on_locale=True


# Generated at 2022-06-12 23:17:42.414782
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    class TestModule(object):
        def __init__(self, out, rc=0, err='', path=True):
            self.rc = rc
            self.out = out
            self.err = err
            self.path = path

        @staticmethod
        def get_bin_path(*args):
            if TestModule.path is not None:
                return 'locale'
            else:
                return None

        def run_command(self, args):
            return self.rc, self.out, self.err

    #
    # No locale program, no preference, no raise: returns 'C'
    #
    TestModule.path = None

# Generated at 2022-06-12 23:17:51.036932
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Test 1: No preferences
    assert get_best_parsable_locale(preferences=None) == 'C'

    # Test 2: Only one preference, default locale
    assert get_best_parsable_locale(preferences=['C']) == 'C'

    # Test 3, but with a different locale
    assert get_best_parsable_locale(preferences=['Nonexistant']) == 'C'

    # Test 4, two locales, one existing
    assert get_best_parsable_locale(preferences=['C', 'Nonexistant']) == 'C'

    # Test 5, two locales, both existing

# Generated at 2022-06-12 23:18:01.889870
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils.basic as dummy_module

    locale_data = u"""
C
en_US.utf8
C.utf8
"""

    locale_data_with_error = u"""
C
en_US.utf8
C.utf8
traceback (most recent call last):
  File "./test_locale.py", line 24, in test_get_best_parsable_locale
    found = get_best_parsable_locale(module)
  File "../lib/ansible/module_utils/escape.py", line 442, in get_best_parsable_locale
    available = out.strip().splitlines()
AttributeError: 'NoneType' object has no attribute 'strip'
"""

    locale_data_no_output = u"""
"""

    locale_data_

# Generated at 2022-06-12 23:18:12.249071
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
    )

    test_preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    test_out = [
        'C.utf8',
        'en_US.utf8',
        'C',
        'POSIX',
    ]

    def mock_run_command(run_cmd, run_args):
        if run_cmd == [module.get_bin_path("locale"), '-a']:
            return 0, '\n'.join(test_out), ''
        else:
            return -1, 'fail', 'fail'

    module.run_command = mock_run_command

    # Best out of all of the test_out

# Generated at 2022-06-12 23:18:18.394792
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    # test_list list of locales we want to test for
    test_list = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    try:
        test_locale = get_best_parsable_locale(module, test_list, True)
        if test_locale not in test_list:
            raise RuntimeWarning("get_best_parsable_locale unit test failed")
    except RuntimeWarning:
        raise

# Generated at 2022-06-12 23:18:28.826276
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # test that we get C as the default
    assert 'C' == get_best_parsable_locale(module)

    # test setting custom preferences
    assert 'C' == get_best_parsable_locale(module, preferences=['foo'])
    assert 'POSIX' == get_best_parsable_locale(module, preferences=['POSIX'])
    assert 'en_US.utf8' == get_best_parsable_locale(module, preferences=['POSIX', 'en_US.utf8'])

    # test fail_on_locale

# Generated at 2022-06-12 23:18:37.087085
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    # Possible locales: (with the univention patch)
    #   de_DE.UTF-8
    #   en_US.UTF-8
    assert 'en_US.UTF-8' == get_best_parsable_locale(module, ['en_US.UTF-8', 'de_DE.UTF-8'])

    # Assert that it is also possible to use preferences which are not in the list of possible locales
    assert 'de_DE.UTF-8' == get_best_parsable_locale(module, ['de_DE.UTF-8', 'en_US.UTF-8'])

# Generated at 2022-06-12 23:19:00.555696
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import sys
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        def __init__(self, params):
            self.params = params

        def get_bin_path(self, _):
            return self.params.get('locale_path', None)

        def run_command(self, cmd):
            if self.params.get('locale_cmd_error', False):
                return 1, None, None
            return 0, "C\nC.UTF-8\nen_US.UTF-8\nen_US.ISO-8859-1", None

    class TestGetBestParsableLocale(unittest.TestCase):
        def setUp(self):
            self.module = MockModule({})

        def tearDown(self):
            pass

# Generated at 2022-06-12 23:19:10.552840
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils.basic
    import ansible.module_utils.local_ansible_utils_extension

    test_module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())
    test_module.get_bin_path = ansible.module_utils.local_ansible_utils_extension.get_bin_path

    tests = dict(
        test_get_best_parsable_locale1=dict(
            module=test_module,
            preferences=['ar_SA.utf8', 'ar_SA'],
            found='C'
        )
    )

    for name, test in tests.items():
        module = test['module']
        preferences = test['preferences']
        expected = test['found']

# Generated at 2022-06-12 23:19:18.280974
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class ModuleMock():
        def __init__(self):
            pass

        def get_bin_path(self, tool):
            return "locale"

        def run_command(self, cmd):
            if cmd[1] == '-a':
                out = "C.utf8\nen_US.utf8\nen_US.utf8\nen_POSIX"
                return 0, out, None
            else:
                return 0, None, None
    module_mock = ModuleMock()
    best_locale = get_best_parsable_locale(module_mock)
    assert best_locale == "C.utf8"
    module_mock = ModuleMock()
    best_locale = get_best_parsable_locale(module_mock, preferences=["C"])


# Generated at 2022-06-12 23:19:29.952257
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # Test 1: No locale found, since we aren't using a system command
    # We should get the default "C" locale

# Generated at 2022-06-12 23:19:41.029083
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    from ..platform.base import BasePlatform

    class TempPlatform(BasePlatform):
        def get_platform_subclass(self, distro, distro_release=None, os_release=None):
            return None

        def get_best_parsable_locale(self, preferences=None, raise_on_locale=False):
            return get_best_parsable_locale(module, preferences, raise_on_locale)

    platform = TempPlatform('Linux', '2.6.32-504.16.2.el6.x86_64', '6.6')

    assert platform.get_best_parsable_locale() == 'C'

    from ..module_utils.basic import Ansible

# Generated at 2022-06-12 23:19:49.205732
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

    module_mock = Mock()
    module_mock.get_bin_path.return_value = False
    assert get_best_parsable_locale(module_mock) == 'C'

    module_mock.get_bin_path.return_value = 'localepath'

    # no output from locale -a
    module_mock.run_command.return_value = (0, '', '')
    assert get_best_parsable_locale(module_mock) == 'C'

    # locale -a output
    module_mock.run_command.return_value = (0, 'fr_FR.UTF-8\n', '')

# Generated at 2022-06-12 23:19:55.141024
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # module function import
    from ansible.module_utils.basic import AnsibleModule

    # define module
    module = AnsibleModule(
        argument_spec=dict(),
    )

    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    locale = get_best_parsable_locale(module, ['en_US.utf8', 'en_US.UTF-8'])
    assert locale == 'C'

# Generated at 2022-06-12 23:20:01.629295
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.process import get_bin_path

    m = basic.AnsibleModule(argument_spec=dict())

    detected_locale = get_best_parsable_locale(m)

    # test if we detected any locale as best alternative
    assert detected_locale is not None, "Could not detect a best alternative locale"

    # test if the detected locale is parsable
    locale = get_bin_path("locale")
    if locale:
        rc, out, err = m.run_command([locale, '-c', '%s' % (to_text(detected_locale))])
        is_parsable = (rc == 0)

# Generated at 2022-06-12 23:20:10.885970
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        def __init__(self, modules):
            self.modules = modules

        def get_bin_path(self, tool, required=False):
            return self.modules[tool]

        def run_command(self, command):
            return self.modules[command]


# Generated at 2022-06-12 23:20:22.354190
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2

    def has_locale(available, preferences):
        test_module = AnsibleModule(argument_spec={})
        test_module.run_command = lambda args: (0, available, '')
        return get_best_parsable_locale(test_module, preferences=preferences, raise_on_locale=False)

    assert has_locale("", ['C.utf8', 'en_US.utf8', 'C', 'POSIX', 'en_GB.utf8']) == 'C'
    assert has_locale("", ['POSIX', 'en_GB.utf8']) == 'C'

# Generated at 2022-06-12 23:20:44.932959
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ['C']) == 'C'
    assert get_best_parsable_locale(None, ['ZOSVMSVL'] + ['C']) == 'C'
    assert get_best_parsable_locale(None, ['C.utf8'] + ['C']) == 'C.utf8'
    assert get_best_parsable_locale(None, ['ZOSVMSVL'] + ['C.utf8'] + ['C']) == 'C.utf8'

# Generated at 2022-06-12 23:20:48.894885
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    assert get_best_parsable_locale(AnsibleModule(
        argument_spec=dict()
    ), ['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

    assert get_best_parsable_locale(AnsibleModule(
        argument_spec=dict()
    ), ['POSIX']) == 'C'

# Generated at 2022-06-12 23:20:49.603275
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale = get_best_parsable_locale()
    assert locale == 'C'

# Generated at 2022-06-12 23:20:55.877122
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    test_locale = ['en_US.utf8', 'en_US.utf8', 'en_US.utf8', 'en_US.utf8', 'en_US.utf8', 'en_US.utf8', 'en_US.utf8', 'en_US.utf8', 'en_US.utf8']
    test_locale_none = []
    assert get_best_parsable_locale(module, test_locale) == 'en_US.utf8'
    assert get_best_parsable_locale(module, test_locale_none) == 'C'

# Generated at 2022-06-12 23:20:59.400401
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={})

    assert(get_best_parsable_locale(m, raise_on_locale=True) == 'C')
    assert(get_best_parsable_locale(m) == 'C')

# Generated at 2022-06-12 23:21:10.762808
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    from ansible.module_utils.six.moves import StringIO

    class TestModule(object):
        def __init__(self):
            self.params = {}
            self.debug = []
            self.warnings = []

        def get_bin_path(self, cmd):
            if cmd == 'locale':
                return cmd

        def run_command(self, args):
            if args[0] == 'locale' and args[1] == '-a':
                # Returning output that should match en_US.utf8
                return 0, 'C.UTF-8\nen_US\nen_US.utf8\n', ''

# Generated at 2022-06-12 23:21:18.815110
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Test function get_best_parsable_locale'''
    class FakeModule():
        def __init__(self):
            self.results = []

        def run_command(self, args):
            return (0, 'C\nen_US.utf8\nru_RU.utf8', '')

        def get_bin_path(self, cmd):
            return True

    class FakeModuleFail():
        def __init__(self):
            self.results = []

        def run_command(self, args):
            return (1, '', '')

        def get_bin_path(self, cmd):
            return True

    module = FakeModule()

# Generated at 2022-06-12 23:21:29.874863
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class FakeModule():
        def __init__(self):
            self.run_command_return_vals = []

        def run_command(self, command):
            return self.run_command_return_vals.pop(0)

        def get_bin_path(self, name):
            if name == 'locale':
                return '/bin/locale'
            else:
                return None

    # Case 1 when locale binary is not present
    module = FakeModule()
    module.run_command_return_vals = [(1, '', '')]

    assert get_best_parsable_locale(module, raise_on_locale=False) == 'C'

    # Case 2 when locale binary is present
    module = FakeModule()

# Generated at 2022-06-12 23:21:36.795518
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale('foo') == 'C'
    assert get_best_parsable_locale('foo', ['POSIX', 'de_DE.UTF-8']) == 'POSIX'
    assert get_best_parsable_locale('foo', ['POSIX']) == 'POSIX'
    assert get_best_parsable_locale('foo', ['POSIX', 'C.UTF-8']) == 'POSIX'

# Generated at 2022-06-12 23:21:44.387273
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # function to mock run_command
    def mock_run_command(module, command):
        return (0, command, '')

    # function to mock get_bin_path
    def mock_get_bin_path(module, executable, required=False):
        return executable

    # mock a module object
    class MockModule(object):
        pass

    # set module methods
    module = MockModule()
    module.run_command = mock_run_command
    module.get_bin_path = mock_get_bin_path

    # test 1
    preferences = ['C', 'POSIX']
    assert get_best_parsable_locale(module, preferences) == 'C'

    # test 2
    preferences = ['POSIX', 'C']

# Generated at 2022-06-12 23:22:19.046742
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import sys
    import unittest
    from ansible.module_utils.basic import AnsibleModule

    def locale_side_effect(*args):
        if args == ('-a',):
            return (0, 'C.utf8', '')
        elif args == ('C.utf8',):
            return (0, 'UTF-8', '')
        else:
            sys.exit(1)

    class AnsibleModuleMock(AnsibleModule):
        def run_command(self, args):
            return locale_side_effect(*args)

    class EnvironmentMock(object):
        def __init__(self, **kwargs):
            self.__dict__ = kwargs

    class TestGetParsableLocale(unittest.TestCase):
        def setUp(self):
            self

# Generated at 2022-06-12 23:22:27.398365
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule()

    assert get_best_parsable_locale(mod) == 'C'
    assert get_best_parsable_locale(mod, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'
    try:
        get_best_parsable_locale(mod, raise_on_locale=True)
    except RuntimeWarning:
        assert True
    else:
        assert False, "Failed to raise RuntimeWarning."
    assert get_best_parsable_locale(mod, preferences=['']) == 'C'

    assert get_best_parsable_locale(mod, preferences=[''], raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:22:34.377393
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale_a = 'C.utf8'
    locale_b = 'C'
    locale_c = 'POSIX'
    locale_d = 'en_US.utf8'
    locale_e = 'ar'
    available_locales = [locale_a, locale_b]

    def run_mock(args, **kwargs):
        assert args[:1] == [locale]
        if any(x not in args for x in (locale_a, locale_b, locale_c, locale_d, locale_e)):
            raise RuntimeWarning("Invalid locale '%s' requested" % args[1])
        return 0, '\n'.join(available_locales), ''

    # Test when no preferences and default locale is used
    fake_module = type('', (), {})
    fake_module.run

# Generated at 2022-06-12 23:22:44.802597
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        import unittest2 as unittest
        unittest  # pacify pyflakes
    except ImportError:
        import unittest

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    # create a temp_path with 'locale' utility
    result = module.run_command(['which', 'locale'])
    locale_path = result[1].strip()

    # create a temp_path with 'locale -a' utility to simulate
    # output from locale -a
    result = module.run_command([locale_path, '-a'])
    locale_path = result[1].strip()

    # create a temp_path with 'locale' utility

# Generated at 2022-06-12 23:22:49.643574
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """ Test case for get_best_parsable_locale """

    from ansible import module_utils
    from ansible.module_utils.basic import AnsibleModule

    # Create a test module for AnsibleModule
    test_module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(test_module) == 'C'

# Generated at 2022-06-12 23:22:52.231612
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:23:00.319568
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    import types

    class FakeModule:
        def __init__(self):
            self.params = {}
            self.fail_json = lambda **kwargs: types.MethodType(self._fail_json, self)
            self.get_bin_path = lambda **kwargs: types.MethodType(self._get_bin_path, self)
            self.run_command = lambda **kwargs: types.MethodType(self._run_command, self)

        def _get_bin_path(self, *args, **kwargs):
            return '/bin/locale'

        def _run_command(self, *args, **kwargs):
            return 0, 'en_US.utf8\nen_US.utf8\nC\nPOSIX\n', ''


# Generated at 2022-06-12 23:23:05.426640
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' unit test for get_best_parsable_locale '''

    fake_module = MockAnsibleModule()
    # if locale binary does not exist then return default locale
    assert get_best_parsable_locale(fake_module, ['en_US.utf8']) == 'C'
    # add locale binary to module
    fake_module.run_command = MockRunCommand(result=0, out='C.UTF-8 en_US.UTF-8', err=None)
    assert get_best_parsable_locale(fake_module, ['en_US.utf8']) == 'C.UTF-8'
    fake_module.run_command = MockRunCommand(result=0, out='C.UTF-8 en_US.UTF-8', err=None)
    assert get_best_p

# Generated at 2022-06-12 23:23:14.842417
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule:

        class FakeAnsibleModule(AnsibleModule):

            def get_bin_path(self, tool):
                return '/usr/bin/locale'

            def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, use_unsafe_shell=False,
                            forcible_shell=False, shell=False, cwd=None, env_string=None, data=None, binary_data=False):
                return 0, '', ''

        def __init__(self, locale=None):
            self.ansible_mod = self.FakeAnsibleModule()
            self.locale = locale


# Generated at 2022-06-12 23:23:22.350833
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Locale command
    module = AnsibleModule({})
    assert get_best_parsable_locale(module) == 'C'

    # Locale command with preferences
    module = AnsibleModule({})
    assert get_best_parsable_locale(module, preferences=['C']) == 'C'

    # No locale command
    module = AnsibleModule({})
    module.get_bin_path = lambda cmd: None
    assert get_best_parsable_locale(module) == 'C'


if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:24:00.993387
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule(argument_spec={})
    assert mod
    # Mock module.run_command
    # Mocking get_bin_path() is not needed because we set
    # the default locale to 'C' which always exists.
    def mocked_run_command(params, check_rc=False, close_fds=True, executable=None,
                           data=None, binary_data=None, path_prefix=None, cwd=None,
                           use_unsafe_shell=False, prompt_regex=None, environ_update=None):
        assert params
        assert params[0] == 'locale'
        if params[1] == '-a':
            rc = 0

# Generated at 2022-06-12 23:24:08.707027
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    test_locale = [
        'fr_FR.utf8',
        'fr_FR'
    ]
    module.run_command = lambda cmd, executable=None: (0, '\n'.join(test_locale), '')
    assert module.get_best_parsable_locale(module) == test_locale[-1]
    assert module.get_best_parsable_locale(module, preferences=['fr_FR.utf8', 'en_US.utf8', 'en_FR.utf8']) == 'fr_FR.utf8'
    # test when locale command fails
    module.run_command = lambda cmd, executable=None: (1, '', '')
   

# Generated at 2022-06-12 23:24:17.959458
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={})
    assert test_module.run_command_environ_update['LC_ALL'] == "C"
    assert test_module.get_bin_path("locale")

    test_module.run_command = mock_run_command1
    assert get_best_parsable_locale(test_module) == "en_US.utf8"

    test_module.run_command = mock_run_command2
    assert get_best_parsable_locale(test_module) == "C"

    test_module.run_command = mock_run_command3
    assert get_best_parsable_locale(test_module) == "C"

    test_module.run_command = mock

# Generated at 2022-06-12 23:24:28.423497
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    import shutil
    import os
    import ansible.module_utils.basic as basic
    import ansible.module_utils.locale as locale

    temp_dir = tempfile.mkdtemp()
    # mimic a valid locale command that is missing some locales we want
    with open(os.path.join(temp_dir, 'locale'), 'w') as f:
        f.write('''#!/usr/bin/env python
import os
import sys

sys.exit(0)
os.write(sys.stdout.fileno(), '\\n'.join(['C', 'en_US.utf8']))
''')
    os.chmod(os.path.join(temp_dir, 'locale'), 0o755)

    # monkey-patch the module_utils basic module so we can find

# Generated at 2022-06-12 23:24:33.679426
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    module = AnsibleModule()

    # The test environement is an AWS EC2 machine (as of 2019-03-01)
    # and all of the following commands yield the same, case-insensitive result
    # $ locale -a | egrep "(C|en_US|POSIX)"
    # C.UTF-8
    # en_US.utf8

    # Test preferences defaults to ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    # The following should return C.UTF-8
    assert get_best_parsable_locale(module) == 'C.UTF-8'

    # Test preferences defaults to ['C.

# Generated at 2022-06-12 23:24:44.552421
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.local_ansible_utils as utils

    class TestModule(basic.AnsibleModule):

        def __init__(self):
            super(TestModule, self).__init__(
                argument_spec=dict(
                    verbose={
                        'type': 'bool', 'default': False, 'required': False},
                ),
                supports_check_mode=True,
            )

        def run_command(self, command):
            if self.params['verbose']:
                print("Running %s" % command)

# Generated at 2022-06-12 23:24:49.625679
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Test get_best_parsable_locale()'''
    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule(
        argument_spec=dict(
            locale_list=dict(choices=['C', 'POSIX', 'en_US.utf8'], default=['C', 'POSIX', 'en_US.utf8']),
        )
    )
    # when preferred locale is in the list of locales
    assert get_best_parsable_locale(test_module, ['POSIX']) == 'POSIX'
    # when preferred locale is not in the list of locales
    assert get_best_parsable_locale(test_module, ['en_US']) == 'C'

# Generated at 2022-06-12 23:24:51.782008
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(module='foo') == 'C'

# Generated at 2022-06-12 23:25:00.657750
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    # pylint: disable=import-error
    # pylint: disable=wrong-import-position
    # pylint: disable=redefined-outer-name
    import pytest

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    rc, out, err = module.run_command(['locale', '-a'])

    if rc != 0:
        pytest.skip("Test only works if system has 'locale' installed")

    available = out.strip().splitlines()

    found = get_best_parsable_locale(module, ['C', 'POSIX'])
    assert found.startswith('C')


# Generated at 2022-06-12 23:25:07.253441
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.local import LocalAnsibleModule
    local_module = LocalAnsibleModule()
    print("Locale: " + get_best_parsable_locale(local_module))

if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:25:43.349541
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six.moves import builtins

    class ModuleStub(object):
        '''
            A stub module class to allow testing the get_best_parsable_locale function
            without the AnsibleModule class
        '''
        def __init__(self, run_command_results):
            self.run_command_results = run_command_results

        def get_bin_path(self, binary, required=False):
            if binary and binary.lower() == "locale":
                return "/usr/bin/locale"
            else:
                return None

        def run_command(self, command_args):
            self.run_command_called

# Generated at 2022-06-12 23:25:50.243521
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    # pylint: disable=import-error
    # ModuleNotFoundError is a later Python addition
    # catch ImportError instead to maintain support for multiple Python versions
    try:
        from unittest import mock
    except ImportError:
        # pylint: disable=import-error
        # ModuleNotFoundError is a later Python addition
        # catch ImportError instead to maintain support for multiple Python versions
        import mock

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        bypass_checks=True,
    )

    m = mock.mock_open()
    m.return_value.read.return_value = 'C.UTF-8\n'

# Generated at 2022-06-12 23:25:57.807242
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        import ansible.module_utils.basic
    except ImportError:
        print("could not import ansible module_utils module")
        return

    import doctest

    m = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())

    result = doctest.testmod(get_best_parsable_locale)
    if result.failed == 0:
        print("Success: %s tests passed." % str(result.attempted))
    else:
        sys.exit(result)

# Generated at 2022-06-12 23:26:04.200081
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale() == 'C'
    assert get_best_parsable_locale([]) == 'C'
    assert get_best_parsable_locale(['en_GB.utf8', 'en_US.utf8']) == 'en_US.utf8'
    assert get_best_parsable_locale(['en_GB.utf8', 'en_US.utf8', 'C']) == 'en_US.utf8'
    assert get_best_parsable_locale(['en_GB.utf8', 'en_US.utf8', 'foo']) == 'C'

# Generated at 2022-06-12 23:26:10.115708
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.shell as shell

    m = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # test default behavior
    if "C.utf8" in shell.get_best_parsable_locale(m):
        m.exit_json(changed=True)
    else:
        m.fail_json(msg="Failed")

# Generated at 2022-06-12 23:26:19.917521
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class Module(object):
        def get_bin_path(self, tool):
            return '/usr/bin/' + tool

        def run_command(self, args, check_rc=False, close_fds=False):
            if args[1] == '-a':
                return 0, '''C
C.utf8
en_US.utf8
POSIX
fr_CA.utf8
''', ''
            elif args[0] == 'module':
                return 1, '', ''
            else:
                return 1, '', '''locale: Command not found.'''

    module = Module()
    assert get_best_parsable_locale(module) == 'C.utf8'

    module = Module()

# Generated at 2022-06-12 23:26:31.449405
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import locale
    import sys

    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class MockModule(object):
        def __init__(self, locale_cmd):
            self.locale_cmd = locale_cmd

        def get_bin_path(self, cmd, **kwargs):
            return self.locale_cmd

        def run_command(self, cmd, **kwargs):
            return (0, locale.getdefaultlocale()[0], '')

    class MockModuleLocaleFailed(object):
        def get_bin_path(self, cmd, **kwargs):
            raise RuntimeWarning('locale not installed')


# Generated at 2022-06-12 23:26:32.670638
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale = get_best_parsable_locale()
    assert locale == 'C'

# Generated at 2022-06-12 23:26:39.591076
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    import ansible.module_utils.local_lib

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())
    ansible.module_utils.local_lib.set_module(module)

    try:
        locale = get_best_parsable_locale(module, preferences, False)
    except RuntimeWarning:
        assert False, "Should not have got RuntimeWarning"
    else:
        assert preferences.index(locale) >= 0, 'returned wrong locale'

# Generated at 2022-06-12 23:26:47.859530
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    module = basic.AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['en_US', 'en_GB']) == 'C'
    assert get_best_parsable_locale(module, preferences=['en_US', 'en_GB'], raise_on_locale=True) == 'C'