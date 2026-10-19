

# Generated at 2022-06-12 23:17:16.328576
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Create a stub module and test that 'C' is returned when locale
    # and locale -a fails
    class StubModule:
        def __init__(self):
            pass
        def run_command(self, command):
            if command[0] == 'locale':
                return 1, '', ''
            else:
                return 1, '', ''
        def get_bin_path(self, command, required=False):
            pass
    assert get_best_parsable_locale(StubModule()) == 'C'

    # Create a stub module and test that 'C' is returned when locale
    # fails but locale -a succeeds
    class StubModule:
        def __init__(self):
            pass
        def run_command(self, command):
            if command[0] == 'locale':
                return 1,

# Generated at 2022-06-12 23:17:24.126143
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())

    # default case, we should get this for most systems
    assert get_best_parsable_locale(module) == 'C'

    # setting to something that exists should work
    assert get_best_parsable_locale(module, ['C']) == 'C'

    # allowing a single string should work
    assert get_best_parsable_locale(module, 'C') == 'C'

    # just to cover the error path
    #assert get_best_parsable_locale(module, raise_on_locale=True) == Exception

    # make sure the default doesn't contain any locales that can't be parsed by English tools
    assert get_best_p

# Generated at 2022-06-12 23:17:30.390310
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic


# Generated at 2022-06-12 23:17:40.830341
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(command_start='')

    # Test for unavailability of the required command
    m.run_command = lambda args: (1, "", "")
    assert get_best_parsable_locale(m) == 'C'
    # Test for shell return code different than 0
    m.run_command = lambda args: (123, "", "")
    assert get_best_parsable_locale(m) == 'C'

    # Test for an empty list of available locales
    m.run_command = lambda args: (0, "", "")
    assert get_best_parsable_locale(m) == 'C'

    # Test for a non-empty list of availa

# Generated at 2022-06-12 23:17:49.754015
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system.locale import get_best_parsable_locale

    class Module(object):
        @staticmethod
        def get_bin_path(binary, required=False):
            if binary == 'locale':
                return binary

        @staticmethod
        def run_command(cmd):
            return (0, cmd[1], '')

    test = get_best_parsable_locale(Module, preferences=['blah', 'C'])
    assert test == 'C'

    test = get_best_parsable_locale(Module, preferences=['blah', 'blah_blah'])
    assert test == 'C'

    test = get_best_parsable_locale(Module)
    assert test == 'C'

    test = get_best_parsable_

# Generated at 2022-06-12 23:17:59.451810
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic

    mod = basic.AnsibleModule(
        argument_spec={}
    )
    print("default: %s" % get_best_parsable_locale(mod))

    mod = basic.AnsibleModule(
        argument_spec={}
    )
    mod.run_command = lambda x: (0, 'fr_FR.utf8\nen_US.utf8\nC\nPOSIX\n', '')
    print("specific: %s" % get_best_parsable_locale(mod))

    mod = basic.AnsibleModule(
        argument_spec={}
    )
    mod.run_command = lambda x: (0, '', '')

