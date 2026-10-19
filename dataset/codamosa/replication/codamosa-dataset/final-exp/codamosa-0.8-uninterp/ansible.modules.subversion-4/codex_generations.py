

# Generated at 2022-06-13 06:10:16.304991
# Unit test for method update of class Subversion
def test_Subversion_update():
    dest = os.environ.get('TEST_SUBSVN_DEST')
    repo = os.environ.get('TEST_SUBSVN_REPO')
    if dest is None or repo is None:
        return True

    svn = Subversion(None, dest, repo, "HEAD", None, None, None, None)
    if svn.update() == True:
        return True
    return False


# Generated at 2022-06-13 06:10:21.216515
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    subversion = Subversion(None, None, None, None, None, None, None)
    subversion.get_revision = lambda: [ "Revision: 42", "URL: http://example.org/svn/test" ]
    subversion._exec = lambda x: "Revision: 43"
    assert subversion.needs_update() == (True, "Revision: 42", "Revision: 43")


# Generated at 2022-06-13 06:10:26.714493
# Unit test for method update of class Subversion
def test_Subversion_update():
    mock_module = MagicMock()
    mock_module.run_command = MagicMock(return_value=(0, "", ""))
    Subversion(mock_module, "", "", "", "", "", "svn").update()
    mock_module.run_command.assert_called_with(['svn', 'update', '-r', '', ''], True, None)



# Generated at 2022-06-13 06:10:38.905601
# Unit test for method update of class Subversion
def test_Subversion_update():
    module = AnsibleModule(argument_spec={})
    dest = "test_dest"
    repo = "test_repo"
    revision = "test_revision"
    username = "test_username"
    password = "test_password"
    svn_path = "test_svn_path"
    validate_certs = False

    test_svn = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs=validate_certs)

    # Test 1: valid output
    module.run_command = mock_run_command_valid_out_update
    assert test_svn.update()
    # Test 2: invalid output
    module.run_command = mock_run_command_invalid_out_update
    assert not test_svn.update()

#

# Generated at 2022-06-13 06:10:49.084823
# Unit test for method update of class Subversion
def test_Subversion_update():
    class AnsibleModule(object):

        def run_command(self, cmd, check_rc, data):
            if check_rc:
                return 0, "R  blah blah blah\nA  blah blah blah", None
            else:
                return 0, "", None

    class FakeModule(object):
        """
        This class is used for faking an instance of the AnsibleModule class
        for testing purposes
        """

        def __init__(self):
            self.params = {}
            self.fail_json = lambda **kwargs: False
            self.warn = lambda **kwargs: False


# Generated at 2022-06-13 06:10:58.190126
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.subversion import Subversion
    import os

    # The mod_mock_base class does not handle creating attributes on modules.
    # Build a class that handles this and extend it.
    class AnsibleModuleMock(AnsibleModule):

        def __init__(self, **kwargs):
            super(AnsibleModuleMock, self).__init__(**kwargs)
            self.check_mode = False

        # Override the exit_json method to just return the data
        def exit_json(self, **kwargs):
            return kwargs


# Generated at 2022-06-13 06:11:06.675299
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    curr = 'Revision: 1'
    curr_rev = int(curr.split(':')[1].strip())
    result = []
    for i in range(1, 4):
        head = 'Revision: ' + str(i)
        head_rev = int(head.split(':')[1].strip())
        # Compare
        if curr_rev < head_rev:
            result.append((True, curr, head))
    # Test result
    assert result == [
        (True, 'Revision: 1', 'Revision: 2'),
        (True, 'Revision: 1', 'Revision: 3'),
    ]


# Generated at 2022-06-13 06:11:08.380162
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    """Unit test stub."""
    pass


# Generated at 2022-06-13 06:11:15.685832
# Unit test for method update of class Subversion
def test_Subversion_update():
    import unittest
    import mock
    mock_module = mock.Mock()
    mock_module.run_command.return_value = (0, "", "")
    mock_module.check_mode = False

    svn = Subversion(mock_module, "/path/to/repo", "svn+ssh://an.example.org/path/to/repo", "HEAD", None, None, "svn", None)
    rc = svn.update()
    assert rc == True



# Generated at 2022-06-13 06:11:24.915495
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    import unittest
    import unittest.mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale

    def mock_run_command(cmd, check_rc=True, data=None):
        return 0, 'Reverted /home/tester\n', 'Reverted /home/tester\n'

    def mock_get_best_parsable_locale():
        return 'en_US'

    # mock run_command

