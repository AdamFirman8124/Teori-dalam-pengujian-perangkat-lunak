

# Generated at 2022-06-13 05:49:39.212415
# Unit test for function main
def test_main():
    """Unit test for main()"""
    # Prepare test objects
    import json
    import tempfile
    import os
    import os.path
    import shutil
    import sys
    import time

    pip_log_dir = tempfile.mkdtemp()
    pip_log_file = os.path.join(pip_log_dir, "pip.log")

    venv_dir = tempfile.mkdtemp()
    test_fixture = tempfile.mkdtemp()

# Generated at 2022-06-13 05:49:48.907175
# Unit test for function main

# Generated at 2022-06-13 05:49:50.049083
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert setup_virtualenv() == 'FAILED'



# Generated at 2022-06-13 05:50:00.140974
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Assumed modules will have already been initialized
    # Imported here to avoid circular import issues.
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_virtualenv_command
    from ansible.module_utils.facts import ansible_virtualenv_python
    from ansible.module_utils.facts import ansible_virtualenv_site_packages

    module_args = dict(
        virtualenv_command=ansible_virtualenv_command,
        virtualenv_python=ansible_virtualenv_python,
        virtualenv_site_packages=ansible_virtualenv_site_packages
    )
    module = AnsibleModule(argument_spec=module_args)

    env = 'test_env'
    chdir = '~'

# Generated at 2022-06-13 05:50:02.559089
# Unit test for function main
def test_main():
    pip = _get_pip()
    cmd = pip + state_map[state]
    _run_command(cmd)


# Generated at 2022-06-13 05:50:11.131848
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    p = Package(name_string="foo")
    assert not p.is_satisfied_by("1.0.0")
    p = Package(name_string="foo==1.0.0")
    assert p.is_satisfied_by("1.0.0")
    assert not p.is_satisfied_by("1.0.1")
    p = Package(name_string="foo>1.0.0")
    assert p.is_satisfied_by("1.0.1")
    assert not p.is_satisfied_by("1.0.0")
    p = Package(name_string="foo<1.0.0")
    assert p.is_satisfied_by("0.9.9")

# Generated at 2022-06-13 05:50:15.909983
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.exit_json = lambda **kwargs: None
            self.fail_json = lambda *args, **kwargs: None

        def run_command(self, cmd, cwd=None, environ_update=None):
            rc, out, err = 0, '', ''
            if self.params['virtualenv_command'] == 'fail':
                rc = 1
                out = 'outerror'
                err = 'errorfail'
            return rc, out, err

        def get_bin_path(self, name, required, opt_dirs):
            return name

    params = dict(virtualenv_command='fail', virtualenv_site_packages=True,
                  virtualenv_python='python2.7')

# Generated at 2022-06-13 05:50:20.040609
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # test simple version
    pkg = Package("foo", "=0.1")
    assert pkg.is_satisfied_by("0.1") is True
    assert pkg.is_satisfied_by("0.2") is False

    # test complex version specifier
    pkg = Package("foo", ">=0.1,<0.3")
    assert pkg.is_satisfied_by("0.2") is True
    assert pkg.is_satisfied_by("0.4") is False

if __name__ == '__main__':
    test_Package_is_satisfied_by()

# Generated at 2022-06-13 05:50:27.556876
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pk = Package("setuptools")
    assert pk.is_satisfied_by("1.1.1")
    assert not pk.is_satisfied_by("1.1")
    assert pk.is_satisfied_by("1.2")
    assert pk.is_satisfied_by("1.3.1")
    assert not pk.is_satisfied_by("2.1")
    assert pk.is_satisfied_by("0.9.9")
    assert pk.is_satisfied_by("1.0.1")

    pk = Package("setuptools", ">=1.1,!=1.2,<2.0")
    assert pk.is_satisfied_by("1.1.1")

# Generated at 2022-06-13 05:50:37.846635
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Mock all required objects
    class Args(object):
        pass
    args = Args()
    args.check_mode = True
    args.virtualenv_command = "/usr/bin/virtualenv"
    args.virtualenv_site_packages = False
    args.virtualenv_python = False
    module = AnsibleModule(
        argument_spec={}
    )
    module.exit_json = Mock()
    out, err = setup_virtualenv(module, env=None, chdir=None, out=None, err=None)

    # Tests
    if out is not None:
        raise AssertionError("setup_virtualenv should return None in out")
    if err is not None:
        raise AssertionError("setup_virtualenv should return None in err")

