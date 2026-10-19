

# Generated at 2022-06-13 06:10:20.871928
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.compat.tests.mock import create_autospec, patch
    from ansible.module_utils._text import to_bytes
    s = Subversion(create_autospec(AnsibleModule),
                   dest="/path/to/something/.svn",
                   repo="svn+ssh://an.example.org/path/to/repo",
                   revision="38",
                   username="foo",
                   password="bar",
                   svn_path="svn",
                   validate_certs=True)
    with patch("ansible.module_utils.common.run_command", return_value=(0, to_bytes(""), to_bytes(""))):
        assert s.is_svn_repo()

# Generated at 2022-06-13 06:10:29.648578
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import tempfile
    import shutil
    import os
    import subprocess
    import sys
    import pexpect
    import re

    # Setup
    # create a temp directory
    tempdir = tempfile.mkdtemp()
    # create a subversion repository
    p = subprocess.Popen(["svnadmin", "create", tempdir], stdout=subprocess.PIPE)
    p.wait()
    # create a checkout, add some files and commit
    p = pexpect.spawn("svn checkout file://" + tempdir + " " + tempdir + "/checkout" )
    p.expect(".*password.*")
    p.sendline("password")
    p.expect(pexpect.EOF)
    p.close()
    os.chdir(tempdir + "/checkout")
   

# Generated at 2022-06-13 06:10:38.683951
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    # Test if 'svn revert -R /Users/lucas/repos/test_repo' is called in the terminal
    test_module = TestModule()
    test_Subversion = Subversion(test_module, "/Users/lucas/repos/test_repo", None, None, None, None, None, None)
    saved_method = test_Subversion._exec
    test_Subversion._exec = lambda args, check_rc: "svn revert -R /Users/lucas/repos/test_repo"
    assert test_Subversion.revert()

    test_Subversion._exec = saved_method


# Generated at 2022-06-13 06:10:39.534709
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    return 'OK'


# Generated at 2022-06-13 06:10:47.882323
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    from ansible.module_utils._text import to_bytes
    import sys
    import tempfile

    if sys.version_info[0] == 2:
        result_stdout_bytes = to_bytes('''svn, version 1.10.0
        ''')
    else:
        result_stdout_bytes = '''svn, version 1.10.0
        '''.encode('utf-8')

    m = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 06:10:53.686198
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class MockModule(object):
        def run_command(args, check_rc, data=None):
            return 0, '', ''

    rev = Subversion(
        MockModule(),
        dest='/tmp/ansible', repo='/tmp/ansible',
        revision='HEAD', username=None, password=None,
        svn_path='svn', validate_certs=True
    )

    assert rev.switch() is True



# Generated at 2022-06-13 06:11:01.019173
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class MockModule:
        class MockRunCommand:
            def __init__(self):
                self._rc = 0

            def __call__(self, _, check_rc=True):
                if check_rc and self._rc != 0:
                    raise Exception('rc != 0')
                return (self._rc, 'Révision : 1889134\nURL : https://example.org/svn/repo\nAutre truc', '')

            @property
            def rc(self):
                return self._rc

            @rc.setter
            def rc(self, value):
                self._rc = value

        run_command = MockRunCommand()

    class MockSubversion:
        REVISION_RE = r'^\w+\s?:\s+\d+$'


# Generated at 2022-06-13 06:11:12.954113
# Unit test for function main

# Generated at 2022-06-13 06:11:22.260647
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    class MockModule(object):
        def run_command(self, cmd, check_rc, data=None):
            return (0, "Reverted 'a.txt'", "")

    class MockModule2(object):
        def run_command(self, cmd, check_rc, data=None):
            return (0, "", "")

    module = MockModule()
    svn = Subversion(module, "", "", "", "", "", "", False)
    assert svn.revert() == True

    module = MockModule2()
    svn = Subversion(module, "", "", "", "", "", "", False)
    assert svn.revert() == False


# Generated at 2022-06-13 06:11:28.422874
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    module = AnsibleModule(argument_spec={
        'repo': dict(type='str', required=True),
        'dest': dict(type='str')
    })
    subversion = Subversion(module, '/src/checkout', 'svn+ssh://an.example.org/path/to/repo', 'HEAD', None, None, '/usr/bin/svn', True)
    change, curr, head = subversion.needs_update()
    assert curr.split(':')[1].strip() == 'None'
    assert head.split(':')[1].strip() == 'None'
    assert not change


