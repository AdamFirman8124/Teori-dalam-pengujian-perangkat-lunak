

# Generated at 2022-06-13 05:49:32.684443
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:49:41.934267
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    package = Package("A", "1.0.1")
    assert package.is_satisfied_by("1.0.1")
    assert not package.is_satisfied_by("1.0.3")

    package = Package("B", "==1.0.1")
    assert package.is_satisfied_by("1.0.1")
    assert not package.is_satisfied_by("1.0.2")

    package = Package("C", ">1.0.1")
    assert package.is_satisfied_by("1.0.2")
    assert not package.is_satisfied_by("1.0.0")

    package = Package("D", ">=1.0.1,<1.0.3")
    assert package.is_satisfied_by

# Generated at 2022-06-13 05:49:49.048939
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package("SomePackage", "1.0.0")
    assert pkg.is_satisfied_by("1.0.0")
    pkg = Package("SomePackage", ">=1.0,<2.0")
    assert pkg.is_satisfied_by("1.0.0")
    assert pkg.is_satisfied_by("1.5.0")
    assert not pkg.is_satisfied_by("2.0.0")
    assert not pkg.is_satisfied_by("0.5.0")



# Generated at 2022-06-13 05:49:57.098897
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package('ansible-base')
    assert pkg.is_satisfied_by('2.8.5') is True
    assert pkg.is_satisfied_by('2.8.4') is False
    pkg = Package('ansible-base', '2.8.5')
    assert pkg.is_satisfied_by('2.8.5') is True
    assert pkg.is_satisfied_by('2.8.6') is False
    assert pkg.has_version_specifier is True
    assert str(pkg) == 'ansible-base==2.8.5'
    assert pkg.package_name == 'ansible-base'


if __name__ == '__main__':
    # Unit test code.
    from ansible.utils.path import get_

# Generated at 2022-06-13 05:49:57.919824
# Unit test for function setup_virtualenv

# Generated at 2022-06-13 05:49:58.434473
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert True



# Generated at 2022-06-13 05:50:08.003413
# Unit test for function main

# Generated at 2022-06-13 05:50:12.942735
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Nose doesn't support multiple yield tests well
    # pylint: disable=no-self-use
    # Test with virtualenv_command being a binary file
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        mock_module = MagicMock()
        mock_module.run_command.return_value = (0,'','')
        mock_module.params.get.return_value = None
        mock_module.check_mode = False
        mock_module.get_bin_path.return_value = '/usr/local/bin/virtualenv'
        out, err = setup_virtualenv(mock_module, "/tmp/venv", "", "", "")

# Generated at 2022-06-13 05:50:14.745714
# Unit test for function main
def test_main():
  assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:50:16.135137
# Unit test for function main
def test_main():
    print('insdie test_main')

# Generated at 2022-06-13 05:50:58.168267
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Test to make sure that if virtualenv_command is 'pyvenv' and
    # virtualenv_python is defined, then virtualenv_python is ignored
    module = Mock(params={'virtualenv_command': 'python -m venv', 'virtualenv_python': 'python3'},
                  run_command=Mock(return_value=(0, "", "")),
                  get_bin_path=Mock(return_value="/bin"))
    setup_virtualenv(module, "env", None, "", "")
    assert module.fail_json.called

    # Test to make sure that if virtualenv_command is 'venv' and
    # virtualenv_python is defined, then virtualenv_python is ignored

# Generated at 2022-06-13 05:51:06.680521
# Unit test for constructor of class Package
def test_Package():
    package_str = "Django==1.9"

    pkg = Package(package_str)
    assert pkg.package_name == "django"
    assert pkg.has_version_specifier
    assert pkg.is_satisfied_by("1.9")
    assert not pkg.is_satisfied_by("1.8")

    pkg = Package("Django")
    assert pkg.package_name == "django"
    assert not pkg.has_version_specifier
    assert pkg.is_satisfied_by("1.9")
    assert pkg.is_satisfied_by("1.8")

    package_str = "Flask (from versions: 0.1, 0.2)"

    pkg = Package(package_str)
    assert pkg

# Generated at 2022-06-13 05:51:12.473812
# Unit test for function main

# Generated at 2022-06-13 05:51:23.466707
# Unit test for function main
def test_main():
    """
    Test function with patching

    :return:
    """

# Generated at 2022-06-13 05:51:30.931465
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    failed = False
    print('Running test for function setup_virtualenv')
    import os
    import shutil
    import json
    import subprocess
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command=dict(default=None),
        virtualenv_python=dict(default=None),
        no_use_wheel=dict(default=False),
        use_mirrors=dict(default=False),
        virtualenv_site_packages=dict(default=False),
        name=dict(default=None, required=True),
        virtualenv=dict(default=None),
    ))
    if os.path.exists("/tmp/test_virtualenv/"):
        shutil.rmtree("/tmp/test_virtualenv/")
    os.makedirs("/tmp/test_virtualenv/")

