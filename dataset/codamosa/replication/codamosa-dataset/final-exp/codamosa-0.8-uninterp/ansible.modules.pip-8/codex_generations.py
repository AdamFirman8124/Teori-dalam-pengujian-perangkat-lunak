

# Generated at 2022-06-13 05:49:43.507253
# Unit test for function main
def test_main():
    # Note: AnsibleModule.exit_json and AnsibleModule.fail_json cannot be used in unit tests.
    # AnsibleModule.exit_json(changed=False, meta=dict(arg1='value'))
    # AnsibleModule.fail_json(msg='error')
    assert False


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:49:51.251070
# Unit test for function main
def test_main():
    import mock
    import os
    from ansible.module_utils import basic

    # get an empty basic AnsibleModule
    def new_module(spec):
        mod = basic.AnsibleModule(
            argument_spec=dict(
                name=dict(type='list', elements='str'),
                version=dict(type='str'),
                requirements=dict(type='str'),
                virtualenv=dict(type='path'),
            )
        )
        # Fake valid PIP to avoid failure in _get_pip
        mod.run_command.return_value = (0, "pip 1.5.6 from /usr/lib/python2.7/dist-packages (python 2.7)", "")
        return mod

    # Do assert inside this function
    def check_args(name, version, requirements, virtualenv):
        print

# Generated at 2022-06-13 05:49:57.072620
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # if venv or pyvenv are used and virtualenv_python is defined, then
    # virtualenv_python is ignored, this has to be acknowledged
    assert (setup_virtualenv(
        None, None, None, {
            'virtualenv_python': True,
            'virtualenv_command': 'pyvenv'
        }
    ), 'virtualenv_python should not be used when'
                ' using the venv module or pyvenv as virtualenv_command'
    )


# Generated at 2022-06-13 05:50:07.501090
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', choices=['present', 'absent', 'latest']),
            name=dict(type='list', elements='str'),
            version=dict(type='str'),
            requirements=dict(type='str'),
            virtualenv=dict(type='path'),
            virtualenv_site_packages=dict(type='bool', default=False),
            virtualenv_command=dict(type='path', default='virtualenv'),
            extra_args=dict(type='str'),
            editable=dict(type='bool', default=False),
            chdir=dict(type='path'),
            executable=dict(type='path'),
        ),
        mutually_exclusive=[['name', 'requirements'], ['executable', 'virtualenv']],
    )
   

# Generated at 2022-06-13 05:50:15.991869
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # test for simple version
    assert Package("A").is_satisfied_by("1.0") == True
    assert Package("A").is_satisfied_by("3.0") == True

    # test for version with specifier
    assert Package("A", ">=2,<3").is_satisfied_by("2.0") == True
    assert Package("A", ">=2,<3").is_satisfied_by("2.9") == True
    assert Package("A", ">=2,<3").is_satisfied_by("1.9") == False
    assert Package("A", ">=2,<3").is_satisfied_by("3.0") == False

    # test for version with specifier with loose version

# Generated at 2022-06-13 05:50:20.992849
# Unit test for function setup_virtualenv

# Generated at 2022-06-13 05:50:24.166241
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pak = Package(name_string="test_pack", version_string="<1.0,>=0.0")
    assert pak.is_satisfied_by("0.1")
    assert not pak.is_satisfied_by("2.0")



# Generated at 2022-06-13 05:50:27.707546
# Unit test for function main
def test_main():
    print("Testing main")
    if (not HAS_SETUPTOOLS):
        return
    if (not HAS_PIP):
        return


# Generated at 2022-06-13 05:50:37.918655
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock()
    env = '/home/myuser/myenv'
    chdir = '/home/myuser/'
    out = ''
    err = ''
    module.check_mode = False
    module.params = {'virtualenv_command': 'virtualenv',
                     'virtualenv_python': 'python3',
                     'virtualenv_site_packages': False}

    module.get_bin_path.return_value = 'virtualenv'

    cmd = shlex.split(module.params['virtualenv_command'])
    cmd[0] = module.get_bin_path(cmd[0], True)

    cmd.append('--no-site-packages')

    cmd.append('-p%s' % module.params['virtualenv_python'])
    cmd.append(env)


# Generated at 2022-06-13 05:50:45.299114
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(
        argument_spec = dict(
            virtualenv_command = dict(default = 'virtualenv'),
            virtualenv_python = dict(default = ''),
            virtualenv_site_packages = dict(default = False)
        )
    )
    os.makedirs('/tmp/env/bin')
    output, err = setup_virtualenv(module, '/tmp/env', '', '', '')
    assertTrue(output, err)


# Generated at 2022-06-13 05:51:15.145780
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    class AnsibleModule:
        modules = {}
        results = {}
        fail_json = lambda self, msg: False

