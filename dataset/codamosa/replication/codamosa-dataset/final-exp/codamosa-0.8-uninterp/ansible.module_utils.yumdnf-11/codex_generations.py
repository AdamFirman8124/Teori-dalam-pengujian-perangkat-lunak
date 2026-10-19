

# Generated at 2022-06-13 04:41:39.732321
# Unit test for constructor of class YumDnf
def test_YumDnf():
    test_module = AnsibleModule(argument_spec={})
    obj = YumDnf(test_module)


# Generated at 2022-06-13 04:41:48.485558
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    def mock_is_lockfile_pid_valid(self):
        return True
    YumDnf.is_lockfile_pid_valid = mock_is_lockfile_pid_valid
    lockfile = tempfile.NamedTemporaryFile(delete=True)
    module = FakeAnsibleModule(
        argument_spec=yumdnf_argument_spec,
        lockfile=lockfile.name
    )
    yumdnf = YumDnf(module)
    yumdnf.run()
    yumdnf.is_lockfile_pid_valid = None



# Generated at 2022-06-13 04:41:50.433481
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    module = MockModule()
    yum = YumDnf(module)
    assert yum.listify_comma_sep_strings_in_list(["a,b,c", "d", "e", "f,g,h,"]) == ["a", "b", "c", "d", "e", "f", "g", "h"]



# Generated at 2022-06-13 04:41:57.746162
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule
    import sys

    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins


# Generated at 2022-06-13 04:42:08.099986
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.yumdnf_base import YumDnf
    yumdnf_test = YumDnf(None)
    assert yumdnf_test.listify_comma_sep_strings_in_list(["some_list"]) == ["some_list"]
    assert yumdnf_test.listify_comma_sep_strings_in_list(["some_list1,some_list2"]) == ["some_list1", "some_list2"]
    assert yumdnf_test.listify_comma_sep_strings_in_list(["some_list1, some_list2"]) == ["some_list1", "some_list2"]
    assert yumdnf_test.listify_comma_sep_strings_in_list

# Generated at 2022-06-13 04:42:18.524136
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    '''
    Test that the listify_comma_sep_strings_in_list method works as expected
    '''

    test_list = ['abcd', 'a,b,c,d', 'efgh,ijk', 'klmn,op,qr,stuv', 'wxyz', '', '%$#@^&*()', ',e', 's,', 's']

    class YumDnfTestClass(YumDnf):
        ''' class to be passed as argument to YumDnf_listify_comma_sep_strings_in_list '''
        def __init__(self, test_list):
            self.module = None
            self.test_list = test_list


# Generated at 2022-06-13 04:42:25.082606
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=yumdnf_argument_spec)
    names = ['sssd-common', 'sssd-client']
    module.params['name'] = names
    yum = YumDnf(module)
    assert yum.names == names


# Generated at 2022-06-13 04:42:31.630825
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    test_module = AnsibleModule(argument_spec={})
    test_YumDnf = YumDnf(test_module)
    test_YumDnf.lockfile = "/tmp/test_lockfile"
    test_YumDnf.lock_timeout = 5

    temp_fd, temp_path = tempfile.mkstemp()
    os.close(temp_fd)
    os.remove(temp_path)
    test_YumDnf.is_lockfile_pid_valid = mock.Mock(return_value=True)

    test_YumDnf.wait_for_lock()

    with open(test_YumDnf.lockfile, 'w'):
        pass
    test_YumDnf.is_lockfile_pid_valid = mock.Mock

# Generated at 2022-06-13 04:42:39.255277
# Unit test for constructor of class YumDnf
def test_YumDnf():
    '''
        Test YumDnf constructor
    '''
    import ansible.module_utils.yum
    import ansible.module_utils.dnf
    module_path = os.path.join(os.path.dirname(ansible.module_utils.yum.__file__),
                               'tests/unit/module_utils/test_yum.py')
    module = ansible.module_utils.yum.AnsibleModule(argument_spec={},
                                                    bypass_checks=True,
                                                    no_log=True,
                                                    check_invalid_arguments=False)

# Generated at 2022-06-13 04:42:41.772756
# Unit test for constructor of class YumDnf
def test_YumDnf():
    yum_module = YumDnf(module=None)
    assert yum_module is not None

# =============
# = Utilities =
# =============