# Generated at 2022-06-13 05:51:32.089812
# Unit test for function main
def test_main():
    assert  main() ==  None

# Generated at 2022-06-13 05:51:39.820002
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Given
    test_module = {'params' : { 'virtualenv_command' : 'virtualenv',
                'virtualenv_site_packages' : False,
                'virtualenv_python' : 'python3'},
                  'run_command' : _run_command,
                  'get_bin_path' : _get_bin_path,
                  'check_mode' : False}
    python_bin = test_module['get_bin_path']('python3', False, [])
    virtual_env = "virtualenv_test"
    # When
    out, err = setup_virtualenv(test_module, virtual_env, ".", "", "")
    # Then
    assert (python_bin in out) and ("-p%s" % python_bin in out)

    # Given

# Generated at 2022-06-13 05:51:43.133324
# Unit test for constructor of class Package
def test_Package():
    pkg = Package("SomePackage", "1.0.0")
    pkg = Package("SomePackage")
    pkg = Package("somepackage")

# This class is only available in newer setuptools, so we have this
# dummy class in case it doesn't exist.

# Generated at 2022-06-13 05:51:52.862916
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.modules.packaging.os.pip import PIP_DISTRIBUTION_PACKAGES
    from ansible.modules.packaging.os.pip import PIP_VIRTUALENV_PACKAGES
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command=dict(default='/usr/bin/virtualenv'),
        virtualenv_site_packages=dict(type='bool', default=False),
        virtualenv_python=dict(default=None),
    ))
    env = '/tmp/testenv'
    chdir = None
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env, chdir, out, err)

# Generated at 2022-06-13 05:52:00.052243
# Unit test for constructor of class Package
def test_Package():
    pkg = Package("setuptools", "==9.9")
    assert pkg.package_name == "setuptools"
    assert pkg.has_version_specifier == True
    assert pkg.is_satisfied_by("9.9") == True
    assert pkg.is_satisfied_by("9.10") == False

    pkg = Package("setuptools", "~=9.9")
    assert pkg.package_name == "setuptools"
    assert pkg.has_version_specifier == True
    assert pkg.is_satisfied_by("9.10") == True
    assert pkg.is_satisfied_by("10.0") == False

    # No version specifier
    pkg = Package("setuptools")
    assert pkg.package_name

# Generated at 2022-06-13 05:53:10.386031
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:53:15.196405
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    try:
        import importlib
    except ImportError:
        importlib = None

    if importlib:
        # noinspection PyUnresolvedReferences
        importlib.reload(sys)

    if not PY3:
        reload(sys)
        sys.setdefaultencoding('utf8')

    # Create a fake module
    mock_module = MagicMock()

    # Create a fake python interpreter
    mock_python_exec = 'mock_python_binary'
    mock_python_binary = MagicMock()
    mock_python_binary.return_value = '2.7'
    mock_get_bin_path = MagicMock()
    mock_get_bin_path.return_value = mock_python_exec
    mock_module.get_bin_path = mock_get_bin_path

    # Mock

# Generated at 2022-06-13 05:53:26.496998
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:53:34.392982
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """
    Return results of setup_virtualenv function for unit testing
    """
    params = {'virtualenv_command': '/usr/bin/virtualenv',
              'virtualenv_python': '/usr/bin/python2',
              'virtualenv_site_packages': False}
    env = 'test_venv'
    chdir = '/tmp'
    out = 'test_out'
    err = 'test_err'
    _setup_virtualenv(params, env, chdir, out, err)



# Generated at 2022-06-13 05:53:38.765902
# Unit test for function main
def test_main():
    args = dict(
        state='present',
        name=['PyYaml'],
        version=None,
        requirements=None,
        virtualenv=None,
        virtualenv_site_packages=False,
        virtualenv_command='virtualenv',
        virtualenv_python=None,
        extra_args=None,
        editable=False,
        chdir='None',
        executable=None,
        umask='None',
    )
    main(args)

if __name__ == '__main__':
    main(sys.argv)

# Generated at 2022-06-13 05:53:50.038121
# Unit test for constructor of class Package
def test_Package():
    # Test for the absence of version specifier
    pip_package = Package('pip')
    assert pip_package.package_name == 'pip'
    assert not pip_package.has_version_specifier

    # Test for the presence of version specifier
    pip_package = Package('pip', '>= 8.0')
    assert pip_package.package_name == 'pip'
    assert pip_package.has_version_specifier
    assert pip_package.is_satisfied_by('8.0')
    assert not pip_package.is_satisfied_by('7.0')

    # Test for the canonicalization of package name
    pip_package = Package('pip')
    assert pip_package.package_name == 'pip'

