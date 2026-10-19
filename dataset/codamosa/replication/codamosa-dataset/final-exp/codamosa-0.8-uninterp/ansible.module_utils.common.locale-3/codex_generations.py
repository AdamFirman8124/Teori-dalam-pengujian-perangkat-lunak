

# Generated at 2022-06-12 23:17:16.014358
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, preferences=['de_AT.utf8']) == 'de_AT.utf8'
    assert get_best_parsable_locale(module, preferences=['de_AT.utf8', 'BAD_LOCALE_NAME']) == 'de_AT.utf8'
    assert get_best_parsable_locale(module, preferences=['BAD_LOCALE_NAME']) == 'C'

# Generated at 2022-06-12 23:17:25.266284
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # template taken from ansible test/units/module_utils/network/common/utils/test.py
    # and modified to use get_best_parsable_locale()
    if sys.version_info[0] >= 3:
        class MockModule(collections.Mapping):

            def __getitem__(self, key):
                return self.__dict__[key]

            def __setitem__(self, key, value):
                self.__dict__[key] = value

            def __iter__(self):
                return iter(self.__dict__)

            def __len__(self):
                return len(self.__dict__)

            def __delitem__(self, key):
                del self.__dict__[key]

        module = MockModule()

# Generated at 2022-06-12 23:17:32.554193
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import unittest
    import os

    sys.path.append(os.getcwd())
    # prevent module import errors
    sys.modules['ansible.module_utils.basic'] = None
    sys.modules['ansible.module_utils.facts'] = None

    from ansible import context
    from ansible.errors import AnsibleError
    from ansible.module_utils.facts.system import locale_info

    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_count = 0

        def get_bin_path(self, name, required=False, opt_dirs=[], consider_installed=True):
            return name


# Generated at 2022-06-12 23:17:43.650414
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import sys
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    class AnsibleModuleTest(AnsibleModule):
        def __init__(self, *args, **kwargs):
            AnsibleModule.__init__(self, *args, **kwargs)
            sys.modules['__main__'] = sys.modules[__name__]
            self.exit_json = lambda **a: 0

    # If locale is not available on system, it should return 'C' locale
    m = AnsibleModuleTest(dict(), dict())
    assert get_best_parsable_locale(m) == 'C'

    # If locale is available, it should return the first matched item of preferences

# Generated at 2022-06-12 23:17:51.921470
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    local_preferences = ['POSIX', 'C', 'C.UTF-8', 'EN_US.UTF-8']
    assert(get_best_parsable_locale(local_preferences) == 'C')

    local_preferences = ['EN_US.UTF-8', 'POSIX', 'C', 'C.UTF-8']
    assert(get_best_parsable_locale(local_preferences) == 'EN_US.UTF-8')

    local_preferences = ['EN_US.UTF-8', 'POSIX', 'C', 'C.UTF-8']
    assert(get_best_parsable_locale(local_preferences, raise_on_locale=True) == 'EN_US.UTF-8')


# Generated at 2022-06-12 23:18:03.137418
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    import pytest

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    from ansible.module_utils.common.locales import get_best_parsable_locale

    # import module snippets
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector

    # Main function to test against
    def main():
        module = AnsibleModule(argument_spec={
            'test_variable': {'type': 'str', 'default': 'default value'},
        })

        test_case = module.params['test_variable']

        # Run test case

