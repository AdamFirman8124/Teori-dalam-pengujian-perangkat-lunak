

# Generated at 2022-06-12 23:17:16.668589
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.modules.system.locale as locale_module
    import ansible.module_utils.basic as basic

    # Create a test AnsibleModule
    dummy_dict = dict(
        ansible_loop=dict(type='set', elements='list', required=True),
        ansible_check_mode=dict(type='bool'),
        ansible_debug=dict(type='bool'),
        ansible_verbosity=dict(type='int', default=0),
    )
    am = basic.AnsibleModule(argument_spec=dummy_dict)

    # Create a test for function get_best_parsable_locale
    def test_get_best_parsable_locale():
        '''
        Sample unit test for get_best_parsable_locale
        '''


# Generated at 2022-06-12 23:17:18.936668
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:17:26.319753
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        test_get_best_parsable_locale - unit test function get_best_parsable_locale
        :return: (success, failure)
    '''

    from ansible.module_utils.basic import AnsibleModule

    # class used by ansible module to throw an error
    class AnsibleFailJson(Exception):
        def __init__(self, msg):
            self.msg = msg

    # class used by ansible module to return a result
    class AnsibleExitJson(Exception):
        def __init__(self, rc):
            self.rc = rc

    # class used by ansible module for logging
    class AnsibleModuleLog(object):
        def __init__(self, msg):
            print(msg)

    # class used by ansible module to get the path of an executable


# Generated at 2022-06-12 23:17:34.578683
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    _preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']


# Generated at 2022-06-12 23:17:45.356533
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    class TestModule(AnsibleModule):
        def get_bin_path(self, arg):
            return 'locale'
        def run_command(self, arg):
            return (0,'de_DE utf8 en_US.utf8 C.utf8 POSIX','')
    test_data = [
        {
            'expected': 'de_DE',
            'preferences': ['de_DE', 'en_US']
        },
        {
            'expected': 'C.utf8',
            'preferences': ['ja_JP.utf8', 'de_DE']
        },
    ]


# Generated at 2022-06-12 23:17:52.976008
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class AnsibleModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name):
            return '/usr/bin/locale'

        def run_command(self, cmd):
            rc = 0
            if cmd[1] == '-a':
                out = 'C.utf8\n' \
                      'de_DE.utf8\n' \
                      'en_US.utf8\n' \
                      'C\n' \
                      'POSIX'
            else:
                rc = 1
                out = 'locale: Cannot set LC_CTYPE to default locale: No such file or directory'

            err = ''

            return rc, out, err

    test_module = AnsibleModule()


# Generated at 2022-06-12 23:18:04.496025
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys

    # silent noqa b'' is because we need the data to be a str, not bytes
    # but because the function is expecting a bytes type, we need to ignore
    # those errors.
    #
    # test_data is a tuple of (preferences, locale_a_output, locale_v_output, locale_v_output_C_url8, expected_return_value)

# Generated at 2022-06-12 23:18:05.173776
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'



# Generated at 2022-06-12 23:18:14.981094
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class Module(object):
        def __init__(self):
            self.exit_json = lambda x, y: None

        def get_bin_path(self, var):
            return '/usr/bin/locale'

        def run_command(self, args):
            rc = 0
            err = ''
            out = '''
en_US.utf8
en_US.UTF-8
en_US.utf-8