# Generated at 2022-06-13 05:51:09.921930
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import json
    import sys
    import helpers
    # Dummy AnsibleModule object
    set_module_args = dict(
        virtualenv_command='/usr/bin/virtualenv',
        virtualenv_python='/opt/local/bin/python2.7',
        virtualenv_site_packages=True,
        name='ansible-test==1.1',
        state='present'
    )
    module = helpers.dummy_ansible_module(**set_module_args)
    module.get_bin_path = lambda x, y, z: x  # No-op

    # Create a dummy environment to create virtualenv
    venv_dir = tempfile.mkdtemp()
    module.params['virtualenv'] = venv_dir
    chdir = os.getcwd()

    # Test the function
   

# Generated at 2022-06-13 05:51:14.834497
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    from unittest import TestCase
    from distutils.version import LooseVersion

    class TestPackage(TestCase):

        def test_is_satisfied_by(self):
            self.assertTrue(Package('testpackage').is_satisfied_by('0.0.1'))
            self.assertTrue(Package('testpackage==0.0.1').is_satisfied_by('0.0.1'))
            self.assertTrue(Package('testpackage>=0.0.1').is_satisfied_by('0.0.1'))
            self.assertTrue(Package('testpackage>=0.0.1').is_satisfied_by('0.0.2'))

# Generated at 2022-06-13 05:51:16.878099
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:51:22.612449
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(
        argument_spec=dict(
            virtualenv_command=dict(default='/usr/local/bin/virtualenv'),
            virtualenv_python=dict(default=None),
            virtualenv_site_packages=dict(default=False)))
    env = "/tmp/test_temp_file"
    chdir = "/tmp"
    out = ""
    err = ""
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out == ""
    assert err == ""


# Generated at 2022-06-13 05:51:25.716054
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleFailJson) as exc:
        main()
    assert 'msg' in exc.value.args[0]

# unit tests for ansible.module_utils.common.command

# Generated at 2022-06-13 05:51:32.179610
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(
        argument_spec = dict(
            env = dict(default=None),
            virtualenv_command = dict(default=None)
        )
    )
    module.exit_json = exit_json
    res = setup_virtualenv(module, 'env', 'chdir', 'out', 'err')
    assert res == ('out', 'err')


# Generated at 2022-06-13 05:51:39.904530
# Unit test for function main
def test_main():
    test_params = {
        'state': 'present',
        'name': [ 'ansible'],
        'version': '2.8.12',
        'requirements': 'requirements.txt',
        'virtualenv': None,
        'virtualenv_site_packages': False,
        'virtualenv_command': '/usr/local/bin/virtualenv',
        'virtualenv_python': None,
        'extra_args': None,
        'editable': False,
        'chdir': None,
        'executable': None,
        'umask': None,
        'dest': None,
        'executable': None,
        'extra_args': None,
        'no_deps': False,
        'requirements': None,
        'state': 'present',
        'virtualenv': False
    }


# Generated at 2022-06-13 05:51:44.924880
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # covers is_satisfied_by when no version specifier exists
    assert Package('foo').is_satisfied_by('1.0')
    assert not Package('foo').is_satisfied_by('0.9')

    # covers is_satisfied_by when a version specifier exists
    assert Package('bar', '>=2.0.1').is_satisfied_by('2.1')
    assert not Package('bar', '>=2.0.1').is_satisfied_by('1.0')

    # covers is_satisfied_by with version specifier from a dependency
    assert Package('pippo', '>=2.0.1,!=2.2').is_satisfied_by('2.1')

# Generated at 2022-06-13 05:51:51.541059
# Unit test for constructor of class Package
def test_Package():
    assert Package("foo==1.0.0").package_name == "foo"
    assert Package("foo==1.0.0").has_version_specifier == True
    assert Package("foo==1.0.0").is_satisfied_by("1.0.0") == True

    assert Package("foo").package_name == "foo"
    assert Package("foo").has_version_specifier == False
    assert Package("foo").is_satisfied_by("1.0.0") == False



# Generated at 2022-06-13 05:51:54.796394
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    out = ''
    err = ''
    assert setup_virtualenv(module, env, chdir, out, err)



# Generated at 2022-06-13 05:52:38.899837
# Unit test for function main

# Generated at 2022-06-13 05:52:45.781627
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    class TestCase:
        def __init__(self, name, version_to_tes, expected_ret):
            self.name = name
            self.version_to_tes = version_to_tes
            self.expected_ret = expected_ret


# Generated at 2022-06-13 05:52:48.140995
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert setup_virtualenv(None, 'testenv/', '/', 'stdout', 'stderr')[0] == 'stdout'
    assert setup_virtualenv(None, 'testenv/', '/', 'stdout', 'stderr')[1] == 'stderr'


