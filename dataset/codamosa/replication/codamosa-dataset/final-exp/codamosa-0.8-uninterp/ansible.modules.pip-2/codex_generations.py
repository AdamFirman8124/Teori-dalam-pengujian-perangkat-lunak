

# Generated at 2022-06-13 05:49:59.844321
# Unit test for function main
def test_main():
    def authenticate(module, msg):
        return True
    def test_w(msg):
        return msg

    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.connect = authenticate
    module.warn = test_w
    module.params = {}

    if not os.path.isdir("/tmp/test-virtualenv"):
        os.makedirs("/tmp/test-virtualenv")
    if not os.path.isdir("/tmp/test-virtualenv/bin"):
        os.makedirs("/tmp/test-virtualenv/bin")
    open("/tmp/test-virtualenv/bin/python", 'a').close()
    open("/tmp/test-virtualenv/bin/activate_this.py", 'a').close()

# Generated at 2022-06-13 05:50:09.147132
# Unit test for function main
def test_main():
    mock_ansible_module = Mock(return_value=None, params=None)
    mock_ansible_module.params = {
    'extra_args': '', 
    'name': ['ansible'], 
    'requirements': '', 
    'version': None,  
    'virtualenv': '', 
    'state': 'present', 
    'virtualenv_command': 'virtualenv', 
    'virtualenv_site_packages': False, 
    'editable': False, 
    'executable': None, 
    'chdir': None 
    }
    mock_ansible_module._ansible_debug = True
    mock_ansible_module._ansible = object()
    mock_ansible_module._ansible_no_log = True
    mock_ansible_module.exit

# Generated at 2022-06-13 05:50:11.590849
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:50:13.059917
# Unit test for function main

# Generated at 2022-06-13 05:50:22.993490
# Unit test for function main

# Generated at 2022-06-13 05:50:35.256590
# Unit test for constructor of class Package
def test_Package():
    p = Package("setuptools", "1.0")
    assert p.has_version_specifier
    assert not p.is_satisfied_by("0.9")
    assert p.is_satisfied_by("1.0")

    p = Package("setuptools")
    assert p.package_name == "setuptools"
    assert not p.has_version_specifier
    assert not p.is_satisfied_by("1.0")

    p = Package("any_package")
    assert p.package_name == "any_package"
    assert not p.has_version_specifier
    assert not p.is_satisfied_by("1.0")

    p = Package("any_package", ">=1.0")
    assert p.package_name == "any_package"

# Generated at 2022-06-13 05:50:37.114988
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert 0



# Generated at 2022-06-13 05:50:48.801171
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Dummy AnsibleModule class to test setup_virtualenv
    class DummyAnsibleModule:
        def __init__(self):
            self.params = {
                'virtualenv_command': 'virtualenv',
                'virtualenv_site_packages': True,
                'virtualenv_python': None
            }
            self.check_mode = None

        def get_bin_path(self, command, required, opt_dirs=None):
            return 'bin/' + command

        def run_command(self, command, cwd=None):
            if command[0] == 'bin/python2.7' and command[1] == '-c':
                return 0, '2.7.6', ''
            else:
                return 0, '', ''

        def fail_json(self, msg):
            pass
   

# Generated at 2022-06-13 05:50:55.326130
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    p1 = Package('setuptools')
    assert p1.is_satisfied_by('2.7')
    assert not p1.is_satisfied_by('0.6c9')
    p2 = Package('pip')
    assert p2.is_satisfied_by('2.7')
    assert not p2.is_satisfied_by('3.3')


# Generated at 2022-06-13 05:51:07.341330
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    from sys import version_info


# Generated at 2022-06-13 05:51:39.016328
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    result = []

    # Testcase 1
    package = Package("passlib==1.7.1")
    version_to_test = "1.7.1"
    if not package.is_satisfied_by(version_to_test):
        result.append(1)

    # Testcase 2
    package = Package("ansible>=2.0.0.2")
    version_to_test = "2.5.5"
    if package.is_satisfied_by(version_to_test):
        result.append(1)

    # Testcase 3
    package = Package("ansible")
    version_to_test = "2.5.5"
    if not package.is_satisfied_by(version_to_test):
        result.append(1)

    # Testcase 4


# Generated at 2022-06-13 05:51:49.697626
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # If we're unit testing, then we don't want to actually
    # install anything, we need to mock these out.
    mock_module = MagicMock()
    mock_module.check_mode = False
    mock_module.params = {
        'chdir': None,
        'env': '/tmp/python-env',
        'out': None,
        'err': None,
        'virtualenv_command': '/usr/bin/virtualenv',
        'virtualenv_site_packages': False,
        'virtualenv_python': None,
    }
    mock_module.get_bin_path.return_value = '/usr/bin/virtualenv'
    mock_module.run_command.return_value =(0, '', '')

    # We call this and exit the function immediately so that we don't
    # actually install

