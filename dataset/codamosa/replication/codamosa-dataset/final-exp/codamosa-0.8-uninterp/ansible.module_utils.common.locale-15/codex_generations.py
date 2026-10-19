

# Generated at 2022-06-12 23:17:16.211291
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.process import get_bin_path

    class TestModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            kwargs['argument_spec'] = dict(
                i18n=dict(type='str'),
                preferences=dict(type='list'),
            )
            super(TestModule, self).__init__(*args, **kwargs)

        def get_bin_path(self, arg, required=True):
            if arg == 'locale':
                return get_bin_path(arg, True, ['.'], [], required)


# Generated at 2022-06-12 23:17:24.072356
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import AnsibleModule

    def get_bin_path(name):
        return name

    module = AnsibleModule.AnsibleModule(
        argument_spec=dict(
        ),
    )
    module.get_bin_path = get_bin_path

    def run_command(args):
        return 0, 'C\nen_US.utf8\nC.utf8\nPOSIX', ''

    module.run_command = run_command

    # Try passing with no additional information
    locale = get_best_parsable_locale(module)
    assert locale == 'C.utf8'

    # Try passing with a list of preferences that would require the first item
    locale = get_best_parsable_locale(module, ['C', 'POSIX'])
    assert locale == 'C'

    # Try passing

# Generated at 2022-06-12 23:17:31.756968
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={})

    # Test case where all options are available.
    available = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    preferred = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    found = get_best_parsable_locale(m, preferred)
    assert 'POSIX' == found, "Found locale is not POSIX."

    # Test case where preferred locale not available.
    available = ['C.utf8', 'C']
    preferred = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    found = get_best_parsable_locale(m, preferred)

# Generated at 2022-06-12 23:17:42.791154
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def run(preferences, out, err, rc, raise_on_locale):
        m = AnsibleModule(argument_spec={})
        m.run_command = lambda x: (rc, out, err)
        ret = get_best_parsable_locale(m, preferences, raise_on_locale)
        return ret

    # This is the output of Fedora 23's locale -a

# Generated at 2022-06-12 23:17:50.484373
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import _load_params

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    test_params = _load_params()

    locale = get_best_parsable_locale(module)

    if locale is not 'C':
        test_params['msg'] = "Expected locale 'C', but we got '{0}'".format(locale)
        test_params['failed'] = True

    module.exit_json(**test_params)