# Generated at 2022-06-12 23:18:10.802749
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test if in the case when "locale -a" command
    returns both the list and single preferred locale
    '''

    class FakeModule:
        def get_bin_path(self, tool):
            return tool

        def run_command(self, cmd):
            if cmd == ['locale', '-a']:
                return (0, 'en_US C C.utf8', '')

    fake_module = FakeModule()
    found = get_best_parsable_locale(fake_module)

    assert found == 'C.utf8'



# Generated at 2022-06-12 23:18:13.583493
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(supports_check_mode=True)
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:18:21.119168
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # The get_bin_path function normally returns an AnsibleModule instance, but
    # for this unit test we can easily mock it so that it returns the string
    # we want to test.
    class AnsibleModule():
        def run_command(self, cmd):
            if cmd == ['locale', '-a'] and cmd == ['locale', '-a']:
                return (0, 'C.UTF-8\nen_US.UTF-8\nen_US.UTF8', '')
            elif not cmd == ['locale', '-a'] and cmd == ['locale', '-a']:
                return (0, 'C.UTF-8\nen_US.UTF8', '')

# Generated at 2022-06-12 23:18:31.981617
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:18:45.599788
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    module = AnsibleModule(argument_spec={})

    for test in [
        (None, "POSIX", []),
        (None, "C", ['POSIX.utf8', 'en_US.utf8']),
        (None, "en_US.utf8", ['POSIX.utf8']),
        (None, "POSIX", ['POSIX.utf8']),
    ]:
        exception_raised = False
        msg = None

        try:
            locale = get_best_parsable_locale(module, test[0], raise_on_locale=True)
            assert locale == test[1]
        except Exception as e:
            exception_raised = True


# Generated at 2022-06-12 23:18:55.906425
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Tests for the get_best_parsable_locales() function.
    '''
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils.common._collections_compat import Mapping

    module = AnsibleModule(argument_spec=dict())

    module.get_bin_path = lambda x: None
    assert get_best_parsable_locale(module) == 'C'

    count = [0]

    def get_bin_path(tool):
        count[0] += 1
        if count[0] == 1:
            return None
        elif count[0] == 2:
            return '/bin/locale'
        elif count[0] == 3:
            return 0
        elif count[0] == 4:
            return 0


# Generated at 2022-06-12 23:19:02.543687
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale() == 'C'
    assert get_best_parsable_locale(preferences=['en_US.utf8', 'en_US.utf-8']) == 'C'
    assert get_best_parsable_locale(preferences=['C']) == 'C'
    assert get_best_parsable_locale(preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:19:13.028697
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    import os
    try:
        os.remove('/tmp/get_best_parsable_locale')
    except:
        pass

    def test_module(preferences=None):
        """ utility to return an ansible module to run commands """

        # Create a new module object
        module = AnsibleModule(
            argument_spec=dict(),
        )

        # Run the locale module
        result = get_best_parsable_locale(module, preferences)

        # Save the results to a file
        with open('/tmp/get_best_parsable_locale', 'w') as fd:
            fd.write(result)

        module.exit_json(msg="success!")

    # Create the module test function

# Generated at 2022-06-12 23:19:19.625370
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # Test one command path
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

    # Test another command path
    module.run_command = lambda x: (0, '', '')
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'

    # Test no command path (first file)
    module.run_command = \
        lambda x: (1, '', 'Unable to get locale information, rc=1: ')

# Generated at 2022-06-12 23:19:31.477000
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Set up fake AnsibleModule class for testing
    class FakeModule():
        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, bin_name):
            return bin_name

        def run_command(self, cmd):
            out = None
            err = "not really an error"
            rc = 0

            if 'locale -a' in cmd:
                out = "C\nC.utf8\nPOSIX\nen_US.utf8"
            elif 'locale' in cmd:
                out = "LANG=en_US.utf8"
            elif 'export' in cmd:
                pass
            else:
                rc = 1

            return rc, out, err

    # Test: Return the first matched preferred locale or 'C' which is the default

# Generated at 2022-06-12 23:19:41.446811
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class AnsibleModule:
        def __init__(self, params):
            self.params = params
            self.fail_json = None
            self.exit_json = None
        def get_bin_path(self, binary):
            return "/bin/{0}".format(binary)
        def run_command(self, command):
            return (0, "en_US.utf8\nPOSIX\nC.utf8\n", None)
    am = AnsibleModule({"faillocale": True})
    assert get_best_parsable_locale(am) == 'C.utf8'
    am = AnsibleModule({"faillocale": True, "preferences": ['POSIX', 'C', 'C.utf8']})

