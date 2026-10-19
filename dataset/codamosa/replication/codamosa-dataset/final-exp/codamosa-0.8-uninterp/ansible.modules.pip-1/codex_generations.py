

# Generated at 2022-06-13 05:49:49.899838
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    cmd = ["pyvenv", "venv"]
    out = ""
    err = ""
    create_virtualenv = setup_virtualenv(module, cmd, cwd=chdir, out=out, err=err)
    if rc != 0:
        _fail(module, cmd, out, err)
    module.exit_json(changed=True)



# Generated at 2022-06-13 05:49:50.381289
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:50:00.200631
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    from distutils.version import LooseVersion
    from distutils.version import StrictVersion

    # Test normal version
    assert Package(package_name='pbr', version_string='>=1.1').is_satisfied_by(LooseVersion('1.2'))
    assert Package(package_name='pbr', version_string='>=1.1').is_satisfied_by(LooseVersion('1.2'))
    assert Package(package_name='pbr', version_string='>=1.1').is_satisfied_by(LooseVersion('1.2'))
    assert not Package(package_name='pbr', version_string='>=1.1').is_satisfied_by(LooseVersion('1.0.1'))

# Generated at 2022-06-13 05:50:01.165771
# Unit test for function main
def test_main():
    assert True


# Generated at 2022-06-13 05:50:05.595843
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package('test_package')
    with mock.patch('ansible_collections.ansible.community.plugins.module_utils.pip.LooseVersion', return_value="1.0.0"):
        pkg.is_satisfied_by("1.0.0")



# Generated at 2022-06-13 05:50:10.268840
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    def mock_run_command(self, cmd, cwd=None, environ_update=None, check_rc=False, data=None):
        return 0, "", ""
    # Virtualenv is installed
    module = type('MockModule', (object,), {'params': {'virtualenv_python': '', 'virtualenv_command': ''}, 'run_command': mock_run_command, 'check_mode': False})
    message, err = setup_virtualenv(module, env, chdir, out, err)
    assert message == "" and err == ""
    # Virtualenv is not installed
    module = type('MockModule', (object,), {'params': {'virtualenv_python': 'mock_python', 'virtualenv_command': None}, 'run_command': mock_run_command, 'check_mode': False})

# Generated at 2022-06-13 05:50:20.790761
# Unit test for function main
def test_main():
    test_module = AnsibleModule(argument_spec={
        'state': dict(default='present', choices=['present', 'latest', 'forcereinstall', 'absent']),
        'name': dict(required=True),
        'extra_args': dict(),
        'requirements': dict(),
        'virtualenv': dict(),
        'virtualenv_site_packages': dict(type='bool', default=False),
        'virtualenv_command': dict(default='virtualenv'),
        'virtualenv_python': dict(),
        'editable': dict(default=False, type='bool'),
        'chdir': dict(),
        'executable': dict(),
        'version': dict(),
        'umask': dict(default=None),
    })

# Generated at 2022-06-13 05:50:25.952521
# Unit test for function main
def test_main():
    sys.modules['setuptools'].Requirement = Mock(return_value=object())
    sys.modules['setuptools'].Package = Mock(return_value=object())

    try:
        main()
    except SystemExit as e:
        assert e.code == 0
        pass
    except Exception:
        assert False
    finally:
        del sys.modules['setuptools'].Requirement
        del sys.modules['setuptools'].Package


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:50:36.954423
# Unit test for function main
def test_main():
    sys.modules['ansible.module_utils.basic'] = MockAnsibleModuleUtilsBasic()
    sys.modules['ansible.module_utils.setup'] = MockAnsibleModuleUtilsSetup()
    sys.modules['ansible.module_utils.path'] = MockAnsibleModuleUtilsPath()
    sys.modules['ansible.module_utils.parsing.convert_bool'] = MockAnsibleModuleUtilsParsingConvertBool()
    sys.modules['ansible.module_utils.parsing.splitter'] = MockAnsibleModuleUtilsParsingSplitter()
    sys.modules['ansible.module_utils.parsing.urlparse'] = MockAnsibleModuleUtilsParsingUrlparse()
    sys.modules['ansible.module_utils.distribution'] = MockAn

