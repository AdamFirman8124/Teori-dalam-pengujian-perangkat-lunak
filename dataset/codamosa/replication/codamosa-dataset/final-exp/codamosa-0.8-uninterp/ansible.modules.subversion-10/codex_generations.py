

# Generated at 2022-06-13 06:10:25.321039
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import subprocess
    import tarfile
    from ansible_collections.ansible.builtin.plugins.modules.subversion import main
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale
    from ansible.module_utils.compat.version import LooseVersion

    class Subversion(object):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            self.module = module
            self.dest = dest
            self.repo = repo
            self.revision = revision
            self.username = username
            self.password = password
            self.svn_path = svn_path
            self

# Generated at 2022-06-13 06:10:34.917191
# Unit test for function main
def test_main():
    from ansible.modules.source_control.subversion import main

    dest = None
    repo = None
    revision = 'HEAD'
    force = False
    username = None
    password = None
    svn_path = None
    export = False
    switch = True
    checkout = True
    update = True
    in_place = False
    validate_certs = False

    svn = main(dest, repo, revision, force, username, password, svn_path, export, switch, checkout, update, in_place, validate_certs)


# Generated at 2022-06-13 06:10:42.891146
# Unit test for method revert of class Subversion

# Generated at 2022-06-13 06:10:48.042129
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    mod_name = 'ansible.builtin.subversion'
    mod = basic._get_unconnected_module_with_checks(mod_name)
    mod.params = {
        'dest': '.',
        'repo': 'svn://',
        'revision': 'HEAD',
        'validate_certs': False
    }

    svn = Subversion(mod, '.', 'svn://', 'HEAD', None, None, 'svn', False)
    rev, _ = svn.get_revision()
    if not to_bytes(svn.REVISION_RE).decode() in rev:
        raise AssertionError(rev)



# Generated at 2022-06-13 06:10:57.431322
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    import os, shutil
    from ansible.module_utils.subversion_spec import SubversionSpec
    from ansible.module_utils.subversion import Subversion
    # Create local svn repo
    os.mkdir('sub_test')
    os.mkdir('sub_test/checkout')
    os.chdir('sub_test/checkout')
    spec = SubversionSpec()
    spec.add_remote_branch('file:///tmp/sub_test/repo/trunk', 'trunk')
    spec.add_revision(3)
    spec.write_wc('/tmp/sub_test/checkout')
    # Create local svn repo
    os.mkdir('/tmp/sub_test/repo')
    os.chdir('/tmp/sub_test/repo')
    os

# Generated at 2022-06-13 06:10:58.495632
# Unit test for method revert of class Subversion
def test_Subversion_revert():
  assert Subversion.revert('self') == True

# Generated at 2022-06-13 06:11:03.712405
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    import unittest
    import mock
    import subprocess

    # Run tests on python 2.6, 2.7, 3.3, and 3.4
    class FakeModule26(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, **kwargs):
            pass

        def run_command(self, command, check_rc=True, data=None):
            return 0, 'Revision: 5'.encode(), ''

        def get_bin_path(self, svn, required=True, opt_dirs=[]):
            return 'svn'

        def warn(self, warning):
            pass

    class FakeModule27(FakeModule26):
        def run_command(self, command, check_rc=True, data=None):
            return

# Generated at 2022-06-13 06:11:15.331539
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    from unittest import mock
    MOD_UTIL_PATH = 'ansible.module_utils.basic'
    REVISION_RE = Subversion.REVISION_RE

    def _mock_run_command(command, check_rc, data=None):
        if command == ['svn', 'info', '/path/to/dest']:
            text = '''URL: svn+ssh://an.example.org/path/to/repo
\u00c9l\u00e9ment principal : /
R\u00e9vision : 1889134
'''
            return (0, text, '')

    def _mock_get_locale():
        return 'fr_FR.UTF-8'


# Generated at 2022-06-13 06:11:24.729961
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    """Unit test for method get_remote_revision of class Subversion"""
    import ansible.module_utils.basic
    import ansible.module_utils.connection
    import ansible.module_utils.urls
    import ansible.module_utils.http
    import ansible.module_utils.six
    import ansible.module_utils.json
    import ansible.module_utils.common.collections
    import ansible.module_utils.common.dict_transformations
    import ansible.module_utils.common.arg_spec
    import ansible.module_utils.common.text
    import ansible.module_utils.common.json_dict
    import ansible.module_utils.common.warnings
    import ansible.module_utils.action
    import ansible.module_utils.action_common_attributes


