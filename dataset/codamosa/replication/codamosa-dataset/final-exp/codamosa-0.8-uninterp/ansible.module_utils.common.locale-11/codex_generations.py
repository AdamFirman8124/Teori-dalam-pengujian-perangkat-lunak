

# Generated at 2022-06-12 23:17:16.777350
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale({}) == 'C'
    assert get_best_parsable_locale({}, raise_on_locale=True) == 'C'
    assert get_best_parsable_locale({}, preferences=['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale({}, preferences=['POSIX', 'C']) == 'C'
    assert get_best_parsable_locale({}, preferences=['POSIX']) == 'C'
    assert get_best_parsable_locale({}, preferences=['_DUMMY']) == 'C'
    assert get_best_parsable_locale({}, preferences=['_DUMMY', 'C']) == 'C'
    assert get_best_parsable

# Generated at 2022-06-12 23:17:26.096071
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # This requires a complete test environment.
    # Entirely skip this test if we don't have a complete environment.
    import platform

    # Import helper.
    import pytest

    pytest.skip("This test requires a complete test environment.")

    # This is taken from ansible/test/utils/shippable/runme.sh
    os_version = platform.platform()
    # This is taken from ansible/test/units/test_runner.py
    if os_version.startswith("SunOS"):
        pytest.skip("This test does not run on SmartOS due to system tools issue.")

    # Import dependencies.
    # Module only valid for Python 2.
    # This is required here to generate a dummy module object.
    import ansible

# Generated at 2022-06-12 23:17:32.156897
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import argparse
    # These are needed in order to load the AnsibleModule
    def load_ansible_module():
        import ansible.module_utils.basic
        return sys.modules['ansible.module_utils.basic']

    def load_ansible_module_data():
        import ansible.module_utils.basic
        return sys.modules['ansible.module_utils.basic']

    import ansible.module_utils.basic

    parser = argparse.ArgumentParser()
    parser.add_argument('--result', default=None, help='What would you like the test result to be?')
    parser.add_argument('--rc', type=int, default=0, help='What would you like the rc to be?')

# Generated at 2022-06-12 23:17:37.379472
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import json

    class TestModule:
        def __init__(self, out=None, rc=0, err=''):
            self.run_command_cap = out, rc, err

        def get_bin_path(self, bin_name, required=False):
            return bin_name

        def run_command(self, args, check_rc=True, close_fds=True, data=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=False, prompt_regex=None):
            return self.run_command_cap

    out = json.dumps(['C', 'POSIX', 'C.UTF-8', 'en_US.utf8', 'is_IS.utf8'])
    test_module = TestModule(out=out)

    #

# Generated at 2022-06-12 23:17:47.765427
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())

    best_locale = 'C'

    # Get list of available locales
    locale = module.get_bin_path("locale")
    rc, out, err = module.run_command([locale, '-a'])
    available = out.strip().splitlines()

    # Check if one of the preferred locales is available
    for pref in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']:
        if pref in available:
            best_locale = pref
            break

    assert get_best_parsable_locale(module) == best_locale

# Generated at 2022-06-12 23:17:54.701130
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        import unittest2 as unittest
        import ansible.module_utils.basic
    except ImportError:
        import unittest
        import ansible.module_utils.basic
    from ansible.module_utils.common.locales import get_best_parsable_locale

    class TestGetBestParsableLocale(unittest.TestCase):
        '''
            Tests for get_best_parsable_locale
        '''
        def setUp(self):
            self.module = ansible.module_utils.basic.AnsibleModule(
                argument_spec = dict(),
                supports_check_mode = True
            )


# Generated at 2022-06-12 23:18:06.798993
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    # Mock external imports
    module.get_bin_path = lambda x: True

    # First test: locale tool not present
    def mock_run_command(arg, check_rc=False, close_fds=False):
        if 'locale' in arg:
            return 127, "no locale tool", ""
        else:
            return 0, "", ""

    module.run_command = mock_run_command
    assert 'C' == get_best_parsable_locale(module, raise_on_locale=False)

    # Second test: locale tool present, no locales

# Generated at 2022-06-12 23:18:16.424837
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test that get_best_parsable_locale() can get best locale
    '''

    assert get_best_parsable_locale(MockModule(locale_output='en_US.utf8')) == 'en_US.utf8'
    assert get_best_parsable_locale(MockModule(locale_output='en_US.utf8\nPOSIX\nC.utf8')) == 'en_US.utf8'
    assert get_best_parsable_locale(MockModule(returncode=1, locale_output='No output from locale')) == 'C'
    assert get_best_parsable_locale(MockModule(returncode=2, locale_output='Unable to get locale information')) == 'C'



# Generated at 2022-06-12 23:18:20.821727
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    function: get_best_parsable_locale should return 'C' if locale is unable to run
    '''
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    module_mock = AnsibleModule(argument_spec=dict())
    module_mock.run_command = lambda x: (1, "", "")
    assert get_best_parsable_locale(module_mock) == 'C'

    module_mock.run_command = lambda x: (0, "", "")
    assert get_best_parsable_locale(module_mock) == 'C'

    module_mock.run_command = lambda x: (0, "en_US.utf8", "")
    assert get_best_pars

# Generated at 2022-06-12 23:18:31.720883
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Originally, the function had a test_get_best_parsable_locale function
    in the get_best_parsable_locale function itself. This is a library function
    that is not required to have a unit test and the test should not be inside
    the function itself. This is a unit test that verifies that the function
    is working as expected.
    '''
    from ansible.module_utils.common.process import get_bin_path

    module_locale = list()

    class DummyModule(object):
        def __init__(self):
            self.fail_json = self.fail
            self.params = dict()

        def run_command(self, cmd):
            if len(module_locale) > 0:
                return 0, module_locale, ""
            else:
                return

# Generated at 2022-06-12 23:18:46.150673
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class AnsibleModule(object):
        def __init__(self):
            self.module_args = {}

        def get_bin_path(self, tool, opt_dirs=[]):
            paths = dict(
                # locale: path
                locale="locale",
                fail="fail"
            )
            return paths.get(tool)


# Generated at 2022-06-12 23:18:56.446040
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class FakeModule():
        def get_bin_path(self, name):
            if name == 'locale':
                return '/usr/bin/locale'
            else:
                return None

        def run_command(self, command, environ_update=None):
            locale_list = ['fr_FR.UTF-8','en_US.UTF-8','C','POSIX','C.UTF-8','en_US.utf8','en_GB.UTF-8','en_US','en_US.ISO_8859-1','fr_FR','fr_FR.ISO_8859-1','C.ISO_8859-1','POSIX.UTF-8','C.utf8','POSIX.ISO_8859-1','POSIX.utf8']

            return (0, '\n'.join(locale_list), '')

# Generated at 2022-06-12 23:19:05.135395
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
    )
    module.fail_json = lambda **kwargs: None

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, ['foo']) == 'C'
    assert get_best_parsable_locale(module, ['foo'], raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, ['C']) == 'C'

# Generated at 2022-06-12 23:19:15.156850
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # test default behavior (en_US.utf8 and C are not missing on any system known to Ansible devs so this should be true)
    # test_missing_locale_tools_exception is testing for when locale is not available on the system
    found = get_best_parsable_locale(None)
    assert found == 'C', "get_best_parsable_locale() should return 'C' by default: found %s instead" % found

    # test default behavior but with none of the default preferences present
    found = get_best_parsable_locale(None, preferences=['I_do_not_exist'])
    assert found == 'C', "get_best_parsable_locale() should return 'C' by default even if preferences are invalid: found %s instead" % found

    # test locale is available with

# Generated at 2022-06-12 23:19:27.389493
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = _mock_ansible_module()
    locale_available = True
    try:
        locale = module.get_bin_path("locale")
        if not locale:
            raise RuntimeWarning("Could not find 'locale' tool")
    except RuntimeWarning:
        locale_available = False

    if locale_available:
        assert get_best_parsable_locale(module) in ['C.utf8', 'C', 'POSIX']
        assert get_best_parsable_locale(module, ['en_US.utf8']) == 'en_US.utf8'

        module.run_command = _mock_run_command_win
        assert get_best_parsable_locale(module) == 'C'

        module.run_command = _mock_run_command_locale_

# Generated at 2022-06-12 23:19:38.616942
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale_list = [
        'C', 'POSIX', 'C.UTF-8', 'ab_CD.UTF-8', 'en_AB.UTF-8',
        'en_US.ISO-8859-1', 'en_US.UTF-8', 'en_CD.UTF-8', 'en_EF.UTF-8',
        'en_GH.UTF-8', 'en_IJ.UTF-8', 'en_KL.UTF-8', 'en_MN.UTF-8',
        'en_OP.UTF-8'
    ]
    locale_prefs = [
        'C.utf8', 'en_US.utf8', 'C', 'POSIX'
    ]
    got_locale = get_best_parsable_locale(locale_list, locale_prefs)

# Generated at 2022-06-12 23:19:47.905368
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = MockModule()
    module.run_command.return_value = (0, '''C
POSIX
de_DE
de_DE.iso88591
de_DE.iso885915@euro
de_DE@euro
de_LU
de_LU.iso88591
fr_BE
fr_BE.iso88591
fr_BE@euro
fr_CH
fr_FR
fr_FR.iso88591
fr_LU
fr_LU.iso88591''', '')

    # [0]: return value, [1]: stdout, [2]: stderr
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'
    assert get_best_parsable_

# Generated at 2022-06-12 23:19:57.270973
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest

    class TestModule(object):
        def __init__(self, out, rc, err):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, *args, **kwargs):
            return "locale"

        def run_command(self, *args, **kwargs):
            return self.rc, self.out, self.err

    class TestCase(unittest.TestCase):
        def test_get_best_parsable_locale(self):
            # Test case 1
            locale = b"en_US.utf8"
            rc = 0
            out = locale
            err = b""
            mod = TestModule(out, rc, err)

# Generated at 2022-06-12 23:20:02.647449
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    class FakeArgs(object):
        def __init__(self, *args, **kwargs):
            self.options = kwargs
    class FakeModule(object):
        def __init__(self):
            self.exit_json = self.fail_json = lambda c, m: c
            self.params = FakeArgs(check_mode=False, diff=False)
            self.run_command = self.get_bin_path = lambda *a: [0, '', '']

    # Should return 'C' by default
    m = FakeModule()
    assert get_best_parsable_locale(m) == 'C'
    # Should return 'en_US.utf8' if available

# Generated at 2022-06-12 23:20:11.509712
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    preferences = ['en_US.utf8', 'C.utf8', 'C', 'POSIX']
    available = ['C', 'C.utf8', 'de_DE.utf8', 'en_GB.utf8', 'en_US.utf8', 'POSIX']

    # preferred locale exists in available locales
    found = get_best_parsable_locale(None, preferences, available)
    assert(found == 'en_US.utf8')

    # preferred locale does not exist in available locales
    preferences = ['es_ES.utf8', 'fr_CA.utf8']
    found = get_best_parsable_locale(None, preferences, available)
    assert(found == 'C')

    # preferred locale does not exist in available locales and
    # no default found, raise exception

# Generated at 2022-06-12 23:20:26.051036
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == "C"

# Generated at 2022-06-12 23:20:36.601443
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({}, check_invalid_arguments=False)

    # For testing we mock things to force happy path

    # no path to locale binary, so error
    module.get_bin_path = lambda x: None
    assert get_best_parsable_locale(module) == 'C'

    # no locale can be found, so error
    module.get_bin_path = lambda x: x
    module.run_command = lambda x: (1, "", "no good")
    assert get_best_parsable_locale(module) == 'C'

    # no locale can be found, so error
    module.run_command = lambda x: (0, "", "")

# Generated at 2022-06-12 23:20:47.996980
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import ModuleDataLoader

    class AnsibleModule:

        def __init__(self, argv):
            self.params = {}

        def get_bin_path(self, name):
            return 'locale'

        def run_command(self, cmd):
            out = "C\nC.UTF-8\nPOSIX\nen_US.utf8"
            return 0, out, ''

    loader = ModuleDataLoader()
    module = AnsibleModule(loader)

    assert get_best_parsable_locale(module) == "POSIX"

    module = AnsibleModule(loader)

    assert get_best_parsable_locale(module, ['en_US.utf8']) == "en_US.utf8"

# Generated at 2022-06-12 23:20:55.836159
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    get_best_parsable_locale test

    This unit test is only run if the python version under test is
    over version 2.7
    '''
    import sys
    if sys.version_info[0] == 2 and sys.version_info[1] >= 7:
        import unittest

        class TestLinuxSystemLocale(unittest.TestCase):
            '''
            Defines the test class for this module
            '''
            def setUp(self):
                '''
                This method sets up the attribute to be used for the unit
                test of this method
                '''
                self.preferences = ['C', 'POSIX', 'en_US.utf8']
                self.raise_on_locale = False


# Generated at 2022-06-12 23:21:02.078525
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test get_best_parsable_locale"""
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    locale_list = ["C", "POSIX", "en_IN.utf8", "fr_FR.utf8"]
    best_locale = get_best_parsable_locale(locale_list, preferences)
    expected_locale = "C"
    assert best_locale == expected_locale

# Generated at 2022-06-12 23:21:09.596482
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    all_locales = ["C", "POSIX", "en_US.utf8", "C.utf8", "fr_FR.utf8", "fr_FR.UTF-8"]
    preferred_locales = ["C.utf8", "en_US.utf8", "POSIX", "C"]
    assert "C" == get_best_parsable_locale(None, all_locales, preferred_locales)
    assert "C" == get_best_parsable_locale(None, [], preferred_locales)

# Generated at 2022-06-12 23:21:17.578548
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    For testing different scenarios while getting the best parsable locale.
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import AnsibleModule
    import platform
    import sys

    class TestModule(AnsibleModule):

        def __init__(self, args=None, kwargs=None):
            self.params = {}
            self.args = args
            self.kwargs = kwargs
            self.exit_args = None
            self.run_command_called = False
            self.fail_json_called = False
            self.fail_json_args = None

        def get_bin_path(self, binary):
            if binary == "locale":
                return binary
            else:
                return None


# Generated at 2022-06-12 23:21:21.405069
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = AnsibleModule(
        argument_spec=dict()
    )
    output = get_best_parsable_locale(module, preferences=['C', 'C.utf8'])
    assert(output == 'C')

# Generated at 2022-06-12 23:21:30.191581
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # Test: match found in preferred locale list
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'C']) == 'en_US.utf8'

    # Test: match not found in preferred locale list, but found in defaults ('C')
    assert get_best_parsable_locale(module, preferences=['fr_FR.utf8']) == 'C'

    # Test: no preference
    assert get_best_parsable_locale(module) == 'C.utf8'

# Generated at 2022-06-12 23:21:40.495096
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils import basic

    class DummyModule(basic.AnsibleModule):

        def __init__(self):
            pass

        def get_bin_path(self, name, required=False):
            return 'locale'

        def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None):
            stdout = 'C\nen_US.utf8\nC.utf8\nen_CA.utf8\nen_GB.utf8\nen_US.utf8'
            return 0, stdout, ''

    mod = DummyModule()

    # test with no prefs

# Generated at 2022-06-12 23:21:55.506677
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'



# Generated at 2022-06-12 23:22:03.353799
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test fixtures for locale testing:
            best_locale is a dict that references the correct locale for
            each fixture.
    '''
    best_locale = {'fixture_1': 'C',
                   'fixture_3': 'C.utf8'}

    for fixture_name, expected_locale in best_locale.items():
        result = get_best_parsable_locale(fixture_name)
        assert result == expected_locale


# Generated at 2022-06-12 23:22:11.741779
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Function to test get_best_parsable_locale
    :return: None
    '''
    from ansible.modules.system import locale_gen
    import ansible.module_utils.basic
    module_args = dict(
        name='en_US.UTF-8',
        state='present',
        update=True
    )
    # Create an ansible module to mock the locale_gen module
    my_locale_gen = locale_gen.Locale(ansible.module_utils.basic.AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    ))
    assert my_locale_gen.get_best_parsable_locale() is 'C'


if __name__ == '__main__':
    test_get_best_p

# Generated at 2022-06-12 23:22:18.837377
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class TestModule(object):
        def __init__(self, out=None, err=None, rc=0):
            self.out = out
            self.err = err
            self.rc = rc

        def run_command(self, cmd):
            return (self.rc, self.out, self.err)

        def get_bin_path(self, cmd):
            if 'locale' in cmd:
                return '/usr/bin/locale'

    module = TestModule()
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    module.out = None
    module.err = 'No output from locale'
    module.rc = 0
    assert get_best_parsable_locale(module) == 'C'


# Generated at 2022-06-12 23:22:21.606749
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert 'POSIX' == get_best_parsable_locale(None)
    assert 'POSIX' == get_best_parsable_locale(None, ['bad', 'POSIX'])



# Generated at 2022-06-12 23:22:29.012388
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' test cases for function get_best_parsable_locale '''
    import os
    import sys
    # our test module 'module' class
    class TestModule(object):
        ''' Class to mock AnsibleModule class in the ansible module '''

        def __init__(self):
            self.run_command_rc = 0
            self.run_command_output = None
            self.run_command_error = None
            self.run_command_stdout = None
            self.run_command_stderr = None

        def get_bin_path(self, bin_name):
            ''' Return the default binary location based on the 'bin' name '''
            if bin_name == "locale":
                return "/usr/bin/locale"

            return None

        # Return our mock stdout/st

# Generated at 2022-06-12 23:22:36.710813
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    test_module = AnsibleModule(argument_spec=dict())

    assert get_best_parsable_locale(test_module) == 'C'

    # override locale as a list so that we can ensure we get the
    # first match from the list of preferences
    locale_list = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    pref_list = ['POSIX', 'C.utf8', 'C', 'en_US.utf8']

    test_module.get_bin_path = lambda x: True
    test_module.run_command = lambda x: (0, os.linesep.join(locale_list), '')

    assert get_best_parsable_locale(test_module, pref_list) == 'POSIX'


# Generated at 2022-06-12 23:22:40.179409
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})
    assert get_best_parsable_locale(module, raise_on_locale=True) is not None

# Generated at 2022-06-12 23:22:48.012070
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModuleMock:
        def __init__(self):
            self.binary_locale = 'test-bin-locale'

        def get_bin_path(self, command):
            return self.binary_locale

        def run_command(self, command):
            if command[0] == 'test-bin-locale':
                if command[1] == '-a':
                    return 0, 'C.utf8\nen_US.utf8\nC\nPOSIX\n', None
                else:
                    return 0, None, None
            else:
                return 1, None, None

    module = AnsibleModuleMock()
    preferences = ['en_US.utf8', 'C']
    assert get_best_parsable_locale(module, preferences) == 'en_US.utf8'

# Generated at 2022-06-12 23:22:57.982984
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale_list = ['C.UTF-8', 'de_DE.utf8', 'de_DE.UTF-8', 'de_DE.utf-8',
                   'en_US.UTF-8', 'en_US.utf8', 'en_US.UTF-8', 'en_US.utf-8',
                   'C']

    prefs = ['C.UTF-8', 'en_US.utf8', 'C']

    def get_prefs(module, preferences=None, raise_on_locale=False):
        return prefs

    def get_locale(module, preferences=None, raise_on_locale=False):
        return locale_list

    import ansible.module_utils.basic as mod_basic


# Generated at 2022-06-12 23:23:31.691317
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    sys.path.append("/home/lofstedt/ansible/hacking/test/units/module_utils")
    from ansible.module_utils.basic import ModuleData, AnsibleModule
    fake_module = ModuleData()
    fake_module.params = {}
    fake_module.run_command = get_best_parsable_locale.get_best_parsable_locale
    sys.modules['ansible.module_utils.basic'] = fake_module
    assert get_best_parsable_locale(AnsibleModule, ['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 0

# Generated at 2022-06-12 23:23:40.260540
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cStringIO

    test_module = AnsibleModule(
        argument_spec={
            'test_prefix': {'required': True},
        },
        supports_check_mode=True
    )

    # Make a fake locale command
    fake_command_output_1 = '''
C.utf8
POSIX
foo_US
bar_US.utf8
'''
    fake_command_output_2 = '''
POSIX
POSIX
POSIX
POSIX
'''

# Generated at 2022-06-12 23:23:47.625376
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    expected = 'C.utf8'
    actual = get_best_parsable_locale({'run_command': run_command_func, 'get_bin_path': lambda x: 'locale'}, preferences=['C.utf8', 'en.utf8'], raise_on_locale=True)
    assert actual == expected, "Expected %s, got %s." % (expected, actual)

    expected = 'C'
    actual = get_best_parsable_locale({'run_command': run_command_func, 'get_bin_path': lambda x: 'locale'}, raise_on_locale=True)
    assert actual == expected, "Expected %s, got %s." % (expected, actual)

    expected = 'C'

# Generated at 2022-06-12 23:23:59.887890
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.tests.common import AnsibleModule
    from ansible.module_utils.facts import get_file_content

    # 'locale -a' should return these locales
    # The 'C' locale is always availale on every system.
    expected_locales = ["C"]
    # This test runs on a Linux system with 'glibc' or 'glibc-locale'
    # These locales are available on the system.
    expected_locales.extend(get_file_content("system_locales_glibc"))
    # This test runs on a Linux system with 'locales-all'
    expected_locales.extend(get_file_content("system_locales_locales-all"))
    # This test runs on a BSD system with 'lang/locales'
    expected

# Generated at 2022-06-12 23:24:01.587215
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from .. import utils

    module = AnsibleModule(argument_spec={})
    utils.get_best_parsable_locale(module)

# Generated at 2022-06-12 23:24:09.301285
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import Ansiballz
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_text

    class MockModule(object):
        def __init__(self, locale_output, locale_return_code, locale=None):
            # we only use one module in here
            self.params = dict(use_locale='C')
            self.run_command_calls = 0
            self.get_bin_path_calls = 0
            self.locale_output = locale_output
            self.locale_return_code = locale_return_code
            self.locale = locale


# Generated at 2022-06-12 23:24:17.042739
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    locale = AnsibleModule(argument_spec=dict())

    # a given preference
    assert get_best_parsable_locale(locale, ['C']) == 'C'
    assert get_best_parsable_locale(locale, ['POSIX']) == 'C'
    assert get_best_parsable_locale(locale, ['C.utf8', 'POSIX']) == 'C.utf8'

    # a given locale works
    assert get_best_parsable_locale(locale, preferences=None, raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:24:21.767350
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    x = AnsibleModule(
        argument_spec=dict(),
    )
    assert x.get_bin_path("locale") == "locale"
    assert get_best_parsable_locale(x) == "C"

# Generated at 2022-06-12 23:24:30.339159
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Test case for get_best_parsable_locale. Returns True if successful, False otherwise'''

    locale_path = "tests/fixtures/get_best_parsable_locale"
    mock_locale_path = "mock_locale"

    try:
        import shutil
        shutil.move("/usr/bin/locale", mock_locale_path)
    except:
        pass

    try:
        shutil.copyfile(locale_path, "/usr/bin/locale")
        found = get_best_parsable_locale(module)
    except:
        shutil.move(mock_locale_path, "/usr/bin/locale")
        return False


# Generated at 2022-06-12 23:24:41.341242
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Test no preferred or available, get C
    m = AnsibleModule(name='Test')
    r = get_best_parsable_locale(m, preferences=None)
    assert r == 'C'

    # Test preferred available, get preference
    preferred = ['preferred1', 'preferred2']
    available = ['preferred1', 'C']
    m = AnsibleModule(name='Test')
    m.run_command = lambda l: (0, '\n'.join(available), None)
    r = get_best_parsable_locale(m, preferences=preferred)
    assert r == preferred[0]

    # Test preferred not available, get C
    preferred = ['preferred1', 'preferred2']

# Generated at 2022-06-12 23:25:44.364630
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # If locale is not available, returns 'C'
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    assert get_best_parsable_locale(module) == 'C'

    # If locale is available, returns 'C'
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.run_command = lambda cmd, **kwargs: (0, 'C\nC.UTF.8\nC.UTF.8\nen_US.UTF.8', None)
    assert get_best_parsable_locale(module) == 'C'

    # If locale is available and 'en_US.UTF.8' is

# Generated at 2022-06-12 23:25:54.777431
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # import AnsibleModule, but only when we are testing this awesome function
    from ansible.module_utils.basic import AnsibleModule

    my_amod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    # we have not mocked 'locale' in this test, so the following calls
    # of the function should raise an exception for failing to get an
    # executable path for 'locale'
    assert get_best_parsable_locale(my_amod) == 'C'
    assert get_best_parsable_locale(my_amod, raise_on_locale=False) == 'C'
    # now if the caller wants this function to raise an exception,
    # due to 'locale' not available, then the function should do so

# Generated at 2022-06-12 23:26:04.590368
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' Test harness for get_best_parsable_locale '''

    # Mock for AnsibleModule
    class AnsibleModule:
        ''' mock for AnsibleModule '''

        def __init__(self):
            pass

        @staticmethod
        def get_bin_path(_):
            ''' mock for get_bin_path '''
            return "locale"

        @staticmethod
        def run_command(cmd):
            ''' mock for run_command '''

            if cmd == ['locale', '-a']:
                return (0, "", "")

            return (0, "en_US.utf8", "")

    # Create an instance of AnsibleModule
    module = AnsibleModule()

    # Test 1 -- preferences == None

# Generated at 2022-06-12 23:26:12.116472
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    mock_module = AnsibleModule()

    default_locale = get_best_parsable_locale(mock_module)
    assert default_locale == 'C', "Returned locale C"

    # Set up a mocked locale command
    # This test case is for when the locale command is not available in the PATH.
    mock_module.run_command = lambda args, **kwargs: (127, "", "sh: locale: command not found")
    try:
        get_best_parsable_locale(mock_module)
    except RuntimeWarning:
        pass
    else:
        assert False, "Should have thrown exception"

    # Make a locale command available in the PATH and not return any output.

# Generated at 2022-06-12 23:26:21.251026
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule, EnvironmentFailure

    def _get_bin_path(arg):
        paths = dict(C='/usr/bin/locale', en_US='/usr/bin/locale')
        if arg in paths:
            return paths[arg]

    def _run_command(arg):
        if arg == ['/usr/bin/locale', '-a']:
            return (0, 'C\nen_US\nC.utf8\nen_US.utf8', '')
        elif arg == ['/usr/bin/locale']:
            return (0, '', '')


# Generated at 2022-06-12 23:26:32.940767
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    from ansible_collections.notmintest.nottests.compat import unittest

    # basic class to mock out AnsibleModule
    class FakeModule:
        def __init__(self, run_command_output, get_bin_path_value=None):
            self.run_command_output = run_command_output
            self.get_bin_path_value = get_bin_path_value

        def get_bin_path(self, _, required=False):
            return self.get_bin_path_value


# Generated at 2022-06-12 23:26:41.296571
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import get_exception
    test_module = AnsibleModule(argument_spec={})

    # Set up mock ansible module for testing
    class MockModule(object):
        def __init__(self):
            self.run_command_results = []
            self.run_command_exceptions = []
            self.fail_json_results = []
            self.fail_json_exceptions = []

        def get_bin_path(self, arg):
            return "/usr/bin/locale"

        def run_command(self, args):
            if self.run_command_results:
                return self.run_command_results.pop(0)
            else:
                raise self.run_command_exceptions.pop(0)


# Generated at 2022-06-12 23:26:49.326718
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    test_cases = [
        {
            'params': {
                'module': module
            },
            'expected': 'C'
        },
        {
            'params': {
                'module': module,
                'preferences': ['ar_EG']
            },
            'expected': 'C'
        }
    ]

    for test_case in test_cases:
        actual = get_best_parsable_locale(**test_case['params'])
        assert test_case['expected'] == actual, \
            "get_best_parsable_locale: expected: %s, actual: %s" % (test_case['expected'], actual)

# Generated at 2022-06-12 23:26:54.541049
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.local_ansible_module import LocalAnsibleModule
    from ansible.errors import AnsibleError
    import os
    import tempfile
    import shutil

    # Setup
    tempdir = tempfile.mkdtemp()
    test_file = os.path.join(tempdir, 'test.py')

# Generated at 2022-06-12 23:27:03.442134
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # locale command has no output
    try:
        get_best_parsable_locale(module=module)
        assert False
    except RuntimeWarning:
        assert True

    # locale command returns garbage
    module.run_command = lambda x: (0, 'garbage', '')
    try:
        get_best_parsable_locale(module=module)
        assert False
    except RuntimeWarning:
        assert True

    # locale command fails
    module.run_command = lambda x: (1, '', 'locale not found')