# Generated at 2022-06-13 05:50:48.591838
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert setup_virtualenv(['pyvenv','/home/neels/test_setup_virtualenv_1']) == 0
    assert setup_virtualenv(['-m venv','/home/neels/test_setup_virtualenv_2']) == 0
    assert setup_virtualenv(['virtualenv','/home/neels/test_setup_virtualenv_3']) == 0
    assert setup_virtualenv(['/home/neels/virtualenv','/home/neels/test_setup_virtualenv_4']) == 0
    assert setup_virtualenv(['virtualenv','/home/neels/test_setup_virtualenv_5','-p/usr/bin/python2']) == 0

# Generated at 2022-06-13 05:51:29.620242
# Unit test for function setup_virtualenv
def test_setup_virtualenv():

    from ansible.modules.packaging.os import pip

    class FakeModule(object):

        def __init__(self, params):
            self.params = params

        def run_command(self, cmd, cwd=None, environ_update=None):
            return 0, '', ''

        def get_bin_path(self, name, required, opt_dirs=[]):
            return '/bin/%s' % name

        def fail_json(self, **kwargs):
            pass

        def exit_json(self, **kwargs):
            pass

    class FakePIP(object):

        def __init__(self):
            self.packages = []

        def run(self, module, venv=None):
            return dict(
                changed=True,
                results=self.packages,
            )


# Generated at 2022-06-13 05:51:38.668361
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock(check_mode=False, params={'virtualenv_command': '/usr/bin/virtualenv','virtualenv_site_packages': False, 'virtualenv_python': '/usr/bin/python3'})
    module.get_bin_path = Mock(return_value='/usr/bin/python3')
    virtualenv_python = module.params['virtualenv_python']
    env = ''
    chdir = ''
    out = ''
    err = ''
    cmd = shlex.split(module.params['virtualenv_command'])
    #cmd = ['/usr/bin/virtualenv', '-p/usr/bin/python3', 'test-env']
    setup_virtualenv(module, env, chdir, out, err)

# Generated at 2022-06-13 05:51:49.511392
# Unit test for function main
def test_main():
    with tempfile.TemporaryDirectory() as venv:
        path = os.path.abspath(venv)

        result = {}

        result['state'] = 'present'
        result['name'] = ['ansible']
        result['version'] = '2.6.5'
        result['requirements'] = '/home/cyoung/ansible/requirements.txt'
        result['virtualenv'] = path
        result['virtualenv_site_packages'] = False
        result['virtualenv_command'] = 'virtualenv'
        result['virtualenv_python'] = ''
        result['extra_args'] = ''
        result['editable'] = False
        result['chdir'] = '/home/cyoung/ansible'
        result['executable'] = ''
        result['umask'] = ''

        obj = {}



# Generated at 2022-06-13 05:51:58.305933
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    import pytest
    # simple case
    assert Package('foo', '1.0').is_satisfied_by('1.0')
    assert Package('foo', '>1.0').is_satisfied_by('1.1')
    assert not Package('foo', '>1.0').is_satisfied_by('1.0')
    assert Package('foo', '>=1.0').is_satisfied_by('1.0')

    # composite case
    assert Package('foo', '>1.0,<2.0').is_satisfied_by('1.5')
    assert not Package('foo', '>1.0,<2.0').is_satisfied_by('0.5')
    assert not Package('foo', '>1.0,<2.0').is_satisf

# Generated at 2022-06-13 05:52:09.689662
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    def run_module(*args, **kwargs):
        if 'check_invalid_arguments' not in kwargs:
            kwargs['check_invalid_arguments'] = False
        if '_ansible_check_mode' not in kwargs:
            kwargs['_ansible_check_mode'] = False

        if '_ansible_diff' not in kwargs:
            kwargs['_ansible_diff'] = False

        if '_ansible_verbosity' not in kwargs:
            kwargs['_ansible_verbosity'] = 0