# Generated at 2022-06-13 06:11:47.317871
# Unit test for method update of class Subversion
def test_Subversion_update():
    module = type('TestAnsibleModule', (object,), dict(run_command=lambda *args, **kwargs: (0, "", "")))
    dest = "foo"
    repo = "bar"
    revision = "baz"
    username = "none"
    password = "none"
    svn_path = "svn"
    validate_certs = "no"
    svn = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    def mock_exec(args, check_rc=True):
        return ["no output", " ", "A  some/path/file.txt"]
    svn._exec = mock_exec
    assert svn.needs_update() == (True, 'no output', 'no output')


# Generated at 2022-06-13 06:11:53.836274
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    import tempfile
    from shutil import rmtree
    from ansible.module_utils._text import to_bytes

    check_output = lambda *args: to_bytes(args[-1], errors='surrogate_or_strict')

    class Subversion_test(Subversion):
        def _exec(self, args, check_rc=True):
            return check_output(*args)

    import subversion_test_data
    # We need a temp directory that SVN can work in
    tmp_dir = tempfile.mkdtemp()

    # Create a temporary checkout of the test repository
    repo_tmp_dir = tempfile.mkdtemp()
    svn = Subversion_test(dict(), repo_tmp_dir, "file://.git_test_repo", '', '', '', '', '')
    svn

# Generated at 2022-06-13 06:12:06.070718
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    svn = Subversion(...)

    # Test with "Revision: 1712" in svn output
    def run_fake_revision(args, check_rc=True):
        return ["", "", "Revision: 1712"]
    svn._exec = run_fake_revision
    assert svn.get_revision() == ('Revision: 1712', 'Unable to get URL')

    # Test with "Revision: 1712" on the 2nd line of svn output
    def run_fake_revision(args, check_rc=True):
        return ["", "Revision: 1712", "Something else"]
    svn._exec = run_fake_revision
    assert svn.get_revision() == ('Revision: 1712', 'Unable to get URL')


# Generated at 2022-06-13 06:12:11.227882
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule()
    svn = Subversion(module, None, 'svn+ssh://an.example.org/path/to/repo', None, None, None, 'svn')
    assert svn.get_remote_revision() == 'Unable to get remote revision'


# Generated at 2022-06-13 06:12:12.995731
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    assert not Subversion(None, None, None, None, None, None, None, None).has_local_mods()



# Generated at 2022-06-13 06:12:27.517774
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import tempfile

    def mock_run_command(*args, **kwargs):
        if args[0] in [['svn', '--non-interactive', '--no-auth-cache', 'switch', '--revision', 'HEAD', 'svn+ssh://an.example.org/path/to/repo', '/src/checkout']]:
            return 0, 'A        bins/\nA        bins/ansible\n', ''
        if args[0] in [['svn', '--non-interactive', '--no-auth-cache', 'switch', '--revision', 'HEAD', 'svn+ssh://an.example.org/path/to/repo', '/src/checkout']]:
            return 0, 'X        bins/\nX        bins/ansible\n', ''

# Generated at 2022-06-13 06:12:37.008468
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale

    def assertEqual(a, b):
        assert a == b

    def assertFalse(a):
        if a not in [None, 0, False]:
            raise AssertionError

    class R:
        def __init__(self, rc, version, err, stdout, stderr):
            self.rc = rc
            self.version = version
            self.err = err
            self.stdout = stdout
            self.stderr = stderr

        def splitlines(self):
            return self.stdout


# Generated at 2022-06-13 06:12:47.786085
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import sys

    class AnsibleModuleStub:
        def __init__(self, exit_json):
            self.exit_json = exit_json
            self._ansible_no_log_values = set()
            self.check_mode = False
            self.params = {}

        def fail_json(self, *args, **kw):
            pass

        def run_command(self, *args, **kw):
            return 0, "123", ""

    m = AnsibleModuleStub(exit_json=sys.exit)
    svn = Subversion(m, '/dest', '/repo', '123', 'user', 'pwd', 'svn', True)
    assert int(svn.get_remote_revision()) == 123


