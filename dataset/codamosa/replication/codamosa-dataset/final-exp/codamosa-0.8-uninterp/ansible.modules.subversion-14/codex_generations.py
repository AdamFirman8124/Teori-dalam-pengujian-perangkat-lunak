

# Generated at 2022-06-13 06:10:18.108511
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    repo = 'test'
    revision = 'head'
    username = 'test'
    password = 'test'
    svn_path = 'test_svn'
    validate_certs = 'test'
    dest = 'test_dest'
    svn = Subversion(None, dest, repo, revision, username, password, svn_path, validate_certs)
    svn.get_remote_revision = lambda : 'test_revision'
    assert svn.get_remote_revision() == 'test_revision'


# Generated at 2022-06-13 06:10:25.162671
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    import os
    import shutil
    import tempfile
    repo_url = 'svn://svn.red-bean.com/repos/testrepo'
    rev = '1'
    dest = tempfile.mkdtemp()

# Generated at 2022-06-13 06:10:37.273104
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    def _exec(self, args, check_rc=True):
        if args[0] == "info":
            return [
                'URL: http://example.com/svn/trunk/',
                'Repository Root: http://example.com/svn',
                'Revision: 112'
            ]
        else:
            raise RuntimeError("Unexpected command: {}".format(args))

    svn = Subversion(None, None, None, None, None, None, None, None)
    svn.get_revision = svn.get_revision.__func__
    svn._exec = _exec.__func__
    assert svn.get_revision() == ('Revision: 112', 'URL: http://example.com/svn/trunk/')



# Generated at 2022-06-13 06:10:43.778536
# Unit test for function main
def test_main():
    # Remove if the function and/or one of its dependencies doesn't use
    # ansible modules or one of its dependencies
    import ansible.modules.source_control.subversion as svn_mod

    svn_mod.main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:10:54.637717
# Unit test for method update of class Subversion
def test_Subversion_update():
    import subprocess
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale
    from ansible.module_utils.six import PY2, StringIO
    from ansible.module_utils.six.moves.urllib.error import HTTPError
    from ansible.module_utils.six.moves.urllib.request import urlopen

    subversion = Subversion()

    def _exec(args, check_rc=True):
        return subprocess.check_output(args).decode().splitlines()

    subversion._exec = _exec

    def _exec_error(args, check_rc=True):
        return subprocess.CalledProcessError(1, args)

    subversion.update

# Generated at 2022-06-13 06:11:01.712050
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import StringIO
    import sys

    print("Testing Subversion_switch")
    # make fake sys.argv
    sys.argv = ["ansible-svn", "--ask-vault-pass"]
    # capture the output
    old = sys.stdout
    sys.stdout = StringIO.StringIO()
    # execute the method 

# Generated at 2022-06-13 06:11:10.600087
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    # Very simple test. This method is already tested via Subversion_needs_update in integration tests.
    # But I keep this file in case further tests are needed.
    #
    # Example text matched by the regexp:
    #  Révision : 1889134
    #  版本: 1889134
    #  Revision: 1889134
    REVISION_RE = r'^\w+\s?:\s+\d+$'

# Generated at 2022-06-13 06:11:21.461903
# Unit test for method update of class Subversion
def test_Subversion_update():
    class MockModule():
        def __init__(self, **kwargs):
            self.run_command_return_value_args = []
            self.run_command_return_value_kwargs = []
            self.run_command_return_value = []
            self.run_command_check_rc_return_value = 0
        def run_command(self, args, data=None, check_rc=True):
            self.run_command_return_value_args.append(args)
            self.run_command_return_value_kwargs.append({"data": data, "check_rc": check_rc})
            return self.run_command_return_value, "stdout", "stderr"
    subj = Subversion(MockModule(), "/tmp", "", "", False)

# Generated at 2022-06-13 06:11:27.964434
# Unit test for function main
def test_main():
    call_function_json = {}
    call_function_kwargs = {}
    call_function_args = ()
    call_function_name = None
    call_function_class = None
    module_args = {
  "check_mode": True,
  "validate_certs": False,
  "checkout": True,
  "password": "ansible",
  "update": True,
  "switch": True,
  "in_place": False,
  "export": False,
  "revision": "HEAD",
  "repo": "svn+ssh://an.example.org/path/to/repo",
  "force": False,
  "username": "jdoe",
  "dest": "/src/export"
}
    from ansible.module_utils.basic import AnsibleModule
   