# Generated at 2022-06-13 05:52:21.051859
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    import ansible.module_utils.basic

    # need to be able to create a module object
    if PY3:
        AnsibleModule = types.SimpleNamespace(
            AnsibleModule=AnsibleModule,
            fail_json=ansible.module_utils.basic.fail_json,
            exit_json=ansible.module_utils.basic.exit_json
        )

# Generated at 2022-06-13 05:52:22.978173
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:52:31.676845
# Unit test for function main
def test_main():
    # Skip this test if running with python2.6 (pip9.0.1 installation fails)
    if sys.version_info[:3] < (2, 7):
        return
    # Install pip9.0.1 on test system.
    # Currently we don't have a better way to test this code.
    import pip9
    pip9.main(['install', 'pip==9.0.1'])


# Generated at 2022-06-13 05:52:42.760337
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    req = Package('pkg_a==0.0.1')
    assert req.is_satisfied_by('0.0.1')

    req = Package('pkg_b', '!=0.0.2')
    assert req.is_satisfied_by('0.0.1')

    req = Package('pkg_b', '>=1.0.0')
    assert req.is_satisfied_by('2.0.0')

    req = Package('pkg_b', '<4.0.0,>=3.0.0')
    assert req.is_satisfied_by('3.5.0')
    assert not req.is_satisfied_by('1.0.0')
    assert not req.is_satisfied_by('4.0.0')

# Generated at 2022-06-13 05:52:52.544108
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    class TestModule(object):
        def __init__(self):
            self.fail_json = lambda msg: self.failures.append(msg)
            self.failures = []

    module = TestModule()
    name_string = 'pip'

# Generated at 2022-06-13 05:54:00.421185
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    fr = FakeRunner()
    module = FakeModule(runner=fr)
    env ="/tmp/env"
    chdir = "/some/tmp/directory"
    out = ""
    err = ""
    setup_virtualenv(module, env, chdir, out, err)
    assert fr.commands_ran == [
        ['virtualenv', '--no-site-packages', env]
    ]



# Generated at 2022-06-13 05:54:07.957050
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    env = '/home/bob/testvenv'
    chdir = '/home/bob/projects'
    out = 'foo'
    err = 'bar'
    # TODO: parametrize this with a bunch of virtualenv_commands as well as
    # a bunch of virtualenv_pythons
    def run_command(self, cmd, cwd=None, environ_update=None,
                    check_rc=False, executable=None, data=None):
        if self.params['virtualenv_command'] != 'venv':
            self.assertEqual(cmd,
                             ['virtualenv',
                              '--system-site-packages',
                              '-p/usr/bin/python',
                              env])

# Generated at 2022-06-13 05:54:15.261856
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import shutil
    module = AnsibleModule(
        argument_spec={
            "virtualenv_python": {},
            "virtualenv_command": {},
            "virtualenv_site_packages": {},
        },
    )
    env = tempfile.mkdtemp()
    chdir = tempfile.mkdtemp()
    try:
        out, err = setup_virtualenv(module, env, chdir, '', '')
    finally:
        # clean up
        shutil.rmtree(env)
        shutil.rmtree(chdir)



# Generated at 2022-06-13 05:54:16.583125
# Unit test for function main
def test_main():
    assert main() is None


# Generated at 2022-06-13 05:54:23.724116
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    name_string = 'Django'
    version_string = '==1.6.1'
    pkg = Package(name_string, version_string)
    assert pkg.is_satisfied_by('1.6.1')
    assert pkg.is_satisfied_by('1.6.1.1')
    assert not pkg.is_satisfied_by('1.6.2')
    assert not pkg.is_satisfied_by('1.6.1-beta1')