# Generated at 2022-06-13 05:51:52.152675
# Unit test for function main
def test_main():
    import ansible_collections.autonix.test.unit.modules.test_pip as test_pip
    test_pip.main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:52:00.000489
# Unit test for constructor of class Package
def test_Package():
    package = Package('ansible', '2.0.0')
    assert package.has_version_specifier
    assert package.is_satisfied_by('2.0.0')
    assert not package.is_satisfied_by('3.0.0')
    assert to_native(package) == 'ansible==2.0.0'

    package = Package('ansible')
    assert not package.has_version_specifier
    assert package.is_satisfied_by('2.0.0')
    assert to_native(package) == 'ansible'

    package = Package('ansible', '>2.0.0')
    assert package.has_version_specifier
    assert not package.is_satisfied_by('2.0.0')
    assert package.is_satisfied_by

# Generated at 2022-06-13 05:52:00.957109
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert False



# Generated at 2022-06-13 05:52:11.154374
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import mock_open, patch, MagicMock
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.basic import AnsibleModule, _ANSIBLE_ARGS
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.pip import setup_virtualenv


    def set_module_args(args):
        args = json.dumps({'ANSIBLE_MODULE_ARGS': args})

# Generated at 2022-06-13 05:52:17.566329
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({u'vertualenv_python': u'', u'virtualenv_site_packages': False, u'virtualenv_command': u'python3 -m venv'})
    env=None
    chdir=None
    out=None
    err=None
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out
    assert err==None



# Generated at 2022-06-13 05:52:18.499005
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert False



# Generated at 2022-06-13 05:52:25.103954
# Unit test for constructor of class Package
def test_Package():
    class Test:
        def assertTrue(self, x):
            assert x

        def assertFalse(self, x):
            assert not x

    t = Test()
    p = Package('ansible')
    t.assertFalse(p.has_version_specifier)
    p = Package('ansible', '>=2.0')
    t.assertTrue(p.has_version_specifier)
    t.assertTrue(p.is_satisfied_by('2.1.1'))
    t.assertTrue(p.is_satisfied_by('2.1'))
    t.assertTrue(p.is_satisfied_by('2.0'))
    t.assertFalse(p.is_satisfied_by('1.9'))

# Generated at 2022-06-13 05:52:29.415335
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.utils.parsing import CommandParser
    from ansible.module_utils.basic import AnsibleModule

    env = '/tmp/venv'
    chdir = '/'
    out = ''
    err = ''
    CommandParser()
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command="/usr/bin/pyvenv",
        virtualenv_python="",
        virtualenv_site_packages=False,
    ))
    out_venv, err_venv = setup_virtualenv(module, env, chdir, out, err)
    assert not out_venv
    assert not err_venv



# Generated at 2022-06-13 05:52:57.081005
# Unit test for function setup_virtualenv

# Generated at 2022-06-13 05:53:08.365180
# Unit test for function main

# Generated at 2022-06-13 05:53:18.164950
# Unit test for function main
def test_main():
    assert HAS_SETUPTOOLS == True

TEST_DEFAULT_ARGS = dict(
  state = 'present',
  name = None,
  requirements = None,
  virtualenv = None,
  extra_args = None,
  editable = False,
  chdir = None,
  executable = None,
  umask = None,
  virtualenv_site_packages = False,
  virtualenv_command = 'virtualenv',
  virtualenv_python = None,
)

TEST_BAD_ARGS_STATE = dict(TEST_DEFAULT_ARGS, state = 'new_state')

TEST_NO_ARGS_NAME_LIST = dict(TEST_DEFAULT_ARGS)


# Generated at 2022-06-13 05:53:21.413785
# Unit test for function main
def test_main():
    class MockModule:
        def faile_json(self,*args,**kwargs):
            self.fail_json_args = args
            self.fail_json_kwargs = kwargs
    m = MockModule()
    main()
    return m

# Generated at 2022-06-13 05:53:25.691507
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    package = Package("foo", ">2.1,<2.2")
    assert package.is_satisfied_by("2.1.1") is True
    assert package.is_satisfied_by("2.2.0") is False



# Generated at 2022-06-13 05:53:29.976218
# Unit test for function main
def test_main():
    sys.modules['ansible'] = Mock()
    mock_module = Mock()
    mock_module.params = dict(
        state='present',
        name = ['pip'],
        chdir = '~/Downloads',
        umask = None
        )
    mock_module.check_mode = False
    main()


# Generated at 2022-06-13 05:53:31.100910
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert setup_virtualenv() == None

# Generated at 2022-06-13 05:53:39.637451
# Unit test for function main
def test_main():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    module = AnsibleModule(argument_spec={})
    try:
        main()
    except Exception as e:
        module.fail_json(msg=get_exception())


