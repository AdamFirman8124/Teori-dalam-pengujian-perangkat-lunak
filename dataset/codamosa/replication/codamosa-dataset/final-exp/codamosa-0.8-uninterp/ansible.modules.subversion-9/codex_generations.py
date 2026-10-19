

# Generated at 2022-06-13 06:10:28.616542
# Unit test for function main

# Generated at 2022-06-13 06:10:38.772762
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    module = "test"
    dest = "test"
    repo = "test"
    revision = "test"
    username = "test"
    password = "test"
    svn_path = "test"
    validate_certs = "test"
    test = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    rc = test._exec(["switch", "--revision", test.revision, test.repo, test.dest], check_rc=False)
    remote_revision = test.get_remote_revision()
    assert(rc == 0)
    assert(remote_revision.split()[1] == test.revision)

# Generated at 2022-06-13 06:10:43.893815
# Unit test for method update of class Subversion
def test_Subversion_update():
        mod = AnsibleModule(argument_spec={}, supports_check_mode= True)
        subversion = Subversion(mod, "", "", "", "", "", "", "")
        change, curr, head = subversion.needs_update()
        return change, curr, head



# Generated at 2022-06-13 06:10:53.008772
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence
    from ansible.module_utils.six import string_types
    import mock

    # Workaround required to mock module.run_command.
    @staticmethod
    def everything_ok_mock_run_command(args, check_rc=True, data=None):
        return 0, '', ''
    module_mock = mock.Mock(name='AnsibleModule')
    module_mock.run_command = everything_ok_mock_run_command
    module_mock.EXIT_FAIL = 1
    module_mock.EXIT_SUCC = 0

# Generated at 2022-06-13 06:10:54.116355
# Unit test for function main
def test_main():
    if False:
        pass

# Generated at 2022-06-13 06:11:01.263974
# Unit test for method switch of class Subversion

# Generated at 2022-06-13 06:11:13.005329
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    import tempfile
    import shutil
    import os
    repo_url = 'https://svn.red-bean.com/repos/test/trunk'
    rev = '1'
    dest = tempfile.mkdtemp()
    s = Subversion(None, dest, repo_url, rev, None, None, '/usr/bin/svn', False)
    s.checkout()
    os.chdir(dest)
    with open('test', 'w') as f:
        f.write('test')
    f.close()
    s.revert()
    rc, out, err = s.module.run_command(['svn', '--non-interactive', '--no-auth-cache', 'status', '--quiet', '--ignore-externals', dest], check_rc=True)
    shut

# Generated at 2022-06-13 06:11:23.200640
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(default=None, required=True, type='str'),
            repo=dict(default=None, required=True, type='str'),
            revision=dict(default=None, required=False, type='str'),
            username=dict(default=None, required=False, type='str'),
            password=dict(default=None, required=False, type='str'),
            svn_path=dict(default=None, required=True, type='str'),
            validate_certs=dict(default=False, required=False, type='bool')
        ),
        supports_check_mode=True
    )
    import StringIO
    class MockFilesystem(object):
        '''Mock Filesystem needed to test Subversion'''

# Generated at 2022-06-13 06:11:29.532148
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    subversion = Subversion('module', 'dest', 'repo', 'revision', 'username', 'password', 'svn_path', 'validate_certs')
    subversion.get_revision()
    assert(subversion.get_revision() == ('Revision:1149', 'URL:https://127.0.0.1/svn/ciao'))


# Generated at 2022-06-13 06:11:31.221600
# Unit test for method update of class Subversion
def test_Subversion_update():
    # TODO: test for update()
    Subversion.update()



# Generated at 2022-06-13 06:11:47.924168
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    src = 'example.org/repo'
    rev = '123'
    has = False
    next = (has, 'Revision: 123', 'Revision: 124')
    assert Subversion.needs_update(next) == True
    next = (has, 'Revision: 124', 'Revision: 124')
    assert Subversion.needs_update(next) == False
    next = (has, 'Revision: 125', 'Revision: 124')
    assert Subversion.needs_update(next) == False


# Generated at 2022-06-13 06:11:55.898987
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    import tempfile
    class MockModule(object):
        def run_command(self, args, check_rc, data=None):
            return 0, '', ''
    class MockArgs(object):
        def __init__(self):
            self.dest = tempfile.mkdtemp()
            self.repo = 'svn+ssh://an.example.org/path/to/repo'
            self.revision = 'HEAD'
            self.username = None
            self.password = None
            self.svn_path = '/usr/bin/svn'
            self.validate_certs = False
    args = MockArgs()
    module = MockModule()