# Generated at 2022-06-13 06:11:34.154268
# Unit test for method update of class Subversion
def test_Subversion_update():
    repo = 'svn+ssh://an.example.org/path/to/repo'
    dest = '/src/export'
    revision = 'HEAD'
    username = ''
    password = ''
    validate_certs = ''
    svn_path = '/usr/bin/svn'
    self = Subversion(None, dest, repo, revision, username, password, svn_path, validate_certs)
    self.update()

if __name__ == '__main__':
    test_Subversion_update()

# Generated at 2022-06-13 06:11:57.972885
# Unit test for method update of class Subversion
def test_Subversion_update():
    class RunCommandMock(object):
        def __init__(self):
            self.output = []
        def run_command(self, cmd, check_rc=True):
            self.output = ["A    my_file1.txt",
                           "A    my_file2.txt"]
            return 0, self.output, ""

    class SubversionInitMock(object):
        def __init__(self, module, dest, repo, revision, username, password, svn_path, validate_certs):
            self.module = module

    class ModuleInitMock(object):
        def __init__(self, **kwargs):
            self.params=kwargs

    module = ModuleInitMock(repo = "file:///svn/repo", dest = ".")
    module.run_command = RunCommandMock

# Generated at 2022-06-13 06:12:09.327531
# Unit test for method is_svn_repo of class Subversion
def test_Subversion_is_svn_repo():
    import tempfile
    import shutil

    svn_test_path = os.path.join(tempfile.mkdtemp(), 'subversion')
    subversion_test_file = os.path.join(svn_test_path, 'test_file')

    svn_obj = Subversion(None, svn_test_path, None, None, None, None, None, None)

    # Test that a path is not a SVN repo when we haven't imported anything.
    assert not svn_obj.is_svn_repo()

    # Create a fake file for testing.
    with open(subversion_test_file, 'a') as test_file:
        test_file.write('test')

    # Create a fake SVN repo if it doesn't exist.

# Generated at 2022-06-13 06:12:13.522338
# Unit test for function main

# Generated at 2022-06-13 06:12:27.769890
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    dest = "/tmp/path/to/repo"
    repo = "svn+ssh://an.example.org/path/to/repo"
    revision = "HEAD"
    username = "username"
    password = "password"
    svn_path = "/path/to/svn"
    subversion = Subversion(None, dest, repo, revision, username, password, svn_path)
    assert subversion.get_revision() == ('Révision : 1889134', 'URL : svn+ssh://an.example.org/path/to/repo')

    # Test with alternate output
    subversion.REVISION_RE = r'^\w+\s?:\s+\d+$'

# Generated at 2022-06-13 06:12:33.187330
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    import os
    import shutil
    import tempfile
    import unittest
    from ansible.module_utils.six import PY2, b
    from ansible.module_utils.six.moves import builtins

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            self.exit_code = 1

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 06:12:44.653871
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    class module:
        def run_command(self, command):
            return '\n'.join([
                '',
                'M       some/revisioned/file',
                '',
                '?       some/unrevisioned/file',
                # https://github.com/ansible/ansible/issues/7542
                '?       .svn/some/revisioned/file',
            ])
    subversion = Subversion(module(), '/tmp/test_repo', 'https://svn.example.com/test_repo', '1337', None, None, '/usr/bin/svn', False)
    assert(subversion.has_local_mods() == True)


# Generated at 2022-06-13 06:12:55.172983
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    import tempfile
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins

    # Create a temp dir for the repo.
    repo = tempfile.mkdtemp()
    if repo[-1] == '/':
        repo = repo[:-1]
    module = FakeModule()
    dest = os.getcwd()

    # Initialize an svn repo.
    svn = Subversion(module, dest, repo, '1', None, None, '/usr/bin/svn', True)
    svn._exec(['checkout', '-r', '1', repo, dest])
    svn._exec(['update', '-r', '2', repo])

    # Get working directory status.
    change, curr, head = svn.needs_update

# Generated at 2022-06-13 06:13:04.334822
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    import subprocess
    import sys
    module = AnsibleModule(
        argument_spec={}
    )
    svn_path = subprocess.check_output(["which", "svn"]).rstrip().decode(sys.stdout.encoding)
    repo = "https://github.com/ansibles/ansible-modules-extras/trunk/testing/test-repo"
    svn = Subversion(module, '', repo, '', '', '', svn_path, "yes")
    rev = svn.get_remote_revision()
    module.exit_json(msg=rev)

