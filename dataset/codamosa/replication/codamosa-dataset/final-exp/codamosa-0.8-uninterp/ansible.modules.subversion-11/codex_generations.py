

# Generated at 2022-06-13 06:10:29.785952
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    revision = 'HEAD'
    # create a temp dir for the tests
    import tempfile
    tmpdir_obj = tempfile.TemporaryDirectory()
    tmpdir = tmpdir_obj.name
    dest = os.path.join(tmpdir, 'revert-repo')

# Generated at 2022-06-13 06:10:40.299243
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class MockModule(object):
        def __init__(self):
            self.check_mode = False
            self.run_command_results = [
                [0, 'wibble\nRevision: 12345', None],
            ]

        def run_command(self, args, check_rc, data=None):
            return self.run_command_results.pop(0)

        def exit_json(self, changed, revision, stdout, url):
            pass

        def fail_json(self, **kwargs):
            pass

        def warn(self, msg):
            pass

    class MockSubversion(Subversion):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            self.module = module


# Generated at 2022-06-13 06:10:45.489478
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    module = AnsibleModule(argument_spec={})
    repo = Subversion(module, '', '', '', '', '', '', False)
    try:
        res = repo.revert()
    except:
        res = False
    assert res is True


# Generated at 2022-06-13 06:10:55.590637
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class MockModule:
        class Run_command:
            def __init__(self):
                self.returncode = 0
                self.stdout = 'A    /tmp/./a.txt\n'
            def __call__(self, args, check_rc=True, **kwargs):
                return (self.returncode, self.stdout, '')
    class MockSubversion:
        def _exec(self, args, check_rc=True):
            return self.module.run_command.stdout.splitlines()
    def get_module(*args, **kwargs):
        return MockModule()
    def get_subversion(*args, **kwargs):
        return MockSubversion()

    import subversion
    orig_module = subversion.AnsibleModule
    subversion.AnsibleModule = get_module
   

# Generated at 2022-06-13 06:11:06.515718
# Unit test for method update of class Subversion
def test_Subversion_update():
    import mock

    m = mock.mock_open(read_data='M       index.html\nM       src/shell.py')
    with mock.patch('ansible.module_utils.subversion.open', m, create=True):
        obj = Subversion(AnsibleModule, 'any', 'any', 'any', 'any', 'any', 'any', 'any')
        assert obj.has_local_mods() is True
    m = mock.mock_open(read_data='?       index.html\n?       src/shell.py')
    with mock.patch('ansible.module_utils.subversion.open', m, create=True):
        assert obj.has_local_mods() is False


# Generated at 2022-06-13 06:11:18.618305
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    # Initialize the test module
    module = AnsibleModule(
        argument_spec=dict(
            # Specify the parameters that would be accepted by this module
            rev=dict(required=False, default='HEAD'),
            repo=dict(required=True),
            dest=dict(required=False, default=None),
            force=dict(required=False, default=False),
            username=dict(required=False, default=None),
            password=dict(required=False, default=None, no_log=True),
        ),
        supports_check_mode=True
    )

    # Create an instance of an Subversion

# Generated at 2022-06-13 06:11:22.976572
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    assert 'Révision : 1889134' == Subversion.get_remote_revision('svn://foo/bar')
    assert '版本: 1889134' == Subversion.get_remote_revision('svn://foo/bar')
    assert 'Revision: 1889134' == Subversion.get_remote_revision('svn://foo/bar')


# Generated at 2022-06-13 06:11:29.798014
# Unit test for method update of class Subversion
def test_Subversion_update():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale
    from ansible.module_utils.compat.version import LooseVersion

    # mock commands to run
    module = AnsibleModule(argument_spec=dict(dest="/home/user1/fake"))
    obj = Subversion(module,"/home/user1/fake","http://fake.repo","1","","","svn",False)
    out = obj._exec(["info","/home/user1/fake"])
    assert out[0] == 'Path: /home/user1/fake'
    assert out[1] == 'Working Copy Root Path: /home/user1/fake'
    assert out[2] == 'URL: http://fake.repo'

