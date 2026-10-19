

# Generated at 2022-06-12 23:17:16.329268
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import os
    import sys
    import mock

    src_dir = os.path.join(os.path.dirname(__file__), '..')
    sys.path.append(src_dir)
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:17:23.988574
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Test function: get_best_parsable_locale
    """
    assert get_best_parsable_locale(None, ['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'C']) == 'C'

# Generated at 2022-06-12 23:17:31.698642
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.removed import removed_module
    from ansible.module_utils.basic import AnsibleModule

    # Stub out Ansible module, we're just testing this function
    class AnsibleModule(object):
        class AnsibleModule(object):
            class returned_from_run_command(object):
                pass
            run_command = returned_from_run_command

        def get_bin_path(self, cmd):
            return cmd

    # Create an instance of our stubbed out Ansible module
    module = AnsibleModule()

    # Test with no preferences, should return 'C' and not raise
    assert get_best_parsable_locale(module, preferences=None, raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:17:42.709176
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    def run_command(*args, **kwargs):
        if args[0][-1] == '-a':
            return (0, 'C\nfr_FR.utf8\nen_US.utf8\nja_JP.utf8\nC.utf8\nPOSIX', '')
        else:
            return (0, 'C.UTF-8', '')
    module = AnsibleModule(
        argument_spec = dict(),
    )
    module.run_command = run_command
    module.get_bin_path = lambda x: x

    locale = get_best_parsable_locale(module)
    assert locale == 'C.utf8'

    # require utf-8 and don't care what the current setting is because
    # our

# Generated at 2022-06-12 23:17:50.698272
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic

    m = basic.AnsibleModule(argument_spec={})

    # Test if exception is not raised when raise_on_locale is False
    try:
        test_val = get_best_parsable_locale(m, raise_on_locale=False)
        assert test_val == 'C'
    except Exception as e:
        assert False
    # Test if exception is raised when raise_on_locale is True
    try:
        test_val = get_best_parsable_locale(m, raise_on_locale=True)
        assert False
    except Exception as e:
        # Exception should be raised when raise_on_locale is True
        assert True

# Generated at 2022-06-12 23:18:01.464595
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes

    # create a fake module environment
    module = AnsibleModule(
        argument_spec={},
    )

    locale_path = get_bin_path('locale')

# Generated at 2022-06-12 23:18:11.846381
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class TestModule(object):
        pass
    test_module = TestModule()

    # case 1
    test_module.get_bin_path = lambda cmd: cmd
    test_module.run_command = lambda cmd: (0, 'C.utf8\nen_US.utf8', '')
    assert get_best_parsable_locale(test_module) == 'C.utf8'

    # case 2
    test_module.get_bin_path = lambda cmd: cmd
    test_module.run_command = lambda cmd: (0, 'fr_FR\nen_US.utf8', '')
    assert get_best_parsable_locale(test_module) == 'en_US.utf8'

    # case 3
    test_module.get_bin_path = lambda cmd: cmd
    test_

# Generated at 2022-06-12 23:18:20.023391
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.modules.system.locale
    import sys

    # Injecting a valid list of supported locales

# Generated at 2022-06-12 23:18:30.667277
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import unittest
    import mock
    import module_utils

    class MockModule(object):
        def __init__(self):
            self.run_command_results = []
            self.run_command_results.append(
                # locale -a, set preferred locales
                (0, 'C\nen_US.utf8\nC.utf8\nPOSIX', ''))
            self.run_command_results.append(
                # locale -a, no preferred locales, but 'C' is supported
                (0, 'C\nPOSIX', ''))
            self.run_command_results.append(
                # locale -a, no preferred locales
                (0, '', ''))

# Generated at 2022-06-12 23:18:33.633323
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict()
    )

    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:18:39.706424
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # We need a proper module instance to run the code in the function, therefore
    # it's almost impossible to test it.
    pass

# Generated at 2022-06-12 23:18:41.336931
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale({'get_bin_path': lambda x: True}) == 'C'

# Generated at 2022-06-12 23:18:51.586136
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    assert get_best_parsable_locale(module) == 'C'

    locale = module.get_bin_path("locale")
    assert get_best_parsable_locale(module, preferences=['en_US.utf8']) == 'en_US.utf8'

    # Test with a non-existing locale
    assert get_best_parsable_locale(module, preferences=['this_locale_does_not_exist']) == 'C'

    # Test with a locale that doesn't exist, but raise_on_locale is True

# Generated at 2022-06-12 23:19:01.861362
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # POSIX compliant
    m = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(m) == 'C'

    # German locale
    m = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(m, ['de_DE.UTF-8']) == 'de_DE.UTF-8'

    # English locale
    m = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(m, ['en_US.UTF-8']) == 'en_US.UTF-8'

    # English locale
    m = AnsibleModule(argument_spec={})

# Generated at 2022-06-12 23:19:12.220575
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic
    import sys
    import os

    mod = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    old_run_command = basic.AnsibleModule.run_command

    def fake_run_command(self, cmd):
        if cmd[0] == mod.get_bin_path("locale"):
            if cmd[1] == '-a':
                output = """