# Generated at 2022-06-13 04:43:09.083720
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    """
    Test if is_lockfile_pid_valid() for different scenarios.

    Verify if the return value of is_lockfile_pid_valid is True if
    pid exists in /proc/ and False if it doesn't exist.
    """

    class FakeModule(object):
        def __init__(self):
            self.params = {'lock_timeout': 30}
            self.lockfile = '/var/run/yum.pid'

    # Test if pid exists in /proc/
    class FakePid(YumDnf):
        pkg_mgr_name = 'yum'

        def __init__(self):
            self.module = FakeModule()
            super(FakePid, self).__init__(self.module)

        def is_lockfile_pid_valid(self):
            return True

   

# Generated at 2022-06-13 04:43:18.022263
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    class FakeModule:
        def __init__(self):
            self.params = {'lock_timeout': 30}
            self.fail = self.fail_json = self.fail_exit = self.fail_message = self.exit_json = None
            self.called_fail_json = False

        def fail_json(self, *args, **kwargs):
            self.called_fail_json = True

        def exit_json(self, *args, **kwargs):
            pass

    class FakeYumDnf(YumDnf):
        def __init__(self):
            self.called_is_lockfile_pid_valid = False
            self.called_is_lockfile_present = False
            self.called_wait_for_lock = 0
            self.pkg_mgr_name = 'yum'

# Generated at 2022-06-13 04:43:26.011443
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    # TODO: Try to import and use proper testing modules after Ansible 2.9 will switch to Python 3 only
    yum_dnf = YumDnf(None)
    # Test with empty list
    test_list = []
    expected_list = []
    assert yum_dnf.listify_comma_sep_strings_in_list(test_list) == expected_list
    # Test with a single element list
    test_list = ['python']
    expected_list = ['python']
    assert yum_dnf.listify_comma_sep_strings_in_list(test_list) == expected_list
    # Test with a list with comma separated strings
    test_list = ['vsftpd, httpd', 'bind', 'docker, docker-ce']

# Generated at 2022-06-13 04:43:37.261380
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.fail_json = lambda msg, results: sys.exit(msg)

        def fail_json(self, msg, results):
            print(msg)
            raise Exception(msg)

    class FakeYumDnf(YumDnf):
        def __init__(self, module):
            super(FakeYumDnf, self).__init__(module=module)
            self.lockfile = '/tmp/fake-yum-dnf.lock'

        def is_lockfile_pid_valid(self):
            return True

        def run(self):
            pass

    # test wait for lock timeout
    with tempfile.NamedTemporaryFile() as temp:
        # create lock file
        temp.write

# Generated at 2022-06-13 04:43:45.546689
# Unit test for constructor of class YumDnf
def test_YumDnf():
    module = MockModule()
    yum = YumDnf(module)

    assert False == yum.allow_downgrade
    assert False == yum.autoremove
    assert False == yum.bugfix
    assert False == yum.cacheonly
    assert None == yum.conf_file
    assert None == yum.disable_excludes
    assert False == yum.disable_gpg_check
    assert [] == yum.disable_plugin
    assert [] == yum.disablerepo
    assert False == yum.download_only
    assert None == yum.download_dir
    assert [] == yum.enable_plugin
    assert [] == yum.enablerepo
    assert [] == yum.exclude
    assert '/' == yum.installroot
    assert True == yum.install_repoquery

# Generated at 2022-06-13 04:43:47.733461
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    ansible_module = AnsibleModule(yumdnf_argument_spec)
    test_ins = YumDnf(ansible_module)
    with pytest.raises(NotImplementedError):
        test_ins.run()


# Generated at 2022-06-13 04:43:57.836509
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.basic import AnsibleModule
    # Constructor
    # module_arguments = dict(allow_downgrade=True, autoremove=False, bugfix=True, cacheonly=True,
    #                         conf_file='conf_file', disable_excludes='disable_excludes',
    #                         disable_gpg_check=True, disable_plugin='plugin_name',
    #                         disablerepo='disablerepo', download_only=True, download_dir='download_dir',
    #                         enable_plugin='enable_plugin', enablerepo='enablerepo', exclude='exclude',
    #                         installroot='installroot', install_repoquery='install_repoquery',
    #                         install_weak_deps=True, list='list', name='name', releasever='releasever',
    #                        

# Generated at 2022-06-13 04:44:04.989595
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():

    # prepare mocks
    class MockModule(object):
        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

    # create YumDnf instance with lock timeout 10
    yd = YumDnf(MockModule())
    yd.lock_timeout = 10

    # prepare mocks
    class MockOs(object):
        def path_isfile(self, path):
            return True

    class MockGlob(object):
        def glob(self, pattern):
            return True

    class MockPid(object):
        def islockfilepidvalid(self):
            return True

    # override os, glob, is_lockfile_pid_valid
    yd.os = MockOs()
    yd.glob = MockGlob()
    yd.is_lockfile_pid