'''
            if args[0] == '/usr/bin/locale':
                if args[1] == '-a':
                    return (rc, out, err)

            rc = 1
            return (rc, out, err)

    module = Module()

    preferences = ['en_US.utf8', 'en_US.UTF-8', 'en_US.utf-8']
    found

# Generated at 2022-06-12 23:18:21.833354
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # setup valid locales with some not utf8
    locales = ['C', 'POSIX', 'C.utf8', 'en_US.utf8', 'en_US.ISO8859-1']

    # valid locale preferences
    # should return best locale from preference list
    assert get_best_parsable_locale(module, ['C.utf8', 'POSIX'], False) == 'C.utf8'
    assert get_best_parsable_locale(module, ['POSIX', 'C.utf8'], False) == 'POSIX'

# Generated at 2022-06-12 23:18:35.739317
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    ''' test above function with an empty list / None - should return "C" '''
    try:
        preferences = list()
        assert get_best_parsable_locale(preferences) == 'C'
    except:
        assert False

    ''' test above function with a list of one item (en_US.utf8) - should return the same item '''
    try:
        preferences = ['en_US.utf8']
        assert get_best_parsable_locale(preferences) == 'en_US.utf8'
    except:
        assert False

    ''' test above function with a list of more than one item - should return the last one '''

# Generated at 2022-06-12 23:18:45.287087
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class FakeModule(object):
        @classmethod
        def get_bin_path(self, name):
            '''
            Fake get_bin_path method
            '''
            return '/bin/locale'

        @classmethod
        def run_command(self, cmd, args=dict(check_rc=True)):
            '''
            Fake run_command method
            '''
            if cmd[1] == '-a':
                return (0, 'C\nen_US.utf8', '')
            else:
                return (0, '', '')

    fake_module = FakeModule()
    result = get_best_parsable_locale(fake_module)
    assert result == 'en_US.utf8'


# Generated at 2022-06-12 23:18:49.111217
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Verify that a default locale is returned
    assert get_best_parsable_locale(None) == 'C'

    # Verify that a preference for a specific locale is honored
    assert get_best_parsable_locale(None, preferences=['fake_locale']) == 'C'

    # Verify that the best locale is returned when multiple are present
    assert get_best_parsable_locale(None, preferences=['C', 'POSIX', 'fake_locale']) == 'C'

# Generated at 2022-06-12 23:18:59.772124
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Mock AnsibleModule class
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}
            self.run_command_results = {
                ('locale', '-a'): (0, 'en_US.utf8\nC\nC.UTF-8\nen_US\nPOSIX\n', None),
            }

        def get_bin_path(self, cmd):
            return '/bin/' + cmd

        def run_command(self, cmd):
            return self.run_command_results[(cmd[0], cmd[1])]

    # Case 1: No locale is available.
    res = get_best_parsable_locale(MockAnsibleModule())
    assert res == 'C'

    # Case 2: Preferred list is not given.


# Generated at 2022-06-12 23:19:09.053156
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    mod = AnsibleModule()

    # This is a pretty lame test but also pretty obvious what it
    # is trying to do
    assert 'C' == get_best_parsable_locale(mod)

    # Same as above
    assert 'C' == get_best_parsable_locale(mod)

    assert 'C' == get_best_parsable_locale(mod, raise_on_locale=True)
    assert 'C' == get_best_parsable_locale(mod, preferences=['LOL', 'ROFL'])
    assert 'C' == get_best_parsable_locale(mod, raise_on_locale=True, preferences=['LOL', 'ROFL'])

# Generated at 2022-06-12 23:19:17.544505
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class ModuleStub():
        def __init__(self):
            self.rc = 0
            self.out = ''
            self.err = ''
        def get_bin_path(self, bin_name, required=None):
            return bin_name
        def run_command(self, bin_path, data=None, check_rc=True, close_fds=True, executable=None,
                        data_encoding=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=False, prompt_regex=None):
            return self.rc, self.out, self.err

    # Test err == 0 and out == ''
    module = ModuleStub()
    test_locale = get_best_parsable_locale(module)
    assert test_locale

# Generated at 2022-06-12 23:19:29.245555
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test if get_best_parsable_locale returns the correct locale from run_command"""
    from ansible.module_utils.basic import AnsibleModule
    import mock

    import locale

    module = AnsibleModule(argument_spec=dict())

    # Test if correct language is found despite different order in the output of subprocess
    run_command_mock = mock.Mock(return_value=(0, "C.UTF-8\nen_US.UTF-8\n", None))
    module.run_command = run_command_mock

    assert get_best_parsable_locale(module) in ("en_US.UTF-8", "C.UTF-8")

    # Test if default 'C' locale is found if no language matches and no preferred languages are given
    run_command_mock = mock.Mock

# Generated at 2022-06-12 23:19:40.508039
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Normal execution
    module_mock = Mock()
    module_mock.get_bin_path.return_value = '/bin/locale'
    module_mock.run_command.return_value = (0, 'C\nen_US.utf8\nC.utf8\nPOSIX\n', None)
    assert 'en_US.utf8' == get_best_parsable_locale(module_mock)

    # No available locales
    module_mock.run_command.return_value = (0, None, None)
    assert 'C' == get_best_parsable_locale(module_mock)

    # 'locale' not found
    module_mock.get_bin_path.return_value = None
    assert 'C' == get_best_parsable

# Generated at 2022-06-12 23:19:48.836122
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def mock_get_bin_path(module, required=False):
        if 'locale' in module:
            return module
        else:
            return None


# Generated at 2022-06-12 23:19:57.997576
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = AnsibleModule(argument_spec={})

    # first use our values
    preferences = ['C', 'POSIX']
    assert get_best_parsable_locale(module, preferences) == "C"

    # now preferences should have come from the module
    assert get_best_parsable_locale(module) == "C"

    # now that we expect a locale to exist, it should raise an exception
    # without the preferences set
    import pytest
    with pytest.raises(Exception):
        get_best_parsable_locale(module, raise_on_locale=True)

    # if we simply try all of them, the order should not matter
    import random
    preferences = ['C', 'POSIX', 'C.utf8', 'en_US.utf8']

# Generated at 2022-06-12 23:20:11.278717
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    assert get_best_parsable_locale(test_module) == "C"

    # zh_HK.utf8 is not present
    assert get_best_parsable_locale(test_module, ["zh_HK.utf8"]) == "C"
    assert get_best_parsable_locale(test_module, ["zh_HK.utf8"], True) == "C"

    # en_US.utf8 is present
    assert get_best_parsable_locale(test_module, ["en_US.utf8"]) == "en_US.utf8"

# Generated at 2022-06-12 23:20:22.468037
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class FakeModule(object):
        def run_command(self, command):
            out = b"""\
C
C.UTF-8
en_US.utf8
POSIX
"""
            return 0, out, None

        def get_bin_path(self, binary):
            return binary

    module = FakeModule()

    # Test with valid arguments
    assert get_best_parsable_locale(module) == "C.UTF-8"

    # Test with locale not available
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'ja_JP.utf8', 'C', 'POSIX']) == "C.utf8"

    # Test with empty preferences
    assert get_best_parsable_locale(module, preferences=[]) == "C"

# Generated at 2022-06-12 23:20:33.520896
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import collections
    import os
    import sys

    import ansible.module_utils.basic as basic

    AnsibleModule = basic.AnsibleModule
    # OSX has fewer locales available than FreeBSD
    # see https://github.com/ansible/ansible/issues/24266
    if sys.platform.startswith('darwin'):
        # osx: only C, UTF-8, US-ASCII
        available_locales = ['C', 'en_US.utf-8', 'en_US.US-ASCII']
        preferred_locales = ['C', 'C.utf8', 'POSIX']
    else:
        preferred_locales = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
        # FreeBSD:

# Generated at 2022-06-12 23:20:39.665660
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class ModuleMock(object):
        def get_bin_path(self, binary):
            if binary == 'locale':
                return './locale'

        def run_command(self, cmd, *args):
            out = ''
            rc = 0

            if cmd == ['./locale', '-a']:
                if 'locale_out' in args:
                    out = args['locale_out']
                if 'locale_rc' in args:
                    rc = args['locale_rc']

            err = ''
            return rc, out, err

    # Test when locale is found, it returns the first match for
    # the preferred locales
    module_mock = ModuleMock()

# Generated at 2022-06-12 23:20:45.833483
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    test_params = dict(
        preferences=['C.utf8', 'C', 'en_US.utf8']
    )
    module = AnsibleModule(
        argument_spec=test_params,
        supports_check_mode=True
    )
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:20:54.582107
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()
    locale = get_best_parsable_locale(module, preferences=['en_US.UTF-8', 'en_US.UTF8', 'C', 'POSIX'])
    assert locale == 'en_US.UTF-8' or locale == 'en_US.UTF8' or locale == 'C' or locale == 'POSIX'

    locale = get_best_parsable_locale(module, preferences=['fr_FR.UTF-8', 'en_US.UTF8', 'C', 'POSIX'])
    assert locale == 'en_US.UTF8' or locale == 'C' or locale == 'POSIX'


# Generated at 2022-06-12 23:21:05.906193
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path

    bin_path = get_bin_path('locale')
    if bin_path is None:
        raise RuntimeError("'locale' not found, test skipped")

    # basic test of English (US)
    module = get_ansible_mod_func('test_module')
    assert module is not None

    rc, out, _ = module.run_command([bin_path, '-a'], check_rc=True)
    locale = get_best_parsable_locale(module)
    assert locale in out

    # test that it works using an alternate, ie. non-english locale
    module = get_ansible_mod_func('test_module')
    assert module is not None


# Generated at 2022-06-12 23:21:10.456848
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    m = ansible.module_utils.basic.AnsibleModule(argument_spec={})

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(m, preferences=preferences) == 'C'

# Generated at 2022-06-12 23:21:11.661784
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    assert get_best_parsable_locale(mock.MagicMock(), raise_on_locale=True) == 'C'

# Generated at 2022-06-12 23:21:21.103447
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.local_ansible_utils as local_ansible_utils
    import ansible.module_utils.common.warnings as warnings

    class FakeModule(object):
        def __init__(self):
            self.fail_json = basic.fail_json
            self.warnings = []
        def get_bin_path(self, name):
            if name == 'locale':
                return True
            return False
        def run_command(self, command):
            if command[0] == 'locale':
                if command[1] == '-a':
                    return (0, 'C\nen_US.UTF-8', '')
            return (0, '', '')

    m = FakeModule()
    assert local_ansible_utils

# Generated at 2022-06-12 23:21:40.801586
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible
    from ansible.module_utils.basic import AnsibleModule

    # define a test module that is available from ansible import module_utils
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # get the best locale for parsing output in english
    locale = get_best_parsable_locale(module)

    # assert that we received a valid locale
    assert type(locale) is str
    assert len(locale) > 0


if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:21:52.090646
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    module.run_command = run_command_fake
    assert get_best_parsable_locale(module) == 'C.utf8'
    assert get_best_parsable_locale(module, preferences=['C']) == 'C'
    assert get_best_parsable_locale(module, preferences=['en_US.utf8']) == 'en_US.utf8'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C.utf8'
    assert get_best_parsable_locale(module, preferences=['C'], raise_on_locale=True) == 'C'
    assert get_best

# Generated at 2022-06-12 23:21:58.681314
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    best = get_best_parsable_locale(None, None, False)
    if best != 'C':
        raise AssertionError("unit test for get_best_parsable_locale failed")
    best = get_best_parsable_locale(None, ['C'], False)
    if best != 'C':
        raise AssertionError("unit test for get_best_parsable_locale failed")



# Generated at 2022-06-12 23:22:07.959345
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    # when we don't have locale
    module.get_bin_path = lambda *args: None
    assert get_best_parsable_locale(module) is 'C'

    # when we have locale but bad/no output
    module.run_command = lambda *args: (0, '', '')
    assert get_best_parsable_locale(module) is 'C'

    module.run_command = lambda *args: (1, '', '')
    assert get_best_parsable_locale(module) is 'C'

    # now we have locale and output, but not what we want
    module.run_command = lambda *args: (0, 'foo\nbar', '')
    assert get

# Generated at 2022-06-12 23:22:12.210469
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    found = get_best_parsable_locale(module)
    assert found == 'C'

    preferences = ['foo', 'bar']
    found = get_best_parsable_locale(module, preferences)
    assert found == 'C'

# Generated at 2022-06-12 23:22:12.654417
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    pass

# Generated at 2022-06-12 23:22:22.281477
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict()
    )

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['doesn\'t','matter','C','as','no','locale','will','be','found']) == 'C'

    module.run_command = lambda cmd: ('/usr/bin/locale', 0, ['c\nC.UTF-8\nPOSIX\nen_US.UTF-8\nen_US.ISO8859-1\n'])
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:22:29.367923
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    This is a unit test for disambiguating locales
    '''

    # Test 1
    preferences_1 = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    available_locales_1 = ['test1', 'test2', 'test3', 'test4']
    expected_result_1 = 'C.utf8'
    assert expected_result_1 == get_best_parsable_locale(None, preferences_1, available_locales_1)

    # Test 2
    preferences_2 = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    available_locales_2 = ['test6', 'test7', 'C', 'test9']
    expected_result_2 = 'C'
    assert expected_result_