# Generated at 2022-06-13 06:11:42.498153
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    import sys
    # On Windows (Python 3.7.2), output gets written to sys.stderr, so set it to sys.stdout
    # so that we can capture it.
    sys.stderr = sys.stdout
    assert Subversion._exec(None, []) == ['Unable to get revision']



# Generated at 2022-06-13 06:11:47.189286
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    # We test for a repo which is outside of the current working tree
    svn = Subversion(module=None, dest='/tmp/ansible-test', repo=None, revision=None, username=None, password=None, svn_path='/usr/bin/svn', validate_certs=False)
    assert (svn.is_svn_repo() == False), 'is_svn_repo should return False'
    # We test for a repo which is inside the current working tree
    svn = Subversion(module=None, dest='.', repo=None, revision=None, username=None, password=None, svn_path='/usr/bin/svn', validate_certs=False)

# Generated at 2022-06-13 06:11:53.645410
# Unit test for method update of class Subversion
def test_Subversion_update():
    import time
    import tempfile
    import shutil
    import sys
    import subprocess
    from ansible.module_utils.basic import AnsibleModule

    # since we don't know where to find svn, see if we can run it from
    # the user's path
    p = subprocess.Popen(['svn', '--version', '--quiet'], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    rc = p.wait()
    if rc != 0:
        sys.exit(3)
    svn_path = 'svn'

    class Args(object):
        repo = 'svn://localhost/netzob/trunk'
        dest = tempfile.mkdtemp()
        revision = 'HEAD'
        username = None
        password = None


# Generated at 2022-06-13 06:11:57.399067
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    subversion = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    assert subversion.revert() == False


# Generated at 2022-06-13 06:12:08.751925
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    module = MockAnsibleModule(argument_spec={
        'repo': dict(required=True, type='str'),
        'dest': dict(required=True, type='str'),
        'username': dict(required=False, type='str'),
        'password': dict(required=False, type='str'),
        'executable': dict(required=False, type=str),
        'revision': dict(required=False, type='str'),
        'validate_certs': dict(required=False, type='bool'),
    })
    svn = Subversion(module, "/tmp/foo", "svn+ssh://an.example.org/path/to/repo", "1893424", "user", "password", "svn", True)

# Generated at 2022-06-13 06:12:16.669690
# Unit test for function main
def test_main():
    if not __salt__['config.option']("with_test"):
        return None
    # Source the real module
    module = importlib.import_module("ansible.modules.system.subversion")
    # Hide the real module so it doesn't conflict with our test version
    importlib.reload(sys.modules["ansible.modules.system.subversion"])
    # Load our test-only module
    sys.modules["ansible.modules.system.subversion"] = importlib.import_module("tests.unit.modules.ansible_collections.source_control.subversion.ansible_collections.source_control.subversion.subversion")
    sys.modules["ansible.modules.system.subversion"].__salt__ = __salt__

# Generated at 2022-06-13 06:12:29.899247
# Unit test for method update of class Subversion
def test_Subversion_update():
    import os, unittest
    from ansible.module_utils.basic import AnsibleModule

    class TestSubversion(unittest.TestCase):

        def setUp(self):
            SVN_PATH = os.getenv('SVN_PATH', 'svn')
            SVN_TEST_REPO = os.getenv('SVN_TEST_REPO')
            SVN_TEST_REPO_USER = os.getenv('SVN_TEST_REPO_USER')
            SVN_TEST_REPO_PASS = os.getenv('SVN_TEST_REPO_PASS')

            if not SVN_TEST_REPO:
                self.fail('Missing SVN_TEST_REPO environment variable')

            self.repo = SVN_TEST_REPO



# Generated at 2022-06-13 06:12:43.616975
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    class Object(object):
        def __init__(self, out, err):
            self.out = out
            self.err = err
    class MockModule(object):
        def run_command(self, command, check_rc):
            if command.startswith('svn info'):
                output = 'Revision: 1889134\n'
            else:
                output = 'URL: http://svn.example.org/project/trunk\n'
            return Object(output, '')
    # Make one instance of FakeModule
    m = MockModule()
    # Make one instance of Subversion
    s = Subversion(m, '', '', '', '', '', '', '')
    # Test
    rev, url = s.get_revision()
    assert rev == 'Revision: 1889134'

# Generated at 2022-06-13 06:12:45.312923
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    Subversion.revert(self)

# Generated at 2022-06-13 06:12:48.075400
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    assert Subversion_instance.get_remote_revision() == 'Revision: 1889134'

# Generated at 2022-06-13 06:13:12.792550
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    pass

# Generated at 2022-06-13 06:13:20.654112
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    # Initialize Subversion object with destination path
    repo = Subversion(dest='')
    # Status with no local mods should return an empty list
    status_nomods = ['']
    assert not repo.has_local_mods(status_nomods)
    # Status with local mods should return a non-empty list
    status_mods = ['  C foo.txt']
    assert repo.has_local_mods(status_mods)



# Generated at 2022-06-13 06:13:27.859768
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    module = AnsibleModule(argument_spec=dict(
        dest=dict(),
        repo=dict(),
        revision=dict(),
        username=dict(),
        password=dict(),
        svn_path=dict(),
        force=dict(),
        in_place=dict(),
        executable=dict(),
        checkout=dict(),
        update=dict(),
        export=dict(),
        switch=dict(),
        validate_certs=dict(),
    ))
    subversion = Subversion(module, dest='', repo='', revision='', username='', password='', svn_path='', validate_certs=True)
    assert subversion.revert() == True


# Generated at 2022-06-13 06:13:37.755449
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import tempfile
    import shutil
    import ansible.utils
    import ansible.errors

    class AnsibleModuleMock:
        def __init__(self):
            self.params = {}

        def run_command(self, args, check_rc=True, data=None):
            print(args)
            if args[-2] == 'info':
                text = '\n'.join([
                    'Revision: 2',
                    'URL: http://localhost/svn/repo',
                ])
                if self.params['check_mode']:
                    print(text)
                return 0, text, ''
            raise OSError(123, 'Command execution failed')

        def fail_json(self, **msg):
            raise ansible.errors.AnsibleError(msg)


# Generated at 2022-06-13 06:13:51.471607
# Unit test for method update of class Subversion
def test_Subversion_update():
    class mock_run_command:
        def __init__(self, module):
            pass
        def __call__(self, args, check_rc=True, data=None):
            return 0, "A       .\nA       file.txt\nA       subdir\nA       subdir/file2.txt\nA       subdir/subsubdir\nA       subdir/subsubdir/file3.txt\n", ""

    class mock_module:
        def __init__(self):
            self.run_command = mock_run_command(self)
        def __call__(self):
            return self
        def fail_json(self, *args):
            self.error = args[0]

    module = mock_module()

# Generated at 2022-06-13 06:14:03.245492
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    module = AnsibleModule(argument_spec=dict(
        repo=dict(aliases=['name', 'repository'], required=True),
        dest=dict(),
        revision=dict(aliases=['rev', 'version'], default='HEAD'),
        force=dict(type='bool', default=False),
        in_place=dict(type='bool', default=False),
        username=dict(),
        password=dict(),
        executable=dict(),
        checkout=dict(type='bool', default=True),
        update=dict(type='bool', default=True),
        export=dict(type='bool', default=False),
        switch=dict(type='bool', default=True),
        validate_certs=dict(type='bool', default=False),
    ))

    dest = '/test/dest'

# Generated at 2022-06-13 06:14:08.555022
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    module = AnsibleModule(argument_spec={})
    subversion = Subversion(module,
                            'dest',
                            'repo',
                            'revision',
                            'username',
                            'password',
                            'svn_path',
                            'validate_certs')
    subversion.get_remote_revision()


# Generated at 2022-06-13 06:14:18.850061
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    m = MockModule()
    svn = Subversion(m, '/path/to/repo', 'svn+ssh://an.example.org/path/to/repo', 'HEAD', 'username', 'password', '/path/to/svn', False)
    # AnsibleModule calls run_command with this data, so simulate that here
    # Make sure to not mutate the response.
    # Also, use deepcopy() instread of copy.copy() because os.environ is a dict subclass
    import copy
    e = copy.deepcopy(m.environ)
    # simulate pre-1.10.0
    e['SVN_VERSION_MINOR_UNIFIED'] = '9'
    m.environ = e
    assert not svn.has_option_password_from_stdin()
    # simulate 1.10

# Generated at 2022-06-13 06:14:29.221922
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    subversion = Subversion(None, '/tmp/test/repo', 'svn+ssh://an.example.org/path/to/repo', 'HEAD', None, None, '/usr/bin/svn', False)
    subversion._exec = mock_exec_info
    subversion.get_revision = mock_get_revision_test_needs_update
    change, curr, head = subversion.needs_update()
    assert change == True
    assert curr == 'Revision: 123'
    assert head == 'Revision: 124'


# Generated at 2022-06-13 06:14:41.790708
# Unit test for method update of class Subversion
def test_Subversion_update():
    import os
    import tempfile
    import json
    import shutil
    import subprocess
    import platform

    def sub_process_call(args, cwd):
        return subprocess.call(args, cwd=cwd)

    workingDir = tempfile.mkdtemp()
    srv_workingDir = tempfile.mkdtemp()
    local_repo = workingDir + '/repo'
    srv_repo = srv_workingDir + '/repo'
    repo_url = 'file://' + srv_repo

    os.mkdir(local_repo)
    os.mkdir(srv_repo)

    sub_process_call(['svnadmin', 'create', srv_repo], cwd=srv_workingDir)

# Generated at 2022-06-13 06:15:41.098908
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    M = MagicMock()
    m = Subversion(M, "C:\\dest", "repo", "revision", "username", "password", "svn_path")
    m._exec = MagicMock()
    m._exec.return_value = [
        "A       svn_demo/index.html",
        "A       svn_demo/test.txt"
    ]
    assert m.switch()
    m._exec.return_value = [
        "R       svn_demo/index.html"
    ]
    assert m.switch()
    m._exec.return_value = [
        "Updated to revision 1.3."
    ]
    assert not m.switch()


# Generated at 2022-06-13 06:15:46.229236
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class SubversionTest(Subversion):

        class ModuleTest(object):

            def __init__(self, rc, out, err):
                self.rc = rc
                self.out = out
                self.err = err

            def run_command(self, cmd, check_rc=True, data=None):
                return self.rc, self.out, self.err

        def __init__(self, module, dest, repo, revision, username, password, svn_path):
            self.module = module
            self.dest = dest
            self.repo = repo
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path


# Generated at 2022-06-13 06:15:51.965072
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    subversion = Subversion(None,  '.', '.', '1', None, None, 'svn', False)
    def mock_exec(self, arg, check_rc=True):
        return []
    Subversion._exec = mock_exec
    assert subversion.revert() == True


# Generated at 2022-06-13 06:15:58.598268
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class Module(object):
        pass
    module = Module()
    module.run_command = lambda x, check_rc=True: (0, 'foo: 123', None)
    module.warn = lambda x: None
    svn = Subversion(module, 'dest', 'repo', 'revision', 'username', 'password', svn_path='svn', validate_certs=False)
    assert svn.get_remote_revision() == 'foo: 123'


# Generated at 2022-06-13 06:16:06.540388
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    '''Unit test'''
    class MockModule: # pylint: disable=R0903
        '''Mock class'''
        def __init__(self):
            self.params = {}
        # pylint: disable=C0103,W0613
        def run_command(self, args, check_rc=True, data=None):
            '''Mock run_command'''
            output_file = args[-1] + '/output.txt'
            file_object = open(output_file)
            try:
                return 0, file_object.read(), None
            finally:
                file_object.close()

# Generated at 2022-06-13 06:16:15.794933
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    import unittest
    import io
    import mock
    class myfile(io.FileIO):
        def __init__(self):
            self.data = ''
    class TestSubversion(unittest.TestCase):
        def test_revert(self):
            svn = Subversion(None, '.', '.', '1', '', '', 'svn', 'yes')
            svn._exec = mock.MagicMock(return_value=['Reverted 1'])
            self.assertEqual(svn.revert(), False)
            svn._exec = mock.MagicMock(return_value=['Reverted '])
            self.assertEqual(svn.revert(), True)
    unittest.main()


# Generated at 2022-06-13 06:16:17.067146
# Unit test for method update of class Subversion
def test_Subversion_update():
    assert(Subversion.update(self)==None)


# Generated at 2022-06-13 06:16:17.772219
# Unit test for method update of class Subversion
def test_Subversion_update():
    pass

# Generated at 2022-06-13 06:16:28.762543
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    mock_module = AnsibleModule(argument_spec={})
    svn = Subversion(mock_module, '/dest', 'http://example.com/repo', '2', 'username', 'password', '', True)
    assert svn.get_revision() == ('Revision\xa0: 1', 'URL: http://example.com/repo')
    assert svn.get_revision() == ('Revision : 1', 'URL: http://example.com/repo')
    assert svn.get_revision() == ('Edition\xa0: 1', 'URL: http://example.com/repo')
    assert svn.get_revision() == ('Edition : 1', 'URL: http://example.com/repo')

# Generated at 2022-06-13 06:16:41.129943
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    from ansible.module_utils.six import StringIO

    class Module(object):
        def __init__(self):
            self.run_command_calls = []
            self.tmpdir = '/tmp/ansible-test-dir'
            os.makedirs(self.tmpdir)

        def run_command(self, cmd, check_rc=True, data=None):
            cmd_str = ' '.join([str(c) for c in cmd])
            self.run_command_calls.append(cmd_str)
            if cmd_str.endswith('info /tmp/ansible-test-dir'):
                return (0, StringIO(u'URL: svn+ssh://an.example.org/path/to/repo\n'), '')

# Generated at 2022-06-13 06:17:58.026210
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    mod = AnsibleModule({'dest':'/tmp/svn_module_test_module_get_remote_revision',
                         'repo':'svn://svn.zope.org/repos/main/ZConfig/trunk',
                         'revision':None,
                         'checkout':False,
                         'update':False,
                         'force':False,
                         'executable':'svn'}, check_invalid_arguments=False)

    svn = Subversion(mod, '/tmp/svn_module_test_module_get_remote_revision', 'svn://svn.zope.org/repos/main/ZConfig/trunk', None, None, None, 'svn', None)
    expected = "Revision: 380232"
    actual = svn.get_remote_revision()


# Generated at 2022-06-13 06:18:05.691110
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.modules.source_control import subversion

    subversion.Subversion = DummySubversion

# Generated at 2022-06-13 06:18:19.848100
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile

    repo = tempfile.mkdtemp() + '/test'
    dest = tempfile.mkdtemp() + '/test'

    module = AnsibleModule(
        argument_spec={})
    svn = Subversion(module, repo, repo, None, None, None, 'svn', False)

    svn._exec(['init', '-q', repo])
    svn._exec(['co', '-q', repo, dest])
    with open(dest + '/test', 'w') as f:
        f.write('test')
    svn._exec(['add', '-q', dest + '/test'])
    svn._exec(['ci', '-q', '-m', 'version 1', dest])


# Generated at 2022-06-13 06:18:29.373478
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    import unittest.mock as mock
    def side_effect(args, check_rc):
        lines = [
            'Révision : 1889134',
            'URL : https://svn.test.tld/repo',
        ]
        if args == ['-r', 'HEAD', '/tmp/src']:
            lines = [
                'Révision : 1888542',
            ]
        if check_rc:
            return lines
        else:
            return 0, '', ''
    mock_module = mock.Mock()
    mock_module.run_command.side_effect = side_effect

    svn = Subversion(mock_module, '/tmp/src', 'some_repo_url', 'some_repo_revision', '', '', 'svn', False)

    actual = sv

# Generated at 2022-06-13 06:18:39.793175
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    import tempfile
    import os.path
    import shutil
    import subprocess
    import sys
    def _display_error(string):
        sys.stderr.write(string + '\n')
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 06:18:46.207474
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class AnsibleResponse:
        def __init__(self,rc,out,err):
            self.rc = rc
            self.stdout = out
            self.stderr = err
    class AnsibleModule:
        def __init__(self,mod_args):
            self.params = mod_args

# Generated at 2022-06-13 06:18:57.627872
# Unit test for function main
def test_main():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w') as temp:
        temp.write('#!/usr/bin/env python\n')
        temp.write('import sys, yaml\n')
        temp.write('print yaml.safe_dump(dict(changed=True, before="head", after="repo"))\n')
        temp.flush()
        import ansible.constants
        ansible.constants.CONFIG_FILE = temp.name
        import ansible.cli
        import ansible.cli.playbook
        import ansible.playbook
        import ansible.playbook.play
        from ansible.playbook.play_context import PlayContext
        import ansible.plugins

# Generated at 2022-06-13 06:19:08.600007
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    # Test case when local modifications exist
    class ModulesMock:
        def __init__(self):
            self.params = {
                'dest': '/home/test/test_git',
                'repo': 'https://github.com/ansible/test',
                'executable': 'python',
                'revision': 'HEAD'}
            self.check_mode = None
            self.debug = True
            self.diff = None
            self.file_mtime = None
            self.new_cmd_found = True
            self.run_command_environ_update = {}

        def run_command(self, cmd, check_rc, data=None):
            return 0, 'X    test.txt', ''
    modules = ModulesMock()

# Generated at 2022-06-13 06:19:16.461086
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    # Test 1: get_revision that retrieves the revision
    text = 'Révision : 1889134'
    obj = Subversion(None, None, None, None, None, None)
    rev = re.search(obj.REVISION_RE, text, re.MULTILINE)
    assert(rev)
    assert(rev.group(0) == text)
    # Test 2: get_revision that does not retrieve the revision
    text = 'Revision: 1889134'
    obj = Subversion(None, None, None, None, None, None)
    rev = re.search(obj.REVISION_RE, text, re.MULTILINE)
    assert(not rev)

# Generated at 2022-06-13 06:19:27.550114
# Unit test for function main