# Generated at 2022-06-13 04:44:15.126739
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    import os
    import shutil
    import tempfile
    import yum
    from ansible.module_utils import yum_base
    from ansible.module_utils.yum_base import YumDnf
    from ansible.module_utils._text import to_native

    current_dir = os.path.dirname(__file__)

    # Create a mocked module
    mock_module = yum_base.AnsibleModule(argument_spec=yumdnf_argument_spec)

    # Create a mock class for yum.YumBase()
    class MockYum(yum.YumBase):
        pass

    # Create a mock class for bundled ansible.module_utils.yum_base.YumDnf class

# Generated at 2022-06-13 04:44:19.797584
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class TestYumDnf(YumDnf):
        def is_lockfile_pid_valid(self):
            return True
    import ansible.module_utils.basic
    m = ansible.module_utils.basic.AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    y = TestYumDnf(m)
    assert y.is_lockfile_pid_valid()


# Generated at 2022-06-13 04:45:06.942461
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    class my_YumDnf(YumDnf):
        def __init__(self):
            self.lockfile = '/var/run/yum.pid'

        def is_lockfile_pid_valid(self):
            return True

    test_object = my_YumDnf()

    assert [] == test_object.listify_comma_sep_strings_in_list([])
    assert [] == test_object.listify_comma_sep_strings_in_list([""])
    assert ['a', 'b'] == test_object.listify_comma_sep_strings_in_list(['a, b'])
    assert ['a', 'b'] == test_object.listify_comma_sep_strings_in_list(['a, b'])

# Generated at 2022-06-13 04:45:12.073910
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    example_param = ['httpd', 'nginx', 'memcached']
    y = YumDnf(object())
    res = y.listify_comma_sep_strings_in_list(example_param)
    assert res == ['httpd', 'nginx', 'memcached']

    example_param = ['httpd,memcached']
    y = YumDnf(object())
    res = y.listify_comma_sep_strings_in_list(example_param)
    assert res == ['httpd', 'memcached']

    example_param = ['httpd,memcached, nginx', 'mysql']
    y = YumDnf(object())
    res = y.listify_comma_sep_strings_in_list(example_param)

# Generated at 2022-06-13 04:45:24.079387
# Unit test for constructor of class YumDnf
def test_YumDnf():

    import sys
    import unittest
    from ansible.module_utils.basic import AnsibleModule

    # Test Case 1 - update_cache param only

    test_values_1 = dict(
        state='present',
        update_cache=True,
    )
    module_1 = AnsibleModule(argument_spec=yumdnf_argument_spec, supports_check_mode=True)
    module_1.params.update(test_values_1)
    yumdnf_obj = YumDnf(module_1)
    assert yumdnf_obj.cacheonly == True
    assert yumdnf_obj.autoremove == False
    assert yumdnf_obj.state == 'present'
    assert yumdnf_obj.list == None

    # Test Case 2 - name param only

    test

# Generated at 2022-06-13 04:45:31.832822
# Unit test for constructor of class YumDnf
def test_YumDnf():

    module = None
    result = {
        "name": ["git", "yum"],
        "disablerepo": ['rhel-6-server-rpms', 'rhel-6-server-optional-rpms'],
        "enablerepo": ['redhat-swat*'],
        "exclude": ['python-rhsm', 'mingw32-nsis', 'mingw64-nsis'],
    }

    yum = YumDnf(module)

    for param in result.keys():
        assert getattr(yum, param, None) == result[param], 'Attribute not set correctly, check class constructor'



# Generated at 2022-06-13 04:45:45.850327
# Unit test for constructor of class YumDnf
def test_YumDnf():
    from ansible.module_utils.yumdnf_base import YumDnf
    # mocking ansible module for tests
    from ansible.module_utils.ansible_aos_yum import AnsibleModule
    module_mock = AnsibleModule(argument_spec={})

# Generated at 2022-06-13 04:45:54.491672
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.basic import AnsibleModule
    if PY2:
        import __builtin__ as builtins  # pylint: disable=import-error
    else:
        import builtins  # pylint: disable=import-error

    def has_exit(self):
        return True

    def exit_json(self, **kwargs):
        return kwargs

    def fail_json(self, **kwargs):
        raise AssertionError(kwargs)

    module = AnsibleModule(argument_spec=yumdnf_argument_spec)
    for attr in ('has_exit', 'exit_json', 'fail_json'):
        setattr(module, attr, locals()[attr])

    # my_obj will be