# Generated at 2022-06-12 23:19:44.725161
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    locale = get_best_parsable_locale(module)

    assert locale in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

# Generated at 2022-06-12 23:19:51.341821
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import unittest
    import sys
    import os
    import locale
    import platform

    # Required for mocking the AnsibleModule
    sys.modules['ansible'] = __import__('ansible')
    sys.modules['ansible.module_utils.basic'] = __import__('ansible.module_utils.basic')
    sys.modules['ansible.module_utils.six'] = __import__('ansible.module_utils.six')
    if sys.version_info[0] == 2:
        # Python 2.7
        from ansible.module_utils.basic import AnsibleModule as AM
    else:
        # Python 3.5
        from ansible.module_utils.basic import AnsibleModule as AM
    from ansible.module_utils import basic


# Generated at 2022-06-12 23:19:59.532492
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Create a module instance
    import tempfile
    temp_dir = tempfile.mkdtemp()
    m = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
        bypass_checks=True
    )
    m.exit_json = lambda **kwargs: kwargs
    m.fail_json = lambda msg: msg

    # Make a fake locale binary
    with open(os.path.join(temp_dir, "locale"), "w") as f:
        f.write("#!/usr/bin/python\n")
        f.write("import sys\n")
        f.write("if '-a' in sys.argv:\n")
        f.write("    if sys.stdout.isatty():\n")

# Generated at 2022-06-12 23:20:11.311431
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ['C.utf8', 'en_US.utf8']) == 'C'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'C.utf8']) == 'en_US.utf8'
    assert get_best_parsable_locale(None, ['blah_blah_Blah', 'C.utf8']) == 'C'
    assert get_best_parsable_locale(None, ['C.utf8', 'blah_blah_Blah']) == 'C'

# Generated at 2022-06-12 23:20:22.469060
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    am = AnsibleModule({})
    am.get_bin_path = lambda x: x
    am.run_command = lambda x: (0, "fake_locale_a\nfake_locale_b\nC", None)

    prefs = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    assert get_best_parsable_locale(am, prefs) == 'C'

    am.run_command = lambda x: (0, "C.utf8\nfake_locale_a\nfake_locale_b", None)

    assert get_best_parsable_locale(am, prefs) == 'C.utf8'


# Generated at 2022-06-12 23:20:33.581276
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Load the bare module for testing
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )
    # Expected to return 'C' as none of preferences are available
    assert get_best_parsable_locale(module, ['fr_FR', 'fr_FR.iso88591'], raise_on_locale=True) == 'C'
    assert get_best_parsable_locale(module, ['fr_FR', 'fr_FR.iso88591'], raise_on_locale=False) == 'C'
    # Expected to return 1st preference
    assert get_best_parsable_locale(module, ['C', 'C.utf8'], raise_on_locale=True) == 'C'
    assert get

