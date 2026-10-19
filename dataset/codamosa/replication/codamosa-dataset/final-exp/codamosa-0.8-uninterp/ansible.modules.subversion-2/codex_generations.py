

# Generated at 2022-06-13 06:10:15.204610
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    # Run get_remote_revision
    result = subversion_obj.get_remote_revision()
    # Verify the result
    assert result


# Generated at 2022-06-13 06:10:19.202854
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import tempfile, os
    module = AnsibleModule({})
    dest = tempfile.mkdtemp(dir='/tmp')
    repo = 'https://github.com/datakurre/ansible-examples.git/tests'
    revision = 'HEAD'
    module.run_command = run_command
    svn = Subversion(module, dest, repo, revision)
    svn.switch()
    assert os.path.isfile(os.path.join(dest, 'test.ini')) == True, "Something went wrong"


# Generated at 2022-06-13 06:10:30.016054
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    import sys
    if sys.version_info[0] == 3:
        string_types = (str, bytes)
    else:
        string_types = (basestring,)
    class Module(object):
        def __init__(self, **kwargs):
            self.run_command_data = kwargs
            self.params = kwargs
            self.run_command_rc = 0
            self.run_command_results = ("Révision : 1889134", "", 0)

        def run_command(self, *args, **kwargs):
            return self.run_command_results
    m = Module(**{})

# Generated at 2022-06-13 06:10:32.461604
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    sub_version = Subversion()
    result = sub_version.get_revision()
    print(result)



# Generated at 2022-06-13 06:10:37.683619
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class_subversion = Subversion(None, 'dest', 'repo', 'revision', None, None, None, None)

    def _exec(args, check_rc=True):
        return '000 0000000 000'

    class_subversion._exec = _exec

    assert class_subversion.get_remote_revision() == 'Révision : 0000000'


# Generated at 2022-06-13 06:10:47.847628
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = args
            self.args = kwargs
            self.changed = False
        def run_command(self, *args, **kwargs):
            return 0, 'Revision: 1889135', ''
        def set_changed(self):
            self.changed = True
    dest = '/tmp/ansible-subversion-test'
    repo = 'svn+ssh://an.example.org/path/to/repo'
    revision = 'HEAD'
    username = None
    password = None
    svn_path = 'svn'
    validate_certs = False
    svn = Subversion(MockModule, dest, repo, revision, username, password, svn_path, validate_certs)
   

# Generated at 2022-06-13 06:10:50.034587
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    assert Subversion.needs_update(self) == ('change', 'curr', 'head')

# End of unit tests


# Generated at 2022-06-13 06:10:58.864966
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    class module_mock(object):
        def run_command(self, cmd, check_rc):
            return 0, 'X      foo.txt\nX      bar.txt', None

        def exit_json(self, changed=False, revision=None, url=None, remote_revision=None):
            raise Exception('exit_json() called')

        def fail_json(self, msg):
            raise Exception('fail_json() called')

    class Subversion_mock(Subversion):
        def __init__(self, m, dest, repo, revision, username, password, svn_path, validate_certs):
            pass

    svn_mock = Subversion_mock(module_mock(), None, None, None, None, None, None, None)
    assert svn_mock.has_local_mods()

# Generated at 2022-06-13 06:11:08.123242
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    destination = os.path.abspath(os.path.join(os.path.dirname(__file__), 'destination'))
    repo = os.path.abspath(os.path.join(os.path.dirname(__file__), 'repo'))
    username = ''
    password = ''
    svn_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'svn'))
    validate_certs = True
    revision = '3'
    s = Subversion(None, repo, repo, revision, username, password, svn_path, validate_certs)
    assert s.switch() == True



# Generated at 2022-06-13 06:11:15.891283
# Unit test for method update of class Subversion
def test_Subversion_update():
#cmd: svn update --revision 123 /tmp/test_repo --non-interactive --no-auth-cache
#('no_change', 'Revision: 123', 'Revision: 123')
    repo = "file:///tmp/test_repo"
    dest = "/tmp/test_repo"
    revision = "123"
    s = Subversion("", dest, repo, revision, "", "", "/usr/bin/svn", False)
    if (s.update()):
        assert False, "svn update failed"



