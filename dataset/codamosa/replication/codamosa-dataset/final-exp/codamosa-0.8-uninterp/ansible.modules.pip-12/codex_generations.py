

# Generated at 2022-06-13 05:49:40.574653
# Unit test for function main
def test_main():
    import platform
    args = dict(
            state='present',
            name=['ansible'],
            version=None,
            requirements=None,
            virtualenv=None,
            virtualenv_site_packages=False,
            virtualenv_command='virtualenv',
            virtualenv_python=None,
            editable=False,
            chdir=tempfile.gettempdir(),
            executable=None,
            umask=None)
    if platform.system() == 'Windows':
        args['executable'] = 'C:\\Python27\\python.exe'
    mod = AnsibleModule(argument_spec=args)
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:49:42.704895
# Unit test for function main
def test_main():
    ''' Unit test for function main '''
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:49:50.794917
# Unit test for function main
def test_main():
    import sys
    import tempfile
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins


# Generated at 2022-06-13 05:50:00.223014
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:50:09.498688
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # testing satisfied case
    assert Package('package', '>= 1.2.3').is_satisfied_by(LooseVersion('1.3.3')) is True
    assert Package('package', '<= 1.2.3').is_satisfied_by(LooseVersion('1.2.0')) is True
    assert Package('package', '== 1.2.3').is_satisfied_by(LooseVersion('1.2.3')) is True
    assert Package('package', '!= 1.2.3').is_satisfied_by(LooseVersion('1.3.3')) is True
    # testing unsatisfied case
    assert Package('package', '>= 1.2.3').is_satisfied_by(LooseVersion('1.2.3')) is False

# Generated at 2022-06-13 05:50:14.219721
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """
    Unit test for function setup_virtualenv
    """
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec={'virtualenv_command': dict(type='str'), 'virtualenv_site_packages': dict(type='bool')},
        supports_check_mode=True)
    mock_module = mock.MagicMock()
    mock_module.params = module.params
    mock_module.run_command = module.run_command
    mock_module.get_bin_path = module.get_bin_path
    mock_module.check_mode = module.check_mode
    setup_virtualenv(mock_module, 'test_env', 'test_chdir', 'test_out', 'test_err')


# Generated at 2022-06-13 05:50:14.941469
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert(os.path.exists('/tmp/venv'))



# Generated at 2022-06-13 05:50:25.096257
# Unit test for constructor of class Package
def test_Package():
    p = Package('Package')
    assert p.package_name == 'package'
    assert p.has_version_specifier == False
    p = Package('MyPackage', '1.2.9')
    assert p.package_name == 'mypackage'
    assert p.has_version_specifier == True
    p = Package('MyPaCkAgE', '>=1.2.9,!=1.3.0,<1.4')
    assert p.package_name == 'mypackage'
    assert p.has_version_specifier == True
    assert p.is_satisfied_by('1.2.9')
    assert p.is_satisfied_by('1.3.5')
    assert not p.is_satisfied_by('1.3.0')

# Generated at 2022-06-13 05:50:25.759532
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:50:26.369263
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:51:00.772838
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    p = Package('mock==1.0.1')
    assert p.is_satisfied_by('1.0.1')
    assert not p.is_satisfied_by('1.0.1.1')
    assert not p.is_satisfied_by('1.0.2')

    p = Package('mock>=1.0.1,<=1.0.2')
    assert p.is_satisfied_by('1.0.1')
    assert p.is_satisfied_by('1.0.1.1')
    assert not p.is_satisfied_by('1.0.2')
    assert p.is_satisfied_by('1.0.2.1')

    p = Package('mock>=1.0.1,<2')

# Generated at 2022-06-13 05:51:08.512652
# Unit test for function main

# Generated at 2022-06-13 05:51:09.142681
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:51:09.589142
# Unit test for function main
def test_main():
    assert test_main()