# Generated at 2022-06-13 05:51:19.878659
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import os
    import sys
    import tempfile

    env_dir = tempfile.mkdtemp()
    pwd = os.path.realpath(os.curdir)
    os.chdir(env_dir)

# Generated at 2022-06-13 05:51:25.246687
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix='ansible-test')
    module = AnsibleModule({'virtualenv_command': 'pyvenv', 'virtualenv_python': None, 'virtualenv_site_packages': False}, tempdir=tmpdir)
    env = 'test'
    chdir = None
    out = ''
    err = ''
    out_venv, err_venv = setup_virtualenv(module, env, chdir, out, err)
    assert out_venv.startswith('Writing new activate script')



# Generated at 2022-06-13 05:51:31.642138
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock()
    out = ''
    err = ''
    env = '/tmp/test_env'
    chdir = '/tmp/test'
    setup_virtualenv(module,env, chdir, out, err)
    assert os.path.exists(env)
    shutil.rmtree(env)



# Generated at 2022-06-13 05:51:32.233938
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:51:39.966601
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:51:50.484616
# Unit test for function main
def test_main():
    if os.uname()[0] == 'Darwin':
        os.chdir("/tmp")
        fd, requirements = tempfile.mkstemp(suffix='.txt')
        os.close(fd)
        fh = open(requirements, "w")
        fh.write("autologin\n")
        fh.close()
        fd, bad_requirements = tempfile.mkstemp(suffix='.txt')
        os.close(fd)
        fh = open(bad_requirements, "w")
        fh.write("bad_requirements\n")
        fh.close()

# Generated at 2022-06-13 05:51:59.057231
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package('pkg', '2.7')
    assert pkg.is_satisfied_by('2.7')
    assert not pkg.is_satisfied_by('2.6')
    assert not pkg.is_satisfied_by('2.8')
    assert pkg.is_satisfied_by('2.7.0')
    assert not pkg.is_satisfied_by('2.7.0.rc1')
    assert not pkg.is_satisfied_by('2.7.0.dev100')
    assert not pkg.is_satisfied_by('2.7.0.dev100+sha')

    pkg = Package('pkg', '>=2.7,<3.0')

# Generated at 2022-06-13 05:52:10.229903
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pip import setup_virtualenv
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.urls import open_url
    import os
    import stat
    import shutil
    import tempfile
    import subprocess
    import pytest

    def run_command(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None):
        return 0, '', ''


# Generated at 2022-06-13 05:52:17.767376
# Unit test for function main
def test_main():
    module_mock = MagicMock(name='module_mock')
    vm_args = dict(name=None, requirements='requirements', state='present',
                   executable='/usr/bin/python', virtualenv='/var/tmp/test_virtualenv',
                   virtualenv_command='virtualenv', virtualenv_python=None)
    module_mock.params = vm_args
    module_mock.check_mode = False
    module_mock.run_command = MagicMock(name='run_command')

    # Test case when state is latest
    vm_args['state'] = 'latest'
    vm_args['version'] = '1.9.0'
    with pytest.raises(Exception) as e:
        main()

    vm_args['state'] = 'present'

    # Test case when package is

# Generated at 2022-06-13 05:52:52.219304
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package("pytest", "2.2.4")
    assert pkg.is_satisfied_by("2.2.4")
    assert not pkg.is_satisfied_by("2.2.5")
    assert pkg.is_satisfied_by("2.2.5.dev3")

    pkg2 = Package("python-future", "0.11.1")
    assert pkg2.is_satisfied_by("0.11.1")
    assert not pkg2.is_satisfied_by("0.11.2")
    assert not pkg2.is_satisfied_by("0.11.2.dev222")

    pkg3 = Package("distribute", "0.6.24")

# Generated at 2022-06-13 05:53:04.166353
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Virtualenv exists
    def run_command(cmd, chdir):
        return (1, '', '')

    def get_bin_path(arg, opt, dirs):
        return '/bin/python'

    env = ''
    chdir = '/tmp'
    out = ''
    err = ''
    module = mock.MagicMock(check_mode=True)
    module.run_command = run_command
    module.get_bin_path = get_bin_path
    module.params = {
        'virtualenv_command': 'python -m venv',
        'virtualenv_python': 'python2'
    }
    assert setup_virtualenv(module, env, chdir, out, err) == ('', '')

    # Virtualenv does not exist

# Generated at 2022-06-13 05:53:08.219709
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command=dict(required=True)
    ))
    assert setup_virtualenv(module, '/test/test', '/', "", "") is not None


# =============================================================================


# Generated at 2022-06-13 05:53:14.809726
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock(run_command=Mock(return_value=(0, 'test_out', 'test_err')))
    env = 'test'
    chdir = 'test'
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out == 'test_out'
    assert err == 'test_err'



