

# Generated at 2022-06-12 23:17:12.782080
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    # This function requires ansible.module_utils.basic.AnsibleModule so we cannot test this function with unit test.
    # Now we just test that the function can be pass through.
    get_best_parsable_locale(module)

# Generated at 2022-06-12 23:17:18.939662
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Creating a fake module
    module = AnsibleModule(
        argument_spec={},
    )
    # Test command not present
    module.get_bin_path = lambda *_: None

    prefs = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    try:
        assert 'C.utf8' == get_best_parsable_locale(module, prefs, raise_on_locale=True)
    except RuntimeWarning:
        assert False
    try:
        assert 'C' == get_best_parsable_locale(module, prefs, raise_on_locale=False)
    except RuntimeWarning:
        assert False

    # Test empty locale command
    def run_command_func(*_): return (0, '', '')
    module.run_

# Generated at 2022-06-12 23:17:20.255912
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:17:29.220231
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils.common.parameters import boolean
    from ansible.module_utils.common.parameters import get_file_contents
    from ansible.module_utils.common.parameters import get_platform_subclass
    from ansible.module_utils.common.parameters import json_decode
    from ansible.module_utils.common.parameters import mk_boolean
    from ansible.module_utils.common.parameters import ntob
    from ansible.module_utils.common.parameters import strip_internal_keys
    from ansible.module_utils.common.process import get_bin_path

# Generated at 2022-06-12 23:17:32.715109
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    x = dict()

    ansible_module = AnsibleModule(argument_spec=x)

    # test on module

# Generated at 2022-06-12 23:17:43.006604
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    from ansible.module_utils.common.sys_info import get_distribution

    distro, distro_release, distro_version = get_distribution()
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )
    if module._name == 'main' and hasattr(module, 'run_command'):
        locale = get_best_parsable_locale(module)

        if distro == 'FreeBSD':
            assert locale == 'C', 'The default locale should be C'
        else:
            assert locale == 'C.utf8', 'The default locale should be C.utf8'


# Generated at 2022-06-12 23:17:48.820917
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, preferences=['POSIX']) == 'C'
    assert get_best_parsable_locale(None, preferences=['POSIX']) != 'C.utf8'
    assert get_best_parsable_locale(None, preferences=['POSIX']) != 'en_US.utf8'
    assert get_best_parsable_locale(None, preferences=['POSIX']) != 'en_US'



