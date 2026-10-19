

# Generated at 2022-06-12 23:17:14.755847
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    if module.get_bin_path('locale'):
        locale = get_best_parsable_locale(module, ['C.utf8'])
        assert locale == 'C.utf8'
    else:
        assert get_best_parsable_locale(module, ['C.utf8']) == 'C'

# Generated at 2022-06-12 23:17:23.936562
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import mock

    m = mock.Mock()
    m.get_bin_path.return_value = 'locale'
    m.run_command.return_value = (0, 'C C.UTF-8 fr_FR.UTF-8 POSIX', '')

    # nopreferences
    assert get_best_parsable_locale(m) == 'C'

    # With preferences
    preferences = ['C.utf8', 'en_US.utf8', 'POSIX']
    assert get_best_parsable_locale(m, preferences=preferences) == 'POSIX'

    # raise on locale not present
    m.run_command.return_value = (1, '', 'error')

# Generated at 2022-06-12 23:17:27.428641
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system.setup import _check_locale_facts
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())
    assert _check_locale_facts(module, get_best_parsable_locale(module))

# Generated at 2022-06-12 23:17:33.142536
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # using a real AnsibleModule instance, so we can test the CLI execution
    test_module = AnsibleModule(argument_spec={})

    # 'C' must always work as a default as it's always on Linux systems
    assert 'C' == get_best_parsable_locale(test_module)

    # a specific locale
    assert 'en_US.utf8' == get_best_parsable_locale(test_module, ['en_US.utf8'])

    # a specific locale not available
    assert 'C' == get_best_parsable_locale(test_module, ['xx_XX.utf8'])

    # 3 existing locales in a row
    assert 'C.utf8' == get_best_parsable_locale

# Generated at 2022-06-12 23:17:44.087436
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # We actually call get_bin_path() in order to avoid having to mock it
    # ourselves, which would be complex. It's the only AnsibleModule method
    # called by the function, so it's the only one we need to mock.
    import ansible.module_utils.basic

    # ansible.module_utils.basic.AnsibleModule.get_bin_path()
    # returns an executable from PATH that corresponds to name
    # or None if no executable is found.
    def mock_get_bin_path(name):
        if name == 'locale':
            return '/usr/bin/locale'
        else:
            raise AssertionError("unexpected call to AnsibleModule.get_bin_path({!r})".format(name))

    # ansible.module_utils.basic.AnsibleModule.run_