# Generated at 2022-06-13 06:11:36.487681
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    # Subversion.switch(self):
    # Change working directory's repo.
    assert True


# Generated at 2022-06-13 06:11:45.217024
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    # Test that dest repo is different from repo
    # Need to have a repo to compare against
    repo = "https://github.com/ansible/ansible/trunk/lib/ansible"
    dest = "https://github.com/ansible/ansible/trunk/lib/ansible/modules/database/mysql"
    svn_path = "svn"
    svn = Subversion(None, dest, repo, None, None, None, svn_path)
    assert svn.switch() == True

    # Test that dest repo is the same as repo
    # If this test fails, then the modules needs to be updated
    repo = "https://github.com/ansible/ansible/trunk/lib/ansible"

# Generated at 2022-06-13 06:11:50.540662
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import BytesIO

    class TestModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    class MockRunner(object):
        def __init__(self, module):
            self.module = module


# Generated at 2022-06-13 06:12:01.265121
# Unit test for function main
def test_main():
    mock_module = Mock(return_value=None)
    mock_module.params = { 'dest': 'abc', 'repo': 'abc', 'revision': 'abc', 'force': 'abc', 'username': 'abc', 'password': 'abc', 'executable': 'abc', 'export': 'abc', 'switch': 'abc', 'checkout': 'abc', 'update': 'abc', 'in_place': 'abc', 'validate_certs': 'abc' }
    mock_module.check_mode = False
    mock_module.run_command = Mock(return_value=(0, '', ''))
    mock_module.run_command_environ_update = { 'LANG': '', 'LC_MESSAGES': '' }
    mock_module.get_bin_path = Mock(return_value='abc')
    mock

# Generated at 2022-06-13 06:12:12.066515
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
  import unittest
  class Subversion_get_remote_revision_Test(unittest.TestCase):
    def test_get_remote_revision(self):
      import subprocess
      import tempfile
      import os

      # Create a SVN repo in a temporary directory
      svn_repo = tempfile.mkdtemp()
      command = ["svnadmin", "create", svn_repo]
      subprocess.check_call(command)

      # Checkout a copy in another temporary directory
      svn_copy = tempfile.mkdtemp()
      command = ["svn", "checkout", "file://" + svn_repo, svn_copy]
      subprocess.check_call(command)

      # Add a new file in the SVN repo

# Generated at 2022-06-13 06:12:18.036210
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():

    module = AnsibleModule({})
    svn = Subversion(module,
                     dest=None,
                     repo=None,
                     revision=None,
                     username=None,
                     password=None,
                     svn_path='svn',
                     validate_certs='no')
    remote_revision = svn.get_remote_revision()
    assert re.match(Subversion.REVISION_RE, remote_revision) is not None


# Generated at 2022-06-13 06:12:20.637603
# Unit test for method update of class Subversion
def test_Subversion_update():
    expected = True
    result = Subversion.update()
    assert result == expected


# Generated at 2022-06-13 06:12:32.670660
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    # Create and prepare a mock module
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda args, check_rc=True: (0, '1.9.7', '')
    # Create the actual object
    svn_cmd = '/usr/bin/svn'
    svn = Subversion(module, svn_cmd, '', '', '', '', '', False)
    assert not svn.has_option_password_from_stdin()
    # Create and prepare a mock module
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda args, check_rc=True: (0, '1.10.0', '')
    # Create the actual object
    svn_cmd = '/usr/bin/svn'

# Generated at 2022-06-13 06:12:41.291330
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    git_control = Subversion(
        "/tmp/ansible-test/ansible-remote-tmp/home/vagrant",
        "git+https://github.com/ansible/ansible.git",
        "HEAD",
        None,
        ["--verbose", "--keep-update"],
        None,
        "git"
    )
    (val, curr, head) = git_control.needs_update()
    assert (git_control.repo == "git+https://github.com/ansible/ansible.git")



# Generated at 2022-06-13 06:12:46.272696
# Unit test for function main
def test_main():
  # created temporary directory for the test
  import tempfile
  dest_dir = tempfile.mkdtemp()
  import shutil
  # created temporary directory for the test
  t_dir = tempfile.mkdtemp()
  import ansible.module_utils.basic
  from ansible.module_utils.basic import AnsibleModule
  from ansible.module_utils.common.locale import get_best_parsable_locale
  from ansible.module_utils.compat.version import LooseVersion