# Generated at 2022-06-12 23:17:55.400326
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    # Create test AnsibleModule for testing get_best_parsable_locale
    class TestAnsibleModule(ansible.module_utils.basic.AnsibleModule):
        def get_bin_path(self, path, required=False):
            if path == 'locale':
                return '/usr/bin/locale'

    module = TestAnsibleModule(argument_spec={})
    module.run_command = lambda args, **kwargs: (0, 'C.utf8\nen_US.utf8\nC\nPOSIX\n', '')
    assert module.get_best_parsable_locale(preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C.utf8'
    module

# Generated at 2022-06-12 23:18:00.650133
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit tests for the get_best_parsable_locale function
        :return: A status code 0 for success
    '''

    # TODO: Add unit tests for function get_best_parsable_locale
    #assert True == False
    return 0

# Generated at 2022-06-12 23:18:11.301731
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Mocking of a module object
    class ModuleMock(object):

        def __init__(self):
            self.run_command_rc = 0

# Generated at 2022-06-12 23:18:21.068967
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common_koji
    preferences = ["C.UTF-8", "en_US.UTF-8"]
    user_locale = common_koji.get_best_parsable_locale(None, preferences, raise_on_locale=False)
    assert user_locale == "C.UTF-8"

# Generated at 2022-06-12 23:18:31.952725
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Import inside function so we can get coverage on function
    from ansible.module_utils.basic import AnsibleModule

    tested_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Test basic function works with nothing installed
    assert get_best_parsable_locale(tested_module) == 'C'

    # Test basic function works with no preferences
    assert get_best_parsable_locale(tested_module, preferences=None) == 'C'

    # Test basic function works with preferences but none installed
    assert get_best_parsable_locale(tested_module, preferences=['foo_FOO.bar_BAR']) == 'C'

    # Test function works with little bit of i18n output

# Generated at 2022-06-12 23:18:36.456906
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    # Test default values
    result = get_best_parsable_locale(module)

    assert result == 'C', "Failed to return default values"

    # Test that we handle a RuntimeWarning during execution
    result = get_best_parsable_locale(module, raise_on_locale=True)

# Generated at 2022-06-12 23:18:40.071032
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:18:45.889816
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    best_locale = get_best_parsable_locale(module)
    assert isinstance(best_locale, str)
    best_locale = get_best_parsable_locale(module, preferences=['C', 'POSIX'])
    assert best_locale in ['C', 'POSIX']

# Generated at 2022-06-12 23:18:56.196382
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    sample_locale = u"""
C
C.UTF-8
POSIX
en_US.utf8
ja_JP.utf8
ja_JP.eucjp
ja_JP.ujis
zh_CN.utf8
zh_CN.gb18030
zh_HK.big5hkscs
"""

    sample_locale_at_C = u"""
C
POSIX
""".strip()

    if PY3:
        sample_locale = sample_locale.encode('utf-8')
        sample_locale_at_C = sample_locale_at_C.encode('utf-8')

    # Test with standard locale permissions

# Generated at 2022-06-12 23:19:04.155038
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert 'en_US.utf8' == get_best_parsable_locale(None,
                                                    preferences=['en_US.utf8', 'C.utf8', 'C', 'POSIX'])

    assert 'C.utf8' == get_best_parsable_locale(None,
                                                preferences=['C.utf8', 'C', 'POSIX'])
    assert 'C' == get_best_parsable_locale(None,
                                           preferences=['C', 'POSIX'])
    assert 'POSIX' == get_best_parsable_locale(None,
                                               preferences=['POSIX', 'C', 'en_US.utf8'])

# Generated at 2022-06-12 23:19:14.408637
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    module = AnsibleModule({})

    # Test 1 - locale returns an array with the requested locale
    locale_bin_path = "/usr/bin/locale"
    locale_stdout = b"""
C
C.UTF-8
en_US.utf8
POSIX
    """
    module.get_bin_path = MagicMock(return_value=locale_bin_path)
    module.run_command = MagicMock(return_value=(0, locale_stdout, ""))

    # test that we get the preferred locale 'en_US.utf8'
    preferences = ['en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(module, preferences) == 'en_US.utf8'

    # test that we get the first available locale 'C' if the requested

# Generated at 2022-06-12 23:19:26.560935
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        This test will test the get_best_parsable_locale function.
        :return: None
    '''

    from ansible.module_utils.basic import AnsibleModule

    # Test 1: There is no preference, but the locale tool is there
    am = AnsibleModule(
        argument_spec={},
    )

    # The test will pass if the locale returned is not c or en_US.utf8
    assert get_best_parsable_locale(am) not in ['C', 'en_US.utf8']

    # Test 2: There is no preference, and the locale tool is not there
    am = AnsibleModule(
        argument_spec={},
    )
    am.get_bin_path = lambda x: None

    # The test will pass if the locale returned is C
    assert get

# Generated at 2022-06-12 23:19:33.083730
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == "C"
    assert get_best_parsable_locale(None, ['fr','en_US','de','C','POSIX','arab']) == 'C'
    assert get_best_parsable_locale(None, ['fr','en_US','de','C','POSIX','arab'], True) == 'de'



# Generated at 2022-06-12 23:19:56.403187
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    output = [
        "C",
        "af_ZA",
        "ar_AE",
        "ar_BH",
        "ar_DZ",
        "ar_EG",
        "ar_IN",
        "ar_IQ",
        "ar_JO",
        "ar_KW",
        "ar_LB",
        "ar_LY",
    ]

    # both ascii and utf8 are valid
    output.append("C.ascii")
    output.append("C.utf8")
    output.append("en_US.utf8")


# Generated at 2022-06-12 23:20:07.205628
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os
    import sys

    try:
        locale = os.environ['LC_ALL']
    except KeyError:
        locale = ''

    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x: (0, 'C\nPOSIX\nen_US.utf8\nC.utf8\n' + locale, '')
    module.get_bin_path = lambda x: '/usr/bin/locale'

    # § LC_ALL=del_IN.utf8 ansible --version
    # ansible 2.0.2.0
    #  config file = /home/alice/ansible.cfg
    #  configured module search path = Default w/o overrides
    #  python version = 2.7.

# Generated at 2022-06-12 23:20:11.872135
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module, preferences=['C.UTF-8', 'en_US.UTF-8', 'C']) == 'C.UTF-8'
    assert get_best_parsable_locale(module, preferences=['en_US.UTF-8', 'C', 'POSIX']) == 'en_US.UTF-8'