# Generated at 2022-06-13 06:11:32.897852
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    assert(Subversion.get_remote_revision('https://github.com/ansible/ansible/commits/stable-2.9')) == '297964'

# Generated at 2022-06-13 06:11:43.843176
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    mock_run_command = module._verbose_override = True

# Generated at 2022-06-13 06:12:11.048284
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    m = AnsibleModule(argument_spec={
        'dest': {'required': False, 'type': 'path'},
        'repo': {'required': True, 'type': 'str'},
        'revision': {'required': False, 'type': 'str'},
        'username': {'required': False, 'type': 'str'},
        'password': {'required': False, 'type': 'str'},
        'svn_path': {'required': False, 'type': 'str'},
        'validate_certs': {'required': False, 'type': 'str'}
    }, supports_check_mode=True)
    m.params['dest'] = None
    m.params['repo'] = 'svn+ssh://an.example.org/path/to/repo'
    m

# Generated at 2022-06-13 06:12:23.627898
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale
    from ansible.module_utils.compat.version import LooseVersion

    class FakeModule(AnsibleModule):
        def __init__(self,module,repo,revision ,username=None,password=None,svn_path="svn",validate_certs=None,dest=None):
            super(FakeModule,self).__init__(
                argument_spec=dict(),
                supports_check_mode=True
            )
            self.repo = repo
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path

# Generated at 2022-06-13 06:12:26.388406
# Unit test for method update of class Subversion
def test_Subversion_update():
    subversion = Subversion(None, '.', '.', None, None, None, None, None)
    assert not subversion.update()

# Generated at 2022-06-13 06:12:32.230341
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    # unit test for Subversion.has_local_mods()
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path'),
        )
    )

    svn = Subversion(module, 'test', '', '', None, None, None, None)

    # returned value has no meaning with this unit test

    # test with no status lines
    out = []
    assert svn.has_local_mods() is False

    # test with no status lines
    out = ['?']
    assert svn.has_local_mods() is False

    # test with one ! status line
    out = ['!       somefile.txt']
    assert svn.has_local_mods() is True

    # test with one M status line


# Generated at 2022-06-13 06:12:45.138884
# Unit test for method update of class Subversion
def test_Subversion_update():
    import sys
    import os
    import tempfile
    import shutil
    import contextlib
    @contextlib.contextmanager
    def tempdir():
        tmp = tempfile.mkdtemp()
        try:
            yield tmp
        finally:
            shutil.rmtree(tmp)

    lines = [
        'G      file1',
        '?      file2',
        'A      file3',
        'X      file4',
        'E      file5',
        'D      file6',
        'C      file7',
    ]
    test_dir = os.path.dirname(__file__)
    sys.path.append(test_dir)

# Generated at 2022-06-13 06:12:55.314640
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import ansible.module_utils.basic
    import ansible.module_utils.common.json
    import ansible.module_utils.common.locale
    import ansible.module_utils.common.run_command
    import ansible.module_utils.common.text
    import ansible.module_utils.common.dictmerge

    module_args = dict(
        repo='svn+ssh://an.example.org/path/to/repo',
        dest='/src/checkout',
        revision='HEAD',
        username=None,
        password=None,
        executable='/usr/bin/svn',
        checkout='yes',
        update='yes',
        export='no',
        switch='yes',
        validate_certs='no'
    )


# Generated at 2022-06-13 06:13:01.174566
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    def get_output(revision, url):
        return "%s\n\n%s" % (revision, url)

    def get_revision_output(revision, url):
        return re.sub(r"\n+", "\n", get_output(revision, url))

    revision = "Revision: 423123"
    url = "URL: http://fake.example.com/foo/bar"

    subversion = Subversion(None, None, None, None, None,
                            None, None, None)
    assert subversion.get_revision() == ("Unable to get revision", "Unable to get URL")

    subversion = Subversion(None, None, None, None, None,
                            None, None, None)