# Generated at 2022-06-12 23:22:34.592141
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # fake class
    class MyClass(object):
        def get_bin_path(self, foo):
            return True

    m = MyClass()
    # test for output that fails
    m.run_command = lambda x: [0, '', '']
    try:
        get_best_parsable_locale(m)
    except RuntimeWarning:
        pass
    else:
        raise AssertionError("locale module should not have loaded")
    # test for output that results in no locale
    m.run_command = lambda x: [1, '', 'Unable to get locale information']
    assert get_best_parsable_locale(m) == "C", "locale module did not load"
    # test for output that results in C.utf8

# Generated at 2022-06-12 23:22:42.962155
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        This tests the get_best_parsable_locale function
    '''

    from ansible.module_utils.basic import AnsibleModule

    # First create a mock module
    module = AnsibleModule(argument_spec={})

    # Verify that we get C locale as that's always supported
    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    tmp_locale = set_locale(module)
    assert tmp_locale != 'C'
    locale = get_best_parsable_locale(module)
    assert locale == tmp_locale



# Generated at 2022-06-12 23:23:15.889647
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    locale_found = get_best_parsable_locale(module, preferences)
    assert isinstance(locale_found, str), 'result is a string'
    assert locale_found != '', 'result is not empty'

# Generated at 2022-06-12 23:23:23.556717
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # pylint: disable=import-error, unused-variable
    import ansible.module_utils.basic
    mock_module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    mock_module.run_command = lambda cmd: (0, 'C.utf8\nen_US.utf8\nC\nPOSIX\nX\n', '')
    assert get_best_parsable_locale(mock_module) == 'C.utf8'
    assert get_best_parsable_locale(mock_module, ['en_US.utf8', 'X']) == 'en_US.utf8'
    assert get_best_parsable_locale(mock_module, ['X', 'Y']) == 'C'

    mock_module.run_command

# Generated at 2022-06-12 23:23:31.921590
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})

    # test happy path
    module.run_command = lambda x: (0, 'C\nen_US.utf8\nBADLOCALE\nen_US.ISO.8859-2\nC.UTF-8\n', '')
    locale = get_best_parsable_locale(module, preferences=['en_US.utf8', 'en_US.ISO.8859.2', 'en_US.ISO.8859-2'])
    assert locale == 'en_US.utf8'

    # test command not found
    module.run_command = lambda x: (127, '', "Mock_RuntimeWarning_locale_not_found")
    locale = get_best_

# Generated at 2022-06-12 23:23:38.240950
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import re
    import subprocess

    # Get the available system locales
    proc = subprocess.Popen(['locale', '-a'], stdout=subprocess.PIPE)
    actual_locales = proc.communicate()[0].strip().splitlines()

    # Build the test parameters array
    test_params = []

    # Build the expected results array
    expected_results = []

    # Build the test with no preferred locale as input parameter
    test_params.append(None)
    expected_results.append('C')
    for locale in actual_locales:
        if re.match('^C$|.utf8$', locale):
            expected_results.append(locale)
            break
    else:
        raise Exception("The 'locale -a' command didn't return the expected result in the test")



# Generated at 2022-06-12 23:23:46.259935
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import get_exception
    from ansible.module_utils.common.locales import get_best_parsable_locale

    # Test 1:
    # The module run_command returns a non-zero exit code,
    # get_best_parsable_locale should return C.
    # (In a normal run the test would abort, but we use a dummy module
    # which allows us to run the test regardless of the results).

    rc, out, err = 1, "", "rc=1"
    module = AnsibleModule(run_command_no_persistent_connect_handle=mock.Mock(return_value=(rc, out, err)))
    best_locale = get_best_pars

# Generated at 2022-06-12 23:23:47.987745
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})
    returned = get_best_parsable_locale(module)

    assert returned == 'C'

# Generated at 2022-06-12 23:23:59.936345
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    
# returns the best possible locale for parsing output in English
# useful for scraping output with i18n tools. When this raises an exception
# and the caller wants to continue, it should use the 'C' locale.

# :param module: an AnsibleModule instance
# :param preferences: A list of preferred locales, in order of preference
# :param raise_on_locale: boolean that determines if we raise exception or not
#         due to locale CLI issues
# :returns: The first matched preferred locale or 'C' which is the default

    # new POSIX standard or English cause those are messages core team expects
    # yes, the last 2 are the same but some systems are weird

    # if preferences is None:
        # preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    assert get_best_pars

# Generated at 2022-06-12 23:24:07.279784
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    """
    Test locale.get_best_parsable_locale()
    """

    import unittest
    import ansible.module_utils.basic
    import ansible_collections.ansible.netcommon.plugins.module_utils.network.common.locale as locale

    # To create a Mock for AnsibleModule, you will need to write the following:
    # ansible.module_utils.basic.AnsibleModule = Mock(return_value=None)
    ansible.module_utils.basic.AnsibleModule = None

    # Mock class for module
    class MockAnsibleModule():
        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, tool, required=False):
            return 'locale'


# Generated at 2022-06-12 23:24:16.961834
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    rc, out, err = module.run_command(['locale', '-a'])
    locale_list = out.strip().splitlines()
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) in ['C.utf8', 'C', 'POSIX']
    if 'en_US.utf8' in locale_list:
        assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'en_US.utf8'

# Generated at 2022-06-12 23:24:19.531944
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:24:58.988389
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Verify function returns the best possible locale for parsing output
    when provided a list of preferred locales.
    """

    import ansible.module_utils.basic
    import ansible.module_utils.locale

    class TestModule(object):
        def get_bin_path(self, arg):
            return True
        def run_command(self, arg):
            out_list = ['C.utf8', 'C.UTF-8', 'C', 'en_US.utf8', 'en_US.UTF-8']
            return 0, '\n'.join(out_list), ''

    module = TestModule()

    assert ansible.module_utils.locale.get_best_parsable_locale(module) == 'C.utf8'
    assert ansible.module_utils.locale.get_best_

# Generated at 2022-06-12 23:25:08.985879
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    # Testing with all possible scenarios
    # Creates a module instance
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # test default preferences
    assert get_best_parsable_locale(module=module) == 'C'

    # test custom preferences
    assert get_best_parsable_locale(module=module, preferences=["custom1"]) == 'C'
    assert get_best_parsable_locale(module=module, preferences=["custom1", "C"]) == 'C'

# Generated at 2022-06-12 23:25:15.242398
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import sys
    import os
    import tempfile
    import shutil

    sys.modules['ansible'] = type('ansible', (object,), {})

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            preferences=dict(type='list', elements='str')
        ))


# Generated at 2022-06-12 23:25:20.670088
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Catch the warning
    from ansible.module_utils.basic import AnsibleModule

    test_module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(test_module, raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:25:30.255981
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import PY3

    module = basic.AnsibleModule(
        argument_spec=dict(),
    )

    # Custom locale list to match

# Generated at 2022-06-12 23:25:35.993238
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = AnsibleModuleMock()
    # Test that it returns the specified preference
    assert get_best_parsable_locale(module, preferences=['prefix.fr_FR.utf8'], raise_on_locale=True) == 'prefix.fr_FR.utf8'

    # Test that it prefers the first preference
    assert get_best_parsable_locale(module, preferences=['prefix.fr_FR.utf8', 'prefix.en_US.utf8'], raise_on_locale=True) == 'prefix.fr_FR.utf8'

    # Test non-existing preference
    assert get_best_parsable_locale(module, preferences=['prefix.en_US.utf8'], raise_on_locale=True) == 'C'


# Mock object to be able to test

# Generated at 2022-06-12 23:25:43.688003
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # Test 1: Check default to C if nothing found
    found = get_best_parsable_locale(module, preferences=['POSIX', 'C'], raise_on_locale=False)
    assert found == 'C'

    # Test 2: Pass in previously found locale (in this case POSIX)
    found = get_best_parsable_locale(module, preferences=['POSIX'], raise_on_locale=False)
    assert found == 'POSIX'

    # Test 3: Check default to POSIX is found if nothing passed in
    found = get_best_parsable_locale(module, preferences=None, raise_on_locale=False)
    assert found == 'POSIX'

# Generated at 2022-06-12 23:25:50.481077
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:26:00.068473
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import copy
    import textwrap
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    # set defaults for ansible module
    # we use to_bytes since this module us run against unicode strings
    # and we need to get bytes to emulate AnsibleModule
    data = copy.deepcopy(module_data)
    data.update({'ANSIBLE_MODULE_ARGS': to_bytes('{}')})
    data.update({'_ansible_version': to_bytes('2.9.9')})
    data.update({'_ansible_no_log': to_bytes(False)})
    data.update({'_ansible_module_name': to_bytes('ansible_module_test')})
    data.update

# Generated at 2022-06-12 23:26:08.778162
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    try:
        from ansible.module_utils.basic import AnsibleModule
        import sys
        has_module_util = True
    except ImportError:
        has_module_util = False

    try:
        from unittest.mock import patch, MagicMock
        from ansible.module_utils.six import StringIO

        has_unittest_mock = True
    except ImportError:
        try:
            from mock import patch, MagicMock
            from ansible.module_utils.six import StringIO

            has_unittest_mock = True
        except ImportError:
            has_unittest_mock = False

    if not has_unittest_mock or not has_module_util:
        return

    out = StringIO()
    sys.stdout = out

    module = MagicM

# Generated at 2022-06-12 23:26:39.661155
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(arguments=['-a'], preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX'], raise_on_locale=True) == 'C.utf8'

# Generated at 2022-06-12 23:26:43.079241
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    preferences = ['C.UTF-8', 'UTF-8']

    # Locale is available, returns the first available locale
    assert get_best_parsable_locale(None, preferences) == preferences[0]

    # Locale is not available, returns 'C'
    preferences = ['non-existing-locale']
    assert get_best_parsable_locale(None, preferences) == 'C'

# Generated at 2022-06-12 23:26:50.630409
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule
    assert get_best_parsable_locale(AnsibleModule(argument_spec=dict())) == 'C'

    assert get_best_parsable_locale(AnsibleModule(argument_spec=dict()),
                                    preferences=['C.UTF-8']) == 'C.UTF-8'

    assert get_best_parsable_locale(AnsibleModule(argument_spec=dict()),
                                    preferences=['C.UTF-8', 'C.utf8']) == 'C.UTF-8'

    assert get_best_parsable_locale(AnsibleModule(argument_spec=dict()),
                                    preferences=['C.utf8', 'C.UTF-8']) == 'C.utf8'

# Generated at 2022-06-12 23:26:53.983822
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, preferences=['en_US.utf8', 'C']) == 'en_US.utf8'
    assert get_best_parsable_locale(None, preferences=['yolo.utf8', 'C']) == 'C'
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:27:03.101336
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import textwrap
    from ansible.module_utils.common.process import get_bin_path, run_command
    # import other modules here
    def get_bin_path(names, required=False):
        return "locale"