# Import module snippets
if __name__ == '__main__':
    main()

# Standard library imports
import re
import shlex
import sys
import tempfile

try:
    from setuptools.version import StrictVersion as LooseVersion
except ImportError:
    from distutils.version import LooseVersion


# Generated at 2022-06-13 05:53:50.823292
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as exec_info:
        state = 'present'
        name = ['docutils']
        version = None
        requirements = None
        extra_args = None
        chdir = None
        umask = None
        env = "/tmp/test_main_venv"
        venv_created = False
        args_list = []
        has_vcs = False
        packages = [Package(pkg) for pkg in _recover_package_name(name)]
        if extra_args:
                args_list = extra_args.split(' ')
        if '-e' not in args_list:
            args_list.append('-e')
                # Ok, we will reconstruct the option string
            extra_args = ' '.join(args_list)

# Generated at 2022-06-13 05:53:53.571037
# Unit test for function main
def test_main():
    test_str = "Successfully installed ansible-test"
    ret = _fail(AnsibleModule(argument_spec=dict()), ["test"],test_str,"")
    assert ret is None


# Generated at 2022-06-13 05:54:51.505618
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-13 05:54:52.437926
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass


# Generated at 2022-06-13 05:54:56.955157
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:55:01.009717
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    dummy_module = AnsibleModule(argument_spec=dict(virtualenv_command=dict(default='pyvenv', type='str'),
                                                    virtualenv_python=dict(default=None, type='str'),
                                                    virtualenv_site_packages=dict(default=False, type='bool')))
    env = 'venv'
    chdir = None
    out = ''
    err = ''
    out, err = setup_virtualenv(dummy_module, env, chdir, out, err)



# Generated at 2022-06-13 05:55:04.476324
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({})
    env = '/tmp/ansible_test_virtualenv'
    chdir = '/tmp'
    out = ''
    err = ''
    (out, err) = setup_virtualenv(module, env, chdir, out, err)
    assert(err == '')



# Generated at 2022-06-13 05:55:06.124579
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:55:13.677658
# Unit test for function main
def test_main():
    with patch.object(os, "umask") as mock_umask:
        mock_umask.return_value = '0774'
        with patch.object(virtualenv, "create_environment") as mock_create_env:
            with patch.object(os, "remove") as mock_remove:
                mock_remove.return_value = None

# Generated at 2022-06-13 05:55:24.073456
# Unit test for function main
def test_main():
    import sys
    import os
    import shutil
    import glob
    import tempfile
    try:
        src = os.path.join(tempfile.mkdtemp(), 'pip')
        shutil.copytree('pip', src)
        sys.path.insert(0, src)
        import ansible_module_pip as module
    finally:
        sys.path.remove(src)
        shutil.rmtree(src)

    if module.HAS_SETUPTOOLS:
        module.pip.main()
        shutil.rmtree(tempfile.gettempdir())


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:55:35.772638
# Unit test for function setup_virtualenv
def test_setup_virtualenv():

    module = AnsibleModule({
        'virtualenv_command': '/usr/bin/pyvenv',
        'virtualenv_python': 'python2',
    })
    env = '/path/to/env'
    chdir = None
    out = ''
    err = ''
    out_venv, err_venv = setup_virtualenv(module, env, chdir, out, err)
    assert out_venv == 'Created virtualenv with interpreter /usr/bin/python2'
    assert err_venv == ''


    module = AnsibleModule({
        'virtualenv_command': '/usr/bin/venv',
        'virtualenv_site_packages': False,
    })
    env = '/path/to/env'
    chdir = None
    out = ''
    err = ''
    out_venv,

# Generated at 2022-06-13 05:55:46.500973
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg_setup = Package("setuptools")
    assert pkg_setup.is_satisfied_by("42.0.2")
    assert not pkg_setup.is_satisfied_by("0")
    assert pkg_setup.is_satisfied_by("1.1.6")
    pkg_setuptools_gt3 = Package("setuptools>3")
    assert pkg_setuptools_gt3.is_satisfied_by("42.0.2")
    assert not pkg_setuptools_gt3.is_satisfied_by("1.1.6")
    pkg_ansible_lt2 = Package("ansible<2")
    assert pkg_ansible_lt2.is_satisfied_by("1")
    assert not pkg_ansible

# Generated at 2022-06-13 05:57:49.209213
# Unit test for function main
def test_main():
    curdir = os.getcwd()
    isdir = os.path.isdir
    
    tempdir = tempfile.mkdtemp()
    tempdir2 = tempfile.mkdtemp()
    tempdir3 = tempfile.mkdtemp()
    
    os.chdir(tempdir)
    
    assert isdir("/tmp")
    assert isdir("/tmp/")
    assert os.path.isabs("/tmp")
    assert not os.path.isabs("tmp")
    
    test_pip = "pip3"
    
    if not ansible_support:
        test_pip = "/usr/bin/pip"
        
    #test_main(test_pip, "test", state="present")
    
    os.chdir(curdir)