# Generated at 2022-06-13 06:12:52.085790
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # mock_data = [[0, ''''M      
    return
        

# Generated at 2022-06-13 06:13:02.257167
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    class Module:
        def run_command(self, cmd, check_rc):
            return 0, "Revision: 1889134", ""
    class Subversion_:
        def __init__(self, module, dest, repo, revision, username, password, svn_path):
            pass

    subversion = Subversion_(None, None, None, None, None, None, None)
    m = Module()
    rev, url = subversion.get_revision(m)
    assert rev == "Revision: 1889134"
    assert url == "Unable to get URL"



# Generated at 2022-06-13 06:13:26.506308
# Unit test for method update of class Subversion
def test_Subversion_update():
    class Module:
        def __init__(self):
            self.check_mode = False
            self.debug = False
            self.params = {}
            self.args = {}
            self.run_command_called = False
            self.run_command_rc = 0
            self.run_command_stdout = ''
            self.run_command_stderr = ''

        def run_command(self, cmd, **kwargs):
            self.run_command_called = True
            self.run_command_cmd = cmd
            self.run_command_kwargs = kwargs
            return self.run_command_rc, self.run_command_stdout, self.run_command_stderr

        def fail_json(self, **kwargs):
            pass


# Generated at 2022-06-13 06:13:36.848439
# Unit test for method get_revision of class Subversion

# Generated at 2022-06-13 06:13:50.489113
# Unit test for function main
def test_main():
    src = 'svn+ssh://an.example.org/path/to/repo'

# Generated at 2022-06-13 06:13:54.931323
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    test = Subversion(None, '', '', '', '', '', '', '')
    output = test._exec(["switch", "--revision", test.revision, test.repo, test.dest])
    for line in output:
        if re.search(r'^[ABDUCGE]\s', line):
            return True
    return False

# Generated at 2022-06-13 06:14:01.668726
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})

    args = [
        "/tmp/good",
        "svn://fake",
        "HEAD",
        "",
        "",
        "",
        "True",
    ]
    svn = Subversion(module, *args)
    rc = svn._exec(["checkout", "-q", "--force", "--depth", "empty", "svn://fake", "/tmp/good"], check_rc=False)
    if rc != 0:
        raise Exception("Cannot run test_Subversion_has_local_mods")
    f = open("/tmp/good/file", "w")
    f.write("content")
    f.close()

# Generated at 2022-06-13 06:14:06.364161
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    repourl = "http://example.org/path/to/repo"
    revision = "HEAD"
    svn = Subversion(None, "/src/checkout", repourl, revision, "", "", "subversion", True)
    # Get a sample output from svn info
    # Output from svn info:
    #   Path: .
    #   URL: %s
    #   Repository Root: %s...
    #   Repository UUID: .........
    #   Revision: 1889134
    #   Node Kind: directory
    #   Schedule: normal
    #   Last Changed Author: ....
    #   Last Changed Rev: 1889133
    #   Last Changed Date: 2016-11-22 15:16:09 +04:30 (Tue, 22 Nov 2016)

# Generated at 2022-06-13 06:14:17.602961
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    class Module(object):
        pass
    class RunCommand(object):
        def __init__(self):
            self.commands = []
        def __call__(self, args, check_rc=True, data=None):
            self.commands.append(args)
            return 0, 'Reverted working copy to revision', ''
    module = Module()
    module.run_command = RunCommand()
    svn = Subversion(module, '', '', '', '', '', '', False)
    # Test command
    svn.revert()
    print(module.run_command.commands)
    # Test equality
    assert module.run_command.commands == [['svn', '--non-interactive', '--no-auth-cache', 'revert', '-R', '']]
# Unit test

# Generated at 2022-06-13 06:14:22.748533
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    module = AnsibleModule({}, {})
    s = Subversion(module, '/tmp/dest', 'https://example.org/tmp/repo', 'HEAD', None, None, '/usr/bin/svn', True)
    assert s.is_svn_repo() is False


