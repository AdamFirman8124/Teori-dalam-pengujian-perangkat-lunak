

# Generated at 2022-06-12 23:17:17.303428
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    # default set of locales
    assert 'C' == get_best_parsable_locale(module)

    # let's say current locales are limited to ascii because we are on Windows
    assert 'C' == get_best_parsable_locale(module, preferences = ['C.utf8','en_US.utf8','C','POSIX'])

    # let's say current locales are limited to ascii because we are on Windows
    assert 'C' == get_best_parsable_locale(module, preferences = ['C.ascii','en_US.ascii','C','POSIX'])

    # let's say we are in China, but still want to use english
   

# Generated at 2022-06-12 23:17:24.947518
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    This unit test is not meant to cover the full functionality, but it tests
    the cases that were found to break in practice.
    """
    def run_command(cmd, *args, **kwargs):
        return 0, kwargs.get('stdout'), None

    # Test if we prefer all English locales
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    module = type('', (), dict(get_bin_path=lambda _, bin: bin, run_command=run_command))()
    result = get_best_parsable_locale(module, preferences)
    assert result == 'en_US.utf8'

    # Test if we prefer all English locales (even if in reverse order)
    preferences.reverse()
    result = get_best_pars

# Generated at 2022-06-12 23:17:25.908701
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:17:28.866988
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils
    found = ansible.module_utils.basic.get_best_parsable_locale(None)
    assert found == 'C', "The default locale should be 'C'"

# Utility function to return a copy of the old dictionary with keys renamed to
# the value of the key in replace_strs.

# Generated at 2022-06-12 23:17:39.194748
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec=dict(
            locale=dict(type='str', default='en_US.utf8'),
        ),
        supports_check_mode=True
    )

    assert get_best_parsable_locale(test_module, ['C', 'en_US.utf8', 'POSIX']) == 'C'

    test_module = AnsibleModule(
        argument_spec=dict(
            locale=dict(type='str', default='en_US.utf8'),
        ),
        supports_check_mode=True
    )

    assert get_best_parsable_locale(test_module, ['POSIX', 'C']) == 'C'


# Generated at 2022-06-12 23:17:48.516212
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Sample locale content
    sample_locale_out = '''C
    POSIX
    en_US.utf8
    en_US.UTF-8'''

    from ansible.module_utils.basic import AnsibleModule

    env_vals = dict()
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    # create a mock module with a default locale command output
    def mock_run_command(cmd, check_rc=True, close_fds=True,
                         executable=None, data=None, binary_data=False):
        return 0, sample_locale_out, ''

    module.run_command = mock_run_command

    # first test, with default preferences and no exceptions
    result = get_best_parsable_locale(module)

# Generated at 2022-06-12 23:17:55.206822
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # We need to mock module to somewhat mimic AnsibleModule.
    # We cannot use mock_module because that would require AnsibleModules
    # to be installed.
    class Module:
        def __init__(self):
            pass

        def get_bin_path(self, name):
            return name

        def run_command(self, cmd):
            # Check if the command is to return the locale information
            if cmd[0] == 'locale' and cmd[1] == '-a':
                return 0, 'C\nC.UTF-8\nC.utf8\nen_US.utf8\nen_US.UTF-8', ''
            raise AssertionError("Unexpected command called %s %s" % (cmd[0], cmd[1]))

    # Nothing to be imported.
    module = Module()
   

# Generated at 2022-06-12 23:18:07.362536
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Stubbed module
    class MockModule(object):
        def get_bin_path(self, tool, required=False):
            return tool

        def run_command(self, cmd, check_rc=True):
            if cmd[0] == 'locale':
                if cmd[1] == '-a':
                    return (0, "en_US.utf8\nen_US.UTF-8\nen_US\nen_US@euro\nen_US.iso88591\nen_US.iso885915@euro\n", None)
                raise RuntimeError("Bad command: %s" % to_native(cmd))
            if cmd[0] == '/bin/ls':
                return (0, "", None)
            return (1, "", None)

    # Test valid locale
    m = MockModule()

# Generated at 2022-06-12 23:18:16.977665
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    #Mock module class
    class FakeModule(object):
        def __init__(self):
            self.bin_path_cache = {}
        def get_bin_path(self, cmd):
            return cmd
        def run_command(self, cmd):
            return 0, 'a-locale\nb-locale\nen_GB.utf8\nC\nen_US.utf8\n', None

    module = FakeModule()
    assert get_best_parsable_locale(module) == 'en_GB.utf8'
    preferences = ['en_US.utf8', 'fr_FR.utf8']
    assert get_best_parsable_locale(module, preferences=preferences) == 'en_US.utf8'
    preferences = ['b-locale']
    assert get_best_p

# Generated at 2022-06-12 23:18:20.979429
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    # Mock class for testing
    class LocalTest(object):
        def __init__(self, module_name, module_paths):
            if module_paths is None:
                module_paths = ["./"]
            self.bin_path = lambda x: "%s/%s" % (module_paths[0], x)
            self.run_command = lambda x, environ_update=None: (0, x, '')

    module = LocalTest("test", None)
    actual = get_best_parsable_locale(module)
    assert actual == 'C'

    # Same as above, but now add an available locale

# Generated at 2022-06-12 23:18:35.940887
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    if 'LANG' in os.environ:
        del os.environ['LANG']
    if 'LC_ALL' in os.environ:
        del os.environ['LC_ALL']

    assert os.environ.get('LANG') is None
    assert os.environ.get('LC_ALL') is None

    C = get_best_parsable_locale(module)
    assert C == 'C'

    os.environ['LANG'] = 'POSIX'
    assert os.environ['LANG'] == 'POSIX'

    C = get_best_parsable_locale(module)

# Generated at 2022-06-12 23:18:45.287609
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.utils.display import Display
    from ansible.module_utils.basic import AnsibleModule

    display = Display()

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # test that basic functionality works
    assert get_best_parsable_locale(module) == 'C'

    # test that locale preferences are taken into account
    assert get_best_parsable_locale(module, preferences=['en_US.utf8']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'C']) == 'en_US.utf8'

    # test that when an available locale is not in preferences it picks the last available locale
    assert get_best_

# Generated at 2022-06-12 23:18:50.812157
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule, get_exception
    import locale

    locale_path = '/usr/bin/locale'

# Generated at 2022-06-12 23:19:01.252292
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    import sys
    import os

    class FakeAnsibleModule(basic.AnsibleModule):
        def __init__(self):
            super(FakeAnsibleModule, self).__init__(_ansible_version=2.5,
                                                    _ansible_module_name='fake_get_best_parsable_locale',
                                                    argument_spec={'preferences': dict(required=False),
                                                                   'raise_on_locale': dict(required=False),
                                                                   'test_default_behaviour': dict(required=False)
                                                                   })

        def get_bin_path(self, name):
            return "/usr/bin/{0}".format(name)

    def run_command(self, cmd):
        return

# Generated at 2022-06-12 23:19:11.432368
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.compat.tests import unittest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text

    class TestLocale(unittest.TestCase):
        def setUp(self):
            self.amodule = AnsibleModule({})

        def test_get_best_parsable_locale(self):
            # setting rc=1 and out=None to force error
            self.amodule.run_command = lambda x: (1, None, u"Error")
            self.assertEqual(get_best_parsable_locale(self.amodule, None, True), u'C')
            self.amodule.run_command = lambda x: (0, to_text(u""), u"")

# Generated at 2022-06-12 23:19:21.139886
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    # This is a sane default and what we expect in most cases for
    # parsing ansible output
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, ['en_US.utf8']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, ['C.utf8']) == 'C'
    assert get_best_parsable_locale(module, ['C', 'POSIX']) == 'C'

    assert get_best_parsable_locale(module, ['C.utf8', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:19:27.924466
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    from ansible.module_utils import basic

    module = mock.MagicMock(spec=basic.AnsibleModule)
    module.get_bin_path.return_value = 'locale'
    module.run_command.return_value = (0, 'C\nC.utf8\nen_US.utf8\nPOSIX\n', None)
    result = get_best_parsable_locale(module)
    assert result == 'C.utf8'

# Generated at 2022-06-12 23:19:39.494199
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    # mock for a module
    module = sys.modules.get(__name__)
    # mock module.run_command
    module.run_command = lambda *args, **kwargs: (0, 'C\nen_US.utf8\nen_US.utf-8\nC.utf8\nen_US.UTF-8\nPOSIX\n', '')
    # case-1: preferences=None
    assert get_best_parsable_locale(module) == 'C'

    # case-2: preferences=[]
    assert get_best_parsable_locale(module, []) == 'C'

    # case-3: preferences=Preferences in order of locale

# Generated at 2022-06-12 23:19:48.230401
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import sys
    import unittest

    from ansible.module_utils.basic import AnsibleModule

    class TestGetBestParsableLocale(unittest.TestCase):
        def setUp(self):
            self.module = AnsibleModule(
                argument_spec=dict(
                    raise_on_locale=dict(type='bool', default=False),
                ),
            )

            def fail_json(msg):
                self.fail(msg)

            def run_command(args):
                return 0, 'C.utf-8', ''

            self.module.run_command = run_command
            self.module.fail_json = fail_json

        def test_no_utf(self):
            preferences = ['C']

# Generated at 2022-06-12 23:19:57.541333
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(name='test')
    module.run_command = lambda cmd, check_rc=True: (0, 'C\nen_US.utf8\nen_US.UTF-8\n', '')

    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.UTF-8', 'C']) == 'en_US.utf8'
    assert get_best_parsable_locale(module) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.UTF-8', 'WAT']) == 'en_US.utf8'

    module

# Generated at 2022-06-12 23:20:12.375883
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    class Module:
        def __init__(self):
            self.fail_json = lambda **_: sys.exit(1)
            self.run_command = lambda *_: (0, "en_US.utf8", "")
            self.get_bin_path = lambda *_: ""

    module = Module()

    # Test the exception path
    try:
        loc = get_best_parsable_locale(module, preferences=['C.utf8'])
        assert False, "Expected exception due to missing get_bin_path"
    except RuntimeWarning as e:
        assert "Could not find 'locale' tool" in str(e)

    # Test the default value returned if no preferences are specified
    module.get_bin_path = lambda *_: "locale"
    module.run_

# Generated at 2022-06-12 23:20:23.433413
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Objective:
    - Make sure that the get_best_parsable_locale function returns the right
      value given different inputs.

    :return:
        None
    '''
    from ansible.module_utils.basic import AnsibleModule

    class AnsibleMod:
        def __init__(self):
            self.params = {}
            self.fail_json = None
            self.exit_json = None

        def run_command(self, cmd):
            return 0, '', ''

        def get_bin_path(self, name):
            return None

    # Test 1: no locale found
    am = AnsibleMod()
    assert 'C' == get_best_parsable_locale(am)

    class AnsibleMod:
        def __init__(self):
            self.params = {}

# Generated at 2022-06-12 23:20:34.482934
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest

    test_cases = [
        # test case 1: no binary, raise exception
        # test case 2: no binary, no raise exception
        # test case 3: no output, raise exception
        # test case 4: no output, no raise exception
        # test case 5: rc != 0, raise exception
        # test case 6: rc != 0, no raise exception
        # test case 7: wrong output, raise exception
        # test case 8: wrong output, no raise exception
        # test case 9: correct output, no raise exception

        # We need to do this with mock and side_effects, not sure how to unit test this with the real run_command
        # TODO: see if we can mock module.run_command()
    ]


# Generated at 2022-06-12 23:20:44.691069
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import pytest

    module = AnsibleModule(argument_spec={})

    def run_command_mock(module, args, check_rc=False, close_fds=True):
        if args[1] == '-a' and args[0] == 'locale':
            return (0, 'C\nen_US.utf8\nC.utf8\nPOSIX\nen_US.utf8\nC', '')
        elif args[0] == 'locale':
            return (0, '', '')

    def get_bin_path_mock(module, tool, required=False):
        if tool == 'locale':
            return 'locale'

    module.run_command = run_command_mock
    module.get_bin

# Generated at 2022-06-12 23:20:53.835926
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    class FakeModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.check_mode = True
            self.debug = False
            self.exit_json_called = False
            self.fail_json_called = False
            self.log_invocation_called = False
            self.log_invocation_args = []
            self.log_invocation_kwargs = {}
            self.runner = None
            self.no_log_values = []
            self.fallback_local_templar = False
            self.disable_fallback = False
            self.aliases = {}
            self.syslog_facility = []


# Generated at 2022-06-12 23:20:57.689591
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    locale = get_best_parsable_locale(module)
    assert locale == 'C'

# Generated at 2022-06-12 23:21:08.915917
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        This is unit test for the function get_best_parsable_locale
    '''
    locale_out = 'C\n'
    locale_out += 'C.UTF-8\n'
    locale_out += 'en_US.utf8\n'
    locale_out += 'en_US.UTF-8\n'
    locale_out += 'POSIX\n'

    class AnsibleModule:
        def __init__(self, **kwargs):
            self.fail_json = kwargs.get('fail_json', None)
            self.params = kwargs.get('params', None)

        def get_bin_path(self, command):
            return '/usr/bin/locale'


# Generated at 2022-06-12 23:21:17.136952
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Make sure get_best_parsable_locale function works as expected
    '''
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        print("Could not find Ansible Module. Cannot test get_best_parsable_locale()")
        return
    class FakeModule:
        '''
            We don't really need a full ansible module for Simple AnsibleModule that
            only defines two methods. One that returns the binary path and another
            that runs a command.
        '''
        BIN_PATH = {
            'locale': '/usr/bin/locale'
        }

        def __init__(self):
            pass

        def get_bin_path(self, command):
            return self.BIN_PATH.get(command, '')



# Generated at 2022-06-12 23:21:27.958573
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.process import get_bin_path

    module = AnsibleModule({})

    # check for locale and warn if not found, then use 'C'
    locale = get_bin_path(module, 'locale')
    if not locale:
        module.fail_json(msg="Required executable 'locale' not found.  Please see ansible.cfg documentation for more information")

    # get available locales
    rc, out, err = module.run_command([locale, '-a'])

    if rc == 0:
        if out:
            available = out.strip().splitlines()

# Generated at 2022-06-12 23:21:32.943069
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

    mock_module = MockModule()
    mock_module.run_command.return_value = (0, 'C', '')
    assert get_best_parsable_locale(mock_module) == 'C'

# Generated at 2022-06-12 23:21:49.170408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=['C', 'POSIX', 'C.utf8', 'en_US.utf8']) == 'C'
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'en_US.utf8', 'POSIX', 'C']) == 'C'

# Generated at 2022-06-12 23:22:00.058463
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModule():
        def __init__(self, **kwargs):
            self.fail_json_msg = None

        def get_bin_path(self, _):
            return 'locale'

        def run_command(self, _):
            # locale -a returns the list of locales that are supported on the system,
            # to simulate different environments we return different output here
            # in order to pick the best locale for parsing
            # for example: C.utf8, C, POSIX, en_US.utf8
            return 0, 'C.utf8\nC\nen_US.utf8\nPOSIX', ''

        def fail_json(self, **kwargs):
            pass

        def exit_json(self, **kwargs):
            pass

    # First test
    # locale -a returns C.utf

# Generated at 2022-06-12 23:22:08.840038
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import ansible.module_utils.basic
    assert os.getenv('LC_ALL') == 'C'
    assert os.getenv('LC_CTYPE') == 'C'
    assert os.getenv('LANG') == 'C'
    assert os.getenv('LANGUAGE') == 'C'
    assert os.getenv('LC_MESSAGES') == 'C'
    assert os.getenv('LC_NUMERIC') == 'C'
    assert os.getenv('LC_TIME') == 'C'
    assert os.getenv('LC_COLLATE') == 'C'
    assert os.getenv('LC_MONETARY') == 'C'
    assert os.getenv('LC_PAPER') == 'C'

# Generated at 2022-06-12 23:22:16.681693
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    class TestAnsibleModule(AnsibleModule):
        def run_command(self, args):
            if args == ['locale', '-a']:
                return 0, 'C\nen_US.utf8\nC.utf8\nPOSIX\n', ''
            else:
                assert False, args
    am = TestAnsibleModule(argument_spec={})
    assert get_best_parsable_locale(am) == 'en_US.utf8'
    assert get_best_parsable_locale(am, preferences=['foo', 'bar']) == 'C'
    assert get_best_parsable_locale(am, preferences=['C', 'bar']) == 'C'

# Generated at 2022-06-12 23:22:25.771131
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import tempfile
    import os
    import shutil
    import sys

    class AnsibleModule:

        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, *args, **kwargs):
            return args[0]

        def run_command(self, *args, **kwargs):
            return 0, '', ''

    class MyTest(unittest.TestCase):

        def setUp(self):
            self.ansible_module = AnsibleModule()
            self.tempdir = tempfile.mkdtemp()
            os.environ["PATH"] = self.tempdir + os.pathsep + os.environ["PATH"]

        def tearDown(self):
            shutil.rmtree(self.tempdir)

# Generated at 2022-06-12 23:22:34.630595
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping

    assert get_best_parsable_locale(AnsibleModule(argument_spec=dict())) == 'C'

    # override locale list so we can just test the return value
    # also test list of locale names and a single locale name
    preferences = ['C', 'POSIX', 'en_US.utf8']

# Generated at 2022-06-12 23:22:44.802984
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Tests get_best_parsable_locale function
    '''
    # Load the required module
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule

    # Initialize the AnsibleModule instance
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Test the function get_best_parsable_locale
    assert get_best_parsable_locale(module, preferences=None, raise_on_locale=False) == 'C'
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX'], raise_on_locale=False) == 'C'
    assert get_

# Generated at 2022-06-12 23:22:54.724762
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class ModuleMock(object):
        def __init__(self, locale_path=None, locale_output='C.utf8\nen_US.utf8', locale_error='', locale_rc=0):
            self.locale_path = locale_path
            self.locale_output = locale_output
            self.locale_error = locale_error
            self.locale_rc = locale_rc

        def get_bin_path(self, executable):
            if executable == 'locale':
                return self.locale_path
        def run_command(self, cmd):
            return self.locale_rc, self.locale_output, self.locale_error


# Generated at 2022-06-12 23:23:01.822393
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common_koji

    mod = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    locale = common_koji.get_best_parsable_locale(mod)
    assert(locale == 'C')

    # test if it always returns 'C' when no preference is provided
    # reason behind this is that this function can be called with
    # raise_on_locale = True or False
    locale = common_koji.get_best_parsable_locale(mod, preferences=None)
    assert(locale == 'C')

    # test if it returns en_US.utf8 if it is defined
    locale = common_koji.get_best_parsable

# Generated at 2022-06-12 23:23:10.796917
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:23:26.521254
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Mocking up a fake module
    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = {}


# Generated at 2022-06-12 23:23:34.097777
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, ['C']) == 'C'
    assert get_best_parsable_locale(None, ['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['C', 'POSIX', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['C', 'POSIX', 'POSIX', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:23:41.252999
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._text import to_text


# Generated at 2022-06-12 23:23:44.305308
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def run_cmd(cmd):
        if cmd[1].startswith('-a'):
            return 0, 'C C.UTF-8 en_US.utf8', ''
        return 0, 'C', ''

    m = AnsibleModule()
    m.run_command = run_cmd
    assert get_best_parsable_locale(m) == 'C'

# Generated at 2022-06-12 23:23:56.247601
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    req_vars = {}
    req_vars['run_command'] = FakeRunCommand()
    req_vars['get_bin_path'] = FakeGetBinPath()
    req_vars['run_command'].fake_run_command_results = (0, '', '')
    module = AnsibleModule(argument_spec={}, required_together=[], supports_check_mode=True, **req_vars)

    locale = get_best_parsable_locale(module, preferences=None, raise_on_locale=False)
    assert locale == 'C'

    locale = get_best_parsable_locale(module, preferences=['notreal', 'C'], raise_on_locale=False)
    assert locale == 'C'

    # not a real locale but good enough
    req_v

# Generated at 2022-06-12 23:24:04.783173
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    assert 'C' == get_best_parsable_locale(None)

    assert 'C.UTF-8' == get_best_parsable_locale(None, preferences=['C.UTF-8', 'C.UTF8'])

    assert 'C.UTF-8' == get_best_parsable_locale(None, preferences=['C.UTF-8', 'C.UTF8', 'C'])

    assert 'C' == get_best_parsable_locale(None, preferences=['whatever', 'C'])

    assert 'C' == get_best_parsable_locale(None, preferences=['whatever', 'C'], raise_on_locale=False)

    raised = False

# Generated at 2022-06-12 23:24:05.997923
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test for the function get_best_parsable_locale
        Returns None if no unit test is implemented
    '''
    pass

# Generated at 2022-06-12 23:24:16.033402
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class TestModule(object):

        def __init__(self, locale=None):
            self.locale = locale

        def get_bin_path(self, tool):
            return self.locale

        def run_command(self, cmd):
            return 0, cmd[1], None

    module = TestModule('/some/where/locale')
    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    out = 'POSIX\nC.UTF-8\nen_US\nen_US.ISO-8859-1\nen_US.ISO-8859-15\nen_US.UTF-8'
    module = TestModule('/some/where/locale')
    locale = get_best_parsable_locale(module)
    assert locale == 'C'



# Generated at 2022-06-12 23:24:26.398095
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test the get_best_parsable_locale function.
        The function get_best_parsable_locale is using subprocess module to
        run the command [locale, '-a']. Here we mock the output and the rc
        to be able to test the get_best_parsable_locale function.
    '''
    # test warnings
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import mock
    from ansible.module_utils.six import PY3

    # get_bin_path function return None
    module = mock.Mock()
    module.configure_mock(**{'_ansible_version': '2.8.0'})
    module.get_bin_path.return_value = None


# Generated at 2022-06-12 23:24:28.825755
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    locale = get_best_parsable_locale(module)
    assert locale == "C"

# Generated at 2022-06-12 23:24:45.639048
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # Ensure C is selected in the absence of any other choice
    assert get_best_parsable_locale(module) == 'C'

    # Check that the default prefs are found in the locale -a list
    module.run_command = lambda args: (0, "af_ZA.UTF-8\nan_US.UTF-8\nC\n", None)
    assert get_best_parsable_locale(module) == 'C'

    # Check that a preference not in the list causes C to be selected
    module.run_command = lambda args: (0, "af_ZA.UTF-8\nan_US.UTF-8\n", None)
    assert get_best_parsable_loc

# Generated at 2022-06-12 23:24:57.386855
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import os
    import sys

    tempdir = tempfile.mkdtemp(prefix="ansible_test")
    tempdir_locale = tempdir + '/locale'
    os.mkdir(tempdir_locale)

    # stub file that simulates locale output
    # both /usr/bin/locale and locale on MacOS behave the same
    # ie they take a -a option and get all supported locales
    test_file_path = tempdir_locale + "/locale"
    f = open(test_file_path, "w")
    f.write("C.utf8\nen_US.utf8\nen_US.utf8\nen_US.utf8\nC\nPOSIX")
    f.close()

   

# Generated at 2022-06-12 23:24:59.080575
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # TODO: Test that function gets expected locale.
    # TODO: Test that function gets C locale as fallback locale.
    pass

# Generated at 2022-06-12 23:25:11.082865
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest

    class AnsibleModuleMock(object):
        def __init__(self, out, err, rc):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, cmd):
            if cmd == "locale":
                return "/usr/bin/locale"
            else:
                return None

        def run_command(self, cmd):
            return (self.rc, self.out, self.err)

    module = AnsibleModuleMock("en_US.utf8\nen_US.utf8\nC\nPOSIX\n", "", 0)
    assert get_best_parsable_locale(module, raise_on_locale=False) == 'C'


# Generated at 2022-06-12 23:25:22.655545
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import ansible
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils.six.moves import zip

    def locale_a():
        sio = StringIO()
        avail = set()
        for line in sys.stdin:
            if line.strip() in avail:
                continue
            avail.add(line.strip())
            sio.write(line)
        sio.seek(0)

        return (sio, avail)

    def locale_fail():
        return 1, 'No such locale', ''

    def locale_success():
        return 0, '', ''


# Generated at 2022-06-12 23:25:33.421729
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import datetime
    import io
    import json
    import subprocess
    from ansible import constants as C
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.locale import get_best_parsable_locale

    # This is to use patched modules at test time
    sys.path.insert(0, 'test/module_utils')

    module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module) == 'C'

    module.run_command = lambda x, environ_update=None: (0, 'C.utf8\nen_US.utf8\nC\nPOSIX\neo_FW.utf8\nfr_FR.utf8\n', '')
    assert get_best_p

# Generated at 2022-06-12 23:25:39.979762
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module) == 'C'

    prefs = ['C', 'POSIX', 'bob']
    assert get_best_parsable_locale(module, prefs) == 'C'

    assert get_best_parsable_locale(module, ['POSIX']) == 'C'

    assert get_best_parsable_locale(module, ['en_US.utf8']) == 'en_US.utf8'

    assert get_best_parsable_locale(module, ['en_US.utf8', 'C']) == 'en_US.utf8'

# Generated at 2022-06-12 23:25:48.343790
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import base64
    import json
    import os
    import tempfile
    import textwrap
    from ansible.module_utils.basic import AnsibleModule

    script = textwrap.dedent('''\
        #!/usr/bin/python
        import os
        import sys
        import json
        import base64
        from ansible.module_utils.basic import AnsibleModule

        if __name__ == '__main__':
            module = AnsibleModule({})
            module.exit_json(**{
                'locale': module.get_bin_path('locale', True),
                'preferences': {},
                'locale_c': get_best_parsable_locale(module),
                'result': None
            })
        ''')


# Generated at 2022-06-12 23:25:58.600883
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = lambda cmd, cwd=None: (0, 'C.UTF-8\nC.utf8\nen_US.utf8\nPOSIX', None)
    result = get_best_parsable_locale(module)
    assert result == 'C.utf8'
    module.run_command = lambda cmd, cwd=None: (0, 'C.UTF-8\nen_US.utf8\nPOSIX', None)
    result = get_best_parsable_locale(module)
    assert result == 'en_US.utf8'

# Generated at 2022-06-12 23:26:03.485029
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as module_common

    test_module = module_common

    # Test for locale found
    locale = get_best_parsable_locale(test_module, ['fr_FR.utf8'])
    assert locale == 'fr_FR.utf8'

    # Test for locale not found
    locale = get_best_parsable_locale(test_module, ['fr_FR.utf8'], True)
    assert locale == 'C'

# Generated at 2022-06-12 23:26:22.804181
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ['en_US.utf8', 'en_US.utf-8']) == 'en_US.utf8'
    assert get_best_parsable_locale(None, ['fr_FR']) == 'C'
    assert get_best_parsable_locale(None, ['fr_FR'], True) == 'C'
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:26:26.564348
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec=dict())
    assert get_best_parsabl

# Generated at 2022-06-12 23:26:27.286549
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # This function does not have a unit test since it depends on the
    # ansible module
    pass

# Generated at 2022-06-12 23:26:37.560389
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.common.removed import removed_module
    latest_result = removed_module.warn_if_removed(removed_in='2.8')
    if latest_result is not None:
        # Function as been removed in current Ansible, and we
        # are running this unit test on a newer Ansible version
        return

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    # construct a mock module object
    class AnsibleModuleMock(AnsibleModule):
        def get_bin_path(self, executable, required=True, opt_dirs=None):
            if executable == 'locale':
                return True
            else:
                return False


# Generated at 2022-06-12 23:26:45.834635
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import locale
    import sys
    import unittest

    class FakeModule():
        def __init__(self):
            self.fail_json = unittest.TestCase.fail

        def get_bin_path(self, tool, required=None):
            return tool

        def run_command(self, command):
            if command == ['locale', '-a']:
                # this matches what the code above will return
                # so we can fake the executable to test
                return 0, "\n".join(locale.locale_alias.values()), ""
            else:
                raise ValueError("unexpected command")

    class TestGetBestParsableLocale(unittest.TestCase):
        def test_sane_locale(self):
            best = get_best_parsable_locale(FakeModule())


# Generated at 2022-06-12 23:26:54.354006
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:27:00.002289
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.common.process as process

    module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True, bypass_checks=True)
    module.run_command = lambda x, **kw: (0, '', '')

    test_get_best_parsable_locale_pass(module)
    test_get_best_parsable_locale_fail(module)



# Generated at 2022-06-12 23:27:08.695944
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import sys
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())
    if sys.version_info >= (3, 0):
        assert 'en_US.utf8' == get_best_parsable_locale(module, preferences=['en_US.utf8'])
        assert 'POSIX' == get_best_parsable_locale(module, preferences=['POSIX'])
        assert 'C' == get_best_parsable_locale(module, preferences=['C'])
        assert 'C' == get_best_parsable_locale(module, preferences=['de'])
        assert 'POSIX' == get_best_parsable_locale(module, preferences=['POSIX', 'de'])