C.UTF-8
en_US.utf8
POSIX
"""
            else:
                output = ''
            return (0, output, '')
        else:
            return old_run_command(self, cmd)

    basic.AnsibleModule.run_command = fake_run

# Generated at 2022-06-12 23:19:22.655950
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:19:34.710656
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.six import PY3
    import random
    import re
    if PY3:
        from subprocess import DEVNULL
    else:
        from subprocess import STDOUT
        DEVNULL = open(os.devnull, 'wb', 0)
    import subprocess

    class AnsibleModule:
        class _anstest:
            class _ansible_test_module_args:
                def __contains__(self, arg):
                    return True
                def __getitem__(self, arg):
                    return ''
            class _ansible_module_post_params:
                def __contains__(self, arg):
                    return True
                def __getitem__(self, arg):
                    return ''


# Generated at 2022-06-12 23:19:42.973338
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    module = AnsibleModule(
        argument_spec=dict(),
    )

    # Mock some things for the module
    module.run_command = lambda args, check_rc=True, close_fds=True, executable=None: (0, 'en_US.utf8', None)
    module.get_bin_path = lambda arg, required=False, opt_dirs=[] : "/bin/%s" % arg

    # This will fail and return the default, 'C'
    module.run_command = lambda args, check_rc=True, close_fds=True, executable=None: (127, None, None)
    found = get_best_parsable_locale(module)
    assert found

# Generated at 2022-06-12 23:19:50.158016
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os
    module = AnsibleModule(argument_spec=dict())
    locale = module.get_bin_path("locale")
    # Test without locale command
    assert get_best_parsable_locale(module) == 'C'
    # Test with default preferences
    assert get_best_parsable_locale(module) == 'C'
    # Test with a custom preferences list
    assert get_best_parsable_locale(module, preferences=['C', 'POSIX']) == 'C'
    # Test with locale command
    os.environ["PATH"] = os.path.dirname(__file__)
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:19:52.917284
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''test_get_best_parsable_locale unit test'''
    test_module = None
    assert get_best_parsable_locale(test_module) == 'C'

# Generated at 2022-06-12 23:20:00.048705
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    pass

# Generated at 2022-06-12 23:20:03.231071
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})

    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:20:11.615226
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    class FakeModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            mock_out = '''
C
C.utf8
en_US.utf8
POSIX
'''

            if PY3:
                mock_out = bytes(mock_out, 'utf-8')

            super(FakeModule, self).__init__({'run_command': {'return_value': [0, mock_out, '']}, 'warnings': []}, *args, **kwargs)

    module = FakeModule()

    assert 'en_US.utf8' == get_best_parsable_locale(module)

# Generated at 2022-06-12 23:20:22.702000
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule, get_bin_path

    assert 'C' == get_best_parsable_locale(AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    ), raise_on_locale=True)

    assert 'C' == get_best_parsable_locale(AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    ), ['en_US.utf8'])

    # the module is not initialized
    assert 'C' == get_best_parsable_locale(None, None, raise_on_locale=True)
    assert 'C' == get_best_parsable_locale(None, None, raise_on_locale=False)

# Generated at 2022-06-12 23:20:33.790934
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Testing POSIX locales
    test_locale_1 = ['en_US.utf8', 'C.utf8', 'C']
    assert get_best_parsable_locale(test_locale_1) == 'C'
    # Testing non-POSIX locales
    test_locale_2 = ['fr_FR.utf8', 'ar_SA.utf8', 'es_ES.utf8']
    assert get_best_parsable_locale(test_locale_2) == 'C'
    # Testing non-existing locales
    test_locale_3 = ['en_GB.utf8', 'en_NZ.utf8', 'en_AU.utf8']
    assert get_best_parsable_locale(test_locale_3) == 'C'
    # Testing locale that

# Generated at 2022-06-12 23:20:39.850566
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Note, this is a unit test which is run in test/sanity/code-smell/test_shared.py
        It is included here, instead of test/units/module_utils/facts/system/os/linux.py
        because it uses a function from this file. Currently this is not important
        but as more function are added to this file and are used for unit testing
        it may be worth moving this test to this file.
    '''
    from ansible.modules.system import linux
    from ansible.module_utils.facts.system.os.linux import get_best_parsable_locale
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes, to_native


# Generated at 2022-06-12 23:20:50.673954
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    best_locale_list = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Best locale is 'C'
    assert get_best_parsable_locale(module, preferences=best_locale_list) == 'C'
    assert get_best_parsable_locale(module, preferences=best_locale_list, raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, preferences=None, raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, preferences=None, raise_on_locale=False) == 'C'

# Generated at 2022-06-12 23:20:57.606274
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module_mock = AnsibleModule()
    module_mock.run_command = run_command_mock
    assert get_best_parsable_locale(module_mock) == 'C.utf8'
    assert get_best_parsable_locale(module_mock, preferences=['en_US.utf8', 'en_US', 'POSIX']) == 'en_US'
    assert get_best_parsable_locale(module_mock, preferences=['POSIX']) == 'C'
    assert get_best_parsable_locale(module_mock, raise_on_locale=True) == 'C'



# Generated at 2022-06-12 23:21:02.509172
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp()

    # Create .dummy-locale
    with open(os.path.join(test_dir, 'dummy-locale'), 'w') as f:
        f.write('')
    os.chmod(os.path.join(test_dir, 'dummy-locale'), 0o755)

    # Create test module
    class TestAnsibleModule:
        def __init__(self):
            self.bin_path = test_dir
            self.run_command_calls = []

        def run_command(self, command, *args, **kwargs):
            self.run_command_calls.append(command)
            if command == ['locale', '-a']:
                return 0,

# Generated at 2022-06-12 23:21:08.008616
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    am = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
    )
    test1 = get_best_parsable_locale(am)
    assert test1 == 'C', "Received unexpected result from get_best_parsable_locale: %s" % test1

# Generated at 2022-06-12 23:21:26.871269
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile

    script = """