# Generated at 2022-06-12 23:20:39.682584
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, []) == 'C'
    assert get_best_parsable_locale(None, ['POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'C']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'C', 'C']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'C', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'C', 'POSIX', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:20:50.506184
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    test_module = AnsibleModule({'prompt': None})
    test_module.fail_json = lambda *args, **kwargs: None
    test_module.get_bin_path = lambda *args: True
    test_module.run_command = lambda *args: [0, 'foo', '']

    # Case 0: neither locale nor english is available
    test_module.run_command = lambda *args: [0, '', '']
    assert get_best_parsable_locale(test_module) == 'C'

    # Case 1: neither locale nor english is available, exception raised
    test_module.run_command = lambda *args: [0, '', '']
    assert get_best_parsable_locale(test_module, raise_on_locale=True) == 'C'

    # Case

# Generated at 2022-06-12 23:20:57.897589
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import base64
    from ansible.module_utils.basic import AnsibleModule
    fake_module = AnsibleModule(argument_spec=dict())
    pref_list = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    locale_list = "C\nen_US.utf8\nPOSIX"
    fake_module.run_command = lambda args, check_rc=True: (0, base64.b64decode(locale_list), '')
    assert get_best_parsable_locale(fake_module) == 'en_US.utf8'
    fake_module.run_command = lambda args, check_rc=True: (1, None, '')
    assert get_best_parsable_locale(fake_module, raise_on_locale=True)

# Generated at 2022-06-12 23:21:09.172032
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class DummyModule(object):
        def get_bin_path(self, cmd):
            return 'locale'

        def run_command(self, cmd):
            if cmd == ['locale', '-a']:
                return 0, """C
C.UTF-8
en_US.utf8
en_US
es_MX.utf8
es_MX
POSIX
""", None
            elif cmd == ['locale', '-a', '--no-archive']:
                return 0, """C
C.UTF-8
en_US.utf8
en_US
es_MX.utf8
es_MX
POSIX
""", None
            elif cmd == ['locale', '-a', '--no-archive']:
                return 0, """C
en_US.utf8
en_US""",

# Generated at 2022-06-12 23:21:17.315119
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import sys

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.process import get_bin_path
    from ansible.utils.display import Display
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    class TestAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(TestAnsibleModule, self).__init__(*args, **kwargs)
            self.logger = Display()
            self.logger.verbosity = 0

    # get_bin_path needs to be mocked out because we test in a git working tree
    from mock import patch
    from mock import MagicMock
    from mock import Mock

   

# Generated at 2022-06-12 23:21:20.053560
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    m = AnsibleModule(
        argument_spec=dict(),
    )

    assert get_best_parsable_locale(m) == 'C'

# Generated at 2022-06-12 23:21:31.120422
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    locale = get_best_parsable_locale(ansible.module_utils.basic._AnsibleModule(argument_spec={}))
    assert locale in ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

    # Test a preference list
    locale = get_best_parsable_locale(ansible.module_utils.basic._AnsibleModule(argument_spec={}), ['C.utf8', 'en_US.utf8', 'POSIX', 'C'])
    assert locale in ['C.utf8', 'en_US.utf8', 'POSIX', 'C']

    # Test a preference list with no matches

# Generated at 2022-06-12 23:21:48.997517
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Test 1: Ensure 'C' locale is returned when list of locale preferences is None
    assert get_best_parsable_locale(None, None) == 'C'

    # Test 2: Ensure 'C' locale is returned when 'locale' command is not present in system
    # class MockModule(object):
    #     def __init__(self, out, rc):
    #         self.out = out
    #         self.rc = rc
    #
    #     def get_bin_path(self, item):
    #         return None
    #
    #     def run_command(self, args):
    #         return [self.rc, self.out, '']
    #
    # test_module = MockModule('/usr/bin:/usr/sbin', 0)
    # assert get_best_parsable

# Generated at 2022-06-12 23:21:59.834217
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    def run_get_best_parsable_locale(preferences, availables, expected):
        # Mock module
        class Module(object):
            def get_bin_path(self, name):
                if name == 'locale':
                    return 'locale'
                raise RuntimeWarning("Could not find '%s' tool" % (name))
            def run_command(self, cmd):
                assert cmd == ['locale', '-a']
                return (0, availables, '')
        module = Module()

        # Run function
        best_locale = get_best_parsable_locale(module, preferences=preferences)
        assert best_locale == expected

    # Test preference list is empty
    availables = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']

# Generated at 2022-06-12 23:22:03.856152
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    preferences = ['en_US.utf8', 'en_CA.utf8']
    get_best_parsable_locale = lambda: get_best_parsable_locale(preferences)

    assert get_best_parsable_locale() == 'en_US.utf8'

# Generated at 2022-06-12 23:22:10.319990
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = type('Module', (object,), {
        'get_bin_path': lambda self, command: command,
        'run_command': lambda self, command, check_rc=True: (0, command[1], None),
    })()
    assert get_best_parsable_locale(module) == 'C'
    module.run_command = lambda self, command, check_rc=True: (1, command[1], None)
    assert get_best_parsable_locale(module, raise_on_locale=True) == 'C'
    module.run_command = lambda self, command, check_rc=True: (0, ['C.utf8', 'en_US.utf8', 'C', 'POSIX'], None)

# Generated at 2022-06-12 23:22:18.010333
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    def _get_bin_path(exc):
        return 'locale'

    m = AnsibleModule(argument_spec={})
    m.get_bin_path = _get_bin_path

    def _run_command(*args, **kwargs):
        if args[1][1] == '-a':
            return (0, 'C', '')
        return (1, '', '')

    m.run_command = _run_command
    assert get_best_parsable_locale(m) == 'C'

    def _run_command(m, *args, **kwargs):
        if args[1][1] == '-a':
            return (0, 'C en_US.utf8 C.utf8', '')

# Generated at 2022-06-12 23:22:19.009875
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert 'C' == get_best_parsable_locale()

# Generated at 2022-06-12 23:22:27.362628
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import subprocess
    import sys

    class AnsibleModule:

        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, name):
            if name.lower() == 'locale':
                return subprocess.__file__
            return sys.executable

        def run_command(self, cmd, *args, **kwargs):
            stdout = b''
            stderr = b''
            rc = 0
            if cmd[0] == sys.executable and cmd[1] == '-c':
                if cmd[2] == 'print("en_US.utf8\nen_US.UTF-8\nC")':
                    stdout = b'en_US.utf8\nen_US.UTF-8\nC'

# Generated at 2022-06-12 23:22:30.903575
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule, env_fallback
    m = AnsibleModule(argument_spec={}, supports_check_mode=True)
    locale = get_best_parsable_locale(m, preferences=['C', 'POSIX'])

    # test we have 'C'
    assert locale == 'C'

# Generated at 2022-06-12 23:22:37.907526
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    import ansible.module_utils.basic as ansible_basic
    from ansible.module_utils.common.collections import ImmutableDict

    class TestModule(object):
        '''Test module class'''

        def __init__(self, params):
            self.params = ImmutableDict(params)
            self.ansible_facts = ImmutableDict()

        def exit_json(self, **kwargs):
            '''Dummy exit_json method'''
            self.ansible_facts = ImmutableDict(kwargs)

        def get_bin_path(self, *args, **kwargs):
            '''Dummy get_bin_path method'''
            return self.params['locale']


# Generated at 2022-06-12 23:22:41.624650
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    assert get_best_parsable_locale(None, preferences) == 'C'



# Generated at 2022-06-12 23:22:58.263891
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import locale

    mod = AnsibleModule(
        argument_spec={},
        supports_check_mode=False
    )

    # Test default list of preferences and what happens when best isn't found
    assert locale.get_best_parsable_locale(mod, preferences=None) == 'C'

    # Test when best is found, when there is a warning and when the locale command isn't found
    assert locale.get_best_parsable_locale(mod, preferences=['C', 'C.utf8']) == 'C'

    assert locale.get_best_parsable_locale(mod, preferences=['C', 'C.utf8']) == 'C'

    assert locale.get_best_parsable_locale

# Generated at 2022-06-12 23:23:04.802147
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # It's difficult to unit test this function because it is inherently
    #  dependent on the environment the test is running in. It will return
    #  a best guess for a *parsable* locale given a list of preferred
    #  locales.
    # The function needs to be able to access locale, which is a system tool
    #  so we're going to use a mocked-up JSON data file with a few sample
    #  locale lists (contrived and extracted from Ubuntu)
    from ansible.module_utils import basic
    import json
    import os
    import sys

    FIXTURE_PATH = os.path.join(os.path.dirname(__file__), '..', 'unit', 'modules', 'files', 'locale_fixtures.json')

# Generated at 2022-06-12 23:23:14.144994
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    dummy_module = AnsibleModule()

    # Test we do get 'C' back when locale is not installed
    assert get_best_parsable_locale(dummy_module) == 'C'

    # Test that we do get the best locale
    dummy_module.get_bin_path = lambda x: '/usr/bin/locale'
    dummy_module.run_command = lambda x: (0, 'C\nen_US.utf8\nen_US.utf\nen_US.iso885915@euro\nen_US', '')

    assert get_best_parsable_locale(dummy_module) == 'C'

# Generated at 2022-06-12 23:23:21.356289
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict(), supports_check_mode=False)

    # Test with no locale tool
    module.get_bin_path = lambda x: None

    try:
        get_best_parsable_locale(module, raise_on_locale=True)
        raise AssertionError("Expected an exception when 'locale' tool not found")
    except RuntimeError:
        pass

    # Test with empty output
    empty = module.run_command = lambda x: (0, '', '')
    module.get_bin_pa