# Generated at 2022-06-12 23:17:50.521743
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module) == 'C'  # default locale
    assert get_best_parsable_locale(module, ['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(module, ['en_US.utf8', 'C.utf8', 'C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(module, ['en_US.utf8']) == 'C'
    assert get_best_parsable_locale(module, ['POSIX']) == 'C'


# Generated at 2022-06-12 23:17:51.839364
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    expected_return = 'C'
    assert expected_return == get_best_parsable_locale()

# Generated at 2022-06-12 23:18:03.039723
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """
    Function to unit test function get_best_parsable_locale
    """

    from ansible.module_utils.basic import AnsibleModule

    def mock_run_command(module, cmd):
        if cmd[0] in ['echo', 'locale']:
            if cmd == ['echo', '$LOCALE']:
                return (0, '', '')
            if cmd == ['locale', '-a']:
                return (0, 'C\nPOSIX\nen_US.utf8\nC.utf8\n', '')
        else:
            return (256, '', '')

    module = AnsibleModule(run_command=mock_run_command, check_invalid_arguments=False)


# Generated at 2022-06-12 23:18:06.664085
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.module_utils import get_best_parsable_locale
    from ansible.module_utils.pycompat24 import get_exception
    import sys

    # Create a fake AnsibleModule class with a fake run_command
    class TestingAnsibleModule(AnsibleModule):
        def __init__(self, argument_spec, bypass_checks=False, no_log=True,
                     check_invalid_arguments=True, mutually_exclusive=None,
                     required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_check_mode=False):
            self.params = {}

# Generated at 2022-06-12 23:18:16.345189
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible import module_utils

    # test defaults
    mod = module_utils.basic.AnsibleModule(
        argument_spec={}
    )

    rc, out, err = mod.run_command(['locale', '-a'])
    if rc != 0:
        raise RuntimeError("locale -a failed: %s" % to_native(err))

    # filter out non-utf8
    langs = [x for x in out.split() if x.endswith('.utf8') and x.split('.')[0] != 'C']

    # we expect it to return the first non-C UTF-8 locale we find
    if langs:
        assert get_best_parsable_locale(mod) in langs

    # test it finds the first preferred locale in the list.
    # NOTE

# Generated at 2022-06-12 23:18:31.580769
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        If module_utils.basic.get_best_parsable_locale() fails for any reason
        it should return 'C'
    '''

    class FakeModule(object):
        '''
            This module is a stand in for AnsibleModule
        '''

        def __init__(self):
            self.rc = 0
            self.stdout = None
            self.stderr = None

        def run_command(self, cmd):
            '''
                this is an override of AnsibleModule.run_command(), it will
                only return the values set by set_results()
            '''
            return self.rc, self.stdout, self.stderr


# Generated at 2022-06-12 23:18:33.891546
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({})

    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:18:42.813076
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    def run_command(module, cmd, check_rc=True):
        fake_rc = 0
        fake_out = ''
        fake_err = ''

        if cmd == [locale, '-a']:
            if 'C' in cmd[2]:
                fake_out = 'C\nC.utf8'
            elif 'POSIX' in cmd[2]:
                fake_out = 'POSIX\nC.utf8'
            elif 'C.utf8' in cmd[2]:
                fake_out = 'POSIX\nC.utf8'
            elif 'en_US.utf8' in cmd[2]:
                fake_out = 'POSIX\nC.utf8\nen_US.utf8'
        else:
            raise RuntimeWarning('Unsupported command: %s' % cmd)

       

# Generated at 2022-06-12 23:18:52.959920
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale
    import os
    import shutil
    import tempfile
    module = AnsibleModule(argument_spec={})

    tmp_dir = tempfile.mkdtemp()
    test_path = os.path.join(tmp_dir, 'test')
    with open(test_path, 'w') as fn:
        fn.write("#!/bin/sh\n")
        fn.write("echo 'en_US.utf8'\n")
        os.chmod(test_path, 0o755)

    os.environ["PATH"] = "{0}:{1}".format(tmp_dir, os.environ["PATH"])

    best_locale = get

# Generated at 2022-06-12 23:19:02.963419
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    def mock_get_bin_path(module, bin_name, required=False):
        return bin_name

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import BytesIO

    class MockModule(AnsibleModule):
        def __init__(self):
            pass
        def run_command(self, cmd):
            if cmd[1] == '-a':
                self.out = BytesIO(b"C\nen_US.utf8\nC.utf8")
                self.rc = 0
            else:
                self.rc = 0
            return (self.rc, self.out, self.err)

    m = MockModule()
    # Monkey patch the module to get get_bin_path
    m.get_bin_path = mock_get_bin

# Generated at 2022-06-12 23:19:13.434164
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # This is a mock AnsibleModule
    class _AnsibleModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, tool, required=True):
            return tool

        def run_command(self, cmd, check_rc=True):
            import subprocess
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = proc.communicate()
            return proc.returncode, stdout, stderr

    am = _AnsibleModule()

    # We don't really have any good way of knowing what locales are installed
    # on the system, so we can't test last two cases.
    # Case 1: Both C and C.UTF-8 are

# Generated at 2022-06-12 23:19:25.410251
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.common.sys_info import get_distribution

    module = basic.AnsibleModule(
        argument_spec=dict(
            locale=dict(type='str', default=None),
        )
    )

    locale_path = get_bin_path('locale')
    if locale_path is None:
        return

    distribution = get_distribution().lower()
    if distribution in ('centos', 'scientificlinux'):
        preferences = ['C.utf8', 'C']
    elif distribution == 'ubuntu':
        preferences = ['C.utf8', 'C', 'en_US.utf8', 'en_US']

# Generated at 2022-06-12 23:19:36.774552
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    # Test if locale -a fails
    module = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(module, preferences=['C.utf8', 'en_US.utf8', 'C', 'POSIX']) == 'C'

    # Test if locale -a succeeds with preference
    module.run_command = lambda args: (0, 'C C.UTF-8 en_US.utf8 POSIX\n', '')
    assert get_best_parsable_locale(module, preferences=['en_US.utf8', 'C.utf8', 'C', 'POSIX']) == 'en_US.utf8'

    # Test if locale -a succeeds without preference

# Generated at 2022-06-12 23:19:43.925715
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system import get_locale
    mod = get_locale.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    # test case 1 - no locale tool
    locale_tool = mod.get_bin_path('locale')
    mod.run_command = lambda cmd: (0, '', '') # no locale tool
    assert get_best_parsable_locale(mod) == 'C'

    # test case 2 - no locales
    mod.run_command = lambda cmd: (0, '', '') # no locales
    assert get_best_parsable_locale(mod) == 'C'

    # test case 3 - locale tool and locales
    locale_tool = mod.get_bin_path('locale')


# Generated at 2022-06-12 23:19:44.789039
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'

# Generated at 2022-06-12 23:19:58.828525
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''Unit test for get_best_parsable_locale'''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.run_command_called = False
            self.run_command_args = []
            self.run_command_kwargs = []
            self.get_bin_path_called = False
            self.get_bin_path_args = []
            self.get_bin_path_kwargs = []
            self.exit_json_called = False
            self.exit_json_args = []
            self.exit_json_kwargs = []
            self.fail_json_called = False
            self.fail_json_args

# Generated at 2022-06-12 23:20:09.062453
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, MagicMock, Mock
    from ansible.module_utils.common.collections import ImmutableDict

    module = MagicMock()
    module.run_command = Mock(return_value=(0, Mock(), Mock()))
    module.get_bin_path = Mock(return_value=Mock())

    # UTF-8 is a default preference and is available
    module.run_command.return_value = (0, "C.UTF-8\nen_US.UTF-8\n", Mock())
    best_locale = get_best_parsable_locale(module)


# Generated at 2022-06-12 23:20:14.076369
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Check if the default locale is POSIX
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=['de_DE.utf8']) == 'C'
    assert get_best_parsable_locale(None, preferences=['C']) == 'C'



# Generated at 2022-06-12 23:20:25.095502
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import sys
    if sys.hexversion > 0x03000000:
        from unittest.mock import MagicMock, Mock
        from io import StringIO
    else:
        from mock import MagicMock, Mock
        from cStringIO import StringIO

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale

    # Test 1: All OK - rc == 0, out == C.UTF8
    module = MagicMock(AnsibleModule)
    module.get_bin_path.return_value = 'locale'

    module.run_command.return_value = 0, StringIO('C.UTF8'), ''
    result = get_best_parsable_locale(module)

# Generated at 2022-06-12 23:20:35.948771
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic

    # Mock module
    class FakeModule():
        def __init__(self):
            self.fail_json = ansible.module_utils.basic.fail_json

    module = FakeModule()

    # Mock run_command
    def run_command(self, args):
        return 0, 'C', None

    module.run_command = run_command

    # Mock get_bin_path
    def get_bin_path(self, path):
        return "/bin/locale"

    module.get_bin_path = get_bin_path

    assert get_best_parsable_locale(module) == 'C'


# Generated at 2022-06-12 23:20:43.936419
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})
    result = get_best_parsable_locale(module, raise_on_locale=True)
    assert result == 'C'

    preferences = ['C.utf8', 'en_US.utf8', 'C', 'POSIX']
    result = get_best_parsable_locale(module, preferences=preferences, raise_on_locale=True)
    assert result in preferences