# Generated at 2022-06-13 05:57:54.567970
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command=dict(default='virtualenv'),
        virtualenv_python=dict(default=None),
        virtualenv_site_packages=dict(
            default=False,
            type='bool'
        ),
    ))
    env = '/tmp/ansible-virtualenv-test'
    chdir = '/tmp'
    out = ''
    err = ''
    test_out, test_err = setup_virtualenv(module, env, chdir, out, err)
    assert not os.path.exists(env)
    module.params['virtualenv_command'] += ' /tmp/ansible-virtualenv-test'
    test_out, test_err = setup_virtualenv(module, env, chdir, out, err)
    assert os.path.ex

# Generated at 2022-06-13 05:57:55.742282
# Unit test for function main
def test_main():
    import doctest
    #doctest.testmod()

if __name__ == '__main__':
    test_main()
    main()

# Generated at 2022-06-13 05:58:00.925549
# Unit test for function main
def test_main():
    """Unit test for function main
    """

    def mock_exit_json(changed, cmd='', name='', version='', state='', requirements='', virtualenv='', stdout='', stderr=''):
        """Mock function exit_json
        """
        self.mock_exit_json_value = dict(
            changed=changed,
            cmd=cmd,
            name=name,
            version=version,
            state=state,
            requirements=requirements,
            virtualenv=virtualenv,
            stdout=stdout,
            stderr=stderr,
        )

    def mock_run_command(cmd, path_prefix=None, cwd=None):
        """Mock function run_command
        """

        rc = 0
        stdout = ''
        stderr = ''

# Generated at 2022-06-13 05:58:10.987536
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import platform
    import shutil
    import tempfile
    import venv
    import virtualenv

    # On Debian stretch pyvenv is used
    if platform.dist()[0] == 'debian' and platform.dist()[1] == 'stretch':
        virtualenv_command = 'pyvenv'
    # On centos 7 venv is used
    if platform.dist()[0] == 'centos' and platform.dist()[1] == '7':
        virtualenv_command = 'python -m venv'
    else:
        virtualenv_command = 'virtualenv'

    class FakeModule(object):
        def __init__(self):
            self.check_mode = False

        def exit_json(self, changed):
            self.changed = changed


# Generated at 2022-06-13 05:58:20.971898
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pip import (
        HAS_SETUPTOOLS,
        SETUPTOOLS_IMP_ERR,
        missing_required_lib,
        _fail,
        _get_cmd_options,
        _get_package_info,
        _get_pip,
        _is_present,
        _recover_package_name,
    )
    from ansible.module_utils.pip import main as pip_main
    import shutil


# Generated at 2022-06-13 05:58:28.822772
# Unit test for constructor of class Package
def test_Package():
    # positive test cases
    name_strings = ["requests", "pytest", "pytest-mock", "pytest<5", "pytest>5",
                    "pytest>5,<6", "pytest>5,<6,>=5.2", "pytest>=5,<=6.3,!=6.1,!=6.2"]
    for name_string in name_strings:
        pkg = Package(name_string)
        assert isinstance(pkg, Package)
        assert pkg.package_name == Package.canonicalize_name(pkg._requirement.project_name)

        if pkg._requirement.project_name == "distribute" and "setuptools" in name_string:
            assert pkg.package_name == "setuptools"


# Generated at 2022-06-13 05:58:34.367464
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # setup_virtualenv() is not unit testable due to `module.run_command` not being mockable
    # without fully mocking the entire module.  The module is not designed to be used in a
    # standalone manner and hence is not designed to be imported and used.  It is designed to
    # be run via the ansible-python-api which initializes the module.
    pass


# Generated at 2022-06-13 05:58:41.993347
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import sys
    import os
    import tempfile
    import shutil
    import subprocess
    import ansible.module_utils.basic
    import ansible.module_utils.pip

    temp_dir = tempfile.mkdtemp()
    env = os.path.join(temp_dir, "env")
    module_args = {
        'virtualenv_command': '/usr/bin/env python -m venv',
        'virtualenv_python': None,
        'virtualenv_site_packages': False,
    }
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write("import ansible.module_utils.pip")
    temp_file.close()

# Generated at 2022-06-13 05:58:51.850003
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import tempfile
    import os

    module = AnsibleModule(argument_spec={'virtualenv_command': dict(default='virtualenv'),
                                          'virtualenv_site_packages': dict(default='false', type='bool'),
                                          'virtualenv_python': dict(default='')})
    env = tempfile.mkdtemp()
    chdir = tempfile.mkdtemp()