# Generated at 2022-06-12 23:23:26.960821
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # no preference, expect to get 'C' locale
    assert get_best_parsable_locale(None, None) == 'C'

    # preference is en_US.utf8, expect to get 'en_US.utf8' locale
    assert get_best_parsable_locale(None, ['en_US.utf8']) == 'en_US.utf8'

    # preference is en_US.utf8, expect to get 'C' locale
    assert get_best_parsable_locale(None, ['en_US.utf8']) == 'C'

# Generated at 2022-06-12 23:23:34.464806
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    parser = argparse.ArgumentParser()
    parser.add_argument('--locale')
    args = parser.parse_args()

    if not args.locale:
        raise Exception("You must provide --locale to test")

    module = namedtuple('Module', 'get_bin_path run_command')

    def my_run_command(cmd, cwd=None, data=None, binary_data=False):
        return (0, args.locale, '')

    module.run_command = my_run_command

    def my_get_bin_path(cmds, required=True):
        return cmds

    module.get_bin_path = my_get_bin_path

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    locale = get_best

# Generated at 2022-06-12 23:23:41.430467
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class Module:

        def __init__(self):
            self.rc = 0
            self.called = []
            self.err = ''
            self.out = ''

        def get_bin_path(self, name):
            self.called.append(name)
            return '/tools/locale'

        def run_command(self, items):
            self.called.append(items)
            return self.rc, self.out, self.err

    # Test normal output
    M = Module()
    M.out = 'C'
    assert get_best_parsable_locale(M) == 'C'
    assert not M.err
    assert M.rc == 0
    assert M.called

    # Test empty output
    M = Module()
    M.rc = 1
    assert get_best_parsable