# Generated at 2022-06-12 23:20:15.080134
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    testmodule = AnsibleModule(argument_spec={'preferences': dict(required=False, type='list')})
    result = get_best_parsable_locale(testmodule, preferences=None)
    assert result == 'C'

# Generated at 2022-06-12 23:20:26.250286
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    found = None
    try:
        import ansible.module_utils.basic
    except ImportError:
        # Use sys.path as Ansible is not installed
        sys.path.append('lib/ansible/module_utils/')
        import basic as ansible_module_utils_basic

    # Set up the module object
    amo = ansible_module_utils_basic.AnsibleModule(
        argument_spec={},
    )
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Execute the function with a good locales_path (from Linux)
    found = get_best_parsable_locale(amo, preferences, False)

    assert found is not None

    # TODO: Add a test for the error case

# Generated at 2022-06-12 23:20:30.611557
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:20:38.742836
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import module_utils
    import tempfile
    import shutil
    import os
    import sys

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Remove the temporary directory
    def cleanup():
        shutil.rmtree(tmpdir)

    # Remove the temporary directory on exit, in case we fail before reaching the
    # cleanup() call.
    atexit = __import__('atexit')
    atexit.register(cleanup)

    # Create a temporary module_utils directory that will be in the import path.
    utilsdir = os.path.join(tmpdir, 'module_utils')
    os.mkdir(utilsdir)

    # Create a dummy AnsibleModule class in a temporary module_utils.basic.py file.

# Generated at 2022-06-12 23:20:49.675908
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.removed import removed_module

    if removed_module("ansible.module_utils.basic"):
        return

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    mocked_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_cases = []
    # test_case[0] is the user's preferred locale list
    # test_case[1] is the list of available locales on the system
    # test_case[2] is the expected result

# Generated at 2022-06-12 23:20:56.847452
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_bytes

    def make_ansible_module(out):
        return AnsibleModule(argument_spec={})

    am = make_ansible_module(to_bytes('C\nen_US.utf8'))
    best = get_best_parsable_locale(am)
    assert best == 'C.utf8'

    am = make_ansible_module(to_bytes('C\nen_US.utf8'))
    best = get_best_parsable_locale(am, preferences=['C', 'en_US.utf8'])
    assert best == 'C' or best == 'en_US.utf8'


# Generated at 2022-06-12 23:21:02.972613
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system.locale import get_best_parsable_locale
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict())

    try:
        assert get_best_parsable_locale(module) == 'C'
    except RuntimeWarning:
        assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:21:40.650927
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    from ansible import constants as C

    # Test the doctest strings
    import doctest
    doctest.testmod(sys.modules[__name__])

    # Test that missing locale return the standard locale
    from ansible.module_utils.basic import AnsibleModule
    m = AnsibleModule(argument_spec={})
    m.get_bin_path = lambda x: None
    assert get_best_parsable_locale(m) == "C"

    # Test that empty run_command output return the standard locale
    m.run_command = lambda x: (0, "", "")
    assert get_best_parsable_locale(m) == "C"

    # Test that non-zero run_command return the standard locale
    m.run_command = lambda x: (1, "", "")

# Generated at 2022-06-12 23:21:46.631968
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:21:48.701615
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:21:59.426458
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    failed = False

# Generated at 2022-06-12 23:22:08.331905
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Make a fake module object that gets passed to function
    import sys
    import json
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Set mock arguments
    if sys.version_info[0] < 3:
        module.params = json.loads(json.dumps(dict(preferences=['C.UTF-8', 'POSIX'])), object_hook=ImmutableDict)
    else:
        module.params = json.loads(json.dumps(dict(preferences=['C.UTF-8', 'POSIX'])), object_hook=ImmutableDict)

    # Mock the module class

