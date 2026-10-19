

# Generated at 2022-06-12 23:17:11.849605
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # TODO: add test code for get_best_parsable_locale
    fake_module = AnsibleModule(argument_spec=dict())
    assert get_best_parsable_locale(fake_module)

# Generated at 2022-06-12 23:17:18.399072
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModuleError

    # fake module object
    class FakeModule:
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.logger = kwargs.get('logger')
            self.warn = lambda x: self.logger.warning(x)

        @property
        def params(self):
            return self._params

        @params.setter
        def params(self, value):
            self._params = value

        def run_command(self, args, check_rc=True):
            if args == ['locale', '-a']:
                return 0, "en_US.utf8\nen_US\nen_US.ISO8859-15",

# Generated at 2022-06-12 23:17:21.032931
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = False
    preferences = ['what', 'does', 'the', 'fox', 'say']
    found = get_best_parsable_locale(module, preferences)
    assert(found == 'C')

# Generated at 2022-06-12 23:17:27.977940
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.facts.system.locale import get_best_parsable_locale

    # Test `-a` return of no locales
    def mock_run_command_no_locale(*args, **kwargs):
        return (0, '', '')

    assert get_best_parsable_locale(None, mock_run_command=mock_run_command_no_locale) == 'C'

    # Test `-a` return of bad locale config
    def mock_run_command_bad_locale(*args, **kwargs):
        return (1, '', 'foo bar')

    assert get_best_parsable_locale(None, mock_run_command=mock_run_command_bad_locale) == 'C'

    # Test `-a` return