if __name__ == '__main__':
    test_Subversion_get_remote_revision()



# Generated at 2022-06-13 06:13:14.640029
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    module = AnsibleModule({
        'repo': 'svn+ssh://an.example.org/path/to/repo',
        'dest': '/src/checkout',
        'revision': '1.0',
        'state': 'present'
    })
    dest = os.path.expanduser('/src/checkout')
    repo = 'svn+ssh://an.example.org/path/to/repo'
    revision = '1.0'
    username = None
    password = None
    svn_path = 'svn'
    validate_certs = False
    obj = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)

# Generated at 2022-06-13 06:13:26.297102
# Unit test for method update of class Subversion
def test_Subversion_update():
    class ModuleMock(object):
        '''Mock of ansible.module_utils.basic.AnsibleModule class'''
        def __init__(self):
            self.params = {}
            self.check_mode = False
        def run_command(self, args, check_rc, data=None):
            # Simulate output of svn info command
            text = '''Repository root: https://svn.freepascal.org/svn/fpc
Repository UUID: 91c68942-7dea-0310-ad7e-fbcb08e9c271
Revision: 38231
Node Kind: directory
Schedule: normal
Last Changed Author: Martin
Last Changed Rev: 37092
Last Changed Date: 2019-06-14 10:45:04 +0200 (Fri, 14 Jun 2019)
'''


# Generated at 2022-06-13 06:14:10.301726
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    #for real usages, import modules.
    class MockModule(object):
        def __init__(self):
            self.params = {'revision': "HEAD"}

        def run_command(self, cmd, check_rc=True, data=None):
            if cmd[0] == 'svn':
                if cmd[2] == '-r':
                    return 0, '', ''
                else:
                    return 0, 'Revision: 123', ''
            else:
                return 0, '', ''

    module = MockModule()
    svn = Subversion(module, "mock_dest_path", "mock_repo_url", "HEAD", None, None, "mock_svn_path")

# Generated at 2022-06-13 06:14:12.034666
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    s=Subversion
    s.revert()

# Generated at 2022-06-13 06:14:19.175332
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    module = AnsibleModule({'repo': 'repo', 'dest': 'dest', 'checkout': True, 'update': True, 'export': False, 'force': True, 'revision': 'HEAD'})
    dest = 'dest'
    repo = 'repo'
    revision = 'HEAD'
    svn_path = 'svn'
    validate_certs = False
    svn = Subversion(module, dest, repo, revision, None, None, svn_path, validate_certs)
    svn.get_remote_revision()



# Generated at 2022-06-13 06:14:31.883712
# Unit test for function main
def test_main():
    import os, tempfile
    fd, repo = tempfile.mkstemp()
    os.close(fd)
    fd, dest = tempfile.mkstemp()
    os.close(fd)
    os.remove(dest)


# Generated at 2022-06-13 06:14:43.308836
# Unit test for function main
def test_main():
   data="""
- name: Checkout subversion repository to specified folder
  ansible.builtin.subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/checkout

- name: Export subversion directory to folder
  ansible.builtin.subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/export
    export: yes

- name: Get information about the repository whether or not it has already been cloned locally
  ansible.builtin.subversion:
    repo: svn+ssh://an.example.org/path/to/repo
    dest: /src/checkout
    checkout: no
    update: no
"""
   from ansible.module_utils.basic import Ans

# Generated at 2022-06-13 06:14:52.739247
# Unit test for function main
def test_main():
    os.system('mv main main.bak')
    with open('main', 'w') as f:
        f.write('#!/usr/bin/python')

    avm = AnsibleModule({}, {})
    avm.fail_json = lambda r:r
    avm.exit_json = lambda r:r

    main()
    res = avm.run_command(['git', 'clone', 'https://github.com/Tiger66639/test_class.git'])
    print(res)
    assert os.path.exists('test_class')
    shutil.rmtree('test_class')
    os.system('mv main.bak main')


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:14:59.100148
# Unit test for method has_local_mods of class Subversion
def test_Subversion_has_local_mods():
    # If a repo is working directory has local mods, method has_local_mods returns True
    class module(object):
        def __init__(self):
            self._exec = lambda x: ['Changed     file.py']
    svn = Subversion(module=module(), dest='', repo='', revision='', username='', password='', svn_path='', validate_certs='')
    assert svn.has_local_mods()

    # If a repo is working directory has no local mods, method has_local_mods returns False
    class module(object):
        def __init__(self):
            self._exec = lambda x: []
    svn = Subversion(module=module(), dest='', repo='', revision='', username='', password='', svn_path='', validate_certs='')