# Generated at 2022-06-13 06:11:35.297554
# Unit test for function main
def test_main():
    import os
    import shutil
    repo = 'file:///tmp/testrepo1'
    dirrepo = '/tmp/testrepo1'
    os.mkdir(dirrepo)
    dirwc = '/tmp/wc'
    svn_path = '/usr/bin/svn'
    if not os.path.exists(svn_path):
        svn_path = '/usr/local/bin/svn'
    if not os.path.exists(svn_path):
        return
    svn = Subversion(None, dirwc, repo, 'HEAD', None, None, svn_path, True)
    svn.checkout()
    os.remove('/tmp/wc/README')
    svn.update()
    svn.export(force=True)


# Generated at 2022-06-13 06:11:57.711168
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class Module(object):
        class run_command():
            @staticmethod
            def run_command(args, check_rc, data=None):
                if "switch" in args:
                    return 0, "A\nA\nA\nA\nA\n", ''
                else:
                    return 0, "Revision: 1889134", ''

    subversion = Subversion(Module(), "/home/some-place", "svn+ssh://an.example.org/path/to/repo", "HEAD", None, None, "/usr/bin/svn", "yes")
    subversion.switch()


# Generated at 2022-06-13 06:12:09.059171
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import subprocess
    import unittest
    import test.support
    import sys

    # Tested with Python 3.4.1 and Ubuntu 14.04
    # Python 3.4.1
    # --------------
    # Subversion 1.9.1
    # SVNKit 1.9.0
    # Oracle JDK 8
    #
    # Subversion 1.9.3
    # SVNKit 1.9.3
    # Apache APR 1.5.1
    # Apache APR-Util 1.5.4
    # Apache Neon 0.30.1
    # SQLite 3.8.11.1
    # Serf 1.3.8
    # ZLib 1.2.8
    # Oracle JDK 8
    #
    # Subversion 1.9.5
    # SVNKit 1.9.3

# Generated at 2022-06-13 06:12:10.060501
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    subversion = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    assert subversion.switch()

# Generated at 2022-06-13 06:12:20.655618
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    class MockModule:
        def run_command(self,args,check_rc=True,data=None):
            class MockRC:
                def __init__(self,rc):
                    self.rc = rc
            if '--version' in args:
                return MockRC(0),'1.10.0','0'
            elif 'revert' in args:
                return MockRC(0),'','0'
            elif 'status' in args:
                return MockRC(0),'','0'
            elif 'info' in args:
                if '-r' in args:
                    return MockRC(0),'','0'
                else:
                    return MockRC(0),'','0'
            else:
                return MockRC(0),'','0'
    module = MockModule()
    subversion = Sub

# Generated at 2022-06-13 06:12:30.745755
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.check_mode = False
            self.diff = False
            self.run_command_results = []

        def fail_json(self, msg):
            raise Exception("Failed during module operation: %s" % msg)

        def run_command(self, cmd, check_rc=True, data=None):
            if self.check_mode:
                return (0, "", "")
            try:
                result = self.run_command_results[0]
                self.run_command_results = self.run_command_results[1:]
            except IndexError as e:
                raise Exception("No more fake results for run_command")
            if len(result) == 2:
                (rc, out) = result


# Generated at 2022-06-13 06:12:35.075288
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    module = AnsibleModule({})
    s = Subversion(module, ".", ".", "HEAD", "user", "pass", "svn", True)
    assert not s.has_local_mods()


# Generated at 2022-06-13 06:12:37.412700
# Unit test for method update of class Subversion
def test_Subversion_update():
    svn = Subversion(None, None, None, None, None, None, None, None)
    assert svn.update() == True



# Generated at 2022-06-13 06:12:39.207174
# Unit test for method update of class Subversion
def test_Subversion_update():
  instance = Subversion()
  assert instance.update() == True


# Generated at 2022-06-13 06:12:51.052762
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    class MockSubversion(Subversion):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            pass
        def _exec(self, args, check_rc=True):
            if len(args) == 3:
                if args[2] == 'dest':
                    return ['R  mod.txt', 'R  new.txt']
                elif args[2] == 'dest2':
                    return ['? unver.txt', 'R  mod.txt', 'R  new.txt']
                elif args[2] == 'dest3':
                    return ['X  mod.txt', '^? unver.txt', 'R  mod.txt', 'R  new.txt']

