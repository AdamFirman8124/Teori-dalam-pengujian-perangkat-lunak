

# Generated at 2022-06-13 05:49:32.712199
# Unit test for constructor of class Package

# Generated at 2022-06-13 05:49:40.558723
# Unit test for function main
def test_main():
    print('Test main')
    args={"name": "cfscrape", "state": "present", "version": "2.0.2", "requirements": None, "virtualenv": None, "virtualenv_site_packages": False, "virtualenv_command": "virtualenv", "virtualenv_python": None, "virtualenv_runas": None, "extra_args": "", "editable": False, "chdir": None, "executable": None, "umask": None, "warnings": []}
    args=collections.namedtuple('args',args.keys())(*args.values())
    main(args)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:49:49.059952
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    if not PY3:
        ansible_module = AnsibleModule({})
        mock_module = Mock()
        mock_module.check_mode = True
        mock_module.params = {'virtualenv_command': 'python -m venv', 'virtualenv_site_packages': False}
        mock_module.get_bin_path.return_value = 'python'
        mock_module.run_command.return_value = (0, '', '')
        out, err = setup_virtualenv(mock_module, '/tmp/mocked_venv', '/tmp', '', '')
        assert not out and not err
        mock_module.run_command.assert_called_once_with(['python', '-m', 'venv', '/tmp/mocked_venv'], cwd='/tmp')



# Generated at 2022-06-13 05:49:59.717429
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import inspect
    import shutil
    import tempfile
    import time
    import locale

    locale.setlocale(locale.LC_ALL, 'C')

    class TestModule(object):
        def __init__(self, params, result):
            self.params = params
            self.result = result
            self.args = ''
            self.bin_path = {}
            self.run_command_rc = 0
            self.run_command_stdout = ''
            self.run_command_stderr = ''
            self.run_command_cwd = []

        def fail_json(self, **kwargs):
            self.result = kwargs
            self.result['failed'] = True


# Generated at 2022-06-13 05:50:00.527061
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert setup_virtualenv() == 'return_value'



# Generated at 2022-06-13 05:50:05.870194
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import string_types
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.pip import Virtualenv
    from io import StringIO
    import tempfile
    sio = StringIO()
    module = AnsibleModule(
        argument_spec=dict(
            virtualenv_command=dict(type="str", default="virtualenv"),
            virtualenv_site_packages=dict(type='bool', default=False),
            virtualenv_python=dict(type='str', default=None),
            chdir=dict(type='str', default=tempfile.gettempdir()),
        )
    )
    venv = Virtualenv(module)
    venv.setup()

# Generated at 2022-06-13 05:50:14.567127
# Unit test for constructor of class Package
def test_Package():
    assert Package('foo') is not None
    assert Package('foo', '1.0') is not None
    assert Package('foo==1.0') is not None
    assert Package('foo==1.0').has_version_specifier is True
    assert Package('foo>=1.0').has_version_specifier is True
    assert Package('foo<1.0').has_version_specifier is True
    assert Package('foo').has_version_specifier is False
    assert Package('foo', '1.0').has_version_specifier is True

    assert Package('foo').is_satisfied_by('1.0') is False
    assert Package('foo==1.0').is_satisfied_by('1.0') is True

# Generated at 2022-06-13 05:50:16.391454
# Unit test for function main
def test_main():
    """ unit testing for main function """
    main()


# Generated at 2022-06-13 05:50:23.092722
# Unit test for constructor of class Package
def test_Package():
    name_string = "setuptools"
    version_string = "===1.2.3"
    package = Package(name_string, version_string)
    assert package.package_name == "setuptools"
    # '===' (only one '=') was changed to '==' for Requirement.parse
    assert str(package) == "setuptools==1.2.3"