# Generated at 2022-06-13 06:14:32.257786
# Unit test for method switch of class Subversion
def test_Subversion_switch():

    def _exec(self, args, check_rc=True):
        return 0, [], None

    Subversion.update = _exec
    test = Subversion(None, '.', '.', '.', '.', '.', '.', '.')
    test.update()

if __name__ == '__main__':
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.compat import ipaddress
from ansible.module_utils.six import string_types



# Generated at 2022-06-13 06:14:41.307130
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    from ansible.module_utils.six.moves import StringIO
    module = AnsibleModule({})
    module.run_command = lambda *args, **kwargs: (0, 'Revision: 42', '')
    obj = Subversion(module, dest='/tmp', repo='svn+ssh://an.example.org/path/to/repo', revision='42', username='user', password='password', svn_path='svn', validate_certs=True)
    assert obj.get_revision() == ('Revision: 42', 'Unable to get URL')



# Generated at 2022-06-13 06:15:12.097708
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import mock
    SubversionMock = mock.Mock(Subversion)
    SubversionMock.get_remote_revision()
    assert SubversionMock.get_remote_revision()==('Unable to get remote revision',)



# Generated at 2022-06-13 06:15:20.296993
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    """Test the Subversion.has_local_mods method"""
    import tempfile
    import shutil
    import os.path
    import hashlib

    # SVN module and Subversion class must not be imported globally
    ansible_module = AnsibleModule(argument_spec={})

    # Create temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create temporary working directory for svn checkout
    wcdir = tempfile.mkdtemp()
    wc_path = os.path.join(wcdir, "wc")


# Generated at 2022-06-13 06:15:28.392850
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    import os
    import textwrap
    import tempfile
    import unittest
    import shutil
    class TestSubversion(unittest.TestCase):
        def setUp(self):
            self.dest = tempfile.mkdtemp(prefix='test-svn-', suffix='-ansible')
            test_file = os.path.join(self.dest, 'test')
            with open(test_file, 'w') as f:
                f.write('test')
            self.svn = Subversion(
                {'run_command': self.run_command, 'warn': lambda x: None},
                self.dest,
                'fake-repo',
                '3',
                None,
                None,
                'svn',
                True
            )

# Generated at 2022-06-13 06:15:37.821125
# Unit test for function main
def test_main():
    test_arguments = dict(
        dest='/home/test',
        repo='test/me',
        revision='test',
        force=False,
        username='test',
        password='test',
        executable='/path/to/svn',
        export=False,
        switch=True,
        checkout=True,
        update=True,
        in_place=False,
        validate_certs=False,
    )

# Generated at 2022-06-13 06:15:42.654002
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    """Test method revert of class Subversion"""
    svn = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    assert svn.revert() == True

# Generated at 2022-06-13 06:15:56.902459
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class MockModule(object):

        def __init__(self):
            self.check_mode = True
            self.params = dict()

        def fail_json(self, *args, **kwargs):
            raise Exception(args, kwargs)

        def run_command(self, cmd, check_rc=False):
            if self.check_mode:
                return 0, '', ''
            else:
                raise Exception('Unexpected command call')

    repo = Subversion(MockModule(), None, None, None, None, None, None, False)
    expected = 'Revision: 123'
    assert repo.get_remote_revision() == expected

    MockModule.check_mode = False
    repo = Subversion(MockModule(), None, None, None, None, None, None, False)

# Generated at 2022-06-13 06:16:05.304938
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    import unittest

    class Subversion_Mock(object):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            self.module = module
            self.dest = dest
            self.repo = repo
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path
            self.validate_certs = validate_certs

        def _exec(self, args, check_rc=True):
            return 0

    class Module_Mock(object):
        def __init__(self):
            pass

    class Run_Command_Mock(object):
        def __init__(self):
            pass


# Generated at 2022-06-13 06:16:09.168476
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    mod = None
    svn = Subversion(mod, '/home/foo/myrepo', '', '', '', '', '', '')
    assert svn.has_local_mods() == True


# Generated at 2022-06-13 06:16:17.154520
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    test_args = {'repo':'https://example.com'}