# Generated at 2022-06-13 05:53:26.408573
# Unit test for function main

# Generated at 2022-06-13 05:53:37.089981
# Unit test for constructor of class Package
def test_Package():
    assert 'ansible' == Package('ansible').package_name

    # Check if the constructor correctly parse package name and version
    # specifier.
    assert 'ansible' == Package('ansible==1.0').package_name
    assert 'ansible' == Package('ansible>=1.0').package_name
    assert Package('ansible').has_version_specifier == False
    assert Package('ansible==1.0').has_version_specifier == True
    assert Package('ansible>=1.0').has_version_specifier == True
    assert Package('ansible==1.0').is_satisfied_by('1.0') == True
    assert Package('ansible>=1.0').is_satisfied_by('1.0') == True
    assert Package('ansible==1.0').is_

# Generated at 2022-06-13 05:53:48.407489
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:53:55.474444
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(
        argument_spec=dict(
            virtualenv_command='/usr/bin/virtualenv',
            virtualenv_python='/usr/bin/python2.7',
            virtualenv_site_packages=False,
            virtualenv=None,
            executable=None,
        )
    )
    env = '/tmp/virtualenv'
    chdir = '/tmp'
    out = 'dummy'
    err = 'dummy'
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out != 'dummy'
    assert err == 'dummy'



# Generated at 2022-06-13 05:53:57.425246
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert 1 == 0, "Need to write unit tests for this"


# Generated at 2022-06-13 05:54:04.835419
# Unit test for function main
def test_main():
    # Set module args
    module_args = dict(
        state='present',
        name=["setuptools", "pip"],
        virtualenv="/opt/test/virtualenv",
        chdir="/opt/test/",
        executable="/opt/test/pip",
        umask="022",
    )
    # Set module params
    module = AnsibleModule(argument_spec=module_args)
    saved_os_umask = os.umask(0)  # save umask
    try:
        main()
    finally:
        os.umask(saved_os_umask)  # restore umask


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:54:48.958747
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    setup_virtualenv()
    pass



# Generated at 2022-06-13 05:54:58.333162
# Unit test for constructor of class Package
def test_Package():
    p1 = Package("abc-def")
    assert p1.package_name == "abc-def"
    assert not p1._plain_package

    p2 = Package("abc-def", "1.2.3")
    assert p2.package_name == "abc-def"
    assert p2._plain_package
    assert p2._requirement.project_name == "abc-def"
    assert p2.has_version_specifier
    assert p2.is_satisfied_by("1.2.3")

    p2 = Package("abc_def", "1.2.3")
    assert p2.package_name == "abc-def"
    assert p2._plain_package
    assert p2._requirement.project_name == "abc-def"
    assert p2.has_version_specifier

# Generated at 2022-06-13 05:55:08.089294
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    import ansible.module_utils.basic
    package = Package("foo", "1.2.3")
    assert package.is_satisfied_by("1.2.3") == True
    package = Package("foo", ">1.2.3")
    assert package.is_satisfied_by("1.2.3") == False
    assert package.is_satisfied_by("2.2.3") == True
    package = Package("foo", ">1.2.3,<2.2.3")
    assert package.is_satisfied_by("1.2.3") == False
    assert package.is_satisfied_by("2.2.3") == False
    assert package.is_satisfied_by("1.3.3") == True

# Generated at 2022-06-13 05:55:14.390851
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({
        'virtualenv_command': './venv-program',
        'virtualenv_site_packages': False,
        'virtualenv_python': None,
    }, check_invalid_arguments=False)
    env = '/path/to/my/env'
    chdir = '/path/to/my/directory'
    out = ''
    err = ''
    out_expected = '''Creating virtual environment /path/to/my/env
'''
    err_expected = ''
    out_actual, err_actual = setup_virtualenv(module, env, chdir, out, err)
    assert out_expected == out_actual
    assert err_expected == err_actual



# Generated at 2022-06-13 05:55:17.715827
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = MagicMock()
    env = "venv"
    chdir = "/tmp"
    out = ""
    err = ""
    return setup_virtualenv(module, env, chdir, out, err)


# Generated at 2022-06-13 05:55:18.610807
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleFailJson):
        main()



# Generated at 2022-06-13 05:55:20.441243
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:55:21.338788
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 05:55:27.836414
# Unit test for function setup_virtualenv