# Generated at 2022-06-13 05:50:35.255204
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({'virtualenv_command': 'echo', 'virtualenv_python': 'python3', 'virtualenv_site_packages': True}, check_invalid_arguments=False)
    if not PY3:
        module.fail_json(msg="Unit tests are supported only on Python3.")
    else:
        out, err = setup_virtualenv(module, "/tmp/test_venv", "/tmp", "", "")
        assert out == "--system-site-packages -ppython3 /tmp/test_venv"
        assert err == ""
    module = AnsibleModule({'virtualenv_command': 'echo', 'virtualenv_site_packages': True}, check_invalid_arguments=False)

# Generated at 2022-06-13 05:51:10.470288
# Unit test for function main
def test_main():
    from ansible_collections.ansible.community.tests.unit.compat import unittest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, MagicMock

    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        kwargs['failed'] = True
        raise AnsibleFailJson(kwargs)


# Generated at 2022-06-13 05:51:17.619080
# Unit test for constructor of class Package
def test_Package():
    # PEP 503: canonicalize_name function
    assert Package.canonicalize_name("foo-bar") == "foo-bar"
    assert Package.canonicalize_name("Foo-Bar") == "foo-bar"
    assert Package.canonicalize_name("foo_bar") == "foo-bar"
    assert Package.canonicalize_name("FOO.BAR") == "foo-bar"
    assert Package.canonicalize_name("foo....bar") == "foo-bar"

    # package name is the only input
    package = Package("foo_bar")
    assert package.package_name == "foo-bar"
    assert not package.has_version_specifier
    assert not package.is_satisfied_by("0.0.0")

# Generated at 2022-06-13 05:51:27.947819
# Unit test for function main

# Generated at 2022-06-13 05:51:37.738908
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # Case 1: invalid requirement (None)
    p = Package(None)
    assert not p.is_satisfied_by("1.0.0")

    # Case 2: requirement is not plain, version string is valid
    p = Package("foo>1.0.0")
    assert not p.is_satisfied_by("2.0.0")

    # Case 3: requirement is plain, version string is invalid
    p = Package("foo", "==1.0.0")
    assert not p.is_satisfied_by("invalid")

    # Case 4: requirement is plain, version string is valid and satisfy the requirement
    p = Package("setuptools", "==29.0.1")
    assert p.is_satisfied_by("29.0.1")

    # Case 5: requirement is plain,

# Generated at 2022-06-13 05:51:42.288825
# Unit test for constructor of class Package
def test_Package():
    # testing the canonicalize_name method
    assert Package.canonicalize_name("mypackage") == "mypackage"
    assert Package.canonicalize_name("my.package") == "my-package"
    assert Package.canonicalize_name("my_package") == "my-package"
    assert Package.canonicalize_name("mY_PACKAGE") == "mY-PACKAGE"
    assert Package.canonicalize_name("my-package") == "my-package"
    assert Package.canonicalize_name("MY--PACKAGE") == "MY-PACKAGE"

    # testing the init method
    pkg = Package("mypackage", "1.0")
    assert pkg.package_name == "mypackage"
    assert pkg.has_version_specifier == True

# Generated at 2022-06-13 05:51:54.278285
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    def _testsatisfy(package_name, package_version, version_to_test):
        pkg = Package('%s' % package_name, package_version)
        return pkg.is_satisfied_by(version_to_test)

    assert _testsatisfy('pkg1', '', '1.2')

    # one requirement
    assert not _testsatisfy('pkg2', '>4.5.6', '4.5.6')
    assert _testsatisfy('pkg3', '>4.5.6', '4.5.7')
    assert _testsatisfy('pkg4', '>4.5.6', '4.5.6a1')
    assert _testsatisfy('pkg5', '>4.5.6', '4.5.6.post1')

    assert not _tests

# Generated at 2022-06-13 05:52:05.741176
# Unit test for function main
def test_main():
    pass