# Generated at 2022-06-13 06:13:12.969564
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    module = AnsibleModule({
        'repo': 'https://github.com/ansible/ansible',
        'dest': '/tmp/ansible',
        'revision': '1734ab05d7cce5e5dd5c5acc5d5efa7e1f9797da',
        'checkout': False,
        'update': False,
    }, check_invalid_arguments=False)
    svn = Subversion(module,
                     module.params['dest'],
                     module.params['repo'],
                     module.params['revision'],
                     module.params['username'],
                     module.params['password'],
                     module.params['executable'],
                     module.params['validate_certs'])

    # git-repo with no commits
    assert svn.checkout

# Generated at 2022-06-13 06:13:19.298995
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    from ansible.module_utils.subversion import Subversion
    svn = Subversion(None, "some-repo", "some-repo", False, False, False, False, False, False, False)
    assert svn.get_remote_revision() == "Unable to get remote revision"


# Generated at 2022-06-13 06:13:27.911373
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    module = AnsibleModule({})
    import os
    import tempfile
    import unittest
    def _exec(args, check_rc=True):
        rc = 1
        return rc
    class Subversion(object):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            self.module = module
            self.dest = dest
            self.repo = repo
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path
            self.validate_certs = validate_certs

# Generated at 2022-06-13 06:13:55.052234
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class ModuleMock(object):
        def run_command(self, bits, check_rc, data=None):
            out = ["A   bar"]
            return 0, out, "error"
    dest = '/dest'
    repo = 'svn+ssh://an.example.org/path/to/repo'
    revision = 'HEAD'
    username = 'username'
    password = 'password'
    svn_path = '/usr/bin/svn'
    validate_certs = 'no'

    subv_obj = Subversion(ModuleMock, dest, repo, revision, username, password, svn_path, validate_certs)
    assert subv_obj.switch() is True, "Subversion.switch() failed"


# Generated at 2022-06-13 06:14:00.976165
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class MockModule(object):
        def __init__(self):
            self.run_command = None
            self.warn = None

        def run_command(self, args, check_rc, data=None):
            return 0, '', ''
    module = MockModule()
    dest = '/tmp/subversion'
    repo = 'https://github.com/jpmonette/ansible-subversion'
    revision = 'HEAD'
    username = 'username'
    password = 'password'
    svn_path = 'svn'
    validate_certs = True
    svn = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    rev = svn.get_remote_revision()
    assert rev == 'Unable to get remote revision'
    return 0


# Generated at 2022-06-13 06:14:10.687637
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    repo = 'svn+ssh://an.example.org/path/to/repo'
    dest = '/src/checkout'
    revision = 'HEAD'
    username = 'fred'
    password = 'secret'
    svn_path = 'svn'
    validate_certs = 'no'
    svn = Subversion(None, dest, repo, revision, username, password, svn_path, validate_certs)
    curr = '日程: 165'
    head = '日程: 178'
    def exec_side_effect(args, check_rc=True):
        if 'info -r HEAD /src/checkout' in args:
            return [head]
        else:
            return [curr]
    svn._exec = exec_side_effect
    needs_update

# Generated at 2022-06-13 06:14:20.069385
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    # mock ansible module
    from ansible.module_utils.basic import AnsibleModule
    import io
    module = AnsibleModule(
        argument_spec=dict(
            repo=dict(type='str', required=True),
            dest=dict(type='path'),
            revision=dict(type='str', default='HEAD'),
            username=dict(type='str'),
            password=dict(type='str', no_log=True),
            executable=dict(type='path'),
            validate_certs=dict(type='bool', default=False),
        ),
        supports_check_mode=True
    )
    # mock module parameters

# Generated at 2022-06-13 06:14:26.218826
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    m = AnsibleModule()
    svn = Subversion(m, '', '', '', '', '', '', False)

    assert svn.has_local_mods() == False, "should not have local mods"


# Generated at 2022-06-13 06:14:34.297733
# Unit test for method has_local_mods of class Subversion

