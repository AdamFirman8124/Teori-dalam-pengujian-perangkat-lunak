

# Generated at 2022-06-12 23:17:14.033831
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale_test_module = AnsibleModule(argument_spec={})
    assert locale_test_module.get_best_parsable_locale() == 'C'
    assert locale_test_module.get_best_parsable_locale(['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:17:15.351090
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:17:24.551169
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import get_exception

    class MockModule(object):
        def get_bin_path(self, name):
            if name == "locale":
                return 'echo'
        def run_command(self, command):
            if command == ['echo', '-a']:
                return (0, 'C.utf8\nen_US.utf8\nC\nPOSIX', '')

    # Check with locale working and good locale available
    module = MockModule()
    out = get_best_parsable_locale(module)
    assert out == 'C.utf8'

    # Check with bad output
    module = MockModule()
    module.run_command = lambda x: (0, '', '')
    out

# Generated at 2022-06-12 23:17:31.097766
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Should return a locale that is available on the local machine
    """
    __import__('ansible.module_utils.basic')
    from ansible.module_utils.basic import AnsibleModule
    import os

    import pytest

    from ansible.module_utils.locale_utils import get_best_parsable_locale
    from ansible import constants as C

    if not os.path.exists(C.DEFAULT_LOCALE_DIR):
        return

    result = get_best_parsable_locale(AnsibleModule(argument_spec={}), raise_on_locale=True)
    assert len(result.split(b'.')) == 2

# Generated at 2022-06-12 23:17:42.074434
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for ansible.module_utils.common.get_best_parsable_locale function
        :return: None
    '''

# Generated at 2022-06-12 23:17:50.734303
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.modules.system.setup import get_best_parsable_locale

    class FakeModuleIndependant:
        def __init__(self, out, rc, err):
            self.bin_path = "/usr/bin/env"
            self.out = out
            self.rc = rc
            self.err = err
            self.fail_json_called = None
        def get_bin_path(self, arg):
            if arg == "locale":
                return arg
            return None
        def run_command(self, arg):
            return self.rc, self.out, self.err

    preference = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

# Generated at 2022-06-12 23:18:01.510008
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from . import test_get_bin_path

    # Inject a posix local
    origins = AnsibleModule._get_bin_path._origins
    AnsibleModule._get_bin_path._origins = origins[:2] + (('posix', b''),) + origins[2:]  # pylint: disable=protected-access

    module = AnsibleModule(
        argument_spec=dict(),
    )

    # Locale tool is not installed
    module.run_command = test_get_bin_path
    assert get_best_parsable_locale(module=module) == 'C'
    assert get_best_parsable_locale(module=module, preferences=['C', 'POSIX']) == 'C'

    # Locale

# Generated at 2022-06-12 23:18:11.890263
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test get_best_parsable_locale function
    '''

    class test_module:
        '''
            Mock class for AnsibleModule
        '''
        locale = 'C'
        out = None
        err = None

        def get_bin_path(self, bin_path):
            '''
                Mock method for get_bin_path
            '''
            return bin_path

        def run_command(self, cmd):
            '''
                Mock method for run_command
            '''
            if not cmd[1] == '-a':
                raise RuntimeWarning("Incorrect command %s" % cmd)

            return (0, self.out, self.err)

    test_ansible_module = test_module()

# Generated at 2022-06-12 23:18:20.043917
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    test_envs = []
    test_envs.append({"LC_ALL": "fr_BE.UTF-8"})
    test_envs.append({"LC_ALL": "fr_BE.UTF-8", "LANG": "en_US.UTF-8"})
    test_envs.append({"LC_ALL": "fr_BE.UTF-8", "LANG": "en_US.UTF-8", "LANGUAGE": "en_US.UTF-8"})
    test_envs.append({"LC_ALL": "fr_BE.UTF-8", "LANG": "en_US.UTF-8", "LANGUAGE": "en_US.UTF-8", "LC_MESSAGES": "en_US.UTF-8"})

# Generated at 2022-06-12 23:18:30.667383
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:18:41.724833
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    import os

    # If we don't have locale in PATH, then we get a RuntimeWarning.

    am = mock.Mock()
    am.get_bin_path.return_value = None
    try:
        get_best_parsable_locale(am)
    except RuntimeWarning:
        pass
    else:
        assert False, "We expected a RuntimeWarning"

    # We can send preferences and get back one of the preferences.

    am = mock.Mock()
    am.get_bin_path.return_value = '/usr/bin/locale'
    am.run_command.return_value = (0, 'C\nC.UTF-8\nen_US.UTF-8', '')

# Generated at 2022-06-12 23:18:51.971933
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common._json_compat import json
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestAnsibleModule(object):
        def __init__(self, locale_out, locale_err, locale_rc, locale_found, locale_path=''):
            self.params = {}
            self.exit_json = self.fail_json = lambda **kwargs: self
            self._debug = self._deprecations = self._socket_path = None
            self._ansible_syslog_facility = self._ansible_verbosity = self._ansible_no_log = self._ansible_debug = None

# Generated at 2022-06-12 23:18:56.497318
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    locale = get_best_parsable_locale(module, raise_on_locale=True)
    assert locale == 'C.utf8' or locale == 'C'

# Generated at 2022-06-12 23:19:05.169565
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # pretend we are using ansible 2.5 and have a module
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    # get_bin_path is a function that _can_ be mocked but doesn't _have_ to be,
    # hence we set the defaults the way we want
    def bin_path(name, opt_dirs=[]):
        return name, ''
    module.get_bin_path = bin_path

    # run_command is a function that _can_ be mocked but doesn't _have_ to be,
    # hence we set the defaults the way we want

# Generated at 2022-06-12 23:19:15.162019
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = FakeAnsibleModule()
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.iso885915', 'en_US'], raise_on_locale=True) == 'en_US'
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'POSIX', 'C'], raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'POSIX', 'C', 'en_US.utf8'], raise_on_locale=True) == 'C'


# Generated at 2022-06-12 23:19:27.389778
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # Test list of available locales
    m.run_command = lambda x, check_rc=True: (0, '\n'.join([
        'C.utf8',
        'en_US.utf8',
        'es_ES.utf8',
        'POSIX',
        'en_US.utf8',
    ]), '')

    assert get_best_parsable_locale(m) == 'en_US.utf8'

    # Test no output from locale
    m.run_command = lambda x, check_rc=True: (0, None, '')

    assert get_best_parsable_locale(m) == 'C'

   

# Generated at 2022-06-12 23:19:38.617410
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
      tests functionality of get_best_parsable_locale, tests all conditions
      to ensure proper outputs are returned
    '''

    # import pytest and AnsibleModule, AnsibleModule required for module_utils
    from ansible.module_utils.basic import AnsibleModule

    import pytest

    # test with no locale found
    text = """Output from locale, without any locale pref"""
    test_module = mock.Mock(spec=AnsibleModule)
    test_module.run_command.return_value = (0, text, '')

    test_return = get_best_parsable_locale(test_module, ['pref_not_there1', 'pref_not_there2'])

    assert test_return == 'C'

    # emulate locale not returning 0 return code

# Generated at 2022-06-12 23:19:45.765246
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    module = AnsibleModule()

    assert get_best_parsable_locale(module) == 'C'

    preferences = None
    assert get_best_parsable_locale(module, preferences) == 'C'

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(module, preferences) == 'C'

# Generated at 2022-06-12 23:19:56.045587
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common import get_platform
    from sys import version_info
    import os

    locale_binary = '/usr/bin/locale'
    if not os.path.exists(locale_binary):
        locale_binary = '/bin/locale'
    platform = get_platform()

    def get_locale(self, **kwargs):
        cmd = kwargs.get('args')
        if cmd == 'args':
            return 0, 'C.utf8\nen_US.utf8\nC\nPOSIX', ''

# Generated at 2022-06-12 23:20:07.159111
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Note that tests are only relevant for POSIX systems supporting locale.
    import platform
    if platform.system() != 'Linux':
        return

    # Importing AnsibleModule would likely result in a failure on Windows.
    from ansible.module_utils.basic import AnsibleModule
    from distutils.version import StrictVersion

    def get_locale(locale='C', update_locale=False):
        from ansible.module_utils.basic import AnsibleModule
        from ansible.module_utils.facts.system.locale import get_best_parsable_locale

        class FakeModule(AnsibleModule):

            def __init__(self, locale, update_locale=False):
                AnsibleModule.__init__(self, '', '', False, False, False)
                self.base_dir = '.'

# Generated at 2022-06-12 23:20:23.443773
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Since we're mocking module, we need to make sure that its attributes get initialized
    module = MockModule()
    locale = MockBinPath()

    # Case 1: if rc is 0, it should return the first available locale in preferences
    locale.run_command.return_value = (0, 'ja_JP.utf8\nC.utf8\nen_US.utf8\nC\nPOSIX', '')
    assert get_best_parsable_locale(module, ['en_US.utf8', 'C.utf8', 'POSIX']) == 'en_US.utf8'

    # Case 2: if rc is not 0, it should raise an exception
    locale.run_command.return_value = (1, '', '')
    with pytest.raises(RuntimeWarning):
        get_best_pars

# Generated at 2022-06-12 23:20:34.481920
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    def _run(module_output, exp_found=None, exp_pref=None):
        class Module:
            def __init__(self, output):
                self._output = output

            def get_bin_path(self, prog):
                if prog.startswith('loc'):
                    return prog
                return None

            def run_command(self, args):
                if args == ['locale', '-a']:
                    return 0, self._output, ''
                return 1, '', ''
        module = Module(module_output)

        prefs = ['a', 'b', 'c']
        found = get_best_parsable_locale(module, prefs)
        if exp_found:
            assert found == exp_found
        if exp_pref:
            assert prefs == exp_pref



# Generated at 2022-06-12 23:20:40.305894
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # No exception means success
    get_best_parsable_locale(_get_fake_module(True))

    # These should not raise exception
    get_best_parsable_locale(_get_fake_module(False))
    get_best_parsable_locale(_get_fake_module(False), ['a', 'b'])
    get_best_parsable_locale(_get_fake_module(False), raise_on_locale=True)
    get_best_parsable_locale(_get_fake_module(False), ['a', 'b'], raise_on_locale=True)

    # These should raise exception

# Generated at 2022-06-12 23:20:51.007966
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    from ansible.module_utils.basic import AnsibleModule

    class MockModule(AnsibleModule):
        def get_bin_path(self, bin_name):
            return "locale"

        def run_command(self, list_of_cmd_and_args):
            return 0, '', ''

    class MockModuleNoLocale(AnsibleModule):
        def get_bin_path(self, bin_name):
            return None

        def run_command(self, list_of_cmd_and_args):
            return 0, '', ''


# Generated at 2022-06-12 23:20:58.345368
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

# Generated at 2022-06-12 23:21:09.690680
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    # Test 1
    # Try to get best parsable locale for English
    # The language is supported by the system
    # The function should return the first available locale
    preferences = ['en_US.utf8', 'en_US.utf-8', 'en_US']
    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module, preferences) == 'en_US.utf8'

    # Test 2
    # Try to get best parsable locale for English
    # The language is not supported by the system
    # The function should return the default locale
    preferences = ['en_US.utf8', 'en_US.utf-8', 'en_US']
    module = AnsibleModule(argument_spec={})
    assert get

# Generated at 2022-06-12 23:21:17.633880
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Ensure get_best_parsable_locale() can parse "locale -a" output properly.
    '''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    class AnsibleModuleTest:

        def __init__(self):
            self.params = dict()
            self.exit_json = dict()
            self.fail_json = dict()
            self.exit = dict()
            self.fail = dict()
            self.run_command = [self.run_command]


# Generated at 2022-06-12 23:21:22.695126
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    locale = get_best_parsable_locale(None, preferences=preferences)
    assert locale == 'C.utf8' or locale == 'en_US.utf8' or locale == 'C' or locale == 'POSIX'

# Generated at 2022-06-12 23:21:33.818032
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class Module:
        def __init__(self, name, available_locales, raise_on_locale=False):
            self.name = name
            self.available_locales = available_locales
            self.raise_on_locale = raise_on_locale

        def get_bin_path(self, name, required=False):
            if name == 'locale':
                return True
            else:
                return ''

        def run_command(self, cmd):
            try:
                return 0, self.available_locales, ''
            except RuntimeWarning:
                if self.raise_on_locale:
                    raise

    # The available locales matches the first preference
    available_locales = '''C
de_DE.utf8
C.utf8
de_DE.utf8'''

# Generated at 2022-06-12 23:21:38.584983
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    result = module.get_best_parsable_locale()
    if result == 'C':
        print('Unit test for get_best_parsable_locale: Sucess')
    else:
        print('Unit test for get_best_parsable_locale: Failed')

# Generated at 2022-06-12 23:21:55.553282
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    try:
        from unittest import TestCase
    except ImportError:
        from unittest2 import TestCase

    class TestGetBestParsableLocale(TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_get_best_parsable_locale(self):
            ''' Test the function get_best_parsable_locale '''
            from ansible.module_utils.basic import _get_exception_on_locale_error
            import ansible.module_utils.basic
            # create a test class to test the module
            test_class = type('TestAnsibleModule', (ansible.module_utils.basic.AnsibleModule,), {})

            mod = test_class(argument_spec={})
            mod.run_

# Generated at 2022-06-12 23:22:06.397773
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    import tempfile
    import shutil
    import os
    import sys

    # Create module stub
    class FakeModule(object):
        def __init__(self):
            self.FAIL_JSON = False

        def get_bin_path(self, cmd):
            return get_bin_path(cmd)

        def run_command(self, args):
            return 0, None, None

    module = FakeModule()

    # Create temporary file
    tmpdir = tempfile.mkdtemp()
    test_locales = os.path.join(tmpdir, 'locale')

    # Create some fake locales to test

# Generated at 2022-06-12 23:22:12.774199
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils import basic

    module = AnsibleModule(argument_spec={})
    # setup test of function
    preferences = ['en_CA.utf8', 'en_US.utf8', 'C.utf8', 'POSIX']

    # test if locale is not found in available list
    class FakeModule(basic.AnsibleModule):
        def run_command(self, args, check_rc=False):
            # test no output
            return 0, '', ''
            # test empty
            return 0, '', ''
            # test no match
            return 0, 'foo.utf8\nbar.utf8', ''
            # test match

# Generated at 2022-06-12 23:22:22.475786
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.common.removed as removed
    import ansible.module_utils.basic
    class FakeModule(ansible.module_utils.basic.AnsibleModule):
        def __init__(self):
            self.params = {}
            self.body = ''
            self.args = []
        def get_bin_path(self, arg):
            if arg == 'locale':
                return arg
            else:
                return None
        def run_command(self, arg):
            if arg == ['locale', '-a']:
                return 0, '\n'.join(['C', 'POSIX', 'C.utf8', 'en_US.utf8']), None
            elif arg == ['locale', '-a']:
                return 0, '\n'.join([]), None


# Generated at 2022-06-12 23:22:29.908370
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test the get_best_parsable_locale function.
    '''
    # test default preferences
    assert 'C' == get_best_parsable_locale(module, preferences=None)

    # test non-standard preferences
    preferences = ['A.utf8', 'B.utf8', 'C', 'POSIX']
    assert 'B.utf8' == get_best_parsable_locale(module, preferences=preferences)


# Generated at 2022-06-12 23:22:37.342384
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    import os

    test_sort_true_stdout = [
        "POSIX",
        "C.UTF-8",
        "C.utf8",
        "C",
        "en_US.utf8",
        "en_US.UTF-8",
        "/usr/share/locale/locale.alias"
    ]

    test_sort_false_stdout = [
        "POSIX",
        "C.utf8",
        "en_US.UTF-8",
        "C.UTF-8",
        "en_US.utf8",
        "C",
        "/usr/share/locale/locale.alias"
    ]

    test_sort_no_output = []


# Generated at 2022-06-12 23:22:46.771002
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os

    from ansible.module_utils.basic import AnsibleModule

    path_to_locale = None
    if os.path.exists('/usr/bin/locale'):
        path_to_locale = '/usr/bin/locale'

    # no best possible locale
    module = AnsibleModule(dict())
    best_possible_locale = get_best_parsable_locale(module)
    assert best_possible_locale == 'C'

    # no locale directory
    module = AnsibleModule({'locale_dir': '/does/not/exist'})
    best_possible_locale = get_best_parsable_locale(module)
    assert best_possible_locale == 'C'

    # posix locale available in locale.d directory

# Generated at 2022-06-12 23:22:56.891176
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' function get_best_parsable_locale() returns the first best usable locale in order of preference if found'''
    from ansible.module_utils.basic import AnsibleModule
    import sys

    if sys.version_info >= (3, 0):
        module = AnsibleModule(argument_spec={})
        module.get_bin_path = lambda a: True
        module.run_command = lambda a: (0, 'C.utf8\nen_US.utf8', '')
    else:
        from ansible.module_utils.basic import get_bin_path, run_command

        module = AnsibleModule(argument_spec={})
        module.get_bin_path = get_bin_path
        module.run_command = run_command


# Generated at 2022-06-12 23:23:03.947725
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    cls = AnsibleModule(argument_spec={})
    cls.run_command = lambda *args, **kwargs: (0, "en_US.utf8\nen_US\nC\n", "")
    assert get_best_parsable_locale(cls) == "en_US.utf8"
    cls.run_command = lambda *args, **kwargs: (0, "en_US.utf8\nen_US\nC\n", "")
    assert get_best_parsable_locale(cls, preferences=['en_US']) == "en_US"

# Generated at 2022-06-12 23:23:05.920356
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:23:22.056206
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'C', 'POSIX']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['en_US', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(module, preferences=['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(module, preferences=['POSIX', 'C']) == 'POSIX'

# Generated at 2022-06-12 23:23:29.992667
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from os import environ

    # Prepare mock for ansible module
    environ['ANSIBLE_MODULE_ARGS'] = "{'_ansible_no_log': False, '_ansible_debug': False, '_ansible_check_mode': False, '_ansible_diff': False}"
    module_test = AnsibleModule(argument_spec={})

    # Test get_best_parsable_locale with no locale
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(module_test, preferences) == 'C'

    # Test get_best_parsable_locale with no locale

# Generated at 2022-06-12 23:23:38.968161
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Expect all below tests to pass. Return 1 if they do not'''
    import sys
    import os
    import tempfile
    import subprocess

    class AnsibleModuleMock(object):

        def get_bin_path(self, cmd):
            return cmd

        def run_command(self, cmd):
            out_fd, out_path = tempfile.mkstemp()
            os.close(out_fd)
            err_fd, err_path = tempfile.mkstemp()
            os.close(err_fd)

# Generated at 2022-06-12 23:23:43.819285
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # This test should run only when the locale CLI is not available.
    # Note that this is a unit test, not a functional test, so we don't have
    # a real AnsibleModule object.
    module = object()
    module.get_bin_path = lambda x: None
    module.run_command = lambda x: (0, '', '')

    locale = get_best_parsable_locale(module)

    assert locale == 'C'

# Generated at 2022-06-12 23:23:50.745556
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    import ansible.module_utils.common

    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    try:
        ansible.module_utils.common.get_best_parsable_locale(module=module)
    except RuntimeWarning:
        pass

# Generated at 2022-06-12 23:24:01.434794
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleExitJson
    from ansible.module_utils.six import iteritems
    from ansible.module_utils.six import PY2

    if PY2:
        from mock import patch
        from mock import MagicMock
        from mock import call
        from mock import mock_open

    else:
        from unittest.mock import patch
        from unittest.mock import MagicMock
        from unittest.mock import mock_open
        from unittest.mock import call


# Generated at 2022-06-12 23:24:02.872828
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale('C') == 'C'


# Generated at 2022-06-12 23:24:10.332672
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils.basic
    from ansible.module_utils.six.moves import StringIO

    class FakeModule:
        def __init__(self, values):
            self.values = values
            self.fail_json_called = False
            self.fail_json_params = []
            self.run_command_rc = 0
            self.run_command_out = None
            self.run_command_err = None
            self.run_command_command = None

        def fail_json(self, msg=None, rc=None):
            self.fail_json_called = True
            self.fail_json_params = [msg, rc]

        def run_command(self, command):
            if len(self.values) == 0:
                raise Exception("No more values")

            self.run_command

# Generated at 2022-06-12 23:24:19.330990
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # pylint: disable=missing-docstring
    import os

    class MockModule:
        def __init__(self):
            self.get_bin_path_results = None
            self.run_command_results = None

        def get_bin_path(self, prog):
            return self.get_bin_path_results

        def run_command(self, cmd):
            return self.run_command_results

    def get_locale():
        return os.getenv('LC_ALL', os.getenv('LC_CTYPE', os.getenv('LANG', 'C')))
    current_locale = get_locale()

    # first get one that works with the environment
    module = MockModule()
    module.get_bin_path_results = None

# Generated at 2022-06-12 23:24:29.034176
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # test with no locale tool available
    test_module = lambda *args, **kwargs: (0, 'C.utf8\nen_US.utf8', '')
    assert 'C' == get_best_parsable_locale(test_module)

    # test with missing locale tool
    test_module = lambda *args, **kwargs: (0, '', '')
    assert 'C' == get_best_parsable_locale(test_module)

    # test with locale command missing
    test_module = lambda *args, **kwargs: (1, '', '')
    assert 'C' == get_best_parsable_locale(test_module)

    # test with more than enough available locales

# Generated at 2022-06-12 23:24:46.075107
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic

    test_module = basic.AnsibleModule(
        argument_spec=dict()
    )

    with test_module.mock_command('locale', rc=0, stdout="C\nen_US.utf8\nen_US.iso88591\nen_US\nen_US.utf8\nen_US.iso88591"):
        assert get_best_parsable_locale(test_module, preferences=['en_US.utf8', 'C.utf8']) == 'en_US.utf8'


# Generated at 2022-06-12 23:24:58.036706
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Unit test for function get_best_parsable_locale
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.sys_info import get_platform_subclass

    platform = get_platform_subclass()
    if platform == 'generic':
        module = AnsibleModule(
        )
    elif platform == 'windows':
        module = AnsibleModule(
            argument_spec=dict(
                shell_type=dict(
                    type='str',
                    default='powershell'
                ),
                load_system_host_vars=dict(
                    type='bool',
                    default=False
                )
            )
        )

# Generated at 2022-06-12 23:25:09.849719
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import os
    import stat
    import pwd
    import tempfile
    import textwrap
    import shutil

    from ansible.module_utils._text import to_bytes

    class Environment():
        def __init__(self):
            self.path_backup = None
            self.locale_backup = {}

    class AnsibleModule():
        def __init__(self, path=None, locale_path=None):
            self.tmpdir = tempfile.mkdtemp(prefix='ansible_test_get_best_parsable_locale_')
            self.environment = Environment()
            self.environment.path_backup = os.environ.get('PATH', None)
            if path is not None:
                os.environ['PATH'] = path
            self.environment.locale_back

# Generated at 2022-06-12 23:25:20.944188
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Simulate ansible module class for testing
    class FakeModule(object):
        def get_bin_path(self, name):
            return 'locale'

        def run_command(self, cmd):
            rc = 0
            out = 'C\nC.UTF-8\nen_US.utf8'
            err = ''
            return rc, out, err

    # Test default
    module = FakeModule()
    best = get_best_parsable_locale(module)
    assert best == 'C'

    # Test first preferred
    module = FakeModule()
    best = get_best_parsable_locale(module, ['en_US.utf8'])
    assert best == 'en_US.utf8'

    # Test second preferred
    module = FakeModule()
    best = get_best_p

# Generated at 2022-06-12 23:25:30.502876
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import mox

    # Various values returned by the locale command
    locale_cmd_outputs = (
        ('C', 'C.UTF-8', 'ja_JP', 'ja_JP.utf8'),
        ('C.UTF-8', 'C', 'ja_JP', 'ja_JP.utf8'),
        ('C.UTF-8', 'C', 'ja_JP', 'ja_JP.utf8'),
        ('C', 'C.UTF-8', 'fr_FR.utf8', 'ja_JP.utf8'),
        ('C', 'C.UTF-8', 'fr_FR.utf8', 'ja_JP.utf8'),
    )
    # Values expected based on locale cmd output

# Generated at 2022-06-12 23:25:36.196071
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test get_best_parsable_locale
    '''
    # Set up the mocks
    class MockRunner():
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, args):
            return (self.rc, self.out, self.err)

    class MockModule():
        def __init__(self, runner):
            self.runner = runner

        def run_command(self, args):
            return self.runner.run_command(args)

        def get_bin_path(self, executable, required=False):
            if executable == "locale":
                if self.runner.out:
                    return "locale"
                return None


# Generated at 2022-06-12 23:25:43.831532
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.collections import ImmutableDict
    from units.compat.mock import patch
    from ansible.module_utils.basic import AnsibleModule

    def run_command(cmd):
        cmd.pop(0)
        if cmd == ['locale', '-a']:
            if get_best_parsable_locale.__name__ == 'get_best_parsable_locale':
                return 0, '\n'.join(['C.utf8', 'en_US.utf8', 'C', 'POSIX']), None
            else:
                return 0, 'C.utf8\nen_US.utf8\nC\nPOSIX', None
        else:
            return 255, '', None


# Generated at 2022-06-12 23:25:50.584741
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from tempfile import mkdtemp
    from shutil import rmtree
    import os
    import traceback
    import ansible.constants as C

    def setup_mock_module(tempdir, tmp_path_factory, extra_locale_data=None):
        '''
            Sets up a test environment in the given tempdir
        '''
        tempdir = to_bytes(tempdir, errors='surrogate_or_strict')
        gettext_data = b"""
domain "test" {
        domain_is "test";
        msgid "test"
        msgstr "test"
}
"""

# Generated at 2022-06-12 23:26:00.115373
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def run_command(args):
        if args == ['/bin/locale', '-a']:
            return (0, 'C\nen_US.utf8', '')
        else:
            return (0, '', '')

    module = AnsibleModule(run_command=run_command)

    assert get_best_parsable_locale(module) == 'en_US.utf8'
    assert get_best_parsable_locale(module, ['en_US.utf8', 'en_US.utf-8']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, ['en_US.utf-8', 'en_US.utf8']) == 'en_US.utf8'

# Generated at 2022-06-12 23:26:08.816667
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest

    class FakeModule(object):
        def __init__(self, out, rc=0, err=None):
            self.out = out
            self.rc = rc
            self.err = err

        def get_bin_path(self, tool, required=True):
            return '/usr/bin/locale'

        def run_command(self, args):
            return self.rc, self.out, self.err


# Generated at 2022-06-12 23:26:23.925461
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class MockModule(object):
        def __init__(self):
            self.fail_json = lambda **kwargs: None
            self.run_command = lambda command: (0, 'af_ZA ISO8859-1\naf_ZA.utf8 UTF-8\nen_US ISO8859-1', None)
            self.get_bin_path = lambda binary: '/bin/locale'

    preferences = ['en_US.utf8', 'en_US']

    locale = get_best_parsable_locale(MockModule(), preferences=preferences)
    assert locale == 'en_US.utf8'

    preferences = ['en_US.utf8', 'en_US']

    locale = get_best_parsable_locale(MockModule(), preferences=preferences)

# Generated at 2022-06-12 23:26:31.624890
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    res = get_best_parsable_locale(AnsibleModule())
    assert res == 'C'

    # on utf8 machine, return utf8 if it is available (which it is)
    res = get_best_parsable_locale(AnsibleModule(), ['en_US.utf8'])
    assert res == 'en_US.utf8'

# Generated at 2022-06-12 23:26:39.556941
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.network.nxos.nxos import get_best_parsable_locale
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert preferences[0] == get_best_parsable_locale(preferences)

    preferences = ['C.ascii', 'en_US.ascii', 'C', 'POSIX']
    assert preferences[2] == get_best_parsable_locale(preferences)

    preferences = ['C.ascii', 'en_US.ascii', 'C', 'POSIX']
    assert preferences[2] == get_best_parsable_locale(preferences)

# Generated at 2022-06-12 23:26:43.847559
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test get_best_parsable_locale"""
    module = None
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, ['POSIX']) == 'C'
    assert get_best_parsable_locale(module, ['eN_uS.utf8']) == 'C'
    assert get_best_parsable_locale(module, ['POSIX', 'eN_uS.utf8']) == 'C'

# Generated at 2022-06-12 23:26:49.201705
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, None) == 'C'
    assert get_best_parsable_locale(None, ['XYZ']) == 'C'

    class Mock_Module:

        module_name = 'mock_module'

        @staticmethod
        def run_command(*_, **__):
            return 0, 'this_is_a_locale\nXX\nYY\nZZ', ''

        @staticmethod
        def get_bin_path(*_, **__):
            return 'some_binary'
    m = Mock_Module()

    assert get_best_parsable_locale(m, ['this_is_a_locale']) == 'this_is_a_locale'

# Generated at 2022-06-12 23:26:57.785106
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # We are not testing func_get_bin_path since this function is already tested
    # as part of func_run_command.
    # We are not testing func_run_command since this function is already tested
    # as part of module_executor.

    # Importing modules here to make the unittest part of ansible-test
    import ansible.module_utils.basic
    import ansible.module_utils.common.process

    class MockModule(ansible.module_utils.basic.AnsibleModule):
        def __init__(self, name=None, **kwargs):
            self.params = kwargs
            self._name = name

        def get_bin_path(self, arg, check_mode=False, required=False, opt_dirs=None):
            return "/bin/" + arg


# Generated at 2022-06-12 23:27:06.785559
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock

    # TEST: run_command returns an error (out, err)
    # TEST: locale -a is not found
    module = mock.MagicMock(name='Module')
    module.run_command = mock.MagicMock(return_value=(1, None, None))
    module.get_bin_path = mock.MagicMock(return_value=None)
    assert get_best_parsable_locale(module) == 'C'

    module = mock.MagicMock(name='Module')
    module.run_command = mock.MagicMock(return_value=(1, None, None))
    module.get_bin_path = mock.MagicMock(return_value='/usr/bin/locale')
    assert get_best_parsable_locale(module) == 'C'

    #