# Generated at 2022-06-13 05:52:09.418211
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkg = Package('testpkg', '>= 1.4, < 1.5')
    assert pkg.is_satisfied_by('1.4.2') is True
    assert pkg.is_satisfied_by('1.4.0') is True
    assert pkg.is_satisfied_by('1.4.0-dev') is True
    assert pkg.is_satisfied_by('1.3.8') is False
    assert pkg.is_satisfied_by('1.5.0') is False
# END OF PIP CODE


# BEGIN OF PIP CODE
# Metadata of a package.
# TODO: Extract this class to a standalone module.

# Generated at 2022-06-13 05:52:20.945612
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """Tests the setup_virtualenv function.

    Tests the setup_virtualenv function by mocking the values and
    calling the function.
    """
    module = AnsibleModule({
        "executable": "/usr/bin/python3",
        "virtualenv": "test_env",
        "virtualenv_command": "virtualenv",
        "virtualenv_python": "python3.5",
        "virtualenv_site_packages": True
    }, check_invalid_arguments=False)
    env = "/tmp/test_env"
    chdir = "/tmp"
    ou = "Successfully installed virtualenv"
    er = ""
    out, err = setup_virtualenv(module, env, chdir, ou, er)
    assert(out == 'Successfully installed virtualenv')
    assert(err == '')




# Generated at 2022-06-13 05:52:27.216343
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule({
        'virtualenv_command': ['venv'],
        'virtualenv_python': 'python2.7'
    })
    env = 'virtualenv'
    out = ''
    err = ''
    try:
        setup_virtualenv(module, env, '', out, err)
    except Exception as e:
        pass



# Generated at 2022-06-13 05:53:21.041403
# Unit test for function main

# Generated at 2022-06-13 05:53:26.331426
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import os
    import tempfile
    import pytest

    # Setup a test environment directory
    test_dir = tempfile.mkdtemp()
    test_env = os.path.join(test_dir, 'test_env')
    test_virtualenv_cmd = 'virtualenv_command'
    test_venv_path = os.path.join(test_dir, 'test_venv')
    test_venv_python = 'python3.6'
    test_venv_with_python = os.path.join(test_dir, 'test_venv_python')
    test_venv_path_no_site_packages = os.path.join(test_dir, 'test_venv_no_site_packages')

# Generated at 2022-06-13 05:53:37.025013
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # Setup
    name_to_test = "some_package"
    version_to_test = "1.2.3"

    # Test 1
    package = Package(name_to_test, "==" + version_to_test)
    assert package.is_satisfied_by(version_to_test)

    # Test 2
    package = Package(name_to_test, "!=" + version_to_test)
    assert not package.is_satisfied_by(version_to_test)

    # Test 3
    package = Package(name_to_test, ">" + version_to_test)
    assert not package.is_satisfied_by(version_to_test)

    # Test 4
    package = Package(name_to_test, "<" + version_to_test)

# Generated at 2022-06-13 05:53:38.642728
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:53:49.912660
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    # Supported oprators in version specifier
    op_dict = {
        '==': operator.eq,
        '!=': operator.ne,
        '<=': operator.le,
        '>=': operator.ge,
        '<': operator.lt,
        '>': operator.gt,
    }


# Generated at 2022-06-13 05:53:57.126399
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec={
        'virtualenv_command': dict(required=True),
        'virtualenv_python': dict(),
        'virtualenv_site_packages': dict()
    })
    env = '/opt/virtualenv'
    module.params['virtualenv_command'] = (
        '/usr/bin/pyvenv --system-site-packages {0}'.format(env)
    )
    chdir = '/'
    out = ''
    err = ''

    out, err = setup_virtualenv(module, env, chdir, out, err)

    assert module._fail_json.call_count == 1
    assert os.path.isdir(env) is True



# Generated at 2022-06-13 05:54:01.769291
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock()
    env = "/root/tmp/venv"
    chdir = "/root"
    out = ''
    err = ''
    virtualenv_command = "conda create python=2 anaconda"
    module.params = {'virtualenv_command': virtualenv_command,
                     'virtualenv_python': 'python2.7'}
    out_venv, err_venv = setup_virtualenv(module, env, chdir, out, err)
    print(out_venv)
    print(err_venv)
    assert out_venv
    assert err_venv == ''