# Generated at 2022-06-13 06:15:03.501838
# Unit test for function main
def test_main():
    import ansible.module_utils.basic.subversion
    ansible.module_utils.basic.subversion.__dict__["main"] = lambda self: "Testing"
    obj = Subversion(1, 1, 1, 1, 1, 1, 1, 1)
    assert obj.main() == "Testing"


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:15:13.800875
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.locale import get_best_parsable_locale
    module = AnsibleModule()
    #svn = Subversion(module, '../test_data', 'http://repo.com/package1/branch1/', 'r1', 'user', 'pwd', '/usr/bin/svn', False)
    #svn = Subversion(module, '', 'http://repo.com/package1/branch1/', 'r1', 'user', 'pwd', '/usr/bin/svn', False)
    #svn = Subversion(module, '../test_data', 'http://repo.com/package1/branch1/', 'r1', 'user', 'pwd', '/usr/bin

# Generated at 2022-06-13 06:15:23.754982
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    module = AnsibleModule(argument_spec={})
    subversion = Subversion(module,
                            None,
                            repo='http://svn.apache.org/repos/asf/httpd/httpd/branches/1.3.x',
                            revision=None,
                            username=None,
                            password=None,
                            svn_path='/usr/bin/svn',
                            validate_certs=False)
    remote_revision = subversion.get_remote_revision()
    assert remote_revision == u'R\xe9vision : 1336103'
# Unit tests for class Subversion with no svn repository

# Generated at 2022-06-13 06:16:48.397437
# Unit test for method update of class Subversion
def test_Subversion_update():
    import unittest

    class Subversion_update_TestCase(unittest.TestCase):
        '''A Test Case for the update method of class Subversion.'''

        def setUp(self):
            '''Setup tasks to be run before every test_* function'''
            pass

        def tearDown(self):
            '''Teardown tasks to be run after every test_* function'''
            pass

        # Place your unit tests for Subversion.update here

    # A couple of unit tests
    class Subversion_update_TestCases(Subversion_update_TestCase):
        '''A collection of Test Cases for the update method of class Subversion.'''

        def test_update(self):
            '''Test 1: Basic sanity test'''

# Generated at 2022-06-13 06:17:01.623233
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class SubversionMock:
        def __init__(self):
            self.args = []
            self.revs = []
            self.stdouts = []
            self.ret = []
        def _exec(self, args, check_rc=True):
            self.args.append(args)
            if check_rc:
                return self.stdouts.pop(0)
            else:
                return self.ret.pop(0)

    class ModuleMock:
        def __init__(self):
            self.changed = False
            self.rc = 0
            self.args = []
            self.revs = []
        def run_command(self, args, check_rc=True, data=None):
            self.args.append(args)
            if check_rc:
                return self.rc, '', ''

# Generated at 2022-06-13 06:17:10.834801
# Unit test for method update of class Subversion
def test_Subversion_update():
    import sys
    import json

    # https://medium.com/@bfortuner/python-unit-testing-with-fake-filesystem-fixtures-d6f5950c1db1
    from pyfakefs import fake_filesystem_unittest  # noqa
    from ansible.module_utils.basic import AnsibleModule  # noqa
    from ansible.module_utils.common.locale import get_best_parsable_locale  # noqa
    from ansible.module_utils.compat.version import LooseVersion  # noqa

    # Py2 and Py3 compatibility:
    if sys.version_info[0] == 3:  # pragma: no cover
        unicode = str


# Generated at 2022-06-13 06:17:22.268653
# Unit test for method revert of class Subversion
def test_Subversion_revert():
    class AnsibleModule(object):
        def __init__(self):
            self.run_command_params = []
            self.run_command_results = []

        def run_command(self, args, **kwargs):
            self.run_command_params.append({
                'args': tuple(args),
                'kwargs': kwargs.copy(),
            })
            return self.run_command_results.pop(0)

    class TestSubversion(Subversion):
        def _exec(self, args, check_rc=True):
            rc, out, err = self.module.run_command(['/bin/false'], check_rc=True)
            return '\n'.join(out.splitlines()[:-1]) # Remove the final line which has the exit status.

    module = AnsibleModule()
   