if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:18:00.971723
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test that the function properly selects the available locale."""

    import sys
    import tempfile
    if sys.version_info[:2] == (2, 6):
        import unittest2 as unittest
    else:
        import unittest


    class FakeAnsibleModule(object):
        def __init__(self, locale_path, locale_output):
            self.locale_path = locale_path
            self.locale_output = locale_output

        def get_bin_path(self, name):
            if name == 'locale':
                return self.locale_path
            else:
                return None

        def run_command(self, cmd):
            assert(cmd[0] == self.locale_path)
            return (0, self.locale_output, '')


# Generated at 2022-06-12 23:18:11.536209
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = AnsibleModule(argument_spec={})
    locale = get_best_parsable_locale(module)
    assert locale in ('C', 'C.utf8')
    locale = get_best_parsable_locale(module, preferences=['de_DE.utf8'])
    assert locale == 'C'
    locale = get_best_parsable_locale(module, preferences=['de_DE.utf8', 'en_US.utf8'])
    assert locale == 'en_US.utf8'

    class MyModule:
        def __init__(self, locale_data):
            self.locale_data = locale_data

        def get_bin_path(self, arg):
            return "echo"


# Generated at 2022-06-12 23:18:19.790285
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.facts import (
        get_file_content,
    )
    from ansible.module_utils.facts.system.locale import (
        get_best_parsable_locale,
    )


# Generated at 2022-06-12 23:18:30.429587
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Test exception is raised if locale binary is not found

    from ansible.module_utils.basic import AnsibleModule

    module_mock = AnsibleModule(argument_spec={})
    module_mock.get_bin_path = lambda filename: None

    try:
        get_best_parsable_locale(module_mock)
        raise AssertionError('Exception not raised')
    except RuntimeWarning:
        pass

    # Test exception is raised if no output is returned

    import tempfile

    devnull = tempfile.TemporaryFile(mode='w+b')

    module_mock.get_bin_path = lambda filename: filename
    module_mock.run_command = lambda args: (0, None, None)


# Generated at 2022-06-12 23:18:38.996371
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # get_best_parsable_locale: TEST 1, simple test
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    assert get_best_parsable_locale(module) == 'C'

    # get_best_parsable_locale: TEST 2, changing preference
    prefs=['C', 'POSIX', 'fr_FR.utf8', 'en_GB.utf8']
    assert get_best_parsable_locale(module, preferences=prefs) == 'C'

    # get_best_parsable_locale: TEST 3, unavailability of locale
    module.run_command = lambda _: (1, '', 'Unable to get locale information')
    assert get_best_p

# Generated at 2022-06-12 23:18:53.807220
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test get_best_parsable_locale.
    '''
    class FakeModule(object):
        '''
        Fake module for testing get_best_parsable_locale.
        '''
        def __init__(self):
            self.run_command_retvals = []
            self.run_command_calls = []

        def run_command(self, args, check_rc=True):
            '''
            Fake run_command method for testing get_best_parsable_locale.
            '''
            self.run_command_calls.append(args)

            retval = self.run_command_retvals.pop(0)

            if len(retval) == 2:
                rc, out = retval
                err = ''
            else:
                rc, out,

# Generated at 2022-06-12 23:19:00.920692
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, ['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['C.UTF-8', 'POSIX']) == 'C'
    # Test case where an exception is raised
    try:
        get_best_parsable_locale(None, ['foo_BAR.UTF-8'], True)
        assert False
    except RuntimeWarning:
        pass

# Generated at 2022-06-12 23:19:07.856425
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # mock module
    class AnsibleModule(object):
        def __init__(self, dummy):
            self.params = dict()

        def get_bin_path(self, item):
            return item

        def run_command(self, args):
            cmd = args[0]
            if cmd == 'locale':
                return 0, [], ''
            else:
                return 0, ['C.utf8', 'en_US.utf8', 'C', 'POSIX'], ''

    # mock module class
    class AnsibleModules(object):
        def __init__(self, dummy):
            self.params = dict()

    # test if function works properly
    module = AnsibleModule('foo')
    assert get_best_parsable_locale(module) == 'C.utf8'

    # test if function

# Generated at 2022-06-12 23:19:16.789574
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    mod_name = 'get_best_parsable_locale'

    # Mock AnsibleModule and its parameters
    module = type('', (object,), {
        'params': {
            'raise_on_locale': False
        },
    })()

    class AnsibleModule():
        def __init__(self, a, b, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None, l=None, m=None, n=None, o=None, p=None, q=None, r=None, s=None, t=None, u=None, v=None, w=None, x=None, y=None, z=None):
            pass

    # Replace AnsibleModule with a mocked instance

# Generated at 2022-06-12 23:19:28.294953
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Check the following scenarios:
    #   - Check that get_best_parsable_locale() prefers C.UTF-8
    #   - Check that get_best_parsable_locale() prefers custom locale
    #     if it is in the list of available locales
    #   - Check that get_best_parsable_locale() prefers C as a default
    #     as it is always available

    module = AnsibleModule(
        argument_spec=dict(),
    )

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['C.UTF-8', 'C']) == 'C.UTF-8'

    # French locale is not normally supported,

# Generated at 2022-06-12 23:19:39.731749
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import tempfile
    import shutil
    from ansible.module_utils.basic import AnsibleModule

    def dummy_run_command(args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None):
        return (0, '', '')
    module = AnsibleModule(run_command=dummy_run_command)
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_i18n_')

# Generated at 2022-06-12 23:19:48.371166
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    fs_encoding = sys.getfilesystemencoding()

    if os.name == 'nt':
        try:
            import win32api

            system_encoding = win32api.GetACP()
        except:
            system_encoding = 'ascii'
        finally:
            del win32api
    else:
        system_encoding = 'ascii'

    # Define test variables

    binary = 'echo'

    arguments = ['Hello']

    if os.name != 'nt':
        preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX', 'fr_FR.utf8', 'LANGUAGE=fr', 'LC_ALL=fr_FR.utf8']

# Generated at 2022-06-12 23:19:57.658080
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock ansible module
    from ansible.module_utils.basic import AnsibleModule
    connection_args = {'ansible_connection': 'local'}
    module = AnsibleModule(argument_spec=dict(),
                           supports_check_mode=True,
                           bypass_checks=False,
                           connection_args=connection_args)
    # Test 1: With no locale binary
    locale = module.get_bin_path("locale")
    module.params['bin_path'] = 'no_bin_path'
    assert module.get_bin_path("locale") == None
    assert get_best_parsable_locale(module) == 'C'

    # Test 2: With locale binary, but no output
    module.params['bin_path'] = locale

# Generated at 2022-06-12 23:20:08.626409
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={},
                           supports_check_mode=False)
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['posix', 'a']) == 'C'
    assert get_best_parsable_locale(module, preferences=['a', 'b', 'posix']) == 'C'
    assert get_best_parsable_locale(module, preferences=['a', 'b', 'c']) == 'C'

    from ansible.module_utils._text import to_bytes
    module._bin_path_cache['locale'] = 'locale'


# Generated at 2022-06-12 23:20:14.442041
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    # Test get_best_parsable_locale with no locale matches
    assert get_best_parsable_locale(module, ['does_not_exists']) == 'C'

    # Test get_best_parsable_locale with no preferences
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:20:27.879475
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    pass

# Generated at 2022-06-12 23:20:37.252781
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    # if not python 3, skip
    if sys.version_info < (3, 0):
        return

    # Add a dummy test module class
    class TestModule():
        def __init__(self):
            self.fail_json = lambda msg: msg

        def get_bin_path(self, name):
            return name

        def run_command(self, cmd):
            if cmd[0] == 'locale':
                return 0, 'C.utf8\nen_US.utf8\n', None
            return 0, '', None

    test_mod = TestModule()
    assert 'C.utf8' == get_best_parsable_locale(test_mod)

    test_mod = TestModule()

# Generated at 2022-06-12 23:20:48.488860
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import ansible
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    if sys.version_info[0] < 3:
        reload(sys)
        sys.setdefaultencoding('utf8')

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    class FakeModule(AnsibleModule):

        def get_bin_path(self, arg, required=False):
            return 'fake_locale'

        def run_command(self, args, check_rc=False):
            if arg == '-a':
                if PY3:
                    return (0, ['C.UTF-8', 'en_US.UTF-8', 'POSIX'], '')

# Generated at 2022-06-12 23:20:56.127106
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import os

    locale_path = os.path.normpath('/tmp/locale')
    locale_file = os.path.normpath('%s/locale' % locale_path)
    locale_cmd = to_bytes('%s -a' % locale_file)

    class TestModule(AnsibleModule):

        def __init__(self, *args, **kwargs):
            if not os.path.exists(locale_path):
                os.makedirs(locale_path)

            self.tmp_dir = locale_path
            self.tmp_path = locale_file
            self.bin_path = locale_path

            kwargs['argument_spec'] = {}
           

# Generated at 2022-06-12 23:21:06.933940
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    module = AnsibleModule(argument_spec=dict())

    r = get_best_parsable_locale(module)
    assert 'C' == r

    r = get_best_parsable_locale(module, raise_on_locale=True)
    assert 'C' == r  # still the same no matter how we ask

    # swap out get_bin_path so the tool isn't available
    def __mock_get_bin_path(name, required=False):
        return None
    module.get_bin_path = __mock_get_bin_path
    r = get_best_parsable_locale(module)
   

# Generated at 2022-06-12 23:21:15.870832
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils._text import to_bytes
    from ansible.modules.system import locale_gen
    from ansible.module_utils.common.process import get_bin_path

    MODULES_PATH = '/path/to/modules'
    BIN_PATH = ['/usr/bin', '/bin', '/usr/sbin', '/sbin', '/usr/local/bin', '/usr/local/sbin']


# Generated at 2022-06-12 23:21:27.198423
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    import sys
    import pytest

    # Assert function output when input array has values
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    module = basic.AnsibleModule(argument_spec={})
    if sys.platform.startswith('linux'):
        assert get_best_parsable_locale(module, preferences) == 'C'
    elif sys.platform.startswith('sunos'):
        assert get_best_parsable_locale(module, preferences) == 'C'
    elif sys.platform.startswith('aix'):
        assert get_best_parsable_locale(module, preferences) == 'C'

# Generated at 2022-06-12 23:21:37.925435
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Test case 1: if out is empty string
    class module(object):
        def run_command(self, cmd):
            return 0, '', 'test'

        def get_bin_path(self, locale):
            return 1

    assert get_best_parsable_locale(module()) == 'C'

    # Test case 2: If rc is not zero
    class module1(object):
        def run_command(self, cmd):
            return 1, '', 'test'

        def get_bin_path(self, locale):
            return 1

    assert get_best_parsable_locale(module1()) == 'C'

    # Test case 3: If locale is not found
    class module2(object):
        def run_command(self, cmd):
            return 0, '', 'test'


# Generated at 2022-06-12 23:21:48.870485
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock

    # Test - no locale binary on the path
    def _run_command_no_locale():
        return (0, '', '')

    m = mock.Mock()
    m.run_command.side_effect = _run_command_no_locale

    # Test - no output from locale command
    def _run_command_no_output():
        return (0, '', '')

    m = mock.Mock()
    m.run_command.side_effect = _run_command_no_output

    # Test - output from locale command
    def _run_command_output():
        return (0, 'C\nPOSIX', '')

    m = mock.Mock()
    m.run_command.side_effect = _run_command_output

    # Test - error from locale command


# Generated at 2022-06-12 23:21:59.667764
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import os
    import pwd
    import shutil
    import tempfile
    import StringIO

    from ansible.module_utils import basic

    # Create a mock module an place it in the module dictionary
    class DummyModule(object):
        def __init__(self):
            self.params = {}
            self.states = {}
            self.check_mode = False
            self.debug = False
            self.verbosity = 0
            self.no_log = False
            self.fail_json = lambda **kwargs: sys.exit(2)
            self.exit_json = lambda **kwargs: sys.exit(0)
            self.run_command = self.dummy_run_command


# Generated at 2022-06-12 23:22:23.710259
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule, missing_required_lib

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    # Test for locale not present
    locale = get_best_parsable_locale(module)
    assert locale == 'C', u"Default locale should be 'C'"

    # Test for locale present - return the first one
    module.run_command = lambda x: (0, u'en_US.utf8\nah_HA\n', u'')
    locale = get_best_parsable_locale(module)
    assert locale == u'en_US.utf8', u"Default locale should be 'en_US.utf8'"

    # Test for locale not found - return the last one

# Generated at 2022-06-12 23:22:33.554412
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    my_module = ansible.module_utils.basic.AnsibleModule(argument_spec=dict())
    # No locale tool
    my_module._executable_exists_cache['locale'] = False
    assert get_best_parsable_locale(my_module) == 'C', 'No locale tool should return C'

    # No available unicode locale
    my_module._executable_exists_cache['locale'] = True
    my_module.run_command = lambda argv: (0, 'en_US.utf8\nen_US.utf8\nC\nPOSIX\n', None)
    assert get_best_parsable_locale(my_module) == 'C', 'No unicode locale should return C'

    # Available unicode locale

# Generated at 2022-06-12 23:22:44.018316
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock AnsibleModule
    module = AnsibleModule({})
    module.run_command = mock.Mock()
    module.run_command.return_value = (0, 'C\nen_US.utf8\n', '')
    module.get_bin_path = mock.Mock()
    module.get_bin_path.return_value = '/usr/bin/locale'

    # Test preferred order - POSIX
    # This should return 'C'
    preferences = ['POSIX', 'en_US.utf8']
    result = get_best_parsable_locale(module, preferences)
    assert result == 'C'

    # Test preferred order - POSIX
    # This should return 'C'
    preferences = ['POSIX', 'en_US.utf8']
    result = get_best_pars

# Generated at 2022-06-12 23:22:54.596692
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class TestModule(object):
        def __init__(self, locale_available=False, locale_list=None, locale_list_output=None):
            self.run_command_rc = 0
            self.locale_available = locale_available
            self.locale_list = locale_list
            self.locale_list_output = locale_list_output
            self.locale = 'locale'

        def get_bin_path(self, name, required=False):
            return self.locale

        def run_command(self, cmd, environ_update=None, check_rc=False, close_fds=True, executable=None):

            if cmd[0] == 'locale':
                if self.locale_available:
                    return self.run_command_rc, self.locale_list_output,

# Generated at 2022-06-12 23:23:01.747408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' Test the get_best_parsable_locale function '''
    from ansible.module_utils.basic import AnsibleModule

    mod = AnsibleModule({})
    mod.run_command = mock.MagicMock(return_value=(0, "C.UTF-8"))

    best_locale = get_best_parsable_locale(mod)
    assert best_locale == "C.UTF-8"

    mod.run_command = mock.MagicMock(return_value=(1, "Unable to get locale information."))

    best_locale = get_best_parsable_locale(mod)
    assert best_locale == "C"

    mod.run_command = mock.MagicMock(return_value=(0, ""))

    best_locale = get_best_pars

# Generated at 2022-06-12 23:23:10.638578
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    test_module = AnsibleModule(argument_spec={'test': {'type': 'str'}})
    test_module.params['test'] = '/usr/bin/locale -a'

    # check that it finds existing en_US.utf8 locale in system
    assert get_best_parsable_locale(test_module) == 'en_US.utf8'

    # set preferred locale to C.utf8 and check it is returned
    assert get_best_parsable_locale(test_module, preferences=['C.utf8']) == 'C.utf8'

    # set preferred locale to en_AU.utf8 which doesn't exist and verify 'C' locale is returned
    assert get_best_parsable_locale(test_module, preferences=['en_AU.utf8']) == 'C'

# Generated at 2022-06-12 23:23:19.848930
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    assert sys.version_info >= (2, 6, )
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    class TestModule(object):
        def __init__(self):
            self.fail_json_called = False
            self.fail_json_msg = {}
        def get_bin_path(self, command):
            return 'locale'
        def run_command(self, command):
            return 0, "C.utf8\nen_US.utf8\nen_US.utf8-charmap\nC\nPOSIX", None
        def fail_json(self, *args, **kwargs):
            self.fail_json_called = True
            self.fail_json_msg = kwargs


# Generated at 2022-06-12 23:23:24.652773
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    test_module = MockAnsibleModule()
    preferences = ['de_DE.utf8', 'en_US.utf8', 'en_US.UTF-8', 'C']
    get_best_parsable_locale(test_module, preferences)
    assert test_module.call_count > 0


# A small mock class to be used in tests only

# Generated at 2022-06-12 23:23:32.320283
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule
    try:
        locale = AnsibleModule(argument_spec={})
    except Exception as e:
        print("Failed to create AnsibleModule()")
        print(str(e))
        assert False

    try:
        prefs = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
        locale_f = get_best_parsable_locale(locale, preferences=prefs)
    except Exception as e:
        print("Failed to get locale from AnsibleModule()")
        print(str(e))
        assert False

    for pref in prefs:
        if pref in locale_f:
            assert True
            break
    assert False

if __name__ == '__main__':
    test_get_best

# Generated at 2022-06-12 23:23:36.956162
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(preferences=['aaa', 'C']) == 'C'
    assert get_best_parsable_locale(preferences=['aaa', 'bbb']) == 'C'
    assert get_best_parsable_locale(preferences=['ddd', 'eee']) == 'C'



# Generated at 2022-06-12 23:24:01.775587
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    test_locale = [
        'C', 'C.utf8', 'POSIX'
    ]

    assert get_best_parsable_locale(test_locale) == 'C'
    assert get_best_parsable_locale(test_locale, ['C']) == 'C'
    assert get_best_parsable_locale(test_locale, ['POSIX']) == 'POSIX'
    assert get_best_parsable_locale(test_locale, ['en_US.utf8']) == 'C'
    assert get_best_parsable_locale(test_locale, ['C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:24:09.501964
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    This function tests the get_best_parsable_locale function.
    Requires python-mock module.
    '''
    import mock

    # We don't need an AnsibleModulue instance but we need a class
    # In fact, this is an AnsibleModule instance without the run_command method.
    class AnsibleModule_mocked:

        def get_bin_path(self, tool):
            self.rc = 1
            self.out = 'No locale tool'
            self.err = ''
            self.stdout = 'No locale tool'
            return True

    # The mock object for the run_command method

# Generated at 2022-06-12 23:24:18.469951
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' test get_best_parsable_locale '''
    module = AnsibleModule(argument_spec=dict(
        preferences=dict(type='list', default=None),
        raise_on_locale=dict(type='bool', default=False)
    ))
    # test default
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

    # test missing locale
    module.get_bin_path = MagicMock(return_value=None)
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

    # test

# Generated at 2022-06-12 23:24:28.677577
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # stub the module object
    module = type('module', (object,), {
        'get_bin_path': lambda self, path: path,
        'run_command': lambda self, cmd: (0, 'C\nC.UTF-8\nen_US.UTF-8', ''),
    })()

    # set up a temporary locale
    old_locale = module.run_command('locale')[1].strip()

    module.run_command('locale -a > /tmp/locale_test', check_rc=True)
    module.run_command('sed -i "2d" /tmp/locale_test', check_rc=True)

# Generated at 2022-06-12 23:24:39.337537
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    import os

    # TODO: add in mock support for tests here
    locale_bin = get_bin_path("locale")
    if not locale_bin:
        raise Exception("Could not find 'locale' tool")

    class FakeModule:

        def __init__(self):
            self.fail_json = basic.fail_json

        def get_bin_path(self, exe_name):
            return locale_bin


# Generated at 2022-06-12 23:24:47.628647
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:24:59.203954
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert (get_best_parsable_locale(None, ['en_US.utf8', 'C', 'POSIX']) == 'C')
    assert (get_best_parsable_locale(None, ['en_US.utf8', 'POSIX', 'C']) == 'C')
    assert (get_best_parsable_locale(None, ['POSIX', 'C', 'en_US.utf8']) == 'C')


# in most situations, you can use the module_utils directly, like so:
# from ansible.module_utils.basic import AnsibleModule
#
# however, you can also call the constructor directly:
#
#  module = AnsibleModule(
#    argument_spec = dict(
#        state     = dict(default='present', choices=['present', 'absent']

# Generated at 2022-06-12 23:25:11.123014
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(supports_check_mode=False)

    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    locale = get_best_parsable_locale(module, preferences=['POSIX', 'C'])
    assert locale == 'C'

    # Test that we can handle when locale command (at least) is not installed
    class fake_module:
        def __init__(self, out=None, rc=0, err=None):
            self.out = out
            self.rc = rc
            self.err = err
            self.changed = False
            self.fail_json = False

        def get_bin_path(self, cmd, required=False):
            return 'locale'



# Generated at 2022-06-12 23:25:18.112448
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    assert ('en_US.utf8' == get_best_parsable_locale(AnsibleModule(), ['en_US.utf8', 'C']))
    assert ('C' == get_best_parsable_locale(AnsibleModule(), ['en_GB.utf8', 'C']))
    assert ('C' == get_best_parsable_locale(AnsibleModule()))

# Generated at 2022-06-12 23:25:24.532577
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_native

    module = AnsibleModule(name='unused')

    # List of locales available in tests/utils/module_data
    available_locales = ['C.UTF-8', 'C.utf8', 'C', 'POSIX']

    # The below are ordered by preference.  If locale is found in the list of available
    # locales, the test will pass.  If it is not found, the test will fail.
    preferred_locales = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Execute with a preferred_locales list and check for expected result

# Generated at 2022-06-12 23:26:01.211329
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Test 1: Basic test with a success case
    module = AnsibleModule(
        argument_spec={},
    )
    assert get_best_parsable_locale(module=module) == 'C'

    # Test 2: Test for a success case for a particular locale
    module = AnsibleModule(
        argument_spec={},
    )
    assert get_best_parsable_locale(module=module, preferences=['C.utf8', 'en_US.utf8', 'POSIX.utf8']) == 'C.utf8'

    # Test 3: Test for a success case for a particular locale
    module = AnsibleModule(
        argument_spec={},
    )

# Generated at 2022-06-12 23:26:09.735009
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    This function is used to unit test the get_best_parsable_locale function.
    Mainly to make sure that in the case that 'locale' does not exist, and a
    dummy function is passed in, we return 'C' and pass.
    '''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    mod = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        bypass_checks=True,
    )

    # Dummy function
    def run_command(cmd, checkrc=True, cwd=None):
        return (0, 'C\nen_US.utf8', '')

    mod.run_command = run_command
    assert get_best_

# Generated at 2022-06-12 23:26:14.775867
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.common.system import get_platform_subclass
    from ansible.module_utils.basic import AnsibleModule

    # simulate macOS
    if get_platform_subclass().subclass == 'darwin':
        module = AnsibleModule(
            argument_spec=dict(),
            supports_check_mode=False,
        )
        assert get_best_parsable_locale(module) == 'en_US.UTF-8'
    else:
        module = AnsibleModule(
            argument_spec=dict(),
            supports_check_mode=False,
        )
        assert 'C' in get_best_parsable_locale(module)


# Generated at 2022-06-12 23:26:22.947283
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.compat.tests.mock import patch, MagicMock

    # Return various locales depending on the preferences
    def sample_run_command(cmd):
        if 'locale' not in cmd:
            # Unexpected case so raise exception
            raise RuntimeWarning("Unexpected command to be tested")

        known_cmd = ['locale', '-a']
        if cmd == known_cmd:
            return (
                '0',
                'C\nC.utf8\nen_US.utf8\nen_US.UTF-8\nPOSIX\n',
                ''
            )

        # Unexpected command so raise exception
        raise RuntimeWarning("Unexpected command to be tested")


# Generated at 2022-06-12 23:26:34.428024
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = False,
    )

    test_preferences = ['c_C.utf-8', 'c_C.utf-8', 'e_E_N_U_S.utf-8']
    assert 'c_C.utf-8' == get_best_parsable_locale(module, test_preferences)
    assert 'c_C.utf-8' == get_best_parsable_locale(module.get_bin_path("locale"), test_preferences)


# Generated at 2022-06-12 23:26:42.478273
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    def run_command_mock(command, **kwargs):
        """Mock for module.run_command"""

        if command == ['locale', '-a']:
            return (0, "C\nen_US.utf8\n", '')
        else:
            raise RuntimeError("Unhandled command %s" % (command))

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.run_command = run_command_mock

    assert get_best_parsable_locale(module) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['ar_SA.utf8', 'es_ES.utf8'])

# Generated at 2022-06-12 23:26:49.956082
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # one locale that should be there
    preferences = ['C.utf8']
    try:
        locale = get_best_parsable_locale(preferences)
        assert locale in preferences
    except RuntimeWarning as e:
        assert False, "This test should not have raised"

    # two of the locales that should be there
    preferences = ['C.utf8', 'C']
    try:
        locale = get_best_parsable_locale(preferences)
        assert locale in preferences
    except RuntimeWarning as e:
        assert False, "This test should not have raised"

    # locales that should not be there
    preferences = ['en_US.utf8']

# Generated at 2022-06-12 23:26:52.045965
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    mymodule = AnsibleModule(
        argument_spec=dict()
    )
    locale = get_best_parsable_locale(mymodule)
    assert locale == 'C'

# Generated at 2022-06-12 23:26:56.551223
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # Test default preferences
    assert get_best_parsable_locale(module) in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Test user specified preferences
    preferences = ['C.UTF-8', 'C', 'POSIX', 'en_US.UTF-8']
    assert get_best_parsable_locale(module, preferences) in preferences


# Generated at 2022-06-12 23:27:01.782058
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for function get_best_parsable_locale
    '''

    import sys
    import tempfile
    import shutil
    import random
    import string
    from ansible.module_utils.basic import AnsibleModule

    class MockAnsibleModule(AnsibleModule):
        '''
             Mock class for AnsibleModule for use in ansible-test command
        '''

        def __init__(self, **kwargs):
            self.mock_locale = kwargs["mock_locale"]
            self.mock_bin_path = kwargs["mock_bin_path"]
            self.mock_module_run_command = kwargs["mock_module_run_command"]