# Generated at 2022-06-13 06:13:14.585539
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    # Create test data
    options = {'repo': "myRepo", 'revision': 'myRev', 'username': 'myUsername', 'password': 'myPassword', 'executable': '/usr/bin/svn', 'checkout': False, 'update': False, 'dest': '/tmp/svn', 'export': False, 'switch': False, 'force': True, 'in_place': True, 'validate_certs': False, 'remote_user': 'ansible', 'remote_tmp': '/tmp', 'no_log': False}
    module = AnsibleModule(**options)
    subversion = Subversion(module, 'value0', 'value1', 'value2', 'value3', 'value4', 'value5', False)
    # Test the switch method
    assert subversion.switch() == None


# Generated at 2022-06-13 06:13:26.266363
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import py.test
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY2, PY3

    module = AnsibleModule(argument_spec={})
    module.params = {
        "dest": "/tmp/test",
        "repo": "http://repo.test/test",
        "revision": "HEAD",
        "username": None,
        "password": None,
        "svn_path": "svn",
        "validate_certs": False}
    module.check_mode = False
    module.no_log = True
    # monkeypatch run_command to simulate the output of svn program

# Generated at 2022-06-13 06:13:33.288711
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    revision = "Revision: 1889134"
    revision_w_space = "Revision : 1889134"
    revision_zh = "版本: 1889134"

    assert Subversion.get_remote_revision(revision) == "1889134"
    assert Subversion.get_remote_revision(revision_w_space) == "1889134"
    assert Subversion.get_remote_revision(revision_zh) == "1889134"


# Generated at 2022-06-13 06:13:37.818786
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    svn = Subversion(None, None, None, None, None, None)
    svn.get_revision = lambda: ('Revision: 4', 'test')
    svn._exec = lambda cmd, check_rc=True: ['Revision: 4', 'Revision: 6']
    assert svn.needs_update() == (True, 'Revision: 4', 'Revision: 6')


# Generated at 2022-06-13 06:13:49.544398
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    mod = AnsibleModule({
        'dest': '',
        'repo': '',
        'revision': '',
        'username': '',
        'password': '',
        'svn_path': '',
        'validate_certs': '',
    })
    dest = 'dest'
    repo = 'repo'
    revision = 'revision'
    username = 'username'
    password = 'password'
    svn_path = 'svn_path'
    validate_certs = 'validate_certs'
    s = Subversion(mod, dest, repo, revision, username, password, svn_path, validate_certs)


# Generated at 2022-06-13 06:13:51.576178
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    Subversion(None, None, None, None, None, None, None, None).switch()

# Generated at 2022-06-13 06:13:54.209932
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    s = Subversion(None, None, '../ansible', None, None, None, 'svn', None)
    s.get_remote_revision()
    assert True


# Generated at 2022-06-13 06:13:59.169602
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    import subprocess
    s = b'''A       test/f1
A       test/f2
A       test/f3
M       test/f4
?       test/f5
A       test/f6
'''
    # set up
    svn = Subversion(None, None, None, None, None, None)
    svn.module = subprocess
    # test
    result = svn.has_local_mods()
    # assert
    assert result is True



# Generated at 2022-06-13 06:14:05.001580
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    def get_remote_revision():
        return 'remote_revision: 1234'

    s = Subversion(None, None, None, None, None, None, None, None)
    s.get_remote_revision = get_remote_revision
    actual = s.get_remote_revision()
    expected = '1234'
    assert actual == expected


# Generated at 2022-06-13 06:14:13.653563
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale
    module = AnsibleModule(argument_spec=dict())
    module.run_command = lambda args, check_rc=True, data=None: (0, '1.9.9\n', '')
    obj = Subversion(module, dest=None, repo=None, revision=None, username=None, password=None, svn_path='/usr/bin/svn', validate_certs=None)
    assert obj.has_option_password_from_stdin() == False
    module.run_command = lambda args, check_rc=True, data=None: (0, '1.10.0\n', '')
    assert obj.has_option_