# Generated at 2022-06-12 23:22:16.578001
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils import basic
    from ansible.module_utils.local import LocalAnsibleModule

    module_args = dict(
        preferences=dict(type='list', elements='str', default=None),
        raise_on_locale=dict(type='bool', default=False),
    )

    module = LocalAnsibleModule(argument_spec=module_args)

    found = get_best_parsable_locale(module)
    assert found == 'C.utf8' or found == 'C', "Locale returned was %s" % found

    found = get_best_parsable_locale(module, preferences=['de_DE', 'de_DE.utf8', 'C'])

# Generated at 2022-06-12 23:22:20.340750
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ['C']) == 'C'
    # if we pass in a list that doesn't contain 'C', C shouldn't be returned
    assert get_best_parsable_locale(None, ['de']) == 'de'

# Generated at 2022-06-12 23:22:28.241043
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Unit tests for get_best_parsable_locale function'''
    # dummy class to mock ansible.module_utils.basic.AnsibleModule
    class TestAnsibleModule:
        '''AnsibleModule mock class'''
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, path, opt_dirs=None):
            '''mock for get_bin_path'''
            if path == 'locale':
                return '/usr/bin/locale'
            else:
                return None

        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None):
            '''Mock for run_command'''

# Generated at 2022-06-12 23:22:34.312327
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # A list of prefered locales to test
    preferences = ['C.UTF-8', 'POSIX', 'C.UTF-8', 'C']
    assert get_best_parsable_locale(m, preferences, True) == 'C.UTF-8'

    # No locale preference is provided, so 'C' is the default
    assert get_best_parsable_locale(m, None, True) == 'C'

# Generated at 2022-06-12 23:22:44.801914
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    # Default (empty) behavior
    fake_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert 'C' == get_best_parsable_locale(fake_module)

    # Use a non-POSIX locale as the only preference, but fail
    fake_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert 'C' == get_best_parsable_locale(fake_module, ['de_DE.utf8'], raise_on_locale=True)

    # Use a POSIX locale as the only preference, but fail
    fake_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert 'C' == get_best_p

# Generated at 2022-06-12 23:23:21.533019
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import tempfile
    import locale

    preferences = ['en_US.utf8', 'POSIX']
    with tempfile.TemporaryDirectory() as tempdir:
        os.mkdir(os.path.join(tempdir, 'bin'))
        test_locale = os.path.join(tempdir, 'bin/locale')
        with open(test_locale, 'w') as test_locale:
            test_locale.write('#!/bin/sh\nfor arg in "$@"; do\n  case $arg in\n    -a) printf "C\\nen_US.utf8\\nPOSIX\\n";;\n    *) exit 1;;\n  esac\ndone\n')
        os.chmod(test_locale, 0o755)

# Generated at 2022-06-12 23:23:24.867805
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # Not sure how to test on a system that has the 'locale' command and
    # also has the additional locales installed. Maybe use a container.
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:23:32.532147
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import BytesIO

    class test_module(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.exit_json = self.exit_json_no_exit
            self.fail_json = self.exit_json
            self.params = {
                'ANSIBLE_MODULE_ARGS': {}
            }
            self.fail = False
            self.exit_args = False
            self._debug = True

            self.run_command_environ_update = dict()
            self.no_log_values = dict()

            self.aliases = dict()

            self._debug_args = dict()

            self.params = dict()
            self.check_mode = False
            self

# Generated at 2022-06-12 23:23:38.921586
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Unit test for function get_best_parsable_locale
    '''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    # locale -a returns every possible locale
    # we provide a list of preferred locales, in order of preference
    # and we check that we received the first matched preferred locale
    # or 'C' which is the default.
    module = AnsibleModule(argument_spec=ImmutableDict(dict(
        preferences=dict(default=['C.utf8', 'en_US.utf8', 'C', 'POSIX']),
    )))
    preferences = module.params['preferences']