# Generated at 2022-06-12 23:23:43.083745
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    locale = get_best_parsable_locale(module=module)
    assert "C" in locale

# Generated at 2022-06-12 23:23:49.618130
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Get the real get_bin_path() so we can inject some fake paths
    from ansible.module_utils.common.process import get_bin_path

    # Fake paths injected into PATH
    paths = [
        'fake_path/locale',  # fake path to a locale binary
        'fake_path/bin/locale',  # fake path that does not exist
        '/usr/bin/locale'  # real locale path
    ]

    # Patch out get_bin_path() with our fake paths
    def fake_get_bin_path(arg, required=True):
        return paths.pop()

    AnsibleModule.get_bin_path = fake_get_bin_path

    # Mock a module with fake output from locale -a
    module = AnsibleModule

# Generated at 2022-06-12 23:23:59.173882
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import load_platform_subclass
    module = load_platform_subclass(AnsibleModule)()
    module.get_bin_path = lambda *args, **kwargs: '/usr/bin/locale'
    module.run_command = lambda *args, **kwargs: (0, 'C C.utf8 POSIX en_US en_US.utf8', '')
    assert get_best_parsable_locale(module) == 'C.utf8'
    assert get_best_parsable_locale(module, preferences=['POSIX']) == 'POSIX'

# Generated at 2022-06-12 23:24:14.360715
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:24:19.450928
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    m = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict()
    )

    assert get_best_parsable_locale(m, ['en_US.utf8', 'en_US', 'C']) == 'en_US.utf8'
    assert get_best_parsable_locale(m, ['en_US']) == 'C'