# Generated at 2022-06-13 06:13:05.145938
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    svn = Subversion(None, "foo", "bar", None)
    svn.has_option_password_from_stdin = lambda: True
    # ----- Test with 0 modified revisioned files ----
    # Mock the _exec() method
    def _exec(args, check_rc=True):
        # Return 0 modified revisioned files
        return ["A file1", "D file2"]

    svn._exec = _exec
    assert svn.has_local_mods() is False
    # ----- Test with 1 modified revisioned file ----
    # Mock the _exec() method
    def _exec(args, check_rc=True):
        # Return 1 modified revisioned file
        return ["A file1"]

    svn._exec = _exec
    assert svn.has_local_mods() is True
    # ----- Test with 2 modified

# Generated at 2022-06-13 06:13:21.429704
# Unit test for method update of class Subversion
def test_Subversion_update():
    assert Subversion(
        module=None,
        dest='',
        repo='',
        revision='',
        username='',
        password='',
        svn_path='',
        validate_certs='').update()


# Generated at 2022-06-13 06:13:28.478615
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class TestModule(object):
        def run_command(self, args, check_rc=True, data=None):
            return 0, "Révision : 45\nURL      : https://www.example.com/bar/\n", ""
    revision = "HEAD"
    repo = "https://www.example.com/foo/"
    dest = "/tmp/my_module_test/"
    module = TestModule()
    svn_obj = Subversion(module, dest, repo, revision, username=None, password=None, svn_path="svn", validate_certs=False)
    assert svn_obj.get_remote_revision() == "Révision : 45"


# Generated at 2022-06-13 06:13:38.182317
# Unit test for method update of class Subversion
def test_Subversion_update():
    class module:
        def __init__(self):
            self.params = {'repo': 'svn+ssh://an.example.org/path/to/repo',
                           'dest':'/src/checkout',
                           'revision':'3.0.0',
                           'username':'mathieu.fenniak',
                           'password':'password'}
            self.check_mode = False

    class ansible_module:
        def __init__(self):
            self.run_command = run_command

    def run_command(self, bits, check_rc, data=None):
        return 0, '''A    file1
        A    file2
        A    file3
        A    file4
        U    file5''', ''


# Generated at 2022-06-13 06:13:51.647438
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule

    file, path = tempfile.mkstemp()
    try:
        sc = Subversion(
            AnsibleModule(
                argument_spec={
                    'path': {
                        'required': False,
                        'type': 'str',
                        'default': path,
                    },
                },
            ),
            path,
            'repo',
            'revision',
            'username',
            'password',
            'svn',
            'no',
        )
        assert not sc.has_local_mods()
        os.write(file, b'FOO')
        assert sc.has_local_mods()
    finally:
        os.close(file)
        os.unlink(path)


# Generated at 2022-06-13 06:13:52.712700
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:14:00.039631
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    # set up test
    module = AnsibleModule(argument_spec={})
    destination = "tests/destination"
    revision = "18000"
    svn_path = "tests/svn"
    repo = "tests/repo"
    username = None
    password = None
    validate_certs = False
    svn = Subversion(module, destination, repo, revision, username, password, svn_path, validate_certs)
    # run test
    revision, url = svn.get_revision()
    expected_revision = "Revision: 18000"
    expected_url = "URL: file:///tests/repo"
    # assert
    assert revision == expected_revision
    assert url == expected_url


# Generated at 2022-06-13 06:14:10.064005
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    class Subversion:
        import re
        import os
        import shutil
        print("unit test for Subversion method revert")
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
            '''Execute a subversion command, and return output. If check_rc is False, returns the return code instead of the output.'''
            bits = []
            stdin_data = None
            rc, out,

# Generated at 2022-06-13 06:14:19.915731
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    Subversion.REVERT = "revert"

    class TestModule():
        def run_command(self,
                        args,
                        check_rc=True,
                        data=None):
            assert(args == [Subversion.svn_path,
                            '--non-interactive',
                            '--no-auth-cache',
                            '--trust-server-cert',
                            Subversion.REVERT,
                            '-R',
                            dest])
            return 0, output, ""

    class TestObj():
        ip_addresses_curr = None
        ip_addresses_prev = None
        changed = True
        result = {}

        def get_remote_revision(self):
            return None

        def get_revision(self):
            return None


# Generated at 2022-06-13 06:14:32.158743
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    results = []
    module = AnsibleModule(
        argument_spec=dict(
            repo=dict(required=True, type='str'),
            dest=dict(required=False, type='str', default='/tmp/ansible_test'),
            revision=dict(required=False, type='str', default='HEAD'),
            username=dict(required=False, type='str', default='anonymous'),
            password=dict(required=False, type='str', default='', no_log=True),
            svn_path=dict(required=False, type='str', default='svn'),
            validate_certs=dict(required=False, type='bool', default=False)
        )
    )