# Generated at 2022-06-13 04:46:04.004557
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    # mock yum lockfile (os.path.isfile is not mocked)
    yum_lockfile = "/var/run/yum.pid"
    open(yum_lockfile, 'a').close()

    # mock dnf lockfile (os.path.isfile is not mocked)
    dnf_lockfile = "/var/run/dnf.pid"
    open(dnf_lockfile, 'a').close()

    # mock is_lockfile_pid_valid method called from _is_lockfile_present
    def is_lockfile_pid_valid(self):
        return os.path.isfile(self.lockfile)

    class MockModule(object):
        params = {'lock_timeout': 2}
        fail_json = lambda x: x

    module = MockModule()

    # create a class

# Generated at 2022-06-13 04:46:15.343979
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    # Create a yum/dnf module instance and a fake lockfile pid
    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule(argument_spec={})
    test_module.params['lock_timeout'] = 30

    # create a temporary file for test purpose
    temp_file_fd, temp_file_name = tempfile.mkstemp()

    with os.fdopen(temp_file_fd, 'w') as temp_file:
        temp_file.write('1')

    test_module.fail_json = lambda x: x
    yumdnf_obj = YumDnf(test_module)
    yumdnf_obj.lockfile = temp_file_name

    is_lockfile_pid_valid = yumdnf_obj.is_lockfile_pid_

# Generated at 2022-06-13 04:46:24.771100
# Unit test for constructor of class YumDnf

# Generated at 2022-06-13 04:46:34.052362
# Unit test for constructor of class YumDnf
def test_YumDnf():
    # Arrange
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 04:47:26.897471
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    pass



# Generated at 2022-06-13 04:47:35.356344
# Unit test for constructor of class YumDnf
def test_YumDnf():
    import ansible_collections.community.general.plugins.module_utils.yumdnf as yumdnf
    import ansible.module_utils.six as six
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 04:47:43.507098
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    # Create instance of class YumDnf
    class_instance = YumDnf(None)
    # test for invalid pid values
    assert(not class_instance.is_lockfile_pid_valid(None))
    assert(not class_instance.is_lockfile_pid_valid("not-a-number"))
    assert(not class_instance.is_lockfile_pid_valid("-1"))

    # Test for valid pid values
    pid_to_test = str(os.getpid())
    assert(class_instance.is_lockfile_pid_valid(pid_to_test))

    # Create a lockfile with valid pid value
    (lock_handle, lock_file) = tempfile.mkstemp(dir='/var/run/')

# Generated at 2022-06-13 04:47:46.973895
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    module = None
    with pytest.raises(NotImplementedError):
        y = YumDnf(module)
        y.run()


# Generated at 2022-06-13 04:47:58.048921
# Unit test for method listify_comma_sep_strings_in_list of class YumDnf
def test_YumDnf_listify_comma_sep_strings_in_list():
    """ Unit test for YumDnf class """

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict())

    os_data = module.params.get('data', {})

    # Test positive case
    os_data['data'] = ["abc,def"]
    module.params.update(os_data)
    obj = YumDnf(module)
    result = obj.listify_comma_sep_strings_in_list(obj.module.params['data'])
    assert result == ["abc", "def"]

    # Test negative case
    os_data['data'] = ["abc,def", "ghi,jkl,mno", "pqr", "stu"]
    module.params.update(os_data)
    obj = Yum

# Generated at 2022-06-13 04:48:11.142681
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.community.general.plugins.modules.system.package.yum import Yum
    import ansible.module_utils.yum as yum_module_utils

    class FakeModule(AnsibleModule):
        def __init__(self):
            super(FakeModule, self).__init__(
                argument_spec={
                    'lock_timeout': dict(required=False, type='int', default=0)
                },
                supports_check_mode=False
            )


# Generated at 2022-06-13 04:48:12.341100
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    with pytest.raises(NotImplementedError):
        instance = YumDnf(module)
        instance.run()


# Generated at 2022-06-13 04:48:18.827545
# Unit test for method run of class YumDnf
def test_YumDnf_run():
    try:
        obj = YumDnf()
    except Exception as e:
        assert type(e) is NotImplementedError
    else:
        raise Exception("test_YumDnf_run did not raise NotImplementedError")