# Generated at 2022-06-12 23:24:29.138418
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    # Test when locale command is not present
    assert get_best_parsable_locale(module) == 'C'

    # Test when preferences is None
    assert get_best_parsable_locale(module, preferences=None) == 'C'

    # Test when locale is present with preferences
    module.run_command = lambda args, check_rc=True: (0, 'C.utf-8\nc\n', '')
    assert get_best_parsable_locale(module, preferences=['C.utf-8', 'c']) == 'C.utf-8'

    module.run_command = lambda args, check_rc=True: (0, 'C.utf-8\nc\n', '')
   

# Generated at 2022-06-12 23:24:36.601863
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, None) == 'C'

    assert get_best_parsable_locale(None, ['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'C']) == 'POSIX'
    assert get_best_parsable_locale(None, ['en_US.utf8', 'POSIX', 'C']) == 'en_US.utf8'

# Generated at 2022-06-12 23:24:46.040835
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """ Unit test to verify get_best_parsable_locale """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    preferences_out = [preferences[0], preferences[2], preferences[3]]

    # Test where locale is not installed
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x: (0, "", "")
    found = get_best_parsable_locale(module, preferences)

    assert found == 'C'

    # Test where locale exists and returns successfully
    module2 = AnsibleModule(argument_spec = {})

    module2

# Generated at 2022-06-12 23:24:58.037399
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from collections import namedtuple
    from ansible.module_utils.basic import AnsibleModule

    DummyModule = namedtuple('Module', ('get_bin_path', 'run_command'))

    def get_bin_path(name):
        return '/bin/%s' % name

    def run_command(cmd):
        if cmd[1] == '-a':
            ret = (0, 'C\nen_US.utf8\nen_GB.utf8\n', '')
        return ret

    module = DummyModule(get_bin_path, run_command)

    ret = get_best_parsable_locale(module)
    assert ret == "C"

    ret = get_best_parsable_locale(module, ['en_GB.utf8'])

# Generated at 2022-06-12 23:25:03.936236
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class FakeModule(object):
        def get_bin_path(self, command, required=False):
            return '/bin/cmd'

        def run_command(self, command):
            return 0, 'locale_output', ''

    module = FakeModule()
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:25:13.790789
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    assert module.get_bin_path("locale")

    # Test the default order of locales
    assert 'en_US.utf8' == get_best_parsable_locale(module)

    # Test the orders in which we are asking for
    assert 'C' == get_best_parsable_locale(module, ['foobar', 'C', 'POSIX'])

    assert 'POSIX' == get_best_parsable_locale(module, ['foobar_blah', 'POSIX'])

    assert 'C.utf8' == get_best_parsable_locale(module, ['C', 'POSIX', 'C.utf8'])



# Generated at 2022-06-12 23:25:25.438310
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.process import get_bin_path

    class MockAnsibleModule(object):
        def __init__(self, instance):
            self.instance = instance

        def get_bin_path(self, name):
            if name == 'locale':
                return '/usr/bin/locale'

        def run_command(self, cmd):
            if cmd == ['/usr/bin/locale', '-a']:
                return (0, 'en_GB.utf8\nen_GB.UTF-8\nen_US.utf8\nen_US.UTF-8\nPOSIX\nC\nzh', '')
            else:
                raise Exception('Bad command')

    module = MockAnsibleModule('instance')

# Generated at 2022-06-12 23:25:36.188816
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()

    # Mock the locale -a command output
    class Result:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

    # Test output of the run_command function
    class RunResult:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

    # Mock the run_command function

# Generated at 2022-06-12 23:26:00.102023
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Mock base class
    class TestModule(object):
        def __init__(self, *args, **kwargs):
            pass

        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/locale'

        def run_command(self, *args, **kwargs):
            return (0, 'C\nC.utf8\nen_US.utf8\nen_US.utf8', None)

    test_module = TestModule()

    # Test all langauges none given
    assert get_best_parsable_locale(test_module, None) == 'C.utf8'

    # Test french given

# Generated at 2022-06-12 23:26:08.818365
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system.locale import get_best_parsable_locale
    test_module = object()
    test_module.get_bin_path = lambda strings: strings.replace('locale','/usr/bin/locale')
    test_module.run_command = lambda args: (0, 'C\nen_US.utf8\nen_US\nen_US.utf-8\nen_US@rg\nen_US.UTF-8\nen_US.UTF8\nen_US.ISO8859-1\nen_US.ISO8859-15\nen_GB.UTF-8', '')
    assert get_best_parsable_locale(test_module) == 'C.utf8'

# Generated at 2022-06-12 23:26:18.807457
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    test_cases = [
        ((['C.utf8', 'en_US.utf8', 'C', 'POSIX'],), 'C'),
        ((['C.utf8', 'POSIX', 'C', 'en_US.utf8'],), 'C'),
        ((['en_US.utf8', 'POSIX', 'C', 'C.utf8'],), 'en_US.utf8'),
        ((['en_US.utf8', 'POSIX', 'C', 'C.utf8'],), 'en_US.utf8')
    ]

    for inargs, expected in test_cases:
        assert expected == get_best_parsable_locale(*inargs)

if __name__ == '__main__':
    test_get_best_parsable_locale()

# Generated at 2022-06-12 23:26:21.819433
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale({'get_bin_path': lambda x: 'true'}, preferences=['C']) == 'C'
    assert get_best_parsable_locale({'get_bin_path': lambda x: 'true'})

# Generated at 2022-06-12 23:26:33.531795
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    import os

    class TestModule(AnsibleModule):
        ''' Class to test get_best_parsable_locale '''
        def get_bin_path(self, arg, required=False, opt_dirs=()):
            return 'locale'


# Generated at 2022-06-12 23:26:41.688360
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class FakeModule(object):
        def get_bin_path(self, binary):
            return binary
        def run_command(self, binary):
            if binary[0] == '/bin/sh':
                return 0, 'C.utf8\nC.utf8', ''
            if binary[0] == 'locale':
                return 0, 'C.utf8\nC\nen_US.utf8\nPOSIX', ''
            return 1, '', ''

    fake_module = FakeModule()

    found_locale = get_best_parsable_locale(fake_module)
    assert found_locale == 'C.utf8'

    # test with a preference of POSIX. POSIX is available in the available output.

# Generated at 2022-06-12 23:26:48.291276
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.common.collections import ImmutableDict
    import pytest
    from ansible.module_utils import basic

    m = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # Make a dict of the modules method calls, returning a string.
    m.run_command = lambda args, check_rc=True: ('', '', 0)
    m.get_bin_path = lambda x: ''

    # check for bad input
    with pytest.raises(RuntimeWarning):
        assert get_best_parsable_locale(m)

    # check for any input
    m.get_bin_path = lambda x: '/usr/bin/locale'
    out1 = get_best_parsable_locale(m)

# Generated at 2022-06-12 23:26:56.835952
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.utils.hashing import md5s
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    best_locale = get_best_parsable_locale(module)

    # check that it returns a string
    assert best_locale is not None and len(best_locale) > 0

    # check that we get a non-french locale
    best_locale = get_best_parsable_locale(module, preferences=['fr_FR.utf8', 'C.utf8'])
    assert 'fr_FR' not in best_locale

    # check that we get an english locale if the platform is configured with it

# Generated at 2022-06-12 23:27:05.713193
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # Dummy classes to simulate AnsibleModule
    class DummyModule:
        def __init__(self, raise_on_locale):
            self.raise_on_locale = raise_on_locale
            self.rc = 0
            self.out = ''
            self.err = ''

        def get_bin_path(self, _):
            return ''

        def run_command(self, cmd):
            return self.rc, self.out, self.err

    class DummyAnsibleModule:
        def __init__(self, locale):
            self.params = {}
            self.module = DummyModule(locale)

    # Test case #1: Output from 'locale -a' is empty, function should return 'C'
    dummy_ansible_module = DummyAnsibleModule(False)
   