# Generated at 2022-06-12 23:20:47.383635
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert module
    assert get_best_parsable_locale(module) == 'C'

# Generated at 2022-06-12 23:20:50.288994
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=['POSIX', 'UTF-8']) == 'POSIX'

# Generated at 2022-06-12 23:20:57.203842
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class TestModule(object):
        def get_bin_path(self, tool):
            if tool.lower() == 'locale':
                return '/usr/bin/locale'

        def run_command(self, command):
            if command == ['/usr/bin/locale', '-a']:
                return (0, 'en_US.utf8\nen_US.UTF-8\nen_US\n', '')
            elif command == ['/usr/bin/locale', 'LANG']:
                return (0, 'en_US.utf8', '')
            elif command == ['/usr/bin/locale', '-u']:
                return (0, '', 'error invoking locale')
            else:
                return (0, '', '')


# Generated at 2022-06-12 23:20:59.825674
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule(argument_spec={})
    assert get_best_parsable_locale(mod) == 'C'

# Generated at 2022-06-12 23:21:09.163290
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ["C"]) == "C"

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-12 23:21:14.724188
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    class FakeModule(AnsibleModule):
        def __init__(self, **kwargs):
            super(FakeModule, self).__init__()

        def get_bin_path(self, name):
            return '/usr/bin/locale'

        def run_command(self, args):
            return (0, """
C
C.utf8
en_US.utf8
""", '')

    module = FakeModule()
    result = get_best_parsable_locale(module)
    assert result == 'C.utf8' or result == 'en_US.utf8'

    module = FakeModule()