# Generated at 2022-06-13 04:48:30.333046
# Unit test for method run of class YumDnf
def test_YumDnf_run():
        import ansible.modules.packaging.os.yum as yum
        import ansible.modules.packaging.os.dnf as dnf

        yum.YumModule._get_version_info = lambda self: {'yum_binary': 'yum', 'version': '1.2.3'}
        yum.YumModule.autoremove_packages = lambda self: dict(changed=False)
        yum.YumModule.expire_cache = lambda self: dict(changed=False)
        yum.YumModule.install_packages = lambda self: dict(changed=False)
        yum.YumModule.remove_packages = lambda self: dict(changed=False)
        yum.YumModule.update_packages = lambda self: dict(changed=False)
        yum.YumModule.list

# Generated at 2022-06-13 04:48:38.004589
# Unit test for constructor of class YumDnf
def test_YumDnf():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.yumdnf.yumdnf import yumdnf_argument_spec

    argument_spec_dict = yumdnf_argument_spec['argument_spec']

    module_args = dict()

    # Required
    module_args['name'] = ['git']

    # Optional
    module_args['allow_downgrade'] = False
    module_args['autoremove'] = False
    module_args['bugfix'] = False
    module_args['cacheonly'] = False
    module_args['conf_file'] = None
    module_args['disable_excludes'] = None
    module_args['disable_gpg_check'] = False
    module_args['disable_plugin'] = []

# Generated at 2022-06-13 04:50:40.192702
# Unit test for constructor of class YumDnf
def test_YumDnf():
    pkg_mgr_name = 'YUM'


# Generated at 2022-06-13 04:50:50.181283
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    class mock_module(object):
        def __init__(self, **kwargs):
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)

        def fail_json(self, msg, results):
            raise Exception(msg)

    class mock_yumdnf(YumDnf):
        def __init__(self, module):
            super(mock_yumdnf, self).__init__(module)
            self.pkg_mgr_name = 'yum'

        def is_lockfile_pid_valid(self):
            return True

    # create a new lockfile and add it to directories
    _, mock_lockfile = tempfile.mkstemp()

    # Testing with a positive timeout
    # lockfile should be present
    assert os.path.isfile

# Generated at 2022-06-13 04:50:56.555126
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class StubYumDnf(YumDnf):

        def is_lockfile_pid_valid(self):
            return True

    stub_module = type('StubModule', (object,), {})
    stub_module.fail_json = lambda *args, **kwargs: args[0]
    stub_module.params = {'state': 'absent',
                          'name': 'vim'
                         }
    stub_yumdnf = StubYumDnf(stub_module)
    assert(stub_yumdnf.is_lockfile_pid_valid() is True)


# Generated at 2022-06-13 04:50:59.377591
# Unit test for constructor of class YumDnf
def test_YumDnf():
    module = MockModule()
    yumdnf = YumDnf(module)
    assert yumdnf


# Generated at 2022-06-13 04:51:09.894116
# Unit test for method is_lockfile_pid_valid of class YumDnf
def test_YumDnf_is_lockfile_pid_valid():
    class DummyModule:
        def __init__(self, **kwargs):
            self.params = kwargs

    # if lockfile does not exist, return False
    tmp_lockfile = tempfile.mktemp()
    if os.path.isfile(tmp_lockfile):
        os.remove(tmp_lockfile)
    yumdnf_obj = YumDnf(DummyModule(lockfile=tmp_lockfile))
    assert yumdnf_obj.is_lockfile_pid_valid() is None

    # if lockfile exists and pid is invalid, return None
    with open(tmp_lockfile, 'w') as f:
        f.write('9999999')
    assert yumdnf_obj.is_lockfile_pid_valid() is None
    os.remove(tmp_lockfile)



# Generated at 2022-06-13 04:51:19.235622
# Unit test for method wait_for_lock of class YumDnf
def test_YumDnf_wait_for_lock():
    import pytest
    from ansible.module_utils.basic import AnsibleModule

    # Passing valid PID in the lock_file
    class MyYumDnf(YumDnf):
        def is_lockfile_pid_valid(self):
            return True

    module = AnsibleModule(argument_spec=yumdnf_argument_spec)
    pytest.set_trace()
    yumdnf = MyYumDnf(module)
    pid = os.getpid()
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False, prefix='ansible-yum-lock') as lockfile:
        lockfile.write(to_native(pid))
        lockfile.flush()
        yumdnf.lockfile = lockfile.name
        # Passing positive value for lock_timeout