from ansible.module_utils.common.locales import get_best_parsable_locale

module_args = dict(
    name='test',
    preferences=['C.utf8', 'en_US.utf8', 'C', u'POSIX']
)

module = AnsibleModule(argument_spec=module_args)
preference = module.params['preferences']
got_locale = get_best_parsable_locale(module, preference)
if got_locale:
    module.exit_json(msg='test', preference=preference, return_value=got_locale)
else:
    module.fail_json(msg="Can't find a valid locale")
"""

    script_output

# Generated at 2022-06-12 23:21:35.221360
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Make sure that we find C locale if it exists
    assert get_best_parsable_locale() == 'C'

    # Make sure that we find C.utf8 locale if it exists
    assert get_best_parsable_locale(preferences=['C.utf8', 'en_US.utf8']) == 'C.utf8'

    # Make sure that we find en_US.utf8 locale if it exists
    assert get_best_parsable_locale(preferences=['en_US.utf8', 'C']) == 'en_US.utf8'

# Generated at 2022-06-12 23:21:43.479484
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ['en_US.utf8', 'C']) == 'C'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'POSIX']) == 'POSIX'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'C.utf8']) == 'C.utf8'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'en_US.utf8', 'POSIX']) == 'en_US.utf8'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'en_US.utf8', 'C.utf8']) == 'en_US.utf8'
   

# Generated at 2022-06-12 23:21:54.283678
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    # If locale is not present then C locale should be returned.
    module.get_bin_path = lambda x: None
    assert module.get_best_parsable_locale() == 'C'

    # Now we mock the locale command to return C locale as available one.
    module.get_bin_path = lambda x: 'locale'
    module.run_command = lambda x: (0, 'C', '')
    assert module.get_best_parsable_locale() == 'C'

    # Now we mock the locale command to return C locale as available one
    # and we expect C locale.

# Generated at 2022-06-12 23:22:05.259088
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock
    # Make sure we do not require 'locale' to be in PATH
    import ansible.module_utils.basic

    # Default locales
    my_module = mock.MagicMock(spec=ansible.module_utils.basic.AnsibleModule)
    assert get_best_parsable_locale(my_module, None) == 'C'

    # Non-existent locale
    my_module.run_command.return_value = (0, '\n'.join(['C', 'en_US', 'POSIX']), '')
    assert get_best_parsable_locale(my_module, ['zh_CN.utf8', 'zh_CN.gb2312']) == 'C'

    # Locale in PATH

# Generated at 2022-06-12 23:22:11.412255
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    locale_info = {
        'c': 'C',
        'default': 'C',
        'en_US.UTF-8': 'en_US.UTF-8',
        'en': 'en_US.UTF-8',
        'en_US': 'en_US.UTF-8',
        'en_US.ISO-8859-1': 'en_US.ISO-8859-1',
        'en.UTF-8': 'en_US.UTF-8',
        'en.ISO-8859-1': 'en_US.ISO-8859-1',
        'c.iso-8859-1': 'c.iso-8859-1'
    }

    for k in locale_info:
        assert get_best_parsable_locale(module=None, preferences=[k]) == locale_

# Generated at 2022-06-12 23:22:14.834720
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    :returns: A tuple containing the function get_best_parsable_locale, and
              the parameters to use for test framework.
    '''
    return (get_best_parsable_locale, dict(preferences=None, raise_on_locale=True))

# Generated at 2022-06-12 23:22:24.737232
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os

    module = AnsibleModule(
        argument_spec=dict(),
    )

    # Check standard preference
    c_locale = get_best_parsable_locale(module)
    assert c_locale == 'C'
    assert c_locale in os.environ.get('LC_ALL', '')

    # check custom locale preference
    c_locale = get_best_parsable_locale(module, ['C', 'en_US.utf8'])
    assert c_locale == 'C'
    assert c_locale in os.environ.get('LC_ALL', '')

if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:22:33.630394
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Import here only to avoid circular imports
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module) == 'C'
    locale = module.get_bin_path("locale")
    assert locale
    assert get_best_parsable_locale(module, ['C.utf8']) == 'C.utf8'
    assert get_best_parsable_locale(module, ['C.utf8', 'POSIX']) == 'C.utf8'
    assert get_best_parsable_locale(module, ['FOO', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:22:44.139326
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    # FIXME: temporary until we have module_utils.local installed
    module.get_bin_path = lambda x: x
    module.run_command = lambda x: (0, 'C\nPOSIX', None)

    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['POSIX']) == 'POSIX'
    assert get_best_parsable_locale(module, preferences=['POSIX', 'C']) == 'POSIX'
    assert get_best_parsable_locale(module, preferences=['en_US', 'en_GB']) == 'C'
    assert get_best_

# Generated at 2022-06-12 23:23:04.899936
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock(return_value=(0, "C\nen_US.utf8\nPOSIX\n", ""))

    locale = get_best_parsable_locale(module)
    assert locale == "C.utf8"

    module.run_command = MagicMock(return_value=(0, "en_GB.utf8\nen_US.utf8\nen_ZA.utf8\nPOSIX\n", ""))
    module.params['preferences'] = ["en_ZA.utf8", "en_GB.utf8"]
    locale = get_best_parsable_locale(module)
    assert locale == "en_ZA.utf8"

    module

# Generated at 2022-06-12 23:23:14.186399
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class testModule:
        def __init__(self):
            self.run_command_checked = self.run_command
            self.run_command = self.run_command_unchecked

        def run_command_checked(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False):
            assert not check_rc, "'get_best_parsable_locale' should not use check_rc=True"
            assert not close_fds, "'get_best_parsable_locale' should not close_fds"
            assert executable is None, "'get_best_parsable_locale' should not set executable"
            assert data is None, "'get_best_parsable_locale' should not set data"

# Generated at 2022-06-12 23:23:22.631631
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._text import to_native
    import locale
    import sys

    # Create the mock module
    am = AnsibleModule(
        argument_spec=dict(),
    )

    # Test without any available locales
    saved_locale = [locale.getlocale(locale.LC_ALL)]

    # Test with no locale selected
    am.run_command = lambda cmd: (1, "", "")
    try:
        assert ('C' == get_best_parsable_locale(am))
    except RuntimeWarning as e:
        pass
        assert ('Could not find \'locale\' tool' == to_native(e))

    # Test with an invalid locale selected

# Generated at 2022-06-12 23:23:30.338172
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test calling get_best_parsable_locale w/ different inputs
    '''
    import ansible.module_utils.basic
    import os

    test_data = {'C': 'aA4k4',
                 'de_DE.utf8': 'äÄ4k4',
                 'fr_FR.utf8': 'àÀ4k4',
                 'it_IT.utf8': 'àÀ4k4',
                 'nl_NL.utf8': 'äÄ4k4',
                 'sv_SE.utf8': 'äÄ4k4',
                 'vi_VN.utf8': 'àÀ4k4'}

    my_locale = os.environ.get('LC_ALL', None)


# Generated at 2022-06-12 23:23:39.278961
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils
    # need a fake module
    class DummyModule(object):
        def __init__(self):
            self.params = {}
            self.module = self.module_arg_spec()
            self.run_command_environ_update = {}
            self.resources = {}
            self.supports_check_mode = True

        def get_bin_path(self, command):
            return '/bin/' + command


# Generated at 2022-06-12 23:23:45.304406
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    locale = get_best_parsable_locale(module)
    assert locale == 'C'

    # Mock locale -a
    module.run_command = lambda args, check_rc=False: (0, 'C.utf8\nen_US.utf8\nC', '')

    locale = get_best_parsable_locale(module, preferences=['en_US.utf8'])
    assert locale == 'en_US.utf8'

# Generated at 2022-06-12 23:23:57.347822
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
        add_file_common_args=False,
    )
    # values from http://man7.org/linux/man-pages/man7/locale.7.html
    locale_list = ['C.UTF-8', 'en_US.iso88591', 'POSIX', 'C']
    assert 'C' == get_best_parsable_locale(m, locale_list)
    locale_list = ['en_US.utf8', 'C.utf8', 'POSIX', 'C']
    assert 'en_US.utf8' == get_best_parsable_locale(m, locale_list)

# Generated at 2022-06-12 23:24:05.187494
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY3

    # Mock module and module utils
    m = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    m.get_bin_path = lambda x: True
    m.run_command = lambda x: (0, 'foo', None)
    assert get_best_parsable_locale(m) == 'foo'

    # Test no system
    m.run_command = lambda x: (1, None, None)
    assert get_best_parsable_locale(m) == 'C'

    # Test no system

# Generated at 2022-06-12 23:24:09.257128
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    preferences = ['C.utf8', 'C', 'POSIX']
    module = AnsibleModule()
    locale = get_best_parsable_locale(module=module, preferences=preferences)
    assert locale == 'C'

# Generated at 2022-06-12 23:24:18.275452
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    LOCALE_OUTPUT = b'''
C
C.UTF-8
en_US.utf8
es_ES.utf8
'''

    class MockModule(object):
        def get_bin_path(self, tool):
            return 'locale'

        def run_command(self, command, **args):
            return 1, LOCALE_OUTPUT, None

    module = MockModule()
    preferred_locales = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # test that the first available locale is returned
    locale = get_best_parsable_locale(module, preferred_locales)
    assert locale == 'C'

    # test that first specified locale is returned

# Generated at 2022-06-12 23:24:43.498591
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit test for get_best_parsable_locale
    '''

    def run_command(cmd, input_data, check_rc=True):
        '''
            Mock function to simulate run_command
        '''
        if cmd[0] != 'locale':
            raise RuntimeError("Not locale command: %s", to_native(cmd))

        if cmd[1] == '-a' and input_data is None:
            rc = 0
            out = "en_US.utf8\nen_US.utf8\nen_US.utf8\nen_US.utf8\nen_US.utf8"
            err = ''
        elif cmd[1] == '-a' and input_data is not None:
            rc = 0

# Generated at 2022-06-12 23:24:49.037155
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = type('module', (object,), dict(
        get_bin_path=lambda x: None if x is 'locale' else 'locale',
        run_command=lambda x: (
            0, 'C\nen_US.utf8', '') if x == ['locale', '-a'] else (1, '', 'locale bin is missing')
    ))()

    class CheckException(Exception):
        pass

    # test for generic case
    try:
        assert 'C' == get_best_parsable_locale(module)
    except Exception:
        raise CheckException("test_get_best_parsable_locale: test for generic case failed")

    # test for C locale

# Generated at 2022-06-12 23:24:59.685479
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class dummy_Klass(object):
        def __init__(self):
            pass

        def get_bin_path(self, arg):
            if arg == "locale":
                return True
            else:
                return False

        def run_command(self, arg):
            if arg[1] == "-a":
                return 0, "C.UTF-8", None
            else:
                return 1, None, "error"

    m = dummy_Klass()
    try:
        get_best_parsable_locale(m, raise_on_locale=True)
    except RuntimeWarning:
        assert False
    m.run_command = lambda arg: (0, "C.UTF-8", None)

# Generated at 2022-06-12 23:25:11.482046
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import EnvironmentFallback

    class TestModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg, required=False):
            return get_bin_path(arg, required=required, opt_dirs=[])

        def run_command(self, cmd, check_rc=True):
            return 0, '', ''

    assert get_best_parsable_locale(TestModule()) == 'C'

    class FakeModule(object):
        def __init__(self):
            self.params = {}


# Generated at 2022-06-12 23:25:23.139514
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # mock the module we are using
    from ansible.module_utils import basic

    # Load module
    m = basic.AnsibleModule(argument_spec={})

    assert m.get_bin_path('locale') is not None

    # test that we have the right services
    assert get_best_parsable_locale(m) == 'C'

    # test that we have the right services
    assert get_best_parsable_locale(m, preferences=['en_US.utf8', 'en_US.UTF-8']) == 'en_US.utf8'
    assert get_best_parsable_locale(m, preferences=['en_US.UTF-8', 'en_US.utf8']) == 'en_US.UTF-8'

    # invalid service should return None

# Generated at 2022-06-12 23:25:33.908027
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import tempfile
    import textwrap
    import locale
    import datetime
    import os
    import copy

    from units.compat import unittest
    from units.compat.mock import patch
    from ansible.module_utils.basic import AnsibleModule

    class MockModule(object):
        def __init__(self, props, fail=False):
            self._ansible_module = AnsibleModule(
                argument_spec=dict(
                    props=dict(type="dict", required=False),
                ),
                params=props
            )
            self.fail_json = self._ansible_module.fail_json

        def get_bin_path(self, name):
            if name == 'locale':
                return '/usr/bin/locale'

            return None


# Generated at 2022-06-12 23:25:38.460314
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    # Although the locale -a returns fr_FR, it does not exist
    module = AnsibleModule(argument_spec=dict())
    loc = module.get_best_parsable_locale(['en_US.utf8', 'en_US.UTF-8', 'fr_FR.utf8'])

    assert loc == 'en_US.utf8'

# Generated at 2022-06-12 23:25:47.016660
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test method get_best_parsable_locale
    '''

    module = MockModule()
    preferences = ['C.utf8', 'fr_FR.utf8', 'POSIX']
    result = get_best_parsable_locale(module, preferences, raise_on_locale=False)
    assert result == 'C'
    assert module.run.call_count == 1
    assert module.run.call_args[0][0][1] == '-a'
    assert module.get_bin_path.call_count == 1
    assert module.get_bin_path.call_args[0][0] == 'locale'

    module = MockModule()
    preferences = ['C.utf8', 'fr_FR.utf8', 'POSIX']
    result = get_best_pars

# Generated at 2022-06-12 23:25:57.314037
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system import locale_gen
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.common.json_utils import AnsibleJSONEncoder


    def _shell_quote(arg):
        return "'%s'" % os.path.expandvars(arg.replace("'", "'\"'\"'"))

    class _MockedModule(object):

        def __init__(self):
            self.fail_json = Exception

        def run_command(self, args):
            self.assertTrue(isinstance(args, list))
            self.assertEqual(args[0], 'locale')
            return 0, 'foo\nC\n', ''

    module = _MockedModule()


# Generated at 2022-06-12 23:26:00.839972
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.locale import get_best_parsable_locale

    module = AnsibleModule(argument_spec={})
    assert isinstance(get_best_parsable_locale(module), str)

# Generated at 2022-06-12 23:26:34.386391
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # run with no expected preferences
    found = get_best_parsable_locale(module)
    assert found == 'C'

    # run with some expected preferences
    found = get_best_parsable_locale(module, preferences=['en_US'])
    assert found == 'en_US'

# Generated at 2022-06-12 23:26:35.426287
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:26:43.599598
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import _get_module_path

    # Test the I18n functions of the module
    from ansible.module_utils.basic import AnsibleModule, AnsibleModuleError

    check_locale = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    check_locale.run_command = lambda x: (0, 'C de_DE de_DE@euro de_DE.utf8 de_DE.UTF-8 de_DE.UTF8 deutsch german POSIX', '')

    parsable_locale = get_best_parsable_locale(module=check_locale)
    assert parsable_locale == 'C'

    # Test if the locale error is raised

# Generated at 2022-06-12 23:26:52.039063
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Run test for get_best_parsable_locale function
    '''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.module_utils.common.text.converters import to_text

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    # list of locales and their expected results

# Generated at 2022-06-12 23:26:54.675597
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    am = AnsibleModule(argument_spec={})
    found = get_best_parsable_locale(am)
    # right now this is fixed, so we can test it
    assert found == 'C'

# Generated at 2022-06-12 23:27:03.636177
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Verify that the correct locale is returned based on the availability
        of locale preferences.
    '''

    # Use the C locale as a default
    assert get_best_parsable_locale(None) == 'C'

    # No preferences passed
    class MockNull(object):
        def get_bin_path(self, name):
            if name == "locale":
                return "/usr/bin/locale"
            else:
                return None

        def run_command(self, cmd):
            assert cmd == ["/usr/bin/locale", "-a"]
            return 0, "en_US.utf8\nen_US.US-ASCII\nen_US\nC\nPOSIX\n", ""