# Generated at 2022-06-12 23:21:18.812860
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    preferences = ['C.utf8', 'C', 'POSIX']
    locale_found = get_best_parsable_locale(AnsibleModule(argument_spec={}), preferences)

    assert locale_found in preferences

# Generated at 2022-06-12 23:21:29.872594
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locales import get_best_parsable_locale


# Generated at 2022-06-12 23:21:40.248398
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.six import StringIO

    class FakeAnsibleModule(object):
        def __init__(self):
            self.params = {}
            self.check_mode = False

        def get_bin_path(self, arg, required=False):
            if arg == 'locale':
                return arg
            else:
                return None

        def run_command(self, cmd):
            if cmd == ['locale', '-a']:
                return 0, 'C.utf8 \n en_US.utf8 \n POSIX \n', ''
            elif cmd == ['locale', '-m']:
                return 0, '''C
en_US
POSIX
a_IS
''', ''
            else:
                return 0, '', ''

    module = FakeAnsibleModule()



# Generated at 2022-06-12 23:21:51.148606
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            locs=dict(type='list', default=None),
        )
    )
    # tests
    assert get_best_parsable_locale(module) == 'C'
    assert get_best_parsable_locale(module, ['C', 'POSIX']) == 'C'
    try:
        get_best_parsable_locale(module, ['ru_RU'], True)
        assert False
    except Exception as e:
        assert "Unable to get locale information" in str(e)
    assert get_best_parsable_locale(module, ['ru_RU']) == 'C'

# Generated at 2022-06-12 23:21:57.641171
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(object()) == 'C'
    assert get_best_parsable_locale(object(), ['C', 'POSIX']) == 'C'
    assert get_best_parsable_locale(object(), ['POSIX', 'C']) == 'POSIX'
    assert get_best_parsable_locale(object(), ['xx_XX.UTF-8', 'yy_YY.UTF-8']) == 'C'

# Generated at 2022-06-12 23:21:59.542049
# Unit test for function get_best_parsable_locale

# Generated at 2022-06-12 23:22:07.852577
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict()
    )

    # If the locale module isn't available in the path
    if get_best_parsable_locale(module, raise_on_locale=True):
        assert True

    # First in the preference list
    assert get_best_parsable_locale(module, ['en_US.utf8', 'en_US.ISO8859-1', 'C']) == 'en_US.utf8'

    # Default if not available
    assert get_best_parsable_locale(module, ['en_FR.utf8', 'en_US.ISO8859-1', 'C']) == 'C'

# Generated at 2022-06-12 23:22:13.436241
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    output = [
        "C",
        "C.UTF-8",
        "de_DE.utf8",
        "POSIX",
        "en_US.utf8",
        "en_US.UTF-8",
    ]

    class TestAnsibleModule(object):
        def __init__(self, bin_path, run_command, execute_module):
            self.bin_path = bin_path
            self.run_command = run_command
            self.execute_module = execute_module

        def get_bin_path(self, *args, **kwargs):
            return self.bin_path(*args, **kwargs)


# Generated at 2022-06-12 23:22:24.991620
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, ['en_US.UTF-8']) == 'en_US.UTF-8'
    assert get_best_parsable_locale(None, ['en_US.UTF-8', 'en_US.UTF-8']) == 'en_US.UTF-8'

# Generated at 2022-06-12 23:22:30.055950
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.utils.vars import combine_vars
    from ansible.module_utils.basic import AnsibleModule

    tmp = {'ANSIBLE_LOCALE': None, 'LC_ALL': 'C'}
    tmp = combine_vars(tmp, dict())

    mod = AnsibleModule(argument_spec=dict(), supports_check_mode=False)

    # Possibly the most vanilla AnsibleModule instance possible
    # it simply needs to support get_bin_path and run_command

    result = get_best_parsable_locale(mod)
    assert result == 'C', "Found locale %s before C!" % result