# Generated at 2022-06-13 05:52:54.282875
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec=(),
        supports_check_mode=True,
    )
    module.run_command = lambda args, **kwargs: (0, '', '')
    module.get_bin_path = lambda x, y, z,: '/usr/bin/virtualenv'
    module.params = dict(
        virtualenv_command='virtualenv',
        virtualenv_python='/usr/local/bin/python2.7',
        virtualenv_site_packages=False,
    )
    (out, err) = setup_virtualenv(
        module=module,
        env='/tmp/virtualenv',
        chdir='/tmp',
        out='',
        err='',
    )
    assert out == ''
    assert err == ''


# Generated at 2022-06-13 05:53:05.902444
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import os
    import tempfile
    import shutil

    module = AnsibleModule(argument_spec={
        # I know this is not a valid virtualenv command, but we don't care because
        # we are not executing the command, just mocking what that command would do
        'virtualenv_command': dict(default='/usr/bin/virtualenv', required=False),
        'virtualenv_site_packages': dict(default=False, required=False)
    })
    module.run_command = Mock()
    tmpdir = tempfile.mkdtemp()
    env = os.path.join(tmpdir, 'venv')
    cmd = ['/usr/bin/virtualenv', '-p', '/usr/bin/python2.7', env]
    # noinspection PyUnresolvedReferences
    module.run_command.return_value

# Generated at 2022-06-13 05:53:14.347346
# Unit test for function main
def test_main():
    # unit test needs to have access to protected members
    # pylint: disable=protected-access
    # if pip is not available, then skip the test
    if PIP_EXE is None:
        return

    now = datetime.utcnow().replace(microsecond=0)

    pip_list_command = '%s list --format=legacy' % PIP_EXE if PIP_EXE is not None else None

# Generated at 2022-06-13 05:53:17.348697
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert setup_virtualenv(module, env, chdir, out, err)


# Generated at 2022-06-13 05:53:27.385009
# Unit test for function main
def test_main():
    # Set args
    sys.argv = ['ansible-test',
        '-v',
        '--color=no',
        '--tb=short',
        'unit']

    # Construct preset args
    args = dict(
        requirements=None, state='present',
        name=['python'], version=None)

    # Set AnsibleModule params

# Generated at 2022-06-13 05:53:32.263280
# Unit test for function main
def test_main():
    from ansible.modules.packaging.os import pip
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    pip.main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:53:39.859180
# Unit test for function main

# Generated at 2022-06-13 05:54:24.661758
# Unit test for function main
def test_main():
    m = MagicMock(side_effect = AnsibleFailJson(msg = 'Error'))
    with patch.dict(ansible_module_pip.__dict__, {'AnsibleModule': m, 'HAS_SETUPTOOLS': False}):
        ansible_module_pip.main()
        assert m.call_count == 1

    # validate argument_spec

# Generated at 2022-06-13 05:54:33.349674
# Unit test for function main
def test_main():

    class FakeModule(object):
        def __init__(self, check_mode, params):
            self.check_mode = check_mode
            self.params = params

        def fail_json(self, *_args, **_kwargs):
            # for now, do nothing if fail_json is called.
            pass

        def exit_json(self, *_args, **kwargs):
            # for now, do nothing if exit_json is called.
            self.exit_json_args = kwargs

        def run_command(self, args, path_prefix=None, cwd=None):
            if path_prefix is None:
                path_prefix = '/tmp/venv/bin'
            # return code
            rc = 0
            # output
            out = ''
            # error
            err = ''
            pip_command

# Generated at 2022-06-13 05:54:36.593425
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(
        argument_spec=dict(
            virtualenv_command=dict(default='virtualenv'),
            virtualenv_site_packages=dict(default=False, type='bool')
        )
    )

    env = '/tmp/test_virtualenv'
    chdir = '/tmp/'
    out = "out"
    err = "err"

    res = setup_virtualenv(module, env, chdir, out, err)

    assert res[1] == ''



# Generated at 2022-06-13 05:54:48.783098
# Unit test for function main
def test_main():
    # AnsibleModule argument mocks
    state_map = dict(
        present=['install'],
        absent=['uninstall', '-y'],
        latest=['install', '-U'],
        forcereinstall=['install', '-U', '--force-reinstall'],
    )


# Generated at 2022-06-13 05:54:49.947056
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:54:58.096339
# Unit test for function main
def test_main():
    args = dict(
        state='present',
        name=['python-setuptools'],
        version='0.9.8',
        requirements='/path/to/requirements.txt',
        virtualenv='/path/to/venv/',
        virtualenv_site_packages=False,
        virtualenv_command='virtualenv',
        virtualenv_python='/usr/bin/python',
        extra_args='',
        editable=False,
        chdir='/path/to/working/directory/',
        executable='/path/to/executable/',
        umask=None
    )

    set_module_args(args)
    result = main()
    assert 'Executing pip with arguments' in result['cmd']