# Generated at 2022-06-13 05:53:53.183942
# Unit test for function main
def test_main():
    doc, func =module._get_module_facts('/usr/bin/ansible/module_utils/basic.py')
    print(doc)
    print(func)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:53:59.984538
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # Testing simple comparator
    # == =
    assert Package("foo", "2").is_satisfied_by("2") is True
    assert Package("foo", "==2").is_satisfied_by("2") is True
    assert Package("foo", "2").is_satisfied_by("3") is False
    assert Package("foo", "==2").is_satisfied_by("3") is False

    # >= >=
    assert Package("foo", ">=2").is_satisfied_by("2") is True
    assert Package("foo", "2").is_satisfied_by("1") is False
    assert Package("foo", ">=2").is_satisfied_by("1") is False

    # <= <=
    assert Package("foo", "<=2").is_satisfied_by

# Generated at 2022-06-13 05:54:01.277689
# Unit test for function main
def test_main():
    # function main
    pass
# Unit tests for function _is_present

# Generated at 2022-06-13 05:54:03.376717
# Unit test for function main
def test_main():
    with patch('ansible_collections.ansible.community.plugins.module_utils.parsing.convert_bool', return_value=True):
        assert main() is False

# Generated at 2022-06-13 05:55:33.400370
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = FakeModule({
        'virtualenv_command': "virtualenv",
        'virtualenv_site_packages': False,
        'virtualenv_python': None
    })
    env = "ansible-test-venv"
    chdir = ""
    out = ""
    err = ""
    # subtract 1 to ignore "setup_virtualenv"
    assert len(inspect.stack()) - 1 == setup_virtualenv(module, env, chdir, out, err)



# Generated at 2022-06-13 05:55:43.608687
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    #test setup_virtualenv using virtualenv
    ansible_module = AnsibleModule({'virtualenv_command':'virtualenv',
                                    'virtualenv_site_packages': False,
                                    'virtualenv_python': None},
                                   "",True,False)
    ansible_module.run_command = MagicMock(return_value=[0,'out','err'])
    out,err = setup_virtualenv(ansible_module,'env','chdir','','','','','','','','','','','','','','','','')
    assert out == 'out'
    assert err == 'err'

    #test setup_virtualenv using pyvenv

# Generated at 2022-06-13 05:55:55.984100
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """Unit test for function setup_virtualenv"""
    PIP_PATH = '/usr/bin/pip'

    # With virtualenv_python
    cmd = ['/venv/virtualenv', '-p', '/opt/python/python-2.7.8/bin/python', '/venv/test1']
    assert setup_virtualenv(None, None, None, None, None)[0] == cmd

    # With venv or pyvenv and virtualenv_python
    cmd = ['/venv/virtualenv', '/venv/test1']
    assert setup_virtualenv(None, None, None, None, None)[0] == cmd

    # With sys.executable
    cmd = ['/venv/virtualenv', '-p', PIP_PATH, '/venv/test1']

# Generated at 2022-06-13 05:56:06.847424
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.parsing.convert_bool import boolean
    import tempfile
    module = AnsibleModule(argument_spec={
        'virtualenv_command': dict(type='path', default='virtualenv'),
        'virtualenv_python': dict(type='path'),
        'virtualenv_site_packages': dict(type='bool', default=True, aliases=['virtualenv_system_site_packages']),
    }, supports_check_mode=True)

    module.run_command = MagicMock(return_value=(0, 'virtualenv out', 'virtualenv err'))
    module.get_bin_path = MagicMock(return_value='/usr/bin/virtualenv')
    module.check_mode = False
    module

# Generated at 2022-06-13 05:56:14.604981
# Unit test for constructor of class Package
def test_Package():
    assert not Package('setuptools', '36.2.0').has_version_specifier
    assert Package('setuptools>=36.2.0').has_version_specifier
    assert Package('setuptools>=36.2.0').is_satisfied_by('36.2.0')
    assert Package('setuptools>=36.2.0').is_satisfied_by('36.3.0')
    assert not Package('setuptools>=36.2.0').is_satisfied_by('36.1.0')
    assert Package('setuptools==36.2.0').is_satisfied_by('36.2.0')
    assert not Package('setuptools==36.2.0').is_satisfied_by('36.2.1')

# Generated at 2022-06-13 05:56:16.732942
# Unit test for function main
def test_main():
    assert main() == None


# Unit test