# Generated at 2022-06-12 23:22:37.451692
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.modules.system.locale

    # Make a module object with the characteristics we care about
    module = type('module', (object,), {'run_command': lambda self, c: [0, 'C\nen_US.utf8\nen_US.utf8\nC\nPOSIX\n', ''], 'get_bin_path': lambda self, b: 'bin/' + b})
    module = module()

    # Test for good input
    assert ansible.modules.system.locale.get_best_parsable_locale(module) is not None

    # Test for run_command returning an error
    module.run_command = lambda self, c: [1, '', '']
    assert ansible.modules.system.locale.get_best_parsable_locale(module) is not None

# Generated at 2022-06-12 23:22:46.861295
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import os
    import sys
    import tempfile

    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from lib.actions import Module

    _, locale_file = tempfile.mkstemp()
    with open(locale_file, "w") as f:
        f.write("./locale -a")
        f.write("C")
        f.write("en_US")

    module = Module()
    module.get_bin_path = lambda x: locale_file

    # Test for when locale is found successfully
    assert get_best_parsable_locale(module) == "C"
    assert get_best_parsable_locale(module, ["C"]) == "C"
    assert get_best_pars

# Generated at 2022-06-12 23:22:56.968074
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Unit tests for function get_best_parsable_locale
    '''
    import imp
    import os
    import unittest

    class MockModule(object):

        def __init__(self, **kwargs):
            self.params = kwargs

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return executable

        def fail_json(self, **kwargs):
            raise Exception(kwargs)


# Generated at 2022-06-12 23:23:00.869538
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic
    assert get_best_parsable_locale(ansible.module_utils.basic.AnsibleModule(argument_spec={})) == 'C'
    assert get_best_parsable_locale(ansible.module_utils.basic.AnsibleModule(argument_spec={}), preferences=['C', 'c']) == 'C'

# Generated at 2022-06-12 23:23:08.190305
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({}, supports_check_mode=True)
    print(get_best_parsable_locale(module, preferences=['C.UTF-8', 'en.utf8']))
    print(get_best_parsable_locale(module, preferences=['C.UTF-8', 'en_US.utf8', 'en.utf8']))
    print(get_best_parsable_locale(module, preferences=['en_US.utf8', 'C.UTF-8', 'en.utf8']))
    print(get_best_parsable_locale(module))

test_get_best_parsable_locale()

# Generated at 2022-06-12 23:23:14.390327
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})

    if not module.check_mode:
        best_locale = get_best_parsable_locale(module)
        assert best_locale

        for bad_locale in ["fr_FR.utf8", "es_ES.utf8"]:
            best_locale = get_best_parsable_locale(module, [bad_locale])
            assert best_locale == 'C'

# Generated at 2022-06-12 23:23:22.710613
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    class FakeModule(object):
        class FakeANSIBLE_MODULE(object):
            class FakeModule(object):
                no_log = True
        ANSIBLE_MODULE_ARGS = {}
        params = {}

        def get_bin_path(self, path, required=False):
            if path == 'locale':
                return '/usr/bin/locale'
            return None


# Generated at 2022-06-12 23:23:30.843948
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # Module imports are moved to the top for forward reference
    # pylint: disable=import-error,redefined-outer-name

    #
    # module_utils.basic.get_exception is used in AnsibleModule instances
    # to derive the ExceptionClass and ExceptionMessage
    # - if we were to use the AnsibleModule defined in the unit tests
    #   it would use the unit test itself as the location of that data
    # - Thus we use the one defined in ansible/module_utils/basic.py
    #   which is utilized in the AnsibleModule.run_command method
    #
    # pylint: disable=import-error,redefined-outer-name
    from ansible.module_utils.basic import get_exception

    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-12 23:23:50.475632
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    # no need to mock the import of the module because it is not actually used
    # in the function.

    # mock ansible module
    try:
        from ansible.module_utils.basic import AnsibleModule
    except ImportError:
        # ansible < 2.0
        from ansible.module_utils.basic import *

    am = AnsibleModule(
        argument_spec=dict()
    )

    # mock command
    am.run_command = Mock(return_value=(0, 'C', ''))

    # mock the bin path
    am.get_bin_path = Mock(return_value='/usr/bin/locale')

    # run the function and test
    locale = get_best_parsable_locale(am)
    assert locale == 'C'

    # test with expected output
    am.run

# Generated at 2022-06-12 23:23:55.635197
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    import ansible.module_utils.basic as basic
    module = basic.AnsibleModule(
        argument_spec=dict(
        ),
        supports_check_mode=False,
    )
    best_locale = get_best_parsable_locale(module)
    assert best_locale == 'C'



# Generated at 2022-06-12 23:24:04.466460
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test for get_best_parsable_locale function"""
    import base64
    try:
        from ansible.module_utils import basic
    except ImportError:
        print('ansible.module_utils not found')
        assert False

# Generated at 2022-06-12 23:24:11.421232
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import OrderedDict

    # fake AnsibleModule class that does not exit
    class _AnsibleModuleFail(AnsibleModule):
        def exit_json(*args, **kwargs):
            raise NotImplementedError

    # fake AnsibleModule class that works
    class _AnsibleModuleWork(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = {
                '_ansible_no_log': True,
                '_ansible_module_name': 'test'
            }
            super(_AnsibleModuleWork, self).__init__(*args, **kwargs)

    # fake AnsibleModule class that works but has no 'loc

# Generated at 2022-06-12 23:24:20.702638
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    class TestModule(object):
        def __init__(self):
            self.result = {}
            self.result['rc'] = 0
            self.result['stdout'] = ''
            self.result['stdout_lines'] = []
            self.result['stderr'] = ''
            self.result['cmd'] = ''
            self.result['changed'] = False
            self.result['warnings'] = []

        def run_command(self, cmd):
            return self.result['rc'], self.result['stdout'], self.result['stderr']

        def get_bin_path(self, cmd):
            bin_path = None
            if cmd == 'locale':
                bin_path = '/usr/bin/locale'
            return bin_path

    locale_test_module = TestModule()

   

# Generated at 2022-06-12 23:24:28.751326
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, ['foo']) == 'C'
    assert get_best_parsable_locale(None, ['C']) == 'C'
    assert get_best_parsable_locale(None, ['foo', 'C']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX', 'foo']) == 'POSIX'
    assert get_best_parsable_locale(None, ['POSIX', 'POSIX']) == 'POSIX'
    assert get_best_parsable_locale(None, ['en_US.UTF-8', 'foo']) == 'en_US.UTF-8'

# Generated at 2022-06-12 23:24:39.480611
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils import basic
    import os

    def mock_get_bin_path(module, *args, **kwargs):
        '''Mock os.path.exists when called from get_bin_path'''
        if args[0] == 'locale':
            return "/usr/bin/locale"
        else:
            return ""

    def mock_run_command(module, *args, **kwargs):
        '''Mock os.path.exists when called from run_command'''
        rc = 0
        out = ""
        err = ""
        if args[0] == '/usr/bin/locale':
            if '-a' in args[0]:
                rc = 0
                out = "C.iso88591\nC.utf8\nen_US.utf8\n"

# Generated at 2022-06-12 23:24:45.457269
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
        Test function for locale_info.get_best_parsable_locale
        Test data is taken from GNU Coreutil 'locale' utility
    '''
    test_locale = 'C'
    retval = get_best_parsable_locale({'run_command': None})
    assert retval == 'C', retval

    test_locale = 'C.utf8'
    retval = get_best_parsable_locale({'run_command': None}, preferences=['C.utf8', 'C', 'POSIX'])
    assert retval == 'C.utf8', retval

    test_locale = 'en_US.utf8'