# Generated at 2022-06-13 05:51:16.046465
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    cmd = ['/usr/bin/pyvenv', '/home/ubuntu/virtualenvs/my_env']
    out = 'Stuff'
    err = ''
    rc = 0
    chdir = 'home/ubuntu/'
    module = MagicMock()
    # If param virtualenv is used, then no option should be added
    out_venv, err_venv = setup_virtualenv(module, '/home/ubuntu/virtualenvs/my_env', chdir, out, err)
    assert out_venv is None
    assert err_venv is None



# Generated at 2022-06-13 05:51:23.883068
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import json
    import tempfile

    test_params = {'state': 'present', 'virtualenv_command': '/usr/bin/pyvenv',
                   'name': 'virtualenv-test', 'virtualenv': '/tmp/virtualenv-test',
                   'env': '/tmp/virtualenv-test'}

    if not os.path.exists('/tmp/virtualenv-test'):
        os.mkdir('/tmp/virtualenv-test')

    test_mod = AnsibleModule(argument_spec=dict(**test_params))
    test_mod.run_command = lambda cmd, **kwargs: (0, '', '')
    test_mod.get_bin_path = lambda cmd, required, **kwargs: '/usr/bin/pyvenv'

# Generated at 2022-06-13 05:51:35.437676
# Unit test for function main
def test_main():
    input_args={u'state': u'present', u'name': [u'git'], u'virtualenv_python': None, u'editable': False, u'virtualenv': None, u'requirements': None, u'virtualenv_command': u'virtualenv', u'virtualenv_site_packages': False, u'extra_args': '', u'chdir': None, u'executable': None, u'umask': None, u'_ansible_check_mode': False, u'_ansible_verbosity': 0, u'_ansible_debug': False, u'_ansible_version': u'2.9.9', u'_ansible_module_name': u'pip'}
    module = Mock(params=input_args)

    main()
    module.fail_json.assert_called_

# Generated at 2022-06-13 05:51:46.911506
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """
    Function tests
    setup_virtualenv(module, env, chdir, out, err)
    by comparing mock input and output
    """
    module = type('Module', (), {'params': {}, 'run_command': None})
    module.params['virtualenv_command'] = 'pyvenv'
    module.params['virtualenv_site_packages'] = False
    module.params['virtualenv_python'] = ''
    env = 'env'
    chdir = '/path/to/foo'
    out = ''
    err = ''
    check_out = ''
    check_err = ''
    check_out, check_err = setup_virtualenv(module, env, chdir, out, err)
    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out == check

# Generated at 2022-06-13 05:51:56.498308
# Unit test for function main
def test_main():
    import sys
    import os
    import re
    from unittest.mock import Mock, patch
    sys.modules['ansible'] = Mock()
    sys.modules['ansible.module_utils.six'] = Mock()
    sys.modules['ansible.module_utils.six.moves'] = Mock()
    sys.modules['pkg_resources'] = Mock()
    os.environ["PYTHONPATH"] = '/python3'
    module = Mock()

# Generated at 2022-06-13 05:52:08.466986
# Unit test for function main
def test_main():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    def mock_get_pip(module, env, executable=None):
        return "pip"

    def mock_setup_virtualenv(module, env, chdir, out, err):
        return out, err

    def mock_run_command(module, cmd, path_prefix=None, cwd=None):
        return 0, "", ""

    def mock_get_packages(module, pip, chdir):
        return "", "", ""

    def mock_is_present(module, package, pkg_list, pkg_cmd):
        return package


# Generated at 2022-06-13 05:52:53.523932
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """
    Unit test for function setup_virtualenv
    """
    import re
    import subprocess
    import json
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    # Create a virtual environment
    cmd = ['virtualenv','/tmp/venv']
    rc, out_venv, err_venv = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if rc != 0:
        print("FAILED: %s" % (out_venv))
        assert False

    # Create AnsibleModule