# Generated at 2022-06-12 23:23:46.749425
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    import json
    import os

    def run_command(command, check_rc=True, close_fds=True, data=None, binary_data=False, path_prefix=None, cwd=None,
                    use_unsafe_shell=False, prompt_regex=None):
        env = os.environ.copy()

        # zap locale stuff in env to test locale failure
        for key in ['LC_ALL', 'LC_CTYPE', 'LANG']:
            if key in env:
                del(env[key])

        env['LANGUAGE'] = 'en_US.utf8'
        env['LC_MESSAGES'] = 'en_US.utf8'
        env['LANG'] = 'en_US.utf8'

# Generated at 2022-06-12 23:23:50.525084
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' Testing availability of get_best_parsable_locale '''
    # FIXME: Needs a unit test



# Generated at 2022-06-12 23:23:51.900246
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:23:58.704250
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        AnsibleModule is an abstract class
        and has no method "run_command",
        so we have no chance to run the following tests.
    '''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # a POSIX locale
    preferences = ['C.utf8']
    assert get_best_parsable_locale(module, preferences) == 'C.utf8'


# Generated at 2022-06-12 23:24:05.922632
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        raise Exception("Cannot import Ansible modules")

    in_memory_module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(in_memory_module) == "C"

    if "C" not in in_memory_module.run_command([in_memory_module.get_bin_path('locale'), '-a'])[1]:
        raise Exception("System locale 'C' is not available")

    assert get_best_parsable_locale(in_memory_module, ["C"]) == "C"
    assert get_best_parsable_locale(in_memory_module, ["C", "POSIX"]) == "C"
    assert get_best_

# Generated at 2022-06-12 23:24:12.302408
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    from ansible.module_utils.basic import AnsibleModule
    ansiblemod = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        bypass_checks=True,
    )
    ansiblemod.run_command = mock.MagicMock(return_value=(0, "de_DE.UTF-8\nC.UTF-8\nen_US.UTF-8\n", ""))
    assert 'en_US.UTF-8' == get_best_parsable_locale(ansiblemod)

    ansiblemod.run_command = mock.MagicMock(return_value=(0, "de_DE.UTF-8\nen_US.UTF-8\n", ""))
    assert 'de_DE.UTF-8' == get_best_parsable_loc

# Generated at 2022-06-12 23:24:47.818193
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModule:
        def __init__(self):
            self.fail_json = lambda *args, **kwargs: {'failed': True, 'msg': 'fail_json'}

        def get_bin_path(self, name):
            return 'locale'

        def run_command(self, command):
            if '-a' in command:
                return 0, ['C\nen_US.utf8'], ''
            if 'C.utf8' in command:
                return 0, '', ''
            if 'en_US.utf8' in command:
                return 0, '', ''
            if 'C' in command:
                return 0, '', ''
            if 'POSIX' in command:
                return 0, '', ''


# Generated at 2022-06-12 23:24:54.930813
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for function get_best_parsable_locale
    '''
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
    )
    best_locale_name = get_best_parsable_locale(module)
    assert best_locale_name == 'C'

# Generated at 2022-06-12 23:25:02.396623
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    example_good_locale_output = (u"""C
en_US.utf8
POSIX
""", u"")

    example_bad_locale_output = (u"", u"")

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    class DummyModule(object):

        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, args):
            return (self.rc, self.out, self.err)

        def get_bin_path(self, param):
            if param == 'locale':
                return "/bin/locale"
            return None