# Generated at 2022-06-13 06:14:44.408436
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # TODO
    return True

    class MockModule(object):
        def __init__(self, module_name, result, **kwargs):
            self.module_name = module_name
            self.result = result

        def fail_json(self, **kwargs):
            pass

        def exit_json(self, **kwargs):
            pass

    class MockAnsibleModule(object):
        def __init__(self, module_name, result, **kwargs):
            self.module = MockModule(module_name, result, **kwargs)

        def run_command(self, command, check_rc=True, data=None):
            if command[0] == "info" and command[1] == "-r" and command[3] == ".":
                return 0, "Revision: 1", ""
            el

# Generated at 2022-06-13 06:14:50.890776
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    module = AnsibleModule({
        'repo': 'https://github.com/ansible/ansible',
        'dest': '.tmp/ansible-test-repo',
        'revision': 'HEAD'
    })
    svn = Subversion(module, '.tmp/ansible-test-repo', 'https://github.com/ansible/ansible', 'HEAD', '', '', '/usr/bin/svn', False)
    assert svn.switch() == True


# Generated at 2022-06-13 06:14:56.511449
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    # 1.9.x - 1.9.7 fails
    m = Mock()
    m.run_command.return_value = (0, "1.9.7", "")
    assert(Subversion(m, "", "", "", "", "", "", False).has_option_password_from_stdin() == False)
    # 1.10.0 - 1.10.99 succeeds
    m = Mock()
    m.run_command.return_value = (0, "1.10.99", "")
    assert(Subversion(m, "", "", "", "", "", "", False).has_option_password_from_stdin() == True)


# Generated at 2022-06-13 06:15:09.873510
# Unit test for method update of class Subversion
def test_Subversion_update():
    class Subversion:
        def _exec(self, args):
            if args == ['status', '--quiet', '--ignore-externals', 'dest']:
                return ['!', 'M', '?', 'X', 'M?']
            if args == ['info', '-r', 'revision', 'dest']:
                return ['?', 'Unable to get revision']
    subversion = Subversion()
    assert subversion.update() == True
    assert subversion.has_local_mods() == True
    assert subversion.get_revision() ==  ('Unable to get revision', 'Unable to get URL')
    assert subversion.needs_update() == (True, 'Unable to get revision', 'Unable to get revision')


# Generated at 2022-06-13 06:15:53.672579
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    """
    Test for method revert of class Subversion.
    """
    assert Subversion.revert is not None


# Generated at 2022-06-13 06:16:01.701740
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    module = AnsibleModule(argument_spec={})
    dest = "dest"
    repo = "repo"
    revision = "revision"
    username = "username"
    password = "password"
    svn_path = "svn"
    validate_certs = False
    subversion = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)
    rev = subversion.REVISION_RE
    string = "Revision: 1889134"
    result = re.search(rev, string, re.MULTILINE)
    assert(result)


# Generated at 2022-06-13 06:16:08.531038
# Unit test for method has_option_password_from_stdin of class Subversion
def test_Subversion_has_option_password_from_stdin():
    ansible_module = AnsibleModule(argument_spec={})
    ansible_module.run_command = MagicMock(return_value=(0, '1.10.0', ''))
    svn = Subversion(ansible_module, None, None, None, None, None, None, None)
    assert svn.has_option_password_from_stdin()
    ansible_module.run_command = MagicMock(return_value=(0, '1.10.5', ''))
    assert svn.has_option_password_from_stdin()
    ansible_module.run_command = MagicMock(return_value=(0, '1.9.0', ''))
    assert not svn.has_option_password_from_stdin()

# Generated at 2022-06-13 06:16:09.842759
# Unit test for method update of class Subversion
def test_Subversion_update():
        assert False



# Generated at 2022-06-13 06:16:14.149530
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    a = Subversion()
    a.dest = r'./test_data/a'
    a.svn_path = '/usr/bin/svn'
    assert a.is_svn_repo()
    a.dest = r'./test_data/b'
    assert not a.is_svn_repo()