# Generated at 2022-06-13 05:53:00.241806
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    mock_run_command_success = MagicMock(return_value=(0, '', ''))
    module = MagicMock(check_mode=False, params={'virtualenv_command': 'virtualenv', 'virtualenv_python': None})
    module.run_command = mock_run_command_success
    _ = setup_virtualenv(module, 'env', 'chdir', '', '')



# Generated at 2022-06-13 05:53:09.192858
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from io import StringIO
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command=dict(type='str', required=False),
        virtualenv_site_packages=dict(type='bool', required=False),
        virtualenv_python=dict(type='str', required=False),
    ))
    env = "/tmp/unittest_venv"
    chdir = "/tmp"
    out = StringIO()
    err = StringIO()
    setup_virtualenv(module, env, chdir, out, err)
    assert(os.path.isdir(env))
    shutil.rmtree(env)



# Generated at 2022-06-13 05:53:10.581413
# Unit test for function main
def test_main():
    print("main called")


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:53:12.518630
# Unit test for function main
def test_main():
    # TODO
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:53:19.860852
# Unit test for function main
def test_main():
    try:
        import unittest.mock
    except ImportError:
        import mock
    from ansible.module_utils import basic

    MockedModule = mock.Mock()

    real_exit_json = basic.AnsibleModule.exit_json
    real_fail_json = basic.AnsibleModule.fail_json
    exit_json = Mock(wraps=real_exit_json)
    fail_json = Mock(wraps=real_fail_json)

    #mocked_module = MockedModule()
    mocked_module = mock.Mock()

# Generated at 2022-06-13 05:53:25.292854
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='list', elements='str'),
        requirements=dict(type='str'),
        virtualenv=dict(type='path'),
        virtualenv_site_packages=dict(type='bool', default=False),
        virtualenv_command=dict(type='path', default='virtualenv'),
        virtualenv_python=dict(type='str'),
        extra_args=dict(type='str'),
        editable=dict(type='bool', default=False),
        chdir=dict(type='path'),
        executable=dict(type='path'),
        umask=dict(type='str'),
    ))

    module.params['name'] = ['test_test_test']
    module.params['state'] = 'present'
    # module.params['name'] = ['

# Generated at 2022-06-13 05:53:36.344982
# Unit test for function main
def test_main():
    global HAS_SETUPTOOLS
    HAS_SETUPTOOLS = True

# Generated at 2022-06-13 05:53:42.140173
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec=dict(
        virtualenv_command=dict(default='virtualenv', type='str'),
        virtualenv_python=dict(),
        virtualenv_site_packages=dict(default=True, type='bool'),
    ))

    env = '/nowhere/test/env'
    chdir = '/nowhere/test'
    out = ''
    err = ''

    out_setup, err_setup = setup_virtualenv(module, env, chdir, out, err)

    assert out_setup == '/bin/sh -c virtualenv /nowhere/test/env\n'
    assert err_setup == ''

    # Now test with a non-standard command

# Generated at 2022-06-13 05:53:53.341513
# Unit test for function main

# Generated at 2022-06-13 05:54:49.666649
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({
        'virtualenv_command': 'virtualenv',
        'virtualenv_python': 'python2.7',
        'virtualenv_site_packages': False,
        'virtualenv_options': '',
        'chdir': '/tmp',
        'env': '/tmp/ansible-venv',
        'state': 'latest'})
    out, err = setup_virtualenv(module, '/tmp/ansible-venv', '/tmp', '', '')
    assert len(out) > 0
    assert len(err) == 0
test_setup_virtualenv()



# Generated at 2022-06-13 05:54:58.397757
# Unit test for function main
def test_main():
    # Run the main function with the predefined input and output
    # The following code is copied from the source code.
    test_params = {
        u'name': 'test',
        u'state': 'present',
        u'virtualenv': 'test',
        u'virtualenv_site_packages': False,
        u'virtualenv_command': 'virtualenv',
        u'virtualenv_python': u'',
        u'extra_args': '',
        u'editable': False,
        u'chdir': '',
        u'executable': '',
        u'umask': ''
    }
    # Set the instance, module, and assert all the results are True