# Generated at 2022-06-13 06:14:43.536794
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    repo = "https://github.com/ansible/ansible.git"
    revision = "9be9feba9b2a395df7104b2dcbb79ed3e3f39e79"
    dest = "./test_Subversion_needs_update"

# Generated at 2022-06-13 06:15:19.807570
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import unittest
    import contextlib
    import types
    class MockRunCommand(object):
        def __init__(self):
            self.calls = []
            self.run_command_return_values = []
            self.run_command_check_rc = []
            self.run_command_data = []
        def run_command(self, args, check_rc, data):
            self.calls.append(args)
            self.run_command_check_rc.append(check_rc)
            self.run_command_data.append(data)
            return self.run_command_return_values.pop(0)
    class MockModule(object):
        def __init__(self):
            self._run_command = MockRunCommand()
        @property
        def run_command(self):
            return

# Generated at 2022-06-13 06:15:28.365113
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    """
    This methods test the get_revision method of class Subversion
    """
    mock_module = AnsibleModule(argument_spec={})

    test_info = [
        {"revision":"Revision: 1889134","url":"URL: https://github.com/ansible/ansible.git"},
        {"revision":"Révision : 1889134","url":"URL: https://github.com/ansible/ansible.git"},
        {"revision":" 版本: 1889134","url":"URL: https://github.com/ansible/ansible.git"},
        {"revision":"Unable to get revision","url":"Unable to get URL"},
        ]

# Generated at 2022-06-13 06:15:37.808664
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    """
    Test revert method of Subversion class.

    Test description
    ----------------
    The revert method calls the 'svn revert' command on the destination folder. We implement a class method in the
    Subversion class which returns the value of the output of 'svn revert' on the destination folder. We then assert that
    this method returns the expected value for the given inputs.
    """
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.compat import LooseVersion
    from ansible.module_utils.compat import _SUBPROCESS_SUBPROCESS_HAS_RUN, _SUBPROCESS_RUN_OUTPUT_IS_BYTES


# Generated at 2022-06-13 06:15:41.096480
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    s = Subversion()
    rev1 = 'Revisionii:  1888888'
    rev2 = 'Revisionii:  1889889'

    # a>b
    assert s.needs_update(rev1, rev2)

    # a=b
    assert not s.needs_update(rev1, rev1)



# Generated at 2022-06-13 06:15:45.999977
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    module = AnsibleModule(argument_spec={})
    svn = Subversion(module, '', '', '', '', '', '/usr/bin/svn', 'yes')
    assert not svn.has_option_password_from_stdin()
    svn = Subversion(module, '', '', '', '', '', '/usr/bin/svn', 'no')
    assert not svn.has_option_password_from_stdin()



# Generated at 2022-06-13 06:15:50.632547
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    return_value = None
    # TODO: write the real test
    if return_value == None:
        # TODO: raise an error if cannot get the answer (it should be obvious)
        return None
    return return_value


# Generated at 2022-06-13 06:15:58.680723
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    module = AnsibleModule({})
    dest = ""
    repo = ""
    revision = ""
    username = ""
    password = ""
    svn_path = ""
    validate_certs = ""

    test_object = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)

    # Test when there is a change in the svn working directory
    assert test_object.switch() == True
    # Test when there is no change in the svn working directory
    assert test_object.switch() == False


# Generated at 2022-06-13 06:16:01.477819
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # https://docs.python.org/3/library/unittest.mock.html
    l = [
        "AnsibleModule", "run_command",
        "exit_json", "warn",
    ]
    # set alias for AnsibleModule
    # mock AnsibleModule.run_command
    # mock AnsibleModule.exit_json
    # ...
    # ...


# Generated at 2022-06-13 06:16:12.099172
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    module = AnsibleModule(argument_spec={})
    dest = "/tmp/ansible"
    repo = "svn+ssh://an.example.org/path/to/repo"
    revision = "HEAD"
    username = None
    password = None
    svn_path = "svn"
    validate_certs = "no"
    svn = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    assert svn.get_revision() == ('Unable to get revision', 'Unable to get URL')


# Generated at 2022-06-13 06:16:18.574115
# Unit test for method has_option_password_from_stdin of class Subversion