# Generated at 2022-06-13 06:12:07.461045
# Unit test for method get_revision of class Subversion

# Generated at 2022-06-13 06:12:15.934045
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    import unittest
    import os
    import tempfile
    import shutil
    import ansible_module_subversion

    class TestSubversion(unittest.TestCase):
        def setUp(self):
            self.ansible_module_subversion = ansible_module_subversion
            self.Subversion = ansible_module_subversion.Subversion

            self.tempdir = tempfile.mkdtemp(dir='/tmp',prefix='subversion-test.')
            self.repo = 'file://%s' % self.tempdir
            self.revision = '1'
            self.dest = self.tempdir + '/checkout'
            os.makedirs(self.dest)
            self.module = MockModule()


# Generated at 2022-06-13 06:12:28.772766
# Unit test for function main

# Generated at 2022-06-13 06:12:42.064084
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    import module_utils.basic
    import ansible.module_utils.basic

    class FakeModule(object):
        def __init__(self):
            self._ansible_version = LooseVersion(ansible.__version__)
            self.check_mode = False
            self.debug = False
            self.run_command = self._run_command
            self.warn = getattr(module_utils.basic, 'warn', None)

        def _run_command(self, command, check_rc=True, data=None):
            if 'invalidcommand' in command:
                return 1, '', ''
            elif 'notarepocommand' in command:
                return 0, '', ''
            else:
                return 0, '', 'URL: https://github.com/ansible/ansible'


# Generated at 2022-06-13 06:12:53.330730
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # Setup mock module
    test = Subversion(module=None, dest='destination', repo='repository', revision='HEAD', username=None, password=None, svn_path='svn', validate_certs=False)
    # Test subversion has local mods
    test.get_revision = lambda: 'Revision: 123', 'URL: https://example.org:12345/repo'
    test.get_remote_revision = lambda: 'Revision: 125'
    assert test.needs_update() == (True, 'Revision: 123', 'Revision: 125')
    # Test subversion has no local mods
    test.get_revision = lambda: 'Revision: 125', 'URL: https://example.org:12345/repo'

# Generated at 2022-06-13 06:13:06.067981
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    import os
    import shutil
    from ansible_collections.community.general.tests.unit.compat import unittest
    from ansible_collections.community.general.tests.unit.compat.mock import patch
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale


# Generated at 2022-06-13 06:13:17.953431
# Unit test for function main
def test_main():
    from ansible.modules.source_control.subversion import main

    fake_module = FakeModule({
        'dest': '',
        'repo': 'svn+ssh://an.example.org/path/to/repo',
        'revision': 'HEAD',
        'force': False,
        'username': '',
        'password': '',
        'executable': '',
        'export': False,
        'checkout': False,
        'update': False,
        'switch': True,
        'in_place': False,
        'validate_certs': False,
        'check_mode': False,
    })

    import os
    import subprocess
    import tempfile

    # create a local svn repository
    with tempfile.TemporaryDirectory() as tmp_path:
        subprocess.run

# Generated at 2022-06-13 06:13:23.245655
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # class Subversion:
    # def needs_update(self):
    # Unit test for method needs_update of class Subversion
    object1 = Subversion(None, '.', '.', 'HEAD', None, None, 'svn', False)
    object1.get_revision = lambda: ('Revision: 11', '')
    object1._exec = lambda args, check_rc=True: ['Revision: 12']
    change, curr, head = object1.needs_update()
    assert change is True
    assert curr == 'Revision: 11'
    assert head == 'Revision: 12'

# Generated at 2022-06-13 06:13:57.631298
# Unit test for function main

# Generated at 2022-06-13 06:14:00.995054
# Unit test for method update of class Subversion
def test_Subversion_update():
    def mock_rc(a, b, c):
        return True, "0", "0"
    module = type("AnsibleModule", (object,), {})()
    module.run_command = mock_rc
    svn = Subversion(module, "/tmp", "", "", "", "", "", False)
    assert svn.get_remote_revision() == 'Unable to get remote revision'