# Generated at 2022-06-13 05:55:40.527155
# Unit test for function main
def test_main():
    from ansible.modules.packaging import python
    from ansible.compat.tests import unittest

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught by the test case"""
        pass

    class AnsibleFailJson(Exception):
        """Exception class to be raised by module.fail_json and caught by the test case"""
        pass

    def exit_json(*args, **kwargs):
        """function to patch over exit_json; package return data into an exception"""
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        """function to patch over fail_json; package return data into an exception"""
        kwargs['failed']

# Generated at 2022-06-13 05:56:47.794173
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package("pip")
    assert not pkg.is_satisfied_by("1.2.0")
    assert not pkg.is_satisfied_by("1.2.1")
    assert pkg.is_satisfied_by("1.3.0")

    pkg = Package("pip==3.3.0")
    assert not pkg.is_satisfied_by("1.2.0")
    assert pkg.is_satisfied_by("3.3.0")
    assert not pkg.is_satisfied_by("1.3.0")

    pkg = Package("pip", ">=2.0")
    assert not pkg.is_satisfied_by("1.1.0")
    assert pkg.is_satisfied_

# Generated at 2022-06-13 05:56:55.703508
# Unit test for constructor of class Package
def test_Package():
    assert Package("setuptools", "3.3").package_name == "setuptools"
    assert Package("setuptools", "3.3").is_satisfied_by("3.3")

    assert Package("setuptools").package_name == "setuptools"
    assert str(Package("setuptools")) == "setuptools"

    assert Package("Django", "1.4.2").package_name == "django"
    assert Package("Django", "1.4.3").package_name == "django"
    assert str(Package("Django", "1.4.4")) == "Django==1.4.4"

    # latest django
    assert Package("Django").package_name == "django"

# Generated at 2022-06-13 05:56:56.509775
# Unit test for function main
def test_main():
    assert 1

# Generated at 2022-06-13 05:57:06.092415
# Unit test for function main

# Generated at 2022-06-13 05:57:12.855867
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.basic
    import ansible.modules.packaging.os.pip as pip

    args = {'name': ['pkg1'],
            'version': '1.0',
            'state': 'present',
            'requirements': None,
            'virtualenv': None,
            'chdir': '/tmp',
            'virtualenv_site_packages': False,
            'extra_args': None,
            'executable': None,
            'editable': False,
            'virtualenv_python': None,
            'virtualenv_command': 'virtualenv',
            '_ansible_check_mode': False,
            'umask': None,
            '_ansible_no_log': False}

# Generated at 2022-06-13 05:57:17.613877
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import pytest
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils import basic

    env = '/home/example/virtualenv'

    # Test when a command is given
    cmd = ['/bin/virtualenv']
    chdir = None

    # Test when it fails
    out = "The virtualenv command failed."
    err = ""
    try:
        out, err = setup_virtualenv(get_module_mock(cmd, out, err), env, chdir, out, err)
    except SystemExit as e:
        assert e.args[0] == '{"msg": "The virtualenv command failed.", "cmd": ["/bin/virtualenv", "/home/example/virtualenv"], "stdout": "The virtualenv command failed."}'

    # Test when we have

# Generated at 2022-06-13 05:57:30.916804
# Unit test for function main
def test_main():
    import unittest
    import requests
    import mock

    _pip_extra_args = """
fake_options:
  description:
    - These options are passed to the pip command
  required: false
  required_one_of: []
  suboptions:
    allow_external:
      description:
        - These options correspond to `--allow-external` and `--allow-insecure`
          from pip.
      required: false
    allow_unverified:
      description:
        - These options correspond to `--allow-external` and `--allow-insecure`
          from pip.
      required: false
"""

# Generated at 2022-06-13 05:57:39.570431
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pip_opts = {'chdir': '/tmp/virtualenv/', 'executable': '/tmp/bin/python', 'virtualenv_command': 'virtualenv', 'virtualenv_python': '/tmp/bin/python', 'virtualenv_site_packages': False}
    class AnsibleModule(object):
        def __init__(self, p_args):
            self.params = p_args
        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            # always returns executable
            return executable
        def run_command(self, cmd, cwd=None, environ_update=None):
            if self.params['virtualenv_command'] in cmd:
                return 0, 'virtualenv_command_output', ''
            else:
                return 0, 'virtualenv_output', ''

# Generated at 2022-06-13 05:57:48.405471
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass
    #m = basic_ansible_module()
    #m.params['virtualenv_command'] = 'virtualenv'
    #m.params['virtualenv_python'] = ''
    #m.params['virtualenv_site_packages'] = True
    #cmd, out, err = setup_virtualenv(m, '/tmp/venv1', '/tmp', '', '')
    #print(cmd, out, err)
    #cmd, out, err = setup_virtualenv(m, '/tmp/venv2', '/tmp', '', '')
    #print(cmd, out, err)
    #m.params['virtualenv_site_packages'] = False
    #cmd, out, err = setup_virtualenv(m, '/tmp/venv3', '/tmp', '', '')
    #print(cmd, out, err

# Generated at 2022-06-13 05:57:49.402251
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    import doctest
    doctest.testmod(Package, verbose=1)