# Generated at 2022-06-12 23:18:06.482824
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale('C') == 'C'
    assert get_best_parsable_locale('C.utf8') == 'C'
    assert get_best_parsable_locale('en_US.utf8') == 'C'
    assert get_best_parsable_locale('POSIX') == 'C'
    assert get_best_parsable_locale('C', raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:18:16.183446
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    This is just to test the function because we don't want to pollute
    our current unit tests.

    :return:
    '''

    assert (get_best_parsable_locale('C') == 'C')
    assert (get_best_parsable_locale(['C.utf8', 'en_US.utf8'], ['fr.utf8', 'C.utf8']) == 'C.utf8')
    assert (get_best_parsable_locale(['C', 'POSIX'], ['fr.utf8', 'C.utf8']) == 'C')
    assert (get_best_parsable_locale(['C', 'POSIX'], ['fr.utf8', 'C.utf8']) == 'C')

# Generated at 2022-06-12 23:18:20.751527
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    # test 1 - standard POSIX return
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
    )
    module.get_bin_path = lambda x: 'locale'
    module.run_command = lambda x: (0, 'C\nen_US.utf8\nC.utf8\nPOSIX', '')
    assert get_best_parsable_locale(module) == 'C.utf8'

    # test 2 - no locale, use default
    module.run_command = lambda x: (1, '', '')
    assert get_best_parsable_locale(module) == 'C'

    # test 3 - no locale, use default

# Generated at 2022-06-12 23:18:23.583210
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = AnsibleModule(argument_spec={})
    x = get_best_parsable_locale(module)
    assert(x == 'C')


# Generated at 2022-06-12 23:18:36.810942
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={})
    locale_types = {
        'linux': 'en_US.UTF-8',
        'aix': 'C',  # aix doesn't have a 'locale' command
    }
    test_module.run_command = lambda x: (0, locale_types.get('linux', 'C'), '')
    assert get_best_parsable_locale(test_module) == 'en_US.utf8'
    test_module.run_command = lambda x: (1, '', 'locale: not found')
    assert get_best_parsable_locale(test_module) == 'C'

# Generated at 2022-06-12 23:18:39.202320
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.modules.system.user as user

    assert get_best_parsable_locale(user.AnsibleModule(argument_spec={}), raise_on_locale=True)

# Generated at 2022-06-12 23:18:45.779274
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    test_locales = [
        'C', 'POSIX'
    ]
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, test_locales) == 'C'

    test_locales = [
        'C.utf8', 'en_US.utf8', 'C', 'POSIX'
    ]
    assert get_best_parsable_locale(None, test_locales) == 'C.utf8'

# Generated at 2022-06-12 23:18:56.094484
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping

    def _run(module_args, real_locale_dict, expected_locale):
        module_tmp = basic.AnsibleModule(
            argument_spec=dict(
                module_args=dict(type='dict', required=False, default=dict())
            ),
            supports_check_mode=True
        )
        module_tmp.get_bin_path = lambda arg, required=False: real_locale_dict[arg]

        # patch AnsibleModule.run_command

        class FakeRunCommandResult(Mapping):
            def __init__(self, rc, out, err, command):
                self.rc = rc
               

# Generated at 2022-06-12 23:19:02.963422
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._json_compat import json

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    locale = get_best_parsable_locale(module)

    assert locale is not None, "Locale not found"

    try:
        assert locale is not None, "Locale not found"
    except AssertionError:
        module.fail_json(msg="locale=%s" % json.dumps(locale))



# Generated at 2022-06-12 23:19:10.789027
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # TODO: This should be part of a unittest that probes the real system
    #       and then feeds in fake responses.

    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=None) == 'C'
    assert get_best_parsable_locale(None, preferences=['foo', 'bar']) == 'C'
    assert get_best_parsable_locale(None, preferences=['foo', 'C', 'bar']) == 'C'

# Generated at 2022-06-12 23:19:18.419761
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Function: get_best_parsable_locale()'''

    # Example output of locale -a
    locale_a_out = '''C
en_US.utf8
'''

    # Example output of locale -a with no locale
    locale_a_out_no_locale = ''

    # Example output of locale -a with an error code
    locale_a_out_error_code = ''

    class FakeModule(object):
        def __init__(self):
            self.fail_json = lambda msg: msg

        def get_bin_path(self, name, required=False):
            return "locale"

        def run_command(self, cmd, check_rc=True):
            if cmd[1] == '-a':
                if locale_a_out_error_code:
                    return 1

# Generated at 2022-06-12 23:19:29.952013
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    m = AnsibleModule(
        argument_spec=dict(),
    )

    m.run_command = lambda cmd, in_data=None: (0, 'C\nC.UTF-8\nC.utf8\nPOSIX\n', '')
    assert m.get_best_parsable_locale() == 'C'

    m.run_command = lambda cmd, in_data=None: (0, 'POSIX\n', '')
    assert m.get_best_parsable_locale() == 'POSIX'

    m.run_command = lambda cmd, in_data=None: (0, 'POSIX\n', '')
    assert m.get_best_pars

# Generated at 2022-06-12 23:19:41.027720
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    import ansible.module_utils.local_ansible_utils_extras
    import os

    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )
    module.run_command = ansible.module_utils.local_ansible_utils_extras.run_command
    module.get_bin_path = ansible.module_utils.local_ansible_utils_extras.get_bin_path

    if os.name == 'nt':
        assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:19:49.205749
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale


# Generated at 2022-06-12 23:20:07.660946
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Test the get_best_parsable_locale function.  mock_module must be
    imported from the mock_module.py file in this directory.

    python -m pytest test_get_best_parsable_locale.py
    """
    from mock_module import mock_module

    best_locale = get_best_parsable_locale(mock_module)
    assert best_locale == 'C'
    assert mock_module.run_command.call_count == 1

# Generated at 2022-06-12 23:20:16.145909
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.system import locale_gen

    test_module = locale_gen.LocaleGen(AnsibleModule)
    pref = ['POSIX', 'C.utf8', 'C', 'en_US.utf8']
    found = get_best_parsable_locale(test_module, preferences=pref, raise_on_locale=True)
    assert found == 'C', "Found locale should be 'C' : " % found
    assert True

    pref = ['POSIX', 'C.utf8', 'C', 'en_US.utf8']

# Generated at 2022-06-12 23:20:23.876611
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    test_module = AnsibleModule(argument_spec={})
    result = get_best_parsable_locale(test_module, preferences=['C', 'en', 'POSIX'])
    assert result == "C", 'failed to get parsable locale'

    test_module = AnsibleModule(argument_spec={})
    result = get_best_parsable_locale(test_module, preferences=['ru', 'en', 'POSIX'])
    assert result == "C", 'failed to get parsable locale'

# Generated at 2022-06-12 23:20:33.885740
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # pylint: disable=no-self-use,invalid-name
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # in case of errors, the function returns 'C' by default.
    # get_best_parsable_locale() call below may raise RuntimeWarning.
    # As we are not passing raise_on_locale=True, we are suppressing that error.
    # pylint: disable=broad-except
    try:
        locale = get_best_parsable_locale(module)
    except Exception:
        locale = 'C'

    # assert that the returned locale is C
    assert locale == 'C'

# Generated at 2022-06-12 23:20:39.920502
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class MockAnsibleModule(object):
        def __init__(self):
            self.command = ''

        def get_bin_path(self, cmd):
            self.command = cmd
            return '/bin/locale'

        def run_command(self, args):
            if args[1] == '-a':
                return 0, 'C\nC.iso885915\nen_US.utf8', ''
            elif args[1] == '-c':
                return 0, 'LC_CTYPE=en_US.utf8', ''

    module = MockAnsibleModule()
    locale = get_best_parsable_locale(module)

    assert locale == 'en_US.utf8'
    assert module.command == 'locale'

    module = MockAnsibleModule()
    locale

# Generated at 2022-06-12 23:20:50.759445
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import to_text
    from ansible.module_utils.common.text.input import InputData
    from ansible.module_utils.common.text.output import OutputData
    from ansible.module_utils.six.moves import _thread as thread

    env = {
        'LC_MESSAGES': 'C',
        'USER': 'root',
        'PATH': '/bin:/usr/bin',
    }

# Generated at 2022-06-12 23:20:59.399305
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from units.compat import unittest
    from units.compat.mock import MagicMock

    # Mock module and get_bin_path()
    module = MagicMock()
    module.get_bin_path.return_value = True

    # Mock run_command
    module.run_command.return_value = (0, 'C', '')

    # Mock module fail_json
    module.fail_json = MagicMock()

    # Test case 1: If get_bin_path() return False
    module.get_bin_path.return_value = False
    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    # Test case 2: If run_command() raises error

# Generated at 2022-06-12 23:21:10.762171
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # set up dummy module with run_command mocking
    class TestModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(TestModule, self).__init__(*args, **kwargs)

            self.exit_json = None
            self.fail_json = None

        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None):
            out = ''
            cmd_to_run = cmd[0]

            if cmd_to_run == 'locale':
                # case 1, locale is not installed
                if cmd[1] == '-a':
                    out = '''
                        C
                        C.UTF-8
                        POSIX
                    '''


# Generated at 2022-06-12 23:21:18.813400
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():


    # test with english preferred
    lc_all = 'en_US.utf8'
    preferred = ['en_US.utf8', 'C']
    rc = 0
    out = 'C\nen_US.utf8\n'
    err = ''
    return_value = get_best_parsable_locale(MockModule(lc_all, rc, out, err), preferred)
    assert return_value == 'en_US.utf8'

    # test with french preferred
    lc_all = 'en_US.utf8'
    preferred = ['fr_FR.utf8', 'C']
    rc = 0
    out = 'en_US.utf8\nfr_FR.utf8\n'
    err = ''

# Generated at 2022-06-12 23:21:29.872390
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(object):
        def __init__(self, locale=None):
            self._locale = locale

        def get_bin_path(self, name, required=False):
            if name == 'locale':
                return self._locale

        def run_command(self, command, check_rc=True, search_path_relative=True, executable=None, data=None, prompt=None,
                        environ_update=None, encoding=None, errors=None):
            if command[0] == self._locale:
                return 0, 'C\nC.utf8\nC.UTF-8\nen_US.utf8\nen_US.UTF-8\n', ''

# Generated at 2022-06-12 23:21:54.567554
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class AnsibleModuleMock(AnsibleModule):

        def __init__(self, fail_json_mock):
            super(AnsibleModuleMock, self).__init__()
            self.fail_json = fail_json_mock
            self.bin_path_mock = None

        def get_bin_path(self, exe):
            return self.bin_path_mock

        def run_command(self, args):
            if args[0] == 'locale':
                if len(args) == 1:
                    return 0, "C.UTF-8\nen_US.UTF-8\nC.utf8\nen_US.utf8\nC\nen_US\nPOSIX", ""

# Generated at 2022-06-12 23:22:03.856935
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    dummy_module = AnsibleModule(
        argument_spec={},
    )

    assert get_best_parsable_locale(dummy_module, None, True) == 'C'
    assert get_best_parsable_locale(dummy_module, ['en_US.utf8', 'C.utf8', 'C', 'POSIX'], True) == 'C'
    assert get_best_parsable_locale(dummy_module, ['en_US.utf8', 'C.utf8', 'C', 'POSIX'], True) == 'C'

# Generated at 2022-06-12 23:22:12.199639
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from .unit.compat import mock, unittest
    from .unit.modules.utils import set_module_args

    class TestGetBestParsableLocale(unittest.TestCase):
        def setUp(self):
            self.mock_module = mock.MagicMock()
            self.mock_module.run_command.side_effect = [
                (0, 'C\nen_US.utf8\n', ''),
                (0, 'C\nen_US.utf8\n', ''),
                (0, 'C\nen_US.utf8\n', ''),
                (0, '', ''),
            ]

        def tearDown(self):
            self.mock_module = None


# Generated at 2022-06-12 23:22:17.184476
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=['POSIX', 'C']) == 'POSIX'
    assert get_best_parsable_locale(None, preferences=['en_US', 'POSIX', 'C'], raise_on_locale=True) == 'en_US'

# Generated at 2022-06-12 23:22:26.097715
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module_fixture = AnsibleModule(
        argument_spec=dict(),
        # This is a workaround for AnsibleModule that doesn't allow run_command without fail_json and fail_json without run_command
        run_command_environ_update={'LANG': 'C', 'LC_ALL': 'C', 'LC_MESSAGES': 'C', 'LANGUAGE': ''}
    )

    preferred_locales = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    received = get_best_parsable_locale(module_fixture, preferred_locales)
    assert received == preferred_locales[0]

    # With no preferred locales, C should be returned
    preferred_locales = []
   

# Generated at 2022-06-12 23:22:29.152382
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    result = get_best_parsable_locale(module)
    assert result == 'C'

# Generated at 2022-06-12 23:22:36.833243
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import b


# Generated at 2022-06-12 23:22:46.349063
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.test_module import AnsibleModuleTest

    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.fail_json = AnsibleModuleTest.fake_fail_json
            self.exit_json = AnsibleModuleTest.fake_exit_json

        def get_bin_path(self, _):
            return 'fake/locale'

        def run_command(self, cmd):
            if cmd[1] == '-a':
                return 0, 'C\nen_US\n', ''
            else:
                return 0, '', ''

    m = FakeModule()

    # first test, preferred locale is en_US, no error checking
    assert 'en_US' == get_

# Generated at 2022-06-12 23:22:49.743519
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = None
    # This is a unit test and the locale command is not available on windows,
    # it will always use the default return value.
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:22:53.915609
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    get_best_parsable_locale test-cases()
    '''

    module = None
    preferences = None
    raise_on_locale = True
    found = get_best_parsable_locale(module, preferences, raise_on_locale)
    assert (found == 'C')

# Generated at 2022-06-12 23:23:10.306329
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:23:19.693488
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock for the AnsibleModule class
    class AnsibleModule:
        def get_bin_path(self, path):
            return 'locale'

        def run_command(self, cmd):
            if cmd[1] == '-a':
                return 0, 'C\nen_US.utf8', None
            if cmd[1] == '-tc':
                return 0, 'C', None

    # Test default preference
    m = AnsibleModule()
    assert get_best_parsable_locale(m) == 'C'

    # Test for user preference
    m = AnsibleModule()
    assert get_best_parsable_locale(m, preferences=['en_US.utf8', 'C']) == 'en_US.utf8'

    # Test for the case when locale is not present

# Generated at 2022-06-12 23:23:28.292532
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class DummyModule(object):

        def __init__(self, out, err, rc):
            self._out = out
            self._err = err
            self._rc = rc

        def get_bin_path(self, executable):
            return True

        def run_command(self, command):
            return self._rc, self._out, self._err

    # Test 1: normal behavior
    out1 = True
    err1 = False
    rc1 = 0
    mod1 = DummyModule(out1, err1, rc1)
    # normal, out has locales
    out1 = 'C\nen_US.utf8\nC.utf8\n'

# Generated at 2022-06-12 23:23:35.503051
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    from ansible.module_utils.basic import AnsibleModule
    results = {}
    results['rc'] = 0
    results['out'] = 'C.utf8\nen_US.utf8\nPOSIX\n'
    results['err'] = ''
    module = mock.Mock()
    module.run_command.return_value = (results['rc'], results['out'], results['err'])
    module.get_bin_path.return_value = '/usr/bin/locale'
    module.module_args = {}
    module.params = {}
    module.check_mode = False
    module.no_log = False
    module.debug = False
    module.args = {}
    module.fail_json.return_value = {}
    module.exit_json.return_value = {}


# Generated at 2022-06-12 23:23:41.178506
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )

    # Test case where locale is not found
    locale = module.get_bin_path = lambda x: None
    assert get_best_parsable_locale(module) == 'C'

    # Test case where output of locale -a is empty
    (rc, out, err) = (0, '', '')
    module.run_command = lambda x: (rc, out, err)
    available = []
    assert get_best_parsable_locale(module) == 'C'

    # Test case where locale is found

# Generated at 2022-06-12 23:23:45.442600
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Unit test for function get_best_parsable_locale
    preferences = None
    raise_on_locale = False
    # preferred locale set to 'C'
    # If a module has a default value, it can be ignored
    assert get_best_parsable_locale(None, preferences, raise_on_locale) == 'C'
    # available locale set to en_US.utf8
    # If a module has a default value, it can be ignored
    preferences = ['en_US.utf8', 'C']
    assert get_best_parsable_locale(None, preferences, raise_on_locale) == 'en_US.utf8'

# Generated at 2022-06-12 23:23:56.584308
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # These should not raise a RuntimeWarning
    assert get_best_parsable_locale() == 'C'
    assert get_best_parsable_locale(
        preferences=['en_US.utf8', 'en_US.iso88591', 'C', 'POSIX']
    ) == 'C'
    assert get_best_parsable_locale(
        preferences=['foo', 'en_US.utf8', 'en_US.iso88591', 'C', 'POSIX']
    ) == 'C'
    assert get_best_parsable_locale(
        preferences=['en_US.ascii88591', 'C', 'POSIX']
    ) == 'C'

# Generated at 2022-06-12 23:23:58.080825
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:24:04.724862
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import sys

    fake_module = os
    fake_module.get_bin_path = os.getenv
    fake_module.run_command = os.spawnvp
    fake_module.exit_json = sys.exit

    try:
        loc = get_best_parsable_locale(fake_module)
    except RuntimeWarning as e:
        real_stdout = sys.stdout
        sys.stdout = os.devnull
        print("WARNING: Failed to get locale, defaulting to 'C' (%s)" % e)
        sys.stdout = real_stdout
        loc = 'C'

    assert loc == 'C'

# Generated at 2022-06-12 23:24:11.572068
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Mock ansible module
    module = AnsibleModule(name='test', argument_spec={})

    # Test with no preference provided
    assert get_best_parsable_locale(module) == 'C'

    # Test with invalid preference
    assert get_best_parsable_locale(module, ['Invalid_Preference']) == 'C'

    # Test with valid preference (C.UTF8)
    assert get_best_parsable_locale(module, ['C.utf8']) == 'C.utf8'

    # Test with valid preference (POSIX)
    assert get_best_parsable_locale(module, ['POSIX']) == 'POSIX'

    # Test with invalid and valid preference (POSIX)
    assert get_best

# Generated at 2022-06-12 23:24:34.662469
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    dummy_module = AnsibleModule(argument_spec={})

    # test valid locale name
    en_utf_locale = "en_US.utf8"
    assert get_best_parsable_locale(dummy_module, (en_utf_locale,)) == en_utf_locale

    # test locale which is not present
    hypothetical_locale = "ABCDEF"
    assert get_best_parsable_locale(dummy_module, (hypothetical_locale,)) == 'C'

    # test the case when locale is not present in system
    dummy_module.get_bin_path = lambda arg: None
    assert get_best_parsable_locale(dummy_module) == 'C'

# Generated at 2022-06-12 23:24:45.225355
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Fake module
    class TestModule(object):
        def get_bin_path(self, arg):
            return 'locale'

        def run_command(self, arg):
            if arg[1] == '-a':
                return 0, 'C\nC.UTF-8\nEn_US.UTF-8\nen_US.utf8\n', ''
            else:
                return 0, '', ''

    # Test with no argument
    module = TestModule()
    assert get_best_parsable_locale(module) == 'C.UTF-8'

    # Test with argumenmt which lists
    module = TestModule()

# Generated at 2022-06-12 23:24:50.196780
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # fail_json() is a private method, so the RuntimeWarning must be captured to test a warning case
    try:
        locale = get_best_parsable_locale(module)
        assert locale == 'C'
        assert isinstance(locale, str)
    except RuntimeWarning:
        pass

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    locale = get_best_parsable_locale(module)
    assert locale == 'C'
    assert isinstance(locale, str)

    locale = get_best_parsable_locale(module, preferences=["en_US.utf8"])
    assert locale == 'en_US.utf8'


# Generated at 2022-06-12 23:25:00.014807
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for function get_best_parsable_locale
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleFallbackNotFound
    from ansible.module_utils.basic import AnsibleFallbackLocaleUTF8

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    module.get_bin_path = AnsibleModule.get_bin_path

    class MockAnsibleModule(object):

        def __init__(self, arg):
            self._argv = arg

        def get_bin_path(self, arg, required=False, opt_dirs=None):
            if arg != "locale" or not required:
                return arg


# Generated at 2022-06-12 23:25:11.788536
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # dummy AnsibleModule instance
    module = object()
    module.get_bin_path = lambda x: '/usr/bin/%s' % x
    module.run_command = lambda x: (0, 'C\nen_US.utf8\n', '')

    os_preferences = ['C', 'C.utf8', 'en.utf8', 'POSIX', 'en_US.utf8']
    available_locales = ['C', 'en_US.utf8']
    locales = []

    # Test with a OS that have C.utf8 locale and
    # an installed locale that matches with C.utf8
    module.run_command = lambda x: (0, u'C\nC.utf8\nen_US.utf8\nen_US.utf8\n', '')

# Generated at 2022-06-12 23:25:23.521508
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    ############################################################################
    # Options for testing, commandline args into testing.
    #
    # NOTE: because of how error results are handled, this should probably be
    #  moved to a non-module test and not use the AnsibleModule
    ############################################################################
    from ansible.module_utils.basic import AnsibleModule
    import types

    module = AnsibleModule(argument_spec={}, check_invalid_arguments=False, add_file_common_args=True)

    ############################################################################
    # Test successful get_best_parsable_locale
    #
    # This test is modeled after the AnsibleModule.run_command method and
    #  its return values.
    ############################################################################
    # Inject our own module call (not mocking, just a different method)
    module.run_command

# Generated at 2022-06-12 23:25:34.252985
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    import os
    import tempfile

    temp = tempfile.NamedTemporaryFile(delete=False)

    # Stub our module and write to 'locale -a' to temp file
    am = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    with temp as tempf:
        # empty case as though we had no locales
        assert get_best_parsable_locale(am) == 'C'
        # no locales
        tempf.write('Foo\n')
        tempf.flush()
        am.get_bin_path = lambda x: temp.name
        assert get_best_parsable_locale(am) == 'C'
        # first preferred locale found
        tempf.write

# Generated at 2022-06-12 23:25:42.269687
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(argument_spec={})
    # test for valid return with valid input
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    available = ['en_US.utf8', 'C.utf8', 'C', 'POSIX']
    best = get_best_parsable_locale(module, preferences, available)
    assert best == 'C.utf8'

    # test for valid return with valid input but only one element
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    available = ['C.utf8']
    best = get_best_parsable_locale(module, preferences, available)
    assert best == 'C.utf8'

# Generated at 2022-06-12 23:25:45.586269
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    # check that 'C' locale is used when locale command is not found
    os.environ['PATH'] = ''
    assert get_best_parsable_locale(module) == 'C', "locale is not 'C'"

# Generated at 2022-06-12 23:25:55.959930
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Fake module to test the function
    class FakeModule:
        def __init__(self):
            self.run_command_called = False
            self.bin_path_called = False

        def get_bin_path(self, name):
            self.bin_path_called = True
            if name == 'locale':
                return '/usr/bin/locale'
            else:
                return None

        def run_command(self, args):
            self.run_command_called = True
            if args[1] == '-a':
                return (0, "C\nen_US.utf8\n", "")
            else:
                return (-1, "", "Error")


    fake_module = FakeModule()
    default_result = get_best_parsable_locale(fake_module)
   

# Generated at 2022-06-12 23:26:35.973646
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False,
    )

    # Test that the default value of preferences is correct
    preferences = [
        'C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(module, preferences) == 'C'

    # Test that an empty list of preferences results in C
    preferences = []
    assert get_best_parsable_locale(module, preferences) == 'C'

    # Test that an random list of preferences results in C
    preferences = ['ABC', 'DEF', 'GHI']
    assert get_best_parsable_locale(module, preferences) == 'C'

    # Test that

# Generated at 2022-06-12 23:26:44.366604
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    class MockModule:
        def __init__(self, preferences):
            self.preferences = preferences

        def get_bin_path(self, cmd):
            if cmd in ['locale']:
                return '/bin/locale'
            else:
                return ''

        def run_command(self, cmd):
            if '/bin/locale' in cmd:
                return 0, self.preferences, ''
            else:
                return 1, '', ''

    # test preferences are returned in order of preference
    for expected,preference in enumerate(preferences):
        module = MockModule([preference])
        out = get_best_parsable

# Generated at 2022-06-12 23:26:52.860151
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import shutil
    import tempfile

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.test.test_utils.test_get_best_locale import _TestGetBestLocale
    from ansible.module_utils.test.test_utils.test_get_best_locale import _FakeModule
    from ansible.module_utils.test.test_utils.test_get_best_locale import _FakeModuleMock

    def get_fake_module(locale_dir, locale_data):
        MOCK_MODULE_PATH = '/dev/null'
        MOCK_MODULE_ARGS = {'test': 'true'}

# Generated at 2022-06-12 23:27:01.588779
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    new_stdout = sys.stdout

    class MockPopen:
        def __init__(self):
            self.rc = 0
            self.STDOUT_text = 'C.utf8\nen_US.utf8\n'
            self.STDERR_text = ''

        def communicate(self):
            return (self.STDOUT_text, self.STDERR_text)

        def poll(self):
            return self.rc

    class MockModule(AnsibleModule):
        def __init__(self):
            self.locale = '/usr/bin/locale'
            self.run_command_rc = 0
            self.run_command_out = ''
            self.run_command_err = ''