# Generated at 2022-06-12 23:17:33.518462
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Test for get_best_parsable_locale()
    """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import shlex_quote
    MOCK_GET_BIN_PATH = 'ansible.module_utils.network.common.get_bin_path'
    MOCK_RUN_COMMAND = 'ansible.module_utils.network.common.run_command'

    # test case 1: default posix, its ascii but always there
    module = AnsibleModule({})
    module.get_bin_path = lambda _: '/usr/bin/locale'
    module.run_command = lambda _: (1, '', '')
    assert get_best_parsable_locale(module) == 'C'



# Generated at 2022-06-12 23:17:41.328460
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())
    assert module._name == 'Test'
    assert module.params == dict()
    assert module.get_bin_path('false') == '/bin/false'
    assert module.run_command('/bin/false') == (1, '', '')

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale.__doc__

# Generated at 2022-06-12 23:17:47.776400
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    def fake_run_command(self, cmd, check_rc=False, close_fds=True):
        if cmd[1] == '-a':
            return (0, '\n'.join(locales), '')
        return (0, '', '')

    module = AnsibleModule(argument_spec={})
    module.run_command = fake_run_command

    # test with more general locale list
    locales = ['C', 'POSIX']
    best_locale = get_best_parsable_locale(module, ['pl_PL.utf8', 'en_US.utf8'])
    assert best_locale == 'C'

    # test with more general locale list
    locales = ['posix']

# Generated at 2022-06-12 23:17:54.963906
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    module = basic.AnsibleModule(argument_spec=dict(), supports_check_mode=False)
    if module.run_command([module.get_bin_path("locale"), "-a"])[0] == 0:
        # The default value if nothing matches is 'C'
        assert get_best_parsable_locale(module) == 'C'
    else:
        # If running 'locale -a' causes a failure an exception is raised
        import pytest
        pytest.raises(RuntimeWarning, get_best_parsable_locale, module)

# Some of the tests below are commented out because they fail on my standard
# Fedora install. For example, I can't list all locales with "locale -a" and
# I don't have en_US

# Generated at 2022-06-12 23:17:59.952408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    assert get_best_parsable_locale(test_module) == 'C'

# Generated at 2022-06-12 23:18:05.073274
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Use the get_best_parsable_locale function to get the best parsable locale.
    # If it is found, the function returns the locale, else it returns C.
    assert get_best_parsable_locale() in ['C', 'C.utf8', 'en_US.utf8']

# Generated at 2022-06-12 23:18:13.183558
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    module = basic.AnsibleModule(argument_spec={})
    found = get_best_parsable_locale(module)
    assert isinstance(found, str)

# Generated at 2022-06-12 23:18:15.479622
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    pref = ['C.utf8', 'C', 'POSIX']

    assert get_best_parsable_locale(preferences=pref) == 'C'

# Generated at 2022-06-12 23:18:22.078020
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock module class
    class MockModule(object):

        class RunCmd(object):
            returncode = 0
            stdout = 'C.utf8\nen_US.utf8\nen_US.utf-8\n'

        def __init__(self):
            self.run_command_values = {
                'locale': self.RunCmd()
            }
            self.static_binaries = {
                'locale': '/bin/locale'
            }

        def get_bin_path(self, binary, required=False):
            return self.static_binaries[binary]


# Generated at 2022-06-12 23:18:32.885150
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.compat.tests import unittest
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.system.base import BaseFactCollector
    import os

    class MyFactCollector(BaseFactCollector):
        def __init__(self, module):
            super(MyFactCollector, self).__init__(module)

        def populate(self):
            self.facts['system'] = self.module.params['system']

    class MyModule():
        def __init__(self):
            self.run_command_environ_update = os.environ.copy()
            self.params = {'system': 'Linux'}

        def get_bin_path(self, name, required=False, opt_dirs=[]):
            return get_

# Generated at 2022-06-12 23:18:36.768813
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda: None

    assert(get_best_parsable_locale(module, preferences) == 'C')

# Generated at 2022-06-12 23:18:43.233067
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = None
    # With no preferences
    assert get_best_parsable_locale(module) == 'C'
    # With one preference supported
    assert get_best_parsable_locale(module, ['C']) == 'C'
    # With multiple preferences supported
    assert get_best_parsable_locale(module, ['C', 'POSIX']) == 'C'
    # With no preferences supported
    assert get_best_parsable_locale(module, ['fr_FR.utf8', 'fr_FR']) == 'C'

# Generated at 2022-06-12 23:18:52.220314
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.utf8']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.utf-8']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['en_US.utf-8']) == 'C'

# Generated at 2022-06-12 23:19:02.385472
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)


# Generated at 2022-06-12 23:19:12.853881
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as mod_utils  # noqa
    module = mod_utils.AnsibleModule(argument_spec={})

    # Here we just stub out get_bin_path, because we don't actually need a
    # valid path to run it
    def stub_get_bin_path(x):
        return '/usr/bin/locale'

    module.get_bin_path = stub_get_bin_path

    # "C" locale always exists, should always be returned by default
    def stub_run_command(x):
        return 0, "", ""
    module.run_command = stub_run_command
    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    # In the absence of a preferred locale, one that looks generic is returned.
   

# Generated at 2022-06-12 23:19:19.527724
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    module = basic.AnsibleModule(
        argument_spec = dict(
            preferences = dict(type='list', required=False),
            raise_on_locale = dict(type='bool', required=False),
        ),
    )

    assert get_best_parsable_locale(module) in ('C', 'POSIX', 'en_US.utf8', 'C.utf8',)
    assert get_best_parsable_locale(module, ['C', 'POSIX', 'C.utf8']) in ('C', 'POSIX', 'C.utf8',)

# Generated at 2022-06-12 23:19:42.286414
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:19:49.989222
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    parser = ArgumentParser()
    parser.add_argument('--bin-path', action='store', default='/usr/bin/')
    args = parser.parse_args()

    # Create a fake module
    class FakeModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, name):
            return self.bin_path + name

        def run_command(self, command):

            if command[0].endswith('locale'):
                if command[1] == '-a':
                    return (0, 'C\nen_US\nen_US.utf8\n', '')


# Generated at 2022-06-12 23:19:58.655350
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import json
    import sys

    # load the module
    from ansible.module_utils.basic import AnsibleModule

    # Create a fake module
    test_module = AnsibleModule(argument_spec=dict())
    test_module.params = dict()

    test_module.run_command = lambda x, **kwargs: (0, "C\nen_US.utf8\nen_US.UTF-8\n", None)
    assert 'en_US.utf8' == get_best_parsable_locale(test_module, preferences=['en_US.utf8', 'C'])

    test_module.run_command = lambda x, **kwargs: (0, "C\nen_US.utf8\nen_US.UTF-8\n", None)
    assert 'C' == get_best_pars

# Generated at 2022-06-12 23:20:08.903982
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import shlex_quote
    from tempfile import NamedTemporaryFile
    from os import path, environ, remove
    from socket import gethostname
    from time import sleep

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.unicode import get_best_parsable_locale

    # test all the cases and their output in one go

    def set_test_locales(locale_cmds):
        with open(local_file, 'w') as f:
            f.write('#!/bin/bash\n')

# Generated at 2022-06-12 23:20:19.535467
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale_bin = '/usr/bin/locale'
    locale_a_available_out = '''C
POSIX
en_US.utf8
'''.strip().split('\n')
    locale_a_unavailable_out = ''''''.strip().split('\n')
    locale_a_unavailable_err = '''locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
'''
    locale_a_no_output_out = ''''''.strip().split('\n')


# Generated at 2022-06-12 23:20:23.734594
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    choices = ['C.UTF-8', 'en_US.utf8', 'en_US', 'C']
    module = AnsibleModule()
    assert get_best_parsable_locale(module) in choices

# Generated at 2022-06-12 23:20:34.438494
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    if sys.version_info[0] == 2:
        from ansible.module_utils import basic
        from ansible.module_utils import common_koji
        from ansible.module_utils import six

        assert basic.AnsibleModule
        assert common_koji.AnsibleModule
        assert six.StringIO

        # basic.AnsibleModule implements AnsibleModule interface
        module = basic.AnsibleModule(
            argument_spec={},
        )

        # Test case: Locale tool is not available
        module.get_bin_path = lambda x: None
        locale = get_best_parsable_locale(module)
        assert locale == 'C'

    else:
        # AnsibleModule is not importable so just skip the test
        pass

# Generated at 2022-06-12 23:20:40.287899
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    if sys.version_info.major == 2:
        from ansible.module_utils.legacy import _AnsibleModule as AnsibleModule
    else:
        from ansible.module_utils.basic import AnsibleModule
    import tempfile

    module = AnsibleModule(
        argument_spec=dict()
    )

    # Test C locale
    test_locale = get_best_parsable_locale(module)
    assert test_locale == 'C'

    # Test C.utf8 locale
    tmp = tempfile.NamedTemporaryFile()
    tmp_file_name = tmp.name
    tmp.close()

    rc, out, err = module.run_command([module.get_bin_path("locale"), "-a"])
    rc, out, err = module.run_command

# Generated at 2022-06-12 23:20:51.007281
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' test for function get_best_parsable_locale '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    module = AnsibleModule(
        argument_spec=dict(),
        bytes_stdin=False,
        add_file_common_args=False,
        no_log=True,
        stdin_add_newline=False)

    module.run_command = lambda args, **kwargs: ([0, 'C\nC.UTF-8\nPOSIX\nen_US.UTF-8', ''], '', 0)
    assert get_best_parsable_locale(module) == 'C'


# Generated at 2022-06-12 23:20:56.392708
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    # Test: No input parameters
    assert get_best_parsable_locale(module) == 'C'

    # Test: With input parameters
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:21:34.680807
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.six import PY2, StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import cStringIO

    def run_command_mock(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        if args[0] == 'locale' and args[1] == '-a':
            if not PY2:
                return (0, "C.utf8\nen_US.utf8\n", cStringIO())
            else:
                return (0, "C.utf8\nen_US.utf8\n", StringIO())
        else:
            self.fail("Incorrect run_command args: %s" % str(args))

# Generated at 2022-06-12 23:21:36.062828
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) is not None

# Generated at 2022-06-12 23:21:43.985885
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible import module_utils
    import ansible.module_utils.basic

    module_args = dict(
        systemd='yes'
    )

    try:
        module = module_utils.basic.AnsibleModule(
            argument_spec=dict(),
            supports_check_mode=True,
        )
    except ImportError as e:
        raise unittest.SkipTest("missing %s" % e.name)
    else:
        assert module is not None

    module.get_bin_path = lambda *args, **kwargs: '/bin/locale'
    module.run_command = lambda *args, **kwargs: (0, 'C', '')
    assert get_best_parsable_locale(module) == 'C'

    # assert that we are getting first item from the list
    module

# Generated at 2022-06-12 23:21:54.833880
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    #
    # Importing here to avoid circular imports
    #
    from ansible.module_utils.basic import AnsibleModule

    #
    # Here we use "None" to simulate a null return from our test
    #
    def module_run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
        return (0, None, "")

    #
    # more mock
    #
    def module_get_bin_path(self, executable, opt_dirs=[]):
        return None

    #
    # Mock the test module behavior
    #
    class FakeModule(AnsibleModule):
        def __init__(self):
            self.run_command = module_run_command
            self.get_bin_path = module_

# Generated at 2022-06-12 23:22:05.754794
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModule:

        def __init__(self):
            self.module_args = {}

        @staticmethod
        def get_bin_path(*args, **kwargs):
            return '/bin/locale'

        @staticmethod
        def run_command(*args, **kwargs):
            # need to return a tuple
            return 0, 'C.utf8\nen_US.utf8', ''

        @staticmethod
        def fail_json(*args, **kwargs):
            print("Fail json called: {}".format(args))
            raise RuntimeError("Failing json with error {}".format(args))

    # test match first preferred
    module = AnsibleModule()
    preferences = ['en_US.utf8', 'C', 'C.utf8']

# Generated at 2022-06-12 23:22:14.088816
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    import os
    import json


# Generated at 2022-06-12 23:22:24.227795
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class TestModule:
        def __init__(self):
            self.fail_json_called = False
            self.fail_json = self.fail_json_func
            self.run_command_stdout = None
            self.run_command_stderr = None
            self.run_command_rc = 0

        def fail_json_func(self, *args, **kwargs):
            self.fail_json_called = True

        def get_bin_path(self, command):
            return '/usr/bin/locale'

        def run_command(self, command):
            if command == ['/usr/bin/locale', '-a']:
                out = self.run_command_stdout
                err = self.run_command_stderr
                rc = self.run_command_rc

# Generated at 2022-06-12 23:22:31.198637
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # return the default locale C
    assert get_best_parsable_locale(None) == 'C'

    # no preferences specified, return the first preference
    assert get_best_parsable_locale(None, ['pref1', 'pref2']) == 'pref1'

    # return the set preference
    assert get_best_parsable_locale(None, ['not_available', 'pref1'], ['pref1', 'pref2']) == 'pref2'

# Generated at 2022-06-12 23:22:38.104112
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
        },
        supports_check_mode=True
    )

    results = get_best_parsable_locale(module, preferences=['en_US.utf8', 'en.utf8'], raise_on_locale=True)
    assert results == 'en_US.utf8'

    # This test requires locale to be installed on the system where you are running.
    # The locale binary is only available if at least one locale is installed by the administrator
    #
    # results = get_best_parsable_locale(module, preferences=['de_DE.utf8', 'ja.utf8'], raise_on_locale=True)
    # assert results == 'C'



# Generated at 2022-06-12 23:22:41.498245
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Unit test for function get_best_parsable_locale
    '''
    # this function is tested in many places where AnsibleModule is imported
    pass

# Generated at 2022-06-12 23:23:19.093991
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Check if 'get_best_parsable_locale' returns first locale that is
    # available than the one requested as preference
    class Module(object):
        def __init__(self):
            self.run_command = run_command
            self.get_bin_path = get_bin_path
        def fail_json(self, msg):
            raise Exception(msg)


# Generated at 2022-06-12 23:23:23.158283
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'C']) == 'C'

# Test environment variables control of locale behavior

# Generated at 2022-06-12 23:23:30.797698
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        test_get_best_parsable_locale: unit test function for function get_best_parsable_locale
    '''
    import errno

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    class TestLocale(AnsibleModule):

        def __init__(self):
            super(TestLocale, self).__init__()

        def run_command(self, cmd):
            out = b''
            err = b''
            rc = 0

            if cmd == ['locale', '-a']:
                out = to_bytes('C\nen_US.utf8\nen_US.UTF-8\nC.UTF-8\nPOSIX\nC\nC.utf8\n')

# Generated at 2022-06-12 23:23:37.833524
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    ok = False
    try:
        m = AnsibleModule(argument_spec={'foo': {'type': 'int'}})
        get_best_parsable_locale(m, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX'], raise_on_locale=True)
    except RuntimeWarning:
        ok = True

    assert ok

if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:23:45.975799
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    example_available_locales = """
    C
    en_US.utf8
    i18n
    etc...
    """
    # For example_available_locales, the 'C' locale should be returned
    assert get_best_parsable_locale(raise_on_locale=False, out=example_available_locales) == 'C'

    # For example_available_locales (C, en_US.utf8, i18n, ...),
    # the 'en_US.utf8' locale should be returned since it's one of the preferences
    assert get_best_parsable_locale(raise_on_locale=False, out=example_available_locales,
                                    preferences=['en_US.utf8', 'C']) == 'en_US.utf8'

# Generated at 2022-06-12 23:23:58.504138
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as module_utils
    from ansible.modules.system import get_best_parsable_locale
    import sys

    # Calling get_best_parsable_locale() for each of the following
    # should return the same value as the fallback (POSIX) locale
    module_utils.MODULE_COMPLEX_ARGS = { }
    m = module_utils.AnsibleModule(argument_spec=dict())

    # this should be the default, even if not present on the system
    assert get_best_parsable_locale(m, preferences=['a', 'POSIX']) == 'C'

    # try a unicode-capable locale

# Generated at 2022-06-12 23:24:02.227733
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test to check that get_best_parsable_locale function is working as expected.
    Depends on the system setup/configuration and therefore, not able to implement all
    possible scenarios.
    """

    # check with preference as defaults
    best_locale = get_best_parsable_locale()
    assert best_locale == 'C'
    # check with preference as specific locale
    best_locale = get_best_parsable_locale(preferences=['POSIX'])
    assert best_locale == 'POSIX'