# Generated at 2022-06-12 23:24:49.924763
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():

    assert get_best_parsable_locale(None, ['C']) == 'C'
    assert get_best_parsable_locale(None, ['POSIX']) == 'C'
    assert get_best_parsable_locale(None, ['en_US.utf8']) == 'C'
    assert get_best_parsable_locale(None, ['C.UTF-8']) == 'C'
    assert get_best_parsable_locale(None, ['C.utf8']) == 'C'
    assert get_best_parsable_locale(None) == 'C'
    assert get_best_parsable_locale(None, preferences=None) == 'C'



# Generated at 2022-06-12 23:24:59.984632
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    class TestModule:
        # simulate existing get_bin_path
        def get_bin_path(self, tool):
            return '/usr/bin/locale'

        # simulate existing run_command
        def run_command(self, args, check_rc=True, close_fds=True):
            # do a mock dict lookup here
            if args[0] == '/usr/bin/locale':
                if args[1] == '-a':
                    return 0, 'no\nC.utf8\nC\nPOSIX\nen_GB.utf8', None

        # we don't care about module stuff
        def exit_json(*args, **kwargs):
            pass

    # Test with preferences = None (default)
    module = TestModule()
    locale = get_best_parsable_locale(module)

# Generated at 2022-06-12 23:25:38.535479
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # need to isolate this test in its own process
    import sys
    import os
    import pytest
    import tempfile
    import subprocess
    import ansible.module_utils.basic as basic

    # create a function that proxies the module_utils module
    import ansible.module_utils.basic as the_real_basic
    sys.modules['ansible.module_utils.basic'] = the_real_basic
    from ansible.module_utils.basic import AnsibleModule

    locale_dir = tempfile.mkdtemp()
    locale_out = 'foo.utf8'

    # make a fake /usr/bin/locale
    with open(os.path.join(locale_dir, 'locale'), 'w') as f:
        f.write('#!/bin/sh\n')

