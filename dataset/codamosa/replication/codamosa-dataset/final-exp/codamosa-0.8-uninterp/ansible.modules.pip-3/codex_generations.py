

# Generated at 2022-06-13 05:50:01.051455
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.common.process import get_bin_path
    bin_path = get_bin_path('python')
    env_path = os.path.abspath('venv')
    if os.path.exists(env_path):
        shutil.rmtree(env_path)
    module = FakeModule(**{
        'virtualenv_command': bin_path,
        'virtualenv_site_packages': True,
        'virtualenv_python': '',
    })
    out, err = setup_virtualenv(module, env_path, None, '', '')
    assert os.path.exists(os.path.join(env_path, 'pyvenv.cfg'))



# Generated at 2022-06-13 05:50:09.824644
# Unit test for function main
def test_main():
    args = dict(
        name='ansible',
        requirements=None,
        state='present',
        extra_args='--allow-external',
    )
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['present', 'absent', 'latest']),
            name=dict(type='list', elements='str'),
            version=dict(type='str'),
            requirements=dict(type='str'),
            extra_args=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    main()

if __name__ == '__main__':
#     test_main()
    main()

# Generated at 2022-06-13 05:50:15.479371
# Unit test for function main
def test_main():
    """ This is a dummy test for function main """
    module = mock.MagicMock()
    module.exit_json = module.exit_json
    module.fail_json = module.fail_json
    pip_version = pip.__version__
    assert pip_version.startswith('1.5.6')



# Generated at 2022-06-13 05:50:17.366066
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    assert Package('six').is_satisfied_by('1.1.0')



# Generated at 2022-06-13 05:50:24.845272
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import sys
    import os
    import shlex
    module_name = "ansible_test_setup_virtualenv_module"
    if module_name in sys.modules:
        # the test function can only be run once
        # because it mocks a AnsibleModule object
        # and already imported modules can't be
        # reloaded in Python 2.x
        return
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.pip import setup_virtualenv


# Generated at 2022-06-13 05:50:34.683125
# Unit test for function main
def test_main():
    import ansible.constants
    ansible.constants.HOST_VARIABLES = {"virtualenv" : "/tmp/mockve/"}
    # mock the built-in function
    main_mock = MagicMock(return_value=None)
    with patch.object(ansible_collections.ansible.community.plugins.module_utils.common.base, 'main') as mocked_main:
        mocked_main.return_value = main_mock
        ansible_collections.ansible.community.plugins.module_utils.common.base.main()
    assert main_mock.called

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:50:47.589678
# Unit test for function main
def test_main():
    # Testing functions
    def get_module(param):
        """Returns a test module."""
        return MagicMock(params=param)

    def get_command(module):
        """Returns the command to execute."""
        return ' '.join(module.run_command.call_args[0][0])

    name = 'PyMySQL'
    version = '0.7.2'
    requirements = '/path/to/requirements.txt'
    virtualenv = '/path/to/virtualenv'
    umask = '066'

# Generated at 2022-06-13 05:50:59.029664
# Unit test for function main

# Generated at 2022-06-13 05:51:00.113662
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-13 05:51:08.049852
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package('foo', '1.2.2')
    assert pkg.is_satisfied_by('1.2.2')
    assert pkg.is_satisfied_by('1.3.0')
    assert not pkg.is_satisfied_by('1.2.0')
    assert not pkg.is_satisfied_by('1.2.2.post0')
    assert not pkg.is_satisfied_by('bar')

    pkg = Package('foo', '<=1.3.0')
    assert pkg.is_satisfied_by('1.2.2')
    assert pkg.is_satisfied_by('1.3.0')
    assert not pkg.is_satisfied_by('1.4.0')

    p

# Generated at 2022-06-13 05:51:39.638479
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:51:50.159312
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pips._text import to_native
    from ansible.module_utils.pips.setuptools import has_setuptools
    import ansible.module_utils.pips.setuptools
    import ansible.module_utils.pips.virtualenv
    import ansible.module_utils.pips.virtualenv_command

    if not has_setuptools:
        print('skipping due to missing setuptools dependency')
        return


# Generated at 2022-06-13 05:51:58.352447
# Unit test for function main

# Generated at 2022-06-13 05:52:03.884882
# Unit test for constructor of class Package
def test_Package():  # noqa
    # Package name with version specifier
    pkg = Package('paramiko', '==2.0.0')
    assert pkg.package_name == 'paramiko'
    assert pkg.has_version_specifier
    assert pkg.is_satisfied_by('2.0.3')

    # Package name without version specifier
    pkg = Package('pip')
    assert pkg.package_name == 'pip'
    assert not pkg.has_version_specifier
    assert not pkg.is_satisfied_by('2.0.3')

    # Package name with "white space"
    pkg = Package('django', '<1.11')
    assert pkg.package_name == 'django'
    assert pkg.has_version_specifier