# Example AnsibleModule module as a placeholder for future implementation

# Generated at 2022-06-12 23:24:09.883094
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import b
    '''
    Test get_best_parsable_locale for the following cases:
    1. We try to get the best locale and expect C.utf8 output.
    2. We simulate failure to get locale and expect UnicodeDecodeError.
    3. We have 'locale' tool but no output from it and expect RadTimeWarning.
    '''

    # Test case 1

    pref = ['test_locale_1', 'test_locale_2', 'test_locale_3']
    pref_result = 'test_locale_1'

    locale = 'test_locale_1' + '\n' + 'test_locale_2' + '\n' + 'test_locale_3'

# Generated at 2022-06-12 23:24:16.556465
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Test data
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    available = [
        'C.UTF-8',
        'en_US.utf8',
        'POSIX',
        'be_BY.ISO8859-5',
        'be_BY.UTF-8',
        'be_BY@latin'
    ]

    # Test code
    assert get_best_parsable_locale(preferences=preferences, available=available) == 'en_US.utf8'


# Generated at 2022-06-12 23:24:26.895178
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import EnvironmentError

    class TestModule(object):
        def __init__(self, module_args, module_kwargs):
            self.params = module_args
            self.fail_json = module_kwargs['fail_json']

        def get_bin_path(self, tool, required=False):
            return tool

        def run_command(self, cmd):
            # This emulates the output of the "locale -a" command
            out = '''\
C
en_US.utf8
POSIX
'''
            return 0, out, ''

    test = TestModule({'preferences': {'en_US.utf8', 'POSIX'}}, {'ansible_facts': {}})

    test