# Generated at 2022-06-12 23:25:09.966312
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, preferences=['c']) == 'C'
    assert get_best_parsable_locale(None, preferences=['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'POSIX']) == 'C.utf8'
    assert get_best_parsable_locale(None, preferences=['C.utf8', 'en_US.utf8']) == 'C.utf8'

# Generated at 2022-06-12 23:25:21.079888
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from collections import namedtuple

    m = AnsibleModule(argument_spec={})

    # test posix, macosx, linux and english fallbacks

# Generated at 2022-06-12 23:25:30.619639
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # test passing of preferences
    assert get_best_parsable_locale(None, ['C', 'POSIX', 'en_US.UTF8']) == 'C'
    assert get_best_parsable_locale(None, ['C', 'POSIX', 'en_US.UTF8', 'fopsi']) == 'fopsi'
    assert get_best_parsable_locale(None, ['C', 'POSIX', 'fopsi', 'en_US.UTF8']) == 'fopsi'
    assert get_best_parsable_locale(None, ['fopsi', 'C', 'en_US.UTF8', 'POSIX']) == 'fopsi'

# Generated at 2022-06-12 23:25:37.299343
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    assert get_best_parsable_locale(test_module, preferences=['a', 'b']) == 'a'
    assert get_best_parsable_locale(test_module, preferences=None) == 'C'

# Generated at 2022-06-12 23:25:44.563977
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def run_module():
        module_args = dict()
        module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=True
        )
        return module

    module = run_module()

    assert get_best_parsable_locale(module, preferences=['C', 'en_US.utf8']) == 'C'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'C']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8']) == 'C.utf8'

# Generated at 2022-06-12 23:25:55.132655
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock an object to get the get_bin_path()
    class AnsibleModuleMock(object):
        def __init__(self, module_name, module_args):
            pass
        def get_bin_path(self, tool):
            return "/usr/bin/locale"
        def run_command(self, commands):
            if commands[1] == '-a':
                return (0, "en_US.utf8\na_BC.utf8", "")
            else:
                return (0, "", "")

    module = AnsibleModuleMock("fake-module-name", "fake-module-args")
    locale = get_best_parsable_locale(module, ['a_BC.utf8', 'C.utf8'], False)

# Generated at 2022-06-12 23:26:02.469451
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import os
    import tempfile

    # Make sure that we create the module class with a load_module call
    # or we will have problems like the test case below that tries to load
    # things from ../library into the module_utils path
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class MyModule(basic.AnsibleModule):
        pass

    # We want to use a temproary directory for the module that is local to our test
    # otherwise we might end up accidentially loading a different module from PATH
    temppath = tempfile.mkdtemp(dir='/tmp')
    os.environ['PATH'] = to_bytes(':'.join([temppath, os.environ['PATH']]))

    test_module_path = os.path

# Generated at 2022-06-12 23:26:39.557341
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Sanity test for get_best_parsable_locale
    '''

    import sys
    import os
    import subprocess
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(AnsibleModule):
        def get_bin_path(self, arg):
            return 'locale'

        def run_command(self, cmd):
            (output, returncode, error) = subprocess.getstatusoutput(cmd)
            return (returncode, output, error)

    mod = MockModule(argument_spec={})

    # We're looking for a specific locale, that should exist everywhere
    test_prefs = ['C.utf8', 'en_US.utf8', 'C', 'POSIX', 'Dutch']

# Generated at 2022-06-12 23:26:45.471679
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for ansible.module_utils.distro.get_best_parsable_locale
        Makes sure that locale for "C" is returned by default
        Makes sure that the first available locale from the preferences is returned
    '''
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
    )

    assert get_best_parsable_locale(module=module) == 'C'

    preferences = ['C.utf8', 'en_UK.utf8']
    available = [preferences[1]]

    module.run_command = lambda args: (0, '\n'.join(available), None)


# Generated at 2022-06-12 23:26:53.495054
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class AnsibleModule:

        def __init__(self):
            self.params = {}
            self.result = dict(changed=False, stderr='', stdout='C.UTF-8')

        def run_command(self, cmd):
            return 0, self.result['stdout'], self.result['stderr']

        def get_bin_path(self, path):
            return True

    module = AnsibleModule()
    assert get_best_parsable_locale(module) == 'C'
    module.result['stdout'] = 'C.UTF-8\nen_US.UTF-8'
    module.result['stderr'] = ''
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:27:02.357728
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Test without any locale preferences
    module = AnsibleModule()
    locale = get_best_parsable_locale(module)
    if locale not in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']:
        raise RuntimeError("What? %s" % locale)

    # Test with a list of locale preferences
    module = AnsibleModule()
    preferences = ['C.utf8', 'en_US.utf8', 'POSIX', 'C']
    locale = get_best_parsable_locale(module, preferences)
    if locale not in ['C.utf8', 'en_US.utf8', 'POSIX', 'C']:
        raise RuntimeError("What? %s" % locale)