# Generated at 2022-06-13 06:14:10.717756
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    class MockModule:
        def __init__(self, *args, **kwargs):
            self.params = {'repo': 'svn+ssh://an.example.org/path/to/repo',
                           'dest': '/src/checkout',
                           'revision': 'HEAD'}

        def run_command(self, command, check_rc=True):
            return 0, '''Path: repo
URL: http://example.org
Repository Root: http://example.org/trunk
Repository UUID: aa3b4d4b-8af4-4e9e-9392-e11b0d66a36a
Revision: 1234
Node Kind: directory''', ''

    # Run the test

# Generated at 2022-06-13 06:14:18.447198
# Unit test for method update of class Subversion
def test_Subversion_update():
    # creation of a mock module object
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    # creation of a mock revision object
    from types import SimpleNamespace
    revision = SimpleNamespace()
    revision.value = '1234'
    # creation of a mock username object
    from types import SimpleNamespace
    username = SimpleNamespace()
    username.value = 'testuser'
    # creation of a mock password object
    from types import SimpleNamespace
    password = SimpleNamespace()
    password.value = 'testpassword'
    # creation of a mock svn_path object
    from types import SimpleNamespace
    svn_path = SimpleNamespace()
    svn_path.value = 'svn'
    # creation of a mock validate_certs object
    from types import SimpleNames

# Generated at 2022-06-13 06:14:31.208746
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    fixture = [
        'URL: https://svn.apache.org/repos/asf/subversion/trunk',
        'Repository Root: https://svn.apache.org/repos/asf',
        'Repository UUID: 13f79535-47bb-0310-9956-ffa450edef68',
        'Revision: 1889134',
        'Node Kind: directory',
        'Schedule: normal',
        'Last Changed Author: stsp',
        'Last Changed Rev: 1889134',
        'Last Changed Date: 2019-03-12 22:56:07 +0100 (Tue, 12 Mar 2019)',
    ]
    fixture_revision = 'Revision: 1889134'

# Generated at 2022-06-13 06:14:43.039149
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    # setup
    def run_command_mock(self, cmd, check_rc=True, data=None):
        return True, None, None

    import types
    os_path_exists_mock = types.MethodType(lambda self, path : True, Subversion)

    m_module = types.ModuleType('__m_module')
    m_module.run_command = types.MethodType(run_command_mock, m_module)
    m_module.params = types.ModuleType('__m_module')
    m_module.exit_json = types.MethodType(lambda self, changed, meta: None, m_module)

    sv = Subversion(m_module, 'args', 'args', 'args', 'args', 'args', 'svn_path', 'args')
    sv.revert = os_path

# Generated at 2022-06-13 06:14:45.096745
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    assert Subversion.switch(self)

# Generated at 2022-06-13 06:14:49.133295
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    r = Subversion(None, '/tmp/test_ansible', 'svn+ssh://an.example.org/path/to/repo', 'HEAD', None, None, 'svn', False)
    assert r.get_remote_revision() == 'Revision: 12345'


# Generated at 2022-06-13 06:14:56.269774
# Unit test for function main
def test_main():
    import os
    import platform
    import shutil
    import tempfile
    import subprocess
    import sys

    class Args(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)


    # Prepare temp folder
    temp_path = tempfile.mkdtemp()
    dest = temp_path + "/checkout"
    repo = "https://github.com/ansible/ansible"
    revision = "HEAD"

# Generated at 2022-06-13 06:15:10.138233
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import unittest
    cmds = []
    def _exec(args, check_rc=True):
        cmds.append(' '.join(args))
        return ['A <path>', 'D <path>']
    module = object()
    module.run_command = lambda x, y, **kwargs: (0, '', '')
    svn = Subversion(
        module=module,
        dest='/a/b/c',
        repo='svn+ssh://an.example.org/path/to/repo',
        revision='HEAD',
        username=None,
        password=None,
        svn_path='/usr/bin/svn',
        validate_certs=False
    )
    svn._exec = _exec
    svn.switch()

# Generated at 2022-06-13 06:16:12.843105
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    from ansible.module_utils.basic import AnsibleModule
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svn_test')
    repo = 'https://github.com/ansible/ansible.github.io.git'
    svn_path = 'svn'
    svn = Subversion(svn_path, dest, repo, None, None, None, None)
    svn.checkout()
    # Try to checkout again. The destination path already contains a SVN repo.
    assert svn.is_svn_repo()