# Generated at 2022-06-12 23:25:02.319084
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Ensure that a module-like object gets created if needed
    # I'm sure there is a better way to do this
    if not hasattr(get_best_parsable_locale, '__self__'):
        import ansible.module_utils.basic
        get_best_parsable_locale.__self__ = ansible.module_utils.basic.AnsibleModule(
            argument_spec=dict(),
            supports_check_mode=True,
            bypass_checks=True
        )
        get_best_parsable_locale.__self__._ansible_version = (2, 3, 0)

    assert 'C' == get_best_parsable_locale(
        get_best_parsable_locale.__self__,
        preferences=['C'])


# Generated at 2022-06-12 23:25:07.853041
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, ['blah']) == 'C'
    assert get_best_parsable_locale(None, ['blah', 'C.UTF-8']) == 'C.UTF-8'

# Generated at 2022-06-12 23:25:14.222625
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
    )

    # test default preferences
    assert get_best_parsable_locale(module) == 'C'

    # test preferences with known locale
    assert get_best_parsable_locale(module, ['POSIX']) == 'POSIX'

    # test preferences with unknown locale
    assert get_best_parsable_locale(module, ['POSIX', 'WIN32']) == 'POSIX'

    # test preferences with no known locales
    assert get_best_parsable_locale(module, ['WIN32']) == 'C'

    # test no preferences and no locale command
    module.get_bin_path = lambda a: None
    assert get_best_parsable