# Generated at 2022-06-13 05:52:10.403075
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = DummyModule()
    env = '/tmp/test_venv'
    chdir = '/Users/laurent'
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert(out == "New python executable in /tmp/test_venv/bin/python\n" +
           "Installing setuptools............done.\n" +
           "Installing pip..................done.\n")
    assert(err == "")



# Generated at 2022-06-13 05:52:21.532259
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import ansible_collections.ansible.community.tests.unit.modules.utils.pip_common as utils
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    with patch.object(utils, '_get_cmd_options', return_value=[]):
        with patch.object(utils, 'is_executable', return_value=True):
            with patch.object(utils, '_fail') as fake_fail:
                module = AnsibleModule({})
                out_venv, err_venv = utils.setup_virtualenv(module, '/venv', 'chdir', 'out_venv', 'err_venv')
                assert out_venv == 'out_venv'
                assert err

# Generated at 2022-06-13 05:52:28.284789
# Unit test for function main
def test_main():
    run_main(requirements=None,
             version=None,
             name='selinux',
             virtualenv='ENV',
             virtualenv_command='virtualenv',
             virtualenv_site_packages=False,
             chdir='chdir',
             state='present',
             extra_args=None,
             editable=False,
             executable=None,
             umask=None)


# Generated at 2022-06-13 05:52:38.642437
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    if not PY2:
        # this method is not used by pip v10+
        return

    tests = [
        ('pytz', '==2016.10'),
        ('pytz', '==2016.10.pytz.SHA1hexdigest'),
        ('pytz', '>=2016.7'),
        ('pytz', '!=2016.10'),
        ('pytz', '!=2016.10.pytz.SHA1hexdigest'),
        ('pytz', '>=2016.7,<2017.0a0'),
    ]
    for name, ver in tests:
        req = Package(name, ver)
        assert req.has_version_specifier
        assert not req.is_satisfied_by('2016.6')
        assert req.is_satisfied_by('2016.10')
       

# Generated at 2022-06-13 05:52:45.583834
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    p = Package("foo")
    assert not p.is_satisfied_by("1.0")
    p = Package("foo==1.0")
    assert p.is_satisfied_by("1.0")
    p = Package("foo==1.0")
    assert not p.is_satisfied_by("1.1")
    p = Package("foo>=1.0")
    assert p.is_satisfied_by("1.0")
    assert p.is_satisfied_by("1.1")
    assert not p.is_satisfied_by("0.9")
    p = Package("foo>1.0")
    assert not p.is_satisfied_by("1.0")
    assert p.is_satisfied_by("1.1")

# Generated at 2022-06-13 05:52:53.974391
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:53:59.354464
# Unit test for function main

# Generated at 2022-06-13 05:54:02.713743
# Unit test for function main
def test_main():
    # Placeholder for future unittest
    assert True == True

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils._text import to_native

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:54:13.993824
# Unit test for function main
def test_main():
    '''
    Unit test for function main
    '''
    # Setup Ansible parameters
    params = dict(
        state='present',
        name=['requests'],
        requirements=None,
        virtualenv=None,
        virtualenv_site_packages=False,
        virtualenv_command='virtualenv',
        virtualenv_python=None,
        extra_args=None,
        editable=False,
        chdir=None,
        executable=None,
        umask=None,
    )

    # Setup AnsibleModule
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:54:15.968373
# Unit test for function main

# Generated at 2022-06-13 05:54:24.984853
# Unit test for constructor of class Package
def test_Package():
    testcase_str = 'pytest==3.0.3'
    pkg = Package(testcase_str)
    assert pkg.package_name == 'pytest'
    assert pkg.has_version_specifier
    assert pkg.is_satisfied_by("3.0.3")
    assert not pkg.is_satisfied_by("3.0")
    assert not pkg.is_satisfied_by("3.0.5")

    pkg = Package("setuptools")
    assert pkg.package_name == 'setuptools'
    assert not pkg.has_version_specifier

    pkg = Package("setuptools==16.0")
    assert pkg.package_name == 'setuptools'
    assert pkg.has_version_specifier
    assert p

# Generated at 2022-06-13 05:54:33.601883
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    import pytest
    package_name = 'nginx'
    p1 = Package(package_name, '1.10')
    assert not p1.is_satisfied_by('1.2.1')
    assert not p1.is_satisfied_by('2.0')

    assert p1.is_satisfied_by('1.10')
    assert p1.is_satisfied_by('1.11')
    assert p1.is_satisfied_by('1.10.99')
    assert p1.is_satisfied_by('1.10.0.a1')

    p2 = Package(package_name, '>=1.10')
    assert p2.is_satisfied_by('1.10')