# Generated at 2022-06-13 05:54:02.306824
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    assert True

# Generated at 2022-06-13 05:54:13.965615
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    from tempfile import NamedTemporaryFile
    from ansible.module_utils.six import StringIO

    Case = namedtuple("Case", "name version_to_test result")

# Generated at 2022-06-13 05:54:24.198548
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:55:41.154816
# Unit test for function main
def test_main():
    args = dict(
        state='present',
        requirements=None,
        virtualenv=None,
        virtualenv_site_packages=False,
        virtualenv_command='python',
        extra_args='',
        editable=False,
        chdir=None,
        executable=None,
        umask=None,
        name=['pip'],
        version=None
    )

# Generated at 2022-06-13 05:55:46.739149
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(type='str', default='present', choices=['present', 'absent']),
            name=dict(type='list', elements='str'),
            version=dict(type='str'),
            requirements=dict(type='str'),
            virtualenv=dict(type='str'),
            extra_args=dict(type='str'),
            editable=dict(type='bool', default=False),
            chdir=dict(type='str'),
            executable=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    assert main() is None


# Generated at 2022-06-13 05:55:48.967283
# Unit test for function main
def test_main():
    assert main() is None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:55:59.525537
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    """
    add venv to the system path, and setup a virtualenv inside the venv folder
    :return:
    """
    import os
    import shutil
    import tempfile
    import unittest

    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils.six.moves.urllib.parse import urlparse
    from ansible.module_utils.six.moves.urllib.request import urlretrieve
    from ansible.modules.packaging.language import pip_utils
    from ansible.modules.packaging.language.venv import (
        _setup_virtualenv
    )


# Generated at 2022-06-13 05:56:10.237516
# Unit test for method is_satisfied_by of class Package

# Generated at 2022-06-13 05:56:21.982022
# Unit test for function main
def test_main():
    # Test normal operation with module_utils.basic._ANSIBLE_ARGS not set
    import module_utils.basic
    try:
        if "_ANSIBLE_ARGS" in module_utils.basic.__dict__:
            del module_utils.basic._ANSIBLE_ARGS
        main()
    except SystemExit:
        assert False, 'main() failed with _ANSIBLE_ARGS not set'

    # Test normal operation with module_utils.basic._ANSIBLE_ARGS set
    module_utils.basic._ANSIBLE_ARGS = dict(
        ansible_facts_prefix='prefix.',
        ansible_facts_dict={
            'newfacts': 'newfactsdict'
        }
    )

# Generated at 2022-06-13 05:56:30.728345
# Unit test for method is_satisfied_by of class Package
def test_Package_is_satisfied_by():
    pkgs = [
        Package(name_string="setuptools"),
        Package(name_string="zope.interface", version_string="4.3.3"),
        Package(name_string="Jinja2>=2.7"),
        Package(name_string="jinja2>=2.7"),
        Package(name_string="numpy==1.10.4"),
    ]
    version_to_test = "4.3.3"
    for pkg in pkgs:
        assert pkg.is_satisfied_by(version_to_test)


# Generated at 2022-06-13 05:56:37.077652
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    # Test is passed a module with a standard module interface.
    # It will call module.fail_json and module.exit_json instead
    # of using return values.  The rest of the function returns
    # nothing but is expected to set the module.params[]
    # dictionary.  It also needs to set module.params['virtualenv_command']
    # to match the method being tested.
    def _test_setup_virtualenv_venv(out, err):
        assert 'Using base prefix' in out or 'No such file or directory' in err
        assert 'Traceback' not in err
        assert '-p' not in ' '.join(cmd)

    def _test_setup_virtualenv_pyvenv(out, err):
        assert 'Using base prefix' in out or 'No such file or directory' in err