# Generated at 2022-06-12 23:25:47.089308
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    # requirements
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    # useful constants
    AVAIL_LOCALE = to_bytes('C\nen_US.utf8\n')

    def mock_rc(cmd, environ_update=None, data=None, cwd=None):
        """Fake return codes"""
        cmd_elements = cmd[0]
        if cmd_elements == 'locale':
            if len(cmd) > 1:
                if cmd[1] == '-a':
                    return (0, AVAIL_LOCALE, '')
            else:
                return (127, '', 'fake exception')

        return (127, '', 'fake exception')


# Generated at 2022-06-12 23:25:49.365173
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test module uses get_best_parsable_locale()"""
    module = MockModule()
    found = get_best_parsable_locale(module)
    assert found == 'C'



# Generated at 2022-06-12 23:25:54.697624
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    """Test get_best_parsable_locale."""
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict()
    )

    assert 'C' in get_best_parsable_locale(module)

# Generated at 2022-06-12 23:25:57.185863
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    assert get_best_parsable_locale(None, None) == 'C'
    assert get_best_parsable_locale(None, ['C', 'POSIX']) == 'C'

# Generated at 2022-06-12 23:26:00.896922
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Function returns best parsable locale in the list of preferences
    '''
    from ansible.module_utils.basic import AnsibleModule
    preferences = ['C', 'POSIX', 'en_US.utf8']
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    assert get_best_parsable_locale(test_module, preferences) == 'C'

# Generated at 2022-06-12 23:26:09.464656
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.modules.system.locale import get_best_parsable_locale as get_best_locale
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule()

    # NOTICE: To test this function, we need to mock the get_bin_path function
    # to return an existing file. We do this by making a copy of the
    # get_best_parsable_locale function, adding get_bin_path to the function
    # as a local function and making the local function return a string.
    # We then call the new function as get_best_locale

    import shutil
    shutil.copy2('./lib/ansible/modules/system/locale.py',
        './test/unit/modules/system/locale.py')


# Generated at 2022-06-12 23:26:13.596878
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    from ansible.module_utils.basic import AnsibleModule

    DummyModule = AnsibleModule(argument_spec={
        'preferences': dict(type='list', default=None)
    })

    locale = get_best_parsable_locale(module=DummyModule)
    assert locale == 'C'

# Generated at 2022-06-12 23:26:17.699906
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    module = AnsibleModule(
        argument_spec=dict(
            languages=dict(default=None, type='list'),
        )
    )
    # Each unittest should have a string representation so assert that is true
    assert str(module) == 'ansible.module_utils.basic.AnsibleModule object'
    # Check one language and verify it returns that language
    languages_one = ['fr_FR']
    assert get_best_parsable_locale(module, languages_one) == 'fr_FR'
    # Check multiple languages and verify it returns the first language in the list
    languages_multiple = ['fr_FR', 'de_DE']
    assert get_best_parsable_locale(module, languages_multiple) == 'fr_FR'



# Generated at 2022-06-12 23:26:24.536092
# Unit test for function get_best_parsable_locale
def test_get_best_parsable_locale():
    '''
    Test for get_best_parsable_locale function
    '''
    from ansible.module_utils import basic

    # 1st test case: System has all the preferences and it will return 1st one in the list
    preferences = ['C.utf8', 'C', 'POSIX', 'en_US.utf8']
    test_module = basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    test_module.run_command = basic.AnsibleModule._run_command
    test_module.get_bin_path = basic.AnsibleModule._get_bin_path

    result = get_best_parsable_locale(test_module, preferences)
    assert result == 'C.utf8'

    # 2nd test case: System