# Generated at 2022-06-13 05:54:45.604351
# Unit test for function main
def test_main():
    temp_dir = tempfile.mkdtemp()
    temp_venv = os.path.join(temp_dir, 'venv')

# Generated at 2022-06-13 05:54:55.591468
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    import unittest

# Generated at 2022-06-13 05:55:01.904975
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import os
    import tempfile
    import shutil
    import shlex
    def run_command(cmd, cwd=None, environ_update=None,
                    use_unsafe_shell=False, data=None):

        p = subprocess.Popen(cmd,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             cwd=cwd,
                             env=os.environ.copy(),
                             shell=use_unsafe_shell)
        (stdout, stderr) = p.communicate()
        return p.returncode, stdout, stderr

    class Module(object):
        def __init__(self):
            self.params = dict()
            self.check_

# Generated at 2022-06-13 05:55:08.203086
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    for _module in modules:
        setuptools_path = os.path.join(_module.params['pip_exec'], 'setuptools')
        os.symlink(sys.argv[0], setuptools_path)
        _module.params['pip_exec'] = which_pip_exec
        out, err = setup_virtualenv(_module, env, chdir, out, err)
        os.remove(setuptools_path)
        assert err.count('Successfully installed') == 1
        del _module.params['pip_exec']



# Generated at 2022-06-13 05:57:02.082908
# Unit test for function setup_virtualenv
def test_setup_virtualenv():

    import sys
    import os
    import shutil
    import tempfile
    import subprocess
    # TODO: Should use this instead of mocked get_bin_path below
    import ansible.module_utils.basic as basic
    basic.MODULE_COMPLEX_ARGS = dict(virtualenv_python=dict())

    class MyModule(object):
        params = dict(virtualenv_command='pyvenv')
        args = dict(virtualenv_python='python2')

        def get_bin_path(self, arg, *args):
            return arg

        def run_command(self, cmd, cwd=None):
            """
            :param cmd: command like
                    ["/path/to/python2", "-m", "virtualenv", "/path/to/venv"]
            :return:
            """
            process = subprocess

# Generated at 2022-06-13 05:57:06.771546
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = get_readonly_fake_module()
    module.params = {'virtualenv_python': None, 'virtualenv_command': '/usr/bin/virtualenv', 'virtualenv_site_packages': False }
    module.run_command = create_runner(module)
    assert isinstance(setup_virtualenv(module, env='testenv', chdir='testdir', out='', err=''), tuple)



# Generated at 2022-06-13 05:57:11.736864
# Unit test for constructor of class Package
def test_Package():
    # test case for requirement contains version specifier
    assert str(Package("setuptools", "3.3.3")) == "setuptools==3.3.3"
    assert str(Package("setuptools", ">=3.3.3")) == "setuptools>=3.3.3"

    # test case for plain package
    assert str(Package("django")) == "django"

    # test case for package with invalid specifier
    assert str(Package("django==!")) == "django==!"


# ===========================================
# Module execution.
#



# Generated at 2022-06-13 05:57:15.096644
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    env = tempfile.mkdtemp()

    module = AnsibleModule(
        {
            'virtualenv_command': 'virtualenv',
            'virtualenv_python': '/usr/bin/python2.7'
        }
    )

    out, err = setup_virtualenv(module, env, '', '', '')

    shutil.rmtree(env)

    assert re.search(r'Running virtualenv with interpreter', str(out))
    assert not err



# Generated at 2022-06-13 05:57:16.906882
# Unit test for function main
def test_main():
    # TODO: mock functions and objects
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:57:29.595934
# Unit test for function main
def test_main():
    pip_cmd = "/usr/bin/python -m pip"
    cmd = [pip_cmd, 'install', '-U', 'ansible[azure]', '-vvvv']
    print()
    # print(cmd)
    m = mock.MagicMock()
    m.params = {'virtualenv': None}
    m.check_mode = False
    m.run_command.return_value = 1, 'Successfully installed ansible-2.9.6', ''
    out, err = get_cmd_data(m, pip_cmd, cmd)
    print(out)
    print(err)
    assert out == 'Successfully installed ansible-2.9.6'
    assert err == ''


# Generated at 2022-06-13 05:57:31.777851
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert 1 == 1



# Generated at 2022-06-13 05:57:39.845172
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes
    from io import StringIO

    # Setup a basic module for testing and initialize some static test data

# Generated at 2022-06-13 05:57:41.350677
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:57:42.528505
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    #TODO
    return {}