# Generated at 2022-06-13 05:55:03.320203
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(
        argument_spec=dict(
            virtualenv_command=dict(required=False, default='virtualenv', type='str'),
        ),
        supports_check_mode=True
    )

    out, err = setup_virtualenv(module, 'test', '.', "", "")
    # Should not crash



# Generated at 2022-06-13 05:55:03.695932
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass



# Generated at 2022-06-13 05:55:09.276035
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package("pytest")
    assert pkg.package_name == "pytest"
    assert not pkg.has_version_specifier
    assert not pkg.is_satisfied_by("1.0.1")

    pkg = Package("pytest", ">=2.8.0")
    assert not pkg.is_satisfied_by("1.0.1")
    assert pkg.is_satisfied_by("2.9.0")
    assert pkg.is_satisfied_by("2.8.0")
    assert not pkg.is_satisfied_by("2.8")

    pkg = Package("pytest", ">=2.8.0,<3.0.0")

# Generated at 2022-06-13 05:55:13.740150
# Unit test for function main
def test_main():
    with patch.object(sys, 'version_info', (2, 7)):
        with patch.object(requests, 'get', return_value=Mock(
            status_code=200,
            json=lambda: {},
            text=''
        )):
            with patch.object(pip, 'main', return_value=0):
                try:
                    main()
                except SystemExit:
                    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:55:25.103138
# Unit test for function main
def test_main():
    mock_module = MagicMock()
    mock_module.params = {'name': ['python-pip'], 'virtualenv': '/tmp/pyenv', 'version': '9.0.1'}
    main(mock_module)
    # 2nd run hits cache.
    main(mock_module)
    mock_module.params = {'name': ['python-pip'], 'virtualenv': '/tmp/pyenv', 'state': 'absent'}
    main(mock_module)
    # 2nd run hits cache.
    main(mock_module)

# Generated at 2022-06-13 05:55:25.875163
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert True


# Generated at 2022-06-13 05:55:38.684708
# Unit test for function main
def test_main():
    # check that the function works with a virtualenv
    with tempfile.TemporaryDirectory() as venv:
        with open(os.path.join(venv, 'test_file'), 'a') as f:
            f.write('')
        try:
            out, err = setup_virtualenv(
                module=dict(params=dict(virtualenv=venv, virtualenv_command='mkdir')),
                chdir=venv,
                env=venv,
                out='',
                err='',
            )
        except SystemExit:
            pass
        else:
            assert False, 'Expected SystemExit exception'

        with open(os.path.join(venv, 'test_file'), 'r') as f:
            assert f.read() == '', 'Expected empty file'

    # check that the function

# Generated at 2022-06-13 05:55:42.259145
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = FakeAnsibleModule()
    # not an existing virtualenv
    out, err = setup_virtualenv(module=module, env='/tmp/venv', chdir='/tmp', out='', err='')
    assert err == ""
    assert out != ""


# Generated at 2022-06-13 05:57:13.154452
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec = dict(virtualenv_command=dict(type='str', required=True),
                                                virtualenv_python=dict(type='str', required=False),
                                                virtualenv_site_packages=dict(type='bool', required=False),
                                                env=dict(type='str', required=True),
                                                chdir=dict(type='str', required=True),
                                                out=dict(type='str', required=True),
                                                err=dict(type='str', required=True)))
    out, err = setup_virtualenv(module,
        module.params['env'],
        module.params['chdir'],
        module.params['out'],
        module.params['err'])


# Generated at 2022-06-13 05:57:23.689189
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    expected = ("Created virtual environment in .tox/py27-ansible-2.1.1./bin/python\nInstalling setuptools, pip...done.\n", '')
    module = MagicMock()
    out = ''
    err = ''
    module.check_mode = False
    module.params = {'virtualenv_command': 'tox -e py27-ansible-2.1.1 --notest', 'virtualenv_python': '', 'virtualenv_site_packages': False}
    env = '.tox/py27-ansible-2.1.1'
    chdir = '/Users/jsmith/Projects/myproject'

    actual = setup_virtualenv(module, env, chdir, out, err)

    assert actual == expected