# Generated at 2022-06-13 06:17:18.197382
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    svn_repo = Subversion(None, '', '', '', '', '', '', False)
    assert svn_repo.has_option_password_from_stdin() == True




# Generated at 2022-06-13 06:17:29.798374
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    import tempfile
    import shutil
    import subprocess
    # Create a scratch directory
    test_base_dir = tempfile.mkdtemp()
    # Checkout a working directory
    subprocess.Popen(['svn', 'checkout', 'https://www.python.org/doc/', test_base_dir]).communicate()
    # Create a new file
    new_file = os.path.join(test_base_dir, 'new_file.txt')
    with open(new_file, 'w') as f:
        f.write('test')
    # Test that the new file is considered modified
    subversion = Subversion('', test_base_dir, '', '', '', '', 'svn', '')
    assert subversion.has_local_mods() is True
    # Clean the temp directory
   

# Generated at 2022-06-13 06:17:37.138116
# Unit test for method update of class Subversion
def test_Subversion_update():
    try:
        svn = Subversion(
            module=MockModule(),
            dest='/tmp/test_svn',
            repo='svn://test_svn_server/tmp/test_repo',
            revision='HEAD',
            username='test_svn_user',
            password='test_svn_pass',
            svn_path='/usr/bin/svn',
            validate_certs=False)
    except Exception:
        raise
    assert svn.update() is True


# Generated at 2022-06-13 06:17:40.307954
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    subversion = Subversion(AnsibleModule(argument_spec={}), '', '', '', '', '', 'svn', False)
    assert subversion.has_option_password_from_stdin() == False



# Generated at 2022-06-13 06:17:47.187568
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    class FakeModule(object):
        def __init__(self):
            self.run_command_ran = False
            self.run_command_called = False
            self.run_command_return = None
            self.run_command_check_rc = True
            self.run_command_cmd = None
            self.params = dict()
            self.called = ''
            self.warned = False

        def run_command(self, cmd, check_rc=None, data=None):
            self.run_command_called = True
            self.run_command_cmd = cmd
            if check_rc is not None:
                self.run_command_check_rc = check_rc
            return self.run_command_return


# Generated at 2022-06-13 06:17:57.590916
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class MockModule(object):
        def __init__(self):
            self.params = {
                'repo':'svn+ssh://an.example.org/path/to/repo',
                'dest':'/src/checkout',
                'revision': 'HEAD',
                'username': None,
                'password': None,
                'svn_path': 'svn',
                'validate_certs': False
            }
            self.check_mode = False
            self.changed = False
            self.result = dict()


# Generated at 2022-06-13 06:18:00.982833
# Unit test for method update of class Subversion
def test_Subversion_update():
    answer = Subversion.update("/Users/user1/Documents/GitHub/ansible/lib/ansible/modules/packaging/language_pkgs/test/test_update_test.py")
    if answer == True:
        print("Test successful")
    else:
        print("Test unsuccessful")


# Generated at 2022-06-13 06:18:05.527526
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    module = AnsibleModule(argument_spec=dict(
        dest=dict(required=False, default='/path/dest'),
        repo=dict(required=False, default='/path/repo'),
        revision=dict(required=False, default='xxx'),
    ))
    subversion = Subversion(module, 'dest', 'repo', 'revision', None, None, 'svn', None)
    assert subversion.get_revision() == ('Unable to get revision', 'Unable to get URL')

# Generated at 2022-06-13 06:18:19.617738
# Unit test for function main
def test_main():
    # Test 1: test when there is an error when a directory already exists, but
    # is not a subversion repository.
    src_dir = '/tmp/ansible_svn_test'
    repo = 'https://github.com/ansible/ansible'
    dest = '/tmp/ansible_svn_test/ansible'
    revision = 'HEAD'
    force = False
    username = None
    password = None
    svn_path = 'svn'
    export = False
    switch = True
    checkout = True
    update = True
    in_place = False
    validate_certs = False


# Generated at 2022-06-13 06:18:28.210508
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    # Arrange
    class MockedModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.check_mode = False

        def fail_json(self, **kwargs):
            self.rc = kwargs['rc']
            raise Exception('Fail json command')

        def run_command(self, args, check_rc=True, data=None):
            return ('0', 'Remote xml version: 10', '')

    m = MockedModule()
    subversion = Subversion(m, '', '', '', '', '', '', False)
    # Act
    actual = subversion.get_remote_revision()
    # Assert
    expected = "Remote xml version: 10"
    assert expected == actual