# Generated at 2022-06-13 05:56:47.624426
# Unit test for function main
def test_main():
    testcase = dict(
        state=dict(type='str', default='present', choices=['present', 'absent', 'latest', 'forcereinstall']),
        name=dict(type='list', elements='str'),
        version=dict(type='str'),
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
    )


# Generated at 2022-06-13 05:56:49.008425
# Unit test for function main
def test_main():
    _test_main(None, None, None, None)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:58:10.901197
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = Mock()
    env = 'test_env'
    chdir = 'test_path'
    out = 'test_out'
    err = 'test_err'
    _setup_virtualenv(module, env, chdir, out, err)
    module.fail_json.assert_called_with(msg=('virtualenv_python should not be used when'
                                             ' using the venv module or pyvenv as virtualenv_command'))



# Generated at 2022-06-13 05:58:21.044007
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    args = dict(
        virtualenv_command='virtualenv',
        virtualenv_site_packages=False,
        virtualenv_python=""
    )
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.basic import AnsibleModule
    out_venv = "virtualenv_output"
    err_venv = "virtualenv_error"
    env = "env_location"
    chdir = "path/to/dir"
    rc = 0
    instance = AnsibleModule(argument_spec=args, supports_check_mode=True)

    m = mock.mock_open()
    with mock.patch('ansible.module_utils.pip.open', m, create=True):
        m

# Generated at 2022-06-13 05:58:28.823627
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    import os
    os.environ['ANSIBLE_PYTHON_INTERPRETER'] = "python3.4"
    if sys.version_info >= (3,):
        os.environ['VIRTUAL_ENV'] = "/tmp/venv34"
        os.environ['PATH'] = "/tmp/venv34/bin:" + os.environ['PATH']
    else:
        os.environ['VIRTUAL_ENV'] = "/tmp/venv27"
        os.environ['PATH'] = "/tmp/venv27/bin:" + os.environ['PATH']
    cmd = "virtualenv"
    env = "/tmp/venv"

# Generated at 2022-06-13 05:58:34.933480
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec={'virtualenv_command': dict(type='str', required=True)})
    module.params['virtualenv_command'] = 'pyvenv'
    env = '/tmp/toto'
    chdir = '/tmp/'
    out = b''
    err = b''


    out, err = setup_virtualenv(module, env, chdir, out, err)
    assert out == err


# Generated at 2022-06-13 05:58:40.827863
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    module = AnsibleModule(argument_spec={'virtualenv_command': dict(required=True),
                                          'virtualenv_python':dict(required=False),
                                          'virtualenv_site_packages':dict(required=False)},
                           supports_check_mode=True)
    env = '/tmp/venv/venv1'
    chdir = '/tmp/venv/venv1'
    out = ''
    err = ''
    out, err = setup_virtualenv(module, env,  chdir, out, err)
    assert out
    assert err



# Generated at 2022-06-13 05:58:41.321147
# Unit test for function setup_virtualenv
def test_setup_virtualenv():
    pass

# Generated at 2022-06-13 05:58:51.505458
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.virtualenv import _get_package_info, _is_present, _fail, _get_cmd_options
    from ansible.module_utils.virtualenv import _get_cmd_version, _get_packages
    from ansible.module_utils.virtualenv import _get_pip, _is_vcs_url, _recover_package_name
    from ansible.module_utils.virtualenv import setup_virtualenv, Package
    #####################
    # Test _get_package_info
    #####################
    args = dict(module=None,
                name="boo",
                virtualenv="/root/test"
               )
    assert _get_package_info(args) is None


# Generated at 2022-06-13 05:59:03.023998
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, env_fallback
    from ansible.module_utils.six import PY2, PY3

    # Pre-load AnsibleModule for side-effect of setting up the basic_module fixture
    if PY2:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            AnsibleModule([])
            assert len(w) == 0
    else:
        AnsibleModule([])

    # noinspection PyUnresolvedReferences