# Generated at 2022-06-13 06:16:26.250673
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class FakeModule(object):
        def __init__(self):
            self.params = dict(
                repo = 'svn+ssh://an.example.org/path/to/repo',
                dest = os.getcwd(),
                revision = 'HEAD',
                username = 'user',
                password = 'pass',
                svn_path = 'svn',
                validate_certs = True,
            )
            self.run_command_calls = 0
            self.run_command_changes = 0
            self.run_command_failures = []

# Generated at 2022-06-13 06:16:33.304697
# Unit test for method update of class Subversion
def test_Subversion_update():
    #Init
    class TestModule(object):
        def __init__(self, repo, dest, revision, username, password, svn_path, validate_certs):
            self.repo = repo
            self.dest = dest
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path
            self.validate_certs = validate_certs
        def run_command(self, cmd, check=True, data=None):
            if cmd[0] == self.svn_path and cmd[1] == "update":
                return 0, "", ""

        def warn(self, msg):
            pass


# Generated at 2022-06-13 06:16:47.194555
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    class Subversion(): pass
    items = []
    class MockModule():
        def __init__(self):
            self.params = dict(repo='https://github.com/ansible/ansible')
            self.args = {}
        def fail_json(self, **kwargs):
            pass
        def run_command(self, args, **kwargs):
            return 0, 'Revision: 12345', ''
    s = Subversion()
    s._exec = lambda *args, **kwargs: '\n'.join(items)
    s.module = MockModule()
    # Expect
    rev = 'Unable to get remote revision'
    # Actual
    items.append("Revision: 12345")
    assert s.get_remote_revision() == rev
    items.clear()
    # Expect

# Generated at 2022-06-13 06:16:54.306772
# Unit test for method update of class Subversion
def test_Subversion_update():
    module = AnsibleModule(argument_spec={})
    class _Subversion():
        def get_revision(self):
            return '2', 'https://github.com/ansible/ansible-modules-core'

        def _exec(self, cmd, check_rc=True):
            return '\n'.join(['A       examples/host_vars.yml', 'M       examples/hosts'])

    svn = Subversion(
        module,
        dest='/home/user/src',
        repo='https://github.com/ansible/ansible-modules-core.git',
        revision='HEAD',
        username=None,
        password=None,
        svn_path='svn',
        validate_certs=False
    )
    svn.__class__ = _Subversion
    assert sv

# Generated at 2022-06-13 06:16:58.149588
# Unit test for method get_remote_revision of class Subversion

# Generated at 2022-06-13 06:18:43.697072
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    # Source: https://github.com/ansible/ansible-modules-core/blob/b82633b322a2b87a7abaa8d0f39055934a3b3a7f/source_control/subversion.py#L268-L283
    #
    # It seems that the arguments are not really used.
    module = None
    dest = None
    repo = None
    revision = None
    username = None
    password = None
    svn_path = None
    validate_certs = None

    s = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)

    # Prepare the mocked Subversion object.