# Generated at 2022-06-13 05:56:24.789479
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import mock
    import cStringIO
    import contextlib

    class _module(object):
        def __init__(self):
            self.params = {'virtualenv_site_packages': 'False',
                           'virtualenv_command': 'pyvenv-3.5',
                           'virtualenv_python': ''}

        @staticmethod
        def get_bin_path(val, warn, opt_dirs):
            print('get_bin_path: %s' % val)
            return '/usr/bin/%s' % val

        @staticmethod
        @contextlib.contextmanager
        def _redirect_stdout(new_stdout):
            old_stdout = cStringIO.StringIO()
            old_stdout = sys.stdout
            sys.stdout = new_stdout

# Generated at 2022-06-13 05:56:25.661744
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # TODO: Add unit test
    pass



# Generated at 2022-06-13 05:56:31.529602
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec={
        'virtualenv_command': dict(type='str', required=True),
        'virtualenv_python': dict(type='str', required=False),
        'virtualenv_site_packages': dict(type='bool', default=False),
        'virtualenv_init': dict(type='bool', default=True),
    })
    env = '/tmp/virtualenv'
    chdir = '.'
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out
    assert not err


# Generated at 2022-06-13 05:56:33.494285
# Unit test for function main
def test_main():
    def test_module(**kwargs):
        dummy_module = MagicMock()
        dummy_module.params = kwargs
        return dummy_module

    main(test_module(virtualenv='my_env'))

# Generated at 2022-06-13 05:58:08.022158
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec=dict(virtualenv_command='virtualenv'))
    env = "test_setup_virtualenv"
    chdir = "/tmp"
    out = ""
    err = ""
    cmd = shlex.split(module.params['virtualenv_command'])
    cmd.append(env)
    rc = module.run_command(cmd, cwd=chdir)
    if rc != 0:
        _fail(module, cmd, out, err)
    print (out,err)



# Generated at 2022-06-13 05:58:12.113078
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = MockModule()
    setup_virtualenv(module=MockModule(),
                     env='/var/tmp/venv',
                     chdir='/var/tmp',
                     out='',
                     err='')



# Generated at 2022-06-13 05:58:21.017596
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    class FakeModule:
        class FakeParams:
            virtualenv_command = 'python -m venv'
            virtualenv_python = None
        class FakeRun:
            rc = 0
        def __init__(self):
            self.params = FakeModule.FakeParams()
            self.run_command = lambda cmd, cwd=None: FakeModule.FakeRun()
    m = FakeModule()
    env = 'mytestenv'
    chdir = 'mychdir'
    out = 'myout'
    err = 'myerr'
    out, err = setup_virtualenv(m, env, chdir, out, err)
    assert(out=='myout')
    assert(err=='myerr')


# Generated at 2022-06-13 05:58:30.033169
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    assert Package("ansible", "2.4.0").is_satisfied_by("2.4.0")
    assert Package("ansible", "==2.4.0").is_satisfied_by("2.4.0")
    assert Package("ansible", ">=2.4.0").is_satisfied_by("2.4.0")

    assert not Package("ansible", ">=2.4.0").is_satisfied_by("2.3.0")
    assert not Package("ansible", ">=2.4.0").is_satisfied_by("2.3.1")
    assert not Package("ansible", ">=2.4.0").is_satisfied_by("2.3.9")


# Generated at 2022-06-13 05:58:37.140269
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # positive cases
    packages = [
        ('foo', 'bar==1.0', '1.0'),
        ('foo', 'bar==1.0', '1.0.0'),
        ('foo', 'bar==1.0.0', '1.0'),
        ('foo', 'bar==1.0.0', '1.0.0'),
        ('foo', 'bar==1.0.0.0', '1.0.0')
    ]

    for package_name, requirement, version in packages:
        pkg = Package(package_name, requirement)
        assert pkg.is_satisfied_by(version)



# Generated at 2022-06-13 05:58:45.247365
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_native
    import ansible.module_utils.parsing.convert_bool as to_bool
    from glob import glob
    from os.path import join, isdir, exists
    from shutil import rmtree
    import sys

    env = {
        'VIRTUAL_ENV': None,
        'LANG': 'C',
        'LC_ALL': 'C',
        'PATH': '/bin:/usr/bin',
    }

    if not HAS_SETUPTOOLS:
        sys.modules['pkg_resources'] = None

    if not HAS_PIP:
        sys.modules['pip'] = None


# Generated at 2022-06-13 05:58:53.192605
# Unit test for function setup_virtualenv

# Generated at 2022-06-13 05:59:04.651016
# Unit test for function main
def test_main():
    # Arguments used in the following test case
    argument = {
        "state": "present",
        "name": ["ansible-test"],
        "version": "1.0.0",
        "requirements": "requirements.txt",
        "virtualenv": "venv",
        "virtualenv_site_packages": False,
        "virtualenv_command": "virtualenv",
        "virtualenv_python": "python",
        "extra_args": "--download-cache /var/cache/pip",
        "editable": False,
        "chdir": "/ansible/test",
        "executable": "python",
        "umask": "0077",
    }