# Generated at 2022-06-13 06:16:25.575788
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    def mock_run_command(bits, check_rc, **kwargs):
        assert bits == ['svn', '--non-interactive', '--no-auth-cache', '--trust-server-cert', 'info', '-r', '5', '/dest']
        return 0, 'Revision: 5\n', ''

    class Args:
        diff_mode = False
        dest = '/dest'
        repo = 'ssh://user@host/repo'
        revision = '5'
        switch = True
        update = True
        force = 'no'
        username = None
        password = None
        validate_certs = 'no'
        svn_path = 'svn'

    class MockModule:
        def __init__(self):
            self.params = Args()


# Generated at 2022-06-13 06:16:32.876312
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.source_control.subversion import Subversion
    from ansible.module_utils.subversion import SubversionException
    from ansible.module_utils.subversion import LOCALE_RE
    from ansible.module_utils.subversion import TZ_RE
    from ast import literal_eval
    import datetime
    import pytz
    import re
    import sys
    import time
    import unittest

    # Make sure the locale module is properly mocked.
    locale_module_name = 'locale'
    if locale_module_name in sys.modules:
        del sys.modules[locale_module_name]
    from ansible.module_utils import basic
    basic.get_best_parsable_locale = lambda: 'C'

# Generated at 2022-06-13 06:16:37.199858
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    sub = Subversion(AnsibleModule, '', '', '', '', '', '', '')
    out = ['Reverted .', 'Reverted .']
    assert sub.revert()


# Generated at 2022-06-13 06:16:38.250756
# Unit test for method update of class Subversion
def test_Subversion_update():
    pass

# Generated at 2022-06-13 06:16:47.194373
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # Arrange
    mock_module = AnsibleModule(argument_spec={})
    mock_module.run_command = MagicMock(return_value=(0, "Révision : 1889134\nurl\n", ""))
    mock_Subversion = Subversion(mock_module, None, None, None, None, None, None, None)
    # Act
    result = mock_Subversion.needs_update()
    # Assert
    assert result == (True, "Révision : 1889134", "Révision : 1889134")


# Generated at 2022-06-13 06:16:54.311302
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class MockModule():
        def __init__(self):
            self.params = {
                'revision': 'HEAD'
                }
        def run_command(self, cmd, check=True, data=None):
            if cmd[0] == 'svn':
                return (0, 'svn info output', '')
    class MockSubversion(Subversion):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            self.module = module
            self.dest = dest
            self.repo = repo
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path
            self.validate_certs = validate_certs
    module = MockModule()
   

# Generated at 2022-06-13 06:17:06.529334
# Unit test for function main

# Generated at 2022-06-13 06:17:11.225384
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    svn = Subversion()
    svn.revert()
    output = svn._exec()

    for line in output:
        if re.search(r'^Reverted ', line) is None:
            return True
    return False


# Generated at 2022-06-13 06:17:22.717920
# Unit test for method update of class Subversion
def test_Subversion_update():
    import tempfile
    import shutil
    import sys

    test_dir = tempfile.mkdtemp()
    os.chdir(test_dir)

    svn_version = '1.14.0'  # for mocking command line call
    repo_url = 'https://svn.apache.org/repos/test/testrepo'
    dest = 'checkout'
    ansible_module = AnsibleModule({
        'dest': dest,
        'repo': repo_url,
    })
    svn = Subversion(
        ansible_module,
        dest,
        repo_url,
        'HEAD',
        '',
        '',
        '/usr/bin/svn',
        True,
    )
    svn._exec = lambda x, check_rc=True: [svn_version]

# Generated at 2022-06-13 06:19:50.740230
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # Some test cases:
    #      curr        head        result
    #      '12345'     '12345'     False
    #      '12345'     '12346'     True
    #      '12345'     '1234'      True
    #      '12345'     '54321'     True
    #      'ABCD'      '12346'     True
    #      '12345'     'ABCD'      True
    #      'ABCD'      'ABCD'      False
    #      'ABCD'      'ABC'       True
    #      '123'       'ABC'       True
    #      'ABC'       '123'       True

    # HELPER FUNCTION: actually call needs_update
    def _needs_update(curr, head):
        mock_module = MockModule()


# Generated at 2022-06-13 06:19:57.699611
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    module = AnsibleModule(dict(repo='svn://', dest='/tmp/subversion_test'))
    svn = Subversion(module, dest='/tmp/subversion_test', repo='svn://', revision='HEAD', username='', password='', svn_path='echo', validate_certs=True)
    assert svn.get_remote_revision() == 'Révision : 4'