# Generated at 2022-06-13 06:14:43.826889
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    test_module = AnsibleModule(argument_spec={
        'force': {'type': 'bool', 'default': False},
        'in_place': {'type': 'bool', 'default': False},
    })
    test_module.params = {
        'repo': 'svn+ssh://an.example.org/path/to/repo',
        'force': False,
        'dest': '/src/export',
        'checkout': True,
        'revision': 'HEAD',
        'export': False,
        'switch': False,
        'username': '',
        'password': '',
        'svn_path': 'svn',
        'in_place': False,
        'validate_certs': False
    }

# Generated at 2022-06-13 06:14:53.535980
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    module = AnsibleModule({}, {})
    # test a valid svn repo
    dest = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'test_svn', 'repo'))
    repo = 'http://test_url'
    revision = '1'
    username = 'test_username'
    password = 'test_password'
    svn_executable = None
    validate_certs = True
    svn_class = Subversion(module, dest, repo, revision, username, password, svn_executable, validate_certs)
    assert svn_class.is_svn_repo() is True
    # test a not valid svn repo

# Generated at 2022-06-13 06:15:01.379768
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # Scenario 1:
    # When we check the SVN status
    # The repository is up to date
    s = Subversion(None, '/home/mypath/project1', 'svn+ssh://an.example.org/path/to/repo', 'HEAD', 'username', 'password', '/usr/bin/svn', False)
    change, curr, head = s.needs_update()
    assert change is False


# Generated at 2022-06-13 06:15:13.060094
# Unit test for function main

# Generated at 2022-06-13 06:15:21.042949
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    module = AnsibleModule(argument_spec={},check_invalid_arguments=False)
    svn_info =  b'''Path: svn-test2
URL: https://example.com/svn/test2
Relative URL: ^/test2
Repository Root: https://example.com/svn
Repository UUID: 5bb8db62-9c41-4f07-a421-4e8cd7ebd55c
Revision: 26
Node Kind: directory
Schedule: normal
Last Changed Author: admin
Last Changed Rev: 26
Last Changed Date: 2019-06-11 17:36:02 -0400 (Tue, 11 Jun 2019)
'''
    module.run_command = lambda *args, **kwargs: (0, svn_info, '')

# Generated at 2022-06-13 06:15:28.606552
# Unit test for function main

# Generated at 2022-06-13 06:15:33.540124
# Unit test for function main
def test_main():
    import tempfile, shutil, os
    from gitdb.util import hex_to_bin
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:15:38.319184
# Unit test for method switch of class Subversion
def test_Subversion_switch():

    import os
    import subprocess
    import sys
    import tempfile

    ansible_python = sys.executable
    test_dir = tempfile.mkdtemp()
    test_repo = os.path.join(test_dir, 'test-repo')
    test_dest = os.path.join(test_dir, 'test-dest')
    # Create svn repo
    subprocess.check_output(['svnadmin', 'create', test_repo])
    # Checkout svn repo
    subprocess.check_output(['svn', 'checkout', 'file://' + test_repo, test_dest])
    # Create first file
    first_file = os.path.join(test_dest, 'first.txt')

# Generated at 2022-06-13 06:15:43.739618
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    class MockModule(object):
        def __init__(self, *args):
            self.args = args
        def run_command(self, command, check_rc=True, data=None):
            self.command = command
            return 0, '', ''

    def mock_exec(self, command, check_rc=True):
        return 'Reverted ' in command

    test = Subversion(MockModule, 'dest', 'repo', 'revision', 'username', 'password', 'svn_path', 'validate_certs')
    test._exec = mock_exec
    revert = test.revert()
    assert revert == True


# Generated at 2022-06-13 06:15:48.458502
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    module = AnsibleModule({})
    svn = Subversion(module, "", "", "", "", "", "", True)
    svn.get_remote_revision()


# Generated at 2022-06-13 06:16:41.517355
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.rc = 0
            self.args = args
            self.kwargs = kwargs
            self.cmd = kwargs["cmd"]
            self.stdout = "Revision: 189\nURL: http://example.org"
            self.stdout_lines = self.stdout.splitlines()

        def run_command(self, cmd, check_rc=True):
            assert cmd == self.cmd
            return self.rc, self.stdout, ""

    subversion = Subversion(
        MockModule(**{"cmd": ["info", "/path/to/repo"]})
    )
    assert subversion.get_revision() == ('Revision: 189', 'URL: http://example.org')