# Generated at 2022-06-13 06:18:48.098557
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class TestModule:
        def __init__(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
            self.run_command = arg1

    def run_command_mock(a1, check_rc, data=None):
        assert(check_rc)
        assert(data is None)
        assert(a1 == ['/path/to/svn', '--non-interactive', '--no-auth-cache', 'switch', '--revision', '1', 'svn://localhost/repo', '/path'])
        return True, 'Mocked-stdout', 'Mocked-stderr'

    module = TestModule(run_command_mock, None, None, None, None, None, None, None)

# Generated at 2022-06-13 06:18:58.942804
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    module = AnsibleModule(
        argument_spec=dict(
            repo=dict(type='str'),
            checkout=dict(type='bool', default=True),
            update=dict(type='bool', default=True),
            force=dict(type='bool', default=False),
            executable=dict(type='str', default='svn'),
            export=dict(type='bool', default=False),
            revision=dict(type='str', default='HEAD'),
            username=dict(type='str'),
            password=dict(type='str', no_log=True),
            src=dict(type='path', aliases=['dest']),
            dest=dict(type='path'),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 06:19:08.892177
# Unit test for method update of class Subversion
def test_Subversion_update():
    class MockModule:
        class MockRun_command:
            def __call__(self, args, check_rc, data=None):
                if args[0] == 'svn':
                    return 0, 'A  foo\nD  bar', None
                return 0, '', ''
        run_command = MockRun_command()

    class MockSubversion:
        def __init__(self, *args, **kwargs):
            pass
        def _exec(self, args, check_rc):
            if args[0] == 'info':
                return 'Revision: 1'
            elif args[0] == 'update':
                return 'A foo.txt\nD bar.txt'
    svn = MockSubversion()
    assert svn.update()


# Generated at 2022-06-13 06:19:17.851406
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins

    curr_revision_expect = """
URL: svn+ssh://an.example.org/path/to/repo
Revision: 1889135
Node Kind: directory
Schedule: normal
Last Changed Author: example
Last Changed Rev: 1889134
Last Changed Date: 2009-05-29 22:12:23 -0700 (Fri, 29 May 2009)
"""


# Generated at 2022-06-13 06:19:28.464622
# Unit test for method update of class Subversion
def test_Subversion_update():
    import tempfile
    import shutil
    import os
    tmpdir = tempfile.mkdtemp(prefix='svn-test-', dir=os.getcwd())
    module = AnsibleModule(argument_spec={})
    svn = Subversion(module, tmpdir, 'file:///' + os.path.join(os.getcwd(), 'test_subversion_repo'), '', None, None, 'svn', True)
    shutil.rmtree(tmpdir)
    svn.checkout()
    assert svn.is_svn_repo()
    assert svn.get_revision() == ('Revision: 3', 'URL: file://' + os.path.join(os.getcwd(), 'test_subversion_repo'))
    assert svn.get_remote_revision

# Generated at 2022-06-13 06:19:41.030412
# Unit test for method update of class Subversion
def test_Subversion_update():
    class ModuleFake:
        def run_command(self, args, check_rc=True, data=None):
            return 0, 'M  some/file\nA  other/file', ''

    class ModuleDummy:
        def run_command(self, args, check_rc=True, data=None):
            return 0, '', ''

    module = ModuleFake()

    # M  some/file
    # A  other/file
    svn = Subversion(module, '', '', '', '', '', '', '')
    assert svn.update() is True

    # No files changed
    svn = Subversion(ModuleDummy(), '', '', '', '', '', '', '')
    assert svn.update() is False



# Generated at 2022-06-13 06:19:46.675462
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    module = AnsibleModule({})
    subversion = Subversion(module, '/', '', '', '', '', '', '')
    text = 'Repository Root: svn://svn.example.com/my-repo\n'
    text = text + 'Repository UUID: 12345678-90ab-cdef-1234-567890abcdef\n'
    text = text + 'Revision: 34567\n'
    text = text + 'Node Kind: directory\n'
    text = text + 'Schedule: normal\n'
    text = text + 'Last Changed Author: username\n'
    text = text + 'Last Changed Rev: 34567\n'
    text = text + 'Last Changed Date: 2016-01-14 15:21:07 -0500 (Thu, 14 Jan 2016)\n'


# Generated at 2022-06-13 06:19:58.238687
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    # set up mock module
    class MockSvnModule:
        def __init__(self):
            self.result = {
                "revert": (0, "Reverted file1\nReverted file2\nD       file1\nD       file2", "")
            }
        def run_command(self, args, check_rc=True, data=None):
            if args == ['/usr/bin/svn', '--non-interactive', '--no-auth-cache', '--trust-server-cert',
                        'revert', '-R', '/src/checkout']:
                return self.result["revert"]
            else:
                return (2, "Unexpected command", "")
    # set up object
    module = MockSvnModule()
    dest = '/src/checkout'