# Generated at 2022-06-12 23:25:25.866555
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit tests for function get_best_parsable_locale

        :returns: boolean if all tests passed or not
    '''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests.mock import patch


# Generated at 2022-06-12 23:25:36.580276
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class module(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name):
            return '/usr/bin/locale'


# Generated at 2022-06-12 23:25:44.089993
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests import unittest
    try:
        from test.support import EnvironmentVarGuard
    except ImportError:
        from ansible.compat.tests import EnvironmentVarGuard

    class AnsibleLocaleTestCase(unittest.TestCase):

        def setUp(self):
            self.env = EnvironmentVarGuard()

        def test_get_best_parsable_locale(self):
            ''' test_get_best_parsable_locale '''
            test_module = dict(
            )
            test_module_ins = AnsibleModule(argument_spec=test_module)

# Generated at 2022-06-12 23:25:50.747741
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import imp
    import unittest
    import os
    import sys

    # Mock Ansible Module
    import ansible.module_utils.basic

    class MockAnsibleModule(ansible.module_utils.basic.AnsibleModule):
        _module = imp.new_module('ansible_module')
        _module.get_bin_path = ansible.module_utils.basic.AnsibleModule.get_bin_path
        _module.run_command = ansible.module_utils.basic.AnsibleModule.run_command

    module = MockAnsibleModule(argument_spec={})

    # Mock locale available output
    module.run_command = lambda x: (0, 'en_US.utf8\nen_US.utf8\nC.utf8\nPOSIX\nC\n')

# Generated at 2022-06-12 23:26:00.102816
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Test the get_best_parsable_locale() function
    """
    try:
        import ansible.modules.system.locale
        # If ansible is not installed (such as in a pytest venv or tox env)
        # then this import will throw a ImportError and the test will be
        # skipped.
    except ImportError:
        import pytest
        pytest.skip('ansible.modules.system.locale not available.')

    module = ansible.modules.system.locale.AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C']) == 'C'
    assert get

# Generated at 2022-06-12 23:26:08.498952
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    supported_locales = ['C', 'C.utf8', 'POSIX', 'en_US.utf8']
    selected_locale = get_best_parsable_locale(module, supported_locales)
    assert selected_locale == 'C' or selected_locale == 'C.utf8' or selected_locale == 'POSIX', 'Locale returned is not one of supported locales'

    selected_locale = get_best_parsable_locale(module, ['en_US.utf8'])
    assert selected_locale == 'en_US.utf8', 'en_US.utf8 not selected for preference'

# Generated at 2022-06-12 23:26:14.349442
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert('en_US.utf8' == get_best_parsable_locale(None, ['en_US.utf8', 'en_us.utf8']))
    assert('en_US.utf8' == get_best_parsable_locale(None, ['en_us.utf8', 'en_US.utf8']))
    assert('en_US.utf8' == get_best_parsable_locale(None, ['en_us.utf8', 'es_US.utf8', 'en_US.utf8']))
    assert('en_US.utf8' == get_best_parsable_locale(None, ['es_US.utf8', 'en_US.utf8']))