# Generated at 2022-06-13 06:16:22.863233
# Unit test for method update of class Subversion
def test_Subversion_update():
    assert Subversion(AnsibleModule(subversion),
                      dest='localhost',
                      repo='repo',
                      revision='revision',
                      username='username',
                      password='password',
                      svn_path='./',
                      validate_certs=True).update() is True


# Generated at 2022-06-13 06:17:07.001716
# Unit test for function main
def test_main():
    from ansible.constants import mk_boolean
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.modules.source_control.ansible.builtin.subversion import Subversion
    from ansible.module_utils import basic
    from ansible.module_utils.common.locale import get_best_parsable_locale
    from ansible.module_utils.compat.version import LooseVersion
    
    Repo = 'svn+ssh://org.repo.path/to/repo'
    Dest = '/src/checkout'
    Revision = 'HEAD'
    Username = None
    Password = None
    Svn_path = '/usr/bin/svn'
    Export = False
    Checkout = True
    Update = True


# Generated at 2022-06-13 06:17:18.669335
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
        class FakeModule(object):
            def __init__(self):
                self.check_mode = False
                self.params = {
                    'dest': '/path/to/repo',
                    'revision': 1,
                    'repo': 'http://svn.example.com/repo',
                    'username': '',
                    'password': '',
                }
            def fail_json(self, *args, **kwargs):
                raise AssertionError('AnsibleModule.fail_json() should not have been called.')
            def exit_json(self, *args, **kwargs):
                raise AssertionError('AnsibleModule.exit_json() should not have been called.')
            def run_command(self, args, check_rc, data=None):
                self.args = args
                # Mock

# Generated at 2022-06-13 06:17:30.261592
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    class ModuleMock:
        def __init__(self):
            self.run_command_result = ('0', r'Révision : 1889134', '')
            self.run_command_call_count = 0

        def run_command(self, command, **kwargs):
            self.run_command_call_count += 1
            return self.run_command_result

        def get_bin_path(self, executable, **kwargs):
            return executable

    class SubversionMock(Subversion):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            pass

        def has_option_password_from_stdin(self):
            return False

        def needs_update(self):
            return 2, 3

    module = ModuleMock()

# Generated at 2022-06-13 06:17:40.567293
# Unit test for method update of class Subversion

# Generated at 2022-06-13 06:17:42.286623
# Unit test for method update of class Subversion
def test_Subversion_update():
  s = Subversion(None, None, None, None, None, None, None)
  assert s.update() == True

# Generated at 2022-06-13 06:17:52.573647
# Unit test for method update of class Subversion
def test_Subversion_update():
    module = AnsibleModule(
        argument_spec=dict(
            repo=dict(required=True, type='str'),
            dest=dict(required=True, type='path'),
            revision=dict(default='HEAD', type='str'),
            force=dict(default=False, type='bool'),
            username=dict(type='str'),
            password=dict(type='str', no_log=True),
            svn_path=dict(default='svn'),
            validate_certs=dict(type='bool', default=False)
        )
    )

# Generated at 2022-06-13 06:18:01.454784
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    # Test module import
    from ansible.modules.source_control.subversion import Subversion
    
    # Create instance of Subversion
    subversion = Subversion(None, '', '', '', None, None, '', '', None)
    
    # Create a valid subversion repository
    import tempfile
    import shutil
    import subprocess
    import os

    svn_repo = tempfile.mkdtemp()

# Generated at 2022-06-13 06:18:07.669372
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    # pylint: disable=protected-access
    from ansible.module_utils._text import to_bytes
    from io import StringIO
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda x, **kwargs: (0, to_bytes(StringIO("""
Path: test
URL: http://example.com
Revision: 18
Last Changed Author: user
Last Changed Rev: 18
Last Changed Date: 2019-08-08T15:29:47.236172Z

Path: test2
URL: http://example.com/test2
Revision: 19
Last Changed Author: user2
Last Changed Rev: 19
Last Changed Date: 2019-08-09T15:29:47.236172Z
""").read()), '')

# Generated at 2022-06-13 06:18:20.436181
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    from ansible.module_utils.ansible_release import __version__
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.network.common.utils import to_list
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.connection import ConnectionError
    class Anon(object):
        pass
    module = Anon()

# Generated at 2022-06-13 06:18:20.915314
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    pass