# Generated at 2022-06-13 06:17:29.022509
# Unit test for method get_remote_revision of class Subversion
def test_Subversion_get_remote_revision():
    args = dict(
        module=None,
        dest=None,
        repo='http://svn.example.com/',
        revision='HEAD',
        username=None,
        password=None,
        svn_path='svn',
        validate_certs=False)

    svn = Subversion(**args)

    # the test mock-up SVN repository returns the expected value
    assert svn.get_remote_revision() == 'Revision: 1'


# Generated at 2022-06-13 06:17:38.997736
# Unit test for function main
def test_main():
    dest = os.getcwd()
    repo = "http://svn/server/project"
    revision = "HEAD"
    force = False
    username = "user"
    password = "pass"
    svn_path = "svn"
    export = False
    switch = True
    checkout = True
    update = True
    in_place = False
    validate_certs = False
    if not dest and (checkout or update or export):
        #module.fail_json(msg="the destination directory must be specified unless checkout=no, update=no, and export=no")
        print("the destination directory must be specified unless checkout=no, update=no, and export=no")

    svn = Subversion(dest, repo, revision, username, password, svn_path, validate_certs)


# Generated at 2022-06-13 06:17:45.977681
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    class ModuleMock(object):
        def __init__(self):
            self.run_command = run_command_mock

    def run_command_mock(*args, **kwargs):
        if args[0][-1] == 'info':
            ret_code = 0
            out = 'Revision: 1909207'
            err = ''
        elif args[0][-1] == 'switch':
            ret_code = 0
            out = 'S    foo\n'
            err = ''
        return ret_code, out, err

    dest = '/path/to/dest'
    repo = 'svn://example.com/repo'
    revision = 'HEAD'
    username = 'user'
    password = 'pass'
    svn_path = 'svn'


# Generated at 2022-06-13 06:17:55.799396
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    import os
    import shutil
    tempdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-repo')
    dest = os.path.join(tempdir, 'src', 'checkout')

    subversion = Subversion(
        module=None,
        dest=dest,
        repo='file://' + tempdir + '/src/repo',
        revision='HEAD',
        username='',
        password='',
        svn_path='svn',
        validate_certs=False,
    )

    shutil.rmtree(dest, ignore_errors=True)
    subversion.checkout()
    assert subversion.switch()



# Generated at 2022-06-13 06:18:00.521559
# Unit test for method needs_update of class Subversion
def test_Subversion_needs_update():
    obj = Subversion(None, None, None, None, None, None, None, None)
    obj.get_revision = MagicMock(return_value=(1, 1))
    obj.get_remote_revision = MagicMock(return_value=2)
    assert obj.needs_update() == (1, 1)
    assert obj.get_revision.called
    assert obj.get_remote_revision.called



# Generated at 2022-06-13 06:18:06.727625
# Unit test for method switch of class Subversion
def test_Subversion_switch():
    repo = "http://svn.example.com/repo"
    dest = "/tmp_test_svn_playground"
    revision = "100"
    svn_path = "/usr/bin/svn"
    validate_certs = False
    if not os.path.exists(dest):
        os.makedirs(dest)
    if os.path.exists(os.path.join(dest, ".svn")):
        shutil.rmtree(os.path.join(dest, ".svn"))

    svn = Subversion(None, dest, repo, revision, None, None, svn_path, validate_certs)
    svn.checkout()

    assert svn.switch() is True

# Generated at 2022-06-13 06:20:00.712323
# Unit test for method get_revision of class Subversion
def test_Subversion_get_revision():
    def assert_is_revision(rev):
        m = re.match('Revision: [0-9]+', rev)
        assert m is not None
    class TestModule:
        def __init__(self):
            self.run_command_called = False
            self.run_command_output = [
                'something irrelevant',
                'Revision: 123'
            ]
            self.run_command_rc = 0
        def run_command(self, cmd):
            self.run_command_called = True
            assert cmd == ['svn', '--non-interactive', '--no-auth-cache', 'info', '/path/to/dest']
            return (self.run_command_rc, self.run_command_output, None)
    test_module = TestModule()