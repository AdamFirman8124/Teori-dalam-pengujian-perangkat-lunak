

# Generated at 2022-06-12 23:17:16.751201
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    locale = None

    # If it returns locale, then we are good
    try: 
        locale = get_best_parsable_locale(module=None)
    except RuntimeWarning:
        assert False, "RuntimeWarning exception was raised for good"

    assert locale != None, "Locale is None. Expected to return locale"

    # If it raises an exception, then we are good if we set raise_on_locale=False
    try: 
        locale = get_best_parsable_locale(module=None, raise_on_locale=False)
    except RuntimeWarning:
        assert False, "RuntimeWarning exception was raised when it should return None"

    assert locale == None, "Locale is not None. Expected to return None"

# Generated at 2022-06-12 23:17:26.095098
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    test_preferences = ['C.UTF-8', 'en_US.utf8', 'C', 'POSIX']
    test_default_locale = 'C'

    # Running this function should always return something
    assert get_best_parsable_locale(test_module) is not None

    # The test preferences should be returned in order of preference
    assert get_best_parsable_locale(test_module, test_preferences) == test_preferences[0]

    # We should always return the default locale, even when it is not in the list

# Generated at 2022-06-12 23:17:28.209970
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    preferences = ['en_US.utf8', 'en_US.UTF-8', 'C.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(preferences=preferences) in preferences

# Generated at 2022-06-12 23:17:30.050768
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    result = 'C.utf8'
    assert get_best_parsable_locale( None, ['C.utf8', 'POSIX', 'C'] ) == result

# Generated at 2022-06-12 23:17:35.543891
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class FakeModule(object):

        def get_bin_path(self, binary):
            return binary

        def run_command(self, command):
            return (0, 'C\nC.UTF-8\nC.utf8\nen_US.UTF-8\nen_US.utf8', '')

    module = FakeModule()
    assert get_best_parsable_locale(module) == 'en_US.utf8'

# Generated at 2022-06-12 23:17:46.172067
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' unit test for get_best_parsable_locale '''
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    assert module.get_bin_path('locale')

    found = get_best_parsable_locale(module)
    assert found in ['C.utf8', 'C']

    found = get_best_parsable_locale(module, raise_on_locale=True)
    assert found in ['C.utf8', 'C']

    from shutil import which
    old_which = which('locale')

    def fake_which():
        return None
    which('locale').side_effect = fake_which


# Generated at 2022-06-12 23:17:52.100771
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(object):
        def get_bin_path(self, tool):
            return tool

        def run_command(self, cmd):
            out = None
            err = None
            rc = None
            if cmd == "locale":
                out = "C\nen_US.utf8\nC.utf8\n"
                rc = 0
            else:
                out = "unknown command"
                rc = 1
            return rc, out, err

    # Test scenario where the default "C" locale is the best way to parse
    module = TestModule()
    t = AnsibleModule(argument_spec={})
    t.fail_json = lambda **kwargs: None

# Generated at 2022-06-12 23:18:03.330146
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import sys

    class TestGetBestParsableLocale(unittest.TestCase):

        def test_get_best_parsable_locale(self):
            from ansible.module_utils.facts import get_distribution, get_distribution_version, get_system_type
            from ansible.module_utils.facts.system import distro_name_map

            distro = get_distribution()
            distro_version = get_distribution_version()

            include_preferences = True
            if distro == 'OpenWrt':
                include_preferences = False
            if distro == 'Synology DSM':
                include_preferences = False
            if distro == 'SunOS':
                include_preferences = False

# Generated at 2022-06-12 23:18:13.590261
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test get_best_parsable_locale() on a locale that exists and a locale that doesn't
    '''
    import mock
    from ansible.utils.hashing import checksum_s

# Generated at 2022-06-12 23:18:18.036593
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    import os.path
    import os
    import shutil
    import textwrap

    original_locale = os.getenv("LC_ALL")


# Generated at 2022-06-12 23:18:32.885189
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import unittest

    # mock out a module and run some tests
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    TEST_MODULE = 'get_best_parsable_locale'

    # these are the first superlative locales that are found for a particular native language
    # Note that this test data is taken from a Linux laptop, so the actual set of locales may vary
    # on different systems.

# Generated at 2022-06-12 23:18:40.546655
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.facts.system.locale_messages

    from ansible.module_utils.facts.system.locale_messages import get_best_parsable_locale
    from ansible.module_utils.facts.system.locale_messages import get_locale_messages
    import os

    # Test fake_module.
    fake_module = object()
    fake_module.run_command = run_command

    # Test locale command is not available.
    assert get_best_parsable_locale(fake_module, raise_on_locale=False) == 'C'
    assert get_best_parsable_locale(fake_module, raise_on_locale=True) == 'C'

    # Test locale command is available.
    fake_module.get_bin_

# Generated at 2022-06-12 23:18:47.513718
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(
        argument_spec=dict(),
    )

    # Test with preferences which have a valid output
    assert get_best_parsable_locale(m, preferences=['C', 'C.UTF-8']) == 'C.UTF-8'

    # Test with preferences which don't have a valid output
    assert get_best_parsable_locale(m, preferences=['C', 'C.UTF-8', 'abc']) == 'C'

# Generated at 2022-06-12 23:18:58.054986
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Locale 'C' should be returned when get_bin_path can't find locale
    module = MockAnsibleModule()
    assert get_best_parsable_locale(module) == 'C'

    # Locale 'C' should be returned when run_command returns non-zero rc
    module.run_command = Mock(return_value=(1, None, None))
    assert get_best_parsable_locale(module) == 'C'

    # Locale 'C' should be returned when run_command return no lines in out
    module.run_command = Mock(return_value=(0, None, None))
    assert get_best_parsable_locale(module) == 'C'

    # Locale 'C' should be returned when default preferences are not found

# Generated at 2022-06-12 23:19:03.462378
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule, get_exception

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    try:
        parsable_locale = get_best_parsable_locale(module)
    except Exception as e:
        module.fail_json(msg=get_exception())

    assert parsable_locale == 'C', "Expected best parsable locale to be 'C'"

# Generated at 2022-06-12 23:19:08.821199
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(argument_spec={})
    # regex to check that the output is a string of length 1-3
    assert m.check_mode
    assert m.check_mode is True
    assert len(get_best_parsable_locale(m)) in (1, 2, 3)

# Generated at 2022-06-12 23:19:17.365734
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class AnsibleModule_dummy:
        def __init__(self, text):
            self.text = text
        def get_bin_path(self, program):
            return program
        def run_command(self, args):
            if args[0] == 'locale' and args[1] == '-a':
                return 0, self.text, ''
            return 1, '', ''

    # Test best case: all preferred locales in the output
    output = 'C\nen_US.utf8\nC.utf8\nPOSIX\n'
    assert get_best_parsable_locale(AnsibleModule_dummy(output)) == 'C'

    # Test 2nd best case: only one preferred locale in the output

# Generated at 2022-06-12 23:19:29.055014
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    def assert_locale(target_locale, available, preferences=None):
        class MockModule(object):
            def __init__(self, result):
                self.result = result

            def run_command(self, cmd):
                self.cmd = cmd
                return 0, '\n'.join(self.result), ''

            def get_bin_path(self, cmd):
                if cmd != 'locale':
                    return None
                return '/usr/bin/locale'

        mock = MockModule(available)
        assert get_best_parsable_locale(mock, preferences=preferences) == target_locale

    assert_locale('C', [])
    assert_locale('C', ['en_US.utf8'])

# Generated at 2022-06-12 23:19:40.298408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule, ModuleFailException
    import mock

    test_module = AnsibleModule(
        argument_spec=dict(),
    )

    # test if locale is not avilable on the system
    with mock.patch.object(AnsibleModule, 'get_bin_path', return_value=None):
        found_locale = get_best_parsable_locale(test_module)
        assert found_locale == 'C'

    # test if locale is available

# Generated at 2022-06-12 23:19:48.684894
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    import os
    import tempfile
    import shutil

    # Test failure to find locale
    try:
        get_best_parsable_locale({})
    except RuntimeWarning as e:
        assert 'Could not find' in str(e)

    # Test failure to get locale output
    try:
        get_best_parsable_locale({'run_command': lambda x, y: (1, '', '')})
    except RuntimeWarning as e:
        assert 'No output from locale' in str(e)

    # Test failure to get locale output

# Generated at 2022-06-12 23:20:00.777111
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import sys
    import mocks.module_helper as module_helper

    # Create a new module mock that has no locale command
    module = module_helper.get_module_mock()
    if sys.platform.startswith('linux'):
        module.run_command = lambda args, **kwargs: (0, 'C', '')
    else:
        module.run_command = lambda args, **kwargs: (0, 'en_US.utf8', '')

    # Check that we get back 'C'
    assert get_best_parsable_locale(module) == 'C'

    # Create a new module mock that has both locale commands
    module = module_helper.get_module_mock()

# Generated at 2022-06-12 23:20:09.897084
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    output = get_best_parsable_locale(module)
    assert output == 'C'

    output = get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX'])
    assert output == 'C'

    output = get_best_parsable_locale(module, preferences=['C'])
    assert output == 'C'

    output = get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'POSIX'])
    assert output == 'C'

# Generated at 2022-06-12 23:20:21.057064
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    expected = 'C'
    assert get_best_parsable_locale() == expected

    expected = 'C'
    assert get_best_parsable_locale({'get_bin_path': lambda tool: None}, {}, False) == expected

    expected = 'POSIX'
    assert get_best_parsable_locale({'get_bin_path': lambda tool: None, 'run_command': lambda args: (0, 'C\nPOSIX\n', '')}, {}, False) == expected

    expected = 'POSIX'
    assert get_best_parsable_locale({'get_bin_path': lambda tool: None, 'run_command': lambda args: (0, 'C\nPOSIX\n', '')}, ['POSIX', 'C'], False) == expected

# Generated at 2022-06-12 23:20:32.630913
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' Unit test for function get_best_parsable_locale '''
    import ansible.module_utils.basic
    from ansible.module_utils._text import to_bytes
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    # When we have to return the first one, there are no preferences
    assert get_best_parsable_locale(module, preferences=None) == 'C'

    # When we are not passing any preferences, we can't guarantee what we get
    assert get_best_parsable_locale(module, preferences=['en_US']) == 'C'

    # When we pass preferences, we should get the first one that is available
    preferences = ['this_local_does_not_exist', 'C', 'POSIX']
    assert get_best

# Generated at 2022-06-12 23:20:39.610408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Return the best possible locale for parsing output in English
    '''
    preferences = None
    raise_on_locale = False
    class AnsibleModuleMock():
        def get_bin_path(self, *args, **kwargs):
            return 'locale'

        def run_command(self, command):
            class OutMock():
                splitlines = lambda self: ['C', 'POSIX', 'en_us.utf8']
            out = OutMock()
            return 0, out, None

    assert get_best_parsable_locale(AnsibleModuleMock(), preferences, raise_on_locale) == 'en_us.utf8'
    preferences = ['POSIX']

# Generated at 2022-06-12 23:20:50.461270
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping

    class MockModule(AnsibleModule):
        def __init__(self):
            super(MockModule, self).__init__(
                argument_spec=dict(),
                bypass_checks=True,
            )

        def get_bin_path(self, bin_name, required=False):
            if bin_name == "locale":
                return "/usr/bin/locale"
            raise RuntimeWarning("Could not find 'locale' tool")


# Generated at 2022-06-12 23:20:56.591786
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class Params(object):
        pass

    params = Params()
    params.get_bin_path = lambda x: True
    params.run_command = lambda x: (0, "en_US.utf8\nen_US\n")
    params.fail_json = lambda *args, **kwargs: False

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )
    module.params = params

    assert get_best_parsable_locale(module) == 'en_US.utf8'

# Generated at 2022-06-12 23:21:07.535535
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    get_best_parsable_locale: Test case 1
    '''
    import sys
    import tempfile
    import subprocess
    import ansible.module_utils

    assert get_best_parsable_locale(ansible.module_utils.basic.AnsibleModule(argument_spec={})) == 'C'

    '''
    get_best_parsable_locale: Test case 2
    '''
    assert get_best_parsable_locale(ansible.module_utils.basic.AnsibleModule(argument_spec={}), preferences=['en_US.utf8']) == 'en_US.utf8'

    '''
    get_best_parsable_locale: Test case 3
    '''
    assert get_best_parsable_locale

# Generated at 2022-06-12 23:21:16.333166
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test implementation of test_get_best_parsable_locale
        to determine if the best possible locale is being returned
        given the preferences
    '''

    from ansible.module_utils.basic import AnsibleModule

    def run_command(args):
        '''
            Fake for module.run_command method
            returns the arguments passed to method
        '''
        return args


    module = AnsibleModule({}, check_invalid_arguments=False)
    module.run_command = run_command
    module._ansible_no_log = False
    module.get_bin_path = lambda x: x

    class FakeAttrDict(dict):
        '''
            Fake for Attribute class
        '''

# Generated at 2022-06-12 23:21:22.199200
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    fake_module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # check if function returns the correct string
    assert get_best_parsable_locale(fake_module) == 'C'

    # check if function returns the correct string (C is in th

# Generated at 2022-06-12 23:21:33.907734
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Assert function with default
    if get_best_parsable_locale():
        assert True
    else:
        assert False

    # Assert function with specific
    if get_best_parsable_locale(preferences=['C.utf8']):
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:21:39.657464
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # i18n: http://docs.python.org/2/library/gettext.html#module-gettext
    # l10n: http://docs.python.org/2/library/locale.html#module-locale
    import ansible.module_utils.facts.system.base
    result = ansible.module_utils.facts.system.base.get_best_parsable_locale(None, raise_on_locale=True)
    assert result == 'C'

# Generated at 2022-06-12 23:21:45.820090
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    # Using a function that returns a string from the module util and
    # asserting the string is an English message to verify the 'C' locale
    # is used when there is no locale available.
    msg = get_best_parsable_locale(module)
    assert msg == 'C'

# Generated at 2022-06-12 23:21:55.826171
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    def test_locale_cmd(cmd):
        for i, c in enumerate(cmd):
            if c == 'locale':
                # locale command
                if i + 2 < len(cmd):
                    return cmd[i + 1], cmd[(i + 2):]
                else:
                    return None, None
        return None, None

    class MockModule(object):
        def __init__(self, bin_path, run_command, get_bin_path):
            self.bin_path = bin_path
            self.run_command = run_command
            self.get_bin_path = get_bin_path
            self.fail_json = lambda **kw: None
            self.fail_json = lambda **kw: None
            self.warn = lambda **kw: None
            self.deprecate = lambda **kw: None

# Generated at 2022-06-12 23:22:02.213534
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale() == 'C'
    assert get_best_parsable_locale(preferences=['GARBAGE']) == 'C'
    assert get_best_parsable_locale(preferences=['en_US.utf8', 'C', 'POSIX']) == 'en_US.utf8'



# Generated at 2022-06-12 23:22:06.798258
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from tests.unit.module_executor import AnsibleModule
    module = AnsibleModule()
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, ['POSIX']) == 'C'
    assert get_best_parsable_locale(module, ['POSIX', 'C.utf8']) == 'C.utf8'

# Generated at 2022-06-12 23:22:12.558786
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    args = dict(
        module=dict(run_command=dict(return_value=(0, 'C\nC.UTF-8\nPOSIX', ''))),
    )

    module = AnsibleModule(**args)

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['POSIX', 'C.utf8', 'en_US.utf8', 'C']) == 'POSIX'
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C']) == 'C.UTF-8'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8']) == 'C'
    assert get_

# Generated at 2022-06-12 23:22:22.153971
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Test module_utils.get_best_parsable_locale, with and without locale
    locale_path = None
    try:
        locale_path = shutil.which('locale')
    except AttributeError:
        locale_path = __file__
    testmodule = type('AnsibleModule', (object,), dict(
        get_bin_path=lambda s, x: locale_path,
        run_command=lambda s, x: [0, '', '']
    ))

    # Test with no preferred preferences
    assert get_best_parsable_locale(testmodule()) == 'C'
    # Test with empty preferred preferences
    assert get_best_parsable_locale(testmodule(), []) == 'C'
    # Test with preferred preferences
    assert get_best_parsable_locale

# Generated at 2022-06-12 23:22:32.672446
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    fail_when_missing_locale = False

    # no locale cli in path
    try:
        assert get_best_parsable_locale(fail_when_missing_locale) == 'C'
    except:
        assert False

    # invalid locale cli found
    try:
        assert get_best_parsable_locale("blah", fail_when_missing_locale) == 'C'
    except:
        assert False

    # missing locale cli found
    try:
        assert get_best_parsable_locale("/path/to/nowhere/locale", fail_when_missing_locale) == 'C'
    except:
        assert False

    # real but invalid locale cli found

# Generated at 2022-06-12 23:22:38.900585
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    module.get_bin_path = lambda x, required=True: {
        'locale': 'locale',
    }.get(x, None)
    module.run_command = lambda x: {
        ('locale', '-a'): (0, 'C\nen_US.utf8\nen_US.US-ASCII\nC.utf8\nPOSIX\n', ''),
    }.get(tuple(x), (1, '', ''))
    assert get_best_parsable_locale(module, ['C', 'en_US.utf8', 'POSIX']) == 'C'
    assert get_best_parsable_locale

# Generated at 2022-06-12 23:22:55.791201
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.modules.system.setup import get_best_parsable_locale
    assert get_best_parsable_locale('', preferences=None, raise_on_locale=False) == 'C'
    assert get_best_parsable_locale('', preferences=None, raise_on_locale=True) == 'C'

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale('', preferences=preferences, raise_on_locale=False) == 'C'
    assert get_best_parsable_locale('', preferences=preferences, raise_on_locale=True) == 'C'

# Expected test_setup.py output:
# > python -m test.units

# Generated at 2022-06-12 23:23:02.806028
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class MockModule:
        class MockRunCommand(object):
            def __init__(self):
                self.rc = 1
                self.out = ''
                self.err = ''

        def __init__(self):
            self.run_command = self.MockRunCommand()

        @staticmethod
        def get_bin_path(name):
            if name == 'locale':
                return name

    # Make sure 'C' is returned when there is no locale
    module = MockModule()
    assert(get_best_parsable_locale(module) == 'C')

    # Test for a preferred value
    module = MockModule()
    module.run_command.rc = 0
    module.run_command.out = 'C.utf8\nen_US.utf8\nC\nPOSIX'

# Generated at 2022-06-12 23:23:11.792381
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import mock
    import os

    # base class
    class FakeModule():

        def __init__(self, argument_spec={}):
            self.params = {}

        def get_bin_path(self, tool, required=False):
            if tool == 'locale':
                return '/usr/bin/locale'
            if tool == 'localedef':
                return '/usr/bin/localedef'

        def run_command(self, cmd, check_rc=True, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None, encoding=None):
            if cmd == ['/usr/bin/locale', '-a']:
                return 0,

# Generated at 2022-06-12 23:23:20.821712
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def test_fail_on_locale(module, preferences=None, raise_on_locale=False):
        try:
            return get_best_parsable_locale(module, preferences, raise_on_locale)
        except RuntimeWarning:
            return None

    def test_default_locale(module, preferences=None, raise_on_locale=True):
        return get_best_parsable_locale(module, preferences, raise_on_locale)

    module = AnsibleModule(argument_spec={})

    assert test_fail_on_locale(module) is None
    assert test_fail_on_locale(module, raise_on_locale=False) is 'C'


# Generated at 2022-06-12 23:23:23.236735
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec=dict(
            preferences=dict(type='list', default=None)
        )
    )
    assert get_best_parsable_locale(test_module, preferences=['ja_JP.eucJP']) == 'C'

# Generated at 2022-06-12 23:23:31.603444
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec={},
    )

    # don't care about args
    preferences = None
    raise_on_locale = False
    locale = 'C'
    # AnsibleModule.run_command is a mock object that returns the passed args
    module.run_command = lambda args: (0, locale, None)

    # should return the locale if no exception is raised
    assert get_best_parsable_locale(module, preferences, raise_on_locale) == locale

    # should raise an exception that is the result of calling run_command

    # mocked run_command fails to find the executable
    module.run_command = lambda args: (1, None, "Can't find 'locale' tool")

# Generated at 2022-06-12 23:23:40.233310
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common_filters
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils import six

    class FakeModule(object):
        def __init__(self):
            self.FILTER_RE = common_filters.FILTER_RE
            self.params = {}
            self.check_mode = False
            self.no_log = False
            self.connection = "local"
            self.debug = True
            self.deprecation = None

        def fail_json(self, **kwargs):
            raise Exception("fail_json called")


# Generated at 2022-06-12 23:23:41.768298
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale({}, raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:23:51.139212
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # We have no way to really test this since we don't have a real module to test with
    # so we only test for exceptions here
    try:
        get_best_parsable_locale(None, None, raise_on_locale=True)
    except RuntimeWarning:
        pass  # We expect a RuntimeWarning here

    try:
        get_best_parsable_locale(None, preferences=['BAD'], raise_on_locale=True)
    except RuntimeWarning:
        pass  # We expect a RuntimeWarning here


if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:24:01.812715
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    builtins.__dict__['__salt__'] = {
        'cmd.run': lambda cmd: 'C.utf8\nen_US.utf8\nen_US.UTF-8\nde_DE',
        'cmd.run_all': lambda cmd: (0, 'C.utf8\nen_US.utf8\nen_US.UTF-8\nde_DE', ''),
    }
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import get_bin_path, AnsibleModule
    module = AnsibleModule({}, {}, {})
    module.get_bin_path = get_bin_path
    module.run_command = lambda cmd: __s

# Generated at 2022-06-12 23:24:12.085560
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    assert get_best_parsable_locale(AnsibleModule(argument_spec={})) == 'C'

# Generated at 2022-06-12 23:24:21.478574
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module) == 'C'

    module.run_command = lambda cmd: (0, 'foo bar', None)
    assert get_best_parsable_locale(module, ['bar', 'foo']) == 'foo'

    module.run_command = lambda cmd: (0, 'foo bar', 'foo is not available')
    assert get_best_parsable_locale(module, ['bar', 'foo']) == 'bar'

    module.run_command = lambda cmd: (1, None, 'foo is not available')
    assert get_best_parsable_locale(module, ['bar', 'foo']) == 'C'

    module.run

# Generated at 2022-06-12 23:24:30.134064
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def run_locale(cmd):
        if cmd == ['/usr/bin/locale', '-a']:
            return (0, '', '')
        elif cmd == ['/usr/bin/locale', '-k', 'LC_MESSAGES']:
            return (1, '', '')
        elif cmd == ['/usr/bin/locale', '-k', 'LANG']:
            return (0, 'LANG=C.UTF-8', '')
        else:
            print('Invalid command')

    # Mock AnsibleModule

# Generated at 2022-06-12 23:24:41.127855
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.core import module_loader
    from ansible.module_utils.basic import AnsibleModule
    import os

    found = 'C'  # default posix, its ascii but always there

# Generated at 2022-06-12 23:24:42.608697
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:24:48.217284
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModule(object):
        '''
        Fake AnsibleModule class used in unit tests
        '''
        def __init__(self):
            self.fail_json = lambda msg: module.fail_json(**msg)
            self.run_command = lambda cmd: module.run_command(cmd)
            self.get_bin_path = lambda bin: module.get_bin_path(bin)

    class FakeError(object):
        pass

    module = FakeError()

    module.get_bin_path = lambda bin: 'locale'
    module.run_command = lambda cmd: ['locale', '-a']

    prefs = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    badprefs = ['fake', 'nope', 'no']

    # test with

# Generated at 2022-06-12 23:24:59.482424
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    ansible_module = AnsibleModule(
        argument_spec=dict(),
    )

    # If a preference is not in the list of available locales, C is returned
    assert get_best_parsable_locale(module=ansible_module, preferences=["foo_BAR", "foobar"],
                                    raise_on_locale=False) == "C"

    # If available locales is empty, C is returned
    ansible_module._executable_has_no_path = False
    ansible_module.run_command = lambda x, check_rc=True, close_fds=True, executable=None: (0, StringIO(), None)
    assert get_best_parsable_loc

# Generated at 2022-06-12 23:25:04.235372
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    found = get_best_parsable_locale(module)
    assert found == 'C'

# Generated at 2022-06-12 23:25:14.049879
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class MockModule:
        class MockRunCommand:
            class CommandResult:
                def __init__(self, rc, out, err):
                    self.rc = rc
                    self.out = out
                    self.err = err

                def __getitem__(self, key):
                    return self.__dict__[key]

        def __init__(self, available, rc=0, err=''):
            self.rc = rc
            self.out = '\n'.join(available) + '\n'
            self.err = err
            self.result = self.CommandResult(rc, self.out, self.err)

        def run_command(self, param):
            return self.result

        def get_bin_path(self, path):
            return path


# Generated at 2022-06-12 23:25:25.698337
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.utils.shlex import shlex_split
    from ansible.plugins.loader import find_plugin
    import ansible.module_utils.basic
    import ansible.module_utils.common.process
    import os

    # Setup a stub module object
    fake_module = find_plugin('test')
    fake_module.run_command = ansible.module_utils.basic.AnsibleModule.run_command

# Generated at 2022-06-12 23:25:39.723881
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.tests.unit.compat.mock import patch, MagicMock

    # We already test the module_utils._text.to_native, but we patch to_native in the function anyway,
    # so we patch it to native here to avoid errors during test.
    m = MagicMock()
    with patch.dict('sys.modules', {'ansible.module_utils._text': m}):
        m.to_native = to_native

        # now, let's test the function
        from ansible.module_utils.basic import AnsibleModule
        from ansible.module_utils.common.locale import get_best_parsable_locale

        # if locale is not found, return 'C'
        module = AnsibleModule(argument_spec=dict())
        module._executable_prefix_length = 0
       

# Generated at 2022-06-12 23:25:48.198922
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for get_best_parsable_locale.
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests import unittest

    class ActionModule(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')

        def warn(self, *args, **kwargs):
            pass

        @staticmethod
        def get_bin_path(val, *args, **kwargs):
            if val == "locale":
                return val

    class TestAnsibleModule(ActionModule, AnsibleModule):
        pass


# Generated at 2022-06-12 23:25:51.417985
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    assert 'C' == get_best_parsable_locale(module)

# Generated at 2022-06-12 23:26:00.218990
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    # Case 1:
    #   - Default preferences
    #   - Locale available
    #   - No raise
    # Expected output:
    #   - First item in preferences list
    module.get_bin_path = MagicMock(return_value='/usr/bin/locale')
    module.run_command = MagicMock(return_value=(0, 'en_US.utf8\nen_US\n', ''))
    assert get_best_parsable_locale(module, ['en_US.utf8', 'en_US']) == 'en_US.utf8'

    # Case 2:

# Generated at 2022-06-12 23:26:08.932463
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    # Test with the default, first one should work
    best_locale = get_best_parsable_locale(module)
    assert best_locale == 'C', 'Default locale not found, returned %s' % best_locale

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Test with a known good locale
    best_locale = get_best_parsable_locale(module, preferences=['C'])
    assert best_locale == 'C', 'C locale not found, returned %s' % best_locale

    # Test with a bad locale, make sure we get the default
    best_

# Generated at 2022-06-12 23:26:18.884737
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import _AnsibleModule


# Generated at 2022-06-12 23:26:23.146939
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    ansible_module = AnsibleModule(argument_spec={})
    preferences = ['it_IT.utf8', 'C.utf8', 'en_US.utf8', 'C', 'POSIX']
    tested_locale = get_best_parsable_locale(ansible_module, preferences=preferences)
    assert tested_locale == "C"

# Generated at 2022-06-12 23:26:34.585540
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(
        argument_spec = dict(),
    )

    # Test when the locale bin is not found
    m.run_command = lambda args: (0, 'an available locale', '')
    assert m.get_bin_path("locale") is None
    assert get_best_parsable_locale(m) == 'C'

    # Test when the locale bin is found,
    # and no available locale matches any of the preferences.
    m.run_command = lambda args: (0, 'an available locale', '')
    assert m.get_bin_path("locale") is not None
    assert get_best_parsable_locale(m, preferences=['abc']) == 'C'

    # Test when the locale bin is found

# Generated at 2022-06-12 23:26:42.633724
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        This function is a unit test for the function get_best_parsable_locale.

        The purpose of the test is to ensure that correct locale is returned for the host system.
        The test attempts to return the best possible locale for parsing output in English
        useful for scraping output with i18n tools. When this raises an exception
        and the caller wants to continue, it should use the 'C' locale.

        :param module: an AnsibleModule instance
        :param preferences: A list of preferred locales, in order of preference
        :returns: The first matched preferred locale or 'C' which is the default
    '''
    import ansible.module_utils._text as to_native
    import json

    # Create a test class
    class TestClass():
        def __init__(self, my_dict):
            self.params = my

# Generated at 2022-06-12 23:26:48.699478
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    import os
    from ansible.compat.tests.mock import patch, MagicMock

    # Test if we found a locale from the list of preferences
    with tempfile.TemporaryFile('w+') as tf:
        tf.write("C.utf8\nen_US.utf8\nC\n")
        tf.seek(0)

# Generated at 2022-06-12 23:27:00.386999
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock module
    class MockModule:
        def __init__(self):
            self.params = {}
            self.run_command = self._run_command

        def get_bin_path(self, name):
            if name == 'locale':
                return 'locale'
            return None

        def _run_command(self, cmd):
            if cmd == ['locale', '-a']:
                return 0, 'C\nC.utf8\nPOSIX', ''
            return 0, '', ''

    m = MockModule()
    assert get_best_parsable_locale(m) == 'C.utf8'

# Generated at 2022-06-12 23:27:09.004521
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    import ansible.module_utils.basic
    import ansible.module_utils.common.process
    import ansible.module_utils.pycompat24

    class FakeModule(object):
        def __init__(self):
            self.fail_json = lambda: sys.exit(-1)
            self.fail_json.__name__ = 'fail_json'
            self.exit_json = lambda: sys.exit(0)
            self.exit_json.__name__ = 'exit_json'
            self._debug = lambda: sys.exit(-1)
            self._debug.__name__ = '_debug'