# Generated at 2022-06-13 05:57:33.405500
# Unit test for function main

# Generated at 2022-06-13 05:57:39.445036
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec={
        'virtualenv_command': dict(type='str', default='virtualenv'),
        'virtualenv_python': dict(type='str', default=None),
        'virtualenv_site_packages': dict(type='bool', default=False),
    }, check_invalid_arguments=False)
    set_module_args(dict(name="foobar", virtualenv_command="foobar"))
    result = setup_virtualenv(module, env=None, chdir="/", out="", err="")
    assert result == ("", "")



# Generated at 2022-06-13 05:57:48.405991
# Unit test for function main
def test_main():
    import pytest
    # pytestmark = pytest.mark.skipif(not HAS_SETUPTOOLS, reason=SETUPTOOLS_IMP_ERR)
    pytest.importorskip("virtualenv")
    pytest.importorskip("setuptools")

    def _mock_run_command(module, cmd, check_rc=True, path_prefix=None, cwd=None, **kwargs):
        """
        Mock function for running commands
        :param module:
        :param cmd:
        :param check_rc:
        :param path_prefix:
        :param cwd:
        :param kwargs:
        :return:
        """

# Generated at 2022-06-13 05:57:53.847747
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import mock
    import os
    import tempfile

    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.six import StringIO

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import EnvironmentDict
    from ansible.module_utils.basic import get_exception

    class TestAnsibleModule(AnsibleModule):
        def __init__(self, **kwargs):
            super(TestAnsibleModule, self).__init__(**kwargs)
            self._environment = EnvironmentDict(os.environ)
            self.exit_json = mock.MagicMock(spec_set=True)
            self.fail_json = mock.MagicMock(spec_set=True)

# Generated at 2022-06-13 05:57:57.742977
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # must supply the valid parameters to test this function
    from ansible.module_utils.basic import *
    module_args = {
        "virtualenv_command": "pyvenv",
        "virtualenv_site_packages": "False",
        "virtualenv_python": None,
    }
    mod_obj = AnsibleModule(argument_spec=module_args)
    setup_virtualenv(mod_obj, "virtualenv", "chdir", "out", "err")
    assert True



# Generated at 2022-06-13 05:58:02.518873
# Unit test for function main
def test_main():
    '''Unit test for function main'''
    print("Function main :")
    # AnsibleModule argument_spec
    state = 'present'
    name = ['ansible']
    version = None
    requirements = None
    virtualenv = None
    virtualenv_site_packages = False
    virtualenv_command = 'virtualenv'
    virtualenv_python = None
    extra_args = None
    editable = False
    chdir = None
    executable = None
    umask = None


# Generated at 2022-06-13 05:58:11.435912
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule()
    virtualenv_command = 'pyvenv'
    virtualenv_python = '/usr/local/bin/python'
    env = '/usr/local/env'
    chdir = '/usr/local'
    out = ''
    err = ''

    results = setup_virtualenv(module, env, chdir, out, err)
    assert ("Creating virtualenv" in results[0] or "Using base prefix" in results[0]) and results[1] == '' and results[2] == ''

# Generated at 2022-06-13 05:58:21.128508
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    py_code = """
import sys
print(sys.executable)
"""
    M = AnsibleModule(dict(check_mode=False, virtualenv_command='/usr/bin/virtualenv',
                           virtualenv_site_packages=False, virtualenv_python='/usr/bin/python3'))
    M.run_command = lambda cmd, cwd: (0, '', '')
    M.get_bin_path = lambda command, warn_on_none=False, opt_dirs=[] : command + '3'
    venv_path = '/tmp/testing_virtualenv'
    out, err = setup_virtualenv(M, venv_path, '/tmp/', '', '')
    M.run_command = Mocker()