# Generated at 2022-06-13 05:54:32.690810
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={
        'virtualenv_command': {'required': True},
        'virtualenv_site_packages': {'required': True},
        'virtualenv_python': {'required': True},
    })

    result_out = 'Test output\n'
    result_err = 'Test error\n'
    result_out, result_err = setup_virtualenv(module, 'venv', '.', result_out, result_err)
    assert result_out == 'Test output\n'
    assert result_err == 'Test error\n'


# Generated at 2022-06-13 05:54:33.662291
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # TODO: add unit test for function setup_virtualenv
    pass



# Generated at 2022-06-13 05:54:35.189624
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:54:38.024626
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    try:
        import virtualenv
    except ImportError:
        module.fail_json(msg=('Unable to import virtualenv or pyvenv or venv'
                              ' to create a virtualenv'))
    setup_virtualenv(module, env, chdir, out, err)
    pass



# Generated at 2022-06-13 05:54:39.973836
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:56:57.788820
# Unit test for function main
def test_main():
    import argparse
    from ansible.module_utils.basic import env_fallback, AnsibleModule
    if sys.version_info >= (2, 7):
        import nose
        import nose.core
        import unittest
        import os
        import shutil
        import tempfile
        import textwrap
        import subprocess
        from nose.plugins.attrib import attr
        @attr(type='smoke')
        class TestPip(unittest.TestCase):
            @classmethod
            def setUpClass(self):
                """Setup AnsibleModule instance and pip module"""
                parser = argparse.ArgumentParser()
                parser.add_argument('-m', dest='module_path', required=True)
                parser.add_argument('-a', dest='module_args', required=True)

# Generated at 2022-06-13 05:57:07.308136
# Unit test for constructor of class Package
def test_Package():
    pkg = Package('ansible', '2.4.3.0')
    assert pkg.package_name == 'ansible'
    assert pkg.has_version_specifier is True
    assert pkg.is_satisfied_by('2.4.3.0') is True
    assert pkg.is_satisfied_by('2.4.4.0') is False

    pkg = Package('ansible', '>2.4.3.0')
    assert pkg.package_name == 'ansible'
    assert isinstance(pkg._requirement.specifier, SpecifierSet)
    assert pkg._requirement.specifier.contains('2.4.3.0', prereleases=True) is True

# Generated at 2022-06-13 05:57:13.677316
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # assert that virtualenv_python is ignored
    module = type('module', (object,), {
        'check_mode': False,
        'params': {
            'virtualenv_command': 'pyvenv',
            'virtualenv_python': 'python3',
            'virtualenv_site_packages': False,
        },
        'get_bin_path': lambda x, y, z: x,
        'run_command': lambda x, cwd=None: [0, '', '']
    })
    env = '/tmp/env'
    chdir = os.getcwd()
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert not any(ex in out for ex in ('-p', 'python3'))
    assert not any

# Generated at 2022-06-13 05:57:14.376234
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:57:20.042539
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # the example from PEP 440
    req_str = "B >= 1.0, ==1.0.2, !=1.1.0, <2.0"
    req = Requirement.parse(req_str)
    package = Package("B", req_str)
    assert package.is_satisfied_by("1.0") == True
    assert package.is_satisfied_by("1.0.0") == True
    assert package.is_satisfied_by("1.0.2") == True
    assert package.is_satisfied_by("1.1.0") == False
    assert package.is_satisfied_by("1.0.2.0") == True
    assert package.is_satisfied_by("2.0") == False
    # the example in PEP 386


# Generated at 2022-06-13 05:57:21.909022
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:57:32.927887
# Unit test for function main
def test_main():
    """ Setup a basic test environment to test main functions. """
    from ansible.module_utils.basic import AnsibleModule
    import json


# Generated at 2022-06-13 05:57:33.449058
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:57:34.266678
# Unit test for function main
def test_main():
    # Test basic execution
    pass

# Generated at 2022-06-13 05:57:36.134228
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()