# Generated at 2022-06-13 05:55:00.334244
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({})
    env = '/tmp/test_setup_virtualenv'
    chdir = '/tmp'
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert '/tmp/test_setup_virtualenv/bin/python' in out
    assert not err


# Generated at 2022-06-13 05:55:03.969410
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 255
    assert exc_info.value.args == ([],)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:55:12.242213
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    p = Package('test_package_name', '==1.0')
    assert p.is_satisfied_by('1.0') is True
    assert p.is_satisfied_by('1.1') is False
    assert p.is_satisfied_by('0.9') is False
    assert p.is_satisfied_by('1.0a') is False
    assert p.is_satisfied_by('1.0rc1') is False
    assert p.is_satisfied_by('1.0.post1') is True
    assert p.is_satisfied_by('1.0.dev1') is False
    assert p.is_satisfied_by('1.0b15') is False
    assert p.is_satisfied_by('1.0c2')

# Generated at 2022-06-13 05:55:24.110901
# Unit test for function main
def test_main():
    with mock.patch('ansible_collections.ansible.builtin.plugins.modules.pip.main.AnsibleModule') as ansible_module:
        ansible_module.return_value = mock.Mock
        main()

# Generated at 2022-06-13 05:56:31.099507
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:56:37.333311
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    class test_args(object):
        def __init__(self, virtualenv_command, virtualenv_python, virtualenv_site_packages):
            self.virtualenv_command = virtualenv_command
            self.virtualenv_python = virtualenv_python
            self.virtualenv_site_packages = virtualenv_site_packages

    class test_module(object):
        def get_bin_path(self, cmd, required, opt_dirs):
            return cmd
        def run_command(self, cmd, cwd=None, environ_update=None, check_rc=False, binary_data=False, path_prefix=None):
            return 0, 'pip freeze', ''

# Generated at 2022-06-13 05:56:41.801958
# Unit test for function main
def test_main():
    os.environ['PYTHONPATH'] = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.dirname(__file__)
    sys.path.append(test_dir)
    template_dir = os.path.join(test_dir, 'templates')

# Generated at 2022-06-13 05:56:49.168234
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock(name="AnsibleModule")
    module._verbosity = 0
    module.params = dict(virtualenv_python='',
                         virtualenv_site_packages=False,
                         virtualenv_command='/usr/bin/virtualenv'
                         )
    module.run_command = Mock()
    module.run_command.retrun_value = 0, "", ""
    module.get_bin_path = Mock()
    module.get_bin_path.return_value = '/usr/bin/virtualenv'
    _get_cmd_options = Mock()
    _get_cmd_options.return_value = ['--system-site-packages', '--no-site-packages']
    module.check_mode = False
    env = "/tmp/ansible-venv"

    # test if virtualenv_command is venv

# Generated at 2022-06-13 05:56:49.986667
# Unit test for function main
def test_main():
    assert main() == True



# Generated at 2022-06-13 05:56:56.011695
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    class MyModule(object):
        def __init__(self, module_params, check_mode, name, virtualenv_python=None, virtualenv_command=None,
                     virtualenv_site_packages=True):
            self.name = name
            self.check_mode = check_mode
            self.run_command_called = False
            self.get_bin_path_called = False
            self.called_with_run_command = None
            self.called_with_get_bin_path = None
            self.run_command_args = None
            self.run_command_kwargs = None
            self.get_bin_path_args = None
            self.get_bin_path_kwargs = None
            self.params = module_params
            self.params['virtualenv_python'] = virtualenv_python
            self

# Generated at 2022-06-13 05:57:05.697408
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    # setup test environment
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.file import unfrackpath
    old_umask = None
    tempdir = tempfile.mkdtemp()
    mod_path = os.path.join(tempdir, 'ansible_module_pip')
    mod_file = open(mod_path, 'w')

# Generated at 2022-06-13 05:57:12.520526
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import ansible.module_utils.basic
    import sys
    # For Py3 we need the source data to be bytes
    if sys.version_info[0] == 3:
        # ansible.module_utils.basic._ANSIBLE_ARGS requires the module_utils entry
        # to be in a list.
        # for the sake of these tests, a fake setup_virtualenv.py is used
        # this is because we cannot import the module_utils.basic module
        # so the _ANSIBLE_ARGS cannot be defined automatically
        ansible_args = '{},{{}}'.format(os.path.join(os.path.dirname(__file__), 'setuptools.py')).encode()

# Generated at 2022-06-13 05:57:17.289641
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import os
    import sys
    import tempfile
    import uuid
    import shutil
    import unittest
    import difflib
    import subprocess
    import ansible.module_utils.basic
    env = "test_setup_virtualenv_" + str(uuid.uuid4())
    saved_cwd = os.getcwd()

# Generated at 2022-06-13 05:57:30.434139
# Unit test for method is_satisfied_by of class Package