# Unit

# Generated at 2022-06-13 06:16:51.221639
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    module = AnsibleModule(argument_spec=dict())
    dest = '/tmp/subversion_test'
    repo = 'svn://svn.apache.org/repos/asf/subversion/trunk'
    revision = 'HEAD'
    username = None
    password = None
    svn_path = 'svn'
    validate_certs = True
    s = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    s.checkout()
    assert s.is_svn_repo() == True
    s._exec(["delete", "--keep-local", "--force", dest])


# Generated at 2022-06-13 06:16:58.538217
# Unit test for method update of class Subversion
def test_Subversion_update():
    import subversion as svn
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    svn = svn.Subversion(module, '/src/checkout', 'url', None, None, None, '/usr/bin/svn', True)
    expected_output = True
    output = svn.update()
    assert output == expected_output



# Generated at 2022-06-13 06:17:09.100478
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    import mock
    rev_regexp = Subversion.REVISION_RE
    # Test 1, simple output:
    # Reverted 'svn-dummy/path/to/repo/trunk/doc/foo.txt'
    # Reverted 'svn-dummy/path/to/repo/trunk/doc/bar.txt'
    output = ['Reverted \'svn-dummy/path/to/repo/trunk/doc/foo.txt\'',
              'Reverted \'svn-dummy/path/to/repo/trunk/doc/bar.txt\'']
    assert Subversion.revert(output) == True

    # Test 2, output with unknown lines:
    # Reverted 'svn-dummy/path/to/repo/trunk/doc/foo.txt'

# Generated at 2022-06-13 06:17:15.352114
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    class TestModuleFail(object):
        def __init__(self):
            self.exit_json = lambda **x: x
            self.fail_json = lambda **x: x

    class TestModuleDontFail(object):
        def __init__(self):
            self.exit_json = lambda **x: x
            self.fail_json = lambda **x: x

    class TestModuleSucceed(object):
        def __init__(self):
            self.exit_json = lambda **x: x
            self.fail_json = lambda **x: x

    class TestSubversion(Subversion):
        def __init__(self):
            pass

        def _exec(self, args, check_rc=True):
            if args[0] == 'status':
                return [' M  test3', 'A    test3']

# Generated at 2022-06-13 06:17:23.273996
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    result = None
    with patch.object(module_builtins, '__import__') as mocked:
        mock_module = MagicMock()
        mock_module.run_command = MagicMock(return_value=[0, 'output', ''])
        mocked.return_value = mock_module
        subversion = Subversion(mock_module, "/dest",  "svn://repo", "123", "username", "password", "svn", True)
        result = subversion.switch()
    assert result == True


# Generated at 2022-06-13 06:17:29.665235
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import action
    from ansible.module_utils.common.locale import get_best_parsable_locale
    import os
    import re
    path = os.path.join(os.path.dirname(__file__), 'main_expect.txt')
    with open(path) as f:
        expect = f.read()

    with open(path) as f:
        lines = f.readlines()
    with open(path) as f:
        lines = f.readlines()
    with open(path) as f:
        lines = f.readlines()
    with open(path) as f:
        lines = f.readlines()
    with open(path) as f:
        lines = f.readlines()

# Generated at 2022-06-13 06:17:30.748515
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    assert False, "unimplemented"


# Generated at 2022-06-13 06:17:35.055807
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    assert Subversion(None, None, None, None, None, None, None, None).has_option_password_from_stdin() == LooseVersion('1.10.0') <= LooseVersion('1.10.0')


# Generated at 2022-06-13 06:17:43.190384
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    # Initialize the object
    module = AnsibleModule(argument_spec=dict())
    dest = '/src/checkout'
    repo = 'svn+ssh://an.example.org/path/to/repo'
    revision = 'HEAD'
    username = ''
    password = ''
    svn_path = 'svn'
    validate_certs = True

    obj = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    # Call the method
    remote_revision = obj.get_remote_revision()
    # Check the result
    if type(remote_revision) == str:
        assert type(remote_revision) == str
    else:
        assert 1 == 0


# Generated at 2022-06-13 06:19:57.166233
# Unit test for function main
def test_main():
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    mock_module = MagicMock()